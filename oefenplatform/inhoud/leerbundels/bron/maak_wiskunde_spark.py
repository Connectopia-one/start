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


BUNDELS["probleemoplossend-denken-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Probleemoplossend denken",
    onder="Hoe je een vraagstuk aanpakt als je niet meteen ziet wat je moet doen.",
    secties=[
        dict(kop="Vier stappen, altijd dezelfde", blokken=[
            ("p", "Bij een vraagstuk is de verleiding groot om meteen met de getallen te beginnen "
                  "rekenen. Net dan gaat het mis. De vakfiche zet er vier stappen tegenover, en die "
                  "volgorde is de hele kunst."),
            ("fig", svg.stappen(["begrijp|het probleem", "maak|een plan", "voer het|plan uit", "reflecteer"]),
             "Pas bij de derde stap ga je rekenen. De eerste twee bepalen of dat rekenwerk ergens toe leidt."),
            ("p", "<strong>Begrijp het probleem</strong> betekent: schrijf op wat er gegeven is en wat er "
                  "gevraagd wordt. <strong>Maak een plan</strong> betekent: kies een aanpak. "
                  "<strong>Voer uit</strong> is het rekenwerk. <strong>Reflecteer</strong> is nakijken of "
                  "je antwoord kan kloppen én of het de gestelde vraag beantwoordt."),
        ]),
        dict(kop="Gegeven en gevraagd uit elkaar halen", blokken=[
            ("p", "„In een klas van 24 leerlingen is een derde afwezig. Hoeveel leerlingen zijn er "
                  "aanwezig?” Gegeven: 24 leerlingen, een derde afwezig. Gevraagd: het aantal "
                  "<strong>aanwezigen</strong>."),
            ("p", "Een derde van 24 is 8. Wie hier stopt, schrijft 8 op. Maar 8 is het aantal afwezigen. "
                  "Het antwoord is 24 − 8 = <strong>16</strong>."),
            ("kader", "Onderstreep in de vraag wat er precies gevraagd wordt. Een juist getal bij de "
                      "verkeerde vraag is even fout als een rekenfout, en het voelt veel juister aan."),
        ]),
        dict(kop="Strategieën die vaak werken", blokken=[
            ("p", "Er is geen enkele aanpak die altijd werkt. Dit zijn de strategieën die de fiche "
                  "noemt en die je het vaakst nodig hebt."),
            ("p", "Een <strong>schets of tekening</strong> maken. Gegevens in een <strong>tabel</strong> "
                  "zetten. <strong>Terugrekenen</strong>, van achter naar voor. <strong>Alle "
                  "mogelijkheden</strong> opschrijven. Een <strong>patroon</strong> zoeken. "
                  "<strong>Schatten</strong> om te zien in welke buurt het antwoord ligt. Het probleem "
                  "<strong>opsplitsen</strong> in kleinere stukken."),
            ("kader", "Werkt je aanpak niet, probeer dan een andere in plaats van dezelfde weg nog eens "
                      "te gaan. Vastlopen is normaal; blijven duwen in dezelfde richting helpt zelden."),
        ]),
        dict(kop="Terugrekenen", blokken=[
            ("p", "„Ik denk aan een getal, tel er 7 bij op en vermenigvuldig met 3. Ik krijg 36.” "
                  "Vooruit rekenen lukt niet, want je kent het begin niet. Dan draai je de weg om."),
            ("fig", svg.stappen(["36", "deel door 3|12", "min 7|5"]),
             "Van achter naar voor, en elke bewerking wordt haar omgekeerde: maal 3 wordt gedeeld door 3, plus 7 wordt min 7."),
            ("p", "Controleer altijd vooruit: (5 + 7) × 3 = 36. Klopt. Datzelfde trucje werkt bij "
                  "korting: een trui kost € 32 ná 20 % korting, dus € 32 is 80 % van de oude prijs, en "
                  "32 : 0,80 = <strong>€ 40</strong>."),
        ]),
        dict(kop="Alle mogelijkheden overlopen", blokken=[
            ("p", "Soms is het antwoord gewoon: tel ze. Maar tel ze dan ook <strong>allemaal</strong>, en "
                  "geen enkele twee keer. Een boompje helpt daarbij."),
            ("fig", svg.mogelijkhedenboom(["trui A", "trui B", "trui C"], ["broek 1", "broek 2"]),
             "Bij elke trui passen twee broeken. Drie takken met elk twee bladeren: 3 × 2 = 6 combinaties."),
            ("p", "Daarom vermenigvuldig je het aantal keuzes. Met de cijfers 1, 2 en 3 kan je "
                  "<strong>6</strong> getallen van twee cijfers maken als elk cijfer maar één keer mag: "
                  "drie keuzes voor het eerste cijfer, en dan nog twee over."),
            ("kader", "Let op wanneer de volgorde értoe doet en wanneer niet. Drie vrienden die elkaar "
                      "een hand geven, geven <strong>3</strong> handdrukken en geen 6: AB en BA is dezelfde "
                      "handdruk."),
        ]),
        dict(kop="Verhoudingen", blokken=[
            ("p", "Veel vraagstukken zijn verhoudingen in vermomming. Ga dan eerst naar één stuk, want "
                  "van daaruit kan je naar elk aantal."),
            ("fig", svg.verhoudingstabel([("4", "300 g"), ("1", "75 g"), ("6", "450 g")],
                                         koppen=("personen", "rijst")),
             "Een recept voor 4 personen vraagt 300 g rijst. Ga naar één persoon, en van daar naar zes."),
            ("p", "Wat je met de ene rij doet, doe je met de andere ook. Dat werkt voor prijzen, "
                  "hoeveelheden, afstanden en tijden."),
        ]),
        dict(kop="Drie valkuilen", blokken=[
            ("p", "<strong>De paalfout.</strong> Langs een tuin van 20 m komt om de 4 meter een paal, ook "
                  "aan het begin en het einde. 20 : 4 = 5, maar er staan <strong>6</strong> palen: de palen "
                  "staan op de grenzen, niet in de vakjes. Maak bij twijfel een tekening."),
            ("p", "<strong>Naar boven afronden.</strong> Voor 100 mensen in rijen van 14 stoelen is "
                  "100 : 14 = 7 met 2 over. Die 2 hebben ook een stoel nodig, dus er zijn <strong>8</strong> "
                  "rijen. Bij dozen, bussen en rijen rond je altijd naar boven af."),
            ("p", "<strong>Eenheden door elkaar.</strong> Een film van 105 minuten duurt "
                  "<strong>1 u 45 min</strong>, niet 1,05 uur. Een uur heeft 60 minuten, geen 100."),
        ]),
        dict(kop="Reflecteren: kan dit kloppen?", blokken=[
            ("p", "De laatste stap kost tien seconden en vangt de meeste fouten. Stel jezelf drie vragen."),
            ("p", "<strong>Is het mogelijk?</strong> Een klas van 25 leerlingen met samen 3 potloden, of "
                  "iemand van 200 jaar: dan ging er iets mis. <strong>Ligt het in de buurt van mijn "
                  "schatting?</strong> 19 × 21 moet rond 400 liggen. <strong>Beantwoordt het de "
                  "vraag?</strong> Er werd naar de aanwezigen gevraagd, niet naar de afwezigen."),
            ("kader", "Een onmogelijk antwoord is geen reden om te twijfelen aan jezelf, wel een aanwijzing "
                      "waar de fout zit. Zoek de stap waar het getal onrealistisch werd."),
        ]),
    ],
    onthoud=[
        "Begrijp het probleem, maak een plan, voer uit, reflecteer. Pas bij stap drie reken je.",
        "Schrijf op wat gegeven is en wat gevraagd wordt, en onderstreep de vraag.",
        "Strategieën: tekening, tabel, terugrekenen, alle mogelijkheden, patroon, schatten, opsplitsen.",
        "Terugrekenen: van achter naar voor, en elke bewerking wordt haar omgekeerde.",
        "Aantal combinaties: vermenigvuldig de keuzes. Maar let op of de volgorde ertoe doet.",
        "Verhoudingen: ga eerst naar één stuk, dan naar elk aantal.",
        "Paalfout: op 20 m om de 4 m staan 6 palen, niet 5.",
        "Bij rijen, dozen en bussen rond je naar boven af.",
        "Een film van 105 minuten is 1 u 45 min, niet 1,05 uur.",
        "Reflecteer: is het mogelijk, ligt het bij mijn schatting, en beantwoordt het de vraag?",
    ])


