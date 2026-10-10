# -*- coding: utf-8 -*-
"""Statica: krachten, moment en evenwicht — 🌍 Beyond, fysica.

Deel 1 gaat over krachten en hun samenstelling: wat een kracht is, hoe je
krachten als vectoren optelt en in componenten ontbindt, welke soorten
krachten de fiche noemt, en wat translatie-evenwicht betekent. Deel 2 gaat
over het krachtmoment: de krachtarm, de formule met de sinus, de
momentenbalans en het rotatie-evenwicht, met wip, hefboom en kraan als
voorbeeld.

Een lichaam staat pas echt stil als beide balansen kloppen: de krachten samen
nul én de momenten samen nul. Veel vragen laten juist één van de twee
mislukken, want daar leer je het verschil tussen schuiven en kantelen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat heeft een kracht naast een grootte nog nodig om volledig bepaald te zijn?",
        opties=[
            "een richting en een zin",
            "een massa en een tijd",
            "een snelheid en een hoogte",
            "een temperatuur en een druk",
        ],
        antwoord=0,
        uitleg="Daarom teken je een kracht als een vector. Het aangrijpingspunt hoort er bij "
        "een star lichaam ook bij.",
    ),
    dict(
        type="invultekst",
        vraag="Uit welke drie basiseenheden is de newton samengesteld?",
        antwoord=["kg·m/s²", "kg m/s2", "kilogram meter seconde"],
        uitleg="\\(1\\ \\text{N} = 1\\ \\text{kg}\\cdot\\text{m/s}^{2}\\). Dat volgt "
        "rechtstreeks uit \\(F = m\\,a\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de zwaartekracht op \\(m = 8{,}0\\ \\text{kg}\\), met "
        "\\(g = 9{,}81\\ \\text{N/kg}\\)?",
        opties=[
            "ongeveer \\(78\\ \\text{N}\\)",
            "ongeveer \\(8{,}0\\ \\text{N}\\)",
            "ongeveer \\(0{,}80\\ \\text{N}\\)",
            "ongeveer \\(785\\ \\text{N}\\)",
        ],
        antwoord=0,
        uitleg="\\(F_{z} = m\\,g = 8{,}0\\cdot 9{,}81 \\approx 78{,}5\\ \\text{N}\\). Let "
        "op: massa staat in kilogram, kracht in newton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe stel je twee krachten samen die niet op één lijn liggen?",
        opties=[
            "met de parallellogramregel voor vectoren",
            "door hun grootten gewoon op te tellen",
            "door de kleinste van de grootste af te trekken",
            "door hun grootten met elkaar te vermenigvuldigen",
        ],
        antwoord=0,
        uitleg="Je kan ook de ene vector aan de kop van de andere zetten. Liggen de twee wel "
        "op één lijn, dan volstaat optellen of aftrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten werken op een lichaam dat op een vlakke tafel ligt? Kruis alles aan wat juist is.",
        opties=[
            "de zwaartekracht naar beneden",
            "de normaalkracht van de tafel omhoog",
            "de middelpuntzoekende kracht opzij",
            "de spankracht van een touw eraan",
        ],
        antwoord=[0, 1],
        uitleg="Die twee heffen elkaar op, en daarom blijft het lichaam liggen. Een "
        "spankracht is er enkel als er een touw aan hangt.",
    ),
    dict(
        type="waarofniet",
        vraag="De normaalkracht staat altijd loodrecht op het oppervlak waarop het lichaam rust.",
        antwoord=True,
        uitleg="Daar komt haar naam vandaan: normaal betekent loodrecht. Op een helling "
        "staat ze dus schuin, en niet recht naar boven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontbind je een kracht in componenten?",
        opties=[
            "om apart te kunnen rekenen langs twee loodrechte assen",
            "om de kracht in twee kleinere stukken te verdelen",
            "om de kracht sneller te laten werken op het lichaam",
            "om de massa van het lichaam te kunnen berekenen",
        ],
        antwoord=0,
        uitleg="Op een helling kies je de assen meestal langs en loodrecht op het vlak. Dan "
        "valt de beweging samen met één as en wordt het rekenwerk eenvoudig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist staat op een helling. Welke component van de zwaartekracht laat haar naar beneden glijden?",
        opties=[
            "de component langs het hellend vlak",
            "de component loodrecht op het vlak",
            "de normaalkracht van het vlak zelf",
            "de wrijvingskracht van het oppervlak",
        ],
        antwoord=0,
        uitleg="De component loodrecht op het vlak wordt door de normaalkracht opgeheven. "
        "Hoe steiler de helling, hoe groter de component langs het vlak.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht die een beweging langs een oppervlak tegenwerkt?",
        antwoord=["wrijvingskracht", "wrijving", "de wrijvingskracht"],
        uitleg="\\(F_{w} = \\mu\\,F_{N}\\): de wrijvingscoëfficiënt maal de normaalkracht. "
        "Hoe harder het lichaam op het vlak drukt, hoe groter ze is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist van \\(20\\ \\text{kg}\\) ligt op een vlakke vloer met "
        "\\(\\mu = 0{,}30\\). Welke kracht heb je minstens nodig om haar te doen schuiven? "
        "Neem \\(g = 10\\ \\text{N/kg}\\).",
        opties=[
            "\\(60\\ \\text{N}\\)",
            "\\(6{,}0\\ \\text{N}\\)",
            "\\(200\\ \\text{N}\\)",
            "\\(600\\ \\text{N}\\)",
        ],
        antwoord=0,
        uitleg="\\(F_{N} = m\\,g = 200\\ \\text{N}\\) en "
        "\\(F_{w} = \\mu\\,F_{N} = 0{,}30\\cdot 200 = 60\\ \\text{N}\\). Je moet net iets "
        "meer dan dat duwen.",
    ),
    dict(
        type="waarofniet",
        vraag="De veerkracht is omgekeerd evenredig met de uitrekking van de veer.",
        antwoord=False,
        uitleg="Ze is er juist recht evenredig mee: dat is de wet van Hooke, "
        "\\(F = k\\,\\Delta\\ell\\). De veerconstante \\(k\\) zegt hoe stug de veer is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een veer met \\(k = 50\\ \\text{N/m}\\) wordt \\(8{,}0\\ \\text{cm}\\) "
        "uitgerekt. Welke kracht levert ze?",
        opties=[
            "\\(4{,}0\\ \\text{N}\\)",
            "\\(400\\ \\text{N}\\)",
            "\\(0{,}16\\ \\text{N}\\)",
            "\\(6{,}25\\ \\text{N}\\)",
        ],
        antwoord=0,
        uitleg="Reken de centimeter eerst om: "
        "\\(F = k\\,\\Delta\\ell = 50\\cdot 0{,}080 = 4{,}0\\ \\text{N}\\). Rekenen met "
        "centimeter geeft een antwoord dat honderd keer te groot is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent translatie-evenwicht?",
        opties=[
            "de som van alle krachten op het lichaam is nul",
            "de som van alle momenten op het lichaam is nul",
            "het lichaam draait met een constante snelheid rond",
            "het lichaam heeft een massa van precies nul",
        ],
        antwoord=0,
        uitleg="Dan verandert de bewegingstoestand niet: het lichaam staat stil of beweegt "
        "eenparig rechtlijnig door. Voor rotatie-evenwicht moeten ook de momenten nul "
        "zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lichaam in translatie-evenwicht moet stilstaan.",
        antwoord=False,
        uitleg="Het kan ook met een constante snelheid rechtdoor bewegen. Wat telt, is dat "
        "er niets aan zijn bewegingstoestand verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee krachten van \\(6{,}0\\ \\text{N}\\) en \\(8{,}0\\ \\text{N}\\) werken "
        "loodrecht op elkaar in op hetzelfde punt. Hoe groot is de resulterende kracht?",
        opties=[
            "\\(10\\ \\text{N}\\)",
            "\\(14\\ \\text{N}\\)",
            "\\(2{,}0\\ \\text{N}\\)",
            "\\(48\\ \\text{N}\\)",
        ],
        antwoord=0,
        uitleg="Loodrecht op elkaar gebruik je Pythagoras: "
        "\\(F = \\sqrt{6{,}0^{2} + 8{,}0^{2}} = \\sqrt{100} = 10\\ \\text{N}\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het gewicht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is een kracht en staat dus in newton",
            "het hangt af van de plaats waar je je bevindt",
            "het is hetzelfde als de massa van het lichaam",
            "het staat net als de massa in kilogram",
        ],
        antwoord=[0, 1],
        uitleg="Massa is de hoeveelheid stof en blijft overal gelijk. Op de maan weegt "
        "dezelfde massa veel minder, want g is daar kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lamp hangt stil aan één koord. Wat weet je over de spankracht?",
        opties=[
            "ze is even groot als de zwaartekracht op de lamp",
            "ze is twee keer zo groot als de zwaartekracht",
            "ze is nul zolang de lamp niet beweegt",
            "ze is half zo groot als de zwaartekracht",
        ],
        antwoord=0,
        uitleg="De lamp hangt stil, dus zijn de krachten in evenwicht. Hangt ze aan twee "
        "schuine koorden, dan ligt het anders.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht waarmee een oppervlak terugduwt op wat erop rust?",
        antwoord=["normaalkracht", "de normaalkracht", "normaal"],
        uitleg="Ze staat loodrecht op dat oppervlak. Op een vlakke vloer is ze even groot "
        "als de zwaartekracht, op een helling kleiner.",
    ),
    dict(
        type="waarofniet",
        vraag="De wrijvingskracht wordt groter als het lichaam harder op het oppervlak drukt.",
        antwoord=True,
        uitleg="Ze is de wrijvingscoëfficiënt maal de normaalkracht. Daarom remt een "
        "zwaarbeladen wagen minder makkelijk weg dan een lege.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten werken er op een auto die met constante snelheid rijdt? Kruis alles aan wat juist is.",
        opties=[
            "de motorkracht naar voren",
            "de wrijvingskracht naar achter",
            "een extra versnellende kracht naar voren",
            "een afremmende kracht van de snelheid zelf",
        ],
        antwoord=[0, 1],
        uitleg="Samen met de zwaartekracht en de normaalkracht zijn ze in evenwicht. Daarom "
        "blijft de snelheid gelijk, ook al staat de motor aan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het moment van een kracht?",
        opties=[
            "de kracht maal de krachtarm ten opzichte van het draaipunt",
            "de kracht gedeeld door de afstand tot het draaipunt",
            "de kracht maal de tijd dat ze werkt",
            "de kracht maal de massa van het lichaam",
        ],
        antwoord=0,
        uitleg="\\(M = F\\,d\\,\\sin\\alpha\\), met \\(d\\) de afstand tot het draaipunt. "
        "Het zegt hoe goed een kracht erin slaagt iets te doen draaien. In de volle "
        "formule staat er nog de sinus van de hoek bij.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je het moment van een kracht uit?",
        antwoord=["newtonmeter", "Nm", "N·m"],
        uitleg="Het is kracht maal afstand, dus \\(\\text{N}\\cdot\\text{m}\\). Al is dat "
        "dezelfde "
        "samenstelling als de joule, het is een andere grootheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het moment van een kracht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is de kracht maal de krachtarm",
            "het staat in newtonmeter",
            "het is nul als de werklijn van de kracht door het draaipunt gaat",
            "het is nul als de kracht loodrecht op de stang staat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Loodrecht is net de stand waarin het moment het grootst is. De krachtarm is "
        "de kortste afstand van het draaipunt tot de werklijn van de kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kracht van 30 N werkt loodrecht op 0,4 m van het draaipunt. Hoe groot is het moment?",
        opties=[
            "12 Nm",
            "75 Nm",
            "7,5 Nm",
            "120 Nm",
        ],
        antwoord=0,
        uitleg="\\(M = F\\,d = 30\\cdot 0{,}40 = 12\\ \\text{N}\\cdot\\text{m}\\). De sinus "
        "van negentig graden "
        "is één, dus valt die factor weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde kracht van 30 N werkt nu onder 30 graden met de stang, nog altijd op 0,4 m. Hoe groot is het moment?",
        opties=[
            "6 Nm",
            "12 Nm",
            "24 Nm",
            "3 Nm",
        ],
        antwoord=0,
        uitleg="\\(\\sin 30^{\\circ} = 0{,}50\\), dus "
        "\\(M = 30\\cdot 0{,}40\\cdot 0{,}50 = 6{,}0\\ \\text{N}\\cdot\\text{m}\\). "
        "Schuin duwen levert dus minder draaiend effect.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht waarvan de werklijn door het draaipunt gaat, heeft geen moment.",
        antwoord=True,
        uitleg="De krachtarm is dan nul. Daarom krijg je een deur niet open door tegen de "
        "scharnieren te duwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zit de klink van een deur zo ver mogelijk van de scharnieren?",
        opties=[
            "zo is de krachtarm groot en volstaat een kleine kracht",
            "zo is de deur in evenwicht en valt ze niet dicht",
            "zo wordt de deur lichter om te dragen",
            "zo staat de deur loodrecht op de muur",
        ],
        antwoord=0,
        uitleg="Het moment is kracht maal arm. Een grotere arm betekent hetzelfde moment met "
        "minder kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent rotatie-evenwicht?",
        opties=[
            "de momenten linksom en rechtsom heffen elkaar op",
            "de krachten omhoog en omlaag heffen elkaar op",
            "het lichaam draait met een constante hoeksnelheid",
            "het draaipunt ligt precies in het midden van het lichaam",
        ],
        antwoord=0,
        uitleg="Het resulterende moment is dan nul. Samen met de krachtenbalans geeft dat "
        "statisch evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind van 30 kg zit op 2 m van het draaipunt van een wip. Op welke afstand moet een kind van 40 kg zitten voor evenwicht?",
        opties=[
            "1,5 m",
            "2,7 m",
            "2 m",
            "1 m",
        ],
        antwoord=0,
        uitleg="De momenten moeten gelijk zijn: "
        "\\(30\\cdot 2{,}0 = 40\\cdot d\\), dus \\(d = \\dfrac{60}{40}\\) is "
        "1,5 meter. Het zwaarste kind zit dus dichter bij het midden.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor statisch evenwicht volstaat het dat de som van de krachten nul is.",
        antwoord=False,
        uitleg="Dan is \\(\\sum F = 0\\) en schuift het lichaam niet, maar het kan nog "
        "draaien. Ook de som van de "
        "momenten moet nul zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarden gelden samen voor statisch evenwicht? Kruis alles aan wat juist is.",
        opties=[
            "de som van alle krachten is nul",
            "de som van alle momenten is nul",
            "het lichaam heeft een gelijkmatige massaverdeling",
            "het draaipunt ligt in het zwaartepunt van het lichaam",
        ],
        antwoord=[0, 1],
        uitleg="De massaverdeling en de plaats van het draaipunt bepalen wel de grootte van "
        "de momenten, maar zijn geen voorwaarde op zich.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee krachten van 50 N werken op een hefboom, de ene op 0,6 m links en de andere op 0,4 m rechts van het draaipunt. Wat gebeurt er?",
        opties=[
            "de hefboom draait naar de kant van de kracht op 0,6 m",
            "de hefboom draait naar de kant van de kracht op 0,4 m",
            "de hefboom blijft precies in evenwicht staan",
            "de hefboom schuift zijwaarts weg van het draaipunt",
        ],
        antwoord=0,
        uitleg="Links is het moment 30 newtonmeter en rechts 20. Het grootste moment wint, "
        "dus kantelt de hefboom die kant op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waarrond een hefboom draait?",
        antwoord=["draaipunt", "het draaipunt", "steunpunt"],
        uitleg="Ten opzichte van dat punt reken je alle krachtarmen uit. Verschuif je het, "
        "dan verandert elk moment mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je een lange steeksleutel om een vastzittende bout los te draaien?",
        opties=[
            "de langere arm geeft bij dezelfde kracht een groter moment",
            "de langere sleutel is zwaarder en duwt harder op de bout",
            "de langere sleutel glijdt minder makkelijk van de bout af",
            "de langere sleutel maakt de bout warmer en dus losser",
        ],
        antwoord=0,
        uitleg="Het moment is kracht maal arm. Daarom schuiven monteurs er soms nog een buis "
        "over, al is dat niet zonder risico voor de bout.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het berekenen van de momenten mag je zelf kiezen welk punt je als draaipunt neemt.",
        antwoord=True,
        uitleg="Bij echt evenwicht is de som van de momenten rond elk punt nul. Een handige "
        "keuze is een punt waar een onbekende kracht aangrijpt, want die valt dan weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plank van 4 m rust op twee steunen aan de uiteinden. Een last staat op 1 m van de linkersteun. Welke steun draagt het meest?",
        opties=[
            "de linkersteun, want de last staat er het dichtst bij",
            "de rechtersteun, want die moet de verste arm aan",
            "beide steunen dragen precies evenveel",
            "dat hangt enkel af van de dikte van de plank",
        ],
        antwoord=0,
        uitleg="Met de momentenbalans rond de rechtersteun vind je dat de linker drie kwart "
        "draagt. Hoe dichter de last bij een steun staat, hoe meer die draagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er bij een torenkraan een zwaar blok aan de achterste arm?",
        opties=[
            "om het moment van de last aan de voorkant tegen te werken",
            "om de kraan zwaarder en dus steviger te maken",
            "om de last aan de voorkant lichter te laten lijken",
            "om de kraan sneller te kunnen laten draaien",
        ],
        antwoord=0,
        uitleg="Zonder dat tegengewicht zou de kraan voorover kantelen. Het blok schuift mee "
        "naar achter als de last verder naar voren gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwaar lichaam met een breed steunvlak kantelt makkelijker dan een smal en hoog lichaam.",
        antwoord=False,
        uitleg="Net omgekeerd: hoe breder het steunvlak en hoe lager het zwaartepunt, hoe "
        "stabieler. Een smalle hoge kast kantelt juist snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarden gelden voor een lichaam in volledig evenwicht? Kruis alles aan wat juist is.",
        opties=[
            "de som van alle krachten is nul",
            "de som van alle momenten is nul",
            "het zwaartepunt ligt boven het steunvlak",
            "de snelheid van het lichaam moet nul zijn",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een lichaam dat met een constante snelheid beweegt, is ook in evenwicht. "
        "Valt het zwaartepunt buiten het steunvlak, dan kantelt het.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waarin je de hele massa van een lichaam mag denken?",
        antwoord=["zwaartepunt", "het zwaartepunt", "massamiddelpunt"],
        uitleg="Daar grijpt de zwaartekracht aan in je tekening. Ligt het laag en binnen het "
        "steunvlak, dan staat het lichaam stabiel.",
    ),
]
