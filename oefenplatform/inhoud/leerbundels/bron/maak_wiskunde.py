# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde, categorie Start (5de en 6de leerjaar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Wiskunde"

PLAATSWAARDE = """
<table style="width:100%;border-collapse:collapse;font-family:'IBM Plex Sans',sans-serif;font-size:10.5pt;">
  <tr>""" + "".join(
    f'<th style="border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 4px;color:#234539;font-weight:600;">{k}</th>'
    for k in ["miljoen", "honderd&shy;duizend", "tien&shy;duizend", "duizend", "honderd", "tien", "een"]
) + """</tr>
  <tr>""" + "".join(
    f'<td style="border:1px solid #e4ded0;padding:9px 4px;text-align:center;font-size:15pt;font-weight:600;color:{"#c17f2b" if c == "6" else "#23291f"};">{c}</td>'
    for c in "2645130"
) + """</tr>
</table>
"""

tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────────────────────────── 1. Getallenkennis
BUNDELS["getallenkennis"] = dict(
    vak=VAK, titel="Getallenkennis",
    onder="Wat getallen betekenen, hoe je ze leest en hoe je ze met elkaar vergelijkt.",
    secties=[
        dict(kop="Grote getallen lezen", blokken=[
            ("p", "Elk cijfer in een getal heeft een eigen plaats, en die plaats bepaalt hoeveel het cijfer waard is. Een 6 vooraan is veel meer waard dan een 6 achteraan."),
            ("fig", PLAATSWAARDE, "In 2 645 130 staat de 6 op de plaats van de honderdduizendtallen. Die 6 is dus 600 000 waard."),
            ("p", "Je leest zo'n getal van links naar rechts, in groepjes van drie: <strong>twee miljoen — zeshonderdvijfenveertigduizend — honderddertig</strong>. Daarom laten we telkens een spatie tussen de groepjes."),
            ("p", "Omgekeerd werkt het net zo. <strong>Twee miljoen driehonderdduizend</strong> schrijf je door elk groepje op zijn plaats te zetten: 2 300 000. En wil je weten hoeveel duizendtallen er in 45 000 zitten, dan deel je door 1 000: dat zijn er 45. Hoeveel honderdtallen in 7 400? Delen door 100 geeft 74."),
            ("weetje", "Die spatie is geen punt en geen komma. In het Engels schrijven ze wel een komma (2,645,130). Hetzelfde getal, een andere gewoonte."),
        ]),
        dict(kop="Afronden", blokken=[
            ("p", "Afronden is een getal vervangen door een rond getal dat er dicht bij ligt. Je kijkt naar het cijfer <em>rechts</em> van de plaats waarop je afrondt: is dat 5 of meer, dan ga je naar boven; is het minder dan 5, dan blijf je beneden."),
            ("fig", svg.getallenlijn(470, 3700, 3800, [
                (3700, "3 700", svg.INK, False), (3750, "helft", svg.DIM, False),
                (3800, "3 800", svg.INK, False), (3748, "3 748", svg.AMBER, True)]),
             "3 748 afgerond op honderdtallen wordt 3 700: het ligt links van de helft."),
            ("p", "Afronden op duizendtallen geeft 4 000, want dan kijk je naar de 7."),
        ]),
        dict(kop="Kommagetallen", blokken=[
            ("p", "Achter de komma gaat het tellen gewoon verder, maar in stukjes: tienden, honderdsten, duizendsten. <strong>0,7 is groter dan 0,65</strong>, want 0,7 is hetzelfde als 0,70."),
            ("fig", svg.getallenlijn(470, 4.0, 5.0, [
                (4.0, "4", svg.INK, False), (4.2, "4,2", svg.DIM, False),
                (4.3, "4,3", svg.AMBER, True), (4.4, "4,4", svg.DIM, False),
                (5.0, "5", svg.INK, False)]),
             "Tussen 4,2 en 4,4 ligt 4,3 precies in het midden."),
            ("p", "Vergelijk je twee kommagetallen, vul dan eerst aan met nullen tot ze evenveel cijfers achter de komma hebben. Dan lees je ze even makkelijk als gewone getallen."),
            ("weetje", "Maal 10 schuift de komma één plaats naar rechts, delen door 10 één plaats naar links. 7,5 × 100 wordt dus 750."),
        ]),
        dict(kop="Breuken", blokken=[
            ("p", "Een breuk is een geheel dat in gelijke stukken verdeeld is. Het onderste getal (de <strong>noemer</strong>) zegt in hoeveel stukken, het bovenste (de <strong>teller</strong>) hoeveel stukken je neemt."),
            ("fig", svg.breukstroken(470), "Hoe groter de noemer, hoe kleiner elk stukje. 1/5 is dus kleiner dan 1/3."),
            ("p", "Staat boven en onder hetzelfde getal, dan heb je het hele ding: 4/4 is 1. En breuken die er anders uitzien kunnen evenveel waard zijn: 2/4 is hetzelfde als 1/2."),
        ]),
        dict(kop="Procent", blokken=[
            ("p", "Procent betekent <em>per honderd</em>. 25% is dus 25 van de 100, of één vierde van het geheel."),
            ("fig", svg.procentraster(25, 215), "25 van de 100 vakjes gekleurd: dat is 25%, of 1/4."),
            ("p", "Handige ankerpunten: 10% is delen door 10, 50% is de helft, 25% is een vierde. Wil je 20% van 250 weten, neem dan 10% (= 25) en verdubbel dat: 50."),
        ]),
        dict(kop="Breuk, kommagetal en procent", blokken=[
            ("p", "Dezelfde hoeveelheid kan er op drie manieren uitzien. Drie vierde, 0,75 en 75% zijn precies hetzelfde. Van een breuk naar een kommagetal deel je de teller door de noemer: 3 : 4 = 0,75. Van een kommagetal naar procent vermenigvuldig je met 100."),
            ("fig", tabel(["Breuk", "Kommagetal", "Procent"], [
                ["1/10", "0,1", "10%"],
                ["1/5", "0,2", "20%"],
                ["1/4", "0,25", "25%"],
                ["1/2", "0,5", "50%"],
                ["3/5", "0,6", "60%"],
                ["3/4", "0,75", "75%"],
            ], "80%"), "Deze zes ken je het best uit het hoofd. De rest reken je daarvan af: 2/5 is twee keer 1/5, dus 40%."),
            ("p", "Een breuk <strong>vereenvoudigen</strong> doe je door de teller en de noemer allebei door hetzelfde getal te delen. 2/4 wordt 1/2, en 8/20 wordt 2/5. De waarde blijft gelijk, de breuk wordt alleen korter."),
        ]),
        dict(kop="Getallenrijen", blokken=[
            ("p", "In een rij getallen zit altijd een regel. Zoek die eerst, dan weet je vanzelf welk getal erna komt. Kijk om te beginnen naar het verschil tussen twee buren; klopt dat niet, kijk dan waarmee je moet vermenigvuldigen."),
            ("kader", "<p style='margin:0 0 4px'><strong>12, 24, 36, 48, …</strong> — er komt telkens 12 bij, dus daarna 60.</p>"
                      "<p style='margin:0'><strong>3, 6, 12, 24, …</strong> — elk getal is het dubbel van het vorige, dus daarna 48.</p>"),
            ("p", "Twijfel je tussen twee regels? Pas ze dan toe op de hele rij, niet alleen op de laatste twee getallen. Een regel die maar één keer klopt, is de juiste niet."),
        ]),
        dict(kop="Negatieve getallen", blokken=[
            ("p", "Links van de nul gaan de getallen verder met een minteken. Denk aan de temperatuur in de winter, of aan verdiepingen onder de grond."),
            ("fig", svg.getallenlijn(470, -10, 10, [
                (-10, "-10", svg.INK, False), (-8, "-8", "#a6432f", True), (-5, "-5", "#a6432f", True),
                (0, "0", svg.INK, False), (5, "5", svg.FOREST, False), (10, "10", svg.INK, False)]),
             "-5 ligt dichter bij nul dan -8, en is dus groter."),
            ("p", "Dat is het stukje dat vaak verwart: bij negatieve getallen is het getal dat er het <em>grootst</em> uitziet, net het kleinste. -10 is kouder dan -3."),
        ]),
        dict(kop="Deelbaarheid en priemgetallen", blokken=[
            ("p", "Je kan aan een getal zien of het deelbaar is, zonder te rekenen:"),
            ("kader", "<p style='margin:0 0 4px'><strong>Door 2</strong> — als het eindigt op 0, 2, 4, 6 of 8.</p>"
                      "<p style='margin:0 0 4px'><strong>Door 5</strong> — als het eindigt op 0 of 5.</p>"
                      "<p style='margin:0 0 4px'><strong>Door 3</strong> — tel de cijfers op; is die som deelbaar door 3, dan het hele getal ook. (471 → 4+7+1 = 12 → ja)</p>"
                      "<p style='margin:0'><strong>Door 9</strong> — net hetzelfde, maar de som moet deelbaar zijn door 9.</p>"),
            ("p", "Een <strong>priemgetal</strong> heeft precies twee delers: 1 en zichzelf. 2, 3, 5, 7, 11 en 13 zijn priemgetallen. Het getal 1 niet, want dat heeft er maar één."),
        ]),
    ],
    onthoud=[
        "De plaats van een cijfer bepaalt zijn waarde.",
        "Afronden: kijk naar het cijfer rechts ervan. 5 of meer gaat naar boven.",
        "0,7 is hetzelfde als 0,70 — vul aan met nullen voor je vergelijkt.",
        "Hoe groter de noemer, hoe kleiner het stukje.",
        "Procent is per honderd. 10% is delen door 10.",
        "Bij negatieve getallen is het grootst uitziende getal het kleinste.",
        "3/4, 0,75 en 75% zijn drie namen voor hetzelfde.",
        "Bij een getallenrij zoek je eerst de regel.",
    ])

