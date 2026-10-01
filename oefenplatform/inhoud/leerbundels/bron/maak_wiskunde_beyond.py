# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde gevorderd op 🌍 Beyond-niveau.

Gebaseerd op de drie vakfiches wiskunde 3de graad doorstroomfinaliteit
(G1, G2 en G3), geldig vanaf 1 januari 2027. Alle drie gelden ze voor
economie-wiskunde, Latijn-wiskunde-wetenschappen en wetenschappen-wiskunde:
het zijn drie examens van hetzelfde vak, dus één vak op het platform.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/wiskunde-gevorderd.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond". Dat is nodig en niet alleen netjes:
Boost doorstroom heeft een vak met precies dezelfde naam, en daar staan
thema's met verwante titels in. De pdf's komen dus naast elkaar in
`leerbundels/wiskunde-gevorderd/` terecht.

Wiskunde staat hier in woorden, niet in symbolen: het platform toont de
vraagtekst als gewone tekst, dus "a tot de macht twee derde" en niet een
exponent in superscript. De bundels volgen diezelfde schrijfwijze, zodat een
kind dezelfde woorden terugvindt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Wiskunde gevorderd"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Machtswortels, machten en logaritmen
BUNDELS["machtswortels-machten-en-logaritmen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Machtswortels, machten en logaritmen",
    onder="Rekenen met rationale exponenten, en de logaritme als de exponent die je zoekt.",
    secties=[
        dict(kop="Machten met een gehele exponent", blokken=[
            ("p", "Je kent de machten met een natuurlijke exponent al. Daar komen twee afspraken bij. "
                  "<strong>Elk getal behalve nul tot de macht nul is gelijk aan één.</strong> Dat is geen "
                  "willekeurige afspraak: a tot de macht n gedeeld door a tot de macht n is enerzijds één, "
                  "en anderzijds a tot de macht nul. En <strong>a tot de macht min n is gelijk aan één "
                  "gedeeld door a tot de macht n</strong>. Een negatieve exponent betekent dus "
                  "<strong>omkeren, niet van teken veranderen</strong>: twee tot de macht min drie is "
                  "één achtste, niet min acht."),
            ("p", tabel(["Rekenregel", "Wat je met de exponenten doet", "Voorbeeld"], [
                ["machten met hetzelfde grondtal vermenigvuldigen", "je telt ze bij elkaar op", "a tot de macht m maal a tot de macht n is a tot de macht m plus n"],
                ["machten met hetzelfde grondtal delen", "je trekt ze van elkaar af", "a tot de macht m gedeeld door a tot de macht n is a tot de macht m min n"],
                ["een macht van een macht", "je vermenigvuldigt ze", "a kwadraat tot de derde macht is a tot de zesde macht"],
                ["een product tot een macht verheffen", "elke factor krijgt die macht", "a maal b, samen tot de macht n, is a tot de macht n maal b tot de macht n"],
            ])),
            ("kader", "Een macht verdeelt zich over een <strong>product</strong> en over een "
                      "<strong>quotiënt</strong>, maar <strong>nooit over een som</strong>. Dat geldt ook "
                      "voor wortels en straks voor logaritmen. Het is de fout die het vaakst gemaakt wordt."),
        ]),
        dict(kop="Machtswortels en rationale exponenten", blokken=[
            ("p", "De <strong>n-de machtswortel uit a</strong> is het getal waarvan de n-de macht a is. "
                  "De <strong>vijfdemachtswortel uit tweeëndertig is twee</strong>, want twee tot de vijfde "
                  "is tweeëndertig. De <strong>derdemachtswortel uit min acht is min twee</strong>, want min "
                  "twee tot de derde is min acht."),
            ("p", "<strong>De n-de machtswortel uit een negatief getal bestaat in de reële getallen alleen "
                  "als n oneven is.</strong> Een even macht van een reëel getal is immers nooit negatief, "
                  "dus de vierkantswortel of de vierdemachtswortel uit een negatief getal bestaat niet in R."),
            ("p", "Een macht met een <strong>rationale exponent</strong> is niets anders dan een wortel. "
                  "<strong>a tot de macht één op n is de n-de machtswortel uit a</strong>: a tot de macht "
                  "één derde is de derdemachtswortel uit a, en zestien tot de macht een half is de "
                  "vierkantswortel uit zestien, dus vier. Algemeen is <strong>a tot de macht m op n gelijk "
                  "aan de n-de machtswortel uit a tot de macht m</strong>: de noemer van de exponent wordt "
                  "de wortelexponent, de teller blijft de macht."),
            ("p", tabel(["Uitdrukking", "Hoe je ze leest", "Uitkomst"], [
                ["acht tot de macht twee derde", "de derdemachtswortel uit acht, dan kwadrateren", "vier"],
                ["zevenentwintig tot de macht twee derde", "de derdemachtswortel uit zevenentwintig, dan kwadrateren", "negen"],
                ["vierenzestig tot de macht één zesde", "de zesdemachtswortel uit vierenzestig", "twee"],
                ["vier tot de macht drie halven", "de wortel uit vier, dan tot de derde", "acht, en dus niet zes"],
            ])),
            ("weetje", "Een <strong>rationale exponent is zonder voorbehoud gedefinieerd voor grondtallen "
                       "groter dan of gelijk aan nul</strong>. Bij een negatief grondtal zou dezelfde "
                       "exponent, anders geschreven, twee verschillende uitkomsten geven. Daarom blijft die "
                       "schrijfwijze beperkt tot niet-negatieve grondtallen, ook al bestaat de "
                       "derdemachtswortel uit min acht gewoon."),
        ]),
        dict(kop="Wortels vereenvoudigen", blokken=[
            ("p", "Een wortel schrijf je <strong>zo eenvoudig mogelijk</strong> door er de volkomen "
                  "machten uit te halen. De <strong>vierkantswortel uit vijftig</strong> is de wortel uit "
                  "vijfentwintig maal twee, en dus <strong>vijf keer de vierkantswortel uit twee</strong>."),
            ("p", "<strong>De vierkantswortel uit a plus b is niet gelijk aan de wortel uit a plus de "
                  "wortel uit b.</strong> Probeer het met negen en zestien: de wortel uit vijfentwintig is "
                  "vijf, maar drie plus vier is zeven."),
            ("p", "Een breuk met een wortel in de noemer maak je netter door de "
                  "<strong>noemer rationaal te maken</strong>: je vermenigvuldigt teller en noemer met "
                  "diezelfde wortel. Zo wordt <strong>één gedeeld door de wortel uit drie</strong> gelijk aan "
                  "<strong>de wortel uit drie gedeeld door drie</strong>."),
        ]),
        dict(kop="De logaritme is een exponent", blokken=[
            ("p", "De <strong>logaritme van x met grondtal a</strong> is <strong>de exponent waartoe je a "
                  "verheft om x te krijgen</strong>. Meer is het niet. De logaritme van acht met grondtal "
                  "twee is drie, want twee tot de derde is acht. De logaritme van eenentachtig met grondtal "
                  "drie is vier, want drie tot de vierde is eenentachtig. De logaritme van zestien met "
                  "grondtal twee is <strong>vier</strong>, niet acht."),
            ("p", "Staat er geen grondtal bij, dan bedoelt men <strong>grondtal tien</strong>: de logaritme "
                  "van honderd is twee, en <strong>tien tot de macht min drie is nul komma nul nul "
                  "één</strong>. Schrijft men <strong>ln</strong>, dan is het grondtal <strong>het getal "
                  "e</strong>, ongeveer <strong>2,718</strong>. De natuurlijke logaritme van e is dus één. "
                  "Eén kan nooit een grondtal zijn, en <strong>de logaritme van een negatief getal bestaat "
                  "niet in de reële getallen</strong>, want een macht van een positief grondtal is altijd "
                  "positief."),
            ("p", tabel(["Rekenregel voor logaritmen", "Waarom", "In woorden"], [
                ["de logaritme van een product", "machten tellen hun exponenten op", "de som van de twee logaritmen"],
                ["de logaritme van een quotiënt", "machten trekken hun exponenten af", "de logaritme van x min die van y"],
                ["de logaritme van x tot de macht n", "een macht van een macht vermenigvuldigt", "n maal de logaritme van x"],
                ["de logaritme van één", "elk grondtal tot de macht nul is één", "altijd nul, welk toegelaten grondtal ook"],
            ])),
            ("kader", "<strong>De logaritme van a plus b is niet de logaritme van a plus de logaritme van "
                      "b.</strong> Die regel geldt voor een <strong>product</strong>. De logaritme van een "
                      "<strong>som</strong> kan je niet splitsen."),
        ]),
        dict(kop="Waar je de logaritme voor gebruikt", blokken=[
            ("p", "Een logaritme haalt de onbekende <strong>uit de exponent</strong>. Bij "
                  "<strong>drie tot de macht x is gelijk aan twintig</strong> heb je ze nodig; bij een "
                  "gewone tweedegraadsvergelijking niet. Soms zie je het antwoord meteen: "
                  "<strong>twee tot de macht x is tweeëndertig</strong> geeft <strong>x is vijf</strong>, "
                  "want tweeëndertig is twee tot de vijfde."),
            ("p", "Een logaritme en een macht met hetzelfde grondtal <strong>heffen elkaar op</strong>: "
                  "<strong>tien tot de macht de logaritme van zeven met grondtal tien is gewoon "
                  "zeven</strong>."),
            ("p", "Je rekenapp kent meestal alleen log en ln. Een andere logaritme bereken je met het "
                  "<strong>veranderen van grondtal</strong>: <strong>de logaritme van x gedeeld door de "
                  "logaritme van a</strong>, allebei met hetzelfde nieuwe grondtal. Let op de volgorde: "
                  "het getal waarvan je de logaritme zoekt staat boven, het oude grondtal onder."),
        ]),
    ],
)

# ───────────────────────── 2. Veeltermen, deelbaarheid en Horner
BUNDELS["veeltermen-deelbaarheid-en-horner-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veeltermen, deelbaarheid en Horner",
    onder="De euclidische deling, de reststelling, het schema van Horner en het ontbinden in factoren.",
    secties=[
        dict(kop="De euclidische deling van veeltermen", blokken=[
            ("p", "Delen van veeltermen werkt zoals delen van getallen. Je krijgt een "
                  "<strong>quotiënt</strong> en een <strong>rest</strong>, en er geldt altijd: "
                  "<strong>deeltal is deler maal quotiënt plus rest</strong>. Dat is meteen de controle op "
                  "elke deling; klopt ze niet, dan zit er een rekenfout in je schema."),
            ("p", "Over de rest weet je één ding zeker: <strong>haar graad is kleiner dan die van de "
                  "deler</strong>. Zolang de rest nog even hoog in graad is als de deler, kan je verder "
                  "delen. Deel je door een <strong>tweedegraadsveelterm</strong>, dan heeft de rest dus "
                  "<strong>hoogstens graad één</strong>. <strong>Gaat een deling op, dan is de rest "
                  "nul</strong>; een rest is een veelterm en nooit een graad."),
            ("p", "De graad van het quotiënt vind je door af te trekken: een "
                  "<strong>vijfdegraadsveelterm gedeeld door een tweedegraadsveelterm</strong> geeft een "
                  "quotiënt van <strong>graad drie</strong>."),
        ]),
        dict(kop="De reststelling", blokken=[
            ("p", "<strong>De rest bij de deling van een veelterm P door x min a is gelijk aan P van "
                  "a.</strong> Je hoeft dus niet te delen om de rest te kennen: <strong>invullen "
                  "volstaat</strong>. Is de waarde van P in a bijvoorbeeld zeven, dan is de rest zeven."),
            ("p", "Voorbeeld: deel <strong>x tot de derde min twee x kwadraat plus drie x min vier door x "
                  "min één</strong>. Vul één in: één min twee plus drie min vier is <strong>min twee</strong>. "
                  "Dat is de rest."),
            ("p", "<strong>De reststelling werkt ook bij een deler van de vorm x plus a</strong>: je "
                  "schrijft x plus a als x min min a en vult dan min a in."),
            ("kader", "Het gevolg dat je het vaakst gebruikt: <strong>is de waarde van P in a gelijk aan "
                      "nul, dan is x min a een deler van P</strong>. De rest is dan immers nul en de deling "
                      "gaat op. Neem <strong>x tot de derde min acht</strong>: de waarde voor x gelijk aan "
                      "twee is <strong>nul</strong>, dus x min twee is een deler. Hetzelfde bij "
                      "<strong>twee x kwadraat min drie x plus één</strong> voor x gelijk aan één: twee min "
                      "drie plus één is <strong>nul</strong>."),
        ]),
        dict(kop="Het rekenschema van Horner", blokken=[
            ("p", "Het <strong>rekenschema van Horner</strong> is een snelle schrijfwijze om <strong>te "
                  "delen door een tweeterm x min a</strong>. Voor een deler van hogere graad, zoals x "
                  "kwadraat plus één, werkt het <strong>niet</strong>; daar val je terug op de gewone "
                  "euclidische deling."),
            ("p", "<strong>Bovenaan zet je alle coëfficiënten</strong>, van de hoogste graad tot en met de "
                  "constante term. Voor een <strong>derdegraadsveelterm</strong> zijn dat er dus "
                  "<strong>vier</strong>. Een ontbrekende graad schrijf je als een nul; die mag je niet "
                  "overslaan."),
            ("p", "<strong>Links zet je a</strong>, en niet het getal uit de deler. Deel je door "
                  "<strong>x plus drie</strong>, dan is dat <strong>x min min drie</strong>, dus zet je "
                  "<strong>min drie</strong> links. Dat tekenfoutje is de klassieker van dit hoofdstuk."),
            ("p", "Onderaan verschijnen de <strong>coëfficiënten van het quotiënt</strong>, en het "
                  "<strong>laatste getal is de rest</strong> van de deling, en dus ook de functiewaarde "
                  "in a."),
        ]),
        dict(kop="Nulwaarden", blokken=[
            ("p", "Een <strong>nulwaarde van een veeltermfunctie</strong> is <strong>een x waarvoor de "
                  "functiewaarde nul is</strong>. Op de grafiek zijn dat de snijpunten met de x-as. De "
                  "waarde in nul is iets anders: dat is het snijpunt met de y-as."),
            ("p", "<strong>Een veelterm van graad n heeft hoogstens n reële nulwaarden</strong>, want elke "
                  "nulwaarde levert een factor van graad één op. <strong>Elke veelterm van oneven graad "
                  "heeft er minstens één</strong>: haar grafiek gaat van min oneindig naar plus oneindig en "
                  "moet de x-as dus kruisen."),
            ("p", "Om te testen of een veelterm <strong>deelbaar is door x min één</strong>, vul je één in. "
                  "Bij <strong>x kwadraat plus twee x min drie</strong> geeft dat één plus twee min drie, "
                  "dus nul: ze is deelbaar. Zoek je een gehele nulwaarde van een derdegraadsveelterm met "
                  "gehele coëfficiënten, probeer dan eerst <strong>de delers van de constante term</strong>. "
                  "Een gehele nulwaarde moet die term immers delen, en dat zijn er meestal maar een handvol."),
        ]),
        dict(kop="Ontbinden in factoren", blokken=[
            ("p", "<strong>Je ontbindt een veelterm in factoren om haar nulwaarden en haar delers te "
                  "zien.</strong> Een product is nul zodra één factor nul is, dus elke factor levert meteen "
                  "een nulwaarde op. <strong>Ontbinden is dus een manier om nulwaarden te vinden.</strong>"),
            ("p", tabel(["Merkwaardig product", "Ontbinding of uitwerking", "Let op"], [
                ["a kwadraat min b kwadraat", "a min b, maal a plus b", "het verschil van twee kwadraten"],
                ["a plus b, in het kwadraat", "a kwadraat plus twee ab plus b kwadraat", "de dubbele term twee ab vergeten is de vaakst gemaakte fout"],
                ["a min b, in het kwadraat", "a kwadraat min twee ab plus b kwadraat", "alleen de middelste term wisselt van teken"],
            ])),
            ("p", "De vier manieren die je nodig hebt, naast elkaar. <strong>De gemeenschappelijke factor "
                  "afzonderen</strong>: drie x tot de derde min zes x kwadraat wordt <strong>drie x "
                  "kwadraat, maal x min twee</strong>. <strong>Termen samennemen</strong>: ax plus ay plus "
                  "bx plus by wordt <strong>a plus b, maal x plus y</strong>. <strong>Een merkwaardig "
                  "product herkennen</strong>: x kwadraat min negen wordt <strong>x min drie, maal x plus "
                  "drie</strong>, en vier x kwadraat min twaalf x plus negen is <strong>twee x min drie, in "
                  "het kwadraat</strong>. En <strong>een nulwaarde zoeken en met Horner delen</strong>: "
                  "x tot de derde min acht wordt <strong>x min twee, maal x kwadraat plus twee x plus "
                  "vier</strong>."),
            ("p", "Bij een tweedegraadsveelterm zoek je twee getallen met de juiste som en het juiste "
                  "product. Zo wordt <strong>x kwadraat min vijf x plus zes</strong> gelijk aan "
                  "<strong>x min twee, maal x min drie</strong>. De <strong>discriminant</strong> van die "
                  "veelterm is <strong>één</strong>: vijfentwintig min vierentwintig. Positief, dus er zijn "
                  "twee reële nulwaarden. <strong>Bij een negatieve discriminant zijn er geen reële "
                  "nulwaarden</strong>, en daarom valt <strong>x kwadraat plus vier</strong> in R "
                  "<strong>niet</strong> uiteen in twee factoren van graad één. In de complexe getallen lukt "
                  "dat wel."),
            ("p", "Nog drie uitkomsten om bij de hand te hebben. <strong>x kwadraat min vier heeft twee "
                  "reële nulwaarden</strong>, twee en min twee. De <strong>nulwaarde van twee x min zes is "
                  "drie</strong>. De <strong>som van de nulwaarden van x kwadraat min zeven x plus "
                  "twaalf</strong> is <strong>zeven</strong>, want de nulwaarden zijn drie en vier, en de som "
                  "is min b op a. <strong>x tot de derde min x heeft drie reële nulwaarden</strong>: zonder "
                  "x af te zonderen krijg je x maal x min één maal x plus één, dus nul, één en min één."),
            ("weetje", "<strong>x tot de vierde min zestien</strong> ontbind je zo ver mogelijk in R tot "
                       "<strong>x min twee, maal x plus twee, maal x kwadraat plus vier</strong>. Eerst het "
                       "verschil van kwadraten, dan nog eens op x kwadraat min vier. De laatste factor blijft "
                       "staan, want die heeft geen reële nulwaarden."),
        ]),
    ],
)

