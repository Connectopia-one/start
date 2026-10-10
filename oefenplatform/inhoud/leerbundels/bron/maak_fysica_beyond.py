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
        dict(kop="Stroom, spanning en weerstand", blokken=[
            ("p", "De <strong>elektrische stroomsterkte</strong> is <strong>de lading die per "
                  "seconde door een doorsnede gaat</strong>. Ze staat in <strong>ampère</strong>. De "
                  "<strong>afgesproken zin van de stroom is die van de positieve lading, dus van "
                  "plus naar min</strong>, terwijl de elektronen in werkelijkheid de andere kant op "
                  "lopen."),
            ("p", "In een stroomkring <strong>worden de elektronen niet door de draad "
                  "opgebruikt</strong>: ze draaien rond en er komen er net zo veel terug als er "
                  "vertrekken. Wat wél verbruikt wordt, is energie."),
            ("p", "De <strong>wet van Ohm</strong> zegt dat "
                  "<strong>de weerstand de spanning gedeeld door de stroomsterkte is</strong>, dus "
                  "ook dat <strong>de spanning de weerstand maal de stroomsterkte is</strong>. "
                  "<strong>Bij gelijke spanning geeft een grotere weerstand een kleinere "
                  "stroom</strong>, en de wet <strong>geldt voor een weerstand waarvan de waarde "
                  "niet verandert</strong>. Weerstand staat in <strong>ohm</strong>."),
            ("p", "Drie keer rekenen. Staat er <strong>12 V</strong> over een weerstand waar "
                  "<strong>3 A</strong> door loopt, dan is die weerstand <strong>4 Ω</strong>. Loopt "
                  "er <strong>0,4 A</strong> door een weerstand van <strong>25 Ω</strong>, dan staat "
                  "er <strong>10 V</strong> over. Staat een <strong>lamp van 6 Ω</strong> op een "
                  "bron van <strong>9 V</strong>, dan loopt er <strong>1,5 A</strong>. En "
                  "<strong>verdubbel je bij gelijke spanning de weerstand</strong>, dan "
                  "<strong>wordt de stroom half zo groot</strong>."),
            ("p", "De weerstand van een draad hangt af <strong>van de lengte van de draad</strong> "
                  "en <strong>van de dikte van de draad</strong>: lang en dun geeft veel weerstand, "
                  "kort en dik weinig. Ook de stof zelf telt mee. Een "
                  "<strong>draad wordt warm als er stroom door loopt</strong> omdat "
                  "<strong>de elektronen tegen de atomen van het rooster botsen</strong>."),
        ]),
        dict(kop="Meten en schema's", blokken=[
            ("p", "Een <strong>ampèremeter zet je in serie</strong> met het onderdeel waarvan je de "
                  "stroom meet, want de stroom moet er door. Hij heeft een "
                  "<strong>heel kleine eigen weerstand</strong>, want <strong>anders verandert hij "
                  "de stroom die hij wil meten</strong>. Het toestel dat de spanning tussen twee "
                  "punten meet, is de <strong>voltmeter</strong>; die zet je er juist naast."),
            ("p", "Een tekening van een stroomkring met symbolen in plaats van voorwerpen heet een "
                  "<strong>elektrisch schema</strong>. Daarin hebben onder meer "
                  "<strong>de schakelaar</strong> en <strong>de voltmeter</strong> hun eigen "
                  "symbool. Een <strong>schakelaar in open stand laat de stroom niet verder "
                  "lopen</strong>: de kring is dan onderbroken. Een "
                  "<strong>regelbare weerstand</strong> laat je de stroom in een kring instellen."),
            ("p", "Het verschil tussen <strong>gelijkstroom en wisselstroom</strong>: "
                  "<strong>gelijkstroom loopt altijd in dezelfde zin</strong>, wisselstroom keert "
                  "voortdurend van zin om. Een batterij geeft gelijkstroom, het stopcontact "
                  "wisselstroom."),
        ]),
        dict(kop="Serieschakeling", blokken=[
            ("p", "In een <strong>serieschakeling</strong> is de "
                  "<strong>stroomsterkte in elk onderdeel even groot</strong>; dat is dus "
                  "<strong>de grootheid die overal even groot is</strong>. Verder geldt: "
                  "<strong>de spanningen over de weerstanden tellen samen tot de "
                  "bronspanning</strong>, en de <strong>vervangingsweerstand is de som van de "
                  "weerstanden</strong>. De <strong>som van de deelspanningen is dus niet groter dan "
                  "de bronspanning</strong>, maar precies gelijk."),
            ("p", "Die ene weerstand die je in de plaats van een hele schakeling mag denken, heet "
                  "de <strong>vervangingsweerstand</strong>. Twee weerstanden van "
                  "<strong>4 Ω en 6 Ω in serie</strong> geven <strong>10 Ω</strong>."),
            ("p", "Rekenen met drie weerstanden: <strong>2 Ω, 3 Ω en 5 Ω in serie op een bron van "
                  "20 V</strong> geven samen 10 Ω, dus loopt er <strong>2 A</strong>. Over de "
                  "weerstand van <strong>3 Ω</strong> staat dan <strong>6 V</strong>."),
            ("p", "Omdat de stroom door alles moet, dooft <strong>één kapotte lamp de hele "
                  "reeks</strong> als de lampen <strong>in serie</strong> staan. Dan "
                  "<strong>blijft de rest dus niet werken</strong>."),
        ]),
        dict(kop="Parallelschakeling", blokken=[
            ("p", "In een <strong>parallelschakeling</strong> staat "
                  "<strong>over elke tak dezelfde spanning</strong> en "
                  "<strong>tellen de stromen van de takken samen tot de hoofdstroom</strong>; "
                  "<strong>de totale stroom is dus de som van de deelstromen</strong>. "
                  "<strong>Door de kleinste weerstand loopt de grootste stroom</strong>, en "
                  "<strong>door elke tak loopt dus niet dezelfde stroom</strong>."),
            ("p", "De <strong>vervangingsweerstand is kleiner dan de kleinste weerstand</strong>: "
                  "<strong>hoe meer weerstanden je parallel bijzet, hoe kleiner de totale weerstand "
                  "wordt</strong>. <strong>Twee gelijke weerstanden parallel geven samen de helft "
                  "van één ervan.</strong> Twee weerstanden van <strong>4 Ω en 6 Ω parallel</strong> "
                  "geven <strong>2,4 Ω</strong>."),
            ("p", "Staan <strong>6 Ω en 12 Ω parallel op 24 V</strong>, dan loopt er 4 A door de "
                  "eerste en 2 A door de tweede, dus <strong>levert de bron 6 A</strong>."),
            ("p", "Omdat <strong>elke lamp haar eigen weg naar de bron heeft</strong>, "
                  "<strong>blijven de andere lampen branden als er in een parallelschakeling één "
                  "lamp stukgaat</strong>. Daarom staan de lampen in een huis parallel."),
        ]),
        dict(kop="Gemengde schakelingen", blokken=[
            ("p", "Bij een <strong>gemengde schakeling reken je eerst het parallelle stuk uit en "
                  "pas daarna de serie</strong>. Je vervangt het parallelle stuk door één weerstand "
                  "en houdt zo een gewone serieschakeling over."),
            ("p", "Een voorbeeld dat in drie stappen gaat. Een weerstand van "
                  "<strong>10 Ω in serie met twee parallelle weerstanden van elk 20 Ω</strong>: die "
                  "twee geven samen 10 Ω, dus is de totale weerstand <strong>20 Ω</strong>. Staat "
                  "die schakeling op <strong>40 V</strong>, dan levert de bron "
                  "<strong>2 A</strong>. Over het <strong>parallelle stuk</strong> staat dan "
                  "2 A maal 10 Ω, dus <strong>20 V</strong>."),
        ]),
    ],
    onthoud=[
        "Stroomsterkte is lading per seconde, in ampère.",
        "Wet van Ohm: U = R · I.",
        "Een ampèremeter staat in serie, een voltmeter ernaast.",
        "In serie: dezelfde stroom, spanningen tellen op, weerstanden tellen op.",
        "Parallel: dezelfde spanning, stromen tellen op, totale weerstand daalt.",
        "Twee gelijke weerstanden parallel geven de helft.",
        "Gemengd: eerst het parallelle stuk, dan de serie.",
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
                  "schudt</strong>."),
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
                  "ongelijknamige polen trekken elkaar aan."),
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
            ("p", "Twee patronen om te kennen: rond een gewone staafmagneet krijg je een "
                  "<strong>dipoolveld</strong>, en tussen de twee benen van een "
                  "<strong>hoefijzermagneet</strong> een <strong>homogeen veld</strong>. De "
                  "<strong>magnetische inductie</strong> krijgt het symbool <strong>B</strong> en "
                  "staat in <strong>tesla</strong>."),
        ]),
        dict(kop="Het veld van een stroom", blokken=[
            ("p", "Rond een <strong>rechte stroomvoerende draad</strong> ziet het magnetisch veld "
                  "eruit <strong>als cirkels rond de draad heen</strong>. De "
                  "<strong>rechterhandregel</strong> dient <strong>om de zin van die veldlijnen rond "
                  "de draad te vinden</strong>: duim in de stroomzin, de vingers krullen mee met het "
                  "veld. Het is de regel waarmee je <strong>met je rechterhand de zin van een "
                  "magnetisch veld vindt</strong>."),
            ("p", "<strong>Verdubbel je de stroom</strong> door een rechte draad, dan "
                  "<strong>wordt het veld twee keer zo sterk</strong>. Ga je "
                  "<strong>twee keer zo ver staan</strong>, dan wordt het "
                  "<strong>half zo sterk</strong>: bij een rechte draad gaat het met één keer de "
                  "afstand."),
            ("p", "In het midden van een <strong>stroomvoerende cirkelvormige lus</strong> "
                  "<strong>staat het veld loodrecht op het vlak van de lus</strong>. De "
                  "<strong>noordpool van een stroomvoerende spoel</strong> vind je "
                  "<strong>met de rechterhand: de vingers volgen de stroom, de duim wijst naar "
                  "noord</strong>."),
            ("p", "Het veld <strong>binnen in een lange stroomvoerende spoel is nagenoeg "
                  "homogeen</strong>, en het hangt af <strong>van het aantal windingen per "
                  "meter</strong> en <strong>van de stroom die erdoor loopt</strong>. Zet je "
                  "<strong>twee stroomvoerende spoelen met hun noordpolen naar elkaar toe</strong>, "
                  "dan <strong>stoten ze elkaar af, net als twee gewone magneten</strong>."),
        ]),
        dict(kop="De elektromagneet", blokken=[
            ("p", "Het verschil tussen een <strong>permanente magneet en een elektromagneet</strong>: "
                  "<strong>een elektromagneet werkt alleen als er stroom loopt</strong>. Een "
                  "<strong>ijzeren kern</strong> in een elektromagneet dient "
                  "<strong>om het magnetisch veld veel sterker te maken</strong>, want de "
                  "weissgebieden in het ijzer richten zich mee."),
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
        "Rond een rechte draad zijn de veldlijnen cirkels; rechterhandregel.",
        "In een spoel is het veld homogeen en hangt het af van n/l en I.",
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
                  "het vlak van die twee."),
            ("p", "De kracht hangt af <strong>van de stroomsterkte door de draad</strong>, "
                  "<strong>van de sterkte van het magnetisch veld</strong> en "
                  "<strong>van de lengte van de draad in het veld</strong>. Ze is dus "
                  "<strong>recht evenredig met de stroomsterkte</strong> en "
                  "<strong>recht evenredig met de magnetische inductie</strong>. Van de eigen "
                  "weerstand van de draad hangt ze niet af."),
            ("p", "Ook de hoek telt mee. De kracht is <strong>het grootst als de draad loodrecht op "
                  "de veldlijnen staat</strong>, en een <strong>draad die evenwijdig met de "
                  "veldlijnen ligt, voelt geen magnetische kracht</strong>. Staat een draad "
                  "<strong>onder 30 graden met de veldlijnen</strong> in plaats van loodrecht, dan "
                  "<strong>wordt de kracht kleiner, want de sinus van 30 graden is maar een "
                  "half</strong>."),
            ("p", "Rekenen: een draad van <strong>0,5 m</strong> die loodrecht in een veld van "
                  "<strong>0,2 T</strong> ligt en <strong>3 A</strong> voert, voelt een kracht van "
                  "<strong>0,3 N</strong>. De zin van die kracht vind je "
                  "<strong>met je rechterhand: vingers in de stroomzin, veld in de handpalm, duim "
                  "geeft de kracht</strong>."),
            ("p", "Twee evenwijdige draden werken ook op elkaar. Voeren ze "
                  "<strong>stroom in dezelfde zin</strong>, dan "
                  "<strong>trekken ze elkaar aan</strong>; voeren ze "
                  "<strong>stroom in tegengestelde zin</strong>, dan "
                  "<strong>stoten ze elkaar af</strong>. Die kracht "
                  "<strong>wordt groter als ze dichter bij elkaar liggen</strong>, niet kleiner."),
        ]),
        dict(kop="Motor en luidspreker", blokken=[
            ("p", "Een <strong>luidspreker</strong> werkt doordat "
                  "<strong>de wisselstroom in een spoel het membraan heen en weer duwt</strong>. De "
                  "kracht die dat doet, is de <strong>laplacekracht</strong>, en omdat de stroom "
                  "van zin wisselt, wisselt ook de kracht van zin."),
            ("p", "De <strong>spoel van een gelijkstroommotor draait</strong> omdat "
                  "<strong>de krachten op de twee zijden in tegengestelde zin wijzen</strong>: in de "
                  "ene zijde loopt de stroom de ene kant op, in de andere de andere kant. De "
                  "<strong>collector</strong> dient <strong>om de stroom elke halve omwenteling om "
                  "te keren</strong>, zodat het koppel altijd dezelfde kant op blijft duwen."),
        ]),
        dict(kop="De lorentzkracht op een lading", blokken=[
            ("p", "De kracht op één bewegende lading in een magnetisch veld heet de "
                  "<strong>lorentzkracht</strong>. Ze hangt af "
                  "<strong>van de grootte van de lading</strong> en "
                  "<strong>van de snelheid van de lading</strong>, en natuurlijk ook van het veld en "
                  "van de hoek ermee. Een <strong>stilstaande lading in een magnetisch veld voelt "
                  "geen magnetische kracht</strong>, want zonder snelheid is er geen kracht. Een "
                  "lading die <strong>precies evenwijdig met de veldlijnen</strong> beweegt, voelt "
                  "<strong>geen enkele kracht, want de hoek met het veld is nul</strong>."),
            ("p", "Rekenen: een lading van <strong>2 mC</strong> die met <strong>500 m/s</strong> "
                  "loodrecht door een veld van <strong>0,4 T</strong> beweegt, voelt een kracht van "
                  "<strong>0,4 N</strong>."),
            ("p", "De <strong>magnetische kracht op een lading staat loodrecht op haar "
                  "snelheid</strong>. Daardoor verricht ze geen arbeid en "
                  "<strong>kan een magnetisch veld de snelheid van een lading niet groter "
                  "maken</strong>: het buigt haar alleen af."),
        ]),
        dict(kop="De cirkelbaan", blokken=[
            ("p", "Een lading die <strong>loodrecht een homogeen magnetisch veld "
                  "binnenkomt</strong>, volgt een <strong>cirkelbaan</strong>, want de kracht blijft "
                  "loodrecht op de snelheid staan en werkt dus als middelpuntzoekende kracht. Een "
                  "<strong>deeltje dat schuin binnenkomt, gaat niet rechtdoor</strong>: het volgt "
                  "een schroeflijn."),
            ("p", "De straal van die cirkelbaan hangt af van <strong>de massa van het "
                  "deeltje</strong>, <strong>de snelheid van het deeltje</strong> en "
                  "<strong>de sterkte van het magnetisch veld</strong>, en ook van zijn lading. "
                  "<strong>Verdubbel je het magnetisch veld</strong>, dan "
                  "<strong>wordt de straal half zo groot</strong>. Een sneller deeltje maakt een "
                  "ruimere bocht."),
            ("p", "Maken <strong>twee deeltjes met dezelfde lading en snelheid</strong> in hetzelfde "
                  "veld een bocht met een andere straal, dan verschilt <strong>hun massa</strong>. "
                  "Vliegen een <strong>positieve en een negatieve lading</strong> met dezelfde "
                  "snelheid het veld binnen, dan <strong>buigen ze naar tegengestelde kanten "
                  "af</strong>."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("p", "De <strong>massaspectrometer</strong> is het toestel dat "
                  "<strong>ionen op hun massa scheidt met een magnetisch veld</strong>. Je weet "
                  "<strong>aan de straal van de bocht die het deeltje beschrijft</strong> of het "
                  "zwaar of licht is: een zwaar deeltje maakt een ruimere bocht."),
            ("p", "Een <strong>cyclotron</strong> dient <strong>om geladen deeltjes tot hoge "
                  "snelheid te versnellen</strong>. Daarin <strong>doet het magnetisch veld niet het "
                  "versnellende werk</strong>: het houdt de deeltjes in hun cirkelbaan, terwijl een "
                  "elektrisch veld ze bij elke ronde een duw geeft. De "
                  "<strong>massaspectrometer</strong> en het <strong>cyclotron</strong> berusten dus "
                  "beide op de kracht op bewegende ladingen."),
            ("p", "Een <strong>hallsensor</strong> dient <strong>om de sterkte van een magnetisch "
                  "veld te meten</strong>. En je ziet het "
                  "<strong>noorderlicht vooral in de buurt van de polen</strong> omdat "
                  "<strong>het aardmagnetisch veld de geladen deeltjes daarheen leidt</strong>. "
                  "<strong>Zuurstof geeft daarbij meestal groen licht</strong>."),
        ]),
    ],
    onthoud=[
        "Laplacekracht: op een stroomvoerende draad, loodrecht op draad en veld.",
        "Evenwijdig met het veld is er geen kracht; loodrecht is ze maximaal.",
        "Gelijke stroomzin trekt aan, tegengestelde stoot af.",
        "Lorentzkracht: op een bewegende lading, loodrecht op haar snelheid.",
        "Een magnetisch veld buigt af maar versnelt niet.",
        "Loodrecht binnenkomen geeft een cirkelbaan; zwaarder is een ruimere bocht.",
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
                  "<strong>het veld maal de doorsneden oppervlakte, met de hoek erbij</strong>. Ze "
                  "hangt dus af van <strong>de sterkte van het magnetisch veld</strong>, "
                  "<strong>de oppervlakte van de winding</strong> en "
                  "<strong>de hoek tussen de winding en het veld</strong>, en ze is het grootst als "
                  "de winding loodrecht in het veld staat. Flux staat in "
                  "<strong>weber</strong>."),
            ("p", "Rekenen: een winding van <strong>0,02 m²</strong> die loodrecht in een veld van "
                  "<strong>0,5 T</strong> staat, heeft een flux van <strong>0,01 Wb</strong>."),
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
                  "verbindt</strong>."),
            ("p", "De inductiespanning van een spoel wordt bepaald door "
                  "<strong>het aantal windingen</strong> en "
                  "<strong>de snelheid waarmee de flux verandert</strong>. "
                  "<strong>Verdubbel je het aantal windingen</strong>, dan "
                  "<strong>wordt ze twee keer zo groot</strong>. Een spoel met "
                  "<strong>200 windingen</strong> die de flux <strong>in 0,1 s met 0,004 Wb</strong> "
                  "ziet veranderen, geeft <strong>8 V</strong>."),
            ("p", "Een <strong>magneet die je sneller in een spoel duwt, levert meer spanning "
                  "op</strong>, want <strong>de flux verandert dan in minder tijd evenveel</strong>. "
                  "Op een fluxgrafiek lees je dat rechtstreeks af: "
                  "<strong>hoe steiler de fluxgrafiek loopt, hoe gróter de inductiespanning op dat "
                  "ogenblik</strong>, en waar de <strong>flux een tijdlang constant blijft, is de "
                  "inductiespanning nul</strong>."),
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
                  "verhouding als de aantallen windingen. Hij "
                  "<strong>werkt niet op gelijkspanning</strong>, want dan verandert de flux niet."),
            ("p", "Twee voorbeelden. Een transformator met <strong>500 windingen primair en 50 "
                  "secundair</strong> <strong>verlaagt 230 V tot 23 V</strong>. Een transformator met "
                  "<strong>100 windingen primair en 400 secundair</strong> is "
                  "<strong>een optransformator, want hij verhoogt de spanning</strong>."),
            ("p", "Een transformator <strong>kan het vermogen niet groter maken dan het vermogen "
                  "dat erin gaat</strong>: gaat de spanning omhoog, dan gaat de stroom omlaag. Dat "
                  "is ook waarom <strong>stroom over grote afstanden op hoogspanning vervoerd "
                  "wordt</strong>: <strong>bij een kleinere stroom gaat er veel minder warmte "
                  "verloren</strong> in de kabels."),
            ("p", "De <strong>kern van een transformator is uit dunne, van elkaar geïsoleerde "
                  "plaatjes</strong> opgebouwd <strong>om de wervelstromen in de kern klein te "
                  "houden</strong>."),
        ]),
        dict(kop="Wervelstromen", blokken=[
            ("p", "<strong>Wervelstromen</strong> zijn de kringstromen die "
                  "<strong>in een massief stuk metaal ontstaan bij een veranderende flux</strong>. "
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
        "Flux is veld maal oppervlakte, met de hoek erbij, in weber.",
        "Faraday: de inductiespanning hangt af van hoe snel de flux verandert.",
        "Meer windingen of sneller veranderen geeft meer spanning.",
        "Lenz: de inductiestroom werkt zijn eigen oorzaak tegen.",
        "Zonder gesloten kring wel spanning, geen stroom.",
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
                  "<strong>kg·m/s²</strong>."),
            ("p", "De <strong>zwaartekracht</strong> op een massa reken je als massa maal g. Op "
                  "<strong>8 kg</strong> met <strong>g gelijk aan 9,81 N/kg</strong> is dat "
                  "<strong>ongeveer 78 N</strong>. Het <strong>gewicht</strong> "
                  "<strong>is een kracht en staat dus in newton</strong>, en het "
                  "<strong>hangt af van de plaats waar je je bevindt</strong>; de massa niet."),
            ("p", "<strong>Twee krachten die niet op één lijn liggen</strong>, stel je samen "
                  "<strong>met de parallellogramregel voor vectoren</strong>. Staan "
                  "<strong>6 N en 8 N loodrecht op elkaar</strong> in hetzelfde punt, dan is de "
                  "resulterende kracht <strong>10 N</strong>, volgens de stelling van Pythagoras."),
            ("p", "Je <strong>ontbindt een kracht in componenten</strong> "
                  "<strong>om apart te kunnen rekenen langs twee loodrechte assen</strong>. Staat "
                  "een <strong>kist op een helling</strong>, dan laat "
                  "<strong>de component langs het hellend vlak</strong> haar naar beneden glijden; "
                  "de andere component drukt op het vlak."),
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
                  "aan 10 N/kg."),
            ("p", "De <strong>veerkracht is recht evenredig met de uitrekking</strong> van de veer, "
                  "niet omgekeerd evenredig. Een veer met een "
                  "<strong>veerconstante van 50 N/m</strong> die <strong>8 cm</strong> uitgerekt "
                  "wordt, levert <strong>4 N</strong>."),
            ("p", "Hangt een <strong>lamp stil aan één koord</strong>, dan is de "
                  "<strong>spankracht even groot als de zwaartekracht op de lamp</strong>. En op een "
                  "<strong>auto die met constante snelheid rijdt</strong>, werken onder meer "
                  "<strong>de motorkracht naar voren</strong> en "
                  "<strong>de wrijvingskracht naar achter</strong>, en die twee houden elkaar in "
                  "evenwicht."),
        ]),
        dict(kop="Translatie-evenwicht", blokken=[
            ("p", "<strong>Translatie-evenwicht</strong> betekent dat "
                  "<strong>de som van alle krachten op het lichaam nul is</strong>. Een "
                  "<strong>lichaam in translatie-evenwicht hoeft niet stil te staan</strong>: ook "
                  "een lichaam met een constante snelheid is in evenwicht, want zijn snelheid "
                  "verandert niet."),
        ]),
        dict(kop="Het moment van een kracht", blokken=[
            ("p", "Het <strong>moment van een kracht</strong> is "
                  "<strong>de kracht maal de krachtarm ten opzichte van het draaipunt</strong>, en "
                  "het staat in <strong>newtonmeter</strong>. De <strong>krachtarm</strong> is de "
                  "kortste afstand van het draaipunt tot de werklijn van de kracht. Een "
                  "<strong>kracht waarvan de werklijn door het draaipunt gaat, heeft geen "
                  "moment</strong>, want dan is die arm nul."),
            ("p", "Rekenen: een kracht van <strong>30 N</strong> die "
                  "<strong>loodrecht op 0,4 m van het draaipunt</strong> werkt, geeft een moment van "
                  "<strong>12 Nm</strong>. Werkt diezelfde kracht "
                  "<strong>onder 30 graden met de stang</strong>, nog altijd op 0,4 m, dan is het "
                  "moment maar <strong>6 Nm</strong>, want de sinus van 30 graden is een half."),
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
                  "moeten nul zijn</strong>."),
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
                  "<strong>waarin je de hele massa van een lichaam mag denken</strong>. Voor "
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
        "Een kracht heeft grootte, richting en zin; de newton is kg·m/s².",
        "Krachten die niet op één lijn liggen: parallellogramregel.",
        "De normaalkracht staat loodrecht op het oppervlak.",
        "Translatie-evenwicht: som van de krachten nul, snelheid mag constant zijn.",
        "Moment is kracht maal krachtarm, in newtonmeter.",
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
                  "<strong>de resulterende kracht de massa maal de versnelling is</strong>. De "
                  "<strong>resulterende kracht</strong> is <strong>de vectoriële som van alle "
                  "krachten</strong> en ze <strong>wijst in dezelfde zin als de versnelling</strong>: "
                  "<strong>de versnelling wijst altijd in dezelfde zin als de resulterende "
                  "kracht</strong>. Versnelling staat in <strong>m/s²</strong>."),
            ("p", "Drie keer rekenen. Werkt op een lichaam van <strong>4 kg</strong> een "
                  "resulterende kracht van <strong>12 N</strong>, dan is de versnelling "
                  "<strong>3 m/s²</strong>. Wordt een <strong>kist van 5 kg met 20 N geduwd</strong> "
                  "terwijl ze <strong>5 N wrijving</strong> voelt, dan blijft er 15 N over en is de "
                  "versnelling <strong>3 m/s²</strong>. Om een lichaam van "
                  "<strong>2 kg vanuit rust in 5 s tot 10 m/s</strong> te brengen, heb je "
                  "<strong>4 N</strong> nodig."),
            ("p", "De massa werkt tegen: een <strong>grotere massa heeft bij dezelfde kracht een "
                  "kleinere versnelling</strong>. Krijgen een <strong>wagen van 1000 kg en een "
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
                  "In de tweede wet valt de massa dan aan beide kanten weg."),
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
        "Tweede wet: F = m · a; de versnelling volgt de resulterende kracht.",
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
            ("p", "Een <strong>eenparig rechtlijnige beweging</strong> is "
                  "<strong>een beweging op een rechte lijn met constante snelheid</strong>. De "
                  "afkorting <strong>ERB</strong> staat voor "
                  "<strong>eenparig rechtlijnige beweging</strong>. Bij een ERB zijn "
                  "<strong>de gemiddelde en de ogenblikkelijke snelheid even groot</strong>."),
            ("p", "De <strong>x(t)-grafiek van een ERB</strong> is "
                  "<strong>een rechte met een constante helling</strong>, en de "
                  "<strong>a(t)-grafiek valt samen met de tijdas</strong>, want er is geen "
                  "versnelling."),
            ("p", "Rekenen: een <strong>auto die 150 km in 2 uur</strong> rijdt, heeft een "
                  "gemiddelde snelheid van <strong>75 km/h</strong>. Een "
                  "<strong>trein met 20 m/s</strong> komt in <strong>2 minuten</strong> "
                  "<strong>2400 m</strong> verder. Vertrekken "
                  "<strong>twee fietsers samen, de ene met 4 m/s en de andere met 6 m/s</strong>, "
                  "dan liggen ze na <strong>30 s</strong> <strong>60 m</strong> uit elkaar. En "
                  "<strong>72 km/h</strong> is <strong>20</strong> meter per seconde: je deelt door "
                  "3,6."),
        ]),
        dict(kop="Weg, verplaatsing en snelheid", blokken=[
            ("p", "<strong>Afgelegde weg en verplaatsing zijn niet altijd even groot.</strong> "
                  "Rijdt een <strong>fietser 3 km naar het noorden en daarna 3 km terug</strong>, "
                  "dan is de <strong>weg 6 km en de verplaatsing 0 km</strong>: hij staat weer waar "
                  "hij vertrok."),
            ("p", "Een snelheid <strong>heeft een grootte, een richting en een zin</strong> en "
                  "<strong>wordt voorgesteld door een vector</strong>. Daarom "
                  "<strong>kan een snelheid langs de x-as wel negatief zijn</strong>: dat betekent "
                  "dat het lichaam de andere kant op gaat."),
            ("p", "Het verschil tussen de <strong>gemiddelde en de ogenblikkelijke snelheid</strong>: "
                  "<strong>de gemiddelde snelheid kijkt naar een heel traject, de ogenblikkelijke "
                  "naar één moment</strong>. Om een gemiddelde snelheid te berekenen heb je "
                  "<strong>de afgelegde weg</strong> en "
                  "<strong>de tijdsduur van de beweging</strong> nodig; je deelt de eerste door de "
                  "tweede."),
        ]),
        dict(kop="Grafieken lezen", blokken=[
            ("p", "Drie dingen over een <strong>x(t)-grafiek</strong>: "
                  "<strong>de helling van de grafiek is de snelheid</strong> op dat ogenblik, "
                  "<strong>een horizontaal stuk betekent dat het lichaam stilstaat</strong>, en "
                  "<strong>een dalend stuk betekent dat het terugkeert naar het vertrekpunt</strong>. "
                  "Loopt een x(t)-grafiek <strong>eerst stijgend en daarna dalend</strong>, dan "
                  "<strong>keert het lichaam onderweg om en komt het terug</strong>."),
            ("p", "De <strong>oppervlakte onder een v(t)-grafiek</strong> stelt "
                  "<strong>de verplaatsing van het lichaam</strong> voor; dat is dus "
                  "<strong>de grootheid die je uit die oppervlakte afleest</strong>. En de "
                  "<strong>oppervlakte onder een a(t)-grafiek geeft de "
                  "snelheidsverandering</strong>."),
        ]),
        dict(kop="De eenparig veranderlijke rechtlijnige beweging", blokken=[
            ("p", "Bij een <strong>eenparig veranderlijke rechtlijnige beweging</strong> "
                  "<strong>blijft de versnelling dezelfde</strong>, is "
                  "<strong>de v(t)-grafiek een rechte</strong> en is "
                  "<strong>de x(t)-grafiek een parabool</strong>. Die "
                  "<strong>v(t)-grafiek is dus een schuine rechte</strong>. Een "
                  "<strong>vrije val zonder luchtweerstand</strong> en "
                  "<strong>een auto die gelijkmatig optrekt</strong> zijn er voorbeelden van."),
            ("p", "Rekenen met de versnelling. Een <strong>auto die in 8 s van 0 naar 24 m/s</strong> "
                  "gaat, heeft een versnelling van <strong>3 m/s²</strong>. Een "
                  "<strong>fietser die van 10 m/s naar stilstand remt in 5 s</strong> heeft een "
                  "versnelling van <strong>−2 m/s²</strong>. Een "
                  "<strong>negatieve versnelling betekent niet altijd dat het lichaam "
                  "vertraagt</strong>: ze betekent enkel dat de versnelling tegen de positieve zin "
                  "van de as in wijst."),
            ("p", "Rekenen met weg en snelheid. Een <strong>wagen die uit rust vertrekt met "
                  "2 m/s²</strong> komt in <strong>6 s</strong> <strong>36 m</strong> ver en rijdt "
                  "dan <strong>12 m/s</strong>. Een <strong>auto met 15 m/s die remt met "
                  "3 m/s²</strong> heeft <strong>37,5 m</strong> nodig om te stoppen, en "
                  "<strong>bij dubbele snelheid is de remweg vier keer zo lang</strong>, want de "
                  "snelheid staat in het kwadraat."),
            ("p", "Een inhaaloefening: rijdt een <strong>wagen met 20 m/s voorbij een stilstaande "
                  "motor die meteen vertrekt met 4 m/s²</strong>, dan haalt de motor hem in "
                  "<strong>na 10 s</strong> in, want dan hebben beide 200 m afgelegd."),
        ]),
        dict(kop="De vrije val", blokken=[
            ("p", "Een <strong>vrije val</strong> is een beweging "
                  "<strong>waarbij enkel de zwaartekracht werkt en de beginsnelheid nul is</strong>. "
                  "De <strong>valversnelling op aarde</strong> is ongeveer "
                  "<strong>9,81 m/s²</strong>; in oefeningen rekenen we vaak met 10."),
            ("p", "Drie dingen gelden voor een vrije val zonder luchtweerstand: "
                  "<strong>de versnelling blijft de hele val even groot</strong>, "
                  "<strong>de snelheid groeit recht evenredig met de tijd</strong> en "
                  "<strong>de afgelegde hoogte groeit met het kwadraat van de tijd</strong>. De "
                  "<strong>valtijd hangt niet af van de massa van het voorwerp</strong>."),
            ("p", "Rekenen: een <strong>steen valt na 3 s</strong> met <strong>30 m/s</strong>, met "
                  "g gelijk aan 10 m/s². Doet een steen <strong>2 s</strong> over het bereiken van "
                  "de bodem van een put, dan is die put <strong>20 m</strong> diep."),
            ("p", "Gooi je een <strong>bal recht omhoog</strong>, dan geldt in het hoogste punt: "
                  "<strong>de snelheid is nul en de versnelling niet</strong>, want de zwaartekracht "
                  "blijft werken. Gooi je hem met <strong>20 m/s</strong> omhoog, dan duurt het "
                  "<strong>2 s</strong> tot het hoogste punt."),
        ]),
    ],
    onthoud=[
        "ERB: rechte lijn, constante snelheid, x(t) een rechte, a(t) op de as.",
        "Weg en verplaatsing zijn niet hetzelfde; snelheid is een vector.",
        "Helling van x(t) is de snelheid; oppervlakte onder v(t) is de verplaatsing.",
        "EVRB: constante versnelling, v(t) een rechte, x(t) een parabool.",
        "Negatieve versnelling betekent niet automatisch vertragen.",
        "Dubbele snelheid is vier keer de remweg.",
        "Vrije val: g is ongeveer 9,81 m/s², onafhankelijk van de massa.",
        "In het hoogste punt is de snelheid nul, de versnelling niet.",
    ],
)

