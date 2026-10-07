# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij wiskunde basis 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere opgaven, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: andere
getallen, andere contexten, en opdrachten die je enkel op papier kan maken —
een tabel aanvullen, een grafiek schetsen, een berekening in stappen
opschrijven. Wie hier iets bijschrijft, legt het eerst naast
`../../boost-doorstroom/wiskunde-basis.json` en naast `maak_wiskunde_basis.py`.

Elk cijfer in dit bestand is nagerekend. Wie een getal verandert, rekent het
antwoord opnieuw uit en zet het ook op het antwoordblad goed.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Wiskunde basis"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
NIVEAU = "-boost-doorstroom"
VOOR = "oefenbundel-"

W = "110px"
WW = "185px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf je tussenstappen op. Een antwoord zonder berekening is niet na te kijken.",
    "Zet bij elk antwoord de eenheid, als er een is.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("de-reele-getallen-wortels-en-machten",
    titel="De reële getallen, wortels en machten",
    reeksen=[
        dict(kop="In welke verzameling hoort het thuis?",
             opdracht="Schrijf de kleinste verzameling op waarin het getal zit: "
                      "ℕ, ℤ, ℚ of ℝ \\ ℚ.",
             oefeningen=[
                 ("rij", [("7", "ℕ"), ("−4", "ℤ"), ("0,75", "ℚ"),
                          ("√9", "ℕ"), ("√2", "ℝ \\ ℚ"), ("π", "ℝ \\ ℚ")],
                  "Welke verzameling?", W),
                 ("open", "Waarom is √9 geen irrationaal getal en √2 wel?",
                  "√9 is precies 3, dus een natuurlijk getal. √2 is geen breuk van twee gehele "
                  "getallen en heeft een oneindige, niet herhalende decimale uitbreiding.", 3),
             ]),
        dict(kop="Rekenen met machten",
             opdracht="Vereenvoudig tot één macht.",
             oefeningen=[
                 ("rij", [("2³ · 2⁵", "2⁸"), ("a⁷ : a³", "a⁴"),
                          ("(3²)⁴", "3⁸"), ("5⁰", "1"),
                          ("x⁻²", "1/x²"), ("(2a³)²", "4a⁶")],
                  "Vereenvoudig.", W),
                 ("rij", [("2⁻³", "1/8"), ("10⁵", "100000"),
                          ("(−3)²", "9"), ("−3²", "−9"),
                          ("(1/2)⁻¹", "2"), ("(2/3)²", "4/9")],
                  "Reken uit.", W),
                 ("open", "Leg uit waarom (−3)² en −3² niet hetzelfde zijn.",
                  "Bij (−3)² staat het minteken binnen de haakjes en wordt het mee gekwadrateerd, "
                  "dus 9. Bij −3² werkt het kwadraat alleen op de 3, en het minteken komt er "
                  "daarna bij: −9.", 3),
             ]),
        dict(kop="Wortels",
             opdracht="Vereenvoudig of reken uit.",
             oefeningen=[
                 ("rij", [("√49", "7"), ("√50", "5√2"),
                          ("√12 + √27", "5√3"), ("√8 · √2", "4"),
                          ("√(16/25)", "4/5"), ("3√5 − √5", "2√5")],
                  "Vereenvoudig.", W),
                 ("open", "Toon met tussenstappen hoe je √12 + √27 vereenvoudigt.",
                  "√12 = √(4·3) = 2√3 en √27 = √(9·3) = 3√3. Samen 2√3 + 3√3 = 5√3.", 3),
                 ("open", "Maak de noemer rationaal: 6 / √3.",
                  "6/√3 = 6√3 / 3 = 2√3.", 2),
             ]),
        dict(kop="Wetenschappelijke notatie",
             opdracht="Schrijf om.",
             oefeningen=[
                 ("rij", [("43 000", "4,3 · 10⁴"), ("0,0052", "5,2 · 10⁻³"),
                          ("6,1 · 10⁵", "610 000"), ("2,4 · 10⁻²", "0,024"),
                          ("(3 · 10⁴) · (2 · 10³)", "6 · 10⁷"),
                          ("(8 · 10⁶) : (4 · 10²)", "2 · 10⁴")],
                  "Schrijf om of reken uit.", WW),
                 ("open", "Een lichtjaar is ongeveer 9,46 · 10¹² km. Hoeveel km is drie "
                          "lichtjaar? Geef het antwoord in wetenschappelijke notatie.",
                  "3 · 9,46 · 10¹² = 28,38 · 10¹² = 2,838 · 10¹³ km.", 3),
             ]),
    ])


# ============================================================
zet("getallen-ordenen-afronden-en-intervallen",
    titel="Getallen ordenen, afronden en intervallen",
    reeksen=[
        dict(kop="Ordenen",
             opdracht="Zet van klein naar groot.",
             oefeningen=[
                 ("open", "0,7 · 3/4 · 0,68 · 7/10",
                  "0,68 &lt; 0,7 = 7/10 &lt; 3/4", 2),
                 ("open", "−2,5 · −3 · −2,05 · 0",
                  "−3 &lt; −2,5 &lt; −2,05 &lt; 0", 2),
                 ("open", "√2 · 1,5 · 1,41 · 3/2",
                  "1,41 &lt; √2 &lt; 1,5 = 3/2", 2),
                 ("open", "Hoe vergelijk je 3/7 en 4/9 zonder rekenmachine?",
                  "Gelijknamig maken: 3/7 = 27/63 en 4/9 = 28/63, dus 3/7 &lt; 4/9.", 3),
             ]),
        dict(kop="Afronden",
             opdracht="Rond af zoals gevraagd.",
             oefeningen=[
                 ("rij", [("3,4567 op 2 decimalen", "3,46"),
                          ("12 849 op honderdtallen", "12 800"),
                          ("0,00472 op 3 beduidende cijfers", "0,00472"),
                          ("2,5 op een geheel getal", "3"),
                          ("149,95 op 1 decimaal", "150,0"),
                          ("0,0996 op 2 decimalen", "0,10")],
                  "Wat is het afgeronde getal?", WW),
                 ("open", "Een winkel verkoopt 3 stuks voor 10 euro. Wat kost één stuk, "
                          "afgerond op een cent, en waarom klopt drie keer dat bedrag niet "
                          "precies?",
                  "10 : 3 = 3,333... dus 3,33 euro. Drie keer 3,33 is 9,99: door het afronden "
                  "gaat er een cent verloren.", 3),
                 ("open", "Waarom rond je bij een eindantwoord pas af en niet tussenin?",
                  "Elke tussentijdse afronding voegt een foutje toe, en die fouten stapelen op. "
                  "Het eindantwoord wordt dan onnauwkeuriger dan nodig.", 3),
             ]),
        dict(kop="Intervallen",
             opdracht="Schrijf het interval op in haakjesnotatie.",
             oefeningen=[
                 ("rij", [("alle x groter dan 2 en kleiner dan of gelijk aan 7", "]2, 7]"),
                          ("alle x vanaf −3 tot en met 0", "[−3, 0]"),
                          ("alle x kleiner dan 5", "]−∞, 5["),
                          ("alle x groter dan of gelijk aan 1", "[1, +∞["),
                          ("alle x tussen −1 en 1, grenzen niet erbij", "]−1, 1["),
                          ("alle reële getallen", "]−∞, +∞[")],
                  "Welk interval is dit?", WW),
                 ("open", "Wat is de doorsnede van [0, 6] en ]4, 9[?",
                  "]4, 6]", 2),
                 ("open", "Wat is de unie van ]−∞, 2[ en [2, +∞[?",
                  "Heel ℝ, dus ]−∞, +∞[.", 2),
                 ("open", "Waarom staat er bij +∞ altijd een open haakje?",
                  "Oneindig is geen getal, dus het kan nooit tot het interval behoren.", 2),
             ]),
    ])


