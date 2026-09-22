# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde op ✨ Spark-niveau.

Gebaseerd op de vakfiche wiskunde 1ste graad A-stroom. Eén bundel per thema,
die bij deel 1 én bij deel 2 hoort.

Alle getalvoorbeelden in deze bundel staan ook in `controleer.py`, dat ze
narekent. Verander je hier een getal, pas het daar dan mee aan — bij wiskunde
is een tikfout in een voorbeeld erger dan een lelijke bladspiegel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

SPARK = "✨ Spark — 1ste en 2de middelbaar"

BUNDELS = {}

BUNDELS["getallenleer"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Getallenleer",
    onder="Welke soorten getallen er zijn, hoe je ermee rekent, en in welke volgorde.",
    secties=[
        dict(kop="Drie soorten getallen", blokken=[
            ("p", "Je begon met tellen: 0, 1, 2, 3 … Dat zijn de <strong>natuurlijke getallen</strong>. "
                  "Maar zodra je 3 − 7 wil uitrekenen, kom je onder nul, en dan heb je meer nodig."),
            ("fig", svg.getallensoorten(),
             "Elke soort zit in de volgende, en elke uitbreiding laat alles wat er al was overeind. Een natuurlijk getal is dus óók een geheel én een rationaal getal."),
            ("p", "De <strong>gehele getallen</strong> voegen de negatieve getallen toe. De "
                  "<strong>rationale getallen</strong> voegen daar alles bij wat je als breuk van twee "
                  "gehele getallen kan schrijven — en dus ook elk kommagetal dat stopt of zich herhaalt."),
            ("kader", "Let op de valkuil: 7 is een natuurlijk getal, maar het is tegelijk een geheel en een "
                      "rationaal getal (7 = 7/1). De vraag is nooit welk hokje het enige juiste is, wel welk "
                      "het kleinste hokje is waar het getal in past."),
        ]),
        dict(kop="Breuken", blokken=[
            ("p", "In de breuk 3/4 is 4 de <strong>noemer</strong>: in hoeveel gelijke stukken het geheel "
                  "verdeeld is. De 3 is de <strong>teller</strong>: hoeveel van die stukken je neemt."),
            ("fig", svg.breukstroken(noemers=(1, 2, 4, 8)),
             "Elke strook is de vorige gehalveerd. Hoe groter de noemer, hoe kleiner elk stuk: 1/8 is kleiner dan 1/4, ook al is 8 groter dan 4."),
            ("p", "Een <strong>stambreuk</strong> heeft 1 als teller: 1/2, 1/3, 1/8. Twee breuken zijn "
                  "<strong>gelijknamig</strong> als ze dezelfde noemer hebben. Optellen kan pas als ze "
                  "gelijknamig zijn: 1/4 + 1/6 wordt 3/12 + 2/12 = 5/12."),
            ("p", "Een breuk is <strong>onvereenvoudigbaar</strong> als teller en noemer geen gemeenschappelijke "
                  "deler meer hebben buiten 1. Zo kan 6/8 nog: deel allebei door 2 en je krijgt 3/4."),
        ]),
        dict(kop="Drie dingen die op elkaar lijken", blokken=[
            ("p", "Deze drie worden vaak verward, terwijl ze iets heel anders doen."),
            ("p", "Het <strong>tegengestelde</strong> draait het teken om: dat van −5 is 5. Samen geven ze "
                  "<strong>0</strong>. Het <strong>omgekeerde</strong> wisselt teller en noemer: dat van 2/3 "
                  "is 3/2. Samen geven ze <strong>1</strong>. De <strong>absolute waarde</strong> is de "
                  "afstand tot nul, en die is nooit negatief: |−7| = 7."),
            ("fig", svg.getallenlijn(470, -8, 8, [
                (-7, "−7", "#a2521f", True), (0, "0", "#23291f", True), (7, "7", "#2f5d50", True),
                (-5, "−5", "#6b7260", False), (5, "5", "#6b7260", False),
            ]),
             "−7 en 7 liggen allebei zeven stappen van nul. Hun absolute waarde is dus dezelfde."),
        ]),
        dict(kop="De namen bij de bewerkingen", blokken=[
            ("p", "Op het examen staan deze woorden in de vraag zelf, dus je moet ze herkennen."),
            ("p", "Optellen: <strong>termen</strong> geven een <strong>som</strong>. Aftrekken: "
                  "<strong>aftrektal</strong> min <strong>aftrekker</strong> geeft het "
                  "<strong>verschil</strong>. Vermenigvuldigen: <strong>factoren</strong> geven een "
                  "<strong>product</strong>. Delen: <strong>deeltal</strong> gedeeld door "
                  "<strong>deler</strong> geeft een <strong>quotiënt</strong>, en soms een "
                  "<strong>rest</strong>."),
            ("kader", "Blijft er niets over, dan heet het een <strong>opgaande</strong> deling. Bij 20 : 3 is "
                      "het quotiënt 6 en de rest 2, dus die is <strong>niet-opgaand</strong>."),
            ("p", "Bij machten: in 5³ is 5 het <strong>grondtal</strong> en 3 de <strong>exponent</strong>. "
                  "5³ = 5 × 5 × 5 = 125. Een tweede macht heet een <strong>kwadraat</strong>. Worteltrekken "
                  "is het omgekeerde: √49 = 7, want 7 × 7 = 49."),
        ]),
        dict(kop="Volgorde van de bewerkingen", blokken=[
            ("p", "2 + 3 × 4 is niet 20. Er is een vaste volgorde, en die is niet van links naar rechts."),
            ("fig", svg.stappen(["haakjes", "machten|en wortels", "maal|en gedeeld", "plus|en min"]),
             "Van links naar rechts werk je deze vier af. Binnen dezelfde stap reken je wél van links naar rechts."),
            ("p", "Dus: eerst 3 × 4 = 12, dan 2 + 12 = <strong>14</strong>. Wil je toch eerst optellen, dan "
                  "moet je haakjes zetten: (2 + 3) × 4 = 20."),
        ]),
        dict(kop="Eigenschappen en rekenregels", blokken=[
            ("p", "<strong>Commutatief</strong>: de volgorde mag wisselen, a + b = b + a. "
                  "<strong>Associatief</strong>: de haakjes mogen anders, (a + b) + c = a + (b + c). "
                  "<strong>Distributief</strong>: 3 × (4 + 5) = 3 × 4 + 3 × 5."),
            ("kader", "Commutatief en associatief gelden bij optellen en vermenigvuldigen, maar "
                      "<strong>niet</strong> bij aftrekken en delen. 5 − 3 is niet hetzelfde als 3 − 5."),
            ("p", "Het <strong>neutraal element</strong> verandert niets: 0 bij optellen, 1 bij "
                  "vermenigvuldigen. Het <strong>opslorpend element</strong> slokt alles op: 0 bij "
                  "vermenigvuldigen, want a × 0 = 0."),
            ("p", "Voor machten met <strong>hetzelfde grondtal</strong>: bij vermenigvuldigen tel je de "
                  "exponenten op (2³ × 2⁴ = 2⁷), bij delen trek je ze af, en bij een macht van een macht "
                  "vermenigvuldig je ze ((2³)² = 2⁶). Een negatieve exponent betekent het omgekeerde: "
                  "2⁻² = 1/2² = 1/4."),
        ]),
        dict(kop="Priemgetallen, ggd en kgv", blokken=[
            ("p", "Een <strong>priemgetal</strong> heeft precies twee delers: 1 en zichzelf. 2, 3, 5, 7, 11, "
                  "13 … 1 hoort er niet bij, want dat heeft er maar één."),
            ("p", "Splits je een getal in priemfactoren, dan vallen ggd en kgv er zo uit. "
                  "12 = 2 × 2 × 3 en 18 = 2 × 3 × 3."),
            ("p", "De <strong>grootste gemeenschappelijke deler</strong> is wat ze allebei hebben: "
                  "2 × 3 = <strong>6</strong>. Die gebruik je om breuken te vereenvoudigen. Het "
                  "<strong>kleinste gemeenschappelijk veelvoud</strong> van 4 en 6 is "
                  "<strong>12</strong>: het eerste getal dat in beide rijtjes veelvouden voorkomt. Dat "
                  "gebruik je om breuken gelijknamig te maken."),
        ]),
        dict(kop="Procent, verhouding en schaal", blokken=[
            ("p", "<strong>Procent</strong> betekent 'per honderd'. Van breuk naar procent: deel de teller "
                  "door de noemer en maal honderd. 3/8 = 0,375 = <strong>37,5 %</strong>."),
            ("fig", svg.procentraster(25),
             "Vijfentwintig van de honderd vakjes: 25 %, ofwel 1/4, ofwel 0,25. Drie schrijfwijzen voor hetzelfde."),
            ("p", "Een trui van € 40 met 25 % korting: de korting is 10 euro, dus je betaalt € 30. Sneller "
                  "gaat het in één keer: je betaalt 75 %, en 0,75 × 40 = 30."),
            ("fig", svg.verhoudingstabel([("1", "€ 1,50"), ("4", "€ 6"), ("10", "€ 15")]),
             "Vier broden voor € 6. Ga eerst naar één brood, dan kan je naar elk aantal. Wat je met de ene rij doet, doe je met de andere ook."),
            ("p", "<strong>Schaal</strong> 1 : 100 wil zeggen dat één centimeter op het plan honderd "
                  "centimeter in het echt is. Een muur van 3 cm op het plan is dus 300 cm, ofwel 3 meter."),
        ]),
        dict(kop="Afronden en schatten", blokken=[
            ("p", "Bij afronden kijk je naar het <strong>eerste cijfer dat wegvalt</strong>. Is dat 5 of meer, "
                  "dan gaat het cijfer ervoor één omhoog; is het minder, dan blijft het staan."),
            ("p", "3,247 tot op twee decimalen: het derde decimaal is 7, dus naar boven: "
                  "<strong>3,25</strong>. Tot op één decimaal wordt het 3,2, want dan kijk je naar de 4."),
            ("kader", "Rond pas op het <strong>einde</strong> af, niet tussendoor. Wie halverwege afrondt en "
                      "dan verder rekent, sleept die fout mee en komt er soms ver naast uit."),
            ("p", "<strong>Schatten</strong> is iets anders dan afronden: je maakt de som expres makkelijker "
                  "om te zien of je uitkomst kán kloppen. 19 × 21 ligt rond 20 × 20 = 400. Krijg je 4 000 op "
                  "je rekenmachine, dan weet je meteen dat er iets fout ging."),
        ]),
    ],
    onthoud=[
        "ℕ zit in ℤ zit in ℚ: elke uitbreiding voegt iets toe en laat de rest overeind.",
        "Breuk: teller boven, noemer onder. Gelijknamig = dezelfde noemer; optellen kan pas dan.",
        "Tegengestelde geeft samen 0, omgekeerde geeft samen 1, absolute waarde is de afstand tot nul.",
        "Termen/som, aftrektal/aftrekker/verschil, factoren/product, deeltal/deler/quotiënt/rest.",
        "Volgorde: haakjes, machten en wortels, maal en gedeeld, plus en min.",
        "Commutatief en associatief gelden niet bij aftrekken en delen.",
        "Machten met hetzelfde grondtal: maal → exponenten optellen, macht van macht → vermenigvuldigen.",
        "Priemgetal heeft precies twee delers. ggd om te vereenvoudigen, kgv om gelijknamig te maken.",
        "Procent is per honderd. 3/8 = 0,375 = 37,5 %. Schaal 1 : 100 → 3 cm op plan = 3 m echt.",
        "Afronden: kijk naar het eerste cijfer dat wegvalt, en rond pas op het einde af.",
    ])