# ───────────────────────── 3. Vergelijkingen en ongelijkheden oplossen
BUNDELS["vergelijkingen-en-ongelijkheden-oplossen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vergelijkingen en ongelijkheden oplossen",
    onder="Algebraïsch en grafisch, met bestaansvoorwaarden, kwadrateringsvoorwaarden en tekenschema's.",
    secties=[
        dict(kop="Grafisch oplossen", blokken=[
            ("p", "<strong>De oplossingen van f van x is nul zijn de snijpunten met de horizontale "
                  "as.</strong> Dat zijn net de nulwaarden. Los je <strong>f van x is g van x</strong> "
                  "grafisch op, dan lees je <strong>de x-waarden van de gemeenschappelijke punten</strong> "
                  "af: op een snijpunt zijn beide functiewaarden gelijk, en de oplossing is de x, niet de y."),
            ("p", "Dat geldt ook als je met een grafische rekenapp werkt: <strong>je noteert de x-waarden "
                  "van de snijpunten</strong>. De oplossingenverzameling bestaat uit x-waarden; de y-waarde "
                  "hoort bij het punt, niet bij de oplossing."),
            ("kader", "<strong>Een vergelijking grafisch oplossen geeft niet altijd een exact antwoord.</strong> "
                      "Meestal lees je een benadering af. Wil je exact werken, dan moet je algebraïsch "
                      "oplossen."),
        ]),
        dict(kop="Bestaansvoorwaarden en kwadrateringsvoorwaarden", blokken=[
            ("p", "Voor je begint te rekenen, schrijf je op wat x mág zijn. Bij de "
                  "<strong>vierkantswortel uit x min drie</strong> is de bestaansvoorwaarde "
                  "<strong>x groter dan of gelijk aan drie</strong>: wat onder een even wortel staat mag "
                  "niet negatief zijn, en nul mag wel. Bij de <strong>logaritme van x min twee</strong> is "
                  "ze <strong>x strikt groter dan twee</strong>: het argument van een logaritme moet strikt "
                  "positief zijn, dus nul mag hier niet."),
            ("p", "<strong>Kwadrateren is geen gelijkwaardige bewerking.</strong> Min twee en twee hebben "
                  "hetzelfde kwadraat, dus <strong>door te kwadrateren kan je oplossingen bijkrijgen die "
                  "niet aan de oorspronkelijke vergelijking voldoen</strong>. Daarom moet je na het "
                  "kwadrateren van een irrationale vergelijking <strong>elke gevonden oplossing in de "
                  "oorspronkelijke vergelijking controleren</strong>."),
            ("p", "Voorbeeld: <strong>de wortel uit x plus één is gelijk aan x min één</strong>. Kwadrateren "
                  "geeft x kwadraat min drie x is nul, dus nul of drie. <strong>De oplossing is x is "
                  "drie.</strong> <strong>Nul is geen geldige oplossing</strong>: vul het in en links staat "
                  "de wortel uit één, dus één, terwijl rechts min één staat. Nul is een valse oplossing van "
                  "het kwadrateren."),
        ]),
        dict(kop="Vergelijkingen van elk soort", blokken=[
            ("p", tabel(["Vergelijking", "Hoe je ze aanpakt", "Oplossing"], [
                ["vijf x min twintig is nul", "twintig gedeeld door vijf", "x is vier"],
                ["x kwadraat is negen", "de wortel nemen, allebei de tekens", "twee oplossingen: drie en min drie"],
                ["twee tot de macht x is acht", "acht schrijven als twee tot de derde", "x is drie"],
                ["drie tot de macht twee x is drie tot de macht x plus vier", "de exponenten gelijkstellen", "x is vier"],
                ["sinus x is nul", "de functie is periodiek", "oneindig veel oplossingen"],
            ])),
            ("p", "De <strong>discriminant van een tweedegraadsvergelijking vertelt hoeveel reële "
                  "oplossingen ze heeft</strong>: positief geeft er twee, nul geeft er één, negatief geen "
                  "enkele. Bij <strong>x kwadraat plus twee x plus één</strong> is de discriminant "
                  "<strong>nul</strong>, dus er is precies één oplossing, min één. Het teken van a bepaalt "
                  "alleen de opening van de parabool."),
            ("p", "<strong>Is de logaritme van x gelijk aan die van y, en bestaan ze allebei, dan is x "
                  "gelijk aan y</strong>: de logaritmische functie is strikt stijgend, dus elke waarde hoort "
                  "bij precies één argument."),
            ("weetje", "<strong>Niet elke vergelijking van de vorm f van x is nul heeft een reële "
                       "oplossing.</strong> Neem x kwadraat plus één: die functie wordt nooit nul, want haar "
                       "grafiek blijft volledig boven de x-as."),
            ("kader", "<strong>Deel nooit beide leden door een uitdrukking met x in.</strong> Die uitdrukking "
                      "kan nul zijn, en dan gooi je net die oplossing weg. Breng alles naar één lid en "
                      "ontbind in factoren."),
        ]),
        dict(kop="Ongelijkheden lezen van de grafiek", blokken=[
            ("p", "<strong>f van x groter dan nul betekent dat de grafiek boven de horizontale as "
                  "ligt.</strong> Het teken van de functiewaarde is de hoogte ten opzichte van de x-as; "
                  "stijgen is iets anders, dat gaat over de richting. En <strong>f van x kleiner dan g van "
                  "x betekent dat de grafiek van f onder die van g ligt</strong>, met de snijpunten als "
                  "grenzen. Bij <strong>groter dan of gelijk aan</strong> horen de snijpunten erbij, want "
                  "daar zijn de twee functiewaarden gelijk."),
            ("p", "<strong>Ongelijkheden los je grafisch op.</strong> Alleen de tweedegraadsongelijkheid "
                  "moet je ook algebraïsch aankunnen; een ongelijkheid van de vijfde graad hoef je niet met "
                  "de hand te ontbinden."),
        ]),
        dict(kop="Tekenschema en oplossingenverzameling", blokken=[
            ("p", "<strong>De eerste stap bij een tweedegraadsongelijkheid is alles naar één lid brengen "
                  "zodat er nul overblijft.</strong> Pas met nul in het andere lid kan je nulwaarden zoeken "
                  "en een tekenschema maken. In het tekenschema van <strong>x kwadraat min negen</strong> "
                  "zet je <strong>twee nulwaarden</strong>, min drie en drie; die verdelen de getallenas in "
                  "drie stukken."),
            ("p", "Daarna gebruik je de vorm van de parabool van die <strong>tweedegraadsfunctie</strong>. Bij een "
                  "<strong>positieve a met twee nulwaarden is de functie negatief tussen de twee nulwaarden in</strong>; bij een "
                  "<strong>negatieve a met twee nulwaarden is ze net dáár positief</strong>."),
            ("p", tabel(["Ongelijkheid", "Oplossing", "Waarom"], [
                ["twee x min zes groter dan nul", "x groter dan drie", "je deelt door een positief getal, het teken blijft"],
                ["drie x plus negen kleiner dan nul", "x kleiner dan min drie", "negen eraf en door drie delen"],
                ["x kwadraat min vier kleiner dan of gelijk aan nul", "van min twee tot en met twee", "tussen de nulwaarden duikt de dalparabool onder de as"],
                ["x kwadraat min vijf x plus zes groter dan nul", "x kleiner dan twee, of x groter dan drie", "buiten de nulwaarden ligt de dalparabool boven de as"],
                ["x min één, maal x plus twee, kleiner dan nul", "x tussen min twee en één", "een product is negatief bij een verschillend teken"],
                ["x kwadraat groter dan of gelijk aan negen", "x kleiner dan of gelijk aan min drie, of x groter dan of gelijk aan drie", "buiten de nulwaarden min drie en drie"],
            ])),
            ("p", "<strong>x kwadraat plus één groter dan nul geldt voor elke reële x</strong>: een kwadraat "
                  "is nooit negatief, dus de som met één is altijd minstens één. Omgekeerd heeft "
                  "<strong>x kwadraat kleiner dan nul geen enkele reële oplossing</strong>."),
            ("p", "Het resultaat noteer je als <strong>interval</strong>. Ligt x tussen min twee en twee met "
                  "de grenzen inbegrepen, dan is dat een <strong>gesloten interval</strong>, met vierkante "
                  "haken aan beide kanten. Bij een strikte ongelijkheid staan de haken open. Let op: "
                  "<strong>een ongelijkheid heeft meestal een heel interval als oplossing</strong>, dus "
                  "oneindig veel getallen, en niet hoogstens twee losse oplossingen."),
            ("kader", "Twee valkuilen die bij elkaar horen. <strong>Deel je beide leden door een negatief "
                      "getal, dan draait het ongelijkheidsteken om</strong>: twee is kleiner dan vier, maar "
                      "min twee is groter dan min vier. En <strong>vermenigvuldig een ongelijkheid nooit "
                      "zomaar met x</strong>, want het teken van x is niet gekend: is x negatief, dan moet "
                      "het teken omdraaien, en is x nul, dan klopt er niets meer."),
        ]),
    ],
)

# ───────────────────────── 4. Een functie aflezen van haar grafiek
BUNDELS["een-functie-aflezen-van-haar-grafiek-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een functie aflezen van haar grafiek",
    onder="Domein, bereik, symmetrie, verloop en asymptoten, en wat een inverse functie is.",
    secties=[
        dict(kop="Domein, bereik en voorstellingswijzen", blokken=[
            ("p", "<strong>Het domein van een functie zijn alle x-waarden waarvoor ze bestaat.</strong> Het "
                  "ligt op de horizontale as. <strong>Het bereik is de verzameling van alle functiewaarden "
                  "die ze aanneemt</strong>, en dat lees je af op de verticale as. Bij <strong>één gedeeld "
                  "door x min vijf</strong> hoort <strong>vijf</strong> niet bij het domein, want dan wordt "
                  "de noemer nul."),
            ("p", "Het <strong>praktisch domein</strong> is <strong>het stuk van het domein dat zinvol is in "
                  "de context</strong>. Bij een model voor de hoogte van een plant is een negatieve tijd "
                  "betekenisloos, ook al staat die in het wiskundige domein."),
            ("p", "Een functie kan je op <strong>vier manieren voorstellen</strong>: met een "
                  "<strong>verwoording</strong>, met een <strong>tabel</strong>, met een "
                  "<strong>grafiek</strong> en met een <strong>voorschrift</strong>. Je moet van elke "
                  "voorstellingswijze naar elke andere kunnen overstappen."),
            ("kader", "<strong>Een verticale rechte mag de grafiek van een functie hoogstens één keer "
                      "snijden.</strong> Bij twee snijpunten zouden er voor dezelfde x twee functiewaarden "
                      "zijn, en dan is het geen functie meer."),
        ]),
        dict(kop="Nulwaarden, tekenverloop en symmetrie", blokken=[
            ("p", "Een <strong>nulwaarde is een getal</strong>, een <strong>nulpunt is een punt op de "
                  "grafiek</strong>. De nulwaarde is de x waarvoor de functie nul wordt; het nulpunt is het "
                  "punt met die x en met y gelijk aan nul. <strong>Snijdt een grafiek de x-as in drie "
                  "punten, dan heeft de functie drie nulwaarden.</strong>"),
            ("p", "In een <strong>tekenverloop</strong> lees je af <strong>waar de functiewaarden positief "
                  "of negatief zijn</strong>, dus boven of onder de x-as. Stijgen en dalen is iets anders: "
                  "dat is het waardeverloop, en dat lees je af uit de afgeleide."),
            ("p", tabel(["Soort symmetrie", "Wat geldt voor de waarden", "Hoe de grafiek ligt"], [
                ["even functie", "de waarde in min x is dezelfde als in x", "symmetrisch om de verticale as"],
                ["oneven functie", "de waarde in min x is het tegengestelde", "symmetrisch om de oorsprong"],
            ])),
            ("kader", "Verwissel die twee niet. <strong>Een grafiek die symmetrisch is om de oorsprong hoort "
                      "bij een oneven functie</strong>, niet bij een even functie. Bij een oneven functie "
                      "legt een halve draai om de oorsprong de grafiek op zichzelf."),
        ]),
        dict(kop="Het verloop lezen", blokken=[
            ("p", "<strong>Een toenemende stijging betekent dat de grafiek stijgt en daarbij almaar steiler "
                  "wordt.</strong> Bij een afnemende stijging gaat ze wel nog omhoog, maar met een kleinere "
                  "helling. Blijft de helling gelijk, dan spreek je van lineaire groei."),
            ("p", "<strong>Een buigpunt is het punt waar hol in bol overgaat.</strong> Het gaat dus over de "
                  "kromming, niet over de richting. Waar stijgen in dalen overgaat, ligt een maximum."),
            ("p", "<strong>In een maximum bereikt de functie niet altijd haar grootste waarde op het hele "
                  "domein.</strong> Dat geldt alleen voor een <strong>absoluut maximum</strong>. Een "
                  "<strong>plaatselijk maximum</strong> is enkel de hoogste waarde in zijn eigen omgeving; "
                  "verderop kan de grafiek nog hoger gaan."),
            ("p", "Bij een golvende grafiek horen nog twee woorden. De <strong>amplitude</strong> is de "
                  "afstand van de evenwichtslijn tot de top: schommelt een sinusgrafiek tussen min drie en "
                  "drie rond de x-as, dan is de amplitude <strong>drie</strong>. De "
                  "<strong>periode</strong> is de kleinste verschuiving waarna het beeld weer hetzelfde is: "
                  "herhaalt een grafiek zich om de vier eenheden, dan is de periode <strong>vier</strong>."),
        ]),
        dict(kop="Gedrag op oneindig en asymptoten", blokken=[
            ("p", "<strong>Het gedrag van een functie op oneindig is wat er met de functiewaarden gebeurt "
                  "als x heel groot of heel klein wordt.</strong> Oneindig is geen getal, dus de functie "
                  "heeft daar geen waarde; je kijkt naar waar de waarden naartoe kruipen."),
            ("p", "<strong>Een horizontale asymptoot betekent dat de grafiek op oneindig een vaste hoogte "
                  "nadert.</strong> <strong>Niet elke functie heeft een asymptoot</strong>: een gewone "
                  "parabool of een rechte heeft er geen enkele. Asymptoten horen vooral bij rationale, "
                  "exponentiële en logaritmische functies."),
        ]),
        dict(kop="De inverse functie", blokken=[
            ("p", "De <strong>inverse functie</strong> maakt ongedaan wat de functie doet. Je vindt haar "
                  "voorschrift door <strong>x en y te verwisselen en dan naar y op te lossen</strong>. Let "
                  "op: <strong>één gedeeld door de functie is iets anders dan de inverse functie</strong>, "
                  "ook al lijkt de notatie erop."),
            ("p", "<strong>De grafieken van een functie en haar inverse zijn elkaars spiegelbeeld om de "
                  "eerste bissectrice</strong>, de rechte met vergelijking <strong>y is gelijk aan "
                  "x</strong>. Die deelt het eerste en het derde kwadrant doormidden; min x is de tweede "
                  "bissectrice. Spiegelen werkt alleen netjes in een orthonormaal assenstelsel. Bij dat "
                  "spiegelen <strong>wisselen de twee coördinaten van plaats</strong>: het punt nul en twee "
                  "op de y-as wordt <strong>het punt twee en nul op de x-as</strong>. Daarom is ook "
                  "<strong>het domein van de inverse het bereik van de oorspronkelijke functie</strong>."),
            ("p", "<strong>Een functie is niet inverteerbaar als een horizontale rechte haar grafiek meer "
                  "dan één keer snijdt</strong>; bij een inverteerbare functie mag dat dus "
                  "<strong>hoogstens één keer</strong>. Anders hoort dezelfde functiewaarde bij meerdere "
                  "x-waarden en weet de inverse niet welke ze moet teruggeven. Daarom is <strong>de "
                  "kwadraatfunctie niet inverteerbaar op heel haar domein</strong>: twee en min twee hebben "
                  "hetzelfde kwadraat. Beperk je ze <strong>tot de getallen groter dan of gelijk aan "
                  "nul</strong>, dan is ze strikt stijgend en is <strong>de vierkantswortel haar "
                  "inverse</strong>. <strong>Ook niet elke rechte is inverteerbaar</strong>: een "
                  "horizontale rechte wordt na spiegeling een verticale rechte, en dat is geen functie."),
            ("p", tabel(["Functie", "Haar inverse", "Waarom"], [
                ["de exponentiële functie met grondtal a", "de logaritmische functie met grondtal a", "de logaritme geeft net de exponent terug"],
                ["de kwadraatfunctie op de niet-negatieve getallen", "de vierkantswortel", "kwadrateren en worteltrekken heffen elkaar daar op"],
                ["x plus drie", "x min drie", "wat de functie erbij doet, haalt de inverse er weer af"],
                ["twee maal x", "de helft, dus voor tien geeft ze vijf", "de functie verdubbelt, de inverse halveert"],
            ])),
            ("p", "De <strong>boogsinus is de inverse van de sinus op een beperkt domein</strong>. "
                  "<strong>Men beperkt het domein omdat de sinus anders dezelfde waarde oneindig vaak "
                  "aanneemt</strong>: zonder beperking zou de boogsinus bij één getal oneindig veel hoeken "
                  "moeten teruggeven. Boogsinus, boogcosinus en boogtangens heten samen de "
                  "<strong>cyclometrische functies</strong>."),
            ("weetje", "Twee gevolgen die je meteen mag gebruiken. <strong>De inverse van een strikt "
                       "stijgende functie is zelf ook strikt stijgend</strong>, want spiegelen draait de "
                       "volgorde van de punten niet om. En ligt een grafiek <strong>symmetrisch om de eerste "
                       "bissectrice, dan is de functie haar eigen inverse</strong>: één gedeeld door x is zo "
                       "een functie."),
        ]),
    ],
)

# ───────────────────────── 5. Tweedegraadsfuncties en transformaties
BUNDELS["tweedegraadsfuncties-en-transformaties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tweedegraadsfuncties en transformaties",
    onder="De parabool met haar top, nulwaarden en symmetrieas, en de vier transformaties van een grafiek.",
    secties=[
        dict(kop="De parabool", blokken=[
            ("p", "<strong>De grafiek van een tweedegraadsfunctie heet een parabool.</strong> Die van "
                  "één gedeeld door x heet een hyperbool, die van een eerstegraadsfunctie een rechte."),
            ("p", "<strong>Alleen het teken van de coëfficiënt van x kwadraat bepaalt de opening.</strong> "
                  "Is <strong>a positief, dan is het een dalparabool</strong> met een minimum. Is a "
                  "negatief, dan krijg je een <strong>bergparabool</strong>, en die heeft "
                  "<strong>geen</strong> minimum maar een maximum. <strong>Hoe groter de absolute waarde van "
                  "a, hoe smaller de parabool</strong>: een grote a rekt de grafiek verticaal uit."),
            ("p", "<strong>De symmetrieas gaat altijd door de top.</strong> Ze is de verticale rechte door "
                  "de top, dus haar vergelijking is van de vorm x is een getal: bij een top in het punt "
                  "<strong>twee en zeven</strong> is dat <strong>x is gelijk aan twee</strong>."),
            ("p", "Om <strong>één parabool vast te leggen heb je minstens drie punten nodig</strong>, want "
                  "er zijn drie onbekende coëfficiënten a, b en c."),
        ]),
        dict(kop="Top, nulwaarden en discriminant", blokken=[
            ("p", "De <strong>x van de top is min b gedeeld door twee a</strong>. De "
                  "<strong>discriminant is b kwadraat min vier a c</strong>, en haar teken beslist over het "
                  "aantal reële nulwaarden: <strong>positief geeft er twee, nul geeft er één</strong> (de "
                  "parabool raakt de x-as dan precies in haar top), en bij een <strong>negatieve "
                  "discriminant zijn er nul</strong> reële nulwaarden, want de parabool ligt dan volledig "
                  "boven of volledig onder de as."),
            ("p", "<strong>Heeft een parabool twee nulwaarden, dan ligt de x van de top precies in het "
                  "midden ertussen.</strong> Het gemiddelde van de nulwaarden geeft dus de top."),
            ("p", tabel(["Vraag over x kwadraat min zes x plus vijf", "Antwoord", "Hoe"], [
                ["de x van de top", "drie", "min b op twee a, dus zes gedeeld door twee"],
                ["de y van de top", "min vier", "vul drie in: negen min achttien plus vijf"],
                ["de nulwaarden", "één en vijf", "twee getallen met som zes en product vijf"],
                ["het snijpunt met de verticale as", "y is vijf", "vul nul in, enkel de constante term blijft"],
            ])),
            ("p", "Nog een voorbeeld: de <strong>top van min x kwadraat plus vier x</strong> is het punt "
                  "<strong>twee en vier</strong>. Min b op twee a is min vier gedeeld door min twee, dus "
                  "twee, en invullen geeft min vier plus acht."),
            ("p", "Een <strong>dalparabool met top in drie en min vier</strong> heeft als bereik "
                  "<strong>alle getallen vanaf min vier</strong>: de top is het laagste punt. En "
                  "<strong>een parabool kan de verticale as niet twee keer snijden</strong>, want voor x "
                  "gelijk aan nul is er maar één functiewaarde, namelijk c."),
            ("weetje", "Bij de hoogte van een <strong>opgegooide bal</strong>, die een bergparabool volgt, "
                       "is <strong>de top het hoogste punt van de baan</strong>. De landing is de tweede "
                       "nulwaarde en de beginhoogte lees je af op de verticale as."),
        ]),
        dict(kop="De topvorm", blokken=[
            ("p", "Staat een voorschrift in de vorm <strong>a maal x min p, in het kwadraat, plus q</strong>, "
                  "dan lees je <strong>de coördinaten van de top meteen af: p en q</strong>. Dat heet de "
                  "<strong>topvorm</strong>. Let op het minteken in de haakjes: x min drie geeft een top in "
                  "drie, niet in min drie."),
            ("p", "Zo heeft <strong>x min vier, in het kwadraat, plus één</strong> haar top in "
                  "<strong>x gelijk aan vier</strong>, en is bij <strong>x min twee, in het kwadraat, plus "
                  "zeven</strong> de <strong>kleinste functiewaarde zeven</strong>, want een kwadraat is "
                  "minstens nul. Bij <strong>twee maal x min één, in het kwadraat, plus drie</strong> is de "
                  "<strong>y van de top drie</strong>: de factor twee verandert de breedte, niet de ligging "
                  "van de top."),
            ("p", "Omgekeerd kan je uit de topvorm een voorschrift opbouwen. Een parabool met "
                  "<strong>top in vier en twee die door het punt vijf en vijf gaat</strong>, heeft als "
                  "voorschrift <strong>drie maal x min vier, in het kwadraat, plus twee</strong>: vul het "
                  "extra punt in, dan is a plus twee gelijk aan vijf."),
        ]),
        dict(kop="De vier transformaties", blokken=[
            ("p", tabel(["Schrijfwijze", "Wat de grafiek doet", "Geheugensteun"], [
                ["f van x plus drie, buiten de haakjes", "drie eenheden omhoog", "buiten de haakjes werkt verticaal"],
                ["f van x min vijf, buiten de haakjes", "vijf eenheden omlaag", "de hele grafiek zakt, ook de top"],
                ["f van x min twee, binnen de haakjes", "twee eenheden naar rechts", "binnen de haakjes werkt omgekeerd"],
                ["f van x plus drie, binnen de haakjes", "drie eenheden naar links", "ook hier omgekeerd dan het voelt"],
                ["min f van x", "spiegeling om de horizontale as", "elke functiewaarde wisselt van teken"],
                ["drie maal f van x", "verticale uitrekking met factor drie", "de grafiek wordt driemaal zo hoog"],
            ])),
            ("p", "<strong>Twee maal x kwadraat is dus smaller dan x kwadraat</strong>, niet breder: elke "
                  "functiewaarde verdubbelt, dus de parabool loopt sneller omhoog."),
            ("p", "Twee voorbeelden met meerdere stappen. Van <strong>x kwadraat naar x plus één, in het "
                  "kwadraat, min drie</strong> ga je met <strong>één naar links en drie naar "
                  "beneden</strong>; de top komt op min één en min drie. Van <strong>x kwadraat naar twee "
                  "maal x min één, in het kwadraat, plus drie</strong> ga je met <strong>één naar rechts, "
                  "verticaal uitrekken met twee, en drie omhoog</strong>."),
            ("p", "<strong>Spiegel je een dalparabool om de horizontale as, dan krijg je een bergparabool "
                  "met een maximum</strong>: het teken van a draait om."),
        ]),
        dict(kop="Wat een transformatie wel en niet verandert", blokken=[
            ("p", "<strong>Een verticale uitrekking laat de nulwaarden onveranderd</strong>, want nul maal "
                  "een factor blijft nul. Elke verschuiving verplaatst de nulwaarden wel."),
            ("p", "<strong>Een verticale verschuiving verandert het bereik</strong>, want alle "
                  "functiewaarden schuiven mee op, maar ze <strong>laat de symmetrieas op haar "
                  "plaats</strong>: de x van de top blijft dezelfde. Ze <strong>kan wel het tekenverloop "
                  "veranderen</strong>, want de nulwaarden verschuiven: een dalparabool die net onder de as "
                  "lag, kan er na twee omhoog helemaal boven komen, en dan zijn de nulwaarden weg."),
            ("p", "<strong>Een horizontale verschuiving verandert het domein van een tweedegraadsfunctie "
                  "niet</strong>: dat is en blijft heel R. Bij een wortelfunctie zou het wel veranderen."),
            ("weetje", "<strong>De linkertak van een gewone dalparabool daalt, met een afnemende "
                       "daling</strong>: ze gaat omlaag, maar steeds minder steil, tot ze in de top even "
                       "vlak loopt."),
        ]),
    ],
)