BUNDELS["redeneringen-en-uitspraken-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Wiskundige redeneringen en uitspraken",
    onder="Hoe je beoordeelt of iets klopt, en hoe je je oordeel opschrijft.",
    secties=[
        dict(kop="Klopt het, en hoe weet je dat?", blokken=[
            ("p", "Wiskunde is niet enkel rekenen. Even vaak krijg je een <strong>uitspraak</strong> "
                  "voorgeschoteld en is de vraag of ze klopt. Je antwoord is dan niet een getal, maar een "
                  "oordeel met een reden erbij."),
            ("p", "Klopt de uitspraak, dan geef je ter illustratie een <strong>voorbeeld</strong> of "
                  "verwijs je naar een eigenschap. Klopt ze niet, dan geef je een "
                  "<strong>tegenvoorbeeld</strong>: één geval waarin ze onderuitgaat."),
            ("kader", "Let op het verschil: een voorbeeld <strong>illustreert</strong>, maar bewijst niets. "
                      "Tien gevallen waarin iets klopt, laten nog altijd ruimte voor een elfde waarin het "
                      "misgaat. Eén tegenvoorbeeld daarentegen is meteen beslissend."),
        ]),
        dict(kop="Eén tegenvoorbeeld is genoeg", blokken=[
            ("p", "„Alle priemgetallen zijn oneven.” Dat klinkt aannemelijk: 3, 5, 7, 11, 13 … Maar "
                  "<strong>2</strong> is een priemgetal, en 2 is even. Daarmee is de uitspraak weerlegd."),
            ("p", "„Als een getal deelbaar is door 2, dan is het deelbaar door 4.” Tegenvoorbeeld: "
                  "<strong>6</strong>. Deelbaar door 2, niet door 4. Klaar."),
            ("kader", "Een tegenvoorbeeld moet wél aan de voorwaarde voldoen. Bij die laatste uitspraak is 9 "
                      "géén tegenvoorbeeld: 9 is niet deelbaar door 2, dus de uitspraak zegt er niets over."),
        ]),
        dict(kop="De als-dan-pijl ⇒", blokken=[
            ("p", "<strong>a ⇒ b</strong> lees je als: als a waar is, dan is b waar. De pijl heeft een "
                  "richting, en die richting is het halve werk."),
            ("fig", svg.pijlrichting("een vierkant", "vier rechte|hoeken", False),
             "Heen klopt het altijd. Terug niet: een rechthoek van 3 bij 5 heeft vier rechte hoeken en is geen vierkant."),
            ("p", "Denk aan: „als het regent, is de straat nat”. Het regent niet — wat weet je over de "
                  "straat? <strong>Niets met zekerheid</strong>. Ze kan nat zijn van een sproeier. De pijl "
                  "zegt alleen iets over het geval waarin het wél regent."),
            ("fig", svg.insluiting("rechthoeken", "vierkanten", "3 bij 5", "4 bij 4"),
             "Elk vierkant zit binnen de rechthoeken, maar niet elke rechthoek zit binnen de vierkanten. Zo zie je meteen welke kant de pijl op mag."),
        ]),
        dict(kop="De dubbele pijl ⇔", blokken=[
            ("p", "Geldt het in <strong>allebei</strong> de richtingen, dan schrijf je <strong>⇔</strong>: "
                  "als en slechts als."),
            ("fig", svg.pijlrichting("eindigt op 0", "deelbaar|door 10", True),
             "Heen: wie op 0 eindigt, is 10, 20, 30 … Terug: elk veelvoud van 10 eindigt op 0. Allebei, dus mag de dubbele pijl."),
            ("p", "Zo ook: een getal is deelbaar door 3 <strong>⇔</strong> de som van zijn cijfers is "
                  "deelbaar door 3. Bij 123: 1 + 2 + 3 = 6, deelbaar door 3, en inderdaad 123 : 3 = 41."),
            ("kader", "Twijfel je tussen ⇒ en ⇔, zoek dan één getal of één figuur dat de terugweg "
                      "onderuithaalt. Vind je er een, dan is het ⇒. Vind je er geen en zie je waarom, dan ⇔."),
        ]),
        dict(kop="Netjes opschrijven hoort erbij", blokken=[
            ("p", "De fiche vraagt uitdrukkelijk dat je een redenering correct noteert. Dat is geen "
                  "opsmuk: wie tussenstappen weglaat, kan zijn eigen fout niet terugvinden."),
            ("p", "Gebruik de juiste tekens. <strong>≤</strong> betekent kleiner dan óf gelijk aan, dus "
                  "x ≤ 5 laat 5 zelf ook toe; <strong>&lt;</strong> niet. Zet <strong>haakjes</strong> waar "
                  "ze nodig zijn: 2 + 3 × 4 = 14, maar (2 + 3) × 4 = 20."),
            ("kader", "Delen en aftrekken zijn niet associatief. 12 : 4 : 2 reken je van links naar rechts: "
                      "12 : 4 = 3 en dan 3 : 2 = <strong>1,5</strong>. Wie eerst 4 : 2 doet, krijgt 6 en heeft "
                      "stilzwijgend de opgave veranderd."),
        ]),
        dict(kop="Redeneerfouten die je moet kunnen betrappen", blokken=[
            ("p", "<strong>De pijl omdraaien.</strong> Uit a ⇒ b volgt niet b ⇒ a. „Alle getallen die op 5 "
                  "eindigen zijn deelbaar door 5” klopt; omgekeerd niet, want 10 is deelbaar door 5 en "
                  "eindigt op 0."),
            ("p", "<strong>Een regel gebruiken waar hij niet geldt.</strong> √(9 + 16) is niet √9 + √16. "
                  "Eerst het haakje: 9 + 16 = 25, en √25 = <strong>5</strong>, niet 7."),
            ("p", "<strong>Percentages optellen.</strong> 10 % korting en daarna nog eens 10 % is geen 20 %. "
                  "Van € 100 blijft € 90 over, daarvan gaat € 9 af, je betaalt € 81. De korting is dus "
                  "<strong>19 %</strong>."),
            ("p", "<strong>Het teken vergeten bij maal min.</strong> Uit 5 &gt; 3 volgt niet −5 &gt; −3. "
                  "Vermenigvuldigen met een negatief getal <strong>draait de ongelijkheid om</strong>: "
                  "−5 &lt; −3. Optellen doet dat niet: uit 5 &gt; 3 volgt gewoon 7 &gt; 5."),
        ]),
        dict(kop="Van voorbeeld naar bewijs", blokken=[
            ("p", "„De som van twee even getallen is even.” Je kan 2 + 4, 6 + 8 en 10 + 12 uitrekenen, "
                  "maar dan heb je drie gevallen, niet alle."),
            ("p", "Met letters dek je ze in één keer. Elk even getal is 2a, dus neem 2a en 2b. Hun som is "
                  "2a + 2b = <strong>2(a + b)</strong>, en dat is een veelvoud van 2. Klaar voor alle even "
                  "getallen tegelijk."),
            ("kader", "Dat is meteen het verschil tussen een voorbeeld en een bewijs: een voorbeeld toont "
                      "één geval, een bewijs dekt ze allemaal."),
            ("p", "Kijk tot slot na of je antwoord de <strong>gestelde vraag</strong> beantwoordt. Een "
                  "redenering waarvan elke stap klopt maar die eindigt bij iets anders dan wat gevraagd "
                  "werd, is nog niet af."),
        ]),
    ],
    onthoud=[
        "Klopt een uitspraak: geef een voorbeeld of een eigenschap. Klopt ze niet: geef een tegenvoorbeeld.",
        "Eén tegenvoorbeeld weerlegt; tien voorbeelden bewijzen niet.",
        "Een tegenvoorbeeld moet zelf aan de voorwaarde voldoen.",
        "a ⇒ b geldt maar één kant op. Elk vierkant is een rechthoek, niet elke rechthoek een vierkant.",
        "⇔ gebruik je pas als je allebei de richtingen apart getest hebt.",
        "≤ laat gelijk ook toe, < niet. Zet haakjes waar ze nodig zijn.",
        "Delen gaat van links naar rechts: 12 : 4 : 2 = 1,5.",
        "√(9 + 16) = 5, niet 3 + 4. Een wortel splits je niet over een som.",
        "10 % en nog eens 10 % korting is samen 19 %, geen 20 %.",
        "Maal een negatief getal draait de ongelijkheid om: uit 5 > 3 volgt −5 < −3.",
        "Even + even: schrijf 2a + 2b = 2(a + b). Zo dek je alle gevallen in één keer.",
    ])


