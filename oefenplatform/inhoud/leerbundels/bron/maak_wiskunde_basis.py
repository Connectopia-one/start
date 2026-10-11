# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde basis op 🚀 Boost doorstroom.

Gebaseerd op de vakfiche wiskunde basis 2DO, geldig vanaf 1 januari 2027. Dit
is het vak voor de richtingen die géén wiskunde gevorderd volgen; de stof
overlapt dus deels met [[maak_wiskunde_boost.py]], maar de bundels staan apart
omdat het een ander vak is met eigen vragen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

Elk getalvoorbeeld dat hier beweerd wordt, staat ook in controleer.py, waar het
uitgerekend wordt in plaats van uitgeschreven. Zet je hier een voorbeeld bij,
zet het daar dan ook bij.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Wiskunde basis"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    BUNDELS[slug + "-boost-doorstroom"] = b


# ───────────────────────── 1. De reële getallen, wortels en machten
zet("de-reele-getallen-wortels-en-machten",
    titel="De reële getallen, wortels en machten",
    onder="De getallenverzamelingen en hun decimale vormen, de wetenschappelijke notatie, rekenen met wortels en machten, en de drie bewerkingseigenschappen.",
    secties=[
        dict(kop="De getallenverzamelingen", blokken=[
            ("p", "De verzamelingen zitten in elkaar als Russische poppetjes: elke kleinere zit volledig in "
                  "de grotere. <strong>Het getal 7 hoort dus tegelijk in \\(\\mathbb{N}\\), \\(\\mathbb{Z}\\), "
                  "\\(\\mathbb{Q}\\) en \\(\\mathbb{R}\\)</strong> — natuurlijk, geheel, rationaal én reëel."),
            ("fig", svg.getallenverzamelingen(),
             "elke kleinere verzameling zit volledig in de grotere"),
            ("kader", tabel(["verzameling", "teken", "wat erbij komt", "voorbeelden"],
                            [["de natuurlijke getallen", "\\(\\mathbb{N}\\)", "de telgetallen", "\\(0\\), \\(1\\), \\(2\\), \\(7\\)"],
                             ["<strong>de gehele getallen</strong>", "\\(\\mathbb{Z}\\)", "<strong>de negatieve getallen</strong>; <strong>alle natuurlijke getallen zitten erin</strong>",
                              "<strong>\\(-5\\)</strong>, \\(-1\\), \\(0\\), \\(7\\)"],
                             ["<strong>de rationale getallen</strong>", "\\(\\mathbb{Q}\\)", "alles wat je <strong>als breuk \\(\\frac{a}{b}\\) van twee gehele getallen</strong> kan schrijven",
                              "<strong>\\(0{,}75\\)</strong>, <strong>\\(-\\frac{2}{3}\\)</strong>, <strong>\\(4\\)</strong>, \\(\\frac{3}{4}\\)"],
                             ["<strong>de reële getallen</strong>", "\\(\\mathbb{R}\\)", "ook <strong>de irrationale</strong>: wat géén breuk is, \\(\\mathbb{R} \\setminus \\mathbb{Q}\\)",
                              "<strong>\\(\\sqrt{2}\\)</strong>, <strong>\\(\\pi\\)</strong>, <strong>\\(\\sqrt{3}\\)</strong>"]])),
            ("p", "Het teken \\(\\subset\\) betekent “zit in”: \\(\\mathbb{N} \\subset \\mathbb{Z} \\subset "
                  "\\mathbb{Q} \\subset \\mathbb{R}\\). Lees die ketting niet achterstevoren. "
                  "<strong>Niet elk reëel getal is dus rationaal</strong>; het is net omgekeerd, want de reële "
                  "getallen omvatten de rationale én de irrationale. En \\(-5 \\in \\mathbb{Z}\\) maar "
                  "\\(-5 \\notin \\mathbb{N}\\): <strong>de gehele getallen voegen de negatieve toe aan de "
                  "natuurlijke</strong>."),
        ]),
        dict(kop="Waarom de reële getallen nodig zijn", blokken=[
            ("p", "<strong>De reële getallen zijn nodig om de getallenas vol te maken.</strong> Tussen de "
                  "breuken zitten gaten: \\(\\sqrt{2}\\) en \\(\\pi\\) liggen wél op de as, maar ze zijn geen "
                  "breuk. <strong>\\(\\sqrt{2}\\) staat niet bij de rationale getallen omdat ze geen breuk "
                  "is</strong> — men kan bewijzen dat geen enkele breuk haar precies gelijk is."),
            ("fig", svg.getallenlijn(470, 0, 4,
                                     [(0, "0", svg.INK, False), (1, "1", svg.INK, False),
                                      (2, "2", svg.INK, False), (3, "3", svg.INK, False),
                                      (4, "4", svg.INK, False),
                                      (0.75, "3/4", svg.FOREST, True),
                                      (1.4142, "√2", svg.AMBER, True),
                                      (3.1416, "π", svg.AMBER, True)], hoogte=96),
             "de groene breuk is rationaal, de twee oranje getallen zijn het niet"),
        ]),
        dict(kop="De decimale vorm verraadt de soort", blokken=[
            ("kader", tabel(["decimale vorm", "wat ze betekent", "voorbeeld"],
                            [["<strong>begrensd</strong> (eindig)", "na enkele cijfers stopt ze", "<strong>\\(0{,}25\\)</strong>"],
                             ["<strong>onbegrensd repeterend</strong>", "de cijfers stoppen niet maar herhalen een patroon",
                              "<strong>\\(\\frac{1}{3} = 0{,}333\\ldots\\)</strong>"],
                             ["<strong>onbegrensd niet-repeterend</strong>", "de cijfers stoppen nooit en herhalen nooit — <strong>dan is het getal irrationaal</strong>",
                              "<strong>\\(\\pi\\)</strong>"]])),
            ("p", "De vakfiche noemt de <strong>vormen</strong> van een getal: de <strong>decimale "
                  "vorm</strong>, de <strong>wortelvorm</strong>, de <strong>breuk en het procent</strong>. "
                  "Een lettervorm is geen getalvorm. Omzetten van de ene vorm naar de andere "
                  "<strong>mag met ICT</strong>; de vakfiche vraagt dat zelfs uitdrukkelijk."),
            ("p", "Van breuk naar procent deel je gewoon uit: <strong>\\(\\frac{3}{5} = 0{,}6 = 60\\,\\%\\)</strong>. "
                  "En omgekeerd werkt een procent als een kommagetal: <strong>\\(12\\,\\%\\) van \\(250\\) is "
                  "\\(0{,}12 \\cdot 250 = 30\\)</strong>."),
            ("p", "Wil je getallen vergelijken, breng ze dan allemaal naar de decimale vorm. "
                  "\\(0{,}8\\) tegen \\(\\frac{3}{4} = 0{,}75\\), \\(\\frac{7}{10} = 0{,}7\\) en "
                  "\\(\\frac{2}{3} \\approx 0{,}67\\): <strong>\\(0{,}8\\) is dan duidelijk het grootste</strong>."),
        ]),
        dict(kop="De wetenschappelijke notatie", blokken=[
            ("p", "Een getal in wetenschappelijke notatie is een getal <strong>tussen \\(1\\) en \\(10\\)</strong>, maal "
                  "een macht van tien: \\(a \\cdot 10^{n}\\) met \\(1 \\leq a < 10\\). <strong>Voor de macht mag "
                  "dus niet elk getal staan</strong>: \\(45 \\cdot 10^{3}\\) is niet correct genoteerd, want "
                  "\\(45\\) ligt niet tussen \\(1\\) en \\(10\\)."),
            ("kader", tabel(["getal", "wetenschappelijke notatie", "waarom"],
                            [["<strong>\\(45\\,000\\)</strong>", "<strong>\\(4{,}5 \\cdot 10^{4}\\)</strong>", "\\(4{,}5 \\cdot 10\\,000 = 45\\,000\\)"],
                             ["<strong>\\(0{,}003\\)</strong>", "<strong>\\(3 \\cdot 10^{-3}\\)</strong>", "een getal kleiner dan \\(1\\) krijgt een <strong>negatieve</strong> exponent"]])),
        ]),
        dict(kop="Wortels", blokken=[
            ("p", "De vierkantswortel vraagt welk getal maal zichzelf je getal geeft; de derdemachtswortel "
                  "welk getal drie keer maal zichzelf. <strong>\\(\\sqrt{81} = 9\\)</strong> want "
                  "\\(9 \\cdot 9 = 81\\), <strong>\\(\\sqrt[3]{27} = 3\\)</strong> en "
                  "<strong>\\(\\sqrt[3]{64} = 4\\)</strong>."),
            ("p", "<strong>Je vereenvoudigt een wortel door er een kwadraat uit te halen.</strong> "
                  "<strong>\\(\\sqrt{50} = 5\\sqrt{2}\\)</strong>, want \\(50 = 25 \\cdot 2\\) en "
                  "\\(\\sqrt{25} = 5\\). Net zo is <strong>\\(\\sqrt{8} = 2\\sqrt{2}\\)</strong>, "
                  "want \\(8 = 4 \\cdot 2\\)."),
            ("kader", tabel(["regel", "wat ze zegt", "voorbeeld"],
                            [["wortels vermenigvuldigen", "de wortel van een product is het product van de wortels",
                              "<strong>\\(\\sqrt{3} \\cdot \\sqrt{12} = \\sqrt{36} = 6\\)</strong>"],
                             ["gelijke wortelvormen optellen", "je telt ze op als gelijke termen",
                              "<strong>\\(\\sqrt{2} + 3\\sqrt{2} = 4\\sqrt{2}\\)</strong>"],
                             ["<strong>de noemer wortelvrij maken</strong>", "<strong>vermenigvuldig boven en onder met die wortel</strong>",
                              "\\(\\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}\\)"]])),
            ("p", "En één valstrik: <strong>de wortel van een som is níét de som van de wortels</strong>, dus "
                  "\\(\\sqrt{a + b} \\neq \\sqrt{a} + \\sqrt{b}\\). Het tegenvoorbeeld staat klaar: "
                  "\\(\\sqrt{9 + 16} = \\sqrt{25} = 5\\), terwijl \\(3 + 4 = 7\\)."),
            ("p", "Ook handig om te weten: \\(\\sqrt[3]{216} = 6\\), want \\(6^{3} = 216\\)."),
        ]),
        dict(kop="Machten", blokken=[
            ("kader", tabel(["regel", "voorbeeld"],
                            [["bij een product tel je de exponenten op", "<strong>\\(2^{3} \\cdot 2^{2} = 2^{5} = 32\\)</strong>; in lettervorm <strong>\\(a^{3} \\cdot a^{5} = a^{8}\\)</strong>"],
                             ["bij een quotiënt trek je ze af", "<strong>\\(\\frac{2^{6}}{2} = 2^{5}\\)</strong>; <strong>\\(\\frac{3^{4}}{3^{2}} = 3^{2} = 9\\)</strong>"],
                             ["<strong>een negatieve exponent</strong> is één gedeeld door de macht", "<strong>\\(10^{-2} = \\frac{1}{100} = 0{,}01\\)</strong>"],
                             ["<strong>een macht nul is altijd 1</strong>", "\\(a^{0} = 1\\) zolang het grondtal niet nul is; het volgt uit de aftrekregel"],
                             ["een <strong>oneven</strong> exponent houdt het minteken", "<strong>\\((-2)^{3} = -8\\)</strong>"],
                             ["een <strong>even</strong> exponent maakt het positief", "<strong>\\((-3)^{2} = 9\\)</strong>, dus niet \\(-9\\) — let op de haakjes, want \\(-3^{2} = -9\\)"]])),
            ("p", "Let op het verschil tussen een macht en een vermenigvuldiging: \\(2 \\cdot 5 = 10\\), en dat "
                  "is iets heel anders dan \\(2^{5} = 32\\)."),
        ]),
        dict(kop="De bewerkingseigenschappen", blokken=[
            ("p", "De vakfiche noemt er <strong>drie</strong>, elk in woorden en in symbolen."),
            ("kader", tabel(["eigenschap", "wat ze zegt", "voorbeeld"],
                            [["<strong>de commutativiteit</strong> (de wisseleigenschap)", "<strong>de orde van twee factoren maakt niet uit</strong>",
                              "\\(3 \\cdot 5 = 5 \\cdot 3\\)"],
                             ["<strong>de associativiteit</strong>", "de manier van groeperen maakt niet uit",
                              "\\((2 + 3) + 4 = 2 + (3 + 4)\\)"],
                             ["<strong>de distributiviteit</strong>", "je verdeelt een factor over elke term, of je haalt hem er juist buiten",
                              "<strong>\\(3 \\cdot 7 + 3 \\cdot 3 = 3 \\cdot 10\\)</strong>: de gemeenschappelijke factor \\(3\\) buiten haakjes"]])),
        ]),
        dict(kop="Exact werken", blokken=[
            ("p", "Transitiviteit staat er niet bij in dat rijtje; dat is een eigenschap van een orde, niet "
                  "van een bewerking."),
            ("weetje", "<strong>Werk zo lang mogelijk exact</strong>, want <strong>afronden onderweg "
                       "vervalst je resultaat</strong>. De vakfiche zegt het letterlijk: hoe onnauwkeuriger "
                       "je tussenresultaten, hoe meer je eindresultaat afwijkt."),
        ]),
    ])


# ───────────────────────── 2. Getallen ordenen, afronden en intervallen
zet("getallen-ordenen-afronden-en-intervallen",
    titel="Getallen ordenen, afronden en intervallen",
    onder="De ongelijkheidstekens en de getallenas, de afrondregel, en de drie soorten intervallen met hun notatie.",
    secties=[
        dict(kop="Ordenen op de getallenas", blokken=[
            ("p", "Over de getallenas klopt: <strong>rechts is groter</strong>, <strong>elk reëel getal "
                  "heeft er een plaats</strong> en <strong>ze loopt in beide richtingen door</strong>. Dat "
                  "eerste punt beslist alles: <strong>hoe verder naar links, hoe kleiner</strong>."),
            ("p", "Bij negatieve getallen keert je gevoel dus om. <strong>\\(-10 < -3\\)</strong>, en "
                  "<strong>\\(-0{,}5 > -1{,}5\\)</strong>. In een rij als \\(-5\\), \\(-2\\), \\(-0{,}5\\) is "
                  "<strong>\\(-5\\) het kleinste</strong>: bij negatieve getallen is het getal met de "
                  "grootste cijferwaarde net het kleinste. Van klein naar groot staat dus "
                  "<strong>\\(-2 < -0{,}5 < 0 < 1{,}5\\)</strong>."),
            ("kader", tabel(["teken", "wat het betekent", "let op"],
                            [["\\(<\\)", "strikt kleiner dan", "de grens doet niet mee"],
                             ["<strong>\\(>\\)</strong>", "<strong>strikt groter dan</strong>", "het teken <strong>zonder streepje</strong> eronder"],
                             ["\\(\\leq\\)", "<strong>kleiner dan of gelijk aan</strong>", "<strong>het streepje eronder voegt de gelijkheid toe</strong>: \\(3 \\leq 3\\) is waar"],
                             ["\\(\\geq\\)", "groter dan of gelijk aan", "mét streepje, dus de grens doet mee"],
                             ["\\(\\neq\\)", "niet gelijk aan", "het isgelijkteken met een schrap erdoor"]])),
            ("p", "<strong>Vergelijk breuken door ze eerst naar de decimale vorm om te zetten, dan zie je de "
                  "orde meteen</strong>: twee kommagetallen vergelijk je cijfer per cijfer. Van \\(0{,}8\\), "
                  "\\(0{,}75\\), \\(0{,}7\\) en \\(\\frac{2}{3}\\) is <strong>\\(0{,}8\\) het grootste</strong>. "
                  "<strong>\\(\\frac{2}{3} = 0{,}6666\\ldots\\)</strong>, en daarvan is <strong>\\(0{,}67\\)</strong> "
                  "de beste benadering. Let wel: afronden maakt het minder exact."),
            ("p", "Nog twee bakens. <strong>Het getal precies tussen \\(4\\) en \\(7\\) is \\(5{,}5\\)</strong>, "
                  "het gemiddelde van de twee. En tussen \\(1\\) en \\(2\\) liggen onder meer "
                  "<strong>\\(1{,}5\\)</strong>, <strong>\\(\\sqrt{2} \\approx 1{,}41\\)</strong> en "
                  "<strong>\\(\\frac{7}{5} = 1{,}4\\)</strong>."),
            ("p", "Een breuk herken je ook terug in een kommagetal: <strong>\\(0{,}375 = \\frac{3}{8}\\)</strong>, "
                  "want \\(\\frac{375}{1000}\\) met teller en noemer gedeeld door \\(125\\) geeft \\(\\frac{3}{8}\\). "
                  "Omzetten van de ene vorm naar de andere <strong>mag met ICT</strong>; de vakfiche vraagt "
                  "dat zelfs."),
        ]),
        dict(kop="Afronden", blokken=[
            ("p", "De regel is kort: <strong>je kijkt enkel naar het eerste cijfer dat wegvalt</strong>. "
                  "<strong>Is dat \\(5\\) of meer, dan rond je naar boven af</strong>; <strong>is het minder "
                  "dan \\(5\\), dan naar beneden</strong>. De cijfers daarachter spelen geen rol."),
            ("kader", tabel(["opgave", "antwoord", "waarom"],
                            [["<strong>\\(3{,}476\\) op twee cijfers na de komma</strong>", "<strong>\\(3{,}48\\)</strong>",
                              "het derde cijfer is een \\(6\\), dus de \\(7\\) gaat naar \\(8\\)"],
                             ["<strong>\\(12{,}3449\\) op één cijfer na de komma</strong>", "<strong>\\(12{,}3\\)</strong>",
                              "het tweede cijfer is een \\(4\\), dus naar beneden; dat de cijfers erna groter zijn, doet niet mee"],
                             ["<strong>\\(1\\,999\\) op honderdtallen</strong>", "<strong>\\(2\\,000\\)</strong>",
                              "het tientalcijfer is \\(9\\), dus \\(19\\) honderdtallen worden er \\(20\\)"]])),
            ("p", "<strong>Altijd naar boven afronden zou de resultaten systematisch te groot maken.</strong> "
                  "Een winkel die elke prijs naar boven afrondt op \\(5\\) cent, komt dus telkens iets te hoog "
                  "uit, en daarom bestaat de regel van \\(5\\) of meer."),
        ]),
        dict(kop="De drie soorten intervallen", blokken=[
            ("p", "De vakfiche noemt <strong>drie</strong> soorten. Ze verschillen alleen in wat er met "
                  "de grenzen gebeurt."),
            ("fig", svg.intervallen(),
             "een vol bolletje betekent dat de grens meedoet, een open bolletje dat ze dat niet doet"),
        ]),
        dict(kop="De notatie", blokken=[
            ("kader", tabel(["soort", "de grenzen", "notatie", "op de getallenas"],
                            [["<strong>open</strong>", "<strong>horen er niet bij</strong>", "\\(\\left]2, 5\\right[\\)", "open bolletjes"],
                             ["<strong>halfopen</strong> (of halfgesloten)", "<strong>één grens hoort erbij, de andere niet</strong>",
                              "\\(\\left[2, 5\\right[\\)", "één open en één vol bolletje"],
                             ["<strong>gesloten</strong>", "<strong>horen erbij</strong>", "\\(\\left[2, 5\\right]\\)",
                              "<strong>volle bolletjes aan de grenzen</strong>"]])),
            ("p", "<strong>Het vierkante haakje wijst naar buiten als de grens niet meedoet</strong>, en naar "
                  "binnen als ze wel meedoet. In de internationale notatie staan er ronde haakjes voor een "
                  "open grens; allebei bedoelen ze hetzelfde. Een <strong>dubbel interval</strong> bestaat "
                  "niet als begrip, en <strong>één enkel getal is geen interval</strong>: een interval is "
                  "een aaneengesloten stuk van de getallenas met twee grenzen."),
        ]),
        dict(kop="Aan de kant van oneindig", blokken=[
            ("p", "<strong>Aan de kant van oneindig staat een interval altijd open</strong>, want "
                  "\\(\\infty\\) is geen getal en kan dus nooit tot de verzameling horen. Je schrijft "
                  "\\(\\left[2, +\\infty\\right[\\), nooit \\(\\left[2, +\\infty\\right]\\)."),
            ("kader", tabel(["ongelijkheid of situatie", "het interval", "waarom"],
                            [["<strong>\\(x > 3\\)</strong>", "<strong>\\(\\left]3, +\\infty\\right[\\)</strong>", "strikt groter, dus \\(3\\) zelf valt erbuiten"],
                             ["<strong>\\(x \\leq 5\\)</strong>", "<strong>\\(\\left]-\\infty, 5\\right]\\)</strong>", "het isgelijkteken zit erin, dus \\(5\\) hoort erbij"],
                             ["<strong>een temperatuur tussen \\(-2\\) en \\(8\\) graden, grenzen meegerekend</strong>",
                              "<strong>\\(\\left[-2, 8\\right]\\)</strong>", "grenzen meegerekend is gesloten aan beide zijden"],
                             ["<strong>een korting vanaf \\(50\\) euro</strong>", "<strong>\\(\\left[50, +\\infty\\right[\\)</strong>",
                              "vanaf \\(50\\) betekent dat \\(50\\) meedoet; <em>vanaf meer dan</em> \\(50\\) zou open zijn"]])),
        ]),
        dict(kop="Wat het woord strikt verandert", blokken=[
            ("p", "In \\(\\left[2, 5\\right]\\) horen <strong>\\(2\\)</strong>, <strong>\\(3{,}5\\)</strong> en "
                  "<strong>\\(5\\)</strong> thuis, maar \\(5{,}5\\) niet. In \\(\\left]0, 1\\right[\\) horen "
                  "<strong>\\(0{,}01\\)</strong>, <strong>\\(0{,}5\\)</strong> en <strong>\\(0{,}99\\)</strong>, "
                  "maar \\(0\\) en \\(1\\) zelf niet."),
            ("p", "Daar zit ook het verschil dat het woordje <strong>strikt</strong> maakt: <strong>de grens "
                  "valt weg</strong>. <strong>Bij \\(x > 0\\) hoort nul dus niet bij de oplossingen</strong>; "
                  "bij \\(x \\geq 0\\) wel."),
            ("p", "<strong>De oplossingenverzameling van een ongelijkheid mag je als interval "
                  "noteren</strong>, en de vakfiche vraagt ook om ze op een getallenas voor te stellen. Dat "
                  "is handig omdat <strong>een interval de oplossing in één blik toont</strong>: je ziet "
                  "meteen waar ze begint en eindigt, en of de grenzen meedoen."),
        ]),
    ])