# ───────────────────── 11. De horizontale worp
BUNDELS["de-horizontale-worp-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De horizontale worp",
    onder="Twee bewegingen tegelijk: eenparig naar voren en vallend naar beneden.",
    secties=[
        dict(kop="Het onafhankelijkheidsbeginsel", blokken=[
            ("p", "Het <strong>onafhankelijkheidsbeginsel</strong> bij een horizontale worp zegt "
                  "dat <strong>de horizontale en de verticale beweging elkaar niet "
                  "beïnvloeden</strong>. Het is dus <strong>het beginsel dat de horizontale en de "
                  "verticale beweging los van elkaar laat verlopen</strong>."),
            ("p", "Het <strong>horizontale deel</strong> is een "
                  "<strong>eenparig rechtlijnige beweging</strong> en het "
                  "<strong>verticale deel</strong> een "
                  "<strong>vrije val met beginsnelheid nul</strong>: de "
                  "<strong>verticale beginsnelheid is dus nul</strong>. De grootheid die "
                  "<strong>bij de horizontale en de verticale beweging dezelfde is</strong>, is "
                  "<strong>de tijd</strong>, en dat is net wat de twee met elkaar verbindt."),
            ("p", "De baan van een horizontale worp heeft de vorm van een "
                  "<strong>parabool</strong>. Tijdens de vlucht werkt, zonder luchtweerstand, "
                  "<strong>enkel de zwaartekracht, recht naar beneden</strong>."),
        ]),
        dict(kop="Valtijd en dracht", blokken=[
            ("p", "De <strong>valtijd</strong> hangt af <strong>van de hoogte waarvan je "
                  "werpt</strong> en <strong>van de valversnelling g</strong>, en "
                  "<strong>niet van de beginsnelheid</strong>: "
                  "<strong>de valtijd hangt dus enkel van de hoogte af</strong>. De "
                  "<strong>grootheid die je bij een horizontale worp eerst uitrekent</strong>, is "
                  "daarom <strong>de valtijd</strong>."),
            ("p", "Daarom raken <strong>twee kogels die tegelijk van dezelfde hoogte "
                  "vertrekken</strong>, de ene gewoon vallend en de andere horizontaal "
                  "weggeschoten, <strong>de grond op hetzelfde ogenblik</strong>. Ook "
                  "<strong>twee ballen die van dezelfde hoogte horizontaal vertrekken met "
                  "verschillende snelheid, raken de grond tegelijk</strong>. Bij "
                  "<strong>twee identieke ballen van dezelfde tafel, de ene twee keer zo snel als "
                  "de andere</strong>, verschilt dus <strong>enkel de dracht, en die is dubbel zo "
                  "groot</strong>."),
            ("p", "De <strong>dracht</strong> is <strong>de horizontale afstand die een voorwerp "
                  "bij een worp aflegt</strong>. Ze hangt af van "
                  "<strong>de hoogte waarvan je werpt</strong> en "
                  "<strong>de horizontale beginsnelheid</strong>. "
                  "<strong>Verdubbel je de beginsnelheid</strong> bij dezelfde hoogte, dan "
                  "<strong>wordt ze twee keer zo groot</strong>. <strong>Verviervoudig je de "
                  "hoogte</strong> bij dezelfde beginsnelheid, dan wordt ze "
                  "<strong>twee keer zo groot</strong>, want de valtijd gaat met de wortel van de "
                  "hoogte. De <strong>dracht is dus niet recht evenredig met de hoogte</strong>."),
            ("p", "Zonder luchtweerstand <strong>komt een zwaarder voorwerp bij dezelfde worp even "
                  "ver als een lichter voorwerp</strong>. In het echt "
                  "<strong>valt een pingpongbal korter dan de formules voorspellen</strong>, want "
                  "<strong>de luchtweerstand remt hem horizontaal af</strong>."),
        ]),
        dict(kop="Snelheid tijdens de vlucht", blokken=[
            ("p", "De <strong>horizontale snelheid blijft tijdens de vlucht precies even "
                  "groot</strong>, zonder luchtweerstand, want in die richting werkt geen kracht. De "
                  "<strong>verticale snelheid groeit elke seconde met ongeveer 9,81 m/s "
                  "aan</strong>. Daardoor <strong>wordt de snelheid van het voorwerp tijdens de "
                  "vlucht steeds groter</strong>."),
            ("p", "De snelheid op een bepaald ogenblik vind je door "
                  "<strong>de horizontale en de verticale snelheid samen te stellen met "
                  "Pythagoras</strong>. Beweegt een voorwerp bij het neerkomen "
                  "<strong>12 m/s horizontaal en 16 m/s verticaal</strong>, dan is zijn totale "
                  "snelheid <strong>20 m/s</strong>."),
            ("p", "De snelheidsvector staat <strong>halverwege de vlucht schuin naar beneden, "
                  "raaklijnig aan de baan</strong>. Het voorwerp "
                  "<strong>raakt de grond dus niet loodrecht</strong>: er blijft altijd een "
                  "horizontale snelheid over."),
        ]),
        dict(kop="Rekenen aan een worp", blokken=[
            ("p", "Een bal wordt <strong>horizontaal weggeschoten van 20 m hoog</strong>, met g "
                  "gelijk aan 10 m/s². De val duurt <strong>2 s</strong>. Vertrok de bal met "
                  "<strong>15 m/s</strong>, dan komt hij <strong>30 m</strong> ver, en hij valt op "
                  "het ogenblik dat hij de grond raakt met <strong>20 m/s</strong> verticaal."),
            ("p", "Een <strong>kogel verlaat een tafel van 1,25 m hoog met 4 m/s</strong>: de "
                  "valtijd is 0,5 s, dus komt hij <strong>2 m</strong> van de tafel neer. Een "
                  "<strong>bal rolt van een tafel van 0,8 m hoog</strong> en raakt de grond na "
                  "<strong>0,4 s</strong>."),
            ("p", "Een <strong>bal wordt horizontaal met 10 m/s weggeschoten</strong> en heeft na "
                  "<strong>20 m horizontaal</strong> 2 s gevlogen, dus verliest hij "
                  "<strong>20 m</strong> hoogte. Het <strong>hoogteverlies is niet recht evenredig "
                  "met de horizontale afstand zelf</strong> maar met het kwadraat ervan."),
            ("p", "Omgekeerd rekenen: een <strong>voetbal wordt van een klif van 45 m horizontaal "
                  "weggetrapt en komt 60 m verder neer</strong>. De valtijd is 3 s, dus werd hij met "
                  "<strong>20 m/s</strong> getrapt."),
        ]),
        dict(kop="Twee situaties om te doorzien", blokken=[
            ("p", "Een <strong>vliegtuig laat een pakket vallen</strong>. Het pakket komt "
                  "<strong>recht onder het vliegtuig terecht, als dat zijn koers aanhoudt</strong>, "
                  "want het houdt de horizontale snelheid van het vliegtuig."),
            ("p", "Je <strong>mikt bij het werpen over een grote afstand hoger dan het "
                  "doel</strong> omdat <strong>het voorwerp onderweg hoogte verliest door de "
                  "val</strong>. Dat hoogteverlies hangt af van hoe lang het onderweg is."),
        ]),
    ],
    onthoud=[
        "Horizontaal is eenparig, verticaal is een vrije val; de tijd verbindt ze.",
        "De baan is een parabool.",
        "De valtijd hangt enkel van de hoogte af, niet van de beginsnelheid.",
        "Twee ballen van dezelfde hoogte komen samen neer, hoe snel ze ook vertrekken.",
        "De dracht is snelheid maal valtijd: dubbel zo snel is dubbel zo ver.",
        "Vier keer hoger is maar twee keer verder.",
        "Reken altijd eerst de valtijd uit.",
    ],
)