BUNDELS["negatieve-getallen-en-procenten-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Negatieve getallen en procenten",
    onder="Rekenen onder nul, en rekenen per honderd \u2014 twee dingen die in het dagelijks leven overal opduiken.",
    secties=[
        dict(kop="Onder nul", blokken=[
            ("p", "Een <strong>negatief getal</strong> is een getal kleiner dan nul. Je kent ze van de "
                  "thermometer, van een lift die naar \u22122 gaat, en van een rekening die in het rood staat."),
            ("fig", svg.getallenlijn(470, -10, 10, [
                (-8, "\u22128", "#a2521f", True), (0, "0", "#23291f", True), (8, "8", "#2f5d50", True),
                (-3, "\u22123", "#6b7260", False), (3, "3", "#6b7260", False),
            ]),
             "Hoe verder naar links, hoe kleiner. Daarom is \u22128 kleiner dan \u22123, ook al klinkt acht groter dan drie."),
            ("kader", "Dit is de valkuil die het vaakst misgaat: bij negatieve getallen draait de volgorde om. "
                      "\u22123 is <strong>groter</strong> dan \u22125, want \u22123 ligt rechts van \u22125 op de lijn."),
            ("p", "Optellen is een stap naar <strong>rechts</strong>, aftrekken een stap naar <strong>links</strong>. "
                  "\u22125 + 8 betekent: begin op \u22125 en ga acht naar rechts. Je komt uit op <strong>3</strong>. "
                  "En 4 \u2212 9 betekent: begin op 4 en ga negen naar links, dus <strong>\u22125</strong>."),
        ]),
        dict(kop="Twee mintekens naast elkaar", blokken=[
            ("p", "Soms staat er een min v\u00f3\u00f3r een negatief getal: 5 \u2212 (\u22126). Die tweede min hoort bij "
                  "het getal, niet bij de bewerking. Iets aftrekken dat zelf onder nul zit, maakt je uitkomst "
                  "juist <strong>groter</strong>."),
            ("p", "Dus 5 \u2212 (\u22126) = 5 + 6 = <strong>11</strong>, en \u22127 \u2212 (\u22123) = \u22127 + 3 = <strong>\u22124</strong>. "
                  "Een handige manier om het te onthouden: het tegengestelde aftrekken is hetzelfde als optellen."),
            ("kader", "Let op het verschil tussen het <strong>teken</strong> van een getal en de <strong>bewerking</strong>. "
                      "In \u22126 \u2212 4 is de eerste min een teken en de tweede een bewerking: je begint op \u22126 en gaat "
                      "nog vier naar links, dus <strong>\u221210</strong>."),
        ]),
        dict(kop="Maal en gedeeld: kijk eerst naar de tekens", blokken=[
            ("p", "Bij vermenigvuldigen en delen reken je eerst met de getallen alsof er geen minnen staan, "
                  "en bepaal je daarna pas het teken."),
            ("fig", svg.tekenregels(),
             "Twee dezelfde tekens geven plus, twee verschillende geven min. Voor delen geldt precies hetzelfde."),
            ("p", "Dus \u22123 \u00d7 4 = <strong>\u221212</strong>, \u22126 \u00d7 \u22122 = <strong>12</strong> en \u221220 : 5 = <strong>\u22124</strong>. "
                  "Twee negatieve getallen vermenigvuldigen geeft altijd een positieve uitkomst."),
            ("p", "Bij <strong>machten</strong> komt dat terug. (\u22122)\u00b3 is \u22122 \u00d7 \u22122 \u00d7 \u22122 = <strong>\u22128</strong>: drie "
                  "mintekens, dus min. Maar (\u22122)\u2074 = <strong>16</strong>: vier mintekens vallen twee aan twee weg. "
                  "Een <strong>even</strong> exponent geeft plus, een <strong>oneven</strong> exponent houdt de min."),
            ("kader", "Vergeet de volgorde niet. Bij \u22123 \u00d7 (4 \u2212 7) reken je eerst het haakje uit: 4 \u2212 7 = \u22123. "
                      "Daarna \u22123 \u00d7 \u22123 = <strong>9</strong>."),
        ]),
        dict(kop="Procent is per honderd", blokken=[
            ("p", "<strong>Procent</strong> betekent letterlijk 'per honderd'. 50 % is vijftig van de honderd, "
                  "ofwel de helft. Elk percentage is dus ook een breuk en een kommagetal."),
            ("fig", svg.procentraster(25),
             "Vijfentwintig van de honderd vakjes: 25 %, ofwel 1/4, ofwel 0,25. Drie schrijfwijzen voor hetzelfde."),
            ("p", "Een percentage van een getal reken je uit door te vermenigvuldigen met het kommagetal. "
                  "10 % van 80 is 0,10 \u00d7 80 = <strong>8</strong>. En 15 % van 200 is 0,15 \u00d7 200 = <strong>30</strong>."),
            ("p", "Andersom kan ook: welk deel is 5 van de 25? Deel door elkaar en maal honderd: "
                  "5 : 25 = 0,20, dus <strong>20 %</strong>. En 3/4 wordt 0,75, dus <strong>75 %</strong>."),
            ("kader", "Omdat het gewoon een vermenigvuldiging is, mag je de getallen omwisselen: 30 % van 50 is "
                      "precies evenveel als 50 % van 30. Allebei <strong>15</strong>. Dat scheelt soms veel rekenwerk."),
        ]),
        dict(kop="Korting en verhoging in \u00e9\u00e9n stap", blokken=[
            ("p", "Bij korting kan je het in twee stappen doen: een jas van \u20ac 60 met 20 % korting \u2192 de korting "
                  "is 0,20 \u00d7 60 = 12 euro, dus je betaalt <strong>\u20ac 48</strong>."),
            ("p", "Sneller gaat het in \u00e9\u00e9n keer. Bij 20 % korting betaal je de overige 80 %, en 0,80 \u00d7 60 = 48. "
                  "Bij een verhoging tel je erbij op: 120 % van 50 is 1,20 \u00d7 50 = <strong>60</strong>."),
            ("fig", svg.verhoudingstabel([("100 %", "\u20ac 60"), ("80 %", "\u20ac 48"), ("50 %", "\u20ac 30")],
                                         koppen=("percentage", "bedrag")),
             "Wat je met de bovenste rij doet, doe je met de onderste ook. Zo lees je elk percentage van hetzelfde bedrag af."),
            ("p", "Ken je de nieuwe prijs en wil je de oude weten, dan moet je <strong>delen</strong>. Een spel kost "
                  "\u20ac 48 n\u00e1 20 % korting: dat is 80 % van de oude prijs, dus 48 : 0,80 = <strong>\u20ac 60</strong>."),
        ]),
        dict(kop="Hoeveel procent is het gestegen?", blokken=[
            ("p", "Om een stijging of daling in procent uit te drukken, vergelijk je het <strong>verschil</strong> "
                  "met waar je vandaan komt \u2014 niet met waar je uitkomt."),
            ("p", "Van 40 naar 50 is een verschil van 10, en dat moet je delen door de <strong>40</strong>: "
                  "10 : 40 = 0,25, dus <strong>25 %</strong> gestegen. Zou je door 50 delen, dan kwam je op 20 % uit, "
                  "en dat is het antwoord op een andere vraag."),
            ("kader", "Andersom werkt het ook: 60 % van een klas zijn meisjes, en dat zijn er 15. Hoeveel "
                      "leerlingen zijn er dan? Deel door het percentage: 15 : 0,60 = <strong>25</strong>."),
        ]),
        dict(kop="Drie valkuilen met procenten", blokken=[
            ("p", "Procenten tellen niet zomaar op, want elk percentage hoort bij een ander getal."),
            ("p", "<strong>Eerst 10 % omhoog en dan 10 % omlaag</strong> brengt je niet terug bij de start. "
                  "\u20ac 100 wordt \u20ac 110, en 10 % daarvan is 11, dus je eindigt op <strong>\u20ac 99</strong>. De tweede "
                  "tien procent wordt van een gr\u00f3ter bedrag genomen."),
            ("p", "<strong>Eerst 50 % duurder en dan 50 % goedkoper</strong> is nog duidelijker: \u20ac 100 wordt \u20ac 150, "
                  "en de helft daarvan is <strong>\u20ac 75</strong>. Je zit dus l\u00e1ger dan waar je begon."),
            ("p", "<strong>Het grootste percentage is niet altijd de grootste korting</strong>. 30 % korting op \u20ac 80 laat je "
                  "0,70 \u00d7 80 = \u20ac 56 betalen; \u20ac 25 korting op \u20ac 80 laat je \u20ac 55 betalen. De winkel met de "
                  "<strong>\u20ac 25</strong> korting is dus de goedkoopste, ook al klinkt 30 % indrukwekkender."),
            ("kader", "Reken bij zo'n vergelijking altijd allebei de eindprijzen uit. Het percentage en het "
                      "bedrag staan naast elkaar in de winkel juist om moeilijk vergelijkbaar te zijn."),
        ]),
    ],
    onthoud=[
        "Hoe verder naar links op de getallenlijn, hoe kleiner: \u22128 is kleiner dan \u22123.",
        "Optellen gaat naar rechts, aftrekken naar links. \u22125 + 8 = 3 en 4 \u2212 9 = \u22125.",
        "Een tegengestelde aftrekken is optellen: 5 \u2212 (\u22126) = 11.",
        "Maal en gedeeld: gelijke tekens geven plus, verschillende tekens geven min.",
        "Macht van een negatief getal: even exponent geeft plus, oneven houdt de min. (\u22122)\u00b3 = \u22128, (\u22122)\u2074 = 16.",
        "Procent is per honderd. 10 % van 80 = 8. En 30 % van 50 = 50 % van 30.",
        "In \u00e9\u00e9n stap: 20 % korting \u2192 \u00d7 0,80. Terug naar de oude prijs \u2192 delen door 0,80.",
        "Stijging in procent: verschil delen door waar je vandaan komt, niet door waar je uitkomt.",
        "10 % omhoog en dan 10 % omlaag geeft 99, niet 100: het tweede percentage hoort bij een ander getal.",
    ])
