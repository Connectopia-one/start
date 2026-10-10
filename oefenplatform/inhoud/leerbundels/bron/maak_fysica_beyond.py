# -*- coding: utf-8 -*-
"""De leerbundels voor fysica op 🌍 Beyond-niveau.

Gebaseerd op de vakfiche fysica van de 3de graad doorstroomfinaliteit, geldig
vanaf 1 januari 2027. Die fiche hoort bij de richtingen die hun wetenschappen
in drie aparte examens afleggen: biologie, chemie en fysica. Ze gaat dus veel
dieper dan het onderdeel fysica van de fiche natuurwetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De drieëntwintig thema's volgen de weging van de fiche zelf: zeven thema's voor
elektriciteit en magnetisme, zes voor de mechanica, vier voor de gaswetten en de
warmteleer met de trillingen en golven erbij, drie voor de kwantum- en
kernfysica, en twee voor het onderzoek en STEM.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde woorden
als de vraag. `python3 dekking.py ../../beyond/fysica.json` doet daar het
voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

Veldlijnenpatronen, vectoren en grafieken tekenen kan in een bundel niet, dus
staat het verloop of het patroon telkens in woorden beschreven.

De bundelsleutels eindigen op "-beyond".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Fysica"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────── 1. Elektrische lading, geleiders en influentie
BUNDELS["elektrische-lading-geleiders-en-influentie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrische lading, geleiders en influentie",
    onder="De grootheid Q, waarom metaal geleidt, en wat influentie met een voorwerp doet.",
    secties=[
        dict(kop="De grootheid Q en haar eenheid", blokken=[
            ("p", r"Er zijn <strong>twee soorten elektrische lading</strong>: "
                  r"<strong>positief en negatief</strong>. Gelijksoortige ladingen stoten elkaar af, "
                  r"ongelijksoortige trekken elkaar aan. De <strong>grootheid</strong> heet "
                  r"<strong>\(Q\)</strong> en haar <strong>eenheid</strong> is de "
                  r"<strong>coulomb</strong>, met symbool \(\text{C}\). Let op dat verschil: "
                  r"\(Q\) is wat je meet, \(\text{C}\) is waarin je het uitdrukt. Je schrijft dus "
                  r"\(Q=-8\ \text{nC}\), en dat lees je als een lading van min acht nanocoulomb."),
            ("p", tabel(["Voorvoegsel", "Betekent", "Voorbeeld"], [
                [r"milli (\(\text{mC}\))", r"\(10^{-3}\)", r"\(2\ \text{mC}=2\cdot 10^{-3}\ \text{C}\)"],
                [r"micro (\(\mu\text{C}\))", r"\(10^{-6}\)", r"\(5\ \mu\text{C}=5\cdot 10^{-6}\ \text{C}\)"],
                [r"nano (\(\text{nC}\))", r"\(10^{-9}\)", r"\(8\ \text{nC}=8\cdot 10^{-9}\ \text{C}\)"],
                [r"pico (\(\text{pC}\))", r"\(10^{-12}\)", r"\(4\ \text{pC}=4\cdot 10^{-12}\ \text{C}\)"],
            ])),
            ("p", r"De kleinste lading die er bestaat is de <strong>elementaire lading</strong> "
                  r"\(e\), de lading van één proton en, op het teken na, van één elektron:"),
            ("p", r"\[e=1{,}602\cdot 10^{-19}\ \text{C}\]"),
            ("p", r"Daarom is <strong>de lading van een voorwerp altijd een geheel veelvoud van "
                  r"\(e\)</strong>. Dat schrijf je als \(Q=n\cdot e\), met \(n\) het aantal "
                  r"elektronen te veel of te weinig. Je kan er geen half elektron bij of af doen; "
                  r"dat heet de <strong>kwantisatie van de lading</strong>. Heeft een voorwerp "
                  r"\(5{,}0\cdot 10^{12}\) elektronen te veel, dan is "
                  r"\(Q=-5{,}0\cdot 10^{12}\cdot 1{,}602\cdot 10^{-19}\ \text{C}"
                  r"\approx -8{,}0\cdot 10^{-7}\ \text{C}\). Omgekeerd hoort bij "
                  r"\(Q=-4{,}8\cdot 10^{-9}\ \text{C}\) een aantal "
                  r"\(n=\dfrac{|Q|}{e}\approx 3{,}0\cdot 10^{10}\) elektronen."),
            ("kader", r"<strong>Een neutraal voorwerp bevat niet géén lading.</strong> Het bevat er "
                      r"enorm veel, maar evenveel positieve als negatieve, dus \(Q=0\) in totaal. "
                      r"Neutraal is geen derde soort lading maar een evenwicht tussen de twee."),
        ]),
        dict(kop="Eén deeltje dat verhuist", blokken=[
            ("p", r"Als een voorwerp elektrisch geladen wordt, is het altijd "
                  r"<strong>het elektron dat verhuist</strong>, want dat zit het losst van de kern. "
                  r"De protonen en de neutronen blijven waar ze zijn. Daarom betekent "
                  r"<strong>negatief</strong> dat er <strong>elektronen bij gekomen</strong> zijn en "
                  r"<strong>positief</strong> dat er <strong>elektronen weggegaan</strong> zijn. Een "
                  r"voorwerp dat elektronen verloren heeft, draagt dus een "
                  r"<strong>positief</strong> teken."),
            ("p", r"Bij het laden door wrijving wordt er <strong>geen nieuwe lading gemaakt</strong>: "
                  r"ze verhuist alleen van het ene voorwerp naar het andere. Daarom geldt achteraf "
                  r"<strong>\(Q_{1}=-Q_{2}\)</strong>, en dus \(Q_{1}+Q_{2}=0\), net als voor het "
                  r"wrijven. Dat is het <strong>behoud van lading</strong>."),
            ("p", r"De <strong>tribo-elektrische reeks</strong> dient <strong>om te zien welke stof "
                  r"bij wrijving elektronen opneemt</strong> en welke ze afgeeft. Wrijf je een "
                  r"<strong>pvc-staaf met een wollen doek</strong>, dan "
                  r"<strong>wordt de staaf negatief en de doek positief</strong>: het pvc neemt "
                  r"elektronen van de wol op."),
        ]),
        dict(kop="Geleider of isolator", blokken=[
            ("p", r"Het verschil tussen een <strong>geleider</strong> en een "
                  r"<strong>isolator</strong> zit op atomaire schaal: "
                  r"<strong>een geleider heeft vrije elektronen, een isolator niet</strong>. Die "
                  r"<strong>vrije elektronen</strong> zijn de elektronen in een metaal "
                  r"<strong>die niet aan één atoom vastzitten</strong> maar door het hele stuk "
                  r"metaal kunnen bewegen. Een <strong>isolator</strong> is dus een stof "
                  r"<strong>waarin de elektronen niet vrij kunnen bewegen</strong>: daar "
                  r"<strong>blijven de elektronen bij hun eigen atoom zitten</strong> en "
                  r"<strong>blijft aangebrachte lading plaatselijk staan</strong>."),
            ("p", r"<strong>Koper</strong> en <strong>aluminium</strong> zijn goede geleiders; glas, "
                  r"rubber en plastic zijn isolatoren. Lading die je op een geleider aanbrengt, "
                  r"<strong>verspreidt zich meteen over het hele oppervlak</strong>, want de vrije "
                  r"elektronen duwen elkaar zo ver mogelijk uiteen."),
            ("p", r"Een <strong>isolator kan je wél elektrisch laden</strong>, bijvoorbeeld door "
                  r"wrijving: de lading blijft dan gewoon zitten op de plaats waar ze terechtkwam."),
        ]),
        dict(kop="De elektroscoop", blokken=[
            ("p", r"Een <strong>elektroscoop</strong> is het toestel "
                  r"<strong>met twee blaadjes dat aantoont dat een voorwerp geladen is</strong>. De "
                  r"<strong>blaadjes wijken uit elkaar</strong> omdat ze <strong>dezelfde lading "
                  r"dragen en elkaar daarom afstoten</strong>. Hoe groter \(|Q|\), hoe verder ze "
                  r"uit elkaar staan."),
            ("fig", svg.elektroscoop(),
             "Links een elektroscoop zonder lading, rechts dezelfde na het laden met een negatieve staaf."),
            ("p", r"Laad je een elektroscoop <strong>door contact</strong> met een negatieve staaf, "
                  r"dan <strong>blijven de blaadjes uit elkaar staan</strong>, ook nadat je de staaf "
                  r"weghaalt: de lading is echt op de elektroscoop overgegaan. Breng je de staaf "
                  r"alleen maar in de buurt, dan vallen de blaadjes weer samen zodra je ze weghaalt."),
        ]),
        dict(kop="Laden door contact", blokken=[
            ("p", r"Raak je een <strong>neutrale metalen bol aan met een negatief geladen "
                  r"staaf</strong>, dan <strong>lopen er elektronen naar de bol en wordt die "
                  r"negatief</strong>. <strong>Laden door contact geeft het voorwerp dus dezelfde "
                  r"soort lading</strong> als het geladen voorwerp."),
            ("p", r"Omdat lading behouden blijft, kan je zo'n contact ook gewoon narekenen. Raken "
                  r"<strong>twee even grote metalen bollen</strong> met \(Q_{1}=+12\ \text{nC}\) en "
                  r"\(Q_{2}=-4\ \text{nC}\) elkaar even aan, dan blijft de som "
                  r"\(Q_{1}+Q_{2}=+8\ \text{nC}\) en verdeelt die zich eerlijk: "
                  r"<strong>elke bol draagt daarna \(+4\ \text{nC}\)</strong>. Zijn de bollen niet "
                  r"even groot, dan krijgt de grootste een groter deel."),
            ("p", r"<strong>Aarden</strong> betekent een geleider met de aarde verbinden, zodat "
                  r"lading er onbeperkt naartoe kan weglopen of vandaan kan komen. Op een "
                  r"<strong>vochtige dag</strong> lopen de ladingen van een voorwerp trouwens "
                  r"<strong>vanzelf weg</strong>, want het water in de lucht geleidt."),
        ]),
        dict(kop="Influentie en polarisatie", blokken=[
            ("p", r"<strong>Influentie</strong> is het verschijnsel waarbij een geladen voorwerp "
                  r"<strong>de lading in een ander voorwerp verschuift zonder het aan te "
                  r"raken</strong>. Breng je een geleider <strong>in de buurt van een negatief "
                  r"geladen staaf</strong>, dan <strong>worden de vrije elektronen naar de verste "
                  r"kant geduwd</strong> en blijft de dichtste kant positief."),
            ("fig", svg.influentie(),
             "Een negatief geladen staaf vlak bij een metalen bol, zonder ze aan te raken."),
            ("p", r"Het voorwerp <strong>blijft in totaal even geladen als ervoor</strong>, dus "
                  r"\(Q=0\) blijft \(Q=0\): <strong>een voorwerp dat enkel door influentie "
                  r"beïnvloed werd, is daarna zelf niet geladen</strong>."),
            ("p", r"Het verschil tussen influentie <strong>bij een geleider en bij een "
                  r"isolator</strong>: <strong>bij een geleider verhuizen de elektronen door het "
                  r"hele voorwerp</strong>, bij een isolator <strong>draaien de moleculen zich een "
                  r"beetje</strong>. Dat verschuiven van de ladingen binnen de moleculen van een "
                  r"isolator heet <strong>polarisatie</strong>, en zo'n molecule met "
                  r"<strong>de ene kant lichtpositief en de andere lichtnegatief</strong> heet een "
                  r"<strong>dipool</strong>."),
            ("fig", svg.polarisatie(),
             "Dezelfde isolator, links op zichzelf en rechts met een negatief geladen staaf ernaast."),
            ("p", r"Daarom trekt een <strong>geladen staaf ook een neutraal stukje papier "
                  r"aan</strong>: <strong>de lading in het papier verschuift en de dichtste kant "
                  r"trekt</strong>. Omdat de kracht met \(\tfrac{1}{r^{2}}\) afneemt, weegt die "
                  r"dichte kant zwaarder door dan de afstoting van de verdere kant. Dezelfde "
                  r"verklaring geldt voor een <strong>opgeblazen ballon die na wrijven aan de muur "
                  r"kleeft</strong>: <strong>de ballon trekt de lading in de muur naar zich "
                  r"toe</strong>."),
            ("p", r"Met influentie kan je een geleider ook écht laden, <strong>zonder hem ooit aan "
                  r"te raken met het geladen voorwerp</strong>. Houd je een negatieve staaf bij een "
                  r"metalen bol, <strong>aard je de bol even en haal je dan de staaf weg</strong>, "
                  r"dan is de bol <strong>positief</strong>, want <strong>er liepen elektronen naar "
                  r"de aarde weg</strong>. Laden kan dus <strong>door wrijving</strong>, "
                  r"<strong>door contact met een geladen voorwerp</strong> en "
                  r"<strong>door influentie met een aarding erbij</strong>; verwarmen hoort daar "
                  r"niet bij."),
            ("p", tabel(["Manier van laden", "Raak je het aan?", "Welk teken krijgt het?"], [
                ["wrijving", "ja, met de andere stof", "hangt af van de tribo-elektrische reeks"],
                ["contact", "ja, met het geladen voorwerp", "hetzelfde als het geladen voorwerp"],
                ["influentie met aarding", "nee", "het tegengestelde van het geladen voorwerp"],
            ])),
        ]),
        dict(kop="Elektrostatica in toepassingen", blokken=[
            ("p", r"Een <strong>fotokopieertoestel</strong> en de <strong>poedercoating van "
                  r"metaal</strong> berusten op elektrostatica. In een kopieertoestel wordt "
                  r"<strong>de toner niet met een laagje lijm</strong> op het papier gebracht, maar "
                  r"<strong>door elektrische aantrekking</strong> vastgehouden en daarna "
                  r"ingebrand."),
            ("p", r"<strong>Poedercoating met geladen poeder werkt beter dan gewoon spuiten</strong> "
                  r"omdat <strong>het geladen poeder naar het hele werkstuk getrokken wordt</strong>, "
                  r"ook naar de achterkant en de hoeken. Zo blijft er veel minder verf in de lucht "
                  r"hangen."),
        ]),
    ],
    onthoud=[
        r"De grootheid is \(Q\), de eenheid de coulomb \(\text{C}\).",
        r"\(Q=n\cdot e\) met \(e=1{,}602\cdot 10^{-19}\ \text{C}\): lading komt in hele pakjes.",
        r"Een neutraal voorwerp heeft \(Q=0\), niet géén lading.",
        r"Er zijn twee soorten lading; alleen elektronen verhuizen.",
        r"Negatief is elektronen erbij, positief is elektronen eraf.",
        r"Wrijven maakt geen lading bij: achteraf is \(Q_{1}=-Q_{2}\).",
        r"Een geleider heeft vrije elektronen, een isolator niet.",
        r"Lading op een geleider gaat meteen naar het hele oppervlak.",
        r"Laden kan door wrijving, door contact en door influentie met aarding.",
        r"Influentie verschuift lading; het voorwerp blijft in totaal neutraal.",
        r"Bij een isolator draaien de moleculen: dat is polarisatie.",
    ],
)

# ───────────────────── 2. De wet van Coulomb en het elektrisch veld
BUNDELS["de-wet-van-coulomb-en-het-elektrisch-veld-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De wet van Coulomb en het elektrisch veld",
    onder="Hoe sterk twee ladingen aan elkaar trekken, en hoe je dat als een veld beschrijft.",
    secties=[
        dict(kop="Een kracht die op afstand werkt", blokken=[
            ("p", r"De elektrische kracht is een <strong>veldkracht</strong>: ze "
                  r"<strong>werkt op afstand, zonder dat er contact nodig is</strong>. Een "
                  r"<strong>puntlading</strong> is daarbij een lading <strong>die zo klein is dat je "
                  r"ze als één punt mag beschouwen</strong>."),
            ("p", r"De kracht tussen twee puntladingen heet de <strong>coulombkracht</strong>, naar "
                  r"de man die ze beschreef. <strong>Gelijksoortige ladingen stoten elkaar af</strong> "
                  r"en <strong>ongelijksoortige trekken elkaar aan</strong>. Twee ladingen die elkaar "
                  r"afstoten, <strong>hoeven niet allebei positief te zijn</strong>: twee negatieve "
                  r"ladingen stoten elkaar even goed af. Kracht wordt uitgedrukt in "
                  r"<strong>newton</strong>, met symbool \(\text{N}\)."),
            ("p", r"De kracht van lading A op lading B is <strong>even groot als die van B op "
                  r"A</strong>, maar tegengesteld van zin: \(\vec{F}_{AB}=-\vec{F}_{BA}\). Dat is "
                  r"de derde wet van Newton, ook hier, en ze geldt ook als de ene lading veel groter "
                  r"is dan de andere."),
            ("p", r"Een <strong>neutraal voorwerp</strong> wordt toch <strong>aangetrokken</strong> "
                  r"door een geladen <strong>staaf</strong> omdat "
                  r"<strong>de dichtste kant tegengesteld geladen is en dus harder trekt</strong>. De "
                  r"staaf verschuift de ladingen in het voorwerp; omdat \(F\sim\tfrac{1}{r^{2}}\), "
                  r"weegt de aantrekking van de nabije kant zwaarder dan de afstoting van de verre."),
        ]),
        dict(kop="De wet van Coulomb", blokken=[
            ("p", r"In de <strong>wet van Coulomb</strong> staan precies drie dingen: "
                  r"<strong>de grootte van \(q_{1}\) en \(q_{2}\)</strong> en "
                  r"<strong>de afstand \(r\) ertussen</strong>."),
            ("p", r"\[F = k\,\frac{|q_{1}\cdot q_{2}|}{r^{2}}\]"),
            ("p", r"De kracht is dus <strong>recht evenredig met het product van de twee "
                  r"ladingen</strong> en <strong>omgekeerd evenredig met \(r^{2}\)</strong>. Massa en "
                  r"temperatuur komen er niet in voor."),
            ("p", r"Een voorbeeld met getallen, met "
                  r"\(k=8{,}99\cdot 10^{9}\ \text{N}\,\text{m}^{2}\text{/C}^{2}\). Neem "
                  r"\(q_{1}=2{,}0\ \mu\text{C}\), \(q_{2}=3{,}0\ \mu\text{C}\) en "
                  r"\(r=0{,}30\ \text{m}\):"),
            ("p", r"\[F = 8{,}99\cdot 10^{9}\cdot\frac{2{,}0\cdot 10^{-6}\cdot 3{,}0\cdot 10^{-6}}"
                  r"{0{,}30^{2}} = \frac{5{,}39\cdot 10^{-2}}{0{,}090}\approx 0{,}60\ \text{N}\]"),
            ("p", r"Zet de ladingen altijd eerst in coulomb en vergeet \(r\) niet te kwadrateren. "
                  r"Dat zijn de twee fouten die het vaakst gemaakt worden."),
            ("p", r"Vaak moet je niet rekenen maar redeneren met verhoudingen:"),
            ("p", tabel(["Wat verandert er?", "Wat doet \\(F\\)?", "Waarom"], [
                [r"\(r\) wordt \(2r\)", r"\(\tfrac{1}{4}\) zo groot", r"\(F\sim\tfrac{1}{r^{2}}\)"],
                [r"\(q_{1}\) wordt \(3q_{1}\)", r"\(3\) keer zo groot", r"\(q_{1}\) staat in de teller"],
                [r"beide ladingen verdubbelen", r"\(4\) keer zo groot", r"\(2\cdot 2=4\)"],
                [r"\(r\) wordt \(\tfrac{r}{2}\)", r"\(4\) keer zo groot", r"halve afstand, kwadraat eronder"],
            ])),
            ("p", r"Trekken twee puntladingen elkaar dus aan met \(F=8{,}0\ \text{N}\) en verdubbel "
                  r"je \(r\), dan blijft er \(2{,}0\ \text{N}\) over. Stoten ze elkaar af met "
                  r"\(F=6{,}0\ \text{N}\) en vervang je \(q_{1}\) door \(3q_{1}\), dan wordt het "
                  r"\(18\ \text{N}\)."),
            ("p", r"De constante <strong>\(k\)</strong> <strong>hangt af van de stof tussen de twee "
                  r"ladingen</strong> en <strong>staat in de bijlage die je op het examen "
                  r"krijgt</strong>. Omdat water de ladingen afschermt, is <strong>de elektrische "
                  r"kracht tussen twee ladingen zwakker in water dan in lucht</strong>, niet sterker."),
            ("kader", r"De <strong>wet van Coulomb en de gravitatiewet hebben dezelfde vorm</strong>: "
                      r"\(F=k\,\dfrac{|q_{1}q_{2}|}{r^{2}}\) naast "
                      r"\(F=G\,\dfrac{m_{1}m_{2}}{r^{2}}\). Een product boven, een kwadraat van de "
                      r"afstand onder. Het verschil is dat de gravitatie altijd aantrekt en de "
                      r"coulombkracht ook kan afstoten."),
        ]),
        dict(kop="Meer dan één lading: optellen als vectoren", blokken=[
            ("p", r"De <strong>resulterende kracht op een lading die door twee andere ladingen "
                  r"beïnvloed wordt</strong>, vind je door <strong>de twee krachten op te tellen als "
                  r"vectoren</strong>: \(\vec{F}=\vec{F}_{1}+\vec{F}_{2}\). Daarom reken je bij twee "
                  r"ladingen in twee hoekpunten van een vierkant <strong>de kracht op een derde "
                  r"lading niet zomaar op door op te tellen</strong>: <strong>de twee krachten "
                  r"wijzen in een andere richting</strong>. Alleen als ze op één lijn liggen, "
                  r"volstaat optellen of aftrekken."),
            ("p", r"Staan <strong>drie gelijke positieve ladingen op één rechte lijn, op gelijke "
                  r"afstand van elkaar</strong>, dan voelt de middelste <strong>geen enkele "
                  r"kracht</strong>, want <strong>de twee krachten heffen elkaar op</strong>: ze zijn "
                  r"even groot en tegengesteld van zin, dus \(\vec{F}=\vec{0}\)."),
            ("p", r"De kracht van een <strong>geladen bol</strong> op een puntlading is het grootst "
                  r"<strong>vlak bij het oppervlak van de bol</strong>. Buiten de bol werkt ze alsof "
                  r"alle lading in het middelpunt zat, dus geldt \(F\sim\tfrac{1}{r^{2}}\) gewoon "
                  r"verder."),
        ]),
        dict(kop="De elektrische veldsterkte", blokken=[
            ("p", r"De <strong>elektrische veldsterkte in een punt</strong> is "
                  r"<strong>de kracht per eenheid van lading in dat punt</strong>. Ze krijgt het "
                  r"symbool <strong>\(E\)</strong>:"),
            ("p", r"\[E = \frac{F}{q}\qquad\text{in}\qquad \text{N/C} = \text{V/m}\]"),
            ("p", r"Daaruit volgt meteen \(F=E\cdot q\). Twee rekenvoorbeelden. Is "
                  r"\(E=200\ \text{N/C}\), dan werkt op \(q=3\ \text{mC}\) een kracht "
                  r"\(F=200\cdot 3\cdot 10^{-3}=0{,}6\ \text{N}\). Werkt op \(q=5\ \mu\text{C}\) een "
                  r"kracht \(F=0{,}1\ \text{N}\), dan is "
                  r"\(E=\dfrac{0{,}1}{5\cdot 10^{-6}}=2{,}0\cdot 10^{4}\ \text{N/C}\)."),
            ("p", r"Rond één puntlading kan je \(E\) ook rechtstreeks berekenen, door in de wet van "
                  r"Coulomb de proeflading weg te delen:"),
            ("p", r"\[E = k\,\frac{|q|}{r^{2}}\]"),
            ("p", r"Op \(r=0{,}10\ \text{m}\) van \(q=5{,}0\ \text{nC}\) geeft dat "
                  r"\(E=8{,}99\cdot 10^{9}\cdot\dfrac{5{,}0\cdot 10^{-9}}{0{,}10^{2}}"
                  r"\approx 4{,}5\cdot 10^{3}\ \text{N/C}\)."),
            ("p", r"Het veld <strong>van een puntlading neemt af met het kwadraat van de "
                  r"afstand</strong> en <strong>hangt niet af van de proeflading die je erin "
                  r"zet</strong>: het veld hoort bij de lading die het maakt. Zit een "
                  r"<strong>positieve lading in een punt waar \(\vec{E}\) naar rechts wijst</strong>, "
                  r"dan werkt de kracht ook <strong>naar rechts, in de zin van het veld</strong>; op "
                  r"een negatieve lading werkt ze er tegenin."),
        ]),
        dict(kop="Veldlijnen en veldpatronen", blokken=[
            ("p", r"Een elektrisch veld in een punt stel je in een tekening voor "
                  r"<strong>met een pijl die de zin en de grootte van het veld aangeeft</strong>, en "
                  r"het hele veld met <strong>veldlijnen</strong>. De afspraak over hun zin: "
                  r"<strong>ze lopen weg van de positieve en naar de negatieve lading</strong>. Dat "
                  r"is de zin van de kracht op een positieve proeflading."),
            ("p", r"Drie regels over veldlijnen. <strong>Ze vertrekken bij een positieve lading en "
                  r"eindigen bij een negatieve.</strong> <strong>Ze snijden elkaar nooit</strong>, "
                  r"want in één punt kan het veld maar één zin hebben. En "
                  r"<strong>hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het veld daar "
                  r"is</strong>."),
            ("fig", svg.veldpatronen(),
             "De patronen die je moet kunnen herkennen en tekenen."),
            ("p", r"Rond <strong>één positieve puntlading</strong> krijg je een <strong>radiaal "
                  r"veld</strong>: <strong>rechte lijnen die stervormig naar buiten wijzen</strong>. "
                  r"Rond een negatieve lading wijst hetzelfde patroon naar binnen. Tussen "
                  r"<strong>twee ongelijknamige puntladingen</strong> krijg je het "
                  r"<strong>dipoolveld</strong>, in gebogen bogen van plus naar min."),
            ("p", r"Tussen <strong>twee evenwijdige, tegengesteld geladen platen</strong> krijg je "
                  r"een <strong>homogeen veld</strong>: daar is <strong>\(E\) overal "
                  r"dezelfde</strong>, zijn de <strong>veldlijnen recht en parallel</strong> en lopen "
                  r"ze <strong>van de positieve naar de negatieve plaat</strong>. Omdat zo'n veld "
                  r"overal even sterk is, <strong>wordt \(E\) niet kleiner naarmate je dichter bij "
                  r"de positieve plaat komt</strong>, en is <strong>de kracht op een lading er overal "
                  r"even groot</strong>. Alleen aan de randen van de platen wijken de lijnen af."),
        ]),
        dict(kop="De kooi van Faraday", blokken=[
            ("p", r"<strong>Binnen in een geladen holle geleider is er geen veld</strong>: "
                  r"\(E=0\), <strong>want de ladingen heffen elkaar daar op</strong>. Alle lading "
                  r"zit op het buitenoppervlak. Een metalen omhulsel dat de binnenkant zo tegen een "
                  r"elektrisch veld afschermt, heet een <strong>kooi van Faraday</strong>."),
            ("p", r"Daarom is <strong>een auto een veilige plaats bij onweer</strong>: het metalen "
                  r"koetswerk leidt de lading rond de inzittenden naar de grond, en binnenin blijft "
                  r"\(E=0\). De rubberen banden hebben er weinig mee te maken. Hetzelfde principe "
                  r"zit in de afscherming van een gevoelige meetkabel."),
        ]),
    ],
    onthoud=[
        r"\(F = k\,\dfrac{|q_{1}q_{2}|}{r^{2}}\), met \(k\approx 8{,}99\cdot 10^{9}\ \text{N}\,\text{m}^{2}\text{/C}^{2}\) in lucht.",
        r"\(F\sim\tfrac{1}{r^{2}}\): dubbele afstand is vier keer minder kracht.",
        r"Zet de ladingen in coulomb en kwadrateer \(r\) voor je deelt.",
        r"Krachten van meerdere ladingen tel je op als vectoren.",
        r"\(E=\dfrac{F}{q}\), in \(\text{N/C}\), en dus \(F=E\cdot q\).",
        r"Rond één puntlading geldt \(E=k\,\dfrac{|q|}{r^{2}}\).",
        r"Veldlijnen lopen van plus naar min en snijden elkaar nooit.",
        r"Radiaal rond een puntlading, dipool tussen twee, homogeen tussen twee platen.",
        r"In een holle geleider is \(E=0\): de kooi van Faraday.",
    ],
)

# ───────────────────── 3. Elektrische energie, potentiaal en spanning
BUNDELS["elektrische-energie-potentiaal-en-spanning-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrische energie, potentiaal en spanning",
    onder="Van arbeid op een lading naar potentiaal, spanning en de elektronvolt.",
    secties=[
        dict(kop="Arbeid van de elektrische kracht", blokken=[
            ("p", r"Een elektrische kracht verricht arbeid <strong>als de lading verplaatst wordt in "
                  r"de zin van de kracht</strong>. Je rekent die arbeid zoals bij elke andere kracht:"),
            ("p", r"\[W = F\cdot d\]"),
            ("p", r"met \(d\) de verplaatsing in de zin van \(F\), \(W\) in joule \(\text{J}\). Wordt een "
                  r"lading van \(2\ \text{C}\) over \(0{,}50\ \text{m}\) verplaatst door een kracht van "
                  r"\(6{,}0\ \text{N}\) in dezelfde zin, dan is \(W = 6{,}0\cdot 0{,}50 = 3{,}0\ \text{J}\). "
                  r"Staat de verplaatsing loodrecht op de kracht, dan is \(W = 0\)."),
            ("p", r"Ken je de spanning in plaats van de kracht, dan reken je rechtstreeks met de lading:"),
            ("p", r"\[W = q\cdot U\]"),
            ("p", r"De arbeid van de elektrische kracht <strong>hangt niet af van de weg die de lading "
                  r"aflegt</strong>, alleen van begin- en eindpunt. De elektrische kracht is dus "
                  r"conservatief, net als de zwaartekracht. Daarom verandert \(E_{p}\) niet als je een "
                  r"lading loodrecht op de veldlijnen verplaatst."),
            ("p", r"Het verband met de beweging is de arbeid-energiestelling: \(W = \Delta E_{k}\), met "
                  r"\(E_{k} = \tfrac{1}{2}m\,v^{2}\) de <strong>kinetische energie</strong> of "
                  r"bewegingsenergie: de energie die een deeltje door zijn beweging heeft. Daarin is "
                  r"\(m\) de massa en \(v\) de snelheid."),
        ]),
        dict(kop="Potentiële energie in een veld", blokken=[
            ("p", r"De elektrische potentiële energie van een lading in een punt is"),
            ("p", r"\[E_{p} = q\cdot V\]"),
            ("p", r"Ze hangt dus af van <strong>twee</strong> dingen: van de lading \(q\) zelf én van de "
                  r"plaats, via de potentiaal \(V\). Je kan ze het best vergelijken met de hoogte-energie "
                  r"van een bal boven de grond: laat je los, dan wordt ze beweging."),
            ("p", r"Beweegt een positieve lading vanzelf van de positieve naar de negatieve plaat, dan "
                  r"daalt \(E_{p}\) en stijgt \(E_{k}\). Om een positieve lading naar de positieve plaat te "
                  r"duwen moet je zelf arbeid leveren. En \(E_{p}\) van een negatieve lading die naar de "
                  r"negatieve plaat beweegt <strong>stijgt</strong>, want die gaat tegen de kracht in."),
            ("p", r"Zonder wrijving blijft \(E_{k} + E_{p}\) behouden. Een elektron dat uit rust bij de "
                  r"negatieve plaat vertrekt, wordt dus versneld en komt met zijn maximale snelheid bij de "
                  r"andere plaat aan: alles wat \(E_{p}\) verliest, wordt beweging. Zo bereken je die "
                  r"snelheid:"),
            ("p", r"\[q\,U = \tfrac{1}{2}m\,v^{2} \qquad\Longrightarrow\qquad v = \sqrt{\dfrac{2q\,U}{m}}\]"),
            ("p", r"Je hebt daarvoor de lading \(q\), de spanning \(U\) en de massa \(m\) nodig, maar niet "
                  r"de afstand tussen de platen en niet de tijd. Een elektron dat uit rust "
                  r"\(500\ \text{V}\) doorloopt, met \(m = 9{,}11\cdot 10^{-31}\ \text{kg}\):"),
            ("p", r"\[v = \sqrt{\dfrac{2\cdot 1{,}602\cdot 10^{-19}\cdot 500}{9{,}11\cdot 10^{-31}}} "
                  r"\approx 1{,}3\cdot 10^{7}\ \text{m/s}\]"),
            ("p", r"Een proton krijgt bij dezelfde spanning dezelfde energie, want \(|q|\) is even groot. "
                  r"Het is wel ruim \(1800\) keer zwaarder, en door die veel grotere massa gaat het ruim "
                  r"\(42\) keer trager. Omgekeerd gaat een elektron door zijn veel kleinere massa bij "
                  r"dezelfde spanning dus veel sneller."),
        ]),
        dict(kop="Potentiaal en spanning", blokken=[
            ("p", r"De elektrische potentiaal in een punt is de potentiële energie per eenheid van lading:"),
            ("p", r"\[V = \dfrac{E_{p}}{q} \qquad\text{in}\qquad \text{V} = \text{J/C}\]"),
            ("p", r"Ze hoort bij het punt en niet bij de lading die je erin zet: zet je er een dubbel zo "
                  r"grote lading in, dan verdubbelt \(E_{p}\) maar niet \(V\). Rond één puntlading geldt"),
            ("p", r"\[V = k\,\dfrac{q}{r}\]"),
            ("p", r"met een \(r\) en geen \(r^{2}\): potentiaal gaat over energie, en energie is kracht maal "
                  r"afstand, dus valt er één \(r\) weg. Let ook op het teken: \(V\) draagt het teken van "
                  r"\(q\), terwijl \(E\) met \(|q|\) rekent."),
            ("p", tabel(["", "veldsterkte", "potentiaal"], [
                ["formule", r"\(E = k\dfrac{|q|}{r^{2}}\)", r"\(V = k\dfrac{q}{r}\)"],
                ["eenheid", r"\(\text{N/C} = \text{V/m}\)", r"\(\text{V} = \text{J/C}\)"],
                ["hoort bij", r"de kracht: \(F = E\,q\)", r"de energie: \(E_{p} = V\,q\)"],
                ["soort", "vector", "getal met teken"],
            ])),
            ("p", r"De spanning tussen twee punten is het verschil van hun potentialen:"),
            ("p", r"\[U_{AB} = V_{A} - V_{B}\]"),
            ("p", r"Een spanning hoort dus altijd bij twee punten, nooit bij één punt alleen. Is "
                  r"\(V_{A} = 120\ \text{V}\) en \(V_{B} = 45\ \text{V}\), dan is \(U_{AB} = 75\ \text{V}\). "
                  r"En \(U = 0\) betekent niet dat er geen lading is, enkel dat de twee punten even hoog "
                  r"liggen."),
            ("p", r"Twee rekenvoorbeelden. Verliest een lading van \(4{,}0\ \text{mC}\) onderweg "
                  r"\(0{,}80\ \text{J}\), dan is "
                  r"\(U = \dfrac{W}{q} = \dfrac{0{,}80}{4{,}0\cdot 10^{-3}} = 200\ \text{V}\). Zit een "
                  r"lading van \(5{,}0\ \text{mC}\) in een punt met \(V = 40\ \text{V}\), dan is "
                  r"\(E_{p} = 5{,}0\cdot 10^{-3}\cdot 40 = 0{,}20\ \text{J}\)."),
            ("p", r"Een positieve lading beweegt vanzelf van hoge naar lage potentiaal, zoals water van "
                  r"hoog naar laag. Een negatieve lading doet net het omgekeerde. Wat een spanningsbron "
                  r"in een kring in stand houdt, is precies dat potentiaalverschil tussen haar polen."),
        ]),
        dict(kop="Equipotentiaallijnen", blokken=[
            ("p", r"Een lijn waarop \(V\) overal dezelfde is, heet een <strong>equipotentiaallijn</strong> "
                  r"(in de ruimte: een equipotentiaaloppervlak). Ze staat altijd <strong>loodrecht op de "
                  r"veldlijnen</strong>."),
            ("fig", svg.equipotentiaal(), "De stippellijnen zijn de equipotentiaallijnen, de volle lijnen "
                                          "met een pijl de veldlijnen."),
            ("p", r"Een lading langs zo'n lijn verplaatsen kost geen arbeid: \(V\) verandert niet, dus "
                  r"\(E_{p}\) ook niet. Tussen twee punten op hetzelfde equipotentiaaloppervlak staat dan "
                  r"ook \(U = 0\)."),
            ("p", r"In een homogeen veld zijn de equipotentiaallijnen evenwijdige rechten en geldt"),
            ("p", r"\[U = E\cdot d \qquad\Longleftrightarrow\qquad E = \dfrac{U}{d}\]"),
            ("p", r"Staan twee platen \(2{,}0\ \text{cm}\) uit elkaar met \(E = 5000\ \text{N/C}\) ertussen, "
                  r"dan is \(U = 5000\cdot 0{,}020 = 100\ \text{V}\). Daaruit zie je meteen waarom "
                  r"\(\text{N/C}\) en \(\text{V/m}\) dezelfde eenheid zijn."),
        ]),
        dict(kop="De elektronvolt", blokken=[
            ("p", r"Voor deeltjes is de joule een onhandig grote eenheid. Daarom rekent men in "
                  r"<strong>elektronvolt</strong>: de energie die één elementaire lading wint bij één volt."),
            ("p", r"\[1\ \text{eV} = e\cdot 1\ \text{V} = 1{,}602\cdot 10^{-19}\ \text{J}\]"),
            ("p", r"Een elektron dat \(500\ \text{V}\) doorloopt wint dus precies \(500\ \text{eV}\), of "
                  r"\(8{,}0\cdot 10^{-17}\ \text{J}\). Van joule naar elektronvolt deel je door "
                  r"\(1{,}602\cdot 10^{-19}\); omgekeerd vermenigvuldig je."),
        ]),
    ],
    onthoud=[
        r"\(W = F\cdot d = q\cdot U\), en \(W = \Delta E_{k}\).",
        r"\(W\) hangt niet van de weg af, enkel van begin- en eindpunt.",
        r"\(E_{p} = q\cdot V\), en \(E_{k} + E_{p}\) blijft behouden.",
        r"\(q\,U = \tfrac{1}{2}m\,v^{2}\), dus \(v = \sqrt{\dfrac{2q\,U}{m}}\).",
        r"\(V = \dfrac{E_{p}}{q}\), in \(\text{V} = \text{J/C}\).",
        r"\(U_{AB} = V_{A} - V_{B}\): een spanning hoort bij twee punten.",
        r"\(V = k\dfrac{q}{r}\): één \(r\), en mét het teken van \(q\).",
        r"Equipotentiaallijnen staan loodrecht op de veldlijnen.",
        r"In een homogeen veld: \(U = E\cdot d\).",
        r"\(1\ \text{eV} = 1{,}602\cdot 10^{-19}\ \text{J}\).",
    ],
)

# ───────────────────── 4. Elektrodynamica: stroom, weerstand en schakelingen
BUNDELS["elektrodynamica-stroom-weerstand-en-schakelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrodynamica: stroom, weerstand en schakelingen",
    onder="Stroom, spanning en weerstand, en hoe je er serie en parallel mee rekent.",
    secties=[
        dict(kop="Stroomsterkte, spanning en weerstand", blokken=[
            ("p", r"De <strong>elektrische stroomsterkte</strong> is de lading die per seconde door "
                  r"een doorsnede gaat:"),
            ("p", r"\[I = \dfrac{\Delta q}{\Delta t} \qquad\text{in}\qquad 1\ \text{A} = 1\ \text{C/s}\]"),
            ("p", r"Het is dus niet de snelheid van één elektron en ook niet het aantal elektronen in "
                  r"de draad. De afgesproken zin van de stroom is die van de positieve lading, van plus "
                  r"naar min; de elektronen bewegen in werkelijkheid net de andere kant op. Die afspraak "
                  r"dateert van voor men wist welk deeltje er beweegt."),
            ("p", r"De <strong>wet van Ohm</strong> legt het verband tussen de drie grootheden:"),
            ("p", r"\[U = R\,I \qquad\Longleftrightarrow\qquad R = \dfrac{U}{I} \qquad\Longleftrightarrow"
                  r"\qquad I = \dfrac{U}{R}\]"),
            ("p", r"met \(R\) in ohm: \(1\ \Omega = 1\ \text{V/A}\). Staat er \(12\ \text{V}\) over een "
                  r"weerstand waar \(3{,}0\ \text{A}\) door loopt, dan is \(R = 4{,}0\ \Omega\). Loopt er "
                  r"\(0{,}40\ \text{A}\) door \(25\ \Omega\), dan staat er \(10\ \text{V}\) over. En een "
                  r"lamp van \(6{,}0\ \Omega\) op \(9{,}0\ \text{V}\) trekt \(1{,}5\ \text{A}\). Verdubbel "
                  r"je bij gelijke \(U\) de weerstand, dan wordt \(I\) half zo groot."),
            ("p", r"Let op wat \(R\) wél en niet bepaalt. De weerstand van een draad hangt af van de "
                  r"stof, van de lengte en van de doorsnede:"),
            ("p", r"\[R = \rho\,\dfrac{\ell}{A}\]"),
            ("p", r"en ook van de temperatuur. \(U\) en \(I\) bepalen \(R\) niet, ze volgen er juist uit. "
                  r"Een weerstand waarvoor \(U = R\,I\) met een vaste \(R\) opgaat, heet ohms; een "
                  r"gloeilamp is dat niet, want warm is haar \(R\) groter."),
            ("p", r"Een draad wordt warm omdat de elektronen tegen de atomen van het rooster botsen en "
                  r"daarbij energie afgeven. Dat is precies wat weerstand betekent. De elektronen zelf "
                  r"worden niet opgebruikt: er loopt er evenveel terug naar de bron als eruit vertrekt. "
                  r"Wat opgebruikt wordt, is energie."),
        ]),
        dict(kop="Het elektrisch schema", blokken=[
            ("p", r"Een <strong>elektrisch schema</strong> is een tekening van een stroomkring met "
                  r"symbolen in plaats van voorwerpen. Het toont welke onderdelen met elkaar verbonden "
                  r"zijn; de werkelijke plaats, de lengte of de kleur van de draden doet er niet toe."),
            ("fig", svg.kringsymbolen(), "De symbolen die in elk schema terugkomen."),
            ("p", r"Een <strong>ampèremeter</strong> zet je <strong>in serie</strong> met het onderdeel "
                  r"waarvan je de stroom meet, want die stroom moet er echt door. Daarom heeft hij een "
                  r"heel kleine eigen weerstand: anders verandert hij de stroom die hij wil meten. Een "
                  r"<strong>voltmeter</strong> zet je er juist <strong>parallel over</strong>, want die "
                  r"meet het verschil tussen twee punten, en hij heeft om dezelfde reden een heel grote "
                  r"weerstand."),
            ("p", r"Een open schakelaar onderbreekt de kring, en dan loopt er nergens stroom: de stroom "
                  r"heeft een gesloten weg nodig. En het verschil tussen gelijk- en wisselstroom: "
                  r"<strong>gelijkstroom loopt altijd in dezelfde zin</strong>. Een batterij levert "
                  r"gelijkstroom, het stopcontact wisselstroom, waarbij de zin voortdurend omkeert."),
        ]),
        dict(kop="Serie en parallel", blokken=[
            ("p", r"De ene weerstand die je in de plaats van een hele schakeling mag denken, heet de "
                  r"<strong>vervangingsweerstand</strong> \(R_{v}\) (ook vervangweerstand of "
                  r"substitutieweerstand). Ze geeft bij dezelfde spanning dezelfde totale stroom, en "
                  r"daarmee reken je een schakeling stap voor stap uit."),
            ("p", r"In een <strong>serieschakeling</strong> is er maar één weg. De stroom is dus in elk "
                  r"onderdeel even groot, de deelspanningen tellen samen tot de bronspanning (nooit meer "
                  r"dan dat), en de weerstanden tellen gewoon op:"),
            ("p", r"\[R_{v} = R_{1} + R_{2} + R_{3}\]"),
            ("p", r"In een <strong>parallelschakeling</strong> heeft elke tak zijn eigen weg naar de "
                  r"bron. Over elke tak staat dezelfde spanning, de deelstromen van de takken tellen "
                  r"samen tot de hoofdstroom, en door de kleinste weerstand loopt de grootste stroom:"),
            ("p", r"\[\dfrac{1}{R_{v}} = \dfrac{1}{R_{1}} + \dfrac{1}{R_{2}} \qquad\text{of, voor twee "
                  r"weerstanden,}\qquad R_{v} = \dfrac{R_{1}R_{2}}{R_{1}+R_{2}}\]"),
            ("fig", svg.schakelingen(), "Dezelfde kringen als in de rekenvoorbeelden hieronder."),
            ("p", r"Twee weerstanden van \(4{,}0\ \Omega\) en \(6{,}0\ \Omega\) geven in serie "
                  r"\(10\ \Omega\) en parallel \(\dfrac{24}{10} = 2{,}4\ \Omega\). In serie ligt "
                  r"\(R_{v}\) dus altijd boven de grootste, parallel altijd onder de kleinste. Bij "
                  r"\(n\) gelijke weerstanden parallel is \(R_{v} = \dfrac{R}{n}\): twee van "
                  r"\(10\ \Omega\) geven \(5{,}0\ \Omega\)."),
            ("p", r"Staan \(2{,}0\ \Omega\), \(3{,}0\ \Omega\) en \(5{,}0\ \Omega\) in serie op "
                  r"\(20\ \text{V}\), dan is \(R_{v} = 10\ \Omega\) en \(I = 2{,}0\ \text{A}\) door alle "
                  r"drie. Over de \(3{,}0\ \Omega\) staat dan \(3{,}0 \cdot 2{,}0 = 6{,}0\ \text{V}\), en "
                  r"de drie deelspanningen \(4{,}0 + 6{,}0 + 10 = 20\ \text{V}\) kloppen weer met de bron."),
            ("p", r"Staan \(6{,}0\ \Omega\) en \(12\ \Omega\) parallel op \(24\ \text{V}\), dan loopt er "
                  r"\(4{,}0\ \text{A}\) door de eerste en \(2{,}0\ \text{A}\) door de tweede, dus levert "
                  r"de bron \(6{,}0\ \text{A}\). Dat klopt met \(R_{v} = 4{,}0\ \Omega\)."),
            ("p", r"Omdat elke lamp haar eigen weg naar de bron heeft, blijven de andere lampen branden "
                  r"als er in een parallelschakeling één lamp stukgaat. Staan de lampen in serie "
                  r"geschakeld, dan dooft één kapotte lamp de hele reeks, want dan is de kring "
                  r"onderbroken. Daarom staan de lampen in een huis parallel."),
        ]),
        dict(kop="Gemengde schakelingen", blokken=[
            ("p", r"Bij een gemengde schakeling werk je <strong>van binnen naar buiten</strong>: eerst "
                  r"het parallelle stuk, dan de serie. Je vervangt het parallelle stuk door één "
                  r"weerstand en houdt een gewone serieschakeling over."),
            ("p", r"Neem \(10\ \Omega\) in serie met twee parallelle weerstanden van elk \(20\ \Omega\), "
                  r"op \(40\ \text{V}\). In drie stappen:"),
            ("p", r"\[R_{\text{par}} = \dfrac{20}{2} = 10\ \Omega \qquad R_{v} = 10 + 10 = 20\ \Omega "
                  r"\qquad I = \dfrac{40}{20} = 2{,}0\ \text{A}\]"),
            ("p", r"Die hele \(2{,}0\ \text{A}\) gaat door de weerstand van \(10\ \Omega\), waarover dus "
                  r"\(10 \cdot 2{,}0 = 20\ \text{V}\) staat. Van de \(40\ \text{V}\) blijft er dan "
                  r"\(20\ \text{V}\) over voor het parallelle stuk, en door elke tak van \(20\ \Omega\) "
                  r"loopt \(\dfrac{20}{20} = 1{,}0\ \text{A}\). Samen weer \(2{,}0\ \text{A}\): dat is "
                  r"je controle."),
        ]),
        dict(kop="Vermogen en energie", blokken=[
            ("p", r"Het <strong>vermogen</strong> dat een toestel omzet, is"),
            ("p", r"\[P = U\,I = R\,I^{2} = \dfrac{U^{2}}{R} \qquad\text{in watt:}\qquad "
                  r"1\ \text{W} = 1\ \text{J/s}\]"),
            ("p", r"en de energie die het over een tijd \(t\) verbruikt is \(E = P\,t\), in joule of in "
                  r"kilowattuur (\(1\ \text{kWh} = 3{,}6\cdot 10^{6}\ \text{J}\)). Dat \(P = R\,I^{2}\) "
                  r"verklaart waarom men elektriciteit over grote afstand bij een heel hoge spanning "
                  r"vervoert: bij een hoge \(U\) volstaat een kleine \(I\) voor hetzelfde vermogen, en de "
                  r"verliezen in de kabels gaan met het kwadraat van die stroom."),
        ]),
    ],
    onthoud=[
        r"\(I = \dfrac{\Delta q}{\Delta t}\), in \(\text{A} = \text{C/s}\).",
        r"Wet van Ohm: \(U = R\,I\), met \(1\ \Omega = 1\ \text{V/A}\).",
        r"\(R = \rho\dfrac{\ell}{A}\): stof, lengte en doorsnede, niet \(U\) of \(I\).",
        r"Een ampèremeter staat in serie, een voltmeter ernaast.",
        r"Serie: dezelfde \(I\), spanningen tellen op, \(R_{v} = R_{1}+R_{2}\).",
        r"Parallel: dezelfde \(U\), stromen tellen op, \(\dfrac{1}{R_{v}} = \dfrac{1}{R_{1}}+\dfrac{1}{R_{2}}\).",
        r"\(n\) gelijke weerstanden parallel geven \(\dfrac{R}{n}\).",
        r"Gemengd: eerst het parallelle stuk, dan de serie.",
        r"\(P = U\,I = R\,I^{2} = \dfrac{U^{2}}{R}\), in watt.",
    ],
)

# ───────────────────── 5. Magneten en het magnetisch veld
BUNDELS["magneten-en-het-magnetisch-veld-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Magneten en het magnetisch veld",
    onder="Weissgebieden, polen, veldlijnen en het veld van een stroom.",
    secties=[
        dict(kop="Waar magnetisme vandaan komt", blokken=[
            ("p", "<strong>IJzer, nikkel en cobalt</strong> zijn de <strong>ferromagnetische "
                  "stoffen</strong>: zij kunnen zelf magnetisch worden. Een "
                  "<strong>magneet trekt dus niet elk metaal aan</strong>; aluminium en koper laat "
                  "hij koud."),
            ("p", "Het magnetisme van één atoom komt <strong>van de kringstroom en de spin van zijn "
                  "elektronen</strong>. In een ferromagnetische stof staan die elementaire "
                  "magneetjes in kleine gebiedjes dezelfde kant op; die gebiedjes heten "
                  "<strong>weissgebieden</strong>."),
            ("p", "In een <strong>ongemagnetiseerd stuk ijzer</strong> "
                  "<strong>wijzen de weissgebieden alle kanten op</strong> en "
                  "<strong>heffen de velden van de gebiedjes elkaar op</strong>. Wordt het stuk "
                  "ijzer <strong>gemagnetiseerd</strong>, dan "
                  "<strong>richten de weissgebieden zich in dezelfde zin</strong>."),
            ("p", "Een permanente magneet kan je <strong>demagnetiseren</strong> "
                  "<strong>door hem sterk op te warmen</strong> of <strong>door er hard op te "
                  "slaan</strong>. Een <strong>magneet die lang in het vuur ligt, stopt met "
                  "werken</strong> omdat <strong>de warmte de weissgebieden weer door elkaar "
                  "schudt</strong>. Boven een bepaalde temperatuur, de "
                  "<strong>curietemperatuur</strong>, houdt elke ordening op; voor ijzer ligt die "
                  "rond \\(770\\ ^{\\circ}\\text{C}\\)."),
        ]),
        dict(kop="Twee polen, altijd", blokken=[
            ("p", "Elke magneet heeft een <strong>noordpool en een zuidpool</strong>. "
                  "<strong>Breek je een staafmagneet in twee</strong>, dan krijg je "
                  "<strong>twee kleinere magneten, elk met twee polen</strong>: een "
                  "<strong>losse magnetische noordpool kan je niet maken</strong>. Een staafmagneet "
                  "is het sterkst <strong>aan de twee uiteinden</strong>."),
            ("p", "Schuif je <strong>twee magneten met hun noordpolen naar elkaar toe</strong>, dan "
                  "<strong>stoten ze elkaar af</strong>. Gelijknamige polen stoten af, ongelijknamige "
                  "trekken aan. Een <strong>magnetische kracht werkt wel door een blad papier "
                  "heen</strong>, en zelfs door een dunne plaat hout of plastic."),
            ("p", "De aarde is zelf een magneet: de <strong>magnetische zuidpool van de aarde ligt "
                  "in de buurt van de geografische noordpool</strong>. Daarom "
                  "<strong>wijst de noordpool van een kompasnaald naar het noorden</strong>: "
                  "<strong>daar ligt de magnetische zuidpool van de aarde</strong>, en "
                  "ongelijknamige polen trekken elkaar aan. Het veld van de aarde is zwak: "
                  "ongeveer \\(5\\cdot 10^{-5}\\ \\text{T}\\)."),
        ]),
        dict(kop="Magnetische influentie", blokken=[
            ("p", "<strong>Magnetische influentie</strong> is het verschijnsel waarbij een magneet "
                  "<strong>een stuk ijzer tijdelijk zelf magnetisch maakt</strong>. Daarom "
                  "<strong>blijft een paperclip aan een magneet hangen, ook al is hij zelf geen "
                  "magneet</strong>: <strong>de magneet richt tijdelijk de weissgebieden in de "
                  "clip</strong>."),
            ("p", "Om dezelfde reden <strong>hangen meerdere paperclips onder elkaar aan één "
                  "magneet</strong>: <strong>elke clip wordt zelf tijdelijk een magneetje</strong>. "
                  "Haal je de magneet weg, dan vallen ze los."),
        ]),
        dict(kop="Veldlijnen van een magneet", blokken=[
            ("p", "De afspraak over de zin van de magnetische veldlijnen <strong>buiten een "
                  "magneet</strong>: <strong>ze lopen van de noordpool naar de zuidpool</strong>. "
                  "Binnen de magneet lopen ze terug, dus "
                  "<strong>heeft een magnetische veldlijn geen begin en geen einde</strong>, anders "
                  "dan een elektrische veldlijn: ze is altijd gesloten."),
            ("p", "<strong>Hoe dichter de magnetische veldlijnen bij elkaar liggen, hoe sterker het "
                  "veld.</strong> Een <strong>kompasnaald gaat met haar noordpool mee met de zin van "
                  "de veldlijn staan</strong>, dus niet ertegenin."),
        ]),
        dict(kop="De grootte van B", blokken=[
            ("p", "Het veld zelf heeft een symbool en een eenheid. De "
                  "<strong>magnetische inductie</strong> of <strong>magnetische veldsterkte</strong> "
                  "noteren we \\(B\\), en ze staat in <strong>tesla</strong>, \\(\\text{T}\\). Eén "
                  "tesla is veel: \\[1\\ \\text{T} = 1\\ \\dfrac{\\text{N}}{\\text{A}\\cdot "
                  "\\text{m}} = 1\\ \\dfrac{\\text{V}\\cdot \\text{s}}{\\text{m}^{2}}\\] "
                  "Een koelkastmagneet zit rond \\(5\\ \\text{mT}\\), een sterke labomagneet rond "
                  "\\(1\\ \\text{T}\\), een MRI-toestel op \\(1{,}5\\) tot \\(3\\ \\text{T}\\). "
                  "Omdat \\(1\\ \\text{T}\\) zo groot is, wordt ook de oudere eenheid gauss nog "
                  "gebruikt: \\(1\\ \\text{T} = 10^{4}\\ \\text{G}\\)."),
            ("p", "Twee patronen om te kennen: rond een gewone staafmagneet krijg je een "
                  "<strong>dipoolveld</strong>, en tussen de twee benen van een "
                  "<strong>hoefijzermagneet</strong> een <strong>homogeen veld</strong>, waar "
                  "\\(B\\) overal dezelfde grootte en dezelfde richting heeft."),
            ("fig", svg.magneetvelden(),
             "De vier patronen die je moet kunnen tekenen. Buiten een magneet lopen de lijnen "
             "van noord naar zuid; rond een rechte draad zijn het cirkels, en in een spoel "
             "liggen ze binnenin bijna recht naast elkaar."),
        ]),
        dict(kop="Het veld van een stroom", blokken=[
            ("p", "Rond een <strong>rechte stroomvoerende draad</strong> ziet het magnetisch veld "
                  "eruit <strong>als cirkels rond de draad heen</strong>. De "
                  "<strong>rechterhandregel</strong> dient <strong>om de zin van die veldlijnen rond "
                  "de draad te vinden</strong>: duim in de stroomzin, de vingers krullen mee met het "
                  "veld. Het is de regel waarmee je <strong>met je rechterhand de zin van een "
                  "magnetisch veld vindt</strong>. In sommige boeken heet diezelfde regel de "
                  "<strong>kurkentrekkerregel</strong>: draai een kurkentrekker in de stroomzin "
                  "en hij draait mee met de veldlijnen."),
            ("p", "Voor zo'n rechte draad kan je \\(B\\) ook uitrekenen. Op een afstand \\(r\\) van "
                  "een draad waar een stroom \\(I\\) door loopt, geldt "
                  "\\[B = \\dfrac{\\mu_{0}\\,I}{2\\pi r}\\] "
                  "met \\(\\mu_{0} = 4\\pi \\cdot 10^{-7}\\ \\text{T}\\cdot\\text{m/A}\\), de "
                  "magnetische permeabiliteit van het vacuüm."),
            ("p", "Uit die formule lees je de twee verhoudingen af. "
                  "<strong>Verdubbel je de stroom</strong> door een rechte draad, dan "
                  "<strong>wordt het veld twee keer zo sterk</strong>, want \\(B\\) is "
                  "rechtstreeks evenredig met \\(I\\). Ga je "
                  "<strong>twee keer zo ver staan</strong>, dan wordt het "
                  "<strong>half zo sterk</strong>: bij een rechte draad gaat het met één keer de "
                  "afstand, dus \\(B \\sim \\dfrac{1}{r}\\) en niet met het kwadraat zoals bij het "
                  "elektrisch veld van een puntlading."),
            ("p", "In het midden van een <strong>stroomvoerende cirkelvormige lus</strong> "
                  "<strong>staat het veld loodrecht op het vlak van de lus</strong>. De "
                  "<strong>noordpool van een stroomvoerende spoel</strong> vind je "
                  "<strong>met de rechterhand: de vingers volgen de stroom, de duim wijst naar "
                  "noord</strong>."),
            ("p", "Het veld <strong>binnen in een lange stroomvoerende spoel is nagenoeg "
                  "homogeen</strong>, en het hangt af <strong>van het aantal windingen per "
                  "meter</strong> en <strong>van de stroom die erdoor loopt</strong>: "
                  "\\[B = \\mu_{0}\\,\\dfrac{N}{\\ell}\\,I\\] "
                  "met \\(N\\) het aantal windingen en \\(\\ell\\) de lengte van de spoel. Let op "
                  "het verschil met de rechte draad: hier staat geen \\(r\\) in, dus het veld is "
                  "binnenin overal ongeveer even groot. Zet je "
                  "<strong>twee stroomvoerende spoelen met hun noordpolen naar elkaar toe</strong>, "
                  "dan <strong>stoten ze elkaar af, net als twee gewone magneten</strong>."),
            ("kader", "De twee formules naast elkaar: bij een rechte draad is "
                      "\\(B = \\dfrac{\\mu_{0}I}{2\\pi r}\\), dus hoe verder, hoe zwakker. Bij een "
                      "lange spoel is \\(B = \\mu_{0}\\dfrac{N}{\\ell}I\\), dus hoe dichter de "
                      "windingen op elkaar, hoe sterker. In beide staat \\(\\mu_{0}\\) en in beide "
                      "is \\(B\\) evenredig met \\(I\\)."),
        ]),
        dict(kop="De elektromagneet", blokken=[
            ("p", "Het verschil tussen een <strong>permanente magneet en een elektromagneet</strong>: "
                  "<strong>een elektromagneet werkt alleen als er stroom loopt</strong>. Een "
                  "<strong>ijzeren kern</strong> in een elektromagneet dient "
                  "<strong>om het magnetisch veld veel sterker te maken</strong>, want de "
                  "weissgebieden in het ijzer richten zich mee. In een formule vervang je dan "
                  "\\(\\mu_{0}\\) door \\(\\mu = \\mu_{r}\\,\\mu_{0}\\), en voor zacht ijzer is die "
                  "relatieve permeabiliteit \\(\\mu_{r}\\) enkele honderden tot enkele duizenden."),
            ("p", "Een <strong>schrootkraan</strong> en een <strong>elektrische deurbel</strong> "
                  "berusten op een elektromagneet. Bij de schrootkraan geldt: "
                  "<strong>de stroom aan betekent oppakken, de stroom af betekent lossen</strong>. "
                  "Met een permanente magneet zou je het schroot nooit meer kwijtraken."),
        ]),
    ],
    onthoud=[
        "IJzer, nikkel en cobalt zijn ferromagnetisch.",
        "Magnetiseren is de weissgebieden gelijk richten; warmte of slaan wist het.",
        "Elke magneet heeft twee polen; een losse pool bestaat niet.",
        "Veldlijnen lopen buiten van noord naar zuid en zijn gesloten.",
        r"B is de magnetische inductie, in tesla: \(1\ \text{T} = 1\ \text{N/(A}\cdot\text{m)}\).",
        r"Rechte draad: \(B = \dfrac{\mu_{0}I}{2\pi r}\), dus \(B \sim \dfrac{1}{r}\); rechterhandregel.",
        r"Lange spoel: \(B = \mu_{0}\dfrac{N}{\ell}I\), binnenin homogeen.",
        r"\(\mu_{0} = 4\pi\cdot 10^{-7}\ \text{T}\cdot\text{m/A}\).",
        "Een elektromagneet werkt alleen met stroom; een ijzeren kern versterkt.",
    ],
)

# ───────────────────── 6. De magnetische kracht op een stroom en op een lading
BUNDELS["de-magnetische-kracht-op-een-stroom-en-op-een-lading-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De magnetische kracht op een stroom en op een lading",
    onder="De laplacekracht, de lorentzkracht en wat je er in motoren en versnellers mee doet.",
    secties=[
        dict(kop="De laplacekracht op een draad", blokken=[
            ("p", "De kracht op een stroomvoerende geleider in een magnetisch veld heet de "
                  "<strong>laplacekracht</strong>. Ze staat "
                  "<strong>loodrecht op de draad en loodrecht op het veld</strong>, dus loodrecht op "
                  "het vlak van die twee. In formule: "
                  "\\[F = B\\,I\\,\\ell\\,\\sin\\alpha\\] "
                  "met \\(B\\) in tesla, \\(I\\) in ampère, \\(\\ell\\) de lengte van de draad "
                  "in het veld in meter, en \\(\\alpha\\) de hoek tussen de draad en de veldlijnen."),
            ("p", "Uit die ene formule lees je alles af. De kracht hangt af "
                  "<strong>van de stroomsterkte door de draad</strong>, "
                  "<strong>van de sterkte van het magnetisch veld</strong> en "
                  "<strong>van de lengte van de draad in het veld</strong>. Ze is dus "
                  "<strong>recht evenredig met de stroomsterkte</strong> en "
                  "<strong>recht evenredig met de magnetische inductie</strong>. Van de eigen "
                  "weerstand van de draad hangt ze niet af: die staat niet in de formule en telt "
                  "enkel onrechtstreeks mee, omdat ze de stroom bepaalt."),
            ("p", "Ook de hoek telt mee, via \\(\\sin\\alpha\\). De kracht is "
                  "<strong>het grootst als de draad loodrecht op de veldlijnen staat</strong>, want "
                  "\\(\\sin 90^{\\circ} = 1\\), en een <strong>draad die evenwijdig met de "
                  "veldlijnen ligt, voelt geen magnetische kracht</strong>, want "
                  "\\(\\sin 0^{\\circ} = 0\\). Staat een draad "
                  "<strong>onder 30 graden met de veldlijnen</strong> in plaats van loodrecht, dan "
                  "<strong>wordt de kracht kleiner, want de sinus van 30 graden is maar een "
                  "half</strong>: er blijft \\(0{,}50\\,B\\,I\\,\\ell\\) over."),
            ("p", "Rekenen: een draad van \\(\\ell = 0{,}50\\ \\text{m}\\) die loodrecht in een "
                  "veld van \\(B = 0{,}20\\ \\text{T}\\) ligt en \\(I = 3{,}0\\ \\text{A}\\) voert, "
                  "voelt \\[F = 0{,}20\\cdot 3{,}0\\cdot 0{,}50 = 0{,}30\\ \\text{N}\\] "
                  "De zin van die kracht vind je "
                  "<strong>met je rechterhand: vingers in de stroomzin, veld in de handpalm, duim "
                  "geeft de kracht</strong>."),
            ("fig", svg.magneetkracht(),
             "Links: het veld gaat het blad in, de stroom naar rechts, dus staat de kracht "
             "omhoog. Rechts: twee draden met dezelfde stroomzin trekken elkaar aan. Onderaan: "
             "het veld komt uit het blad, dus draait een positieve lading met de wijzers mee en "
             "wijst de kracht altijd naar het middelpunt."),
            ("p", "Twee evenwijdige draden werken ook op elkaar, want elke draad ligt in het veld "
                  "van de andere. Voeren ze "
                  "<strong>stroom in dezelfde zin</strong>, dan "
                  "<strong>trekken ze elkaar aan</strong>; voeren ze "
                  "<strong>stroom in tegengestelde zin</strong>, dan "
                  "<strong>stoten ze elkaar af</strong>. Per meter draad geldt "
                  "\\[\\dfrac{F}{\\ell} = \\dfrac{\\mu_{0}\\,I_{1}\\,I_{2}}{2\\pi d}\\] "
                  "met \\(d\\) de afstand tussen de twee draden. Omdat \\(d\\) in de noemer staat, "
                  "<strong>wordt die kracht groter als ze dichter bij elkaar liggen</strong>, niet "
                  "kleiner."),
        ]),
        dict(kop="Motor en luidspreker", blokken=[
            ("p", "Een <strong>luidspreker</strong> werkt doordat "
                  "<strong>de wisselstroom in een spoel het membraan heen en weer duwt</strong>. De "
                  "kracht die dat doet, is de <strong>laplacekracht</strong>, en omdat de stroom "
                  "van zin wisselt, wisselt ook de kracht van zin."),
            ("p", "De <strong>spoel van een gelijkstroommotor draait</strong> omdat "
                  "<strong>de krachten op de twee zijden in tegengestelde zin wijzen</strong>: in de "
                  "ene zijde loopt de stroom de ene kant op, in de andere de andere kant. Met "
                  "\\(N\\) windingen en een spoel met oppervlakte \\(A\\) is het koppel "
                  "\\(M = N\\,B\\,I\\,A\\,\\sin\\alpha\\). De "
                  "<strong>collector</strong> dient <strong>om de stroom elke halve omwenteling om "
                  "te keren</strong>, zodat het koppel altijd dezelfde kant op blijft duwen."),
        ]),
        dict(kop="De lorentzkracht op een lading", blokken=[
            ("p", "De kracht op één bewegende lading in een magnetisch veld heet de "
                  "<strong>lorentzkracht</strong>: "
                  "\\[F = q\\,v\\,B\\,\\sin\\alpha\\] "
                  "met \\(q\\) de lading in coulomb, \\(v\\) haar snelheid in meter per seconde en "
                  "\\(\\alpha\\) de hoek tussen de snelheid en het veld. Het is dezelfde kracht als "
                  "de laplacekracht, maar dan op één deeltje in plaats van op een hele draad vol "
                  "bewegende ladingen."),
            ("p", "Ze hangt dus af <strong>van de grootte van de lading</strong> en "
                  "<strong>van de snelheid van de lading</strong>, en natuurlijk ook van het veld en "
                  "van de hoek ermee. De massa staat er níet in. Een <strong>stilstaande lading in "
                  "een magnetisch veld voelt geen magnetische kracht</strong>, want \\(v = 0\\). Een "
                  "lading die <strong>precies evenwijdig met de veldlijnen</strong> beweegt, voelt "
                  "<strong>geen enkele kracht, want de hoek met het veld is nul</strong> en "
                  "\\(\\sin 0^{\\circ} = 0\\)."),
            ("p", "Rekenen: een lading van \\(q = 2{,}0\\ \\text{mC}\\) die met "
                  "\\(v = 500\\ \\text{m/s}\\) loodrecht door een veld van "
                  "\\(B = 0{,}40\\ \\text{T}\\) beweegt, voelt "
                  "\\[F = 2{,}0\\cdot 10^{-3}\\cdot 500\\cdot 0{,}40 = 0{,}40\\ \\text{N}\\] "
                  "Let op de omzetting van millicoulomb naar coulomb."),
            ("p", "De <strong>magnetische kracht op een lading staat loodrecht op haar "
                  "snelheid</strong>. Daardoor is \\(W = F\\,d\\,\\cos 90^{\\circ} = 0\\): ze "
                  "verricht geen arbeid, en dus "
                  "<strong>kan een magnetisch veld de snelheid van een lading niet groter "
                  "maken</strong>. Het buigt haar alleen af. Daarin verschilt ze van een elektrisch "
                  "veld, dat wel arbeid levert."),
        ]),
        dict(kop="De cirkelbaan", blokken=[
            ("p", "Een lading die <strong>loodrecht een homogeen magnetisch veld "
                  "binnenkomt</strong>, volgt een <strong>cirkelbaan</strong>, want de kracht blijft "
                  "loodrecht op de snelheid staan en werkt dus als middelpuntzoekende kracht. Stel "
                  "de twee aan elkaar gelijk: "
                  "\\[q\\,v\\,B = \\dfrac{m\\,v^{2}}{r} \\quad\\Longrightarrow\\quad "
                  "r = \\dfrac{m\\,v}{q\\,B}\\] "
                  "Een <strong>deeltje dat schuin binnenkomt, gaat niet rechtdoor</strong>: het stuk "
                  "van de snelheid langs het veld loopt door, het stuk dwars erop maakt een cirkel, "
                  "en samen geeft dat een schroeflijn."),
            ("p", "In \\(r = \\dfrac{m\\,v}{q\\,B}\\) lees je af waar de straal van afhangt: van "
                  "<strong>de massa van het deeltje</strong>, <strong>de snelheid van het "
                  "deeltje</strong> en <strong>de sterkte van het magnetisch veld</strong>, en ook "
                  "van zijn lading. <strong>Verdubbel je het magnetisch veld</strong>, dan "
                  "<strong>wordt de straal half zo groot</strong>, want \\(B\\) staat in de noemer. "
                  "Een sneller deeltje maakt een ruimere bocht, want \\(v\\) staat in de teller."),
            ("p", "Maken <strong>twee deeltjes met dezelfde lading en snelheid</strong> in hetzelfde "
                  "veld een bocht met een andere straal, dan verschilt <strong>hun massa</strong>. "
                  "Vliegen een <strong>positieve en een negatieve lading</strong> met dezelfde "
                  "snelheid het veld binnen, dan <strong>buigen ze naar tegengestelde kanten "
                  "af</strong>: het teken van \\(q\\) keert de zin van de kracht om, maar de grootte "
                  "van \\(r\\) blijft gelijk."),
            ("kader", "De omlooptijd van zo'n cirkelbaan is merkwaardig: uit "
                      "\\(T = \\dfrac{2\\pi r}{v}\\) en \\(r = \\dfrac{m v}{q B}\\) volgt "
                      "\\(T = \\dfrac{2\\pi m}{q\\,B}\\). Daar staat geen \\(v\\) meer in. Een "
                      "sneller deeltje maakt een ruimere bocht, maar doet er even lang over. "
                      "Net daarom werkt een cyclotron: de duwtjes mogen altijd op hetzelfde ritme "
                      "komen."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("p", "De <strong>massaspectrometer</strong> is het toestel dat "
                  "<strong>ionen op hun massa scheidt met een magnetisch veld</strong>. Je weet "
                  "<strong>aan de straal van de bocht die het deeltje beschrijft</strong> of het "
                  "zwaar of licht is: een zwaar deeltje maakt een ruimere bocht, want "
                  "\\(r \\sim m\\). Uit de gemeten straal haal je de massa terug: "
                  "\\(m = \\dfrac{q\\,B\\,r}{v}\\)."),
            ("p", "Een <strong>cyclotron</strong> dient <strong>om geladen deeltjes tot hoge "
                  "snelheid te versnellen</strong>. Daarin <strong>doet het magnetisch veld niet het "
                  "versnellende werk</strong>: het houdt de deeltjes in hun cirkelbaan, terwijl een "
                  "elektrisch veld ze bij elke ronde een duw geeft. De "
                  "<strong>massaspectrometer</strong> en het <strong>cyclotron</strong> berusten dus "
                  "beide op de kracht op bewegende ladingen."),
            ("p", "Een <strong>hallsensor</strong> dient <strong>om de sterkte van een magnetisch "
                  "veld te meten</strong>: het veld duwt de ladingen in een plaatje naar één zijde, "
                  "en de spanning die daardoor ontstaat is evenredig met \\(B\\). En je ziet het "
                  "<strong>noorderlicht vooral in de buurt van de polen</strong> omdat "
                  "<strong>het aardmagnetisch veld de geladen deeltjes daarheen leidt</strong>: ze "
                  "volgen een schroeflijn rond de veldlijnen, en die komen bij de polen samen. "
                  "<strong>Zuurstof geeft daarbij meestal groen licht</strong>."),
        ]),
    ],
    onthoud=[
        r"Laplacekracht: \(F = B\,I\,\ell\,\sin\alpha\), loodrecht op draad en veld.",
        r"Evenwijdig met het veld is \(\sin\alpha = 0\); loodrecht is de kracht maximaal.",
        "Gelijke stroomzin trekt aan, tegengestelde stoot af; dichterbij is sterker.",
        r"Lorentzkracht: \(F = q\,v\,B\,\sin\alpha\), loodrecht op de snelheid.",
        "Een magnetisch veld verricht geen arbeid: het buigt af maar versnelt niet.",
        r"Cirkelbaan: \(r = \dfrac{m\,v}{q\,B}\); zwaarder of sneller is een ruimere bocht.",
        r"Omlooptijd \(T = \dfrac{2\pi m}{q\,B}\), onafhankelijk van de snelheid.",
        "Collector: keert de stroom elke halve omwenteling om.",
    ],
)

# ───────────────────── 7. Elektromagnetische inductie
BUNDELS["elektromagnetische-inductie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektromagnetische inductie",
    onder="Flux, de wetten van Faraday en Lenz, en alles van dynamo tot draadloze lader.",
    secties=[
        dict(kop="De magnetische flux", blokken=[
            ("p", "De <strong>magnetische flux door een winding</strong> is "
                  "<strong>het veld maal de doorsneden oppervlakte, met de hoek erbij</strong>: "
                  "\\[\\Phi = B\\,A\\,\\cos\\alpha\\] "
                  "met \\(\\alpha\\) de hoek tussen het veld en de normaal op het vlak van de "
                  "winding. Je kan \\(\\Phi\\) zien als het aantal veldlijnen dat door de "
                  "winding gaat. Ze "
                  "hangt dus af van <strong>de sterkte van het magnetisch veld</strong>, "
                  "<strong>de oppervlakte van de winding</strong> en "
                  "<strong>de hoek tussen de winding en het veld</strong>, en ze is het grootst als "
                  "de winding loodrecht in het veld staat, want dan is "
                  "\\(\\cos\\alpha = 1\\). Flux staat in "
                  "<strong>weber</strong>, en \\(1\\ \\text{Wb} = 1\\ "
                  "\\text{T}\\cdot\\text{m}^{2}\\)."),
            ("p", "Rekenen: een winding van \\(A = 0{,}020\\ \\text{m}^{2}\\) die loodrecht "
                  "in een veld van \\(B = 0{,}50\\ \\text{T}\\) staat, heeft "
                  "\\[\\Phi = 0{,}50\\cdot 0{,}020 = 0{,}010\\ \\text{Wb}\\]"),
            ("p", "De flux door een spoel laten veranderen kan je "
                  "<strong>door een magneet in of uit de spoel te bewegen</strong> of "
                  "<strong>door de spoel in het veld te laten draaien</strong>. Een "
                  "<strong>magneet die stil in een spoel ligt, wekt geen inductiespanning op</strong>, "
                  "want dan verandert er niets."),
        ]),
        dict(kop="De wet van Faraday", blokken=[
            ("p", "De <strong>inductiewet van Faraday</strong> zegt dat "
                  "<strong>de inductiespanning afhangt van hoe snel de flux verandert</strong>. Het "
                  "is dus <strong>de wet die de inductiespanning met de fluxverandering "
                  "verbindt</strong>: "
                  "\\[U = -N\\,\\dfrac{\\Delta\\Phi}{\\Delta t}\\] "
                  "Het minteken is de wet van Lenz, verderop. Let op wat er níet in staat: de "
                  "flux zelf. Een grote maar onveranderlijke flux levert niets op, want dan is "
                  "\\(\\Delta\\Phi = 0\\)."),
            ("p", "De inductiespanning van een spoel wordt dus bepaald door "
                  "<strong>het aantal windingen</strong> en "
                  "<strong>de snelheid waarmee de flux verandert</strong>. "
                  "<strong>Verdubbel je het aantal windingen</strong>, dan "
                  "<strong>wordt ze twee keer zo groot</strong>, want \\(N\\) staat als factor "
                  "vooraan. Een spoel met "
                  "\\(N = 200\\) windingen die de flux in "
                  "\\(\\Delta t = 0{,}10\\ \\text{s}\\) met "
                  "\\(\\Delta\\Phi = 0{,}0040\\ \\text{Wb}\\) ziet veranderen, geeft "
                  "\\[U = 200\\cdot\\dfrac{0{,}0040}{0{,}10} = 8{,}0\\ \\text{V}\\]"),
            ("p", "Een <strong>magneet die je sneller in een spoel duwt, levert meer spanning "
                  "op</strong>, want <strong>de flux verandert dan in minder tijd evenveel</strong>: "
                  "\\(\\Delta t\\) staat in de noemer. "
                  "Op een fluxgrafiek lees je dat rechtstreeks af, want "
                  "\\(\\dfrac{\\Delta\\Phi}{\\Delta t}\\) is net de helling van die "
                  "grafiek: "
                  "<strong>hoe steiler de fluxgrafiek loopt, hoe gróter de inductiespanning op dat "
                  "ogenblik</strong>, en waar de <strong>flux een tijdlang constant blijft, is de "
                  "inductiespanning nul</strong>."),
            ("fig", svg.inductie(),
             "Links duw je een noordpool naar de spoel toe; de spoel maakt aan die kant zelf een "
             "noordpool en duwt terug. Onderaan: waar de fluxgrafiek vlak loopt, is de spanning "
             "nul, en waar ze de andere kant op helt, keert de spanning van teken."),
            ("p", "<strong>Zonder een gesloten kring is er wel een inductiespanning, maar geen "
                  "inductiestroom</strong>: de spanning staat er, maar er kan niets lopen."),
            ("p", "Een <strong>rechthoekige winding die rondraait in een homogeen veld</strong> "
                  "geeft een spanning die <strong>regelmatig van teken wisselt, als een "
                  "sinus</strong>. Daarom levert een <strong>generator met een draaiende "
                  "winding wisselspanning</strong>."),
        ]),
        dict(kop="De wet van Lenz", blokken=[
            ("p", "De <strong>wet van Lenz</strong> zegt dat "
                  "<strong>de inductiestroom de verandering die hem veroorzaakt tegenwerkt</strong>. "
                  "Het is dus <strong>de wet die zegt dat een inductiestroom zijn eigen oorzaak "
                  "tegenwerkt</strong>."),
            ("p", "Duw je de <strong>noordpool van een magneet in een spoel</strong>, dan "
                  "<strong>maakt de spoel aan die kant zelf een noordpool en duwt ze terug</strong>. "
                  "Daarom <strong>moet je arbeid leveren om een magneet in een gesloten spoel te "
                  "duwen</strong>: die arbeid is net de energie die de stroom meekrijgt."),
        ]),
        dict(kop="Dynamo en generator", blokken=[
            ("p", "Een <strong>dynamo op een fiets</strong> wekt spanning op doordat "
                  "<strong>een magneet langs een spoel draait en de flux laat wisselen</strong>. "
                  "Zodra de lamp brandt, loopt er een stroom, en volgens de wet van Lenz werkt die "
                  "de beweging tegen: daarom <strong>fietst een dynamo zwaarder zodra de lamp "
                  "brandt</strong>."),
            ("p", "De <strong>pick-up van een elektrische gitaar</strong> werkt doordat "
                  "<strong>de trillende stalen snaar de flux door een spoeltje verandert</strong>. "
                  "Een <strong>detectielus in het wegdek merkt een wagen op doordat de wagen de flux "
                  "door de lus verandert</strong>."),
            ("p", "Een <strong>draadloze oplader</strong> laadt een telefoon op doordat "
                  "<strong>een spoel in de lader een stroom opwekt in een spoel in de "
                  "telefoon</strong>. De <strong>dynamo op een fiets</strong> en de "
                  "<strong>draadloze oplader</strong> berusten dus beide op inductie, net als een "
                  "<strong>transformator in een laadblokje</strong> en een "
                  "<strong>inductiekookplaat</strong>."),
        ]),
        dict(kop="De transformator", blokken=[
            ("p", "Een <strong>transformator</strong> dient <strong>om een wisselspanning hoger of "
                  "lager te maken</strong>. Hij heeft twee spoelen: een "
                  "<strong>primaire en een secundaire</strong>. De spanningen staan in dezelfde "
                  "verhouding als de aantallen windingen: "
                  "\\[\\dfrac{U_{1}}{U_{2}} = \\dfrac{N_{1}}{N_{2}}\\] "
                  "Hij <strong>werkt niet op gelijkspanning</strong>, want dan verandert de flux "
                  "niet en is \\(\\Delta\\Phi = 0\\)."),
            ("p", "Twee voorbeelden. Een transformator met <strong>500 windingen primair en 50 "
                  "secundair</strong> <strong>verlaagt 230 V tot 23 V</strong>, want "
                  "\\(U_{2} = 230\\cdot\\dfrac{50}{500}\\). Een transformator met "
                  "<strong>100 windingen primair en 400 secundair</strong> is "
                  "<strong>een optransformator, want hij verhoogt de spanning</strong>, tot vier "
                  "keer de ingangsspanning."),
            ("p", "Een transformator <strong>kan het vermogen niet groter maken dan het vermogen "
                  "dat erin gaat</strong>. In het beste geval geldt "
                  "\\(U_{1}I_{1} = U_{2}I_{2}\\): gaat de spanning omhoog, dan gaat de stroom "
                  "evenredig omlaag. Dat "
                  "is ook waarom <strong>stroom over grote afstanden op hoogspanning vervoerd "
                  "wordt</strong>: <strong>bij een kleinere stroom gaat er veel minder warmte "
                  "verloren</strong> in de kabels. Dat verlies is "
                  "\\(P_{\\text{verlies}} = R\\,I^{2}\\), dus tien keer minder stroom is "
                  "honderd keer minder verlies."),
            ("p", "De <strong>kern van een transformator is uit dunne, van elkaar geïsoleerde "
                  "plaatjes</strong> opgebouwd <strong>om de wervelstromen in de kern klein te "
                  "houden</strong>."),
        ]),
        dict(kop="Wervelstromen", blokken=[
            ("p", "<strong>Wervelstromen</strong> zijn de kringstromen die "
                  "<strong>in een massief stuk metaal ontstaan bij een veranderende flux</strong>. "
                  "Ze heten ook <strong>foucaultstromen</strong>. "
                  "Ze <strong>werken de beweging die ze veroorzaakt tegen</strong>, en "
                  "<strong>gleuven of dunne plaatjes maken ze veel kleiner</strong>. In een isolator "
                  "ontstaan ze niet, want daar zijn geen vrije elektronen."),
            ("p", "Daarom <strong>valt de slinger van von Waltenhofen met een volle plaat trager dan "
                  "die met gleuven erin</strong>, en daarom <strong>raakt een elektromagnetische rem "
                  "het wiel niet aan</strong>: de wervelstromen remmen zonder contact."),
            ("p", "Een <strong>inductiekookplaat</strong> werkt doordat "
                  "<strong>een wisselend veld wervelstromen opwekt in de bodem van de pan</strong>, "
                  "die daardoor zelf warm wordt. Hij <strong>werkt niet met een pan van "
                  "aluminium</strong>, want <strong>aluminium is niet ferromagnetisch genoeg voor de "
                  "koppeling</strong>."),
        ]),
    ],
    onthoud=[
        r"Flux: \(\Phi = B\,A\,\cos\alpha\), in weber; \(1\ \text{Wb} = 1\ \text{T}\cdot\text{m}^{2}\).",
        r"Faraday: \(U = -N\,\dfrac{\Delta\Phi}{\Delta t}\); de flux zelf staat er niet in.",
        "Meer windingen of sneller veranderen geeft meer spanning.",
        "Op een fluxgrafiek is de spanning de helling, niet de hoogte.",
        "Lenz: de inductiestroom werkt zijn eigen oorzaak tegen; dat is het minteken.",
        "Zonder gesloten kring wel spanning, geen stroom.",
        r"Transformator: \(\dfrac{U_{1}}{U_{2}} = \dfrac{N_{1}}{N_{2}}\), en \(U_{1}I_{1} = U_{2}I_{2}\).",
        "Een transformator werkt enkel op wisselspanning en maakt geen vermogen bij.",
        "Wervelstromen remmen en verwarmen; gleuven en plaatjes houden ze klein.",
    ],
)

# ───────────────────── 8. Statica: krachten, moment en evenwicht
BUNDELS["statica-krachten-moment-en-evenwicht-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Statica: krachten, moment en evenwicht",
    onder="Krachten samenstellen en ontbinden, en wanneer een lichaam niet beweegt of kantelt.",
    secties=[
        dict(kop="Een kracht is een vector", blokken=[
            ("p", "Een kracht heeft naast een grootte ook "
                  "<strong>een richting en een zin</strong> nodig om volledig bepaald te zijn: ze "
                  "is een vector. Kracht staat in newton, en de "
                  "<strong>newton is uit drie basiseenheden samengesteld</strong>: "
                  "<strong>kg·m/s²</strong>, dus kilogram maal meter per seconde kwadraat."),
            ("p", "De <strong>zwaartekracht</strong> op een massa reken je als "
                  "\\(F_{z} = m\\,g\\). Op "
                  "<strong>8 kg</strong> met <strong>g gelijk aan 9,81 N/kg</strong> is dat "
                  "\\(8{,}0\\cdot 9{,}81 \\approx 78\\ \\text{N}\\), dus "
                  "<strong>ongeveer 78 N</strong>. Het <strong>gewicht</strong> "
                  "<strong>is een kracht en staat dus in newton</strong>, en het "
                  "<strong>hangt af van de plaats waar je je bevindt</strong>; de massa niet."),
            ("p", "<strong>Twee krachten die niet op één lijn liggen</strong>, stel je samen "
                  "<strong>met de parallellogramregel voor vectoren</strong>. Staan "
                  "<strong>6 N en 8 N loodrecht op elkaar</strong> in hetzelfde punt, dan is de "
                  "resulterende kracht <strong>10 N</strong>, volgens de stelling van Pythagoras: "
                  "\\[F = \\sqrt{6{,}0^{2} + 8{,}0^{2}} = \\sqrt{100} = 10\\ \\text{N}\\]"),
            ("p", "Je <strong>ontbindt een kracht in componenten</strong> "
                  "<strong>om apart te kunnen rekenen langs twee loodrechte assen</strong>. Staat "
                  "een <strong>kist op een helling</strong>, dan laat "
                  "<strong>de component langs het hellend vlak</strong> haar naar beneden glijden; "
                  "de andere component drukt op het vlak. Met \\(\\alpha\\) de hellingshoek "
                  "is die eerste component \\(F_{z}\\sin\\alpha\\) en de tweede "
                  "\\(F_{z}\\cos\\alpha\\); die tweede wordt door de normaalkracht "
                  "opgeheven."),
            ("fig", svg.krachtenbeeld(),
             "Links het blok op de helling: de zwaartekracht valt uiteen in een stuk langs het "
             "vlak en een stuk loodrecht erop. Rechts twee krachten die loodrecht op elkaar "
             "staan. Onderaan de krachtarm, de kortste afstand van het draaipunt tot de "
             "werklijn."),
        ]),
        dict(kop="De krachten op een lichaam", blokken=[
            ("p", "Op een lichaam dat op een vlakke tafel ligt, werken "
                  "<strong>de zwaartekracht naar beneden</strong> en "
                  "<strong>de normaalkracht van de tafel omhoog</strong>. De "
                  "<strong>normaalkracht</strong> is de kracht <strong>waarmee een oppervlak "
                  "terugduwt op wat erop rust</strong>, en ze staat "
                  "<strong>altijd loodrecht op het oppervlak waarop het lichaam rust</strong>."),
            ("p", "De <strong>wrijvingskracht</strong> is de kracht die "
                  "<strong>een beweging langs een oppervlak tegenwerkt</strong>. Ze "
                  "<strong>wordt groter als het lichaam harder op het oppervlak drukt</strong>. Een "
                  "<strong>kist van 20 kg op een vlakke vloer met een wrijvingscoëfficiënt van "
                  "0,3</strong> vraagt minstens <strong>60 N</strong> om te schuiven, met g gelijk "
                  "aan 10 N/kg: \\(F_{N} = m\\,g = 200\\ \\text{N}\\) en "
                  "\\(F_{w} = \\mu\\,F_{N} = 0{,}30\\cdot 200 = 60\\ \\text{N}\\)."),
            ("p", "De <strong>veerkracht is recht evenredig met de uitrekking</strong> van de veer, "
                  "niet omgekeerd evenredig. Dat is de wet van Hooke: "
                  "\\[F = k\\,\\Delta\\ell\\] "
                  "Een veer met een "
                  "<strong>veerconstante van 50 N/m</strong> die <strong>8 cm</strong> uitgerekt "
                  "wordt, levert \\(50\\cdot 0{,}080 = 4{,}0\\ \\text{N}\\). Reken de "
                  "centimeter eerst om naar meter, anders staat je antwoord er honderd keer "
                  "naast."),
            ("p", "Hangt een <strong>lamp stil aan één koord</strong>, dan is de "
                  "<strong>spankracht even groot als de zwaartekracht op de lamp</strong>. En op een "
                  "<strong>auto die met constante snelheid rijdt</strong>, werken onder meer "
                  "<strong>de motorkracht naar voren</strong> en "
                  "<strong>de wrijvingskracht naar achter</strong>, en die twee houden elkaar in "
                  "evenwicht."),
        ]),
        dict(kop="Translatie-evenwicht", blokken=[
            ("p", "<strong>Translatie-evenwicht</strong> betekent dat "
                  "<strong>de som van alle krachten op het lichaam nul is</strong>, dus "
                  "\\(\\sum \\vec{F} = \\vec{0}\\). Een "
                  "<strong>lichaam in translatie-evenwicht hoeft niet stil te staan</strong>: ook "
                  "een lichaam met een constante snelheid is in evenwicht, want zijn snelheid "
                  "verandert niet."),
        ]),
        dict(kop="Het moment van een kracht", blokken=[
            ("p", "Het <strong>moment van een kracht</strong> is "
                  "<strong>de kracht maal de krachtarm ten opzichte van het draaipunt</strong>, en "
                  "het staat in <strong>newtonmeter</strong>: "
                  "\\[M = F\\,d\\,\\sin\\alpha\\] "
                  "met \\(d\\) de afstand van het draaipunt tot het aangrijpingspunt en "
                  "\\(\\alpha\\) de hoek tussen de stang en de kracht. De "
                  "<strong>krachtarm</strong> is \\(d\\sin\\alpha\\), de "
                  "kortste afstand van het draaipunt tot de werklijn van de kracht. Een "
                  "<strong>kracht waarvan de werklijn door het draaipunt gaat, heeft geen "
                  "moment</strong>, want dan is die arm nul."),
            ("p", "Rekenen: een kracht van <strong>30 N</strong> die "
                  "<strong>loodrecht op 0,4 m van het draaipunt</strong> werkt, geeft "
                  "\\(M = 30\\cdot 0{,}40 = 12\\ \\text{N}\\cdot\\text{m}\\), want "
                  "\\(\\sin 90^{\\circ} = 1\\). Werkt diezelfde kracht "
                  "<strong>onder 30 graden met de stang</strong>, nog altijd op 0,4 m, dan is "
                  "\\(M = 30\\cdot 0{,}40\\cdot 0{,}50 = 6{,}0\\ "
                  "\\text{N}\\cdot\\text{m}\\): de helft, want de sinus van 30 graden is "
                  "een half."),
            ("p", "Daarom zit <strong>de klink van een deur zo ver mogelijk van de "
                  "scharnieren</strong>: <strong>zo is de krachtarm groot en volstaat een kleine "
                  "kracht</strong>. En daarom gebruik je <strong>een lange steeksleutel om een "
                  "vastzittende bout los te draaien</strong>: "
                  "<strong>de langere arm geeft bij dezelfde kracht een groter moment</strong>."),
            ("p", "Het punt waarrond een hefboom draait, heet het <strong>draaipunt</strong>. "
                  "<strong>Bij het berekenen van de momenten mag je zelf kiezen welk punt je als "
                  "draaipunt neemt</strong>; een handige keuze laat onbekende krachten wegvallen."),
        ]),
        dict(kop="Rotatie-evenwicht", blokken=[
            ("p", "<strong>Rotatie-evenwicht</strong> betekent dat "
                  "<strong>de momenten linksom en rechtsom elkaar opheffen</strong>. "
                  "<strong>Voor statisch evenwicht volstaat het dus niet dat de som van de krachten "
                  "nul is</strong>: <strong>de som van alle krachten én de som van alle momenten "
                  "moeten nul zijn</strong>, dus \\(\\sum \\vec{F} = \\vec{0}\\) én "
                  "\\(\\sum M = 0\\)."),
            ("p", "Op een wip: zit een <strong>kind van 30 kg op 2 m</strong> van het draaipunt, "
                  "dan moet een <strong>kind van 40 kg</strong> op <strong>1,5 m</strong> zitten "
                  "voor evenwicht, want 30 maal 2 is 40 maal 1,5. Werken "
                  "<strong>twee krachten van 50 N</strong> op een hefboom, "
                  "<strong>de ene op 0,6 m links en de andere op 0,4 m rechts</strong>, dan "
                  "<strong>draait de hefboom naar de kant van de kracht op 0,6 m</strong>, want daar "
                  "is het moment groter."),
            ("p", "Twee toepassingen. Rust een <strong>plank van 4 m op twee steunen aan de "
                  "uiteinden</strong> met een <strong>last op 1 m van de linkersteun</strong>, dan "
                  "draagt <strong>de linkersteun het meest, want de last staat er het dichtst "
                  "bij</strong>. En bij een <strong>torenkraan staat er een zwaar blok aan de "
                  "achterste arm</strong> <strong>om het moment van de last aan de voorkant tegen te "
                  "werken</strong>."),
        ]),
        dict(kop="Zwaartepunt en kantelen", blokken=[
            ("p", "Het <strong>zwaartepunt</strong> is het punt "
                  "<strong>waarin je de hele massa van een lichaam mag denken</strong>; het heet ook het <strong>massamiddelpunt</strong>. Voor "
                  "<strong>volledig evenwicht</strong> moeten "
                  "<strong>de som van alle krachten nul</strong> zijn, "
                  "<strong>de som van alle momenten nul</strong> zijn en moet "
                  "<strong>het zwaartepunt boven het steunvlak liggen</strong>."),
            ("p", "Een voorwerp <strong>kantelt zodra zijn zwaartepunt buiten het steunvlak "
                  "valt</strong>. Daarom <strong>kantelt een zwaar lichaam met een breed steunvlak "
                  "juist minder makkelijk</strong> dan een smal en hoog lichaam: een laag "
                  "zwaartepunt en een breed steunvlak maken een voorwerp stabiel."),
        ]),
    ],
    onthoud=[
        r"Een kracht heeft grootte, richting en zin; \(1\ \text{N} = 1\ \text{kg}\cdot\text{m/s}^{2}\).",
        "Krachten die niet op één lijn liggen: parallellogramregel.",
        "De normaalkracht staat loodrecht op het oppervlak.",
        "Translatie-evenwicht: som van de krachten nul, snelheid mag constant zijn.",
        r"Moment: \(M = F\,d\,\sin\alpha\), in newtonmeter.",
        r"Zwaartekracht \(F_{z} = m\,g\), wrijving \(F_{w} = \mu F_{N}\), veer \(F = k\,\Delta\ell\).",
        "Door het draaipunt werken betekent geen moment.",
        "Statisch evenwicht vraagt krachten én momenten nul.",
        "Kantelen gebeurt zodra het zwaartepunt buiten het steunvlak valt.",
    ],
)

# ───────────────────── 9. De wetten van Newton
BUNDELS["de-wetten-van-newton-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De wetten van Newton",
    onder="Traagheid, F = m · a en actie en reactie, met de voorbeelden erbij.",
    secties=[
        dict(kop="De eerste wet: traagheid", blokken=[
            ("p", "De <strong>eerste wet van Newton</strong> zegt dat "
                  "<strong>zonder resulterende kracht de bewegingstoestand niet verandert</strong>: "
                  "wat stilstaat blijft stilstaan, wat beweegt blijft met dezelfde snelheid "
                  "rechtdoor gaan. Met één woord heet ze de <strong>traagheidswet</strong>. Er zijn "
                  "in totaal <strong>drie</strong> wetten van Newton."),
            ("p", "Daaruit volgt dat een <strong>lichaam geen voortdurende kracht nodig heeft om "
                  "met constante snelheid door te blijven bewegen</strong>, en dat een "
                  "<strong>lichaam dat met constante snelheid rechtdoor beweegt, geen resulterende "
                  "kracht voelt</strong>. Op een <strong>lift die met constante snelheid naar boven "
                  "gaat</strong>, is de resulterende kracht dus "
                  "<strong>nul, want de snelheid verandert niet</strong>."),
            ("p", "Voorbeelden van <strong>traagheid</strong>: "
                  "<strong>je glijdt vooruit als de trein plots afremt</strong> en "
                  "<strong>een tafellaken wegtrekken zonder de borden mee</strong>. Ook "
                  "<strong>naar voren vliegen als de bus plots remt</strong> hoort erbij: "
                  "<strong>je lichaam wil met dezelfde snelheid door blijven gaan</strong>. Een "
                  "<strong>gordel die je bij een botsing tegenhoudt</strong>, en een "
                  "<strong>tafellaken dat onder de borden vandaan getrokken wordt</strong>, zijn "
                  "allebei de <strong>eerste wet</strong>."),
            ("p", "De grootheid die zegt <strong>hoe moeilijk een lichaam van bewegingstoestand "
                  "verandert</strong>, is zijn <strong>massa</strong>. Massa is dus de maat van de "
                  "traagheid."),
        ]),
        dict(kop="De tweede wet: F = m · a", blokken=[
            ("p", "De <strong>tweede wet van Newton</strong> zegt dat "
                  "<strong>de resulterende kracht de massa maal de versnelling is</strong>: "
                  "\\[F_{\\text{res}} = m\\,a \\quad\\text{en dus}\\quad "
                  "a = \\dfrac{F_{\\text{res}}}{m}\\] "
                  "De "
                  "<strong>resulterende kracht</strong> is <strong>de vectoriële som van alle "
                  "krachten</strong> en ze <strong>wijst in dezelfde zin als de versnelling</strong>: "
                  "<strong>de versnelling wijst altijd in dezelfde zin als de resulterende "
                  "kracht</strong>. Versnelling staat in \\(\\text{m/s}^{2}\\)."),
            ("fig", svg.newtonkrachten(),
             "Links tel je eerst alle krachten op één lichaam samen; wat overblijft is de "
             "resulterende kracht, en die deel je door de massa. Rechts twee krachten die "
             "even groot en tegengesteld zijn maar op verschillende lichamen aangrijpen, en "
             "elkaar daarom niet opheffen."),
            ("p", "Drie keer rekenen. Werkt op een lichaam van \\(4{,}0\\ \\text{kg}\\) een "
                  "resulterende kracht van \\(12\\ \\text{N}\\), dan is "
                  "\\(a = \\dfrac{12}{4{,}0} = 3{,}0\\ \\text{m/s}^{2}\\). Wordt een "
                  "kist van \\(5{,}0\\ \\text{kg}\\) met \\(20\\ \\text{N}\\) "
                  "geduwd terwijl ze \\(5{,}0\\ \\text{N}\\) wrijving voelt, dan is "
                  "\\(F_{\\text{res}} = 15\\ \\text{N}\\) en "
                  "\\(a = 3{,}0\\ \\text{m/s}^{2}\\). Om een lichaam van "
                  "\\(2{,}0\\ \\text{kg}\\) vanuit rust in \\(5{,}0\\ \\text{s}\\) "
                  "tot \\(10\\ \\text{m/s}\\) te brengen, reken je eerst "
                  "\\(a = \\dfrac{\\Delta v}{\\Delta t} = 2{,}0\\ \\text{m/s}^{2}\\) "
                  "en dan \\(F = 2{,}0\\cdot 2{,}0 = 4{,}0\\ \\text{N}\\)."),
            ("p", "De massa werkt tegen, want ze staat in de noemer van "
                  "\\(a = \\dfrac{F}{m}\\): een <strong>grotere massa heeft bij dezelfde "
                  "kracht een kleinere versnelling</strong>. Krijgen een <strong>wagen van 1000 kg "
                  "en een "
                  "vrachtwagen van 10 000 kg dezelfde kracht</strong>, dan "
                  "<strong>versnelt de wagen tien keer zo hard als de vrachtwagen</strong>. Daarom "
                  "verklaart de <strong>tweede wet</strong> ook waarom een "
                  "<strong>volle winkelkar trager op gang komt</strong>: "
                  "<strong>een grotere massa geeft minder versnelling</strong>."),
            ("p", "De zin van de versnelling volgt uit de kracht. Bij een "
                  "<strong>afremmende auto</strong> wijst ze "
                  "<strong>tegen de bewegingszin in</strong>. Rolt een "
                  "<strong>bal een helling af</strong>, dan zorgt "
                  "<strong>de component van de zwaartekracht langs het vlak</strong> voor de "
                  "versnelling."),
            ("p", "Een <strong>steen valt in een luchtledige buis even snel als een veertje</strong> "
                  "omdat <strong>er geen luchtweerstand is, dus werkt enkel de zwaartekracht</strong>. "
                  "In de tweede wet valt de massa dan aan beide kanten weg: uit "
                  "\\(m\\,g = m\\,a\\) volgt \\(a = g\\), ongeacht hoe zwaar het "
                  "voorwerp is."),
        ]),
        dict(kop="De derde wet: actie en reactie", blokken=[
            ("p", "De <strong>derde wet van Newton</strong> zegt dat "
                  "<strong>elke kracht samengaat met een even grote tegengestelde kracht</strong>. "
                  "Met één woord: de <strong>actie-reactiewet</strong>. Duw je "
                  "<strong>met 200 N tegen een muur</strong>, dan duwt de muur "
                  "<strong>met 200 N</strong> terug."),
            ("p", "<strong>Actie en reactie heffen elkaar niet op</strong> omdat "
                  "<strong>ze op twee verschillende lichamen werken</strong>: ze werken dus "
                  "<strong>niet op hetzelfde lichaam</strong> in. Daarom kan je met zo'n paar nooit "
                  "rechtstreeks rekenen aan één lichaam."),
            ("p", "Twee krachten vormen een <strong>actie-reactiepaar</strong> als ze op elkaars "
                  "lichaam werken: <strong>de aarde trekt aan de maan en de maan aan de "
                  "aarde</strong>, en <strong>jij duwt tegen de muur en de muur duwt tegen "
                  "jou</strong>. De reactie op <strong>de zwaartekracht die de aarde op jou "
                  "uitoefent</strong>, is <strong>de kracht waarmee jij aan de aarde trekt</strong>. "
                  "En <strong>als jij op de grond springt, duw jij de aarde ook een beetje "
                  "weg</strong> — alleen merk je dat niet, want haar massa is onvoorstelbaar veel "
                  "groter."),
            ("p", "Voorbeelden van de derde wet: <strong>een zwemmer die water naar achter "
                  "duwt</strong> en <strong>een ballon die leegloopt en wegvliegt</strong>. Een "
                  "<strong>raket komt in de ruimte vooruit</strong> doordat "
                  "<strong>ze gassen naar achter duwt en die haar naar voren duwen</strong>. En een "
                  "<strong>geweer slaat terug bij het afvuren</strong> omdat "
                  "<strong>de kogel even hard terugduwt als het geweer hem vooruit duwt</strong>."),
            ("p", "Een <strong>paard trekt aan een kar met dezelfde kracht als waarmee de kar aan "
                  "het paard trekt</strong>, en toch komt het geheel vooruit: "
                  "<strong>het paard duwt ook met zijn hoeven tegen de grond</strong>, en die kracht "
                  "van buiten het stel zet alles in beweging. Bij een "
                  "<strong>botsing tussen een vrachtwagen en een auto zijn de twee krachten even "
                  "groot</strong>; de schade is anders doordat de massa's verschillen."),
        ]),
        dict(kop="Zwaarder en lichter voelen", blokken=[
            ("p", "Versnelt een <strong>lift naar boven</strong>, dan "
                  "<strong>voel je je zwaarder dan anders</strong>, want de vloer moet je naast je "
                  "gewicht ook nog versnellen. Bij een versnelling naar beneden voel je je lichter."),
            ("p", "Een <strong>astronaut in een baan rond de aarde voelt nog wél "
                  "zwaartekracht</strong>: die houdt hem net in zijn baan. Hij zweeft omdat hij "
                  "samen met zijn station in een vrije val zit."),
            ("p", "Voetgangers <strong>buigen hun knieën bij het landen van een sprong</strong> "
                  "omdat <strong>het afremmen dan langer duurt en de kracht kleiner is</strong>. Dat "
                  "is de tweede wet in omgekeerde richting: dezelfde "
                  "snelheidsverandering over een langere tijd vraagt een kleinere kracht."),
        ]),
    ],
    onthoud=[
        "Eerste wet: zonder resulterende kracht verandert de bewegingstoestand niet.",
        "Massa is de maat van de traagheid.",
        r"Tweede wet: \(F_{\text{res}} = m\,a\), dus \(a = \dfrac{F_{\text{res}}}{m}\).",
        "Dezelfde kracht geeft een tien keer zwaarder lichaam tien keer minder versnelling.",
        "Derde wet: elke kracht heeft een even grote tegengestelde kracht.",
        "Actie en reactie heffen elkaar niet op: ze werken op twee lichamen.",
        "Langer afremmen betekent een kleinere kracht.",
    ],
)

# ───────────────────── 10. Rechtlijnige beweging: ERB en EVRB
BUNDELS["rechtlijnige-beweging-erb-en-evrb-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Rechtlijnige beweging: ERB en EVRB",
    onder="Grafieken lezen en rekenen aan een beweging met en zonder versnelling.",
    secties=[
        dict(kop="De eenparig rechtlijnige beweging", blokken=[
            ("p", "Een <strong>eenparig rechtlijnige beweging</strong> is een beweging op een "
                  "rechte lijn met <strong>constante snelheid</strong>. De afkorting "
                  "<strong>ERB</strong> staat voor <strong>eenparig rechtlijnige "
                  "beweging</strong>. De versnelling is er nul, \\(a = 0\\), en dus is ook "
                  "\\(\\sum \\vec{F} = \\vec{0}\\): dat is de eerste wet van Newton. Bij een ERB "
                  "zijn de gemiddelde en de ogenblikkelijke snelheid even groot."),
            ("kader", "<strong>De twee formules van een ERB</strong><br>"
                      "\\[v = \\dfrac{\\Delta x}{\\Delta t} \\qquad\\text{en}\\qquad "
                      "x = x_{0} + v\\,t\\]"
                      "\\(x_{0}\\) is de plaats op \\(t = 0\\). De eenheid van \\(v\\) is "
                      "\\(\\text{m/s}\\); van km/h naar m/s deel je door \\(3{,}6\\), "
                      "omgekeerd vermenigvuldig je ermee. Zo is \\(108\\) km/h gelijk aan "
                      "\\(\\dfrac{108}{3{,}6} = 30\\) m/s."),
            ("p", "Rekenen aan een ERB. Een <strong>auto</strong> die \\(243\\) km aflegt in "
                  "\\(2\\) h \\(30\\) min, heeft \\(v_{\\text{gem}} = \\dfrac{243\\ "
                  "\\text{km}}{2{,}5\\ \\text{h}} = 97{,}2\\) km/h. Een <strong>trein</strong> "
                  "met \\(27\\) m/s komt in \\(3\\) min \\(20\\) s, dus in \\(200\\) s, "
                  "\\(27 \\times 200 = 5400\\) m verder, of \\(5{,}4 \\times 10^{3}\\) m. "
                  "Vertrekken <strong>twee fietsers</strong> samen met \\(4{,}5\\) m/s en "
                  "\\(7{,}0\\) m/s, dan groeit hun onderlinge afstand met "
                  "\\(\\Delta v = 2{,}5\\) m/s, en liggen ze na \\(40\\) s \\(100\\) m uit "
                  "elkaar."),
        ]),
        dict(kop="Weg, verplaatsing en snelheid", blokken=[
            ("p", "<strong>Afgelegde weg en verplaatsing zijn niet altijd even groot.</strong> "
                  "De afgelegde weg \\(s\\) telt elke meter mee; de verplaatsing is "
                  "\\(\\Delta x = x_{\\text{eind}} - x_{\\text{begin}}\\). Rijdt een "
                  "<strong>fietser</strong> \\(4{,}5\\) km naar het noorden en daarna "
                  "\\(1{,}5\\) km terug, dan is \\(s = 6{,}0\\) km en \\(\\Delta x = 3{,}0\\) km "
                  "naar het noorden. Gaat hij de volle \\(4{,}5\\) km terug, dan is "
                  "\\(\\Delta x = 0\\) terwijl hij toch \\(9{,}0\\) km heeft gefietst."),
            ("p", "Een snelheid heeft <strong>een grootte, een richting en een zin</strong> en "
                  "wordt voorgesteld door een vector \\(\\vec{v}\\). Daarom kan een snelheid "
                  "langs de \\(x\\)-as wel degelijk <strong>negatief</strong> zijn: het teken "
                  "zegt de zin van de beweging langs die as. Alleen de grootte "
                  "\\(\\lvert v \\rvert\\) blijft altijd positief. "
                  "\\(\\text{m/s}^{2}\\) is níét de eenheid van een snelheid maar van een "
                  "versnelling."),
            ("p", "Het verschil tussen de twee snelheden: "
                  "\\(v_{\\text{gem}} = \\dfrac{\\Delta x}{\\Delta t}\\) kijkt naar een heel "
                  "traject, terwijl de <strong>ogenblikkelijke snelheid</strong> diezelfde "
                  "verhouding is voor een heel klein tijdsinterval, dus op één moment. Dat is "
                  "wat je op een snelheidsmeter leest. Om \\(v_{\\text{gem}}\\) te berekenen heb "
                  "je enkel de <strong>afgelegde weg</strong> en de <strong>tijdsduur</strong> "
                  "nodig; de massa \\(m\\) en de versnelling \\(a\\) doen daar niets toe."),
        ]),
        dict(kop="De zes bewegingsgrafieken", blokken=[
            ("fig", svg.bewegingsgrafieken(),
             "Boven een ERB, onder een EVRB. De ingekleurde oppervlakte onder een "
             "v(t)-grafiek is telkens de verplaatsing."),
        ]),
        dict(kop="Grafieken lezen", blokken=[
            ("p", "Wat je uit een <strong>\\(x(t)\\)-grafiek</strong> afleest: de "
                  "<strong>helling is de snelheid</strong>, want "
                  "\\(\\dfrac{\\Delta x}{\\Delta t} = v\\). Een horizontaal stuk betekent dat "
                  "het lichaam <strong>stilstaat</strong>, een dalend stuk dat het "
                  "<strong>terugkeert naar het vertrekpunt</strong>. Loopt zo'n grafiek eerst "
                  "stijgend en daarna dalend, dan keert het lichaam onderweg om; op het hoogste "
                  "punt van de grafiek is \\(v = 0\\). De oppervlakte onder een "
                  "\\(x(t)\\)-grafiek betekent niets."),
            ("p", "Wat je uit de twee andere grafieken afleest: de oppervlakte onder een "
                  "<strong>\\(v(t)\\)-grafiek</strong> is de <strong>verplaatsing</strong>, want "
                  "\\(\\Delta x = v\\,\\Delta t\\) voor elk smal stukje, en een stuk onder de as "
                  "telt negatief mee. De oppervlakte onder een "
                  "<strong>\\(a(t)\\)-grafiek</strong> geeft op dezelfde manier de "
                  "<strong>snelheidsverandering</strong> \\(\\Delta v = a\\,\\Delta t\\). Bij een "
                  "ERB valt die \\(a(t)\\)-grafiek samen met de tijdas."),
        ]),
        dict(kop="De eenparig veranderlijke rechtlijnige beweging", blokken=[
            ("p", "Bij een <strong>eenparig veranderlijke rechtlijnige beweging</strong> (EVRB) "
                  "blijft de <strong>versnelling</strong> dezelfde: elke seconde verandert de "
                  "snelheid met evenveel. De \\(v(t)\\)-grafiek is dan een schuine rechte en de "
                  "\\(x(t)\\)-grafiek een parabool. Een <strong>vrije val zonder "
                  "luchtweerstand</strong> en een <strong>auto die gelijkmatig optrekt</strong> "
                  "zijn voorbeelden; een kind op een <strong>draaimolen</strong> niet, want die "
                  "beweging is niet rechtlijnig."),
            ("kader", "<strong>De vier formules van een EVRB</strong><br>"
                      "\\[a = \\dfrac{\\Delta v}{\\Delta t} \\qquad v = v_{0} + a\\,t\\]"
                      "\\[x = x_{0} + v_{0}\\,t + \\tfrac{1}{2}a\\,t^{2} \\qquad "
                      "v^{2} = v_{0}^{2} + 2a\\,\\Delta x\\]"
                      "De laatste gebruik je als je de tijd niet kent of niet nodig hebt."),
        ]),
        dict(kop="Rekenen aan een EVRB", blokken=[
            ("p", "Rekenen met de versnelling. Een auto die in \\(8{,}0\\) s van \\(12\\) m/s "
                  "naar \\(30\\) m/s gaat, heeft \\(a = \\dfrac{30 - 12}{8{,}0} = 2{,}25\\ "
                  "\\text{m/s}^{2}\\). Een fietser die van \\(10\\) m/s tot stilstand remt in "
                  "\\(5{,}0\\) s, heeft \\(a = \\dfrac{0 - 10}{5{,}0} = -2{,}0\\ "
                  "\\text{m/s}^{2}\\). Een <strong>negatieve versnelling betekent niet altijd "
                  "vertragen</strong>: ze betekent dat \\(\\vec{a}\\) tegen de positieve zin van "
                  "de as in wijst. Is \\(v\\) ook negatief, dan versnelt het lichaam juist."),
            ("p", "Rekenen met weg en snelheid. Een <strong>wagen</strong> die uit rust vertrekt "
                  "met \\(2{,}5\\ \\text{m/s}^{2}\\) komt in \\(6{,}0\\) s "
                  "\\(x = \\tfrac{1}{2}a\\,t^{2} = 45\\) m ver en rijdt dan "
                  "\\(v = a\\,t = 15\\) m/s; zijn gemiddelde over die rit was maar "
                  "\\(7{,}5\\) m/s. Een auto met \\(22\\) m/s die remt met \\(4{,}0\\ "
                  "\\text{m/s}^{2}\\) heeft een <strong>remweg</strong> van "
                  "\\(\\dfrac{v_{0}^{2}}{2a} = \\dfrac{484}{8{,}0} = 60{,}5\\) m. Omdat "
                  "\\(v_{0}\\) daar in het kwadraat staat, is de remweg bij "
                  "<strong>dubbele snelheid vier keer zo lang</strong>."),
            ("p", "Een <strong>inhaaloefening</strong>. Een wagen rijdt met \\(25\\) m/s voorbij "
                  "een stilstaande <strong>motor</strong>, die meteen vertrekt met \\(4{,}0\\ "
                  "\\text{m/s}^{2}\\). Stel de twee plaatsen gelijk: "
                  "\\(25\\,t = \\tfrac{1}{2} \\times 4{,}0 \\times t^{2}\\), dus "
                  "\\(t = \\dfrac{2v}{a} = 12{,}5\\) s. Beide hebben dan \\(312{,}5\\) m "
                  "afgelegd, en de motor rijdt op dat ogenblik \\(50\\) m/s, dubbel zo snel als "
                  "de wagen."),
        ]),
        dict(kop="De vrije val en de verticale worp", blokken=[
            ("p", "Een <strong>vrije val</strong> is een beweging waarbij enkel de "
                  "zwaartekracht werkt en de beginsnelheid nul is. De "
                  "<strong>valversnelling</strong> op aarde is \\(g = 9{,}81\\ "
                  "\\text{m/s}^{2}\\); in oefeningen rekent men soms met \\(10\\). Op de maan is "
                  "\\(g\\) ongeveer zes keer kleiner. Een vrije val is dus een EVRB met "
                  "\\(v_{0} = 0\\) en \\(a = g\\):"),
            ("kader", "\\[v = g\\,t \\qquad\\text{en}\\qquad h = \\tfrac{1}{2}g\\,t^{2}\\]"
                      "Een <strong>steen</strong> valt na \\(3{,}0\\) s met "
                      "\\(v = 9{,}81 \\times 3{,}0 = 29{,}4\\) m/s en is dan \\(44{,}1\\) m "
                      "gevallen. Doet een steen \\(2{,}0\\) s over de bodem van een "
                      "<strong>put</strong>, dan is die put \\(h = 0{,}5 \\times 9{,}81 \\times "
                      "4{,}0 = 19{,}6\\) m diep."),
        ]),
        dict(kop="Valtijd, massa en de verticale worp", blokken=[
            ("p", "Drie dingen gelden voor een vrije val zonder luchtweerstand: de versnelling "
                  "blijft de hele val even groot, de snelheid groeit recht evenredig met de "
                  "tijd, en de afgelegde hoogte groeit met het kwadraat van de tijd. De "
                  "<strong>valtijd hangt niet af van de massa van het voorwerp</strong>: uit \\(m\\,g = m\\,a\\) "
                  "volgt altijd \\(a = g\\), want de massa valt links en rechts weg. Een steen "
                  "en een pluim vallen dus even snel."),
            ("p", "Gooi je een <strong>bal</strong> recht omhoog, dan heb je een "
                  "<strong>verticale worp</strong>. In het hoogste punt is \\(v = 0\\) maar "
                  "blijft \\(a = g\\) omlaag wijzen, want de zwaartekracht blijft werken; "
                  "daarom valt de bal meteen weer terug. Gooi je hem met \\(24\\) m/s omhoog, "
                  "dan geeft \\(v = v_{0} - g\\,t = 0\\) een stijgtijd van "
                  "\\(t = \\dfrac{24}{9{,}81} = 2{,}45\\) s; de hele vlucht duurt \\(4{,}89\\) s, "
                  "want het terugvallen duurt even lang."),
        ]),
    ],
    onthoud=[
        "ERB: \\(a = 0\\), \\(v\\) constant, \\(x = x_{0} + v\\,t\\), \\(x(t)\\) een rechte.",
        "Weg en verplaatsing zijn niet hetzelfde; \\(\\vec{v}\\) is een vector.",
        "Helling van \\(x(t)\\) is \\(v\\); oppervlakte onder \\(v(t)\\) is \\(\\Delta x\\).",
        "EVRB: \\(v = v_{0} + a\\,t\\) en \\(x = x_{0} + v_{0}t + \\tfrac{1}{2}a\\,t^{2}\\).",
        "Zonder tijd: \\(v^{2} = v_{0}^{2} + 2a\\,\\Delta x\\), handig voor een remweg.",
        "Een negatieve \\(a\\) betekent niet automatisch vertragen.",
        "Dubbele snelheid is vier keer de remweg, want \\(v_{0}\\) staat in het kwadraat.",
        "Vrije val: \\(g = 9{,}81\\ \\text{m/s}^{2}\\), onafhankelijk van de massa.",
        "In het hoogste punt van een worp is \\(v = 0\\), maar \\(a\\) niet.",
    ],
)


# ───────────────────── 11. De horizontale worp
BUNDELS["de-horizontale-worp-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De horizontale worp",
    onder="Twee bewegingen tegelijk: eenparig naar voren en vallend naar beneden.",
    secties=[
        dict(kop="Het onafhankelijkheidsbeginsel", blokken=[
            ("p", "Het <strong>onafhankelijkheidsbeginsel</strong> zegt dat de horizontale en "
                  "de verticale beweging elkaar <strong>niet beïnvloeden</strong>. Je mag ze "
                  "dus apart uitrekenen. Het <strong>horizontale deel</strong> is een ERB met "
                  "\\(v_{x} = v_{0}\\) constant, want zonder luchtweerstand werkt er in die "
                  "richting geen kracht. Het <strong>verticale deel</strong> is een vrije val "
                  "met \\(v_{0y} = 0\\): de verticale beginsnelheid is nul, want je werpt "
                  "precies horizontaal. De grootheid die de twee delen gemeen hebben is "
                  "<strong>de tijd</strong> \\(t\\), en dat is net wat ze met elkaar verbindt."),
            ("kader", "<strong>Alles wat je nodig hebt</strong><br>"
                      "\\[x = v_{0}\\,t \\qquad y = \\tfrac{1}{2}g\\,t^{2} \\qquad "
                      "v_{y} = g\\,t\\]"
                      "\\[t = \\sqrt{\\dfrac{2h}{g}} \\qquad "
                      "v = \\sqrt{v_{x}^{2} + v_{y}^{2}}\\]"
                      "Tijdens de vlucht werkt er, zonder luchtweerstand, "
                      "<strong>enkel de zwaartekracht</strong> \\(F_{z} = m\\,g\\), recht "
                      "omlaag. De hand die werpt heeft het voorwerp al losgelaten, dus is er "
                      "geen kracht meer die het vooruit duwt."),
            ("fig", svg.worpbaan(),
             "Links de baan met de snelheid ontbonden, rechts de proef met twee ballen."),
        ]),
        dict(kop="De baan is een parabool", blokken=[
            ("p", "Vul \\(t = \\dfrac{x}{v_{0}}\\) in \\(y = \\tfrac{1}{2}g\\,t^{2}\\) in en de "
                  "tijd verdwijnt: \\[y = \\dfrac{g}{2v_{0}^{2}}\\,x^{2}\\] Dat is de "
                  "vergelijking van een <strong>parabool</strong>, en dat is dus de vorm van de "
                  "baan. Je leest er meteen in dat het <strong>hoogteverlies niet recht "
                  "evenredig is met de horizontale afstand</strong> maar met het "
                  "<strong>kwadraat</strong> ervan: twee keer zo ver is vier keer zo veel "
                  "hoogteverlies."),
        ]),
        dict(kop="Valtijd en dracht", blokken=[
            ("p", "De <strong>valtijd</strong> volgt uit \\(h = \\tfrac{1}{2}g\\,t^{2}\\), dus "
                  "\\(t = \\sqrt{\\dfrac{2h}{g}}\\). Daarin staat <strong>geen</strong> "
                  "\\(v_{0}\\) en <strong>geen</strong> \\(m\\): de valtijd hangt enkel af van de hoogte en van de valversnelling. Anders gezegd: van "
                  "de hoogte en van \\(g\\). Daarom is de valtijd ook de grootheid die je bij "
                  "een worp <strong>als eerste uitrekent</strong>."),
            ("p", "Daaruit volgen twee dingen die je moet kunnen uitleggen. Twee kogels die "
                  "tegelijk van dezelfde hoogte vertrekken, de ene gewoon vallend en de andere "
                  "horizontaal weggeschoten, raken de grond <strong>op hetzelfde "
                  "ogenblik</strong>. En twee ballen die van dezelfde hoogte horizontaal "
                  "vertrekken met een verschillende snelheid, raken de grond <strong>ook "
                  "tegelijk</strong>; bij twee identieke ballen van dezelfde tafel, de ene twee "
                  "keer zo snel als de andere, verschilt dus enkel de dracht, en die is dubbel "
                  "zo groot."),
        ]),
        dict(kop="Hoe de dracht verandert", blokken=[
            ("p", "De <strong>dracht</strong> is de horizontale afstand die het voorwerp "
                  "aflegt: \\[x = v_{0}\\,t = v_{0}\\sqrt{\\dfrac{2h}{g}}\\] Ze hangt dus af "
                  "van \\(h\\) en van \\(v_{0}\\). <strong>Verdubbel je \\(v_{0}\\)</strong> bij "
                  "dezelfde hoogte, dan wordt ze <strong>twee keer</strong> zo groot, want ze is "
                  "er recht evenredig mee. <strong>Verviervoudig je de hoogte</strong> bij "
                  "dezelfde beginsnelheid, dan wordt ze maar <strong>twee keer</strong> zo "
                  "groot, want \\(h\\) staat onder een wortel. De dracht is dus "
                  "<strong>niet</strong> recht evenredig met de hoogte."),
        ]),
        dict(kop="Massa en luchtweerstand", blokken=[
            ("p", "De massa \\(m\\) staat in geen enkele van die formules. Zonder "
                  "luchtweerstand komt een <strong>zwaarder voorwerp dus even ver</strong> als "
                  "een lichter. In het echt valt een <strong>pingpongbal</strong> wél korter dan "
                  "de formules voorspellen, want de <strong>luchtweerstand remt hem horizontaal "
                  "af</strong>. Bij een licht voorwerp met veel oppervlak is dat verschil het "
                  "grootst."),
        ]),
        dict(kop="De snelheid tijdens de vlucht", blokken=[
            ("p", "\\(v_{x}\\) blijft de hele vlucht even groot, want \\(a_{x} = 0\\). "
                  "\\(v_{y} = g\\,t\\) groeit elke seconde met ongeveer \\(9{,}81\\) m/s aan. "
                  "Samen wordt de snelheid dus <strong>steeds groter</strong>, en je stelt ze "
                  "samen met <strong>Pythagoras</strong>: "
                  "\\(v = \\sqrt{v_{x}^{2} + v_{y}^{2}}\\). Beweegt een voorwerp bij het "
                  "neerkomen met \\(12\\) m/s horizontaal en \\(16\\) m/s verticaal, dan is "
                  "\\(v = \\sqrt{144 + 256} = 20\\) m/s. Gewoon optellen mag niet, want de twee "
                  "staan loodrecht op elkaar."),
            ("p", "De snelheidsvector staat altijd <strong>raaklijnig aan de baan</strong>, dus "
                  "halverwege de vlucht schuin omlaag. De hoek volgt uit "
                  "\\(\\tan\\alpha = \\dfrac{v_{y}}{v_{x}}\\) en wordt steiler naarmate "
                  "\\(v_{y}\\) groeit. Het voorwerp raakt de grond daarom <strong>niet "
                  "loodrecht</strong>: er blijft altijd een horizontale snelheid over."),
        ]),
        dict(kop="Rekenen aan een worp", blokken=[
            ("p", "Een bal wordt horizontaal weggeschoten van \\(20\\) m hoog, met "
                  "\\(g = 9{,}81\\ \\text{m/s}^{2}\\). Dan is "
                  "\\(t = \\sqrt{\\dfrac{40}{9{,}81}} = 2{,}02\\) s. Vertrok de bal met "
                  "\\(15\\) m/s, dan is de dracht \\(15 \\times 2{,}02 = 30{,}3\\) m, is "
                  "\\(v_{y} = 9{,}81 \\times 2{,}02 = 19{,}8\\) m/s bij het neerkomen, en is de "
                  "totale snelheid \\(\\sqrt{19{,}8^{2} + 15^{2}} = 24{,}8\\) m/s."),
            ("p", "Nog drie, met \\(g = 10\\ \\text{m/s}^{2}\\) om het rekenen kort te houden. "
                  "Een kogel verlaat een tafel van \\(1{,}25\\) m hoog met \\(4{,}0\\) m/s: "
                  "\\(t = 0{,}50\\) s, dus komt hij \\(2{,}0\\) m van de tafel neer. Een bal "
                  "rolt van een tafel van \\(0{,}80\\) m hoog en raakt de grond na "
                  "\\(t = \\sqrt{0{,}16} = 0{,}40\\) s. En een bal die horizontaal met \\(10\\) "
                  "m/s vertrekt, heeft na \\(20\\) m horizontaal \\(2{,}0\\) s gevlogen en "
                  "verliest dus \\(20\\) m hoogte."),
            ("p", "Omgekeerd rekenen kan ook. Een voetbal wordt van een klif van \\(45\\) m "
                  "horizontaal weggetrapt en komt \\(60\\) m verder neer. Uit de hoogte volgt "
                  "\\(t = \\sqrt{\\dfrac{90}{10}} = 3{,}0\\) s, en dan is "
                  "\\(v_{0} = \\dfrac{60}{3{,}0} = 20\\) m/s."),
        ]),
        dict(kop="Twee situaties om te doorzien", blokken=[
            ("p", "Een <strong>vliegtuig laat een pakket vallen</strong>. Het pakket houdt "
                  "\\(v_{x} = v_{0}\\) van het vliegtuig, dus komt het <strong>recht onder het "
                  "vliegtuig</strong> terecht als dat zijn koers aanhoudt. Vanuit de piloot "
                  "gezien valt het gewoon recht naar beneden."),
            ("p", "Je <strong>mikt bij het werpen over een grote afstand hoger dan het "
                  "doel</strong>, omdat het voorwerp onderweg hoogte verliest door de val. Dat "
                  "hoogteverlies is \\(y = \\dfrac{g}{2v_{0}^{2}}\\,x^{2}\\), dus hoe verder het "
                  "doel, hoe meer je hoger moet richten."),
        ]),
    ],
    onthoud=[
        "Horizontaal \\(x = v_{0}\\,t\\), verticaal \\(y = \\tfrac{1}{2}g\\,t^{2}\\); \\(t\\) verbindt ze.",
        "De baan is de parabool \\(y = \\dfrac{g}{2v_{0}^{2}}\\,x^{2}\\).",
        "\\(t = \\sqrt{\\dfrac{2h}{g}}\\): de valtijd hangt enkel van de hoogte af.",
        "Twee ballen van dezelfde hoogte komen samen neer, hoe snel ze ook vertrekken.",
        "Dracht \\(= v_{0}\\,t\\): dubbel zo snel is dubbel zo ver.",
        "Vier keer hoger is maar twee keer verder, want \\(h\\) staat onder een wortel.",
        "\\(v_{x}\\) blijft, \\(v_{y} = g\\,t\\) groeit, samen \\(v = \\sqrt{v_{x}^{2} + v_{y}^{2}}\\).",
        "Reken altijd eerst de valtijd uit.",
    ],
)


# ───────────────────── 12. De gravitatiekracht en de cirkelbeweging
BUNDELS["de-gravitatiekracht-en-de-cirkelbeweging-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gravitatiekracht en de cirkelbeweging",
    onder="Rondjes draaien, en waarom een satelliet niet naar beneden valt.",
    secties=[
        dict(kop="De eenparig cirkelvormige beweging", blokken=[
            ("p", "Een lichaam voert een <strong>eenparig cirkelvormige beweging</strong> (ECB) "
                  "uit als het een cirkel beschrijft met een <strong>constante "
                  "baansnelheid</strong>. De <strong>grootte</strong> van \\(\\vec{v}\\) blijft "
                  "dus gelijk, terwijl haar <strong>richting</strong> voortdurend verandert. De "
                  "<strong>periode</strong> \\(T\\), ook de <strong>omlooptijd</strong>, is de tijd "
                  "voor één volledige omwenteling, "
                  "en de <strong>frequentie</strong> \\(f\\) is haar omgekeerde, in "
                  "<strong>hertz</strong> (\\(1\\ \\text{Hz} = 1\\ \\text{s}^{-1}\\))."),
            ("kader", "<strong>De grootheden van een ECB</strong><br>"
                      "\\[f = \\dfrac{1}{T} \\qquad \\omega = \\dfrac{2\\pi}{T} \\qquad "
                      "v = \\omega\\,r = \\dfrac{2\\pi r}{T}\\]"
                      "\\(\\omega\\) is de <strong>hoeksnelheid</strong>, de afgelegde hoek per "
                      "seconde, in rad/s. Een wiel dat \\(150\\) keer per minuut rondgaat heeft "
                      "\\(f = \\dfrac{150}{60} = 2{,}5\\) Hz en dus \\(T = 0{,}40\\) s."),
            ("p", "Twee kinderen op dezelfde draaimolen hebben <strong>dezelfde "
                  "\\(\\omega\\)</strong>, ook al zitten ze niet even ver van het midden: ze "
                  "doen er even lang over om rond te gaan. Hun <strong>baansnelheid verschilt "
                  "wel</strong>, want \\(v = \\omega\\,r\\). Draait een draaimolen met "
                  "\\(\\omega = 0{,}80\\) rad/s, dan beweegt een kind op \\(3{,}5\\) m van het "
                  "midden met \\(v = 2{,}8\\) m/s. En doet een kind op \\(2{,}5\\) m van het "
                  "midden \\(4{,}0\\) s over één ronde, dan is "
                  "\\(v = \\dfrac{2\\pi \\times 2{,}5}{4{,}0} = 3{,}9\\) m/s."),
        ]),
        dict(kop="Twee tekeningen om bij te houden", blokken=[
            ("fig", svg.cirkelbeweging(),
             "Links een gewone cirkelbeweging, rechts een satelliet rond een planeet."),
        ]),
        dict(kop="De middelpuntzoekende versnelling", blokken=[
            ("p", "Een lichaam in een ECB heeft tóch een versnelling, omdat de "
                  "<strong>richting</strong> van \\(\\vec{v}\\) voortdurend verandert. Die "
                  "versnelling wijst <strong>naar het middelpunt</strong> en heet de "
                  "<strong>centripetale</strong> versnelling; ze heet dus <strong>centripetaal</strong> "
                  "of middelpuntzoekend. Snelheid en "
                  "versnelling staan daarbij <strong>loodrecht op elkaar</strong>: de snelheid "
                  "raakt aan de cirkel, de versnelling wijst naar binnen."),
            ("kader", "\\[a_{c} = \\dfrac{v^{2}}{r} = \\omega^{2}r \\qquad\\text{en}\\qquad "
                      "F_{c} = m\\,a_{c} = \\dfrac{m\\,v^{2}}{r}\\]"
                      "Omdat \\(v\\) in het kwadraat staat, wordt \\(a_{c}\\) <strong>vier keer "
                      "zo groot</strong> als je twee keer zo snel rijdt. Rijdt een auto met "
                      "\\(14\\) m/s door een bocht met straal \\(35\\) m, dan is "
                      "\\(a_{c} = \\dfrac{196}{35} = 5{,}6\\ \\text{m/s}^{2}\\); voor een wagen "
                      "van \\(1200\\) kg is dat \\(F_{c} = 6{,}7\\) kN wrijving."),
        ]),
        dict(kop="Middelpuntzoekend is een rol, geen extra kracht", blokken=[
            ("p", "\\(F_{c}\\) is <strong>geen nieuwe kracht</strong> naast de gewone krachten: "
                  "het is de <strong>rol</strong> die een bestaande kracht speelt. Die rol kan "
                  "gespeeld worden door de <strong>wrijvingskracht tussen de banden en het "
                  "wegdek</strong> van een auto "
                  "in een bocht, door de <strong>spanning</strong> in een touw waaraan je een "
                  "steen rondslingert, of door de <strong>gravitatiekracht</strong> op een "
                  "satelliet. Je tekent haar dus nooit apart naast de andere krachten."),
            ("p", "Twee gevolgen. Omdat \\(F_{c}\\) loodrecht op de beweging staat, "
                  "<strong>verricht ze geen arbeid</strong>: \\(W = F\\,s\\cos 90^\\circ = 0\\), "
                  "en de kinetische energie blijft constant. En <strong>breekt het touw</strong> "
                  "van een rondgeslingerde steen, dan is er geen kracht meer naar het midden: de "
                  "steen vliegt <strong>raaklijnig</strong> verder, niet naar buiten. Dat is de "
                  "traagheidswet."),
        ]),
        dict(kop="De universele gravitatiewet", blokken=[
            ("p", "Elke twee massa's trekken elkaar aan. De kracht is recht evenredig met het "
                  "<strong>product van de twee massa's</strong> en omgekeerd evenredig met het "
                  "<strong>kwadraat van hun afstand</strong>, en ze werkt tussen <strong>alle "
                  "massa's, hoe klein ook</strong>."),
        ]),
        dict(kop="De formule van Newton", blokken=[
            ("kader", "\\[F = G\\,\\dfrac{m_{1}m_{2}}{r^{2}} \\qquad "
                      "G = 6{,}67 \\times 10^{-11}\\ \\text{N}\\,\\text{m}^{2}\\text{/kg}^{2}\\]"
                      "\\(G\\) heet de <strong>gravitatieconstante</strong> en staat in de "
                      "bijlage van het examen. Vergelijk met de wet van Coulomb, "
                      "\\(F = k\\dfrac{\\lvert q_{1}q_{2}\\rvert}{r^{2}}\\): beide hebben "
                      "\\(r^{2}\\) in de noemer en een product in de teller. Het grote verschil "
                      "is dat gravitatie <strong>altijd aantrekt</strong>, want er bestaat geen "
                      "negatieve massa."),
            ("p", "<strong>Verdrievoudig je de afstand</strong>, dan wordt de kracht "
                  "<strong>negen</strong> keer zo klein, want \\(3^{2} = 9\\). Dat heet de "
                  "kwadratenwet. Je voelt geen aantrekking tussen twee voorwerpen in een kamer "
                  "omdat \\(G\\) zo klein is dat de kracht onmeetbaar blijft, maar het "
                  "gravitatieveld van de aarde <strong>houdt nergens op</strong>: het wordt "
                  "alleen steeds zwakker."),
        ]),
        dict(kop="Het gravitatieveld", blokken=[
            ("p", "Het gravitatieveld rond een planeet is <strong>radiaal, met de lijnen naar "
                  "de planeet toe</strong>, want gravitatie trekt altijd aan. De veldsterkte is "
                  "\\(g = \\dfrac{F}{m}\\), in \\(\\text{N/kg}\\), en dat is net dezelfde "
                  "waarde als de valversnelling in \\(\\text{m/s}^{2}\\). Vlak boven het "
                  "aardoppervlak mag je dat <strong>zwaarteveld</strong> als <strong>homogeen</strong> "
                  "beschouwen: over "
                  "een paar honderd meter verandert er zo goed als niets en lopen de lijnen "
                  "zowat evenwijdig."),
        ]),
        dict(kop="Zwaartekracht en valversnelling", blokken=[
            ("p", "De <strong>zwaartekracht is de gravitatiekracht van de aarde op een "
                  "lichaam</strong>. Stel de twee uitdrukkingen gelijk en de massa van het "
                  "voorwerp valt weg: \\[m\\,g = G\\,\\dfrac{M\\,m}{R^{2}} "
                  "\\quad\\Longrightarrow\\quad g = \\dfrac{GM}{R^{2}}\\] De valversnelling aan "
                  "het oppervlak hangt dus enkel af van de <strong>massa</strong> en de "
                  "<strong>straal</strong> van de planeet, en niet van het vallende voorwerp. "
                  "Daarom valt alles even snel."),
        ]),
        dict(kop="g op de maan, en je eigen massa", blokken=[
            ("p", "Daarom is \\(g\\) op de maan ongeveer zes keer kleiner: de maan heeft veel "
                  "minder massa, ondanks haar kleinere straal. Hebben twee planeten dezelfde "
                  "massa en heeft de ene een twee keer zo grote straal, dan is \\(g\\) aan haar "
                  "oppervlak <strong>vier</strong> keer kleiner, want \\(R\\) staat in het "
                  "kwadraat. Je <strong>massa verandert niet</strong> als je naar de maan gaat; "
                  "je gewicht wel, want dat is een kracht \\(F_{z} = m\\,g\\)."),
        ]),
        dict(kop="Satellieten", blokken=[
            ("p", "Een satelliet in een <strong>cirkelbaan</strong> wordt daarin gehouden door de "
                  "<strong>gravitatiekracht "
                  "van de aarde</strong>, en die speelt daar de rol van middelpuntzoekende "
                  "kracht. Hij heeft dus geen motor nodig. Je berekent zijn baansnelheid door "
                  "die twee gelijk te stellen:"),
            ("kader", "\\[G\\,\\dfrac{M\\,m}{r^{2}} = \\dfrac{m\\,v^{2}}{r} "
                      "\\quad\\Longrightarrow\\quad v = \\sqrt{\\dfrac{GM}{r}}\\]"
                      "De massa \\(m\\) van de satelliet valt links en rechts weg. Een "
                      "<strong>zware en een lichte satelliet in dezelfde baan hebben dus "
                      "dezelfde snelheid</strong>. Voor het ISS, op "
                      "\\(r = 6{,}77 \\times 10^{6}\\) m, geeft dat \\(7{,}7\\) km/s."),
        ]),
        dict(kop="Verder weg is trager", blokken=[
            ("p", "Omdat \\(r\\) in de noemer staat, beweegt een satelliet die <strong>verder "
                  "van de aarde</strong> draait <strong>trager</strong>, en doet hij er langer "
                  "over per omloop. Een satelliet die altijd boven hetzelfde punt blijft hangen "
                  "heet <strong>geostationair</strong>: zijn periode is precies één etmaal, en "
                  "dat lukt enkel boven de evenaar op \\(35\\,786\\) km hoogte. Daarom hoef je "
                  "een schotelantenne nooit bij te stellen."),
            ("p", "<strong>Astronauten zweven</strong> in een ruimtestation omdat ze samen met "
                  "het station voortdurend <strong>rond de aarde vallen</strong>, niet omdat er "
                  "geen gravitatie meer zou zijn. Op die hoogte is \\(g\\) nog ongeveer negentig "
                  "procent van die aan het oppervlak; ze voelen alleen niets, omdat niets hen "
                  "tijdens dat vallen tegenhoudt."),
        ]),
    ],
    onthoud=[
        "ECB: \\(\\lvert v \\rvert\\) constant, de richting niet.",
        "\\(f = \\dfrac{1}{T}\\), \\(\\omega = \\dfrac{2\\pi}{T}\\) en \\(v = \\omega\\,r\\).",
        "\\(a_{c} = \\dfrac{v^{2}}{r}\\) wijst naar het midden, loodrecht op \\(v\\).",
        "Middelpuntzoekend is een rol, geen extra kracht, en ze verricht geen arbeid.",
        "Breekt het touw, dan vliegt de steen raaklijnig weg.",
        "\\(F = G\\dfrac{m_{1}m_{2}}{r^{2}}\\): drie keer verder is negen keer zwakker.",
        "\\(g = \\dfrac{GM}{R^{2}}\\): enkel de massa en de straal van de planeet tellen.",
        "Satelliet: \\(v = \\sqrt{\\dfrac{GM}{r}}\\), zonder de massa van de satelliet.",
    ],
)


# ───────────────────── 13. Arbeid, energie en vermogen
BUNDELS["arbeid-energie-en-vermogen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Arbeid, energie en vermogen",
    onder="Wanneer een kracht arbeid verricht, en waar de energie naartoe gaat.",
    secties=[
        dict(kop="Wat arbeid is", blokken=[
            ("p", "Een kracht verricht <strong>arbeid</strong> als haar aangrijpingspunt "
                  "verplaatst wordt in de zin van de kracht. Arbeid staat in "
                  "<strong>joule</strong>, en \\(1\\ \\text{J} = 1\\ \\text{N}\\,\\text{m}\\). "
                  "Het is ook de eenheid van energie, want arbeid is een omzetting van "
                  "energie."),
            ("kader", "<strong>De formule van de arbeid</strong><br>"
                      "\\[W = F\\,s\\cos\\alpha\\]"
                      "\\(\\alpha\\) is de hoek tussen de kracht en de verplaatsing. Bij "
                      "\\(\\alpha = 0^\\circ\\) is \\(\\cos\\alpha = 1\\) en is "
                      "\\(W = F\\,s\\); bij \\(90^\\circ\\) is \\(W = 0\\); bij "
                      "\\(180^\\circ\\) is \\(W\\) negatief. Verplaatst een kracht van "
                      "\\(45\\) N een kist \\(3{,}2\\) m in dezelfde zin, dan is "
                      "\\(W = 144\\) J."),
            ("p", "Een kracht verricht <strong>geen arbeid</strong> als er geen verplaatsing "
                  "is, als ze <strong>loodrecht</strong> op de verplaatsing staat, of als ze "
                  "zelf nul is. Daarom verricht een <strong>kelner</strong> die een blad met "
                  "glazen horizontaal draagt geen arbeid op dat blad, en verricht ook de "
                  "<strong>normaalkracht</strong> op een lichaam dat over een vlakke vloer "
                  "schuift geen arbeid. Om dezelfde reden is de arbeid van de "
                  "<strong>middelpuntzoekende kracht</strong> op een satelliet in een "
                  "cirkelbaan nul. Duw je tegen een muur die niet wijkt, dan is \\(s = 0\\) "
                  "en dus ook \\(W = 0\\), hoe moe je ook wordt."),
        ]),
        dict(kop="Positieve en negatieve arbeid", blokken=[
            ("p", "<strong>Arbeid kan negatief zijn</strong>, namelijk als de kracht tegen de "
                  "verplaatsing in werkt: \\(\\cos 180^\\circ = -1\\). Daarom is de arbeid van "
                  "de <strong>wrijvingskracht altijd negatief</strong>. Schuift een kist "
                  "\\(4{,}0\\) m over een vloer met een wrijvingskracht van \\(25\\) N, dan is "
                  "\\(W = -100\\) J, en die \\(100\\) J verdwijnt als warmte."),
            ("p", "Staat de kracht <strong>schuin</strong>, dan telt enkel de component langs "
                  "de verplaatsing mee. Een kracht van \\(20\\) N onder \\(60^\\circ\\) levert "
                  "over \\(5{,}0\\) m \\(W = 20 \\times 5{,}0 \\times 0{,}5 = 50\\) J. Twee "
                  "hefoefeningen: til je een doos van \\(10\\) kg \\(1{,}5\\) m hoog, dan is "
                  "\\(W = m\\,g\\,h = 147\\) J met \\(g = 9{,}81\\ \\text{N/kg}\\); loop je "
                  "met een tas van \\(5\\) kg een trap van \\(3\\) m op, dan is dat "
                  "\\(150\\) J met \\(g = 10\\ \\text{N/kg}\\). Hoe lang de trap is of hoe "
                  "traag je gaat, verandert daar niets aan."),
        ]),
        dict(kop="Arbeid van een veranderlijke kracht", blokken=[
            ("fig", svg.arbeid_energie(),
             "Links de oppervlakte onder F(x), rechts de omzetting van Ep in Ek."),
            ("p", "De <strong>oppervlakte onder een \\(F(x)\\)-grafiek</strong> is de "
                  "verrichte arbeid; die oppervlakte heet dus gewoon de "
                  "<strong>arbeid</strong>. Bij een kracht die onderweg verandert, kan je niet "
                  "gewoon kracht maal weg nemen en reken je met een "
                  "<strong>integraal</strong>: \\[W = \\int F\\,\\mathrm{d}x\\] Niet constant "
                  "zijn onder meer de <strong>veerkracht</strong> \\(F = k\\,x\\) en de "
                  "<strong>gravitatiekracht</strong> over grote afstandsverschillen, die met "
                  "\\(\\dfrac{1}{r^{2}}\\) daalt."),
        ]),
        dict(kop="Conservatieve krachten", blokken=[
            ("p", "Een <strong>conservatieve kracht</strong> is een kracht waarvan de arbeid "
                  "<strong>niet van de gevolgde weg</strong> afhangt: alleen het begin- en het "
                  "eindpunt tellen. Daarom kan je er een potentiële energie bij definiëren. "
                  "De <strong>zwaartekracht</strong> en de <strong>veerkracht</strong> zijn "
                  "conservatief, net als de gravitatiekracht en de coulombkracht."),
            ("p", "Een kracht waarvan de arbeid <strong>wél van de weg afhangt</strong>, heet "
                  "<strong>niet-conservatief</strong> of dissipatief. Wrijving is daarvan het "
                  "voorbeeld: hoe langer de weg, hoe meer energie er als warmte verdwijnt. "
                  "Ook de normaalkracht, de <strong>luchtweerstand</strong>, de spierkracht "
                  "en een motorkracht zijn niet conservatief. Bij een <strong>botsing</strong> "
                  "gaat een deel van de energie in andere <strong>energievormen</strong> over, "
                  "zoals warmte en geluid."),
        ]),
        dict(kop="Kinetische en potentiële energie", blokken=[
            ("kader", "\\[E_{k} = \\tfrac{1}{2}m\\,v^{2} \\qquad E_{p} = m\\,g\\,h \\qquad "
                      "E_{\\text{veer}} = \\tfrac{1}{2}k\\,x^{2}\\]"
                      "In \\(E_{k}\\) staat \\(v\\) in het kwadraat, dus <strong>twee keer zo "
                      "snel is vier keer zoveel energie</strong>. Welke hoogte je als nulpunt "
                      "voor \\(E_{p}\\) kiest, mag je zelf bepalen, meestal het "
                      "<strong>aardoppervlak</strong>: alleen \\(\\Delta E_{p}\\) telt."),
            ("p", "Een auto van \\(1{,}0 \\times 10^{3}\\) kg die \\(20\\) m/s rijdt heeft "
                  "\\(E_{k} = \\tfrac{1}{2} \\times 1000 \\times 400 = 2{,}0 \\times 10^{5}\\) "
                  "J, dus \\(200\\) kJ. Een steen van \\(2\\) kg op \\(15\\) m hoogte heeft "
                  "\\(E_{p} = 300\\) J en raakt de grond met "
                  "\\(v = \\sqrt{2gh} = \\sqrt{300} \\approx 17\\) m/s. De "
                  "<strong>veerenergie</strong> is niet recht evenredig met de uitrekking maar "
                  "met het <strong>kwadraat</strong> ervan: twee keer zo ver uitrekken kost "
                  "vier keer zoveel energie."),
        ]),
        dict(kop="Het arbeid-energietheorema", blokken=[
            ("p", "Het <strong>arbeid-energietheorema</strong> zegt dat de totale arbeid op "
                  "een lichaam gelijk is aan zijn verandering van kinetische energie: "
                  "\\[W_{\\text{tot}} = \\Delta E_{k}\\] Remt een lichaam af, dan is die "
                  "arbeid negatief. Je kan er de eindsnelheid mee berekenen zonder de tijd te "
                  "kennen."),
        ]),
        dict(kop="Behoud van mechanische energie", blokken=[
            ("p", "In een gesloten systeem <strong>zonder wrijving</strong> blijft "
                  "\\(E_{k} + E_{p}\\) constant. Dat is het behoud van mechanische energie. "
                  "Bij een <strong>slingerende schommel</strong> wisselen kinetische en "
                  "gravitationele potentiële energie elkaar daarom voortdurend af: boven is "
                  "alles potentieel, beneden alles kinetisch. Glijdt een slee van \\(20\\) kg "
                  "zonder wrijving van een heuvel van \\(5\\) m hoog, dan geeft "
                  "\\(m\\,g\\,h = \\tfrac{1}{2}m\\,v^{2}\\) meteen "
                  "\\(v = \\sqrt{2gh} = 10\\) m/s, met \\(g = 10\\ \\text{N/kg}\\). De "
                  "<strong>massa valt weg</strong>, dus een zware en een lichte slee komen "
                  "even snel beneden."),
        ]),
        dict(kop="Energie en wrijving", blokken=[
            ("p", "<strong>Met wrijving</strong> geldt het behoud nog altijd, maar met een "
                  "extra post: \\[E_{p} = E_{k} + Q\\] met \\(Q\\) de warmte, gelijk aan de "
                  "grootte van de arbeid van de wrijving. Glijdt een kist met wrijving een "
                  "helling af, dan wordt de potentiële energie kinetische energie "
                  "<strong>plus warmte</strong>, en komt ze trager beneden. Stuitert een bal "
                  "van \\(2\\) m hoog maar tot \\(1{,}4\\) m, dan is de rest als "
                  "<strong>warmte en geluid</strong> vrijgekomen: energie gaat nooit verloren, "
                  "ze verandert van vorm."),
        ]),
        dict(kop="Vermogen", blokken=[
            ("p", "<strong>Vermogen</strong> is de arbeid die per seconde verricht wordt: "
                  "\\[P = \\dfrac{W}{t}\\] Het staat in <strong>watt</strong>, en "
                  "\\(1\\ \\text{W} = 1\\ \\text{J/s}\\). Een lift die "
                  "\\(6{,}0 \\times 10^{4}\\) J arbeid levert in \\(20\\) s, heeft "
                  "\\(P = 3{,}0 \\times 10^{3}\\) W, dus \\(3\\) kW. Wie een doos "
                  "<strong>sneller</strong> even hoog tilt, levert daardoor niet meer arbeid: "
                  "alleen het vermogen is groter."),
            ("p", "Op een elektriciteitsfactuur staat de energie in <strong>kilowattuur</strong>. "
                  "Dat is geen vermogen maar een hoeveelheid energie: "
                  "\\(E = P\\,t = 1000 \\times 3600 = 3{,}6 \\times 10^{6}\\) J."),
        ]),
    ],
    onthoud=[
        "\\(W = F\\,s\\cos\\alpha\\), in joule; \\(1\\ \\text{J} = 1\\ \\text{N}\\,\\text{m}\\).",
        "Loodrecht op de beweging betekent \\(W = 0\\); tegen de beweging in, \\(W < 0\\), "
        "zoals bij wrijving.",
        "De oppervlakte onder \\(F(x)\\) is \\(W\\); veranderlijk vraagt \\(\\int F\\,\\mathrm{d}x\\). "
        "Conservatief: de arbeid hangt niet van de weg af.",
        "\\(E_{k} = \\tfrac{1}{2}m\\,v^{2}\\), \\(E_{p} = m\\,g\\,h\\), \\(E_{\\text{veer}} = \\tfrac{1}{2}k\\,x^{2}\\).",
        "\\(W_{\\text{tot}} = \\Delta E_{k}\\), en zonder wrijving blijft \\(E_{k} + E_{p}\\) gelijk.",
        "\\(P = \\dfrac{W}{t}\\), in watt; \\(1\\) kWh is \\(3{,}6 \\times 10^{6}\\) J.",
    ],
)


# ───────────────────── 14. De gaswetten en de algemene gaswet
BUNDELS["de-gaswetten-en-de-algemene-gaswet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gaswetten en de algemene gaswet",
    onder="Druk, volume en temperatuur van een gas, en altijd rekenen in kelvin.",
    secties=[
        dict(kop="Vier toestandsgrootheden", blokken=[
            ("p", "De <strong>toestandsgrootheden van een gas</strong> zijn "
                  "<strong>druk \\(p\\), volume \\(V\\), temperatuur \\(T\\) en "
                  "stofhoeveelheid \\(n\\)</strong>. Ken je er drie, dan volgt de vierde "
                  "eruit."),
            ("kader", "<strong>Altijd in kelvin</strong><br>"
                      "\\[T(\\text{K}) = \\theta(^\\circ\\text{C}) + 273\\]"
                      "Je <strong>mag de temperatuur niet in graden celsius invullen</strong>, "
                      "ook niet als je overal dezelfde eenheid gebruikt: de wetten gelden voor "
                      "de absolute temperatuur. \\(27\\ ^\\circ\\text{C}\\) is dus "
                      "\\(300\\) K, en \\(0\\) K ligt bij \\(-273\\ ^\\circ\\text{C}\\)."),
        ]),
        dict(kop="Isotherm: bij constante temperatuur", blokken=[
            ("p", "Bij <strong>constante temperatuur</strong> blijft het product van druk en "
                  "volume gelijk: \\[p\\,V = \\text{cte} \\quad\\text{of}\\quad "
                  "p_{1}V_{1} = p_{2}V_{2}\\] Zo'n proces heet <strong>isotherm</strong>: de "
                  "temperatuur verandert tijdens het proces niet, en druk en volume zijn "
                  "<strong>omgekeerd evenredig</strong>. Wordt een gas van \\(6{,}0\\) L bij "
                  "\\(100\\) kPa bij dezelfde temperatuur samengeperst tot \\(2{,}0\\) L, dan "
                  "is \\(p_{2} = \\dfrac{100 \\times 6{,}0}{2{,}0} = 300\\) kPa."),
        ]),
        dict(kop="Isobaar: bij constante druk", blokken=[
            ("p", "Bij <strong>constante druk</strong> is het volume recht evenredig met de "
                  "absolute temperatuur: \\[\\dfrac{V}{T} = \\text{cte}\\] Zo'n proces heet "
                  "<strong>isobaar</strong>. Een gas van \\(2{,}0\\) L bij \\(300\\) K dat bij "
                  "gelijke druk tot \\(600\\) K verwarmd wordt, heeft \\(4{,}0\\) L. Een ballon "
                  "van \\(3{,}0\\) L bij \\(20\\ ^\\circ\\text{C}\\) die in een koelkast op "
                  "\\(5\\ ^\\circ\\text{C}\\) gelegd wordt, krimpt tot "
                  "\\(V_{2} = \\dfrac{3{,}0 \\times 278}{293} \\approx 2{,}85\\) L: zet eerst "
                  "om naar \\(293\\) en \\(278\\) kelvin."),
        ]),
        dict(kop="Isochoor: bij constant volume", blokken=[
            ("p", "Bij <strong>constant volume</strong> stijgt de druk als je het gas "
                  "verwarmt: \\[\\dfrac{p}{T} = \\text{cte}\\] Zo'n proces heet "
                  "<strong>isochoor</strong>, dus verloopt een isochoor proces "
                  "<strong>niet</strong> bij constante druk maar bij constant volume. Een "
                  "gesloten vat op \\(2{,}0\\) bar bij \\(250\\) K komt bij \\(500\\) K op "
                  "\\(4{,}0\\) bar. De drie namen samen: <strong>isobaar</strong> bij "
                  "constante druk, <strong>isochoor</strong> bij constant volume, "
                  "<strong>isotherm</strong> bij constante temperatuur."),
        ]),
        dict(kop="De drie grafieken", blokken=[
            ("fig", svg.gaswetten(),
             "Dezelfde drie wetten, elk in de grafiek waarin je ze herkent."),
            ("p", "Een <strong>\\(p(V)\\)-grafiek van een isotherm proces</strong> is een "
                  "kromme die daalt zoals een omgekeerde evenredigheid, dus een "
                  "<strong>hyperbool</strong>. Een <strong>\\(V(T)\\)-grafiek bij constante "
                  "druk</strong> is, met \\(T\\) in kelvin, een <strong>rechte door de "
                  "oorsprong</strong>, en bij constant volume is de "
                  "<strong>\\(p(T)\\)-grafiek</strong> er ook een. In graden celsius snijden "
                  "die rechten de as pas bij \\(-273\\). Een \\(p(T)\\)-grafiek van een "
                  "isotherm proces is iets anders: dat is één <strong>verticale lijn</strong>, "
                  "want \\(T\\) verandert niet terwijl de druk wel verandert."),
        ]),
        dict(kop="De algemene gaswet", blokken=[
            ("p", "Voor een vaste hoeveelheid gas geldt: "
                  "\\[\\dfrac{p\\,V}{T} = \\text{cte} \\quad\\text{of}\\quad "
                  "\\dfrac{p_{1}V_{1}}{T_{1}} = \\dfrac{p_{2}V_{2}}{T_{2}}\\] De drie "
                  "afzonderlijke wetten zijn daar bijzondere gevallen van: houd je er één "
                  "grootheid constant, dan blijft telkens een van de drie over. Gaat een gas "
                  "van \\(2{,}0\\) L bij \\(300\\) K en \\(100\\) kPa naar \\(400\\) K en "
                  "\\(200\\) kPa, dan krijgt het "
                  "\\(V_{2} = \\dfrac{100 \\times 2{,}0 \\times 400}{300 \\times 200} = "
                  "1{,}33\\) L."),
        ]),
        dict(kop="De ideale gaswet", blokken=[
            ("kader", "<strong>De ideale gaswet</strong><br>"
                      "\\[p\\,V = n\\,R\\,T\\]"
                      "\\(n\\) is de stofhoeveelheid in mol en "
                      "\\(R = 8{,}31\\ \\text{J/(mol}\\cdot\\text{K)}\\) de "
                      "<strong>universele gasconstante</strong>, dezelfde voor elk gas. Vul in met "
                      "\\(p\\) in pascal, \\(V\\) in kubieke meter en \\(T\\) in kelvin."),
            ("p", "De grootheid die je <strong>naast druk, volume en temperatuur</strong> moet "
                  "kennen, is dus de <strong>stofhoeveelheid</strong>, en die staat in mol. De "
                  "wet geldt ook voor een <strong>mengsel</strong> van gassen zoals lucht: je "
                  "telt dan alle deeltjes samen als \\(n\\). In een vat van "
                  "\\(0{,}025\\ \\text{m}^{3}\\) bij \\(300\\) K en \\(100\\) kPa zit "
                  "\\(n = \\dfrac{1{,}0 \\times 10^{5} \\times 0{,}025}{8{,}31 \\times 300} "
                  "\\approx 1{,}0\\) mol gas."),
            ("p", "Twee gevolgen van dezelfde wet. <strong>Twee verschillende gassen bij "
                  "dezelfde druk en temperatuur bevatten in hetzelfde volume evenveel "
                  "deeltjes.</strong> En pomp je bij gelijk volume en gelijke temperatuur meer "
                  "gas in een vat, dan blijft de druk <strong>niet</strong> gelijk: ze stijgt, "
                  "want \\(n\\) en \\(p\\) zijn recht evenredig. Bij "
                  "<strong>normomstandigheden</strong>, \\(0\\ ^\\circ\\text{C}\\) en "
                  "\\(101{,}3\\) kPa, neemt één mol van een ideaal gas ongeveer "
                  "\\(22{,}4\\) L in."),
        ]),
        dict(kop="Ideaal en reëel", blokken=[
            ("p", "Een <strong>ideaal gas</strong> is een gas waarvan de deeltjes zelf geen "
                  "eigen volume hebben en geen kracht op elkaar uitoefenen; de botsingen zijn "
                  "volkomen <strong>elastisch</strong>. Zo'n gas bestaat niet echt, maar bij "
                  "lage druk en hoge temperatuur komen echte gassen er dicht bij. Een "
                  "<strong>reëel gas</strong> wijkt dus niet het meest af bij hoge temperatuur "
                  "en lage druk maar juist bij <strong>lage temperatuur en hoge druk</strong>, "
                  "dicht bij het condenseren."),
            ("p", "Het <strong>deeltjesmodel</strong> verklaart ook waar de grootheden vandaan "
                  "komen. De <strong>druk</strong> van een gas op de wand komt van de "
                  "botsingen van de deeltjes tegen die wand. De <strong>temperatuur</strong> "
                  "zegt hoe groot de gemiddelde kinetische energie van de deeltjes is. Het "
                  "<strong>absolute nulpunt</strong> ligt bij \\(-273\\ ^\\circ\\text{C}\\), "
                  "preciezer bij \\(-273{,}15\\)."),
        ]),
        dict(kop="Drie situaties uit het dagelijks leven", blokken=[
            ("p", "De druk in een <strong>fietsband</strong> stijgt als je lang gepompt hebt "
                  "omdat de lucht samengeperst en ook warmer geworden is."),
            ("p", "Op een <strong>spuitbus</strong> staat dat je hem niet boven "
                  "\\(50\\ ^\\circ\\text{C}\\) mag bewaren, omdat bij constant volume de druk "
                  "mee stijgt met de temperatuur: de bus kan niet uitzetten."),
            ("p", "Een <strong>duiker</strong> die op \\(20\\) m diepte lucht inademt bij "
                  "ongeveer \\(3\\) bar, mag bij het opstijgen de adem niet inhouden, want de "
                  "lucht in zijn longen zet bij de dalende druk sterk uit: van \\(3\\) naar "
                  "\\(1\\) bar is een drie keer zo groot volume."),
        ]),
    ],
    onthoud=[
        "Toestandsgrootheden: \\(p\\), \\(V\\), \\(T\\) en \\(n\\).",
        "Reken altijd in kelvin: \\(T = \\theta + 273\\).",
        "Isotherm: \\(p\\,V = \\text{cte}\\). Isobaar: \\(\\dfrac{V}{T} = \\text{cte}\\). "
        "Isochoor: \\(\\dfrac{p}{T} = \\text{cte}\\).",
        "Algemene gaswet: \\(\\dfrac{p\\,V}{T}\\) blijft constant.",
        "Ideale gaswet: \\(p\\,V = n\\,R\\,T\\), met pascal, \\(\\text{m}^{3}\\), kelvin en mol.",
        "Eén mol neemt bij normomstandigheden ongeveer \\(22{,}4\\) L in.",
        "Druk komt van botsingen, \\(T\\) is de gemiddelde kinetische energie.",
    ],
)


# ───────────────────── 15. Warmteleer: temperatuur, warmte en faseovergangen
BUNDELS["warmteleer-temperatuur-warmte-en-faseovergangen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Warmteleer: temperatuur, warmte en faseovergangen",
    onder="Opwarmen, warmte uitwisselen en van fase veranderen zonder dat de thermometer beweegt.",
    secties=[
        dict(kop="Warmte is niet hetzelfde als temperatuur", blokken=[
            ("p", "<strong>Warmte \\(Q\\) is energie die stroomt, temperatuur \\(T\\) is een "
                  "toestand.</strong> Warmte staat daarom in <strong>joule</strong>, "
                  "temperatuur in kelvin. Een voorwerp van \\(1000\\) K bevat "
                  "<strong>niet</strong> altijd meer warmte dan een voorwerp van \\(300\\) K: "
                  "een vonk bevat veel minder energie dan een bad, want de massa en de stof "
                  "tellen even hard mee."),
            ("p", "<strong>Warmte stroomt van het warme naar het koude voorwerp</strong>, "
                  "nooit spontaan de andere kant op. Twee voorwerpen die elkaar raken, houden "
                  "dus <strong>niet</strong> elk hun eigen temperatuur: er stroomt warmte tot "
                  "ze gelijk staan. Die toestand heet <strong>thermisch evenwicht</strong>. "
                  "Een stijging van \\(10\\) K is hetzelfde als een stijging van "
                  "\\(10\\ ^\\circ\\text{C}\\): de twee schalen hebben even grote stappen, "
                  "enkel hun nulpunt verschilt, dus bij een \\(\\Delta T\\) mag je wel in "
                  "celsius rekenen."),
        ]),
        dict(kop="De drie wegen van de warmte", blokken=[
            ("p", "Warmte verplaatst zich op drie manieren: <strong>geleiding</strong>, door "
                  "contact tussen de deeltjes, <strong>stroming</strong>, doordat warm water "
                  "of warme lucht stijgt, en <strong>straling</strong>, doordat een warm "
                  "voorwerp licht uitzendt. Daarom zit er tussen de twee glazen van een "
                  "<strong>thermosfles</strong> een <strong>vacuüm</strong>: zonder deeltjes "
                  "kan er niets geleid of gestroomd worden, en de spiegelende wand houdt de "
                  "straling tegen."),
        ]),
        dict(kop="Meten met een calorimeter", blokken=[
            ("p", "Een <strong>calorimeter</strong> gebruik je om een hoeveelheid uitgewisselde "
                  "warmte te meten. Bij een calorimeterproef geldt: de warmte die de ene stof "
                  "afgeeft, neemt de andere op, en het vat moet zo goed mogelijk "
                  "<strong>geïsoleerd</strong> zijn. De twee stoffen hoeven niet dezelfde massa "
                  "te hebben. Met een <strong>joulevat</strong> meet je hoeveel warmte een "
                  "elektrische weerstand aan water geeft: je meet spanning, stroom en tijd, en "
                  "de temperatuurstijging laat zien dat die energie warmte geworden is."),
        ]),
        dict(kop="Warmtecapaciteit", blokken=[
            ("kader", "<strong>Opwarmen</strong><br>"
                      "\\[Q = c\\,m\\,\\Delta T \\qquad Q = C\\,\\Delta T\\]"
                      "\\(C\\) is de <strong>warmtecapaciteit</strong> van een voorwerp, in "
                      "\\(\\text{J/K}\\); \\(c\\) is de <strong>specifieke "
                      "warmtecapaciteit</strong> van een stof: de warmte voor één kilogram "
                      "en één kelvin, in \\(\\text{J/(kg}\\cdot\\text{K)}\\). In \\(C\\) zit "
                      "de massa al mee."),
            ("p", "\\(c\\) hangt af van de stof en niet van de massa, en water heeft een hoge "
                  "waarde in vergelijking met metalen: "
                  "\\(c_{\\text{water}} = 4186\\ \\text{J/(kg}\\cdot\\text{K)}\\). Daarom warmt "
                  "een <strong>pan</strong> sneller op dan het water erin: het metaal heeft een "
                  "veel lagere \\(c\\)."),
        ]),
        dict(kop="Rekenen aan het opwarmen", blokken=[
            ("p", "\\(2{,}0\\) kg water \\(10\\) K opwarmen vraagt "
                  "\\(Q = 4186 \\times 2{,}0 \\times 10 = 8{,}37 \\times 10^{4}\\) J, dus "
                  "ongeveer \\(84\\) kJ. Giet je \\(1{,}0\\) kg water van "
                  "\\(80\\ ^\\circ\\text{C}\\) bij \\(1{,}0\\) kg water van "
                  "\\(20\\ ^\\circ\\text{C}\\), dan krijg je \\(50\\ ^\\circ\\text{C}\\): bij "
                  "gelijke massa's ligt het antwoord precies in het midden, want de warmte die "
                  "het ene afgeeft, neemt het andere op."),
        ]),
        dict(kop="De zes faseovergangen", blokken=[
            ("fig", svg.faseovergangen(),
             "Oranje: er gaat warmte bij. Blauw: er gaat warmte weg."),
        ]),
        dict(kop="Welke nemen warmte op?", blokken=[
            ("p", "De zes faseovergangen komen in drie paren: <strong>smelten en "
                  "stollen</strong>, <strong>verdampen en condenseren</strong>, "
                  "<strong>sublimeren en rijpen</strong>. Smelten is vast naar vloeibaar, "
                  "condenseren gas naar vloeistof, sublimeren vast rechtstreeks naar gas, en "
                  "rijpen gas rechtstreeks naar vast. <strong>Smelten, verdampen en "
                  "sublimeren</strong> nemen warmte op, want ze gaan naar een lossere toestand; "
                  "stollen, condenseren en rijpen geven warmte af aan hun omgeving."),
        ]),
        dict(kop="Een vlak stuk op de curve", blokken=[
            ("fig", svg.verwarmingscurve(),
             "Dezelfde massa water, van ijs tot stoom, bij steeds meer toegevoerde warmte."),
            ("p", "Tijdens het smelten blijft de temperatuur van een zuivere stof "
                  "<strong>gelijk</strong>, want alle warmte gaat naar het losmaken van de "
                  "deeltjes. Op een <strong>smeltcurve</strong> zie je daarom een stijging, dan "
                  "een horizontaal stuk, dan weer een stijging; op een "
                  "<strong>stolcurve</strong> een daling, dan een horizontaal stuk, dan weer "
                  "een daling. Een <strong>mengsel</strong> heeft geen scherp smeltpunt zoals "
                  "een zuivere stof: het smelt over een temperatuurgebied, dus is dat stuk niet "
                  "vlak."),
        ]),
        dict(kop="Rekenen aan een faseovergang", blokken=[
            ("kader", "<strong>Van fase veranderen</strong><br>"
                      "\\[Q = l\\,m\\]"
                      "\\(l\\) is de <strong>specifieke smelt-, verdampings- of "
                      "sublimatiewarmte</strong>: de warmte per kilogram, in "
                      "\\(\\text{J/kg}\\). Er staat geen "
                      "\\(\\Delta T\\) in, want de temperatuur verandert niet."),
        ]),
        dict(kop="Smelten en verdampen in cijfers", blokken=[
            ("p", "\\(0{,}50\\) kg ijs van \\(0\\ ^\\circ\\text{C}\\) laten smelten vraagt "
                  "\\(Q = 334 \\times 0{,}50 = 167\\) kJ. De specifieke verdampingswarmte van "
                  "water is <strong>veel groter</strong> dan zijn smeltwarmte: \\(2256\\) "
                  "tegenover \\(334\\) kJ/kg. Wil je \\(1{,}0\\) kg water "
                  "opwarmen van \\(20\\) naar \\(100\\ ^\\circ\\text{C}\\) en dan laten "
                  "verdampen, dan kost het <strong>verdampen</strong> veruit het meest: "
                  "\\(2256\\) tegenover \\(335\\) kJ."),
            ("p", "Daarom voelt het <strong>koel</strong> aan als er water op je huid "
                  "verdampt: het verdampende water neemt die warmte van je huid mee. Dat is net "
                  "waarom zweten werkt."),
        ]),
        dict(kop="Kookpunt en smeltpunt verschuiven", blokken=[
            ("p", "Het <strong>kookpunt</strong> hangt af van de druk boven de vloeistof: bij "
                  "lagere druk ligt het lager, en het is altijd hoger dan het smeltpunt van de "
                  "stof. \\(100\\ ^\\circ\\text{C}\\) is het kookpunt van water bij normale "
                  "druk, niet van elke vloeistof. Daarom gaat koken in een "
                  "<strong>snelkookpan</strong> sneller: de hogere druk duwt het kookpunt naar "
                  "boven, en heter water gaart het eten vlugger."),
        ]),
        dict(kop="Zout op een besneeuwde weg", blokken=[
            ("p", "Men strooit <strong>zout</strong> op een besneeuwde weg omdat het zout het "
                  "smeltpunt van het ijs <strong>verlaagt</strong>: pekel bevriest pas onder "
                  "\\(0\\ ^\\circ\\text{C}\\). Bij strenge vorst werkt dat niet meer."),
        ]),
    ],
    onthoud=[
        "Warmte is energie die stroomt en gaat altijd van warm naar koud, tot het "
        "thermisch evenwicht.",
        "Geleiding, stroming en straling zijn de drie wegen.",
        "Opwarmen: \\(Q = c\\,m\\,\\Delta T\\); water heeft \\(c = 4186\\).",
        "Zes faseovergangen; smelten, verdampen en sublimeren nemen warmte op.",
        "Tijdens een faseovergang blijft \\(T\\) gelijk: \\(Q = l\\,m\\); verdampen kost "
        "veel meer dan smelten.",
        "Lagere druk verlaagt het kookpunt; zout verlaagt het smeltpunt.",
    ],
)


# ───────────────────── 16. Harmonische trillingen
BUNDELS["harmonische-trillingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Harmonische trillingen",
    onder="Eén vergelijking voor de hele beweging, van amplitude tot resonantie.",
    secties=[
        dict(kop="Wat een harmonische trilling is", blokken=[
            ("p", "Een <strong>harmonische trilling</strong> is een beweging waarvan de "
                  "uitwijking een <strong>sinus van de tijd</strong> is. Een massa aan een "
                  "veer en een slinger met een kleine uitslag zijn de twee "
                  "schoolvoorbeelden."),
            ("p", "De <strong>amplitude \\(A\\)</strong> is de grootste uitwijking, in meter; "
                  "ze kan <strong>geen negatieve waarde</strong> hebben. De uitwijking "
                  "\\(y\\) zelf wel: die krijgt aan de ene kant van de evenwichtslijn een "
                  "minteken. De <strong>evenwichtslijn</strong> is de stand waar het lichaam "
                  "zonder trilling zou blijven."),
        ]),
        dict(kop="De grafiek lezen", blokken=[
            ("fig", svg.trillingsgrafiek(),
             "Links een vrije trilling, rechts dezelfde trilling met wrijving erbij."),
            ("p", "De <strong>periode \\(T\\)</strong> is de tijd van één volledige "
                  "heen-en-terugbeweging, in seconde, en de frequentie is haar omgekeerde: "
                  "\\[f = \\dfrac{1}{T}\\] Een trilling met \\(T = 0{,}25\\) s heeft dus "
                  "\\(f = 4{,}0\\) Hz, en een trilling met een <strong>hogere frequentie heeft "
                  "een kleinere periode</strong>."),
        ]),
        dict(kop="De trillingsvergelijking", blokken=[
            ("kader", "<strong>Eén vergelijking voor de hele beweging</strong><br>"
                      "\\[y(t) = A\\sin(\\omega t + \\varphi)\\]"
                      "\\(A\\) is de amplitude in meter, \\(\\omega\\) de pulsatie in "
                      "\\(\\text{rad/s}\\) en \\(\\varphi\\) de beginfase in radiaal. De massa "
                      "staat er niet in."),
            ("p", "Daaruit lees je rechtstreeks de <strong>amplitude</strong>, de "
                  "<strong>pulsatie</strong> en de <strong>beginfase</strong>. Om er zelf een "
                  "op te stellen heb je de amplitude, de periode of de frequentie, en de "
                  "beginfase nodig; de massa van het lichaam hoeft niet."),
        ]),
        dict(kop="De pulsatie en de beginfase", blokken=[
            ("p", "De <strong>pulsatie</strong> is \\[\\omega = \\dfrac{2\\pi}{T} = 2\\pi f\\] "
                  "in \\(\\text{rad/s}\\); ze heet ook de hoeksnelheid. Ze wordt "
                  "<strong>kleiner</strong> als \\(T\\) groter wordt, want \\(T\\) staat in de "
                  "noemer, en ze is iets heel anders dan \\(T\\) zelf."),
            ("p", "Een <strong>beginfase van nul</strong> betekent dat de trilling op "
                  "\\(t = 0\\) uit de evenwichtsstand vertrekt, want \\(\\sin 0 = 0\\). "
                  "Vertrekt ze uit de uiterste stand, dan is "
                  "\\(\\varphi = \\tfrac{\\pi}{2}\\). Een trilling met \\(A = 5\\) cm, "
                  "\\(\\omega = 4\\) rad/s en \\(\\varphi = 0\\) heeft na een halve periode de "
                  "uitwijking <strong>nul</strong>, want de fase is dan \\(\\pi\\) en "
                  "\\(\\sin \\pi = 0\\)."),
        ]),
        dict(kop="Snelheid en versnelling tijdens de trilling", blokken=[
            ("p", "Twee dingen die altijd gelden: de uitwijking is <strong>nul in de "
                  "evenwichtsstand</strong> en de snelheid is <strong>nul in de uiterste "
                  "stand</strong>. De snelheid is dus <strong>niet</strong> het grootst in de "
                  "uiterste stand maar in de evenwichtsstand. De <strong>versnelling</strong> "
                  "is net omgekeerd het grootst in de <strong>uiterste standen</strong>, waar "
                  "de uitwijking maximaal is, want daar is de terugroepkracht het grootst; in "
                  "de evenwichtsstand is ze nul."),
            ("p", "De amplitude doet niets met de periode: verdubbel je de amplitude van een "
                  "slinger met een kleine uitslag, dan blijft de periode ongeveer gelijk. Dat "
                  "is net waarom een slingeruurwerk zo nauwkeurig was."),
        ]),
        dict(kop="Faseverschil", blokken=[
            ("p", "Het <strong>faseverschil \\(\\Delta\\varphi\\)</strong> tussen twee "
                  "harmonische trillingen is het verschil tussen hun fasen op hetzelfde "
                  "tijdstip, in radiaal. Ze trillen <strong>in fase</strong> als "
                  "\\(\\Delta\\varphi = 0\\) of een veelvoud van \\(2\\pi\\) is, en "
                  "<strong>in tegenfase</strong> als \\(\\Delta\\varphi = \\pi\\). Hebben twee "
                  "trillingen dezelfde frequentie en \\(\\Delta\\varphi = \\tfrac{\\pi}{2}\\), "
                  "dan is de ene een <strong>kwart periode</strong> voor op de andere: staat de "
                  "ene in de evenwichtsstand, dan staat de andere uiterst."),
        ]),
        dict(kop="De veer", blokken=[
            ("kader", "<strong>Terugroepkracht en eigenfrequentie</strong><br>"
                      "\\[F = -k\\,y \\qquad f_{0} = \\dfrac{1}{2\\pi}\\sqrt{\\dfrac{k}{m}}\\]"
                      "\\(k\\) is de <strong>krachtconstante</strong> van de veer, in "
                      "\\(\\text{N/m}\\). Het minteken zegt dat de kracht altijd naar de "
                      "evenwichtsstand wijst."),
            ("p", "Bij een <strong>massa-veersysteem</strong> is de terugroepkracht de "
                  "kracht van de veer, naar de evenwichtsstand <strong>gericht</strong>. Ze "
                  "is recht evenredig met de uitwijking en altijd tegengesteld eraan, en net "
                  "daardoor is de beweging harmonisch. Een "
                  "<strong>stijvere veer</strong> geeft een hogere eigenfrequentie en een "
                  "<strong>grotere massa</strong> een lagere. Hang je een dubbel zo zware "
                  "massa aan dezelfde veer, dan wordt \\(f_{0}\\) kleiner met een factor "
                  "\\(\\sqrt{2}\\); de amplitude doet er niet toe."),
        ]),
        dict(kop="De slinger", blokken=[
            ("p", "Voor een slinger met een kleine uitslag geldt "
                  "\\[f_{0} = \\dfrac{1}{2\\pi}\\sqrt{\\dfrac{g}{\\ell}}\\] De eigenfrequentie "
                  "hangt dus af van zijn <strong>lengte</strong> en van de "
                  "<strong>valversnelling</strong>, en niet van de massa van de bol. Een "
                  "<strong>langere slinger trilt langzamer</strong> dan een korte, want "
                  "\\(\\ell\\) staat onder de wortel in de noemer."),
        ]),
        dict(kop="Demping", blokken=[
            ("p", "Bij een <strong>gedempte</strong> harmonische trilling neemt niet de "
                  "frequentie af maar de <strong>amplitude</strong>: de uitwijking verloopt "
                  "als een sinus die tussen twee <strong>krimpende grenzen</strong> past. De "
                  "energie van de trilling verdwijnt daarbij naar de omgeving, als warmte door "
                  "wrijving en luchtweerstand. Zo komt een schommel zonder duw tot stilstand."),
        ]),
        dict(kop="Resonantie", blokken=[
            ("p", "Een <strong>gedwongen trilling</strong> is een trilling die een uitwendige "
                  "kracht blijft aandrijven; het lichaam neemt dan de frequentie van die "
                  "kracht over. De <strong>eigenfrequentie</strong> is de frequentie waarmee "
                  "een lichaam vrij trilt. <strong>Resonantie</strong> treedt op als de "
                  "frequentie van de kracht de eigenfrequentie benadert: de amplitude wordt "
                  "dan <strong>veel groter</strong>, met een kleine kracht."),
            ("p", "Voorbeelden: een schommel die je op het juiste ritme steeds hoger duwt, een "
                  "glas dat breekt bij een zuivere toon van de juiste hoogte, en een brug die "
                  "door marcherende stappen hevig begint te trillen. Daarom zet men "
                  "<strong>dempers</strong> in een gebouw dat tegen aardbevingen moet kunnen: "
                  "om de amplitude bij resonantie klein te houden. De bodem zelf krijg je niet "
                  "stil."),
        ]),
    ],
    onthoud=[
        "Harmonisch: de uitwijking is een sinus van de tijd.",
        "\\(y(t) = A\\sin(\\omega t + \\varphi)\\); daaruit lees je \\(A\\), \\(\\omega\\) en \\(\\varphi\\).",
        "\\(\\omega = \\dfrac{2\\pi}{T} = 2\\pi f\\), in \\(\\text{rad/s}\\).",
        "Snelheid maximaal in het evenwicht, versnelling maximaal uiterst.",
        "De periode hangt niet van de amplitude af.",
        "Veer: \\(f_{0} = \\dfrac{1}{2\\pi}\\sqrt{\\dfrac{k}{m}}\\); slinger: \\(\\ell\\) en \\(g\\), niet de massa.",
        "Resonantie: aandrijven op de eigenfrequentie geeft een grote amplitude.",
    ],
)


# ───────────────────── 17. Golven en hun eigenschappen
BUNDELS["golven-en-hun-eigenschappen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Golven en hun eigenschappen",
    onder="Een trilling die zich voortplant, en de vier dingen die ze onderweg kan doen.",
    secties=[
        dict(kop="Wat een golf vervoert", blokken=[
            ("p", "Een golf vervoert <strong>energie, maar geen materie</strong>. De deeltjes "
                  "trillen rond hun eigen evenwichtsstand en blijven dus ter plaatse; enkel de "
                  "trilling schuift door. De richting waarin ze heen en weer gaan, heet de "
                  "<strong>trilrichting</strong> of trillingsrichting."),
            ("p", "Een <strong>mechanische golf heeft een stof nodig</strong> om door te gaan, "
                  "een <strong>elektromagnetische</strong> niet: zichtbaar licht, radiogolven "
                  "en röntgenstraling lopen ook door vacuüm, geluid niet. Een "
                  "<strong>transversale</strong> golf is er een waarbij de deeltjes "
                  "<strong>dwars</strong> op de voortplantingsrichting trillen; trillen ze "
                  "<strong>langs</strong> die richting, dan is de golf "
                  "<strong>longitudinaal</strong>. Geluid in de lucht bestaat uit "
                  "longitudinale golven."),
        ]),
        dict(kop="De golf in beeld", blokken=[
            ("fig", svg.golfbeeld(),
             "Links een golf die doorloopt, rechts een golf die tussen twee wanden vastzit."),
            ("p", "De <strong>golflengte \\(\\lambda\\)</strong> is de afstand tussen twee "
                  "punten die in fase trillen, bijvoorbeeld van berg tot berg. De "
                  "<strong>amplitude \\(A\\)</strong> is de grootste uitwijking, dwars op de "
                  "golf. Twee heel verschillende dingen dus: \\(\\lambda\\) is een afstand "
                  "<strong>langs</strong> de golf, \\(A\\) een uitwijking "
                  "<strong>dwars</strong> erop."),
        ]),
        dict(kop="Golflengte, frequentie en snelheid", blokken=[
            ("kader", "<strong>De golfsnelheid</strong><br>"
                      "\\[v = \\lambda\\,f = \\dfrac{\\lambda}{T}\\]"
                      "In één periode schuift de golf precies één golflengte op. Een golf met "
                      "\\(\\lambda = 2{,}0\\) m en \\(f = 50\\) Hz loopt dus \\(100\\) m/s."),
            ("p", "De snelheid hangt af van de <strong>stof</strong> waar de golf door loopt, "
                  "niet van hoe hard je de bron aanslaat: een golf met een grotere amplitude "
                  "loopt <strong>niet</strong> sneller. Alle deeltjes op een lopende golf "
                  "trillen met <strong>dezelfde frequentie</strong>, want ze krijgen allemaal "
                  "het ritme van de bron. Verhoog je \\(f\\), dan krimpt \\(\\lambda\\) en "
                  "blijft \\(v\\) gelijk."),
        ]),
        dict(kop="De golfvergelijking", blokken=[
            ("kader", "<strong>Eén vergelijking voor plaats en tijd</strong><br>"
                      "\\[y(x,t) = A\\sin(\\omega t - k\\,x) \\qquad k = \\dfrac{2\\pi}{\\lambda}\\]"
                      "\\(k\\) is het <strong>golfgetal</strong>, in \\(\\text{rad/m}\\): de "
                      "ruimtelijke tegenhanger van de pulsatie "
                      "\\(\\omega = \\dfrac{2\\pi}{T}\\). Het minteken hoort bij een golf die "
                      "naar <strong>rechts</strong> loopt: een rechtslopende golf."),
            ("p", "Daaruit lees je de <strong>amplitude</strong>, de <strong>pulsatie</strong> "
                  "en dus \\(T\\), en het <strong>golfgetal</strong> en dus \\(\\lambda\\). De "
                  "stof staat er niet in, al bepaalt die wel de snelheid."),
        ]),
        dict(kop="Wie wanneer begint te trillen", blokken=[
            ("p", "<strong>Niet alle deeltjes</strong> van een lopende golf beginnen op "
                  "hetzelfde ogenblik te trillen: de trilling moet er eerst toe komen. Trilt "
                  "een bron al \\(3{,}0\\) s, ligt een deeltje \\(10\\) m verder en loopt de "
                  "golf \\(5{,}0\\) m/s, dan was de golf "
                  "\\(\\dfrac{10}{5{,}0} = 2{,}0\\) s onderweg en trilt dat deeltje nog maar "
                  "\\(1{,}0\\) s. Loopt een golf naar <strong>rechts</strong>, dan beweegt een "
                  "deeltje dat net vóór een berg ligt <strong>naar boven</strong>, want die "
                  "berg schuift naar hem toe."),
        ]),
        dict(kop="Huygens: weerkaatsen, breken, buigen", blokken=[
            ("p", "Het <strong>principe van Huygens</strong> zegt dat elk punt van een "
                  "golffront zelf als een <strong>nieuwe bron</strong> werkt. Daarmee verklaar "
                  "je <strong>weerkaatsing</strong> of reflectie, waarbij de golf tegen een "
                  "wand terugkaatst, <strong>breking</strong> of refractie, en "
                  "<strong>buiging</strong> of diffractie, waarbij de golf kan afbuigen rond "
                  "een hoek. Demping hoort er niet "
                  "bij: dat is een verlies van energie en geen gevolg van het golffront."),
        ]),
        dict(kop="Breking en de wet van Snellius", blokken=[
            ("kader", "<strong>De wet van Snellius</strong><br>"
                      "\\[\\dfrac{\\sin i}{\\sin r} = \\dfrac{n_{r}}{n_{i}} \\qquad "
                      "n = \\dfrac{c}{v}\\]"
                      "De wet geldt voor de <strong>sinussen</strong> van de hoeken, niet voor "
                      "de hoeken zelf. Let op welke brekingsindex boven staat."),
            ("p", "Bij breking veranderen de <strong>snelheid</strong>, de "
                  "<strong>golflengte</strong> en de <strong>richting</strong>, maar de "
                  "<strong>frequentie niet</strong>: die blijft van de bron. Bij de overgang "
                  "naar een stof met een <strong>hogere</strong> brekingsindex breekt de straal "
                  "naar de normaal <strong>toe</strong>. Een brekingsindex van \\(1{,}5\\) "
                  "betekent dat licht er \\(1{,}5\\) keer <strong>langzamer</strong> gaat dan "
                  "in vacuüm, want \\(n = \\dfrac{c}{v}\\). Daarom lijkt een rietje in een glas "
                  "water geknikt."),
            ("p", "Buiging lukt beter bij een grote golflengte. Daarom hoor je een laag "
                  "gebrom van een feest verder dan de hoge tonen: lage tonen hebben een "
                  "grotere \\(\\lambda\\) en buigen beter af rond huizen en hoeken. De buiging "
                  "is het sterkst achter een smalle opening, even groot als "
                  "\\(\\lambda\\) of kleiner."),
        ]),
        dict(kop="Interferentie", blokken=[
            ("p", "<strong>Interferentie</strong> is twee golven die samen één nieuwe "
                  "uitwijking geven: je telt de uitwijkingen punt per punt op, en daarna lopen "
                  "beide golven gewoon verder. Van <strong>constructieve</strong> "
                  "interferentie spreek je als ze er <strong>in fase</strong> aankomen; bij "
                  "<strong>destructieve</strong> "
                  "interferentie, in tegenfase en met dezelfde amplitude, kunnen ze elkaar "
                  "volledig <strong>uitdoven</strong>. Een koptelefoon met ruisonderdrukking "
                  "werkt zo. Twee bronnen zijn <strong>coherent</strong> als ze dezelfde "
                  "frequentie en een <strong>vast faseverschil</strong> hebben; alleen dan "
                  "blijft het patroon op zijn plaats staan."),
        ]),
        dict(kop="Staande golven", blokken=[
            ("p", "Een <strong>staande golf</strong> ontstaat door interferentie van een golf "
                  "met haar eigen <strong>weerkaatsing</strong>. Een punt dat helemaal niet "
                  "trilt, heet een <strong>knoop</strong> of knooppunt; het punt dat het "
                  "hevigst trilt, een "
                  "<strong>buik</strong>. De knopen schuiven niet op, en dat is net het "
                  "kenmerk van een staande golf. In fase met elkaar trillen de punten "
                  "<strong>tussen twee opeenvolgende knopen</strong>; over een knoop heen is "
                  "\\(\\Delta\\varphi = \\pi\\), dus tegenfase."),
        ]),
    ],
    onthoud=[
        "Een golf vervoert energie, geen materie.",
        "Mechanisch heeft een stof nodig; elektromagnetisch niet.",
        "Transversaal trilt dwars, longitudinaal langs de looprichting.",
        "\\(v = \\lambda\\,f\\); de stof bepaalt \\(v\\), de bron bepaalt \\(f\\).",
        "\\(y(x,t) = A\\sin(\\omega t - k\\,x)\\), met \\(k = \\dfrac{2\\pi}{\\lambda}\\).",
        "Huygens verklaart weerkaatsing, breking en buiging.",
        "Bij breking verandert alles behalve de frequentie.",
        "Staande golf: knopen trillen niet, buiken maximaal.",
    ],
)


# ───────────────────── 18. Licht, geluid en het elektromagnetisch spectrum
BUNDELS["licht-geluid-en-het-elektromagnetisch-spectrum-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Licht, geluid en het elektromagnetisch spectrum",
    onder="Van spiegel en lens tot decibel en dopplereffect.",
    secties=[
        dict(kop="Licht als elektromagnetische golf", blokken=[
            ("p", "Een <strong>elektromagnetische golf</strong> is een "
                  "<strong>transversale</strong> golf waarin een elektrisch en een magnetisch "
                  "veld samen trillen. Ze heeft <strong>geen stof nodig</strong>: licht, "
                  "radiogolven en röntgenstraling lopen ook door vacuüm. Geluid kan dat niet, "
                  "want dat is een <strong>mechanische</strong> golf."),
            ("kader", "<strong>De lichtsnelheid</strong><br>"
                      "\\[c = 3{,}00 \\times 10^{8}\\ \\text{m/s} \\qquad n = \\dfrac{c}{v}\\]"
                      "Dat is \\(300\\,000\\,000\\) meter per seconde. In een stof "
                      "gaat licht langzamer, en net dat drukt de brekingsindex \\(n\\) uit."),
            ("p", "In water is \\(n \\approx 1{,}33\\), in glas ongeveer \\(1{,}5\\). Licht "
                  "gaat er dus \\(1{,}33\\) of \\(1{,}5\\) keer trager dan in vacuüm, en "
                  "daarom breekt het aan het oppervlak."),
        ]),
        dict(kop="Weerkaatsing en de vlakke spiegel", blokken=[
            ("p", "Bij een <strong>glad</strong> oppervlak kaatsen alle stralen netjes dezelfde "
                  "kant op: dat is <strong>regelmatige</strong> weerkaatsing. Bij een "
                  "<strong>ruw</strong> oppervlak kaatsen ze alle kanten op, en dat heet "
                  "<strong>diffuse</strong> weerkaatsing. Daarom zie je jezelf in een spiegel "
                  "en niet in een blad papier."),
        ]),
        dict(kop="Het beeld in een vlakke spiegel", blokken=[
            ("p", "Het beeld in een vlakke spiegel is <strong>virtueel</strong>, staat "
                  "<strong>rechtop</strong> en is <strong>even groot</strong> als het voorwerp. "
                  "Het ligt even ver achter de spiegel als het voorwerp ervoor. Links en rechts "
                  "lijken verwisseld, boven en onder niet."),
            ("p", "Een <strong>virtueel beeld</strong> kan je <strong>niet</strong> op een "
                  "scherm opvangen: de stralen komen er niet echt samen, ze lijken er enkel "
                  "vandaan te komen. Een <strong>reëel beeld</strong> kan je er wel op vangen."),
        ]),
        dict(kop="Schaduw en verduistering", blokken=[
            ("p", "In de <strong>kernschaduw</strong> komt er van de bron <strong>geen</strong> "
                  "licht meer toe, in de <strong>bijschaduw</strong> nog van een deel ervan. "
                  "Een puntbron geeft daarom alleen kernschaduw, een grote lamp allebei."),
            ("p", "Bij een <strong>zonsverduistering</strong> staat de <strong>maan</strong> "
                  "tussen de zon en de aarde; bij een <strong>maansverduistering</strong> staat "
                  "de <strong>aarde</strong> ertussen en valt haar schaduw op de maan."),
        ]),
        dict(kop="De bolle lens", blokken=[
            ("fig", svg.lensbeeld(),
             "Twee hulpstralen vanuit de top van het voorwerp snijden elkaar rechts."),
            ("p", "Het <strong>brandpunt</strong> \\(F\\) van een bolle lens is het punt waar "
                  "stralen die <strong>evenwijdig met de optische as</strong> binnenkomen, "
                  "samenkomen. De afstand van de lens tot dat punt is de "
                  "<strong>brandpuntsafstand</strong> \\(f\\). Een bolle lens heeft een "
                  "brandpunt aan elke kant."),
        ]),
        dict(kop="Welk beeld krijg je?", blokken=[
            ("p", "Staat het voorwerp <strong>verder dan \\(2f\\)</strong>, dan is het beeld "
                  "<strong>reëel, omgekeerd en kleiner</strong>. Dat doet de lens van een "
                  "fototoestel. Staat het <strong>tussen \\(f\\) en \\(2f\\)</strong>, dan is "
                  "het beeld reëel, omgekeerd en <strong>groter</strong>, zoals bij een "
                  "beamer. Staat het <strong>binnen \\(f\\)</strong>, dan krijg je een "
                  "<strong>virtueel</strong>, rechtopstaand en groter beeld: een vergrootglas."),
        ]),
        dict(kop="Het elektromagnetisch spectrum", blokken=[
            ("fig", svg.emspectrum(),
             "Eén balk, van radiogolven links tot gammastraling rechts."),
            ("p", "Van lage naar hoge frequentie: <strong>radiogolven, microgolven, infrarood, "
                  "zichtbaar licht, uv, röntgen, gamma</strong>. Het zijn allemaal dezelfde "
                  "soort golf, met dezelfde snelheid in vacuüm; alleen \\(\\lambda\\) en "
                  "\\(f\\) verschillen. Zichtbaar licht is maar een smalle strook in het midden."),
        ]),
        dict(kop="Het foton", blokken=[
            ("kader", "<strong>De energie van een foton</strong><br>"
                      "\\[E = h\\,f = \\dfrac{h\\,c}{\\lambda} \\qquad "
                      "h = 6{,}63 \\times 10^{-34}\\ \\text{J}\\cdot\\text{s}\\]"
                      "Een <strong>foton</strong> is het kleinste pakketje energie van licht. "
                      "Hoe hoger \\(f\\), hoe groter \\(E\\): de energie stijgt met de frequentie "
                      "en daalt met de golflengte. Een foton heet ook een lichtkwantum."),
            ("p", "<strong>Ioniserend</strong> zijn <strong>röntgenstraling</strong>, "
                  "<strong>gammastraling</strong> en harde <strong>uv-straling</strong>: hun "
                  "fotonen dragen genoeg energie om een elektron uit een atoom te slaan. "
                  "Radiogolven en microgolven kunnen dat niet. Een magnetron verwarmt dan ook "
                  "niet door te ioniseren, maar door watermoleculen te laten trillen."),
        ]),
        dict(kop="Waar het spectrum voor dient", blokken=[
            ("p", "<strong>Radiogolven</strong> gebruikt men voor communicatie over grote afstand "
                  "omdat ze een groot doordringend vermogen hebben en goed afbuigen. "
                  "<strong>Infrarood</strong> zit in een nachtkijker en een warmtecamera. "
                  "<strong>Röntgenstraling</strong> gaat door een koffer maar niet door metaal: "
                  "dat is wat een bagagescanner op de luchthaven gebruikt."),
        ]),
        dict(kop="Beschermen tegen straling", blokken=[
            ("p", "Welke maatregelen beschermen tegen hoogenergetische straling? Die met "
                  "<strong>zonnecrème en een zonnebril</strong> tegen uv, een "
                  "<strong>loden schort</strong> bij een röntgenfoto, en door zo kort en zo "
                  "weinig mogelijk blootgesteld te worden. Gammastraling gaat door glas heen "
                  "alsof het er niet is; daar heb je lood of beton voor nodig. "
                  "<strong>Afstand, tijd en afscherming</strong> zijn de drie sleutels."),
        ]),
        dict(kop="De proef van Young", blokken=[
            ("p", "Laat je licht door <strong>twee smalle spleten</strong> vallen, dan "
                  "verschijnt op het scherm erachter een patroon van <strong>lichte en donkere "
                  "strepen</strong>. Dat is <strong>interferentie</strong>, en dat kan alleen "
                  "een golf. De proef van Young bewijst dus dat licht zich als een golf "
                  "gedraagt."),
            ("p", "Voor interferentie heb je <strong>twee coherente bronnen</strong> nodig: "
                  "dezelfde frequentie en een <strong>vast faseverschil</strong>. Eén bron "
                  "achter twee spleten zorgt daar vanzelf voor."),
        ]),
        dict(kop="Geluid is een mechanische golf", blokken=[
            ("p", "Geluid loopt het <strong>snelst in vaste stoffen</strong>: in staal sneller "
                  "dan in water, en in water sneller dan in lucht. Hoe steviger de deeltjes aan "
                  "elkaar hangen, hoe vlugger ze de verdichting doorgeven. In "
                  "<strong>vacuüm</strong> loopt geluid helemaal niet, want er is niets om door "
                  "te gaan."),
            ("p", "In <strong>warme</strong> lucht gaat geluid sneller dan in koude: rond "
                  "\\(20\\ ^\\circ\\text{C}\\) is \\(v = 343\\) m/s. Zie je een bliksem en hoor "
                  "je de donder \\(6{,}0\\) s later, dan is het onweer "
                  "\\(d = v\\,t = 340 \\times 6{,}0 = 2040\\) m ver. Het licht is er zo goed "
                  "als meteen."),
        ]),
        dict(kop="Toonhoogte, toonsterkte en klankkleur", blokken=[
            ("p", "De <strong>frequentie</strong> bepaalt de <strong>toonhoogte</strong>: een "
                  "hogere \\(f\\) geeft een hogere toon. De <strong>amplitude</strong> bepaalt "
                  "hoe <strong>luid</strong> het klinkt. De <strong>vorm</strong> van het "
                  "patroon in de tijd bepaalt de <strong>klankkleur</strong> of "
                  "<strong>timbre</strong>: daaraan hoor je het verschil tussen een viool en "
                  "een fluit die dezelfde toon spelen."),
        ]),
        dict(kop="Het gehoorgebied", blokken=[
            ("p", "Een mens hoort normaal van \\(20\\) Hz tot \\(20\\,000\\) Hz. Daaronder "
                  "heet het <strong>infrasoon</strong>, daarboven <strong>ultrasoon</strong>. "
                  "Een echografie bij de dokter, een vleermuis die zijn weg zoekt en een sonar die de diepte van de zee meet, "
                  "zijn drie toepassingen van ultrasoon geluid: ze meten een afstand uit de "
                  "tijd die de echo nodig heeft. Met de jaren verdwijnt de bovenkant van het "
                  "gehoorgebied."),
        ]),
        dict(kop="De decibelschaal", blokken=[
            ("kader", "<strong>Logaritmisch, niet gewoon</strong><br>"
                      "\\[+10\\ \\text{dB} \;\\Rightarrow\; I \\times 10 \\qquad "
                      "I \\sim \\dfrac{1}{r^{2}}\\]"
                      "\\(0\\) dB is de gehoordrempel, \\(80\\) dB de gevaargrens en \\(120\\) "
                      "dB de pijndrempel. \\(60\\) dB is dus \\(10^{3}\\) keer zo intens als "
                      "\\(30\\) dB, niet twee keer."),
            ("p", "Omdat het vermogen zich over een boloppervlak verdeelt, gaat de intensiteit "
                  "met \\(\\dfrac{1}{r^{2}}\\): ga je <strong>twee keer zo dicht</strong> bij "
                  "een geluidsbron staan, dan wordt de geluidsintensiteit <strong>vier keer</strong> "
                  "zo groot."),
        ]),
        dict(kop="Gehoorschade voorkomen", blokken=[
            ("p", "Blijvende gehoorschade ontstaat doordat de <strong>trilhaartjes van de "
                  "haarcellen</strong> in het binnenoor afbreken; die groeien niet terug. "
                  "Schade hangt <strong>zowel van het geluidsniveau als van de duur van de "
                  "blootstelling</strong> af, dus een lange avond kan erger zijn dan één knal. "
                  "Wat helpt: <strong>oordopjes</strong> die gelijkmatig dempen, "
                  "<strong>verder</strong> van de luidspreker staan en tussendoor een "
                  "<strong>pauze</strong> op een stillere plek."),
        ]),
        dict(kop="Grondtoon en boventonen", blokken=[
            ("kader", "<strong>De harmonischen van een snaar</strong><br>"
                      "\\[f_{n} = n\\,f_{1}\\]"
                      "\\(f_{1}\\) is de <strong>grondfrequentie</strong>: de laagste frequentie "
                      "waarop de snaar als staande golf kan trillen. Bij \\(f_{1} = 220\\) Hz heeft "
                      "de derde harmonische \\(f_{3} = 660\\) Hz."),
            ("p", "De boventonen klinken mee naast de grondtoon, en hun onderlinge sterkte "
                  "maakt de klankkleur van het instrument."),
        ]),
        dict(kop="Het dopplereffect", blokken=[
            ("p", "Bij het <strong>dopplereffect</strong> verschilt de <strong>waargenomen</strong> "
                  "frequentie omdat bron en waarnemer ten opzichte van elkaar bewegen. Een "
                  "ziekenwagen die <strong>nadert</strong> klinkt <strong>hoger</strong>, een "
                  "die wegrijdt lager. Wat de bron <strong>uitzendt</strong> verandert niet; "
                  "daarom hoort de bestuurder zelf niets veranderen."),
        ]),
    ],
    onthoud=[
        "Licht is een transversale EM-golf; \\(c = 3{,}00 \\times 10^{8}\\) m/s.",
        "Een spiegelbeeld is virtueel, rechtop en even groot.",
        "Verder dan \\(2f\\): reëel, omgekeerd en kleiner; binnen \\(f\\): virtueel en groter.",
        "Radio, micro, infrarood, licht, uv, röntgen, gamma.",
        "\\(E = h\\,f\\); ioniserend zijn röntgen, gamma en harde uv.",
        "Young: interferentie bewijst dat licht een golf is.",
        "Geluid: \\(f\\) is de toonhoogte, \\(A\\) de sterkte, de vorm het timbre.",
        "\\(20\\) Hz tot \\(20\\,000\\) Hz; \\(+10\\) dB is tien keer zo intens.",
        "Doppler verandert wat je hoort, niet wat de bron uitzendt.",
    ],
)


# ───────────────────── 19. Kwantumfysica: het foto-elektrisch effect en dualiteit
BUNDELS["kwantumfysica-het-foto-elektrisch-effect-en-dualiteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kwantumfysica: het foto-elektrisch effect en dualiteit",
    onder="Twee proeven die licht een deeltje maakten en materie een golf.",
    secties=[
        dict(kop="Het foto-elektrisch effect", blokken=[
            ("p", "Schijn je licht op een metaaloppervlak, dan kunnen er "
                  "<strong>elektronen uit losgeslagen</strong> worden. Dat heet het "
                  "<strong>foto-elektrisch effect</strong>. Het licht geeft zijn energie in "
                  "één keer door aan één elektron, en als dat genoeg is, komt het elektron "
                  "los."),
        ]),
        dict(kop="De frequentie beslist", blokken=[
            ("p", "Het verrassende is <strong>waarvan het afhangt</strong> of er elektronen "
                  "<strong>loskomen</strong>: van de <strong>frequentie</strong> van het "
                  "licht, niet van hoe fel het schijnt. De laagste frequentie waarbij er "
                  "iets loskomt heet de <strong>drempelfrequentie</strong> of "
                  "grensfrequentie \\(f_{0}\\). Daaronder komt er "
                  "<strong>geen enkel</strong> elektron los, hoe lang en hoe fel je ook "
                  "schijnt. Heeft een metaal \\(f_{0} = 6 \\times 10^{14}\\) Hz, dan doet licht "
                  "van \\(4 \\times 10^{14}\\) Hz helemaal niets."),
            ("p", "Boven die drempel verandert een <strong>grotere intensiteit</strong> alleen "
                  "het <strong>aantal</strong>: er komen meer elektronen los, elk met "
                  "<strong>dezelfde</strong> energie. Meer intensiteit betekent meer fotonen, "
                  "geen krachtigere fotonen. Kort: de frequentie beslist "
                  "<strong>of</strong>, de intensiteit beslist <strong>hoeveel</strong>."),
        ]),
        dict(kop="De energie van een foton", blokken=[
            ("kader", "<strong>Eén pakketje tegelijk</strong><br>"
                      "\\[E = h\\,f = \\dfrac{h\\,c}{\\lambda} \\qquad "
                      "h = 6{,}63 \\times 10^{-34}\\ \\text{J}\\cdot\\text{s}\\]"
                      "Een foton van \\(f = 5 \\times 10^{14}\\) Hz draagt dus "
                      "\\(E = 3{,}3 \\times 10^{-19}\\) J."),
            ("p", "Omdat een kleine \\(\\lambda\\) bij een hoge \\(f\\) hoort, heeft "
                  "<strong>blauw</strong> licht een energierijker foton dan "
                  "<strong>rood</strong>. Daarom kan blauw licht elektronen losmaken waar rood "
                  "dat niet lukt. Om de minimale fotonenergie van een metaal te kennen heb je "
                  "maar twee gegevens nodig: \\(f_{0}\\) en \\(h\\), want "
                  "\\(E_{\\min} = h\\,f_{0}\\)."),
        ]),
        dict(kop="Wat er met de rest van de energie gebeurt", blokken=[
            ("fig", svg.fotoelektrisch(),
             "De kinetische energie van het losgeslagen elektron tegen de frequentie."),
            ("kader", "<strong>De vergelijking van Einstein</strong><br>"
                      "\\[E_{k} = h\\,f - W\\]"
                      "\\(W\\) is de <strong>uittree-arbeid</strong>: wat het kost om het "
                      "elektron los te maken. Wat overblijft, wordt de "
                      "<strong>kinetische energie</strong> van het elektron."),
            ("p", "De rechte snijdt de \\(f\\)-as precies in \\(f_{0}\\), want daar is "
                  "\\(h\\,f = W\\) en blijft er niets over. Haar <strong>helling</strong> is "
                  "\\(h\\): uit zo'n grafiek kan je de constante van Planck aflezen."),
        ]),
        dict(kop="Waarom het golfmodel tekortschiet", blokken=[
            ("p", "Een <strong>golf</strong> zou energie langzaam kunnen opsparen. Het klassieke "
                  "golfmodel voorspelt daarom dat fel rood licht na enige tijd ook elektronen "
                  "losmaakt, en dat er een <strong>wachttijd</strong> is voor het eerste "
                  "elektron. Geen van beide gebeurt."),
            ("p", "Eén elektron neemt de energie van <strong>één</strong> foton op, alles of "
                  "niets; het telt de energie van meerdere fotonen niet samen op. Net daarom bestaat er "
                  "een scherpe \\(f_{0}\\), en net daarom laat deze proef zien dat licht ook "
                  "een <strong>deeltjeskarakter</strong> heeft."),
        ]),
        dict(kop="Waar je het effect tegenkomt", blokken=[
            ("p", "Een <strong>zonnepaneel</strong>, een <strong>fotocel</strong> in een "
                  "bewegingsdetector en een <strong>rookdetector</strong> die met licht werkt, "
                  "maken alle drie van licht een stroom. Een gloeilamp doet net het omgekeerde."),
        ]),
        dict(kop="Fotocel en rookdetector", blokken=[
            ("p", "Een <strong>zonnecel</strong> werkt doordat het licht in een halfgeleider "
                  "ladingen losmaakt die samen een stroom vormen; een zonneboiler werkt wel met "
                  "warmte. Een fotocel zendt <strong>zelf geen licht uit</strong>: de bron "
                  "staat ertegenover, en valt de bundel weg, dan valt de stroom weg. In een "
                  "rookdetector verstrooit de rook de bundel, waardoor de cel minder licht "
                  "krijgt en het alarm afgaat."),
        ]),
        dict(kop="Materie blijkt ook een golf", blokken=[
            ("p", "<strong>Davisson en Germer</strong> stuurden een elektronenbundel van "
                  "losse <strong>elektronen</strong> op een <strong>nikkelplaatje</strong>. Die "
                  "regelmatige rijen atomen werkten als een rooster, en erachter verscheen een "
                  "<strong>buigingspatroon</strong>. Dat kan alleen een golf geven. Hun proef "
                  "en de proef van Young hebben dus hetzelfde gemeen: allebei tonen ze een "
                  "<strong>golfkarakter</strong>, de ene bij materie, de andere bij licht."),
            ("kader", "<strong>De golflengte van de Broglie</strong><br>"
                      "\\[\\lambda = \\dfrac{h}{m\\,v}\\]"
                      "Hoe groter de massa, hoe kleiner \\(\\lambda\\). De golfkant van een voetbal "
                      "merken we daarom niet: zijn \\(\\lambda\\) is "
                      "onvoorstelbaar klein; voor een elektron is ze van de orde van een atoom, "
                      "en daar meet je ze dus wel."),
        ]),
        dict(kop="Dualiteit: twee gezichten", blokken=[
            ("p", "Licht en materie gedragen zich <strong>soms als een golf en soms als een "
                  "deeltje</strong>. Welk gezicht je ziet, hangt af van de proef die je doet. "
                  "Het <strong>golfmodel</strong> verklaart interferentie bij Young, buiging "
                  "rond een smalle opening en breking bij de overgang naar glas. Het "
                  "<strong>deeltjesmodel</strong> verklaart het foto-elektrisch effect en de "
                  "drempelfrequentie van een metaal."),
        ]),
        dict(kop="Geen van beide is het hele verhaal", blokken=[
            ("p", "Het deeltjesmodel is dus <strong>geen rekentruc</strong> bovenop een golf: "
                  "beide kanten beschrijven echt gedrag, en geen van de twee is in zijn eentje "
                  "het hele verhaal. De vraag wat licht nu <em>echt</em> is, heeft geen van "
                  "beide antwoorden."),
        ]),
        dict(kop="Eén elektron per keer", blokken=[
            ("fig", svg.tweespleten(),
             "Hetzelfde tweespletenexperiment, met steeds meer afgevuurde elektronen."),
            ("p", "Vuur je in het tweespletenexperiment de elektronen <strong>één per "
                  "één</strong> afvuurt, dan landt elk elektron als <strong>één stip</strong>. Toch "
                  "staat er na lang wachten een <strong>patroon van strepen</strong>: de "
                  "kansen van alle losse elektronen samen vormen het golfpatroon. Eén elektron "
                  "interfereert dus met zichzelf."),
        ]),
        dict(kop="De golffunctie en het orbitaal", blokken=[
            ("p", "De <strong>golffunctie</strong> van een deeltje geeft de <strong>kans</strong> "
                  "om het op een bepaalde plaats te vinden, geen baan en geen spoor. Je bepaalt "
                  "haar met de <strong>Schrödingervergelijking</strong>; daaruit volgen de "
                  "kansen en de toegelaten energieën."),
            ("p", "Volgens de <strong>Kopenhaagse interpretatie</strong> valt die golffunctie "
                  "bij een <strong>meting</strong> samen tot één uitkomst: vóór de meting is er "
                  "enkel een kansverdeling, erna één plaats. De meting hoort dus bij het "
                  "verhaal."),
        ]),
        dict(kop="Het orbitaal", blokken=[
            ("p", "In een atoom is de plaats van een elektron daarom een "
                  "<strong>kansverdeling</strong>: sommige plaatsen zijn veel waarschijnlijker "
                  "dan andere. Het gebied waar je het met grote kans vindt, heet een "
                  "<strong>orbitaal</strong> of waarschijnlijkheidsgebied. Dat is een wolk van "
                  "kansen, geen cirkelbaan: dat "
                  "laatste was een ouder model."),
        ]),
        dict(kop="Het onzekerheidsbeginsel", blokken=[
            ("kader", "<strong>Heisenberg</strong><br>"
                      "\\[\\Delta x \\cdot \\Delta p \\geq \\dfrac{h}{4\\pi}\\]"
                      "Hoe scherper je de <strong>plaats</strong> kent, hoe vager de "
                      "<strong>impuls</strong>, en omgekeerd."),
            ("p", "Dat komt <strong>niet</strong> doordat onze meettoestellen nog niet nauwkeurig "
                  "genoeg zijn; het zit "
                  "in de natuur zelf, en een beter toestel maakt er geen einde aan. En net "
                  "daarom kan je van een elektron <strong>geen baan tekenen</strong> zoals van "
                  "een planeet: een baan vraagt plaats en snelheid tegelijk scherp, en dat kan "
                  "niet."),
        ]),
    ],
    onthoud=[
        "Foto-elektrisch effect: licht slaat elektronen uit een metaal.",
        "De frequentie beslist of, de intensiteit hoeveel.",
        "\\(E = h\\,f\\), met \\(h = 6{,}63 \\times 10^{-34}\\) J·s.",
        "\\(E_{k} = h\\,f - W\\); de helling van de grafiek is \\(h\\).",
        "Davisson en Germer: elektronen buigen op nikkel, dus golf.",
        "\\(\\lambda = \\dfrac{h}{m\\,v}\\): bij grote massa onmeetbaar klein.",
        "Dualiteit: golf en deeltje zijn allebei echt.",
        "De golffunctie geeft kansen; een orbitaal is zo'n kansgebied.",
        "\\(\\Delta x \\cdot \\Delta p \\geq \\dfrac{h}{4\\pi}\\): nooit samen scherp.",
    ],
)


# ───────────────────── 20. De atoomkern, radioactief verval en halveringstijd
BUNDELS["de-atoomkern-radioactief-verval-en-halveringstijd-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De atoomkern, radioactief verval en halveringstijd",
    onder="Wat er in een kern zit, wanneer ze het niet volhoudt, en hoe snel ze verdwijnt.",
    secties=[
        dict(kop="Hoe je een kern benoemt", blokken=[
            ("kader", "<strong>Drie getallen</strong><br>"
                      "\\[A = Z + N \\qquad N = A - Z\\]"
                      "\\(A\\) is het <strong>massagetal</strong>: het aantal protonen en "
                      "neutronen samen, de <strong>nucleonen</strong> of kerndeeltjes. \\(Z\\) is het "
                      "<strong>atoomnummer</strong> of ladingsgetal: het aantal protonen. "
                      "\\(N\\) is het neutronental."),
            ("p", "Je schrijft een nuclide als <strong>X-14</strong>, met het massagetal achter "
                  "de naam, of met beide getallen bij het symbool: "
                  "\\(^{14}_{\\ 6}\\text{C}\\). Een nuclide met \\(A = 23\\) en \\(Z = 11\\) "
                  "heeft dus \\(N = 12\\) neutronen; uranium-238 met \\(Z = 92\\) heeft er "
                  "\\(146\\)."),
            ("p", "Zodra je \\(A\\) en \\(Z\\) kent, liggen het aantal protonen, het aantal "
                  "neutronen én het element vast. De <strong>halveringstijd</strong> volgt er "
                  "niet uit: die moet je opzoeken."),
        ]),
        dict(kop="Isotopen", blokken=[
            ("p", "<strong>Isotopen</strong> van een element zijn kernen met "
                  "<strong>hetzelfde \\(Z\\)</strong> en een <strong>ander \\(N\\)</strong>, "
                  "dus hetzelfde element met een ander massagetal. Koolstof-12 en koolstof-14 "
                  "verschillen alleen in hun aantal neutronen: zes tegenover acht."),
            ("p", "Een ander aantal neutronen maakt dus <strong>geen ander element</strong>; "
                  "alleen het aantal protonen bepaalt welk element het is. Koolstof-14 is wel "
                  "onstabiel, en net dat maakt de koolstofdatering mogelijk."),
        ]),
        dict(kop="Wat een kern samenhoudt", blokken=[
            ("p", "In een kern spelen twee krachten tegen elkaar in. De <strong>sterke "
                  "kernkracht</strong> is de kracht die alle nucleonen aantrekt, maar ze werkt "
                  "enkel over een "
                  "heel korte afstand. De <strong>coulombkracht</strong> is de kracht die de "
                  "protonen afstoot, en die werkt over de hele kern. De gravitatie is "
                  "volkomen "
                  "verwaarloosbaar."),
            ("p", "Bij lichte kernen met \\(Z < 20\\) is \\(N \\approx Z\\): koolstof-12 heeft "
                  "zes van elk. Bij zware kernen met \\(Z > 20\\) zijn er "
                  "<strong>meer neutronen dan protonen</strong> nodig, want elk extra neutron "
                  "geeft wel kernkracht maar <strong>geen</strong> extra afstoting."),
        ]),
        dict(kop="De stabiliteitsband", blokken=[
            ("fig", svg.nuclidenkaart(),
             "Een nuclidenkaart met het neutronental tegen het atoomnummer."),
            ("p", "De strook stabiele kernen heet de <strong>stabiliteitsband</strong>. Uit de "
                  "plaats van een kern lees je of hij stabiel is en, zo niet, welk verval hij "
                  "zal doen. Die band heet ook de stabiliteitszone. <strong>Boven</strong> de "
                  "band heeft een kern te veel neutronen en "
                  "vervalt hij via <strong>bèta-min</strong>, <strong>onder</strong> de band "
                  "te veel protonen en dus <strong>bèta-plus</strong>."),
        ]),
        dict(kop="Radionucliden", blokken=[
            ("p", "Een <strong>radionuclide</strong> is een kern die onstabiel is en "
                  "<strong>spontaan</strong> vervalt. Spontaan betekent: van zichzelf, niet "
                  "van iets wat je eraan doet. Verwarmen, samenpersen of in een verbinding "
                  "stoppen kan het verval niet versnellen, want verval is een "
                  "kernproces. Daarom blijft langlevend radioactief afval ook duizenden jaren "
                  "een probleem."),
        ]),
        dict(kop="De vier soorten verval", blokken=[
            ("kader", "<strong>De regels van Soddy</strong><br>"
                      "\\[\\alpha:\\ ^{A}_{Z}X \\rightarrow\\ ^{A-4}_{Z-2}Y + ^{4}_{2}\\text{He} "
                      "\\qquad \\beta^{-}:\\ ^{1}_{0}n \\rightarrow\\ ^{1}_{1}p + e^{-}\\]"
                      "Bij \\(\\alpha\\) daalt \\(A\\) met vier en \\(Z\\) met twee. Bij "
                      "\\(\\beta^{-}\\) blijft \\(A\\) gelijk en stijgt \\(Z\\) met één. Bij "
                      "\\(\\gamma\\) blijven \\(A\\) en \\(Z\\) allebei gelijk."),
        ]),
        dict(kop="Alfa, bèta en gamma", blokken=[
            ("p", "Bij <strong>alfaverval</strong> vertrekt een heliumkern met twee protonen "
                  "en twee neutronen. Bij <strong>bèta-min</strong> wordt een neutron een "
                  "proton en vliegt er een elektron weg, samen met een antineutrino. Bij "
                  "<strong>bèta-plus</strong> gebeurt het omgekeerde en vertrekt er een "
                  "<strong>positron</strong> of antielektron, het antideeltje van het elektron. "
                  "Bij <strong>gammaverval</strong> vertrekt er <strong>gammastraling</strong>, "
                  "een foton met heel veel energie: "
                  "de kern "
                  "verandert niet van element, ze raakt enkel haar overtollige energie kwijt."),
            ("p", "Een kern met \\(A = 226\\) en \\(Z = 88\\) die alfaverval doet, wordt dus "
                  "een kern met \\(A = 222\\) en \\(Z = 86\\): radium-226 wordt radon-222. In "
                  "elke reactievergelijking moeten \\(A\\) en \\(Z\\) links en rechts kloppen."),
        ]),
        dict(kop="Halveringstijd", blokken=[
            ("fig", svg.vervalcurve(),
             "Het aantal kernen dat nog niet vervallen is, tegen de tijd."),
            ("kader", "<strong>Elke keer de helft</strong><br>"
                      "\\[N(t) = N_{0}\\left(\\tfrac{1}{2}\\right)^{t/T_{1/2}}\\]"
                      "\\(T_{1/2}\\) is de <strong>halveringstijd</strong> of halfwaardetijd: de tijd "
                      "waarin de "
                      "helft van de kernen vervalt. Ze ligt voor elk radionuclide vast."),
        ]),
        dict(kop="Rekenen met halveringen", blokken=[
            ("p", "Na één halveringstijd is de <strong>helft</strong> vervallen, na twee een "
                  "kwart over, na drie een achtste. Een stof met \\(T_{1/2} = 8\\) dagen heeft "
                  "na \\(24\\) dagen dus nog \\(\\left(\\tfrac{1}{2}\\right)^{3} = "
                  "\\tfrac{1}{8}\\) over. <strong>Volledig</strong> verdwijnen gebeurt in dit "
                  "model nooit: van een radioactieve stof gaat telkens maar de helft weg."),
        ]),
        dict(kop="Activiteit", blokken=[
            ("kader", "<strong>Hoeveel vervallen er per seconde?</strong><br>"
                      "\\[A = \\lambda\\,N \\qquad \\lambda = \\dfrac{\\ln 2}{T_{1/2}} "
                      "= \\dfrac{0{,}693}{T_{1/2}}\\]"
                      "De <strong>activiteit</strong> \\(A\\) staat in "
                      "<strong>becquerel</strong>: één Bq is één verval per seconde. "
                      "\\(\\lambda\\) is de <strong>desintegratieconstante</strong>."),
            ("p", "Omdat \\(A\\) recht evenredig is met \\(N\\), daalt ze op precies dezelfde "
                  "manier: ze <strong>halveert na elke halveringstijd</strong>. Een bron van "
                  "\\(800\\) Bq met \\(T_{1/2} = 5\\) jaar staat na \\(10\\) jaar op "
                  "\\(200\\) Bq. Een <strong>kortere</strong> halveringstijd geeft een grotere "
                  "\\(\\lambda\\), en dus bij dezelfde hoeveelheid een <strong>hogere</strong> "
                  "activiteit."),
            ("p", "Om \\(N\\) uit een massa te halen heb je de massa, de "
                  "<strong>molaire massa</strong> en het <strong>getal van Avogadro</strong> "
                  "nodig. Een dosis staat in <strong>gray</strong> of "
                  "<strong>sievert</strong>."),
        ]),
        dict(kop="De koolstof-14-methode", blokken=[
            ("p", "Zolang een organisme leeft, vult het zijn voorraad koolstof-14 aan. Na de "
                  "dood stopt dat, en daalt het gehalte met een vaste halveringstijd van "
                  "ongeveer \\(5730\\) jaar. Uit wat er nog over is, lees je dus af hoelang "
                  "geleden het gestorven is, en zo bepaal je de ouderdom."),
        ]),
    ],
    onthoud=[
        "\\(A = Z + N\\); isotopen hebben zelfde \\(Z\\), ander \\(N\\).",
        "Sterke kernkracht trekt aan, coulombkracht stoot protonen af.",
        "De stabiliteitsband zegt of en hoe een kern vervalt.",
        "\\(\\alpha\\): \\(A-4\\), \\(Z-2\\). \\(\\beta^{-}\\): \\(Z+1\\). \\(\\gamma\\): niets verandert.",
        "Verval versnel je met niets: niet met warmte, niet met chemie.",
        "\\(N(t) = N_{0}\\left(\\tfrac{1}{2}\\right)^{t/T_{1/2}}\\).",
        "\\(A = \\lambda\\,N\\) in becquerel, met \\(\\lambda = \\tfrac{0{,}693}{T_{1/2}}\\).",
    ],
)


# ───────────────────── 21. Kernenergie, straling en haar effecten
BUNDELS["kernenergie-straling-en-haar-effecten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kernenergie, straling en haar effecten",
    onder="Van massadefect tot jodiumpil: waar de energie zit en wat de straling doet.",
    secties=[
        dict(kop="Massa is energie", blokken=[
            ("kader", "<strong>De formule van Einstein</strong><br>"
                      "\\[E = m\\,c^{2}\\]"
                      "Elke massa <strong>is</strong> een hoeveelheid energie. Omdat "
                      "\\(c^{2}\\) enorm groot is, zit er in een kleine massa heel veel "
                      "energie: in \\(1\\) g zit \\(9 \\times 10^{13}\\) J."),
            ("p", "Bij een kernproces blijft de totale massa van de deeltjes dus "
                  "<strong>niet</strong> gelijk: een stukje massa wordt energie, en net daar "
                  "komt de opbrengst vandaan. Massa en energie samen blijven wel bewaard. In "
                  "de kernfysica rekent men vaak met \\(931{,}49\\) MeV per atomaire "
                  "massa-eenheid."),
        ]),
        dict(kop="Massadefect en bindingsenergie", blokken=[
            ("kader", "<strong>Wat de kern samenhoudt</strong><br>"
                      "\\[E_{b} = \\Delta m\\,c^{2} \\qquad \\text{per nucleon: } "
                      "\\dfrac{E_{b}}{A}\\]"
                      "\\(\\Delta m\\) is het <strong>massadefect</strong>: het verschil "
                      "tussen de massa van de losse nucleonen en die van de kern."),
            ("p", "Een kern weegt dus <strong>minder</strong> dan haar delen apart. Die "
                  "ontbrekende massa zit als <strong>bindingsenergie</strong> of "
                  "kernbindingsenergie in de kern: "
                  "precies de energie die je nodig hebt om haar weer in losse nucleonen te "
                  "splitsen. Deel je door het aantal nucleonen, dan krijg je de "
                  "<strong>specifieke bindingsenergie</strong>, en daarmee kan je kernen van "
                  "heel verschillende grootte vergelijken: hoe groter ze is, hoe "
                  "<strong>stabieler</strong> de kern."),
        ]),
        dict(kop="Splijting en fusie", blokken=[
            ("fig", svg.bindingsenergiecurve(),
             "De specifieke bindingsenergie van de lichtste tot de zwaarste kernen."),
            ("p", "<strong>Kernsplijting</strong> is een zware kern die in twee lichtere "
                  "uiteenvalt; <strong>kernfusie</strong> is twee lichte kernen die "
                  "samensmelten. Allebei leveren ze energie, want allebei schuiven ze naar "
                  "kernen met een <strong>grotere</strong> specifieke bindingsenergie. Boven "
                  "aan de curve ligt ijzer-56, de stabielste kern van allemaal."),
        ]),
        dict(kop="De kerncentrale", blokken=[
            ("p", "De zon haalt haar energie uit <strong>kernfusie van waterstof tot "
                  "helium</strong>. Een gewone kerncentrale op aarde werkt met "
                  "<strong>kernsplijting</strong> en gebruikt <strong>uranium</strong>, ook uraan "
                  "genoemd, als splijtstof. Bij zo'n "
                  "centrale horen een <strong>reactorvat</strong> met splijtstaven en "
                  "regelstaven, een <strong>stoomgenerator</strong> met een turbine, en een "
                  "<strong>betonnen koepel</strong> rond de reactor."),
            ("p", "De <strong>regelstaven</strong> in een kernreactor vangen neutronen weg en "
                  "houden zo de "
                  "kettingreactie in de hand. Bij het opwekken van stroom stoot een "
                  "kerncentrale <strong>geen CO₂</strong> uit; het probleem zit in het afval. "
                  "Een centrale op <strong>fusie</strong> zou daarin beter scoren: veel minder "
                  "langlevend afval, en geen kettingreactie die ontspoort."),
        ]),
        dict(kop="Radioactief afval", blokken=[
            ("p", "Afval wordt ingedeeld volgens <strong>twee</strong> kenmerken: hoe intens "
                  "de straling is, dus de intensiteit, en hoe lang ze duurt. In "
                  "<strong>categorie A</strong> zit kortlevend laagactief en middelactief "
                  "afval, bijvoorbeeld beschermkledij en "
                  "gereedschap uit een ziekenhuis of een labo."),
            ("p", "Voor hoogactief afval van <strong>categorie C</strong> ligt in België nog "
                  "<strong>geen</strong> definitieve bergingsplaats vast. Er is wel een "
                  "onderzoekslabo in de kleilaag onder Mol, maar de keuze is niet gemaakt."),
        ]),
        dict(kop="Alfa, bèta en gamma onderweg", blokken=[
            ("fig", svg.doordringend(),
             "Drie soorten straling tegen een blad papier, aluminium en lood."),
            ("p", "<strong>Alfastraling</strong> heeft het grootste "
                  "<strong>ioniserend</strong> vermogen en het <strong>kleinste</strong> "
                  "doordringend vermogen. Die twee gaan altijd omgekeerd samen: wie veel "
                  "ioniseert, raakt zijn energie snel kwijt. Een blad papier houdt alfa tegen, "
                  "een plaatje aluminium houdt bèta tegen, en een dikke laag lood of beton "
                  "zwakt gamma af."),
        ]),
        dict(kop="Straling in een veld", blokken=[
            ("p", "Alfa- en bètastraling zijn <strong>geladen</strong>, dus ze buigen af in "
                  "een elektrisch én in een magnetisch veld. Omdat hun lading tegengesteld is, "
                  "buigen ze naar <strong>tegengestelde</strong> kanten. "
                  "<strong>Gammastraling</strong> heeft geen lading en gaat dus "
                  "<strong>recht</strong> door."),
        ]),
        dict(kop="Bestraling en besmetting", blokken=[
            ("p", "Bij <strong>bestraling</strong> sta je in de straling van een bron die "
                  "buiten je blijft. Bij <strong>besmetting</strong> zit de radioactieve stof "
                  "zelf op of in je lichaam; zit ze erin, dan heet dat een "
                  "<strong>inwendige</strong> besmetting. Daarom is alfastraling van buiten "
                  "ongevaarlijk, maar ingeslikt of ingeademd juist het gevaarlijkst."),
        ]),
        dict(kop="Drie soorten dosis", blokken=[
            ("kader", "<strong>Van energie naar risico</strong><br>"
                      "\\[D = \\dfrac{E}{m} \\quad [\\text{Gy}] \\qquad "
                      "H = w_{R} \\cdot D \\quad [\\text{Sv}] \\qquad "
                      "E_{\\text{eff}} = \\sum w_{T} \\cdot H\\]"
                      "\\(1\\ \\text{Gy} = 1\\ \\text{J/kg}\\). De equivalente en de "
                      "effectieve dosis staan in <strong>sievert</strong>."),
            ("p", "De <strong>geabsorbeerde dosis</strong> \\(D\\) is de energie van de "
                  "straling per kilogram weefsel. De <strong>stralingsweegfactor</strong> "
                  "\\(w_{R}\\) verrekent dat de ene soort straling meer schade doet dan de "
                  "andere: alfastraling scoort er veel hoger omdat ze al haar energie in een "
                  "heel klein gebied afgeeft, zodat alle ionisaties op dezelfde paar cellen "
                  "terechtkomen."),
            ("p", "De <strong>weefselweegfactor</strong> \\(w_{T}\\) verrekent dat het ene "
                  "orgaan gevoeliger is dan het andere: beenmerg weegt zwaarder dan huid. De "
                  "<strong>effectieve dosis</strong> houdt dus rekening met de soort straling én "
                  "met het bestraalde weefsel, en net daarom is zij de maat voor het risico "
                  "voor de mens."),
        ]),
        dict(kop="Beschermen", blokken=[
            ("p", "Tegen ioniserende straling werken drie dingen, en altijd dezelfde drie: "
                  "<strong>afstand</strong> (verder van de bron gaan staan), "
                  "<strong>tijd</strong> (zo kort mogelijk in de buurt blijven) en "
                  "<strong>afscherming</strong> (lood of beton ertussen). De bron verwarmen "
                  "doet niets: verval trekt zich daar niets van aan."),
            ("p", "Bij een kernongeval deelt men <strong>jodiumpillen</strong> uit. De "
                  "schildklier zit dan vol met gewoon jodium en neemt het radioactieve jodium "
                  "uit de lucht niet meer op."),
        ]),
        dict(kop="Wat straling met een cel doet", blokken=[
            ("p", "Ioniserende straling kan het <strong>DNA</strong> van een cel beschadigen, "
                  "waardoor de cel kan afsterven of muteren. Een deel van de straling om ons heen "
                  "is <strong>natuurlijk</strong>: radon uit de bodem en straling uit de "
                  "kosmos. Die is er altijd, ook zonder centrale in de buurt."),
            ("p", "Dezelfde straling helpt ook: <strong>radiotherapie</strong> tegen een "
                  "tumor, een <strong>PET-scan</strong> met een radioactieve tracer, en het "
                  "<strong>doorstralen</strong> van voedsel om het langer te bewaren. "
                  "Doorstraald voedsel wordt <strong>niet</strong> zelf radioactief: de "
                  "straling doodt de micro-organismen en gaat er dan gewoon door. In een "
                  "PET-scan kiest men een stof met een <strong>korte halveringstijd</strong>, "
                  "zodat de straling snel weer uit het lichaam weg is."),
        ]),
    ],
    onthoud=[
        "\\(E = m\\,c^{2}\\); bij een kernproces verdwijnt er massa.",
        "\\(E_{b} = \\Delta m\\,c^{2}\\); per nucleon telt: \\(\\tfrac{E_{b}}{A}\\).",
        "Splijting van zwaar en fusie van licht leveren allebei energie.",
        "Regelstaven vangen neutronen en houden de reactie in de hand.",
        "Categorie C, hoogactief, heeft in België nog geen bergingsplaats.",
        "Alfa ioniseert het sterkst en dringt het minst door.",
        "\\(D\\) in gray, \\(H = w_{R} \\cdot D\\) in sievert, dan \\(w_{T}\\) erbij.",
        "Afstand, tijd en afscherming beschermen je.",
    ],
)


# ───────────────────── 22. Veilig werken, meetinstrumenten en meetonzekerheid
BUNDELS["veilig-werken-meetinstrumenten-en-meetonzekerheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig werken, meetinstrumenten en meetonzekerheid",
    onder="Het juiste toestel, het juiste bereik en het juiste aantal cijfers.",
    secties=[
        dict(kop="Elk toestel heeft zijn grenzen", blokken=[
            ("p", "Het <strong>meetbereik</strong> van een meetinstrument is de kleinste en de "
                  "grootste waarde die het kan meten. Een multimeter die tot \\(10\\ \\text{A}\\) "
                  "gaat, zegt je niets meer over een stroom van \\(25\\ \\text{A}\\). Erger nog: "
                  "de meting is dan onbetrouwbaar én het toestel kan beschadigen. Daarom kies je "
                  "altijd eerst je bereik, en pas dan sluit je aan."),
            ("p", "De <strong>nauwkeurigheid</strong>, ook de <strong>resolutie</strong> genoemd, "
                  "is het kleinste verschil dat een meetinstrument nog kan aanwijzen. Bij een lat "
                  "met millimeters is dat \\(1\\ \\text{mm}\\), bij een gewone keukenweegschaal "
                  "\\(1\\ \\text{g}\\). Je antwoord mag nooit nauwkeuriger lijken dan je toestel is: "
                  "wie met die lat \\(12{,}437\\ \\text{cm}\\) noteert, verzint de laatste twee "
                  "cijfers."),
            ("p", "Een meting is daarom nooit helemaal exact. Niet omdat je slordig werkt, maar "
                  "omdat elk instrument een beperkte nauwkeurigheid heeft. Dat is geen zwakte van "
                  "de fysica, het is er een afspraak van: je zegt er altijd bij hoe goed je "
                  "gemeten hebt."),
        ]),
        dict(kop="Nauwkeuriger is niet altijd beter", blokken=[
            ("p", "Je moet kiezen tussen twee chronometers, een van \\(0{,}1\\ \\text{s}\\) en een "
                  "van \\(0{,}01\\ \\text{s}\\). Voor een val van ongeveer een halve seconde neem "
                  "je die van \\(0{,}01\\ \\text{s}\\): met \\(0{,}1\\ \\text{s}\\) zit je al op "
                  "\\(\\dfrac{0{,}1}{0{,}5} = 20\\ \\%\\) ernaast. De vuistregel is dat de "
                  "nauwkeurigheid klein moet zijn tegenover wat je meet."),
            ("p", "Toch is een nauwkeuriger meetinstrument niet altijd de beste keuze. Het is vaak "
                  "duurder, trager of beperkter in bereik. Voor de lengte van een lokaal volstaat "
                  "een rolmeter, en een duur toestel buiten zijn bereik meet slechter dan een "
                  "eenvoudig toestel erbinnen. Je kiest het toestel bij de meting, niet omgekeerd."),
            ("p", "Bij een snelle beweging gebruik je liever een <strong>sensor</strong> dan een "
                  "handchronometer, want je eigen reactietijd geeft bij de hand een fout van wel "
                  "een tiende seconde. Een lichtpoortje start en stopt zonder reactietijd, en meet "
                  "zo ook een val van \\(0{,}5\\ \\text{s}\\) nog betrouwbaar."),
        ]),
        dict(kop="Recht van boven aflezen", blokken=[
            ("fig", svg.parallax(),
             "De naald hangt een stukje boven de schaal, dus verschuift ze mee met je ooghoogte."),
            ("p", "Een analoge meter met een naald lees je af recht van boven, zodat de naald niet "
                  "verschoven lijkt. Kijk je schuin, dan lees je door de "
                  "<strong>parallaxfout</strong> een andere waarde. Sommige toestellen hebben daar "
                  "een spiegeltje voor: je leest goed af wanneer de naald haar spiegelbeeld precies "
                  "bedekt."),
            ("p", "En een toestel dat een onwaarschijnlijke waarde aanwijst, mag je niet zonder "
                  "meer overnemen. Controleer eerst het bereik, de aansluiting en de stand van het "
                  "toestel. Een schatting vooraf helpt je zo'n fout meteen te zien."),
        ]),
        dict(kop="Welk toestel voor welke grootheid", blokken=[
            ("p", "Een kracht meet je met een <strong>dynamometer</strong>, een veer met een "
                  "schaal erachter. Een tijdsduur meet je met een <strong>chronometer</strong>, en "
                  "het geluidsniveau in een ruimte met een <strong>decibelmeter</strong>, ook een "
                  "<strong>geluidsmeter</strong> genoemd. Die laatste gebruik je bijvoorbeeld om "
                  "na te gaan of een zaal de geluidsnorm haalt."),
            ("p", "Met een <strong>multimeter</strong> meet je drie dingen: de spanning over een "
                  "lamp, de stroom door een draad en de weerstand van een component. Elk op zijn "
                  "eigen stand, en elk met zijn eigen manier van aansluiten. Spanning meet je "
                  "<em>over</em> het onderdeel, stroom meet je <em>door</em> de kring, dus daar moet "
                  "je de kring openknippen en de meter ertussen zetten."),
        ]),
        dict(kop="Veilig en duurzaam in het labo", blokken=[
            ("p", "Drie werkwijzen horen bij veilig werken in een fysicalabo. Een spanningsbron "
                  "zet je op de laagste stand voor je hem aansluit. Zo kan je de "
                  "spanning rustig opdrijven zonder iets te laten doorbranden. Je leest ook de "
                  "handleiding van een toestel voor je het gebruikt, om het meetbereik, de "
                  "aansluiting en de voorzorgen te kennen."),
            ("p", "Elektrische toestellen bedien je nooit met natte handen, want water geleidt. "
                  "Veilig werken en duurzaam werken lopen hier samen: het meetbereik en de "
                  "nauwkeurigheid van een toestel respecteren spaart het toestel, en een "
                  "meetinstrument uitschakelen als je er niet mee meet spaart de batterij."),
        ]),
        dict(kop="Afval van het labo", blokken=[
            ("p", "De batterijen van meetmateriaal dat je weggooit, horen bij het klein gevaarlijk "
                  "afval en gaan apart. Ze bevatten zware metalen die anders in de bodem "
                  "terechtkomen. Duurzaam werken houdt bij het afval niet op."),
        ]),
        dict(kop="Werken met een radioactieve bron", blokken=[
            ("p", "Bij een radioactieve bron horen drie voorzorgen, en ze zijn alle drie dezelfde "
                  "als bij straling in het algemeen. Blijf zo ver mogelijk van de bron, haal ze zo "
                  "kort mogelijk uit haar houder, en zet een afscherming tussen jou en de bron."),
            ("kader", "Afstand, tijd en afscherming. De intensiteit daalt met "
                      "\\(\\dfrac{1}{r^{2}}\\), dus twee keer zo ver is vier keer zo weinig."),
        ]),
        dict(kop="De SI-eenheden", blokken=[
            ("p", "De SI-eenheid van kracht is de <strong>newton</strong>. De joule hoort bij "
                  "energie, het pascal bij druk en de watt bij vermogen; elk van die drie is uit de "
                  "newton opgebouwd. Verder zijn de meter voor een lengte, de kilogram voor een "
                  "massa en de seconde voor een tijd SI-eenheden."),
            ("kader", "\\(1\\ \\text{N} = 1\\ \\text{kg}\\cdot\\text{m/s}^{2}\\), "
                      "\\(1\\ \\text{J} = 1\\ \\text{N}\\cdot\\text{m}\\), "
                      "\\(1\\ \\text{W} = 1\\ \\text{J/s}\\) en "
                      "\\(1\\ \\text{Pa} = 1\\ \\text{N/m}^{2}\\)."),
        ]),
        dict(kop="Omrekenen naar SI", blokken=[
            ("p", "De kilometer per uur is géén SI-eenheid. Ze is handig op een verkeersbord, maar "
                  "niet de eenheid waarmee je rekent. Om van \\(\\text{km/h}\\) naar "
                  "\\(\\text{m/s}\\) te gaan vermenigvuldig je met \\(\\dfrac{1}{3{,}6}\\), dus je "
                  "deelt door \\(3{,}6\\): een uur heeft \\(3600\\) seconden en een kilometer "
                  "\\(1000\\) meter. Zo is \\(72\\ \\text{km/h}\\) gelijk aan "
                  "\\(20\\ \\text{m/s}\\)."),
        ]),
        dict(kop="Voorvoegsels", blokken=[
            ("fig", svg.voorvoegsels(),
             "Van giga tot nano: elk vakje staat voor duizend keer het volgende."),
            ("p", "Een voorvoegsel is niets anders dan een macht van tien die bij de eenheid hoort. "
                  "<strong>Milli</strong> is een duizendste, dus is "
                  "\\(2{,}5\\ \\text{mA} = 0{,}0025\\ \\text{A}\\): de komma schuift drie plaatsen "
                  "naar links, en je leest het af in ampère. <strong>Kilo</strong> is duizend, dus is "
                  "\\(4{,}7\\ \\text{k}\\Omega = 4700\\ \\Omega\\)."),
        ]),
        dict(kop="Micro, nano en mega", blokken=[
            ("p", "<strong>Micro</strong> is een miljoenste, \\(10^{-6}\\), en "
                  "<strong>nano</strong> een miljardste, \\(10^{-9}\\). <strong>Mega</strong> gaat "
                  "juist de andere kant op: een miljoen keer zoveel, \\(10^{6}\\). Een factor "
                  "duizend ernaast door een verkeerd voorvoegsel is de meest gemaakte fout van "
                  "allemaal."),
        ]),
        dict(kop="Beduidende cijfers", blokken=[
            ("p", "De <strong>beduidende cijfers</strong> van een meting laten zien hoe goed je "
                  "gemeten hebt. De meting \\(0{,}0250\\ \\text{m}\\) heeft er <strong>drie</strong>: "
                  "de nullen vooraan tellen niet mee, de nul achteraan wel. Die laatste nul zegt "
                  "namelijk dat er tot op die plaats gemeten is."),
        ]),
        dict(kop="Optellen en afronden", blokken=[
            ("p", "Tel je \\(2{,}5\\ \\text{m}\\) en \\(1{,}25\\ \\text{m}\\) op, dan schrijf je het "
                  "antwoord met één cijfer na de komma, dus \\(3{,}8\\ \\text{m}\\) en niet "
                  "\\(3{,}75\\ \\text{m}\\). Bij een som bepaalt de slechtste meting hoeveel cijfers "
                  "na de komma je mag houden. Je antwoord kan nu eenmaal niet nauwkeuriger zijn dan "
                  "je meting."),
            ("p", "Daarom schrijf je ook niet alle cijfers van je rekenmachine op: je antwoord zou "
                  "dan nauwkeuriger lijken dan je meting is. Tien cijfers achter de komma bij een "
                  "meting met een lat is onzin."),
        ]),
        dict(kop="Wetenschappelijke notatie en schatten", blokken=[
            ("p", "In de <strong>wetenschappelijke notatie</strong> zet je één cijfer anders dan "
                  "nul voor de komma, en de rest in de macht van tien. Zo wordt \\(0{,}00045\\) "
                  "gelijk aan \\(4{,}5 \\times 10^{-4}\\), en \\(32\\,000\\) gelijk aan "
                  "\\(3{,}2 \\times 10^{4}\\). Er staan dus niet twee cijfers voor de komma, maar "
                  "precies één."),
            ("p", "Die schrijfwijze maakt heel grote en heel kleine getallen vergelijkbaar, en je "
                  "ziet er meteen aan hoeveel beduidende cijfers er zijn. "
                  "\\(4{,}50 \\times 10^{-4}\\) zegt iets anders dan \\(4{,}5 \\times 10^{-4}\\)."),
        ]),
        dict(kop="Eerst schatten", blokken=[
            ("p", "Maak vooraf een <strong>schatting</strong> van je uitkomst, om een onzinnig "
                  "antwoord meteen te herkennen. Een mens die \\(300\\ \\text{m/s}\\) loopt, klopt "
                  "niet. Zo'n schatting kost tien seconden en vangt de meeste rekenfouten op."),
        ]),
        dict(kop="Van tabel naar grafiek", blokken=[
            ("p", "Meetgegevens verwerk je in drie stappen: de gegevens in een tabel zetten, een "
                  "grafiek tekenen om het verband te zien, en het antwoord met de juiste eenheid "
                  "noteren. Wat je instelt komt op de horizontale as, wat je meet op de verticale."),
            ("p", "Een meting die niet past, laat je niet zomaar weg. Dat mag alleen met een reden "
                  "die je opschrijft, bijvoorbeeld dat de chronometer te laat gestart is. Anders pas "
                  "je je gegevens aan je verwachting aan, en dat is precies de omgekeerde weg."),
        ]),
        dict(kop="Drie verbanden herkennen", blokken=[
            ("fig", svg.drieverbanden(),
             "Dezelfde twee grootheden, drie manieren waarop ze van elkaar kunnen afhangen."),
            ("p", "Zie je in een grafiek een <strong>rechte door de oorsprong</strong>, dan is het "
                  "verband <strong>recht evenredig</strong>: \\(y = k\\,x\\). Verdubbel je het ene, "
                  "dan verdubbelt het andere. Een rechte die de as ergens anders snijdt, "
                  "\\(y = k\\,x + q\\), is wel <strong>lineair</strong> maar niet recht evenredig."),
        ]),
        dict(kop="Omgekeerd evenredig en kwadratisch", blokken=[
            ("p", "Bij een <strong>omgekeerd evenredig</strong> verband hoort een kromme die daalt "
                  "en de assen nadert. Het product van de twee grootheden blijft dan constant: "
                  "\\(x\\,y = k\\), dus \\(y = \\dfrac{k}{x}\\). De \\(p(V)\\)-grafiek bij constante "
                  "temperatuur is daarvan het schoolvoorbeeld. En bij een "
                  "<strong>kwadratisch</strong> verband, \\(y = k\\,x^{2}\\), hoort een parabool door "
                  "de oorsprong. Beduidend hoort bij de cijfers van een meting, niet in dit rijtje."),
        ]),
        dict(kop="Een formule omvormen", blokken=[
            ("p", "Weet je dat \\(F = m\\,a\\), dan vind je \\(a\\) door beide kanten door \\(m\\) "
                  "te delen: \\(a = \\dfrac{F}{m}\\). Zo vorm je elke formule om naar de grootheid "
                  "die je zoekt. Doe wat je links doet ook rechts, dan blijft de gelijkheid staan."),
            ("kader", "\\(F = m\\,a\\) geeft \\(a = \\dfrac{F}{m}\\) en \\(m = \\dfrac{F}{a}\\)."),
        ]),
        dict(kop="Twee formules combineren", blokken=[
            ("p", "Je mag ook twee formules combineren door een grootheid die in beide staat te "
                  "vervangen. Zo kom je aan een verband dat je niet rechtstreeks gemeten hebt. Let "
                  "er wel op dat je overal dezelfde eenheden gebruikt, en schrijf bij je antwoord "
                  "altijd de eenheid: zonder eenheid weet niemand of je \\(5\\ \\text{m}\\) of "
                  "\\(5\\ \\text{km}\\) bedoelt."),
        ]),
    ],
    onthoud=[
        "Meetbereik: niet erbuiten meten. Nauwkeurigheid: de kleinste stap.",
        "Het beste toestel is dat wat bij de meting past.",
        "Dynamometer, chronometer, decibelmeter, multimeter.",
        "Laagste stand eerst, droge handen, handleiding vooraf.",
        "Radioactieve bron: ver, kort en achter een afscherming.",
        "Milli \\(10^{-3}\\), micro \\(10^{-6}\\), nano \\(10^{-9}\\), kilo \\(10^{3}\\), mega \\(10^{6}\\).",
        "Beduidende cijfers: de slechtste meting bepaalt het antwoord.",
        "Wetenschappelijke notatie: één cijfer voor de komma.",
        "\\(y = k\\,x\\), \\(y = \\dfrac{k}{x}\\) of \\(y = k\\,x^{2}\\): kijk naar de grafiek.",
        "Elk antwoord krijgt zijn eenheid.",
    ],
)


# ───────────────────── 23. Wetenschappelijk onderzoek, ontwerpen en STEM
BUNDELS["wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="Van een vraag naar een antwoord, en van een probleem naar een ontwerp.",
    secties=[
        dict(kop="De stappen van een onderzoek", blokken=[
            ("fig", svg.stappen(["vraag|wat wil ik weten", "hypothese|wat verwacht ik",
                                 "plan|hoe ga ik meten", "meten|en verwerken",
                                 "besluit|wat is het antwoord"]),
             "Elke stap steunt op de vorige, en het besluit brengt je meestal bij een nieuwe vraag."),
            ("p", "Een <strong>onderzoeksvraag</strong> is de vraag die je met je onderzoek wil "
                  "beantwoorden. Een <strong>hypothese</strong> is de verwachting die je vooraf "
                  "opstelt en die je kan nagaan. En het <strong>onderzoeksplan</strong> is de stap "
                  "waarin je vastlegt hoe je je onderzoek zal uitvoeren: welke grootheid je "
                  "verandert, wat je meet en met welk toestel."),
            ("p", "Daarna komt het werk zelf: data verzamelen en analyseren. Een onderzoek begint "
                  "dus niet bij het meten maar bij het probleem definiëren en afbakenen."),
        ]),
        dict(kop="Een bruikbare onderzoeksvraag", blokken=[
            ("p", "Een onderzoeksvraag is bruikbaar wanneer je ze met een proef kan beantwoorden. "
                  "<em>Hoe hangt de periode van een slinger af van zijn lengte?</em> is zo'n vraag: "
                  "je weet meteen wat je zal veranderen, de lengte, en wat je zal meten, de "
                  "periode."),
            ("p", "Een onderzoeksvraag moet dus niet zo breed mogelijk opgesteld zijn. <em>Hoe werkt "
                  "zwaartekracht?</em> klinkt indrukwekkend, maar met één proef kom je er niet. Hoe "
                  "scherper de vraag, hoe duidelijker het antwoord dat je er achteraf op kan geven."),
        ]),
        dict(kop="Wat een hypothese moet kunnen", blokken=[
            ("p", "Over een hypothese gelden drie uitspraken. Ze wordt opgesteld voor je begint te "
                  "meten, ze moet met een proef na te gaan zijn, en ze kan door de resultaten "
                  "weerlegd worden. Die laatste is de belangrijkste: een verwachting die nooit fout "
                  "kan zijn, leert je niets."),
            ("p", "Een meting die je hypothese tegenspreekt is daarom een geldig resultaat, geen "
                  "mislukking. Je hebt dan iets geleerd wat je vooraf niet wist, en dat is precies "
                  "waarvoor je de proef deed."),
        ]),
        dict(kop="Eén grootheid tegelijk", blokken=[
            ("p", "In een proef verander je maar één grootheid tegelijk, anders weet je niet welke "
                  "verandering het verschil veroorzaakte. De grootheid die je bewust verandert heet "
                  "de <strong>onafhankelijke variabele</strong>; wat je daarbij meet is de "
                  "afhankelijke."),
            ("p", "Meet je de valtijd \\(t\\) van een bal vanaf verschillende hoogtes \\(h\\), dan "
                  "zet je de hoogte op de horizontale as, want die kies je zelf. Je tekent dus "
                  "\\(t(h)\\). Alle andere grootheden, zoals de massa van de bal, houd je constant."),
        ]),
        dict(kop="Herhalen en vergelijken", blokken=[
            ("p", "Je herhaalt een meting meerdere keren om toevallige afwijkingen uit je resultaat "
                  "te halen. Drie metingen die binnen een paar procent bij elkaar liggen zeggen veel "
                  "meer dan één enkele meting die er toevallig goed uitziet."),
            ("p", "Een <strong>controleproef</strong> dient om te vergelijken met een opstelling "
                  "waarin je niets verandert. Zonder dat ijkpunt weet je niet of het effect dat je "
                  "ziet van jouw ingreep komt of gewoon altijd gebeurt."),
            ("p", "Wijkt één meting sterk van de rest af, dan zoek je de oorzaak en vermeldt wat je "
                  "ermee doet. Weglaten mag alleen met een reden die je opschrijft, bijvoorbeeld dat "
                  "de chronometer te laat gestart is."),
        ]),
        dict(kop="Besluiten en verslag", blokken=[
            ("p", "Een goede conclusie beantwoordt de onderzoeksvraag op basis van de data. Ze gaat "
                  "niet verder dan wat je gemeten hebt: heb je slingers tot een meter gemeten, dan "
                  "zeg je niets over slingers van tien meter."),
            ("p", "In een goed verslag staat welke instrumenten je gebruikt hebt, welke grootheden "
                  "je constant gehouden hebt, en de meetwaarden met hun eenheid. Daarmee kan iemand "
                  "anders je proef overdoen."),
            ("p", "Dat is ook wat <strong>herhaalbaar</strong> betekent: iemand anders moet met jouw "
                  "plan hetzelfde kunnen vinden. Je laat anderen je resultaten nalezen omdat zij "
                  "fouten en andere verklaringen zien die jij gemist hebt, en reflecteren over je "
                  "gekozen methode hoort bij het onderzoek zelf, niet erna."),
        ]),
        dict(kop="Ontwerpen in stappen", blokken=[
            ("fig", svg.stappen(["probleem|helder definiëren", "criteria|waaraan moet het voldoen",
                                 "opsplitsen|in deelproblemen", "ontwerpen|en testen",
                                 "bijsturen|en opnieuw testen"]),
             "De laatste stap wijst terug naar de vorige: testen en bijsturen gaan een paar keer rond."),
            ("p", "De eerste stap bij het ontwerpen van een oplossing is het probleem helder "
                  "definiëren. Pas daarna stel je <strong>criteria</strong> op: de eisen waaraan je "
                  "oplossing moet voldoen. Die drie stappen samen, het probleem definiëren, criteria "
                  "opstellen en het probleem in deelproblemen splitsen, vormen een "
                  "probleemoplossende strategie."),
        ]),
        dict(kop="Criteria zijn meetbaar", blokken=[
            ("p", "Een criterium is meetbaar, zodat je achteraf kan nagaan of je het haalt. Moet je "
                  "een koeltas ontwerpen die een drankje \\(4\\) h koel houdt, dan is <em>de "
                  "temperatuur blijft na \\(4\\) h onder \\(8\\ ^\\circ\\text{C}\\)</em> een "
                  "criterium. <em>Mooi en opvallend</em> is dat niet: dat is een mening."),
            ("p", "De fysicakennis die bij die koeltas helpt, is hoe warmte zich door geleiding, "
                  "stroming en straling verplaatst. Je houdt alle drie die wegen tegen, zoals in een "
                  "thermosfles: een spiegelende laag in de wand kaatst de straling terug."),
        ]),
        dict(kop="Deelproblemen en de totaaloplossing", blokken=[
            ("p", "De kleinere stukken waarin je een groot probleem opsplitst heten "
                  "<strong>deelproblemen</strong>, soms ook subproblemen genoemd. Het geheel waarin "
                  "je de oplossingen van alle deelproblemen samenbrengt is de "
                  "<strong>totaaloplossing</strong>."),
            ("p", "Je mag een deelprobleem niet oplossen zonder na te gaan of het in de "
                  "totaaloplossing past. Een isolatielaag die perfect werkt maar niet meer in de tas "
                  "geraakt, lost niets op."),
        ]),
        dict(kop="Evalueren en bijsturen", blokken=[
            ("p", "Voldoet je ontwerp niet aan een criterium, dan stuur je het ontwerp bij en test "
                  "je opnieuw. Ook nadat je een gegeven oplossing geëvalueerd hebt, stuur je ze bij "
                  "waar ze de criteria niet haalt. Bij een ontwerp volstaat het trouwens soms om een "
                  "bestaand systeem aan te passen; je hoeft niet bij nul te beginnen."),
            ("p", "Drie vragen helpen je een ontwerp te evalueren. Haalt het elk criterium dat we "
                  "opgesteld hebben? Waar zit de zwakste schakel in het geheel? En wat zou de "
                  "volgende versie beter doen?"),
            ("p", "Ontwerp je een brug van spaghetti die zoveel mogelijk moet dragen, dan zet je het "
                  "evenwicht van krachten, \\(\\sum \\vec{F} = \\vec{0}\\), en het moment van een "
                  "kracht, \\(M = F\\,d\\), in. Je kijkt waar de krachten samenkomen en waar het "
                  "moment het grootst is: daar versterk je de constructie."),
        ]),
        dict(kop="STEM", blokken=[
            ("fig", svg.stemvierluik(),
             "Vier manieren van kijken naar hetzelfde probleem, die op één ontwerp uitkomen."),
            ("p", "De letters van <strong>STEM</strong> staan voor wetenschappen, technologie, "
                  "techniek en wiskunde. Je bekijkt een probleem vanuit verschillende disciplines "
                  "omdat elk vak een stuk van de oplossing aanbrengt. Bij een STEM-opdracht volstaat "
                  "het dus niet om één discipline grondig in te zetten: dan blijft een deel van het "
                  "probleem liggen."),
        ]),
        dict(kop="Corona als voorbeeld", blokken=[
            ("p", "Tijdens de coronacrisis bracht de wiskunde de verspreiding van het virus in "
                  "kaart. Met die modellen kon men zien wat een maatregel twee weken later zou doen, "
                  "lang voor de cijfers het lieten zien."),
            ("p", "Technologische kennis was voor heel andere taken nodig: het vaccin op een heel "
                  "lage temperatuur bewaren, het op grote schaal produceren, en het over de hele "
                  "wereld vervoeren. Geen enkele discipline had dat alleen gekund."),
        ]),
        dict(kop="Onderzoek en de samenleving", blokken=[
            ("p", "Maatschappelijke uitdagingen zijn een reden om nieuwe technieken en materialen te "
                  "ontwikkelen. Een pandemie, een energiecrisis of een droge zomer zet onderzoek in "
                  "gang dat er anders niet was gekomen."),
            ("p", "Daarom is een onderzoek naar zonnepanelen ook een maatschappelijke zaak: de "
                  "keuzes die eruit volgen raken ieders energie en kosten. Wat in een labo begint, "
                  "komt vroeg of laat op iemands dak terecht."),
        ]),
    ],
    onthoud=[
        "Onderzoeksvraag, hypothese, onderzoeksplan, meten, besluiten.",
        "Een hypothese moet weerlegd kunnen worden.",
        "Eén grootheid tegelijk; de onafhankelijke op de horizontale as.",
        "Herhalen haalt toevallige afwijkingen eruit; een controleproef vergelijkt.",
        "Een conclusie blijft binnen wat je gemeten hebt.",
        "Herhaalbaar: iemand anders vindt met jouw plan hetzelfde.",
        "Ontwerpen: definiëren, criteria, deelproblemen, testen, bijsturen.",
        "Een criterium is meetbaar, een mening niet.",
        "Elk deelprobleem moet in de totaaloplossing passen.",
        "STEM is wetenschappen, technologie, techniek en wiskunde samen.",
    ],
)