# ───────────────────────── 6. Exponentiële en logaritmische functies
BUNDELS["exponentiele-en-logaritmische-functies-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Exponentiële en logaritmische functies",
    onder="De twee grafieken en hun asymptoten, en groeimodellen met groeifactor, verdubbelings- en halveringstijd.",
    secties=[
        dict(kop="De exponentiële functie", blokken=[
            ("p", "<strong>Het domein van a tot de macht x zijn alle reële getallen</strong>: je mag elke "
                  "exponent nemen, ook negatieve en gebroken. <strong>Het bereik zijn de strikt positieve "
                  "getallen</strong>: een macht van een positief grondtal wordt nooit nul of negatief. "
                  "<strong>Zonder transformatie kan zo'n functie dus geen negatieve waarden aannemen.</strong>"),
            ("p", "Elke grafiek van a tot de macht x gaat door <strong>het punt nul en één</strong>, want "
                  "elk grondtal tot de macht nul is één, en door <strong>het punt één en a</strong>. Dat "
                  "tweede punt is handig: <strong>in x gelijk aan één lees je het grondtal rechtstreeks "
                  "af</strong>. Gaat de grafiek door het punt één en vijf, dan is het grondtal "
                  "<strong>vijf</strong>. Zo is ook de functiewaarde van <strong>drie tot de macht x in "
                  "twee gelijk aan negen</strong>."),
            ("p", "<strong>Is a groter dan één, dan stijgt de functie</strong>; dat geldt dus ook voor "
                  "grondtal <strong>e</strong>, dat ongeveer 2,718 is. <strong>Ligt a tussen nul en één, "
                  "dan daalt ze</strong>: een half tot de macht drie is een achtste. <strong>Het getal één "
                  "is niet toegelaten als grondtal, omdat de grafiek dan een horizontale rechte "
                  "wordt</strong>, en een constante functie groeit niet."),
            ("p", "<strong>Twee tot de macht x heeft de rechte y is nul als horizontale asymptoot.</strong> "
                  "<strong>De grafiek snijdt haar asymptoot nooit</strong>; ze nadert die alleen oneindig "
                  "dicht. Schuif je de grafiek op, dan schuift de asymptoot mee: <strong>twee tot de macht "
                  "x, plus vijf, heeft de rechte y is vijf</strong>, en <strong>twee tot de macht x, min "
                  "vier, is vier eenheden naar beneden geschoven</strong>, met asymptoot y is min vier. "
                  "<strong>Spiegel je twee tot de macht x om de horizontale as, dan wordt het bereik de "
                  "strikt negatieve getallen.</strong>"),
        ]),
        dict(kop="De logaritmische functie", blokken=[
            ("p", "<strong>Het domein van de logaritmische functie bestaat uit alle getallen strikt groter "
                  "dan nul</strong>: alleen strikt positieve argumenten hebben een logaritme. Daarom heeft "
                  "ze <strong>een verticale asymptoot</strong>: voor x die naar nul kruipt, duikt de "
                  "logaritme naar min oneindig, dus de y-as is die asymptoot."),
            ("p", "<strong>Haar grafiek gaat altijd door het punt één en nul</strong>, want de logaritme van "
                  "één is nul bij elk grondtal. Dat is net het spiegelbeeld van het punt nul en één van de "
                  "exponentiële functie."),
            ("p", "<strong>De exponentiële functie en de logaritmische functie met hetzelfde grondtal zijn "
                  "elkaars spiegelbeeld om de eerste bissectrice.</strong> Het zijn elkaars inverse "
                  "functies, en inverse functies spiegelen altijd om de rechte y is x."),
        ]),
        dict(kop="Groeifactor en procenten", blokken=[
            ("p", "Een <strong>groeifactor</strong> is het getal waarmee je per tijdseenheid "
                  "vermenigvuldigt. <strong>Hij is nooit negatief.</strong> Bij een toename van p procent "
                  "is hij <strong>één plus p gedeeld door honderd</strong>; bij een afname blijft er p "
                  "procent over."),
            ("p", tabel(["Situatie", "Groeifactor", "In woorden"], [
                ["drie procent groei per jaar", "1,03", "één plus drie honderdsten"],
                ["twintig procent daling per jaar", "0,8", "er blijft tachtig procent over"],
                ["vijf procent samengestelde intrest", "1,05", "elk jaar met dezelfde factor"],
                ["van honderd naar honderdvijftig", "1,5", "honderdvijftig gedeeld door honderd"],
                ["groeifactor 1,12 gegeven", "twaalf procent erbij", "trek één af en maal honderd"],
            ])),
            ("p", "<strong>Een groeifactor kleiner dan één betekent dat de hoeveelheid afneemt.</strong> Bij "
                  "precies één blijft alles gelijk."),
            ("p", "Groeifactoren combineer je door te <strong>vermenigvuldigen</strong>, nooit door op te "
                  "tellen. <strong>Van een maandfactor naar een jaarfactor verhef je tot de macht "
                  "twaalf</strong>, en <strong>is de jaarfactor twee, dan is de factor per twee jaar "
                  "vier</strong>. Daaruit volgt ook een bekende valstrik: <strong>een stijging met tien "
                  "procent gevolgd door een daling met tien procent brengt je niet terug bij de "
                  "beginwaarde</strong>, want 1,1 maal 0,9 is 0,99, dus je verliest één procent."),
        ]),
        dict(kop="Groeimodellen", blokken=[
            ("p", "In het model <strong>b maal a tot de macht x</strong> is <strong>b de "
                  "beginwaarde</strong>: bij <strong>tweehonderd maal 1,05 tot de macht x</strong> is de "
                  "beginwaarde <strong>tweehonderd</strong>, want voor x gelijk aan nul is de macht één."),
            ("p", tabel(["Soort groei", "Vorm", "Waaraan je ze herkent"], [
                ["lineaire groei", "a maal x plus b", "elke tijdseenheid komt hetzelfde getal erbij"],
                ["exponentiële groei", "b maal a tot de macht x", "elke tijdseenheid dezelfde vermenigvuldigingsfactor"],
            ])),
            ("p", "Staat in een tabel bij elke stap van één in x <strong>dezelfde "
                  "vermenigvuldigingsfactor</strong>, dan past een <strong>exponentieel model</strong>. De "
                  "rij <strong>3, 6, 12, 24</strong> is exponentieel, telkens maal twee. Een rij met een "
                  "vaste toename is lineair. <strong>Kies een lineair model als de verandering per "
                  "tijdseenheid even groot blijft</strong>: een vast bedrag sparen per maand is lineair, "
                  "intrest op intrest is exponentieel. <strong>Bij exponentiële groei komt er niet elke "
                  "tijdseenheid evenveel bij</strong>, maar elke tijdseenheid hetzelfde percentage, en dus "
                  "in absolute aantallen steeds meer."),
            ("p", "De <strong>verdubbelingstijd</strong> is <strong>de tijd die nodig is om twee keer zo "
                  "groot te worden</strong>, en bij exponentiële groei is die altijd even lang, waar je ook "
                  "begint te meten. De <strong>halveringstijd hoort bij een groeifactor kleiner dan "
                  "één</strong>; radioactief verval is het bekendste voorbeeld. Heeft een stof een "
                  "halveringstijd van vijf jaar, dan blijft er <strong>na tien jaar een kwart</strong> over."),
            ("p", "<strong>Om te berekenen na hoeveel jaar een bedrag met groeifactor 1,05 verdubbeld is, "
                  "heb je een logaritme nodig</strong>, want de onbekende staat in de exponent: je lost "
                  "1,05 tot de macht t is twee op. Honderd delen door het percentage is enkel een ruwe "
                  "vuistregel."),
            ("kader", "Twee grenzen aan zo'n model. <strong>Een zuiver exponentieel model voorspelt een "
                      "groei die nooit stopt</strong>, terwijl echte groei vastloopt op voedsel, ruimte of "
                      "geld. En <strong>een groeimodel heeft vaak een praktisch domein</strong>, omdat een "
                      "negatieve tijd meestal geen betekenis heeft."),
        ]),
    ],
)

# ───────────────────────── 7. Goniometrische functies en goniometrie
BUNDELS["goniometrische-functies-en-goniometrie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Goniometrische functies en goniometrie",
    onder="Driehoeken oplossen met de sinus- en cosinusregel, de goniometrische cirkel, en de algemene sinusfunctie.",
    secties=[
        dict(kop="Driehoeken oplossen", blokken=[
            ("p", "<strong>De som van de hoeken in een driehoek is honderdtachtig graden.</strong> Ken je "
                  "twee hoeken, dan volgt de derde daar meteen uit."),
            ("p", tabel(["Wat je kent", "Welke regel", "Waarom"], [
                ["een zijde samen met de hoek ertegenover", "de sinusregel", "die koppelt telkens een zijde aan haar overstaande hoek"],
                ["twee zijden en de hoek ertussen", "de cosinusregel", "er is geen zijde met haar overstaande hoek bekend"],
                ["de drie zijden", "de cosinusregel", "de sinusregel heeft altijd één gekende hoek nodig"],
            ])),
            ("p", "<strong>De cosinusregel voor zijde a tegenover hoek A luidt: a kwadraat is b kwadraat "
                  "plus c kwadraat min twee bc maal de cosinus van A.</strong> De hoek in de formule is "
                  "altijd de hoek tegenover de zijde die je zoekt."),
            ("kader", "<strong>De cosinusregel is een veralgemening van de stelling van Pythagoras.</strong> "
                      "Bij een rechte hoek is de cosinus nul, dus valt de laatste term weg en blijft "
                      "Pythagoras over."),
        ]),
        dict(kop="Graden en radialen", blokken=[
            ("p", "<strong>Pi radialen is honderdtachtig graden</strong>, en daaruit volgt elke andere "
                  "omzetting. <strong>Twee pi radialen is driehonderdzestig graden</strong>, een volledige "
                  "omwenteling. <strong>Negentig graden is pi gedeeld door twee</strong> radialen en "
                  "<strong>pi gedeeld door drie radialen is zestig graden</strong>. <strong>Eén radiaal is "
                  "ongeveer zevenenvijftig graden</strong>, want honderdtachtig gedeeld door pi is ongeveer "
                  "57,3."),
            ("p", "<strong>Van graden naar radialen vermenigvuldig je met pi en deel je door "
                  "honderdtachtig.</strong> De andere kant op doe je net het omgekeerde. Zet altijd eerst "
                  "je rekenapp in de juiste stand."),
        ]),
        dict(kop="De goniometrische cirkel", blokken=[
            ("p", "<strong>De goniometrische cirkel heeft straal één.</strong> Door de straal op één te "
                  "zetten, zijn de coördinaten van het beeldpunt meteen de cosinus en de sinus. <strong>De "
                  "cosinus is de x-coördinaat en de sinus de y-coördinaat</strong>; die twee verwisselen is "
                  "de klassieke fout."),
            ("p", "Daaruit lees je de bekende waarden af. <strong>De cosinus van nul graden is één</strong> "
                  "(het beeldpunt ligt helemaal rechts), <strong>de sinus is gelijk aan één bij negentig "
                  "graden</strong> (het beeldpunt ligt bovenaan), en <strong>de sinus van dertig graden is "
                  "een half</strong>, net als de cosinus van zestig graden. <strong>De sinus van een hoek "
                  "kan nooit groter zijn dan één</strong>, want ze is een coördinaat op een cirkel met "
                  "straal één. De tangens kent die grens niet."),
            ("p", "<strong>De grondformule van de goniometrie luidt: de sinus in het kwadraat plus de "
                  "cosinus in het kwadraat is één.</strong> Ze volgt rechtstreeks uit Pythagoras op die "
                  "cirkel. De sinus gedeeld door de cosinus is de tangens. <strong>Je gebruikt de "
                  "grondformule vooral om de ene goniometrische functie in de andere om te zetten</strong>: "
                  "ken je de sinus, dan haal je er de cosinus uit, op het teken na, en dat teken bepaal je "
                  "met het kwadrant."),
            ("p", tabel(["Verband tussen twee hoeken", "Hun som of vorm", "Wat geldt"], [
                ["tegengesteld", "de ene is min de andere", "dezelfde cosinus, tegengestelde sinus"],
                ["supplementair", "samen honderdtachtig graden", "dezelfde sinus, tegengestelde cosinus"],
                ["complementair", "samen negentig graden", "de sinus van de ene is de cosinus van de andere"],
            ])),
            ("p", "Bij <strong>tegengestelde hoeken</strong> spiegelt het beeldpunt om de horizontale as; "
                  "bij <strong>supplementaire hoeken</strong> om de verticale as. Bij "
                  "<strong>complementaire hoeken</strong> zie je het meteen in een rechthoekige driehoek: "
                  "de overstaande zijde van de ene is de aanliggende van de andere. Hieruit volgt ook dat "
                  "<strong>de sinus van min x gelijk is aan min de sinus van x</strong>: de sinus is een "
                  "oneven functie, de cosinus een even."),
        ]),
        dict(kop="De algemene sinusfunctie", blokken=[
            ("p", "Schrijf een golvende grafiek als <strong>a maal de sinus van b maal x min c, plus "
                  "d</strong>. Elk van die vier letters doet iets anders."),
            ("p", tabel(["Letter", "Wat ze doet", "Voorbeeld"], [
                ["a", "de amplitude, de hoogte van de golf", "drie maal de sinus van x heeft amplitude drie"],
                ["b", "perst de grafiek samen, de periode wordt twee pi gedeeld door b", "de sinus van twee x heeft periode pi"],
                ["c", "zorgt voor een horizontale verschuiving, de faseverschuiving", "het schuift de hele golf opzij"],
                ["d", "schuift verticaal en bepaalt de evenwichtslijn", "de sinus van x, plus vier, schommelt rond y is vier"],
            ])),
            ("p", "<strong>De periode van de gewone sinusfunctie is twee pi</strong>: na één volledige "
                  "omwenteling begint het beeld opnieuw. <strong>De sinus van drie x heeft een periode die "
                  "drie keer korter is.</strong> De <strong>frequentie van een periodieke functie</strong> is <strong>het aantal "
                  "volledige schommelingen per eenheid</strong>, dus één gedeeld door de periode."),
            ("p", "<strong>De amplitude kan niet negatief zijn</strong>, want ze is een afstand. Een "
                  "negatieve factor voor de sinus spiegelt de grafiek wel om de evenwichtslijn. Het bereik "
                  "volgt uit a en d: <strong>twee maal de sinus van x, plus één, loopt van min één tot en "
                  "met drie</strong>, en <strong>de grootste waarde van vijf maal de sinus van x is "
                  "vijf</strong>. <strong>Tussen nul en twee pi, de grenzen inbegrepen, heeft de sinus drie "
                  "nulwaarden</strong>: in nul, in pi en in twee pi."),
            ("weetje", "<strong>Een sinusfunctie is een geschikt model voor het getij aan de kust.</strong> "
                       "Het water stijgt en daalt met een vaste periode rond een gemiddeld peil, en dat is "
                       "precies wat zo'n functie beschrijft."),
        ]),
        dict(kop="Goniometrische formules", blokken=[
            ("p", "<strong>De verdubbelingsformule voor de sinus luidt: de sinus van twee x is twee maal de "
                  "sinus van x maal de cosinus van x.</strong> Ze volgt uit de somformule met twee gelijke "
                  "hoeken; gewoon maal twee werkt niet. <strong>De cosinus van twee x is evenmin twee maal "
                  "de cosinus van x</strong>: de juiste formule is de cosinus in het kwadraat min de sinus "
                  "in het kwadraat. Een goniometrisch getal is geen factor die je zomaar buiten haalt."),
            ("p", "<strong>De formules van Simpson zetten een som van sinussen om in een product.</strong> "
                  "Ze heten daarom ook de som-naar-productformules, en ze zijn handig om een vergelijking "
                  "te ontbinden in factoren."),
            ("kader", "<strong>Een goniometrische identiteit bewijs je door één lid te herleiden tot het "
                      "andere met bekende formules.</strong> Enkele hoeken invullen toont alleen dat ze "
                      "daar klopt, niet dat ze altijd klopt. Een grafiek is een aanwijzing, geen bewijs."),
        ]),
    ],
)

# ───────────────────────── 8. Limieten, continuïteit en asymptoten
BUNDELS["limieten-continuiteit-en-asymptoten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Limieten, continuïteit en asymptoten",
    onder="Wat een limiet is, hoe je onbepaaldheden wegwerkt, en hoe je alle soorten asymptoten vindt.",
    secties=[
        dict(kop="Wat een limiet zegt", blokken=[
            ("p", "<strong>De limiet van f voor x naar a is b</strong> betekent: <strong>de functiewaarden "
                  "naderen b als x dicht genoeg bij a komt</strong>. Een limiet zegt dus iets over de "
                  "<strong>buurt</strong> van a, niet over a zelf. <strong>Een functie hoeft in a niet "
                  "gedefinieerd te zijn om daar een limiet te hebben.</strong>"),
            ("p", "In de <strong>epsilon-deltadefinitie</strong> is <strong>epsilon eerst gegeven</strong>: "
                  "de gewenste nauwkeurigheid op de y-as. Iemand daagt je uit met een epsilon, en jij moet "
                  "er een delta bij vinden. Die volgorde omdraaien maakt de definitie betekenisloos."),
            ("p", "<strong>De limiet in een punt bestaat als de linkerlimiet en de rechterlimiet gelijk "
                  "zijn.</strong> Verschillen ze, dan maakt de grafiek daar een sprong. Daarom "
                  "<strong>bestaat de limiet voor x naar nul van één gedeeld door x niet</strong>: van "
                  "links kruipt ze naar min oneindig, van rechts naar plus oneindig. Bij <strong>één "
                  "gedeeld door x kwadraat is de limiet in nul wel plus oneindig</strong>, want een "
                  "kwadraat is langs beide kanten positief."),
            ("p", "Is de functie <strong>continu</strong>, dan mag je gewoon invullen: de "
                  "<strong>limiet voor x naar drie van x plus vijf is acht</strong>."),
        ]),
        dict(kop="Onbepaaldheden wegwerken", blokken=[
            ("p", "<strong>Een onbepaaldheid is een vorm waaruit je de uitkomst nog niet kan "
                  "afleiden.</strong> Nul op nul kan alles opleveren: een getal, oneindig of niets. Je moet "
                  "eerst herschrijven."),
            ("p", tabel(["Wat je krijgt", "Wat je doet", "Voorbeeld"], [
                ["teller en noemer allebei nul", "ontbinden en de gemeenschappelijke factor schrappen", "x kwadraat min vier op x min twee geeft in twee de limiet vier"],
                ["teller niet nul, noemer wel", "er ligt een pool, dus plus of min oneindig", "met een tekenonderzoek links en rechts bepaal je het teken"],
                ["oneindig min oneindig met twee wortels", "vermenigvuldigen met de toegevoegde tweeterm", "het verschil maal de som laat de wortels verdwijnen"],
                ["een breuk op oneindig", "de hoogstegraadstermen tegen elkaar afwegen", "drie x kwadraat plus één op x kwadraat min vijf geeft drie"],
            ])),
            ("p", "<strong>De limiet voor x naar plus oneindig van twee x plus één, gedeeld door x "
                  "kwadraat, is nul</strong>: de noemer groeit sneller dan de teller. In het algemeen "
                  "<strong>bepaalt enkel de term met de hoogste graad het gedrag van een veeltermfunctie op "
                  "oneindig</strong>. Bij een <strong>irrationale functie</strong> is de eerste stap "
                  "<strong>de hoogstegraadsterm buiten de wortel afzonderen</strong>."),
            ("p", "<strong>De regel van de l'Hôpital mag je rechtstreeks toepassen op nul op nul en op "
                  "oneindig op oneindig.</strong> De andere onbepaaldheden, zoals nul maal oneindig of "
                  "oneindig min oneindig, moet je eerst omvormen tot een van die twee breuken. <strong>Op "
                  "twee gedeeld door nul mag je l'Hôpital niet toepassen</strong>: dat is geen "
                  "onbepaaldheid maar een pool."),
            ("p", "De gewone <strong>rekenregels</strong> helpen zolang de limieten bestaan en eindig zijn: "
                  "<strong>de limiet van een som is de som van de limieten</strong>. Bij oneindig moet je "
                  "opletten voor onbepaaldheden."),
            ("weetje", "<strong>Een perforatie is een punt dat op de grafiek ontbreekt terwijl de limiet er "
                       "wel bestaat.</strong> Je tekent er een open bolletje. De functie is er niet "
                       "gedefinieerd, maar de grafiek loopt er verder gewoon door."),
        ]),
        dict(kop="Continuïteit", blokken=[
            ("p", "<strong>Een functie is continu in a als de functiewaarde in a bestaat en gelijk is aan "
                  "de limiet daar.</strong> Drie dingen moeten dus kloppen: de limiet bestaat, de "
                  "functiewaarde bestaat, en ze zijn gelijk. <strong>Op een grafiek betekent continuïteit "
                  "dat je ze kan tekenen zonder je pen op te heffen.</strong> Een knik mag wel."),
            ("p", "<strong>Elke veeltermfunctie is continu op heel haar domein</strong>: er zit geen noemer "
                  "en geen wortel in, dus nergens een pool of een sprong. <strong>Eén gedeeld door x is "
                  "niet continu in nul</strong>, want die functie bestaat daar niet. <strong>Verschillen de "
                  "linker- en de rechterlimiet in een punt, dan zie je een sprong in de grafiek</strong>; "
                  "bij een gat zijn de twee limieten net wel gelijk, maar ontbreekt de functiewaarde."),
            ("p", "<strong>Continuïteit is belangrijk omdat je de limiet dan mag berekenen door gewoon in "
                  "te vullen.</strong> En <strong>een functie die in een punt afleidbaar is, is daar zeker "
                  "ook continu</strong>; omgekeerd geldt het niet, want de absolute waarde is continu in "
                  "nul maar heeft er een knik en dus geen afgeleide."),
        ]),
        dict(kop="Asymptoten", blokken=[
            ("p", tabel(["Soort asymptoot", "Hoe je ze vindt", "Wanneer ze er is"], [
                ["verticaal", "de noemer nulstellen", "bij een pool van de functie"],
                ["horizontaal", "de limiet op plus en min oneindig berekenen", "als die limiet een getal is"],
                ["schuin", "de euclidische deling, of de formules van Cauchy", "als de graad van de teller precies één hoger is"],
            ])),
            ("p", "<strong>Eén gedeeld door x min drie heeft één verticale asymptoot</strong>, met "
                  "vergelijking <strong>x is drie</strong>. <strong>Een verticale asymptoot hoort bij een "
                  "pool</strong>: daar gaat de functiewaarde naar plus of min oneindig."),
            ("p", "<strong>Drie x plus één, gedeeld door x min twee, heeft de rechte y is drie als "
                  "horizontale asymptoot</strong>: teller en noemer hebben dezelfde graad, dus je deelt de "
                  "hoogste coëfficiënten. <strong>Een grafiek mag haar horizontale asymptoot snijden</strong>, "
                  "zelfs meermaals; alleen op oneindig moet ze er onbeperkt dicht bij komen. Een verticale "
                  "asymptoot snijden kan niet."),
            ("p", "Bij een <strong>schuine asymptoot</strong> werk je met de <strong>euclidische "
                  "deling</strong>: <strong>het quotiënt van de deling is de vergelijking van de "
                  "asymptoot</strong>, want de rest gedeeld door de noemer kruipt naar nul. Zo heeft "
                  "<strong>x kwadraat plus één, gedeeld door x, als schuine asymptoot y is x</strong>. "
                  "Met de <strong>formules van Cauchy</strong> gaat het ook: de "
                  "<strong>richtingscoëfficiënt is de limiet op oneindig van f van x gedeeld door x</strong>, "
                  "en daarna vind je het snijpunt met de y-as als de limiet van f van x min die "
                  "richtingscoëfficiënt maal x."),
            ("p", "<strong>Een functie kan aan dezelfde kant niet tegelijk een horizontale en een schuine "
                  "asymptoot hebben</strong>: allebei beschrijven ze het gedrag op oneindig, en dat kan maar "
                  "één ding tegelijk zijn. Aan de andere kant kan het wel anders lopen. <strong>Een gewone "
                  "parabool heeft nul asymptoten</strong>: ze groeit wel naar oneindig, maar nadert daarbij "
                  "geen enkele rechte."),
            ("kader", "<strong>Teken asymptoten als stippellijnen</strong>, want ze horen niet bij de "
                      "grafiek. Een asymptoot is een hulplijn die het gedrag beschrijft."),
        ]),
    ],
)

