# -*- coding: utf-8 -*-
r"""De wet van Coulomb en het elektrisch veld — 🌍 Beyond, fysica.

Deel 1 gaat over de kracht zelf: dat ze een veldkracht is, hoe ze met het
kwadraat van de afstand afneemt, en hoe je met de wet van Coulomb rekent, ook
als er meer dan twee ladingen in het spel zijn. Deel 2 gaat over het veld
eromheen: de veldsterkte, de drie patronen die de fiche noemt (radiaal,
dipool en homogeen), de zin van de veldlijnen, en de schermwerking van een
holle geleider.

In echte wetenschappelijke notatie, tussen \( en \); zie
oefenplatform/lib/wiskunde.ts. De twee formules van dit thema:

    \[F = k\,\frac{|q_{1}\cdot q_{2}|}{r^{2}}\]   en   \[E = \frac{F}{q}\]

De fiche vraagt om veldlijnen te tekenen. Dat kan in een vraag niet, dus
vragen de vragen naar het patroon in woorden; in de leerbundel staan de vier
patronen wel getekend (zie svg.veldlijnen in leerbundels/bron/svg.py). De
rekenvragen geven de nodige waarden mee, want op het examen staan de formules
en de constanten in een bijlage.
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
        vraag=r"Welk verband tussen \(F\) en \(r\) staat in \(F=k\,\dfrac{|q_{1}q_{2}|}{r^{2}}\)?",
        opties=[
            r"\(F\sim\dfrac{1}{r^{2}}\)",
            r"\(F\sim\dfrac{1}{r}\)",
            r"\(F\sim r^{2}\)",
            r"\(F\) hangt niet van \(r\) af",
        ],
        antwoord=0,
        uitleg=r"\(r^{2}\) staat in de noemer, dus \(F\) is omgekeerd evenredig met het "
        r"kwadraat van de afstand: twee keer zo ver is vier keer zo weinig kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee puntladingen trekken elkaar aan met \(F=8{,}0\ \text{N}\). Je verdubbelt \(r\). Hoe groot is \(F\) dan?",
        opties=[
            r"\(2{,}0\ \text{N}\)",
            r"\(4{,}0\ \text{N}\)",
            r"\(8{,}0\ \text{N}\)",
            r"\(16\ \text{N}\)",
        ],
        antwoord=0,
        uitleg=r"\(F\sim\tfrac{1}{r^{2}}\), dus twee keer verder is vier keer minder: "
        r"\(\tfrac{8{,}0}{4}=2{,}0\ \text{N}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee puntladingen stoten elkaar af met \(F=6{,}0\ \text{N}\). Je vervangt \(q_{1}\) door \(3q_{1}\). Hoe groot is \(F\) dan?",
        opties=[
            r"\(18\ \text{N}\)",
            r"\(6{,}0\ \text{N}\)",
            r"\(2{,}0\ \text{N}\)",
            r"\(54\ \text{N}\)",
        ],
        antwoord=0,
        uitleg=r"\(F\) is recht evenredig met elk van de twee ladingen, want ze staan beide "
        r"in de teller. Drie keer \(q_{1}\) geeft dus drie keer \(F\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De kracht van lading A op lading B is even groot als die van B op A.",
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
            r"de grootte van \(q_{1}\) en \(q_{2}\)",
            r"de afstand \(r\) ertussen",
            r"de massa \(m\) van de twee voorwerpen",
            r"de temperatuur \(T\) van de twee voorwerpen",
        ],
        antwoord=[0, 1],
        uitleg=r"Massa en temperatuur komen in \(F=k\,\dfrac{|q_{1}q_{2}|}{r^{2}}\) niet voor. "
        r"Wel staat er een constante \(k\) in, en die hangt af van de stof ertussen.",
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
        vraag=r"Twee puntladingen zijn \(q_{1}=2\ \mu\text{C}\) en \(q_{2}=3\ \mu\text{C}\). Wat gebeurt er met \(F\) als je beide verdubbelt?",
        opties=[
            "de kracht wordt vier keer zo groot",
            "de kracht wordt twee keer zo groot",
            "de kracht wordt acht keer zo groot",
            "de kracht blijft precies even groot",
        ],
        antwoord=0,
        uitleg=r"In de teller staat \(q_{1}\cdot q_{2}\), dus \(2\cdot 2=4\). \(r\) is niet veranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(F\) tussen \(q_{1}=2{,}0\ \mu\text{C}\) en \(q_{2}=3{,}0\ \mu\text{C}\) "
        r"op \(r=0{,}30\ \text{m}\). Neem \(k=8{,}99\cdot 10^{9}\ \text{N}\,\text{m}^{2}\text{/C}^{2}\).",
        opties=[
            r"\(0{,}60\ \text{N}\)",
            r"\(0{,}18\ \text{N}\)",
            r"\(6{,}0\ \text{N}\)",
            r"\(1{,}8\cdot 10^{-4}\ \text{N}\)",
        ],
        antwoord=0,
        uitleg=r"\(F=8{,}99\cdot 10^{9}\cdot\dfrac{2{,}0\cdot 10^{-6}\cdot 3{,}0\cdot 10^{-6}}"
        r"{0{,}30^{2}}=\dfrac{5{,}39\cdot 10^{-2}}{0{,}09}\approx 0{,}60\ \text{N}\). "
        r"Wie \(r\) vergeet te kwadrateren komt op \(0{,}18\ \text{N}\) uit.",
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
        uitleg=r"In lucht is \(k\approx 8{,}99\cdot 10^{9}\ \text{N}\,\text{m}^{2}\text{/C}^{2}\). "
        r"In water ligt ze tientallen keren lager, en daarom werken ionen in water veel "
        r"minder hard op elkaar in.",
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
        uitleg=r"Door influentie of polarisatie komt de tegengestelde lading het dichtst bij "
        r"de staaf. Omdat \(F\sim\tfrac{1}{r^{2}}\), wint die aantrekking het van de "
        r"afstoting verderop.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de elektrische veldsterkte \(E\) in een punt?",
        opties=[
            r"\(E=\dfrac{F}{q}\), de kracht per eenheid van lading",
            r"\(E=F\cdot q\), de kracht maal de lading",
            r"\(E=\dfrac{W}{q}\), de arbeid per eenheid van lading",
            r"\(E=\dfrac{q}{t}\), de lading per seconde",
        ],
        antwoord=0,
        uitleg=r"Je deelt de kracht op een proeflading door die lading zelf. Zo krijg je een "
        r"eigenschap van het punt, los van wat je erin zet. \(\tfrac{W}{q}\) is de "
        r"potentiaal en \(\tfrac{q}{t}\) is de stroomsterkte.",
    ),
    dict(
        type="invultekst",
        vraag=r"In welke eenheid druk je \(E\) uit? Schrijf ze als een breuk met een schuine streep.",
        antwoord=["N/C", "newton per coulomb", "V/m"],
        uitleg=r"Newton per coulomb, want \(E=\tfrac{F}{q}\). "
        r"\(1\ \text{N/C}=1\ \text{V/m}\), dus volt per meter is evengoed juist.",
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
        vraag=r"Een positieve lading zit in een punt waar \(\vec{E}\) naar rechts wijst. Welke kant op werkt \(\vec{F}\)?",
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
            r"\(E\sim\dfrac{1}{r^{2}}\)",
            r"\(E\) hangt niet af van de proeflading die je erin zet",
            r"\(E\) is overal rond de lading even groot",
            r"\(\vec{E}\) wijst altijd naar de lading toe, wat haar teken ook is",
        ],
        antwoord=[0, 1],
        uitleg="De veldsterkte is een eigenschap van het punt zelf. Daarom staat er in haar "
        "formule enkel de lading die het veld maakt, en niet de lading die je erin brengt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een punt is \(E=200\ \text{N/C}\). Welke kracht werkt er op \(q=3\ \text{mC}\)?",
        opties=[
            r"\(0{,}6\ \text{N}\)",
            r"\(600\ \text{N}\)",
            r"\(67\ \text{N}\)",
            r"\(0{,}015\ \text{N}\)",
        ],
        antwoord=0,
        uitleg=r"Uit \(E=\tfrac{F}{q}\) volgt \(F=E\cdot q=200\cdot 3\cdot 10^{-3}=0{,}6\ \text{N}\). "
        r"Wie de millicoulomb vergeet om te zetten komt op \(600\ \text{N}\) uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op \(q=5\ \mu\text{C}\) werkt in een punt een kracht \(F=0{,}1\ \text{N}\). Hoe groot is \(E\)?",
        opties=[
            r"\(2{,}0\cdot 10^{4}\ \text{N/C}\)",
            r"\(0{,}5\ \text{N/C}\)",
            r"\(5{,}0\cdot 10^{2}\ \text{N/C}\)",
            r"\(5{,}0\cdot 10^{4}\ \text{N/C}\)",
        ],
        antwoord=0,
        uitleg=r"\(E=\dfrac{F}{q}=\dfrac{0{,}1}{5\cdot 10^{-6}}=2{,}0\cdot 10^{4}\ \text{N/C}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een homogeen veld is \(F\) op een gegeven lading overal even groot.",
        antwoord=True,
        uitleg=r"Homogeen betekent dat \(E\) overal dezelfde is, en \(F=E\cdot q\) volgt "
        r"daaruit. In een radiaal veld hangt \(E\) wel af van waar je zit.",
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
        vraag=r"Hoe groot is \(E\) op \(r=0{,}10\ \text{m}\) van een puntlading \(q=5{,}0\ \text{nC}\)? "
        r"Neem \(k=8{,}99\cdot 10^{9}\ \text{N}\,\text{m}^{2}\text{/C}^{2}\).",
        opties=[
            r"\(4{,}5\cdot 10^{3}\ \text{N/C}\)",
            r"\(4{,}5\cdot 10^{2}\ \text{N/C}\)",
            r"\(4{,}5\cdot 10^{4}\ \text{N/C}\)",
            r"\(45\ \text{N/C}\)",
        ],
        antwoord=0,
        uitleg=r"\(E=k\dfrac{|q|}{r^{2}}=8{,}99\cdot 10^{9}\cdot\dfrac{5{,}0\cdot 10^{-9}}"
        r"{0{,}10^{2}}=\dfrac{45}{0{,}010}\approx 4{,}5\cdot 10^{3}\ \text{N/C}\). "
        r"Wie \(r\) niet kwadrateert komt op \(4{,}5\cdot 10^{2}\ \text{N/C}\) uit.",
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
            "het dipoolveld tussen twee ongelijknamige ladingen",
            "het spiraalveld rond een draaiende lading",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat zijn de drie patronen die je moet kennen. Een spiraalveld bestaat in dit "
        "verband niet; een spiraal hoort bij het magnetisch veld rond een spoel.",
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
        vraag=r"\(E\) tussen twee geladen platen wordt kleiner naarmate je dichter bij de positieve plaat komt.",
        antwoord=False,
        uitleg=r"Tussen twee platen is het veld homogeen, dus \(E\) is overal even groot. "
        r"Alleen bij een puntlading of een bol hangt \(E\) van \(r\) af.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk symbool schrijf je de elektrische veldsterkte? Schrijf de letter.",
        antwoord=["E", "de E", "E-vector"],
        uitleg=r"De kracht schrijf je met \(F\) en de lading met \(q\). In \(E=\dfrac{F}{q}\) "
        r"zie je meteen hoe de drie samenhangen.",
    ),
]