# ============================================================
zet("logica-bewerkingen-en-waarheidstabellen",
    titel="Logica: bewerkingen en waarheidstabellen",
    reeksen=[
        dict(kop="Waar of niet waar?",
             opdracht="p is waar, q is niet waar. Bepaal de waarheidswaarde.",
             oefeningen=[
                 ("rij", [("p ∧ q", "niet waar"), ("p ∨ q", "waar"),
                          ("¬p", "niet waar"), ("¬q", "waar"),
                          ("p ⇒ q", "niet waar"), ("q ⇒ p", "waar")],
                  "Waar of niet waar?", WW),
                 ("open", "Waarom is q ⇒ p waar als q niet waar is?",
                  "Een implicatie is alleen vals als het eerste deel waar is en het tweede "
                  "niet. Met een vals eerste deel belooft de implicatie niets, dus ze is "
                  "waar.", 3),
             ]),
        dict(kop="Een waarheidstabel invullen",
             opdracht="Vul de tabel aan met W of N.",
             oefeningen=[
                 ("tabel", ["p", "q", "p ∧ q", "p ∨ q", "p ⇒ q"],
                  [["W", "W", None, None, None], ["W", "N", None, None, None],
                   ["N", "W", None, None, None], ["N", "N", None, None, None]],
                  "rij 1: W, W, W · rij 2: N, W, N · rij 3: N, W, W · rij 4: N, N, W",
                  "50px"),
                 ("tabel", ["p", "q", "¬p", "¬p ∨ q"],
                  [["W", "W", None, None], ["W", "N", None, None],
                   ["N", "W", None, None], ["N", "N", None, None]],
                  "rij 1: N, W · rij 2: N, N · rij 3: W, W · rij 4: W, W",
                  "50px"),
                 ("open", "Vergelijk de laatste kolom van beide tabellen. Wat besluit je?",
                  "¬p ∨ q heeft exact dezelfde waarden als p ⇒ q. De twee uitdrukkingen zijn "
                  "dus logisch gelijkwaardig.", 3),
             ]),
        dict(kop="Omkeren, omgekeerde en contrapositie",
             opdracht="Schrijf de gevraagde vorm op van: als het regent, dan is de straat nat.",
             oefeningen=[
                 ("open", "De omgekeerde implicatie.",
                  "Als de straat nat is, dan regent het.", 2),
                 ("open", "De contrapositie.",
                  "Als de straat niet nat is, dan regent het niet.", 2),
                 ("open", "Welke van de twee is zeker waar als de oorspronkelijke zin waar is?",
                  "De contrapositie. De omgekeerde implicatie hoeft niet waar te zijn: de "
                  "straat kan ook nat zijn van een sproeiwagen.", 3),
                 ("open", "Ontken de zin: alle leerlingen van deze klas hebben een fiets.",
                  "Er is minstens één leerling van deze klas die geen fiets heeft.", 2),
                 ("open", "Ontken de zin: er bestaat een getal waarvan het kwadraat negatief "
                          "is.",
                  "Voor elk getal geldt dat het kwadraat niet negatief is.", 2),
             ]),
    ])


# ============================================================
zet("redeneren-bewijzen-en-tegenvoorbeelden",
    titel="Redeneren, bewijzen en tegenvoorbeelden",
    reeksen=[
        dict(kop="Geef een tegenvoorbeeld",
             opdracht="Elke bewering hieronder is fout. Schrijf één tegenvoorbeeld op.",
             oefeningen=[
                 ("rij", [("Elk priemgetal is oneven.", "2"),
                          ("Als x² = 9, dan is x = 3.", "x = −3"),
                          ("Elke vierhoek met vier gelijke zijden is een vierkant.",
                           "een ruit die geen rechte hoeken heeft"),
                          ("Als a &gt; b, dan is a² &gt; b².", "a = 1 en b = −2"),
                          ("De som van twee oneven getallen is oneven.", "3 + 5 = 8"),
                          ("Elk getal deelbaar door 3 is deelbaar door 9.", "6")],
                  "Welk tegenvoorbeeld?", WW),
                 ("open", "Waarom volstaat één tegenvoorbeeld om een bewering te weerleggen, "
                          "terwijl honderd voorbeelden ze niet bewijzen?",
                  "Een bewering met 'elk' of 'alle' zegt iets over alle gevallen. Eén geval dat "
                  "niet klopt, maakt ze vals. Maar honderd kloppende gevallen zeggen niets over "
                  "het honderdeneerste.", 4),
             ]),
        dict(kop="Een bewijs schrijven",
             opdracht="Schrijf het bewijs uit met tussenstappen.",
             oefeningen=[
                 ("open", "Bewijs dat de som van twee even getallen even is.",
                  "Neem twee even getallen 2a en 2b met a en b geheel. De som is 2a + 2b = "
                  "2(a + b). Omdat a + b geheel is, is de som een veelvoud van 2, dus even.", 4),
                 ("open", "Bewijs dat het product van twee opeenvolgende gehele getallen even "
                          "is.",
                  "Van twee opeenvolgende getallen n en n+1 is er altijd één even. Een product "
                  "met een even factor is even.", 3),
                 ("open", "Bewijs dat (a + b)² = a² + 2ab + b².",
                  "(a + b)² = (a + b)(a + b) = a·a + a·b + b·a + b·b = a² + ab + ab + b² = "
                  "a² + 2ab + b².", 4),
             ]),
        dict(kop="Soorten redeneren",
             opdracht="Schrijf op of het inductief of deductief is.",
             oefeningen=[
                 ("rij", [("Ik tel de eerste tien priemgetallen en vermoed een patroon.",
                           "inductief"),
                          ("Alle vierkanten zijn rechthoeken, dit is een vierkant, dus het is "
                           "een rechthoek.", "deductief"),
                          ("Bij elke driehoek die ik meet komt 180° uit, dus dat zal altijd zo "
                           "zijn.", "inductief"),
                          ("Uit de stelling van Pythagoras volgt dat c = 5.", "deductief"),
                          ("Deze vijf leerlingen zijn moe, dus de hele klas is moe.",
                           "inductief"),
                          ("x + 3 = 7, dus x = 4.", "deductief")],
                  "Inductief of deductief?", WW),
                 ("open", "Waarom is een inductieve redenering in de wiskunde nooit een bewijs?",
                  "Ze besluit uit een aantal gevallen iets over alle gevallen. Dat kan een goed "
                  "vermoeden opleveren, maar zekerheid geeft alleen een deductief bewijs dat "
                  "voor elk geval geldt.", 4),
             ]),
    ])