# ───────────────────────── 9. Afgeleiden en het verloop van een functie
BUNDELS["afgeleiden-en-het-verloop-van-een-functie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Afgeleiden en het verloop van een functie",
    onder="Van differentiequotiënt naar raaklijn, de rekenregels, en het volledige functieonderzoek.",
    secties=[
        dict(kop="Van gemiddelde naar ogenblikkelijke verandering", blokken=[
            ("p", "<strong>Een differentiequotiënt berekent de gemiddelde verandering over een "
                  "interval</strong>: je deelt het verschil in functiewaarden door het verschil in x. Voor "
                  "<strong>x kwadraat tussen één en drie</strong> is dat <strong>vier</strong>: negen min "
                  "één is acht, gedeeld door twee."),
            ("p", "<strong>De afgeleide in een punt is de limiet van het differentiequotiënt.</strong> Je "
                  "laat het tweede punt naar het eerste kruipen; de koorde wordt dan de raaklijn. "
                  "<strong>Meetkundig is de afgeleide de richtingscoëfficiënt van de raaklijn in dat "
                  "punt</strong>."),
            ("p", "Een voorbeeld van begin tot eind: de <strong>raaklijn aan x kwadraat in het punt met x "
                  "gelijk aan drie</strong> is <strong>y is zes x min negen</strong>. De helling is zes, "
                  "het raakpunt is drie en negen, en invullen geeft q is min negen."),
        ]),
        dict(kop="De rekenregels", blokken=[
            ("p", tabel(["Functie", "Haar afgeleide", "Let op"], [
                ["x tot de macht n", "n maal x tot de macht n min één", "de exponent komt vooraan en gaat zelf met één omlaag"],
                ["een constante functie", "nul", "de grafiek is een horizontale rechte"],
                ["vijf x plus twee", "vijf", "de afgeleide van een rechte is haar richtingscoëfficiënt"],
                ["de sinus van x", "de cosinus van x", "en de cosinus van x geeft min de sinus van x"],
                ["e tot de macht x", "e tot de macht x", "de machtsregel geldt hier niet, x staat in de exponent"],
                ["de natuurlijke logaritme van x", "één gedeeld door x", "altijd positief, dus de functie stijgt overal"],
            ])),
            ("p", "Zo is de afgeleide van <strong>x kwadraat in drie gelijk aan zes</strong> en die van "
                  "<strong>x tot de derde in twee gelijk aan twaalf</strong>. Sinus wordt cosinus, en "
                  "cosinus wordt min sinus: pas na vier keer afleiden sta je weer bij het begin."),
            ("p", "<strong>De productregel</strong> luidt: <strong>de afgeleide van de eerste maal de "
                  "tweede, plus de eerste maal de afgeleide van de tweede</strong>. <strong>De afgeleide "
                  "van een product is dus niet het product van de afgeleiden</strong>: probeer het met x "
                  "maal x, de afgeleide is twee x en niet één. Bij de <strong>quotiëntregel</strong> staat "
                  "<strong>de noemer van de breuk in het kwadraat in de noemer</strong>, en in de teller "
                  "de afgeleide van de teller maal de noemer, min de teller maal de afgeleide van de "
                  "noemer. Het minteken hoort dus bij de quotiëntregel, niet bij de productregel."),
            ("p", "<strong>De kettingregel</strong> zegt: <strong>de afgeleide van de buitenste functie, "
                  "maal de afgeleide van de binnenste</strong>. Je leidt af van buiten naar binnen en "
                  "vermenigvuldigt onderweg. De binnenste afgeleide vergeten is de klassieke fout."),
        ]),
        dict(kop="De hellinggrafiek", blokken=[
            ("p", "<strong>Op de verticale as van een hellinggrafiek staat de afgeleide van de "
                  "oorspronkelijke functie.</strong> Een hellinggrafiek is dus gewoon de grafiek van de "
                  "afgeleide functie."),
            ("p", "<strong>Waar de functie een vloeiend maximum heeft, snijdt haar afgeleide de "
                  "x-as</strong>: in de top loopt de raaklijn horizontaal, dus is de afgeleide daar nul en "
                  "wisselt ze van teken."),
        ]),
        dict(kop="Stijgen, dalen en extrema", blokken=[
            ("p", "<strong>Is de afgeleide op een interval positief, dan stijgt de functie daar.</strong> "
                  "Het teken van de afgeleide gaat over de richting, niet over de hoogte: een stijgende "
                  "functie kan best negatieve waarden hebben."),
            ("p", "<strong>Is de afgeleide nul in a en wisselt ze daar van plus naar min, dan heeft de "
                  "functie in a een maximum</strong>; van min naar plus geeft een minimum. <strong>Niet elk "
                  "punt waar de afgeleide nul is, is een extremum</strong>: bij x tot de derde is de "
                  "afgeleide nul in nul, maar de functie blijft stijgen. Zonder tekenwissel is er geen "
                  "extremum. En <strong>een functie kan een maximum bereiken in een punt waar ze niet "
                  "afleidbaar is</strong>, zoals in de scherpe punt van min de absolute waarde van x."),
            ("p", "<strong>x tot de derde min drie x heeft twee extrema</strong>: de afgeleide drie x "
                  "kwadraat min drie is nul in min één en in één. Het <strong>minimum ligt bij x gelijk aan "
                  "één</strong>. <strong>Twee nulwaarden van de afgeleide verdelen de getallenas in drie "
                  "stukken</strong> in het tekenschema."),
            ("p", "<strong>Is de tweede afgeleide op een interval positief, dan is de grafiek daar hol</strong>, "
                  "met de holle kant naar boven: de helling neemt toe. <strong>Buigpunten vind je waar de "
                  "tweede afgeleide nul is en van teken wisselt.</strong> <strong>De eerste afgeleide hoeft "
                  "in een buigpunt niet nul te zijn</strong>: een buigpunt kan midden op een stijgend stuk "
                  "liggen, want alleen de kromming verandert er. Is de eerste afgeleide nul in a en de "
                  "tweede daar positief, dan ligt er <strong>een minimum</strong>; dat is de "
                  "tweede-afgeleidetest."),
            ("p", "<strong>Stijgt een functie steeds trager, dan is haar eerste afgeleide positief en haar "
                  "tweede negatief.</strong> Stijgen geeft een positieve eerste afgeleide; trager stijgen "
                  "betekent dat die afgeleide zelf daalt."),
            ("p", "In de <strong>samenvattende tabel van een functieonderzoek</strong> zet je <strong>het "
                  "teken van de eerste en de tweede afgeleide, met stijgen, dalen, hol, bol, extrema en "
                  "buigpunten</strong>. Daarmee kan je de grafiek schetsen zonder nog één punt te berekenen."),
        ]),
        dict(kop="Twee stellingen en de toepassingen", blokken=[
            ("p", "<strong>De stelling van Rolle eist dat de functiewaarden in de twee uiteinden gelijk "
                  "zijn.</strong> Pas dan kan je besluiten dat er ergens tussenin een punt ligt met een "
                  "horizontale raaklijn. <strong>De middelwaardestelling van Lagrange</strong> zegt dat "
                  "<strong>ergens de raaklijn evenwijdig is met de koorde tussen de uiteinden</strong>: er "
                  "is dus een punt waar de ogenblikkelijke verandering gelijk is aan de gemiddelde. Rolle "
                  "is het bijzondere geval waarin die koorde horizontaal loopt."),
            ("p", "<strong>De eerste stap bij een extremumprobleem met context is zelf een veranderlijke "
                  "kiezen en het functievoorschrift opstellen.</strong> Zonder voorschrift valt er niets af "
                  "te leiden. Daarna bereken je de extrema, en <strong>je gaat na of je oplossing in het "
                  "praktisch domein ligt</strong>: een negatieve lengte is wiskundig misschien een "
                  "oplossing, in de opgave niet."),
            ("p", "Twee toepassingen uit de praktijk. Geeft een functie de <strong>afgelegde weg in functie "
                  "van de tijd</strong>, dan is haar afgeleide <strong>de snelheid op dat ogenblik</strong>; "
                  "de afgeleide van de snelheid is de versnelling, en de gemiddelde snelheid is het "
                  "differentiequotiënt over het hele interval. Kent een bedrijf zijn <strong>totale kost in "
                  "functie van het aantal stuks</strong>, dan is de <strong>marginale kost de afgeleide van "
                  "de totale kost</strong>: ze zegt wat één extra stuk ongeveer kost."),
            ("weetje", "<strong>Is de afgeleide overal positief, dan is de functie overal strikt stijgend "
                       "en dus inverteerbaar.</strong> Strikt stijgend betekent immers dat elke "
                       "functiewaarde maar één keer voorkomt."),
        ]),
    ],
)

# ───────────────────────── 10. Rijen en hun limiet
BUNDELS["rijen-en-hun-limiet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rijen en hun limiet",
    onder="Rekenkundige en meetkundige rijen, hun sommen, en wat convergeren betekent.",
    secties=[
        dict(kop="Twee soorten rijen", blokken=[
            ("p", tabel(["Soort rij", "Wat je telkens doet", "Hoe het vaste getal heet"], [
                ["rekenkundige rij", "telkens hetzelfde getal optellen", "het verschil"],
                ["meetkundige rij", "telkens met hetzelfde getal vermenigvuldigen", "de reden"],
            ])),
            ("p", "In de rij <strong>drie, zeven, elf, vijftien</strong> is het <strong>verschil "
                  "vier</strong>. In de rij <strong>twee, zes, achttien, vierenvijftig</strong> is de "
                  "<strong>reden drie</strong>; dat is dus <strong>geen rekenkundige rij</strong>, want "
                  "het verschil groeit telkens terwijl de factor gelijk blijft. In de rij <strong>één, een "
                  "derde, een negende</strong> is de reden <strong>een derde</strong>."),
            ("p", "<strong>Een recursief voorschrift berekent elke term uit de vorige term</strong>, en "
                  "daarom heb je er altijd een beginterm bij nodig. Een <strong>expliciet "
                  "voorschrift</strong> geeft de n-de term rechtstreeks: bij <strong>vier n min één</strong> "
                  "is de <strong>eerste term drie</strong>."),
        ]),
        dict(kop="Termen en sommen berekenen", blokken=[
            ("p", "<strong>Het expliciete voorschrift van een rekenkundige rij is: de eerste term plus n "
                  "min één, maal het verschil.</strong> Om bij de n-de term te komen tel je het verschil "
                  "n min één keer op. Zo is de <strong>tiende term van drie, zeven, elf gelijk aan "
                  "negenendertig</strong>: drie plus negen maal vier, dus negen stappen en niet tien. Bij "
                  "een meetkundige rij vermenigvuldig je: de <strong>vijfde term van twee, zes, achttien "
                  "is honderdtweeënzestig</strong>, namelijk twee maal drie tot de vierde."),
            ("p", "<strong>De som van de eerste n termen van een rekenkundige rij is n maal het gemiddelde "
                  "van de eerste en de laatste term.</strong> Je legt de rij twee keer naast elkaar, een "
                  "keer vooruit en een keer achteruit, en elk paar geeft dan dezelfde som. Zo is de "
                  "<strong>som van de getallen één tot en met tien gelijk aan vijfenvijftig</strong>."),
            ("p", "Voor de <strong>som van de eerste n termen van een meetkundige rij</strong> heb je "
                  "<strong>de eerste term, de reden en het aantal termen</strong> nodig, want in de formule "
                  "staat de reden tot de macht n. Die formule werkt niet als de reden één is."),
        ]),
        dict(kop="Hoe een rij verloopt", blokken=[
            ("p", "<strong>Een rekenkundige rij daalt als het verschil negatief is.</strong> Alleen het "
                  "teken van het verschil beslist: een rij die begint bij min honderd met verschil drie "
                  "stijgt gewoon. <strong>De punten van een rekenkundige rij liggen op een rechte</strong>, "
                  "met het verschil als richtingscoëfficiënt; daarom hoort ze bij <strong>lineaire "
                  "groei</strong>. Bij een <strong>meetkundige rij hoort exponentiële groei</strong>."),
            ("p", "Een <strong>meetkundige rij met een reden groter dan één en een positieve eerste term "
                  "stijgt, met een toenemende stijging</strong>: elke stap wordt groter dan de vorige. "
                  "<strong>Bij reden één blijft elke term gelijk</strong> en is de rij constant, dus zo'n "
                  "rij stijgt zeker niet steeds sneller. <strong>Bij een negatieve reden wisselen de "
                  "termen van teken</strong>; zo'n rij heet <strong>alternerend</strong>, en je herkent "
                  "haar aan een factor min één tot de macht n in het voorschrift."),
            ("weetje", "Zet je geld op een rekening met <strong>samengestelde intrest</strong>, dan vormen "
                       "de jaarlijkse saldo's een <strong>meetkundige rij</strong>: elk jaar dezelfde "
                       "groeifactor. Bij enkelvoudige intrest zou je elk jaar hetzelfde bedrag optellen, en "
                       "dan is de rij rekenkundig."),
        ]),
        dict(kop="Convergeren en divergeren", blokken=[
            ("p", "<strong>Een rij convergeert als haar termen een vast eindig getal naderen</strong>; dat "
                  "getal is haar limiet. Gaat ze naar oneindig of blijft ze springen, dan "
                  "<strong>divergeert</strong> ze. <strong>Een divergente rij kan dus naar plus oneindig "
                  "gaan</strong>: divergent betekent alleen dat er geen eindige limiet is."),
            ("p", tabel(["Rij", "Limiet", "Waarom"], [
                ["één gedeeld door n", "nul", "hoe groter n, hoe kleiner de breuk"],
                ["twee n plus één, gedeeld door n", "twee", "splits op in twee plus één op n"],
                ["twee tot de macht n", "plus oneindig", "bij een reden groter dan één groeien de termen onbeperkt"],
                ["min één tot de macht n", "bestaat niet", "de rij blijft springen tussen min één en één"],
                ["een meetkundige rij met reden tussen min één en één", "nul", "telkens met een kleiner getal vermenigvuldigen"],
            ])),
            ("p", "<strong>Een rekenkundige rij met verschil twee convergeert niet</strong>: ze blijft met "
                  "twee per stap toenemen. Alleen een rekenkundige rij met verschil nul convergeert. Voor "
                  "<strong>twee convergente rijen is de limiet van de som de som van de limieten</strong>, "
                  "net als bij functies."),
            ("kader", "<strong>Bij een rij spreek je alleen over de limiet op oneindig, omdat een rij enkel "
                      "in de natuurlijke getallen gedefinieerd is.</strong> Er zijn geen tussenwaarden om "
                      "naartoe te kruipen: tussen de derde en de vierde term ligt niets."),
        ]),
        dict(kop="De oneindige meetkundige som", blokken=[
            ("p", "<strong>De somrij van een rij is de rij van de som van de eerste n termen.</strong> Haar "
                  "n-de term is dus de som tot en met de n-de term van de oorspronkelijke rij. <strong>De "
                  "somrij van een meetkundige rij met reden een half convergeert.</strong>"),
            ("p", "<strong>De som van een oneindige meetkundige rij bereken je als de eerste term gedeeld "
                  "door één min de reden.</strong> De reden tot de macht n kruipt immers naar nul, dus uit "
                  "de gewone somformule blijft dat over. Zo is <strong>één plus een half plus een vierde "
                  "plus een achtste, en zo verder, gelijk aan twee</strong>."),
            ("p", "<strong>Niet elke oneindige meetkundige rij heeft een eindige som.</strong> De "
                  "voorwaarde is dat <strong>de absolute waarde van de reden kleiner is dan één</strong>; "
                  "bij reden twee groeit de som onbeperkt."),
            ("p", "Een voorbeeld uit de praktijk: een <strong>bal die telkens tot zeventig procent van de "
                  "vorige hoogte stuitert</strong>. Omdat nul komma zeven onder één ligt, kan je <strong>de "
                  "totale afgelegde hoogte berekenen</strong>: oneindig veel sprongen geven samen een "
                  "eindige hoogte."),
            ("weetje", "<strong>Nul komma negen negen negen, met oneindig veel negens, is gelijk aan "
                       "één.</strong> Het is de som van een meetkundige rij met eerste term negen tienden "
                       "en reden een tiende, en die som is precies één."),
        ]),
    ],
)