BUNDELS["meetkunde-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Meetkunde",
    onder="Hoeken, driehoeken en vierhoeken, en de eigenschappen waarmee je de rest uitrekent.",
    secties=[
        dict(kop="Soorten hoeken", blokken=[
            ("p", "Een hoek meet je in <strong>graden</strong>. De vier soorten herken je aan hoe ze zich "
                  "verhouden tot de rechte hoek van 90°."),
            ("fig", svg.hoekenrij(),
             "Scherp is minder dan 90°, recht is precies 90°, stomp ligt tussen 90° en 180°, gestrekt is 180° en dus een rechte lijn."),
            ("p", "Twee hoeken die samen een gestrekte hoek vormen, heten <strong>nevenhoeken</strong>: ze "
                  "zijn samen 180°. Bij twee snijdende rechten zijn de <strong>overstaande</strong> hoeken "
                  "even groot. Is een hoek 70°, dan is de overstaande ook 70° en de nevenhoek 110°."),
            ("kader", "<strong>Loodrecht</strong> betekent een hoek van 90°. <strong>Evenwijdig</strong> "
                      "betekent dat twee rechten elkaar nooit snijden en overal dezelfde afstand houden."),
        ]),
        dict(kop="De hoekensom", blokken=[
            ("p", "Dit is de eigenschap die je het vaakst nodig hebt. In <strong>elke</strong> driehoek is "
                  "de som van de hoeken <strong>180°</strong>, hoe scheef hij ook staat."),
            ("p", "Twee hoeken van 50° en 60°? Dan is de derde 180 − 50 − 60 = <strong>70°</strong>. In een "
                  "gelijkzijdige driehoek zijn de drie hoeken even groot, dus elk 180 : 3 = <strong>60°</strong>."),
            ("p", "In een <strong>vierhoek</strong> is de hoekensom <strong>360°</strong>. Dat hoef je niet "
                  "te onthouden: trek één diagonaal en je hebt twee driehoeken, dus 2 × 180°."),
            ("kader", "In een <strong>gelijkbenige</strong> driehoek zijn de twee basishoeken even groot. "
                      "Is de tophoek 40°, dan blijft er 140° over voor twee gelijke hoeken: elk "
                      "<strong>70°</strong>. En is een basishoek 50°, dan is de tophoek 180 − 100 = <strong>80°</strong>."),
        ]),
        dict(kop="Soorten driehoeken", blokken=[
            ("p", "Een driehoek krijgt <strong>twee</strong> namen: één naar zijn zijden en één naar zijn "
                  "hoeken. Die twee staan los van elkaar."),
            ("p", "Naar de <strong>zijden</strong>: gelijkzijdig (drie gelijke), gelijkbenig (twee gelijke) "
                  "of ongelijkbenig. Naar de <strong>hoeken</strong>: scherphoekig, rechthoekig of "
                  "stomphoekig. Een driehoek met hoeken van 90° en 45° is dus rechthoekig én gelijkbenig."),
            ("p", "In een gelijkbenige driehoek heten de twee gelijke zijden de <strong>benen</strong>, de "
                  "hoek ertussen de <strong>tophoek</strong>, en de twee andere de <strong>basishoeken</strong>. "
                  "In een rechthoekige driehoek heet de zijde tegenover de rechte hoek de "
                  "<strong>schuine zijde</strong>; dat is altijd de langste."),
        ]),
        dict(kop="Soorten vierhoeken", blokken=[
            ("fig", svg.vormenrij(),
             "Van links naar rechts wordt een vierhoek bijzonderder: hoe meer eigenschappen, hoe specifieker de naam."),
            ("p", "Een <strong>trapezium</strong> heeft één paar evenwijdige zijden. Een "
                  "<strong>parallellogram</strong> twee paar. Een <strong>ruit</strong> is een "
                  "parallellogram met vier gelijke zijden, een <strong>rechthoek</strong> een parallellogram "
                  "met vier rechte hoeken, en een <strong>vierkant</strong> heeft allebei."),
            ("p", "Daarom is elk vierkant een ruit én een rechthoek, maar niet omgekeerd. In een "
                  "parallellogram zijn overstaande hoeken gelijk en aanliggende hoeken samen 180°: is er "
                  "één 110°, dan is die ernaast <strong>70°</strong>."),
            ("kader", "De <strong>diagonalen</strong> verraden veel. In een parallellogram delen ze elkaar "
                      "middendoor. In een ruit staan ze bovendien <strong>loodrecht</strong>. In een "
                      "rechthoek zijn ze even lang."),
        ]),
        dict(kop="De cirkel", blokken=[
            ("fig", svg.cirkel_straal(),
             "De straal gaat van het middelpunt naar de rand, de diameter gaat er helemaal door en is dus dubbel zo lang."),
            ("p", "Een <strong>koorde</strong> is elk lijnstuk tussen twee punten van de cirkel. De "
                  "<strong>middellijn</strong> is de langste koorde, want die gaat door het middelpunt. "
                  "Een straal van 6 cm geeft dus een diameter van <strong>12 cm</strong>."),
        ]),
        dict(kop="Hoeken bij twee evenwijdige rechten", blokken=[
            ("p", "Snijdt één rechte twee evenwijdige rechten, dan ontstaan er acht hoeken. En die acht "
                  "zijn eigenlijk maar <strong>twee</strong> verschillende groottes."),
            ("fig", svg.evenwijdige_hoeken(),
             "De hoeken 1, 4, 5 en 8 zijn even groot; 2, 3, 6 en 7 ook. Elke hoek uit de ene groep en elke hoek uit de andere zijn samen 180°."),
            ("p", "<strong>Overeenkomstige</strong> hoeken (1 en 5, 2 en 6) zijn gelijk. "
                  "<strong>Verwisselende binnenhoeken</strong> (4 en 5) zijn gelijk. "
                  "<strong>Binnenhoeken aan dezelfde kant</strong> van de snijlijn (3 en 5) zijn samen 180°."),
            ("kader", "Dus: is een binnenhoek 65°, dan is de binnenhoek aan dezelfde kant "
                      "180 − 65 = <strong>115°</strong>. Zoek in een tekening altijd eerst één hoek die je "
                      "kent, en werk van daaruit verder."),
        ]),
        dict(kop="De merkwaardige lijnen", blokken=[
            ("p", "Elke driehoek heeft vier soorten bijzondere lijnen. Ze lijken op elkaar, en net daarom "
                  "worden ze verward."),
            ("fig", svg.merkwaardige_lijnen(),
             "De bissectrice deelt een hoek in twee, de hoogtelijn staat loodrecht op de overstaande zijde, de middelloodlijn staat loodrecht op een zijde én door het midden ervan, de zwaartelijn gaat naar dat midden."),
            ("p", "Let op het verschil tussen de <strong>hoogtelijn</strong> en de "
                  "<strong>middelloodlijn</strong>: allebei staan ze loodrecht op een zijde, maar de "
                  "hoogtelijn vertrekt uit een hoekpunt en de middelloodlijn uit het midden van de zijde. "
                  "Alleen in een gelijkbenige of gelijkzijdige driehoek vallen ze samen."),
        ]),
        dict(kop="Congruente driehoeken", blokken=[
            ("p", "Twee figuren zijn <strong>congruent</strong> als ze volledig gelijk zijn: zelfde vorm "
                  "én zelfde grootte. Je hoeft niet alle zes de maten te vergelijken; drie goed gekozen "
                  "volstaan."),
            ("p", "De kenmerken: <strong>ZZZ</strong> (drie zijden), <strong>ZHZ</strong> (twee zijden en "
                  "de hoek ertussen), <strong>HZH</strong> (twee hoeken en de zijde ertussen), "
                  "<strong>ZHH</strong> (een zijde en twee hoeken) en <strong>ZZ90°</strong> (twee zijden "
                  "en een rechte hoek)."),
            ("kader", "Drie gelijke <strong>hoeken</strong> volstaat <strong>niet</strong>. Twee "
                      "gelijkzijdige driehoeken van 2 cm en van 5 cm hebben alle drie hun hoeken van 60°, "
                      "maar ze zijn niet even groot. Gelijke hoeken geven dezelfde vorm, niet dezelfde maat."),
            ("p", "Toon je aan dat twee driehoeken congruent zijn, dan zijn <strong>alle</strong> "
                  "overeenkomstige zijden en hoeken gelijk. Net daarom gebruik je congruentie: om te "
                  "bewijzen dat twee zijden even lang of twee hoeken even groot zijn."),
        ]),
        dict(kop="Transformaties en symmetrie", blokken=[
            ("p", "Een <strong>translatie</strong> schuift een figuur op over een vector. Een "
                  "<strong>rotatie</strong> draait hem rond een centrum over een hoek. Een "
                  "<strong>spiegeling</strong> klapt hem om, rond een rechte of rond een punt."),
            ("p", "Alle drie behouden ze de lengtes, de hoeken en de evenwijdigheid. Het beeld is dus "
                  "altijd <strong>congruent</strong> met de oorspronkelijke figuur. Eén ding verandert wél "
                  "bij een spiegeling om een rechte: de draairichting keert om."),
            ("p", "Een <strong>symmetrieas</strong> is een lijn waarover je de figuur kan dubbelvouwen. Een "
                  "vierkant heeft er <strong>4</strong>, een rechthoek die geen vierkant is "
                  "<strong>2</strong>, een gelijkzijdige driehoek <strong>3</strong>."),
            ("kader", "Een <strong>symmetriemiddelpunt</strong> is iets anders: de figuur valt op zichzelf "
                      "na een halve draai. Een parallellogram dat geen ruit of rechthoek is, heeft wél een "
                      "middelpunt maar géén as. Een gelijkbenige driehoek net omgekeerd."),
        ]),
    ],
    onthoud=[
        "Scherp < 90° < stomp < 180° = gestrekt. Nevenhoeken samen 180°, overstaande hoeken gelijk.",
        "Hoekensom: driehoek 180°, vierhoek 360°. Gelijkzijdig betekent drie hoeken van 60°.",
        "Gelijkbenig: de twee basishoeken zijn gelijk. Tophoek 40° geeft basishoeken van 70°.",
        "Een driehoek heeft twee namen: naar zijn zijden én naar zijn hoeken.",
        "Trapezium 1 paar evenwijdig, parallellogram 2, ruit 4 gelijke zijden, rechthoek 4 rechte hoeken.",
        "Diagonalen: parallellogram deelt middendoor, ruit ook loodrecht, rechthoek even lang.",
        "Diameter = 2 × straal. De middellijn is de langste koorde.",
        "Bij evenwijdige rechten: overeenkomstige en verwisselende binnenhoeken gelijk, dezelfde kant samen 180°.",
        "Hoogtelijn vertrekt uit een hoekpunt, middelloodlijn uit het midden van een zijde.",
        "Congruent: ZZZ, ZHZ, HZH, ZHH, ZZ90°. Drie gelijke hoeken volstaat niet.",
        "Translatie, rotatie en spiegeling behouden lengte en hoek: het beeld is congruent.",
        "Symmetrieassen: vierkant 4, rechthoek 2, gelijkzijdige driehoek 3.",
    ])