# ============================================================
zet("ruimtefiguren-vlakke-voorstellingen-en-vectoren",
    titel="Ruimtefiguren, vlakke voorstellingen en vectoren",
    reeksen=[
        dict(kop="Ruimtefiguren herkennen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een balk: aantal hoekpunten, ribben, grensvlakken", "8, 12, 6"),
                          ("een driezijdig prisma: hoekpunten, ribben, grensvlakken",
                           "6, 9, 5"),
                          ("een vierzijdige piramide: hoekpunten, ribben, grensvlakken",
                           "5, 8, 5"),
                          ("de formule van Euler", "h − r + g = 2"),
                          ("de ontwikkeling van een cilinder", "twee cirkels en een rechthoek"),
                          ("de ontwikkeling van een kegel", "een cirkel en een cirkelsector")],
                  "Vul aan.", WL),
                 ("open", "Controleer de formule van Euler bij de balk.",
                  "8 − 12 + 6 = 2, dus ze klopt.", 2),
             ]),
        dict(kop="Rekenen aan ruimtefiguren",
             opdracht="Reken uit. Gebruik π ≈ 3,14 en rond af op één decimaal.",
             oefeningen=[
                 ("rij", [("volume balk 4 bij 5 bij 6", "120"),
                          ("volume cilinder r = 3, h = 10", "282,7"),
                          ("volume kegel r = 5, h = 12", "314,2"),
                          ("oppervlakte bol r = 6", "452,4"),
                          ("volume kubus met ribbe 7", "343"),
                          ("oppervlakte kubus met ribbe 7", "294")],
                  "Wat is het resultaat?", WW),
                 ("open", "Een cilindervormige regenton heeft een diameter van 60 cm en een "
                          "hoogte van 90 cm. Hoeveel liter gaat erin? Rond af op een liter.",
                  "r = 30 cm. V = π · 30² · 90 = π · 81 000 ≈ 254 469 cm³. Eén liter is "
                  "1 000 cm³, dus ongeveer 254 liter.", 4),
                 ("open", "Wat gebeurt er met het volume van een kubus als je elke ribbe "
                          "verdubbelt?",
                  "Het volume wordt acht keer zo groot, want 2³ = 8.", 2),
             ]),
        dict(kop="Vectoren",
             opdracht="Reken met de vectoren u = (3, −2) en v = (−1, 5).",
             oefeningen=[
                 ("rij", [("u + v", "(2, 3)"), ("u − v", "(4, −7)"),
                          ("2u", "(6, −4)"), ("−v", "(1, −5)"),
                          ("3u + v", "(8, −1)"), ("de lengte van u", "√13")],
                  "Wat is het resultaat?", WW),
                 ("open", "Een punt A(2, 1) wordt verschoven over de vector (−4, 3). Waar komt "
                          "het terecht?",
                  "In (−2, 4).", 2),
                 ("open", "Twee vectoren zijn evenwijdig als de ene een veelvoud is van de "
                          "andere. Zijn (2, 6) en (−3, −9) evenwijdig? Toon het.",
                  "Ja: (−3, −9) = −1,5 · (2, 6), dus ze zijn evenwijdig.", 3),
             ]),
    ])


# ============================================================
zet("schaalverandering-en-gelijkvormige-figuren",
    titel="Schaalverandering en gelijkvormige figuren",
    reeksen=[
        dict(kop="Schaal lezen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("schaal 1 : 25 000, op de kaart 7 cm", "1,75 km"),
                          ("schaal 1 : 100, op het plan 4,5 cm", "4,5 m"),
                          ("schaal 1 : 50 000, in het echt 12 km", "24 cm"),
                          ("schaal 2 : 1, voorwerp van 3 mm", "6 mm op de tekening"),
                          ("schaal 1 : 200, op het plan 8 cm", "16 m"),
                          ("schaal 1 : 20, in het echt 3 m", "15 cm")],
                  "Wat is het antwoord?", WW),
                 ("open", "Leg uit waarom een schaal 1 : 25 000 kleiner is dan 1 : 1 000, "
                          "terwijl 25 000 een groter getal is.",
                  "Hoe groter het tweede getal, hoe meer de werkelijkheid verkleind is. Bij "
                  "1 : 25 000 stelt één centimeter 250 meter voor, bij 1 : 1 000 maar tien "
                  "meter.", 3),
             ]),
        dict(kop="Lengte, oppervlakte en volume",
             opdracht="Vul de tabel aan met de factor.",
             oefeningen=[
                 ("tabel", ["schaalfactor k", "lengte ×", "oppervlakte ×", "volume ×"],
                  [["2", None, None, None], ["3", None, None, None],
                   ["1/2", None, None, None], ["10", None, None, None]],
                  "k = 2: 2, 4, 8 · k = 3: 3, 9, 27 · k = 1/2: 1/2, 1/4, 1/8 · "
                  "k = 10: 10, 100, 1000", "70px"),
                 ("open", "Een maquette is op schaal 1 : 50. Het echte gebouw heeft een "
                          "gevel van 200 m². Hoeveel is dat op de maquette?",
                  "De oppervlakte wordt gedeeld door 50² = 2 500. 200 m² : 2 500 = 0,08 m², "
                  "dus 800 cm².", 3),
                 ("open", "Een flesje van 0,5 liter wordt in alle richtingen twee keer zo "
                          "groot gemaakt. Hoeveel liter gaat er dan in?",
                  "Het volume wordt 2³ = 8 keer zo groot: 4 liter.", 2),
             ]),
        dict(kop="Gelijkvormige driehoeken",
             opdracht="Reken de ontbrekende zijde uit.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Driehoek ABC is gelijkvormig met driehoek DEF. "
                  "AB = 6, BC = 8, AC = 10 en DE = 9.</em></p>"),
                 ("kort", "Wat is de schaalfactor van ABC naar DEF?", "1,5", W),
                 ("kort", "Hoe lang is EF?", "12", W),
                 ("kort", "Hoe lang is DF?", "15", W),
                 ("open", "Een boom werpt een schaduw van 12 m. Een stok van 1,5 m werpt op "
                          "hetzelfde moment een schaduw van 2 m. Hoe hoog is de boom?",
                  "De driehoeken zijn gelijkvormig: hoogte / 12 = 1,5 / 2, dus hoogte = 9 m.", 3),
                 ("open", "Noem de twee voorwaarden waaraan gelijkvormige figuren voldoen.",
                  "Hun overeenkomstige hoeken zijn gelijk, en hun overeenkomstige zijden staan "
                  "in dezelfde verhouding.", 3),
             ]),
    ])