# ───────────────────────── 11. Primitieven en de onbepaalde integraal
BUNDELS["primitieven-en-de-onbepaalde-integraal-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Primitieven en de onbepaalde integraal",
    onder="Afleiden in omgekeerde richting, de basisprimitieven en de vier integratiemethoden.",
    secties=[
        dict(kop="Wat een primitieve is", blokken=[
            ("p", "<strong>Een primitieve functie van f is een functie waarvan de afgeleide f is.</strong> "
                  "<strong>Primitiveren is dus de omgekeerde bewerking van afleiden</strong>, en dat is "
                  "meteen de beste controle op je werk: <strong>leid je antwoord af en je moet de "
                  "integrand terugkrijgen</strong>. Leid je een primitieve van f af, dan krijg je "
                  "<strong>f</strong>."),
            ("p", "<strong>Bij een onbepaalde integraal schrijf je altijd plus C, omdat elke constante bij "
                  "het afleiden verdwijnt.</strong> Een functie met één primitieve heeft er dus "
                  "<strong>oneindig veel</strong>. <strong>Twee primitieven van dezelfde functie hebben "
                  "altijd dezelfde afgeleide</strong>; ze verschillen alleen een constante. Daarom heet de "
                  "integraal zonder grenzen de <strong>onbepaalde</strong> integraal: <strong>de uitkomst "
                  "blijft op een constante na onbepaald</strong>."),
            ("p", "<strong>Het verschil met een bepaalde integraal: die heeft grenzen en levert een getal "
                  "op.</strong> De onbepaalde integraal is een familie van functies. <strong>Bij een "
                  "bepaalde integraal schrijf je geen plus C, want die valt bij het aftrekken van de twee "
                  "grenzen weg.</strong> De functie die je integreert heet de <strong>integrand</strong>, "
                  "en die staat tussen het integraalteken en de dx."),
            ("weetje", "<strong>Elke continue functie heeft een primitieve.</strong> Dat volgt uit de "
                       "hoofdstelling van de integraalrekening. Of je die primitieve ook in een formule kan "
                       "schrijven, is een andere vraag."),
        ]),
        dict(kop="De basisprimitieven", blokken=[
            ("p", tabel(["Functie", "Haar primitieve", "Let op"], [
                ["x tot de macht n", "x tot de macht n plus één, gedeeld door n plus één", "de exponent gaat omhoog, en je deelt door die nieuwe exponent"],
                ["één gedeeld door x", "de natuurlijke logaritme van de absolute waarde van x", "de regel hierboven werkt niet voor n gelijk aan min één"],
                ["een constante k", "k maal x", "de grafiek van de primitieve is een rechte met helling k"],
                ["de cosinus van x", "de sinus van x", "afleiden gaat de andere kant op"],
                ["de sinus van x", "min de cosinus van x", "het minteken hoort erbij"],
                ["e tot de macht x", "e tot de macht x", "die functie is haar eigen afgeleide én haar eigen primitieve"],
            ])),
            ("p", "Bij elk van die primitieven hoort nog <strong>plus een constante</strong>. De regel voor "
                  "x tot de macht n <strong>werkt niet voor n gelijk aan min één</strong>, want dan zou je "
                  "door nul delen; die ene integraal geeft net de logaritme. De <strong>absolute waarde</strong> "
                  "in die logaritme zorgt dat de formule ook werkt voor negatieve x."),
            ("p", "<strong>De lineariteit van de integraal</strong> zegt dat je <strong>termsgewijs mag "
                  "integreren en constanten buiten mag halen</strong>. <strong>Een constante factor mag dus "
                  "voor het integraalteken</strong>; een factor met een x erin niet. Voor een product of een "
                  "quotiënt werkt het evenmin, en daar bestaan net de andere methodes voor."),
            ("p", "Twee bepaalde integralen om mee te oefenen: de <strong>integraal van nul tot twee van "
                  "x</strong> is <strong>twee</strong> (de primitieve is x kwadraat gedeeld door twee, en "
                  "het is ook de oppervlakte van een driehoek met basis twee en hoogte twee), en de "
                  "<strong>integraal van nul tot één van x kwadraat</strong> is <strong>een derde</strong>."),
        ]),
        dict(kop="De vier integratiemethoden", blokken=[
            ("p", tabel(["Methode", "Wanneer", "Hoe"], [
                ["onmiddellijke integratie", "de integrand staat meteen in de tabel", "soms moet je eerst herschrijven, een wortel als een macht"],
                ["integratie door splitsing", "de integrand is een som", "elke term apart integreren, dankzij de lineariteit"],
                ["integratie door substitutie", "een binnenste functie staat er met haar afgeleide naast", "de kettingregel in omgekeerde richting"],
                ["partiële integratie", "een product van twee heel verschillende functies", "u maal v, min de integraal van v maal de afgeleide van u"],
            ])),
            ("p", "<strong>Splits je de integraal van twee x plus drie, dan valt ze uiteen in twee aparte "
                  "integralen</strong>, en de twee mag je buiten de eerste halen."),
            ("p", "<strong>Bij een substitutie kies je als nieuwe veranderlijke een binnenste functie "
                  "waarvan de afgeleide ook in de integrand staat.</strong> Zonder die afgeleide erbij kan "
                  "je de dx niet omzetten en loopt de substitutie vast. Een vast patroon: <strong>de "
                  "primitieve van de afgeleide van f, gedeeld door f, is de natuurlijke logaritme van de "
                  "absolute waarde van f</strong>; je herkent het aan de afgeleide van de noemer die in de "
                  "teller staat. <strong>Een integraal met een wortel erin kan je wel degelijk met "
                  "substitutie oplossen</strong>; dat is er zelfs een van de vaste methodes voor."),
            ("p", "<strong>Partiële integratie volgt uit de productregel voor afgeleiden</strong>: je "
                  "integreert die regel langs beide kanten en brengt één term naar de andere kant. Het "
                  "typische geval is <strong>x maal e tot de macht x</strong>. <strong>Het minteken in de "
                  "formule vergeten</strong> is de meest gemaakte fout bij deze methode."),
            ("kader", "<strong>Bij een bepaalde integraal mag je na een substitutie de oude grenzen niet "
                      "laten staan.</strong> Ze horen bij de oude veranderlijke: zet ze mee om, of ga na de "
                      "integratie eerst terug naar x."),
        ]),
        dict(kop="Handigheden", blokken=[
            ("p", "<strong>Bij een breuk waarvan de teller een hogere graad heeft dan de noemer, voer je "
                  "eerst een euclidische deling uit.</strong> Na de deling houd je een veelterm over plus "
                  "een eenvoudige rest, en die twee stukken integreer je apart."),
            ("p", "<strong>Soms heb je goniometrische formules nodig</strong>, en dan vooral <strong>de "
                  "grondformule en de formule voor de dubbele hoek</strong>. Daarmee herschrijf je "
                  "bijvoorbeeld de sinus in het kwadraat tot iets wat je wel kan integreren. Zo is de "
                  "<strong>integraal van nul tot pi van de sinus van x gelijk aan twee</strong>, en de "
                  "<strong>integraal van één tot drie van twee x gelijk aan acht</strong>."),
            ("p", "<strong>Volstaat één methode niet, dan combineer je methodes</strong>, bijvoorbeeld "
                  "eerst splitsen en dan substitueren. Bij een moeilijkere integraal heb je er vaak "
                  "meerdere na elkaar nodig."),
            ("p", "<strong>Controleer het resultaat van een onbepaalde integraal door je antwoord af te "
                  "leiden en met de integrand te vergelijken.</strong> Dat is een echte controle, want "
                  "afleiden is eenduidig; opnieuw rekenen herhaalt vaak dezelfde fout. En vergeet de "
                  "<strong>constante</strong> niet: de integraal van vijf dx is vijf x plus een constante."),
        ]),
    ],
)

# ───────────────────────── 12. De bepaalde integraal en haar toepassingen
BUNDELS["de-bepaalde-integraal-en-haar-toepassingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De bepaalde integraal en haar toepassingen",
    onder="Van Riemannsommen naar de hoofdstelling, en wat je met een integraal allemaal berekent.",
    secties=[
        dict(kop="Riemannsommen", blokken=[
            ("p", "<strong>Een Riemannsom is de som van de oppervlakten van rechthoekjes onder een "
                  "grafiek.</strong> Je verdeelt het interval in smalle stukjes en benadert elk stukje "
                  "door een rechthoekje. <strong>De dx in een integraal komt overeen met de breedte van "
                  "die rechthoekjes</strong>; de functiewaarde is de hoogte."),
            ("p", "<strong>De ondersom is het kleinst en de bovensom het grootst</strong>: de ondersom "
                  "gebruikt in elk stukje de laagste functiewaarde, de bovensom de hoogste, en de echte "
                  "oppervlakte ligt ertussen. <strong>Een ondersom is dus nooit groter dan de werkelijke "
                  "oppervlakte.</strong> <strong>Hoe meer deelintervallen je gebruikt, hoe beter de "
                  "benadering</strong>, want de rechthoekjes volgen de kromme dan nauwer."),
            ("p", "<strong>De limiet van Riemannsommen levert een exacte oppervlakte op omdat onder- en "
                  "bovensom naar hetzelfde getal kruipen.</strong> De werkelijke oppervlakte ligt er altijd "
                  "tussen, dus als de twee samenvallen is er maar één getal mogelijk. Dat getal is de "
                  "integraal."),
        ]),
        dict(kop="De georiënteerde oppervlakte", blokken=[
            ("p", "<strong>De georiënteerde oppervlakte is een oppervlakte die onder de x-as negatief "
                  "meetelt.</strong> Dat is wat de bepaalde integraal rechtstreeks berekent. Ligt een "
                  "functie op het hele interval onder de x-as, dan is <strong>haar bepaalde integraal daar "
                  "negatief</strong>. <strong>Een bepaalde integraal is dus niet altijd positief</strong>, "
                  "en ze kan zelfs nul worden als de stukken elkaar opheffen. <strong>Een werkelijke "
                  "oppervlakte kan nooit negatief zijn</strong>; alleen de georiënteerde."),
            ("p", "<strong>Snijdt de grafiek de x-as midden in het interval, dan splits je in de nulwaarde "
                  "en tel je de stukken positief op.</strong> Anders heffen een positief en een negatief "
                  "stuk elkaar op en krijg je een te kleine of zelfs een nul-uitkomst."),
            ("p", "Twee eigenschappen die je vaak gebruikt: <strong>de integraal van twee tot twee is "
                  "nul</strong>, want onder- en bovengrens vallen samen, en <strong>verwissel je de twee "
                  "grenzen, dan wisselt het resultaat van teken</strong>. <strong>De bovengrens is de "
                  "rechterkant van het interval waarover je integreert</strong>; de grenzen staan op de "
                  "x-as, niet op de y-as."),
        ]),
        dict(kop="De hoofdstelling", blokken=[
            ("p", "<strong>Het gevolg van de hoofdstelling van de integraalrekening zegt: de integraal van "
                  "a tot b is de primitieve in b min de primitieve in a.</strong> Daarmee hoef je geen "
                  "rechthoekjes meer te tellen; een primitieve zoeken volstaat. <strong>Dat invullen en "
                  "aftrekken noteer je kort met een rechte streep achter de primitieve en de grenzen "
                  "erbij</strong>, zodat je eerst de primitieve opschrijft en pas daarna invult."),
            ("p", "<strong>De hoofdstelling geldt voor continue functies</strong>, niet voor elke functie: "
                  "bij een sprong moet je het interval eerst opsplitsen."),
            ("p", "<strong>De middelwaardestelling van de integraalrekening</strong> zegt dat er "
                  "<strong>een punt is waar de functiewaarde gelijk is aan de gemiddelde waarde</strong>. "
                  "Er bestaat dus een rechthoek met dezelfde breedte en dezelfde oppervlakte als het gebied "
                  "onder de kromme."),
            ("p", tabel(["Integraal", "Uitkomst", "Hoe"], [
                ["van nul tot drie van het getal twee", "zes", "een rechthoek van drie breed en twee hoog"],
                ["van nul tot twee van drie x kwadraat", "acht", "de primitieve is x tot de derde"],
                ["van één tot twee van één gedeeld door x kwadraat", "een half", "de primitieve is min één gedeeld door x"],
                ["van nul tot één van x min x kwadraat", "een zesde", "een half min een derde"],
            ])),
        ]),
        dict(kop="Oppervlakte tussen twee krommen", blokken=[
            ("p", "<strong>De oppervlakte tussen twee krommen is de integraal van de bovenste functie min "
                  "de onderste.</strong> Het hoogteverschil is de hoogte van elk reepje. Als "
                  "<strong>grenzen neem je meestal de x-waarden van hun snijpunten</strong>; die vind je "
                  "door de twee voorschriften aan elkaar gelijk te stellen."),
            ("p", "<strong>Kruisen twee krommen elkaar midden in het interval, dan splits je in het "
                  "snijpunt</strong>, want daar wisselen boven en onder van rol. <strong>Maak eerst een "
                  "schets om te zien welke kromme boven ligt en waar ze elkaar snijden</strong>; zonder "
                  "schets zet je de twee functies gemakkelijk in de verkeerde volgorde."),
            ("p", "Twee voorbeelden: de <strong>oppervlakte tussen y is x en y is x kwadraat, tussen hun "
                  "twee snijpunten, is een zesde</strong> (de snijpunten liggen in nul en één, en daar ligt "
                  "de rechte boven de parabool), en de <strong>oppervlakte onder de rechte y is twee tussen "
                  "nul en vijf is tien</strong>. Lopen twee grafieken evenwijdig met de ene overal drie "
                  "hoger, dan is de oppervlakte over een interval van lengte vier gelijk aan "
                  "<strong>twaalf</strong>."),
        ]),
        dict(kop="Omwentelingslichaam en booglengte", blokken=[
            ("p", "<strong>Bij een omwentelingslichaam om de x-as neem je pi maal de integraal van f tot "
                  "de tweede macht.</strong> <strong>Je kwadrateert de functie dus onder het "
                  "integraalteken</strong>: elke dunne schijf is een cirkel met straal f van x, en in de "
                  "oppervlakte van een cirkel staat de straal in het kwadraat. <strong>De inhoud hangt af "
                  "van de as waarrond je de kromme laat draaien</strong>: rond de x-as of rond de y-as "
                  "geeft een heel ander lichaam."),
            ("p", "<strong>In de formule voor de booglengte staat onder de wortel: één plus de afgeleide in "
                  "het kwadraat.</strong> Ze volgt uit Pythagoras op een heel klein stukje kromme, met een "
                  "horizontale dx en een verticale dy."),
        ]),
        dict(kop="Integralen met een betekenis", blokken=[
            ("p", tabel(["Wat je integreert", "Wat je krijgt", "Let op"], [
                ["de snelheid over de tijd", "de verplaatsing", "niet de afgelegde weg, want achteruit telt negatief"],
                ["de versnelling over de tijd", "de verandering van de snelheid", "één stap terug in dezelfde ketting"],
                ["het debiet van een kraan over de tijd", "de totale hoeveelheid water", "liter per seconde maal seconden geeft liter"],
                ["de marginale kost over een aantal stuks", "de toename van de totale kost", "de marginale kost is de afgeleide van de totale"],
            ])),
            ("p", "<strong>De eenheden rekenen mee</strong>: integreer je een snelheid in meter per seconde "
                  "over seconden, dan is het resultaat in <strong>meter</strong>. Die controle vangt veel "
                  "fouten."),
            ("kader", "<strong>ICT gebruik je bij een integraal als de opgave dat met het icoon aangeeft, "
                      "en ook dan toon je je werkwijze.</strong> Functioneel gebruik betekent dat ICT het "
                      "rekenwerk ondersteunt, terwijl je redenering en je tussenstappen op papier staan."),
        ]),
    ],
)

# ───────────────────────── 13. Complexe getallen
BUNDELS["complexe-getallen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Complexe getallen",
    onder="De imaginaire eenheid, het vlak van Gauss, de goniometrische vorm en de formule van de Moivre.",
    secties=[
        dict(kop="De imaginaire eenheid", blokken=[
            ("p", "<strong>De imaginaire eenheid i is het getal waarvan het kwadraat min één is.</strong> "
                  "<strong>De complexe getallen werden ingevoerd omdat niet elke vergelijking een oplossing "
                  "had in de reële getallen</strong>: een getal met kwadraat min één bestond niet, en door "
                  "het toe te voegen kreeg elke veeltermvergelijking oplossingen."),
            ("p", "De machten van i <strong>herhalen zich om de vier</strong>: i, dan min één, dan "
                  "<strong>min i</strong>, dan <strong>één</strong>. <strong>i tot de derde is dus niet i "
                  "maar min i</strong>, en <strong>i tot de vierde is één</strong>. Pas i tot de vijfde is "
                  "weer i."),
            ("p", "Een complex getal schrijf je in <strong>cartesische vorm</strong> als een reëel deel "
                  "plus een imaginair deel maal i. Bij <strong>drie min vijf i</strong> is het "
                  "<strong>reëel deel drie</strong>; bij <strong>zeven min twee i</strong> is het "
                  "<strong>imaginair deel min twee</strong>, dus zonder de i erbij. <strong>Elk reëel getal "
                  "is ook een complex getal</strong>, met imaginair deel nul. <strong>Een zuiver imaginair "
                  "getal heeft reëel deel nul.</strong>"),
            ("kader", "<strong>Je kan twee complexe getallen niet van klein naar groot ordenen.</strong> "
                      "Hun moduli kan je wel vergelijken, maar de getallen zelf niet."),
        ]),
        dict(kop="Rekenen in cartesische vorm", blokken=[
            ("p", "<strong>Optellen doe je deel per deel</strong>: twee plus drie i, plus één min i, geeft "
                  "<strong>drie plus twee i</strong>, net als bij vectoren. Bij vermenigvuldigen werk je "
                  "uit en gebruik je dat i in het kwadraat min één is: <strong>één plus i, in het kwadraat, "
                  "is twee i</strong>."),
            ("p", "Het <strong>toegevoegde complexe getal</strong> krijg je door enkel het imaginair deel "
                  "van teken te laten wisselen: dat van <strong>twee plus drie i is twee min drie i</strong>. "
                  "<strong>Een complex getal maal zijn toegevoegde is altijd een reëel getal</strong>, "
                  "namelijk het kwadraat van de modulus. Daarom <strong>deel je door een complex getal door "
                  "teller en noemer met de toegevoegde van de noemer te vermenigvuldigen</strong>: de noemer "
                  "wordt dan reëel. Apart delen werkt niet, net zoals bij een breuk met een wortel."),
        ]),
        dict(kop="Het vlak van Gauss", blokken=[
            ("p", "Elk complex getal is een <strong>punt in het vlak van Gauss</strong>: horizontaal het "
                  "reëel deel, en <strong>op de verticale as het imaginair deel</strong>. De reële getallen "
                  "liggen dus op de horizontale as, de zuiver imaginaire op de verticale."),
            ("p", "De <strong>modulus</strong> is de afstand tot de oorsprong. Die van <strong>drie plus "
                  "vier i is vijf</strong> (de wortel uit negen plus zestien), die van <strong>vijf i is "
                  "vijf</strong>, en die van <strong>min drie is drie</strong>: een modulus is nooit "
                  "negatief, en voor een reëel getal is ze de absolute waarde. Het "
                  "<strong>argument</strong> is <strong>de hoek met de positieve reële as</strong>. Samen "
                  "leggen modulus en argument het getal volledig vast. Het argument van <strong>i is "
                  "negentig graden</strong>, dat van een <strong>negatief reëel getal honderdtachtig "
                  "graden</strong>."),
            ("p", "Daarmee krijgen de bewerkingen een meetkundige betekenis. <strong>Optellen is dezelfde "
                  "constructie als het optellen van twee vectoren</strong>: je legt de pijlen achter "
                  "elkaar. <strong>Het toegevoegde nemen spiegelt het punt om de horizontale as.</strong> "
                  "En <strong>vermenigvuldigen met i draait het punt een kwart slag rond de "
                  "oorsprong</strong>, want de modulus van i is één en haar argument negentig graden."),
        ]),
        dict(kop="De goniometrische vorm", blokken=[
            ("p", "<strong>De goniometrische vorm is de modulus maal de cosinus van het argument plus i "
                  "maal de sinus ervan.</strong> Zo zie je de twee gegevens meteen staan: hoe ver en onder "
                  "welke hoek. <strong>Van cartesisch naar goniometrisch bereken je de modulus en het "
                  "argument uit het reëel en imaginair deel</strong>: de modulus is de wortel uit de som "
                  "van de kwadraten, en het argument vind je met de tangens, met het juiste kwadrant erbij."),
            ("p", tabel(["Bewerking", "Met de moduli", "Met de argumenten"], [
                ["vermenigvuldigen", "vermenigvuldigen", "optellen"],
                ["delen", "delen", "aftrekken"],
                ["tot de macht n verheffen", "tot de macht n verheffen", "met n vermenigvuldigen"],
            ])),
            ("p", "Vermenigvuldigen is dus <strong>uitrekken en draaien tegelijk</strong>, delen is krimpen "
                  "en terugdraaien. <strong>De modulus van een product is het product van de moduli, niet "
                  "hun som</strong>; het zijn de argumenten die worden opgeteld. De regel voor machten "
                  "heet de <strong>formule van de Moivre</strong>: <strong>je verheft de modulus tot de "
                  "macht n en vermenigvuldigt het argument met n</strong>. Ze volgt rechtstreeks uit de "
                  "regel voor vermenigvuldigen, n keer toegepast. <strong>Daarom is de goniometrische vorm "
                  "zo handig bij machtsverheffen</strong>: probeer één plus i tot de tiende maar eens in "
                  "cartesische vorm."),
        ]),
        dict(kop="Vergelijkingen in de complexe getallen", blokken=[
            ("p", "<strong>Een tweedegraadsvergelijking met een negatieve discriminant heeft wel degelijk "
                  "oplossingen in de complexe getallen</strong>, namelijk twee. In de reële getallen zijn "
                  "er inderdaad geen. Zo heeft <strong>x kwadraat plus één is nul</strong> als oplossingen "
                  "<strong>i</strong> en min i, en <strong>x kwadraat min twee x plus vijf is nul</strong> "
                  "de oplossingen <strong>één plus twee i en één min twee i</strong>: de discriminant is "
                  "min zestien, de wortel daaruit is vier i."),
            ("p", "<strong>De twee complexe oplossingen van een tweedegraadsvergelijking met reële "
                  "coëfficiënten zijn elkaars toegevoegde</strong>: ze verschillen alleen in het teken voor "
                  "de wortel uit de discriminant."),
            ("p", "<strong>De vergelijking z tot de derde is acht heeft drie oplossingen</strong> in de "
                  "complexe getallen; algemeen heeft <strong>z tot de macht n is a er precies n</strong>, "
                  "en <strong>een complex getal dat niet nul is heeft precies n n-de machtswortels</strong>. "
                  "<strong>Die n oplossingen liggen op één cirkel, gelijkmatig over de omtrek "
                  "verdeeld</strong>: ze hebben dezelfde modulus en hun argumenten verschillen telkens "
                  "evenveel, dus ze vormen de hoekpunten van een regelmatige veelhoek."),
            ("weetje", "<strong>Een veelterm van graad n heeft in de complexe getallen precies n "
                       "nulwaarden</strong>, als je ze met hun multipliciteit telt. Dat is de hoofdstelling "
                       "van de algebra. In de reële getallen kunnen het er minder zijn."),
        ]),
    ],
)

