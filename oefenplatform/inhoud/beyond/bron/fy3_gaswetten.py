# -*- coding: utf-8 -*-
"""De gaswetten en de algemene gaswet — 🌍 Beyond, fysica.

Deel 1 gaat over de vier toestandsgrootheden en over de drie afzonderlijke
gaswetten: bij constante temperatuur, bij constante druk en bij constant
volume. Daar hoort het rekenen bij, altijd in kelvin, en het lezen van een
p(V)-, een V(T)- en een p(T)-grafiek. Deel 2 gaat over de algemene en de
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
        uitleg="Samen liggen ze vast in de algemene gaswet. Ken je er drie, dan volgt de "
        "vierde eruit.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid moet je de temperatuur in de gaswetten invullen?",
        antwoord=["kelvin", "K", "de kelvin"],
        uitleg="Nul kelvin is het absolute nulpunt, bij min 273 graden celsius. Rekenen in "
        "celsius geeft meteen een fout antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kelvin is 27 graden celsius?",
        opties=[
            "300 K",
            "246 K",
            "27 K",
            "273 K",
        ],
        antwoord=0,
        uitleg="Tel er 273 bij: 27 plus 273 is 300 kelvin. Omgekeerd trek je er 273 van af.",
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
        uitleg="Pers je een gas in de helft van het volume, dan verdubbelt de druk. Zo'n "
        "proces heet isotherm.",
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
        vraag="Een gas van 6 L bij 100 kPa wordt bij dezelfde temperatuur samengeperst tot 2 L. Welke druk heeft het dan?",
        opties=[
            "300 kPa",
            "33 kPa",
            "200 kPa",
            "600 kPa",
        ],
        antwoord=0,
        uitleg="Het product van druk en volume blijft gelijk: 100 maal 6 is 600, en 600 "
        "gedeeld door 2 is 300 kilopascal.",
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
        uitleg="Verwarm je een ballon, dan zet hij uit. Dat heet een isobaar proces.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas van 2 L bij 300 K wordt bij gelijke druk tot 600 K verwarmd. Welk volume heeft het dan?",
        opties=[
            "4 L",
            "1 L",
            "8 L",
            "2 L",
        ],
        antwoord=0,
        uitleg="Volume gedeeld door temperatuur blijft gelijk, en de temperatuur verdubbelt. "
        "Had je in celsius gerekend, dan was het antwoord fout geweest.",
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
        vraag="Een gesloten vat met gas staat op 2 bar bij 250 K. Tot welke druk stijgt het bij 500 K?",
        opties=[
            "4 bar",
            "1 bar",
            "2 bar",
            "8 bar",
        ],
        antwoord=0,
        uitleg="Druk gedeeld door temperatuur blijft gelijk bij constant volume. De "
        "temperatuur verdubbelt, dus de druk ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet een p(V)-grafiek van een isotherm proces eruit?",
        opties=[
            "een kromme die daalt zoals een omgekeerde evenredigheid",
            "een rechte door de oorsprong",
            "een horizontale rechte",
            "een stijgende parabool",
        ],
        antwoord=0,
        uitleg="Het product van de twee blijft constant, dus is het een hyperbool. Een "
        "V(T)-grafiek bij constante druk is wel een rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een isotherm proces zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het product van druk en volume blijft gelijk",
            "de p(V)-grafiek is een hyperbool",
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
            "bij constante druk is de V(T)-grafiek een rechte door de oorsprong",
            "bij constant volume is de p(T)-grafiek een rechte door de oorsprong",
            "bij constante temperatuur daalt de p(V)-grafiek als een kromme",
            "bij constante druk is de V(T)-grafiek een dalende kromme",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste twee gelden alleen met de temperatuur in kelvin. In graden celsius "
        "snijden die rechten de as pas bij min 273.",
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
        vraag="Een ballon van 3 L bij 20 °C wordt bij gelijke druk in een koelkast op 5 °C gelegd. Welk volume krijgt hij ongeveer?",
        opties=[
            "ongeveer 2,85 L",
            "ongeveer 0,75 L",
            "ongeveer 3,15 L",
            "ongeveer 12 L",
        ],
        antwoord=0,
        uitleg="Zet eerst om naar kelvin: 293 en 278. Dan is 3 maal 278 gedeeld door 293 "
        "ongeveer 2,85 liter.",
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
            "p maal V gedeeld door T blijft constant",
            "p maal V maal T blijft constant",
            "p gedeeld door V maal T blijft constant",
            "p plus V plus T blijft constant",
        ],
        antwoord=0,
        uitleg="De drie afzonderlijke gaswetten zijn bijzondere gevallen daarvan. Houd je er "
        "één constant, dan blijft de rest over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de ideale gaswet?",
        opties=[
            "p maal V is n maal R maal T",
            "p maal V is m maal R maal T",
            "p gedeeld door V is n maal R maal T",
            "p maal T is n maal R maal V",
        ],
        antwoord=0,
        uitleg="Hier staat n voor de stofhoeveelheid in mol en R voor de universele "
        "gasconstante. Die staat in de bijlage van het examen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de constante R uit de ideale gaswet?",
        antwoord=["gasconstante", "de gasconstante", "universele gasconstante"],
        uitleg="Ze is ongeveer 8,31 joule per mol per kelvin. Dezelfde waarde geldt voor elk "
        "gas, en dat is net het bijzondere eraan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas gaat van 2 L bij 300 K en 100 kPa naar 400 K en 200 kPa. Welk volume krijgt het?",
        opties=[
            "ongeveer 1,33 L",
            "ongeveer 3 L",
            "ongeveer 0,75 L",
            "ongeveer 2,67 L",
        ],
        antwoord=0,
        uitleg="p maal V gedeeld door T blijft gelijk: 2 maal 100 gedeeld door 300 is "
        "0,667, dus V is 0,667 maal 400 gedeeld door 200 is 1,33 liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de ideale gaswet zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze geldt ook voor een mengsel van gassen zoals lucht",
            "de stofhoeveelheid n staat erin in mol",
            "de constante R is voor elk gas dezelfde",
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
        vraag="Bij welke temperatuur in graden celsius ligt het absolute nulpunt?",
        antwoord=["−273", "-273", "min 273"],
        uitleg="Preciezer is dat min 273,15 graden celsius. Lager dan nul kelvin kan niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verstaat men onder normomstandigheden?",
        opties=[
            "nul graden celsius en een druk van 101,3 kPa",
            "twintig graden celsius en een druk van 100 kPa",
            "vijfentwintig graden celsius en een druk van 1 kPa",
            "nul kelvin en een druk van nul pascal",
        ],
        antwoord=0,
        uitleg="Onder die omstandigheden neemt één mol gas ongeveer 22,4 liter in. Zo kan je "
        "metingen van verschillende dagen met elkaar vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel liter neemt één mol van een ideaal gas in bij normomstandigheden?",
        opties=[
            "ongeveer 22,4 L",
            "ongeveer 1 L",
            "ongeveer 24,5 L",
            "ongeveer 100 L",
        ],
        antwoord=0,
        uitleg="Dat geldt voor élk ideaal gas, hoe zwaar zijn deeltjes ook zijn. Bij "
        "kamertemperatuur is het ongeveer 24 liter.",
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
        vraag="Hoeveel mol gas zit er in een vat van 0,025 m³ bij 300 K en 100 kPa? Neem R gelijk aan 8,31.",
        opties=[
            "ongeveer 1 mol",
            "ongeveer 10 mol",
            "ongeveer 0,1 mol",
            "ongeveer 100 mol",
        ],
        antwoord=0,
        uitleg="n is p maal V gedeeld door R maal T: 100 000 maal 0,025 gedeeld door 8,31 "
        "maal 300 is ongeveer 1 mol. Let op de eenheden: pascal en kubieke meter.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je bij gelijk volume en gelijke temperatuur meer gas in een vat pompt, blijft de druk gelijk.",
        antwoord=False,
        uitleg="De druk stijgt, want meer deeltjes betekent meer botsingen tegen de wand. In "
        "de ideale gaswet is n recht evenredig met p.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er op een spuitbus dat je hem niet boven 50 °C mag bewaren?",
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
        vraag="Een duiker ademt op 20 m diepte lucht in bij ongeveer 3 bar. Waarom mag hij bij het opstijgen niet de adem inhouden?",
        opties=[
            "de lucht in zijn longen zet bij de dalende druk sterk uit",
            "de lucht in zijn longen koelt bij het stijgen snel af",
            "de lucht lost bij lagere druk op in zijn bloed",
            "de lucht wordt bij het stijgen zwaarder dan water",
        ],
        antwoord=0,
        uitleg="Bij constante temperatuur is het product van druk en volume constant. Van 3 "
        "naar 1 bar betekent dus een drie keer zo groot volume.",
    ),
    dict(
        type="waarofniet",
        vraag="De ideale gaswet geldt ook voor een mengsel van gassen zoals lucht.",
        antwoord=True,
        uitleg="Je telt dan alle deeltjes samen als n. Welke soorten het zijn, maakt voor de "
        "wet niet uit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid moet je naast druk, volume en temperatuur kennen om de ideale gaswet te gebruiken?",
        antwoord=["de stofhoeveelheid", "stofhoeveelheid", "het aantal mol"],
        uitleg="Ze staat in mol en krijgt het symbool n. Blijft ze constant, dan volstaat de "
        "algemene gaswet.",
    ),
]