# ============================================================
zet("pythagoras-en-de-goniometrische-verhoudingen",
    titel="Pythagoras en de goniometrische verhoudingen",
    reeksen=[
        dict(kop="Pythagoras",
             opdracht="Reken de ontbrekende zijde uit. Rond af op één decimaal waar nodig.",
             oefeningen=[
                 ("rij", [("rechthoekszijden 9 en 12, schuine zijde?", "15"),
                          ("rechthoekszijden 7 en 24, schuine zijde?", "25"),
                          ("schuine zijde 13, één rechthoekszijde 5, andere?", "12"),
                          ("rechthoekszijden 5 en 5, schuine zijde?", "√50 ≈ 7,1"),
                          ("schuine zijde 10, één rechthoekszijde 6, andere?", "8"),
                          ("rechthoekszijden 8 en 15, schuine zijde?", "17")],
                  "Hoe lang is de gevraagde zijde?", WW),
                 ("open", "Is een driehoek met zijden 6, 8 en 11 rechthoekig? Toon je "
                          "berekening.",
                  "6² + 8² = 36 + 64 = 100, maar 11² = 121. Omdat 100 ≠ 121 is de driehoek "
                  "niet rechthoekig.", 3),
                 ("open", "Een deur is 90 cm breed en 200 cm hoog. Past een plaat van 215 cm "
                          "diagonaal door de opening?",
                  "De diagonaal is √(90² + 200²) = √(8 100 + 40 000) = √48 100 ≈ 219,3 cm. "
                  "Een plaat van 215 cm past dus.", 4),
             ]),
        dict(kop="Sinus, cosinus en tangens",
             opdracht="Vul in. Werk in een rechthoekige driehoek met hoek α.",
             oefeningen=[
                 ("rij", [("sin α =", "overstaande / schuine zijde"),
                          ("cos α =", "aanliggende / schuine zijde"),
                          ("tan α =", "overstaande / aanliggende"),
                          ("sin 30°", "0,5"), ("cos 60°", "0,5"), ("tan 45°", "1")],
                  "Vul aan.", WL),
                 ("open", "In een rechthoekige driehoek is de overstaande zijde 5 en de "
                          "aanliggende 12. Hoe groot is de hoek? Rond af op 0,1°.",
                  "tan α = 5/12 = 0,4167, dus α ≈ 22,6°.", 3),
                 ("open", "Een hoek heeft sin α = 0,6. Hoe groot is α, afgerond op 0,1°?",
                  "α ≈ 36,9°.", 2),
                 ("open", "Een ladder van 4 m staat onder een hoek van 70° tegen een muur. Tot "
                          "op welke hoogte reikt ze? Rond af op een centimeter.",
                  "hoogte = 4 · sin 70° ≈ 3,76 m.", 3),
                 ("open", "Een helling stijgt 8 m over een horizontale afstand van 100 m. "
                          "Hoeveel procent is dat, en hoeveel graden?",
                  "8 / 100 = 8 %. De hoek is arctan(0,08) ≈ 4,6°.", 3),
             ]),
        dict(kop="Toepassen",
             opdracht="Maak een schets en reken uit.",
             oefeningen=[
                 ("teken", "Een boom staat 20 m van je af. Je kijkt onder een hoek van 35° "
                           "omhoog naar de top; je ogen zitten 1,6 m hoog. Teken de situatie.",
                  "Een rechthoekige driehoek met de horizontale zijde 20 m, de hoek van 35° bij "
                  "het oog, en de verticale zijde die je zoekt, plus 1,6 m voor de ooghoogte.",
                  55),
                 ("open", "Reken nu de hoogte van de boom uit.",
                  "20 · tan 35° ≈ 14,0 m, plus 1,6 m ooghoogte, dus ongeveer 15,6 m.", 3),
             ]),
    ])


# ============================================================
zet("formules-omvormen",
    titel="Formules omvormen",
    reeksen=[
        dict(kop="Los op naar de gevraagde letter",
             opdracht="Schrijf de omgevormde formule op.",
             oefeningen=[
                 ("rij", [("A = l · b, naar b", "b = A / l"),
                          ("P = 2(l + b), naar l", "l = P/2 − b"),
                          ("v = s / t, naar t", "t = s / v"),
                          ("A = πr², naar r", "r = √(A/π)"),
                          ("F = m · a, naar a", "a = F / m"),
                          ("C = 5/9 (F − 32), naar F", "F = 9C/5 + 32")],
                  "Vorm om.", WW),
                 ("open", "Toon stap voor stap hoe je y = 3x + 7 omvormt naar x.",
                  "y = 3x + 7 · y − 7 = 3x · x = (y − 7)/3.", 3),
                 ("open", "Vorm om naar h: V = (1/3)πr²h.",
                  "h = 3V / (πr²).", 2),
             ]),
        dict(kop="Invullen en uitrekenen",
             opdracht="Vul in en reken uit.",
             oefeningen=[
                 ("open", "Zet 25 °C om naar graden Fahrenheit met F = 9C/5 + 32.",
                  "9 · 25 / 5 + 32 = 45 + 32 = 77 °F.", 2),
                 ("open", "Een cirkel heeft een oppervlakte van 78,5 cm². Hoe groot is de "
                          "straal? Gebruik π ≈ 3,14.",
                  "r = √(78,5 / 3,14) = √25 = 5 cm.", 3),
                 ("open", "Een auto rijdt 150 km in 1 uur 15 minuten. Wat is de gemiddelde "
                          "snelheid?",
                  "1 uur 15 min is 1,25 uur. v = 150 / 1,25 = 120 km/u.", 3),
                 ("open", "Een rechthoek heeft een omtrek van 46 cm en een lengte van 14 cm. "
                          "Hoe breed is ze?",
                  "P = 2(l + b), dus 46 = 2(14 + b), 23 = 14 + b, b = 9 cm.", 3),
             ]),
        dict(kop="Evenredigheid",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("y = 4x: welk soort evenredigheid?", "recht evenredig"),
                          ("y = 12/x: welk soort?", "omgekeerd evenredig"),
                          ("bij recht evenredig blijft dit gelijk", "het quotiënt y/x"),
                          ("bij omgekeerd evenredig blijft dit gelijk", "het product x·y"),
                          ("y = 4x, als x verdubbelt", "y verdubbelt"),
                          ("y = 12/x, als x verdubbelt", "y halveert")],
                  "Vul aan.", WW),
                 ("open", "Vier werkmensen doen een klus in zes dagen. Hoeveel dagen doen zes "
                          "werkmensen erover, als ze even snel werken?",
                  "Het product blijft gelijk: 4 · 6 = 24 werkdagen. Met zes mensen: 24 / 6 = "
                  "4 dagen.", 3),
             ]),
    ])