# ───────────────────── 12. De gravitatiekracht en de cirkelbeweging
BUNDELS["de-gravitatiekracht-en-de-cirkelbeweging-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gravitatiekracht en de cirkelbeweging",
    onder="Rondjes draaien, en waarom een satelliet niet naar beneden valt.",
    secties=[
        dict(kop="De eenparig cirkelvormige beweging", blokken=[
            ("p", "Een lichaam voert een <strong>eenparig cirkelvormige beweging</strong> uit "
                  "<strong>als het een cirkel beschrijft met een constante baansnelheid</strong>. "
                  "Bij een <strong>ECB blijft de grootte van de baansnelheid constant</strong>, "
                  "terwijl <strong>de richting van de baansnelheid voortdurend verandert</strong>."),
            ("p", "De <strong>periode</strong> is <strong>de tijd die een lichaam nodig heeft voor "
                  "één volledige omwenteling</strong>; de <strong>frequentie</strong> is haar "
                  "omgekeerde en staat in <strong>hertz</strong>. Een "
                  "<strong>wiel dat 120 keer per minuut</strong> rondraait, heeft een frequentie van "
                  "<strong>2 Hz</strong>."),
            ("p", "De <strong>hoeksnelheid</strong> is <strong>de afgelegde hoek per seconde</strong>, "
                  "in radiaal per seconde. <strong>Twee kinderen op dezelfde draaimolen hebben "
                  "dezelfde hoeksnelheid, ook al zitten ze niet even ver van het midden</strong>; "
                  "hun baansnelheid verschilt wel. Draait een "
                  "<strong>draaimolen met 0,5 rad/s</strong>, dan beweegt een "
                  "<strong>kind op 4 m van het midden</strong> met <strong>2 m/s</strong>. Doet een "
                  "<strong>kind op 3 m van het midden 6 s over één ronde</strong>, dan is zijn "
                  "baansnelheid <strong>ongeveer 3,1 m/s</strong>."),
        ]),
        dict(kop="De middelpuntzoekende versnelling en kracht", blokken=[
            ("p", "Een lichaam in een ECB heeft toch een versnelling omdat "
                  "<strong>de richting van de snelheid voortdurend verandert</strong>. Die "
                  "versnelling wijst <strong>naar het middelpunt van de cirkel</strong> en heet de "
                  "<strong>centripetale versnelling</strong>. Bij een ECB "
                  "<strong>staan de snelheid en de versnelling loodrecht op elkaar</strong>."),
            ("p", "Drie dingen over de <strong>middelpuntzoekende versnelling</strong>: "
                  "<strong>ze wijst naar het midden van de cirkel</strong>, "
                  "<strong>ze is het kwadraat van de snelheid gedeeld door de straal</strong>, en "
                  "<strong>ze wordt vier keer zo groot als je twee keer zo snel rijdt</strong>. "
                  "Rijdt een <strong>auto met 10 m/s door een bocht met een straal van 20 m</strong>, "
                  "dan is de centripetale versnelling <strong>5 m/s²</strong>. De "
                  "<strong>middelpuntzoekende kracht op een auto van 1000 kg die met 5 m/s² naar "
                  "het midden versnelt</strong>, is dus <strong>5000 N</strong>."),
            ("p", "De <strong>middelpuntzoekende kracht is geen extra kracht naast de gewone "
                  "krachten</strong>: het is een rol die een bestaande kracht speelt. Die rol kan "
                  "gespeeld worden door <strong>de wrijving van de wielen van een auto in een "
                  "bocht</strong>, <strong>de spanning in een touw waaraan je een steen "
                  "rondslingert</strong> of <strong>de gravitatiekracht op een satelliet rond de "
                  "aarde</strong>. Wat een <strong>auto in een bocht houdt</strong>, is dus "
                  "<strong>de wrijvingskracht tussen de banden en het wegdek</strong>."),
            ("p", "Omdat die kracht loodrecht op de snelheid staat, "
                  "<strong>verricht de middelpuntzoekende kracht geen arbeid</strong> op een lichaam "
                  "in een ECB. En <strong>breekt het touw</strong> van een rondgeslingerde steen, "
                  "dan <strong>vliegt de steen raaklijnig verder, niet naar buiten</strong>."),
        ]),
        dict(kop="De universele gravitatiewet", blokken=[
            ("p", "De <strong>universele gravitatiewet</strong> zegt dat "
                  "<strong>elke twee massa's elkaar aantrekken, met r² in de noemer</strong>. De "
                  "kracht is <strong>recht evenredig met het product van de twee massa's</strong>, "
                  "<strong>omgekeerd evenredig met het kwadraat van de afstand</strong>, en ze "
                  "<strong>werkt tussen alle massa's, hoe klein ook</strong>. De constante G heet de "
                  "<strong>gravitatieconstante</strong>."),
            ("p", "De gravitatiewet <strong>lijkt op de wet van Coulomb</strong>: "
                  "<strong>beide hebben het kwadraat van de afstand in de noemer</strong> en "
                  "<strong>beide hebben het product van twee grootheden in de teller</strong>. "
                  "<strong>Verdrievoudig je de afstand</strong> tussen twee massa's, dan "
                  "<strong>wordt de kracht negen keer zo klein</strong>."),
            ("p", "Je <strong>voelt geen aantrekking tussen twee gewone voorwerpen in een "
                  "kamer</strong> omdat G zo klein is dat de kracht onmeetbaar blijft. En het "
                  "<strong>gravitatieveld van de aarde houdt nergens op</strong>: het wordt alleen "
                  "steeds zwakker."),
            ("p", "Het gravitatieveld rond een planeet ziet eruit als "
                  "<strong>radiaal, met de lijnen naar de planeet toe</strong>. "
                  "<strong>Vlak boven het aardoppervlak mag je het zwaarteveld als homogeen "
                  "beschouwen</strong>, want over een paar meter verandert er zo goed als niets."),
        ]),
        dict(kop="Zwaartekracht en valversnelling", blokken=[
            ("p", "Het verband tussen zwaartekracht en gravitatiekracht: "
                  "<strong>de zwaartekracht is de gravitatiekracht van de aarde op een "
                  "lichaam</strong>. De <strong>valversnelling aan het oppervlak van een "
                  "planeet</strong> wordt bepaald door <strong>de massa van de planeet</strong> en "
                  "<strong>de straal van de planeet</strong>."),
            ("p", "Daarom is <strong>g op de maan ongeveer zes keer kleiner dan op aarde</strong>: "
                  "<strong>de maan heeft veel minder massa, ondanks haar kleinere straal</strong>. "
                  "Hebben <strong>twee planeten dezelfde massa en heeft de ene een twee keer zo "
                  "grote straal</strong>, dan is g aan haar oppervlak "
                  "<strong>vier keer kleiner</strong>."),
            ("p", "Je <strong>massa verandert niet als je naar de maan gaat</strong>: je gewicht "
                  "wel, want dat is een kracht en hangt van g af."),
        ]),
        dict(kop="Satellieten", blokken=[
            ("p", "De kracht die een <strong>satelliet in zijn baan rond de aarde houdt</strong>, is "
                  "<strong>de gravitatiekracht van de aarde</strong>; zij "
                  "<strong>speelt de rol van middelpuntzoekende kracht</strong>. Je "
                  "<strong>berekent de baansnelheid</strong> dus door "
                  "<strong>de gravitatiekracht gelijk te stellen aan de middelpuntzoekende "
                  "kracht</strong>."),
            ("p", "Daarbij <strong>valt de massa van de satelliet uit de formule van de "
                  "baansnelheid weg</strong>: een <strong>zware en een lichte satelliet in dezelfde "
                  "baan hebben dezelfde snelheid</strong>. Voor een satelliet die "
                  "<strong>verder van de aarde draait</strong>, geldt: hij "
                  "<strong>beweegt trager en doet er langer over per omloop</strong>, dus hoort "
                  "<strong>verder weg bij een kleinere baansnelheid</strong>."),
            ("p", "Een satelliet die <strong>altijd boven hetzelfde punt van de aarde blijft "
                  "hangen</strong>, heet <strong>geostationair</strong>: zijn periode is precies "
                  "één dag."),
            ("p", "<strong>Astronauten zweven in een ruimtestation</strong> omdat "
                  "<strong>ze samen met het station voortdurend rond de aarde vallen</strong>, niet "
                  "omdat er geen gravitatie meer zou zijn: die houdt hen juist in hun baan."),
        ]),
    ],
    onthoud=[
        "ECB: grootte van de snelheid constant, richting niet.",
        "Periode en frequentie zijn elkaars omgekeerde.",
        "Centripetale versnelling is v²/r en wijst naar het midden.",
        "Middelpuntzoekend is een rol, geen extra kracht.",
        "Breekt het touw, dan vliegt de steen raaklijnig weg.",
        "Gravitatie: ∝ product van de massa's, ∝ 1/r².",
        "g aan een oppervlak hangt af van de massa en de straal van de planeet.",
        "Bij een satelliet is de gravitatiekracht de middelpuntzoekende kracht.",
    ],
)