# ───────────────────────── 3. Logica: bewerkingen en waarheidstabellen
zet("logica-bewerkingen-en-waarheidstabellen",
    titel="Logica: bewerkingen en waarheidstabellen",
    onder="De vijf logische bewerkingen met hun symbolen, de waarheidstabel met haar rijen, tautologie en contradictie, de kwantoren en de logische poorten.",
    secties=[
        dict(kop="Uitspraken en bewerkingen", blokken=[
            ("p", "Een <strong>logische uitspraak</strong> is <strong>een bewering die waar of vals "
                  "is</strong>. Ze heeft precies <strong>twee</strong> mogelijke waarheidswaarden, en een "
                  "derde bestaat in deze logica niet. Een vraag of een bevel is dus geen uitspraak."),
            ("p", "De vakfiche noemt <strong>vijf</strong> bewerkingen: <strong>negatie \\(\\neg\\) en "
                  "conjunctie \\(\\wedge\\)</strong>, <strong>disjunctie \\(\\vee\\)</strong>, "
                  "<strong>implicatie \\(\\Rightarrow\\) en equivalentie \\(\\Leftrightarrow\\)</strong>. "
                  "Substitutie is een methode bij stelsels en geen logische bewerking."),
            ("kader", tabel(["bewerking", "teken", "het woord", "wanneer ze waar is"],
                            [["<strong>de negatie</strong> (de ontkenning)", "\\(\\neg p\\)", "niet",
                              "<strong>ze keert de waarheidswaarde om</strong>: was de uitspraak waar, dan is de negatie vals"],
                             ["<strong>de conjunctie</strong>", "\\(p \\wedge q\\)", "<strong>en</strong>",
                              "<strong>als beide delen waar zijn</strong>; één vals deel maakt het geheel vals"],
                             ["<strong>de disjunctie</strong>", "\\(p \\vee q\\)", "of",
                              "<strong>als minstens één deel waar is</strong>; <strong>ook als beide waar zijn</strong>"],
                             ["<strong>de implicatie</strong>", "\\(p \\Rightarrow q\\)", "als … dan",
                              "altijd, <strong>behalve als \\(p\\) waar en \\(q\\) vals is</strong>"],
                             ["<strong>de equivalentie</strong>", "\\(p \\Leftrightarrow q\\)", "dan en slechts dan als",
                              "<strong>als beide delen dezelfde waarde hebben</strong>: twee keer waar of twee keer vals"]])),
            ("p", "<strong>Het of van de logica sluit niet uit dat beide delen waar zijn.</strong> Daar "
                  "verschilt het van het of in de omgangstaal, waar men vaak een keuze bedoelt."),
            ("p", "Bij de implicatie zit nog een valstrik: <strong>een implicatie met een vals eerste deel "
                  "is niet vals maar juist waar</strong>. Als het regent, dan draag ik een jas — regent het "
                  "niet, dan is de belofte niet geschonden. Daar zit meteen het verschil met het als-dan van "
                  "de omgangstaal: <strong>het logische \\(p \\Rightarrow q\\) zegt niets over een "
                  "oorzaak</strong>."),
            ("p", "Zo zet je een zin om in symbolen: <em>p is waar en q is vals</em> wordt "
                  "<strong>\\(p \\wedge \\neg q\\)</strong>."),
        ]),
        dict(kop="Tautologie en contradictie", blokken=[
            ("p", "Een <strong>tautologie</strong> is <strong>een uitspraak die altijd waar is</strong>: "
                  "bij elke combinatie komt waar uit, dus haar kolom staat vol waar. Een "
                  "<strong>contradictie</strong> is het omgekeerde: <strong>altijd vals</strong>."),
            ("p", "Tautologieën zijn bijvoorbeeld <strong>\\(p \\vee \\neg p\\)</strong>, "
                  "<strong>\\(p \\Rightarrow p\\)</strong> en <strong>\\(p \\Leftrightarrow p\\)</strong>. "
                  "<strong>\\(p \\vee \\neg p\\) is dus geen contradictie maar een tautologie</strong>; een "
                  "contradictie is \\(p \\wedge \\neg p\\): het regent én het regent niet."),
            ("p", "<strong>Je bewijst een tautologie met een tabel waarin alle rijen waar geven.</strong> "
                  "Eén rij met vals volstaat om haar te weerleggen."),
        ]),
        dict(kop="Nodig en voldoende", blokken=[
            ("kader", tabel(["soort voorwaarde", "wat ze betekent", "voorbeeld"],
                            [["<strong>nodig</strong>", "<strong>zonder haar geldt het besluit niet</strong>",
                              "een cijfer halen is nodig om te slagen, maar niet voldoende"],
                             ["<strong>voldoende</strong>", "<strong>met haar geldt het besluit zeker</strong>",
                              "<strong>deelbaar zijn door \\(4\\) is voldoende om even te zijn</strong>, maar niet nodig: \\(6\\) is ook even"]])),
            ("p", "<strong>Bij een equivalentie is de voorwaarde zowel nodig als voldoende</strong>: de pijl "
                  "gaat in beide richtingen, en daarom staat \\(p \\Leftrightarrow q\\) voor <em>dan en "
                  "slechts dan als</em>."),
            ("p", "De vakfiche noemt <strong>twee</strong> kwantoren: <strong>voor elke, \\(\\forall\\)</strong> "
                  "en <strong>er bestaat, \\(\\exists\\)</strong>. <em>Er bestaat precies één</em>, "
                  "\\(\\exists !\\), staat er niet bij. Let op het omkeren: <strong>de negatie van "
                  "\\(\\forall x: x > 0\\) is \\(\\exists x: x \\leq 0\\)</strong>, dus er bestaat een getal "
                  "dat niet positief is. Niet-voor-elke keert de kwantor om naar er-bestaat."),
        ]),
        dict(kop="De waarheidstabel opstellen", blokken=[
            ("p", "Elke extra uitspraak <strong>verdubbelt</strong> het aantal rijen, want elke uitspraak kan "
                  "waar of vals zijn."),
            ("kader", tabel(["aantal uitspraken", "aantal rijen", "rekenwijze"],
                            [["twee", "<strong>\\(4\\)</strong>", "\\(2 \\cdot 2\\)"],
                             ["drie", "<strong>\\(8\\)</strong>", "\\(2 \\cdot 2 \\cdot 2 = 2^{3}\\)"],
                             ["vier", "<strong>\\(16\\)</strong>", "\\(2^{4}\\)"]])),
            ("p", "In een tabel met twee uitspraken is <strong>\\(p \\wedge q\\) in één rij waar</strong> "
                  "(alleen als beide waar zijn), <strong>\\(p \\vee q\\) in drie rijen</strong> (overal "
                  "behalve waar beide vals zijn) en <strong>\\(p \\Rightarrow q\\) ook in drie rijen</strong> "
                  "(ze is enkel vals bij waar-dan-vals)."),
            ("fig", svg.waarheidstabel(),
             "W is waar, V is vals; links de twee uitspraken, rechts wat de bewerkingen ermee doen"),
            ("p", "Het opstellen gaat in drie stappen: <strong>alle combinaties opschrijven</strong>, "
                  "<strong>de deeluitdrukkingen uitwerken</strong> en <strong>de eindkolom bepalen</strong>. "
                  "Over waarheidstabellen klopt: <strong>ze tonen alle gevallen</strong>, <strong>ze bewijzen "
                  "een tautologie</strong> en <strong>hun aantal rijen verdubbelt per uitspraak</strong>. Ze "
                  "werken met waar en vals, of met \\(1\\) en \\(0\\) bij poorten, niet met gewone getallen."),
        ]),
        dict(kop="Logische poorten", blokken=[
            ("p", "<strong>De werking van een logische poort kan je wél in een waarheidstabel zetten</strong>, "
                  "en de vakfiche vraagt dat ook uitdrukkelijk."),
            ("fig", svg.poorten(),
             "dezelfde drie bewerkingen, maar dan als schakeling"),
            ("kader", tabel(["poort", "bij welke bewerking", "wanneer de uitgang \\(1\\) is"],
                            [["<strong>de en-poort</strong>", "de conjunctie \\(\\wedge\\)", "<strong>enkel als beide ingangen \\(1\\) zijn</strong>"],
                             ["<strong>de of-poort</strong>", "<strong>de disjunctie \\(\\vee\\)</strong>", "zodra minstens één ingang \\(1\\) is"],
                             ["<strong>de niet-poort</strong>", "de negatie \\(\\neg\\)", "<strong>ze keert het signaal om</strong>: een \\(1\\) wordt \\(0\\) en een \\(0\\) wordt \\(1\\)"]])),
            ("p", "<strong>Twee en-poorten op een rij geven \\(1\\) als alle ingangen \\(1\\) zijn</strong>, "
                  "want elke en-poort eist dat al haar ingangen \\(1\\) zijn."),
            ("p", "Zo herken je ze in het echt. <strong>Een lamp die enkel brandt als twee schakelaars samen "
                  "aan staan, is een en-poort.</strong> <strong>Een lamp die brandt als minstens één "
                  "schakelaar aan staat, is dus geen en-poort maar een of-poort.</strong> En <strong>een "
                  "schakeling met drie ingangen vraagt een tabel van acht rijen</strong>."),
        ]),
    ])


# ───────────────────────── 4. Redeneren, bewijzen en tegenvoorbeelden
zet("redeneren-bewijzen-en-tegenvoorbeelden",
    titel="Redeneren, bewijzen en tegenvoorbeelden",
    onder="Waarom voorbeelden geen bewijs zijn, hoe je met één tegenvoorbeeld weerlegt, hoe een bewijs eruitziet, en wat je op het examen mag gebruiken.",
    secties=[
        dict(kop="Voorbeeld tegenover bewijs", blokken=[
            ("p", "<strong>Voorbeelden bewijzen niets; ze maken een uitspraak enkel geloofwaardiger.</strong> "
                  "Ze geven je een idee van de correctheid, maar <strong>honderd voorbeelden vormen geen "
                  "bewijs</strong>. Wie uit twee voorbeelden besluit dat een eigenschap altijd geldt, maakt "
                  "dus een fout: <strong>misschien bestaat er een derde geval dat ze wel schendt</strong>."),
            ("p", "<strong>Een bewijs moet voor alle gevallen gelden, niet enkel voor je voorbeeld.</strong> "
                  "Daarom werk je <strong>met letters in plaats van met getallen</strong>: met a en b staat "
                  "je redenering voor elk getal, met \\(3\\) en \\(5\\) enkel voor dat ene geval."),
            ("p", "Dat loopt gelijk met de twee kwantoren. <strong>Voor elke, \\(\\forall\\),</strong> betekent dat "
                  "<strong>de uitspraak voor alle gevallen geldt</strong>, dus <strong>één tegenvoorbeeld "
                  "maakt ze vals</strong>. <strong>Er bestaat, \\(\\exists\\),</strong> betekent dat <strong>er minstens één "
                  "geval is</strong>, dus <strong>om zo'n uitspraak te bewijzen volstaat één "
                  "voorbeeld</strong>."),
            ("p", "Twee woorden keren bij elke redenering terug. Een <strong>nodige voorwaarde</strong> is "
                  "er een waarzonder het besluit niet geldt: <strong>aanwezig zijn op het examen is nodig "
                  "om te slagen</strong>, maar het is niet voldoende. Een <strong>voldoende "
                  "voorwaarde</strong> is er een waarmee het besluit zeker geldt: <strong>deelbaar zijn "
                  "door \\(4\\) is voldoende om even te zijn</strong>, maar niet nodig, want \\(6\\) is "
                  "ook even."),
        ]),
        dict(kop="Het tegenvoorbeeld", blokken=[
            ("p", "<strong>Een foutieve wiskundige uitspraak weerleg je met een tegenvoorbeeld</strong>, en "
                  "<strong>één volstaat</strong>. Maar het moet wel een tegenvoorbeeld bij díé uitspraak "
                  "zijn: <strong>een tegenvoorbeeld dat buiten de uitspraak valt, zegt niets over de "
                  "uitspraak</strong>. Een cirkel weerlegt niets over rechthoeken."),
            ("kader", tabel(["foutieve uitspraak", "tegenvoorbeeld", "waarom het werkt"],
                            [["<strong>\\(\\sqrt{a + b} = \\sqrt{a} + \\sqrt{b}\\)</strong>",
                              "<strong>\\(a = 9\\) en \\(b = 16\\)</strong>", "\\(\\sqrt{25} = 5\\), maar \\(3 + 4 = 7\\)"],
                             ["<strong>\\(a^{2} > 0\\) voor elke \\(a\\)</strong>", "<strong>\\(a = 0\\)</strong>",
                              "\\(0^{2} = 0\\), en dat is niet groter dan nul"],
                             ["<strong>\\(-a < 0\\) voor elke \\(a\\)</strong>", "\\(a = -3\\)",
                              "\\(-(-3) = 3\\), dus positief"],
                             ["<strong>delen maakt altijd kleiner</strong>", "delen door \\(\\frac{1}{2}\\)",
                              "\\(6 : \\frac{1}{2} = 12\\), dus groter"],
                             ["<strong>elke rechthoek is een vierkant</strong>", "<strong>een rechthoek van \\(2 \\times 5\\)</strong>",
                              "ongelijke zijden, dus geen vierkant"],
                             ["<strong>lengte \\(\\times 2\\) geeft oppervlakte \\(\\times 2\\)</strong>", "een vierkant van zijde \\(2\\) naar zijde \\(4\\)",
                              "de oppervlakte gaat van \\(4\\) naar \\(16\\), dus <strong>vier keer zo groot</strong>: de oppervlakte volgt het kwadraat van de factor"]])),
            ("fig", svg.schaalfactor(),
             "de zijde verdubbelt; de oppervlakte gaat van 4 naar 16, het volume van 8 naar 64"),
            ("p", "De vakfiche laat je twee soorten fouten weerleggen: <strong>rekenregels die fout worden "
                  "toegepast</strong> en <strong>uitspraken over schaalverandering</strong>, dus "
                  "<strong>allebei</strong>. Een klassieker van het eerste soort: wie schrijft dat "
                  "\\(2 + 3 \\cdot 4 = 20\\), miste <strong>de volgorde van de bewerkingen</strong> — eerst "
                  "maal, dan plus, dus \\(3 \\cdot 4 = 12\\) en daarbij \\(2\\) geeft <strong>\\(14\\)</strong>. "
                  "Met haakjes, \\((2 + 3) \\cdot 4\\), zou er wel \\(20\\) staan."),
        ]),
        dict(kop="Hoe een bewijs eruitziet", blokken=[
            ("p", "Drie stappen horen erbij: <strong>de gegevens benoemen</strong>, <strong>elke stap "
                  "verantwoorden</strong> en <strong>het besluit formuleren</strong>. Raden hoort nergens in "
                  "een bewijs. Het laatste deel heet <strong>het besluit</strong> of de conclusie; daar "
                  "herneem je wat je wou aantonen."),
            ("p", "Over bewijzen klopt dus: <strong>ze gelden voor alle gevallen</strong>, <strong>elke stap "
                  "wordt verantwoord</strong> en <strong>ze eindigen met een besluit</strong>."),
            ("p", "Verantwoorden betekent zeggen waarom een stap mag. Trek je bij \\(x + 3 = 7\\) aan beide "
                  "kanten \\(3\\) af, dan steun je op <strong>een eigenschap van gelijkheden</strong>: wat je links "
                  "doet, doe je rechts, en zo blijft de gelijkheid gelden. Wil je aantonen dat twee "
                  "driehoeken gelijkvormig zijn, dan wijs je <strong>een gelijkvormigheidskenmerk</strong> "
                  "aan: HH, ZHZ, ZZZ of het geval met een rechte hoek."),
            ("p", "De vakfiche vraagt bij een aangereikte redenering om <strong>de redeneerstappen te "
                  "beargumenteren</strong>, en <strong>redeneerstappen aan te vullen</strong> in de bewijzen "
                  "uit de lijst met bewijzen. Ze vraagt ook <strong>een bewijs te reconstrueren in een "
                  "gewijzigde situatie</strong>, en dat betekent: <strong>met andere symbolen of een andere "
                  "tekening</strong>, of voor een specifiek geval."),
        ]),
        dict(kop="Noteren, en wat mag mee op het examen", blokken=[
            ("p", "Bij een correct genoteerde redenering hoort <strong>vaktaal gebruiken</strong>, <strong>de "
                  "symbolen correct zetten</strong> en <strong>tussenstappen verklaren</strong>, met haakjes "
                  "en bewerkingstekens op de juiste plaats. Enkel het antwoord volstaat niet. <strong>Je "
                  "tussenstappen tellen mee omdat ze je redenering tonen</strong>: de fiche vraagt "
                  "uitdrukkelijk je werkwijze en redenering volledig uit te schrijven, en <strong>de correcte "
                  "notatie van begrippen en symbolen bepaalt mee je resultaat</strong>."),
            ("p", "<strong>Een berekening uitschrijven met de juiste symbolen is dus zelf al een wiskundige "
                  "redenering</strong>; de fiche noemt dat uitdrukkelijk zo. Welke symbolen ze vraagt: "
                  "<strong>\\(\\wedge\\), \\(\\vee\\), \\(\\neg\\)</strong>, <strong>\\(\\Rightarrow\\)</strong> en "
                  "<strong>\\(\\Leftrightarrow\\)</strong> voor de equivalentie, plus de twee kwantoren. Het "
                  "sommatieteken \\(\\sum\\) staat er niet bij. <strong>De dubbele pijl moet je niet "
                  "systematisch gebruiken bij het "
                  "oplossen van vergelijkingen</strong>; dat zegt de fiche zelf. Waar je de symbolen gebruikt, "
                  "moeten ze wel correct zijn."),
            ("kader", tabel(["bijlage", "mag mee op het examen"],
                            [["<strong>het formularium</strong>", "<strong>ja</strong>, als enige"],
                             ["de lijst met bewijzen", "<strong>neen</strong>"],
                             ["de lijst met begrippen en notaties", "<strong>neen</strong>"]])),
            ("weetje", "<strong>Reflectie over je oplossing hoort bij het werk</strong>, want <strong>zo "
                       "controleer je of je antwoord klopt</strong>. De vier stappen zijn: begrijp het "
                       "probleem, maak een plan, voer het uit, en reflecteer. Die vierde is volwaardig."),
        ]),
    ])


