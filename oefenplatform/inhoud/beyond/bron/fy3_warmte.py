# -*- coding: utf-8 -*-
"""Warmteleer: temperatuur, warmte en faseovergangen — 🌍 Beyond, fysica.

Deel 1 gaat over het verschil tussen temperatuur en warmte, over de
calorimeter en het joulevat, over warmtecapaciteit en specifieke
warmtecapaciteit, en over het rekenen met \(Q = C\,\Delta T\) en
\(Q = c\,m\,\Delta T\). Deel 2 gaat over de zes faseovergangen, het smelt-, kook- en
sublimatiepunt, de specifieke smelt-, verdampings- en sublimatiewarmte, en
over het lezen van een smelt- en een stolcurve.

De rode draad is dat warmte energie is die van warm naar koud stroomt, en dat
een stof die van fase verandert warmte opneemt of afgeeft zonder dat de
thermometer beweegt. Dat tweede is wat kinderen bij een stolcurve het vaakst
verkeerd lezen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen warmte en temperatuur?",
        opties=[
            "warmte is energie die stroomt, temperatuur is een toestand",
            "warmte is een toestand, temperatuur is energie die stroomt",
            "warmte meet je in kelvin, temperatuur in joule",
            "warmte en temperatuur zijn twee woorden voor hetzelfde",
        ],
        antwoord=0,
        uitleg=r"Een kopje thee en een bad van dezelfde temperatuur bevatten heel "
        r"verschillende hoeveelheden warmte. Warmte \(Q\) staat in joule, temperatuur "
        r"\(T\) in kelvin.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je een hoeveelheid warmte uit?",
        antwoord=["joule", "J", "de joule"],
        uitleg="Warmte is een vorm van energie, dus geldt dezelfde eenheid als voor arbeid. "
        "De oude eenheid calorie komt nog op voedingslabels voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Warmte stroomt van het warme naar het koude voorwerp.",
        antwoord=True,
        uitleg="Nooit spontaan de andere kant op. Een koelkast kan dat wel, maar die moet er "
        "energie in stoppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een calorimeter?",
        opties=[
            "om een hoeveelheid uitgewisselde warmte te meten",
            "om de temperatuur van een vlam te meten",
            "om de druk van een gas te meten",
            "om de massa van een vloeistof te meten",
        ],
        antwoord=0,
        uitleg="Het is een goed geïsoleerd vat, zodat er zo weinig mogelijk warmte ontsnapt. "
        "Uit de temperatuurstijging van het water bereken je de warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet je met een joulevat?",
        opties=[
            "hoeveel warmte een elektrische weerstand aan water geeft",
            "hoeveel lading er door een weerstand gestroomd is",
            "hoeveel warmte een vlam aan een metaal geeft",
            "hoeveel water er per seconde door een buis gaat",
        ],
        antwoord=0,
        uitleg="Je meet spanning, stroom en tijd, en daaruit de geleverde energie. De "
        "temperatuurstijging van het water laat zien dat die energie warmte geworden is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de warmtecapaciteit van een voorwerp?",
        opties=[
            "de warmte die het nodig heeft om één kelvin op te warmen",
            "de warmte die het bij kamertemperatuur in totaal bevat",
            "de hoogste temperatuur die het voorwerp kan halen",
            "de warmte die het per seconde aan de lucht afgeeft",
        ],
        antwoord=0,
        uitleg=r"Ze hangt af van de stof én van de massa van dat ene voorwerp. Het symbool "
        r"is \(C\), in \(\text{J/K}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de specifieke warmtecapaciteit van een stof?",
        opties=[
            "de warmte voor één kilogram en één kelvin",
            "de warmte voor één liter en één graad celsius",
            "de warmte die één kilogram in totaal kan bevatten",
            "de warmte die één kilogram bij smelten opneemt",
        ],
        antwoord=0,
        uitleg=r"Het symbool is \(c\), in \(\text{J/(kg}\cdot\text{K)}\). Ze is een "
        r"eigenschap van de stof en niet van het voorwerp.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel joule heeft één kilogram water nodig om één kelvin op te warmen?",
        antwoord=["4186", "4180", "ongeveer 4200"],
        uitleg=r"\(c_{\text{water}} = 4186\ \text{J/(kg}\cdot\text{K)}\), heel veel in "
        r"vergelijking met metalen. Daarom is water zo'n goede warmteopslag, en daarom koelt "
        r"de zee zo langzaam af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke formule bereken je de warmte die een massa nodig heeft om op te warmen?",
        opties=[
            r"\(Q = c\,m\,\Delta T\)",
            r"\(Q = \dfrac{c\,m}{\Delta T}\)",
            r"\(Q = c + m + \Delta T\)",
            r"\(Q = \dfrac{c\,\Delta T}{m}\)",
        ],
        antwoord=0,
        uitleg=r"Ken je de warmtecapaciteit van het hele voorwerp, dan volstaat "
        r"\(Q = C\,\Delta T\). De massa zit dan al in die \(C\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel warmte heeft \(2{,}0\) kg water nodig om \(10\) K op te warmen? Neem \(c = 4186\ \text{J/(kg}\cdot\text{K)}\).",
        opties=[
            r"\(83{,}7\) kJ",
            r"\(8{,}37\) kJ",
            r"\(41{,}9\) kJ",
            r"\(837\) kJ",
        ],
        antwoord=0,
        uitleg=r"\(Q = c\,m\,\Delta T = 4186 \times 2{,}0 \times 10 = "
        r"8{,}37 \times 10^{4}\) J, dus ongeveer \(84\) kJ.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de specifieke warmtecapaciteit zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "water heeft een hoge waarde in vergelijking met metalen",
            "ze hangt af van de stof en niet van de massa",
            "ze is voor elke stof dezelfde waarde",
            r"ze wordt uitgedrukt in \(\text{J/K}\)",
        ],
        antwoord=[0, 1],
        uitleg=r"\(\text{J/K}\) is de eenheid van de gewone warmtecapaciteit \(C\). De "
        r"specifieke \(c\) staat in \(\text{J/(kg}\cdot\text{K)}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom warmt een pan sneller op dan het water erin?",
        opties=[
            "het metaal heeft een veel lagere specifieke warmtecapaciteit",
            "het metaal heeft een veel hogere specifieke warmtecapaciteit",
            "het metaal raakt het vuur en het water niet",
            "het metaal heeft een veel grotere massa dan het water",
        ],
        antwoord=0,
        uitleg="Per kilogram en per kelvin heeft metaal veel minder warmte nodig. Daarom "
        "voelt de steel van een pan zo snel heet aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee voorwerpen die elkaar raken, houden elk hun eigen temperatuur.",
        antwoord=False,
        uitleg="Er stroomt warmte van het warme naar het koude tot ze gelijk staan. Die "
        "toestand heet thermisch evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je giet \(1{,}0\) kg water van \(80\ ^\circ\text{C}\) bij \(1{,}0\) kg water van \(20\ ^\circ\text{C}\). Welke temperatuur krijg je?",
        opties=[
            r"\(50\ ^\circ\text{C}\)",
            r"\(60\ ^\circ\text{C}\)",
            r"\(100\ ^\circ\text{C}\)",
            r"\(30\ ^\circ\text{C}\)",
        ],
        antwoord=0,
        uitleg="De massa's zijn gelijk, dus ligt het antwoord precies in het midden. De "
        "warmte die het ene afgeeft, neemt het andere op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een voorwerp van \(1000\) K bevat altijd meer warmte dan een voorwerp van \(300\) K.",
        antwoord=False,
        uitleg=r"Een vonk van \(1000\) K bevat veel minder energie dan een bad van "
        r"\(300\) K. De massa en de stof tellen even hard mee als de temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de drie manieren waarop warmte zich verplaatst? Kruis alles aan wat juist is.",
        opties=[
            "geleiding, door contact tussen de deeltjes",
            "stroming, doordat warm water of lucht stijgt",
            "straling, doordat een warm voorwerp licht uitzendt",
            "weerstand, doordat de warmte wordt tegengehouden",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn geleiding, convectie en straling. Weerstand is geen "
        "manier van verplaatsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zit er tussen de twee glazen van een thermosfles een vacuüm?",
        opties=[
            "zonder deeltjes kan er geen warmte geleid of gestroomd worden",
            "een vacuüm houdt ook de warmtestraling volledig tegen",
            "een vacuüm koelt de inhoud van de fles actief af",
            "een vacuüm houdt de druk in de fles constant",
        ],
        antwoord=0,
        uitleg="Alleen straling raakt er nog door, en daarom is de wand spiegelend gemaakt. "
        "Zo blijft koffie uren warm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een calorimeterproef zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de warmte die de ene stof afgeeft, neemt de andere op",
            "het vat moet zo goed mogelijk geïsoleerd zijn",
            "het vat moet open staan om de warmte te laten ontsnappen",
            "de twee stoffen moeten dezelfde massa hebben",
        ],
        antwoord=[0, 1],
        uitleg="Verschillende massa's mogen gerust, je rekent ze dan apart. Een open vat zou "
        "net warmte verliezen en de meting bederven.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een stijging van \(10\) K is hetzelfde als een stijging van \(10\ ^\circ\text{C}\).",
        antwoord=True,
        uitleg=r"De twee schalen hebben even grote stappen, enkel hun nulpunt verschilt. Bij "
        r"een \(\Delta T\) mag je dus wel in celsius rekenen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de toestand waarin twee voorwerpen geen warmte meer uitwisselen?",
        antwoord=["thermisch evenwicht", "evenwicht", "het thermisch evenwicht"],
        uitleg="Ze hebben dan dezelfde temperatuur. Een thermometer werkt net doordat hij "
        "die toestand met het voorwerp bereikt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de overgang van vast naar vloeibaar?",
        opties=[
            "smelten",
            "stollen",
            "verdampen",
            "sublimeren",
        ],
        antwoord=0,
        uitleg=r"De omgekeerde overgang heet stollen. Water doet dat bij "
        r"\(0\ ^\circ\text{C}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zes faseovergangen bestaan er? Kruis alles aan wat juist is.",
        opties=[
            "smelten en stollen",
            "verdampen en condenseren",
            "sublimeren en rijpen",
            "oplossen en neerslaan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Oplossen is geen faseovergang maar een mengsel maken. Rijpen is van gas "
        "rechtstreeks naar vast.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de overgang van vast rechtstreeks naar gas?",
        antwoord=["sublimeren", "sublimatie", "subliminatie"],
        uitleg="Droogijs doet dat, en daarom laat het geen plas achter. De omgekeerde weg "
        "heet rijpen.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens het smelten blijft de temperatuur van een zuivere stof gelijk.",
        antwoord=True,
        uitleg="Alle warmte gaat naar het losmaken van de deeltjes. Op een smeltcurve zie je "
        "daar een horizontaal stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je op een smeltcurve van een zuivere stof?",
        opties=[
            "een stijging, dan een horizontaal stuk, dan weer een stijging",
            "een rechte stijging van begin tot eind",
            "een daling, dan een horizontaal stuk, dan een stijging",
            "een horizontaal stuk van begin tot eind",
        ],
        antwoord=0,
        uitleg="Het horizontale stuk ligt op het smeltpunt en duurt tot alles gesmolten is. "
        "Bij een mengsel is dat stuk niet vlak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de specifieke smeltwarmte van een stof?",
        opties=[
            "de warmte om één kilogram ervan te laten smelten",
            "de warmte om één kilogram ervan één kelvin op te warmen",
            "de temperatuur waarbij één kilogram ervan smelt",
            "de warmte die één kilogram ervan bij stollen opneemt",
        ],
        antwoord=0,
        uitleg=r"Het symbool is \(l\), in \(\text{J/kg}\). Je rekent ermee als "
        r"\(Q = l\,m\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke formule bereken je de warmte voor een faseovergang?",
        opties=[
            r"\(Q = l\,m\)",
            r"\(Q = l\,m\,\Delta T\)",
            r"\(Q = \dfrac{l}{m}\)",
            r"\(Q = l\,\Delta T\)",
        ],
        antwoord=0,
        uitleg=r"Er staat geen \(\Delta T\) in, want de temperatuur verandert niet. Dat is "
        r"net het kenmerk van een faseovergang.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel warmte heb je nodig om \(0{,}50\) kg ijs van \(0\ ^\circ\text{C}\) te laten smelten? Neem \(l = 334\) kJ/kg.",
        opties=[
            r"\(167\) kJ",
            r"\(334\) kJ",
            r"\(668\) kJ",
            r"\(84\) kJ",
        ],
        antwoord=0,
        uitleg=r"\(Q = l\,m = 334 \times 0{,}50 = 167\) kJ. Daarna begint de temperatuur "
        r"pas te stijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="De specifieke verdampingswarmte van water is kleiner dan zijn specifieke smeltwarmte.",
        antwoord=False,
        uitleg=r"Ze is juist veel groter: \(2256\) tegenover \(334\) kJ/kg. Bij verdampen "
        r"moeten de deeltjes helemaal los van elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom voelt het koel aan als er water op je huid verdampt?",
        opties=[
            "het verdampende water neemt warmte van je huid mee",
            "het water is altijd kouder dan je eigen huid",
            "de lucht rond je huid wordt door het water verwarmd",
            "het water houdt de warmtestraling van de zon tegen",
        ],
        antwoord=0,
        uitleg="Verdampen kost veel energie, en die haalt het water uit je huid. Daarom "
        "zweten we om af te koelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het kookpunt zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het hangt af van de druk boven de vloeistof",
            "bij lagere druk ligt het kookpunt lager",
            r"het is voor elke vloeistof \(100\ ^\circ\text{C}\)",
            "het is altijd hoger dan het smeltpunt van de stof",
        ],
        antwoord=[0, 1, 3],
        uitleg=r"\(100\ ^\circ\text{C}\) is het kookpunt van water bij normale druk, niet "
        r"van elke vloeistof. Hoog in de bergen kookt water bij een lagere temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat koken in een snelkookpan sneller?",
        opties=[
            "de hogere druk duwt het kookpunt van water naar boven",
            "de hogere druk duwt het kookpunt van water naar beneden",
            "de pan geeft de warmte sneller aan het water door",
            "de pan houdt de damp vast en die kookt het eten mee",
        ],
        antwoord=0,
        uitleg=r"Het water wordt dan heter dan \(100\ ^\circ\text{C}\) zonder weg te "
        r"koken. Heter water gaart het eten sneller.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de overgang van gas naar vloeistof?",
        antwoord=["condenseren", "condensatie", "condenseert"],
        uitleg="Dat zie je op een koud raam in de winter. De omgekeerde weg heet verdampen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je op een stolcurve van een zuivere stof?",
        opties=[
            "een daling, dan een horizontaal stuk, dan weer een daling",
            "een stijging, dan een horizontaal stuk, dan een daling",
            "een rechte daling van begin tot eind",
            "een daling, dan een stijging, dan weer een daling",
        ],
        antwoord=0,
        uitleg="Op het horizontale stuk geeft de stof warmte af terwijl ze stolt. De "
        "thermometer beweegt daar niet, al koelt het voorwerp wel af.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij stollen geeft een stof warmte af aan haar omgeving.",
        antwoord=True,
        uitleg="Het is de omgekeerde weg van smelten, dus komt diezelfde energie weer vrij. "
        "Daarom koelt een vijver langzamer af zodra er ijs begint te vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke faseovergangen nemen warmte op? Kruis alles aan wat juist is.",
        opties=[
            "smelten",
            "verdampen",
            "sublimeren",
            "condenseren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie gaan naar een lossere toestand en kosten dus energie. Stollen, "
        "condenseren en rijpen geven warmte af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je wil \(1{,}0\) kg water van \(20\ ^\circ\text{C}\) eerst opwarmen tot \(100\ ^\circ\text{C}\) en dan laten verdampen. Welk deel kost de meeste warmte?",
        opties=[
            r"het verdampen, want dat vraagt \(2256\) kJ",
            r"het opwarmen, want dat vraagt \(2256\) kJ",
            r"de twee delen vragen ongeveer evenveel warmte",
            r"het opwarmen, want een faseovergang kost niets",
        ],
        antwoord=0,
        uitleg=r"Het opwarmen vraagt \(4186 \times 1{,}0 \times 80 \approx 335\) kJ. Het "
        r"verdampen vraagt bijna zeven keer zoveel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mengsel heeft net als een zuivere stof één scherp smeltpunt.",
        antwoord=False,
        uitleg="Een mengsel smelt over een temperatuurgebied, dus is dat stuk van de curve "
        "niet vlak. Een scherp smeltpunt is zelfs een teken van zuiverheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom strooit men zout op een besneeuwde weg?",
        opties=[
            "het zout verlaagt het smeltpunt van het ijs",
            "het zout verhoogt het smeltpunt van het ijs",
            "het zout geeft bij het oplossen veel warmte af",
            "het zout houdt de warmte van de weg beter vast",
        ],
        antwoord=0,
        uitleg=r"Pekel bevriest pas onder \(0\ ^\circ\text{C}\), dus blijft het water "
        r"vloeibaar. Bij strenge vorst werkt dat niet meer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de overgang van gas rechtstreeks naar vast?",
        antwoord=["rijpen", "rijping", "rijpt"],
        uitleg="Dat geeft de witte laag op een autoruit in de vroege ochtend. De omgekeerde "
        "weg heet sublimeren.",
    ),
]
