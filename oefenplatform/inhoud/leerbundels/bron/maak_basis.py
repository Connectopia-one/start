# -*- coding: utf-8 -*-
"""De leerbundels voor 🧱 Basis: de bouwstenen van wiskunde herhalen.

Kim vroeg op 23 september 2026 om een heel eenvoudige basismodule voor kinderen
die de basis nog niet vlot beheersen: maal en gedeeld door 10, 100 en 1000 met
de komma die meeschuift, maten omzetten, van breuk naar kommagetal naar geheel
getal, hoe alles heet (teller, noemer, quotiënt, rest), en ggd en kgv.

Eén bundel per thema, die bij deel 1 én bij deel 2 hoort. De bestandsnamen
krijgen het achtervoegsel -basis, zodat ze naast die van Start en Spark in de
map wiskunde/ kunnen staan zonder dat je ze verwart.

Schrijf kort en zonder omwegen: wie deze bundel leest, vond de leerstof de
eerste keer al moeilijk. Elk stuk één idee, met een tekening.

Alle getalvoorbeelden hieruit staan ook in `controleer.py`, dat ze narekent.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

BASIS = "🧱 Basis — de bouwstenen herhalen"
PLAATS = ["D", "H", "T", "E", "t", "h", "d"]

BUNDELS = {}


# ---------------------------------------------------------------------------
BUNDELS["maal-en-gedeeld-door-10-100-1000-basis"] = dict(
    vak="Wiskunde", niveau=BASIS, titel="Maal en gedeeld door 10, 100 en 1000",
    onder="Waarom de komma verspringt, en hoe je weet naar welke kant.",
    secties=[
        dict(kop="Wat elk cijfer waard is", blokken=[
            ("p", "In een getal telt niet alleen welk cijfer er staat, maar ook <strong>waar</strong> het "
                  r"staat. In \(345{,}6\) is de \(3\) geen drie, maar drie <strong>honderdtallen</strong>: \(300\)."),
            ("fig", svg.cijfertabel(PLAATS, [
                dict(cijfers=["", "3", "4", "5", "6", "", ""], komma=3, label="= 345,6"),
            ], accent=3),
             "D = duizendtal, H = honderdtal, T = tiental, E = eenheid. Na de komma: t = tiende, h = honderdste, d = duizendste."),
            ("p", "De komma staat <strong>altijd</strong> net achter de eenheden. Ze scheidt de hele "
                  "getallen van de stukjes die kleiner zijn dan één."),
        ]),
        dict(kop="Maal 10, 100 of 1000", blokken=[
            ("p", r"Bij <strong>maal \(10\)</strong> wordt elk cijfer tien keer zoveel waard. Een eenheid wordt "
                  "een tiental, een tiende wordt een eenheid. Alle cijfers schuiven dus één plaats naar links."),
            ("fig", svg.cijfertabel(PLAATS, [
                dict(cijfers=["", "", "", "3", "4", "5", ""], komma=3, label="3,45"),
                dict(cijfers=["", "", "3", "4", "5", "", ""], komma=3, label="× 10 = 34,5"),
                dict(cijfers=["", "3", "4", "5", "", "", ""], komma=3, label="× 100 = 345"),
                dict(cijfers=["3", "4", "5", "0", "", "", ""], komma=3, label="× 1000 = 3450", bijgezet=[3]),
            ], accent=3),
             r"Elke nul in \(10\), \(100\) of \(1000\) is één plaats. Bij × \(1000\) blijft de eenheid leeg: daar zet je een \(0\)."),
        ]),
        dict(kop="De komma springt", blokken=[
            ("p", "In plaats van alle cijfers te verschuiven, mag je ook de komma laten springen. Dat komt op "
                  "hetzelfde neer en gaat sneller."),
            ("kader", r"<strong>Maal</strong> \(10\), \(100\) of \(1000\): tel de nullen. Zoveel plaatsen springt de komma "
                      "naar <strong>rechts</strong>."),
            ("fig", svg.kommasprong("3,45", 2, "3,45 × 100 = 345"),
             "Twee nullen, twee sprongen naar rechts. De komma staat nu achteraan, dus je schrijft ze niet meer."),
            ("fig", svg.kommasprong("2,7", 3, "2,7 × 1000 = 2700"),
             r"Drie sprongen, maar er is maar één cijfer na de komma. Voor elke lege plaats zet je een \(0\) bij."),
            ("weetje", r"Een geheel getal heeft een verborgen komma achteraan: \(45\) is hetzelfde als \(45{,}0\). "
                       r"Zo zie je dat \(45 \cdot 100 = 4500\)."),
        ]),
        dict(kop="Gedeeld door 10, 100 of 1000", blokken=[
            ("kader", r"<strong>Gedeeld door</strong> \(10\), \(100\) of \(1000\): tel de nullen. Zoveel plaatsen springt "
                      "de komma naar <strong>links</strong>."),
            ("fig", svg.kommasprong("45", -2, "45 : 100 = 0,45"),
             r"De verborgen komma achter \(45\) springt twee plaatsen naar links. Vóór de komma zet je een \(0\)."),
            ("fig", svg.kommasprong("7", -3, "7 : 1000 = 0,007"),
             "Drie sprongen, maar er staat maar één cijfer. De lege plaatsen vul je met nullen."),
            ("p", r"Schrijf altijd een \(0\) vóór de komma als er geen ander cijfer staat: <strong>\(0{,}45\)</strong>, "
                  r"niet ,\(45\)."),
        ]),
        dict(kop="Links of rechts? Denk even na", blokken=[
            ("p", "Twijfel je naar welke kant de komma moet, vraag je dan af of het getal "
                  "<strong>groter</strong> of <strong>kleiner</strong> moet worden."),
            ("fig", svg.stappen(["maal 10, 100, 1000|wordt groter", "komma|naar rechts"]),
             "Maal maakt groter: de komma gaat naar rechts."),
            ("fig", svg.stappen(["gedeeld door|wordt kleiner", "komma|naar links"], kleur=svg.AMBER),
             "Gedeeld door maakt kleiner: de komma gaat naar links."),
            ("p", r"Controleer zo je uitkomst: \(3{,}45 \cdot 100\) kan nooit \(0{,}0345\) zijn, want dat is kleiner dan "
                  "waarmee je begon."),
            ("weetje", r"Nullen achteraan na de komma mag je weglaten: \(34{,}50 = 34{,}5\). Bij een geheel getal "
                       r"mag dat niet: \(30\) is iets anders dan \(3\), en \(305\) iets anders dan \(35\)."),
        ]),
    ],
    onthoud=[
        "De komma staat altijd net achter de eenheden.",
        r"Maal \(10\), \(100\), \(1000\): de komma springt \(1\), \(2\) of \(3\) plaatsen naar rechts.",
        r"Gedeeld door \(10\), \(100\), \(1000\): de komma springt \(1\), \(2\) of \(3\) plaatsen naar links.",
        "Tel de nullen: zoveel plaatsen springt de komma.",
        r"Een lege plaats vul je met een \(0\). Een geheel getal heeft een verborgen komma achteraan.",
        "Maal maakt groter, gedeeld door maakt kleiner. Kijk zo je uitkomst na.",
    ])


# ---------------------------------------------------------------------------
BUNDELS["maten-omzetten-basis"] = dict(
    vak="Wiskunde", niveau=BASIS, titel="Maten omzetten",
    onder="Lengte, gewicht en inhoud: van de ene maat naar de andere met de maatladder.",
    secties=[
        dict(kop="Drie maatladders", blokken=[
            ("p", "Voor lengte, gewicht en inhoud bestaat telkens een trapje van maten. Elke trede is "
                  r"<strong>\(10\) keer</strong> kleiner dan de vorige."),
            ("fig", svg.maatladder(["km", "hm", "dam", "m", "dm", "cm", "mm"]), "Lengte: de hoofdmaat is de meter."),
            ("fig", svg.maatladder(["kg", "hg", "dag", "g", "dg", "cg", "mg"]), "Gewicht: de hoofdmaat is de gram."),
            ("fig", svg.maatladder(["hl", "dal", "l", "dl", "cl", "ml"]), "Inhoud: de hoofdmaat is de liter."),
        ]),
        dict(kop="Wat het stukje voor de maat betekent", blokken=[
            ("p", "De ladders lijken op elkaar, omdat de voorvoegsels overal hetzelfde betekenen. Ken je ze, "
                  "dan ken je alle drie de ladders."),
            ("fig", bundel.tabel(["voorvoegsel", "betekent", "voorbeeld"], [
                ["kilo (k)", r"\(1000\) keer", r"\(1\) km = \(1000\) m"],
                ["hecto (h)", r"\(100\) keer", r"\(1\) hl = \(100\) l"],
                ["deca (da)", r"\(10\) keer", r"\(1\) dag = \(10\) g"],
                ["deci (d)", "een tiende", r"\(1\) dm = \(0{,}1\) m"],
                ["centi (c)", "een honderdste", r"\(1\) cl = \(0{,}01\) l"],
                ["milli (m)", "een duizendste", r"\(1\) mg = \(0{,}001\) g"],
            ]), ""),
        ]),
        dict(kop="Naar een kleinere maat: maal", blokken=[
            ("p", "Ga je op de ladder naar <strong>rechts</strong>, naar een kleinere maat, dan heb je er "
                  "<strong>meer</strong> van nodig. Het getal wordt groter: je doet <strong>maal</strong>."),
            ("p", r"Tel de treden. Van km naar m zijn het er drie, dus maal \(1000\)."),
            ("fig", svg.kommasprong("3,5", 3, "3,5 km = 3500 m"),
             r"Drie treden, dus de komma springt drie plaatsen naar rechts. Twee lege plaatsen worden een \(0\)."),
        ]),
        dict(kop="Naar een grotere maat: gedeeld door", blokken=[
            ("p", "Ga je naar <strong>links</strong>, naar een grotere maat, dan heb je er "
                  "<strong>minder</strong> van nodig. Het getal wordt kleiner: je doet <strong>gedeeld door</strong>."),
            ("fig", svg.kommasprong("250", -2, "250 cm = 2,5 m"),
             r"Van cm naar m zijn twee treden, dus de komma springt twee plaatsen naar links. \(2{,}50\) m is hetzelfde als \(2{,}5\) m."),
            ("kader", "Vraag je altijd af: wordt het getal groter of kleiner? Een meter is groter dan een "
                      r"centimeter, dus er gaan er <strong>minder</strong> in. \(250\) cm wordt \(2{,}5\) m, niet \(25\,000\) m."),
        ]),
        dict(kop="Met de herleidingstabel", blokken=[
            ("p", "Werk je liever met een tabel, dan kan dat ook. Zet het cijfer net vóór de komma onder de "
                  "maat die je hebt, en de rest van de cijfers ernaast."),
            ("fig", svg.cijfertabel(["km", "hm", "dam", "m", "dm", "cm", "mm"], [
                dict(cijfers=["1", "2", "5", "", "", "", ""], komma=0, label="1,25 km"),
                dict(cijfers=["1", "2", "5", "0", "", "", ""], komma=3, label="= 1250 m", bijgezet=[3]),
            ], accent=3),
             r"Bovenaan staat \(1{,}25\) km: de \(1\) onder km. Wil je meter, dan zet je de komma achter de m-kolom en vul je de lege plaats met een \(0\)."),
        ]),
        dict(kop="Welke maat past?", blokken=[
            ("p", "Een goede maat kiezen is ook een vaardigheid. Kies de maat waarbij je een handig getal krijgt."),
            ("fig", bundel.tabel(["wat", "lengte, gewicht of inhoud", "handige maat"], [
                ["een potlood", r"ongeveer \(18\)", "cm"],
                ["een deur", r"ongeveer \(2\)", "m"],
                ["een fietstocht", r"ongeveer \(25\)", "km"],
                ["een zak aardappelen", r"\(5\)", "kg"],
                ["een appel", r"ongeveer \(150\)", "g"],
                ["een fles water", r"\(1{,}5\)", "l"],
                ["een theelepel", r"\(5\)", "ml"],
            ]), ""),
            ("weetje", r"\(1\) liter water weegt ongeveer \(1\) kilogram. Daarom weegt een fles van \(1{,}5\) l ook "
                       r"ongeveer \(1{,}5\) kg."),
        ]),
    ],
    onthoud=[
        r"Elke trede op de maatladder is × \(10\) of : \(10\).",
        r"Kilo = \(1000\), hecto = \(100\), deca = \(10\), deci = een tiende, centi = een honderdste, milli = een duizendste.",
        "Naar een kleinere maat (naar rechts): maal. Het getal wordt groter.",
        "Naar een grotere maat (naar links): gedeeld door. Het getal wordt kleiner.",
        "Tel de treden: zoveel plaatsen springt de komma.",
        r"\(1\) km = \(1000\) m, \(1\) m = \(100\) cm, \(1\) kg = \(1000\) g, \(1\) l = \(100\) cl = \(1000\) ml.",
    ])


# ---------------------------------------------------------------------------
BUNDELS["wiskundewoorden-basis"] = dict(
    vak="Wiskunde", niveau=BASIS, titel="Wiskundewoorden",
    onder="Hoe de getallen in een som, een deling of een breuk heten.",
    secties=[
        dict(kop="Optellen en aftrekken", blokken=[
            ("p", "In een opdracht staat soms niet 'tel op', maar 'bereken de som'. Dan moet je weten wat "
                  "dat woord betekent."),
            ("fig", svg.benoemde_som([("12", "term"), ("+", None), ("5", "term"), ("=", None), ("17", "som")]),
             "Bij optellen heten de getallen termen. De uitkomst is de som."),
            ("fig", svg.benoemde_som([("17", "aftrektal"), ("−", None), ("5", "aftrekker"), ("=", None), ("12", "verschil")]),
             "Bij aftrekken: het aftrektal min de aftrekker geeft het verschil."),
            ("weetje", r"Het verschil tussen \(17\) en \(5\) is \(12\): zoveel liggen ze uit elkaar."),
        ]),
        dict(kop="Vermenigvuldigen", blokken=[
            ("fig", svg.benoemde_som([("4", "factor"), ("×", None), ("6", "factor"), ("=", None), ("24", "product")]),
             "De getallen die je vermenigvuldigt heten factoren. De uitkomst is het product."),
            ("p", r"De volgorde van de factoren maakt niet uit: \(4 \cdot 6\) en \(6 \cdot 4\) geven allebei \(24\)."),
        ]),
        dict(kop="Delen", blokken=[
            ("fig", svg.benoemde_som([("24", "deeltal"), (":", None), ("6", "deler"), ("=", None), ("4", "quotiënt")]),
             "Het deeltal wordt gedeeld door de deler. De uitkomst heet het quotiënt."),
            ("p", "Onthoud het zo: het <strong>deeltal</strong> is het getal dat verdeeld wordt. De "
                  "<strong>deler</strong> is het getal waardoor je deelt. Hier mag de volgorde "
                  r"<strong>niet</strong> wisselen: \(24 : 6\) is iets anders dan \(6 : 24\)."),
        ]),
        dict(kop="Delen met een rest", blokken=[
            ("p", r"Soms gaat een deling niet mooi op. Verdeel \(20\) knikkers in groepjes van \(3\): je krijgt \(6\) "
                  r"groepjes, en er blijven er \(2\) over."),
            ("fig", svg.groepjes(20, 3), "Zes volle groepjes van drie, en twee knikkers die overblijven."),
            ("fig", svg.benoemde_som([("20", "deeltal"), (":", None), ("3", "deler"), ("=", None),
                                     ("6", "quotiënt"), ("rest 2", "rest")], grootte=22),
             "Wat overblijft heet de rest."),
            ("kader", "Zo controleer je een deling met rest: <strong>quotiënt × deler + rest = deeltal</strong>. "
                      r"Hier: \(6 \cdot 3 + 2 = 20\). Klopt!"),
            ("p", r"De rest is altijd <strong>kleiner dan de deler</strong>. Blijft er \(3\) of meer over bij "
                  r"groepjes van \(3\), dan kan je nog een groepje maken. Is de rest \(0\), dan zeggen we dat de "
                  "deling <strong>opgaat</strong>."),
        ]),
        dict(kop="Een breuk", blokken=[
            ("fig", svg.breuk_namen(3, 4), ""),
            ("p", r"\(\tfrac{3}{4}\) lees je als <strong>drie vierde</strong>. De <strong>noemer</strong> (onder) zegt in "
                  "hoeveel gelijke stukken het geheel verdeeld is. De <strong>teller</strong> (boven) zegt "
                  "hoeveel stukken je neemt."),
            ("weetje", "Een ezelsbruggetje: de teller <strong>telt</strong> de stukken, de noemer "
                       "<strong>noemt</strong> hoe groot ze zijn (vierden, vijfden, tienden)."),
        ]),
        dict(kop="Alles op een rijtje", blokken=[
            ("fig", bundel.tabel(["bewerking", "de getallen heten", "de uitkomst heet"], [
                ["optellen  +", "termen", "som"],
                ["aftrekken  −", "aftrektal en aftrekker", "verschil"],
                ["vermenigvuldigen  ×", "factoren", "product"],
                ["delen  :", "deeltal en deler", "quotiënt (en soms een rest)"],
                [r"breuk  \(\tfrac{3}{4}\)", "teller en noemer", "—"],
            ]), ""),
        ]),
    ],
    onthoud=[
        "Optellen: termen geven een som.",
        "Aftrekken: aftrektal − aftrekker = verschil.",
        "Vermenigvuldigen: factoren geven een product.",
        "Delen: deeltal : deler = quotiënt, soms met een rest.",
        "De rest is altijd kleiner dan de deler. Controle: quotiënt × deler + rest = deeltal.",
        "Breuk: de teller staat boven, de noemer onder, met de breukstreep ertussen.",
    ])


# ---------------------------------------------------------------------------
BUNDELS["breuken-kommagetallen-en-gehele-getallen-basis"] = dict(
    vak="Wiskunde", niveau=BASIS, titel="Breuken, kommagetallen en gehele getallen",
    onder="Hetzelfde getal op drie manieren schrijven, en stap voor stap van de ene naar de andere.",
    secties=[
        dict(kop="Een breuk is een deling", blokken=[
            ("p", r"De breukstreep betekent <strong>gedeeld door</strong>. \(\tfrac{3}{4}\) is dus hetzelfde als \(3 : 4\). "
                  "Reken je die deling uit, dan krijg je een kommagetal."),
            ("fig", svg.stappen(["breuk|3/4", "deling|3 : 4", "kommagetal|0,75"]),
             "Drie stappen van breuk naar kommagetal: schrijf de breuk als deling en reken ze uit."),
            ("p", r"Dat werkt voor elke breuk: \(\tfrac{1}{2} = 1 : 2 = 0{,}5\) en \(\tfrac{2}{5} = 2 : 5 = 0{,}4\)."),
        ]),
        dict(kop="De snelle weg: noemer 10, 100 of 1000", blokken=[
            ("p", r"Is de noemer \(10\), \(100\) of \(1000\), dan hoef je bijna niet te rekenen. Delen door \(10\), \(100\) of "
                  r"\(1000\) ken je al: de komma springt naar links."),
            ("fig", bundel.tabel(["breuk", "hoe", "kommagetal"], [
                [r"\(\tfrac{7}{10}\)", r"\(7 : 10\), één sprong", r"\(0{,}7\)"],
                [r"\(\tfrac{23}{100}\)", r"\(23 : 100\), twee sprongen", r"\(0{,}23\)"],
                [r"\(\tfrac{5}{1000}\)", r"\(5 : 1000\), drie sprongen", r"\(0{,}005\)"],
            ]), ""),
            ("p", r"Soms kan je de noemer eerst \(10\) of \(100\) maken. Doe met de teller dan hetzelfde als met de "
                  r"noemer: \(\tfrac{3}{5} = \tfrac{6}{10} = 0{,}6\) en \(\tfrac{1}{4} = \tfrac{25}{100} = 0{,}25\)."),
            ("fig", svg.procentraster(25),
             r"\(25\) van de \(100\) vakjes: \(\tfrac{25}{100}\), en dat is ook \(\tfrac{1}{4}\) en \(0{,}25\)."),
        ]),
        dict(kop="Breuken die je best vanbuiten kent", blokken=[
            ("fig", svg.dubbele_getallenlijn(0, 1, [
                (0, "0", "0"), (0.25, "1/4", "0,25"), (0.5, "1/2", "0,5"),
                (0.75, "3/4", "0,75"), (1, "1", "1"),
            ]),
             "Hetzelfde punt op de getallenlijn, met boven de breuk en onder het kommagetal."),
            ("fig", bundel.tabel(["breuk", "kommagetal"], [
                [r"\(\tfrac{1}{2}\)", r"\(0{,}5\)"], [r"\(\tfrac{1}{4}\)", r"\(0{,}25\)"], [r"\(\tfrac{3}{4}\)", r"\(0{,}75\)"],
                [r"\(\tfrac{1}{5}\)", r"\(0{,}2\)"], [r"\(\tfrac{1}{10}\)", r"\(0{,}1\)"], [r"\(\tfrac{1}{100}\)", r"\(0{,}01\)"],
            ], breed="60%"), ""),
        ]),
        dict(kop="Van kommagetal naar breuk", blokken=[
            ("p", r"Tel de cijfers na de komma. Eén cijfer: de noemer is \(10\). Twee cijfers: \(100\). Drie cijfers: \(1000\). "
                  "De cijfers zelf worden de teller."),
            ("fig", svg.stappen(["kommagetal|0,75", "over 100|75/100", "vereenvoudig|: 25", "breuk|3/4"]),
             r"Twee cijfers na de komma, dus over \(100\). Dan teller en noemer delen door hetzelfde getal."),
            ("p", "Vereenvoudigen is niet verplicht, maar wel netjes. Je deelt teller en noemer door "
                  "hetzelfde getal, liefst het grootste dat kan: dat is de <strong>ggd</strong> "
                  "(zie de bundel over delers en veelvouden)."),
        ]),
        dict(kop="Wanneer is een breuk een geheel getal?", blokken=[
            ("p", "Als de deling <strong>opgaat</strong>, is de uitkomst een geheel getal. Dat gebeurt als "
                  r"de teller in de tafel van de noemer staat: \(\tfrac{8}{4} = 8 : 4\) = <strong>\(2\)</strong>."),
            ("fig", svg.dubbele_getallenlijn(0, 3, [
                (0, "0/4", "0"), (0.5, "2/4", "0,5"), (1, "4/4", "1"), (1.5, "6/4", "1,5"),
                (2, "8/4", "2"), (2.5, "10/4", "2,5"), (3, "12/4", "3"),
            ]),
             r"Vierden op een rij. Bij \(\tfrac{4}{4}\), \(\tfrac{8}{4}\) en \(\tfrac{12}{4}\) kom je precies op een geheel getal uit."),
            ("p", r"Staat de teller gelijk aan de noemer, dan heb je precies één geheel: \(\tfrac{5}{5} = 1\)."),
        ]),
        dict(kop="Groter dan één", blokken=[
            ("p", "Is de teller groter dan de noemer, dan is de breuk meer dan één geheel. Deel met rest: "
                  r"\(\tfrac{7}{2} = 7 : 2 = 3\), rest \(1\). Dat zijn \(3\) gehelen en nog \(\tfrac{1}{2}\)."),
            ("fig", svg.stappen(["breuk|7/2", "deel met rest|3 rest 1", "gemengd|3 en 1/2", "kommagetal|3,5"]),
             "De rest wordt de teller van de breuk die overblijft."),
        ]),
    ],
    onthoud=[
        r"De breukstreep betekent gedeeld door: \(\tfrac{3}{4} = 3 : 4 = 0{,}75\).",
        r"Noemer \(10\), \(100\) of \(1000\): de komma springt \(1\), \(2\) of \(3\) plaatsen naar links.",
        r"Kommagetal naar breuk: tel de cijfers na de komma. \(0{,}75 = \tfrac{75}{100} = \tfrac{3}{4}\).",
        r"Ken vanbuiten: \(\tfrac{1}{2} = 0{,}5\), \(\tfrac{1}{4} = 0{,}25\), \(\tfrac{3}{4} = 0{,}75\), \(\tfrac{1}{5} = 0{,}2\), \(\tfrac{1}{10} = 0{,}1\).",
        r"Gaat de deling op, dan is de breuk een geheel getal: \(\tfrac{8}{4} = 2\).",
        r"Teller groter dan noemer: meer dan één geheel. \(\tfrac{7}{2} = 3{,}5\).",
    ])


# ---------------------------------------------------------------------------
BUNDELS["delers-en-veelvouden-ggd-en-kgv-basis"] = dict(
    vak="Wiskunde", niveau=BASIS, titel="Delers en veelvouden: ggd en kgv",
    onder="Wat delers en veelvouden zijn, en hoe je de ggd en het kgv zoekt.",
    secties=[
        dict(kop="Deler en veelvoud", blokken=[
            ("p", r"\(3\) is een <strong>deler</strong> van \(12\), want \(12 : 3 = 4\) gaat op: er blijft niets over. "
                  r"Omgekeerd is \(12\) een <strong>veelvoud</strong> van \(3\), want \(12\) staat in de tafel van \(3\)."),
            ("fig", svg.rijtjes([
                ("tafel van 3", [3, 6, 9, 12, 15, 18, 21, 24, None], {12}, 12),
            ]),
             r"De veelvouden van \(3\) zijn de tafel van \(3\). \(12\) staat erin, dus \(3\) is een deler van \(12\)."),
            ("p", r"Delers zoek je het makkelijkst <strong>in paren</strong>: \(1 \cdot 12\), \(2 \cdot 6\) en \(3 \cdot 4\). "
                  r"De delers van \(12\) zijn dus \(1\), \(2\), \(3\), \(4\), \(6\) en \(12\)."),
            ("weetje", "Een getal heeft maar een paar delers, maar oneindig veel veelvouden: de tafel gaat altijd door."),
        ]),
        dict(kop="Snel zien of een getal deelbaar is", blokken=[
            ("fig", bundel.tabel(["deelbaar door", "als …", "voorbeeld"], [
                [r"\(2\)", r"het laatste cijfer even is (\(0\), \(2\), \(4\), \(6\), \(8\))", r"\(348\)"],
                [r"\(5\)", r"het laatste cijfer \(0\) of \(5\) is", r"\(235\)"],
                [r"\(10\)", r"het laatste cijfer \(0\) is", r"\(470\)"],
                [r"\(3\)", r"de som van de cijfers deelbaar is door \(3\)", r"\(123\): \(1 + 2 + 3 = 6\)"],
                [r"\(9\)", r"de som van de cijfers deelbaar is door \(9\)", r"\(729\): \(7 + 2 + 9 = 18\)"],
                [r"\(4\)", r"de laatste twee cijfers deelbaar zijn door \(4\)", r"\(316\): \(16 : 4 = 4\)"],
            ]), ""),
        ]),
        dict(kop="De grootste gemeenschappelijke deler (ggd)", blokken=[
            ("fig", svg.stappen(["schrijf|alle delers op", "kleur|wat in beide staat", "kies|het grootste"]),
             "Drie stappen voor de ggd."),
            ("fig", svg.rijtjes([
                ("delers van 12", [1, 2, 3, 4, 6, 12], {1, 2, 3, 6}, 6),
                ("delers van 18", [1, 2, 3, 6, 9, 18], {1, 2, 3, 6}, 6),
            ]),
             r"\(1\), \(2\), \(3\) en \(6\) staan in allebei de rijtjes. De grootste daarvan is \(6\), dus \(\text{ggd}(12, 18) = 6\)."),
            ("weetje", "In sommige boeken heet dit de grootste <em>gemene</em> deler. Dat is hetzelfde."),
        ]),
        dict(kop="Het kleinste gemeenschappelijk veelvoud (kgv)", blokken=[
            ("fig", svg.stappen(["schrijf|de tafels op", "kleur|wat in beide staat", "kies|het kleinste"]),
             "Drie stappen voor het kgv."),
            ("fig", svg.rijtjes([
                ("tafel van 4", [4, 8, 12, 16, 20, 24, None], {12, 24}, 12),
                ("tafel van 6", [6, 12, 18, 24, 30, 36, None], {12, 24}, 12),
            ]),
             r"\(12\) en \(24\) staan in allebei de tafels. De kleinste is \(12\), dus \(\text{kgv}(4, 6) = 12\)."),
            ("kader", "Sneller: loop de tafel van het <strong>grootste</strong> getal af, en stop bij het "
                      r"eerste getal dat ook in de tafel van het kleinste staat. \(6\), \(12\) … en \(12\) staat in de "
                      r"tafel van \(4\)."),
        ]),
        dict(kop="Waarvoor heb je ze nodig?", blokken=[
            ("p", r"<strong>De ggd</strong> gebruik je om een breuk te vereenvoudigen. Bij \(\tfrac{12}{18}\) deel je "
                  r"teller en noemer door \(6\): dat geeft <strong>\(\tfrac{2}{3}\)</strong>."),
            ("p", r"<strong>Het kgv</strong> gebruik je om breuken dezelfde noemer te geven. Bij \(\tfrac{1}{4} + \tfrac{1}{6}\) "
                  r"wordt de noemer \(12\): \(\tfrac{3}{12} + \tfrac{2}{12}\) = <strong>\(\tfrac{5}{12}\)</strong>."),
            ("p", r"En in het echt: een bus vertrekt elke \(4\) minuten, een tram elke \(6\) minuten. Om 8.00 u "
                  r"vertrekken ze samen. Het kgv van \(4\) en \(6\) is \(12\), dus ze vertrekken weer samen om "
                  "<strong>8.12 u</strong>."),
            ("weetje", r"Een getal met precies twee delers, \(1\) en zichzelf, heet een priemgetal: \(2\), \(3\), \(5\), \(7\), \(11\), \(13\) …"),
        ]),
    ],
    onthoud=[
        r"\(3\) is een deler van \(12\), want \(12 : 3\) gaat op. \(12\) is een veelvoud van \(3\), want het staat in de tafel van \(3\).",
        r"Delers zoek je in paren: \(1 \cdot 12\), \(2 \cdot 6\), \(3 \cdot 4\).",
        r"ggd: alle delers opschrijven, wat in beide staat, het grootste. \(\text{ggd}(12, 18) = 6\).",
        r"kgv: de tafels opschrijven, wat in beide staat, het kleinste. \(\text{kgv}(4, 6) = 12\).",
        "ggd om te vereenvoudigen, kgv om breuken dezelfde noemer te geven.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