# ───────────────────────── 5. Ruimtefiguren, vlakke voorstellingen en vectoren
zet("ruimtefiguren-vlakke-voorstellingen-en-vectoren",
    titel="Ruimtefiguren, vlakke voorstellingen en vectoren",
    onder="De onderlinge ligging van rechten en vlakken, hoe je een ruimtefiguur plat tekent, en vectoren met hun richting, zin en grootte.",
    secties=[
        dict(kop="Rechten en vlakken in de ruimte", blokken=[
            ("p", "In de ruimte komt er één ligging bij die in het platte vlak niet bestaat: "
                  "<strong>kruisend</strong>. Twee rechten zijn kruisend als <strong>ze niet snijden en niet "
                  "evenwijdig lopen</strong>; ze liggen dan in geen enkel gemeenschappelijk vlak. "
                  "<strong>Twee kruisende rechten liggen dus nooit in hetzelfde vlak</strong> — was er zo'n "
                  "vlak, dan zouden ze snijden of evenwijdig zijn."),
            ("kader", tabel(["wat tegenover wat", "welke liggingen"],
                            [["<strong>twee rechten</strong>", "<strong>evenwijdig</strong>, samenvallend, <strong>snijdend</strong>, <strong>kruisend</strong> of loodrecht"],
                             ["<strong>twee vlakken</strong>", "<strong>evenwijdig</strong>, <strong>samenvallend</strong>, <strong>snijdend of loodrecht</strong>"],
                             ["<strong>een rechte en een vlak</strong>", "<strong>evenwijdig, erin, snijdend of loodrecht</strong> (loodrecht is een bijzonder geval van snijdend)"]])),
            ("fig", svg.rechteenvlak(),
             "een rechte tegenover een vlak, in de drie gevallen die de tabel noemt"),
            ("p", "<strong>Twee vlakken kunnen niet kruisend zijn</strong>: dat begrip bestaat alleen voor "
                  "rechten. Vlakken snijden, vallen samen of zijn evenwijdig."),
            ("p", "De doorsnede zegt wat ze gemeen hebben. <strong>Twee snijdende vlakken hebben een rechte "
                  "als doorsnede</strong>; <strong>twee snijdende rechten hebben een punt</strong>, en precies "
                  "één, want met meer gemeenschappelijke punten zouden ze samenvallen."),
            ("p", "De vakfiche gebruikt hierbij begrippen uit de verzamelingenleer: element, "
                  "<strong>deelverzameling</strong>, <strong>doorsnede</strong>, <strong>unie en "
                  "verschil</strong>. Een functie hoort bij een ander onderdeel."),
        ]),
        dict(kop="Ruimtefiguren plat tekenen", blokken=[
            ("p", "Een <strong>ruimtefiguur</strong> heeft <strong>hoogte, breedte én diepte</strong>; ze is "
                  "driedimensionaal. <strong>Een balk</strong>, <strong>een kegel</strong> en <strong>een "
                  "bol</strong> zijn ruimtefiguren, een vierkant niet — dat is vlak."),
            ("fig", svg.ruimtefiguren(),
             "elk van deze figuren heeft een volume"),
            ("kader", tabel(["manier", "wat ze doet"],
                            [["<strong>het cavalièreperspectief</strong>", "<strong>een manier om ruimte te tekenen</strong>: de diepte komt onder een hoek en vaak verkort op papier"],
                             ["<strong>de aanzichten</strong>", "<strong>vooraanzicht</strong>, <strong>zijaanzicht</strong> en <strong>bovenaanzicht</strong>; een binnenaanzicht bestaat niet"],
                             ["<strong>de ontwikkeling</strong>", "<strong>de figuur uitgeplooid in het vlak</strong>, zoals het bouwplan van een doos"]])),
            ("fig", svg.aanzichten(),
             "dezelfde figuur, van voor, van opzij en van boven bekeken"),
            ("p", "<strong>Men tekent drie aanzichten omdat ze samen alle maten tonen</strong>: hoogte, "
                  "breedte en diepte."),
            ("p", "Tel de onderdelen van een kubus goed uit elkaar: <strong>zes zijvlakken</strong> (en dus "
                  "zes vlakken in haar ontwikkeling), <strong>\\(12\\) ribben</strong> en <strong>\\(8\\) "
                  "hoekpunten</strong>. En pas op met te algemene uitspraken: <strong>de ribben van het "
                  "bovenvlak en die van het ondervlak zijn niet allemaal kruisend</strong> — elke ribbe boven "
                  "is evenwijdig met of kruisend met een ribbe onder."),
        ]),
        dict(kop="Vectoren", blokken=[
            ("p", "Een vector heeft <strong>drie</strong> kenmerken: <strong>richting</strong> (de stand van "
                  "de lijn), <strong>zin</strong> (de kant waarop de pijl wijst) en <strong>grootte</strong> "
                  "(de lengte). <strong>Twee vectoren zijn gelijk als die drie gelijk zijn</strong>; hun "
                  "plaats in het vlak doet niet mee, en daarom mag je een vector verschuiven."),
            ("p", "Over vectoren klopt dus: <strong>hun plaats doet niet mee</strong>, <strong>ze hebben "
                  "richting, zin en grootte</strong> en <strong>ze beschrijven een verschuiving</strong>. Dat "
                  "laatste is het verband dat de vakfiche legt: <strong>een vector beschrijft een "
                  "verschuiving of translatie</strong> — zo veel die kant op."),
            ("kader", tabel(["begrip of bewerking", "wat het betekent"],
                            [["<strong>de nulvector \\(\\vec{0}\\)</strong>", "<strong>een vector met grootte nul</strong>: begin- en eindpunt vallen samen, richting en zin zijn onbepaald"],
                             ["<strong>de tegengestelde vector \\(-\\vec{u}\\)</strong>", "<strong>dezelfde grootte, de andere zin</strong>; <strong>\\(\\vec{u} + \\left(-\\vec{u}\\right) = \\vec{0}\\)</strong>"],
                             ["<strong>\\(\\vec{u} + \\vec{v}\\)</strong>", "<strong>kop aan staart zetten</strong>; de somvector loopt van het begin van de eerste naar het einde van de tweede"],
                             ["<strong>\\(\\vec{u} - \\vec{v}\\)</strong>", "<strong>de tegengestelde erbij optellen</strong>: \\(\\vec{u} + \\left(-\\vec{v}\\right)\\), dus je keert de tweede pijl om"],
                             ["<strong>\\(3\\vec{u}\\)</strong>", "<strong>drie keer zo lang</strong>, richting en zin blijven"],
                             ["<strong>\\(-2\\vec{u}\\)</strong>", "<strong>dubbel zo lang en omgekeerd</strong> van zin"],
                             ["<strong>\\(\\frac{1}{2}\\vec{u}\\)</strong>", "<strong>de grootte wordt gehalveerd</strong>, dus korter en niet langer"]])),
            ("fig", svg.vectoroptelling(),
             "kop aan staart: de somvector loopt van het begin van de eerste naar het einde van de tweede"),
            ("p", "De vakfiche gebruikt vectoren bij <strong>krachten</strong>, <strong>verplaatsing</strong> "
                  "en <strong>snelheid</strong>. <strong>Temperatuur is geen vectorgrootheid</strong>: ze "
                  "heeft wel een grootte maar geen richting."),
            ("kader", tabel(["situatie", "uitkomst"],
                            [["<strong>twee krachten van \\(5\\) N in dezelfde zin</strong>", "<strong>\\(10\\) N</strong>: de groottes tellen op"],
                             ["<strong>twee krachten van \\(5\\) N in tegengestelde zin</strong>", "<strong>de nulvector \\(\\vec{0}\\)</strong>: ze heffen elkaar op, het voorwerp blijft in evenwicht"],
                             ["<strong>een boot vaart naar het noorden, de stroming duwt naar het oosten</strong>",
                              "<strong>tel de twee vectoren op</strong>: de somvector loopt schuin naar het noordoosten, en dat is de werkelijke koers"]])),
            ("p", "<strong>De som van twee vectoren kan dus kleiner zijn dan elk van de twee "
                  "afzonderlijk</strong>, namelijk als ze tegen elkaar in werken. Denk aan twee mensen die "
                  "elk aan een kant van een touw trekken."),
        ]),
    ])


# ───────────────────────── 6. Schaalverandering en gelijkvormige figuren
zet("schaalverandering-en-gelijkvormige-figuren",
    titel="Schaalverandering en gelijkvormige figuren",
    onder="De gelijkvormigheidsfactor en wat ze doet met lengte, oppervlakte en volume, werken met een schaal, en de vier gelijkvormigheidskenmerken van driehoeken.",
    secties=[
        dict(kop="De gelijkvormigheidsfactor", blokken=[
            ("p", "Twee figuren zijn <strong>gelijkvormig</strong> als ze <strong>dezelfde vorm hebben in een "
                  "andere grootte</strong>: alle hoeken zijn gelijk en alle zijden staan in dezelfde "
                  "verhouding. <strong>De gelijkvormigheidsfactor is de verhouding van de lengtes</strong>: "
                  "je deelt een lengte van de nieuwe figuur door de overeenkomstige lengte van de oude. "
                  "<strong>Gaat een figuur van \\(3\\) cm naar \\(12\\) cm, dan is \\(k = \\frac{12}{3} = 4\\)</strong>; "
                  "<strong>bij zijden \\(2\\) en \\(10\\) is \\(k = \\frac{10}{2} = 5\\)</strong>."),
            ("p", "<strong>Bij \\(k < 1\\) wordt de figuur kleiner</strong>: met \\(k = \\frac{1}{2}\\) "
                  "halveert elke lengte, en dan wordt de oppervlakte \\(\\frac{1}{4}\\)."),
            ("fig", svg.gelijkvormigedriehoeken(),
             "de rechtse driehoek is de linkse, maal 1,5"),
        ]),
        dict(kop="Lengte, oppervlakte en volume gaan niet gelijk op", blokken=[
            ("p", "Dit is de kern van het hoofdstuk, en meteen de klassieke misvatting. <strong>Niet alles "
                  "gaat met dezelfde factor.</strong>"),
            ("kader", tabel(["grootheid", "hoe ze meegaat", "bij \\(k = 2\\)", "bij \\(k = 3\\)"],
                            [["<strong>de lengte</strong>", "<strong>\\(\\times k\\)</strong>", "<strong>\\(\\times 2\\)</strong>", "\\(\\times 3\\)"],
                             ["<strong>de oppervlakte</strong>", "<strong>\\(\\times k^{2}\\)</strong>", "<strong>\\(\\times 4\\)</strong>", "<strong>\\(\\times 9\\)</strong>"],
                             ["<strong>het volume</strong>", "<strong>\\(\\times k^{3}\\)</strong>", "<strong>\\(\\times 8\\)</strong>", "<strong>\\(\\times 27\\)</strong>"],
                             ["<strong>de hoeken</strong>", "<strong>ze blijven gelijk</strong>", "gelijk", "gelijk"]])),
            ("fig", svg.schaalfactor(),
             "de zijde verdubbelt; de oppervlakte gaat van 4 naar 16, het volume van 8 naar 64"),
            ("p", "<strong>Bij een dubbele lengte wordt het volume dus niet dubbel zo groot maar acht keer "
                  "zo groot.</strong> Dat is precies het soort uitspraak dat de vakfiche je laat weerleggen. "
                  "<strong>Een blikje dat in alle richtingen dubbel zo groot wordt, heeft acht keer zoveel "
                  "inhoud.</strong> En <strong>een foto op dubbele breedte, met dezelfde vorm, vraagt vier "
                  "keer zoveel inkt</strong>, want de inkt volgt de oppervlakte."),
            ("p", "Reken het na op een vierkant: <strong>een vierkant met zijde \\(2\\) cm, vergroot met "
                  "\\(k = 4\\), krijgt een zijde van \\(8\\) cm en dus een oppervlakte van \\(64\\) cm²</strong>. "
                  "Of korter: \\(4^{2} \\cdot 4 = 64\\)."),
            ("p", "<strong>Gelijkvormige driehoeken hebben dus ook niet dezelfde omtrek</strong>: die gaat "
                  "gewoon met de factor mee. Alleen de hoeken blijven gelijk. En <strong>twee driehoeken met "
                  "gelijke hoeken hebben niet automatisch dezelfde oppervlakte</strong>: ze zijn "
                  "gelijkvormig, niet gelijk."),
            ("weetje", "<strong>Grote dieren hebben dikkere botten omdat hun gewicht sneller groeit dan de "
                       "doorsnede van hun botten</strong>: het gewicht gaat met de derde macht, de doorsnede "
                       "met het kwadraat. Een mooi gevolg van schaalverandering."),
        ]),
        dict(kop="Werken met een schaal", blokken=[
            ("p", "<strong>Bij een schaal hoort geen eenheid</strong>: het is een verhouding, en 1 op 50 "
                  "geldt in welke eenheid je ook meet. Je schrijft ze als \\(1 : 50\\)."),
            ("kader", tabel(["schaal", "op papier", "in het echt", "rekenwijze"],
                            [["<strong>\\(1 : 50\\)</strong>", "\\(4\\) cm", "<strong>\\(2\\) m</strong>", "\\(4 \\cdot 50 = 200\\) cm"],
                             ["<strong>\\(1 : 100\\)</strong>", "\\(3\\) cm", "<strong>\\(3\\) m</strong>", "\\(3 \\cdot 100 = 300\\) cm"],
                             ["<strong>\\(1 : 25\\,000\\)</strong>", "\\(4\\) cm", "<strong>\\(1\\) km</strong>", "\\(4 \\cdot 25\\,000 = 100\\,000\\) cm \\(= 1\\,000\\) m"]])),
        ]),
        dict(kop="De gelijkvormigheidskenmerken van driehoeken", blokken=[
            ("p", "De vakfiche noemt <strong>HH</strong>, <strong>ZHZ</strong>, <strong>ZZZ</strong> en het "
                  "geval met een rechte hoek van \\(90^{\\circ}\\). Eén gelijke scherpe hoek volstaat niet."),
            ("kader", tabel(["kenmerk", "wat je moet weten"],
                            [["<strong>HH</strong>", "<strong>twee hoeken zijn gelijk</strong>"],
                             ["<strong>ZHZ</strong>", "<strong>twee zijden in verhouding met de ingesloten hoek ertussen</strong> gelijk; <strong>de hoek moet er echt tussen liggen</strong>"],
                             ["<strong>ZZZ</strong>", "<strong>de drie zijden staan in verhouding</strong>"],
                             ["rechte hoek", "beide driehoeken hebben een hoek van \\(90^{\\circ}\\), plus nog een gegeven"]])),
            ("p", "<strong>Twee gelijke hoeken volstaan omdat de derde hoek eruit volgt</strong>: "
                  "<strong>de hoekensom van een driehoek is \\(180^{\\circ}\\)</strong>, dus hij ligt vast. Heeft "
                  "een driehoek hoeken van \\(40^{\\circ}\\) en \\(60^{\\circ}\\), dan is de derde "
                  "<strong>\\(180^{\\circ} - 40^{\\circ} - 60^{\\circ} = 80^{\\circ}\\)</strong>."),
            ("p", "<strong>Bij gelijkvormige driehoeken staan de overeenkomstige zijden in dezelfde "
                  "verhouding</strong>, en daarmee bereken je de onbekende. Drie stappen: <strong>het "
                  "kenmerk aanwijzen</strong>, <strong>de verhouding opstellen</strong> en <strong>de "
                  "onbekende berekenen</strong>. De oppervlakte heb je er niet voor nodig."),
            ("kader", tabel(["opgave", "antwoord", "rekenwijze"],
                            [["<strong>\\(k = 2\\), een zijde van \\(5\\) cm</strong>", "<strong>\\(10\\) cm</strong>", "\\(5 \\cdot 2\\)"],
                             ["<strong>zijden \\(4\\) en \\(6\\), de tweede zijde van de kleine is \\(3\\)</strong>", "<strong>\\(4{,}5\\) cm</strong>",
                              "\\(k = \\frac{6}{4} = 1{,}5\\) en \\(3 \\cdot 1{,}5 = 4{,}5\\)"],
                             ["<strong>een stok van \\(1\\) m geeft \\(1{,}5\\) m schaduw, een boom \\(12\\) m schaduw</strong>", "<strong>de boom is \\(8\\) m</strong>",
                              "\\(\\frac{12}{1{,}5} = 8\\) en \\(1 \\cdot 8 = 8\\)"],
                             ["<strong>een stok van \\(2\\) m geeft \\(3\\) m schaduw, hoeveel geeft een boom van \\(10\\) m?</strong>", "<strong>\\(15\\) m</strong>",
                              "de verhouding is \\(\\frac{3}{2} = 1{,}5\\), dus \\(10 \\cdot 1{,}5 = 15\\)"]])),
            ("fig", svg.schaduwmeting(),
             "de zonnestralen vallen evenwijdig in, dus beide driehoeken hebben dezelfde hoeken"),
            ("p", "<strong>De twee driehoeken bij een schaduwmeting zijn gelijkvormig omdat de zonnestralen "
                  "gelijk invallen</strong>: dezelfde hoek met de grond, en beide keren een rechte hoek. Dat "
                  "is het kenmerk HH."),
            ("p", "<strong>De vakfiche vraagt het kenmerk te benoemen en niet enkel te rekenen, want het "
                  "kenmerk is de verantwoording.</strong> Zonder kenmerk weet je niet waarom je die "
                  "verhouding mag opstellen."),
        ]),
    ])


