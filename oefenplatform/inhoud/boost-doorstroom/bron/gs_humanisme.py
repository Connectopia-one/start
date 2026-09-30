# -*- coding: utf-8 -*-
"""De vragen voor "Humanisme, Reformatie, renaissance en barok".

Uit de vakfiche: de nieuwe visie op mens, wereld, geloof en kunst. Het
humanisme (ontstaan, verspreiding, kenmerken, de vernieuwing van de
wetenschappelijke methode, de humanisten zelf), de Reformatie en de
Contrareformatie (oorzaken, lutheranisme, anglicanisme en calvinisme,
verspreiding, maatregelen), de renaissancekunst en de barokkunst.

Deel 1 gaat over het humanisme en de Reformatie. Deel 2 over renaissance en
barok.

De fiche vraagt uitdrukkelijk dat een leerling kan uitleggen waarom de David van
Michelangelo tot de renaissance behoort, en hoe het contact met de Arabische
wereld de westerse geneeskunde beïnvloedde.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar ontstond het humanisme?",
        opties=[
            "in de rijke Italiaanse steden",
            "aan het Franse hof",
            "in de Duitse kloosters",
            "in de Engelse universiteiten",
        ],
        antwoord=0,
        uitleg="Florence, Venetië en Rome hadden het geld, de handelscontacten en de Romeinse resten om op verder te bouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn kenmerken van het humanisme?",
        opties=[
            "belangstelling voor de mens en zijn mogelijkheden",
            "teruggrijpen naar de Griekse en Romeinse oudheid",
            "kritisch onderzoek van de oorspronkelijke teksten",
            "het verwerpen van elke vorm van godsdienst en geloof",
        ],
        antwoord=[0, 1, 2],
        uitleg="De meeste humanisten bleven gelovig; Erasmus was priester. Ze wilden het geloof zuiveren, niet afschaffen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke humanist uit Rotterdam schreef 'Lof der Zotheid'?",
        antwoord="Erasmus",
        uitleg="Hij bespotte er de misbruiken in Kerk en samenleving mee, en pleitte voor onderwijs en verdraagzaamheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De boekdrukkunst hielp de ideeën van de humanisten snel verspreiden.",
        antwoord=True,
        uitleg="Wat vroeger één monnik in maanden overschreef, rolde nu bij honderden van de pers. Zonder Gutenberg geen Erasmus in heel Europa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat veranderde er aan de wetenschappelijke methode?",
        opties=[
            "men ging zelf waarnemen en proeven doen in plaats van oude teksten te geloven",
            "men stopte met alle onderzoek en hield zich enkel nog met kunst bezig",
            "men baseerde zich voortaan enkel op de Bijbel en op geen enkele andere bron",
            "men liet de wiskunde helemaal vallen omdat ze uit de oudheid kwam",
        ],
        antwoord=0,
        uitleg="Vesalius ontleedde zelf lichamen en ontdekte dat de oude Galenus zich vergist had. Dat je dat mág vaststellen, is het echte nieuwe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bereikte de westerse geneeskunde níét langs de Arabische wereld?",
        opties=[
            "de microscoop",
            "de handboeken van Ibn Sina",
            "de Griekse teksten in vertaling",
            "kennis over geneesmiddelen",
        ],
        antwoord=0,
        uitleg="De microscoop komt uit de Nederlanden, in de 17de eeuw. De drie andere kwamen wel langs Bagdad, Córdoba en Toledo binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vesalius toonde aan dat de oude Griekse geneeskundige teksten niet in alles gelijk hadden.",
        antwoord=True,
        uitleg="Door zelf te ontleden zag hij wat er echt zat. Zijn boek uit 1543 staat vol tekeningen naar eigen waarneming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren oorzaken van de Reformatie?",
        opties=[
            "misbruiken in de Kerk, zoals de aflaathandel",
            "de rijkdom en het wereldse leven van hoge geestelijken",
            "de kritische lezing van de Bijbel door humanisten",
            "het verbod van de paus op elk kerkbezoek in Duitsland",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kerkbezoek werd nergens verboden. De drie andere samen verklaren waarom Luthers kritiek zo snel weerklank vond.",
    ),
    dict(
        type="invultekst",
        vraag="Welke monnik hing in 1517 zijn stellingen tegen de aflaathandel op?",
        antwoord="Luther",
        uitleg="Vijfennegentig stellingen, in Wittenberg. Hij wilde een discussie, geen scheuring, maar die kwam er wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een aflaat?",
        opties=[
            "een kwijtschelding van straf voor zonden, die men ook kon kopen",
            "een belasting op graan die aan het klooster betaald moest worden",
            "een boete die een wereldlijke rechter aan een schuldige oplegde",
            "een toelating van de heer om zijn domein te mogen verlaten",
        ],
        antwoord=0,
        uitleg="Het geld diende onder meer voor de bouw van de Sint-Pietersbasiliek. Dat je je plaats in het hiernamaals kon kopen, stootte velen tegen de borst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat leerde Luther over hoe een mens gered wordt?",
        opties=[
            "door het geloof alleen, en door de Bijbel als enige bron",
            "door goede werken te doen en genoeg aflaten te kopen",
            "door de paus in alles te gehoorzamen, ook in de leer",
            "door minstens één keer een verre pelgrimstocht te maken",
        ],
        antwoord=0,
        uitleg="Sola fide en sola scriptura. Dat zet meteen de bemiddelende rol van de Kerk en haar priesters op de helling.",
    ),
    dict(
        type="waarofniet",
        vraag="Het anglicanisme ontstond uit een geloofsdiscussie, niet uit een politieke breuk.",
        antwoord=False,
        uitleg="Hendrik VIII wilde scheiden en de paus weigerde. Hij maakte zichzelf hoofd van de Engelse Kerk; in de leer bleef er eerst weinig veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor het calvinisme?",
        opties=[
            "de predestinatie: God heeft vooraf bepaald wie gered wordt",
            "een sobere eredienst, in een kerk zonder beelden",
            "een kerk die door gekozen ouderlingen bestuurd wordt",
            "de paus in Rome als hoogste gezag in de geloofsleer",
        ],
        antwoord=[0, 1, 2],
        uitleg="De paus erkennen ze juist niet. De drie andere kenmerken verklaren ook waarom calvinisten later zo op eigen bestuur gesteld waren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar sloeg het protestantisme het sterkst aan?",
        opties=[
            "in Noord-Europa: de Duitse vorstendommen, Scandinavië, Engeland, Schotland",
            "in Zuid-Europa: vooral in Spanje en Portugal, tot in hun koloniën toe",
            "in Italië, waar het van Rome uit over het hele schiereiland uitwaaierde",
            "in Ierland, waar het de oudste kloosters van het eiland overnam",
        ],
        antwoord=0,
        uitleg="Vorsten die zich van Rome losmaakten, konden ook de kerkelijke goederen in beslag nemen. Godsdienst en macht liepen ook hier door elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="De Contrareformatie bestond enkel uit vervolging van protestanten.",
        antwoord=False,
        uitleg="Er waren ook hervormingen van binnenuit: het Concilie van Trente, betere priesteropleidingen, nieuwe orden zoals de jezuïeten met hun scholen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregel hoort níét bij de Contrareformatie?",
        opties=[
            "de afschaffing van de mis",
            "het Concilie van Trente",
            "een betere priesteropleiding",
            "een index van verboden boeken",
        ],
        antwoord=0,
        uitleg="De mis werd juist bevestigd en plechtiger gemaakt. De drie andere moesten de eigen Kerk versterken en de leer bewaken.",
    ),
    dict(
        type="invultekst",
        vraag="Welk concilie legde in de 16de eeuw de katholieke leer opnieuw vast?",
        antwoord="Trente",
        uitleg="Het vergaderde met tussenpozen van 1545 tot 1563. Wat daar beslist werd, bleef vierhonderd jaar lang gelden.",
    ),
    dict(
        type="waarofniet",
        vraag="De godsdienstige breuk van de 16de eeuw had ook politieke gevolgen.",
        antwoord=True,
        uitleg="Godsdienstoorlogen in Frankrijk, de Dertigjarige Oorlog in Duitsland, de Opstand in de Nederlanden. Wie welk geloof had, bepaalde mee wie welke macht kreeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het humanisme een voorwaarde voor de Reformatie?",
        opties=[
            "humanisten lazen de Bijbel in de brontaal en zagen dat de vertaling niet klopte",
            "humanisten wilden zelf een nieuwe kerk stichten naast de bestaande",
            "humanisten schaften het Latijn af als taal van Kerk en geleerdheid",
            "humanisten verboden aan gewone gelovigen het lezen van de Bijbel",
        ],
        antwoord=0,
        uitleg="Wie de brontekst mag nakijken, mag ook vaststellen dat een gebruik er niet in staat. Erasmus legde het ei, zei men, en Luther broedde het uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk maatschappelijk domein hoort de Reformatie in de eerste plaats?",
        opties=[
            "het culturele domein",
            "het economische domein",
            "het maritieme domein",
            "het militaire domein",
        ],
        antwoord=0,
        uitleg="Godsdienst hoort bij cultuur. Dat ze vorstendommen tegen elkaar opzette, maakt haar daarnaast ook politiek van het grootste belang.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waaraan ontleent de renaissance haar naam?",
        opties=[
            "aan de wedergeboorte van de klassieke oudheid",
            "aan de geboorte van een nieuwe godsdienst",
            "aan de hergeboorte van het Romeinse Rijk als staat",
            "aan de herbouw van Jeruzalem",
        ],
        antwoord=0,
        uitleg="Kunstenaars en geleerden namen de Grieken en Romeinen opnieuw als voorbeeld, in vormen, verhoudingen en onderwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn kenmerken van de renaissancekunst?",
        opties=[
            "evenwicht, rust en heldere verhoudingen",
            "perspectief, waardoor diepte ontstaat",
            "het menselijk lichaam naar de natuur bestudeerd",
            "bewust scheve en onrustige lijnen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onrust en beweging horen bij de barok. De renaissance zoekt juist de maat en het evenwicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Het perspectief laat toe om op een plat vlak de indruk van diepte te wekken.",
        antwoord=True,
        uitleg="Lijnen die naar één verdwijnpunt lopen, en dingen die kleiner worden naarmate ze verder staan. Brunelleschi en Alberti schreven de regels uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom behoort de David van Michelangelo tot de renaissance?",
        opties=[
            "het naakte lichaam is naar de natuur bestudeerd, in rustige klassieke verhoudingen",
            "het beeld is van brons gegoten, een techniek die pas in die eeuw uitgevonden werd",
            "het beeld toont een heilige met een aureool, zoals dat in die tijd hoorde",
            "het beeld is bedoeld voor een graf en toont daarom een liggende figuur",
        ],
        antwoord=0,
        uitleg="Het is marmer, geen brons, en er is geen aureool te bekennen. De mens zelf, zelfbewust en in verhouding, is het onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kunstenaar hoort níét bij de Italiaanse renaissance?",
        opties=[
            "Peter Paul Rubens",
            "Leonardo da Vinci",
            "Michelangelo",
            "Rafaël",
        ],
        antwoord=0,
        uitleg="Rubens is een barokschilder uit Antwerpen, een eeuw later. De drie andere werkten in Florence en Rome rond 1500.",
    ),
    dict(
        type="invultekst",
        vraag="Wie schilderde het plafond van de Sixtijnse Kapel?",
        antwoord="Michelangelo",
        uitleg="Vier jaar lang, op een stelling. Hij noemde zichzelf liever beeldhouwer dan schilder.",
    ),
    dict(
        type="waarofniet",
        vraag="Renaissancekunstenaars kozen enkel godsdienstige onderwerpen.",
        antwoord=False,
        uitleg="Ze schilderden ook portretten, verhalen uit de oudheid en stadsgezichten. Dat wereldse onderwerpen erbij komen, is juist kenmerkend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe stond de renaissancekunst in dienst van een nieuw mens- en wereldbeeld?",
        opties=[
            "ze zette de mens zelf in het midden, met zijn eigen gelaat en zijn eigen kunnen",
            "ze toonde de mens juist als nietig en zonder waarde tegenover de schepping",
            "ze weigerde mensen af te beelden en hield het bij symbolen en patronen",
            "ze toonde enkel dieren en planten, want die waren rechtstreeks door God gemaakt",
        ],
        antwoord=0,
        uitleg="Het portret wordt een genre op zich, en een opdrachtgever laat zich gerust in een bijbeltafereel meeschilderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de barokkunst?",
        opties=[
            "beweging, drama en sterke licht-donkercontrasten",
            "weelderige versiering en rijke kleuren",
            "grote, meeslepende taferelen die de kijker willen raken",
            "sobere, kale kerkruimtes zonder beelden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kale kerken zonder beelden horen bij het calvinisme. De barok wil juist overweldigen.",
    ),
    dict(
        type="waarofniet",
        vraag="De barok staat los van de godsdienstige strijd van haar tijd.",
        antwoord=False,
        uitleg="Ze is grotendeels de kunst van de Contrareformatie: waar de protestanten beelden weghaalden, zette de katholieke Kerk er nog grotere bij.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Antwerpse schilder is de bekendste vertegenwoordiger van de barok bij ons?",
        antwoord="Rubens",
        uitleg="Hij leidde een werkplaats met tientallen medewerkers en werkte ook als diplomaat voor de vorst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruikten vorsten de barokkunst?",
        opties=[
            "om hun macht en hun aanzien te tonen",
            "om hun paleizen en tuinen indruk te laten maken",
            "om zichzelf in grote portretten te laten vereeuwigen",
            "om hun onderdanen tot soberheid aan te zetten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Soberheid was wel het laatste wat Versailles uitstraalde. Kunst in dienst van geloof én macht, dat is de barok.",
    ),
    dict(
        type="waarofniet",
        vraag="Het verschil tussen renaissance en barok zie je aan rust tegenover beweging.",
        antwoord=True,
        uitleg="Zet de David naast een beeld van Bernini: het ene staat stil en in evenwicht, het andere zit midden in een beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een stijlkenmerk waaraan je barokbouwkunst herkent?",
        opties=[
            "gebogen gevels, zuilen en veel beeldhouwwerk",
            "spitsbogen en luchtbogen",
            "dikke muren met kleine rondboogvensters",
            "gladde betonnen vlakken",
        ],
        antwoord=0,
        uitleg="Spitsbogen horen bij de gotiek, dikke muren met rondbogen bij de romaanse stijl, beton bij de 20ste eeuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schilderden de Vlaamse primitieven anders dan de Italiaanse renaissancekunstenaars?",
        opties=[
            "zij gingen met olieverf vooral voor het detail, de Italianen voor de verhoudingen",
            "zij gebruikten helemaal geen kleur en werkten enkel in zwart en wit",
            "zij schilderden enkel landschappen en nooit mensen of binnenruimtes",
            "zij werkten enkel op muren en nooit op houten panelen of op doek",
        ],
        antwoord=0,
        uitleg="Van Eyck schildert elke haar en elke weerspiegeling; een Italiaan zoekt eerst de bouw van het geheel. Twee wegen naar de natuur toe.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kunstwerk is ook een historische bron.",
        antwoord=True,
        uitleg="Het vertelt je wat men mooi vond, wie de opdracht gaf en wat die wilde uitstralen. Dat is geschiedenis, ook zonder één geschreven woord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag brengt je het minst bij de bedoeling van een schilderij als bron?",
        opties=[
            "was de verf duur?",
            "wie betaalde het werk, en waarom?",
            "voor welke plaats en welk publiek is het gemaakt?",
            "wat staat er bewust wel en niet op?",
        ],
        antwoord=0,
        uitleg="De prijs van de verf zegt hooguit iets over de rijkdom van de opdrachtgever. De drie andere vragen brengen je wel bij wat het werk wilde uitstralen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grootste verschil tussen de middeleeuwse en de renaissancekunst?",
        opties=[
            "de renaissance toont de wereld zoals het oog ze ziet, de middeleeuwen zoals de betekenis ze ordent",
            "de middeleeuwen kenden helemaal geen kunst, de renaissance vond ze opnieuw uit",
            "de renaissance gebruikte geen enkel godsdienstig onderwerp, de middeleeuwen alleen maar",
            "de middeleeuwen werkten enkel in marmer, de renaissance enkel in hout en verf",
        ],
        antwoord=0,
        uitleg="Op een middeleeuws paneel is de belangrijkste figuur het grootst, hoe ver hij ook staat. Het perspectief maakt daar een einde aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Renaissance en barok zijn twee namen voor dezelfde stijl uit dezelfde eeuw.",
        antwoord=False,
        uitleg="De renaissance bloeit rond 1500, de barok vanaf ongeveer 1600. Daartussen liggen de Reformatie en de godsdienstoorlogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de vroegmoderne tijd een breuk met de middeleeuwen?",
        opties=[
            "mens- en wereldbeeld, geloof, wetenschap en kunst veranderen alle vier tegelijk",
            "de bevolking van Europa verdween bijna volledig in de loop van die eeuwen",
            "er werd in die eeuwen niets meer gebouwd, noch kerken noch stadhuizen",
            "het Latijn werd overal afgeschaft als taal van de Kerk en van de geleerden",
        ],
        antwoord=0,
        uitleg="Toch blijft veel doorlopen: de standen, de landbouw, de macht van de vorsten. Een breuk in het ene domein is nog geen breuk in alle.",
    ),
]