# ───────────────────────────────────────────── 2. Bewerkingen
BUNDELS["bewerkingen"] = dict(
    vak=VAK, titel="Bewerkingen",
    onder="Optellen, aftrekken, vermenigvuldigen en delen — en in welke volgorde.",
    secties=[
        dict(kop="De volgorde van de bewerkingen", blokken=[
            ("p", "Staan er in één som verschillende bewerkingen, dan mag je niet zomaar van links naar rechts werken. Er is een vaste volgorde."),
            ("fig", svg.stappen(["Haakjes|eerst ( ) uitrekenen", "Maal en delen|× en :", "Plus en min|+ en −"]),
             "Bij 20 − 5 × 2 reken je dus eerst 5 × 2 = 10, en pas daarna 20 − 10 = 10."),
            ("p", "Haakjes zijn daarbij de baas: <strong>(12 − 4) × 5 = 40</strong>, maar zonder haakjes wordt 12 − 4 × 5 iets helemaal anders."),
        ]),
        dict(kop="Optellen en aftrekken", blokken=[
            ("p", "Bij het cijferen zet je de getallen onder elkaar, met de eenheden onder de eenheden. Kom je boven de 10, dan schuift er 1 door naar de kolom links."),
            ("kader", "<p style='margin:0 0 5px'><strong>476 + 358</strong> → 6+8 = 14, schrijf 4 en onthoud 1 · 7+5+1 = 13, schrijf 3 en onthoud 1 · 4+3+1 = 8. Samen <strong>834</strong>.</p>"
                      "<p style='margin:0'><strong>900 − 237</strong> → makkelijker in stappen: 900 − 200 = 700, dan − 37 = <strong>663</strong>.</p>"),
            ("p", "Bij optellen mag je de getallen van plaats wisselen, bij aftrekken niet. 7 + 3 en 3 + 7 zijn gelijk, maar 9 − 4 en 4 − 9 zeker niet."),
        ]),
        dict(kop="Vermenigvuldigen met een omweg", blokken=[
            ("p", "Grote maaltafels worden makkelijk als je ze in stukken hakt of een slimme omweg neemt."),
            ("fig", tabel(["Som", "Handige omweg", "Uitkomst"], [
                ["37 × 4", "30 × 4 = 120 en 7 × 4 = 28", "148"],
                ["16 × 50", "16 × 100 = 1 600, dan : 2", "800"],
                ["1 250 : 5", "× 2 = 2 500, dan : 10", "250"],
                ["24 × 25", "24 : 4 = 6, dan × 100", "600"],
                ["0,25 × 80", "een vierde van 80", "20"],
            ]), "Niet elke som vraagt om cijferen; vaak is omdenken sneller."),
            ("p", "Ook handig: maal 0 geeft altijd 0, en delen door 1 verandert niets."),
        ]),
        dict(kop="Delen, stap voor stap", blokken=[
            ("p", "Een grote deling hoef je niet in één keer te zien. Hak het getal in stukken die je wél kent, deel die apart, en tel de uitkomsten op."),
            ("kader", "<p style='margin:0 0 5px'><strong>756 : 7</strong> → 700 : 7 = 100 en 56 : 7 = 8. Samen <strong>108</strong>.</p>"
                      "<p style='margin:0'><strong>924 : 4</strong> → 800 : 4 = 200, 120 : 4 = 30 en 4 : 4 = 1. Samen <strong>231</strong>.</p>"),
            ("p", "Pas op voor de nul in het midden. Bij <strong>832 : 8</strong> gaat 8 één keer in de 8, nul keer in de 3, en vier keer in de 32. Dat geeft <strong>104</strong>, niet 14. Wie de nul vergeet te schrijven, komt tien keer te laag uit."),
        ]),
        dict(kop="Rekenen met breuken", blokken=[
            ("p", "Hebben twee breuken dezelfde noemer, dan tel je gewoon de tellers op of trek je ze af. De noemer blijft staan."),
            ("kader", "<p style='margin:0 0 4px'><strong>3/4 − 1/4 = 2/4</strong>, en dat kan je vereenvoudigen tot <strong>1/2</strong>.</p>"
                      "<p style='margin:0'><strong>2/3 van 90</strong> → deel eerst door 3 (= 30), neem er dan 2 (= 60).</p>"),
            ("p", "Zijn de noemers verschillend, dan maak je ze eerst gelijk. 1/2 wordt 2/4, en dan kan je 2/4 + 1/4 = 3/4 rekenen."),
        ]),
        dict(kop="Rekenen met procent", blokken=[
            ("p", "Bijna elke procentvraag los je op via 10% of via 1%."),
            ("fig", svg.stappen(["10% zoeken|deel door 10", "Vermenigvuldigen|× hoeveel tienden", "Klaar|lees je antwoord"], kleur=svg.AMBER),
             "20% van 250: 10% is 25, dus 20% is 50."),
            ("p", "Zoek je 15%, dan neem je 10% plus de helft daarvan. Zoek je 25%, dan is delen door 4 het snelst."),
        ]),
        dict(kop="Kommagetallen in een som", blokken=[
            ("p", "Bij optellen en aftrekken zet je de komma's netjes onder elkaar. 4,50 + 2,75 = 7,25."),
            ("p", "Bij delen reken je eerst zonder komma en zet je ze achteraf terug: 48 : 4 = 12, dus <strong>4,8 : 4 = 1,2</strong>."),
            ("weetje", "Een rekenmachine schrijft 1.2 met een punt. Op je blad schrijf je 1,2 met een komma. Hetzelfde getal."),
        ]),
    ],
    onthoud=[
        "Eerst haakjes, dan maal en delen, dan plus en min.",
        "Bij optellen mag je wisselen, bij aftrekken en delen niet.",
        "Hak een grote maalsom in stukken: 37 × 4 = 30 × 4 + 7 × 4.",
        "Gelijke noemers? Dan tel je gewoon de tellers op.",
        "Procent: zoek eerst 10% en reken van daaruit verder.",
        "Zet bij kommagetallen de komma's onder elkaar.",
        "Hak een grote deling in stukken die je kent.",
    ])