# ============================================================
zet("eerstegraadsvergelijkingen-en-ongelijkheden",
    titel="Eerstegraadsvergelijkingen en -ongelijkheden",
    reeksen=[
        dict(kop="Los op",
             opdracht="Schrijf de oplossing op.",
             oefeningen=[
                 ("rij", [("3x + 5 = 20", "x = 5"), ("7 − 2x = 1", "x = 3"),
                          ("4(x − 3) = 8", "x = 5"), ("x/4 + 2 = 5", "x = 12"),
                          ("5x − 3 = 2x + 9", "x = 4"),
                          ("2(x + 1) = 3(x − 2)", "x = 8")],
                  "Wat is x?", W),
                 ("open", "Los op en schrijf je tussenstappen: (x − 1)/3 + 2 = x/2.",
                  "Vermenigvuldig alles met 6: 2(x − 1) + 12 = 3x, dus 2x − 2 + 12 = 3x, "
                  "2x + 10 = 3x, x = 10.", 4),
                 ("open", "Wat betekent het als je bij het oplossen 0 = 5 uitkomt?",
                  "Er is geen enkele oplossing: de vergelijking is strijdig.", 2),
                 ("open", "En als je 0 = 0 uitkomt?",
                  "Elke x is een oplossing: de vergelijking is een identiteit.", 2),
             ]),
        dict(kop="Ongelijkheden",
             opdracht="Los op en schrijf de oplossing als interval.",
             oefeningen=[
                 ("rij", [("2x + 1 &gt; 9", "x &gt; 4, dus ]4, +∞["),
                          ("−3x ≥ 12", "x ≤ −4, dus ]−∞, −4]"),
                          ("x/2 − 1 &lt; 3", "x &lt; 8, dus ]−∞, 8["),
                          ("5 − x ≤ 2", "x ≥ 3, dus [3, +∞["),
                          ("4x + 3 &lt; x − 6", "x &lt; −3, dus ]−∞, −3["),
                          ("−2(x − 1) &gt; 6", "x &lt; −2, dus ]−∞, −2[")],
                  "Wat is de oplossing?", WL),
                 ("open", "Waarom draait het teken om bij −3x ≥ 12?",
                  "Je deelt beide leden door een negatief getal; dan keert de volgorde van de "
                  "getallen om en moet het ongelijkheidsteken mee omdraaien.", 3),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Stel een vergelijking op en los ze op.",
             oefeningen=[
                 ("open", "Een taxi vraagt 3,50 euro opstapgeld en 1,80 euro per kilometer. "
                          "Hoeveel kilometer rijd je voor 30,50 euro?",
                  "3,50 + 1,80x = 30,50, dus 1,80x = 27, x = 15 km.", 3),
                 ("open", "Lotte is drie keer zo oud als haar broer. Samen zijn ze 32. Hoe oud "
                          "is elk?",
                  "x + 3x = 32, dus 4x = 32 en x = 8. De broer is 8 en Lotte is 24.", 3),
                 ("open", "Een rechthoek is 4 cm langer dan breed en heeft een omtrek van 36 "
                          "cm. Hoe groot is ze?",
                  "2(b + 4 + b) = 36, dus 4b + 8 = 36, b = 7 en l = 11 cm.", 3),
                 ("open", "Een abonnement kost 12 euro per maand plus 0,05 euro per minuut. "
                          "Vanaf hoeveel minuten betaal je meer dan 20 euro?",
                  "12 + 0,05x &gt; 20, dus 0,05x &gt; 8 en x &gt; 160 minuten.", 3),
             ]),
    ])


# ============================================================
zet("stelsels-van-twee-vergelijkingen",
    titel="Stelsels van twee vergelijkingen",
    reeksen=[
        dict(kop="Los op met substitutie",
             opdracht="Werk uit en schrijf het koppel (x, y) op.",
             oefeningen=[
                 ("open", "y = 2x + 1 en 3x + y = 11",
                  "3x + 2x + 1 = 11, dus 5x = 10 en x = 2; y = 5. Oplossing (2, 5).", 3),
                 ("open", "x = y − 3 en 2x + y = 9",
                  "2(y − 3) + y = 9, dus 3y = 15 en y = 5; x = 2. Oplossing (2, 5).", 3),
             ]),
        dict(kop="Los op met combinatie",
             opdracht="Werk uit en schrijf het koppel (x, y) op.",
             oefeningen=[
                 ("open", "2x + 3y = 16 en 2x − y = 0",
                  "Trek de tweede van de eerste af: 4y = 16, dus y = 4. Vul in in de tweede: "
                  "2x − 4 = 0, dus x = 2. Oplossing (2, 4).", 4),
                 ("open", "3x + 2y = 12 en x − 2y = 4",
                  "Tel op: 4x = 16, dus x = 4; dan 4 − 2y = 4 geeft y = 0. Oplossing (4, 0).", 3),
                 ("open", "5x + 2y = 1 en 3x − 4y = 11",
                  "Vermenigvuldig de eerste met 2: 10x + 4y = 2. Tel op bij de tweede: "
                  "13x = 13, dus x = 1; dan 5 + 2y = 1 geeft y = −2. Oplossing (1, −2).", 4),
             ]),
        dict(kop="Hoeveel oplossingen?",
             opdracht="Schrijf op: één oplossing, geen oplossing of oneindig veel.",
             oefeningen=[
                 ("rij", [("y = 2x + 1 en y = 2x + 4", "geen oplossing"),
                          ("y = 2x + 1 en y = 3x − 2", "één oplossing"),
                          ("y = 2x + 1 en 2y = 4x + 2", "oneindig veel"),
                          ("x + y = 5 en x + y = 7", "geen oplossing"),
                          ("x − y = 0 en x + y = 4", "één oplossing"),
                          ("3x + 3y = 9 en x + y = 3", "oneindig veel")],
                  "Hoeveel oplossingen?", WW),
                 ("open", "Wat betekent 'geen oplossing' als je de twee rechten tekent?",
                  "De rechten zijn evenwijdig en vallen niet samen, dus ze snijden elkaar "
                  "nergens.", 2),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Stel een stelsel op en los het op.",
             oefeningen=[
                 ("open", "Drie broodjes en twee koffies kosten 13 euro. Eén broodje en vier "
                          "koffies kosten 11 euro. Wat kost elk?",
                  "3b + 2k = 13 en b + 4k = 11. Uit de tweede: b = 11 − 4k. Invullen: "
                  "33 − 12k + 2k = 13, dus 10k = 20 en k = 2; b = 3. Een broodje kost 3 euro, "
                  "een koffie 2 euro.", 5),
                 ("open", "Een zaal telt 120 plaatsen. Een ticket vooraan kost 15 euro, achteraan "
                          "9 euro. Alles is uitverkocht en de opbrengst is 1 320 euro. Hoeveel "
                          "tickets van elke soort?",
                  "v + a = 120 en 15v + 9a = 1 320. Uit de eerste: a = 120 − v. Invullen: "
                  "15v + 1 080 − 9v = 1 320, dus 6v = 240 en v = 40; a = 80.", 5),
             ]),
    ])


# ============================================================
zet("tweedegraadsvergelijkingen",
    titel="Tweedegraadsvergelijkingen",
    reeksen=[
        dict(kop="Ontbinden",
             opdracht="Ontbind in factoren.",
             oefeningen=[
                 ("rij", [("x² − 9", "(x − 3)(x + 3)"),
                          ("x² + 6x + 9", "(x + 3)²"),
                          ("x² − 5x + 6", "(x − 2)(x − 3)"),
                          ("x² + 2x − 15", "(x + 5)(x − 3)"),
                          ("2x² − 8x", "2x(x − 4)"),
                          ("x² − 4x + 4", "(x − 2)²")],
                  "Ontbind.", WW),
                 ("open", "Los op door te ontbinden: x² − 7x + 12 = 0.",
                  "(x − 3)(x − 4) = 0, dus x = 3 of x = 4.", 3),
             ]),
        dict(kop="De discriminant",
             opdracht="Bereken D en zeg hoeveel oplossingen er zijn.",
             oefeningen=[
                 ("tabel", ["vergelijking", "D", "aantal oplossingen"],
                  [["x² − 6x + 5 = 0", None, None], ["x² + 4x + 4 = 0", None, None],
                   ["x² + x + 3 = 0", None, None], ["2x² − 3x − 2 = 0", None, None],
                   ["x² − 2x − 8 = 0", None, None], ["3x² + 2x + 1 = 0", None, None]],
                  "x²−6x+5: D = 16, twee · x²+4x+4: D = 0, één · x²+x+3: D = −11, geen · "
                  "2x²−3x−2: D = 25, twee · x²−2x−8: D = 36, twee · 3x²+2x+1: D = −8, geen",
                  "110px"),
                 ("open", "Schrijf de formule voor de oplossingen op en los x² − 6x + 5 = 0 "
                          "ermee op.",
                  "x = (−b ± √D) / (2a). Hier: D = 36 − 20 = 16, √D = 4, dus "
                  "x = (6 ± 4)/2, dus x = 5 of x = 1.", 4),
                 ("open", "Los op: 2x² − 3x − 2 = 0.",
                  "D = 9 + 16 = 25, √D = 5, x = (3 ± 5)/4, dus x = 2 of x = −0,5.", 3),
             ]),
        dict(kop="Som en product",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de som van de wortels", "−b/a"), ("het product", "c/a"),
                          ("x² − 7x + 10 = 0: som en product", "7 en 10"),
                          ("de wortels daarvan", "2 en 5"),
                          ("x² + 3x − 10 = 0: som en product", "−3 en −10"),
                          ("de wortels daarvan", "2 en −5")],
                  "Vul aan.", WW),
                 ("open", "Stel een tweedegraadsvergelijking op met wortels 4 en −1.",
                  "Som is 3 en product is −4, dus x² − 3x − 4 = 0.", 3),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Stel een vergelijking op en los ze op.",
             oefeningen=[
                 ("open", "Een rechthoek heeft een oppervlakte van 60 cm² en is 7 cm langer "
                          "dan breed. Hoe groot is ze?",
                  "b(b + 7) = 60, dus b² + 7b − 60 = 0. D = 49 + 240 = 289, √D = 17, "
                  "b = (−7 + 17)/2 = 5. De rechthoek is 5 bij 12 cm.", 5),
                 ("open", "Een steen valt van een toren. De hoogte is h = 45 − 5t². Na hoeveel "
                          "seconden raakt hij de grond?",
                  "45 − 5t² = 0, dus t² = 9 en t = 3 seconden; de negatieve wortel heeft hier "
                  "geen betekenis.", 4),
             ]),
    ])