# ───────────────────────── 7. Pythagoras en de goniometrische verhoudingen
zet("pythagoras-en-de-goniometrische-verhoudingen",
    titel="Pythagoras en de goniometrische verhoudingen",
    onder="De stelling van Pythagoras en haar omgekeerde, afstanden en diagonalen berekenen, en sinus, cosinus en tangens met de grondformule.",
    secties=[
        dict(kop="De stelling van Pythagoras", blokken=[
            ("p", r"In een rechthoekige driehoek met rechthoekszijden \(a\) en \(b\) en schuine zijde "
                  r"\(c\) geldt <strong>\(a^{2} + b^{2} = c^{2}\)</strong>: de twee kleine kwadraten samen "
                  r"geven het grote. Ze <strong>geldt enkel in een rechthoekige driehoek</strong>, dus niet "
                  r"in elke driehoek. <strong>De schuine zijde ligt tegenover de rechte hoek, en ze is "
                  r"altijd de langste zijde</strong>, want ze ligt tegenover de grootste hoek."),
            ("fig", svg.pythagorasvierkanten(),
             "Op elke zijde van de driehoek 3-4-5 staat het vierkant van die zijde."),
            ("kader", tabel(["gegeven", "gevraagd", "rekenwijze", "antwoord"],
                            [[r"<strong>rechthoekszijden \(3\) en \(4\)</strong>", "de schuine zijde", r"\(9 + 16 = 25\)", r"<strong>\(5\)</strong>"],
                             [r"<strong>rechthoekszijden \(6\) en \(8\)</strong>", "de schuine zijde", r"\(36 + 64 = 100\)", r"<strong>\(10\)</strong>"],
                             [r"<strong>schuine zijde \(13\), rechthoekszijde \(5\)</strong>", "de andere rechthoekszijde", r"\(169 - 25 = 144\)", r"<strong>\(12\)</strong>"]])),
        ]),
        dict(kop="De omgekeerde stelling", blokken=[
            ("p", r"Met de <strong>omgekeerde</strong> stelling toon je aan dát een driehoek rechthoekig "
                  r"is. <strong>Bij zijden \(9\), \(12\) en \(15\): \(9^{2} + 12^{2} = 225\) en "
                  r"\(15^{2} = 225\)</strong>, dus de hoek is recht. <strong>Een driehoek met zijden "
                  r"\(5\), \(6\) en \(8\) is niet rechthoekig</strong>: \(25 + 36 = 61\) en \(8^{2} = 64\), "
                  r"en dat klopt niet."),
            ("p", r"Drietallen die wél passen: <strong>\((3, 4, 5)\)</strong>, "
                  r"<strong>\((5, 12, 13)\)</strong> en <strong>\((8, 15, 17)\)</strong>. Bij "
                  r"\((2, 3, 4)\) lukt het niet, want \(4 + 9 = 13\) en niet \(16\)."),
        ]),
        dict(kop="De afstand tussen twee punten", blokken=[
            ("p", r"<strong>De afstand tussen twee punten in het vlak bereken je met Pythagoras op de "
                  r"verschillen</strong>: het verschil in \(x\) en het verschil in \(y\) zijn de "
                  r"rechthoekszijden, de afstand is de schuine zijde. De formule is "
                  r"<strong>\(\left|AB\right| = \sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}\)</strong>. "
                  r"<strong>Van \(O(0, 0)\) naar \(P(3, 4)\) is dat \(5\)</strong>, en <strong>van "
                  r"\(A(1, 1)\) naar \(B(4, 5)\) ook \(5\)</strong>, want de verschillen zijn weer \(3\) "
                  r"en \(4\)."),
            ("fig", svg.puntafstand(),
             "Van A(1, 2) naar B(4, 6): de verschillen 3 en 4 geven de afstand 5."),
        ]),
        dict(kop="Pythagoras in de ruimte", blokken=[
            ("p", r"<strong>Pythagoras werkt ook in de ruimte</strong>, bijvoorbeeld voor de "
                  r"ruimtediagonaal van een balk: je past hem twee keer toe, eerst in het grondvlak en dan "
                  r"met de hoogte erbij. <strong>De ruimtediagonaal van een kubus met ribbe \(1\) is "
                  r"\(\sqrt{3}\)</strong>: de diagonaal van het grondvlak is \(\sqrt{2}\), en "
                  r"\(2 + 1 = 3\)."),
            ("fig", svg.ruimtediagonaal(),
             "Eerst de diagonaal van het grondvlak, dan diezelfde diagonaal met de hoogte erbij."),
        ]),
        dict(kop="Problemen aanpakken", blokken=[
            ("kader", tabel(["probleem", "antwoord", "rekenwijze"],
                            [[r"<strong>een ladder van \(5\) m, de voet \(3\) m van de muur</strong>", r"<strong>\(4\) m hoog</strong>", r"\(25 - 9 = 16\)"],
                             [r"<strong>een kast van \(2\) bij \(1\) m, hoe schuin past ze</strong>", r"<strong>\(\sqrt{5} \approx 2{,}24\) m</strong>", r"\(4 + 1 = 5\)"],
                             [r"<strong>een rechthoekig veld van \(30\) bij \(40\) m</strong>", r"<strong>de diagonaal is \(50\) m</strong>", r"\(900 + 1\,600 = 2\,500\)"]])),
            ("p", r"<strong>Bij een ladder tegen een muur is de muur niet de schuine zijde</strong>: de "
                  r"muur en de grond vormen juist de rechte hoek, en de ladder ligt daar tegenover."),
            ("p", r"Drie stappen helpen: <strong>een schets maken</strong>, <strong>de rechte hoek "
                  r"aanwijzen</strong> en <strong>de schuine zijde benoemen</strong>. Meten hoeft niet, je "
                  r"rekent. <strong>Je maakt eerst een schets omdat je dan ziet welke zijde de schuine "
                  r"is</strong>; zonder schets verwissel je die gemakkelijk met een rechthoekszijde."),
        ]),
        dict(kop="Sinus, cosinus en tangens", blokken=[
            ("fig", svg.goniodriehoek(),
             "Vanuit de hoek alfa gezien heet elke zijde anders."),
            ("kader", tabel(["getal", "welke zijden", "bij de driehoek 3-4-5"],
                            [[r"<strong>\(\sin \alpha\)</strong>", r"<strong>\(\frac{\text{overstaande}}{\text{schuine}}\)</strong>", r"<strong>\(\frac{3}{5} = 0{,}6\)</strong>"],
                             [r"<strong>\(\cos \alpha\)</strong>", r"<strong>\(\frac{\text{aanliggende}}{\text{schuine}}\)</strong>", r"<strong>\(\frac{4}{5} = 0{,}8\)</strong>"],
                             [r"<strong>\(\tan \alpha\)</strong>", r"<strong>\(\frac{\text{overstaande}}{\text{aanliggende}}\)</strong>; <strong>ze gebruikt de schuine zijde niet</strong>", r"<strong>\(\frac{3}{4} = 0{,}75\)</strong>"]])),
            ("p", r"Over die drie klopt: <strong>\(\tan \alpha\) mist de schuine zijde</strong>, "
                  r"<strong>\(\sin \alpha\) gebruikt de overstaande zijde</strong> en "
                  r"<strong>\(\cos \alpha\) gebruikt de aanliggende zijde</strong>."),
        ]),
        dict(kop="De grondformule", blokken=[
            ("p", r"<strong>Voor een scherpe hoek is \(\sin \alpha < 1\)</strong>, want de overstaande "
                  r"zijde is korter dan de schuine. Om dezelfde reden <strong>kan \(\cos \alpha\) nooit "
                  r"groter zijn dan \(1\)</strong>."),
            ("p", r"<strong>De grondformule van de goniometrie is "
                  r"\(\sin^{2}\alpha + \cos^{2}\alpha = 1\).</strong> Ze staat <strong>niet los van "
                  r"Pythagoras maar volgt er juist uit</strong>: deel bij \(a^{2} + b^{2} = c^{2}\) alles "
                  r"door \(c^{2}\). <strong>Voor dezelfde hoek is die som dus altijd \(1\).</strong> Ken je "
                  r"de sinus, dan ken je ook de cosinus: <strong>is \(\sin \alpha = 0{,}6\), dan is "
                  r"\(\cos \alpha = 0{,}8\)</strong> bij een scherpe hoek, want \(1 - 0{,}36 = 0{,}64\) en "
                  r"\(\sqrt{0{,}64} = 0{,}8\)."),
        ]),
        dict(kop="Een rechthoekige driehoek oplossen", blokken=[
            ("p", r"Drie stappen: <strong>de gegeven zijden benoemen</strong>, <strong>het juiste "
                  r"goniometrische getal kiezen</strong> en <strong>de onbekende berekenen met "
                  r"ICT</strong>. De vakfiche laat je de goniometrische getallen met ICT opzoeken; de "
                  r"oppervlakte heb je er niet voor nodig."),
            ("kader", tabel(["je kent", "je zoekt", "welk getal"],
                            [[r"<strong>de hoek en de aanliggende zijde</strong>", "de overstaande zijde", r"<strong>\(\tan \alpha\)</strong>"],
                             [r"<strong>de hoek en de schuine zijde</strong>", "de overstaande zijde", r"<strong>\(\sin \alpha\)</strong>: \(\text{overstaande} = \sin \alpha \cdot \text{schuine}\)"],
                             [r"<strong>een bergpad van \(200\) m onder \(30^{\circ}\)</strong>", "het hoogteverschil", r"<strong>\(\sin \alpha\)</strong>: het pad is de schuine zijde, \(\sin 30^{\circ} = \frac{1}{2}\), dus \(100\) m"]])),
        ]),
        dict(kop="Meten met een hoek", blokken=[
            ("p", r"<strong>Met \(\tan \alpha\) bereken je de hoogte van een boom uit de kijkhoek en de "
                  r"afstand</strong>; de vakfiche noemt dat voorbeeld zelf. <strong>Sta je \(20\) m van "
                  r"een boom en kijk je onder \(45^{\circ}\) naar de top, dan is de boom ongeveer \(20\) m "
                  r"hoog</strong>, want <strong>\(\tan 45^{\circ} = 1\)</strong>. Je ooghoogte komt er nog "
                  r"bij."),
            ("p", r"Bij \(45^{\circ}\) klopt trouwens alles tegelijk: <strong>\(\tan 45^{\circ} = 1\)"
                  r"</strong>, <strong>de twee rechthoekszijden zijn even lang</strong> en "
                  r"<strong>\(\sin 45^{\circ} = \cos 45^{\circ}\)</strong>. De schuine zijde blijft wel de "
                  r"langste."),
        ]),
    ])


# ───────────────────────── 8. Formules omvormen
zet("formules-omvormen",
    titel="Formules omvormen",
    onder="De eigenschappen van gelijkheden, een letter vrijmaken in de omgekeerde orde, en formules uit de wiskunde en de natuurwetenschappen omvormen.",
    secties=[
        dict(kop="Wat mag je met een gelijkheid doen", blokken=[
            ("p", r"Eén regel draagt het hele hoofdstuk: <strong>doe aan beide kanten "
                  r"hetzelfde</strong>. Optellen, aftrekken, vermenigvuldigen of delen aan beide kanten "
                  r"houdt de gelijkheid in stand; één kant veranderen breekt ze."),
            ("fig", svg.gelijkheidbalans(),
             "Links en rechts blijven gelijk zolang je aan beide kanten hetzelfde doet."),
            ("p", r"Met één voorbehoud: <strong>de deler mag geen \(0\) zijn</strong>. <strong>Door "
                  r"\(0\) mag je nooit delen</strong>, dus bij een letter ga je altijd na of ze nul kan "
                  r"worden."),
        ]),
        dict(kop="Een letter vrijmaken", blokken=[
            ("p", r"<strong>Een letter vrijmaken en een formule omvormen zijn hetzelfde</strong>: je zet "
                  r"die letter alleen aan één kant van het \(=\)-teken. <strong>De betekenis van de "
                  r"formule verandert daarbij niet</strong>; je schrijft dezelfde samenhang anders op."),
            ("p", r"<strong>Je maakt een formule vrij in de omgekeerde orde van de bewerkingen</strong>: "
                  r"wat het laatst bij de onbekende kwam, haal je eerst weg, net als bij het uitpakken "
                  r"van een doos."),
        ]),
        dict(kop="Uitpakken in drie stappen", blokken=[
            ("fig", svg.lettervrijmaken(),
             "Eerst gaat de + 6 weg, dan pas de maal 3."),
            ("p", r"Let nog op één ding: <strong>bij \(\cdot (-1)\) keert er in een gelijkheid geen teken "
                  r"om</strong>, want er is geen ongelijkheidsteken. Bij een ongelijkheid gebeurt dat wel."),
        ]),
        dict(kop="Formules uit de wiskunde", blokken=[
            ("p", r"De vakfiche noemt als wiskundige voorbeelden <strong>\(y = ax + b\)</strong>, "
                  r"<strong>\(y = ax^{2} + bx + c\)</strong> en <strong>de formules voor omtrek en "
                  r"oppervlakte</strong>. \(U = I \cdot R\) staat bij de natuurwetenschappen."),
            ("kader", tabel(["formule", "gevraagd", "omgevormd"],
                            [[r"omtrek rechthoek: \(P = 2l + 2b\)", r"\(l\)", r"<strong>\(l = \frac{P}{2} - b\)</strong>"],
                             [r"oppervlakte rechthoek: \(A = l \cdot b\)", r"\(b\)", r"<strong>\(b = \frac{A}{l}\)</strong>"],
                             [r"oppervlakte vierkant: \(A = z^{2}\)", r"de zijde \(z\)", r"<strong>\(z = \sqrt{A}\)</strong>, de vierkantswortel"],
                             [r"oppervlakte driehoek: \(A = \frac{b \cdot h}{2}\)", r"\(h\)", r"<strong>\(h = \frac{2A}{b}\)</strong>"],
                             [r"omtrek cirkel: \(P = 2\pi r\)", r"de straal \(r\)", r"<strong>\(r = \frac{P}{2\pi}\)</strong>"],
                             [r"\(y = a \cdot x\)", r"\(a\)", r"<strong>\(a = \frac{y}{x}\)</strong>, mits \(x \neq 0\)"]])),
        ]),
        dict(kop="Twee gevallen nagerekend", blokken=[
            ("p", r"<strong>Een driehoek met \(A = 12\) en \(b = 6\) heeft \(h = 4\)</strong>, want "
                  r"\(h = \frac{2 \cdot 12}{6} = 4\). En <strong>een vierkant met \(A = 49\) heeft "
                  r"\(z = 7\)</strong>, want \(\sqrt{49} = 7\)."),
            ("p", r"<strong>Bij een formule met \(x^{2}\) krijg je twee oplossingen</strong>: "
                  r"\(x = \sqrt{a}\) of \(x = -\sqrt{a}\). <strong>Bij een lengte houd je enkel de "
                  r"positieve, want een lengte is nooit negatief.</strong> De wiskunde geeft twee "
                  r"antwoorden, de context sluit er één uit; dat heet demathematiseren."),
        ]),
        dict(kop="Formules uit de natuurwetenschappen", blokken=[
            ("p", r"De vakfiche noemt <strong>\(\rho = \frac{m}{V}\)</strong>, <strong>\(U = I \cdot "
                  r"R\)</strong>, en <strong>\(F = k \cdot x\) en \(p = \frac{F}{A}\)</strong>. "
                  r"\(a^{2} + b^{2} = c^{2}\) is wiskunde en geen natuurwetenschappelijke formule."),
            ("kader", tabel(["formule", "gevraagd", "omgevormd", "voorbeeld"],
                            [[r"massadichtheid: \(\rho = \frac{m}{V}\)", r"\(m\)", r"<strong>\(m = \rho \cdot V\)</strong>",
                              r"<strong>\(20\) g in \(4\) cm³ geeft \(5\) g/cm³</strong>"],
                             [r"dezelfde formule", r"\(V\)", r"<strong>\(V = \frac{m}{\rho}\)</strong>", ""],
                             [r"<strong>de wet van Ohm: \(U = I \cdot R\)</strong>", r"de weerstand \(R\)", r"<strong>\(R = \frac{U}{I}\)</strong>",
                              r"<strong>\(12\) V bij \(3\) A geeft \(4\) ohm</strong>"],
                             [r"zwaartekracht: \(F_{z} = m \cdot g\)", r"\(m\)", r"<strong>\(m = \frac{F_{z}}{g}\)</strong>", ""],
                             [r"veerkracht: \(F = k \cdot x\)", r"de uitrekking \(x\)", r"<strong>\(x = \frac{F}{k}\)</strong>", ""],
                             [r"molaire concentratie: \(c = \frac{n}{V}\)", r"\(n\)", r"<strong>\(n = c \cdot V\)</strong>",
                              r"<strong>\(2\) mol/l in \(3\) l is \(6\) mol</strong>"],
                             [r"vermogen: \(P = \frac{E}{t}\)", r"\(E\)", r"<strong>\(E = P \cdot t\)</strong>",
                              r"<strong>\(100\) W gedurende \(20\) s is \(2\,000\) joule</strong>"]])),
        ]),
        dict(kop="Wat de formule je vertelt", blokken=[
            ("p", r"<strong>Druk is \(p = \frac{F}{A}\)</strong>, dus <strong>bij een kleinere \(A\) "
                  r"wordt \(p\) groter</strong>. Daarom prikt een speld zo goed. En omgekeerd: "
                  r"<strong>bij dezelfde \(F\) geeft een grotere \(A\) minder druk</strong>, en daarom "
                  r"zakken brede sneeuwschoenen minder weg."),
            ("p", r"<strong>In \(E_{k} = \frac{1}{2}mv^{2}\) staat de snelheid in het kwadraat</strong>, "
                  r"dus <strong>een auto die dubbel zo snel rijdt heeft vier keer zoveel kinetische "
                  r"energie</strong>, en daarom een veel langere remweg. Let op bij "
                  r"\(E_{p} = m \cdot g \cdot h\): <strong>die hangt niet van de hoogte alleen af</strong>, "
                  r"maar van massa, valversnelling én hoogte samen."),
            ("p", r"Drie stappen bij het omvormen: <strong>bepaal welke letter je zoekt</strong>, "
                  r"<strong>werk met eigenschappen van gelijkheden</strong> en <strong>controleer de "
                  r"eenheden</strong>. Snel afronden is net wat de vakfiche afraadt."),
            ("weetje", r"<strong>Formules omvormen is buiten de wiskunde nuttig omdat je er elke "
                       r"grootheid mee berekent</strong> die erin staat, zolang je de andere kent. Eén "
                       r"formule, zoveel vragen als er letters in staan."),
        ]),
    ])