# ───────────────────────────────────────────── 3. Meten en metend rekenen
BUNDELS["meten-en-metend-rekenen"] = dict(
    vak=VAK, titel="Meten en metend rekenen",
    onder="Lengte, inhoud, massa, tijd en temperatuur — en hoe je ze omrekent.",
    secties=[
        dict(kop="De maatladder", blokken=[
            ("p", "Eenheden van lengte volgen elkaar op met telkens een stap van tien. Ga je naar rechts op de ladder, dan vermenigvuldig je met 10; ga je naar links, dan deel je door 10."),
            ("fig", svg.maatladder(["km", "hm", "dam", "m", "dm", "cm", "mm"]),
             "3,5 m is drie stappen naar rechts tot cm: 350 cm."),
            ("p", "Voor inhoud (kl, hl, dal, l, dl, cl, ml) en voor massa (kg, hg, dag, g, dg, cg, mg) werkt precies dezelfde ladder."),
            ("p", "De voorvoegsels zeggen precies hoeveel. <strong>Kilo</strong> is duizend, <strong>hecto</strong> honderd, <strong>deca</strong> tien, <strong>deci</strong> een tiende, <strong>centi</strong> een honderdste en <strong>milli</strong> een duizendste. Een hectometer is dus honderd meter — de hectometerpaaltjes langs de snelweg staan om de 100 meter — en in één liter gaan 100 centiliter."),
            ("weetje", "1 liter is 1 000 milliliter, 1 kilogram is 1 000 gram, en 1 ton is 1 000 kilogram. Telkens drie stappen, dus drie keer tien."),
        ]),
        dict(kop="Omtrek en oppervlakte", blokken=[
            ("p", "De <strong>omtrek</strong> is de lengte van de lijn rond een figuur: wat je nodig hebt voor een omheining. De <strong>oppervlakte</strong> is het aantal vierkantjes dat erin past: wat je nodig hebt voor tegels of verf."),
            ("fig", svg.rechthoek_maten(8, 5, 340),
             "Omtrek: 8 + 5 + 8 + 5. Oppervlakte: 8 × 5, dus 40 vierkantjes van 1 cm²."),
            ("p", "Bij een vierkant zijn alle zijden gelijk: omtrek is zijde × 4, oppervlakte is zijde × zijde. Een vierkant van 9 cm heeft dus een oppervlakte van 81 cm²."),
            ("p", "Je kan de som ook omdraaien. Ken je de oppervlakte en één zijde, dan vind je de andere door te delen: een rechthoek van 48 cm² die 6 cm breed is, is 48 : 6 = <strong>8 cm</strong> lang. En een vierkant van 36 cm² heeft een zijde van <strong>6 cm</strong>, want 6 × 6 = 36."),
        ]),
        dict(kop="Vierkante en kubieke eenheden", blokken=[
            ("p", "Bij gewone lengte is elke stap maal of gedeeld door 10. Bij oppervlakte tellen twee richtingen mee, dus is elke stap maal of gedeeld door <strong>100</strong>. Bij inhoud zijn het er drie, dus maal of gedeeld door <strong>1 000</strong>."),
            ("fig", tabel(["1 van deze", "is zoveel van die"], [
                ["1 m²", "100 dm²"],
                ["1 dm²", "100 cm²"],
                ["1 cm²", "100 mm²"],
                ["1 dm³", "1 000 cm³"],
                ["1 dm³", "1 liter"],
            ], "70%"), "Een vierkante meter is dus honderd vierkante decimeter, niet tien."),
            ("p", "Teken het gerust eens na: in een vierkant van 1 m op 1 m passen tien rijen van tien vierkantjes van 1 dm. Tien keer tien is honderd. Daarom springt de maatladder bij oppervlakte twee plaatsen tegelijk."),
        ]),
        dict(kop="Inhoud van een balk", blokken=[
            ("p", "Bij een ruimtefiguur komt er een derde maat bij: de hoogte. De inhoud is lengte × breedte × hoogte."),
            ("kader", "<p style='margin:0'>Een balk van 4 cm bij 3 cm bij 2 cm heeft een inhoud van 4 × 3 × 2 = <strong>24 cm³</strong>. Dat zijn 24 blokjes van één kubieke centimeter.</p>"),
            ("p", "Bij een <strong>kubus</strong> zijn alle ribben even lang, dus wordt het ribbe × ribbe × ribbe. Een kubus met een ribbe van 3 cm heeft een inhoud van 3 × 3 × 3 = <strong>27 cm³</strong>."),
            ("p", "Let op de eenheid: cm voor lengte, cm² voor oppervlakte en cm³ voor inhoud. Het kleine cijfer zegt hoeveel richtingen je vermenigvuldigd hebt."),
        ]),
        dict(kop="De klok en de kalender", blokken=[
            ("p", "Tijd rekent niet met tien maar met zestig. Een uur heeft 60 minuten, een minuut 60 seconden."),
            ("fig", svg.naast_elkaar([svg.klok(14, 10), svg.klok(7, 45)]),
             "Links 14.10 u, rechts 7.45 u — of kwart voor acht."),
            ("p", "Duurt iets 50 minuten vanaf 13.20 u, reken dan eerst tot het volgende hele uur (40 minuten tot 14.00 u) en tel de rest erbij: 14.10 u."),
            ("fig", tabel(["Eenheid", "Hoeveel"], [
                ["1 kwartier", "15 minuten = 900 seconden"],
                ["1 uur", "60 minuten = 3 600 seconden"],
                ["1 dag", "24 uur"],
                ["1 jaar", "12 maanden ≈ 52 weken = 365 dagen"],
                ["1 schrikkeljaar", "366 dagen (om de 4 jaar)"],
            ], "80%"), "Handig om uit het hoofd te kennen."),
        ]),
        dict(kop="Welke eenheid kies je?", blokken=[
            ("p", "Een goede eenheid geeft een getal dat je vlot kan uitspreken. De afstand tussen Hasselt en Genk in millimeter uitdrukken kan perfect, maar niemand doet het."),
            ("fig", tabel(["Wat je meet", "Handigste eenheid"], [
                ["de afstand tussen twee steden", "kilometer"],
                ["de lengte van je tafel", "meter of centimeter"],
                ["de dikte van een blad", "millimeter"],
                ["het water in een badkuip", "liter"],
                ["een lepel siroop", "milliliter"],
                ["een zak aardappelen", "kilogram"],
                ["een brief", "gram"],
            ], "80%"), "Kies de eenheid waarin het getal noch heel groot noch heel klein wordt."),
            ("p", "Moet je twee maten vergelijken, zet ze dan eerst allemaal in dezelfde eenheid. 500 g, 0,75 kg, 1,2 g en 200 g worden zo 500 g, <strong>750 g</strong>, 1,2 g en 200 g. Pas dan zie je dat 0,75 kg het zwaarst is."),
        ]),
        dict(kop="Temperatuur", blokken=[
            ("p", "We meten temperatuur in graden Celsius. Water bevriest bij 0 °C en kookt bij 100 °C."),
            ("fig", svg.getallenlijn(470, -20, 40, [
                (-20, "-20°", svg.INK, False), (0, "vriespunt", "#3b6ea5", True),
                (20, "kamer", svg.FOREST, False), (37, "lichaam", svg.AMBER, True),
                (40, "40°", svg.INK, False)]),
             "Onder nul gaan de graden verder met een minteken."),
            ("p", "Hoe lager het getal onder nul, hoe kouder het is: -12 °C is kouder dan -3 °C."),
        ]),
    ],
    onthoud=[
        "Elke stap op de maatladder is maal of gedeeld door 10.",
        "1 liter = 1 000 ml, 1 kg = 1 000 g, 1 ton = 1 000 kg.",
        "Omtrek is rond de figuur, oppervlakte is erin.",
        "Oppervlakte in cm², inhoud in cm³.",
        "Tijd rekent met 60, niet met 10.",
        "Reken bij tijd eerst tot het volgende hele uur.",
        "Bij oppervlakte is elke stap maal of gedeeld door 100, bij inhoud door 1 000.",
        "Vergelijken? Zet eerst alles in dezelfde eenheid.",
    ])