# ───────────────────── 13. Arbeid, energie en vermogen
BUNDELS["arbeid-energie-en-vermogen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Arbeid, energie en vermogen",
    onder="Wanneer een kracht arbeid verricht, en waar de energie naartoe gaat.",
    secties=[
        dict(kop="Arbeid", blokken=[
            ("p", "Een kracht verricht <strong>arbeid</strong> "
                  "<strong>als het aangrijpingspunt verplaatst wordt in de zin van de "
                  "kracht</strong>. Arbeid staat in <strong>joule</strong>. Verplaatst een kracht "
                  "van <strong>40 N</strong> een kist <strong>3 m</strong> in dezelfde zin, dan is "
                  "de arbeid <strong>120 J</strong>."),
            ("p", "Een kracht verricht <strong>geen arbeid</strong> "
                  "<strong>als er geen verplaatsing is</strong>, "
                  "<strong>als de kracht loodrecht op de verplaatsing staat</strong> of "
                  "<strong>als de kracht zelf nul is</strong>. Daarom "
                  "<strong>verricht een kelner die een blad met glazen horizontaal draagt geen "
                  "arbeid op dat blad</strong>, en verricht ook "
                  "<strong>de normaalkracht op een lichaam dat over een vlakke vloer schuift geen "
                  "arbeid</strong>. Om dezelfde reden verricht "
                  "<strong>de middelpuntzoekende kracht op een satelliet in een cirkelbaan</strong> "
                  "<strong>nul arbeid, want ze staat loodrecht op de beweging</strong>."),
            ("p", "<strong>Arbeid kan negatief zijn.</strong> Ze is "
                  "<strong>negatief als de kracht tegen de verplaatsing in werkt</strong>, en "
                  "daarom is <strong>de arbeid van de wrijvingskracht altijd negatief</strong>. "
                  "Schuift een <strong>kist 4 m over een vloer met een wrijvingskracht van "
                  "25 N</strong>, dan verricht de wrijving <strong>−100 J</strong>."),
            ("p", "Staat de kracht schuin, dan telt alleen de component langs de verplaatsing mee. "
                  "Een kracht van <strong>20 N onder een hoek van 60 graden</strong> levert over "
                  "<strong>5 m</strong> <strong>50 J</strong>, want de cosinus van 60 graden is een "
                  "half."),
            ("p", "Twee hefoefeningen. Til je een <strong>doos van 10 kg 1,5 m hoog</strong>, dan "
                  "lever je <strong>150 J</strong>, met g gelijk aan 10 N/kg. Loop je met een "
                  "<strong>tas van 5 kg een trap van 3 m</strong> op, dan is dat ook "
                  "<strong>150 J</strong>."),
            ("p", "De <strong>oppervlakte onder een F(x)-grafiek</strong> is "
                  "<strong>de verrichte arbeid</strong>; die oppervlakte heet dus gewoon "
                  "<strong>arbeid</strong>. Bij een "
                  "<strong>niet-constante kracht reken je met een integraal</strong>, want dan kan "
                  "je niet gewoon kracht maal weg nemen. Niet constant zijn onder meer "
                  "<strong>de veerkracht</strong> en "
                  "<strong>de gravitatiekracht op grote afstandsverschillen</strong>."),
        ]),
        dict(kop="Conservatieve krachten", blokken=[
            ("p", "Een <strong>conservatieve kracht</strong> is "
                  "<strong>een kracht waarvan de arbeid niet van de gevolgde weg afhangt</strong>. "
                  "<strong>De zwaartekracht</strong> en <strong>de veerkracht</strong> zijn "
                  "conservatief, net als de gravitatiekracht en de coulombkracht."),
            ("p", "Een kracht waarvan de arbeid <strong>wél van de gevolgde weg afhangt</strong>, "
                  "heet <strong>niet-conservatief</strong>. Wrijving is daarvan het voorbeeld: hoe "
                  "langer de weg, hoe meer energie er als warmte verdwijnt."),
        ]),
        dict(kop="Kinetische en potentiële energie", blokken=[
            ("p", "De <strong>kinetische energie</strong> bereken je als "
                  "<strong>een half maal de massa maal het kwadraat van de snelheid</strong>, dus "
                  "<strong>de helft van de massa maal het kwadraat van de snelheid</strong>. Daarom "
                  "betekent <strong>twee keer zo snel vier keer zoveel kinetische energie</strong>. "
                  "Een <strong>auto van 1000 kg die 20 m/s rijdt</strong>, heeft "
                  "<strong>200 000 J</strong>."),
            ("p", "De <strong>gravitationele potentiële energie vlak bij het aardoppervlak</strong> "
                  "reken je als <strong>m·g·h</strong>: "
                  "<strong>de massa maal g maal de hoogte</strong>. Een "
                  "<strong>steen van 2 kg op 15 m hoogte</strong> heeft "
                  "<strong>300 J</strong>, en hij raakt de grond met "
                  "<strong>ongeveer 17 m/s</strong> als je de luchtweerstand verwaarloost."),
            ("p", "De <strong>potentiële energie van een veer is niet recht evenredig met haar "
                  "uitrekking zelf</strong> maar met het kwadraat ervan: twee keer zo ver uitrekken "
                  "kost vier keer zoveel energie."),
        ]),
        dict(kop="Behoud van energie", blokken=[
            ("p", "Het <strong>arbeid-energietheorema</strong> zegt dat "
                  "<strong>de totale arbeid op een lichaam gelijk is aan zijn verandering van "
                  "kinetische energie</strong>."),
            ("p", "<strong>In een gesloten systeem zonder wrijving blijft de som van de kinetische "
                  "en de potentiële energie gelijk.</strong> Bij een "
                  "<strong>slingerende schommel</strong> wisselen "
                  "<strong>kinetische energie</strong> en "
                  "<strong>gravitationele potentiële energie</strong> elkaar daarom voortdurend af."),
            ("p", "Glijdt een <strong>slee van 20 kg zonder wrijving van een heuvel van 5 m "
                  "hoog</strong>, dan is hij beneden <strong>10 m/s</strong> snel, met g gelijk aan "
                  "10 N/kg. <strong>Bij die berekening speelt de massa van de slee geen rol</strong>, "
                  "want ze valt aan beide kanten van de gelijkheid weg."),
            ("p", "Met wrijving erbij geldt het behoud nog altijd, maar met een extra post: glijdt "
                  "een <strong>kist met wrijving een helling af</strong>, dan "
                  "<strong>wordt de potentiële energie kinetische energie plus warmte</strong>. "
                  "Valt een <strong>bal van 2 m hoog en stuitert hij tot 1,4 m</strong>, dan is de "
                  "rest van de energie <strong>bij de botsing als warmte en geluid "
                  "vrijgekomen</strong>."),
        ]),
        dict(kop="Vermogen", blokken=[
            ("p", "<strong>Vermogen</strong> is <strong>de arbeid die per seconde verricht "
                  "wordt</strong>, dus <strong>de arbeid gedeeld door de tijd</strong>. Het staat in "
                  "<strong>watt</strong>, en <strong>één watt is één joule per seconde</strong>. Een "
                  "<strong>lift die 60 000 J arbeid in 20 s</strong> levert, heeft een vermogen van "
                  "<strong>3000 W</strong>."),
            ("p", "<strong>Wie een doos sneller even hoog tilt, levert daardoor niet meer "
                  "arbeid</strong>: de arbeid is dezelfde, alleen het vermogen is groter."),
            ("p", "Op een elektriciteitsfactuur staat de energie in kilowattuur: "
                  "<strong>één kilowattuur is 3 600 000 J</strong>, want 1000 watt gedurende 3600 "
                  "seconden."),
        ]),
    ],
    onthoud=[
        "Arbeid is kracht maal verplaatsing in de zin van de kracht, in joule.",
        "Loodrecht op de beweging betekent geen arbeid.",
        "Wrijving levert altijd negatieve arbeid.",
        "De oppervlakte onder F(x) is de arbeid; niet-constant vraagt een integraal.",
        "Conservatief: de arbeid hangt niet van de weg af.",
        "Kinetische energie is ½mv², potentiële m·g·h.",
        "Zonder wrijving blijft de som van kinetische en potentiële energie gelijk.",
        "Vermogen is arbeid per seconde, in watt; 1 kWh is 3,6 miljoen joule.",
    ],
)

# ───────────────────── 14. De gaswetten en de algemene gaswet
BUNDELS["de-gaswetten-en-de-algemene-gaswet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gaswetten en de algemene gaswet",
    onder="Druk, volume en temperatuur van een gas, en altijd rekenen in kelvin.",
    secties=[
        dict(kop="Vier toestandsgrootheden", blokken=[
            ("p", "De <strong>toestandsgrootheden van een gas</strong> zijn "
                  "<strong>druk, volume, temperatuur en stofhoeveelheid</strong>. Ken je er drie, "
                  "dan volgt de vierde eruit."),
            ("p", "De temperatuur moet je in de gaswetten altijd in "
                  "<strong>kelvin</strong> invullen. Je "
                  "<strong>mag de temperatuur dus niet in graden celsius invullen, ook niet als je "
                  "overal dezelfde eenheid gebruikt</strong>, want de wetten gelden voor de "
                  "absolute temperatuur. <strong>27 graden celsius</strong> is "
                  "<strong>300 K</strong>: je telt er 273 bij."),
        ]),
        dict(kop="De drie afzonderlijke gaswetten", blokken=[
            ("p", "Bij <strong>constante temperatuur</strong> geldt: "
                  "<strong>het product van druk en volume blijft gelijk</strong>. Zo'n proces heet "
                  "<strong>isotherm</strong>: <strong>de temperatuur verandert tijdens het proces "
                  "niet</strong>, en <strong>druk en volume zijn omgekeerd evenredig</strong>. Wordt "
                  "een gas van <strong>6 L bij 100 kPa</strong> bij dezelfde temperatuur "
                  "samengeperst tot <strong>2 L</strong>, dan is de druk <strong>300 kPa</strong>."),
            ("p", "Bij <strong>constante druk</strong> geldt: "
                  "<strong>het volume is recht evenredig met de absolute temperatuur</strong>. Zo'n "
                  "proces heet <strong>isobaar</strong>. Een gas van "
                  "<strong>2 L bij 300 K</strong> dat bij gelijke druk tot <strong>600 K</strong> "
                  "verwarmd wordt, heeft <strong>4 L</strong>. Een "
                  "<strong>ballon van 3 L bij 20 °C</strong> die in een koelkast op "
                  "<strong>5 °C</strong> gelegd wordt, krimpt tot "
                  "<strong>ongeveer 2,85 L</strong>: zet eerst om naar 293 en 278 kelvin."),
            ("p", "Bij <strong>constant volume</strong> geldt: "
                  "<strong>bij constant volume stijgt de druk van een gas als je het "
                  "verwarmt</strong>. Zo'n proces heet <strong>isochoor</strong>, dus "
                  "<strong>verloopt een isochoor proces niet bij constante druk</strong> maar bij "
                  "constant volume. Een <strong>gesloten vat op 2 bar bij 250 K</strong> komt bij "
                  "<strong>500 K</strong> op <strong>4 bar</strong>."),
            ("p", "De drie namen samen: <strong>isobaar, bij constante druk</strong>, "
                  "<strong>isochoor, bij constant volume</strong>, en isotherm, bij constante "
                  "temperatuur."),
        ]),
        dict(kop="De grafieken", blokken=[
            ("p", "Een <strong>p(V)-grafiek van een isotherm proces</strong> is "
                  "<strong>een kromme die daalt zoals een omgekeerde evenredigheid</strong>, dus "
                  "<strong>een hyperbool</strong>. Een "
                  "<strong>V(T)-grafiek bij constante druk</strong>, met T in kelvin, is "
                  "<strong>een rechte die door de oorsprong gaat</strong>, en "
                  "<strong>bij constant volume is de p(T)-grafiek een rechte door de "
                  "oorsprong</strong>. In graden celsius snijden die rechten de as pas bij min 273."),
            ("p", "Een <strong>p(T)-grafiek van een isotherm proces</strong> is iets anders: dat is "
                  "<strong>één verticale lijn, want de temperatuur verandert niet</strong> terwijl "
                  "de druk wel verandert."),
        ]),
        dict(kop="De algemene en de ideale gaswet", blokken=[
            ("p", "De <strong>algemene gaswet</strong> voor een vaste hoeveelheid gas zegt dat "
                  "<strong>p maal V gedeeld door T constant blijft</strong>. De drie afzonderlijke "
                  "wetten zijn daar bijzondere gevallen van. Gaat een gas van "
                  "<strong>2 L bij 300 K en 100 kPa naar 400 K en 200 kPa</strong>, dan krijgt het "
                  "<strong>ongeveer 1,33 L</strong>."),
            ("p", "De <strong>ideale gaswet</strong> luidt: "
                  "<strong>p maal V is n maal R maal T</strong>. Hier is n de stofhoeveelheid en R "
                  "de <strong>gasconstante</strong>, ongeveer 8,31 joule per mol per kelvin; die "
                  "<strong>constante R is voor elk gas dezelfde</strong>. De grootheid die je "
                  "<strong>naast druk, volume en temperatuur moet kennen</strong>, is dus "
                  "<strong>de stofhoeveelheid</strong>, en die <strong>staat erin in mol</strong>. "
                  "De wet <strong>geldt ook voor een mengsel van gassen zoals lucht</strong>: je "
                  "telt dan alle deeltjes samen als n."),
            ("p", "Vul de grootheden in SI-eenheden in: <strong>de druk in pascal</strong>, "
                  "<strong>het volume in kubieke meter</strong> en "
                  "<strong>de temperatuur in kelvin</strong>. In een vat van "
                  "<strong>0,025 m³ bij 300 K en 100 kPa</strong> zit zo "
                  "<strong>ongeveer 1 mol</strong> gas."),
            ("p", "Twee deeltjes van dezelfde wet. "
                  "<strong>Twee verschillende gassen bij dezelfde druk en temperatuur bevatten in "
                  "hetzelfde volume evenveel deeltjes.</strong> En "
                  "<strong>pomp je bij gelijk volume en gelijke temperatuur meer gas in een vat, dan "
                  "blijft de druk niet gelijk</strong>: ze stijgt, want n en p zijn recht evenredig."),
            ("p", "Bij <strong>normomstandigheden</strong>, "
                  "<strong>nul graden celsius en een druk van 101,3 kPa</strong>, neemt één mol van "
                  "een ideaal gas <strong>ongeveer 22,4 L</strong> in."),
        ]),
        dict(kop="Ideaal en reëel", blokken=[
            ("p", "Een <strong>ideaal gas</strong> is een gas waarvan "
                  "<strong>de deeltjes zelf geen eigen volume hebben</strong> en "
                  "<strong>geen kracht op elkaar uitoefenen</strong>. De botsingen zijn volkomen "
                  "elastisch. Zo'n gas bestaat niet echt, maar bij lage druk en hoge temperatuur "
                  "komen echte gassen er dicht bij: een "
                  "<strong>reëel gas wijkt niet het meest af bij hoge temperatuur en lage "
                  "druk</strong> maar juist bij lage temperatuur en hoge druk, dicht bij het "
                  "condenseren."),
            ("p", "Het deeltjesmodel verklaart ook waar de grootheden vandaan komen. De "
                  "<strong>druk van een gas op de wand</strong> komt "
                  "<strong>van de botsingen van de deeltjes tegen die wand</strong>. De "
                  "<strong>temperatuur van een gas</strong> zegt "
                  "<strong>hoe groot de gemiddelde kinetische energie van de deeltjes is</strong>. "
                  "Het <strong>absolute nulpunt</strong> ligt bij "
                  "<strong>−273</strong> graden celsius, preciezer bij min 273,15."),
        ]),
        dict(kop="Drie situaties uit het dagelijks leven", blokken=[
            ("p", "De druk in een <strong>fietsband stijgt als je lang gepompt hebt</strong> omdat "
                  "<strong>de lucht samengeperst en ook warmer geworden is</strong>."),
            ("p", "Op een <strong>spuitbus</strong> staat dat je hem "
                  "<strong>niet boven 50 °C mag bewaren</strong> omdat "
                  "<strong>bij constant volume de druk mee stijgt met de temperatuur</strong>."),
            ("p", "Een <strong>duiker die op 20 m diepte lucht inademt bij ongeveer 3 bar</strong>, "
                  "mag bij het opstijgen <strong>de adem niet inhouden</strong>, want "
                  "<strong>de lucht in zijn longen zet bij de dalende druk sterk uit</strong>: van 3 "
                  "naar 1 bar is een drie keer zo groot volume."),
        ]),
    ],
    onthoud=[
        "Toestandsgrootheden: druk, volume, temperatuur en stofhoeveelheid.",
        "Reken altijd in kelvin: celsius plus 273.",
        "Isotherm: p·V constant. Isobaar: V/T constant. Isochoor: p/T constant.",
        "Algemene gaswet: p·V/T blijft constant.",
        "Ideale gaswet: p·V = n·R·T, met pascal, m³, kelvin en mol.",
        "Eén mol neemt bij normomstandigheden ongeveer 22,4 liter in.",
        "Druk komt van botsingen, temperatuur is gemiddelde kinetische energie.",
    ],
)