# ============================================================
zet("het-functiebegrip-en-de-eerstegraadsfunctie",
    titel="Het functiebegrip en de eerstegraadsfunctie",
    reeksen=[
        dict(kop="Is het een functie?",
             opdracht="Schrijf ja of nee, en waarom.",
             oefeningen=[
                 ("rij", [("bij elke leerling hoort één geboortedatum", "ja"),
                          ("bij elke geboortedatum hoort één leerling", "nee, meerdere"),
                          ("y = 3x − 1", "ja"),
                          ("x² + y² = 25", "nee, twee y bij één x"),
                          ("bij elk huisnummer hoort één straat", "ja"),
                          ("bij elke kleur hoort één leerling", "nee, meerdere")],
                  "Functie of niet?", WW),
                 ("open", "Wat is het verschil tussen het domein en het bereik?",
                  "Het domein is de verzameling van alle toegelaten x-waarden; het bereik is de "
                  "verzameling van alle y-waarden die er daadwerkelijk uitkomen.", 3),
             ]),
        dict(kop="De eerstegraadsfunctie",
             opdracht="Bij f(x) = −2x + 6.",
             oefeningen=[
                 ("rij", [("f(0)", "6"), ("f(3)", "0"), ("f(−1)", "8"),
                          ("de richtingscoëfficiënt", "−2"),
                          ("het snijpunt met de y-as", "(0, 6)"),
                          ("het nulpunt", "x = 3")],
                  "Wat is het antwoord?", W),
                 ("teken", "Teken de grafiek van f(x) = −2x + 6 in een assenstelsel.",
                  "Een dalende rechte door (0, 6) en (3, 0).", 60),
                 ("open", "Is f stijgend of dalend? Leg uit aan de hand van de "
                          "richtingscoëfficiënt.",
                  "Dalend: de richtingscoëfficiënt is −2, dus negatief. Per eenheid naar rechts "
                  "zakt de grafiek twee eenheden.", 3),
             ]),
        dict(kop="Een functievoorschrift opstellen",
             opdracht="Schrijf het voorschrift op.",
             oefeningen=[
                 ("open", "Een rechte gaat door (0, 4) en (2, 10).",
                  "De richtingscoëfficiënt is (10 − 4)/(2 − 0) = 3, dus y = 3x + 4.", 3),
                 ("open", "Een rechte gaat door (1, 5) en (4, −1).",
                  "rc = (−1 − 5)/(4 − 1) = −2. Invullen van (1, 5): 5 = −2 + q, dus q = 7 en "
                  "y = −2x + 7.", 4),
                 ("open", "Een gsm-abonnement kost 15 euro per maand plus 0,10 euro per "
                          "sms. Schrijf de kostfunctie en bereken de kost bij 80 sms'en.",
                  "k(x) = 15 + 0,10x. Bij x = 80: 15 + 8 = 23 euro.", 3),
                 ("open", "Twee abonnementen: A kost 15 + 0,10x en B kost 20 + 0,05x. Vanaf "
                          "hoeveel sms'en is B voordeliger?",
                  "15 + 0,10x &gt; 20 + 0,05x geeft 0,05x &gt; 5 en x &gt; 100. Vanaf 101 "
                  "sms'en is B goedkoper.", 4),
             ]),
    ])