# ───────────────────────── 9. Eerstegraadsvergelijkingen en -ongelijkheden
zet("eerstegraadsvergelijkingen-en-ongelijkheden",
    titel="Eerstegraadsvergelijkingen en -ongelijkheden",
    onder="Vergelijkingen oplossen en het aantal oplossingen herkennen, ongelijkheden met de omkeerregel, en de grafische betekenis van positief en negatief.",
    secties=[
        dict(kop="Een eerstegraadsvergelijking oplossen", blokken=[
            ("p", r"In een <strong>eerstegraadsvergelijking in één onbekende staat de onbekende in de "
                  r"eerste macht</strong>: \(ax + b = 0\), één letter, zonder kwadraat of hogere macht. "
                  r"Haar grafiek is een rechte."),
            ("p", r"Oplossen steunt op één eigenschap: <strong>aan beide kanten mag je hetzelfde "
                  r"doen</strong>. <strong>Aan beide kanten \(+ 5\)</strong>, <strong>aan beide kanten "
                  r"aftrekken</strong>, <strong>\(\cdot 3\)</strong> of <strong>\(: 2\)</strong>, altijd "
                  r"aan beide kanten tegelijk, want één kant veranderen breekt de gelijkheid."),
            ("p", r"De stappen: <strong>haakjes uitwerken</strong>, <strong>de onbekenden "
                  r"samenbrengen</strong> en <strong>delen door de coëfficiënt</strong>. Een grafiek hoeft "
                  r"niet voor een algebraïsche oplossing, al helpt ze bij de controle."),
            ("kader", tabel(["vergelijking", "tussenstap", "oplossing"],
                            [[r"<strong>\(3x + 5 = 20\)</strong>", r"\(3x = 15\), dan \(: 3\)", r"<strong>\(x = 5\)</strong>"],
                             [r"<strong>\(2x - 4 = 10\)</strong>", r"\(2x = 14\), dan \(: 2\)", r"<strong>\(x = 7\)</strong>"],
                             [r"<strong>\(5x = 2x + 12\)</strong>", r"\(2x\) naar links: \(3x = 12\)", r"<strong>\(x = 4\)</strong>"],
                             [r"<strong>\(4(x - 1) = 12\)</strong>", r"\(4x - 4 = 12\), dus \(4x = 16\)", r"<strong>\(x = 4\)</strong>"]])),
        ]),
        dict(kop="De oplossing opschrijven", blokken=[
            ("p", r"<strong>Je noteert de oplossing als een oplossingenverzameling</strong>, bijvoorbeeld "
                  r"\(V = \{5\}\): bij een vergelijking een verzameling met één of enkele getallen. Een "
                  r"interval hoort bij een ongelijkheid."),
            ("p", r"<strong>Controleer je oplossing in de oorspronkelijke vergelijking, want zo vind je "
                  r"rekenfouten</strong>: vul je antwoord in, en komen links en rechts hetzelfde uit, dan "
                  r"klopt het. Dat is de reflectiestap."),
        ]),
        dict(kop="Niet altijd één oplossing", blokken=[
            ("p", r"<strong>Een eerstegraadsvergelijking heeft niet altijd precies één oplossing.</strong>"),
            ("kader", tabel(["vergelijking", "wat eruit komt", "oplossingenverzameling"],
                            [[r"<strong>\(x = x + 1\)</strong>", r"\(0 = 1\), en dat is vals", r"<strong>\(V = \emptyset\)</strong>"],
                             [r"<strong>\(x = x + 5\)</strong>", r"\(0 = 5\)", r"<strong>geen enkele oplossing</strong>"],
                             [r"<strong>\(2x + 2 = 2(x + 1)\)</strong>", r"links en rechts hetzelfde", r"<strong>\(V = \mathbb{R}\)</strong>"]])),
            ("p", r"<strong>De oplossing van \(f(x) = 0\) is de nulwaarde van \(f\).</strong> Dat verband "
                  r"staat op de vakfiche; grafisch is het het snijpunt met de \(x\)-as."),
        ]),
        dict(kop="Vraagstukken vertalen", blokken=[
            ("p", r"<strong>Een vraagstuk naar een vergelijking vertalen hoort wél bij de "
                  r"leerstof</strong>; de vakfiche vraagt het uitdrukkelijk."),
            ("kader", tabel(["vraagstuk", "de vergelijking", "antwoord"],
                            [[r"<strong>een getal plus zijn dubbele is \(21\)</strong>", r"<strong>\(x + 2x = 21\)</strong>", r"\(x = 7\)"],
                             [r"<strong>drie opeenvolgende getallen met som \(24\)</strong>", r"\((x-1) + x + (x+1) = 3x = 24\)", r"<strong>het middelste is \(8\)</strong>"],
                             [r"<strong>twee getallen schelen \(6\), hun som is \(20\)</strong>", r"\(x + (x + 6) = 20\)", r"<strong>het kleinste is \(7\)</strong>, het andere \(13\)"],
                             [r"<strong>een abonnement van \(20\) euro plus \(3\) euro per uur, wanneer kost het \(50\) euro?</strong>", r"\(20 + 3x = 50\)", r"<strong>na \(10\) uur</strong>"]])),
        ]),
        dict(kop="Ongelijkheden en de omkeerregel", blokken=[
            ("p", r"Bijna alles blijft hetzelfde, op één regel na: <strong>deel of vermenigvuldig je met "
                  r"een negatief getal, dan keert het ongelijkheidsteken om</strong>. Dat is de klassieke "
                  r"valkuil. <strong>Bij optellen aan beide kanten blijft het teken gewoon staan.</strong>"),
            ("kader", tabel(["ongelijkheid", "wat je doet", "oplossing"],
                            [[r"<strong>\(2x > 10\)</strong>", r"\(: 2\), positief, teken blijft", r"<strong>\(x > 5\)</strong>"],
                             [r"<strong>\(x + 4 > 9\)</strong>", r"\(4\) aftrekken", r"<strong>\(x > 5\)</strong>, de \(5\) zelf hoort er niet bij"],
                             [r"<strong>\(3x - 2 < 7\)</strong>", r"\(3x < 9\), dan \(: 3\)", r"<strong>\(x < 3\)</strong>"],
                             [r"<strong>\(-3x > 9\)</strong>", r"\(: (-3)\), <strong>teken omkeren</strong>", r"<strong>\(x < -3\)</strong>"],
                             [r"<strong>\(-x > -4\)</strong>", r"\(\cdot (-1)\), <strong>teken omkeren</strong>", r"<strong>\(x < 4\)</strong>"]])),
        ]),
        dict(kop="De valkuil en de controle", blokken=[
            ("p", r"<strong>Je mag dus niet zonder nadenken met \(-1\) vermenigvuldigen</strong>: vergeet "
                  r"je het teken om te keren, dan krijg je precies de verkeerde helft van de getallenas. "
                  r"<strong>Controleer daarom één getal uit je oplossing</strong>: klopt de ongelijkheid, "
                  r"dan koos je de juiste kant."),
            ("p", r"De stappen: <strong>de onbekende vrijmaken</strong>, <strong>het teken omkeren bij een "
                  r"negatieve deler</strong> en <strong>de oplossing als interval noteren</strong>. Een top "
                  r"hoort bij een parabool, niet hier."),
        ]),
        dict(kop="De oplossing als interval", blokken=[
            ("p", r"<strong>De oplossing van \(x \geq 2\) is \(\left[2, +\infty\right[\)</strong>, want het "
                  r"\(=\)-teken zit erin en het haakje staat naar binnen. Bij <strong>\(x < 3\)</strong> "
                  r"zijn <strong>\(2\)</strong>, <strong>\(0\)</strong> en <strong>\(-5\)</strong> "
                  r"oplossingen, maar \(3\) zelf niet: het teken is strikt, dus vanaf die grens telt het getal zelf niet mee. <strong>Een oplossing van een ongelijkheid bestaat "
                  r"meestal uit oneindig veel getallen</strong>, en daarom noteer je ze als interval en "
                  r"niet als lijst."),
            ("fig", svg.intervallen(),
             "Een vol bolletje telt de grens mee, een open bolletje niet."),
            ("p", r"<strong>Op een getallenas kan je de oplossing ook voorstellen</strong>, met open of "
                  r"volle bolletjes aan de grens; de vakfiche vraagt dat. Een voorbeeld uit het leven: "
                  r"<strong>een taxi kost \(5\) euro plus \(2\) euro per kilometer en je hebt \(25\) "
                  r"euro</strong>, dus \(5 + 2x \leq 25\), \(2x \leq 20\) en je kan <strong>ten hoogste "
                  r"\(10\) km</strong>."),
        ]),
        dict(kop="Grafisch lezen", blokken=[
            ("p", r"<strong>Een vergelijking los je grafisch op door het snijpunt van de grafieken te "
                  r"zoeken</strong>: de \(x\) van dat punt is de oplossing. Bij \(f(x) = 0\) is dat het "
                  r"snijpunt met de \(x\)-as."),
        ]),
        dict(kop="Boven of onder de as", blokken=[
            ("fig", svg.tekenverloop(),
             "Een stijgende rechte met nulwaarde 4: links ligt ze onder de as, rechts erboven."),
            ("p", r"<strong>\(f(x) > 0\) betekent dat de grafiek boven de \(x\)-as ligt</strong>, daar "
                  r"is de functie positief, en <strong>\(f(x) < 0\) dat ze eronder ligt</strong>, daar is "
                  r"de functie negatief. <strong>Een stijgende rechte die de \(x\)-as snijdt in \(4\), is "
                  r"positief voor \(x > 4\).</strong> <strong>Bij een dalende rechte is het net "
                  r"omgekeerd</strong>: ze komt van boven en duikt na haar nulpunt onder de as, dus links "
                  r"is de functie positief."),
        ]),
    ])


# ───────────────────────── 10. Stelsels van twee vergelijkingen
zet("stelsels-van-twee-vergelijkingen",
    titel="Stelsels van twee vergelijkingen",
    onder="De drie oplossingsmethodes, de drie soorten stelsels met hun grafische betekenis, en vraagstukken met twee onbekenden.",
    secties=[
        dict(kop="Wat een stelsel is", blokken=[
            ("p", r"Een stelsel zijn <strong>twee vergelijkingen die samen gelden</strong>: je zoekt de "
                  r"waarden die aan beide tegelijk voldoen. Je schrijft het met een accolade: "
                  r"\[\begin{cases} x + y = 10 \\ x - y = 2 \end{cases}\]"),
            ("p", r"<strong>De oplossing noteer je niet als één getal maar als een koppel</strong> "
                  r"\((x, y)\), eerst de \(x\) en dan de \(y\); de vakfiche noemt dat de "
                  r"koppelvoorstelling. Hier is dat \((6, 4)\), en de oplossingenverzameling is "
                  r"\(V = \{(6, 4)\}\)."),
        ]),
        dict(kop="De drie methodes", blokken=[
            ("p", r"De vakfiche noemt <strong>drie</strong> algebraïsche methodes. De discriminant hoort "
                  r"bij de tweedegraadsvergelijkingen en niet hier."),
            ("kader", tabel(["methode", "wat je doet", "voorbeeld"],
                            [[r"<strong>de combinatiemethode</strong>", r"<strong>optellen of aftrekken</strong>, zodat <strong>één onbekende wegvalt</strong>",
                              r"<strong>\(x + y = 10\) en \(x - y = 2\)</strong>: optellen geeft \(2x = 12\), dus <strong>\((6, 4)\)</strong>"],
                             [r"<strong>de substitutiemethode</strong>", r"<strong>een onbekende vervangen door een uitdrukking</strong>",
                              r"<strong>\(y = 2x\) en \(x + y = 9\)</strong>: \(3x = 9\), dus <strong>\((3, 6)\)</strong>"],
                             [r"<strong>de gelijkstellingsmethode</strong>", r"beide keren staat dezelfde letter alleen, dus stel je de rechterleden gelijk",
                              r"<strong>\(y = 3x - 1\) en \(y = x + 5\)</strong>: \(2x = 6\), dus <strong>\((3, 8)\)</strong>"]])),
        ]),
        dict(kop="Zelf narekenen", blokken=[
            ("p", r"Nog drie om zelf na te rekenen. <strong>\(x + y = 12\) en \(x - y = 4\) geeft "
                  r"\(x = 8\)</strong> (en \(y = 4\)). <strong>\(2x + y = 11\) met \(y = 3\) geeft "
                  r"\(x = 4\).</strong> <strong>\(3x + y = 17\) met \(y = 2\) geeft \(x = 5\).</strong>"),
            ("p", r"<strong>Controleer je oplossing in beide vergelijkingen</strong>, want ze moet aan "
                  r"allebei voldoen: een koppel dat maar aan één vergelijking voldoet, is geen oplossing "
                  r"van het stelsel."),
        ]),
        dict(kop="Drie soorten stelsels", blokken=[
            ("fig", svg.driestelsels(),
             "Snijden de rechten elkaar, lopen ze naast elkaar, of liggen ze op elkaar?"),
            ("kader", tabel(["soort", "hoeveel oplossingen", "grafisch", "voorbeeld"],
                            [[r"<strong>bepaald</strong>", r"<strong>precies één</strong>", r"<strong>twee snijdende rechten</strong>, dus een <strong>verschillende \(a\)</strong>",
                              r"\(x + y = 10\) en \(x - y = 2\)"],
                             [r"<strong>strijdig</strong>", r"<strong>geen enkele</strong>; <strong>\(V = \emptyset\)</strong>",
                              r"<strong>twee evenwijdige rechten</strong> die niet samenvallen: <strong>nul snijpunten</strong>",
                              r"<strong>\(x + y = 5\) en \(x + y = 7\)</strong>: dezelfde som kan niet \(5\) én \(7\) zijn"],
                             [r"<strong>onbepaald</strong>", r"<strong>oneindig veel</strong>", r"<strong>twee samenvallende rechten</strong>: dezelfde \(a\) én dezelfde \(b\)",
                              r"<strong>\(x + y = 5\) en \(2x + 2y = 10\)</strong>: de tweede is het dubbele van de eerste"]])),
        ]),
        dict(kop="Het soort herkennen", blokken=[
            ("p", r"<strong>Een stelsel met precies één oplossing heet dus bepaald, niet "
                  r"strijdig</strong>; strijdig betekent juist dat er géén oplossing is. <strong>Twee "
                  r"rechten met dezelfde richtingscoëfficiënt \(a\) zijn evenwijdig</strong>: verschilt ook "
                  r"hun \(b\), het snijpunt met de \(y\)-as, dan vallen ze niet samen en is het stelsel "
                  r"strijdig."),
            ("p", r"Over stelsels kloppen deze uitspraken: <strong>ze kunnen geen oplossing "
                  r"hebben</strong>, <strong>ze "
                  r"kunnen er oneindig veel hebben</strong> en <strong>ze kunnen er precies één "
                  r"hebben</strong>. Precies twee oplossingen bestaat niet bij een stelsel van "
                  r"eerstegraadsvergelijkingen."),
            ("p", r"<strong>Het soort stelsel benoemen is nuttig omdat je dan weet wat je antwoord "
                  r"betekent</strong>: komt er \(0 = 5\) uit, dan is het stelsel strijdig en is dát je "
                  r"antwoord, geen rekenfout."),
        ]),
        dict(kop="Grafisch oplossen", blokken=[
            ("p", r"<strong>Grafisch is de oplossing het snijpunt van twee rechten</strong>: het punt dat "
                  r"op beide ligt, voldoet aan beide vergelijkingen. Op de grafiek zie je ook meteen "
                  r"welk soort stelsel je hebt. <strong>Grafisch oplossen mag met "
                  r"ICT</strong>; de vakfiche vraagt zelfs uitdrukkelijk om stelsels grafisch op te "
                  r"lossen, met en zonder ICT."),
            ("p", r"Maar <strong>grafisch oplossen is niet even nauwkeurig als algebraïsch "
                  r"oplossen</strong>: een snijpunt lees je af, en dat is zelden exact. Algebraïsch krijg "
                  r"je de precieze waarden."),
        ]),
        dict(kop="Vraagstukken met twee onbekenden", blokken=[
            ("p", r"<strong>Een vraagstuk met twee onbekenden los je niet op met één "
                  r"vergelijking</strong>: dan blijft het onbepaald. Je hebt evenveel vergelijkingen als "
                  r"onbekenden nodig."),
            ("p", r"De stappen: <strong>twee onbekenden benoemen</strong>, <strong>twee vergelijkingen "
                  r"opstellen</strong> en <strong>het stelsel oplossen</strong>. De vakfiche vraagt daarna "
                  r"het antwoord terug in de context te plaatsen."),
            ("kader", tabel(["vraagstuk", "het stelsel", "antwoord"],
                            [[r"<strong>twee getallen met som \(20\) en verschil \(4\)</strong>", r"\(x + y = 20\) en \(x - y = 4\)",
                              r"<strong>het grootste is \(12\)</strong>"],
                             [r"<strong>twaalf stukken fruit, \(4\) peren meer dan appels</strong>", r"\(a + p = 12\) en \(p = a + 4\)",
                              r"<strong>\(4\) appels</strong> (en \(8\) peren)"],
                             [r"<strong>abonnement A: \(20\) euro plus \(2\) per uur; abonnement B: \(10\) euro plus \(4\) per uur</strong>", r"\(20 + 2x = 10 + 4x\)",
                              r"<strong>na \(5\) uur kosten ze evenveel</strong>"],
                             [r"<strong>een kaars van \(20\) cm die \(2\) cm per uur brandt, en een van \(14\) cm die \(1\) cm per uur brandt</strong>", r"\(20 - 2x = 14 - x\)",
                              r"<strong>na \(6\) uur</strong>, beide zijn dan \(8\) centimeter"]])),
            ("p", r"Bij de abonnementen zegt het snijpunt waar de omslag ligt: <strong>bij veel uren is "
                  r"dat met het laagste uurtarief het voordeligst</strong>, want dan weegt het uurtarief "
                  r"het zwaarst."),
        ]),
    ])