BUNDELS["metend-rekenen-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Metend rekenen",
    onder="Eenheden omzetten, en omtrek, oppervlakte en volume uitrekenen.",
    secties=[
        dict(kop="Eerst de eenheid, dan het getal", blokken=[
            ("p", "Elke meting bestaat uit een <strong>maatgetal</strong> en een <strong>eenheid</strong>. "
                  "Het getal alleen zegt niets: 3 kan 3 millimeter of 3 kilometer zijn."),
            ("fig", svg.maatladder(["km", "hm", "dam", "m", "dm", "cm", "mm"]),
             "Bij lengte is elke stap naar rechts maal 10, en elke stap naar links gedeeld door 10. Van km naar m zijn het drie stappen: 3,5 km = 3500 m."),
            ("p", "Dezelfde ladder geldt voor <strong>inhoud</strong> (l, dl, cl, ml) en voor "
                  "<strong>massa</strong> (kg, g, mg). Kies altijd de eenheid die bij de zaak past: "
                  "een afstand tussen steden in kilometer, de dikte van een blad in millimeter."),
            ("kader", "<strong>Tijd telt niet per tien.</strong> Een uur heeft 60 minuten en een minuut 60 "
                      "seconden. Dus 2,5 uur is 150 minuten, en een kwartier is 15 × 60 = 900 seconden. "
                      "Wie hier de maatladder gebruikt, komt er altijd naast."),
        ]),
        dict(kop="Oppervlakte gaat per honderd", blokken=[
            ("p", "Dit is de fout die het vaakst gemaakt wordt. Bij <strong>oppervlakte</strong> is één "
                  "stap niet maal 10 maar maal <strong>100</strong>, want je zet de lengte én de breedte om."),
            ("fig", svg.vierkante_stap(),
             "Eén vierkante decimeter is tien rijen van tien vierkante centimeter. Het oranje vakje is één cm²."),
            ("p", "Dus 2,5 m² = <strong>250</strong> dm², en 3 m² = 3 × 100 × 100 = <strong>30 000</strong> cm². "
                  "Bij <strong>volume</strong> is elke stap zelfs maal <strong>1000</strong>, want er komt "
                  "nog een derde richting bij."),
            ("kader", "Voor grond gebruik je are en hectare: 1 are = 100 m² en 1 hectare = 100 are = "
                      "10 000 m². Een tuin van 20 m bij 15 m is 300 m², dus <strong>3 are</strong>."),
        ]),
        dict(kop="Omtrek of oppervlakte?", blokken=[
            ("p", "<strong>Omtrek</strong> is hoe ver je loopt als je één keer rond de figuur gaat, en "
                  "staat in cm of m. <strong>Oppervlakte</strong> is hoeveel vakjes er binnen passen, en "
                  "staat in cm² of m²."),
            ("fig", svg.rechthoek_maten(7, 3),
             "Rond de rand: 7 + 3 + 7 + 3. Binnenin: zeven rijen van drie vakjes."),
            ("p", "Een hek rond een tuin is dus omtrek, gras zaaien is oppervlakte. Bij een vierkant met "
                  "zijde 6 cm is de omtrek 4 × 6 = <strong>24 cm</strong> en de oppervlakte 6 × 6 = "
                  "<strong>36 cm²</strong>. De eenheid verraadt meteen welke van de twee je berekend hebt."),
            ("kader", "Twee figuren met dezelfde omtrek hoeven <strong>niet</strong> dezelfde oppervlakte "
                      "te hebben. Een rechthoek van 1 bij 5 en een van 3 bij 3 hebben allebei omtrek 12, "
                      "maar oppervlakte 5 en 9."),
        ]),
        dict(kop="De formules voor vlakke figuren", blokken=[
            ("p", "<strong>Rechthoek</strong>: lengte × breedte. <strong>Vierkant</strong>: zijde × zijde. "
                  "<strong>Parallellogram</strong>: basis × hoogte — zonder delen door 2."),
            ("p", "<strong>Driehoek</strong>: (basis × hoogte) : 2, want een driehoek is de helft van een "
                  "rechthoek met dezelfde basis en hoogte. Met basis 8 en hoogte 5 geeft dat "
                  "(8 × 5) : 2 = <strong>20 cm²</strong>."),
            ("p", "<strong>Trapezium</strong>: (som van de twee evenwijdige zijden) × hoogte : 2. Met 6, "
                  "10 en hoogte 4: (6 + 10) × 4 : 2 = <strong>32 cm²</strong>. <strong>Ruit</strong>: "
                  "(diagonaal × diagonaal) : 2, dus met 8 en 6 is dat <strong>24 cm²</strong>."),
            ("kader", "De <strong>hoogte</strong> in deze formules is altijd de <strong>loodrechte</strong> "
                      "afstand, nooit de schuine zijde. Staat er een schuine zijde in de opgave, dan is dat "
                      "meestal een afleider."),
        ]),
        dict(kop="De cirkel", blokken=[
            ("fig", svg.cirkel_straal(),
             "De diameter is twee keer de straal. Welke van de twee gegeven is, bepaalt welke formule het handigst is."),
            ("p", "<strong>Omtrek</strong> = 2 × π × straal, of even goed π × diameter. "
                  "<strong>Oppervlakte</strong> = π × straal². Reken met π ≈ 3,14 tenzij er iets anders "
                  "gevraagd wordt."),
            ("p", "Bij een straal van 5 cm: omtrek 2 × 3,14 × 5 = <strong>31,4 cm</strong>, oppervlakte "
                  "3,14 × 25 = <strong>78,5 cm²</strong>. Bij een diameter van 10 cm is de omtrek "
                  "3,14 × 10 = <strong>31,4 cm</strong> — dezelfde cirkel, dus logisch."),
            ("kader", "Verwar de twee formules niet. In de omtrek staat de straal één keer en de 2 ervoor; "
                      "in de oppervlakte staat de straal in het <strong>kwadraat</strong> en geen 2."),
        ]),
        dict(kop="Ruimtefiguren", blokken=[
            ("fig", svg.ruimtefiguren(),
             "Kubus, balk en cilinder zijn de drie waarvan je oppervlakte én volume moet kunnen berekenen."),
            ("p", "<strong>Volume kubus</strong> = ribbe³, dus een ribbe van 4 cm geeft "
                  "<strong>64 cm³</strong>. <strong>Volume balk</strong> = lengte × breedte × hoogte: "
                  "5 × 3 × 2 = <strong>30 cm³</strong>. <strong>Volume cilinder</strong> = π × straal² × "
                  "hoogte: met straal 3 en hoogte 10 is dat 3,14 × 9 × 10 = <strong>282,6 cm³</strong>."),
            ("p", "De <strong>oppervlakte</strong> is alles wat je zou moeten inpakken. Een kubus heeft zes "
                  "gelijke vierkanten: bij ribbe 3 is dat 6 × 9 = <strong>54 cm²</strong>. Een balk heeft "
                  "drie paar vlakken: bij 5 bij 4 bij 2 is dat 2 × 20 + 2 × 10 + 2 × 8 = "
                  "<strong>76 cm²</strong>."),
            ("kader", "<strong>1 liter = 1 dm³</strong> en <strong>1 ml = 1 cm³</strong>. Een kubus van 2 dm "
                      "bevat dus 8 liter. En 1 m³ = 1000 liter, dus een zwembad van 10 bij 5 bij 1,5 m "
                      "houdt 75 m³ = <strong>75 000 liter</strong>."),
        ]),
        dict(kop="Samengesteld, en omgekeerd", blokken=[
            ("p", "Een figuur die je niet kent, <strong>knip je in stukken</strong> die je wél kent. Een "
                  "vierkant van 6 cm met daarop een halve cirkel van diameter 6: 36 + (3,14 × 9) : 2 = "
                  "36 + 14,13 = <strong>50,13 cm²</strong>."),
            ("p", "Gaat er iets af, dan trek je af. Knip je uit een vierkant van 10 cm in elke hoek een "
                  "vierkantje van 2 cm, dan blijft er 100 − 4 × 4 = <strong>84 cm²</strong> over."),
            ("p", "Soms krijg je de uitkomst en zoek je een maat. Een vierkant met oppervlakte 49 cm² heeft "
                  "een zijde van √49 = <strong>7 cm</strong>. Een rechthoek met oppervlakte 48 cm² en "
                  "lengte 8 cm is 48 : 8 = <strong>6 cm</strong> breed."),
            ("kader", "Verdubbel je de zijde van een vierkant, dan wordt de oppervlakte <strong>vier</strong> "
                      "keer zo groot, niet twee: van 3 cm (9 cm²) naar 6 cm (36 cm²). Allebei de "
                      "afmetingen groeien mee."),
        ]),
        dict(kop="Voor je je antwoord opschrijft", blokken=[
            ("p", "Zet alles eerst in <strong>dezelfde eenheid</strong>. Een pad van 1,2 km in 15 minuten: "
                  "maak er 1200 m van, dan is het 1200 : 15 = <strong>80 meter per minuut</strong>."),
            ("p", "Kijk of je <strong>eenheid</strong> past bij wat je berekende: cm bij omtrek, cm² bij "
                  "oppervlakte, cm³ of liter bij volume. En rond pas op het <strong>einde</strong> af: "
                  "12,467 tot op twee decimalen is <strong>12,47</strong>, want het derde decimaal is 7."),
            ("kader", "Rond zinvol af. 5 × 250 ml is 1250 ml, dus je hebt <strong>2</strong> pakjes van een "
                      "liter nodig — 1,25 pakje bestaat niet. Bij dozen, pakjes en bussen rond je naar boven af."),
        ]),
    ],
    onthoud=[
        "Lengte, inhoud en massa: elke stap is maal of gedeeld door 10.",
        "Tijd niet: een uur is 60 minuten, een minuut 60 seconden. 2,5 uur = 150 min.",
        "Oppervlakte: elke stap maal 100. Volume: elke stap maal 1000.",
        "1 are = 100 m², 1 hectare = 10 000 m².",
        "Omtrek staat in cm, oppervlakte in cm². Dezelfde omtrek betekent niet dezelfde oppervlakte.",
        "Driehoek (b × h) : 2, parallellogram b × h, trapezium (a + b) × h : 2, ruit (d × d) : 2.",
        "De hoogte is de loodrechte afstand, nooit de schuine zijde.",
        "Cirkel: omtrek 2 × π × r, oppervlakte π × r². Met r = 5: 31,4 cm en 78,5 cm².",
        "Volume: kubus r³, balk l × b × h, cilinder π × r² × h.",
        "1 liter = 1 dm³, 1 ml = 1 cm³, 1 m³ = 1000 liter.",
        "Samengesteld: knip in stukken die je kent, en trek af wat eruit gaat.",
        "Zijde verdubbelen maakt de oppervlakte vier keer zo groot.",
    ])