# ============================================================
zet("de-tweedegraadsfunctie-en-haar-parabool",
    titel="De tweedegraadsfunctie en haar parabool",
    reeksen=[
        dict(kop="De vorm van de parabool",
             opdracht="Vul aan voor f(x) = ax² + bx + c.",
             oefeningen=[
                 ("rij", [("a &gt; 0", "dalparabool, opent naar boven"),
                          ("a &lt; 0", "bergparabool, opent naar beneden"),
                          ("de x van de top", "−b / (2a)"),
                          ("het snijpunt met de y-as", "(0, c)"),
                          ("D &gt; 0", "twee snijpunten met de x-as"),
                          ("D &lt; 0", "geen snijpunt met de x-as")],
                  "Vul aan.", WL),
                 ("open", "Waarom ligt de top altijd op de symmetrieas?",
                  "De parabool is symmetrisch om de verticale rechte x = −b/(2a); de top is het "
                  "enige punt dat op die as ligt en dus het laagste of hoogste punt.", 3),
             ]),
        dict(kop="Toppen en nulpunten",
             opdracht="Bereken de top en de nulpunten.",
             oefeningen=[
                 ("tabel", ["functie", "top", "nulpunten"],
                  [["f(x) = x² − 4x + 3", None, None],
                   ["f(x) = −x² + 6x − 5", None, None],
                   ["f(x) = x² + 2x + 5", None, None],
                   ["f(x) = x² − 9", None, None]],
                  "x²−4x+3: top (2, −1), nulpunten 1 en 3 · −x²+6x−5: top (3, 4), "
                  "nulpunten 1 en 5 · x²+2x+5: top (−1, 4), geen nulpunten · "
                  "x²−9: top (0, −9), nulpunten −3 en 3", "150px"),
                 ("teken", "Schets de parabool van f(x) = x² − 4x + 3: zet de top, de "
                           "nulpunten en het snijpunt met de y-as erop.",
                  "Een dalparabool met top (2, −1), nulpunten (1, 0) en (3, 0), en (0, 3) op "
                  "de y-as.", 65),
             ]),
        dict(kop="Teken van de functie",
             opdracht="Bij f(x) = x² − 4x + 3.",
             oefeningen=[
                 ("open", "Voor welke x is f(x) &lt; 0?",
                  "Tussen de nulpunten: voor x in ]1, 3[.", 2),
                 ("open", "Voor welke x is f(x) &gt; 0?",
                  "Buiten de nulpunten: voor x in ]−∞, 1[ ∪ ]3, +∞[.", 2),
                 ("open", "Wat is de kleinste waarde die f kan aannemen, en bij welke x?",
                  "De y-waarde van de top: −1, bij x = 2.", 2),
             ]),
        dict(kop="Een vraagstuk",
             opdracht="Werk uit.",
             oefeningen=[
                 ("open", "Een bal wordt omhoog geschoten. De hoogte is h(t) = −5t² + 20t. Na "
                          "hoeveel seconden is hij het hoogst, en hoe hoog komt hij?",
                  "t van de top: −20 / (2 · −5) = 2 seconden. h(2) = −20 + 40 = 20 meter.", 4),
                 ("open", "Wanneer raakt de bal weer de grond?",
                  "−5t² + 20t = 0 geeft −5t(t − 4) = 0, dus t = 0 of t = 4. Hij valt na "
                  "4 seconden.", 3),
                 ("open", "Een boer heeft 40 m draad voor een rechthoekige weide tegen een "
                          "muur, dus hij omheint maar drie zijden. Welke afmetingen geven de "
                          "grootste oppervlakte?",
                  "Noem de twee zijden loodrecht op de muur x. Dan is de derde zijde 40 − 2x en "
                  "de oppervlakte A = x(40 − 2x) = −2x² + 40x. De top ligt bij "
                  "x = −40 / (2 · −2) = 10. De weide is dus 10 bij 20 m, met 200 m².", 6),
             ]),
    ])


# ============================================================
zet("telproblemen-en-problemen-oplossen",
    titel="Telproblemen en problemen oplossen",
    reeksen=[
        dict(kop="Tellen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("4 broeken en 6 hemden: aantal combinaties", "24"),
                          ("op hoeveel volgordes kan je 5 boeken zetten", "120"),
                          ("een code van 4 cijfers, cijfers mogen herhalen", "10 000"),
                          ("een code van 4 verschillende cijfers", "5 040"),
                          ("hoeveel paren kan je kiezen uit 6 mensen", "15"),
                          ("hoeveel keuzes van 3 uit 5, volgorde telt mee", "60")],
                  "Hoeveel mogelijkheden?", WW),
                 ("open", "Leg het verschil uit tussen een geval waarin de volgorde meetelt en "
                          "een waarin ze niet meetelt. Geef bij elk een voorbeeld.",
                  "Bij een podium met goud, zilver en brons telt de volgorde mee: ABC is iets "
                  "anders dan BAC. Bij het kiezen van drie klasgenoten voor een werkgroep telt "
                  "ze niet mee: dezelfde drie zijn dezelfde groep.", 4),
                 ("open", "Reken na: hoeveel paren kan je kiezen uit 6 mensen? Toon de "
                          "berekening.",
                  "6 · 5 / 2 = 15. Je deelt door 2 omdat het paar AB hetzelfde is als BA.", 3),
             ]),
        dict(kop="Een probleem aanpakken",
             opdracht="Schrijf bij elke aanpak welke strategie je gebruikt.",
             oefeningen=[
                 ("rij", [("je noemt het onbekende aantal x", "variabelen invoeren"),
                          ("je maakt een schets van de situatie", "tekenen"),
                          ("je probeert eerst het geval met 2 in plaats van 100",
                           "een eenvoudiger geval bekijken"),
                          ("je zet alles in een tabel", "systematisch opsommen"),
                          ("je werkt van het antwoord terug naar de vraag",
                           "achterwaarts werken"),
                          ("je splitst de vraag in drie kleinere vragen",
                           "opsplitsen in deelproblemen")],
                  "Welke strategie?", WL),
                 ("open", "Hoeveel keer schrijf je het cijfer 9 als je de getallen 1 tot en "
                          "met 100 opschrijft? Los op met een systematische aanpak.",
                  "In de eenheden: 9, 19, 29, ... 99, dat zijn er 10. In de tientallen: 90 tot "
                  "en met 99, dat zijn er ook 10. Samen 20.", 4),
                 ("open", "Een slak klimt overdag 3 m omhoog in een put van 10 m en zakt "
                          "'s nachts 2 m terug. Na hoeveel dagen is ze boven?",
                  "Elke volle dag wint ze 1 m. Na 7 dagen staat ze op 7 m; op dag 8 klimt ze "
                  "3 m en is ze op 10 m, dus boven. Antwoord: 8 dagen.", 4),
             ]),
    ])