# ───────────────────────── 14. Telproblemen en het binomium
BUNDELS["telproblemen-en-het-binomium-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Telproblemen en het binomium",
    onder="Faculteit, permutaties, variaties en combinaties, de driehoek van Pascal en het binomium van Newton.",
    secties=[
        dict(kop="Faculteit en permutaties", blokken=[
            ("p", "<strong>n faculteit is het product van alle natuurlijke getallen van één tot en met "
                  "n.</strong> <strong>Vijf faculteit is dus honderdtwintig</strong>. <strong>Nul "
                  "faculteit is één</strong>: dat is een afspraak die alle formules kloppend houdt, want "
                  "er is precies één manier om niets te rangschikken."),
            ("p", "Een <strong>permutatie</strong> is een rangschikking van álle elementen. <strong>Vijf "
                  "verschillende boeken naast elkaar zetten kan op honderdtwintig manieren</strong>, dus "
                  "op vijf faculteit manieren."),
            ("p", "Een <strong>herhalingspermutatie is een rangschikking van alle elementen waarvan er "
                  "enkele gelijk zijn</strong>. Je deelt dan door de faculteiten van de groepjes gelijke "
                  "elementen: met de letters van <strong>MAMA</strong> maak je <strong>zes</strong> "
                  "verschillende woorden, want vier faculteit gedeeld door twee faculteit maal twee "
                  "faculteit."),
        ]),
        dict(kop="Variaties en combinaties", blokken=[
            ("p", tabel(["Soort", "Telt de volgorde mee?", "Voorbeeld"], [
                ["variatie", "ja", "goud, zilver en brons op een podium"],
                ["combinatie", "nee", "drie leden van een jury kiezen uit twaalf"],
                ["herhalingsvariatie", "ja, en herhaling is toegelaten", "een code van vier cijfers"],
            ])),
            ("p", "<strong>Bij een variatie telt de volgorde mee en bij een combinatie niet.</strong> "
                  "Daarom zijn er <strong>altijd minder combinaties dan variaties</strong> bij dezelfde n "
                  "en p: bij een combinatie vallen alle volgordes van dezelfde keuze samen. <strong>Bij "
                  "een herhalingsvariatie mag een element wel meer dan één keer voorkomen</strong>; bij "
                  "een gewone variatie niet. Zo bestaan er <strong>tienduizend codes van vier "
                  "cijfers</strong> als elk cijfer van nul tot negen mag en herhaling toegelaten is."),
            ("p", "Drie uitkomsten om bij de hand te hebben. <strong>Twee personen kiezen uit vijf zonder "
                  "volgorde kan op tien manieren</strong>. <strong>Zes mensen die elkaar allemaal één keer "
                  "een hand geven, geven vijftien handdrukken</strong>. En <strong>één persoon kiezen uit "
                  "tien kan op tien manieren</strong>. <strong>Een jury van drie uit twaalf kandidaten is "
                  "een combinatie</strong>, want de volgorde van de drie telt niet mee; zou je een "
                  "voorzitter, een secretaris en een penningmeester kiezen, dan was het een variatie."),
            ("p", "<strong>Het aantal manieren om p uit n te kiezen is even groot als het aantal manieren "
                  "om n min p uit n te kiezen</strong>: wie je kiest, bepaalt meteen wie je niet kiest."),
        ]),
        dict(kop="De drie telregels", blokken=[
            ("p", "<strong>De somregel gebruik je als je moet kiezen tussen twee mogelijkheden die elkaar "
                  "uitsluiten.</strong> <strong>De productregel gebruik je bij keuzes die na elkaar "
                  "komen</strong>: eerst een hoofdgerecht en daarna een dessert. <strong>Of-of betekent "
                  "optellen, en-en betekent vermenigvuldigen</strong>, en dat onderscheid is de kern van "
                  "elk telprobleem."),
            ("p", "<strong>De complementregel zegt: tel het aantal gevallen dat niet voldoet en trek dat "
                  "van het totaal af.</strong> Bij een opgave met de woorden minstens of hoogstens is dat "
                  "vaak veel korter werk."),
            ("weetje", "<strong>Het sommatieteken dient om een lange som kort te schrijven met een lopende "
                       "index.</strong> Onder het teken staat waar de index begint, erboven waar hij "
                       "eindigt."),
        ]),
        dict(kop="De driehoek van Pascal", blokken=[
            ("p", "<strong>In de driehoek van Pascal staan de binomiaalcoëfficiënten, rij per rij.</strong> "
                  "<strong>Je berekent een getal als de som van de twee getallen schuin erboven</strong>, "
                  "en dat is net wat <strong>de formule van Stifel-Pascal</strong> in symbolen zegt: "
                  "<strong>één binomiaalcoëfficiënt als de som van twee andere uit de vorige rij</strong>. "
                  "Daarmee bouw je de hele driehoek op zonder één faculteit te berekenen."),
            ("p", "<strong>Aan het begin en op het einde van elke rij staat een één</strong>: er is maar "
                  "één manier om niets te kiezen en maar één manier om alles te kiezen. <strong>Nul "
                  "elementen kiezen uit n kan dus op één manier.</strong> <strong>Elke rij is "
                  "symmetrisch, omdat p elementen kiezen hetzelfde is als n min p elementen "
                  "weglaten.</strong> <strong>De som van alle getallen in een rij is een macht van "
                  "twee</strong>: rij n telt op tot twee tot de macht n, en dat is ook het aantal "
                  "deelverzamelingen van een verzameling met n elementen. Zo is de <strong>som van de rij "
                  "één, drie, drie, één gelijk aan acht</strong>."),
            ("p", "Twee aantallen die je rechtstreeks uit de driehoek haalt: <strong>twee elementen kiezen "
                  "uit vier kan op zes manieren</strong>, het middelste getal van de rij één, vier, zes, "
                  "vier, één."),
            ("kader", "<strong>De driehoek van Pascal heeft wel degelijk met kansrekening te maken.</strong> "
                      "De binomiale verdeling gebruikt net die coëfficiënten: ze tellen op hoeveel manieren "
                      "k successen in n pogingen kunnen vallen."),
        ]),
        dict(kop="Het binomium van Newton", blokken=[
            ("p", "<strong>Het binomium van Newton geeft de uitwerking van een tweeterm tot een "
                  "willekeurige macht.</strong> Elke term bestaat uit een binomiaalcoëfficiënt maal een "
                  "macht van a maal een macht van b. <strong>Het heet zo omdat het over een macht van een "
                  "tweeterm gaat</strong>, en een binomium is een som van twee termen."),
            ("p", "<strong>a plus b, tot de derde macht, is a tot de derde, plus drie a kwadraat b, plus "
                  "drie a b kwadraat, plus b tot de derde.</strong> De coëfficiënten één, drie, drie, één "
                  "zijn de vierde rij van de driehoek. <strong>De coëfficiënt bij a kwadraat b is dus "
                  "drie</strong>: je kiest uit de drie factoren er één waaruit je b neemt. <strong>a plus "
                  "b, tot de vijfde macht, heeft zes termen</strong>, altijd één meer dan de exponent. En "
                  "in <strong>één plus x, tot de vierde macht, heeft x kwadraat coëfficiënt zes</strong>."),
            ("p", "<strong>Bij a min b tot de macht n wisselen de tekens van term tot term</strong>, want "
                  "je past dezelfde formule toe met min b in plaats van b. En de bekendste valstrik: "
                  "<strong>a plus b in het kwadraat is niet a kwadraat plus b kwadraat</strong>, want de "
                  "middelste term twee ab ontbreekt; de tweede rij van Pascal is één, twee, één."),
            ("p", "<strong>Eén bepaalde term vind je zonder alles uit te werken met de algemene term uit "
                  "het binomium van Newton</strong>: je vult de juiste index in en krijgt meteen de "
                  "coëfficiënt en de twee machten."),
            ("kader", "<strong>Een identiteit met binomiaalcoëfficiënten bewijs je door beide leden met "
                      "faculteiten uit te schrijven en te vereenvoudigen.</strong> Een paar getallen "
                      "invullen toont alleen dat het dáár klopt. Een telkundige redenering mag ook, als ze "
                      "voor alle n geldt."),
        ]),
    ],
)

# ───────────────────────── 15. Kansrekenen en kansverdelingen
BUNDELS["kansrekenen-en-kansverdelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansrekenen en kansverdelingen",
    onder="Laplace, kansbomen en kruistabellen, voorwaardelijke kans, en de binomiale verdeling.",
    secties=[
        dict(kop="Wat een kans is", blokken=[
            ("p", "<strong>De wet van Laplace zegt: de kans is het aantal gunstige gedeeld door het aantal "
                  "mogelijke uitkomsten.</strong> Ze geldt alleen als alle uitkomsten even waarschijnlijk "
                  "zijn, dus bij een eerlijke dobbelsteen of munt."),
            ("p", tabel(["Vraag", "Kans", "Hoe"], [
                ["een even getal met een dobbelsteen", "een half", "drie gunstige van de zes"],
                ["een zes met een dobbelsteen", "een zesde", "één gunstige van de zes"],
                ["een getal kleiner dan drie", "een derde", "één en twee, dus twee van de zes"],
                ["harten uit een spel van tweeënvijftig kaarten", "een vierde", "dertien harten op tweeënvijftig"],
            ])),
            ("p", "<strong>Een kans kan nooit groter zijn dan één</strong>: ze ligt altijd tussen nul en "
                  "één. Krijg je meer dan één, dan zit er een fout in je redenering. <strong>De som van de "
                  "kansen op alle mogelijke uitkomsten samen is één</strong>, want er gebeurt altijd iets. "
                  "<strong>Een kans gelijk aan nul betekent dat de gebeurtenis bij dit experiment niet kan "
                  "voorkomen</strong>, zoals een zeven gooien met een gewone dobbelsteen."),
            ("p", "De <strong>uitkomstenverzameling is de verzameling van alle mogelijke uitkomsten</strong>: "
                  "bij één worp met een dobbelsteen de getallen één tot en met zes. Het verschil met een "
                  "gebeurtenis: <strong>een gebeurtenis kan uit meerdere uitkomsten bestaan</strong>, zoals "
                  "een even getal gooien."),
            ("weetje", "<strong>Bij heel veel herhalingen komt de relatieve frequentie dicht bij de kans te "
                       "liggen.</strong> Dat is net wat een kans in de praktijk betekent. Bij tien worpen "
                       "kan het nog ver uit elkaar liggen."),
        ]),
        dict(kop="Kansbomen, kruistabellen en voorwaardelijke kans", blokken=[
            ("p", "<strong>In een kansboom vermenigvuldig je de kansen op de takken van één pad.</strong> "
                  "<strong>Verschillende paden die allemaal voldoen, tel je daarna op.</strong> Na elkaar "
                  "betekent dus vermenigvuldigen, of-of betekent optellen, op voorwaarde dat de gevallen "
                  "elkaar uitsluiten. Zo is de <strong>kans op twee keer kop bij twee worpen met een munt "
                  "een vierde</strong>: een half maal een half."),
            ("p", "<strong>In een kruistabel zet je de aantallen voor elke combinatie van twee "
                  "kenmerken.</strong> De randtotalen geven je de gewone kansen, de cellen de kansen op "
                  "beide kenmerken samen."),
            ("p", "<strong>Een voorwaardelijke kans is de kans op A als je al weet dat B gebeurd is.</strong> "
                  "Je kijkt dan alleen nog naar de gevallen waarin B optreedt, dus naar één rij of één "
                  "kolom van de kruistabel."),
            ("p", "<strong>Twee gebeurtenissen zijn onafhankelijk als de ene de kans op de andere niet "
                  "verandert</strong>; dan is de kans op allebei samen gewoon het product. <strong>Twee "
                  "keer een kaart trekken zonder terugleggen is niet onafhankelijk</strong>, want de eerste "
                  "kaart verandert wat er nog in het spel zit. Mét terugleggen wel."),
            ("p", "<strong>De complementregel voor kansen zegt: de kans dat iets niet gebeurt is één min "
                  "de kans dat het wel gebeurt.</strong> Is de kans op een gebeurtenis nul komma drie, dan "
                  "is de kans dat ze niet gebeurt <strong>nul komma zeven</strong>. Daarom bereken je "
                  "<strong>de kans op minstens één succes als één min de kans op nul successen</strong>."),
        ]),
        dict(kop="Kansvariabelen", blokken=[
            ("p", "<strong>Een kansvariabele is een grootheid die aan elke uitkomst een getal "
                  "toekent.</strong> Bij tien worpen met een munt kan dat het aantal keer kop zijn."),
            ("p", "<strong>Een discrete kansvariabele neemt losse waarden aan, een continue elke waarde in "
                  "een interval.</strong> Het aantal defecte stukken is discreet; <strong>de tijd die een "
                  "trein te laat is, is continu</strong>, want tijd kan elke waarde in een interval "
                  "aannemen. <strong>De som van alle kansen in een kansverdeling is één.</strong>"),
            ("p", "<strong>De verwachtingswaarde is het gemiddelde dat je op lange termijn zou "
                  "meten.</strong> Bij één enkel experiment zegt ze niets met zekerheid. <strong>Ze hoeft "
                  "zelf geen mogelijke uitkomst te zijn</strong>: het gemiddelde aantal kinderen per gezin "
                  "is één komma zeven, en zoveel kinderen heeft geen enkel gezin."),
        ]),
        dict(kop="De binomiale verdeling", blokken=[
            ("p", "<strong>Een Bernoulli-experiment heeft precies twee mogelijke uitkomsten</strong>, "
                  "succes of mislukking, en bestaat uit <strong>één</strong> poging. Herhaal je het, dan "
                  "krijg je een binomiale verdeling."),
            ("p", "<strong>Een kansvariabele is binomiaal verdeeld bij een vast aantal onafhankelijke "
                  "pogingen met telkens dezelfde slaagkans.</strong> Drie voorwaarden dus; valt er één weg, "
                  "dan is de verdeling niet binomiaal. <strong>De slaagkans mag dus niet van poging tot "
                  "poging verschillen</strong>, en daarom voldoet een trekking zonder terugleggen uit een "
                  "kleine groep vaak niet. <strong>Het aantal zessen in vijftig worpen met een dobbelsteen "
                  "is wel binomiaal verdeeld.</strong>"),
            ("p", "<strong>In de formule voor de kans op precies k successen uit n pogingen staat een "
                  "binomiaalcoëfficiënt maal p tot de k maal één min p tot de n min k.</strong> Die "
                  "coëfficiënt telt op hoeveel verschillende volgordes die k successen kunnen hebben."),
            ("p", tabel(["Grootheid", "Formule", "Voorbeeld"], [
                ["verwachtingswaarde", "het aantal pogingen maal de kans per poging", "tien worpen met een munt: vijf keer kop"],
                ["verwachtingswaarde", "zelfde formule", "twintig stukken met kans nul komma één: twee foute stukken"],
                ["standaardafwijking", "de wortel uit n maal p maal één min p", "onder de wortel staat de variantie"],
            ])),
            ("p", "<strong>Een grotere standaardafwijking betekent dat de uitkomsten verder uit elkaar "
                  "liggen</strong>; ze meet hoe sterk de waarden rond de verwachtingswaarde schommelen. "
                  "Hebben <strong>twee binomiale verdelingen dezelfde verwachtingswaarde maar een "
                  "verschillende standaardafwijking</strong>, dan <strong>liggen de uitkomsten bij de ene "
                  "meer verspreid dan bij de andere</strong>: gemiddeld hetzelfde resultaat, maar bij de "
                  "ene schommelt het sterker."),
            ("kader", "<strong>Aan de rekenapp laat je de kansen, de verwachtingswaarde en de "
                      "standaardafwijking berekenen.</strong> Beoordelen of het model past en wat het "
                      "antwoord betekent, blijft jouw werk."),
        ]),
    ],
)

# ───────────────────────── 16. Statistiek: normale verdeling en hypothesetoets
BUNDELS["statistiek-normale-verdeling-en-hypothesetoets-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Statistiek: normale verdeling en hypothesetoets",
    onder="De Gausskromme en de z-score, steekproeven en vertekening, samenhang en causaliteit, en toetsen met een p-waarde.",
    secties=[
        dict(kop="De normale verdeling", blokken=[
            ("p", "<strong>De grafiek van een normale verdeling is klokvormig en symmetrisch rond het "
                  "gemiddelde</strong>; die kromme heet de <strong>Gausskromme</strong>. <strong>Het "
                  "gemiddelde bepaalt waar de top ligt</strong> en <strong>de standaardafwijking bepaalt "
                  "hoe breed de kromme is</strong>: klein geeft een smalle, hoge klok, groot een brede, "
                  "platte. Hebben <strong>twee Gausskrommen hetzelfde gemiddelde en is de ene "
                  "smaller</strong>, dan <strong>liggen bij die smalle de metingen dichter bij het "
                  "gemiddelde</strong>."),
            ("p", "<strong>De totale oppervlakte onder een Gausskromme is één</strong>, want alle kans "
                  "samen is één. <strong>Een kans komt dus overeen met de oppervlakte onder de "
                  "kromme</strong>; de hoogte alleen zegt niets. Daaruit volgt ook dat <strong>bij een "
                  "continue verdeling de kans op precies één welbepaalde waarde nul is</strong>: een "
                  "enkele waarde heeft geen breedte. En <strong>vijftig procent van de metingen ligt links "
                  "van het gemiddelde</strong>."),
            ("p", "<strong>De Gausskromme raakt de horizontale as niet.</strong> Ze nadert die wel, maar "
                  "bereikt haar nooit, dus elke waarde blijft in principe mogelijk. <strong>Of de normale "
                  "verdeling een geschikt model is, beoordeel je door te kijken of het histogram ongeveer "
                  "klokvormig is</strong>; je kan er ook de dichtheidsfunctie met de geschatte parameters "
                  "over tekenen. Is een histogram duidelijk scheef, dan past het model niet."),
        ]),
        dict(kop="De z-score", blokken=[
            ("p", "<strong>De z-score bereken je als het verschil met het gemiddelde, gedeeld door de "
                  "standaardafwijking.</strong> Ze meet dus <strong>hoeveel standaardafwijkingen je van "
                  "het gemiddelde af zit</strong>, en daardoor kan je metingen uit verschillende groepen "
                  "vergelijken. <strong>Een meting die precies gelijk is aan het gemiddelde heeft z-score "
                  "nul</strong>, en bij een <strong>gemiddelde van zeventig met standaardafwijking vijf "
                  "heeft een meting van tachtig z-score twee</strong>."),
            ("p", "<strong>Een z-score kan negatief zijn</strong>: dan ligt de meting onder het "
                  "gemiddelde. <strong>Een z-score van min anderhalf betekent dat de meting anderhalve "
                  "standaardafwijking onder het gemiddelde ligt</strong>; de z-score telt in "
                  "standaardafwijkingen, niet in de eenheid van de meting zelf."),
            ("p", "<strong>De standaardnormale verdeling heeft gemiddelde nul en standaardafwijking "
                  "één.</strong> Ze is de normale verdeling na omzetting naar z-scores, zodat één eenheid "
                  "op de as precies één standaardafwijking is."),
            ("p", tabel(["Binnen hoeveel standaardafwijkingen", "Ongeveer welk deel van de metingen"], [
                ["één", "achtenzestig procent"],
                ["twee", "vijfennegentig procent"],
                ["drie", "negenennegentig komma zeven procent"],
            ])),
            ("kader", "Let op de eerste rij: <strong>binnen één standaardafwijking ligt ongeveer "
                      "achtenzestig procent, niet vijfennegentig.</strong> Vijfennegentig procent hoort bij "
                      "twee standaardafwijkingen."),
        ]),
        dict(kop="Steekproeven", blokken=[
            ("p", "<strong>Het gemiddelde van een populatie is de echte waarde, dat van een steekproef een "
                  "schatting ervan.</strong> Daarom krijgen ze een ander symbool: je kent het "
                  "populatiegemiddelde meestal niet."),
            ("p", "<strong>Een steekproef is representatief als ze op de belangrijke kenmerken op de "
                  "populatie lijkt.</strong> Grootte alleen helpt niet: een heel grote maar scheve "
                  "steekproef blijft scheef. <strong>Randomisatie betekent iedereen uit de populatie "
                  "evenveel kans geven om gekozen te worden</strong>, en dat is de beste bescherming tegen "
                  "vertekening."),
            ("p", "<strong>Een steekproeffout komt door het toeval van de trekking, een niet-steekproeffout "
                  "door de opzet.</strong> Toeval kan je inschatten en kleiner maken: <strong>een grotere "
                  "aselecte steekproef geeft doorgaans een betrouwbaarder resultaat</strong>. Een fout in "
                  "de opzet blijft ook bij duizend deelnemers bestaan."),
            ("p", "Laat een krant haar lezers online stemmen over een stelling, dan heb je "
                  "<strong>vrijwillige respons</strong>: wie zich sterk betrokken voelt, stemt vaker. De "
                  "groep die antwoordt is dan niet toevallig samengesteld, en meer stemmen lost dat niet op."),
        ]),
        dict(kop="Samenhang is geen oorzaak", blokken=[
            ("p", "<strong>In een spreidingsdiagram lees je af of er een verband is tussen twee numerieke "
                  "grootheden.</strong> Elk punt is één waarneming met twee kenmerken. Een "
                  "<strong>trendlijn is een rechte of kromme die het patroon in de puntenwolk "
                  "samenvat</strong>; ze gaat meestal niet door de punten zelf."),
            ("p", "<strong>De correlatiecoëfficiënt ligt tussen min één en plus één.</strong> Het teken "
                  "geeft de richting, de grootte de sterkte van het lineaire verband. <strong>Dicht bij "
                  "nul betekent dus net dat er nauwelijks lineair verband is</strong>; sterk is ze dicht "
                  "bij min één of plus één."),
            ("kader", "<strong>Sterke samenhang betekent niet dat de ene de oorzaak van de andere is.</strong> "
                      "Het kan ook komen van een <strong>derde verborgen variabele</strong>, van omgekeerde "
                      "oorzaak en gevolg, of gewoon van toeval. In de zomer worden er meer ijsjes verkocht "
                      "en gebeuren er meer verdrinkingen: de verborgen variabele is <strong>het warme "
                      "weer</strong>, dat allebei de aantallen verhoogt."),
        ]),
        dict(kop="De hypothesetoets", blokken=[
            ("p", "<strong>De nulhypothese is niet wat je wil aantonen, maar wat je probeert te "
                  "verwerpen.</strong> Wat je wil aantonen, staat in de alternatieve hypothese."),
            ("p", "<strong>De p-waarde is de kans op zo'n resultaat of extremer, als de nulhypothese waar "
                  "is.</strong> Ze zegt niets over de kans dat de hypothese klopt, alleen hoe verrassend je "
                  "resultaat zou zijn mocht ze kloppen. Je vergelijkt ze met het "
                  "<strong>significantieniveau</strong> alfa, <strong>de kans die je vooraf aanvaardt om "
                  "de nulhypothese onterecht te verwerpen</strong>. Alfa gelijk aan nul komma nul vijf is "
                  "<strong>vijf procent</strong>; soms kiest men één procent als een vals alarm duur "
                  "uitvalt. <strong>Ligt de p-waarde onder alfa, dan verwerp je</strong>: bij een p-waarde "
                  "van nul komma nul twee en alfa nul komma nul vijf is het antwoord <strong>ja</strong>."),
            ("p", tabel(["Soort fout", "Wat er gebeurt", "Hoe je het noemt"], [
                ["type I", "de nulhypothese verwerpen terwijl ze waar is", "een vals alarm; de kans erop is alfa"],
                ["type II", "de nulhypothese onterecht niet verwerpen", "er was wel een effect, maar je vond het niet"],
            ])),
            ("p", "Een type II-fout gebeurt vaker bij een kleine steekproef. <strong>Een eenzijdige toets "
                  "gebruik je als je vooraf een richting verwacht</strong>, bijvoorbeeld een stijging; "
                  "vermoed je alleen dat er íéts verandert, dan toets je tweezijdig."),
            ("kader", "<strong>Verwerp je de nulhypothese niet, dan besluit je dat er onvoldoende bewijs "
                      "tegen gevonden is.</strong> Geen bewijs vinden is niet hetzelfde als bewijzen dat er "
                      "niets is: misschien was je steekproef gewoon te klein."),
        ]),
    ],
)

