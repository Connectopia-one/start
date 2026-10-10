# -*- coding: utf-8 -*-
"""De gaswetten en de algemene gaswet — 🌍 Beyond, fysica.

Deel 1 gaat over de vier toestandsgrootheden en over de drie afzonderlijke
gaswetten: bij constante temperatuur, bij constante druk en bij constant
volume. Daar hoort het rekenen bij, altijd in kelvin, en het lezen van een
\(p(V)\)-, een \(V(T)\)- en een \(p(T)\)-grafiek. Deel 2 gaat over de algemene en de
ideale gaswet, de gasconstante, het verschil tussen een ideaal en een reëel
gas, de normomstandigheden, en wat je met het deeltjesmodel kan verklaren.

Eén fout komt in dit thema voortdurend terug: rekenen met graden celsius. De
vragen zeggen de temperatuur daarom meestal in celsius, zodat het omzetten
naar kelvin telkens een echte stap is.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke grootheden noemt men de toestandsgrootheden van een gas?",
        opties=[
            "druk, volume, temperatuur en stofhoeveelheid",
            "druk, massa, snelheid en temperatuur",
            "volume, massa, dichtheid en warmte",
            "druk, kracht, oppervlakte en tijd",
        ],
        antwoord=0,
        uitleg=r"Samen liggen ze vast in de algemene gaswet \(\dfrac{p\,V}{T} = \text{cte}\). "
        r"Ken je er drie, dan volgt de vierde eruit.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid moet je de temperatuur in de gaswetten invullen?",
        antwoord=["kelvin", "K", "de kelvin"],
        uitleg=r"Nul kelvin is het absolute nulpunt, bij \(-273\ ^\circ\text{C}\). "
        r"Rekenen in celsius geeft meteen een fout antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel kelvin is \(27\ ^\circ\text{C}\)?",
        opties=[
            r"\(300\) K",
            r"\(246\) K",
            r"\(27\) K",
            r"\(273\) K",
        ],
        antwoord=0,
        uitleg=r"\(T = \theta + 273 = 27 + 273 = 300\) K. Omgekeerd trek je er \(273\) van af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de gaswet bij constante temperatuur?",
        opties=[
            "het product van druk en volume blijft gelijk",
            "de som van druk en volume blijft gelijk",
            "druk gedeeld door volume blijft gelijk",
            "volume gedeeld door temperatuur blijft gelijk",
        ],
        antwoord=0,
        uitleg=r"\[p\,V = \text{cte} \quad\text{of}\quad p_{1}V_{1} = p_{2}V_{2}\] "
        r"Pers je een gas in de helft van het volume, dan verdubbelt de druk. Zo'n proces "
        r"heet isotherm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een proces waarbij de temperatuur constant blijft?",
        antwoord=["isotherm", "isotherme", "isothermisch"],
        uitleg="Bij constante druk spreek je van isobaar en bij constant volume van "
        "isochoor.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een gas van \(6{,}0\) L bij \(100\) kPa wordt bij dezelfde temperatuur samengeperst tot \(2{,}0\) L. Welke druk heeft het dan?",
        opties=[
            r"\(300\) kPa",
            r"\(33\) kPa",
            r"\(200\) kPa",
            r"\(600\) kPa",
        ],
        antwoord=0,
        uitleg=r"\(p_{2} = \dfrac{p_{1}V_{1}}{V_{2}} = \dfrac{100 \times 6{,}0}{2{,}0} "
        r"= 300\) kPa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de gaswet bij constante druk?",
        opties=[
            "het volume is recht evenredig met de absolute temperatuur",
            "het volume is omgekeerd evenredig met de temperatuur",
            "het volume is recht evenredig met het kwadraat van T",
            "het volume blijft gelijk hoe warm je het gas ook maakt",
        ],
        antwoord=0,
        uitleg=r"\[\dfrac{V}{T} = \text{cte}\] Verwarm je een ballon, dan zet hij uit. Dat "
        r"heet een isobaar proces.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een gas van \(2{,}0\) L bij \(300\) K wordt bij gelijke druk tot \(600\) K verwarmd. Welk volume heeft het dan?",
        opties=[
            r"\(4{,}0\) L",
            r"\(1{,}0\) L",
            r"\(8{,}0\) L",
            r"\(2{,}0\) L",
        ],
        antwoord=0,
        uitleg=r"\(\dfrac{V}{T}\) blijft gelijk, en \(T\) verdubbelt. Had je in celsius "
        r"gerekend, dan was het antwoord fout geweest.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij constant volume stijgt de druk van een gas als je het verwarmt.",
        antwoord=True,
        uitleg="De deeltjes botsen dan sneller en harder tegen de wand. Daarom mag je een "
        "spuitbus nooit in het vuur gooien.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een gesloten vat met gas staat op \(2{,}0\) bar bij \(250\) K. Tot welke druk stijgt het bij \(500\) K?",
        opties=[
            r"\(4{,}0\) bar",
            r"\(1{,}0\) bar",
            r"\(2{,}0\) bar",
            r"\(8{,}0\) bar",
        ],
        antwoord=0,
        uitleg=r"Bij constant volume blijft \(\dfrac{p}{T}\) gelijk. \(T\) verdubbelt, "
        r"dus \(p\) ook.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ziet een \(p(V)\)-grafiek van een isotherm proces eruit?",
        opties=[
            "een kromme die daalt zoals een omgekeerde evenredigheid",
            "een rechte door de oorsprong",
            "een horizontale rechte",
            "een stijgende parabool",
        ],
        antwoord=0,
        uitleg=r"\(p\,V = \text{cte}\), dus is het een hyperbool. Een \(V(T)\)-grafiek "
        r"bij constante druk is wel een rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een isotherm proces zijn juist? Kruis alles aan wat juist is.",
        opties=[
            r"het product \(p\,V\) blijft gelijk",
            r"de \(p(V)\)-grafiek is een hyperbool",
            "de temperatuur verandert tijdens het proces niet",
            "het volume is recht evenredig met de druk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het volume is net omgekeerd evenredig met de druk. Recht evenredig met de "
        "temperatuur is het wel, maar dan bij constante druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een isochoor proces verloopt bij constante druk.",
        antwoord=False,
        uitleg="Isochoor is bij constant volume, denk aan een gesloten metalen vat. Bij "
        "constante druk heet het isobaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen horen bij een proces van een gas? Kruis alles aan wat juist is.",
        opties=[
            "isobaar, bij constante druk",
            "isochoor, bij constant volume",
            "isomeer, bij constante massa",
            "isotoop, bij constant aantal deeltjes",
        ],
        antwoord=[0, 1],
        uitleg="Het derde proces is isotherm, bij constante temperatuur. Isomeer en isotoop "
        "horen bij de chemie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grafieken horen bij welke gaswet? Kruis alles aan wat juist is.",
        opties=[
            r"bij constante druk is de \(V(T)\)-grafiek een rechte door de oorsprong",
            r"bij constant volume is de \(p(T)\)-grafiek een rechte door de oorsprong",
            r"bij constante temperatuur daalt de \(p(V)\)-grafiek als een kromme",
            r"bij constante druk is de \(V(T)\)-grafiek een dalende kromme",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"De eerste twee gelden alleen met \(T\) in kelvin. In graden celsius "
        r"snijden die rechten de as pas bij \(-273\).",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag in de gaswetten de temperatuur in graden celsius invullen zolang je overal dezelfde eenheid gebruikt.",
        antwoord=False,
        uitleg="De wetten gelden voor de absolute temperatuur. Nul graden celsius is niet "
        "nul kelvin, dus klopt de verhouding anders niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een ballon van \(3{,}0\) L bij \(20\ ^\circ\text{C}\) wordt bij gelijke druk in een koelkast op \(5\ ^\circ\text{C}\) gelegd. Welk volume krijgt hij ongeveer?",
        opties=[
            r"\(2{,}85\) L",
            r"\(0{,}75\) L",
            r"\(3{,}15\) L",
            r"\(12{,}0\) L",
        ],
        antwoord=0,
        uitleg=r"Zet eerst om naar kelvin: \(293\) en \(278\). Dan is "
        r"\(V_{2} = \dfrac{3{,}0 \times 278}{293} \approx 2{,}85\) L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt de druk in een fietsband als je lang gepompt hebt?",
        opties=[
            "de lucht is samengeperst en ook warmer geworden",
            "de band wordt stijver en knijpt de lucht samen",
            "er lekt lucht weg en de rest zet uit",
            "de deeltjes worden door het pompen zelf zwaarder",
        ],
        antwoord=0,
        uitleg="Je perst meer deeltjes in hetzelfde volume, en het samenpersen verwarmt de "
        "lucht bovendien. Daarom voelt een fietspomp na het pompen warm aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een proces waarbij de druk constant blijft?",
        antwoord=["isobaar", "isobare", "isobarisch"],
        uitleg="Een ballon die opwarmt in de zon maakt zo'n proces door. Bij constant volume "
        "heet het isochoor.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een isotherm proces zijn druk en volume omgekeerd evenredig.",
        antwoord=True,
        uitleg="Hun product blijft constant, en dat is precies wat omgekeerd evenredig "
        "betekent. De grafiek is daardoor een hyperbool.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de algemene gaswet voor een vaste hoeveelheid gas?",
        opties=[
            r"\(\dfrac{p\,V}{T}\) blijft constant",
            r"\(p\,V\,T\) blijft constant",
            r"\(\dfrac{p\,T}{V}\) blijft constant",
            r"\(p + V + T\) blijft constant",
        ],
        antwoord=0,
        uitleg=r"\[\dfrac{p_{1}V_{1}}{T_{1}} = \dfrac{p_{2}V_{2}}{T_{2}}\] De drie "
        r"afzonderlijke gaswetten zijn bijzondere gevallen daarvan. Houd je er één "
        r"constant, dan blijft de rest over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de ideale gaswet?",
        opties=[
            r"\(p\,V = n\,R\,T\)",
            r"\(p\,V = m\,R\,T\)",
            r"\(\dfrac{p}{V} = n\,R\,T\)",
            r"\(p\,T = n\,R\,V\)",
        ],
        antwoord=0,
        uitleg=r"Hier staat \(n\) voor de stofhoeveelheid in mol en \(R\) voor de "
        r"universele gasconstante. Die staat in de bijlage van het examen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe noem je de constante \(R\) uit de ideale gaswet?",
        antwoord=["gasconstante", "de gasconstante", "universele gasconstante"],
        uitleg=r"\(R = 8{,}31\ \text{J/(mol}\cdot\text{K)}\). Dezelfde waarde geldt "
        r"voor elk gas, en dat is net het bijzondere eraan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een gas gaat van \(2{,}0\) L bij \(300\) K en \(100\) kPa naar \(400\) K en \(200\) kPa. Welk volume krijgt het?",
        opties=[
            r"\(1{,}33\) L",
            r"\(3{,}00\) L",
            r"\(0{,}75\) L",
            r"\(2{,}67\) L",
        ],
        antwoord=0,
        uitleg=r"\(V_{2} = \dfrac{p_{1}V_{1}T_{2}}{T_{1}p_{2}} = "
        r"\dfrac{100 \times 2{,}0 \times 400}{300 \times 200} = 1{,}33\) L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de ideale gaswet zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze geldt ook voor een mengsel van gassen zoals lucht",
            r"de stofhoeveelheid \(n\) staat erin in mol",
            r"de constante \(R\) is voor elk gas dezelfde",
            "de temperatuur mag je erin in graden celsius invullen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De temperatuur moet in kelvin, want de wet geldt voor de absolute "
        "temperatuur. Een ideaal gas met deeltjes zonder eigen volume bestaat niet echt, maar "
        "bij lage druk komen echte gassen er dicht bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reëel gas wijkt het meest van de ideale gaswet af bij hoge temperatuur en lage druk.",
        antwoord=False,
        uitleg="Net dan klopt de wet het best, want de deeltjes zitten ver uiteen. De "
        "afwijking is het grootst bij lage temperatuur en hoge druk, dicht bij het "
        "condenseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aannames maakt het model van een ideaal gas? Kruis alles aan wat juist is.",
        opties=[
            "de deeltjes hebben zelf geen eigen volume",
            "de deeltjes oefenen geen kracht op elkaar uit",
            "de deeltjes staan volledig stil bij kamertemperatuur",
            "de deeltjes verliezen energie bij elke botsing",
        ],
        antwoord=[0, 1],
        uitleg="De botsingen zijn volkomen elastisch, dus er gaat geen energie verloren. "
        "Deeltjes die stilstaan, zouden helemaal geen druk geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar komt de druk van een gas op de wand vandaan?",
        opties=[
            "van de botsingen van de deeltjes tegen die wand",
            "van het gewicht van de deeltjes op de bodem",
            "van de aantrekking tussen de deeltjes onderling",
            "van de warmte die de wand zelf uitstraalt",
        ],
        antwoord=0,
        uitleg="Elke botsing geeft een duwtje, en samen geven ze een constante druk. Meer "
        "deeltjes of snellere deeltjes betekenen meer druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de temperatuur van een gas over zijn deeltjes?",
        opties=[
            "hoe groot hun gemiddelde kinetische energie is",
            "hoeveel deeltjes er in het vat aanwezig zijn",
            "hoe zwaar elk deeltje afzonderlijk is",
            "hoe groot het volume van elk deeltje is",
        ],
        antwoord=0,
        uitleg="Verwarmen betekent dus sneller bewegen. Bij het absolute nulpunt zou die "
        "beweging tot een minimum herleid zijn.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij welke temperatuur in graden celsius ligt het absolute nulpunt?",
        antwoord=["−273", "-273", "min 273"],
        uitleg=r"Preciezer is dat \(-273{,}15\ ^\circ\text{C}\). Lager dan \(0\) K kan niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verstaat men onder normomstandigheden?",
        opties=[
            r"\(0\ ^\circ\text{C}\) en een druk van \(101{,}3\) kPa",
            r"\(20\ ^\circ\text{C}\) en een druk van \(100\) kPa",
            r"\(25\ ^\circ\text{C}\) en een druk van \(1{,}0\) kPa",
            r"\(0\) K en een druk van \(0\) Pa",
        ],
        antwoord=0,
        uitleg=r"Onder die omstandigheden neemt één mol gas ongeveer \(22{,}4\) L in. Zo "
        r"kan je metingen van verschillende dagen met elkaar vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel liter neemt één mol van een ideaal gas in bij normomstandigheden?",
        opties=[
            r"\(22{,}4\) L",
            r"\(1{,}0\) L",
            r"\(24{,}5\) L",
            r"\(100\) L",
        ],
        antwoord=0,
        uitleg=r"Dat geldt voor élk ideaal gas, hoe zwaar zijn deeltjes ook zijn. Bij "
        r"kamertemperatuur is het ongeveer \(24\) L.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee verschillende gassen bij dezelfde druk en temperatuur bevatten in hetzelfde volume evenveel deeltjes.",
        antwoord=True,
        uitleg="Dat volgt rechtstreeks uit de ideale gaswet. De massa van die deeltjes "
        "verschilt wel, dus wegen de twee vaten niet even zwaar.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel mol gas zit er in een vat van \(0{,}025\ \text{m}^{3}\) bij \(300\) K en \(100\) kPa? Neem \(R = 8{,}31\).",
        opties=[
            r"\(1{,}0\) mol",
            r"\(10{,}0\) mol",
            r"\(0{,}10\) mol",
            r"\(100\) mol",
        ],
        antwoord=0,
        uitleg=r"\(n = \dfrac{p\,V}{R\,T} = \dfrac{1{,}0 \times 10^{5} \times 0{,}025}"
        r"{8{,}31 \times 300} \approx 1{,}0\) mol. Let op de eenheden: pascal en "
        r"kubieke meter.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je bij gelijk volume en gelijke temperatuur meer gas in een vat pompt, blijft de druk gelijk.",
        antwoord=False,
        uitleg=r"De druk stijgt, want meer deeltjes betekent meer botsingen tegen de wand. "
        r"In \(p\,V = n\,R\,T\) is \(n\) recht evenredig met \(p\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom staat er op een spuitbus dat je hem niet boven \(50\ ^\circ\text{C}\) mag bewaren?",
        opties=[
            "bij constant volume stijgt de druk mee met de temperatuur",
            "het gas erin lost bij warmte op in de vloeistof",
            "de bus zet bij warmte zo sterk uit dat hij scheurt",
            "de inhoud verliest bij warmte zijn werking",
        ],
        antwoord=0,
        uitleg="De bus kan niet uitzetten, dus moet de druk omhoog. Boven een bepaalde "
        "grens begeeft de wand het.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke eenheden vul je de grootheden van de ideale gaswet in? Kruis alles aan wat juist is.",
        opties=[
            "de druk in pascal",
            "het volume in kubieke meter",
            "de temperatuur in kelvin",
            "de stofhoeveelheid in gram",
        ],
        antwoord=[0, 1, 2],
        uitleg="De stofhoeveelheid staat in mol en niet in gram. Vergeet je een van die "
        "omzettingen, dan zit je er meteen een factor duizend naast.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een duiker ademt op \(20\) m diepte lucht in bij ongeveer \(3\) bar. Waarom mag hij bij het opstijgen niet de adem inhouden?",
        opties=[
            "de lucht in zijn longen zet bij de dalende druk sterk uit",
            "de lucht in zijn longen koelt bij het stijgen snel af",
            "de lucht lost bij lagere druk op in zijn bloed",
            "de lucht wordt bij het stijgen zwaarder dan water",
        ],
        antwoord=0,
        uitleg=r"Bij constante temperatuur is \(p\,V\) constant. Van \(3\) naar "
        r"\(1\) bar betekent dus een drie keer zo groot volume.",
    ),
    dict(
        type="waarofniet",
        vraag="De ideale gaswet geldt ook voor een mengsel van gassen zoals lucht.",
        antwoord=True,
        uitleg=r"Je telt dan alle deeltjes samen als \(n\). Welke soorten het zijn, maakt "
        r"voor de wet niet uit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid moet je naast druk, volume en temperatuur kennen om de ideale gaswet te gebruiken?",
        antwoord=["de stofhoeveelheid", "stofhoeveelheid", "het aantal mol"],
        uitleg=r"Ze staat in mol en krijgt het symbool \(n\). Blijft ze constant, dan "
        r"volstaat de algemene gaswet \(\dfrac{p\,V}{T} = \text{cte}\).",
    ),
]
