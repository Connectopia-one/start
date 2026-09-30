# -*- coding: utf-8 -*-
"""De leerbundels voor geschiedenis op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche geschiedenis 2de graad doorstroomfinaliteit, geldig
vanaf 1 januari 2027. Die ene fiche geldt voor alle doorstroomrichtingen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/geschiedenis.json`
doet daar het voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie. Dat is nodig en niet alleen netjes: ✨ Spark heeft een hoofdstuk dat
precies "Het historisch referentiekader" heet, net als dit. Zonder de categorie
in de bestandsnaam weet noch dekking.py noch het uploadscherm welke van de twee
bedoeld is, en kiest het uploadscherm liever niets dan verkeerd. "-boost" alleen
volstaat niet, want dat past even goed op Boost dubbele finaliteit.

De oefenbundels dragen daarbovenop het voorvoegsel "oefenbundel-", want die
zouden anders met de leerbundel zelf botsen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Geschiedenis"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Het historisch referentiekader
BUNDELS["het-historisch-referentiekader-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het historisch referentiekader",
    onder="Tijd, ruimte en de maatschappelijke domeinen: het rooster waarmee je elke samenleving kan plaatsen.",
    secties=[
        dict(kop="Waarvoor dient een referentiekader?", blokken=[
            ("p", "Geschiedenis is niet een stapel losse jaartallen. Om iets te kunnen begrijpen, moet je het "
                  "eerst kunnen <strong>plaatsen</strong>: wanneer was het, waar was het, en waarover ging het? "
                  "Die drie vragen samen vormen het <strong>historisch referentiekader</strong>. Het is het "
                  "rooster waarop je elke gebeurtenis, elke bron en elke samenleving legt."),
            ("p", "De drie assen zijn de <strong>tijd</strong>, de <strong>ruimte</strong> en de "
                  "<strong>maatschappelijke domeinen</strong>. Wie er één weglaat, krijgt een scheef beeld. "
                  "Een datum zonder plaats zegt weinig, en een gebeurtenis zonder domein weet je niet waarmee "
                  "te vergelijken."),
            ("kader", "Onthoud de drie: <strong>tijd</strong>, <strong>ruimte</strong> en "
                      "<strong>maatschappelijke domeinen</strong>. Elke opdracht op het examen begint "
                      "eigenlijk met die drie vragen, ook als ze er niet letterlijk staan."),
        ]),
        dict(kop="Structuurbegrippen van de tijd", blokken=[
            ("p", "De <strong>structuurbegrippen</strong> van de tijd zijn de woorden waarmee je over tijd "
                  "praat. De belangrijkste zijn <strong>chronologie</strong>, <strong>periodisering</strong>, "
                  "<strong>continuïteit en verandering</strong>, <strong>evolutie en revolutie</strong>, "
                  "<strong>gelijktijdigheid en ongelijktijdigheid</strong>, en <strong>duur</strong>. Let op: "
                  "<strong>maritiem</strong> hoort er niet bij, dat is een begrip van de ruimte."),
            ("p", "<strong>Chronologie</strong> is gebeurtenissen in de juiste volgorde zetten: wat kwam eerst, "
                  "wat daarna? <strong>Periodisering</strong> is iets anders: dat is de tijd in stukken "
                  "verdelen en die stukken een naam geven, zoals de middeleeuwen of de vroegmoderne tijd. "
                  "Chronologie en periodisering betekenen dus niet hetzelfde: het ene ordent, het andere "
                  "groepeert."),
            ("p", "<strong>Continuïteit</strong> is wat blijft duren, ook al verandert er elders veel. "
                  "<strong>Verandering</strong> is wat anders wordt. In elke periode zitten die twee door "
                  "elkaar: terwijl het wereldbeeld in de 16de eeuw grondig verandert, blijft de landbouw "
                  "bijna werken zoals in 1300."),
            ("p", "Een <strong>evolutie</strong> is een geleidelijke verandering, een "
                  "<strong>revolutie</strong> een snelle en ingrijpende. Het woord revolutie slaat daarbij op "
                  "de <strong>omvang</strong> van de verandering, niet altijd op de snelheid: de industriële "
                  "revolutie duurde meer dan een eeuw en heet toch zo. Evolutie gaat trouwens niet over de "
                  "natuur en revolutie niet enkel over politiek; allebei kunnen ze in elk domein voorkomen."),
            ("p", "<strong>Gelijktijdigheid</strong> is dat twee dingen in dezelfde tijd gebeuren, ook al "
                  "weten de twee plaatsen niets van elkaar. <strong>Ongelijktijdigheid</strong> is het "
                  "omgekeerde: een ontwikkeling die op de ene plaats al ver staat en op de andere nog niet. "
                  "In het begin van de 13de eeuw schrijft men in het <strong>Arabische rijk</strong> al op "
                  "<strong>papier</strong>, terwijl men in <strong>Europa</strong> nog "
                  "<strong>perkament</strong> gebruikt: dezelfde eeuw, twee heel verschillende stadia. Dat is "
                  "geen scharnierpunt en geen revolutie, maar ongelijktijdigheid."),
            ("p", "Met <strong>duur</strong> bedoelt een historicus <strong>hoe lang een toestand of een "
                  "ontwikkeling voortduurt</strong>. Niet hoe zwaar iets was, niet hoeveel het kostte, en ook "
                  "niet in welke volgorde de gebeurtenissen kwamen: dat laatste is chronologie."),
            ("weetje", "Onze jaartelling telt vanaf een afgesproken nulpunt. Jaartallen "
                       "<strong>voor Christus</strong> tellen achterwaarts: 200 v.C. ligt vroeger dan 100 v.C. "
                       "Let daarmee op bij het berekenen van een verschil. En een "
                       "<strong>tijdrekening</strong> begint niet overal ter wereld bij hetzelfde jaar nul: "
                       "de islamitische telt vanaf de hidjra, de joodse vanaf de schepping."),
        ]),
        dict(kop="Periodes en scharnierpunten", blokken=[
            ("p", "De courante westerse periodisering telt <strong>zeven</strong> periodes: de "
                  "<strong>prehistorie</strong>, het <strong>oude nabije oosten</strong>, de "
                  "<strong>klassieke oudheid</strong>, de <strong>middeleeuwen</strong>, de "
                  "<strong>vroegmoderne tijd</strong>, de <strong>moderne tijd</strong> en de "
                  "<strong>hedendaagse tijd</strong>. De ijstijd en de ruimtetijd zijn géén historische "
                  "periodes: de eerste is een klimaatbegrip, de tweede hoort bij de natuurkunde."),
            ("p", "De <strong>prehistorie</strong> is de periode vóór het <strong>schrift</strong>, "
                  "<strong>waarvan</strong> we alleen <strong>materiële resten</strong> hebben: werktuigen, "
                  "graven, beenderen, rotstekeningen. Zodra er geschreven bronnen zijn, spreekt men van "
                  "geschiedenis. Meteen ná de <strong>klassieke oudheid</strong> komen de "
                  "<strong>middeleeuwen</strong>, en de <strong>Tweede Wereldoorlog</strong> situeer je in de "
                  "<strong>hedendaagse tijd</strong>."),
            ("p", tabel(["Periode", "Ruw van wanneer tot wanneer"], [
                ["prehistorie", "tot de uitvinding van het schrift"],
                ["het oude nabije oosten", "vanaf ± 3000 v.C."],
                ["de klassieke oudheid", "± 800 v.C. tot 476"],
                ["de middeleeuwen", "476 tot 1453 of 1492"],
                ["de vroegmoderne tijd", "1453/1492 tot 1789"],
                ["de moderne tijd", "1789 tot 1914"],
                ["de hedendaagse tijd", "1914 tot nu"],
            ])),
            ("kader", "Voor dit vak zijn het de <strong>middeleeuwen</strong> en de <strong>vroegmoderne "
                      "tijd</strong> die je grondig moet kennen. De andere vijf periodes moet je kunnen "
                      "plaatsen, meer niet."),
            ("p", "Je bakent een periode af met twee <strong>principes</strong>: een <strong>selectie van "
                  "kenmerken en gebeurtenissen</strong> die je belangrijk vindt, en een "
                  "<strong>symbolische begin- en einddatum</strong>. Beide zijn keuzes. Daarom is een "
                  "periodegrens altijd voor discussie vatbaar: de verandering gebeurt niet overal op hetzelfde "
                  "moment en niet in alle domeinen tegelijk."),
            ("p", "Een <strong>scharnierpunt</strong> is een gebeurtenis of evolutie die de overgang vormt "
                  "tussen twee periodes. Bekende scharnierpunten zijn de <strong>val van het West-Romeinse "
                  "Rijk in 476</strong>, de <strong>val van Constantinopel in 1453</strong> en de "
                  "<strong>aankomst van Columbus op de Caraïben in 1492</strong>. Met dat laatste jaartal laat men een nieuwe "
                  "periode beginnen omdat de contacten tussen de continenten daarna blijvend veranderen."),
            ("p", "Periodisering heeft daardoor haar <strong>beperkingen</strong>. Ze is gebouwd op een "
                  "<strong>selectie</strong>, dus wat niet gekozen is, valt weg. Ze suggereert een "
                  "<strong>scherpe breuk</strong> waar de werkelijkheid geleidelijk is. En ze "
                  "<strong>past niet even goed op niet-westerse samenlevingen</strong>: de westerse indeling "
                  "past niet zo goed op de geschiedenis van China als op die van Europa. Wat ze niét doet, is "
                  "het dateren van gebeurtenissen onmogelijk maken."),
            ("p", "Er bestaan ook andere periodiseringen dan de westerse: de Chinese geschiedenis wordt in "
                  "dynastieën ingedeeld, de islamitische telt vanaf de hidjra, en <strong>Nederland</strong> "
                  "gebruikt een eigen indeling met <strong>tien tijdvakken</strong>. Dat laatste bewijst niet "
                  "dat tien juister is dan zeven; het toont dat de indeling van de geschiedenis een "
                  "<strong>keuze</strong> is en geen natuurwet. Je vergelijkt periodiseringen niet om te "
                  "bewijzen welke de beste is, maar om te zien dat elke indeling steunt op een keuze van "
                  "kenmerken. Hetzelfde jaartal kan daardoor in de ene indeling een grens zijn en in de "
                  "andere niet."),
        ]),
        dict(kop="Structuurbegrippen van de ruimte", blokken=[
            ("p", "Bij de ruimte horen begrippen als <strong>lokaal</strong>, <strong>regionaal</strong>, "
                  "<strong>nationaal</strong>, <strong>continentaal</strong> en <strong>mondiaal</strong>, "
                  "en daarnaast <strong>maritiem</strong>, <strong>ruraal</strong> en "
                  "<strong>stedelijk</strong>, <strong>westers</strong> en <strong>niet-westers</strong> en "
                  "de aanduiding van een <strong>wereldstreek</strong>. <strong>Mondiaal</strong> is het <strong>ruimtebegrip</strong> "
                  "dat je gebruikt voor iets dat de hele wereld raakt, <strong>ruraal</strong> betekent <strong>op het "
                  "platteland</strong>, en <strong>revolutie</strong> hoort hier níét bij: dat is een begrip "
                  "van de tijd."),
            ("p", "<strong>Westers</strong> verwijst niet louter naar een <strong>windstreek</strong> op de "
                  "kaart. Het slaat op een groep samenlevingen met een gedeelde geschiedenis, en waar die "
                  "groep precies ophoudt, is zelf een discussie. Hetzelfde geldt voor niet-westers: dat is "
                  "een verzamelnaam voor heel verschillende werelden."),
            ("p", "Een <strong>historische kaart</strong> toont hoe een gebied er in een bepaalde tijd "
                  "uitzag, met de grenzen, de namen en de machtsverhoudingen van toen. Ze verschilt dus van "
                  "een kaart van vandaag: het gaat niet om een andere kleur, maar om een andere wereld. Leg je "
                  "een kaart van het <strong>rijk van Karel V</strong> naast een kaart van vandaag, dan ben je "
                  "een historisch gegeven aan het <strong>situeren in de ruimte</strong> — niet in de tijd, en "
                  "je beoordeelt er ook geen bron mee op betrouwbaarheid."),
            ("kader", "Dezelfde gebeurtenis kan op verschillende schaalniveaus betekenis hebben. De "
                      "Guldensporenslag is lokaal een veldslag bij Kortrijk, regionaal een zaak van het "
                      "graafschap Vlaanderen en continentaal een episode in de strijd om Frankrijk."),
        ]),
        dict(kop="De maatschappelijke domeinen", blokken=[
            ("p", "De vakfiche onderscheidt <strong>vier</strong> <strong>maatschappelijke domeinen</strong>: het "
                  "<strong>politieke</strong>, het <strong>sociale</strong>, het <strong>economische</strong> "
                  "en het <strong>culturele</strong> domein. Het politieke gaat over macht en bestuur, het "
                  "sociale over de verhouding tussen groepen mensen, het economische over produceren, handelen "
                  "en betalen, het culturele over godsdienst, kunst, wetenschap en wereldbeeld."),
            ("p", tabel(["Domein", "Waarover het gaat", "Voorbeelden"], [
                ["politiek", "macht, bestuur, wetten", "het absolutisme van Lodewijk XIV"],
                ["sociaal", "groepen en hun verhouding", "de gelaagde samenleving, migratie, slavernij"],
                ["economisch", "produceren, handelen, betalen", "de geldeconomie, e-commerce"],
                ["cultureel", "geloof, kunst, wetenschap", "de Reformatie, een godsdienst, de drukkunst"],
            ])),
            ("p", "Let op de voorbeelden in die tabel. <strong>E-commerce</strong>, handel over het internet, "
                  "hoort in het <strong>economische</strong> domein, hoe modern het ook klinkt. Een "
                  "<strong>godsdienst</strong> hoort in het <strong>culturele</strong> domein. En de "
                  "<strong>gelaagde samenleving</strong>, <strong>migratie</strong> en "
                  "<strong>slavernij</strong> zijn drie <strong>rijen</strong> van het "
                  "<strong>sociale</strong> domein: ze gaan alle drie over de verhouding tussen groepen "
                  "mensen. De <strong>drukkunst</strong> hoort daar niet bij, die is cultureel."),
            ("p", "Eén gebeurtenis kan in <strong>meerdere domeinen tegelijk</strong> thuishoren. De "
                  "Guldensporenslag hoort zowel in het politieke als in het sociale domein: het ging om macht "
                  "over Vlaanderen én om de verhouding tussen bevolkingsgroepen in de steden. Wie dat moet "
                  "uitleggen, toont precies die twee kanten aan."),
            ("p", "Een <strong>geschilderd portret van sultan Süleyman I</strong> is een mooi voorbeeld van "
                  "twee domeinen tegelijk. Het is een <strong>politiek</strong> stuk, want het toont de macht "
                  "van de <strong>sultan</strong> en is gemaakt om die macht te tonen, en het is een "
                  "<strong>cultureel</strong> stuk, want het is een kunstwerk uit een bepaalde stijl. Met het "
                  "economische of het sociale domein heeft het weinig te maken."),
            ("p", "Het <strong>geografische domein</strong>, het <strong>maritieme domein</strong> en het "
                  "<strong>militaire domein</strong> staan niet in de lijst: dat zijn géén maatschappelijke "
                  "domeinen. Wat op zee, in een landschap of in een oorlog gebeurt, breng je onder bij een van "
                  "de vier."),
        ]),
        dict(kop="Waarvoor gebruik je het kader?", blokken=[
            ("p", "Je gebruikt het referentiekader om een bron, een gebeurtenis of een samenleving te "
                  "<strong>situeren</strong>, en daarna om te kunnen <strong>vergelijken</strong>. Zonder een "
                  "vast rooster vergelijk je appelen met peren."),
            ("p", "Het dient ook om een <strong>historische vraag</strong> af te bakenen. Een vraag die niet "
                  "in tijd, ruimte en domein afgebakend is, kan je niet met bronnen beantwoorden. Daarover "
                  "gaat de bundel <em>Redeneren met historische bronnen</em>."),
            ("weetje", "Het referentiekader is geen stof die je apart instudeert en daarna vergeet. Het komt "
                       "in elke andere bundel terug, want elk thema wordt erin geplaatst."),
        ]),
    ],
)

# ───────────────────────── 2. Van Rome naar de Franken
BUNDELS["van-rome-naar-de-franken-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Van Rome naar de Franken",
    onder="Het einde van het West-Romeinse Rijk, de Germaanse migraties, en het rijk van de Merovingers en de Karolingers.",
    secties=[
        dict(kop="Het einde van het West-Romeinse Rijk", blokken=[
            ("p", "Volgens de <strong>symbolische datering</strong> valt het <strong>West-Romeinse Rijk</strong> in "
                  "<strong>476</strong>: dat jaar wordt de laatste keizer afgezet. Dat jaartal geldt als scharnierpunt tussen de klassieke oudheid en de "
                  "middeleeuwen. Het <strong>Oost-Romeinse Rijk</strong>, met Constantinopel als hoofdstad, "
                  "blijft nog bijna duizend jaar bestaan."),
            ("p", "Historici noemen de val van Rome liever een <strong>proces</strong> dan een gebeurtenis, "
                  "omdat het gezag over meer dan een eeuw stukje bij beetje wegviel. Er ging niet op één dag "
                  "een lamp uit: belastingen werden niet meer geïnd, legers werden niet meer betaald, steden "
                  "liepen leeg en het bestuur viel uiteen."),
            ("p", "Er waren <strong>interne</strong> en <strong>externe</strong> oorzaken. Intern: "
                  "burgeroorlogen tussen keizers en tegenkeizers, muntontwaarding, zware belastingdruk en een "
                  "leger dat steeds meer uit ingehuurde Germanen bestond. Extern: de druk van volkeren aan de "
                  "grenzen."),
            ("p", "Na de val viel West-Europa uiteen in <strong>kleinere, zwak bestuurde "
                  "koninkrijken</strong>. De Romeinse staat met zijn belastingen, zijn ambtenaren en zijn "
                  "beroepsleger verdween; wat ervoor in de plaats kwam, was veel losser georganiseerd."),
        ]),
        dict(kop="De Germaanse volksverhuizingen", blokken=[
            ("p", "Met de <strong>Germaanse migraties</strong> bedoelt men de verplaatsing van Germaanse "
                  "volkeren naar het gebied van het Romeinse Rijk. Ook hier onderscheid je oorzaken. Met "
                  "<strong>interne oorzaken van de Germaanse migraties</strong> bedoelt men redenen binnen de "
                  "Germaanse samenlevingen zelf: <strong>bevolkingsgroei</strong> en <strong>gebrek aan "
                  "landbouwgrond</strong>."),
            ("p", "De <strong>externe oorzaken</strong> komen van búíten de Germaanse wereld. De "
                  "belangrijkste is de druk van de <strong>Hunnen</strong> uit het oosten, die andere volkeren "
                  "voor zich uit dreef. Daarnaast tellen de <strong>rijkdom</strong> en het "
                  "<strong>klimaat</strong> van het Romeinse rijk als <strong>aantrekkingskracht</strong>, en "
                  "de <strong>verzwakte grensverdediging</strong> van Rome. Bevolkingsgroei is dus intern, de "
                  "Hunnen en de aantrekkingskracht van Rome zijn extern."),
            ("p", "De migraties verliepen <strong>niet overal en altijd gewelddadig</strong>. Sommige groepen "
                  "vielen binnen, andere werden als bondgenoot binnengelaten of als soldaat in dienst genomen, "
                  "en nog andere trokken gewoon geleidelijk mee met de rest. <strong>Migratie</strong> is in "
                  "deze periode trouwens zowel een <strong>sociaal</strong> als een <strong>politiek "
                  "verschijnsel</strong>: het verandert wie er naast wie woont, én wie er de macht heeft."),
            ("p", "Wat volgt, is geen vervanging van de ene cultuur door de andere maar een "
                  "<strong>versmelting</strong>. Drie <strong>tradities</strong> versmelten daarbij tot één nieuwe "
                  "cultuur: de <strong>Germaanse</strong>, de <strong>Romeinse</strong> en de "
                  "<strong>christelijke</strong>. Hun gewoonten en gebruiken "
                  "bestonden naast elkaar en vermengden zich: Germaans recht naast Romeins recht, Latijn als "
                  "schrijftaal naast Germaanse spreektalen, oude feesten die een christelijke betekenis "
                  "kregen. Dat is wat men bedoelt met een <strong>gemengde samenleving</strong>."),
            ("kader", "Gemengd betekent hier níét dat iedereen dezelfde taal sprak, dat er van elke groep "
                      "evenveel mensen waren, of dat de koning half Romein en half Frank was. Het gaat over "
                      "gewoonten die zich met elkaar vermengen."),
            ("p", "Een stuk <strong>Romeinse erfenis</strong> blijft in de vroege middeleeuwen "
                  "<strong>doorwerken</strong>: het <strong>Latijn</strong> als taal van kerk en bestuur, het "
                  "<strong>wegennet</strong> dat men blijft gebruiken, en de <strong>indeling in "
                  "bisdommen</strong> naar de Romeinse steden, die vandaag nog altijd zichtbaar is. Wat niet "
                  "doorwerkt, is het keizerschap zoals de Romeinen het kenden: van een keizerschap dat het "
                  "volk zou kiezen, is bij de Franken geen sprake."),
        ]),
        dict(kop="De Merovingers", blokken=[
            ("p", "De <strong>Franken</strong> wonen oorspronkelijk <strong>langs de benedenloop van de "
                  "Rijn</strong>, dus niet in Noord-Afrika, niet op het Iberisch schiereiland en niet in "
                  "Zuid-Italië. Van daaruit vestigen ze zich in het noorden van Gallië. De "
                  "<strong>Merovingers</strong> zijn de eerste <strong>dynastie</strong> die over het "
                  "Frankische rijk regeert; de Karolingers komen later, de Capetingers en de Ottonen nog veel "
                  "later. Onder "
                  "<strong>Clovis</strong> groeit hun gebied uit tot een rijk. Clovis laat zich rond 500 "
                  "<strong>dopen</strong>, en dat is een politieke daad zoveel als een godsdienstige: hij "
                  "kiest voor het katholieke geloof van de Gallo-Romeinse bevolking en van de bisschoppen, en "
                  "wint hun steun."),
            ("p", "Het <strong>Frankische erfrecht</strong> houdt in dat het rijk bij de dood van de koning "
                  "<strong>onder zijn zonen verdeeld</strong> wordt. Niet de oudste zoon erft alles; elk van "
                  "de zonen krijgt een stuk. Het gevolg voor de koninklijke macht is ernstig: het rijk viel "
                  "telkens opnieuw uiteen in kleinere delen, met broederoorlogen erbovenop."),
            ("p", "Daardoor wisselen <strong>periodes van eenheid en verdeeldheid</strong> elkaar af. Onder de "
                  "laatste Merovingers is de koninklijke macht zo uitgehold dat de echte beslissingen elders "
                  "vallen: bij de <strong>hofmeier</strong>, de hoogste ambtenaar aan het hof, die in naam van "
                  "de koning bestuurde. De laatste Merovingische koningen kregen daarom de spotnaam "
                  "<strong>vadsige koningen</strong>: ze droegen de titel, maar de echte macht lag bij de "
                  "hofmeiers."),
        ]),
        dict(kop="De Karolingers", blokken=[
            ("p", "De hofmeiers nemen de macht uiteindelijk zelf over. <strong>Pepijn de Korte</strong> laat "
                  "zich in 751 koning maken en door de <strong>paus zalven</strong>: zo laat hij zijn "
                  "machtsovername godsdienstig bevestigen. Politiek en godsdienst versterken elkaar, en de "
                  "paus krijgt er een beschermer voor terug."),
            ("p", "Onder <strong>Karel de Grote</strong> bereikt het rijk zijn grootste omvang: van de Ebro "
                  "in Spanje tot voorbij de Elbe, en tot in Italië. In het jaar <strong>800</strong> wordt hij "
                  "in Rome tot <strong>keizer</strong> gekroond. Die <strong>keizerskroning</strong> versterkte de band "
                  "tussen de Frankische macht en de Kerk. Het rijk wordt bestuurd in "
                  "<strong>gouwen</strong>, bestuurlijke gebieden onder leiding van een <strong>graaf</strong>. "
                  "Hoe hield hij toezicht op zo'n uitgestrekt rijk? Met die graven, met rondreizende "
                  "controleurs — de <strong>missi dominici</strong> of koningsboden — en met "
                  "<strong>wetten en richtlijnen die hij liet opschrijven</strong>. Een vast parlement dat de "
                  "wetten stemde, bestond niet. En de graven bleven niet altijd trouwe uitvoerders van de "
                  "koninklijke wil: hoe verder van Aken, hoe meer ze hun gouw als hun eigen bezit gingen "
                  "beschouwen."),
            ("p", "<strong>Aken</strong> is zijn hoofdplaats, en daar komt een <strong>culturele "
                  "heropleving</strong> op gang die men de <strong>Karolingische renaissance</strong> noemt: "
                  "een school aan het hof, kopieerwerkplaatsen waar oude teksten overgeschreven werden, en een "
                  "nieuw, leesbaar schrift. Veel Latijnse teksten uit de oudheid kennen wij enkel omdat ze "
                  "daar gekopieerd zijn. Gotische kathedralen en de boekdrukkunst komen pas eeuwen later, en "
                  "de Romeinse theaters en badhuizen gingen niet opnieuw open."),
            ("p", "Die heropleving bleef wel een zaak van het hof, de kloosters en een kleine groep "
                  "geletterden. De <strong>gewone boerenbevolking bereikte ze nauwelijks</strong>: die kon "
                  "niet lezen en kwam nooit in Aken."),
            ("p", "Vergelijk je de koninklijke macht onder de <strong>Merovingers</strong> en de "
                  "<strong>Karolingers</strong>, dan zie je dat ze onder de Karolingers eerst "
                  "<strong>sterker</strong> werd, om daarna opnieuw te <strong>verbrokkelen</strong>. Het "
                  "erfrecht bleef immers gelden."),
        ]),
        dict(kop="Verdun en wat daarna kwam", blokken=[
            ("p", "Bij het <strong>Verdrag van Verdun in 843</strong> wordt het rijk onder drie kleinzonen van "
                  "Karel de Grote verdeeld. Uit die <strong>verdeling van Verdun</strong> groeien de latere "
                  "koninkrijken <strong>Frankrijk</strong> en <strong>Duitsland</strong>. Of dat een voorbeeld is van territoriale eenheid of van "
                  "verdeeldheid, is een beoordelingsvraag: het rijk blijft in naam één keizerrijk, maar in "
                  "feite ontstaan er drie zelfstandige delen, waaruit later Frankrijk en Duitsland groeien."),
            ("p", "In de 9de en 10de eeuw wordt het rijk getroffen door nieuwe <strong>aanvallen</strong>, de "
                  "<strong>invallen</strong> van drie kanten: "
                  "<strong>Noormannen</strong> vanuit het noorden, <strong>Saracenen</strong> vanuit het "
                  "zuiden, <strong>Hongaren</strong> of Magyaren vanuit het oosten. De "
                  "<strong>Mongolen</strong> horen daar niet bij; die komen pas in de 13de eeuw en bereiken "
                  "West-Europa niet. Het gevolg voor de macht in het rijk: "
                  "de bevolking zocht bescherming bij de <strong>lokale heer</strong>, want die kon meteen "
                  "helpen en de verre koning niet. Daardoor verzwakte het centrale gezag verder."),
            ("weetje", "Daar ligt het begin van het <strong>leenstelsel</strong>: een heer geeft grond in "
                       "leen in ruil voor trouw en krijgsdienst. Macht wordt zo een keten van persoonlijke "
                       "afspraken in plaats van een staat met ambtenaren."),
        ]),
        dict(kop="Karel de Grote als historische vraag", blokken=[
            ("p", "De <strong>zalving van een koning door de paus</strong> situeer je in twee domeinen: in "
                  "het <strong>politieke</strong> domein, want het gaat over wie er mag heersen, en in het "
                  "<strong>culturele</strong> domein, want het is een godsdienstige plechtigheid. Bij de "
                  "Franken waren politiek en godsdienst dus géén twee <strong>gescheiden werelden</strong>: "
                  "ze leunden juist op elkaar. De keizerstitel gaf Karel de Grote trouwens geen rechtstreekse "
                  "macht over heel Europa; buiten zijn eigen rijk betekende hij vooral aanzien."),
            ("p", "\"Kan je Karel de Grote de vader van Europa noemen?\" is een <strong>historische "
                  "vraag</strong> en geen feitenvraag, omdat het antwoord afhangt van wat je onder Europa "
                  "verstaat en van welke bronnen je kiest. Er is geen jaartal dat het beslist."),
            ("p", "Wie naar zijn rijk kijkt, ziet Frankrijk, Duitsland en Italië onder één gezag. Wie naar "
                  "zijn veldtochten kijkt, ziet een veroveraar die de Saksen met geweld bekeerde. Wie naar de "
                  "school in Aken kijkt, ziet een culturele erfenis. Alle drie steunen op bronnen."),
            ("kader", "Onthoud de manier van werken: je verzamelt argumenten uit bronnen, je zet ze tegenover "
                      "elkaar, je weegt ze af, en je formuleert een <strong>beargumenteerd antwoord</strong>. "
                      "Dat het antwoord van iemand anders kan verschillen, is geen fout."),
        ]),
    ],
)

# ───────────────────────── 3. Standen, domein en stad
BUNDELS["standen-domein-en-stad-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Standen, domein en stad",
    onder="De gelaagde samenleving, het domein als zelfvoorzienend systeem, en de heropbloei van de steden.",
    secties=[
        dict(kop="De drie standen", blokken=[
            ("p", "De middeleeuwse samenleving werd voorgesteld als een samenleving van drie "
                  "<strong>standen</strong>: de <strong>geestelijkheid</strong>, de <strong>adel</strong> en "
                  "de <strong>derde stand</strong>. De taak van de geestelijkheid was <strong>bidden</strong>, die van de "
                  "adel <strong>strijden</strong>, en die van de derde stand <strong>werken</strong>. De geestelijkheid bad "
                  "voor het zielenheil van allen, de adel beschermde met het zwaard, en de derde stand werkte "
                  "en onderhield de twee andere."),
            ("p", "In welke stand je geboren werd, bepaalde bijna helemaal welk leven je kreeg. Niet je "
                  "verdienste maar je <strong>geboorte</strong> bepaalde je plaats. Dat onderscheidt een "
                  "standensamenleving van een samenleving met sociale mobiliteit."),
            ("p", "De adel had <strong>rechten die de derde stand niet had</strong>: eigen rechtspraak over de "
                  "bewoners van zijn domein, vrijstelling van bepaalde belastingen, en het recht om te jagen "
                  "in de heerlijke bossen. Verkiezingen bestonden niet, dus stemrecht hoorde er niet bij."),
            ("p", "De <strong>sociale ongelijkheid bleef zo lang bestaan</strong> omdat de ordening als door "
                  "God gewild werd voorgesteld, én omdat de voorrechten erfelijk waren. Wie de ordening in "
                  "vraag stelde, ging in tegen wat de Kerk verkondigde."),
            ("kader", "De voorstelling van de drie standen is zélf een bron die je kritisch moet bekijken: ze "
                      "is opgeschreven door <strong>geestelijken</strong>, die er zelf bovenaan in staan. Wie "
                      "een ordening beschrijft, beschrijft meteen zijn eigen plaats erin."),
            ("p", "De standensamenleving bleef ook niet de hele middeleeuwen dezelfde. Met de groei van de "
                  "steden komt er een groep bij die rijk is zonder adellijk te zijn. En er waren "
                  "<strong>minderheidsgroepen</strong>, zoals de joden, die buiten de driedeling vielen: de "
                  "driedeling was een christelijk beeld van een christelijke samenleving."),
            ("p", "Qua maatschappelijk domein situeer je de standensamenleving in het <strong>sociale</strong>, het "
                  "<strong>politieke</strong> en het <strong>culturele</strong> domein: ze bepaalt wie waar "
                  "staat, wie mag beslissen, en de Kerk levert er de rechtvaardiging voor. Maritiem is geen "
                  "domein maar een ruimtebegrip."),
        ]),
        dict(kop="De agrarische samenleving en het domein", blokken=[
            ("p", "Een <strong>domein</strong> is het grondbezit van een heer. Het bestaat uit "
                  "<strong>vroonland</strong>, dat de heer voor zichzelf liet bewerken, en "
                  "<strong>hoevenland</strong>, dat hij onder de boeren verdeelde."),
            ("p", "Het domein was <strong>zelfvoorzienend</strong>: bijna alles wat men nodig had, werd er "
                  "zelf geproduceerd. Voedsel, kleding, gereedschap. Er werd weinig gekocht en weinig "
                  "verkocht."),
            ("p", "De bewoners hadden <strong>rechten en plichten</strong>. Een <strong>horige</strong> was "
                  "niet vrij om te vertrekken, maar <strong>horigen waren geen slaven</strong> en konden niet verkocht "
                  "worden: een horige "
                  "had een eigen hoeve. Zijn verplichtingen waren <strong>herendiensten</strong> op het "
                  "vroonland, een deel van de oogst afstaan, en tol en heffingen betalen bij de molen en de "
                  "oven van de heer. In het leger van de koning dienen hoorde bij de tweede stand."),
        ]),
        dict(kop="Vernieuwingen in de landbouw", blokken=[
            ("p", "In de middeleeuwen komen er <strong>landbouwvernieuwingen</strong> op: het "
                  "<strong>drieslagstelsel</strong>, de <strong>keerploeg</strong> en het "
                  "<strong>haam</strong>, waardoor een paard met zijn schouders kan trekken in plaats van met "
                  "zijn keel. Kunstmest hoort daar niet bij; die komt pas in de 19de eeuw."),
            ("p", "Bij het <strong>drieslagstelsel</strong> wordt de grond in drie delen verdeeld: "
                  "wintergraan, zomergraan en <strong>braak</strong>. Braakland is het deel dat een jaar niet "
                  "bewerkt wordt om te herstellen. Tegenover het oudere tweeslagstelsel ligt er zo maar een "
                  "derde braak in plaats van de helft, en dus is er meer grond in gebruik."),
            ("p", "Meer voedsel leidde tot een <strong>groeiende bevolking</strong>, en die groei maakte "
                  "steden mogelijk: niet iedereen moest nog voedsel produceren."),
            ("p", "Op de <strong>lokale markt</strong> verhandelde men vooral voedsel en gereedschap. Over "
                  "<strong>lange afstand</strong> ging het vooral om dure en lichte waren: specerijen, zijde, "
                  "edelmetaal, later laken. Vervoer was traag en duur, dus loonde het enkel voor wat veel "
                  "waarde in weinig gewicht had. De vooruitgang in de landbouw en de groei van de handel "
                  "hangen samen: pas als er een overschot is, valt er iets te verkopen."),
        ]),
        dict(kop="De heropbloei van de steden", blokken=[
            ("p", "Vanaf de <strong>11de eeuw</strong> bloeien de steden weer op. De factoren die daartoe "
                  "bijdragen: een <strong>groeiende bevolking</strong> door betere landbouw, meer "
                  "<strong>veiligheid</strong> waardoor handel over langere afstand kon, en de "
                  "<strong>ligging</strong> aan een rivier, een weg of een kruispunt."),
            ("p", "Veel steden ontstonden aan een <strong>rivier</strong> omdat water de goedkoopste manier "
                  "was om zware vracht te vervoeren. Een schip draagt veel meer dan een kar, en het hoeft geen "
                  "slechte wegen te trotseren."),
            ("p", "In de stad werken <strong>ambachtslui</strong>. Wie hetzelfde beroep uitoefent, verenigt "
                  "zich in een <strong>ambacht</strong>, ook <strong>gilde</strong> genoemd. Dat regelt wie "
                  "het beroep mag uitoefenen, de kwaliteit van het geleverde werk en de opleiding van "
                  "leerjongen over gezel tot meester. De belastingen van het hele graafschap regelde het "
                  "niet; dat was de zaak van de vorst."),
            ("p", "<strong>Meester worden</strong> kon niet zomaar: je doorliep jaren als leerjongen en "
                  "gezel, je maakte een meesterproef, en je had geld nodig voor een eigen werkplaats. Zonen "
                  "van meesters kwamen er veel makkelijker in."),
        ]),
        dict(kop="Geld, macht en ongelijkheid in de stad", blokken=[
            ("p", "Met de stad komt de <strong>geldeconomie</strong> op: goederen en arbeid worden steeds "
                  "vaker met <strong>geld</strong> betaald in plaats van in natura. Op het domein betaalde men "
                  "in dagen werk en in graan; in de stad betaalt men in munten. Daarmee komen ook "
                  "<strong>wisselaars</strong>, <strong>kredietvormen</strong> en <strong>boekhouding</strong> "
                  "op, en uit dat beroep groeit het bankwezen. Het ontstaan van de geldeconomie hoort in de "
                  "eerste plaats in het <strong>economische</strong> maatschappelijk domein thuis."),
            ("p", "Steden kregen <strong>politieke zelfstandigheid</strong> doordat ze "
                  "<strong>privileges</strong> van hun vorst kochten of verkregen. Zo'n oorkonde met "
                  "stadsrechten heet een <strong>keure</strong>. Een vorst had geld nodig en een stad had "
                  "geld; in ruil kreeg ze eigen rechtspraak, eigen bestuur en het recht op een markt."),
            ("p", "Binnen de muren was niet iedereen gelijk. Een kleine groep rijke koopmansfamilies, de "
                  "<strong>patriciërs</strong>, bestuurde de stad. De politieke ongelijkheid leidde tot "
                  "<strong>opstanden van de ambachten tegen de patriciërs</strong>; in de Vlaamse steden "
                  "veroverden de ambachten in de 14de eeuw een plaats in het stadsbestuur."),
            ("p", "Bij een stad horen eigen <strong>gebouwen</strong>: het <strong>belfort</strong> als toren "
                  "van de stedelijke vrijheid en bewaarplaats van de privileges, de <strong>lakenhalle</strong> "
                  "om handelswaar te verhandelen en te keuren, en de <strong>kathedraal</strong> als centrum "
                  "van het godsdienstige leven. Het belfort is dus geen kerkelijk gebouw maar het wereldlijke "
                  "tegenbeeld van de kerktoren."),
        ]),
        dict(kop="De pest, en stad en platteland samen", blokken=[
            ("p", "In het midden van de <strong>14de eeuw</strong> treft de <strong>pest</strong> West-Europa "
                  "het hardst. Vanaf 1347 sterft op enkele jaren tijd naar schatting een derde van de "
                  "bevolking. De gevolgen: arbeid werd schaars en dus stegen de lonen, veel grond kwam leeg te "
                  "liggen, en sommige groepen, zoals de joden, kregen de schuld en werden vervolgd. De "
                  "bevolking groeide niet, ze kromp."),
            ("p", "<strong>Stad en platteland</strong> stonden niet los van elkaar maar waren met elkaar "
                  "<strong>verweven</strong>. De stad haalde haar voedsel en haar nieuwe inwoners van het "
                  "platteland, het platteland kocht gereedschap en laken in de stad, en stedelijke burgers "
                  "kochten grond buiten de muren. Het platteland bestuurde de stad niet; het ging net "
                  "andersom."),
            ("weetje", "<strong>Stadslucht maakt vrij.</strong> Wie lang genoeg in de stad verbleef, meestal "
                       "een jaar en een dag, kon zijn horigheid kwijtraken. De stad werd zo een uitweg voor "
                       "wie op het domein vastzat."),
            ("p", "De groei van de steden is daarom een <strong>verandering</strong> en niet zomaar een "
                  "continuïteit: er ontstaat een nieuwe groep die rijk is zonder adellijk te zijn, en de oude "
                  "standenleer had daar geen plaats voor."),
        ]),
    ],
)

# ───────────────────────── 4. Geloof, kunst en macht in de middeleeuwen
BUNDELS["geloof-kunst-en-macht-in-de-middeleeuwen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Geloof, kunst en macht in de middeleeuwen",
    onder="De christelijke samenleving, romaans en gotisch, de strijd om de macht, en het contact met de islamitische wereld.",
    secties=[
        dict(kop="De bekering van West-Europa", blokken=[
            ("p", "Het <strong>christendom</strong> verspreidde zich over West-Europa doordat "
                  "<strong>missionarissen</strong> eerst de vorst bekeerden, en daarna zijn volk. Bekeerde je "
                  "de koning, dan volgde zijn hofhouding en daarna zijn onderdanen. Daarom is de doop van "
                  "Clovis zo'n keerpunt."),
            ("p", "Oude gewoonten verdwenen niet altijd: sommige feesten en gebruiken kregen gewoon een "
                  "<strong>christelijke betekenis</strong>. Een midwinterfeest werd Kerstmis, een bron werd "
                  "een heiligenbron. Dat samengaan hoort bij de versmelting van Germaanse, Romeinse en "
                  "christelijke gebruiken."),
        ]),
        dict(kop="De organisatie van de Kerk", blokken=[
            ("p", "De <strong>katholieke Kerk</strong> was opgebouwd als een <strong>piramide</strong>: de "
                  "<strong>paus</strong> bovenaan, daaronder de <strong>bisschoppen</strong>, en daaronder de "
                  "<strong>pastoors</strong> in de parochies. Die vaste ordening gaf de Kerk een macht die "
                  "over de grenzen van vorstendommen heen reikte."),
            ("p", "Daarnaast waren er de <strong>kloosters</strong>. Een <strong>monnik</strong> is een "
                  "geestelijke die in een klooster leeft volgens een <strong>regel</strong>; die van "
                  "Benedictus is de bekendste. Naast het gebed <strong>kopieerden en bewaarden</strong> de "
                  "kloosters oude teksten, <strong>ontgonnen</strong> ze woeste grond tot landbouwgrond en "
                  "<strong>zorgden</strong> ze voor zieken en reizigers. Munten slaan deden ze niet; dat was "
                  "een recht van de vorst."),
            ("p", "De Kerk bepaalde mee het <strong>ritme van het dagelijkse leven</strong>: de klokken gaven "
                  "de uren aan, de zondag en de feestdagen de week en het jaar, en doop, huwelijk en "
                  "begrafenis de levensloop. Qua maatschappelijk domein situeer je de organisatie van de "
                  "katholieke Kerk vooral in het <strong>culturele domein</strong>, al was ze ook economisch "
                  "en politiek van gewicht."),
        ]),
        dict(kop="Tegenover wie anders geloofde", blokken=[
            ("p", "<strong>Ketterij</strong> is een geloofsopvatting die van de leer van de Kerk afwijkt. "
                  "Omdat geloof en samenleving samenvielen, werd afwijken ook als een aanval op de orde zelf "
                  "gezien."),
            ("p", "<strong>Joden</strong> hadden in de middeleeuwse steden niet dezelfde rechten als "
                  "christenen. Ze mochten vaak geen grond bezitten en geen ambacht uitoefenen, moesten soms "
                  "apart wonen of een kenteken dragen, en werden bij rampen zoals de pest als zondebok "
                  "aangewezen."),
            ("kader", "Een middeleeuwse bron over joden lees je extra kritisch, want ze is bijna altijd door "
                      "een <strong>christelijke auteur</strong> geschreven, met zijn beeld van de ander. De "
                      "stem van de groep zelf ontbreekt meestal."),
        ]),
        dict(kop="Kunst als verhaal in beeld", blokken=[
            ("p", "Voor wie niet kon lezen, diende <strong>christelijke kunst</strong> als een "
                  "<strong>verhaal in beeld</strong>: glasramen, beelden en muurschilderingen vertelden de "
                  "Bijbel. Men noemde een kerk daarom wel eens de bijbel van de armen. Ook vandaag verspreidt "
                  "die kunst nog waarden, in gebouwen die er nog staan."),
            ("p", "<strong>Romaanse</strong> bouwkunst herken je aan <strong>rondbogen</strong>, "
                  "<strong>dikke muren met kleine vensters</strong> en een zware, gesloten en donkere indruk. "
                  "De muur moet het hele gewicht dragen, dus blijven de vensters klein."),
            ("p", "De <strong>gotische</strong> kerk is lichter en hoger omdat "
                  "<strong>spitsbogen</strong>, <strong>kruisribgewelven</strong> en "
                  "<strong>luchtbogen</strong> het gewicht opvangen. Een spitsboog is een boog met een punt "
                  "bovenaan; hij leidt het gewicht steiler naar beneden dan een rondboog. Draagt het geraamte "
                  "het gewicht, dan hoeft de muur dat niet meer, en kunnen er grote glasramen in."),
            ("p", "Het verschil tussen romaans en gotisch zit dus niet in de versiering maar in de "
                  "<strong>bouwtechniek</strong>: de rondboog duwt naar buiten, de spitsboog vooral naar "
                  "beneden."),
            ("p", "De <strong>Vlaamse primitieven</strong>, met <strong>Jan van Eyck</strong> voorop, heten zo "
                  "omdat ze bij de <strong>eersten</strong> waren die met olieverf zo gedetailleerd "
                  "schilderden. Primitief betekent hier eerste, niet onbeholpen. Het Lam Gods in Gent toont "
                  "hoe ver die techniek al stond."),
        ]),
        dict(kop="Mens- en wereldbeeld en geleerdheid", blokken=[
            ("p", "In het middeleeuwse <strong>wereldbeeld</strong> stond de aarde in het midden en was alles "
                  "door God geordend. Elk wezen had zijn vaste plaats in die ordening, van steen tot engel. "
                  "Ook de standenleer past in dat beeld."),
            ("p", "Aan een <strong>middeleeuwse kaart</strong> zie je dat ze geen aardrijkskundige kaart is "
                  "zoals wij die kennen: <strong>Jeruzalem staat in het midden</strong> en het "
                  "<strong>oosten bovenaan</strong>. Zo'n kaart ordent de wereld naar geloof, niet naar "
                  "afstand. Ze meet niet, ze vertelt."),
            ("p", "De <strong>Arabische wetenschappen</strong> hadden grote invloed op christelijk Europa: "
                  "Griekse teksten kwamen via <strong>Arabische vertalingen</strong> terug, de "
                  "<strong>cijfers</strong> waarmee wij nog altijd rekenen kwamen langs die weg, en "
                  "geneeskunde, sterrenkunde en wiskunde gingen er sterk op vooruit. De boekdrukkunst met "
                  "losse letters hoort daar niet bij; die komt van Gutenberg in de 15de eeuw."),
            ("weetje", "Hoger onderwijs bestond wel degelijk. Vanaf de 12de eeuw ontstaan "
                       "<strong>universiteiten</strong>, zoals Bologna, Parijs en later Leuven. Men studeerde "
                       "er in het Latijn."),
        ]),
        dict(kop="De strijd om de macht: Frankrijk en Engeland", blokken=[
            ("p", "In <strong>Frankrijk</strong> breidde de koning in de late middeleeuwen zijn gebied en zijn "
                  "gezag <strong>stap voor stap uit</strong>. Van een koning die alleen rond Parijs iets te "
                  "zeggen had, groeit hij uit tot vorst van een groot en centraal bestuurd rijk."),
            ("p", "In <strong>Engeland</strong> ging het anders: daar moest de koning zijn macht "
                  "<strong>delen met een parlement</strong>. De <strong>Magna Carta</strong> van 1215, door de "
                  "adel afgedwongen, legde vast dat ook de koning zich aan afspraken moest houden. Dat is nog "
                  "geen democratie, maar wel een macht die niet meer onbeperkt is."),
            ("p", "Het verschil aan het einde van de middeleeuwen is dus: de <strong>Franse</strong> koning "
                  "regeert steeds meer alleen, de <strong>Engelse</strong> steeds meer samen met een "
                  "parlement. Die twee wegen lopen eeuwen later nog door."),
        ]),
        dict(kop="De Guldensporenslag", blokken=[
            ("p", "Op <strong>11 juli 1302</strong> vond bij Kortrijk de <strong>Guldensporenslag</strong> "
                  "plaats. Tegenover elkaar stonden een <strong>Vlaams leger met veel stedelingen</strong> en "
                  "het <strong>ridderleger van de Franse koning</strong>. De graaf van Vlaanderen was leenman "
                  "van die koning; de steden, met de ambachten voorop, kwamen tegen diens greep in opstand."),
            ("p", "De <strong>gevolgen voor het graafschap Vlaanderen</strong>: de Franse inlijving werd "
                  "voorlopig afgewend, de ambachten kregen meer invloed in de steden, en toch moest Vlaanderen "
                  "later zware betalingen aan Frankrijk doen. Een onafhankelijk koninkrijk werd het niet."),
            ("p", "De slag was <strong>geen taalstrijd</strong> tussen Nederlands en Frans. Het ging over "
                  "macht, geld en zeggenschap in de steden. De taalkant is er pas in de 19de eeuw bij gekomen. "
                  "Qua maatschappelijk domein breng je de Guldensporenslag vooral onder bij het <strong>politieke domein</strong>, met "
                  "het sociale erdoorheen."),
            ("weetje", "11 juli is vandaag de feestdag van de Vlaamse Gemeenschap. Dat een middeleeuwse "
                       "gebeurtenis vandaag nog betekenis krijgt, en dat die betekenis meegroeit met haar "
                       "eigen tijd, hoort bij <strong>beeldvorming</strong>."),
        ]),
        dict(kop="Het Arabische Rijk en de kruistochten", blokken=[
            ("p", "De islam ontstaat vanaf ongeveer <strong>600</strong>; Mohammed leeft van ongeveer 570 tot "
                  "632. Daarna groeit het <strong>Arabische Rijk</strong> bijzonder snel. Op zijn hoogtepunt "
                  "omvat het het <strong>Arabische schiereiland</strong>, <strong>Noord-Afrika</strong> en een "
                  "groot deel van het <strong>Iberisch schiereiland</strong>, tot voorbij Perzië. Scandinavië "
                  "lag er ver buiten."),
            ("p", "De verspreiding verliep in <strong>fasen</strong> die je op een historische kaart kan "
                  "aflezen: eerst het Arabische schiereiland, daarna de snelle veroveringen naar Perzië en "
                  "Noord-Afrika, en ten slotte de verdere uitbreiding onder de kaliefen tot in Spanje."),
            ("p", "De <strong>Arabische cultuur</strong> blonk uit in <strong>wiskunde, sterrenkunde en "
                  "geneeskunde</strong>, in <strong>sierschrift en bouwkunst</strong>, en in het "
                  "<strong>vertalen en bewaren van Griekse geleerdheid</strong>. Stoommachines bouwen hoorde "
                  "daar niet bij."),
            ("p", "De <strong>zijderoutes</strong> zijn de handelswegen die het Westen met China verbonden. "
                  "Het is geen enkele weg maar een net van routes, over land en over zee, en er ging veel meer "
                  "over dan zijde alleen."),
            ("p", "De <strong>motieven</strong> voor de <strong>kruistochten</strong> waren "
                  "<strong>godsdienstig</strong> (de heilige plaatsen in bezit krijgen), "
                  "<strong>economisch</strong> (handel en buit) en <strong>sociaal</strong> (jongere "
                  "adellijke zonen zochten een eigen gebied). Wetenschap was geen motief, al kwam er wel "
                  "kennis mee terug."),
            ("p", "De veroverde kruisvaardersstaten hielden het geen twee eeuwen vol: in 1291 viel Akko, het "
                  "laatste steunpunt. De <strong>gevolgen voor West-Europa</strong> waren wel blijvend: meer "
                  "handel met het oosten via Italiaanse steden, nieuwe producten en kennis die meekwamen, en "
                  "een verharding van de verhouding met moslims en joden. De standensamenleving verdween er "
                  "niet door."),
            ("kader", "De <strong>aard van het interculturele contact</strong> tussen de islam en het Westen "
                      "bestond zowel uit <strong>oorlog</strong> als uit <strong>handel en "
                      "kennisoverdracht</strong>. In Toledo en Palermo werd samen vertaald terwijl er elders "
                      "gevochten werd. Daarom mag je de kruistochten niet enkel vanuit de westerse bronnen "
                      "bekijken: wie schrijft, kiest wat hij vertelt, en de Arabische kronieken geven een "
                      "ander beeld van dezelfde gebeurtenis."),
        ]),
    ],
)

# ───────────────────────── 5. De 'Nieuwe' Wereld en de driehoekshandel
BUNDELS["de-nieuwe-wereld-en-de-driehoekshandel-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De 'Nieuwe' Wereld en de driehoekshandel",
    onder="Ontdekkingsreizen, kolonisatie en slavenhandel, en de commerciële revolutie in Europa zelf.",
    secties=[
        dict(kop="Waarom die reizen?", blokken=[
            ("p", "De <strong>motieven</strong> voor de <strong>ontdekkingsreizen</strong> waren "
                  "<strong>economisch</strong> (een eigen weg naar de specerijen van Azië), "
                  "<strong>godsdienstig</strong> (het christendom verspreiden) en <strong>politiek</strong> "
                  "(aanzien en gebied voor de eigen vorst). Goud, God en glorie, zegt men wel eens; bij bijna "
                  "elke reis lopen die drie door elkaar."),
            ("p", "De Portugezen en Spanjaarden zochten een <strong>zeeweg naar Azië</strong> omdat de "
                  "landroute door gebieden liep waar <strong>tussenhandelaars de prijs bepaalden</strong>. "
                  "Specerijen die via vele handen kwamen, waren in Lissabon peperduur."),
            ("p", "<strong>Technische vernieuwingen</strong> maakten die reizen mogelijk: het "
                  "<strong>kompas</strong> voor de richting, het <strong>astrolabium</strong> en later de "
                  "<strong>jakobsstaf</strong> om op open zee de <strong>breedtegraad</strong> te bepalen door "
                  "de hoogte van zon of ster te meten, en een scheepstype dat tegen de wind in kon laveren. "
                  "Een scheepsmotor bestond nog niet."),
        ]),
        dict(kop="De reizigers en hun routes", blokken=[
            ("p", "<strong>Christoffel Columbus</strong> vaart in <strong>1492</strong> in dienst van Spanje "
                  "de Atlantische Oceaan over en bereikt eilanden in de Caraïben. Hij dacht tot aan Azië te "
                  "zijn gevaren, en hield dat ook vol: bij zijn terugkeer wist hij niet dat hij een voor "
                  "Europa onbekend werelddeel bereikt had. Amerigo Vespucci gaf het later zijn naam."),
            ("p", "<strong>Vasco da Gama</strong> vaart als eerste rond Kaap de Goede Hoop tot in Indië en "
                  "bereikt in 1498 Calicut. De vloot van <strong>Magellaan</strong> vaart als eerste rond de "
                  "wereld. <strong>Cortés</strong> is geen ontdekkingsreiziger maar veroveraar."),
            ("p", "De <strong>eerste kolonisatiegolf</strong> is die van <strong>Portugal en Spanje</strong>, "
                  "vanaf ongeveer 1500. Portugal bouwde vooral een net van <strong>handelsposten langs de "
                  "kusten</strong>, Spanje veroverde grote gebieden in het <strong>binnenland</strong>. "
                  "Portugal wilde de handel beheersen, Spanje het land zelf."),
        ]),
        dict(kop="De gevolgen voor de precolumbiaanse bevolking", blokken=[
            ("p", "De Spanjaarden vernietigden in de 16de eeuw het <strong>Aztekenrijk</strong> in Mexico, "
                  "het <strong>Incarijk</strong> in de Andes en de <strong>Mayasteden</strong> in "
                  "Midden-Amerika. Het Chinese keizerrijk bleef buiten hun bereik."),
            ("p", "De belangrijkste oorzaak van de <strong>demografische inzinking</strong> van de "
                  "<strong>precolumbiaanse bevolking</strong> waren <strong>ziekten waartegen zij geen "
                  "weerstand hadden</strong>, zoals pokken en mazelen. Oorlog en dwangarbeid kwamen daar "
                  "bovenop. Naar schatting stierf het grootste deel van de bevolking binnen een eeuw."),
            ("p", "Het <strong>encomiendasysteem</strong> is het Spaanse systeem waarbij een kolonist "
                  "<strong>arbeid mocht opeisen</strong> van de inheemse bevolking; in ruil moest hij hen "
                  "beschermen en bekeren. In de praktijk was het dwangarbeid in de mijnen en op de velden."),
            ("kader", "De <strong>demografische inzinking</strong>, het <strong>encomiendasysteem</strong> en "
                      "de <strong>Afrikaanse slavenhandel</strong> hangen samen: stierf de inheemse bevolking "
                      "weg, dan viel de gedwongen arbeid weg, en werd die arbeid van elders gehaald, uit "
                      "Afrika."),
        ]),
        dict(kop="De tweede golf en de blijvende sporen", blokken=[
            ("p", "De <strong>tweede kolonisatiegolf</strong> is die van <strong>Engeland</strong>, "
                  "<strong>Frankrijk</strong> en de <strong>Verenigde Provinciën</strong>, vanaf de 17de "
                  "eeuw."),
            ("p", "Vandaag zie je nog aan de <strong>taal</strong> en aan de <strong>plaatsnamen</strong> welk "
                  "land welk gebied koloniseerde: Brazilië spreekt Portugees, de rest van Zuid-Amerika Spaans. "
                  "Ook godsdienst en rechtssysteem dragen dat spoor. De kolonisatie liet de godsdienst van de "
                  "gekoloniseerde volkeren dus niet ongemoeid: missionering hoorde bij het project zelf."),
            ("p", "<strong>Monocultuur</strong> is dat een heel gebied met <strong>één gewas</strong> beplant "
                  "wordt, voor de uitvoer: suikerriet, katoen of tabak zo ver je kijken kan. "
                  "<strong>Roofbouw</strong> betekent dat men de grond of de mijn <strong>uitput</strong> "
                  "zonder aan de toekomst te denken."),
            ("p", "Uit de koloniën kwamen <strong>zilver</strong> uit de Andes, <strong>suiker en "
                  "tabak</strong> uit de Caraïben, en <strong>aardappelen en maïs</strong> uit Amerika. Rijst "
                  "kwam uit Azië. Het zilver veranderde de prijzen in Europa, de aardappel en de maïs het "
                  "voedsel."),
            ("p", "Men schrijft <strong>'Nieuwe' Wereld</strong> met aanhalingstekens omdat die wereld enkel "
                  "nieuw was voor de <strong>Europeanen die er aankwamen</strong>. Er woonden al miljoenen "
                  "mensen met eigen rijken en steden. Kolonisatie draait in de eerste plaats om het "
                  "<strong>politieke domein</strong>, want het gaat over gezag over gebied, al raakt ze "
                  "tegelijk alle maatschappelijke domeinen."),
            ("weetje", "Een <strong>Spaanse kroniek</strong> over de verovering van Mexico geeft niet het "
                       "volledige beeld: ze is geschreven door de winnaar, vaak om zijn eigen optreden te "
                       "verdedigen. Er bestaan ook Azteekse verslagen, en die vertellen het anders."),
        ]),
        dict(kop="De driehoekshandel", blokken=[
            ("p", "De <strong>driehoekshandel</strong> had drie hoekpunten: <strong>Europa</strong>, "
                  "<strong>West-Afrika</strong> en <strong>Amerika</strong>. Op elk been werd winst gemaakt."),
            ("p", tabel(["Been", "Lading"], [
                ["Europa naar Afrika", "wapens, textiel en alcohol"],
                ["Afrika naar Amerika", "tot slaaf gemaakte mensen"],
                ["Amerika naar Europa", "suiker, katoen en tabak"],
            ])),
            ("p", "De oversteek van Afrika naar Amerika heet de <strong>middenpassage</strong>: weken in het "
                  "ruim, vastgeketend. Een groot deel van de mensen overleefde die overtocht niet. De "
                  "specerijen uit Azië kwamen langs een heel andere route."),
            ("p", "De <strong>slavenhandel</strong> werd in Europa lange tijd als een <strong>gewone "
                  "handel</strong> beschouwd. Er werd openlijk in geïnvesteerd, met aandelen en "
                  "verzekeringen. Pas in de 18de eeuw groeit er een beweging die ze wil afschaffen."),
            ("kader", "De driehoekshandel toont hoe het <strong>economische</strong> en het "
                      "<strong>sociale</strong> domein in elkaar grijpen: wat op papier een handelsstroom is, "
                      "gaat over mensen die tot koopwaar gemaakt werden."),
        ]),
        dict(kop="De commerciële revolutie", blokken=[
            ("p", "De <strong>commerciële revolutie</strong> is een grondige verandering van het "
                  "<strong>economische systeem</strong> door handel en geld. Niet plots zoals een opstand, "
                  "maar wel ingrijpend: wie handelt en investeert, wordt belangrijker dan wie grond bezit. "
                  "Handel en geld bestonden al eeuwen; nieuw is dat winst systematisch opnieuw geïnvesteerd "
                  "wordt."),
            ("p", "Kenmerken van het <strong>handelskapitalisme</strong>: <strong>winst wordt opnieuw "
                  "geïnvesteerd</strong> om meer winst te maken, <strong>kapitaal wordt door meerdere mensen "
                  "samengelegd</strong>, en het <strong>risico</strong> van een reis wordt gespreid over vele "
                  "aandeelhouders. De schepen waren meestal van particuliere compagnieën, niet van de vorst."),
            ("p", "Het <strong>mercantilisme</strong> houdt in dat een land <strong>meer moet uitvoeren dan "
                  "invoeren</strong>, om edelmetaal binnen te halen. Daarom beschermde een vorst zijn eigen "
                  "nijverheid met invoerrechten en behield hij de handel met zijn koloniën voor zichzelf. "
                  "Vrije handel met alle landen is dus net niet wat het mercantilisme wil; dat idee komt pas "
                  "met Adam Smith."),
            ("p", "Een <strong>handelscompagnie</strong> is een onderneming waarvan het kapitaal in "
                  "verhandelbare delen verdeeld is; de Verenigde Oost-Indische Compagnie is het bekendste "
                  "voorbeeld. Bij <strong>huisnijverheid</strong> levert een handelaar grondstof aan gezinnen "
                  "die <strong>thuis</strong> het werk uitvoeren. In een <strong>manufactuur</strong> werken "
                  "de arbeiders <strong>samen op één plaats, onder toezicht</strong>, nog altijd met de hand."),
            ("p", "In de vroegmoderne tijd komen ook <strong>wisselbrieven</strong>, <strong>banken</strong> "
                  "en <strong>beurzen</strong> op. De beurs van Antwerpen, en later Amsterdam, maakt handel "
                  "mogelijk zonder dat er een zak munten mee moet reizen."),
            ("p", "Het verband tussen de <strong>ontdekkingsreizen</strong> en het handelskapitalisme: de "
                  "reizen vroegen <strong>veel kapitaal vooraf</strong> en beloofden <strong>grote winst "
                  "achteraf</strong>. Precies daarom legde men geld samen en spreidde men het risico."),
        ]),
        dict(kop="Landbouw en samenleving in de vroegmoderne tijd", blokken=[
            ("p", "Ook in de landbouw komen <strong>technische vernieuwingen</strong>: het "
                  "<strong>vruchtwisselstelsel</strong>, waarbij elk jaar een ander gewas op hetzelfde veld "
                  "staat zodat er geen braakland meer nodig is; <strong>voedergewassen</strong> zoals klaver "
                  "en rapen; en meer <strong>mest</strong> doordat er meer vee op stal staat. Kunstmest komt "
                  "pas in de 19de eeuw."),
            ("p", "Het verband tussen <strong>landbouwproductiviteit</strong> en "
                  "<strong>bevolkingsgroei</strong>: meer voedsel per stuk grond betekent dat er meer mensen "
                  "kunnen leven, en minder hongersnood betekent minder sterfte. De bevolking van Europa groeit "
                  "in de 18de eeuw dan ook sterk."),
            ("p", "De <strong>standensamenleving</strong> verdween in de vroegmoderne tijd niet: de standen "
                  "blijven in de wet bestaan tot de Franse Revolutie. Maar de verhoudingen schuiven wel: de "
                  "<strong>rijke burgerij</strong> wordt machtiger dan haar stand laat vermoeden, sommige "
                  "adellijke families verarmen, en geld begint titels te kopen, door huwelijk of door de "
                  "aankoop van een ambt. De grond bleef grotendeels in handen van adel en Kerk."),
            ("weetje", "Het <strong>zilver uit Amerika</strong> maakte Spanje níét blijvend het sterkste land "
                       "van Europa. Het ging naar oorlogen en naar invoer, de prijzen stegen, en de eigen "
                       "nijverheid kwijnde. De winst bleef uiteindelijk bij de landen die leverden."),
        ]),
    ],
)

# ───────────────────────── 6. Humanisme, Reformatie, renaissance en barok
BUNDELS["humanisme-reformatie-renaissance-en-barok-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Humanisme, Reformatie, renaissance en barok",
    onder="Een nieuwe visie op mens, wereld, geloof en kunst, van Erasmus tot Rubens.",
    secties=[
        dict(kop="Het humanisme", blokken=[
            ("p", "Het <strong>humanisme</strong> ontstond in de rijke <strong>Italiaanse steden</strong>: "
                  "Florence, Venetië en Rome hadden het geld, de handelscontacten en de Romeinse resten om op "
                  "verder te bouwen."),
            ("p", "De <strong>kenmerken</strong>: belangstelling voor de <strong>mens en zijn "
                  "mogelijkheden</strong>, <strong>teruggrijpen naar de Griekse en Romeinse oudheid</strong>, "
                  "en <strong>kritisch onderzoek van de oorspronkelijke teksten</strong>. De meeste "
                  "humanisten bleven gelovig; Erasmus was priester. Ze wilden het geloof zuiveren, niet "
                  "afschaffen."),
            ("p", "<strong>Erasmus</strong> van Rotterdam schreef <em>Lof der Zotheid</em>, waarin hij de "
                  "misbruiken in Kerk en samenleving bespotte en voor onderwijs en verdraagzaamheid pleitte."),
            ("p", "De <strong>boekdrukkunst</strong> hielp de ideeën van de humanisten snel verspreiden. Wat "
                  "vroeger één monnik in maanden overschreef, rolde nu bij honderden van de pers."),
        ]),
        dict(kop="Een nieuwe wetenschappelijke methode", blokken=[
            ("p", "Aan de <strong>wetenschappelijke methode</strong> verandert dat men <strong>zelf ging "
                  "waarnemen en proeven doen</strong> in plaats van enkel oude gezaghebbende teksten te "
                  "geloven."),
            ("p", "<strong>Vesalius</strong> ontleedde zelf lichamen en toonde aan dat de oude Griekse "
                  "geneeskundige teksten, zoals die van Galenus, <strong>niet in alles gelijk</strong> "
                  "hadden. Zijn boek uit 1543 staat vol tekeningen naar eigen waarneming. Dat je dat mág "
                  "vaststellen, is het echte nieuwe."),
            ("p", "De westerse geneeskunde was ondertussen sterk beïnvloed door het contact met de "
                  "<strong>Arabische wereld</strong>: Arabische handboeken zoals die van <strong>Ibn "
                  "Sina</strong> werden eeuwenlang aan de universiteiten gebruikt, <strong>Griekse "
                  "geneeskundige teksten</strong> kwamen via Arabische vertalingen terug, en kennis over "
                  "<strong>geneesmiddelen en ziekenzorg</strong> kwam mee. De microscoop kwam niet uit Bagdad "
                  "maar uit de Nederlanden, in de 17de eeuw."),
        ]),
        dict(kop="De Reformatie", blokken=[
            ("p", "De <strong>oorzaken van de Reformatie</strong>: <strong>misbruiken in de Kerk</strong> "
                  "zoals de aflaathandel, de <strong>rijkdom en het wereldse leven van hoge "
                  "geestelijken</strong>, en de <strong>kritische lezing van de Bijbel door humanisten</strong>. "
                  "Kerkbezoek werd nergens verboden."),
            ("p", "Een <strong>aflaat</strong> is een kwijtschelding van straf voor zonden, die men ook kon "
                  "<strong>kopen</strong>. Het geld diende onder meer voor de bouw van de "
                  "Sint-Pietersbasiliek. In <strong>1517</strong> hing de monnik <strong>Luther</strong> in "
                  "Wittenberg zijn vijfennegentig stellingen tegen die aflaathandel op. Hij wilde een "
                  "discussie, geen scheuring."),
            ("p", "<strong>Luther</strong> leerde dat een mens gered wordt <strong>door het geloof "
                  "alleen</strong>, en door de <strong>Bijbel als enige bron</strong>: <em>sola fide</em> en "
                  "<em>sola scriptura</em>. Dat zet de bemiddelende rol van de Kerk en haar priesters meteen "
                  "op de helling."),
            ("p", "Het <strong>anglicanisme</strong> ontstond niet uit een geloofsdiscussie maar uit een "
                  "<strong>politieke breuk</strong>: Hendrik VIII wilde scheiden, de paus weigerde, en hij "
                  "maakte zichzelf hoofd van de Engelse Kerk."),
            ("p", "Het <strong>calvinisme</strong> kenmerkt zich door de <strong>predestinatie</strong> (God "
                  "heeft vooraf bepaald wie gered wordt), een <strong>sobere eredienst zonder beelden</strong>, "
                  "en een kerk die door <strong>gekozen ouderlingen</strong> bestuurd wordt. De paus erkennen "
                  "ze niet."),
            ("p", "Het <strong>protestantisme</strong> sloeg het sterkst aan in <strong>Noord-Europa</strong>: "
                  "de Duitse vorstendommen, Scandinavië, Engeland en Schotland. Vorsten die zich van Rome "
                  "losmaakten, konden ook de kerkelijke goederen in beslag nemen."),
            ("kader", "Het <strong>humanisme</strong> is een voorwaarde voor de Reformatie: humanisten lazen "
                      "de Bijbel in de <strong>oorspronkelijke taal</strong> en zagen dat de vertaling niet "
                      "overal klopte. Erasmus legde het ei, zei men, en Luther broedde het uit. De Reformatie "
                      "zelf hoort qua maatschappelijk domein in de eerste plaats bij het <strong>culturele domein</strong>, al zette ze "
                      "vorstendommen tegen elkaar op."),
        ]),
        dict(kop="De Contrareformatie", blokken=[
            ("p", "De <strong>Contrareformatie</strong> bestond niet enkel uit vervolging. Er waren ook "
                  "hervormingen van binnenuit. De <strong>maatregelen</strong>: het <strong>Concilie van "
                  "Trente</strong> legde de katholieke leer opnieuw vast, <strong>seminaries</strong> leidden "
                  "priesters beter op, en een <strong>index van verboden boeken</strong> bewaakte wat men "
                  "las. De mis werd niet afgeschaft maar juist bevestigd en plechtiger gemaakt."),
            ("p", "Het concilie van <strong>Trente</strong> vergaderde met tussenpozen van 1545 tot 1563. Wat "
                  "daar beslist werd, bleef vierhonderd jaar lang gelden. Nieuwe orden zoals de "
                  "<strong>jezuïeten</strong> richtten scholen op."),
            ("p", "De godsdienstige breuk van de 16de eeuw had ook <strong>politieke gevolgen</strong>: "
                  "godsdienstoorlogen in Frankrijk, de Dertigjarige Oorlog in Duitsland, de Opstand in de "
                  "Nederlanden."),
        ]),
        dict(kop="De renaissance", blokken=[
            ("p", "De <strong>renaissance</strong> ontleent haar naam aan de <strong>wedergeboorte van de "
                  "klassieke oudheid</strong>. Kunstenaars en geleerden namen de Grieken en Romeinen opnieuw "
                  "als voorbeeld, in vormen, verhoudingen en onderwerpen."),
            ("p", "<strong>Kenmerken van de renaissancekunst</strong>: <strong>evenwicht, rust en heldere "
                  "verhoudingen</strong>, het <strong>perspectief</strong> waardoor diepte ontstaat, en het "
                  "<strong>menselijk lichaam naar de natuur bestudeerd</strong>. Het perspectief laat toe om "
                  "op een plat vlak de indruk van diepte te wekken: lijnen lopen naar één verdwijnpunt, en "
                  "dingen worden kleiner naarmate ze verder staan."),
            ("p", "De <strong>David van Michelangelo</strong> behoort tot de renaissance omdat het "
                  "<strong>naakte lichaam naar de natuur bestudeerd</strong> is, in <strong>rustige klassieke "
                  "verhoudingen</strong>. Het is marmer, geen brons, en er is geen aureool te bekennen: de "
                  "mens zelf is het onderwerp. Michelangelo schilderde ook het plafond van de "
                  "<strong>Sixtijnse Kapel</strong>."),
            ("p", "Andere kunstenaars van de Italiaanse renaissance zijn <strong>Leonardo da Vinci</strong> "
                  "en <strong>Rafaël</strong>. Rubens hoort er niet bij; die is een barokschilder van een "
                  "eeuw later."),
            ("p", "Renaissancekunstenaars kozen niet enkel godsdienstige onderwerpen: ze schilderden ook "
                  "<strong>portretten</strong>, verhalen uit de oudheid en stadsgezichten. Zo stond de kunst "
                  "in dienst van een nieuw <strong>mens- en wereldbeeld</strong>: ze zette de mens zelf in "
                  "het midden, met zijn eigen gelaat en zijn eigen kunnen."),
            ("p", "Het grootste verschil met de <strong>middeleeuwse kunst</strong>: de renaissance toont de "
                  "wereld <strong>zoals het oog ze ziet</strong>, de middeleeuwen <strong>zoals de betekenis "
                  "ze ordent</strong>. Op een middeleeuws paneel is de belangrijkste figuur het grootst, hoe "
                  "ver hij ook staat."),
            ("p", "De <strong>Vlaamse primitieven</strong> schilderden anders dan de Italianen: zij werkten "
                  "met <strong>olieverf</strong> en gingen vooral voor het <strong>detail</strong>, de "
                  "Italianen meer voor de <strong>klassieke verhoudingen</strong>. Twee wegen naar de natuur "
                  "toe."),
        ]),
        dict(kop="De barok", blokken=[
            ("p", "<strong>Kenmerkend voor de barokkunst</strong>: <strong>beweging, drama en sterke "
                  "licht-donkercontrasten</strong>, <strong>weelderige versiering en rijke kleuren</strong>, "
                  "en grote, <strong>meeslepende taferelen</strong> die de kijker willen raken. Kale kerken "
                  "zonder beelden horen bij het calvinisme."),
            ("p", "De barok staat niet los van de godsdienstige strijd van haar tijd: ze is grotendeels de "
                  "kunst van de <strong>Contrareformatie</strong>. Waar de protestanten beelden weghaalden, "
                  "zette de katholieke Kerk er nog grotere bij. <strong>Rubens</strong> uit Antwerpen is de "
                  "bekendste vertegenwoordiger bij ons; hij leidde een werkplaats met tientallen medewerkers "
                  "en werkte ook als diplomaat."),
            ("p", "Vorsten gebruikten de barokkunst om hun <strong>macht en aanzien</strong> te tonen, om hun "
                  "<strong>paleizen en tuinen</strong> indruk te laten maken, en om zichzelf in grote "
                  "<strong>portretten</strong> te laten vereeuwigen. Soberheid was wel het laatste wat "
                  "Versailles uitstraalde: kunst in dienst van geloof én macht."),
            ("p", "<strong>Barokbouwkunst</strong> herken je aan <strong>gebogen gevels, zuilen en veel "
                  "beeldhouwwerk</strong>. Het verschil tussen renaissance en barok zie je aan <strong>rust "
                  "tegenover beweging</strong>: zet de David naast een beeld van Bernini."),
            ("p", "Renaissance en barok volgen elkaar op, met bijna een eeuw ertussen: de renaissance bloeit "
                  "rond 1500, de barok vanaf ongeveer 1600. Daartussen liggen de Reformatie en de "
                  "godsdienstoorlogen."),
            ("kader", "Een <strong>kunstwerk is ook een historische bron</strong>. Vraag je bij een schilderij "
                      "af <strong>wie het betaalde en waarom</strong>, <strong>voor welke plaats en welk "
                      "publiek</strong> het gemaakt is, en <strong>wat er bewust wel en niet op staat</strong>. "
                      "De prijs van de verf brengt je niet ver."),
            ("p", "Men noemt de <strong>vroegmoderne tijd</strong> een breuk met de middeleeuwen omdat "
                  "mens- en wereldbeeld, geloof, wetenschap en kunst <strong>alle vier tegelijk</strong> "
                  "veranderen. Toch blijft veel doorlopen: de standen, de landbouw, de macht van de vorsten."),
        ]),
    ],
)

# ───────────────────────── 7. Vorsten, opstand en de Verlichting
BUNDELS["vorsten-opstand-en-de-verlichting-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Vorsten, opstand en de Verlichting",
    onder="Tussen absolute en parlementaire monarchie, de Opstand in de Nederlanden, en de ideeën die de grondwet dragen.",
    secties=[
        dict(kop="Het vorstelijk absolutisme in Frankrijk", blokken=[
            ("p", "<strong>Kenmerken van het vorstelijk absolutisme</strong>: <strong>alle macht ligt bij de "
                  "koning</strong>, die aan niemand verantwoording schuldig is; hij <strong>stelt zijn "
                  "ministers zelf aan en zet ze zelf af</strong>; en de <strong>standenvergadering wordt niet "
                  "meer bijeengeroepen</strong>. Verkozen worden hoort bij een republiek."),
            ("p", "De koning steunde zijn macht op het <strong>droit divin</strong>: zijn macht komt "
                  "rechtstreeks van God. Wie zich tegen de koning verzet, verzet zich dan tegen God zelf. "
                  "Godsdienst staat hier dus in dienst van de vorst."),
            ("p", "<strong>Lodewijk XIV</strong>, de <strong>Zonnekoning</strong>, regeerde tweeënzeventig "
                  "jaar en bouwde <strong>Versailles</strong>. Hij gebruikte dat hof om de <strong>adel aan "
                  "het hof te binden</strong> en zo onschadelijk te maken, om zijn macht in <strong>kunst en "
                  "ceremonie</strong> zichtbaar te maken, en om het <strong>bestuur onder zijn eigen "
                  "oog</strong> te houden. De Staten-Generaal riep hij niet meer samen."),
            ("p", "Op lange termijn werd die absolute macht <strong>ondermijnd</strong> door "
                  "<strong>oorlogen en geldgebrek</strong>. Oorlogen en hofhouding kostten enorm veel, en de "
                  "belasting drukte op wie ze het minst kon dragen."),
        ]),
        dict(kop="De parlementaire monarchie in Engeland", blokken=[
            ("p", "Een <strong>constitutionele parlementaire monarchie</strong> is een koningschap dat aan "
                  "een <strong>grondwet gebonden</strong> is, met een <strong>parlement dat mee "
                  "beslist</strong>. De koning blijft, maar hij regeert binnen regels die hij niet zelf kan "
                  "veranderen."),
            ("p", "De <strong>oorzaken van de Glorious Revolution</strong>: de koning wilde <strong>zonder "
                  "het parlement regeren</strong>, hij was <strong>katholiek in een overwegend protestants "
                  "land</strong>, en het <strong>parlement vreesde voor zijn eigen bestaan</strong>. In "
                  "<strong>1688</strong> verliep de omwenteling zonder grote veldslag in Engeland: Jacobus II "
                  "vluchtte, en Willem III werd uit de Nederlanden gehaald."),
            ("p", "De <strong>Bill of Rights</strong> van 1689 legde vast dat de koning <strong>geen wetten "
                  "mag opheffen of belastingen heffen zonder het parlement</strong>. Daarmee is de macht van "
                  "de vorst voor het eerst in een tekst begrensd."),
            ("kader", "Het grote verschil tussen de <strong>Franse</strong> en de <strong>Engelse</strong> weg "
                      "in de 17de eeuw: in Frankrijk wint de vorst het van het parlement, in Engeland het "
                      "parlement van de vorst. Dezelfde eeuw, twee tegengestelde antwoorden."),
        ]),
        dict(kop="De Nederlanden: eenheid en scheiding", blokken=[
            ("p", "<strong>Karel V</strong> en <strong>Filips II</strong> probeerden het bestuur van de "
                  "Nederlanden te <strong>centraliseren</strong>, stelden <strong>nieuwe bisdommen</strong> "
                  "in en traden <strong>hard op tegen het protestantisme</strong>. Meer privileges gaven ze "
                  "de steden niet; ze knabbelden er net aan."),
            ("p", "<strong>Centralisatie</strong> betekent dat het bestuur <strong>vanuit één punt</strong> "
                  "geregeld wordt, in plaats van door elk gewest apart. Voor de vorst is dat doelmatig; voor "
                  "een stad met een eigen keure voelt het als diefstal van haar rechten."),
            ("p", "De <strong>oorzaken van de Opstand</strong>: de centralisatie tastte de oude "
                  "<strong>privileges</strong> aan, er was de <strong>vervolging van protestanten</strong>, "
                  "en er waren <strong>zware belastingen</strong> zoals de tiende penning."),
            ("p", "In <strong>1566</strong> vernielden beeldenstormers de beelden in de kerken: de "
                  "<strong>Beeldenstorm</strong>. Hij begon in Steenvoorde en trok in enkele weken over de "
                  "Nederlanden. Voor Filips II was het het bewijs dat hard optreden nodig was; hij stuurde de "
                  "<strong>hertog van Alva</strong> met zijn Raad van Beroerten."),
            ("p", "Alva staat verschillend beschreven in een Spaanse en in een Nederlandse bron omdat "
                  "<strong>elke auteur schrijft vanuit zijn eigen kant van het conflict</strong>. Voor de ene "
                  "redt hij de orde en het geloof, voor de andere is hij de bloedhertog. Twee bronnen die "
                  "elkaar tegenspreken, betekent niet dat er zeker één liegt: ze kunnen allebei eerlijk zijn "
                  "en toch iets anders belangrijk vinden."),
            ("p", "In <strong>1581</strong> zworen de gewesten Filips II als vorst af met het <strong>Plakkaat "
                  "van Verlatinghe</strong>. Het redeneert dat een vorst die zijn onderdanen als een tiran "
                  "behandelt, zijn recht verspeelt: een idee dat bij de Verlichting terugkomt."),
            ("p", "De oorlog met Spanje duurde <strong>tachtig jaar</strong>, van 1568 tot 1648, met een "
                  "bestand van twaalf jaar ertussen. De <strong>Vrede van Münster</strong> in 1648 erkende de "
                  "onafhankelijkheid van de <strong>Noordelijke Nederlanden</strong>."),
            ("p", "De <strong>gevolgen voor de Zuidelijke Nederlanden</strong>: de <strong>Schelde werd "
                  "gesloten</strong>, wat Antwerpen zwaar trof; veel <strong>kooplui en geleerden trokken "
                  "naar het noorden</strong>; en het gebied bleef <strong>katholiek en onder Spaans "
                  "bestuur</strong>, later Oostenrijks. Een republiek werd juist het noorden."),
        ]),
        dict(kop="De Verlichting en haar filosofen", blokken=[
            ("p", "De <strong>Verlichting</strong> is een stroming die het <strong>verstand</strong> als "
                  "leidraad neemt voor kennis en samenleving. Het licht in de naam is dat van de rede "
                  "tegenover de duisternis van vooroordeel en willekeur. Ze ontstond vooral in de "
                  "<strong>18de eeuw</strong>, met <strong>Frankrijk en Engeland</strong> als zwaartepunten; "
                  "salons, koffiehuizen en de Encyclopédie verspreidden de ideeën."),
            ("p", tabel(["Filosoof", "Zijn idee"], [
                ["John Locke", "natuurlijke rechten op leven, vrijheid en bezit; kennis komt uit de ervaring"],
                ["Voltaire", "godsdienstige verdraagzaamheid en vrije meningsuiting"],
                ["Charles de Montesquieu", "de scheiding der machten"],
                ["Jean-Jacques Rousseau", "de volkssoevereiniteit: de macht gaat uit van het volk"],
                ["Immanuel Kant", "durf zelf te denken"],
            ])),
            ("p", "<strong>Montesquieu</strong> splitst in <em>De l'esprit des lois</em> de wetgevende, de "
                  "uitvoerende en de rechterlijke macht, zodat de ene de andere kan tegenhouden. De "
                  "<strong>scheiding der machten</strong> betekent dus níét dat de regering de rechtbanken "
                  "leidt, maar net het omgekeerde."),
            ("p", "<strong>Rousseau</strong> laat in <em>Du contrat social</em> burgers onderling een verdrag "
                  "sluiten: het gezag is van hen, niet van een vorst bij Gods gratie. <strong>Locke</strong> "
                  "zegt dat een bestuur dat de natuurlijke rechten schendt, afgezet mag worden; het "
                  "<strong>droit divin</strong> verwerpt hij. <strong>Kant</strong> vat alles samen in "
                  "<em>durf zelf te denken</em>, <em>sapere aude</em>."),
            ("p", "Verlichte denkers wilden de koning niet altijd afschaffen: velen hoopten juist op een "
                  "<strong>verlicht vorst</strong> die van bovenaf hervormde, zoals Jozef II."),
        ]),
        dict(kop="De verlichte politieke en wetenschappelijke ideeën", blokken=[
            ("p", "<strong>Rechtsgelijkheid</strong> betekent dat dezelfde wet voor iedereen geldt, "
                  "<strong>ongeacht stand of geboorte</strong>. Dat botst frontaal met de standensamenleving. "
                  "<strong>Rechtszekerheid</strong> betekent dat je <strong>vooraf kan weten wat verboden is "
                  "en welke straf erop staat</strong>; willekeur is het tegendeel."),
            ("p", "Een <strong>grondwet</strong> is de tekst waarin de grondregels en de macht van een staat "
                  "vastgelegd zijn. Ze staat boven de gewone wetten. Het <strong>weerstandsrecht</strong> is "
                  "het recht om je te <strong>verzetten tegen een bestuur dat je rechten schendt</strong>."),
            ("p", "Bij de wetenschappelijke ideeën horen het <strong>empirisme</strong>, dat van de "
                  "<strong>waarneming</strong> vertrekt, en het <strong>rationalisme</strong>, dat van het "
                  "<strong>redeneren</strong> vertrekt. Allebei verwerpen ze het argument van het gezag "
                  "alleen. Het <strong>vooruitgangsoptimisme</strong> is het geloof dat kennis en rede de "
                  "samenleving beter kunnen maken."),
        ]),
        dict(kop="Die ideeën vandaag", blokken=[
            ("p", "In de <strong>Belgische grondwet</strong> herken je de <strong>scheiding der "
                  "machten</strong>, de <strong>gelijkheid van alle Belgen voor de wet</strong>, en de "
                  "<strong>vrijheid van godsdienst en van meningsuiting</strong>. Erfelijke voorrechten van "
                  "de adel zijn juist afgeschaft. De grondwet van 1831 gold in haar tijd als een van de meest "
                  "verlichte van Europa."),
            ("p", "De macht gaat volgens die grondwet <strong>uit van de natie</strong>, in artikel 33: de "
                  "volkssoevereiniteit van Rousseau. De koning heeft enkel de bevoegdheden die de grondwet "
                  "hem geeft."),
            ("p", "In België wordt beslist op het niveau van de <strong>gemeente</strong>, van de "
                  "<strong>gemeenschappen en de gewesten</strong>, op het <strong>federale</strong> en op het "
                  "<strong>Europese</strong> niveau. Een provincieraad van Europa bestaat niet."),
            ("p", "Zelf <strong>verantwoordelijkheid opnemen</strong> binnen die rechtsstaat kan door "
                  "<strong>te gaan stemmen</strong> en je te informeren, door een <strong>petitie te "
                  "ondertekenen</strong> of naar een inspraakmoment te gaan, en door je aan te sluiten bij een "
                  "<strong>vereniging of een jeugdraad</strong>."),
            ("kader", "De Verlichting is een <strong>keerpunt in het politieke domein</strong> omdat de bron "
                      "van het gezag verschuift van <strong>God naar het volk</strong>. Wie zegt dat de macht "
                      "van het volk komt, zegt ook dat ze teruggenomen kan worden."),
        ]),
    ],
)

# ───────────────────────── 8. Amerika, Frankrijk en de industriële omwenteling
BUNDELS["amerika-frankrijk-en-de-industriele-omwenteling-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Amerika, Frankrijk en de industriële omwenteling",
    onder="Twee politieke revoluties en één economische, en wat ze bij ons hebben nagelaten.",
    secties=[
        dict(kop="De Amerikaanse Revolutie", blokken=[
            ("p", "De <strong>oorzaken van de Amerikaanse Revolutie</strong>: <strong>belastingen zonder "
                  "vertegenwoordiging</strong> in het Londense parlement, het feit dat <strong>Londen bepaalde "
                  "met wie de kolonies mochten handelen</strong>, en de <strong>verlichte ideeën</strong> over "
                  "vrijheid en natuurlijke rechten. Van een hongersnood was geen sprake."),
            ("p", "De leuze <em>no taxation without representation</em> betekent: <strong>wie geen "
                  "vertegenwoordigers in het parlement heeft, mag er ook niet belast worden</strong>. De "
                  "kolonisten betwistten niet de belasting zelf, maar wie ze mocht opleggen. Dat is een "
                  "politieke vraag."),
            ("p", "De <strong>Onafhankelijkheidsverklaring</strong> werd op 4 juli <strong>1776</strong> in "
                  "Philadelphia ondertekend. Ze steunt op de gedachte dat <strong>alle mensen met gelijke "
                  "rechten geboren worden</strong>: leven, vrijheid en het streven naar geluk. Dat de "
                  "slavernij tegelijk bleef bestaan, maakt de spanning in die tekst meteen zichtbaar."),
            ("p", "<strong>Politieke kenmerken van de Amerikaanse staat</strong>: een <strong>republiek met "
                  "een verkozen president</strong>, een <strong>federale staat</strong> met bevoegdheden bij "
                  "de staten én bij de unie, en een <strong>grondwet met een strikte scheiding der "
                  "machten</strong>. Een erfelijke koning is er juist niet."),
            ("p", "Die grondwet gaf niet meteen aan iedereen <strong>stemrecht</strong>: vrouwen, tot slaaf "
                  "gemaakte mensen en inheemse volkeren bleven uitgesloten, en in veel staten moest je bezit "
                  "hebben."),
        ]),
        dict(kop="De Franse Revolutie", blokken=[
            ("p", "De <strong>oorzaken van de Franse Revolutie</strong>: de <strong>staatskas was leeg</strong> "
                  "na dure oorlogen, de <strong>derde stand betaalde de belastingen en had niets te "
                  "zeggen</strong>, en <strong>misoogsten</strong> deden de broodprijs stijgen. Bezet was "
                  "Frankrijk niet."),
            ("p", "De <strong>aanleiding</strong>: de koning riep de <strong>Staten-Generaal</strong> samen "
                  "om geld, en die liep uit de hand. De derde stand eiste stemming per hoofd in plaats van "
                  "per stand en verklaarde zich tot Nationale Vergadering. Op <strong>14 juli 1789</strong> "
                  "werd de <strong>Bastille</strong> bestormd: er zaten nauwelijks gevangenen, maar het "
                  "gebouw stond voor de willekeur van de koning."),
            ("p", "De <strong>Verklaring van de Rechten van de Mens en de Burger</strong> van 1789 zegt dat "
                  "<strong>mensen vrij en gelijk in rechten geboren worden</strong>, dat de "
                  "<strong>soevereiniteit bij de natie</strong> berust, en waarborgt de <strong>vrijheid van "
                  "mening en van godsdienst</strong>. De voorrechten van de adel werden in de nacht van "
                  "4 augustus juist afgeschaft. Je brengt die verklaring onder bij het <strong>politieke "
                  "domein</strong>."),
            ("p", "Ze gaf <strong>geen</strong> gelijke politieke rechten aan vrouwen. Olympe de Gouges "
                  "schreef daarom in 1791 een eigen verklaring voor de rechten van de vrouw; ze werd twee "
                  "jaar later onthoofd."),
            ("p", "De <strong>fasen</strong> van de revolutie: eerst een <strong>grondwettelijke "
                  "monarchie</strong>, daarna een <strong>republiek met de Terreur</strong>, ten slotte het "
                  "<strong>Directoire</strong> en de machtsovername van <strong>Napoleon</strong>. Een "
                  "terugkeer naar het absolutisme van voor 1789 kwam er nooit."),
            ("p", "Tijdens de <strong>Terreur</strong> werden duizenden mensen zonder behoorlijk proces "
                  "terechtgesteld. Een revolutie die rechtszekerheid op haar vaandel schreef, schond ze in "
                  "die maanden zelf; Robespierre eindigde onder dezelfde guillotine."),
            ("p", "Het grootste verschil tussen de <strong>samenleving voor en na</strong>: de "
                  "<strong>standen met hun voorrechten</strong> maken plaats voor <strong>burgers die gelijk "
                  "zijn voor de wet</strong>. Ongelijkheid verdwijnt daarmee niet, maar ze staat niet langer "
                  "in de wet."),
        ]),
        dict(kop="Wat de twee revoluties delen, en wat ze nalieten", blokken=[
            ("p", "De <strong>gemeenschappelijke politieke oorzaken</strong> van de Amerikaanse en de Franse "
                  "Revolutie: allebei beroepen ze zich op <strong>verlichte ideeën</strong>, allebei "
                  "verwerpen ze een <strong>gezag waarin de bevolking niet vertegenwoordigd is</strong>, en "
                  "allebei leggen ze <strong>rechten vast in een geschreven tekst</strong>. Een keizer komt "
                  "er enkel in Frankrijk, en pas achteraf."),
            ("p", "De Amerikaanse Revolutie had wel degelijk invloed op Frankrijk: Franse officieren, onder "
                  "wie <strong>Lafayette</strong>, vochten mee in Amerika en kwamen terug met de ideeën én "
                  "met het bewijs dat het kon."),
            ("p", "Het <strong>Franse bestuur in de Zuidelijke Nederlanden</strong> liet blijvende sporen na: "
                  "de <strong>burgerlijke stand</strong>, waar geboorte en huwelijk geregistreerd worden; een "
                  "<strong>wetboek</strong> dat aan de basis ligt van ons burgerlijk recht; en het "
                  "<strong>metriek stelsel</strong>, met meter en kilogram. Het Nederlands werd juist géén "
                  "bestuurstaal: dat werd het Frans."),
            ("p", "Ook op <strong>cultureel vlak</strong> zijn die sporen vandaag niet uitgewist: kerkelijke "
                  "goederen werden verkocht, kloosters opgeheven, begraafplaatsen buiten de dorpskern gelegd. "
                  "Ook je familienaam staat sinds die tijd vast."),
            ("kader", "Men noemt <strong>1789</strong> een breuk omdat de <strong>bron van het gezag</strong> "
                      "en de <strong>grondslag van de samenleving</strong> allebei veranderen. Toch blijft er "
                      "veel doorlopen: dezelfde dorpen, dezelfde landbouw, dezelfde armoede."),
        ]),
        dict(kop="Naar een industriële samenleving", blokken=[
            ("p", "De <strong>industriële revolutie</strong> begon in <strong>Groot-Brittannië</strong>, "
                  "vanaf ongeveer 1750. <strong>België</strong> volgde als een van de eerste landen op het "
                  "vasteland, rond Luik, Charleroi en Gent; Cockerill bouwde in Seraing een bedrijf dat zijn "
                  "eigen machines maakte."),
            ("p", "<strong>Technische vernieuwingen</strong>: de <strong>stoommachine</strong>, "
                  "<strong>machines om te spinnen en te weven</strong>, en het gebruik van "
                  "<strong>cokes</strong> in plaats van houtskool bij het ijzer. De verbrandingsmotor komt "
                  "pas veel later. De stoommachine zet <strong>warmte om in beweging</strong>; Newcomen "
                  "bouwde er een om water uit mijnen te pompen, Watt maakte ze veel zuiniger."),
            ("p", "<strong>Steenkool</strong> was de brandstof waarop alles draaide: ze stookte de "
                  "stoomketels en maakte, als cokes, beter ijzer. Ook het <strong>vervoer</strong> veranderde "
                  "grondig: eerst kanalen en verharde wegen, daarna de spoorweg en het stoomschip."),
            ("p", "<strong>Organisatorische vernieuwingen</strong>: het werk wordt <strong>opgesplitst in "
                  "kleine, vaste handelingen</strong>, arbeiders werken <strong>samen in een fabriek</strong> "
                  "in plaats van thuis, en er wordt op <strong>vaste uren</strong> gewerkt, op het ritme van "
                  "de machine. Dat één arbeider een product van begin tot eind maakt, is juist wat verdwijnt."),
            ("p", "Het verschil tussen een <strong>manufactuur</strong> en een <strong>fabriek</strong>: in "
                  "een fabriek doen <strong>machines</strong> het zware werk, in een manufactuur "
                  "<strong>handen</strong>. Samen werken op één plaats deed men al in de manufactuur; nieuw is "
                  "de aandrijving, eerst water en daarna stoom."),
            ("kader", "De industriële revolutie betekende voor het <strong>arbeidsproces</strong> zowel "
                      "<strong>evolutie</strong> als <strong>revolutie</strong>: de technieken groeiden "
                      "geleidelijk, maar de manier van werken veranderde ingrijpend. En men spreekt van een "
                      "revolutie omdat de <strong>gevolgen zo diep ingrijpen</strong> dat de samenleving er "
                      "een andere van wordt, niet omdat het snel ging. Het is dan ook geen gebeurtenis met "
                      "een vaste begin- en einddatum maar een proces van meer dan een eeuw."),
        ]),
        dict(kop="Aanbod, vraag en gevolgen", blokken=[
            ("p", "Een <strong>aanbodfactor</strong> is iets dat de <strong>productie</strong> mogelijk "
                  "maakt: grondstoffen, kapitaal of arbeidskrachten. De <strong>vraagkant</strong> gaat over "
                  "wie het koopt. Je hebt beide nodig."),
            ("p", "De <strong>aanbodfactoren</strong> van Groot-Brittannië: <strong>steenkool en "
                  "ijzererts</strong> in eigen bodem, <strong>kapitaal</strong> uit handel en koloniën, en "
                  "<strong>arbeidskrachten</strong> die door landbouwvernieuwing vrijkwamen. Ondernemen was er "
                  "bovendien makkelijker dan elders."),
            ("p", "De <strong>vraagfactor</strong>: een <strong>groeiende bevolking</strong> thuis en een "
                  "<strong>groot koloniaal afzetgebied</strong>. Wie massaal produceert, moet massaal "
                  "verkopen."),
            ("p", "De <strong>enclosures</strong> zijn de omheinde velden die in Engeland de gemene gronden "
                  "vervingen. Ze maakten de landbouw productiever maar duwden kleine boeren van het land; "
                  "velen belandden zo in de fabrieken. Dat is meteen het verband tussen de "
                  "<strong>landbouwvernieuwing</strong> en de fabrieken: <strong>minder handen op het "
                  "land</strong> betekent meer handen voor de fabriek."),
            ("p", "De <strong>sociale gevolgen</strong>: de <strong>steden groeiden snel</strong> en werden "
                  "overbevolkt, er ontstond een nieuwe groep <strong>fabrieksarbeiders</strong>, en "
                  "<strong>kinderarbeid</strong> en werkdagen van meer dan twaalf uur waren gewoon. De "
                  "sociale ongelijkheid verdween niet; ze kreeg een nieuwe vorm. Daarom is dit ook een "
                  "verandering in het <strong>sociale domein</strong>: er ontstaan <strong>twee nieuwe "
                  "groepen</strong>, fabriekseigenaars en loonarbeiders."),
            ("p", "Om die aanbod- en vraagfactoren te onderzoeken, gebruik je <strong>cijfers</strong> over "
                  "steenkoolproductie en bevolkingsgroei, <strong>kaarten</strong> met kolenvelden, kanalen "
                  "en spoorlijnen, en <strong>verslagen van onderzoekscommissies</strong> over de "
                  "arbeidsomstandigheden. Een hedendaagse roman is geen bron over die tijd zelf."),
            ("weetje", "De drie revoluties van deze periode raken elk een ander maatschappelijk domein: de Amerikaanse en de "
                       "Franse het <strong>politieke</strong>, de industriële het "
                       "<strong>economische</strong> en het <strong>sociale</strong>. Ze werken wel op elkaar "
                       "in."),
        ]),
    ],
)

# ───────────────────────── 9. Het Ottomaanse Rijk en samenlevingen vergelijken
BUNDELS["het-ottomaanse-rijk-en-samenlevingen-vergelijken-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het Ottomaanse Rijk en samenlevingen vergelijken",
    onder="Een niet-westers wereldrijk in dezelfde eeuw als Karel V, en de vaste punten waarop je samenlevingen naast elkaar legt.",
    secties=[
        dict(kop="Een rijk op drie werelddelen", blokken=[
            ("p", "Het zwaartepunt van het <strong>Ottomaanse Rijk</strong> lag rond de <strong>oostelijke "
                  "Middellandse Zee</strong>, met <strong>Constantinopel</strong> als hoofdstad. Van daaruit "
                  "reikte het over de Balkan, Anatolië, het Nabije Oosten en Noord-Afrika: een rijk op drie "
                  "werelddelen tegelijk."),
            ("p", "In <strong>1453</strong> veroverden de Ottomanen Constantinopel. Daarmee eindigt het "
                  "Byzantijnse Rijk, en veel historici nemen dat jaar als een van de grenzen tussen "
                  "middeleeuwen en vroegmoderne tijd."),
            ("p", "De heerser heette de <strong>sultan</strong>. Hij was ook <strong>kalief</strong>, dus "
                  "<strong>wereldlijk en godsdienstig hoofd tegelijk</strong>. Bij Lodewijk XIV was dat "
                  "anders: die stelde de godsdienst in dienst van zijn macht, maar het hoofd van de Kerk was "
                  "de paus."),
            ("p", "Wat het <strong>absolutisme van de sultan</strong> en dat van <strong>Lodewijk XIV</strong> "
                  "gemeen hebben: <strong>alle macht ligt bij één persoon</strong>, die aan niemand "
                  "verantwoording schuldig is. Verkiezing, grondwet en parlement ontbreken bij allebei."),
        ]),
        dict(kop="Minderheden en economie", blokken=[
            ("p", "Het <strong>millet-stelsel</strong> liet godsdienstige minderheden toe hun eigen "
                  "gemeenschap te besturen, met <strong>eigen recht en eigen scholen</strong>. Christenen en "
                  "joden betaalden een aparte belasting, maar mochten hun geloof behouden."),
            ("p", "Joden die na 1492 uit <strong>Spanje</strong> verdreven werden, vonden in het Ottomaanse "
                  "Rijk een nieuwe thuis, vooral in Saloniki en Constantinopel. Dat is het duidelijkste "
                  "voorbeeld van het verschil in houding: in het Ottomaanse Rijk mochten andere godsdiensten "
                  "<strong>blijven bestaan</strong>, terwijl in christelijk Europa afwijking <strong>vervolgd "
                  "werd</strong>. Gelijkheid was het niet, maar er was wel een plaats."),
            ("p", "Economisch beheerste het rijk wel degelijk <strong>handelsroutes</strong> tussen Europa en Azië: de "
                  "<strong>landroutes tussen Europa en Azië</strong> liepen door zijn gebied. Daarnaast "
                  "bloeiden <strong>handel en ambacht</strong> in grote steden, en hield de <strong>staat "
                  "toezicht op prijzen en voorraden</strong>. Met christelijke landen werd juist volop "
                  "gehandeld. Dat het rijk die landroutes beheerste, is een van de redenen waarom Europa een "
                  "<strong>zeeweg</strong> zocht."),
        ]),
        dict(kop="Contact met Europa", blokken=[
            ("p", "<strong>Suleyman I</strong>, in het Westen <strong>de Prachtlievende</strong> genoemd en "
                  "in eigen land de Wetgever, regeerde van 1520 tot 1566. Tegenover hem stond "
                  "<strong>Karel V</strong>: twee heersers van twee wereldrijken, in dezelfde jaren. Wenen "
                  "werd in 1529 belegerd en hield stand."),
            ("p", "De <strong>Franse koning</strong> Frans I sloot een verstandhouding met de sultan, hoewel "
                  "die een andere godsdienst had: hij zocht een bondgenoot tegen de Habsburgers. Politiek "
                  "belang woog daar zwaarder dan geloof."),
            ("p", "De <strong>capitulaties</strong> zijn <strong>handelsvoorrechten</strong> die de sultan "
                  "aan Europese kooplui gaf; Franse en later andere kooplui kregen eigen rechten in "
                  "Ottomaanse havens. De naam heeft niets met overgave te maken."),
            ("p", "Het contact tussen het rijk en Europa verliep dus door <strong>oorlog</strong> aan de "
                  "grenzen in de Balkan en op zee, door <strong>handel</strong> in het Middellandse "
                  "Zeegebied, en door <strong>diplomatie</strong>, met vaste gezanten aan het hof. Daarom mag "
                  "je het rijk niet enkel als vijand van Europa beschrijven."),
            ("p", "De <strong>16de eeuw</strong> is het <strong>hoogtepunt</strong> van het rijk, geen "
                  "verval. Het latere verval heeft meerdere oorzaken: de <strong>handel verlegde zich naar de "
                  "oceanen</strong>, weg van de landroutes; <strong>Europa liep voor</strong> op het gebied "
                  "van techniek en leger; en het rijk was zo <strong>groot</strong> dat het moeilijk te "
                  "besturen was."),
            ("p", "<strong>Ottomaanse bouwkunst</strong> herken je aan grote <strong>koepels</strong> en "
                  "slanke <strong>minaretten</strong>, aan <strong>sierschrift en geometrische "
                  "patronen</strong> in plaats van mensenfiguren, en aan <strong>tegelwerk</strong> in blauw "
                  "en wit. De Süleymaniye in Istanbul toont die drie samen."),
        ]),
        dict(kop="Samenlevingen vergelijken: de vaste punten", blokken=[
            ("p", "Je vergelijkt samenlevingen op <strong>politieke</strong>, <strong>sociale</strong>, "
                  "<strong>culturele</strong> en <strong>economische</strong> kenmerken. De afstand tot de "
                  "evenaar hoort daar niet bij; dat is geen kenmerk van de samenleving zelf."),
            ("p", tabel(["Soort kenmerk", "Vergelijkingspunten"], [
                ["politiek", "bestuurlijke organisatie, imperialisme, kolonialisme"],
                ["sociaal", "migratie, ongelijkheid, slavernij, staatsvorm"],
                ["cultureel", "kunstuitingen, levensbeschouwing, multiculturele samenleving, wetenschappen, gelaagde samenleving"],
                ["economisch", "landbouw, ambacht, handel, economische systemen"],
            ])),
            ("p", "<strong>Imperialisme</strong> is het streven van een staat om zijn <strong>macht over "
                  "andere gebieden</strong> uit te breiden. <strong>Kolonialisme</strong> is daar één vorm "
                  "van, met vestiging en bestuur ter plaatse; de twee betekenen dus niet hetzelfde."),
            ("p", "Bij <strong>bestuurlijke organisatie</strong> vergelijk je <strong>wie beslist, hoe die "
                  "aan de macht komt en hoe ver die macht reikt</strong>. Een sultan, een absolute koning, "
                  "een parlement en een stadsbestuur van patriciërs zijn telkens een ander antwoord."),
            ("p", "Bij de <strong>gelaagde samenleving</strong> vergelijk je <strong>wie bovenaan en wie "
                  "onderaan staat, en waardoor dat bepaald wordt</strong>. De Egyptische en de middeleeuwse "
                  "gelaagde samenleving hebben gemeen dat een <strong>kleine groep bovenaan leeft van het "
                  "werk van een grote groep onderaan</strong>, dat <strong>godsdienst de ordening "
                  "rechtvaardigt</strong>, en dat je <strong>geboorte</strong> je leven grotendeels bepaalt. "
                  "Opklimmen kon in geen van beide."),
            ("p", "Een <strong>multiculturele samenleving</strong> is een samenleving waarin mensen met "
                  "<strong>verschillende culturen en godsdiensten</strong> naast elkaar leven; het Ottomaanse "
                  "Rijk en het middeleeuwse Al-Andalus zijn voorbeelden. <strong>Slavernij</strong> komt in "
                  "meerdere bestudeerde samenlevingen voor, niet enkel in de koloniale tijd: ook in de "
                  "klassieke oudheid en in het Arabische Rijk."),
            ("p", "<strong>Economische systemen</strong> die je naast elkaar kan leggen: een "
                  "<strong>zelfvoorzienend domein</strong> in de middeleeuwen, het "
                  "<strong>handelskapitalisme</strong> van de vroegmoderne tijd, en de <strong>industriële "
                  "productie</strong> van de 19de eeuw."),
        ]),
        dict(kop="Hoe je vergelijkt, en wat het oplevert", blokken=[
            ("p", "Vergelijken betekent zowel <strong>gelijkenissen</strong> als <strong>verschillen</strong> "
                  "benoemen. Enkel gelijkenissen noemen maakt alles hetzelfde, enkel verschillen maakt alles "
                  "uniek."),
            ("p", "Je vergelijkt <strong>binnen eenzelfde periode</strong> en <strong>over periodes "
                  "heen</strong>. Twee samenlevingen uit dezelfde tijd vergelijken heeft wel degelijk zin: "
                  "het Ottomaanse Rijk en Frankrijk bestonden tegelijk en verschilden grondig."),
            ("p", "Je werkt met <strong>vaste kenmerken</strong> en niet zomaar met wat opvalt, want met "
                  "vaste punten vergelijk je <strong>hetzelfde met hetzelfde</strong>, en zie je ook wat je "
                  "anders over het hoofd zou zien. Wat opvalt, is vaak enkel wat vreemd is aan ons."),
            ("p", "De <strong>historische periodes</strong> waartussen je vergelijkt zijn de prehistorie, het "
                  "oude nabije oosten, de klassieke oudheid, de middeleeuwen en de vroegmoderne tijd. Die "
                  "indeling — de tijd in <strong>stukken</strong> verdelen en die stukken <strong>namen</strong> en "
                  "grenzen geven — heet <strong>periodisering</strong>. De <strong>ijstijd</strong> en de "
                  "<strong>ruimtetijd</strong> zijn géén <strong>namen</strong> van historische periodes. "
                  "Een periodisering is altijd een keuze: een "
                  "<strong>periodegrens</strong> is voor discussie vatbaar omdat de verandering niet overal "
                  "tegelijk en niet in alle domeinen samen gebeurt. <strong>Continuïteit</strong> is wat "
                  "blijft duren terwijl er elders wel verandert."),
            ("kader", "Twee valkuilen. Een <strong>anachronisme</strong> is iets in de verkeerde tijd "
                      "plaatsen, of het verleden beoordelen met de <strong>maatstaf van vandaag</strong>; "
                      "spreken over 'de Belgen' in 1302 is er een. <strong>Historische empathie</strong> is "
                      "het vermogen om je in te leven in de tijd van de mensen die je bestudeert: begrijpen "
                      "waarom iets toen vanzelfsprekend leek, wat niet hetzelfde is als goedkeuren."),
            ("p", "Een vergelijking tussen samenlevingen is ook een <strong>vergelijking tussen "
                  "bronnen</strong>: over de ene heb je archieven, over de andere enkel scherven. En wat je "
                  "eruit leert, is dat er <strong>meerdere antwoorden mogelijk zijn op dezelfde menselijke "
                  "vragen</strong>: hoe ordenen mensen macht, hoe verdelen ze werk, hoe gaan ze om met wie "
                  "anders is?"),
        ]),
    ],
)

# ───────────────────────── 10. Redeneren met historische bronnen
BUNDELS["redeneren-met-historische-bronnen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Redeneren met historische bronnen",
    onder="Van een goede historische vraag naar een beargumenteerd antwoord, in vier stappen.",
    secties=[
        dict(kop="De historische vraag", blokken=[
            ("p", "Je krijgt alleen een goed beeld van het verleden als je er <strong>historische "
                  "vragen</strong> aan stelt. Een historicus stelt daarom <strong>eerst een vraag</strong> en "
                  "gaat pas daarna bronnen zoeken: zonder vraag weet je niet waarnaar je in een bron moet "
                  "kijken. Dezelfde kloosterrekening geeft een ander antwoord aan wie naar voeding vraagt dan "
                  "aan wie naar arbeid vraagt."),
            ("p", "De <strong>criteria voor de onderzoekbaarheid</strong> van een historische vraag: een "
                  "<strong>afbakening in tijd</strong>, een <strong>afbakening in ruimte</strong>, een "
                  "<strong>afbakening binnen maatschappelijke domeinen</strong>, het <strong>bestaan van "
                  "bronnen</strong> en de <strong>bruikbaarheid</strong> van die bronnen."),
            ("p", "De vraag <em>Waarom gingen mensen op ontdekkingstocht?</em> is zonder verdere afbakening "
                  "nog geen goede onderzoeksvraag: welke mensen, wanneer, van waaruit? De vraag <em>Welke rol "
                  "speelden de Arabieren in de internationale handel?</em> mist vooral de "
                  "<strong>afbakening in tijd</strong>: over welke eeuw gaat het? Handel is al een economisch "
                  "domein, en de ruimte staat er ook in."),
        ]),
        dict(kop="Stap 1: de context van de bron", blokken=[
            ("p", "De drie stappen hieronder vormen samen de <strong>bronnenanalyse</strong>. Elke stap heeft "
                  "zijn eigen werk: in stap 1 verzamel je, in stap 2 beoordeel je, in stap 3 interpreteer je. "
                  "Wat in een latere stap hoort, doe je in de eerste nog niet; en hoeveel een bron vandaag als "
                  "voorwerp waard is, hoort in géén enkele stap thuis."),
            ("p", "In <strong>stap 1</strong> verzamel je informatie over de <strong>context</strong> van "
                  "elke bron. Je <strong>situeert</strong> ze in het referentiekader: waar en wanneer ze "
                  "ontstond, en in welk <strong>domein</strong> ze thuishoort. Je bepaalt welke "
                  "<strong>soort bron</strong> het is, je <strong>contextualiseert de maker</strong>, en je "
                  "bepaalt het <strong>doelpubliek</strong>, de <strong>inhoud</strong> en de "
                  "<strong>bedoeling</strong>. Wat de bron vandaag waard is, hoort er niet bij."),
            ("p", "Bij stap 1 hoort ook vaststellen welke <strong>contextgegevens ontbreken</strong>. Een "
                  "bron zonder datum of zonder bekende maker kan nog altijd bruikbaar zijn, maar je moet "
                  "weten dat dat gat er is."),
            ("p", "Een <strong>primaire bron</strong> komt uit de tijd zelf, een <strong>secundaire "
                  "bron</strong> is er later over gemaakt. Een dagboek uit 1789 is primair, een "
                  "geschiedenisboek over 1789 secundair. Primair betekent niet automatisch beter, en een "
                  "secundaire bron van een historicus is niet automatisch betrouwbaarder dan een "
                  "ooggetuigenverslag: je beoordeelt elke bron apart."),
            ("p", "Naar <strong>vorm</strong> onderscheid je <strong>geschreven</strong>, "
                  "<strong>mondelinge</strong>, <strong>materiële</strong> en <strong>audiovisuele</strong> "
                  "bronnen. Een <strong>materiële bron</strong> is een voorwerp of een gebouw: een muntstuk, "
                  "een scherf, een belfort. <strong>Archeologische bronnen</strong> zijn belangrijk voor "
                  "periodes met weinig geschriften, want ze vertellen over het <strong>dagelijkse leven van "
                  "mensen die zelf niet schreven</strong>. Die vier vormen zijn de hele lijst: een "
                  "<strong>denkbeeldige bron</strong> bestaat niet, want een bron is altijd iets dat "
                  "echt bewaard is gebleven."),
            ("p", "Over de <strong>maker</strong> wil je weten <strong>wie het is</strong> (naam, beroep, "
                  "afkomst), welke <strong>maatschappelijke positie</strong> hij innam, en <strong>wie de "
                  "opdracht gaf</strong> en met welk doel. Een <strong>ooggetuige</strong> heeft de "
                  "gebeurtenis zelf gezien; een <strong>tijdgenoot</strong> leefde in dezelfde tijd maar was "
                  "er daarom nog niet bij. Je vraagt je ook af <strong>voor wie</strong> de bron gemaakt is, "
                  "want het publiek bepaalt mee wat er verteld en verzwegen wordt."),
            ("weetje", "Bij <strong>digitale bronnen</strong> houd je rekening met ethische, sociale en "
                       "legale regels: vermeld de herkomst, respecteer het auteursrecht, en let op privacy "
                       "bij recent materiaal."),
        ]),
        dict(kop="Stap 2 en 3: lezen en interpreteren", blokken=[
            ("p", "In <strong>stap 2</strong> lees of bekijk je de bronnen. In <strong>stap 3</strong> "
                  "<strong>interpreteer</strong> je ze: je legt uit hoe de historische context en de "
                  "<strong>standplaatsgebondenheid</strong> van de maker de inhoud al dan niet bepalen."),
            ("p", "<strong>Standplaatsgebondenheid</strong> betekent dat wie iets vertelt, dat doet vanuit "
                  "zijn eigen <strong>plaats, tijd en belangen</strong>. Een Spaanse en een Nederlandse bron "
                  "over Alva zijn daar het schoolvoorbeeld van. Ze maakt een bron niet waardeloos, "
                  "integendeel: je leert er de blik van de maker uit kennen."),
            ("p", "Bronnen die elkaar <strong>tegenspreken</strong>, herleid je niet zo snel mogelijk tot één "
                  "verhaal. Juist dat verschil is informatie. Je <strong>vergelijkt</strong> de bronnen op "
                  "hun <strong>context</strong>, hun <strong>inhoud</strong> en hun "
                  "<strong>betrouwbaarheid</strong>, en onderscheidt daarbij gelijkenissen en verschillen."),
        ]),
        dict(kop="Bruikbaarheid en betrouwbaarheid", blokken=[
            ("p", "De <strong>bruikbaarheid</strong> van een bron is de mate waarin ze <strong>jouw "
                  "historische vraag helpt beantwoorden</strong>. Een betrouwbare bron over een ander "
                  "onderwerp is voor jouw vraag onbruikbaar; bruikbaarheid hangt dus altijd van de vraag af."),
            ("p", "Je vraagt je af: geeft de bron <strong>rechtstreekse informatie</strong> over het "
                  "onderwerp? Geeft ze <strong>onrechtstreekse informatie</strong>? Geeft ze een "
                  "<strong>volledig, gedeeltelijk of geen antwoord</strong> op de vraag? Een bron die maar "
                  "een deel beantwoordt, is daarom nog niet waardeloos: je legt hem naast andere."),
            ("p", "Bij de <strong>betrouwbaarheid</strong> kijk je eerst naar elementen uit de "
                  "<strong>historische context</strong> die haar beïnvloeden: de maker <strong>hing af</strong> "
                  "van de persoon over wie hij schrijft, er heerste <strong>censuur</strong>, of de bron werd "
                  "pas <strong>lang na de feiten</strong> opgeschreven."),
            ("p", "Daarna gebruik je de <strong>criteria</strong> om de inhoud in vraag te stellen: de "
                  "gebruikte <strong>argumentatie</strong>, de <strong>interpretatie</strong>, "
                  "<strong>veralgemening</strong>, <strong>vooroordeel</strong> en "
                  "<strong>stereotypering</strong>. De lengte van de tekst zegt niets."),
            ("p", "Een <strong>veralgemening</strong> is uit één of enkele gevallen een besluit over het "
                  "<strong>geheel</strong> trekken; let op woorden als 'iedereen', 'altijd' en 'overal'. Een "
                  "<strong>stereotype</strong> is een vast, te eenvoudig beeld van een hele groep mensen: de "
                  "luie boer, de wrede Spanjaard. Een <strong>vooroordeel</strong> is een mening die al "
                  "vaststaat <strong>voor</strong> men de feiten bekeken heeft."),
        ]),
        dict(kop="Stap 4: een beargumenteerd antwoord", blokken=[
            ("p", "In <strong>stap 4</strong> formuleer je een <strong>beargumenteerd antwoord</strong>: je "
                  "<strong>kiest informatie</strong> uit de bronnen en <strong>staaft je antwoord met "
                  "argumenten</strong>. Een samenvatting van elke bron is nog geen antwoord."),
            ("p", "Eén bron volstaat daarvoor niet: <strong>elke bron is standplaatsgebonden en "
                  "onvolledig</strong>, en samen dekken ze elkaars blinde vlekken. Wat twee onafhankelijke "
                  "bronnen allebei zeggen, staat sterker dan wat er in één staat."),
            ("p", "Onderzoek je hoe bloedig de <strong>Slag bij Hastings</strong> verliep, dan wegen de "
                  "<strong>bronnen samen</strong> het zwaarst, na vergelijking en weging van hun "
                  "betrouwbaarheid. Een lofdicht van een tijdgenoot op de overwinnaar overdrijft met opzet."),
            ("p", "Op een historische vraag kan <strong>meer dan één beargumenteerd antwoord</strong> "
                  "bestaan. Of Karel de Grote de vader van Europa is, hangt af van wat je onder Europa "
                  "verstaat. Wat telt, is of je antwoord door de bronnen gedragen wordt."),
        ]),
        dict(kop="De historische redeneerwijzen", blokken=[
            ("p", "De <strong>historische redeneerwijzen</strong> zijn de manieren van denken waarmee je een "
                  "antwoord opbouwt: <strong>oorzaak en gevolg benoemen</strong>, <strong>bedoelde en "
                  "onbedoelde gevolgen onderscheiden</strong>, <strong>meerdere perspectieven "
                  "hanteren</strong>, <strong>continuïteit en verandering benoemen</strong>, <strong>bewijs "
                  "gebruiken</strong>, <strong>actualiseren</strong>, <strong>verbanden leggen</strong>, "
                  "<strong>historisch contextualiseren</strong>, <strong>menselijke actoren</strong> of "
                  "<strong>agency</strong> benoemen, en <strong>veralgemening</strong> en "
                  "<strong>stereotypering analyseren</strong>."),
            ("p", "<strong>Bewijs gebruiken</strong> betekent dat je elke uitspraak <strong>staaft met "
                  "informatie uit een bron</strong>. Zonder bron is het een mening."),
            ("p", "Een <strong>onbedoeld gevolg</strong> is een gevolg dat <strong>niemand nastreefde</strong> "
                  "maar dat er toch kwam: Columbus zocht een weg naar Azië en veroorzaakte de kolonisatie van "
                  "Amerika."),
            ("p", "<strong>Actualiseren</strong> is een verband leggen tussen het verleden en vandaag. "
                  "<strong>Historisch contextualiseren</strong> is een gebeurtenis of bron begrijpen "
                  "<strong>vanuit de tijd waarin ze thuishoort</strong>: wie de Beeldenstorm beoordeelt zonder "
                  "de honger en de vervolging van 1566 te kennen, ziet enkel vandalisme."),
            ("p", "<strong>Agency</strong> of menselijke actoren benoemen betekent aangeven welke mensen zelf "
                  "iets in gang zetten: het verleden overkwam hen niet alleen, ze maakten het ook. "
                  "<strong>Meerdere perspectieven hanteren</strong> betekent niet dat elk standpunt evenveel "
                  "waard is, maar dat je verschillende standpunten kent en weegt."),
        ]),
    ],
)

# ───────────────────────── 11. Beeldvorming en het verleden vandaag
BUNDELS["beeldvorming-en-het-verleden-vandaag-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Beeldvorming en het verleden vandaag",
    onder="Hoe een beeld van het verleden gemaakt wordt, en hoe het meespeelt in wie wij vandaag zijn.",
    secties=[
        dict(kop="Wat beeldvorming is", blokken=[
            ("p", "Alles wat vroeger gebeurd is, ligt achter ons. Wat wij hebben, is <strong>historische "
                  "beeldvorming</strong>: het <strong>beeld van het verleden dat iemand opbouwt uit "
                  "bronnen</strong>. Historici brengen dat verleden in beeld door bronnen kritisch te "
                  "analyseren."),
            ("p", "Zo'n beeld is <strong>altijd een constructie</strong> van iemand, vanuit een bepaald "
                  "perspectief. Die persoon <strong>selecteert bronnen</strong>, <strong>leidt er informatie "
                  "uit af</strong>, <strong>interpreteert</strong> en <strong>zoekt samenhang</strong>. Elk "
                  "van die stappen is een keuze. Wat er destijds gebeurd is, ligt wel vast; alleen is het "
                  "niet volledig kenbaar."),
            ("p", "Het beeld van een gebeurtenis kan in de loop van de tijd <strong>veranderen</strong>, "
                  "omdat er <strong>nieuwe bronnen</strong> bijkomen en <strong>nieuwe vragen</strong> aan "
                  "die bronnen gesteld worden. Een bron die <strong>zeldzaam of pas ontdekt</strong> is, kan "
                  "het bestaande beeld in beweging brengen."),
            ("p", "Komen twee historici tot een verschillend beeld, dan heeft daarom niet één slecht "
                  "gewerkt: ze kunnen andere bronnen gebruiken of andere vragen stellen. Pas als een beeld de "
                  "bronnen tegenspreekt, is er een echt probleem."),
            ("kader", "Daarom bekijk je beeldvorming met <strong>voorzichtigheid</strong>: een beeld is "
                      "altijd door iemand gemaakt, met keuzes en met blinde vlekken. Voorzichtig zijn is niet "
                      "hetzelfde als niets geloven."),
        ]),
        dict(kop="Standplaatsgebondenheid", blokken=[
            ("p", "De <strong>persoonlijke context</strong> van een maker kleurt zijn beeld: zijn "
                  "<strong>afkomst, geloof en beroep</strong> bepalen mee wat hij belangrijk vindt. Een "
                  "geestelijke die over de Beeldenstorm schrijft, ziet iets anders dan een wever uit dezelfde "
                  "stad."),
            ("p", "Ook de <strong>maatschappelijke context</strong> speelt mee: een <strong>land in "
                  "oorlog</strong> vertelt zijn verleden anders dan een land in vrede, een "
                  "<strong>schoolboek van vandaag</strong> legt andere accenten dan dat van honderd jaar "
                  "geleden, en <strong>wie het geld voor het onderzoek geeft</strong>, bepaalt mee welke "
                  "vragen gesteld worden. Ook een geschiedenisboek van vandaag is dus standplaatsgebonden."),
            ("p", "De <strong>inname van Jeruzalem in 1099</strong> is daar een scherp voorbeeld van. De "
                  "<strong>Arabische bronnen</strong> geven van de <strong>Franken</strong> het beeld van "
                  "<strong>ruwe, gewelddadige indringers van ver weg</strong>; westerse kronieken vertellen "
                  "hetzelfde bloedbad als een door God gewild succes. Ze verschillen vooral omdat hun makers "
                  "<strong>aan een andere kant stonden</strong>."),
            ("p", "Lees je maar één kant van een conflict, dan <strong>neem je de blik van die kant "
                  "over</strong> zonder het te merken. Daarom leg je bronnen van beide kanten naast elkaar."),
            ("p", "Het beeld van <strong>Karel de Grote</strong> verschilt zo sterk omdat de vraag die je "
                  "stelt het antwoord bepaalt: <strong>vader van Europa</strong>, <strong>Frankische "
                  "veroveraar</strong> of <strong>Duits keizer</strong>. Frankrijk en Duitsland claimden hem "
                  "allebei, en na 1945 werd hij het symbool van Europese eenheid."),
            ("p", "Bij een beeld dat je voorgeschoteld krijgt, vraag je je af: <strong>wie maakte dit, en "
                  "wanneer</strong>? <strong>Welke bronnen</strong> liggen eraan ten grondslag? <strong>Wat "
                  "wordt er niet verteld</strong>? En het is nuttig te weten <strong>wie de opdracht "
                  "gaf</strong>, want de opdrachtgever bepaalt vaak mee wat verteld en verzwegen wordt."),
            ("p", "Een <strong>stereotype</strong> in een oude bron neem je niet zomaar over: je benoemt het "
                  "en analyseert het. <strong>Veralgemening analyseren</strong> is nagaan of een uitspraak "
                  "over een hele groep wel op <strong>meer dan enkele gevallen</strong> steunt. "
                  "<em>De middeleeuwer geloofde dat de aarde plat was</em> is zo'n uitspraak; ze klopt niet, "
                  "en ze wordt toch voortdurend herhaald. Ook een <strong>schilderij of een "
                  "standbeeld</strong> doet aan beeldvorming: wie wordt afgebeeld, hoe groot, in welke "
                  "houding?"),
        ]),
        dict(kop="Verleden, heden en toekomst", blokken=[
            ("p", "Aan eenzelfde historische persoon, plaats of gebeurtenis geven mensen verschillende "
                  "<strong>betekenissen</strong>. <strong>Vlaamsgezinden</strong> geven de "
                  "<strong>Guldensporenslag</strong> de betekenis van een <strong>Vlaamse overwinning op een "
                  "vreemde overheerser</strong>, als teken van eigenheid. In de 19de eeuw, toen men een "
                  "Vlaamse identiteit zocht, kreeg 1302 die rol."),
            ("p", "Die betekenis is dus niet altijd dezelfde gebleven: voor de tijdgenoten was het een "
                  "<strong>sociale en politieke strijd</strong>. De taalkundige en nationale betekenis komt "
                  "er pas vijfhonderd jaar later bij. Ook verschillende <strong>personen</strong> geven "
                  "vandaag een verschillende betekenis aan dezelfde datum."),
            ("p", "Dat een <strong>herdenking</strong> iets over het <strong>heden</strong> vertelt, betekent "
                  "dat <strong>wát men herdenkt en hóé</strong> afhangt van wat een samenleving nú belangrijk "
                  "vindt. De feestdag van de Vlaamse Gemeenschap valt op <strong>11 juli</strong>, naar de "
                  "Guldensporenslag; dat die keuze pas in de 20ste eeuw gemaakt werd, hoort bij het verhaal."),
            ("p", "Een historisch fenomeen geeft mee vorm aan een <strong>groepsidentiteit</strong> door een "
                  "<strong>gedeelde herinnering</strong> te worden waarin een groep zich herkent: een "
                  "feestdag, een standbeeld, een lied op school."),
            ("p", "De <strong>lagen van identiteit</strong> zijn de <strong>Vlaamse</strong>, de "
                  "<strong>Belgische</strong>, de <strong>westerse en niet-westerse</strong> laag, de "
                  "<strong>sociaaleconomische positie</strong> en de <strong>levensbeschouwing</strong>. Een "
                  "mens heeft niet één identiteit tegelijk: die lagen sluiten elkaar niet uit."),
            ("p", "Je mag het verleden niet met de <strong>maatstaf van vandaag</strong> beoordelen, want dan "
                  "begrijp je niet <strong>waarom iets toen vanzelfsprekend leek</strong>. Begrijpen is niet "
                  "hetzelfde als goedkeuren."),
        ]),
        dict(kop="Kunst- en cultuuruitingen analyseren", blokken=[
            ("p", "Kunst- en cultuuruitingen geven zicht op de mens en de wereld. Je analyseert ze met een "
                  "<strong>stappenplan</strong>."),
            ("p", "In <strong>stap 1</strong> verzamel je informatie: de <strong>tijd</strong> en de "
                  "<strong>ruimte</strong> waarin het gemaakt is, de <strong>maker</strong> en de "
                  "<strong>maatschappelijke context</strong>, de <strong>titel</strong> en de "
                  "<strong>soort uiting</strong>. De huidige verkoopprijs hoort er niet bij. De soorten die "
                  "de fiche noemt: een <strong>schilderij</strong>, een <strong>beeldhouwwerk</strong>, een "
                  "<strong>bouwwerk</strong>, een <strong>film</strong>, een <strong>game</strong>, "
                  "<strong>graffiti</strong> en een <strong>lied</strong>."),
            ("p", "In <strong>stap 2</strong> beschrijf je wat je <strong>letterlijk ziet of hoort</strong>: "
                  "welke <strong>materialen</strong>, welke <strong>figuren en vormen</strong>, de "
                  "<strong>schikking</strong> van de beeldelementen, de <strong>kleuren</strong>, het gebruik "
                  "van <strong>licht en schaduw</strong>, en bij geluid de <strong>klanken, het ritme en het "
                  "tempo</strong> en de <strong>instrumenten of stemmen</strong>. Eerst kijken, dan pas "
                  "duiden."),
            ("p", "In <strong>stap 3</strong> interpreteer je. Je bepaalt het <strong>onderwerp</strong> "
                  "(waarover het gaat), het <strong>doelpubliek</strong> (voor wie het gemaakt is) en de "
                  "<strong>bedoeling</strong> (waarom het gemaakt is): <strong>bekritiseren</strong>, "
                  "<strong>bevestigen</strong>, <strong>decoreren</strong>, <strong>entertainen</strong>, "
                  "<strong>identiteit vormgeven</strong>, <strong>informeren</strong>, <strong>praktisch "
                  "gebruiken</strong> of <strong>schoonheid creëren</strong>. Vaak zijn er meerdere tegelijk. "
                  "Daarna licht je toe hoe wat je ziet of hoort het onderwerp en de bedoeling ondersteunt, en "
                  "welke invloed de maatschappelijke context daarop had. In <strong>stap 4</strong> verwoord "
                  "je je analyse."),
            ("p", "Zo ondersteunt de vorm van een <strong>barokschilderij</strong> zijn bedoeling: "
                  "<strong>beweging, licht en grote gebaren</strong> moeten de kijker meeslepen en "
                  "overtuigen. De Contrareformatie wilde het geloof niet uitleggen maar laten voelen. Je "
                  "kijkt daarbij ook naar de <strong>maatschappelijke context</strong>, want die verklaart "
                  "mee waarom juist dit onderwerp en deze bedoeling gekozen werden: een Mariabeeld uit 1650 "
                  "in Antwerpen is een antwoord op de Beeldenstorm van bijna een eeuw eerder."),
            ("p", "Kunst uit het verleden zegt dus niet alleen iets over kunst: ze toont wat men mooi vond, "
                  "wie kon betalen, wat men wilde uitstralen en wat men liever niet liet zien."),
            ("weetje", "Nadenken over beeldvorming helpt je ook bij <strong>nieuws en sociale media</strong> "
                       "van vandaag. Wie maakte dit, met welke bronnen, voor wie en waarom? Dezelfde vragen, "
                       "alleen is de bron van gisteren."),
            ("kader", "De kern van dit vak: een <strong>beeld van het verleden is altijd gemaakt</strong>, en "
                      "je mag vragen <strong>door wie en waarom</strong>. Niet alles is even waar, en niet "
                      "niets is kenbaar."),
        ]),
    ],
)