# ───────────────────────── 17. Matrices en hun bewerkingen
BUNDELS["matrices-en-hun-bewerkingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Matrices en hun bewerkingen",
    onder="Dimensie, optellen en vermenigvuldigen, bijzondere matrices, en de determinant, de inverse en de rang.",
    secties=[
        dict(kop="Dimensie en bewerkingen", blokken=[
            ("p", "<strong>Een matrix van dimensie drie bij vier heeft drie rijen en vier kolommen.</strong> "
                  "Eerst de rijen, dan de kolommen: die volgorde omdraaien is de meest gemaakte fout van "
                  "het hoofdstuk. Een matrix van <strong>twee bij vijf heeft tien elementen</strong>, en "
                  "een <strong>kolommatrix met vier elementen heeft vier rijen</strong>."),
            ("p", "<strong>Twee matrices kan je optellen als ze precies dezelfde dimensie hebben</strong>, "
                  "want je telt element per element op. <strong>Bij een vermenigvuldiging met een reëel "
                  "getal vermenigvuldig je elk element met dat getal</strong>; dat heet de scalaire "
                  "vermenigvuldiging en is iets heel anders dan het product van twee matrices."),
            ("p", "<strong>Het product A maal B kan je berekenen als het aantal kolommen van A gelijk is "
                  "aan het aantal rijen van B.</strong> Elk element van het product is een rij van A tegen "
                  "een kolom van B, en die twee moeten even lang zijn. Zo heeft het <strong>product van "
                  "een matrix twee bij drie met een matrix drie bij vier de dimensie twee bij vier</strong>: "
                  "de binnenste getallen vallen weg, de buitenste blijven over."),
            ("kader", "<strong>Het vermenigvuldigen van matrices is niet commutatief.</strong> A maal B is "
                      "in het algemeen iets anders dan B maal A, en soms bestaat maar één van de twee. Dat "
                      "is het grote verschil met gewone getallen."),
        ]),
        dict(kop="Bijzondere matrices", blokken=[
            ("p", tabel(["Soort matrix", "Wat ze is", "Weetje"], [
                ["vierkante matrix", "evenveel rijen als kolommen", "alleen zij kan een determinant of een inverse hebben"],
                ["nulmatrix", "elk element is nul", "niet te verwarren met een matrix met determinant nul"],
                ["eenheidsmatrix", "enen op de hoofddiagonaal, elders nullen", "van orde drie staan er dus drie enen"],
                ["diagonaalmatrix", "vierkant, en alles buiten de hoofddiagonaal is nul", "de eenheidsmatrix is er een bijzonder geval van"],
                ["symmetrische matrix", "gelijk aan haar getransponeerde", "ze is dan noodzakelijk vierkant"],
            ])),
            ("p", "<strong>De eenheidsmatrix is het neutraal element voor de vermenigvuldiging van "
                  "vierkante matrices</strong>: vermenigvuldigen ermee verandert niets. Een matrix met "
                  "<strong>determinant nul</strong> heet een niet-inverteerbare of singuliere matrix, en "
                  "dat is iets anders dan een nulmatrix."),
            ("p", "<strong>Transponeren maakt van de rijen kolommen en van de kolommen rijen.</strong> Een "
                  "matrix van twee bij vijf wordt zo een matrix van vijf bij twee, met dus "
                  "<strong>vijf</strong> rijen. <strong>De getransponeerde van een product A maal B is de "
                  "getransponeerde van B maal de getransponeerde van A</strong>: de volgorde draait om, "
                  "anders zouden de dimensies niet meer passen."),
            ("p", "<strong>De matrices van een vaste dimensie vormen met de optelling de structuur van een "
                  "commutatieve groep</strong>: de nulmatrix is het neutraal element en de tegengestelde matrix het "
                  "symmetrisch element."),
            ("weetje", "<strong>Bij matrices bestaan er nuldelers.</strong> Twee matrices die geen van "
                       "beide nul zijn, kunnen samen toch de nulmatrix geven. Bij reële getallen kan dat "
                       "niet."),
        ]),
        dict(kop="De determinant", blokken=[
            ("p", "<strong>De determinant van een matrix van orde twee is het product van de "
                  "hoofddiagonaal min het product van de andere diagonaal</strong>: linksboven maal "
                  "rechtsonder, min rechtsboven maal linksonder. Voor de matrix met op de eerste rij één "
                  "en twee en op de tweede rij drie en vier is dat <strong>min twee</strong>. De "
                  "<strong>determinant van de eenheidsmatrix is één</strong>, en een matrix met "
                  "<strong>twee volledig gelijke rijen heeft determinant nul</strong>."),
            ("p", "<strong>Alleen vierkante matrices hebben een determinant.</strong> Bij een rechthoekige "
                  "matrix is ze niet gedefinieerd; de rang kan je er wel van bepalen."),
            ("p", "<strong>De minor van een element is de determinant die overblijft als je zijn rij en "
                  "kolom schrapt.</strong> Een <strong>cofactor is die minor met een teken dat van de "
                  "plaats afhangt</strong>, afwisselend als een schaakbord, te beginnen met plus "
                  "linksboven. <strong>Een determinant van orde drie bereken je met de hand door te "
                  "ontwikkelen naar een rij of een kolom, met minoren en cofactoren</strong>; kies er een "
                  "met veel nullen, dan valt het meeste rekenwerk weg."),
            ("p", "<strong>De determinant is nuttig omdat je er in één berekening mee ziet of een matrix "
                  "inverteerbaar is</strong>, en daarmee ook of een stelsel met die coëfficiëntenmatrix "
                  "precies één oplossing heeft."),
        ]),
        dict(kop="Inverse en rang", blokken=[
            ("p", "<strong>Een vierkante matrix is inverteerbaar als haar determinant verschillend is van "
                  "nul.</strong> Determinant nul betekent dat rijen van elkaar afhangen, en dan kan je de "
                  "bewerking niet ongedaan maken: <strong>zo'n matrix heeft geen inverse</strong>. "
                  "<strong>Een rechthoekige matrix heeft er evenmin een.</strong> <strong>Vermenigvuldig "
                  "je een matrix met haar inverse, dan krijg je de eenheidsmatrix</strong>, in beide "
                  "volgordes."),
            ("p", "<strong>De rang van een matrix is het aantal rijen dat niet nul is in haar rijcanonieke "
                  "vorm.</strong> De rang zegt dus hoeveel rijen echt nieuwe informatie geven. De "
                  "<strong>rang van de eenheidsmatrix van orde drie is drie</strong> en de <strong>rang "
                  "van de nulmatrix is nul</strong>. <strong>Een matrix heeft maar één rijcanonieke "
                  "vorm</strong>, welke rijoperaties je ook kiest, en daarom is de rang eenduidig bepaald."),
            ("p", "<strong>Een vierkante matrix van orde n is inverteerbaar als haar rang gelijk is aan "
                  "n.</strong> Volle rang, determinant verschillend van nul en inverteerbaar zijn drie "
                  "manieren om hetzelfde te zeggen."),
            ("p", "<strong>De drie elementaire rijoperaties</strong> zijn: <strong>rijen verwisselen, een "
                  "rij met een getal vermenigvuldigen, of een veelvoud van een rij bij een andere "
                  "tellen</strong>. Ze veranderen de rang niet en houden een stelsel gelijkwaardig. "
                  "Vermenigvuldigen met nul mag niet."),
            ("p", "Een praktijkvoorbeeld van het product: zet een winkel <strong>de bestelde aantallen in "
                  "één matrix en de eenheidsprijzen in een andere</strong>, dan geeft hun product <strong>de "
                  "totale prijs per bestelling</strong>, want elk element is een rij aantallen tegen een "
                  "kolom prijzen."),
            ("kader", "<strong>Bij de inverse van een matrix van orde drie laat je het rekenwerk aan de "
                      "rekenapp over, maar je controleert het resultaat met de eenheidsmatrix.</strong> Het "
                      "product met de oorspronkelijke matrix moet de eenheidsmatrix geven. Die controle "
                      "kost één bewerking en vangt elke tikfout."),
        ]),
    ],
)

# ───────────────────────── 18. Stelsels oplossen en matrixmodellen
BUNDELS["stelsels-oplossen-en-matrixmodellen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stelsels oplossen en matrixmodellen",
    onder="Gauss-Jordan, de rang en de vrijheidsgraden, en matrices die een toestand laten evolueren.",
    secties=[
        dict(kop="Een stelsel als matrix", blokken=[
            ("p", "<strong>In de uitgebreide coëfficiëntenmatrix staan de coëfficiënten én de constanten "
                  "uit het rechterlid.</strong> Die constanten komen in een extra kolom, meestal met een "
                  "streep ervoor."),
            ("p", "<strong>Twee stelsels heten gelijkwaardig als ze dezelfde oplossingenverzameling "
                  "hebben.</strong> Elke <strong>elementaire rijoperatie maakt een gelijkwaardig "
                  "stelsel</strong> en <strong>verandert de oplossingenverzameling dus niet</strong>; "
                  "daarom mag je ze blijven toepassen tot de oplossing eruit af te lezen is. "
                  "<strong>Rijen optellen en verwisselen mag omdat die bewerkingen een gelijkwaardig "
                  "stelsel opleveren</strong> — de determinant verandert er wél door, maar die telt hier "
                  "niet. <strong>Een rij met nul vermenigvuldigen mag niet</strong>: dan gooi je een hele "
                  "vergelijking weg. Vermenigvuldigen mag alleen met een getal dat niet nul is."),
            ("p", "<strong>De methode van Gauss-Jordan vormt de matrix met rijoperaties om naar de "
                  "rijcanonieke vorm.</strong> In die vorm lees je de oplossing meteen af, of zie je dat "
                  "er geen of oneindig veel zijn."),
        ]),
        dict(kop="Bepaald, onbepaald of strijdig", blokken=[
            ("p", tabel(["Soort stelsel", "Wat geldt voor de rangen", "Hoeveel oplossingen"], [
                ["bepaald", "beide rangen gelijk aan het aantal onbekenden", "één"],
                ["onbepaald", "beide rangen gelijk, maar kleiner dan het aantal onbekenden", "oneindig veel"],
                ["strijdig", "de rang van de coëfficiëntenmatrix is de kleinste", "nul"],
            ])),
            ("p", "<strong>Een bepaald stelsel heeft precies één oplossing</strong>, en daarvoor moeten "
                  "<strong>beide rangen gelijk zijn aan het aantal onbekenden</strong>: bij vier "
                  "onbekenden dus rang <strong>vier</strong>. Evenveel vergelijkingen als onbekenden "
                  "volstaat niet, want twee keer dezelfde vergelijking telt maar één keer mee. Je kan zo'n "
                  "stelsel ook <strong>met de inverse matrix oplossen, als de coëfficiëntenmatrix vierkant "
                  "en inverteerbaar is</strong>."),
            ("p", "<strong>Een onbepaald stelsel heeft oneindig veel oplossingen</strong>, die je schrijft "
                  "met parameters. <strong>Een vrijheidsgraad is een onbekende die je vrij mag kiezen, "
                  "waarna de rest vastligt</strong>, en het aantal vrijheidsgraden is het aantal "
                  "onbekenden min de rang: bij <strong>drie onbekenden en rang twee is dat "
                  "één</strong>. Je <strong>noteert de oplossingenverzameling als een verzameling van "
                  "koppels of drietallen met een parameter erin</strong>, zodat je ziet hoe de oplossingen "
                  "van elkaar afhangen."),
            ("p", "<strong>Een strijdig stelsel heeft nul oplossingen</strong>: de "
                  "oplossingenverzameling is leeg. Je <strong>herkent het in de rijcanonieke vorm aan een "
                  "rij met overal nullen links en een getal dat niet nul is rechts</strong>. Die rij zegt "
                  "letterlijk dat nul gelijk is aan dat getal; een rij met overal nullen, ook rechts, is "
                  "net onschuldig. Meetkundig: <strong>twee evenwijdige rechten die niet samenvallen geven "
                  "een strijdig stelsel</strong>."),
            ("kader", "<strong>Een stelsel met meer onbekenden dan vergelijkingen heeft niet altijd "
                      "oplossingen.</strong> Het kan nog strijdig zijn. Heeft het er wel, dan zijn het "
                      "meteen oneindig veel."),
        ]),
        dict(kop="Matrixmodellen", blokken=[
            ("p", "<strong>Een overgangsmatrix beschrijft hoe een toestand overgaat in de volgende "
                  "toestand.</strong> Je vermenigvuldigt de huidige toestand ermee en krijgt de volgende. "
                  "<strong>Een overgangsmatrix is altijd vierkant</strong>, want ze zet een toestand om in "
                  "een toestand van dezelfde soort. <strong>Een nul erin betekent dat die overgang niet "
                  "voorkomt.</strong>"),
            ("p", "<strong>De toestand na twee overgangen bereken je met het kwadraat van de "
                  "overgangsmatrix</strong>, en na vijf stappen verhef je haar tot de "
                  "<strong>vijfde</strong> macht: één macht per stap. Voor tien jaar klantenverloop neem "
                  "je dus <strong>de beginverdeling maal de overgangsmatrix tot de tiende macht</strong>."),
            ("p", tabel(["Soort matrix", "Wat ze beschrijft", "Kenmerk"], [
                ["Markov-matrix", "overgangskansen tussen toestanden", "elke kolom telt op tot één"],
                ["Lesliematrix", "hoe een populatie per leeftijdsgroep evolueert", "met overlevingskansen en nakomelingen"],
                ["migratiematrix", "hoeveel inwoners van de ene streek naar de andere verhuizen", "de toestanden zijn de streken"],
                ["verbindingsmatrix", "welke knopen van een graaf verbonden zijn", "een één bij een verbinding, anders een nul"],
            ])),
            ("p", "<strong>Een graaf is een tekening met punten en verbindingen ertussen</strong>; die "
                  "punten heten knopen. Elke graaf kan je als matrix schrijven en elke zo'n matrix als "
                  "graaf tekenen: <strong>een graaf met vier knopen geeft een verbindingsmatrix van orde "
                  "vier</strong>. Een <strong>directe wegen matrix laat zien welke knopen rechtstreeks "
                  "verbonden zijn</strong>; omwegen vind je pas in haar machten terug, want <strong>het "
                  "kwadraat van een verbindingsmatrix telt de wegen van lengte twee</strong>."),
            ("p", "<strong>Een evenwichtstoestand is een toestand die na de overgang gelijk blijft.</strong> "
                  "Je <strong>ziet dat een model stabiliseert doordat de opeenvolgende toestanden bijna niet "
                  "meer van elkaar verschillen</strong>. <strong>Niet elk matrixmodel komt in evenwicht</strong>: "
                  "sommige blijven schommelen of groeien onbeperkt, dus dat moet je nagaan."),
            ("kader", "<strong>Een matrixmodel voorspelt niet met zekerheid wat er zal gebeuren.</strong> "
                      "Het rekent uit wat er gebeurt als de overgangen gelijk blijven. Verandert er iets in "
                      "de werkelijkheid, dan klopt het model niet meer. <strong>De rekenapp gebruik je "
                      "omdat je vaak hoge machten nodig hebt</strong>: het model opstellen en de uitkomst "
                      "duiden blijft jouw werk."),
        ]),
        dict(kop="Een stelsel uit een context", blokken=[
            ("p", "Ken je het <strong>totaalbedrag van drie bestellingen met telkens dezelfde drie "
                  "artikelen</strong>, dan kan je <strong>de prijs per artikel berekenen als het stelsel "
                  "bepaald is</strong>. Drie vergelijkingen met drie onbekenden, maar enkel als de drie "
                  "bestellingen echt nieuwe informatie geven; anders is het stelsel onbepaald of strijdig."),
        ]),
    ],
)

# ───────────────────────── 19. Algebraïsche structuren en groepen
BUNDELS["algebraische-structuren-en-groepen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Algebraïsche structuren en groepen",
    onder="De vier eigenschappen van een groep, de Cayley-tabel, en de uniciteit van het neutraal en het invers element.",
    secties=[
        dict(kop="Wat een groep is", blokken=[
            ("p", "<strong>Een verzameling met een bewerking is een groep als ze aan vier eigenschappen "
                  "voldoet</strong>: de bewerking is <strong>intern</strong> en <strong>associatief</strong>, "
                  "er is een <strong>neutraal element</strong>, en elk element heeft een <strong>invers "
                  "element</strong>."),
            ("p", tabel(["Eigenschap", "Wat ze zegt", "Voorbeeld"], [
                ["intern", "het resultaat ligt altijd weer in de verzameling", "de optelling in de gehele getallen wel, de deling niet"],
                ["associatief", "de haakjes mogen verschuiven zonder gevolg", "a met (b met c) geeft hetzelfde als (a met b) met c"],
                ["neutraal element", "het laat elk ander element ongewijzigd", "nul bij de optelling, één bij de vermenigvuldiging"],
                ["invers element", "samen met a geeft het het neutraal element", "het tegengestelde, of het omgekeerde"],
            ])),
            ("p", "<strong>Een groep heet commutatief als de volgorde van de twee elementen niets "
                  "uitmaakt.</strong> Dat is een vijfde eigenschap die erbij komt, dus <strong>niet elke "
                  "groep is commutatief</strong>: de vermenigvuldiging van matrices bijvoorbeeld niet. "
                  "<strong>Een eindige groep is een groep met een eindig aantal elementen</strong>, maar "
                  "<strong>een groep hoeft niet eindig te zijn</strong>: de gehele getallen met de "
                  "optelling vormen een oneindige groep."),
            ("p", "<strong>Om aan te tonen dat iets een groep is, ga je de vier eigenschappen één voor één "
                  "na.</strong> Eén tegenvoorbeeld bij één eigenschap volstaat om te besluiten dat het "
                  "geen groep is."),
        ]),
        dict(kop="Voorbeelden en tegenvoorbeelden", blokken=[
            ("p", "<strong>De gehele getallen vormen met de optelling een groep</strong>: de optelling is "
                  "intern en associatief, <strong>nul is het neutraal element</strong> en elk geheel getal "
                  "heeft zijn tegengestelde. Het <strong>invers element van zeven is min zeven</strong>."),
            ("p", "<strong>De natuurlijke getallen vormen met de optelling geen groep</strong>: er zijn "
                  "geen negatieve getallen, dus drie heeft geen tegengestelde binnen de verzameling. "
                  "<strong>De gehele getallen vormen met de vermenigvuldiging evenmin een groep</strong>: "
                  "het invers van drie zou een derde zijn, en dat is geen geheel getal. Alleen één en min "
                  "één hebben er een."),
            ("p", "<strong>De reële getallen zonder nul vormen met de vermenigvuldiging wél een "
                  "groep</strong>, met <strong>één</strong> als neutraal element. Nul moet eruit, want "
                  "<strong>nul heeft geen invers element voor de vermenigvuldiging</strong>: er bestaat "
                  "geen getal dat maal nul één geeft."),
            ("p", "<strong>De matrices van orde twee vormen onder de optelling een groep, en ze is "
                  "bovendien commutatief</strong>: de nulmatrix is het neutraal element en elke matrix "
                  "heeft haar tegengestelde. Bij de vermenigvuldiging lukt het niet."),
            ("weetje", "Een voorbeeld uit de meetkunde: de <strong>vier draaiingen die een vierkant op "
                       "zichzelf afbeelden</strong>, met na elkaar uitvoeren als bewerking, vormen een "
                       "<strong>eindige commutatieve groep</strong>. De draaiing over nul graden is het "
                       "neutraal element en elke draaiing heeft haar tegendraaiing."),
        ]),
        dict(kop="De Cayley-tabel", blokken=[
            ("p", "<strong>In een Cayley-tabel staat het resultaat van de bewerking voor elk paar "
                  "elementen</strong>: rij voor het eerste element, kolom voor het tweede, en in het vakje "
                  "het resultaat. Een groep met <strong>vijf elementen</strong> geeft dus een tabel met "
                  "<strong>vijfentwintig</strong> vakjes, en een groep met zes elementen heeft "
                  "<strong>zes</strong> rijen. <strong>Van een oneindige groep kan je de volledige tabel "
                  "niet opstellen</strong>, want ze zou oneindig veel rijen hebben."),
            ("p", "Uit de tabel lees je de eigenschappen af. <strong>Is de tabel symmetrisch om de "
                  "hoofddiagonaal, dan is de groep commutatief.</strong> <strong>Het neutraal element "
                  "herken je doordat zijn rij en zijn kolom gewoon de kopregel herhalen.</strong> <strong>Het "
                  "invers element van a vind je door in de rij van a te zoeken waar het neutraal element "
                  "staat</strong>; de kolom waarin dat vakje staat, wijst het aan. En <strong>is elk "
                  "element zijn eigen invers, dan staat op de hoofddiagonaal overal het neutraal "
                  "element</strong>."),
            ("p", "<strong>In de Cayley-tabel van een groep komt elk element precies één keer voor in elke "
                  "rij.</strong> Zou een element twee keer voorkomen, dan had je twee oplossingen voor "
                  "dezelfde vergelijking, en dat kan niet in een groep."),
        ]),
        dict(kop="Uniciteit en rekenen in een groep", blokken=[
            ("p", "<strong>Een groep heeft juist één neutraal element</strong> en <strong>elk element heeft "
                  "juist één invers element</strong>. Dat heet de <strong>uniciteit</strong>: allebei zijn ze "
                  "<strong>uniek</strong>, en dat is te bewijzen. Let op wat je precies bewijst: <strong>dat er één bestaat, is een van de vier "
                  "eigenschappen; dat het er maar één is, moet je aantonen.</strong> <strong>Het bewijs "
                  "begint door te veronderstellen dat er twee neutrale elementen zijn</strong>; daarna "
                  "bewerk je ze met elkaar en toont elk van de twee aan dat het resultaat de andere is."),
            ("p", "Twee rekenregels voor inversen. <strong>Het invers van het invers van a is "
                  "a</strong>: twee keer omkeren brengt je terug bij het begin. En bij een product "
                  "<strong>keert de volgorde om</strong>: het invers van a bewerkt met b is eerst het "
                  "invers van b en dan dat van a, <strong>niet andersom</strong>. <strong>Dat komt omdat "
                  "je het binnenste paar eerst moet kunnen wegwerken</strong>: zet je ze omgekeerd naast "
                  "elkaar, dan valt eerst b weg en pas daarna a. Bij een commutatieve groep maakt dat "
                  "verschil natuurlijk niets uit."),
            ("p", "<strong>In een groep mag je links en rechts van het gelijkheidsteken hetzelfde element "
                  "wegwerken</strong> door beide leden met zijn invers te bewerken. Dat is het hele idee "
                  "achter het oplossen van vergelijkingen in een groep, en <strong>de kant volgt a</strong>: "
                  "bij <strong>a bewerkt met x is b</strong> bewerk je <strong>links</strong> met het "
                  "invers van a, bij <strong>x bewerkt met a is b</strong> bewerk je <strong>rechts</strong>. "
                  "In een groep die niet commutatief is, is die kant belangrijk."),
        ]),
    ],
)