# ───────────────────────── 11. Tweedegraadsvergelijkingen
zet("tweedegraadsvergelijkingen",
    titel="Tweedegraadsvergelijkingen",
    onder="De merkwaardige producten, ontbinden in factoren, de discriminant en wat ze zegt, en vraagstukken van de tweede graad.",
    secties=[
        dict(kop="De merkwaardige producten", blokken=[
            ("p", r"Er zijn er <strong>drie</strong>, en je moet ze in beide richtingen kunnen lezen: "
                  r"van product naar som om uit te werken, en van som naar product om te ontbinden."),
            ("kader", tabel(["product", "uitgewerkt", "voorbeeld"],
                            [[r"<strong>\((a + b)^{2}\)</strong>", r"<strong>\(a^{2} + 2ab + b^{2}\)</strong>",
                              r"<strong>\(x^{2} + 2x + 1 = (x + 1)^{2}\)</strong>"],
                             [r"<strong>\((a - b)^{2}\)</strong>", r"\(a^{2} - 2ab + b^{2}\); <strong>het dubbele product is hier negatief</strong>",
                              r"<strong>\((x - 4)^{2} = x^{2} - 8x + 16\)</strong>"],
                             [r"<strong>\((a + b)(a - b)\)</strong>", r"<strong>\(a^{2} - b^{2}\)</strong>: de twee middelste termen vallen weg",
                              r"<strong>\(x^{2} - 25 = (x - 5)(x + 5)\)</strong>"]])),
            ("p", r"Let dus op het teken: <strong>bij \((a - b)^{2}\) is het dubbele product niet "
                  r"positief</strong> maar negatief; het volgt het teken in de tweeterm."),
        ]),
        dict(kop="Waarom dat middelste stuk twee keer telt", blokken=[
            ("fig", svg.merkwaardigvierkant(),
             "Een vierkant met zijde a + b valt uiteen in vier stukken."),
            ("p", r"De twee rechthoeken zijn even groot, elk \(ab\), en samen geven ze het dubbele "
                  r"product \(2ab\). Daarom is \((a + b)^{2}\) niet gewoon \(a^{2} + b^{2}\)."),
        ]),
        dict(kop="Ontbinden in factoren", blokken=[
            ("p", r"<strong>Ontbinden in factoren betekent een som als een product schrijven.</strong> "
                  r"Dat is handig omdat <strong>een product nul is zodra één factor nul is</strong>, en "
                  r"<strong>elke factor dus een oplossing geeft</strong>."),
            ("p", r"De stappen, in deze orde: <strong>eerst een gemeenschappelijke factor "
                  r"zoeken</strong>, dan <strong>een merkwaardig product herkennen</strong>, dan "
                  r"<strong>twee getallen zoeken met de juiste som en het juiste product</strong>. "
                  r"Letters vervangen door getallen is geen ontbinding."),
            ("kader", tabel(["veelterm", "ontbonden", "hoe je erop komt"],
                            [[r"<strong>\(6x^{2} + 9x\)</strong>", r"<strong>\(3x\)</strong>\((2x + 3)\)", r"\(3x\) staat in beide termen"],
                             [r"<strong>\(3x^{2} + 6x\)</strong>", r"<strong>\(3x(x + 2)\)</strong>", r"controle: \(3x \cdot x = 3x^{2}\) en \(3x \cdot 2 = 6x\)"],
                             [r"<strong>\(2x^{2} + 6x\)</strong>", r"<strong>\(2x(x + 3)\)</strong>", r"de oplossingen zijn dan <strong>\(0\) en \(-3\)</strong>"],
                             [r"<strong>\(x^{2} + 5x + 6\)</strong>", r"<strong>\((x + 2)(x + 3)\)</strong>", r"twee getallen met <strong>som \(5\)</strong> en product \(6\)"],
                             [r"<strong>\(x^{2} - 7x + 12\)</strong>", r"\((x - 3)(x - 4)\)", r"<strong>som \(-7\)</strong> en product \(12\)"],
                             [r"<strong>\(x^{2} - 2x - 8\)</strong>", r"<strong>\((x - 4)(x + 2)\)</strong>", r"som \(-2\) en product \(-8\)"]])),
            ("p", r"<strong>Niet elke veelterm van de tweede graad is te ontbinden in reële "
                  r"factoren</strong>: dat lukt alleen als de discriminant niet negatief is. "
                  r"\(x^{2} + 1\) lukt dus niet in \(\mathbb{R}\)."),
        ]),
        dict(kop="De vergelijking en haar discriminant", blokken=[
            ("p", r"In een tweedegraadsvergelijking <strong>is de hoogste macht twee</strong>: de vorm "
                  r"is <strong>\(ax^{2} + bx + c = 0\)</strong>, met <strong>\(a \neq 0\)</strong>, "
                  r"<strong>anders blijft \(bx + c\) over, en dat is eerste graad</strong>."),
            ("p", r"<strong>De discriminant is \(D = b^{2} - 4ac\).</strong> Ze <strong>geeft niet de "
                  r"oplossingen zelf maar enkel het aantal</strong>; de oplossingen vind je daarna met "
                  r"\[x = \frac{-b \pm \sqrt{D}}{2a}\]"),
        ]),
        dict(kop="Drie parabolen", blokken=[
            ("fig", svg.discriminant(),
             "Het teken van de discriminant zegt hoe vaak de parabool de as raakt of snijdt."),
        ]),
        dict(kop="Wat de discriminant zegt", blokken=[
            ("kader", tabel(["discriminant", "aantal reële oplossingen", "grafisch", "voorbeeld"],
                            [[r"<strong>\(D > 0\)</strong>", r"<strong>twee</strong>", r"de grafiek snijdt de \(x\)-as twee keer",
                              r"<strong>\(x^{2} - 5x + 6\) heeft \(D = 1\)</strong> (\(25 - 24\)), met oplossingen \(2\) en \(3\)"],
                             [r"<strong>\(D = 0\)</strong>", r"<strong>één</strong> (een dubbele wortel)", r"de grafiek raakt de \(x\)-as",
                              r"<strong>\(x^{2} + 2x + 1\) heeft \(D = 0\)</strong> (\(4 - 4\)), met \(x = -1\)"],
                             [r"<strong>\(D < 0\)</strong>", r"<strong>geen</strong>", r"<strong>de grafiek snijdt de \(x\)-as niet</strong> en blijft er helemaal boven of onder",
                              r"<strong>\(x^{2} + 9 = 0\) heeft geen reële oplossing</strong>: \(x^{2} + 9\) is altijd groter dan \(0\)"]])),
        ]),
        dict(kop="Zonder de formule", blokken=[
            ("p", r"Twee vergelijkingen die je zonder formule oplost. <strong>\(x^{2} = 49\) geeft "
                  r"\(x = 7\) of \(x = -7\)</strong>, en de negatieve oplossing vergeten is een klassieke "
                  r"fout. En <strong>\(x^{2} - 4x = 0\) geeft \(x = 0\) of \(x = 4\)</strong>: haal \(x\) "
                  r"buiten haakjes, want <strong>een product van twee factoren is nul als minstens één "
                  r"factor nul is</strong>."),
            ("p", r"Daarbij één waarschuwing: <strong>bij \(x^{2} = 4x\) mag je niet door \(x\) delen, "
                  r"want \(x\) kan nul zijn</strong>. Je zou de oplossing \(x = 0\) kwijtspelen. Ontbind "
                  r"liever in factoren."),
        ]),
        dict(kop="Vraagstukken van de tweede graad", blokken=[
            ("p", r"De stappen: <strong>de vergelijking opstellen</strong>, <strong>de discriminant "
                  r"berekenen</strong> en <strong>de oplossingen toetsen aan het vraagstuk</strong>. Dat "
                  r"laatste hoort er echt bij, want <strong>een vraagstuk van de tweede graad heeft niet "
                  r"altijd twee bruikbare antwoorden</strong>: een negatieve lengte of tijd valt weg, en "
                  r"je maakt ze niet positief."),
            ("p", r"Een voorbeeld: <strong>een rechthoek met \(A = 40\) waarvan de lengte \(3\) meer is "
                  r"dan de breedte, heeft breedte \(5\)</strong>, want \(5 \cdot 8 = 40\). De andere "
                  r"oplossing is \(-8\), en die valt weg."),
        ]),
    ])


# ───────────────────────── 12. Het functiebegrip en de eerstegraadsfunctie
zet("het-functiebegrip-en-de-eerstegraadsfunctie",
    titel="Het functiebegrip en de eerstegraadsfunctie",
    onder="Wat een functie is, domein en bereik, wat je uit een grafiek leest, en de eerstegraadsfunctie met haar richtingscoëfficiënt.",
    secties=[
        dict(kop="Wat een functie is", blokken=[
            ("p", r"Een functie is een verband waarbij <strong>elke \(x\) precies één \(y\) "
                  r"krijgt</strong>: elk getal uit het domein heeft juist één beeld. <strong>Eén "
                  r"\(x\)-waarde kan dus geen twee verschillende beelden hebben</strong>, dan is het geen "
                  r"functie. Omgekeerd mag wel: <strong>twee verschillende \(x\)-waarden mogen hetzelfde "
                  r"beeld hebben</strong>, zoals \(2\) en \(-2\) bij \(f(x) = x^{2}\), die allebei \(4\) "
                  r"geven."),
            ("p", r"Daarop steunt de <strong>verticale-lijntest</strong>: <strong>een verticale rechte mag "
                  r"de grafiek maar in één punt snijden</strong>."),
            ("fig", svg.verticalelijntest(),
             "De stippellijn raakt de linkse kromme één keer en de rechtse twee keer."),
        ]),
        dict(kop="Rekenen met een voorschrift", blokken=[
            ("p", r"<strong>Voor \(f(x) = 2x + 1\) is \(f(4) = 9\)</strong>, en <strong>voor "
                  r"\(f(x) = x^{2}\) is \(f(-3) = 9\)</strong>, want een kwadraat is nooit negatief. En "
                  r"<strong>als \(f(2) = 0\), dan is \(2\) een nulwaarde</strong>: de grafiek gaat door het "
                  r"punt \((2, 0)\)."),
            ("p", r"<strong>Het domein van elke functie is niet heel de reële rechte \(\mathbb{R}\)</strong>: over het "
                  r"domein klopt dat <strong>het de \(x\)-waarden zijn</strong>, dat <strong>bij een breuk "
                  r"de noemer niet nul mag zijn</strong> en dat <strong>bij een wortel wat eronder staat "
                  r"niet negatief mag zijn</strong>."),
        ]),
        dict(kop="De woorden op een rij", blokken=[
            ("kader", tabel(["woord", "wat het betekent"],
                            [[r"<strong>het origineel</strong> (of het argument)", r"<strong>de \(x\)-waarde waarvan je het beeld neemt</strong>"],
                             [r"<strong>het beeld</strong>", r"de bijhorende \(y\)-waarde; <strong>\(f(3)\) is het beeld van \(3\)</strong>, en <strong>op de verticale as lees je de beelden af</strong>"],
                             [r"<strong>het domein</strong>", r"<strong>alle \(x\)-waarden die mogen</strong>"],
                             [r"<strong>het bereik</strong>", r"<strong>alle \(y\)-waarden die voorkomen</strong>"],
                             [r"<strong>de nulwaarde</strong> (of het nulpunt)", r"de \(x\)-waarde waar de grafiek de \(x\)-as snijdt, dus waar \(f(x) = 0\)"]])),
        ]),
        dict(kop="Vier manieren om een functie voor te stellen", blokken=[
            ("kader", tabel(["voorstelling", "wat ze geeft"],
                            [[r"<strong>een woordelijke beschrijving</strong>", r"het verband in gewone taal"],
                             [r"<strong>een tabel</strong>", r"<strong>een rij \(x\)-waarden met hun beeld</strong>: boven de \(x\), onder de beelden. Handig, maar nooit volledig"],
                             [r"<strong>een grafiek</strong>", r"het beeld in één oogopslag; punten noteer je als <strong>\((1, 5)\)</strong>, <strong>eerst de \(x\) en dan de \(y\)</strong>"],
                             [r"<strong>een voorschrift</strong>", r"de regel zelf; <strong>het voordeel boven een tabel is dat je er elke \(x\) in kan invullen</strong>"]])),
            ("p", r"Uit een functiegrafiek lees je rechtstreeks af: <strong>de nulwaarden</strong>, "
                  r"<strong>waar de functie stijgt</strong> en daalt, <strong>het hoogste punt</strong> en "
                  r"de andere extrema, en het teken."),
        ]),
        dict(kop="De eerstegraadsfunctie", blokken=[
            ("p", r"Haar voorschrift is <strong>\(f(x) = ax + b\)</strong>, met \(a \neq 0\), en haar "
                  r"grafiek is <strong>altijd een rechte</strong>. Daarom <strong>teken je ze het snelst "
                  r"met twee punten en een lat</strong>; een derde punt is een handige controle. En "
                  r"<strong>een eerstegraadsfunctie kan geen twee nulwaarden hebben</strong>: een schuine "
                  r"rechte snijdt de \(x\)-as precies één keer."),
            ("fig", svg.rechtegrafiek(),
             "De rechte y = 2x + 3: b is waar ze de as snijdt, a is het trapje."),
        ]),
        dict(kop="Wat a en b zeggen", blokken=[
            ("kader", tabel(["letter", "wat ze zegt"],
                            [[r"<strong>\(a\), de richtingscoëfficiënt</strong>", r"<strong>hoe steil de rechte loopt</strong>: de stijging per stap van \(1\) naar rechts"],
                             [r"<strong>\(b\)</strong>", r"<strong>het beeld \(f(0)\)</strong>, dus het snijpunt met de \(y\)-as"]])),
            ("p", r"Over de richtingscoëfficiënt klopt: <strong>\(a > 0\) betekent stijgend</strong>, "
                  r"<strong>\(a < 0\) betekent dalend</strong> en <strong>\(a = 0\) geeft een horizontale "
                  r"rechte</strong>. Het snijpunt met de \(y\)-as is \(b\) en niet \(a\); \(b\) schuift de "
                  r"rechte enkel op of neer."),
            ("p", r"<strong>Uit twee punten bereken je "
                  r"\(a = \frac{y_{2} - y_{1}}{x_{2} - x_{1}}\).</strong> Voor de rechte door "
                  r"<strong>\((0, 1)\) en \((2, 7)\)</strong> is dat <strong>\(\frac{6}{2} = 3\)</strong>."),
        ]),
        dict(kop="Vijf functies gelezen", blokken=[
            ("kader", tabel(["functie", "wat je meteen weet"],
                            [[r"<strong>\(f(x) = 3x - 2\)</strong>", r"<strong>\(a = 3\)</strong>: per stap naar rechts \(3\) omhoog"],
                             [r"<strong>\(f(x) = -2x + 7\)</strong>", r"<strong>\(f(0) = 7\)</strong>; in nul blijft enkel \(b\) over"],
                             [r"<strong>\(f(x) = -3x + 4\)</strong>", r"<strong>de functie is dalend</strong>, <strong>de grafiek snijdt de \(y\)-as in \(4\)</strong> en <strong>de rechte zakt \(3\) per stap</strong>"],
                             [r"<strong>\(f(x) = 2x - 6\)</strong>", r"<strong>de nulwaarde is \(3\)</strong>, want \(2x = 6\)"],
                             [r"<strong>\(f(x) = x + 5\)</strong>", r"<strong>de nulwaarde is \(-5\)</strong>"]])),
        ]),
        dict(kop="Recht en omgekeerd evenredig", blokken=[
            ("p", r"<strong>Een recht evenredig verband is \(f(x) = ax\), met \(b = 0\).</strong> Dan "
                  r"<strong>gaat de grafiek door de oorsprong</strong>, want \(f(0) = 0\), en dubbel zoveel "
                  r"\(x\) geeft dubbel zoveel \(y\)."),
            ("p", r"<strong>Bij een omgekeerd evenredig verband is de grafiek geen rechte maar een "
                  r"hyperbool</strong>: daar blijft het product \(x \cdot y\) gelijk."),
        ]),
    ])