BUNDELS["relaties-en-verandering-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Relaties en verandering",
    onder="Coördinaten, rekenen met letters, verbanden tussen grootheden, en vergelijkingen.",
    secties=[
        dict(kop="Coördinaten", blokken=[
            ("p", "In een <strong>assenstelsel</strong> ligt elk punt vast met twee getallen. Het eerste "
                  "hoort bij de <strong>x-as</strong> (horizontaal), het tweede bij de <strong>y-as</strong> "
                  "(verticaal). Altijd in die volgorde."),
            ("fig", svg.assenstelsel([(3, 5, "A(3, 5)")]),
             "Punt A: drie naar rechts en vijf omhoog. Het snijpunt van de twee assen heet de oorsprong en heeft coördinaten (0, 0)."),
            ("kader", "Ligt een punt <strong>op de x-as</strong>, dan is zijn y-coördinaat 0. Ligt het op de "
                      "y-as, dan is zijn x-coördinaat 0."),
        ]),
        dict(kop="Rekenen met letters", blokken=[
            ("p", "Een <strong>eenterm</strong> is een getal maal letters, zoals 5x³. De "
                  "<strong>coëfficiënt</strong> is het getal vooraan (5), het <strong>lettergedeelte</strong> "
                  "is x³, en de <strong>graad</strong> is de exponent (3). Een <strong>veelterm</strong> is "
                  "een som van eentermen; haar graad is de hoogste die erin voorkomt, dus "
                  "3x² + 5x − 7 heeft graad <strong>2</strong>."),
            ("p", "Optellen mag alleen bij <strong>gelijksoortige</strong> eentermen, dat zijn eentermen met "
                  "hetzelfde lettergedeelte. 3x + 7x = 10x, en 4a + 3a − a = <strong>6a</strong>. Maar "
                  "3x + 3x² kan je niet samennemen, en 3x + 3y evenmin."),
            ("p", "Haakjes werk je weg met de distributieve eigenschap: 3(x + 2) = <strong>3x + 6</strong>. "
                  "En 2(3x − 5) + 4x wordt 6x − 10 + 4x = <strong>10x − 10</strong>."),
            ("kader", "De <strong>getalwaarde</strong> krijg je door de letters te vervangen door getallen. "
                      "x² − 3x bij x = 5 is 25 − 15 = <strong>10</strong>. En 2a − b bij a = 3 en b = −4 is "
                      "6 − (−4) = <strong>10</strong>: let op de twee mintekens."),
        ]),
        dict(kop="De merkwaardige producten", blokken=[
            ("p", "Twee uitwerkingen komen zo vaak terug dat je ze uit het hoofd kent. Ze staan ook op de "
                  "vakfiche."),
            ("p", "<strong>(a + b)² = a² + 2ab + b²</strong>. De middelste term wordt het vaakst vergeten. "
                  "Toets het met getallen: (2 + 3)² = 25, en 4 + 12 + 9 = 25. Klopt. Zo wordt "
                  "(x + 4)² dus <strong>x² + 8x + 16</strong>."),
            ("p", "<strong>(a + b)(a − b) = a² − b²</strong>. Hier vallen de middelste termen juist weg, "
                  "want −ab + ab = 0. Toets: 5 en 2 geeft 7 × 3 = 21, en 25 − 4 = 21."),
            ("kader", "Twijfel je of je een merkwaardig product juist uitwerkte, vul dan twee getallen in "
                      "en reken allebei de kanten uit. Komen ze niet overeen, dan weet je het meteen."),
        ]),
        dict(kop="Recht en omgekeerd evenredig", blokken=[
            ("p", "Twee grootheden zijn <strong>recht evenredig</strong> als ze samen meegroeien: dubbel "
                  "zoveel van het ene geeft dubbel zoveel van het andere. Ze zijn <strong>omgekeerd "
                  "evenredig</strong> als het ene groter wordt terwijl het andere even veel keer kleiner "
                  "wordt."),
            ("fig", svg.evenredig_grafieken(),
             "Recht evenredig geeft een rechte lijn door de oorsprong. Omgekeerd evenredig geeft een kromme die naar de assen toe buigt zonder ze te raken."),
            ("p", "Het onderscheid maak je met één blik op de tabel. Bij <strong>recht</strong> evenredig is "
                  "het <strong>quotiënt</strong> telkens hetzelfde: bij 2 hoort 6, bij 4 hoort 12, bij 5 "
                  "hoort 15, en 6 : 2 = 12 : 4 = 15 : 5 = 3. De formule is dan y = 3x, en die 3 heet de "
                  "<strong>evenredigheidsfactor</strong>."),
            ("p", "Bij <strong>omgekeerd</strong> evenredig is het <strong>product</strong> telkens "
                  "hetzelfde. Zes werklui doen een klus in 4 dagen, dus 6 × 4 = 24. Met twaalf werklui: "
                  "12 × ? = 24, dus <strong>2 dagen</strong>. De formule is y = 24 : x."),
        ]),
        dict(kop="Patronen in een formule zetten", blokken=[
            ("p", "Bij een patroon zoek je eerst wat er telkens bij komt, en daarna wat er aan het begin "
                  "staat."),
            ("p", "Vierkantjes van lucifers op een rij: één vierkant kost 4 lucifers, twee kosten er 7, "
                  "drie kosten er 10. Er komt telkens <strong>3</strong> bij, want elk volgend vierkant "
                  "deelt een zijde met het vorige. Bij n vierkantjes: <strong>3n + 1</strong>. Toets bij "
                  "n = 3: 3 × 3 + 1 = 10."),
            ("p", "Let op wat voor soort rij het is. Bij 3, 7, 11, 15 komt er telkens 4 bij, dus het "
                  "volgende is <strong>19</strong>. Bij 2, 4, 8, 16 wordt er telkens maal 2 gedaan, dus het "
                  "volgende is <strong>32</strong> — dat groeit veel sneller."),
        ]),
        dict(kop="Vergelijkingen oplossen", blokken=[
            ("p", "Een <strong>vergelijking</strong> heeft een <strong>linkerlid</strong>, een "
                  "<strong>gelijkheidsteken</strong> en een <strong>rechterlid</strong>. De letter is de "
                  "<strong>onbekende</strong>; de waarde die de gelijkheid klopt maakt, is de "
                  "<strong>oplossing</strong>."),
            ("fig", svg.stappen(["2x + 5 = 17", "min 5|2x = 12", "deel door 2|x = 6"]),
             "Elke stap doe je aan allebei de kanten. Zo krijg je telkens een gelijkwaardige vergelijking: ze ziet er anders uit, maar heeft dezelfde oplossing."),
            ("p", "Staan er x'en aan beide kanten, breng ze dan eerst samen. 5x − 3 = 2x + 9 wordt "
                  "3x = 12, dus x = <strong>4</strong>. Staan er haakjes, dan kan je delen of uitwerken: "
                  "3(x − 2) = 15 geeft x − 2 = 5, dus x = <strong>7</strong>."),
            ("kader", "Wat je links doet, moet je <strong>ook rechts</strong> doen. Een vergelijking is een "
                      "evenwicht; verander je maar één kant, dan klopt de gelijkheid niet meer. En "
                      "controleer je oplossing altijd door ze in te vullen."),
        ]),
        dict(kop="Van een verhaal naar een vergelijking", blokken=[
            ("p", "Het moeilijkste is niet het oplossen, wel het opstellen. Zet eerst met woorden wat de "
                  "onbekende is, en vertaal dan zin per zin."),
            ("p", "„Een taxi vraagt € 3 opstapgeld en € 2 per kilometer. Je betaalt € 19.” Noem het "
                  "aantal kilometer x. Dan is de rit 3 + 2x, en dat is 19. Uit 2x = 16 volgt "
                  "x = <strong>8 kilometer</strong>."),
            ("p", "„De omtrek van een rechthoek is 26 cm en de lengte is 8 cm.” De omtrek is "
                  "2 × (lengte + breedte), dus 2(8 + b) = 26. Delen door 2 geeft 8 + b = 13, dus "
                  "b = <strong>5 cm</strong>."),
            ("kader", "Formuleer op het einde een <strong>antwoord in woorden</strong>, met de eenheid erbij. "
                      "„x = 8” is het halve werk; „de rit was 8 kilometer lang” is het antwoord op de vraag."),
        ]),
    ],
    onthoud=[
        "Coördinaten: eerst x (horizontaal), dan y (verticaal). De oorsprong is (0, 0).",
        "Op de x-as is y = 0; op de y-as is x = 0.",
        "In 5x³ is 5 de coëfficiënt, x³ het lettergedeelte en 3 de graad.",
        "Optellen mag enkel bij gelijksoortige eentermen: 3x + 7x = 10x, maar 3x + 3x² niet.",
        "(a + b)² = a² + 2ab + b². Vergeet de middelste term niet.",
        "(a + b)(a − b) = a² − b². Daar valt de middelste term juist weg.",
        "Recht evenredig: het quotiënt blijft gelijk, grafiek is een rechte door de oorsprong.",
        "Omgekeerd evenredig: het product blijft gelijk. 6 werklui × 4 dagen = 12 × 2.",
        "Patroon: zoek wat er telkens bij komt, en wat er aan het begin staat. Lucifervierkantjes: 3n + 1.",
        "Wat je links van het gelijkheidsteken doet, doe je ook rechts.",
        "Controleer je oplossing door ze in te vullen, en antwoord met een zin en een eenheid.",
    ])