# ============================================================
zet("gegevens-weergeven-en-samenvatten",
    titel="Gegevens weergeven en samenvatten",
    reeksen=[
        dict(kop="Een reeks samenvatten",
             opdracht="Werk met deze tien waarden: 12, 15, 15, 18, 20, 21, 24, 25, 25, 25.",
             oefeningen=[
                 ("rij", [("de som", "200"), ("het gemiddelde", "20"),
                          ("de mediaan", "20,5"), ("de modus", "25"),
                          ("het bereik", "13"), ("het aantal waarden", "10")],
                  "Wat is het resultaat?", W),
                 ("open", "Leg uit hoe je de mediaan van tien waarden bepaalt.",
                  "Je zet ze op volgorde en neemt het gemiddelde van de vijfde en de zesde: "
                  "(20 + 21)/2 = 20,5.", 3),
                 ("open", "Het gemiddelde is 20 en de mediaan 20,5. Wat zegt dat over de "
                          "verdeling?",
                  "Ze liggen dicht bij elkaar, dus de verdeling is vrij symmetrisch; er is geen "
                  "uitschieter die het gemiddelde ver wegtrekt.", 3),
             ]),
        dict(kop="Wanneer welk kengetal?",
             opdracht="Schrijf op welk kengetal je kiest en waarom.",
             oefeningen=[
                 ("open", "De lonen in een bedrijf waar de directeur tien keer zoveel verdient "
                          "als de rest.",
                  "De mediaan: het gemiddelde wordt door dat ene hoge loon omhoog getrokken en "
                  "geeft geen beeld van wat een gewone werknemer verdient.", 3),
                 ("open", "De meest verkochte schoenmaat in een winkel.",
                  "De modus: je wil weten welke maat het vaakst voorkomt, niet het gemiddelde "
                  "van alle maten.", 2),
                 ("open", "De gemiddelde temperatuur van een maand.",
                  "Het gemiddelde: alle waarden liggen dicht bij elkaar en elke dag telt even "
                  "zwaar mee.", 2),
                 ("waar", "Een uitschieter verandert de mediaan meestal sterker dan het "
                          "gemiddelde.", False),
             ]),
        dict(kop="Spreiding",
             opdracht="Reken uit of leg uit.",
             oefeningen=[
                 ("open", "Bereken het eerste en het derde kwartiel van de reeks hierboven, "
                          "en de interkwartielafstand.",
                  "Q1 is de derde waarde, 15; Q3 is de achtste waarde, 25. De "
                  "interkwartielafstand is 10.", 3),
                 ("open", "Twee klassen hebben allebei een gemiddelde van 60 %. Klas A heeft "
                          "een standaardafwijking van 4, klas B van 15. Wat betekent dat?",
                  "In klas A liggen de punten dicht bij het gemiddelde; in klas B lopen ze ver "
                  "uiteen, met zwakke en sterke leerlingen. Hetzelfde gemiddelde zegt dus niets "
                  "over de klas.", 4),
                 ("open", "Waarvoor dient een boxplot?",
                  "Hij toont in één beeld het minimum, Q1, de mediaan, Q3 en het maximum, zodat "
                  "je de spreiding en de scheefheid van een reeks meteen ziet.", 3),
             ]),
        dict(kop="Grafieken lezen en kiezen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("rij", [("het verloop van de temperatuur over een jaar", "een lijngrafiek"),
                          ("het aandeel van vier partijen in een parlement", "een cirkeldiagram"),
                          ("het aantal leerlingen per studierichting", "een staafdiagram"),
                          ("de spreiding van punten in twee klassen", "twee boxplots"),
                          ("het verband tussen lengte en gewicht", "een puntenwolk"),
                          ("hoe vaak elke score voorkomt", "een histogram")],
                  "Welke grafiek kies je?", WW),
                 ("open", "Een staafdiagram begint niet bij nul maar bij 90. Waarom is dat "
                          "misleidend?",
                  "Een klein verschil lijkt dan enorm, omdat je alleen het topje van de staven "
                  "ziet. De verhouding tussen de staven klopt niet meer.", 3),
             ]),
    ])


# ============================================================
zet("verbanden-tussen-twee-grootheden",
    titel="Verbanden tussen twee grootheden",
    reeksen=[
        dict(kop="Welk verband?",
             opdracht="Schrijf op: recht evenredig, omgekeerd evenredig, lineair of geen van "
                      "de drie.",
             oefeningen=[
                 ("rij", [("y = 5x", "recht evenredig"), ("y = 5x + 2", "lineair"),
                          ("y = 20/x", "omgekeerd evenredig"), ("y = x²", "geen van de drie"),
                          ("de prijs van benzine per liter", "recht evenredig"),
                          ("een taxi met opstapgeld", "lineair")],
                  "Welk verband?", WW),
                 ("open", "Wat is het verschil tussen recht evenredig en lineair?",
                  "Recht evenredig is een bijzonder geval van lineair: de grafiek gaat door de "
                  "oorsprong. Bij een lineair verband met een constante erbij gaat ze dat "
                  "niet.", 3),
             ]),
        dict(kop="Een tabel aanvullen",
             opdracht="Vul de tabel aan en schrijf het verband op.",
             oefeningen=[
                 ("tabel", ["x", "1", "2", "4", "5", "8"],
                  [["y recht evenredig, y = 3x", None, None, None, None, None]],
                  "3, 6, 12, 15, 24", "55px"),
                 ("tabel", ["x", "1", "2", "4", "5", "10"],
                  [["y omgekeerd evenredig, x·y = 20", None, None, None, None, None]],
                  "20, 10, 5, 4, 2", "55px"),
                 ("open", "In een tabel staat: x = 2 geeft y = 7, x = 4 geeft y = 13 en x = 6 "
                          "geeft y = 19. Welk verband is dit? Schrijf het voorschrift.",
                  "Lineair: per stap van 2 in x stijgt y met 6, dus rc = 3. Invullen van "
                  "(2, 7): 7 = 6 + q, dus q = 1 en y = 3x + 1.", 4),
             ]),
        dict(kop="Puntenwolk en samenhang",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("rij", [("de punten lopen van linksonder naar rechtsboven",
                           "positieve samenhang"),
                          ("de punten lopen van linksboven naar rechtsonder",
                           "negatieve samenhang"),
                          ("de punten liggen willekeurig verspreid", "geen samenhang"),
                          ("de punten liggen bijna op één rechte", "sterke samenhang"),
                          ("de rechte die het best door de wolk loopt", "de regressierechte"),
                          ("een punt dat ver van de wolk ligt", "een uitschieter")],
                  "Hoe noemen we dit?", WW),
                 ("open", "In een stad stijgt het aantal ijsjes én het aantal verdrinkingen in "
                          "dezelfde maanden. Mag je besluiten dat ijsjes gevaarlijk zijn?",
                  "Nee. Er is wel een samenhang, maar geen oorzakelijk verband: de warmte is "
                  "de derde factor die allebei verklaart.", 3),
                 ("open", "Noem twee redenen waarom een samenhang nog geen oorzaak is.",
                  "Er kan een derde factor zijn die beide beïnvloedt, en de richting kan "
                  "omgekeerd zijn dan je denkt. Daarbij kan een verband ook toeval zijn, "
                  "zeker bij kleine aantallen.", 4),
             ]),
        dict(kop="Toepassen",
             opdracht="Werk uit.",
             oefeningen=[
                 ("open", "Een drukker rekent 25 euro opstartkost plus 0,40 euro per affiche. "
                          "Schrijf de formule en bereken de prijs voor 150 affiches.",
                  "p(x) = 25 + 0,40x. Bij 150: 25 + 60 = 85 euro.", 3),
                 ("open", "Bij welke oplage kost één affiche minder dan 0,60 euro, alles "
                          "meegerekend?",
                  "(25 + 0,40x)/x &lt; 0,60 geeft 25 + 0,40x &lt; 0,60x, dus 25 &lt; 0,20x en "
                  "x &gt; 125. Vanaf 126 affiches.", 4),
             ]),
    ])