# ───────────────────────── 13. De tweedegraadsfunctie en haar parabool
zet("de-tweedegraadsfunctie-en-haar-parabool",
    titel="De tweedegraadsfunctie en haar parabool",
    onder="De parabool met haar top en symmetrieas, wat je uit het voorschrift leest, de topvorm en de verschuivingen, en het onderzoek van de functie.",
    secties=[
        dict(kop="De parabool", blokken=[
            ("p", r"Het voorschrift is <strong>\(f(x) = ax^{2} + bx + c\)</strong>, met \(a \neq 0\), en de "
                  r"grafiek heet <strong>een parabool</strong>. Ze ligt spiegelgelijk rond haar "
                  r"<strong>symmetrieas</strong>, de verticale rechte door de top; <strong>de top ligt dus "
                  r"altijd op de symmetrieas</strong>."),
            ("p", r"<strong>De top is het hoogste of het laagste punt.</strong> <strong>Bij \(a > 0\) "
                  r"opent de parabool naar boven</strong> en is de top het laagste punt; <strong>bij "
                  r"\(a < 0\) is de top juist het hoogste punt</strong>."),
            ("fig", svg.paraboolgrafiek(),
             "De parabool \\(y = x^{2} - 4x + 3\\): twee nulwaarden, de top en de symmetrieas."),
        ]),
        dict(kop="Welke kenmerken je uit het voorschrift leest", blokken=[
            ("kader", tabel(["wat je zoekt", "waar je het leest", "voorbeeld"],
                            [[r"<strong>de opening</strong>", r"<strong>het teken van \(a\)</strong>", r"bij \(-x^{2} + 4\) opent ze naar onder"],
                             [r"<strong>het snijpunt met de \(y\)-as</strong>", r"<strong>de waarde van \(c\)</strong>, want \(f(0) = c\)",
                              r"<strong>\(2x^{2} - 8\) snijdt de \(y\)-as in \((0, -8)\)</strong>"],
                             [r"<strong>de \(x\)-waarde van de top</strong>", r"<strong>\(\frac{-b}{2a}\)</strong> (die formule staat in het formularium)",
                              r"<strong>\(x^{2} - 4x + 3\) heeft top-\(x\) \(2\)</strong>; <strong>\(x^{2} - 6x\) heeft top-\(x\) \(3\)</strong>"]])),
        ]),
        dict(kop="De top en de nulwaarden berekenen", blokken=[
            ("kader", tabel(["wat je zoekt", "waar je het leest", "voorbeeld"],
                            [[r"<strong>de \(y\)-waarde van de top</strong>", r"die top-\(x\) invullen",
                              r"<strong>\(f(2) = 4 - 8 + 3 = -1\), dus de top is \((2, -1)\)</strong>"],
                             [r"<strong>de nulwaarden</strong>", r"<strong>\(f(x) = 0\) stellen</strong> en de vergelijking oplossen", r"de snijpunten met de \(x\)-as"]])),
            ("p", r"<strong>De top van \(f(x) = x^{2}\) ligt in \((0, 0)\)</strong>, de eenvoudigste "
                  r"parabool van allemaal."),
        ]),
        dict(kop="Twee, één of geen nulwaarde", blokken=[
            ("p", r"<strong>Een parabool heeft niet altijd twee snijpunten met de \(x\)-as</strong>: dat "
                  r"hangt van de discriminant \(D\) af, dus twee, één of geen. <strong>Ligt de top "
                  r"op de \(x\)-as, dan is er precies één nulwaarde</strong> en is de discriminant "
                  r"nul. En <strong>\(f(x) = x^{2} + 2\) heeft er geen</strong>: haar top ligt in "
                  r"\((0, 2)\) en ze opent naar boven, dus ze blijft boven de \(x\)-as."),
            ("p", r"Uit <strong>\(f(x) = -x^{2} + 4\)</strong> lees je in één keer: <strong>de "
                  r"parabool opent naar onder</strong>, <strong>de top ligt in \((0, 4)\)</strong> en "
                  r"<strong>er zijn twee nulwaarden</strong>, namelijk \(2\) en \(-2\)."),
            ("weetje", r"De parabool is de baan van alles wat je weggooit. Een bal, een pijl, een "
                       r"waterstraal uit een fontein: de zwaartekracht trekt even hard aan het begin "
                       r"als op het einde, en die gelijkmatige kromming is precies een parabool."),
        ]),
        dict(kop="De topvorm", blokken=[
            ("p", r"<strong>In de topvorm \(a(x - p)^{2} + q\) is de top het punt \((p, q)\).</strong> "
                  r"Daarom is die vorm zo handig: je leest de top zonder te rekenen. <strong>De top van "
                  r"\((x - 4)^{2} + 1\) is \((4, 1)\)</strong>, en <strong>\(x^{2} - 4x + 3\) wordt in "
                  r"topvorm \((x - 2)^{2} - 1\)</strong>."),
            ("p", r"Uit <strong>\(f(x) = (x + 1)^{2} - 2\)</strong> lees je dus: <strong>\(1\) naar "
                  r"links</strong>, <strong>\(2\) omlaag</strong>, en <strong>de top ligt in "
                  r"\((-1, -2)\)</strong>."),
        ]),
        dict(kop="De verschuivingen", blokken=[
            ("kader", tabel(["wat je verandert", "wat er met de basisparabool gebeurt"],
                            [[r"<strong>\(x^{2} + 3\)</strong>", r"<strong>ze schuift \(3\) omhoog</strong>: een getal buiten het kwadraat verschuift verticaal"],
                             [r"<strong>\((x - 2)^{2}\)</strong>", r"<strong>ze schuift \(2\) naar rechts</strong>; dat voelt omgekeerd aan, maar de top ligt in \(x = 2\)"],
                             [r"<strong>het minteken in \(-x^{2}\)</strong>", r"<strong>ze spiegelt om de \(x\)-as</strong>: elke \(y\)-waarde keert om, dus ze opent naar onder"],
                             [r"<strong>\(ax^{2}\) met \(a > 1\)</strong>", r"<strong>de parabool wordt smaller</strong>, dus steiler"],
                             [r"<strong>\(0 < a < 1\)</strong>", r"<strong>ze wordt breder</strong>, dus vlakker"]])),
            ("fig", svg.paraboolverschuiving(),
             "In stippellijn de basisparabool \\(y = x^{2}\\), in het volle groen de verschoven parabool."),
        ]),
        dict(kop="Twee dingen die je niet mag verwarren", blokken=[
            ("p", r"<strong>De factor \(a\) verandert de plaats van de top niet</strong>: bij "
                  r"\(f(x) = ax^{2}\) blijft de top in de oorsprong, alleen de breedte verandert. En "
                  r"<strong>een verschuiving naar boven laat de nulwaarden niet onveranderd</strong>: de "
                  r"grafiek komt hoger te liggen, dus de snijpunten met de \(x\)-as verschuiven of "
                  r"verdwijnen. <strong>Bij een verschuiving naar rechts veranderen wél niet: de "
                  r"vorm</strong>, <strong>de breedte</strong> en <strong>de richting van de "
                  r"opening</strong> — alleen de plaats van de top verandert."),
        ]),
        dict(kop="De functie onderzoeken", blokken=[
            ("p", r"Bij een functieonderzoek ga je na: <strong>de nulwaarden</strong>, <strong>waar de "
                  r"functie stijgt en daalt</strong>, <strong>het extremum</strong> en het teken. Een "
                  r"grafiek heeft geen lengte, dus die hoort er niet bij."),
            ("p", r"<strong>Het extremum is de \(y\)-waarde van de top</strong>: <strong>een parabool die "
                  r"naar boven opent heeft een minimum</strong>, een die naar onder opent een maximum. En "
                  r"<strong>\(f(x) = x^{2}\) stijgt rechts van de top</strong>; links daalt ze, want de "
                  r"top is het keerpunt."),
        ]),
        dict(kop="Het tekenonderzoek", blokken=[
            ("p", r"<strong>Een tekenonderzoek is nagaan waar \(f(x) > 0\) is</strong>: boven de \(x\)-as "
                  r"positief, eronder negatief. <strong>\(f(x) = x^{2} - 4\) is negatief tussen \(-2\) en "
                  r"\(2\)</strong>, want tussen de twee nulwaarden ligt de parabool onder de as."),
            ("fig", svg.paraboolteken(),
             "Links de parabool, rechts dezelfde tekens kort op een getallenlijn."),
        ]),
    ])


# ───────────────────────── 14. Telproblemen en problemen oplossen
zet("telproblemen-en-problemen-oplossen",
    titel="Telproblemen en problemen oplossen",
    onder="Het boomdiagram en het venndiagram, de som-, product- en complementregel, en de vierslag om een vraagstuk aan te pakken.",
    secties=[
        dict(kop="De drie telregels", blokken=[
            ("p", r"De vakfiche noemt er <strong>drie</strong>: <strong>de somregel</strong>, <strong>de "
                  r"productregel</strong> en <strong>de complementregel</strong>. Een wortelregel bestaat "
                  r"hier niet. Bij twee muntstukken tel je met die laatste regel één geval in "
                  r"plaats van drie."),
            ("kader", tabel(["regel", "wanneer je ze gebruikt", "voorbeeld"],
                            [[r"<strong>de productregel</strong>", r"<strong>bij keuzes na elkaar</strong>: vermenigvuldigen",
                              r"<strong>\(3\) truien en \(4\) broeken geven \(3 \cdot 4 = 12\) combinaties</strong>"],
                             [r"<strong>de somregel</strong>", r"<strong>bij keuzes die elkaar uitsluiten</strong>: het een of het ander, maar niet beide",
                              r"de aantallen optellen"],
                             [r"<strong>de complementregel</strong>", r"<strong>tel het tegendeel en trek het af</strong> van het totaal",
                              r"<strong>het complement van minstens één keer kop is twee keer munt</strong>"]])),
            ("p", r"<strong>De somregel mag je niet gebruiken als de twee gevallen kunnen "
                  r"samenvallen</strong>: dan tel je de overlap dubbel, en moet je ze aftrekken."),
        ]),
        dict(kop="Tellen met de productregel", blokken=[
            ("kader", tabel(["telprobleem", "antwoord", "rekenwijze"],
                            [[r"<strong>twee dobbelstenen gooien</strong>", r"<strong>\(36\) uitkomsten</strong>", r"\(6 \cdot 6\)"],
                             [r"<strong>een munt en een dobbelsteen gooien</strong>", r"<strong>\(12\) uitkomsten</strong>", r"\(2 \cdot 6\)"],
                             [r"<strong>drie keer een munt gooien</strong>", r"<strong>\(8\) uitkomsten</strong>", r"\(2 \cdot 2 \cdot 2 = 2^{3}\)"],
                             [r"<strong>\(3\) kinderen in een rij zetten</strong>", r"<strong>\(6\) manieren</strong>", r"\(3 \cdot 2 \cdot 1\): na elke keuze blijft er één kind minder over"],
                             [r"<strong>pincodes van \(4\) cijfers</strong>", r"<strong>\(10\,000\)</strong>", r"\(10^{4}\): elk cijfer mag opnieuw"]])),
        ]),
        dict(kop="Het boomdiagram", blokken=[
            ("p", r"<strong>Een boomdiagram is een schema van alle mogelijkheden</strong>: elke tak is een "
                  r"keuze, en door de takken te volgen tel je alles. Het is handig <strong>bij keuzes na "
                  r"elkaar</strong>, <strong>bij een klein aantal mogelijkheden</strong> en <strong>om geen "
                  r"geval te vergeten</strong>. Het telt mogelijkheden; gemiddelden berekent het niet."),
            ("fig", svg.mogelijkhedenboom(["kop", "munt"], ["1", "2", "3", "4", "5", "6"]),
             "Een munt en een dobbelsteen: twee takken van elk zes bladeren, samen \\(2 \\cdot 6 = 12\\)."),
        ]),
        dict(kop="Het venndiagram", blokken=[
            ("p", r"<strong>Een venndiagram toont overlappende groepen</strong>: twee of drie cirkels met "
                  r"hun overlap. <strong>In de overlap staat wat in beide verzamelingen zit</strong>, de "
                  r"doorsnede \(A \cap B\), en net daarom zie je er dubbele tellingen in. <strong>Je telt "
                  r"die overlap niet twee keer mee</strong>: \(|A \cup B| = |A| + |B| - |A \cap B|\)."),
            ("fig", svg.venndiagram("voetbal", "zwemmen", "8", "4", "5"),
             "\\(12\\) voetballers en \\(9\\) zwemmers, \\(4\\) doen beide: samen \\(8 + 4 + 5 = 17\\) sporters."),
        ]),
        dict(kop="Tellen met overlap", blokken=[
            ("kader", tabel(["situatie", "antwoord", "rekenwijze"],
                            [[r"<strong>\(12\) kinderen voetballen, \(9\) zwemmen, \(4\) doen beide</strong>", r"<strong>\(17\) doen sport</strong>", r"\(12 + 9 - 4 = 17\)"],
                             [r"<strong>van \(30\) leerlingen spreken er \(18\) Frans en \(7\) twee talen</strong>", r"<strong>\(11\) spreken enkel Frans</strong>", r"\(18 - 7\)"]])),
            ("p", r"De fouten die je makkelijk maakt: <strong>gevallen dubbel tellen</strong>, <strong>een "
                  r"geval vergeten</strong> en <strong>optellen in plaats van vermenigvuldigen</strong>. "
                  r"Daarom helpt een schema zo: het maakt dubbels zichtbaar."),
        ]),
        dict(kop="Een probleem aanpakken", blokken=[
            ("p", r"De klassieke vierslag: <strong>begrijpen wat gevraagd is</strong>, <strong>een plan "
                  r"kiezen</strong>, <strong>het plan uitvoeren en controleren</strong>. <strong>De eerste "
                  r"stap is dus de vraag goed lezen</strong>: wat is gegeven en wat is gevraagd? En "
                  r"<strong>een vraagstuk heeft niet altijd maar één oplossingsweg</strong>; de "
                  r"fiche vraagt net dat je een weg kiest en verantwoordt."),
            ("p", r"<strong>Een heuristiek is een hulpmiddel om te zoeken</strong>: geen recept, maar een "
                  r"manier van aanpakken."),
            ("kader", tabel(["heuristiek", "wat ze doet"],
                            [[r"<strong>een tekening of schema maken</strong>", r"<strong>helpt ook zonder meetkunde</strong>: het maakt een verband zichtbaar dat in woorden verborgen zit"],
                             [r"<strong>het probleem eerst vereenvoudigen</strong>", r"<strong>een eenvoudiger geval proberen</strong> met kleine getallen; het patroon werkt vaak ook groot"],
                             [r"<strong>van achteren naar voren werken</strong>", r"<strong>terugwerken</strong>: je begint bij de gevraagde uitkomst en draait elke stap om"],
                             [r"<strong>een tabel maken</strong>", r"<strong>handig om een patroon op het spoor te komen</strong>: de gevallen staan naast elkaar"]])),
        ]),
        dict(kop="Schatten en controleren", blokken=[
            ("p", r"<strong>Schatten vóór je rekent is je controle</strong>: wijkt je uitkomst er "
                  r"ver van af, dan zoek je de fout. Je merkt zo <strong>een rare uitkomst</strong> meteen."),
            ("p", r"<strong>Op het einde controleer je.</strong> De vragen daarbij: <strong>is dit een "
                  r"antwoord op de vraag</strong>, <strong>klopt de grootteorde</strong> en <strong>staat "
                  r"de eenheid erbij</strong>? <strong>De eenheid mag je niet weglaten</strong>: \(5\) meter "
                  r"is niet hetzelfde als \(5\) seconden. En <strong>een onmogelijke uitkomst, zoals een "
                  r"negatieve leeftijd, wijst op een fout of op een oplossing die wegvalt</strong>."),
            ("p", r"<strong>Je stappen opschrijven helpt je je fout te vinden</strong>, en de verbetering "
                  r"ziet hoe je gedacht hebt. Op het examen levert dat punten op."),
        ]),
        dict(kop="Vijf vraagstukken uitgewerkt", blokken=[
            ("kader", tabel(["vraagstuk", "antwoord", "rekenwijze"],
                            [[r"<strong>ik denk aan een getal, tel er \(5\) bij en verdubbel; ik krijg \(26\)</strong>", r"<strong>\(8\)</strong>",
                              r"terugwerken: \(26 : 2 = 13\) en \(13 - 5 = 8\)"],
                             [r"<strong>een trui van \(40\) euro met \(25\,\%\) korting</strong>", r"<strong>\(30\) euro</strong>", r"\(25\,\%\) van \(40\) is \(10\)"],
                             [r"<strong>een trui kost na \(20\,\%\) korting \(40\) euro</strong>", r"<strong>de oude prijs was \(50\) euro</strong>", r"\(40\) is \(80\,\%\) van de oude prijs, dus \(40 : 0{,}8\)"],
                             [r"<strong>\(10\,\%\) van \(250\)</strong>", r"<strong>\(25\)</strong>", r"tien procent nemen is delen door \(10\)"],
                             [r"<strong>drie vrienden delen \(18\) euro, één krijgt het dubbele van elk van de andere twee</strong>", r"<strong>hij krijgt \(9\) euro</strong>",
                              r"samen vier gelijke delen: \(18 : 4 = 4{,}5\), en het dubbele is \(9\)"]])),
        ]),
    ])