# ───────────────────────────────────────────── 4. Meetkunde
BUNDELS["meetkunde"] = dict(
    vak=VAK, titel="Meetkunde",
    onder="Hoeken, vlakke figuren, ruimtefiguren en de cirkel.",
    secties=[
        dict(kop="Hoeken", blokken=[
            ("p", "Een hoek meet je in graden. De rechte hoek van 90° is het ijkpunt: daarmee vergelijk je alle andere."),
            ("fig", svg.hoekenrij(470), "Scherp is kleiner dan 90°, stomp ligt tussen 90° en 180°, gestrekt is precies 180°."),
            ("p", "Een volledige draai is 360°, een halve draai 180°, een kwartdraai 90°. Twee lijnen die elkaar onder 90° kruisen, noem je <strong>loodrecht</strong>."),
        ]),
        dict(kop="Vlakke figuren", blokken=[
            ("p", "Vlakke figuren liggen plat op het blad. Je herkent ze aan het aantal zijden en aan de hoeken."),
            ("fig", svg.vormenrij(470), "Een vierkant is ook een rechthoek: alle vier de hoeken zijn recht."),
            ("fig", tabel(["Figuur", "Waaraan je hem herkent"], [
                ["vierkant", "vier gelijke zijden én vier rechte hoeken"],
                ["rechthoek", "vier rechte hoeken, overstaande zijden gelijk"],
                ["ruit", "vier gelijke zijden, maar de hoeken hoeven niet recht te zijn"],
                ["trapezium", "een vierhoek met minstens één paar evenwijdige zijden"],
                ["gelijkzijdige driehoek", "drie gelijke zijden"],
                ["gelijkbenige driehoek", "twee gelijke zijden"],
            ]), "De hoeken van elke driehoek zijn samen 180°, die van elke vierhoek 360°."),
            ("p", "Een figuur met rechte zijden noemen we naar het aantal zijden: drie is een driehoek, vier een vierhoek, vijf een vijfhoek, zes een <strong>zeshoek</strong> en acht een <strong>achthoek</strong> — zoals een stopbord in het verkeer."),
            ("p", "Twee lijnen die overal even ver uit elkaar liggen, noem je <strong>evenwijdig</strong>. Hoe ver je ze ook doortrekt, ze raken elkaar nooit. De twee lange zijden van een rechthoek zijn evenwijdig; een trapezium heeft er minstens één paar."),
        ]),
        dict(kop="Symmetrie en verschuiven", blokken=[
            ("p", "Kan je een figuur langs een lijn dubbelvouwen zodat de twee helften precies op elkaar passen, dan is die lijn een <strong>symmetrieas</strong>. Een vierkant heeft er vier, een rechthoek twee, een cirkel oneindig veel."),
            ("p", "Niet elke figuur heeft er vier. Een gelijkbenige driehoek heeft er precies <strong>één</strong>: de lijn door de top, tussen de twee even lange zijden in. Een gelijkzijdige driehoek heeft er drie, en een figuur zonder gelijke zijden vaak geen enkele."),
            ("p", "Bij een spiegeling of een verschuiving blijft de figuur even groot en houdt ze dezelfde vorm. Alleen haar plaats verandert."),
        ]),
        dict(kop="De cirkel", blokken=[
            ("p", "Een cirkel heeft geen zijden en geen hoeken: het is één gebogen lijn waarvan elk punt even ver van het midden ligt."),
            ("fig", svg.cirkel_straal(300), "De diameter is precies twee keer de straal."),
            ("p", "Is de straal 6 cm, dan is de diameter 12 cm. En omgekeerd: is de diameter 10 cm, dan is de straal 5 cm."),
        ]),
        dict(kop="Ruimtefiguren", blokken=[
            ("p", "Ruimtefiguren nemen plaats in: je kan ze vastnemen. Je telt er vlakken, ribben en hoekpunten aan."),
            ("fig", svg.ruimtefiguren(470), "Een kubus en een balk hebben allebei 6 vlakken, 12 ribben en 8 hoekpunten."),
            ("fig", tabel(["Figuur", "Vlakken", "Bijzonder"], [
                ["kubus", "6 gelijke vierkanten", "alle ribben even lang"],
                ["balk", "6 rechthoeken", "zoals een schoendoos"],
                ["cilinder", "2 cirkels + een gebogen vlak", "zoals een blikje"],
                ["kegel", "1 cirkel + een punt", "zoals een ijshoorntje"],
                ["piramide", "1 grondvlak + driehoeken", "de driehoeken komen samen in één top"],
                ["bol", "geen enkel vlak vlak", "rolt alle kanten op"],
            ]), None),
            ("p", "Tel je de vlakken van een <strong>piramide met een vierkant grondvlak</strong>, dan kom je aan vijf: het vierkant onderaan plus de vier driehoeken errond. Vergeet het grondvlak niet mee te tellen, dat is de fout die iedereen maakt."),
        ]),
    ],
    onthoud=[
        "Een rechte hoek is 90°, een volledige draai 360°.",
        "De hoeken van een driehoek zijn samen 180°, van een vierhoek 360°.",
        "Een vierkant is ook een rechthoek, maar niet omgekeerd.",
        "De diameter is twee keer de straal.",
        "Een kubus en een balk: 6 vlakken, 12 ribben, 8 hoekpunten.",
        "Spiegelen en verschuiven verandert niets aan de grootte.",
        "Evenwijdige lijnen raken elkaar nooit.",
        "Een piramide met een vierkant grondvlak heeft 5 vlakken.",
    ])