# ───────────────────── 15. Warmteleer: temperatuur, warmte en faseovergangen
BUNDELS["warmteleer-temperatuur-warmte-en-faseovergangen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Warmteleer: temperatuur, warmte en faseovergangen",
    onder="Opwarmen, warmte uitwisselen en van fase veranderen zonder dat de thermometer beweegt.",
    secties=[
        dict(kop="Warmte is niet hetzelfde als temperatuur", blokken=[
            ("p", "Het verschil tussen warmte en temperatuur: "
                  "<strong>warmte is energie die stroomt, temperatuur is een toestand</strong>. "
                  "Warmte staat daarom in <strong>joule</strong>, temperatuur in kelvin. Een "
                  "<strong>voorwerp van 1000 K bevat niet altijd meer warmte dan een voorwerp van "
                  "300 K</strong>: een vonk bevat veel minder energie dan een bad, want de massa en "
                  "de stof tellen even hard mee."),
            ("p", "<strong>Warmte stroomt van het warme naar het koude voorwerp</strong>, nooit "
                  "spontaan de andere kant op. Daarom "
                  "<strong>houden twee voorwerpen die elkaar raken niet elk hun eigen "
                  "temperatuur</strong>: er stroomt warmte tot ze gelijk staan. Die toestand "
                  "<strong>waarin twee voorwerpen geen warmte meer uitwisselen</strong>, heet "
                  "<strong>thermisch evenwicht</strong>."),
            ("p", "Een <strong>stijging van 10 K is hetzelfde als een stijging van 10 graden "
                  "celsius</strong>: de twee schalen hebben even grote stappen, enkel hun nulpunt "
                  "verschilt. Bij een verschil mag je dus wel in celsius rekenen."),
            ("p", "Warmte verplaatst zich op drie manieren: "
                  "<strong>geleiding, door contact tussen de deeltjes</strong>, "
                  "<strong>stroming, doordat warm water of lucht stijgt</strong>, en "
                  "<strong>straling, doordat een warm voorwerp licht uitzendt</strong>. Daarom zit er "
                  "<strong>tussen de twee glazen van een thermosfles een vacuüm</strong>: "
                  "<strong>zonder deeltjes kan er geen warmte geleid of gestroomd worden</strong>, "
                  "en de spiegelende wand houdt de straling tegen."),
        ]),
        dict(kop="Meten met een calorimeter", blokken=[
            ("p", "Een <strong>calorimeter</strong> gebruik je "
                  "<strong>om een hoeveelheid uitgewisselde warmte te meten</strong>. Bij een "
                  "calorimeterproef geldt: <strong>de warmte die de ene stof afgeeft, neemt de "
                  "andere op</strong>, en <strong>het vat moet zo goed mogelijk geïsoleerd "
                  "zijn</strong>. De twee stoffen hoeven niet dezelfde massa te hebben."),
            ("p", "Met een <strong>joulevat</strong> meet je "
                  "<strong>hoeveel warmte een elektrische weerstand aan water geeft</strong>. Je "
                  "meet spanning, stroom en tijd, en de temperatuurstijging van het water laat zien "
                  "dat die energie warmte geworden is."),
        ]),
        dict(kop="Warmtecapaciteit", blokken=[
            ("p", "De <strong>warmtecapaciteit van een voorwerp</strong> is "
                  "<strong>de warmte die het nodig heeft om één kelvin op te warmen</strong>, met "
                  "het symbool grote C in joule per kelvin. De "
                  "<strong>specifieke warmtecapaciteit van een stof</strong> is "
                  "<strong>de warmte voor één kilogram en één kelvin</strong>, met het symbool "
                  "kleine c; ze <strong>hangt af van de stof en niet van de massa</strong>, en "
                  "<strong>water heeft een hoge waarde in vergelijking met metalen</strong>."),
            ("p", "Eén kilogram water heeft <strong>4186</strong> joule nodig om één kelvin op te "
                  "warmen. Daarom warmt <strong>een pan sneller op dan het water erin</strong>: "
                  "<strong>het metaal heeft een veel lagere specifieke warmtecapaciteit</strong>."),
            ("p", "De formule is <strong>Q is c maal m maal ΔT</strong>; ken je de warmtecapaciteit "
                  "van het hele voorwerp, dan volstaat Q is C maal ΔT. "
                  "<strong>2 kg water 10 K</strong> opwarmen vraagt "
                  "<strong>ongeveer 83,7 kJ</strong>. Giet je "
                  "<strong>1 kg water van 80 °C bij 1 kg water van 20 °C</strong>, dan krijg je "
                  "<strong>ongeveer 50 °C</strong>: bij gelijke massa's ligt het antwoord precies in "
                  "het midden."),
        ]),
        dict(kop="De zes faseovergangen", blokken=[
            ("p", "De zes faseovergangen komen in drie paren: "
                  "<strong>smelten en stollen</strong>, "
                  "<strong>verdampen en condenseren</strong> en "
                  "<strong>sublimeren en rijpen</strong>. "
                  "<strong>Smelten</strong> is de overgang van vast naar vloeibaar, "
                  "<strong>condenseren</strong> die van gas naar vloeistof, "
                  "<strong>sublimeren</strong> die van vast rechtstreeks naar gas, en "
                  "<strong>rijpen</strong> die van gas rechtstreeks naar vast."),
            ("p", "<strong>Smelten</strong>, <strong>verdampen</strong> en "
                  "<strong>sublimeren</strong> nemen warmte op, want ze gaan naar een lossere "
                  "toestand. Stollen, condenseren en rijpen geven warmte af: "
                  "<strong>bij stollen geeft een stof warmte af aan haar omgeving</strong>."),
            ("p", "<strong>Tijdens het smelten blijft de temperatuur van een zuivere stof "
                  "gelijk</strong>, want alle warmte gaat naar het losmaken van de deeltjes. Op een "
                  "<strong>smeltcurve</strong> zie je daarom "
                  "<strong>een stijging, dan een horizontaal stuk, dan weer een stijging</strong>, en "
                  "op een <strong>stolcurve</strong> "
                  "<strong>een daling, dan een horizontaal stuk, dan weer een daling</strong>. Een "
                  "<strong>mengsel heeft niet één scherp smeltpunt</strong> zoals een zuivere stof: "
                  "het smelt over een temperatuurgebied, dus is dat stuk niet vlak."),
        ]),
        dict(kop="Rekenen aan een faseovergang", blokken=[
            ("p", "De <strong>specifieke smeltwarmte van een stof</strong> is "
                  "<strong>de warmte om één kilogram ervan te laten smelten</strong>, met het "
                  "symbool kleine l in joule per kilogram. De formule voor een faseovergang is "
                  "<strong>Q is l maal m</strong>: er staat geen ΔT in, want de temperatuur "
                  "verandert niet."),
            ("p", "<strong>0,5 kg ijs van 0 °C</strong> laten smelten vraagt "
                  "<strong>ongeveer 167 kJ</strong>, met l gelijk aan 334 kJ/kg."),
            ("p", "De <strong>specifieke verdampingswarmte van water is niet kleiner dan zijn "
                  "specifieke smeltwarmte</strong> maar juist veel groter: ongeveer 2256 tegenover "
                  "334 kilojoule per kilogram. Wil je <strong>1 kg water van 20 °C eerst opwarmen "
                  "tot 100 °C en dan laten verdampen</strong>, dan kost "
                  "<strong>het verdampen de meeste warmte, want dat vraagt ongeveer "
                  "2256 kJ</strong> tegenover ongeveer 335 kJ voor het opwarmen."),
            ("p", "Daarom <strong>voelt het koel aan als er water op je huid verdampt</strong>: "
                  "<strong>het verdampende water neemt warmte van je huid mee</strong>. Dat is net "
                  "waarom zweten werkt."),
        ]),
        dict(kop="Kookpunt en smeltpunt verschuiven", blokken=[
            ("p", "Het <strong>kookpunt hangt af van de druk boven de vloeistof</strong>: "
                  "<strong>bij lagere druk ligt het kookpunt lager</strong>, en het "
                  "<strong>is altijd hoger dan het smeltpunt van de stof</strong>. Honderd graden is "
                  "het kookpunt van water bij normale druk, niet van elke vloeistof."),
            ("p", "Daarom gaat <strong>koken in een snelkookpan sneller</strong>: "
                  "<strong>de hogere druk duwt het kookpunt van water naar boven</strong>, en heter "
                  "water gaart het eten vlugger. Hoog in de bergen kookt water juist bij een lagere "
                  "temperatuur."),
            ("p", "<strong>Men strooit zout op een besneeuwde weg</strong> omdat "
                  "<strong>het zout het smeltpunt van het ijs verlaagt</strong>: pekel bevriest pas "
                  "onder nul graden. Bij strenge vorst werkt dat niet meer."),
        ]),
    ],
    onthoud=[
        "Warmte is energie die stroomt; temperatuur is een toestand.",
        "Warmte gaat altijd van warm naar koud tot thermisch evenwicht.",
        "Geleiding, stroming en straling zijn de drie wegen.",
        "Q = c · m · ΔT voor opwarmen; water heeft c ongeveer 4186.",
        "Zes faseovergangen; smelten, verdampen en sublimeren nemen warmte op.",
        "Tijdens een faseovergang blijft de temperatuur gelijk: Q = l · m.",
        "Verdampingswarmte van water is veel groter dan zijn smeltwarmte.",
        "Lagere druk verlaagt het kookpunt; zout verlaagt het smeltpunt.",
    ],
)

