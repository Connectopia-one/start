# -*- coding: utf-8 -*-
"""Elektrodynamica: stroom, weerstand en schakelingen — 🌍 Beyond, fysica.

Deel 1 gaat over de grootheden zelf: stroomsterkte, spanning en weerstand, de
wet van Ohm, het elektrisch schema met zijn symbolen, en hoe je een
ampèremeter en een voltmeter aansluit. Deel 2 gaat over het rekenwerk in
schakelingen: serie, parallel en de gemengde schakeling van drie weerstanden
die de fiche uitdrukkelijk noemt.

De vragen geven telkens hele getallen, zodat het kind de redenering kan tonen
zonder rekentoestel. Bij een gemengde schakeling zegt de vraag erbij welke
twee weerstanden samen staan, want een schema tekenen kan hier niet.

De formules staan in notatie, tussen \\( en \\): I = dq/dt, U = R I,
R = rho l / A, de som voor serie en de som van de omgekeerden voor parallel.
Dat vroeg Enya Vermeyen op 10 oktober 2026: een leerling moet die notatie
kunnen lezen, dus staat ze in de vraag en niet enkel in de uitleg.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de elektrische stroomsterkte \(I\)?",
        opties=[
            "de lading die per seconde door een doorsnede gaat",
            "de energie die per seconde door een draad gaat",
            "het aantal elektronen dat in de draad aanwezig is",
            "de snelheid waarmee één elektron zich voortbeweegt",
        ],
        antwoord=0,
        uitleg=r"\(I=\dfrac{\Delta q}{\Delta t}\), in ampère: "
        r"\(1\ \text{A}=1\ \text{C/s}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"In welke eenheid druk je de stroomsterkte \(I\) uit?",
        antwoord=["ampère", "A", "ampere"],
        uitleg=r"Het symbool van de eenheid is \(\text{A}\), dat van de grootheid \(I\). "
        r"\(1\ \text{A}=1\ \text{C/s}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Ohm?",
        opties=[
            r"\(R=\dfrac{U}{I}\)",
            r"\(R=U\cdot I\)",
            r"\(R=\dfrac{I}{U}\)",
            r"\(R=\dfrac{U}{P}\)",
        ],
        antwoord=0,
        uitleg=r"\(R=\dfrac{U}{I}\), of omgekeerd \(U=R\,I\). Zet je er meer spanning op, "
        r"dan loopt er bij dezelfde \(R\) evenredig meer stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Over een weerstand staat \(12\ \text{V}\) en er loopt \(3{,}0\ \text{A}\) door. "
        r"Hoe groot is \(R\)?",
        opties=[
            r"\(4{,}0\ \Omega\)",
            r"\(36\ \Omega\)",
            r"\(0{,}25\ \Omega\)",
            r"\(15\ \Omega\)",
        ],
        antwoord=0,
        uitleg=r"\(R=\dfrac{U}{I}=\dfrac{12}{3{,}0}=4{,}0\ \Omega\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Door een weerstand van \(25\ \Omega\) loopt \(0{,}40\ \text{A}\). Welke spanning "
        r"staat erover?",
        opties=[
            r"\(10\ \text{V}\)",
            r"\(62{,}5\ \text{V}\)",
            r"\(0{,}016\ \text{V}\)",
            r"\(25{,}4\ \text{V}\)",
        ],
        antwoord=0,
        uitleg=r"\(U=R\,I=25\cdot 0{,}40=10\ \text{V}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"In welke eenheid druk je de elektrische weerstand \(R\) uit?",
        antwoord=["ohm", "Ω", "de ohm"],
        uitleg=r"Het symbool is de Griekse hoofdletter \(\Omega\): "
        r"\(1\ \Omega=1\ \text{V/A}\).",
    ),
    dict(
        type="waarofniet",
        vraag="Een ampèremeter zet je in serie met het onderdeel waarvan je de stroom meet.",
        antwoord=True,
        uitleg="De stroom moet er dan ook echt door. Een voltmeter zet je er juist "
        "parallel over, want die meet het verschil tussen twee punten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een goede ampèremeter een heel kleine eigen weerstand?",
        opties=[
            "anders verandert hij de stroom die hij wil meten",
            "anders geeft hij een te kleine spanning weer",
            "anders wordt hij bij een grote stroom te koud",
            "anders meet hij de spanning in plaats van de stroom",
        ],
        antwoord=0,
        uitleg="Hij staat in serie, dus telt zijn weerstand bij die van de kring. Een "
        "voltmeter heeft om dezelfde reden juist een heel grote weerstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen hebben een eigen symbool in een elektrisch schema? Kruis alles aan wat juist is.",
        opties=[
            "de schakelaar",
            "de voltmeter",
            "de kleur van de draad",
            "de lengte van de kring",
        ],
        antwoord=[0, 1],
        uitleg="Ook de spanningsbron, de weerstand, de lamp en de ampèremeter hebben hun "
        "eigen symbool. Een schema toont de verbindingen, niet de afmetingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen gelijkstroom en wisselstroom?",
        opties=[
            "gelijkstroom loopt altijd in dezelfde zin",
            "gelijkstroom loopt altijd met dezelfde snelheid",
            "gelijkstroom loopt enkel door een metalen draad",
            "gelijkstroom heeft geen spanningsbron nodig",
        ],
        antwoord=0,
        uitleg="Een batterij levert gelijkstroom, het stopcontact wisselstroom. Bij "
        "wisselstroom keert de zin voortdurend om.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgesproken zin van de stroom is die van de positieve lading, dus van plus naar min.",
        antwoord=True,
        uitleg="De elektronen bewegen in werkelijkheid net de andere kant op. Die afspraak "
        "dateert van voor men wist welk deeltje er beweegt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarvan hangt \(R\) van een draad af? Kruis alles aan wat juist is.",
        opties=[
            r"van de lengte \(\ell\)",
            r"van de doorsnede \(A\)",
            r"van de spanning \(U\) erop",
            r"van de stroom \(I\) erdoor",
        ],
        antwoord=[0, 1],
        uitleg=r"\(R=\rho\,\dfrac{\ell}{A}\), met \(\rho\) de soortelijke weerstand van de "
        r"stof; ook de temperatuur speelt mee. \(U\) en \(I\) bepalen \(R\) niet, ze volgen "
        r"er juist uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het toestel dat de spanning tussen twee punten meet?",
        antwoord=["voltmeter", "een voltmeter", "de voltmeter"],
        uitleg="Je zet hem parallel over het onderdeel. De ampèremeter zet je juist in "
        "serie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een draad warm als er stroom door loopt?",
        opties=[
            "de elektronen botsen tegen de atomen van het rooster",
            "de elektronen wrijven langs de buitenkant van de draad",
            "de spanningsbron stuurt warmte mee de draad in",
            "de lucht rond de draad wordt door de lading geduwd",
        ],
        antwoord=0,
        uitleg="Bij elke botsing geven de elektronen wat energie af aan het rooster, en dat "
        "trilt heviger. Dat is precies wat weerstand betekent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schakelaar in open stand laat de stroom gewoon verder lopen.",
        antwoord=False,
        uitleg="Een open schakelaar onderbreekt de kring, en dan loopt er nergens stroom. "
        "De stroom heeft een gesloten weg nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met \(I\) als je bij gelijke \(U\) de weerstand verdubbelt?",
        opties=[
            "de stroom wordt half zo groot",
            "de stroom wordt twee keer zo groot",
            "de stroom blijft precies even groot",
            "de stroom wordt vier keer zo klein",
        ],
        antwoord=0,
        uitleg=r"\(I=\dfrac{U}{R}\): bij vaste \(U\) zijn \(I\) en \(R\) omgekeerd evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een lamp van \(6{,}0\ \Omega\) staat op een bron van \(9{,}0\ \text{V}\). Hoeveel "
        r"stroom loopt er?",
        opties=[
            r"\(1{,}5\ \text{A}\)",
            r"\(54\ \text{A}\)",
            r"\(0{,}67\ \text{A}\)",
            r"\(15\ \text{A}\)",
        ],
        antwoord=0,
        uitleg=r"\(I=\dfrac{U}{R}=\dfrac{9{,}0}{6{,}0}=1{,}5\ \text{A}\).",
    ),
    dict(
        type="waarofniet",
        vraag="In een stroomkring worden de elektronen door de draad opgebruikt.",
        antwoord=False,
        uitleg="Er verdwijnt geen enkel elektron: er loopt er evenveel terug naar de bron "
        "als eruit vertrekt. Wat opgebruikt wordt, is energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de wet van Ohm zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"\(U=R\,I\)",
            r"bij gelijke \(U\) geeft een grotere \(R\) een kleinere \(I\)",
            r"ze geldt voor een \(R\) die niet verandert",
            r"\(R\) van een draad hangt af van de \(U\) die je aanlegt",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"\(R\) is een eigenschap van de draad zelf, niet van de bron. Een weerstand "
        r"waarvoor \(U=R\,I\) met een vaste \(R\) opgaat, heet een ohmse weerstand; een "
        r"gloeilamp is dat bijvoorbeeld niet, want warm is haar \(R\) groter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een tekening van een stroomkring met symbolen in plaats van voorwerpen?",
        antwoord=["elektrisch schema", "schema", "een schema"],
        uitleg="Het toont welke onderdelen met elkaar verbonden zijn. De werkelijke plaats "
        "of lengte van de draden doet er niet toe.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor de stroomsterkte in een serieschakeling?",
        opties=[
            "ze is in elk onderdeel even groot",
            "ze verdeelt zich over de onderdelen",
            "ze is in het laatste onderdeel het kleinst",
            "ze is in het eerste onderdeel het grootst",
        ],
        antwoord=0,
        uitleg="Er is maar één weg, dus moet alles er overal door. De spanning verdeelt "
        "zich wel over de onderdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt er in een parallelschakeling voor de spanning en de stroom? Kruis alles aan wat juist is.",
        opties=[
            "over elke tak staat dezelfde spanning",
            "de stromen van de takken tellen samen tot de hoofdstroom",
            "door de kleinste weerstand loopt de grootste stroom",
            "door elke tak loopt dezelfde stroom",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dezelfde stroom door alles hoort bij een serieschakeling. Elke tak heeft hier "
        "zijn eigen weg naar de bron.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee weerstanden van \(4{,}0\ \Omega\) en \(6{,}0\ \Omega\) staan in serie. Hoe "
        r"groot is \(R_{v}\)?",
        opties=[
            r"\(10\ \Omega\)",
            r"\(2{,}4\ \Omega\)",
            r"\(24\ \Omega\)",
            r"\(5{,}0\ \Omega\)",
        ],
        antwoord=0,
        uitleg=r"\(R_{v}=R_{1}+R_{2}=4{,}0+6{,}0=10\ \Omega\). In serie is \(R_{v}\) altijd "
        r"groter dan de grootste.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee weerstanden van \(4{,}0\ \Omega\) en \(6{,}0\ \Omega\) staan parallel. Hoe "
        r"groot is \(R_{v}\)?",
        opties=[
            r"\(2{,}4\ \Omega\)",
            r"\(10\ \Omega\)",
            r"\(5{,}0\ \Omega\)",
            r"\(24\ \Omega\)",
        ],
        antwoord=0,
        uitleg=r"\(\dfrac{1}{R_{v}}=\dfrac{1}{4{,}0}+\dfrac{1}{6{,}0}\), of voor twee "
        r"weerstanden korter \(R_{v}=\dfrac{R_{1}R_{2}}{R_{1}+R_{2}}=\dfrac{24}{10}="
        r"2{,}4\ \Omega\). Parallel ligt \(R_{v}\) altijd onder de kleinste.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de ene weerstand die je in de plaats van een hele schakeling mag denken?",
        antwoord=["vervangingsweerstand", "substitutieweerstand", "vervangweerstand"],
        uitleg="Ze geeft bij dezelfde spanning dezelfde totale stroom. Daarmee reken je een "
        "schakeling stap voor stap uit.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee gelijke weerstanden parallel geven samen \(\tfrac{R}{2}\).",
        antwoord=True,
        uitleg=r"Twee van \(10\ \Omega\) geven \(5{,}0\ \Omega\). Bij \(n\) gelijke "
        r"weerstanden parallel is \(R_{v}=\dfrac{R}{n}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Drie weerstanden van \(2{,}0\ \Omega\), \(3{,}0\ \Omega\) en \(5{,}0\ \Omega\) "
        r"staan in serie op \(20\ \text{V}\). Hoeveel stroom loopt er?",
        opties=[
            r"\(2{,}0\ \text{A}\)",
            r"\(10\ \text{A}\)",
            r"\(4{,}0\ \text{A}\)",
            r"\(0{,}50\ \text{A}\)",
        ],
        antwoord=0,
        uitleg=r"\(R_{v}=10\ \Omega\), dus \(I=\dfrac{20}{10}=2{,}0\ \text{A}\). Door elke "
        r"weerstand loopt diezelfde \(2{,}0\ \text{A}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde serieschakeling met \(I=2{,}0\ \text{A}\): welke spanning staat er over "
        r"de \(3{,}0\ \Omega\)?",
        opties=[
            r"\(6{,}0\ \text{V}\)",
            r"\(20\ \text{V}\)",
            r"\(3{,}0\ \text{V}\)",
            r"\(1{,}5\ \text{V}\)",
        ],
        antwoord=0,
        uitleg=r"\(U=R\,I=3{,}0\cdot 2{,}0=6{,}0\ \text{V}\). De drie deelspanningen "
        r"\(4{,}0\), \(6{,}0\) en \(10\ \text{V}\) zijn samen weer \(20\ \text{V}\).",
    ),
    dict(
        type="waarofniet",
        vraag="In een serieschakeling is de som van de deelspanningen groter dan de bronspanning.",
        antwoord=False,
        uitleg="Ze is er juist precies gelijk aan. De energie die een lading bij de bron "
        "krijgt, geeft ze onderweg stuk voor stuk af, en meer dan dat kan ze niet "
        "afgeven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee weerstanden van \(6{,}0\ \Omega\) en \(12\ \Omega\) staan parallel op "
        r"\(24\ \text{V}\). Hoeveel stroom levert de bron?",
        opties=[
            r"\(6{,}0\ \text{A}\)",
            r"\(4{,}0\ \text{A}\)",
            r"\(2{,}0\ \text{A}\)",
            r"\(1{,}33\ \text{A}\)",
        ],
        antwoord=0,
        uitleg=r"\(I_{1}=\dfrac{24}{6{,}0}=4{,}0\ \text{A}\) en \(I_{2}=\dfrac{24}{12}="
        r"2{,}0\ \text{A}\), samen \(6{,}0\ \text{A}\). Dat klopt met \(R_{v}=4{,}0\ \Omega\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een parallelschakeling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"\(I=I_{1}+I_{2}\)",
            r"\(R_{v}\) is kleiner dan de kleinste weerstand",
            r"\(U=U_{1}+U_{2}\)",
            r"\(R_{v}=R_{1}+R_{2}\)",
        ],
        antwoord=[0, 1],
        uitleg="De twee laatste gelden juist voor een serieschakeling. Elke tak die je "
        "bijzet, maakt de totale weerstand kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijven de andere lampen branden als er in een parallelschakeling één lamp stukgaat?",
        opties=[
            "elke lamp heeft haar eigen weg naar de bron",
            "de andere lampen nemen de stroom van die lamp over",
            "een parallelschakeling heeft geen gesloten kring nodig",
            "de bron verhoogt dan vanzelf haar spanning een beetje",
        ],
        antwoord=0,
        uitleg="Er zijn evenveel gesloten kringen als takken. In een serieschakeling is er "
        "maar één weg, en daar valt alles uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe staan de lampen geschakeld als één kapotte lamp de hele reeks dooft?",
        antwoord=["in serie", "serie", "serieschakeling"],
        uitleg="De kring is dan onderbroken, dus loopt er nergens nog stroom. Parallel "
        "blijft de rest wel branden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een weerstand van \(10\ \Omega\) staat in serie met twee parallelle weerstanden van "
        r"elk \(20\ \Omega\). Hoe groot is \(R_{v}\)?",
        opties=[
            r"\(20\ \Omega\)",
            r"\(50\ \Omega\)",
            r"\(30\ \Omega\)",
            r"\(10\ \Omega\)",
        ],
        antwoord=0,
        uitleg=r"De twee parallelle geven \(\dfrac{20}{2}=10\ \Omega\), en die staan in serie "
        r"met de eerste: \(10+10=20\ \Omega\). Werk bij een gemengde schakeling altijd van "
        r"binnen naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Die schakeling staat op \(40\ \text{V}\). Hoeveel stroom levert de bron?",
        opties=[
            r"\(2{,}0\ \text{A}\)",
            r"\(4{,}0\ \text{A}\)",
            r"\(1{,}0\ \text{A}\)",
            r"\(0{,}50\ \text{A}\)",
        ],
        antwoord=0,
        uitleg=r"\(I=\dfrac{U}{R_{v}}=\dfrac{40}{20}=2{,}0\ \text{A}\). Die hele stroom gaat "
        r"door de \(10\ \Omega\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde schakeling: welke spanning staat er over het parallelle stuk?",
        opties=[
            r"\(20\ \text{V}\)",
            r"\(40\ \text{V}\)",
            r"\(10\ \text{V}\)",
            r"\(4{,}0\ \text{V}\)",
        ],
        antwoord=0,
        uitleg=r"Over de \(10\ \Omega\) staat \(10\cdot 2{,}0=20\ \text{V}\), dus blijft er "
        r"van de \(40\ \text{V}\) nog \(20\ \text{V}\) over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een gemengde schakeling reken je eerst het parallelle stuk uit en pas daarna de serie.",
        antwoord=True,
        uitleg="Je vervangt het parallelle stuk door één weerstand en houdt zo een gewone "
        "serieschakeling over. Van binnen naar buiten werken houdt het overzichtelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een serieschakeling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"door elke weerstand loopt dezelfde \(I\)",
            r"\(U=U_{1}+U_{2}+U_{3}\)",
            r"\(R_{v}=R_{1}+R_{2}+R_{3}\)",
            "valt één weerstand weg, dan blijft de rest werken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Valt er één weg, dan is de kring open en staat alles stil. Dat blijven "
        "werken hoort bij een parallelschakeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer weerstanden je parallel bijzet, hoe groter de totale weerstand wordt.",
        antwoord=False,
        uitleg="Net omgekeerd: elke extra tak is een extra weg voor de stroom, dus daalt de "
        "totale weerstand. In serie stijgt ze wel.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid is in een serieschakeling overal even groot?",
        antwoord=["de stroomsterkte", "stroomsterkte", "de stroom"],
        uitleg="Er is maar één weg, dus gaat overal dezelfde lading per seconde langs. In "
        "een parallelschakeling is juist de spanning overal gelijk.",
    ),
]