# ───────────────────────── 20. Punten, vectoren en afstanden in de ruimte
BUNDELS["punten-vectoren-en-afstanden-in-de-ruimte-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Punten, vectoren en afstanden in de ruimte",
    onder="Vectoren met hun coördinaten en hun norm, het scalair product, en afstanden, hoeken en zwaartepunten.",
    secties=[
        dict(kop="Vrije vector en puntvector", blokken=[
            ("p", "<strong>Een vrije vector is een richting, een zin en een lengte, zonder vast "
                  "beginpunt.</strong> Je mag hem overal in de ruimte neerleggen; het blijft dezelfde "
                  "vector. <strong>Twee pijlen met dezelfde coördinaten maar met een ander beginpunt zijn "
                  "dus dezelfde vrije vector.</strong> Een <strong>puntvector</strong> is <strong>de "
                  "vector van de oorsprong naar een punt</strong>, en zijn coördinaten zijn precies die "
                  "van het punt."),
            ("p", "<strong>Een vector in de ruimte heeft drie coördinaten</strong>, één per as; in het "
                  "vlak zijn het er twee. Je werkt in een <strong>orthonormaal assenstelsel</strong>: "
                  "<strong>de assen staan loodrecht op elkaar en de eenheden zijn even lang</strong>. "
                  "Alleen dan kloppen de formules voor de norm, de afstand en de hoek."),
            ("p", "<strong>De coördinaten van de vector van A naar B zijn die van B min die van A</strong>: "
                  "eindpunt min beginpunt. Draai je het om, dan krijg je de tegengestelde vector. Een "
                  "<strong>richtingsvector van een rechte is een vector die evenwijdig is met die "
                  "rechte</strong>, en <strong>elke rechte heeft er oneindig veel</strong>, want elk "
                  "veelvoud is er ook een."),
        ]),
        dict(kop="Rekenen met vectoren", blokken=[
            ("p", "<strong>Optellen doe je coördinaat per coördinaat</strong>: de eerste bij de eerste, en "
                  "zo verder. <strong>Grafisch leg je de staart van de tweede aan de kop van de "
                  "eerste</strong>, en de somvector loopt van de eerste staart naar de laatste kop; met de "
                  "parallellogramregel krijg je hetzelfde. <strong>De optelling van vectoren is "
                  "commutatief</strong>, <strong>de nulvector is het neutraal element</strong> en "
                  "<strong>het symmetrisch element is de tegengestelde vector</strong>, met alle "
                  "coördinaten van teken veranderd."),
            ("p", "<strong>Bij een vermenigvuldiging met een getal vermenigvuldig je elke coördinaat "
                  "afzonderlijk</strong>: de vector twee, min één, drie maal twee heeft als eerste "
                  "coördinaat <strong>vier</strong>. <strong>Met een negatief getal keert de zin om</strong>; "
                  "de richting blijft dezelfde en de lengte verandert met de grootte van dat getal."),
            ("p", "<strong>De norm van een vector is zijn lengte</strong>, berekend als de wortel uit de "
                  "som van de kwadraten van de coördinaten. <strong>Een norm kan nooit negatief zijn</strong>; "
                  "alleen de nulvector heeft norm nul. De norm van de vector <strong>drie, nul, vier is "
                  "vijf</strong>."),
            ("p", "<strong>Een vector ontbinden in zijn componenten betekent hem schrijven als een som van "
                  "vectoren langs de assen.</strong> Elke coördinaat is de lengte van één component, en "
                  "dat kan grafisch en door te rekenen."),
            ("weetje", "Werken er <strong>twee krachten tegelijk op een voorwerp</strong>, dan vind je de "
                       "<strong>resulterende kracht door de twee krachtvectoren op te tellen</strong>. Een "
                       "kracht heeft immers een grootte én een richting. Enkel de getallen optellen klopt "
                       "alleen als ze dezelfde kant op wijzen."),
        ]),
        dict(kop="Het scalair product", blokken=[
            ("p", "<strong>Het scalair product van twee vectoren levert een getal op</strong>, geen "
                  "vector; daar komt de naam vandaan. <strong>In coördinaten tel je de producten van de "
                  "overeenkomstige coördinaten op</strong>: voor één, twee, drie en twee, nul, één geeft "
                  "dat <strong>vijf</strong>. <strong>Het scalair product is commutatief.</strong>"),
            ("p", "<strong>Het scalair product van twee loodrechte vectoren is nul</strong>, en dat werkt "
                  "ook omgekeerd: dat is het <strong>criterium voor loodrechte stand</strong>. <strong>Om "
                  "na te gaan of twee rechten loodrecht staan, bereken je dus het scalair product van hun "
                  "richtingsvectoren</strong>, tenminste in een orthonormaal assenstelsel. <strong>Het "
                  "werkt omdat de cosinus van negentig graden nul is</strong>: het scalair product is het "
                  "product van de normen maal die cosinus."),
            ("p", "<strong>De hoek tussen twee vectoren bereken je uit het scalair product gedeeld door "
                  "het product van de normen</strong>; die breuk is de cosinus van de hoek. <strong>Is het "
                  "scalair product negatief, dan is de hoek stomp</strong>, niet scherp: bij een scherpe "
                  "hoek is het positief, bij een rechte hoek nul."),
            ("p", "<strong>Het scalair product van een vector met zichzelf is het kwadraat van zijn "
                  "norm</strong>, niet de norm zelf. En <strong>twee vectoren zijn evenwijdig als de ene "
                  "een veelvoud van de andere is</strong>: alle coördinaten verschillen dan met dezelfde "
                  "factor. Een <strong>normaalvector van een vlak</strong> is <strong>een vector die "
                  "loodrecht op dat vlak staat</strong>; zijn coördinaten lees je af uit de cartesische "
                  "vergelijking."),
        ]),
        dict(kop="Afstanden, middens en zwaartepunten", blokken=[
            ("p", "<strong>De afstand tussen twee punten is de norm van de vector tussen die twee "
                  "punten</strong>: eerst de vector, dan zijn lengte. De punten <strong>één, twee, drie en "
                  "één, twee, acht liggen vijf uit elkaar</strong>, en het punt <strong>twee, drie, zes "
                  "ligt zeven van de oorsprong</strong>."),
            ("p", tabel(["Wat je zoekt", "Hoe je het berekent", "Voorbeeld"], [
                ["het midden van een lijnstuk", "het gemiddelde van de coördinaten van de twee uiteinden", "tussen twee, vier, zes en vier, acht, tien is de eerste coördinaat drie"],
                ["het zwaartepunt van een driehoek", "de som van de drie hoekpunten gedeeld door drie", "bij eerste coördinaten nul, drie en zes wordt dat drie"],
                ["het zwaartepunt van een viervlak", "de som van de vier hoekpunten gedeeld door vier", "hetzelfde recept, met vier punten"],
            ])),
            ("weetje", "Vliegt een drone <strong>eerst drie meter naar het oosten en dan vier meter naar "
                       "het noorden</strong>, dan vind je zijn verplaatsing <strong>als de som van de twee "
                       "verplaatsingsvectoren</strong>: vijf meter, niet zeven. De afgelegde weg is wel "
                       "zeven meter."),
        ]),
    ],
)

# ───────────────────────── 21. Rechten en vlakken in de ruimte
BUNDELS["rechten-en-vlakken-in-de-ruimte-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rechten en vlakken in de ruimte",
    onder="Vectoriële, parametrische en cartesische vergelijkingen, onderlinge ligging, afstanden en hoeken.",
    secties=[
        dict(kop="De vergelijking van een rechte", blokken=[
            ("p", "<strong>Om de vergelijking van een rechte op te stellen heb je een punt en een "
                  "richtingsvector nodig</strong>: het punt zegt waar ze ligt, de richtingsvector welke "
                  "kant ze op loopt. Twee punten volstaan ook, want daar haal je de richtingsvector uit."),
            ("p", "In de <strong>parametrische vergelijkingen</strong> geeft <strong>elke waarde van de "
                  "parameter een ander punt van de rechte</strong>; laat je de parameter alle reële "
                  "waarden doorlopen, dan krijg je de hele rechte. In de ruimte zijn dat <strong>drie</strong> "
                  "vergelijkingen, één per coördinaat, allemaal met dezelfde parameter."),
            ("p", "<strong>Een rechte in de ruimte heeft twee cartesische vergelijkingen, geen één</strong>: "
                  "ze is de doorsnede van twee vlakken. <strong>In het vlak heeft een rechte er wel precies "
                  "één</strong>. <strong>Van parametrisch naar cartesisch werk je de parameter weg</strong>: "
                  "je drukt hem uit in één vergelijking en vult die in de twee andere in."),
            ("p", "<strong>Of een punt op een rechte ligt, controleer je door zijn coördinaten in de "
                  "vergelijkingen in te vullen.</strong> Bij de parametrische vorm moet er voor alle drie "
                  "dezelfde parameterwaarde uitkomen."),
        ]),
        dict(kop="De vergelijking van een vlak", blokken=[
            ("p", "<strong>Een vlak ligt vast door één punt en twee richtingsvectoren die niet evenwijdig "
                  "zijn</strong>, of door <strong>drie punten die niet op eenzelfde rechte liggen</strong>. "
                  "<strong>Drie punten op één rechte bepalen geen vlak</strong>, want daar gaan oneindig "
                  "veel vlakken door. Daarom staat een tafel met drie poten nooit te wiebelen. In de "
                  "<strong>parametrische vergelijkingen van een vlak staan twee parameters</strong>, één "
                  "per richtingsvector."),
            ("p", "<strong>De cartesische vergelijking van een vlak heeft de vorm: a maal x plus b maal y "
                  "plus c maal z plus d is nul.</strong> Eén vergelijking van de eerste graad in drie "
                  "onbekenden. <strong>De coëfficiënten van x, y en z vormen samen een "
                  "normaalvector</strong> van dat vlak: voor <strong>twee x min drie y plus z min vijf is "
                  "nul</strong> is de eerste coördinaat daarvan <strong>twee</strong>. Ken je <strong>een "
                  "punt en een normaalvector, dan kan je die cartesische vergelijking opstellen</strong>. "
                  "Het vlak door de x-as en de y-as heeft als vergelijking <strong>z is gelijk aan "
                  "nul</strong>."),
            ("p", "<strong>Met een drie bij drie determinant stel je de cartesische vergelijking op door "
                  "die determinant gelijk te stellen aan nul.</strong> In de determinant staan de "
                  "verbindingsvector naar een onbekend punt en de twee richtingsvectoren. Nul betekent "
                  "<strong>dat de drie vectoren in eenzelfde vlak liggen</strong>; was de determinant niet "
                  "nul, dan zouden ze de hele ruimte opspannen."),
            ("p", "Omgekeerd, <strong>van cartesisch naar parametrisch zoek je een punt en twee "
                  "richtingsvectoren van het vlak</strong>. Twee van de drie onbekenden mag je vrij kiezen, "
                  "en die twee vrijheidsgraden worden je twee parameters."),
        ]),
        dict(kop="Onderlinge ligging", blokken=[
            ("p", tabel(["Wat je vergelijkt", "Mogelijke liggingen"], [
                ["twee rechten", "samenvallend, evenwijdig, snijdend of kruisend"],
                ["een rechte en een vlak", "in het vlak, evenwijdig ernaast, of snijdend"],
                ["twee vlakken", "samenvallend, evenwijdig, of snijdend volgens een rechte"],
            ])),
            ("p", "<strong>Kruisende rechten zijn rechten die niet evenwijdig zijn en toch geen snijpunt "
                  "hebben.</strong> Ze liggen niet in eenzelfde vlak; denk aan twee wegen boven elkaar met "
                  "een brug ertussen. Dat bestaat alleen in de ruimte, en daarom zijn <strong>twee rechten "
                  "die elkaar niet snijden niet noodzakelijk evenwijdig</strong>. <strong>Twee evenwijdige "
                  "rechten liggen wél altijd in eenzelfde vlak</strong>, en door twee kruisende rechten "
                  "gaat net geen enkel vlak."),
            ("p", "<strong>Twee vlakken zijn evenwijdig als hun normaalvectoren veelvouden van elkaar "
                  "zijn.</strong> Ze <strong>vallen samen als je de ene vergelijking uit de andere kan "
                  "vermenigvuldigen</strong>; anders liggen ze er netjes naast. <strong>Twee vlakken die "
                  "niet evenwijdig zijn, snijden elkaar volgens een rechte</strong>, nooit in één punt."),
            ("p", "<strong>Een rechte is evenwijdig met een vlak als haar richtingsvector loodrecht op de "
                  "normaalvector staat</strong>, dus als hun scalair product nul is. Ligt er dan ook nog "
                  "een punt van de rechte in het vlak, dan ligt ze er helemaal in; in de praktijk "
                  "<strong>volstaat het dat twee van haar punten in het vlak liggen</strong>. "
                  "<strong>Loodrecht op het vlak staat ze als haar richtingsvector evenwijdig is met de "
                  "normaalvector.</strong>"),
        ]),
        dict(kop="Afstanden en hoeken", blokken=[
            ("p", "<strong>De afstand van een punt tot een vlak meet je langs de loodlijn uit dat punt op "
                  "het vlak</strong>, want de afstand is altijd de kortste. <strong>De afstand tussen twee "
                  "evenwijdige vlakken bereken je als de afstand van een punt van het ene tot het "
                  "andere</strong>; welk punt je kiest maakt niet uit. <strong>Tussen twee samenvallende "
                  "vlakken is de afstand nul</strong>, en ook <strong>tussen twee snijdende rechten is ze "
                  "nul</strong>, want ze hebben een punt gemeen."),
            ("p", "<strong>De hoek tussen twee vlakken is de hoek tussen hun normaalvectoren</strong>, "
                  "waarvan je de scherpe neemt. <strong>Tussen twee evenwijdige vlakken is die hoek "
                  "nul</strong> graden. <strong>De hoek tussen twee rechten vind je uit het scalair "
                  "product van hun richtingsvectoren</strong>, ook bij kruisende rechten, want de hoek "
                  "hangt enkel van de richtingen af."),
            ("weetje", "Bij een <strong>hellend dakvlak en de verticale gevel eronder</strong> is de hoek "
                       "tussen de twee vlakken <strong>de hoek tussen hun normaalvectoren, als scherpe hoek "
                       "genomen</strong>. De hellingshoek van het dak met de grond is een andere hoek."),
        ]),
    ],
)

# ───────────────────────── 22. Programmeren: algoritmen en structuren
BUNDELS["programmeren-algoritmen-en-structuren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Programmeren: algoritmen en structuren",
    onder="De bouwstenen van een programma, de vier datastructuren, de algoritmische technieken, en correctheid en eindigheid.",
    secties=[
        dict(kop="Van probleem naar programma", blokken=[
            ("p", "<strong>Een algoritme is een stappenplan dat na eindig veel stappen tot een oplossing "
                  "komt.</strong> Het bestaat los van de taal; pas daarna schrijf je het in "
                  "<strong>Python</strong>, in een online omgeving, zodat je niets op je eigen computer "
                  "hoeft te installeren."),
            ("p", "Je werkt in <strong>vier stappen</strong>: <strong>het probleem analyseren, een "
                  "algoritme ontwerpen, het programmeren, en testen en debuggen</strong>. Meteen beginnen "
                  "typen zonder het probleem te analyseren kost je achteraf meer tijd dan het wint. "
                  "<strong>Debuggen is fouten opsporen en herstellen</strong>, en je <strong>test ook met "
                  "randgevallen, omdat fouten zich daar verstoppen</strong>: een lege lijst, één element, "
                  "een nul, een negatief getal."),
            ("p", "<strong>Geef variabelen een zinvolle naam, zodat je code leesbaar blijft</strong> voor "
                  "jezelf en voor anderen. De computer kan het niets schelen, maar een lezer wel, en dat "
                  "telt mee in de beoordeling. <strong>Commentaar wordt niet mee uitgevoerd</strong>; ze "
                  "staat er alleen voor wie de code leest."),
        ]),
        dict(kop="De bouwstenen", blokken=[
            ("p", tabel(["Bouwsteen", "Wat ze doet", "In Python"], [
                ["variabele", "een naam waarachter een waarde zit die kan veranderen", "je overschrijft de waarde gewoon"],
                ["constante", "een waarde die tijdens het programma niet verandert", "het aantal seconden in een uur, met een naam erbij"],
                ["conditie", "een stuk code alleen laten lopen als iets waar is", "de constructie met als en anders"],
                ["iteratie", "een herhaling van hetzelfde stuk code", "een lus, over een lijst of zolang iets geldt"],
                ["functie", "een stuk code een naam geven en hergebruiken", "één keer schrijven, zo vaak oproepen als je wil"],
            ])),
        ]),
        dict(kop="De vier datastructuren", blokken=[
            ("p", "<strong>Een string is een rij tekens</strong>: letters, cijfers en leestekens na "
                  "elkaar, tussen aanhalingstekens."),
            ("p", tabel(["Datastructuur", "Waarvoor", "Kenmerk"], [
                ["list", "een geordende rij die je nog wil aanpassen", "geordend én aanpasbaar"],
                ["tuple", "een geordende rij die vastligt", "je kan hem achteraf niet meer wijzigen"],
                ["set", "enkel de verschillende waarden overhouden", "elk element komt er maar één keer in voor"],
                ["dictionary, in het Nederlands een woordenboek", "paren van een sleutel en een waarde", "je zoekt iets op met de sleutel"],
            ])),
            ("p", "<strong>Een list en een tuple zijn allebei geordend; alleen de tuple ligt vast.</strong> "
                  "<strong>Een set kan hetzelfde element niet twee keer bevatten</strong>: steek je de "
                  "getallen één, twee, twee en drie erin, dan blijven er <strong>drie</strong> elementen "
                  "over. Dubbels eruit halen is precies waar een set voor dient."),
        ]),
        dict(kop="Algoritmische technieken", blokken=[
            ("p", "<strong>Recursie is een functie die zichzelf oproept</strong>, waarbij het probleem "
                  "telkens een beetje kleiner wordt tot het vanzelf oplosbaar is. <strong>Elke recursieve "
                  "functie heeft een geval nodig waarin ze zichzelf niet meer oproept</strong>, een "
                  "stopgeval. <strong>Zonder dat blijft ze zichzelf oproepen tot het programma "
                  "vastloopt</strong>, en geeft Python een foutmelding omdat de oproepen te diep gaan."),
            ("p", "<strong>Verdeel-en-heers</strong> is de techniek waarbij je <strong>een probleem "
                  "opsplitst in kleinere deelproblemen en de deeloplossingen daarna samenvoegt</strong>. "
                  "Sorteren doe je zo: splits de lijst in twee, sorteer elke helft en voeg ze samen. Moet "
                  "je in een <strong>gesorteerde lijst van duizend getallen</strong> nagaan of een getal "
                  "erin staat, dan is de slimste aanpak <strong>telkens de helft wegnemen</strong>: tien "
                  "stappen volstaan dan."),
            ("p", "<strong>Bij dynamisch programmeren bewaar je tussenresultaten zodat je ze niet twee "
                  "keer hoeft te berekenen.</strong> Bij de rij van Fibonacci scheelt dat het verschil "
                  "tussen een seconde en een eeuwigheid. Het <strong>kost meer geheugen maar wint "
                  "tijd</strong>."),
        ]),
        dict(kop="Correctheid, eindigheid en vergelijken", blokken=[
            ("p", "<strong>Een algoritme is correct als het voor elke toegelaten invoer het juiste antwoord "
                  "geeft</strong>, niet alleen voor de gevallen die je toevallig uitprobeerde. <strong>Het "
                  "is eindig als het na een eindig aantal stappen stopt.</strong> <strong>Je "
                  "beargumenteert de eindigheid omdat een programma dat blijft lopen niets oplost</strong>, "
                  "ook al klopt elke stap: bij een lus toon je dat de voorwaarde ooit vals wordt, bij "
                  "recursie dat je het stopgeval altijd bereikt."),
            ("p", "<strong>Twee oplossingen voor hetzelfde probleem vergelijk je op snelheid, "
                  "geheugengebruik en gedrag bij veel gegevens.</strong> <strong>Twee algoritmen die "
                  "hetzelfde antwoord geven, zijn daarom nog niet even snel</strong>: het ene kan duizend "
                  "keer trager zijn. Een oplossing die bij tien getallen vlot werkt, kan bij een miljoen "
                  "getallen onbruikbaar worden."),
        ]),
        dict(kop="Bestanden en bibliotheken", blokken=[
            ("p", "Naast een gewoon tekstbestand lees je ook <strong>CSV</strong>-bestanden in en schrijf "
                  "je ze weg: bestanden waarin de waarden door komma's of puntkomma's gescheiden staan, "
                  "zoals een tabel."),
            ("p", "<strong>Je mag matplotlib, numpy en random gebruiken</strong>, en geen andere, tenzij "
                  "de opdracht er uitdrukkelijk een vermeldt en toelicht. <strong>Matplotlib dient om "
                  "grafieken te tekenen</strong> van je gegevens, <strong>numpy om vlot met grote rijen "
                  "getallen te rekenen</strong> (veel sneller dan met een lus over een gewone list), en "
                  "<strong>random om toevalsgetallen te laten genereren</strong>, handig voor een simulatie."),
            ("p", "<strong>Een numerieke methode is een manier om een antwoord te benaderen met "
                  "rekenstappen.</strong> Je krijgt geen exacte formule maar een benadering, die je zo "
                  "nauwkeurig maakt als je wil. Zo <strong>benader je een bepaalde integraal door de "
                  "oppervlakte van heel veel smalle stroken op te tellen</strong>: precies de Riemannsom, "
                  "maar dan door de computer uitgevoerd."),
        ]),
    ],
)