# ───────────────────────── 15. Gegevens weergeven en samenvatten
zet("gegevens-weergeven-en-samenvatten",
    titel="Gegevens weergeven en samenvatten",
    onder="Categorische en numerieke gegevens, de frequentietabel, de grafiek die bij je gegevens past, de centrummaten en de spreidingsmaten, en hoe een grafiek je om de tuin kan leiden.",
    secties=[
        dict(kop="Twee soorten gegevens", blokken=[
            ("p", "Voor je iets tekent of berekent, kijk je eerst <strong>wat voor gegevens je hebt</strong>. "
                  "<strong>Categorische gegevens zijn gegevens in groepen</strong>: haarkleur, vervoermiddel, "
                  "lievelingsvak. Je kan ze tellen, maar <strong>je kan ze niet zinvol optellen</strong>: het "
                  "gemiddelde van blauw en groen bestaat niet. <strong>Numerieke gegevens zijn gegevens die je "
                  "meet of telt</strong>: lengte, leeftijd, het aantal broers en zussen. <strong>Daarmee kan "
                  "je wél rekenen.</strong> Hun aantal noemen we \\(n\\)."),
            ("kader", tabel(["gegeven", "soort"],
                            [["<strong>de lengte in centimeter</strong>", "<strong>numeriek</strong>, je meet ze"],
                             ["<strong>het aantal broers en zussen</strong>", "<strong>numeriek</strong>, je telt ze"],
                             ["<strong>de leeftijd in jaren</strong>", "<strong>numeriek</strong>, je telt ze"],
                             ["<strong>de haarkleur</strong>", "<strong>categorisch</strong>, het is een groep"],
                             ["<strong>het vervoermiddel naar school</strong>", "<strong>categorisch</strong>, het is een groep"]])),
        ]),
        dict(kop="De frequentietabel", blokken=[
            ("p", "<strong>De frequentietabel zet elke waarde met haar aantal op een rij</strong>: links de "
                  "waarden, rechts hoe vaak ze voorkomen. <strong>De som van de frequenties is gelijk aan "
                  "\\(n\\)</strong>, en dat is meteen je controle: komt die som niet uit, dan ben je "
                  "een gegeven vergeten."),
            ("p", "<strong>Zijn er te veel verschillende waarden, dan werk je met klassen.</strong> Bij "
                  "lengtes van \\(1{,}52\\) tot \\(1{,}89\\) meter heeft bijna elke leerling een eigen "
                  "waarde; dan groepeer je in klassen, bijvoorbeeld van \\(5\\) centimeter. "
                  "<strong>Voor lengtes van \\(150\\) tot \\(190\\) centimeter heb je vier klassen "
                  "van \\(10\\) centimeter nodig</strong>: \\(\\left[150, 160\\right[\\), "
                  "\\(\\left[160, 170\\right[\\), \\(\\left[170, 180\\right[\\) en "
                  "\\(\\left[180, 190\\right[\\)."),
        ]),
        dict(kop="De relatieve frequentie", blokken=[
            ("p", "<strong>De relatieve frequentie is het aandeel, meestal in procent</strong>: de frequentie "
                  "gedeeld door het totaal. <strong>Komen \\(20\\) van de \\(50\\) leerlingen met de bus, "
                  "dan is de relatieve frequentie \\(40\\,\\%\\)</strong>, want "
                  "\\(\\frac{20}{50} = 0{,}4\\). Dat getal laat je twee groepen van verschillende "
                  "grootte toch vergelijken."),
            ("weetje", "Een percentage verzwijgt hoeveel gegevens erachter zitten. “67 procent beveelt het "
                       "aan” klinkt sterk, tot je leest dat er drie mensen bevraagd werden."),
        ]),
        dict(kop="De grafiek die bij je gegevens past", blokken=[
            ("p", "Elke grafiek hoort bij een soort gegevens. <strong>Kies je de verkeerde, dan is je grafiek "
                  "niet fout gerekend maar wel onleesbaar.</strong>"),
            ("kader", tabel(["grafiek", "waarvoor", "hoe ze eruitziet"],
                            [["<strong>staafdiagram</strong>", "<strong>categorische gegevens</strong>", "<strong>losse staven met ruimte ertussen</strong>, één per categorie"],
                             ["<strong>histogram</strong>", "<strong>numerieke gegevens in klassen</strong>", "<strong>staven tegen elkaar</strong>, want de klassen sluiten aan"],
                             ["<strong>cirkeldiagram</strong>", "<strong>delen van een geheel</strong>", "<strong>partjes die samen \\(100\\,\\%\\) vormen</strong>"],
                             ["<strong>lijndiagram</strong>", "<strong>een verloop in de tijd</strong>", "<strong>een lijn die opeenvolgende momenten verbindt</strong>"],
                             ["<strong>dotplot</strong>", "<strong>een kleine reeks metingen</strong>", "<strong>één stip per gegeven</strong>, zo zie je meteen de vorm"],
                             ["<strong>boxplot</strong>", "<strong>de spreiding van een reeks</strong>", "<strong>de kwartielen en de mediaan</strong> in één beeld"]])),
        ]),
        dict(kop="Staafdiagram of histogram", blokken=[
            ("p", "<strong>Het verschil tussen een staafdiagram en een histogram zit in die ruimte.</strong> "
                  "Bij een staafdiagram staan de staven los, want de categorieën staan los van elkaar. "
                  "<strong>Bij een histogram staan de staven tegen elkaar</strong>, want "
                  "\\(\\left[160, 170\\right[\\) sluit aan op \\(\\left[170, 180\\right[\\)."),
            ("p", "<strong>Een cirkeldiagram is niet geschikt om \\(20\\) categorieën te vergelijken</strong>: "
                  "twintig partjes zijn niet van elkaar te onderscheiden. Een staafdiagram leest dan veel "
                  "beter. En <strong>een spreidingsdiagram toont geen verloop in de tijd</strong>, dat doet "
                  "een lijndiagram; daarover gaat het volgende hoofdstuk."),
        ]),
        dict(kop="Wat op elke grafiek hoort", blokken=[
            ("p", "<strong>Op elke grafiek horen drie dingen te staan</strong>: <strong>een titel</strong>, "
                  "<strong>een naam bij elke as</strong> en <strong>de eenheid van de getallen</strong>. "
                  "<strong>Zonder naam bij de as en zonder eenheid is een grafiek niet te lezen.</strong>"),
        ]),
        dict(kop="De centrummaten", blokken=[
            ("p", "<strong>Een centrummaat vat een hele reeks samen in één getal.</strong> Er zijn er drie, en "
                  "ze zeggen elk iets anders."),
            ("kader", tabel(["maat", "wat ze is", "voorbeeld"],
                            [["<strong>het gemiddelde</strong>", "<strong>\\(\\bar{x} = \\frac{\\text{som}}{n}\\)</strong>, de som gedeeld door het aantal",
                              "<strong>\\(4, 6\\) en \\(8\\) hebben \\(\\bar{x} = 6\\)</strong>, want \\(\\frac{18}{3} = 6\\)"],
                             ["<strong>de mediaan</strong>", "<strong>de middelste waarde</strong> als je ze van klein naar groot zet",
                              "<strong>de mediaan van \\(3, 5, 9, 11\\) en \\(12\\) is \\(9\\)</strong>: vijf waarden, dus de derde"],
                             ["<strong>de modus</strong>", "<strong>de meest voorkomende waarde</strong>",
                              "<strong>ook bij categorische gegevens</strong>: de meest gekozen kleur"]])),
        ]),
        dict(kop="Mediaan en modus in de praktijk", blokken=[
            ("p", "<strong>Bij een even aantal waarden neem je voor de mediaan het gemiddelde van de twee "
                  "middelste.</strong> <strong>De mediaan van \\(2, 4, 6\\) en \\(10\\) is dus \\(5\\)</strong>, "
                  "want \\(\\frac{4 + 6}{2} = 5\\)."),
            ("p", "<strong>Er kunnen ook twee modi zijn</strong>, als twee waarden even vaak voorkomen. En "
                  "<strong>de modus bestaat niet enkel bij numerieke gegevens</strong>: ook bij een kleur of "
                  "een vervoermiddel is er een waarde die het vaakst gekozen wordt."),
        ]),
        dict(kop="Als er een uitschieter bij zit", blokken=[
            ("p", "<strong>Bij een uitschieter zegt de mediaan meer dan het gemiddelde.</strong> Neem de "
                  "reeks \\(6, 7, 7, 8\\) en \\(32\\). <strong>Het gemiddelde is \\(\\bar{x} = 12\\)</strong>, "
                  "want de som is \\(60\\); <strong>de mediaan is \\(7\\)</strong>. Niemand van de "
                  "eerste vier zit in de buurt van \\(12\\): "
                  "<strong>die ene uitschieter trekt het gemiddelde mee omhoog, terwijl de mediaan amper "
                  "beweegt</strong>, want die ligt vast door de middelste waarde."),
            ("fig", svg.middelmaten([6, 7, 7, 8, 32]),
             "De vier lage waarden liggen dicht bij de mediaan, en het gemiddelde ligt een stuk rechts van "
             "alle vier."),
            ("p", "<strong>Een gemiddelde zegt dus niet altijd genoeg over een groep.</strong> Twee groepen "
                  "met hetzelfde gemiddelde kunnen heel anders gespreid zijn: daarvoor heb je de "
                  "spreidingsmaten nodig."),
        ]),
        dict(kop="De spreidingsmaten", blokken=[
            ("p", "<strong>Een spreidingsmaat zegt hoe ver de gegevens uiteen liggen.</strong> Ook hier zijn "
                  "er drie."),
            ("kader", tabel(["maat", "wat ze is", "voorbeeld"],
                            [["<strong>de variatiebreedte</strong>", "<strong>het grootste min het kleinste</strong>",
                              "<strong>bij \\(7, 12\\) en \\(20\\) is ze \\(13\\)</strong>, want \\(20 - 7 = 13\\)"],
                             ["<strong>de interkwartielafstand</strong>", "<strong>\\(Q_{3} - Q_{1}\\)</strong>, het derde kwartiel min het eerste",
                              "<strong>de breedte van de middelste helft</strong>; uitschieters tellen er niet in mee"],
                             ["<strong>de standaardafwijking</strong>", "<strong>hoe ver de gegevens gemiddeld van het gemiddelde liggen</strong>",
                              "<strong>klein</strong> is dicht bij het gemiddelde, <strong>groot</strong> is sterk gespreid"]])),
        ]),
        dict(kop="De boxplot", blokken=[
            ("p", "<strong>De boxplot tekent de spreiding.</strong> Je leest er <strong>de kwartielen en de "
                  "mediaan</strong> op af, en daarmee ook het minimum en het maximum: vijf getallen in één "
                  "beeld. <strong>De doos is de middelste helft van de gegevens</strong>, de streep erin is de "
                  "mediaan."),
            ("fig", svg.boxplot([2, 5, 6, 7, 8, 10, 11, 12, 14, 15, 20]),
             "Deze reeks loopt van \\(2\\) tot \\(20\\), de middelste helft ligt tussen \\(6\\) en \\(14\\), en de mediaan ligt op \\(10\\)."),
            ("p", "Bij die reeks is <strong>de variatiebreedte \\(18\\)</strong> (\\(20 - 2\\)) en <strong>de "
                  "interkwartielafstand \\(8\\)</strong> (\\(14 - 6\\)). <strong>De interkwartielafstand is dus een stuk kleiner "
                  "dan de variatiebreedte, en net dat is haar nut</strong>: ze kijkt enkel naar de middelste "
                  "helft en laat de uiteinden links liggen."),
            ("weetje", "Op een boxplot zie je niet hoeveel gegevens erachter zitten. Een doos van tien "
                       "metingen ziet er precies hetzelfde uit als een doos van duizend."),
        ]),
        dict(kop="Een grafiek kritisch lezen", blokken=[
            ("p", "<strong>Een grafiek kan kloppen en toch misleiden.</strong> De bekendste manier is "
                  "<strong>een afgeknotte as</strong>: <strong>een \\(y\\)-as die niet bij \\(0\\) begint kan een "
                  "klein verschil groot doen lijken</strong>. Zet je twee staven van \\(98\\) en "
                  "\\(100\\) op een as die bij \\(97\\) begint in plaats van bij \\(0\\), dan "
                  "steekt de ene er \\(1\\) boven uit en de andere \\(3\\): <strong>de tweede staaf "
                  "lijkt zo drie keer zo hoog als de eerste</strong>, terwijl ze maar "
                  "\\(2\\,\\%\\) verschillen."),
            ("kader", tabel(["waar je op let", "waarom"],
                            [["<strong>waar de assen beginnen</strong>", "<strong>een afgeknotte as blaast een verschil op</strong>"],
                             ["<strong>welke eenheid er staat</strong>", "<strong>zonder eenheid betekent een getal niets</strong>"],
                             ["<strong>hoeveel gegevens erachter zitten</strong>", "<strong>een percentage van \\(4\\) mensen zegt iets heel anders dan een percentage van \\(4\\,000\\)</strong>"]])),
            ("p", "<strong>Dat kritisch lezen is zelf leerstof.</strong> Op het examen krijg je een grafiek "
                  "en de vraag wat je eruit mag besluiten; <strong>het juiste antwoord is vaak dat je er "
                  "minder uit mag besluiten dan de grafiek suggereert</strong>."),
        ]),
    ])


# ───────────────────────── 16. Verbanden tussen twee grootheden
zet("verbanden-tussen-twee-grootheden",
    titel="Verbanden tussen twee grootheden",
    onder="Het spreidingsdiagram en de puntenwolk, de trendlijn en wat je ermee mag voorspellen, de correlatiecoëfficiënt, en waarom samenhang nog geen oorzaak is.",
    secties=[
        dict(kop="Het spreidingsdiagram", blokken=[
            ("p", "Tot nu ging het over één grootheid tegelijk. <strong>Wil je twee grootheden naast elkaar "
                  "leggen, dan teken je een spreidingsdiagram: één punt per meetpaar.</strong> <strong>Elk punt "
                  "heeft twee waarden</strong>, een op de x-as en een op de y-as. <strong>Er horen dus twee "
                  "waarden bij elk punt</strong>, en die twee komen van dezelfde persoon of hetzelfde voorwerp."),
            ("p", "<strong>De wolk punten noem je de puntenwolk</strong>, en haar vorm verraadt het verband. "
                  "<strong>Je gebruikt een spreidingsdiagram net om een verband tussen twee grootheden te "
                  "zien</strong>: je merkt meteen of de punten een richting hebben."),
            ("fig", svg.puntenwolk([(152, 36), (156, 37), (160, 38), (163, 38), (165, 39),
                                    (168, 40), (170, 41), (174, 41), (178, 43), (182, 44)],
                                   xlabel="lengte in cm", ylabel="schoenmaat"),
             "Tien leerlingen: de kleinste meet 152 centimeter en heeft maat 36, de grootste meet 182 "
             "centimeter en heeft maat 44."),
            ("kader", tabel(["wat je ziet", "wat het betekent"],
                            [["<strong>de punten stijgen</strong>", "<strong>een positief verband</strong>: hoe hoger x, hoe hoger y"],
                             ["<strong>de punten dalen</strong>", "<strong>een negatief verband</strong>: hoe hoger x, hoe lager y"],
                             ["<strong>geen richting</strong>", "<strong>geen verband</strong>: de punten liggen verspreid"]])),
            ("p", "<strong>In een spreidingsdiagram van lengte en schoenmaat stijgen de punten: grotere "
                  "mensen hebben een grotere maat.</strong> Een dalend verband vind je bijvoorbeeld tussen "
                  "schermtijd en uren slaap. <strong>Een spreidingsdiagram toont geen verloop in de tijd</strong>, "
                  "dat doet een lijndiagram, uit het vorige hoofdstuk."),
            ("p", "<strong>Drie dingen lees je uit een spreidingsdiagram</strong>: <strong>de richting van het "
                  "verband</strong>, <strong>hoe sterk het verband is</strong> en <strong>of er uitschieters "
                  "zijn</strong>. Een percentage lees je er niet uit."),
            ("p", "<strong>Bij een goed spreidingsdiagram staat er een naam bij elke as, de eenheid erbij en "
                  "een passende schaal.</strong> <strong>De punten verbinden hoort er niet bij</strong>: dan "
                  "maak je er een lijndiagram van, en dat zegt iets anders."),
        ]),
        dict(kop="De trendlijn", blokken=[
            ("p", "<strong>De trendlijn is de rechte die het patroon van de puntenwolk volgt.</strong> "
                  "<strong>Ze loopt zo dicht mogelijk bij alle punten, zonder er per se door te gaan</strong>: "
                  "<strong>een trendlijn hoeft niet door alle punten te gaan</strong>, en door alle punten gaan "
                  "lukt meestal niet eens."),
            ("p", "<strong>Teken je ze met de hand, dan leg je ze zo dat er evenveel punten boven als onder "
                  "liggen.</strong> Zo ligt ze zo dicht mogelijk bij de hele wolk. Op de grafische "
                  "rekenmachine laat je ze berekenen; dan krijg je er meteen de vergelijking bij."),
            ("p", "<strong>Waarvoor dient ze? Om een voorspelling te doen.</strong> <strong>Met haar "
                  "vergelijking schat je een y bij een x die je niet gemeten hebt.</strong> In de tekening "
                  "hierboven lees je zo af welke maat je verwacht bij iemand van 172 centimeter."),
            ("kader", tabel(["valkuil", "waarom"],
                            [["<strong>ver buiten de gemeten waarden voorspellen</strong>", "<strong>het verband kan daar anders zijn</strong>: buiten het bereik van je metingen weet je niet of de rechte nog klopt"],
                             ["<strong>een uitschieter laten staan zonder te kijken</strong>", "<strong>één punt ver weg kan de trendlijn flink doen kantelen</strong>"],
                             ["<strong>een rechte opleggen aan een kromme wolk</strong>", "<strong>een trendlijn is niet altijd een rechte</strong>; vaak wel, maar een verband kan ook krom zijn"]])),
            ("p", "<strong>Kijk dus altijd eerst naar de wolk zelf</strong>, en pas daarna naar de rechte. "
                  "Daarom begint elke oefening met tekenen en niet met rekenen."),
            ("weetje", "Een trendlijn heet ook een regressielijn. Dat woord komt van een onderzoek uit 1886 "
                       "over de lengte van ouders en kinderen, waarin de kinderen telkens naar het gemiddelde "
                       "toe “terugkeerden”."),
        ]),
        dict(kop="De correlatiecoëfficiënt", blokken=[
            ("p", "<strong>Correlatie is samenhang tussen twee grootheden</strong>, meer niet. <strong>De "
                  "correlatiecoëfficiënt zet die samenhang in één getal</strong>, en <strong>dat getal ligt "
                  "altijd tussen min 1 en 1</strong>."),
            ("kader", tabel(["waarde", "wat ze zegt"],
                            [["<strong>1</strong>", "<strong>een perfect stijgend verband</strong>: alle punten liggen precies op een stijgende rechte"],
                             ["<strong>0,9</strong>", "<strong>een sterk stijgend verband</strong>: de punten liggen bijna op een stijgende rechte"],
                             ["<strong>0,1</strong>", "<strong>bijna geen verband</strong>: de punten liggen bijna richtingloos"],
                             ["<strong>0</strong>", "<strong>geen lineair verband</strong>: de punten liggen zonder richting verspreid"],
                             ["<strong>−0,8</strong>", "<strong>een sterk dalend verband</strong>"],
                             ["<strong>−1</strong>", "<strong>een perfect dalend verband</strong>"]])),
            ("p", "Onthoud de twee helften van dat getal: <strong>het teken geeft de richting, de grootte "
                  "geeft de sterkte</strong>. <strong>Een correlatie van min 1 is dus niet zwakker dan een van "
                  "0,5, maar net het sterkst mogelijke verband</strong>; <strong>de sterkst mogelijke waarden "
                  "zijn 1 en min 1</strong>. Kijk naar de grootte, niet naar het teken."),
            ("p", "<strong>Bij de tien leerlingen hierboven is de correlatiecoëfficiënt ongeveer 0,99</strong>: "
                  "bijna 1, en inderdaad liggen de punten bijna op een rechte."),
            ("p", "<strong>Eén beperking telt altijd mee: de correlatiecoëfficiënt zegt enkel iets over een "
                  "lineair verband.</strong> <strong>Een duidelijk krom verband kan toch een correlatie dicht "
                  "bij nul geven</strong>, en dan is nul niet “geen verband” maar “geen rechte”. Opnieuw: eerst "
                  "de wolk bekijken."),
        ]),
        dict(kop="Correlatie is geen causaliteit", blokken=[
            ("p", "<strong>Dit is het hart van het hoofdstuk: correlatie is geen causaliteit.</strong> "
                  "<strong>Samen bewegen is niet hetzelfde als elkaar veroorzaken</strong>, en <strong>een "
                  "sterke correlatie bewijst dus niet dat het ene het andere veroorzaakt</strong>."),
            ("kader", tabel(["mogelijke verklaring", "voorbeeld"],
                            [["<strong>het ene veroorzaakt het andere</strong>", "<strong>meer uren studeren en een beter resultaat</strong>"],
                             ["<strong>een derde factor verklaart beide</strong>", "<strong>ijsjes en zwemongevallen</strong>: de warmte duwt beide omhoog"],
                             ["<strong>het is toeval</strong>", "<strong>twee reeksen die een tijdlang toevallig samen stijgen</strong>"]])),
            ("p", "<strong>Een derde factor is iets dat beide verklaart</strong>, ook wel een "
                  "<strong>verstorende factor</strong> genoemd. <strong>Het aantal ijsjes "
                  "en het aantal zwemongevallen stijgen samen omdat het warm weer is</strong>, niet omdat "
                  "ijsjes gevaarlijk zijn. <strong>Stijgen het aantal ooievaars en het aantal geboorten samen "
                  "in een land, dan besluit je dus enkel dat er samenhang is</strong>: het bekendste "
                  "schijnverband uit de handboeken."),
            ("p", "<strong>Hoe toon je een oorzakelijk verband dan wel aan? Met een opgezet experiment</strong>: "
                  "je verandert één ding en houdt de rest gelijk. <strong>Dat kan een grafiek niet.</strong> "
                  "En <strong>voor je uit een grafiek een oorzaak besluit, zoek je naar een verklaring</strong>: "
                  "<strong>een verband zonder plausibele verklaring blijft een vermoeden</strong>."),
            ("p", "<strong>Uit een correlatiecoëfficiënt van 0,95 mag je drie dingen besluiten</strong>: "
                  "<strong>de punten liggen dicht bij een rechte</strong>, <strong>het verband is "
                  "stijgend</strong> en <strong>voorspellen lukt hier redelijk goed</strong>. <strong>Over "
                  "oorzaak zegt dat getal niets.</strong>"),
            ("weetje", "Er bestaan hele verzamelingen van zulke schijnverbanden, bijvoorbeeld tussen het "
                       "aantal films met een bepaalde acteur en het aantal echtscheidingen in een staat. "
                       "Zoek er lang genoeg, en je vindt altijd twee reeksen die samen bewegen."),
        ]),
    ])