BUNDELS["data-en-onzekerheid-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Data en onzekerheid",
    onder="Gegevens verzamelen en ordenen, gemiddelde, mediaan en modus, diagrammen lezen en doorzien.",
    secties=[
        dict(kop="Gegevens verzamelen en ordenen", blokken=[
            ("p", "Statistiek begint niet bij rekenen maar bij een <strong>onderzoeksvraag</strong>. Die is "
                  "goed als je er met gegevens een antwoord op kan geven. „Hoeveel uur slapen de leerlingen "
                  "van mijn klas gemiddeld per nacht?” kan je onderzoeken; „slaapt iedereen genoeg?” niet, "
                  "want daar staat nergens wat genoeg is."),
            ("p", "Wat je meet heet een <strong>variabele</strong>. Kan je ze tellen of meten, dan is ze "
                  "<strong>numeriek</strong> (aantal broers en zussen, lengte in cm). Is het een naam of een "
                  "categorie, dan is ze <strong>categorisch</strong> (lievelingskleur, vervoermiddel). Dat "
                  "onderscheid bepaalt wat je er later mee mag doen."),
            ("fig", svg.frequentietabel([(0, 4), (1, 9), (2, 6), (3, 2), (4, 1)],
                                        koppen=("broers en zussen", "hoe vaak")),
             "Een frequentietabel zet elke waarde naast het aantal keer dat ze voorkomt. De som van de frequenties is altijd het aantal metingen: hier 22 leerlingen."),
            ("kader", "Controleer je tabel altijd door de frequenties op te tellen. Komt dat niet uit op het "
                      "aantal mensen dat je bevraagd hebt, dan ben je iets kwijt of heb je iets dubbel geteld."),
        ]),
        dict(kop="Gemiddelde, mediaan en modus", blokken=[
            ("p", "Drie manieren om het midden van een reeks in één getal te vatten. Ze geven niet hetzelfde "
                  "antwoord, en dat is precies waarom je ze alle drie kent."),
            ("p", "Het <strong>gemiddelde</strong> is de som gedeeld door het aantal. Van 4, 6 en 8 is dat "
                  "18 : 3 = <strong>6</strong>. De <strong>mediaan</strong> is het middelste getal als je ze "
                  "op volgorde zet: van 3, 7, 9, 12, 20 is dat <strong>9</strong>. Bij een even aantal neem "
                  "je het gemiddelde van de twee middelste: van 2, 4, 6, 10 is dat (4 + 6) : 2 = "
                  "<strong>5</strong>. De <strong>modus</strong> is de waarde die het vaakst voorkomt: van "
                  "3, 7, 7, 9, 12 is dat <strong>7</strong>."),
            ("fig", svg.middelmaten([3, 5, 6, 8, 10, 16]),
             "Bij een reeks zonder uitschieters liggen gemiddelde en mediaan dicht bij elkaar. De variatiebreedte is het grootste min het kleinste en zegt hoe ver de waarden uit elkaar liggen."),
            ("p", "De modus is de enige van de drie die ook werkt bij een <strong>categorische</strong> "
                  "variabele. Van lievelingskleuren kan je geen gemiddelde nemen, maar je kan wel zeggen "
                  "welke kleur het vaakst gekozen werd. Er kunnen ook <strong>twee</strong> waarden even "
                  "vaak voorkomen; dan heeft de reeks gewoon twee modi."),
            ("kader", "Het gemiddelde hoeft <strong>geen</strong> waarde uit de reeks te zijn, en zelfs geen "
                      "bestaand aantal. „De gemiddelde Belg heeft 1,7 kinderen” klopt gewoon: het is een "
                      "rekenresultaat, geen beschrijving van één gezin."),
        ]),
        dict(kop="Wanneer welke maat?", blokken=[
            ("p", "Eén uitschieter trekt het gemiddelde helemaal mee, maar laat de mediaan bijna ongemoeid. "
                  "Daar moet je op letten."),
            ("fig", svg.staafdiagram([("Aya", 10), ("Bram", 12), ("Cis", 14), ("Dina", 500)],
                                     breedte=430, hoogte=200, stap=100),
             "Vier weeklonen in euro. Het gemiddelde is € 134, terwijl drie van de vier mensen minder dan € 15 verdienen. De mediaan, € 13, beschrijft deze groep veel eerlijker."),
            ("p", "Gebruik het <strong>gemiddelde</strong> als de waarden ongeveer bij elkaar liggen, en de "
                  "<strong>mediaan</strong> zodra er uitschieters zijn. Twee reeksen kunnen hetzelfde "
                  "gemiddelde hebben en toch heel verschillend zijn: bij gemiddelde 14 en variatiebreedte 4 "
                  "zit iedereen dicht bijeen, bij gemiddelde 14 en variatiebreedte 15 liggen de resultaten "
                  "ver uit elkaar. Is de variatiebreedte <strong>0</strong>, dan zijn alle waarden gelijk."),
            ("p", "Met het gemiddelde kan je ook terugrekenen. Is het gemiddelde van vier toetsen 14, dan is "
                  "de som 14 × 4 = <strong>56</strong>. Heb je 12, 15 en 16, en wil je een gemiddelde van 15, "
                  "dan moet de som 60 worden; je staat op 43, dus je hebt <strong>17</strong> nodig."),
            ("kader", "Vergelijk je twee klassen van verschillende grootte, gebruik dan "
                      "<strong>percentages</strong> en geen aantallen. 8 van de 16 is meer dan 9 van de 30, "
                      "ook al is 9 het grootste getal."),
        ]),
        dict(kop="Diagrammen", blokken=[
            ("p", "Elk soort diagram beantwoordt een ander soort vraag. Kies het diagram bij je vraag, niet "
                  "bij wat er mooi uitziet."),
            ("fig", svg.naast_elkaar([svg.staafdiagram([("fiets", 10), ("te voet", 8), ("bus", 7)]),
                                      svg.taartdiagram([("fiets 40 %", .40, svg.FOREST),
                                                        ("te voet 32 %", .32, svg.AMBER),
                                                        ("bus 28 %", .28, "#3b6ea5")])]),
             "Een staafdiagram vergelijkt groepen: je leest de hoogte af op de verticale as. Een cirkeldiagram toont welk deel van het geheel elke groep is."),
            ("p", "Een <strong>lijndiagram</strong> gebruik je voor verandering in de tijd. Loopt de lijn "
                  "tussen 14 u en 15 u steil omhoog, dan werd het in dat uur snel warmer: de "
                  "<strong>steilheid</strong> vertelt hoe snel het ging, niet hoe warm het was."),
            ("p", "In een <strong>cirkeldiagram</strong> is de hele cirkel <strong>360°</strong> en dus "
                  "100 %. Een groep van 20 % krijgt 20 % van 360° = <strong>72°</strong>. Een sector van "
                  "90° is <strong>een vierde</strong> van het geheel. Van 40 leerlingen komen er 15 te voet; "
                  "dat is 15/40 van 360° = <strong>135°</strong>."),
            ("kader", "Een verticale as die niet bij <strong>0</strong> begint, blaast kleine verschillen op. "
                      "Kijk altijd eerst naar de as voor je naar de staven kijkt: dat is de meest gebruikte "
                      "manier om met een eerlijke grafiek toch te misleiden."),
        ]),
        dict(kop="Een onderzoek afmaken", blokken=[
            ("p", "Een statistisch onderzoek is een rondje: je stelt een vraag, verzamelt gegevens, ordent ze "
                  "in een tabel, tekent een diagram, rekent een centrummaat uit — en dan komt de stap die het "
                  "vaakst vergeten wordt."),
            ("p", "Die laatste stap is een <strong>antwoord formuleren op je onderzoeksvraag</strong>, in "
                  "woorden. Een tabel en een grafiek zijn tussenstappen. Wie stopt bij de grafiek, heeft "
                  "gegevens verzameld maar niets onderzocht."),
            ("kader", "Zeg er ook bij <strong>waarover</strong> je iets weet. Je onderzocht jouw klas, dus je "
                      "besluit gaat over jouw klas, niet over alle kinderen van het land."),
        ]),
    ],
    onthoud=[
        "Een goede onderzoeksvraag kan je met gegevens beantwoorden.",
        "Numeriek kan je tellen of meten; categorisch is een naam of een categorie.",
        "In een frequentietabel is de som van de frequenties het aantal metingen.",
        "Gemiddelde = som : aantal. Het hoeft geen waarde uit de reeks te zijn.",
        "Mediaan = het middelste getal op volgorde; bij een even aantal het gemiddelde van de twee middelste.",
        "Modus = wat het vaakst voorkomt. De enige maat die ook werkt bij kleuren of categorieën.",
        "Variatiebreedte = grootste − kleinste. Is ze 0, dan zijn alle waarden gelijk.",
        "Bij uitschieters is de mediaan eerlijker dan het gemiddelde.",
        "Staafdiagram vergelijkt groepen, lijndiagram toont verandering in de tijd, cirkeldiagram toont delen van een geheel.",
        "De hele cirkel is 360°, dus 100 %. 20 % is 72°, en 90° is een vierde.",
        "Een as die niet bij 0 begint, maakt kleine verschillen groot. Kijk eerst naar de as.",
        "Vergelijk klassen van verschillende grootte met percentages, niet met aantallen.",
        "De laatste stap is een antwoord in woorden op je onderzoeksvraag.",
    ])