# ───────────────────────────────────────────── 5. Kansrekenen en statistiek
BUNDELS["kansrekenen-en-statistiek"] = dict(
    vak=VAK, titel="Kansrekenen en statistiek",
    onder="Hoe groot is de kans, wat is het gemiddelde, en wat lees je af uit een grafiek?",
    secties=[
        dict(kop="Kans", blokken=[
            ("p", "Een kans zegt hoe waarschijnlijk iets is. Je schrijft ze als een breuk: het aantal keren dat het kan lukken, op het totaal aantal mogelijkheden."),
            ("fig", svg.naast_elkaar([svg.dobbelsteen(n) for n in (1, 2, 3, 4, 5, 6)], 10),
             "Een dobbelsteen heeft zes zijden, dus de kans op een 4 is 1 op 6."),
            ("p", "De kans op een even getal is 3 op 6, want 2, 4 en 6 tellen mee. Dat is hetzelfde als 1/2."),
            ("kader", "<p style='margin:0 0 4px'><strong>Kans 0</strong> — het gebeurt nooit. De kans op een 7 met één dobbelsteen.</p>"
                      "<p style='margin:0'><strong>Kans 1</strong> — het gebeurt zeker. Een kans kan dus nooit groter zijn dan 1.</p>"),
        ]),
        dict(kop="Wat je mag verwachten", blokken=[
            ("p", "Gooi je 60 keer met een dobbelsteen, dan verwacht je ongeveer 10 keer een zes: 60 gedeeld door 6. In het echt wordt het zelden precies 10."),
            ("p", "Hoe vaker je gooit, hoe dichter het resultaat bij de verwachting komt. Bij tien worpen kan het alle kanten op, bij duizend worpen bijna niet meer."),
            ("weetje", "Een muntstuk heeft geen geheugen. Vijf keer kop na elkaar verandert niets aan de kans op de zesde worp: nog altijd 1 op 2."),
        ]),
        dict(kop="Het gemiddelde", blokken=[
            ("p", "Het gemiddelde vind je door alles op te tellen en te delen door het aantal getallen."),
            ("fig", svg.staafdiagram([("6", 6), ("8", 8), ("8", 8), ("10", 10)], 300, 160),
             "6 + 8 + 8 + 10 = 32, gedeeld door 4 getallen geeft een gemiddelde van 8."),
            ("p", "Het gemiddelde ligt altijd tussen het kleinste en het grootste getal van de rij. Komt er iets daarbuiten uit, dan heb je je vergist."),
        ]),
        dict(kop="Het vaakst en het middelste", blokken=[
            ("p", "Naast het gemiddelde zijn er nog twee manieren om een rij getallen in één cijfer samen te vatten."),
            ("kader", "<p style='margin:0 0 4px'><strong>Het vaakst</strong> — welk getal komt het meeste voor? Bij 12, 15, 15 en 18 graden is dat 15.</p>"
                      "<p style='margin:0'><strong>Het middelste</strong> — zet de getallen op volgorde en neem het midden. Bij 3, 5, 7, 9 en 11 is dat 7.</p>"),
            ("p", "Het middelste vind je alleen na sorteren. Staat de rij nog door elkaar, dan zegt het getal dat toevallig in het midden van je blad staat helemaal niets."),
        ]),
        dict(kop="Van aantal naar deel en procent", blokken=[
            ("p", "Vaak vragen ze niet hoeveel er zijn, maar welk <em>deel</em> dat is. Schrijf het dan eerst als een breuk: het aantal dat meetelt, op het totaal. Daarna vereenvoudig je, en als het gevraagd wordt reken je door naar procent."),
            ("kader", "<p style='margin:0 0 4px'>8 van de 20 kinderen hebben een huisdier → 8/20, en dat is <strong>2/5</strong>.</p>"
                      "<p style='margin:0 0 4px'>5 van de 20 komen met de fiets → 5/20 = 1/4 = <strong>25%</strong>.</p>"
                      "<p style='margin:0'>10 van de 50 komen te voet → dat is hetzelfde als 20 van de 100, dus <strong>20%</strong>.</p>"),
            ("p", "Die laatste stap is de handigste van allemaal: reken je deel om naar <em>hoeveel op honderd</em>. Procent betekent letterlijk per honderd, dus dan staat het antwoord er meteen."),
        ]),
        dict(kop="Grafieken lezen", blokken=[
            ("p", "Elke grafiek heeft zijn eigen werk. Kies je de verkeerde, dan verstop je net wat je wil tonen."),
            ("fig", svg.naast_elkaar([
                svg.staafdiagram([("ma", 3), ("di", 5), ("wo", 2), ("do", 6), ("vr", 4)], 250, 160),
                svg.lijngrafiek([3, 5, 4, 7, 9], 250, 160, ["ma", "di", "wo", "do", "vr"]),
            ]), "Links een staafdiagram om te vergelijken, rechts een lijngrafiek om verandering te tonen."),
            ("fig", svg.taartdiagram([("1/2", .5, svg.FOREST), ("1/4", .25, svg.AMBER), ("1/4", .25, "#3b6ea5")]),
             "Een cirkeldiagram toont hoe een geheel verdeeld is in delen."),
            ("p", "Een staafdiagram lees je af op de as waar de getallen staan: je kijkt tot waar de staaf komt en leest daar het getal af. In een tabel lees je af via de rij en de kolom: je zoekt waar die twee elkaar kruisen."),
        ]),
    ],
    onthoud=[
        "Een kans is: het aantal gunstige gevallen op het totaal.",
        "Een kans ligt altijd tussen 0 en 1.",
        "Gemiddelde = alles optellen, delen door hoeveel getallen er zijn.",
        "Het gemiddelde ligt tussen het kleinste en het grootste getal.",
        "Staafdiagram om te vergelijken, lijngrafiek voor verandering, cirkeldiagram voor delen van een geheel.",
        "Het middelste getal vind je pas nadat je gesorteerd hebt.",
        "Een deel op honderd is een procent.",
    ])

