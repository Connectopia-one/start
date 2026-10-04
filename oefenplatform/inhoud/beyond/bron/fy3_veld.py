# -*- coding: utf-8 -*-
"""De wet van Coulomb en het elektrisch veld — 🌍 Beyond, fysica.

Deel 1 gaat over de kracht zelf: dat ze een veldkracht is, hoe ze met het
kwadraat van de afstand afneemt, en hoe je met de wet van Coulomb rekent, ook
als er meer dan twee ladingen in het spel zijn. Deel 2 gaat over het veld
eromheen: de veldsterkte, de drie patronen die de fiche noemt (radiaal,
dipool en homogeen), de zin van de veldlijnen, en de schermwerking van een
holle geleider.

De fiche vraagt om veldlijnen te tekenen; dat kan hier niet, dus vragen de
vragen naar het patroon in woorden. De rekenvragen geven de nodige waarden
mee, want op het examen staan de formules en de constanten in een bijlage.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat de elektrische kracht een veldkracht is?",
        opties=[
            "ze werkt op afstand, zonder dat er contact nodig is",
            "ze werkt enkel als de twee voorwerpen elkaar raken",
            "ze werkt enkel in een leeg vat zonder lucht erin",
            "ze werkt altijd even sterk, hoe ver je ook gaat",
        ],
        antwoord=0,
        uitleg="De zwaartekracht en de magnetische kracht zijn ook veldkrachten. Het veld "
        "is de manier waarop die kracht zich door de ruimte laat voelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Coulomb over het verband tussen de kracht en de afstand?",
        opties=[
            "de kracht is omgekeerd evenredig met het kwadraat van r",
            "de kracht is omgekeerd evenredig met de afstand r zelf",
            "de kracht is recht evenredig met het kwadraat van r",
            "de kracht blijft gelijk hoe groot de afstand ook wordt",
        ],
        antwoord=0,
        uitleg="In de formule staat r² in de noemer. Twee keer zo ver betekent dus vier "
        "keer zo weinig kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee puntladingen trekken elkaar aan met 8 N. Je verdubbelt de afstand. Hoe groot is de kracht dan?",
        opties=[
            "2 N",
            "4 N",
            "8 N",
            "16 N",
        ],
        antwoord=0,
        uitleg="De kracht gaat met het kwadraat van de afstand: twee keer verder is vier "
        "keer minder. 8 gedeeld door 4 is 2 newton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee puntladingen stoten elkaar af met 6 N. Je verdrievoudigt één van de twee ladingen. Hoe groot is de kracht?",
        opties=[
            "18 N",
            "6 N",
            "2 N",
            "54 N",
        ],
        antwoord=0,
        uitleg="De kracht is recht evenredig met elk van de twee ladingen. Drie keer zo "
        "veel lading betekent dus drie keer zo veel kracht.",
    ),
    dict(
        type="waarofniet",
        vraag="De kracht die lading A op lading B uitoefent, is even groot als die van B op A.",
        antwoord=True,
        uitleg="Dat is de derde wet van Newton: actie en reactie. Ook al is de ene lading "
        "veel groter dan de andere, de twee krachten blijven even groot en tegengesteld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de coulombkracht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "gelijksoortige ladingen stoten elkaar af",
            "ongelijksoortige ladingen trekken elkaar aan",
            "gelijksoortige ladingen trekken elkaar aan",
            "de kracht hangt niet af van de grootte van de ladingen",
        ],
        antwoord=[0, 1],
        uitleg="Het teken van de ladingen bepaalt de zin van de kracht, hun grootte bepaalt "
        "hoe sterk ze is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht tussen twee puntladingen, naar de man die ze beschreef?",
        antwoord=["coulombkracht", "de coulombkracht", "coulomb"],
        uitleg="Men spreekt ook gewoon van de elektrische kracht. De eenheid van lading "
        "draagt dezelfde naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie gelijke positieve ladingen staan op één rechte lijn, op gelijke afstand van elkaar. Welke kracht voelt de middelste?",
        opties=[
            "geen enkele, want de twee krachten heffen elkaar op",
            "een kracht naar links, want die buur staat het dichtst",
            "een kracht naar rechts, want die buur duwt het hardst",
            "een kracht loodrecht op de lijn, naar boven toe",
        ],
        antwoord=0,
        uitleg="De twee buren zijn even groot en staan even ver, dus duwen ze even hard in "
        "tegengestelde zin. De resulterende kracht op de middelste is dan nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de resulterende kracht op een lading die door twee andere ladingen beïnvloed wordt?",
        opties=[
            "je telt de twee krachten op als vectoren",
            "je telt de twee grootheden gewoon bij elkaar op",
            "je neemt telkens de grootste van de twee krachten",
            "je trekt de kleinste kracht van de grootste af",
        ],
        antwoord=0,
        uitleg="Een kracht heeft een richting en een zin, dus moet je ze als vectoren "
        "samenstellen. Alleen als de twee op één lijn liggen, volstaat optellen of "
        "aftrekken.",
    ),
    dict(
        type="waarofniet",
        vraag="De wet van Coulomb en de gravitatiewet hebben dezelfde vorm.",
        antwoord=True,
        uitleg="Beide hebben het product van twee grootheden in de teller en het kwadraat "
        "van de afstand in de noemer. Het verschil is dat de zwaartekracht altijd "
        "aantrekt en de elektrische kracht ook kan afstoten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden staan in de wet van Coulomb? Kruis alles aan wat juist is.",
        opties=[
            "de grootte van de beide ladingen",
            "de afstand tussen de twee ladingen",
            "de massa van de twee geladen voorwerpen",
            "de temperatuur van de twee voorwerpen",
        ],
        antwoord=[0, 1],
        uitleg="Massa en temperatuur spelen geen rol. Wel staat er een constante k in, en "
        "die hangt af van de stof tussen de twee ladingen.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je een kracht uit?",
        antwoord=["newton", "N", "de newton"],
        uitleg="Het symbool is N. Eén newton is ongeveer de kracht waarmee de aarde aan "
        "een appel van honderd gram trekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee ladingen staan in twee hoekpunten van een vierkant. Waarom reken je de kracht op een derde lading in een derde hoekpunt niet zomaar op door op te tellen?",
        opties=[
            "de twee krachten wijzen in een andere richting",
            "de twee krachten zijn altijd precies even groot",
            "de afstand tot beide ladingen is altijd dezelfde",
            "de ladingen in een vierkant werken niet op elkaar in",
        ],
        antwoord=0,
        uitleg="Bij een vierkant staan de twee verbindingslijnen loodrecht op elkaar of "
        "onder een hoek van 45 graden. Je moet de krachten dus eerst in vectoren "
        "ontbinden of met een driehoek samenstellen.",
    ),
    dict(
        type="waarofniet",
        vraag="De elektrische kracht tussen twee ladingen is sterker in water dan in lucht.",
        antwoord=False,
        uitleg="Net omgekeerd: water verzwakt de kracht sterk, want zijn polaire moleculen "
        "schermen de ladingen af. De constante in de wet van Coulomb hangt daarom af van "
        "de stof ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee puntladingen van 2 µC en 3 µC trekken of stoten elkaar. Wat gebeurt er als je beide verdubbelt?",
        opties=[
            "de kracht wordt vier keer zo groot",
            "de kracht wordt twee keer zo groot",
            "de kracht wordt acht keer zo groot",
            "de kracht blijft precies even groot",
        ],
        antwoord=0,
        uitleg="In de teller staat het product van de twee ladingen, dus twee maal twee is "
        "vier. De afstand is niet veranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar is de kracht van een geladen bol op een puntlading het grootst?",
        opties=[
            "vlak bij het oppervlak van de bol",
            "precies in het midden van de bol zelf",
            "op grote afstand van de bol vandaan",
            "overal rond de bol even groot gespreid",
        ],
        antwoord=0,
        uitleg="Buiten de bol werkt ze alsof alle lading in het middelpunt zat, dus neemt "
        "ze af met het kwadraat van de afstand. Dicht bij het oppervlak is ze daarom het "
        "sterkst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een lading die zo klein is dat je ze als één punt mag beschouwen?",
        antwoord=["puntlading", "een puntlading", "puntladingen"],
        uitleg="De wet van Coulomb is in die vorm voor puntladingen geschreven. Voor een "
        "geladen bol geldt ze ook, zolang je buiten de bol blijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee ladingen die elkaar afstoten, moeten allebei positief zijn.",
        antwoord=False,
        uitleg="Twee negatieve ladingen stoten elkaar even goed af. Afstoting wijst op "
        "gelijksoortige ladingen, niet noodzakelijk op positieve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de constante k in de wet van Coulomb zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze hangt af van de stof tussen de twee ladingen",
            "ze staat in de bijlage die je op het examen krijgt",
            "ze is voor elke stof precies even groot",
            "ze wordt kleiner naarmate de ladingen groter zijn",
        ],
        antwoord=[0, 1],
        uitleg="In lucht is ze ongeveer 9·10⁹ N·m²/C². In water ligt ze tientallen keren "
        "lager, en daarom werken ionen in water veel minder hard op elkaar in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een neutraal voorwerp toch aangetrokken door een geladen staaf?",
        opties=[
            "de dichtste kant is tegengesteld geladen en trekt dus harder",
            "de dichtste kant is gelijk geladen en duwt dus minder hard",
            "het hele voorwerp wordt door de staaf tegengesteld geladen",
            "de staaf geeft wat lading af en trekt die daarna terug aan",
        ],
        antwoord=0,
        uitleg="Door influentie of polarisatie komt de tegengestelde lading het dichtst bij "
        "de staaf. Omdat de kracht met r² afneemt, wint die aantrekking het van de "
        "afstoting verderop.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de elektrische veldsterkte in een punt?",
        opties=[
            "de kracht per eenheid van lading in dat punt",
            "de kracht op een lading van één coulomb per meter",
            "de arbeid die nodig is om er een lading te brengen",
            "de lading die er per seconde langs stroomt",
        ],
        antwoord=0,
        uitleg="Je deelt de kracht op een proeflading door de grootte van die lading. Zo "
        "krijg je een eigenschap van het punt zelf, los van de lading die je erin zet.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de elektrische veldsterkte uit?",
        antwoord=["N/C", "newton per coulomb", "V/m"],
        uitleg="Newton per coulomb, want ze is kracht gedeeld door lading. Volt per meter "
        "is daarmee gelijkwaardig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het veldlijnenpatroon rond één positieve puntlading eruit?",
        opties=[
            "rechte lijnen die stervormig naar buiten wijzen",
            "rechte lijnen die stervormig naar binnen wijzen",
            "gesloten kringen rond de lading heen getekend",
            "evenwijdige lijnen die van links naar rechts lopen",
        ],
        antwoord=0,
        uitleg="Dat heet een radiaal veld. Bij een negatieve lading loopt hetzelfde patroon "
        "juist naar de lading toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het veld tussen twee geladen platen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de veldsterkte is er overal dezelfde",
            "de veldlijnen zijn recht en lopen parallel",
            "ze lopen van de positieve naar de negatieve plaat",
            "het veld is in het midden het sterkst",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zo'n veld heet homogeen, en dat betekent net overal even sterk. Alleen aan de "
        "randen van de platen wijken de lijnen af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het veld tussen twee ongelijknamige puntladingen?",
        antwoord=["dipoolveld", "een dipoolveld", "dipool"],
        uitleg="De veldlijnen vertrekken bij de positieve lading en komen bij de negatieve "
        "toe, in gebogen bogen. Rond één enkele lading heet het veld radiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de afspraak over de zin van de elektrische veldlijnen?",
        opties=[
            "ze lopen weg van de positieve en naar de negatieve lading",
            "ze lopen weg van de negatieve en naar de positieve lading",
            "ze lopen altijd van onder naar boven in de tekening",
            "ze lopen altijd in de zin waarin de kracht het grootst is",
        ],
        antwoord=0,
        uitleg="De zin is die van de kracht op een positieve proeflading. Op een negatieve "
        "lading werkt de kracht dus net de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het veld daar is.",
        antwoord=True,
        uitleg="De dichtheid van de lijnen is precies de manier waarop een tekening de "
        "veldsterkte weergeeft. Daarom lopen de lijnen dicht bij een lading dicht op "
        "elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een positieve lading zit in een punt waar het veld naar rechts wijst. Welke kant op werkt de kracht?",
        opties=[
            "naar rechts, in de zin van het veld",
            "naar links, dus tegen het veld in",
            "loodrecht op het veld, naar boven",
            "er werkt geen kracht op die lading",
        ],
        antwoord=0,
        uitleg="Op een positieve lading werkt de kracht in de zin van het veld. Op een "
        "negatieve lading werkt ze er juist tegenin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het veld van een puntlading zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het neemt af met het kwadraat van de afstand",
            "het hangt niet af van de proeflading die je erin zet",
            "het is overal rond de lading even sterk gespreid",
            "het wijst altijd naar de lading toe, wat haar teken ook is",
        ],
        antwoord=[0, 1],
        uitleg="De veldsterkte is een eigenschap van het punt zelf. Daarom staat er in haar "
        "formule enkel de lading die het veld maakt, en niet de lading die je erin brengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een punt is de veldsterkte 200 N/C. Welke kracht werkt er op een lading van 3 mC?",
        opties=[
            "0,6 N",
            "600 N",
            "67 N",
            "0,015 N",
        ],
        antwoord=0,
        uitleg="De kracht is de veldsterkte maal de lading: 200 maal 0,003 is 0,6 newton. "
        "Let op de omzetting van millicoulomb naar coulomb.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een lading van 5 µC werkt in een punt een kracht van 0,1 N. Hoe groot is de veldsterkte daar?",
        opties=[
            "20 000 N/C",
            "0,5 N/C",
            "500 N/C",
            "50 000 N/C",
        ],
        antwoord=0,
        uitleg="Deel de kracht door de lading: 0,1 gedeeld door 5·10⁻⁶ is 2·10⁴ newton per "
        "coulomb.",
    ),
    dict(
        type="waarofniet",
        vraag="In een homogeen veld is de kracht op een lading overal even groot.",
        antwoord=True,
        uitleg="Homogeen betekent dat de veldsterkte overal dezelfde is, en de kracht volgt "
        "daaruit. In een radiaal veld hangt ze wel af van waar je zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er van het elektrisch veld binnen in een geladen holle geleider?",
        opties=[
            "er is geen veld, want de ladingen heffen elkaar daar op",
            "het veld is daar juist het sterkst van allemaal",
            "het veld is er even sterk als vlak buiten de geleider",
            "het veld wijst er altijd naar het middelpunt toe",
        ],
        antwoord=0,
        uitleg="De lading zit volledig op het buitenoppervlak en verdeelt zich zo dat de "
        "bijdragen binnenin elkaar precies opheffen. Dat heet elektrische schermwerking.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een metalen omhulsel dat de binnenkant tegen een elektrisch veld afschermt?",
        antwoord=["kooi van Faraday", "faradaykooi", "kooi"],
        uitleg="Een auto met metalen koets werkt zo bij een blikseminslag. Ook de metalen "
        "mantel rond een kabel beschermt het signaal op die manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een auto een veilige plaats bij onweer?",
        opties=[
            "het metalen koetswerk leidt de lading rond de inzittenden",
            "de rubberen banden houden de bliksem volledig tegen",
            "de lucht in de auto geleidt de lading niet verder",
            "het glas van de ruiten weerkaatst de blikseminslag",
        ],
        antwoord=0,
        uitleg="De auto werkt als een kooi van Faraday: de lading blijft op de buitenkant "
        "en binnenin is er geen veld. De banden hebben er weinig mee te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee elektrische veldlijnen kunnen elkaar kruisen.",
        antwoord=False,
        uitleg="In een kruispunt zou het veld twee verschillende zinnen tegelijk hebben, en "
        "dat kan niet. Daarom snijden veldlijnen elkaar nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veldlijnenpatronen komen bij een elektrisch veld voor? Kruis alles aan wat juist is.",
        opties=[
            "het radiale veld rond een puntlading",
            "het homogene veld tussen twee platen",
            "het spiraalveld rond een draaiende lading",
            "het golvende veld tussen drie gelijke ladingen",
        ],
        antwoord=[0, 1],
        uitleg="Het derde patroon is het dipoolveld tussen twee ongelijknamige ladingen. "
        "Een spiraal- of golfveld bestaat in dit verband niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over elektrische veldlijnen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze vertrekken bij een positieve lading en eindigen bij een negatieve",
            "ze snijden elkaar nooit",
            "hoe dichter ze bij elkaar liggen, hoe sterker het veld",
            "ze lopen binnen een holle geleider van wand tot wand",
        ],
        antwoord=[0, 1, 2],
        uitleg="Binnen een holle geleider is het veld nul, dus lopen er geen lijnen. Dat is "
        "het gevolg van de kooi van Faraday.",
    ),
    dict(
        type="waarofniet",
        vraag="De veldsterkte tussen twee geladen platen wordt kleiner naarmate je dichter bij de positieve plaat komt.",
        antwoord=False,
        uitleg="Tussen twee platen is het veld homogeen, dus overal even sterk. Alleen bij "
        "een puntlading of een bol hangt de sterkte van de afstand af.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk symbool schrijf je de elektrische veldsterkte?",
        antwoord=["E", "de E", "E-vector"],
        uitleg="De elektrische kracht schrijf je met F. In de formule E is gelijk aan F "
        "gedeeld door Q zie je meteen hoe de twee samenhangen.",
    ),
]