BUNDELS["verzamelingen-spark"] = dict(
    vak="Wiskunde", niveau=SPARK, titel="Verzamelingen",
    onder="Elementen en deelverzamelingen, doorsnede, unie en verschil, en het venndiagram.",
    secties=[
        dict(kop="Wat is een verzameling?", blokken=[
            ("p", "Een <strong>verzameling</strong> is een groep dingen die je samen wil bekijken. Je "
                  "schrijft ze tussen <strong>accolades</strong>: {1, 2, 3}. De dingen erin heten de "
                  "<strong>elementen</strong>."),
            ("p", "Twee regels waar je vaak op getest wordt. Ten eerste telt elk element maar "
                  "<strong>één keer</strong>: {3, 5, 5, 7} heeft dus <strong>3</strong> elementen. Ten "
                  "tweede maakt de <strong>volgorde niet uit</strong>: {1, 2, 3} en {3, 1, 2} zijn dezelfde "
                  "verzameling. Bij coördinaten als (1, 2) maakt de volgorde wél uit, en daarom staan die "
                  "tussen ronde haakjes."),
            ("p", "Een verzameling zonder elementen heet de <strong>lege verzameling</strong>, geschreven "
                  "als <strong>∅</strong> of { }. Pas op met {0}: dat is een verzameling met één element "
                  "erin, dus niet leeg. Een lege doos is niet hetzelfde als een doos met een nul erin."),
        ]),
        dict(kop="De tekens", blokken=[
            ("p", "Vier tekens, en de regel welk teken waar mag staan."),
            ("p", "<strong>∈</strong> betekent „is een element van” en staat tussen een <em>ding</em> en een "
                  "verzameling: 3 ∈ {1, 2, 3}. De doorstreepte versie <strong>∉</strong> betekent „is geen "
                  "element van”: 5 ∉ {1, 2, 3}."),
            ("p", "<strong>⊂</strong> betekent „is een deelverzameling van” en staat tussen "
                  "<em>twee verzamelingen</em>: B ⊂ A wil zeggen dat elk element van B ook in A zit. Met "
                  "A = {1, 2, 3, 4} en B = {2, 4} geldt B ⊂ A, maar niet omgekeerd, want 1 en 3 zitten niet "
                  "in B."),
            ("kader", "De meest gemaakte fout is <strong>∈ en ⊂ verwisselen</strong>. Vraag je af wat er "
                      "links staat: één ding, dan ∈. Een hele verzameling, dan ⊂."),
            ("p", "Twee dingen die altijd waar zijn: elke verzameling is een deelverzameling van "
                  "<strong>zichzelf</strong> (A ⊂ A), en de lege verzameling is een deelverzameling van "
                  "<strong>elke</strong> verzameling. Daarom heeft {a, b} vier deelverzamelingen: ∅, {a}, "
                  "{b} en {a, b} zelf."),
        ]),
        dict(kop="Doorsnede, unie en verschil", blokken=[
            ("p", "Drie bewerkingen die van twee verzamelingen een nieuwe maken."),
            ("fig", svg.venndiagram("A", "B", "1", "2, 3", "4",
                                    buiten="A = {1, 2, 3} en B = {2, 3, 4}"),
             "De doorsnede A ∩ B staat in het midden: {2, 3}. De unie A ∪ B is alles samen: {1, 2, 3, 4}. Het verschil A \\ B is het linkerdeel zonder het midden: {1}."),
            ("p", "De <strong>doorsnede ∩</strong> is wat in allebei zit. De <strong>unie ∪</strong> is "
                  "alles samen, waarbij je niets dubbel schrijft: {1, 2} ∪ {2, 5} = <strong>{1, 2, 5}</strong>. "
                  "Het <strong>verschil A \\ B</strong> is wat in A zit maar niet in B: "
                  "{1, 2, 3, 4} \\ {3, 4} = <strong>{1, 2}</strong>."),
            ("p", "Hebben twee verzamelingen niets gemeenschappelijk, dan is hun doorsnede "
                  "<strong>leeg</strong>: {1, 3, 5} ∩ {2, 4, 6} = ∅. En een unie met de lege verzameling "
                  "verandert niets: {1, 2, 3} ∪ ∅ = {1, 2, 3}."),
            ("kader", "Bij het <strong>verschil</strong> maakt de volgorde wél uit. Met A = {1, 2} en "
                      "B = {2, 3} is A \\ B = {1} en B \\ A = {3}. Bij ∩ en ∪ maakt de volgorde niet uit."),
        ]),
        dict(kop="Het venndiagram bij vraagstukken", blokken=[
            ("p", "Zodra een vraagstuk twee groepen heeft die elkaar overlappen, teken je een venndiagram. "
                  "Zo zie je meteen wie er dubbel geteld wordt, en dat is daar de meest gemaakte fout."),
            ("fig", svg.venndiagram("Frans (18)", "Duits (14)", "13", "5", "9",
                                    buiten="30 leerlingen; 3 volgen geen van beide"),
             "Vul eerst het midden in: 5 volgen allebei. De rest van Frans is dan 18 − 5 = 13, en de rest van Duits 14 − 5 = 9. Samen 13 + 5 + 9 = 27, dus 30 − 27 = 3 leerlingen volgen geen van beide."),
            ("p", "Dezelfde redenering in één regel: het aantal in de unie is "
                  "<strong>A + B − de overlap</strong>. Doen van 20 leerlingen er 12 aan voetbal en 8 aan "
                  "zwemmen, en 3 allebei, dan doen er 12 + 8 − 3 = <strong>17</strong> minstens één van de "
                  "twee. Heeft A 7 elementen, B 5, en hun doorsnede 2, dan heeft de unie "
                  "7 + 5 − 2 = <strong>10</strong> elementen."),
            ("kader", "Begin altijd <strong>in het midden</strong>. Wie de overlap als laatste invult, heeft "
                      "de andere twee gebieden al fout."),
        ]),
        dict(kop="Verzamelingen in de rest van de wiskunde", blokken=[
            ("p", "De tekens zijn niet het doel. Ze zijn een korte manier om te zeggen hoe de dingen die je "
                  "al kent bij elkaar horen."),
            ("fig", svg.insluiting("R: de rechthoeken", "V: de vierkanten",
                                   "3 bij 5", "4 bij 4"),
             "V ⊂ R: elk vierkant is een rechthoek, want het heeft vier rechte hoeken. Omgekeerd niet: een rechthoek van 3 bij 5 is geen vierkant."),
            ("p", "Zo zit het ook bij de <strong>getallen</strong>: elk natuurlijk getal is een geheel "
                  "getal, dus <strong>ℕ ⊂ ℤ</strong>. Omgekeerd niet, want −3 is geheel maar niet "
                  "natuurlijk. En bij de <strong>driehoeken</strong>: een gelijkzijdige driehoek heeft drie "
                  "gelijke zijden en dus zeker ook twee, dus Z ⊂ G."),
            ("p", "Een doorsnede geeft soms een bekende naam terug. Een ruit heeft vier gelijke zijden, een "
                  "rechthoek vier rechte hoeken; wie allebei is, is een <strong>vierkant</strong>. De "
                  "doorsnede van de even getallen en de veelvouden van 3 zijn de <strong>veelvouden van "
                  "6</strong>. En de doorsnede van de priemgetallen en de even getallen is "
                  "<strong>{2}</strong>, want elk ander even getal is deelbaar door 2 en heeft dus meer dan "
                  "twee delers."),
        ]),
    ],
    onthoud=[
        "Een verzameling staat tussen accolades: {1, 2, 3}. Wat erin zit, zijn de elementen.",
        "Elk element telt één keer, en de volgorde maakt niet uit.",
        "∅ is de lege verzameling. {0} is niet leeg: daar zit één element in.",
        "∈ staat tussen een element en een verzameling; ⊂ staat tussen twee verzamelingen.",
        "A ⊂ A, en ∅ is een deelverzameling van elke verzameling. {a, b} heeft 4 deelverzamelingen.",
        "∩ is de doorsnede (wat in allebei zit), ∪ is de unie (alles samen, niets dubbel).",
        "A \\ B is wat in A zit maar niet in B. Daar maakt de volgorde wél uit.",
        "Hebben ze niets gemeen, dan is de doorsnede leeg.",
        "Aantal in de unie = A + B − de overlap. Teken een venndiagram en begin in het midden.",
        "ℕ ⊂ ℤ, de vierkanten ⊂ de rechthoeken, de gelijkzijdige ⊂ de gelijkbenige driehoeken.",
        "Ruiten ∩ rechthoeken = de vierkanten. Priemgetallen ∩ even getallen = {2}.",
    ])