# ───────────────────────────────────────────── 6. Vraagstukken
BUNDELS["vraagstukken-en-problemen-oplossen"] = dict(
    vak=VAK, titel="Vraagstukken en problemen oplossen",
    onder="Een stappenplan om van een verhaaltje naar het juiste antwoord te gaan.",
    secties=[
        dict(kop="Het stappenplan", blokken=[
            ("p", "Een vraagstuk is geen rekenoefening maar een verhaaltje. Het moeilijkste is niet het rekenen, wel uitzoeken <em>wat</em> je moet rekenen."),
            ("fig", svg.stappen(["Lees|wat wordt gevraagd?", "Zoek|welke getallen tellen mee?", "Reken|kies de bewerking", "Kijk na|kan dit kloppen?"]),
             "Begin bij de vraag, niet bij de getallen. Dan weet je meteen wat je nodig hebt."),
            ("p", "Schrijf je antwoord altijd met de eenheid erbij: 16 euro, 45 vierkante meter, 9 dagen. Een kaal getal is maar een half antwoord."),
        ]),
        dict(kop="Welke bewerking hoort erbij?", blokken=[
            ("fig", tabel(["Wat er in het verhaaltje staat", "Wat je doet"], [
                ["samen, erbij, in totaal", "optellen"],
                ["hoeveel blijft er over, verschil, hoeveel meer", "aftrekken"],
                ["evenveel keer, rijen van, per stuk", "vermenigvuldigen"],
                ["eerlijk verdelen, hoeveel passen erin", "delen"],
                ["korting, deel van een geheel", "procent of breuk"],
            ]), "Die woorden zijn een goede gids, maar lees altijd het hele verhaaltje na."),
        ]),
        dict(kop="Verhoudingen en prijs per stuk", blokken=[
            ("p", "Staat er <em>1 op 3</em> of <em>3 van elke 5</em>, dan gaat het over een verhouding. Je verdeelt het geheel eerst in even grote groepjes, en daarna neem je er zoveel als gevraagd wordt."),
            ("kader", "<p style='margin:0 0 4px'><strong>1 op 3 van 30 kinderen</strong> → 30 : 3 = <strong>10 kinderen</strong>.</p>"
                      "<p style='margin:0'><strong>3 van elke 5, in een klas van 25</strong> → 25 : 5 = 5 groepjes, en 3 × 5 = <strong>15 kinderen</strong>.</p>"),
            ("p", "Bij een prijs werkt het net zo. Kosten 3 pakken melk samen 4,50 euro, dan kost één pak 4,50 : 3 = 1,50 euro. En dubbel zoveel kost dubbel zoveel: zijn 4 broden 6 euro, dan zijn 8 broden 12 euro."),
            ("p", "Wordt er iets opgegeten of weggenomen, dan is wat overblijft ook een breuk. Van een pizza in 8 stukken waarvan je er 3 opeet, blijft <strong>5/8</strong> over. Van een taart in 12 stukken waarvan er 9 op zijn, blijft 3/12 over, en dat vereenvoudig je tot <strong>1/4</strong>."),
        ]),
        dict(kop="Vraagstukken met geld", blokken=[
            ("kader", "<p style='margin:0 0 5px'><strong>Je hebt 100 euro. Schoenen kosten 55 euro, een broek 29 euro. Hoeveel hou je over?</strong></p>"
                      "<p style='margin:0'>Eerst samen: 55 + 29 = 84. Dan aftrekken: 100 − 84 = <strong>16 euro</strong>.</p>"),
            ("p", "Bij korting reken je eerst hoeveel de korting waard is, en trek je die af. Op een jas van 80 euro met 20% korting: 20% van 80 is 16, dus je betaalt 64 euro."),
        ]),
        dict(kop="Vraagstukken met meten", blokken=[
            ("p", "Hier is de vraag altijd: gaat het om de lijn rond iets (omtrek), om het vlak erbinnen (oppervlakte), of om de ruimte erin (inhoud)?"),
            ("fig", svg.stappen(["Omheining|rond de tuin|→ omtrek", "Tegels of verf|op het vlak|→ oppervlakte", "Water of zand|erin|→ inhoud"], kleur=svg.AMBER),
             "Een terras van 9 m op 5 m betegelen vraagt de oppervlakte: 45 m²."),
            ("p", "Let op de eenheden: staan er liters en milliliters door elkaar, zet ze dan eerst allemaal in dezelfde eenheid."),
        ]),
        dict(kop="Vraagstukken met tijd en snelheid", blokken=[
            ("p", "Reken bij tijd altijd via het volgende hele uur. Een trein vertrekt om 9.35 u en rijdt 1 uur en 40 minuten: eerst een uur later is 10.35 u, dan nog 40 minuten geeft 11.15 u."),
            ("p", "Bij snelheid geldt: 20 km per uur betekent 10 km in een half uur en 5 km in een kwartier. Je deelt de afstand net zoals je de tijd deelt."),
            ("weetje", "Een tijd van 11.75 u bestaat niet. Na 59 minuten komt een nieuw uur, want de klok telt tot 60 en niet tot 100."),
        ]),
        dict(kop="Nakijken", blokken=[
            ("p", "Lees je antwoord nog eens samen met de vraag. Kan dit kloppen? Als drie vrienden 84 knikkers verdelen en je krijgt er 240 per persoon uit, dan weet je meteen dat er iets mis is."),
            ("p", "Een goede test is omgekeerd rekenen: 84 : 3 = 28, en 28 × 3 = 84. Klopt."),
        ]),
    ],
    onthoud=[
        "Lees eerst wat er gevraagd wordt, pas daarna de getallen.",
        "Niet elk getal in het verhaaltje heb je nodig.",
        "Schrijf de eenheid bij je antwoord.",
        "Omheining is omtrek, tegels zijn oppervlakte, water is inhoud.",
        "Zet alles eerst in dezelfde eenheid.",
        "Kijk na met omgekeerd rekenen.",
        "1 op 3 betekent: eerst delen door 3.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