# ───────────────────── 16. Harmonische trillingen
BUNDELS["harmonische-trillingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Harmonische trillingen",
    onder="Eén vergelijking voor de hele beweging, van amplitude tot resonantie.",
    secties=[
        dict(kop="Wat een harmonische trilling is", blokken=[
            ("p", "Een <strong>harmonische trilling</strong> is "
                  "<strong>een beweging waarvan de uitwijking een sinus van de tijd is</strong>. Een "
                  "massa aan een veer en een slinger met een kleine uitslag zijn de twee "
                  "schoolvoorbeelden."),
            ("p", "De <strong>amplitude</strong> is <strong>de grootste uitwijking van een "
                  "trilling</strong>; ze <strong>staat in meter</strong> en "
                  "<strong>kan geen negatieve waarde hebben</strong>. De uitwijking zelf wel: die "
                  "krijgt aan de ene kant van de evenwichtslijn een minteken. De "
                  "<strong>evenwichtslijn</strong> is <strong>de stand waar het lichaam zonder "
                  "trilling zou blijven</strong>."),
            ("p", "De <strong>periode</strong> is <strong>de tijd van één volledige "
                  "heen-en-terugbeweging</strong>, in seconde. De frequentie is haar omgekeerde: "
                  "een trilling met een <strong>periode van 0,25 s</strong> heeft "
                  "<strong>4 Hz</strong>. Een <strong>trilling met een hogere frequentie heeft een "
                  "kleinere periode</strong>."),
        ]),
        dict(kop="De trillingsvergelijking", blokken=[
            ("p", "De <strong>trillingsvergelijking</strong> luidt: "
                  "<strong>y is A maal de sinus van ω maal t plus φ</strong>. Daaruit lees je "
                  "rechtstreeks <strong>de amplitude van de trilling</strong>, "
                  "<strong>de pulsatie van de trilling</strong> en "
                  "<strong>de beginfase van de trilling</strong>; de massa staat er niet in. Om er "
                  "zelf een op te stellen heb je <strong>de amplitude</strong>, "
                  "<strong>de periode of de frequentie</strong> en "
                  "<strong>de beginfase</strong> nodig."),
            ("p", "De <strong>pulsatie</strong> is <strong>twee pi gedeeld door de "
                  "periode</strong>; ze <strong>is dus twee pi maal de frequentie</strong> en "
                  "<strong>staat in radiaal per seconde</strong>. Ze heet ook de hoeksnelheid. De "
                  "<strong>beginfase staat in radiaal</strong>, want de fase is een hoek in de "
                  "sinus."),
            ("p", "Een <strong>beginfase van nul</strong> betekent dat "
                  "<strong>de trilling op t is nul uit de evenwichtsstand vertrekt</strong>, want de "
                  "sinus van nul is nul. Vertrekt ze uit de uiterste stand, dan is de beginfase een "
                  "halve pi. Een trilling met een <strong>amplitude van 5 cm en een pulsatie van "
                  "4 rad/s</strong> en beginfase nul heeft na een halve periode een uitwijking van "
                  "<strong>nul, want de sinus is dan weer nul</strong>."),
        ]),
        dict(kop="Snelheid en versnelling tijdens de trilling", blokken=[
            ("p", "Twee dingen die altijd gelden: <strong>de uitwijking is nul in de "
                  "evenwichtsstand</strong> en <strong>de snelheid is nul in de uiterste "
                  "stand</strong>. Bij een harmonische trilling is "
                  "<strong>de snelheid dus niet het grootst in de uiterste stand</strong> maar in "
                  "de evenwichtsstand."),
            ("p", "De <strong>versnelling van een harmonisch trillend lichaam is het grootst in de "
                  "uiterste standen, waar de uitwijking maximaal is</strong>, want daar is de "
                  "terugroepkracht het grootst. In de evenwichtsstand is de versnelling nul."),
            ("p", "De amplitude doet niets met de periode: "
                  "<strong>verdubbel je de amplitude van een slinger met een kleine uitslag</strong>, "
                  "dan <strong>blijft de periode ongeveer gelijk</strong>. Dat is net waarom een "
                  "slingeruurwerk zo nauwkeurig was."),
        ]),
        dict(kop="Faseverschil", blokken=[
            ("p", "Het <strong>faseverschil tussen twee harmonische trillingen</strong> is "
                  "<strong>het verschil tussen hun fasen op hetzelfde tijdstip</strong>, in "
                  "radiaal. Twee trillingen trillen <strong>in fase</strong> "
                  "<strong>als hun faseverschil nul of een veelvoud van twee pi is</strong>; bij een "
                  "faseverschil van <strong>pi radiaal</strong> zijn ze "
                  "<strong>in tegenfase</strong>."),
            ("p", "Hebben twee trillingen <strong>dezelfde frequentie en een faseverschil van een "
                  "halve pi</strong>, dan is <strong>de ene een kwart periode voor op de "
                  "andere</strong>: staat de ene in de evenwichtsstand, dan staat de andere uiterst."),
        ]),
        dict(kop="De veer en de slinger", blokken=[
            ("p", "De <strong>terugroepkracht bij een massa-veersysteem</strong> is "
                  "<strong>de kracht van de veer, naar de evenwichtsstand gericht</strong>. Ze is "
                  "recht evenredig met de uitwijking en altijd tegengesteld eraan, en net daardoor "
                  "is de beweging harmonisch. De constante k van een veer heet de "
                  "<strong>krachtconstante</strong>, in newton per meter."),
            ("p", "De <strong>eigenfrequentie van een massa-veersysteem</strong> bereken je als "
                  "<strong>één gedeeld door twee pi, maal de wortel van k gedeeld door m</strong>. "
                  "Daarom geeft <strong>een stijvere veer een hogere eigenfrequentie</strong> en "
                  "<strong>een grotere massa een lagere eigenfrequentie</strong>. Hang je een "
                  "<strong>dubbel zo zware massa</strong> aan dezelfde veer, dan "
                  "<strong>wordt ze kleiner, met een factor wortel twee</strong>."),
            ("p", "De <strong>eigenfrequentie van een slinger</strong> hangt af "
                  "<strong>van zijn lengte en van de valversnelling</strong>, en niet van de massa "
                  "van de bol. <strong>Een langere slinger trilt langzamer dan een korte</strong>, "
                  "want de lengte staat onder de wortel in de noemer."),
        ]),
        dict(kop="Demping en resonantie", blokken=[
            ("p", "Bij een <strong>gedempte harmonische trilling neemt niet vooral de frequentie "
                  "af</strong> maar de amplitude: de uitwijking verloopt "
                  "<strong>als een sinus die tussen twee krimpende grenzen past</strong>. "
                  "<strong>Bij een gedempte trilling verdwijnt de energie van de trilling naar de "
                  "omgeving</strong>, als warmte door wrijving."),
            ("p", "Een <strong>gedwongen trilling</strong> is "
                  "<strong>een trilling die een uitwendige kracht blijft aandrijven</strong>. Het "
                  "lichaam neemt dan de frequentie van die kracht over, terwijl de "
                  "<strong>eigenfrequentie</strong> de frequentie is "
                  "<strong>waarmee een lichaam vrij trilt</strong>."),
            ("p", "<strong>Resonantie</strong> treedt op "
                  "<strong>als de frequentie van de kracht de eigenfrequentie benadert</strong>. "
                  "Dan kan de amplitude heel groot worden met een kleine kracht: "
                  "<strong>bij resonantie is de amplitude dus niet kleiner dan normaal</strong> maar "
                  "juist veel groter."),
            ("p", "Voorbeelden van resonantie: <strong>een schommel die je op het juiste ritme "
                  "steeds hoger duwt</strong>, <strong>een glas dat breekt bij een zuivere toon van "
                  "de juiste hoogte</strong> en <strong>een brug die door marcherende stappen hevig "
                  "begint te trillen</strong>. Daarom <strong>zet men dempers in een gebouw dat "
                  "tegen aardbevingen moet kunnen</strong>: "
                  "<strong>om de amplitude bij resonantie klein te houden</strong>."),
        ]),
    ],
    onthoud=[
        "Harmonisch: de uitwijking is een sinus van de tijd.",
        "y = A · sin(ω·t + φ); daaruit lees je A, ω en φ.",
        "Pulsatie is 2π/T, dus 2π maal de frequentie, in rad/s.",
        "Snelheid maximaal in het evenwicht, versnelling maximaal uiterst.",
        "De periode hangt niet van de amplitude af.",
        "Veer: stijver trilt sneller, zwaarder trilt langzamer.",
        "Slinger: alleen lengte en g tellen, niet de massa.",
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
                  "<strong>trillen rond hun eigen evenwichtsstand</strong> en blijven dus ter "
                  "plaatse; enkel de trilling schuift door. Hoe je de "
                  "<strong>richting waarin de deeltjes heen en weer gaan</strong> noemt: de "
                  "<strong>trilrichting</strong>."),
            ("p", "Het verschil tussen een mechanische en een elektromagnetische golf: "
                  "<strong>een mechanische golf heeft een stof nodig om door te gaan</strong>. "
                  "Elektromagnetisch zijn onder andere "
                  "<strong>zichtbaar licht</strong>, <strong>radiogolven</strong> en "
                  "<strong>röntgenstraling</strong>; die lopen ook door vacuüm."),
            ("p", "Een <strong>transversale</strong> golf is er een waarbij "
                  "<strong>de deeltjes dwars op de voortplantingsrichting trillen</strong>. Trillen "
                  "ze langs de voortplantingsrichting, dan is de golf "
                  "<strong>longitudinaal</strong>: "
                  "<strong>geluid in de lucht is een longitudinale golf</strong>, want de lucht "
                  "verdicht en verdunt in de looprichting."),
        ]),
        dict(kop="Golflengte, frequentie en snelheid", blokken=[
            ("p", "De <strong>golflengte</strong> van een lopende golf is "
                  "<strong>de afstand tussen twee punten die in fase trillen</strong>, bijvoorbeeld "
                  "van berg tot berg. De snelheid bereken je als "
                  "<strong>de golflengte maal de frequentie</strong>: een golf met een "
                  "<strong>golflengte van 2 m en een frequentie van 50 Hz</strong> loopt "
                  "<strong>100 m/s</strong>."),
            ("p", "De snelheid van een golf hangt af "
                  "<strong>van de stof waar de golf door loopt</strong>, niet van hoe hard je de "
                  "bron aanslaat: <strong>een golf met een grotere amplitude loopt niet "
                  "sneller</strong>. <strong>Alle deeltjes op een lopende golf trillen met dezelfde "
                  "frequentie</strong>, want ze krijgen allemaal het ritme van de bron."),
            ("p", "Het <strong>golfgetal</strong> is <strong>twee pi gedeeld door de "
                  "golflengte</strong>, de ruimtelijke tegenhanger van de pulsatie. De "
                  "<strong>golfvergelijking van een rechtslopende golf</strong> luidt "
                  "<strong>y is A maal de sinus van ω maal t min k maal x</strong>. Daaruit lees je "
                  "<strong>de amplitude van de golf</strong>, "
                  "<strong>de pulsatie en dus de periode</strong> en "
                  "<strong>het golfgetal en dus de golflengte</strong>."),
        ]),
        dict(kop="Wie wanneer begint te trillen", blokken=[
            ("p", "<strong>Niet alle deeltjes van een lopende golf beginnen op hetzelfde ogenblik "
                  "te trillen</strong>: de trilling moet er eerst toe komen. Trilt een bron al "
                  "<strong>3 s</strong>, ligt een deeltje <strong>10 m</strong> verder en loopt de "
                  "golf <strong>5 m/s</strong>, dan was de golf 2 s onderweg en trilt dat deeltje "
                  "nog maar <strong>1 s</strong>."),
            ("p", "Loopt een golf <strong>naar rechts</strong>, dan beweegt een deeltje dat net "
                  "voor een berg ligt <strong>naar boven, want de berg schuift naar hem toe</strong>. "
                  "Wie de vorm een klein stukje naar rechts schuift, ziet het meteen."),
        ]),
        dict(kop="Huygens: weerkaatsen, breken, buigen", blokken=[
            ("p", "Het <strong>principe van Huygens</strong> zegt dat "
                  "<strong>elk punt van een golffront zelf als een nieuwe bron werkt</strong>. "
                  "Daarmee verklaar je <strong>de weerkaatsing van een golf op een wand</strong>, "
                  "<strong>de breking van een golf bij een andere stof</strong> en "
                  "<strong>de buiging van een golf achter een opening</strong>. Die drie heten "
                  "samen <strong>weerkaatsing of reflectie</strong>, "
                  "<strong>breking of refractie</strong> en "
                  "<strong>buiging of diffractie</strong>; het terugkaatsen op een wand heet dus "
                  "ook <strong>reflectie</strong>, en het afbuigen achter een smalle opening "
                  "<strong>buiging</strong>."),
            ("p", "Bij breking verandert <strong>de snelheid van de golf</strong>, "
                  "<strong>de golflengte van de golf</strong> en "
                  "<strong>de richting van de golf</strong>, maar "
                  "<strong>bij breking verandert de frequentie van de golf niet</strong>: die blijft "
                  "van de bron. De <strong>wet van Snellius</strong> luidt: "
                  "<strong>de sinus van i gedeeld door de sinus van r is n_r gedeeld door "
                  "n_i</strong>. <strong>Bij de overgang naar een stof met een hogere brekingsindex "
                  "buigt de straal naar de normaal toe</strong>."),
            ("p", "Een <strong>brekingsindex van 1,5 betekent niet dat licht in die stof 1,5 keer "
                  "sneller gaat dan in vacuüm</strong> maar juist 1,5 keer langzamer: de index is "
                  "de lichtsnelheid in vacuüm gedeeld door die in de stof. Daarom "
                  "<strong>lijkt een rietje in een glas water geknikt</strong>: "
                  "<strong>het licht breekt bij de overgang van water naar lucht</strong>."),
            ("p", "Buiging lukt beter bij een grote golflengte. Daarom "
                  "<strong>hoor je een laag gebrom van een feest verder dan de hoge tonen</strong>: "
                  "<strong>lage tonen hebben een grotere golflengte en buigen beter af</strong> rond "
                  "huizen en hoeken."),
        ]),
        dict(kop="Interferentie en staande golven", blokken=[
            ("p", "<strong>Interferentie</strong> is "
                  "<strong>twee golven die samen één nieuwe uitwijking geven</strong>. "
                  "<strong>Constructieve</strong> interferentie treedt op "
                  "<strong>als de twee golven er in fase aankomen</strong>; "
                  "<strong>bij destructieve interferentie kunnen twee golven elkaar volledig "
                  "uitdoven</strong>. Twee bronnen zijn <strong>coherent</strong> als "
                  "<strong>ze dezelfde frequentie en een vast faseverschil hebben</strong>."),
            ("p", "Een <strong>staande golf</strong> ontstaat "
                  "<strong>door interferentie van een golf met haar eigen weerkaatsing</strong>. Een "
                  "punt dat helemaal niet trilt is een <strong>knoop</strong>: "
                  "<strong>een knoop trilt helemaal niet</strong> en "
                  "<strong>een buik trilt met de grootste amplitude</strong>. In fase met elkaar "
                  "trillen <strong>de punten tussen twee opeenvolgende knopen</strong>; over een "
                  "knoop heen slaat de uitwijking om."),
        ]),
    ],
    onthoud=[
        "Een golf vervoert energie, geen materie.",
        "Mechanisch heeft een stof nodig; elektromagnetisch niet.",
        "Transversaal trilt dwars, longitudinaal langs de looprichting.",
        "v = λ · f; de stof bepaalt v, de bron bepaalt f.",
        "y = A · sin(ω·t − k·x), met k = 2π/λ.",
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
            ("p", "Een <strong>elektromagnetische golf</strong> is "
                  "<strong>een transversale golf die in vacuüm met de lichtsnelheid loopt</strong>. "
                  "Die lichtsnelheid is <strong>300000000</strong> meter per seconde, en "
                  "<strong>licht gaat in water langzamer dan in vacuüm</strong>."),
            ("p", "Het verschil tussen regelmatige en diffuse weerkaatsing: "
                  "<strong>bij een ruw oppervlak kaatsen de stralen alle kanten op</strong>. Daarom "
                  "zie je in een blad papier geen beeld en in een spiegel wel."),
            ("p", "Het beeld in een vlakke spiegel <strong>is virtueel</strong>, "
                  "<strong>staat rechtop</strong> en "
                  "<strong>is even groot als het voorwerp</strong>. Een "
                  "<strong>virtueel beeld</strong> is "
                  "<strong>een beeld dat je niet op een scherm kan opvangen</strong>: de stralen "
                  "komen er niet echt samen, ze lijken er enkel vandaan te komen."),
            ("p", "Een <strong>kernschaduw</strong> ontstaat doordat "
                  "<strong>daar geen licht van de bron meer toe komt</strong>. "
                  "<strong>Bij een maansverduistering staat de maan niet tussen de zon en de "
                  "aarde</strong> maar de aarde tussen de zon en de maan; staat de maan ertussen, "
                  "dan is het een zonsverduistering."),
            ("p", "Het <strong>brandpunt van een bolle lens</strong> is "
                  "<strong>het punt waar stralen langs de optische as samenkomen</strong>. Staat een "
                  "<strong>voorwerp verder dan tweemaal de brandpuntsafstand</strong>, dan krijg je "
                  "<strong>een reëel, omgekeerd en kleiner beeld</strong>, zoals in een fototoestel."),
        ]),
        dict(kop="Het spectrum van radiogolf tot gamma", blokken=[
            ("p", "Van lage naar hoge frequentie liggen de soorten straling zo: "
                  "<strong>radiogolven, microgolven, infrarood, licht, uv, röntgen, "
                  "gamma</strong>. Het verband met het pakketje energie: "
                  "<strong>de energie stijgt met de frequentie en daalt met de golflengte</strong>. "
                  "Dat kleinste pakketje energie van licht heet een <strong>foton</strong>."),
            ("p", "<strong>Ioniserend</strong> zijn <strong>röntgenstraling</strong>, "
                  "<strong>gammastraling</strong> en "
                  "<strong>hoogenergetische uv-straling</strong>: die fotonen dragen genoeg energie "
                  "om een elektron uit een molecule te slaan. "
                  "<strong>Microgolven worden in een magnetron niet gebruikt omdat ze ioniserend "
                  "zijn</strong> maar omdat ze watermoleculen doen trillen, wat warmte geeft."),
            ("p", "<strong>Radiogolven</strong> gebruikt men voor communicatie over grote afstand "
                  "omdat <strong>ze een groot doordringend vermogen hebben en goed afbuigen</strong>. "
                  "Een <strong>bagagescanner op de luchthaven</strong> werkt met "
                  "<strong>röntgenstraling</strong>, die door een koffer gaat en door metaal niet."),
            ("p", "Beschermen tegen hoogenergetische straling doe je met "
                  "<strong>zonnecrème en een zonnebril tegen uv-straling</strong>, "
                  "<strong>een loden schort bij een röntgenfoto</strong> en door "
                  "<strong>zo weinig en zo kort mogelijk blootgesteld te worden</strong>."),
            ("p", "De <strong>proef van Young</strong> laat zien "
                  "<strong>dat licht zich als een golf gedraagt</strong>: achter twee spleten "
                  "ontstaat een patroon van lichte en donkere strepen. "
                  "<strong>Voor interferentie van licht heb je twee coherente bronnen nodig</strong>, "
                  "en daar zorgt die dubbele spleet voor."),
        ]),
        dict(kop="Geluid: snelheid, toonhoogte en klankkleur", blokken=[
            ("p", "Geluid loopt het snelst <strong>in staal</strong>: hoe steviger de deeltjes aan "
                  "elkaar hangen, hoe vlugger de verdichting doorgeeft. "
                  "<strong>Geluid loopt in warme lucht sneller dan in koude lucht</strong>, want de "
                  "moleculen bewegen er heftiger. Zie je een bliksem en hoor je de donder "
                  "<strong>6 s</strong> later, dan is het onweer "
                  "<strong>ongeveer 2 km</strong> ver, met 340 m/s."),
            ("p", "Het verband met wat je hoort: "
                  "<strong>een hogere frequentie geeft een hogere toon</strong>. Het verschil tussen "
                  "een viool en een fluit op dezelfde toon hoor je "
                  "<strong>aan de klankkleur, dus aan de vorm van het patroon</strong>; die "
                  "klankkleur heet ook <strong>timbre</strong>."),
            ("p", "Een mens hoort normaal <strong>van ongeveer 20 Hz tot ongeveer 20 000 Hz</strong>. "
                  "<strong>Ultrasoon</strong> geluid is <strong>geluid met een frequentie boven de "
                  "20 000 Hz</strong>, gebruikt bij "
                  "<strong>een echografie bij de dokter</strong>, door "
                  "<strong>een vleermuis die zijn weg zoekt</strong> en in "
                  "<strong>een sonar die de diepte van de zee meet</strong>."),
        ]),
        dict(kop="Decibel en gehoorschade", blokken=[
            ("p", "De gehoordrempel van een mens ligt <strong>bij 0 dB</strong>. Van de gevaargrens "
                  "voor het gehoor spreekt men vanaf <strong>80</strong> decibel. "
                  "<strong>Gehoorschade hangt zowel van het geluidsniveau als van de duur van de "
                  "blootstelling af</strong>: zacht en lang kan even schadelijk zijn als hard en "
                  "kort."),
            ("p", "De decibelschaal is logaritmisch: "
                  "<strong>een geluid van 60 dB is niet twee keer zo intens als een geluid van "
                  "30 dB</strong> maar duizend keer. Ga je "
                  "<strong>twee keer zo dicht bij een geluidsbron staan</strong>, dan wordt de "
                  "intensiteit <strong>vier keer zo groot</strong>, want ze daalt met het kwadraat "
                  "van de afstand."),
            ("p", "Blijvende gehoorschade in het binnenoor ontstaat doordat "
                  "<strong>de trilhaartjes van de haarcellen afbreken en niet terug groeien</strong>. "
                  "Voorkomen doe je door <strong>oordopjes te dragen die het geluid gelijkmatig "
                  "dempen</strong>, <strong>verder van de luidspreker te gaan staan</strong> en "
                  "<strong>tussendoor een pauze te nemen op een stillere plek</strong>."),
        ]),
        dict(kop="Snaren en het dopplereffect", blokken=[
            ("p", "De <strong>grondfrequentie van een snaar</strong> is "
                  "<strong>de laagste frequentie waarop ze als staande golf kan trillen</strong>. De "
                  "harmonischen zijn er de veelvouden van: bij een grondfrequentie van "
                  "<strong>220 Hz</strong> heeft de derde harmonische "
                  "<strong>660 Hz</strong>."),
            ("p", "Het <strong>dopplereffect</strong> bij geluid is dat "
                  "<strong>de waargenomen frequentie verschilt als bron en waarnemer "
                  "bewegen</strong>: een ziekenwagen klinkt hoger als hij nadert. "
                  "<strong>Bij het dopplereffect verandert de frequentie die de bron zelf uitzendt "
                  "niet</strong>; enkel de golven komen dichter op elkaar of verder uit elkaar bij "
                  "de waarnemer."),
        ]),
    ],
    onthoud=[
        "Licht is een transversale EM-golf, in vacuüm 3 · 10⁸ m/s.",
        "Een spiegelbeeld is virtueel, rechtop en even groot.",
        "Radio, micro, infrarood, licht, uv, röntgen, gamma.",
        "Ioniserend: röntgen, gamma en harde uv.",
        "Young laat zien dat licht een golf is.",
        "Geluid: hoger in frequentie is hoger van toon; timbre is de klankkleur.",
        "20 Hz tot 20 000 Hz; boven 80 dB wordt het gevaarlijk.",
        "Doppler verandert wat je hoort, niet wat de bron uitzendt.",
    ],
)

# ───────────────────── 19. Kwantumfysica: het foto-elektrisch effect en dualiteit
BUNDELS["kwantumfysica-het-foto-elektrisch-effect-en-dualiteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kwantumfysica: het foto-elektrisch effect en dualiteit",
    onder="Twee proeven die licht een deeltje maakten en materie een golf.",
    secties=[
        dict(kop="Het foto-elektrisch effect", blokken=[
            ("p", "Bij het <strong>foto-elektrisch effect</strong> "
                  "<strong>slaat licht elektronen uit een metaaloppervlak los</strong>. Of er "
                  "elektronen loskomen, hangt af "
                  "<strong>van de frequentie van het licht</strong> en niet van hoe fel het schijnt. "
                  "De laagste frequentie waarbij er elektronen loskomen heet de "
                  "<strong>drempelfrequentie</strong>."),
            ("p", "Boven die drempel doet een grotere intensiteit dit: "
                  "<strong>er komen meer elektronen los, met dezelfde energie</strong>. Kort samen: "
                  "<strong>de frequentie beslist of er elektronen loskomen</strong> en "
                  "<strong>de intensiteit beslist hoeveel elektronen er loskomen</strong>. Heeft een "
                  "metaal een <strong>drempelfrequentie van 6 maal 10¹⁴ Hz</strong> en schijn je "
                  "licht van <strong>4 maal 10¹⁴ Hz</strong>, dan "
                  "<strong>komt er geen enkel elektron los</strong>, hoe fel je ook schijnt."),
            ("p", "Het <strong>klassieke golfmodel verklaart het foto-elektrisch effect niet</strong>, "
                  "want <strong>het voorspelt dat fel rood licht ook elektronen losmaakt</strong>: "
                  "genoeg energie, enkel wat langer wachten. Dat gebeurt niet. "
                  "<strong>Bij het foto-elektrisch effect neemt één elektron de energie van "
                  "meerdere fotonen niet samen op</strong>: elk elektron krijgt precies één foton, "
                  "en dat ene foton moet op zich genoeg energie hebben. Daarom "
                  "<strong>laat het foto-elektrisch effect zien dat licht ook een deeltjeskarakter "
                  "heeft</strong>."),
        ]),
        dict(kop="De energie van een foton", blokken=[
            ("p", "De energie van een foton bereken je als "
                  "<strong>de constante van Planck maal de frequentie</strong>; de constante in die "
                  "formule is die <strong>van Planck</strong>, met symbool h. Een foton van "
                  "<strong>5 maal 10¹⁴ Hz</strong> heeft met h gelijk aan 6,63 · 10⁻³⁴ J·s "
                  "<strong>ongeveer 3,3 · 10⁻¹⁹ J</strong>."),
            ("p", "Het verband met de golflengte: "
                  "<strong>een kleinere golflengte geeft een energierijker foton</strong>. Daarom "
                  "heeft <strong>blauw licht een energierijker foton dan rood licht</strong>. Om de "
                  "minimale fotonenergie voor een metaal te bepalen heb je "
                  "<strong>de drempelfrequentie van dat metaal</strong> en "
                  "<strong>de constante van Planck</strong> nodig."),
            ("p", "Wat er van de fotonenergie overblijft nadat het elektron los is: "
                  "<strong>het verschil wordt kinetische energie van het elektron</strong>. Een deel "
                  "gaat naar het losmaken zelf, de rest naar de snelheid."),
        ]),
        dict(kop="Waar je het effect tegenkomt", blokken=[
            ("p", "Met het foto-elektrisch effect werken "
                  "<strong>een zonnepaneel op een dak</strong>, "
                  "<strong>een fotocel in een bewegingsdetector</strong> en "
                  "<strong>een rookdetector die met licht werkt</strong>. Een "
                  "<strong>zonnecel</strong> werkt doordat "
                  "<strong>het licht ladingen losmaakt die een stroom vormen</strong>."),
            ("p", "<strong>Een fotocel in een bewegingsdetector zendt zelf geen licht uit om te "
                  "meten</strong>: ze meet enkel het licht dat erop valt. Een "
                  "<strong>rookdetector met licht</strong> gaat af omdat "
                  "<strong>de rook de bundel verstrooit en de fotocel minder licht krijgt</strong>."),
        ]),
        dict(kop="Materie als golf", blokken=[
            ("p", "Het <strong>experiment van Davisson en Germer</strong> liet zien "
                  "<strong>dat een bundel elektronen zich als een golf gedraagt</strong>. Ze "
                  "stuurden hun elektronenbundel op <strong>nikkel</strong> en kregen een "
                  "buigingspatroon: <strong>ook een elektron kan een buigingspatroon geven, net als "
                  "licht</strong>. Wat die proef en de proef van Young gemeen hebben: "
                  "<strong>ze laten allebei een golfkarakter zien</strong>."),
            ("p", "Met de <strong>dualiteit</strong> van licht en materie bedoelt men dat "
                  "<strong>ze zich soms als een golf en soms als een deeltje gedragen</strong>. Het "
                  "golfmodel verklaart het best <strong>interferentie bij de proef van "
                  "Young</strong>, <strong>buiging rond een smalle opening</strong> en "
                  "<strong>breking bij de overgang naar glas</strong>; het deeltjesmodel is nodig "
                  "voor <strong>het foto-elektrisch effect</strong> en "
                  "<strong>de drempelfrequentie van een metaal</strong>. "
                  "<strong>Licht is dus niet in werkelijkheid alleen een golf met het "
                  "deeltjesmodel als rekentruc</strong>: beide kanten zijn even echt, je ziet er "
                  "telkens één van."),
            ("p", "Waarom we de golfkant van een voetbal niet merken: "
                  "<strong>zijn golflengte is onvoorstelbaar klein door zijn grote massa</strong>. "
                  "Bij een elektron is die golflengte wel van de orde van een atoom, en daar zie je "
                  "het effect dus."),
        ]),
        dict(kop="Kansen in plaats van banen", blokken=[
            ("p", "De <strong>golffunctie</strong> van een deeltje beschrijft "
                  "<strong>de kans om het deeltje op een bepaalde plaats te vinden</strong>; je "
                  "bepaalt ze met de <strong>Schrödingervergelijking</strong>. Volgens de "
                  "Kopenhaagse interpretatie <strong>valt ze bij een meting samen tot één "
                  "uitkomst</strong>."),
            ("p", "<strong>Volgens de kwantumfysica is de plaats van een elektron in een atoom een "
                  "kansverdeling</strong>: <strong>sommige plaatsen zijn veel waarschijnlijker dan "
                  "andere</strong>. Het gebied waar een elektron zich met grote kans bevindt heet "
                  "een <strong>orbitaal</strong>. Een elektron "
                  "<strong>heeft een golfkarakter én een deeltjeskarakter</strong> en "
                  "<strong>zijn plaats in een atoom is een kansverdeling</strong>."),
            ("p", "Het <strong>onzekerheidsbeginsel van Heisenberg</strong> zegt dat "
                  "<strong>plaats en impuls niet samen scherp te kennen zijn</strong>. "
                  "<strong>Dat komt niet doordat onze meettoestellen nog niet nauwkeurig genoeg "
                  "zijn</strong>: het zit in de natuur zelf. Daarom "
                  "<strong>kan je van een elektron geen baan tekenen zoals van een planeet</strong>, "
                  "want <strong>plaats en snelheid zijn niet samen scherp te kennen</strong>."),
            ("p", "Vuur je in het <strong>tweespletenexperiment</strong> de elektronen "
                  "<strong>één per één</strong> af, dan "
                  "<strong>staat er na lang wachten toch een patroon van strepen</strong>. Elk "
                  "elektron komt als één stip aan, maar samen vormen ze het golfpatroon."),
        ]),
    ],
    onthoud=[
        "Foto-elektrisch effect: licht slaat elektronen uit een metaal.",
        "De frequentie beslist of, de intensiteit hoeveel.",
        "E = h · f; kleinere golflengte is energierijker.",
        "Davisson en Germer: elektronen buigen op nikkel, dus golf.",
        "Dualiteit: golf en deeltje zijn beide echt.",
        "De golffunctie geeft kansen; een orbitaal is zo'n kansgebied.",
        "Heisenberg: plaats en impuls nooit samen scherp.",
        "Eén per één door twee spleten geeft toch strepen.",
    ],
)

# ───────────────────── 20. De atoomkern, radioactief verval en halveringstijd
BUNDELS["de-atoomkern-radioactief-verval-en-halveringstijd-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De atoomkern, radioactief verval en halveringstijd",
    onder="Wat er in een kern zit, wanneer ze het niet volhoudt, en hoe snel ze verdwijnt.",
    secties=[
        dict(kop="Hoe je een kern benoemt", blokken=[
            ("p", "Het <strong>massagetal</strong> van een nuclide is "
                  "<strong>het aantal protonen en neutronen samen</strong>; het "
                  "<strong>atoomnummer</strong> zegt <strong>hoeveel protonen de kern "
                  "bevat</strong>. De deeltjes van een atoomkern heten samen "
                  "<strong>nucleonen</strong>. Je schrijft een nuclide van element X met massagetal "
                  "14 <strong>als X-14, met het massagetal achter de naam</strong>."),
            ("p", "Heeft een nuclide <strong>massagetal 23 en atoomnummer 11</strong>, dan heeft "
                  "hij <strong>12</strong> neutronen: 23 min 11. "
                  "<strong>Uranium-238, met atoomnummer 92</strong>, heeft "
                  "<strong>92 protonen en 146 neutronen</strong>. Zodra je massagetal en "
                  "atoomnummer kent, liggen "
                  "<strong>het aantal protonen in de kern</strong>, "
                  "<strong>het aantal neutronen in de kern</strong> en "
                  "<strong>om welk element het gaat</strong> vast. Kort: "
                  "<strong>het massagetal is de som van protonen en neutronen</strong> en "
                  "<strong>het atoomnummer is gelijk aan het aantal protonen</strong>."),
            ("p", "<strong>Isotopen</strong> van een element zijn "
                  "<strong>kernen met hetzelfde aantal protonen en een ander aantal "
                  "neutronen</strong>. <strong>Twee isotopen van hetzelfde element hebben hetzelfde "
                  "atoomnummer</strong>, en "
                  "<strong>een nuclide met een ander aantal neutronen is geen ander "
                  "element</strong>: enkel het aantal protonen bepaalt het element. "
                  "<strong>Koolstof-12 en koolstof-14</strong> verschillen dus "
                  "<strong>in hun aantal neutronen</strong>."),
        ]),
        dict(kop="Wat een kern stabiel houdt", blokken=[
            ("p", "De kracht die de nucleonen samenhoudt is "
                  "<strong>de sterke kernkracht</strong>. In een kern spelen twee krachten tegen "
                  "elkaar in: <strong>de sterke kernkracht, die alle nucleonen aantrekt</strong> en "
                  "<strong>de coulombkracht, die de protonen afstoot</strong>. De kernkracht werkt "
                  "enkel over heel korte afstand, de afstoting over de hele kern."),
            ("p", "<strong>Bij lichte kernen met Z kleiner dan 20 zijn het aantal protonen en "
                  "neutronen ongeveer gelijk</strong>. Zware kernen met Z groter dan 20 zijn pas "
                  "stabiel met meer neutronen dan protonen, want "
                  "<strong>de extra neutronen geven kernkracht zonder extra afstoting</strong>."),
            ("p", "De strook stabiele kernen op een nuclidenkaart heet de "
                  "<strong>stabiliteitsband</strong>. Uit de plaats van een kern op die kaart lees "
                  "je <strong>of hij stabiel is en welk verval hij anders zal doen</strong>: "
                  "<strong>een kern onder de stabiliteitsband heeft te veel neutronen en vervalt via "
                  "bèta-min-straling</strong>."),
            ("p", "Een <strong>radionuclide</strong> is "
                  "<strong>een kern die onstabiel is en spontaan vervalt</strong>. "
                  "<strong>Je kan dat verval niet versnellen door hem te verwarmen</strong>: "
                  "temperatuur, druk en chemie laten de kern onverschillig."),
        ]),
        dict(kop="De vier soorten verval", blokken=[
            ("p", "Bij <strong>alfaverval</strong> zendt een kern "
                  "<strong>een kern van helium, met twee protonen en twee neutronen</strong> uit. "
                  "Bij <strong>bèta-min-verval</strong> "
                  "<strong>wordt een neutron een proton en vertrekt er een elektron</strong>; bij "
                  "bèta-plus-verval vliegt er een <strong>positron</strong> weg. "
                  "<strong>Gammastraling</strong> is "
                  "<strong>een foton met heel veel energie uit de kern</strong>."),
            ("p", "De <strong>regels van Soddy</strong> in drie regels: "
                  "<strong>bij alfaverval daalt het massagetal met vier</strong>, "
                  "<strong>bij bèta-min-verval stijgt het atoomnummer met één</strong> en "
                  "<strong>bij gammaverval blijven A en Z dezelfde</strong>. Daarom "
                  "<strong>verandert de kern bij gammaverval niet in een ander element</strong>; ze "
                  "raakt enkel energie kwijt. Doet een kern met "
                  "<strong>massagetal 226 en atoomnummer 88</strong> alfaverval, dan krijg je "
                  "<strong>massagetal 222 en atoomnummer 86</strong>."),
        ]),
        dict(kop="Halveringstijd en activiteit", blokken=[
            ("p", "De <strong>halveringstijd</strong> is "
                  "<strong>de tijd waarin de helft van de kernen vervalt</strong>. "
                  "<strong>Na één halveringstijd is de helft van de kernen vervallen</strong>, "
                  "<strong>ze ligt voor elk radionuclide vast</strong> en "
                  "<strong>een kortere halveringstijd geeft bij dezelfde hoeveelheid een hogere "
                  "activiteit</strong>. <strong>Na twee halveringstijden is een radioactieve stof "
                  "niet volledig vervallen</strong> maar nog voor een kwart over. Bij een "
                  "halveringstijd van <strong>8 dagen</strong> is er na "
                  "<strong>24 dagen</strong> nog <strong>een achtste</strong> over, want dat zijn "
                  "drie halveringen."),
            ("p", "De <strong>activiteit</strong> van een radionuclide is "
                  "<strong>het aantal kernen dat per seconde vervalt</strong>. Ze "
                  "<strong>staat in becquerel</strong>, ze "
                  "<strong>is de desintegratieconstante maal het aantal kernen</strong> en ze "
                  "<strong>halveert na elke halveringstijd</strong>. "
                  "<strong>De activiteit van een bron daalt in de tijd op dezelfde manier als het "
                  "aantal kernen</strong>. Een bron van <strong>800 Bq</strong> met een "
                  "halveringstijd van <strong>5 jaar</strong> staat na "
                  "<strong>10 jaar</strong> op <strong>200 Bq</strong>."),
            ("p", "De <strong>desintegratieconstante</strong> bereken je als "
                  "<strong>0,693 gedeeld door de halveringstijd</strong>; 0,693 is de natuurlijke "
                  "logaritme van twee. Om het aantal kernen in een massa stof te berekenen heb je "
                  "<strong>de massa van de stof</strong>, "
                  "<strong>de molaire massa van de stof</strong> en "
                  "<strong>het getal van Avogadro</strong> nodig."),
            ("p", "De <strong>koolstof-14-methode</strong> om ouderdom te bepalen werkt omdat "
                  "<strong>het gehalte koolstof-14 na de dood met een vaste halveringstijd "
                  "daalt</strong>. Zolang een organisme leeft, vult het zijn voorraad aan; daarna "
                  "niet meer."),
        ]),
    ],
    onthoud=[
        "A is protonen plus neutronen, Z is het aantal protonen.",
        "Isotopen: zelfde Z, ander aantal neutronen.",
        "Sterke kernkracht trekt aan, coulombkracht stoot protonen af.",
        "De stabiliteitsband zegt of en hoe een kern vervalt.",
        "Alfa: A −4, Z −2. Bèta-min: Z +1. Gamma: niets verandert.",
        "Verval versnel je met niets: niet met warmte, niet met chemie.",
        "Halveringstijd: na n keer blijft (1/2)ⁿ over.",
        "Activiteit in becquerel, is λ · N, halveert mee.",
    ],
)

# ───────────────────── 21. Kernenergie, straling en haar effecten
BUNDELS["kernenergie-straling-en-haar-effecten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kernenergie, straling en haar effecten",
    onder="Van massadefect tot jodiumpil: waar de energie zit en wat de straling doet.",
    secties=[
        dict(kop="Massa is energie", blokken=[
            ("p", "De formule van Einstein zegt over een massa: "
                  "<strong>elke massa is een hoeveelheid energie, namelijk m maal c "
                  "kwadraat</strong>. In <strong>1 g</strong> massa zit met c gelijk aan "
                  "3 · 10⁸ m/s dus <strong>ongeveer 9 · 10¹³ J</strong>. En "
                  "<strong>bij een kernproces blijft de totale massa van de deeltjes niet precies "
                  "gelijk</strong>: een stukje massa wordt energie."),
            ("p", "Het <strong>massadefect</strong> van een kern is "
                  "<strong>het verschil tussen de massa van de losse nucleonen en de kern</strong>. "
                  "De energie die nodig is om een kern in losse nucleonen te splitsen heet de "
                  "<strong>bindingsenergie</strong>; de "
                  "<strong>specifieke bindingsenergie</strong> is "
                  "<strong>de bindingsenergie gedeeld door het aantal nucleonen</strong>. "
                  "<strong>Een kern met een grotere specifieke bindingsenergie is stabieler</strong>."),
        ]),
        dict(kop="Splijting en fusie", blokken=[
            ("p", "<strong>Kernsplijting</strong> is: "
                  "<strong>een zware kern valt in twee lichtere kernen uiteen</strong>. Zowel "
                  "<strong>fusie van twee lichte kernen</strong> als "
                  "<strong>splijting van een zware kern</strong> levert energie, want in beide "
                  "gevallen schuif je naar kernen met een grotere specifieke bindingsenergie. Bij "
                  "fusie van lichte kernen komt energie vrij omdat "
                  "<strong>de nieuwe kern een grotere specifieke bindingsenergie heeft</strong>."),
            ("p", "De energie van de zon komt van <strong>kernfusie van waterstof tot "
                  "helium</strong>. Een gewone kerncentrale gebruikt "
                  "<strong>uranium</strong> als splijtstof. Een centrale op kernfusie zou boven een "
                  "op kernsplijting <strong>veel minder langlevend afval en geen kettingreactie die "
                  "ontspoort</strong> hebben."),
            ("p", "De <strong>regelstaven</strong> in een kernreactor dienen hiervoor: "
                  "<strong>ze vangen neutronen weg en houden de kettingreactie in de hand</strong>. "
                  "Bij een kerncentrale op kernsplijting horen "
                  "<strong>een reactorvat met splijtstaven en regelstaven</strong>, "
                  "<strong>een stoomgenerator en een turbine</strong> en "
                  "<strong>een betonnen koepel rond de reactor</strong>. "
                  "<strong>Een kerncentrale op kernsplijting stoot bij het opwekken van stroom geen "
                  "CO₂ uit</strong>; het probleem zit in het afval."),
        ]),
        dict(kop="Radioactief afval", blokken=[
            ("p", "Radioactief afval wordt ingedeeld volgens twee kenmerken: "
                  "<strong>de intensiteit van de straling en hoe lang ze duurt</strong>. In "
                  "categorie A zit <strong>kortlevend laagactief en middelactief afval</strong>. "
                  "Laagactief afval komt onder meer "
                  "<strong>van beschermkledij en gereedschap uit een ziekenhuis of labo</strong>."),
            ("p", "<strong>Voor hoogactief afval van categorie C ligt in België nog geen "
                  "definitieve bergingsplaats vast</strong>: er is een onderzoekslabo in de kleilaag "
                  "onder Mol, maar de keuze is niet gemaakt."),
        ]),
        dict(kop="Alfa, bèta en gamma onderweg", blokken=[
            ("p", "<strong>Alfastraling</strong> heeft het grootste ioniserend vermogen, maar "
                  "<strong>alfastraling heeft van de drie soorten niet het grootste doordringend "
                  "vermogen</strong>: juist het kleinste. Die twee gaan omgekeerd samen, want wie "
                  "veel ioniseert, raakt zijn energie snel kwijt."),
            ("p", "Wat welke straling tegenhoudt: "
                  "<strong>een blad papier houdt alfastraling tegen</strong>, "
                  "<strong>een plaatje aluminium houdt bètastraling tegen</strong> en "
                  "<strong>een dikke laag lood of beton zwakt gammastraling af</strong>."),
            ("p", "Omdat alfa en bèta geladen zijn, "
                  "<strong>buigt alfastraling af in een elektrisch veld</strong>. In een magnetisch "
                  "veld geldt: <strong>alfa en bèta buigen naar tegengestelde kanten, gamma gaat "
                  "recht</strong>, want gammastraling heeft geen lading."),
        ]),
        dict(kop="Dosis en bescherming", blokken=[
            ("p", "Het verschil tussen bestraling en besmetting: "
                  "<strong>bij besmetting zit de radioactieve stof op of in je lichaam</strong>. Zit "
                  "ze in het lichaam, dan spreekt men van "
                  "<strong>inwendige besmetting</strong>."),
            ("p", "De <strong>geabsorbeerde dosis</strong> is "
                  "<strong>de energie van de straling per kilogram weefsel</strong>, in "
                  "<strong>gray</strong>. De <strong>equivalente dosis</strong> is "
                  "<strong>de geabsorbeerde dosis maal de stralingsweegfactor</strong>. "
                  "Alfastraling heeft een veel hogere stralingsweegfactor dan gammastraling omdat "
                  "<strong>ze haar energie in een heel klein gebied afgeeft</strong>. De "
                  "<strong>weefselweegfactor</strong> dient "
                  "<strong>om te verrekenen dat sommige organen gevoeliger zijn</strong>, en "
                  "<strong>de effectieve dosis houdt rekening met de soort straling en met het "
                  "bestraalde weefsel</strong>."),
            ("p", "Beschermen tegen ioniserende straling doe je door "
                  "<strong>verder van de bron te gaan staan</strong>, "
                  "<strong>zo kort mogelijk in de buurt van de bron te blijven</strong> en met "
                  "<strong>een afscherming van lood of beton tussen jou en de bron</strong>: "
                  "afstand, tijd en afscherming."),
            ("p", "Bij een kernongeval deelt men jodiumpillen uit omdat "
                  "<strong>de schildklier dan vol zit en geen radioactief jodium meer "
                  "opneemt</strong>."),
        ]),
        dict(kop="Wat straling met een cel doet, en waar ze helpt", blokken=[
            ("p", "Het effect van ioniserende straling op een cel: "
                  "<strong>ze kan het DNA beschadigen en de cel doen afsterven of muteren</strong>. "
                  "<strong>Natuurlijke straling</strong> is "
                  "<strong>straling van radon uit de bodem en van de kosmos</strong>; die is er "
                  "altijd, ook zonder centrale in de buurt."),
            ("p", "Toepassingen die ioniserende straling gebruiken: "
                  "<strong>het doorstralen van voedsel om het langer te bewaren</strong>, "
                  "<strong>radiotherapie tegen een tumor</strong> en "
                  "<strong>een PET-scan met een radioactieve tracer</strong>. "
                  "<strong>Doorstraald voedsel wordt zelf niet radioactief</strong>: de straling "
                  "doodt de micro-organismen en gaat er dan door."),
            ("p", "In een PET-scan gebruikt men een stof met een korte halveringstijd omdat "
                  "<strong>de straling in het lichaam dan snel weer weg is</strong>."),
        ]),
    ],
    onthoud=[
        "E = m · c²; bij een kernproces verdwijnt er massa.",
        "Massadefect geeft de bindingsenergie; per nucleon telt.",
        "Splijting van zwaar en fusie van licht leveren beide energie.",
        "Regelstaven vangen neutronen en houden de reactie in de hand.",
        "Categorie C, hoogactief, heeft in België nog geen bergingsplaats.",
        "Alfa ioniseert het sterkst, dringt het minst door.",
        "Gray voor de geabsorbeerde dosis, met weegfactoren naar de effectieve dosis.",
        "Afstand, tijd en afscherming beschermen je.",
    ],
)

# ───────────────────── 22. Veilig werken, meetinstrumenten en meetonzekerheid
BUNDELS["veilig-werken-meetinstrumenten-en-meetonzekerheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig werken, meetinstrumenten en meetonzekerheid",
    onder="Het juiste toestel, het juiste bereik en het juiste aantal cijfers.",
    secties=[
        dict(kop="Meetbereik en nauwkeurigheid", blokken=[
            ("p", "Het <strong>meetbereik</strong> van een meetinstrument is "
                  "<strong>de kleinste en de grootste waarde die het kan meten</strong>. Daarbuiten "
                  "mag je het niet gebruiken, want "
                  "<strong>de meting is dan onbetrouwbaar en het toestel kan beschadigen</strong>. "
                  "De <strong>nauwkeurigheid</strong> is "
                  "<strong>het kleinste verschil dat een meetinstrument nog kan "
                  "aanwijzen</strong>."),
            ("p", "Een meting is nooit helemaal exact, want "
                  "<strong>elk instrument heeft een beperkte nauwkeurigheid</strong>. Kies je "
                  "tussen een chronometer van 0,1 s en een van 0,01 s voor een val van ongeveer een "
                  "halve seconde, dan neem je "
                  "<strong>die van 0,01 s, want anders is de fout te groot</strong>. Toch is "
                  "<strong>een nauwkeuriger meetinstrument niet altijd de beste keuze, wat je ook "
                  "meet</strong>: voor de lengte van een lokaal volstaat een rolmeter, en een duur "
                  "toestel buiten zijn bereik meet slechter dan een eenvoudig toestel erin."),
            ("p", "Een analoge meter met een naald lees je af "
                  "<strong>recht van boven, zodat de naald niet verschoven lijkt</strong>. Bij een "
                  "snelle beweging gebruik je liever een sensor dan een handchronometer, want "
                  "<strong>je eigen reactietijd geeft bij de hand een fout van wel een tiende "
                  "seconde</strong>. En <strong>een toestel dat een onwaarschijnlijke waarde "
                  "aanwijst, mag je niet zonder meer overnemen</strong>: eerst nagaan of je goed "
                  "aangesloten en goed ingesteld hebt."),
        ]),
        dict(kop="Welk toestel voor welke grootheid", blokken=[
            ("p", "Een kracht meet je <strong>met een dynamometer</strong>, het geluidsniveau in een "
                  "ruimte met <strong>een decibelmeter</strong>. Samengevat: "
                  "<strong>een dynamometer voor een kracht</strong>, "
                  "<strong>een chronometer voor een tijdsduur</strong> en "
                  "<strong>een decibelmeter voor een geluidsniveau</strong>."),
            ("p", "Met een <strong>multimeter</strong> meet je "
                  "<strong>de spanning over een lamp</strong>, "
                  "<strong>de stroom door een draad</strong> en "
                  "<strong>de weerstand van een component</strong>, elk op zijn eigen stand en met "
                  "zijn eigen manier van aansluiten."),
        ]),
        dict(kop="Veilig en duurzaam in het labo", blokken=[
            ("p", "Veilig en duurzaam werken in een fysicalabo betekent "
                  "<strong>het meetbereik en de nauwkeurigheid van een toestel respecteren</strong>, "
                  "<strong>een meetinstrument uitschakelen als je er niet mee meet</strong> en "
                  "<strong>de handleiding van een toestel vooraf doorlezen</strong>. Dat laatste "
                  "doe je <strong>om het meetbereik, de aansluiting en de voorzorgen te "
                  "kennen</strong>, en <strong>een meetinstrument uitschakelen als je niet meet, "
                  "hoort bij duurzaam werken</strong>."),
            ("p", "Een spanningsbron zet je op de laagste stand voor je hem aansluit, want "
                  "<strong>zo kan je de spanning rustig opdrijven zonder iets te laten "
                  "doorbranden</strong>. En <strong>je mag elektrische toestellen niet met natte "
                  "handen bedienen</strong>, want water geleidt."),
            ("p", "Bij het werken met een radioactieve bron horen deze voorzorgen: "
                  "<strong>zo ver mogelijk van de bron blijven</strong>, "
                  "<strong>de bron zo kort mogelijk uit zijn houder halen</strong> en "
                  "<strong>een afscherming tussen jou en de bron zetten</strong>. De batterijen van "
                  "meetmateriaal dat je weggooit: "
                  "<strong>ze horen bij het klein gevaarlijk afval en gaan apart</strong>."),
        ]),
        dict(kop="Eenheden en voorvoegsels", blokken=[
            ("p", "De SI-eenheid van kracht is <strong>de newton</strong>. SI-eenheden zijn onder "
                  "andere <strong>de meter voor een lengte</strong>, "
                  "<strong>de kilogram voor een massa</strong> en "
                  "<strong>de seconde voor een tijd</strong>."),
            ("p", "Om van kilometer per uur naar meter per seconde te gaan vermenigvuldig je met "
                  "<strong>1/3,6</strong>. Verder: "
                  "<strong>2,5 mA</strong> is <strong>0,0025 A</strong>, "
                  "<strong>4,7 kΩ</strong> is <strong>4700 Ω</strong>, het voorvoegsel voor een "
                  "miljoenste is <strong>micro</strong> en "
                  "<strong>nano staat voor een miljardste van de eenheid</strong>."),
            ("p", "<strong>Een antwoord zonder eenheid is in de fysica niet even goed als een "
                  "antwoord met eenheid</strong>: zonder eenheid is een getal nietszeggend. Het "
                  "<strong>antwoord met de juiste eenheid noteren</strong> hoort dus bij het werk."),
        ]),
        dict(kop="Beduidende cijfers en notatie", blokken=[
            ("p", "De meting <strong>0,0250 m</strong> heeft <strong>drie</strong> beduidende "
                  "cijfers: de nullen vooraan tellen niet mee, de nul achteraan wel. Tel je "
                  "<strong>2,5 m en 1,25 m</strong> op, dan schrijf je het antwoord "
                  "<strong>met één cijfer na de komma, dus 3,8 m</strong>: de slechtste meting "
                  "bepaalt het resultaat."),
            ("p", "Je schrijft niet alle cijfers van je rekenmachine op, want "
                  "<strong>je antwoord zou dan nauwkeuriger lijken dan je meting is</strong>. In "
                  "wetenschappelijke notatie wordt <strong>0,00045</strong> "
                  "<strong>4,5 · 10⁻⁴</strong>; <strong>in de wetenschappelijke notatie staan er "
                  "niet altijd twee cijfers voor de komma</strong> maar precies één."),
            ("p", "Een schatting vooraf maak je "
                  "<strong>om een onzinnig antwoord meteen te herkennen</strong>."),
        ]),
        dict(kop="Van tabel naar grafiek naar formule", blokken=[
            ("p", "Bij het verwerken van meetgegevens horen "
                  "<strong>de gegevens in een tabel zetten</strong>, "
                  "<strong>een grafiek tekenen om het verband te zien</strong> en "
                  "<strong>het antwoord met de juiste eenheid noteren</strong>."),
            ("p", "Tussen twee grootheden kan je een <strong>recht evenredig</strong>, een "
                  "<strong>omgekeerd evenredig</strong> of een <strong>kwadratisch</strong> verband "
                  "tegenkomen. Zie je in een grafiek een rechte door de oorsprong, dan is dat "
                  "<strong>een recht evenredig verband</strong>; bij een omgekeerd evenredig "
                  "verband hoort <strong>een kromme die daalt en de assen nadert</strong>."),
            ("p", "Weet je dat F gelijk is aan m maal a, dan is "
                  "<strong>a gelijk aan F gedeeld door m</strong>. En "
                  "<strong>je mag twee formules combineren door een grootheid die in beide staat te "
                  "vervangen</strong>; zo kom je aan een verband dat je niet rechtstreeks gemeten "
                  "hebt."),
        ]),
    ],
    onthoud=[
        "Meetbereik: niet erbuiten meten. Nauwkeurigheid: de kleinste stap.",
        "Het beste toestel is dat wat bij de meting past.",
        "Dynamometer, chronometer, decibelmeter, multimeter.",
        "Laagste stand eerst, droge handen, handleiding vooraf.",
        "Radioactieve bron: ver, kort en achter een afscherming.",
        "Beduidende cijfers: de slechtste meting bepaalt het antwoord.",
        "Wetenschappelijke notatie: één cijfer voor de komma.",
        "Elk antwoord krijgt zijn eenheid.",
    ],
)

# ───────────────────── 23. Wetenschappelijk onderzoek, ontwerpen en STEM
BUNDELS["wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="Van een vraag naar een antwoord, en van een probleem naar een ontwerp.",
    secties=[
        dict(kop="Vraag, hypothese en plan", blokken=[
            ("p", "Een <strong>onderzoeksvraag</strong> is "
                  "<strong>de vraag die je met je onderzoek wil beantwoorden</strong>; een "
                  "<strong>hypothese</strong> is "
                  "<strong>een verwachting die je vooraf opstelt en kan nagaan</strong>. De stap "
                  "waarin je vastlegt hoe je je onderzoek zal uitvoeren is het "
                  "<strong>onderzoeksplan</strong>."),
            ("p", "De stappen van een wetenschappelijk onderzoek: "
                  "<strong>het probleem definiëren en afbakenen</strong>, "
                  "<strong>een onderzoeksvraag en een hypothese opstellen</strong> en "
                  "<strong>data verzamelen en analyseren</strong>."),
            ("p", "Een bruikbare onderzoeksvraag voor een proef is er een als "
                  "<strong>hoe hangt de periode van een slinger af van zijn lengte?</strong> "
                  "<strong>Een onderzoeksvraag moet niet zo breed mogelijk opgesteld zijn</strong> "
                  "maar juist scherp genoeg om te kunnen meten."),
            ("p", "Over een hypothese geldt: "
                  "<strong>ze wordt opgesteld voor je begint te meten</strong>, "
                  "<strong>ze moet met een proef na te gaan zijn</strong> en "
                  "<strong>ze kan door de resultaten weerlegd worden</strong>. Zo'n weerlegging is "
                  "geen mislukking: <strong>een meting die je hypothese tegenspreekt, is een geldig "
                  "resultaat</strong>."),
        ]),
        dict(kop="Meten en verwerken", blokken=[
            ("p", "In een proef verander je maar één grootheid tegelijk, want "
                  "<strong>anders weet je niet welke verandering het verschil veroorzaakte</strong>. "
                  "De grootheid die je bewust verandert heet "
                  "<strong>de onafhankelijke variabele</strong>. Meet je de valtijd van een bal "
                  "vanaf verschillende hoogtes, dan zet je op de horizontale as "
                  "<strong>de hoogte, want die kies je zelf</strong>."),
            ("p", "Je herhaalt een meting meerdere keren "
                  "<strong>om toevallige afwijkingen uit je resultaat te halen</strong>. Een "
                  "<strong>controleproef</strong> dient "
                  "<strong>om te vergelijken met een opstelling waarin je niets verandert</strong>. "
                  "Met een meting die sterk van de rest afwijkt doe je dit: "
                  "<strong>je zoekt de oorzaak en vermeldt wat je ermee doet</strong>, in plaats van "
                  "ze stil te laten verdwijnen."),
            ("p", "Een goede conclusie moet "
                  "<strong>de onderzoeksvraag beantwoorden op basis van de data</strong>; "
                  "<strong>een conclusie mag niet verder gaan dan wat je gemeten hebt</strong>. In "
                  "een goed verslag staat <strong>welke instrumenten je gebruikt hebt</strong>, "
                  "<strong>welke grootheden je constant gehouden hebt</strong> en "
                  "<strong>de meetwaarden met hun eenheid</strong>."),
            ("p", "Dat een onderzoek <strong>herhaalbaar</strong> moet zijn, betekent: "
                  "<strong>iemand anders moet met jouw plan hetzelfde kunnen vinden</strong>. Je "
                  "laat anderen je resultaten nalezen omdat "
                  "<strong>zij fouten en andere verklaringen zien die jij gemist hebt</strong>, en "
                  "<strong>reflecteren over je gekozen methode hoort bij het onderzoek zelf</strong>."),
        ]),
        dict(kop="Ontwerpen in stappen", blokken=[
            ("p", "De eerste stap bij het ontwerpen van een oplossing is "
                  "<strong>het probleem helder definiëren</strong>. "
                  "<strong>Criteria</strong> zijn "
                  "<strong>de eisen waaraan je oplossing moet voldoen</strong>, en de kleinere "
                  "stukken waarin je een groot probleem opsplitst zijn "
                  "<strong>deelproblemen</strong>. Het geheel waarin je de oplossingen van alle "
                  "deelproblemen samenbrengt is <strong>de totaaloplossing</strong>; "
                  "<strong>je mag een deelprobleem niet oplossen zonder na te gaan of het in de "
                  "totaaloplossing past</strong>."),
            ("p", "Bij een probleemoplossende strategie horen "
                  "<strong>het probleem definiëren</strong>, "
                  "<strong>criteria voor de oplossing opstellen</strong> en "
                  "<strong>het probleem in deelproblemen splitsen</strong>. Voldoet je ontwerp niet "
                  "aan een criterium, dan "
                  "<strong>stuur je het ontwerp bij en test opnieuw</strong>; en ook nadat je een "
                  "gegeven oplossing geëvalueerd hebt, "
                  "<strong>stuur je ze bij waar ze de criteria niet haalt</strong>. "
                  "<strong>Bij een ontwerp volstaat het soms om een bestaand systeem aan te "
                  "passen</strong>."),
            ("p", "Vragen die je helpen een ontwerp te evalueren: "
                  "<strong>haalt het elk criterium dat we opgesteld hebben?</strong>, "
                  "<strong>waar zit de zwakste schakel in het geheel?</strong> en "
                  "<strong>wat zou de volgende versie beter doen?</strong>"),
            ("p", "Moet je een koeltas ontwerpen die een drankje vier uur koel houdt, dan is dit "
                  "een criterium: <strong>de temperatuur mag na vier uur niet boven acht graden "
                  "zijn</strong>. De fysicakennis die daarbij helpt, is "
                  "<strong>hoe warmte door geleiding, stroming en straling verplaatst</strong>. "
                  "Ontwerp je een brug van spaghetti die zoveel mogelijk moet dragen, dan zet je "
                  "<strong>het evenwicht van krachten en het moment van een kracht</strong> in."),
        ]),
        dict(kop="STEM", blokken=[
            ("p", "De letters van <strong>STEM</strong> staan voor "
                  "<strong>wetenschappen, technologie, techniek en wiskunde</strong>. Je bekijkt een "
                  "probleem vanuit verschillende disciplines omdat "
                  "<strong>elk vak een stuk van de oplossing aanbrengt</strong>, en "
                  "<strong>bij een STEM-opdracht volstaat het niet om één discipline grondig in te "
                  "zetten</strong>."),
            ("p", "Tijdens de coronacrisis speelde wiskunde deze rol: "
                  "<strong>de verspreiding van het virus in kaart brengen</strong>. "
                  "Technologische kennis vroegen "
                  "<strong>het vaccin op een heel lage temperatuur bewaren</strong>, "
                  "<strong>het vaccin op grote schaal produceren</strong> en "
                  "<strong>het vaccin over de hele wereld vervoeren</strong>."),
            ("p", "<strong>Maatschappelijke uitdagingen zijn een reden om nieuwe technieken en "
                  "materialen te ontwikkelen</strong>. Daarom is een onderzoek naar zonnepanelen "
                  "ook een maatschappelijke zaak: "
                  "<strong>de keuzes die eruit volgen raken ieders energie en kosten</strong>."),
        ]),
    ],
    onthoud=[
        "Onderzoeksvraag, hypothese, onderzoeksplan, meten, besluiten.",
        "Eén grootheid tegelijk; de onafhankelijke op de horizontale as.",
        "Herhalen haalt toevallige afwijkingen eruit.",
        "Een conclusie blijft binnen wat je gemeten hebt.",
        "Herhaalbaar: iemand anders vindt met jouw plan hetzelfde.",
        "Ontwerpen: definiëren, criteria, deelproblemen, testen, bijsturen.",
        "Elk deelprobleem moet in de totaaloplossing passen.",
        "STEM is wetenschappen, technologie, techniek en wiskunde samen.",
    ],
)
