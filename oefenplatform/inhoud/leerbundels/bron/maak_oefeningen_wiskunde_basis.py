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
                      "\\(\\mathbb{N}\\), \\(\\mathbb{Z}\\), \\(\\mathbb{Q}\\) of \\(\\mathbb{R} \\setminus \\mathbb{Q}\\).",
             oefeningen=[
                 ("rij", [("\\(7\\)", "\\(\\mathbb{N}\\)"), ("\\(-4\\)", "\\(\\mathbb{Z}\\)"),
                          ("\\(0{,}75\\)", "\\(\\mathbb{Q}\\)"),
                          ("\\(\\sqrt{9}\\)", "\\(\\mathbb{N}\\)"),
                          ("\\(\\sqrt{2}\\)", "\\(\\mathbb{R} \\setminus \\mathbb{Q}\\)"),
                          ("\\(\\pi\\)", "\\(\\mathbb{R} \\setminus \\mathbb{Q}\\)"),
                          ("\\(-\\frac{2}{3}\\)", "\\(\\mathbb{Q}\\)"),
                          ("\\(\\sqrt[3]{8}\\)", "\\(\\mathbb{N}\\)")],
                  "Verzameling", W),
                 ("waar", "\\(\\mathbb{R} \\subset \\mathbb{Q}\\)", False),
                 ("waar", "Elk natuurlijk getal is ook een reëel getal.", True),
                 ("open", "Waarom is \\(\\sqrt{9}\\) geen irrationaal getal en \\(\\sqrt{2}\\) wel?",
                  "\\(\\sqrt{9} = 3\\), dus een natuurlijk getal. \\(\\sqrt{2}\\) is geen breuk van twee gehele "
                  "getallen en heeft een oneindige, niet herhalende decimale uitbreiding.", 3),
             ]),
        dict(kop="Decimale vorm, breuk en procent",
             opdracht="Zet om naar de gevraagde vorm.",
             oefeningen=[
                 ("rij", [("\\(\\frac{3}{5}\\) in procent", "\\(60\\,\\%\\)"),
                          ("\\(\\frac{1}{8}\\) in decimale vorm", "\\(0{,}125\\)"),
                          ("\\(0{,}4\\) als breuk", "\\(\\frac{2}{5}\\)"),
                          ("\\(35\\,\\%\\) als kommagetal", "\\(0{,}35\\)"),
                          ("\\(\\frac{2}{9}\\): welke decimale vorm?", "onbegrensd repeterend"),
                          ("\\(\\pi\\): welke decimale vorm?", "onbegrensd niet-repeterend")],
                  "Omzetten", WW),
                 ("kort", "Hoeveel is \\(18\\,\\%\\) van \\(350\\)?", "\\(63\\)", W),
                 ("kort", "Zet \\(0{,}8\\), \\(\\frac{3}{4}\\), \\(\\frac{2}{3}\\) in stijgende volgorde.",
                  "\\(\\frac{2}{3} < \\frac{3}{4} < 0{,}8\\)", WL),
             ]),
        dict(kop="Rekenen met machten",
             opdracht="Vereenvoudig tot één macht of reken uit.",
             oefeningen=[
                 ("rij", [("\\(2^{3} \\cdot 2^{5}\\)", "\\(2^{8}\\)"),
                          ("\\(\\frac{a^{7}}{a^{3}}\\)", "\\(a^{4}\\)"),
                          ("\\(\\left(3^{2}\\right)^{4}\\)", "\\(3^{8}\\)"),
                          ("\\(5^{0}\\)", "\\(1\\)"),
                          ("\\(x^{-2}\\)", "\\(\\frac{1}{x^{2}}\\)"),
                          ("\\(\\left(2a^{3}\\right)^{2}\\)", "\\(4a^{6}\\)")],
                  "Vereenvoudig", W),
                 ("rij", [("\\(2^{-3}\\)", "\\(\\frac{1}{8}\\)"),
                          ("\\(10^{5}\\)", "\\(100\\,000\\)"),
                          ("\\((-3)^{2}\\)", "\\(9\\)"),
                          ("\\(-3^{2}\\)", "\\(-9\\)"),
                          ("\\(\\left(\\frac{1}{2}\\right)^{-1}\\)", "\\(2\\)"),
                          ("\\(\\left(\\frac{2}{3}\\right)^{2}\\)", "\\(\\frac{4}{9}\\)")],
                  "Uitrekenen", W),
             ]),
        dict(kop="Machten: de valkuilen",
             opdracht="Lees de haakjes goed.",
             oefeningen=[
                 ("kies", "Welke bewering is juist?",
                  ["\\(2^{3} + 2^{3} = 2^{6}\\)",
                   "\\(2^{3} \\cdot 2^{3} = 2^{6}\\)",
                   "\\(2^{3} \\cdot 2^{3} = 4^{3} \\cdot 2\\)"], 1),
                 ("open", "Leg uit waarom \\((-3)^{2}\\) en \\(-3^{2}\\) niet hetzelfde zijn.",
                  "Bij \\((-3)^{2}\\) staat het minteken binnen de haakjes en wordt het mee gekwadrateerd, "
                  "dus \\(9\\). Bij \\(-3^{2}\\) werkt het kwadraat alleen op de \\(3\\), en het minteken komt "
                  "er daarna bij: \\(-9\\).", 3),
             ]),
        dict(kop="Wortels",
             opdracht="Vereenvoudig of reken uit.",
             oefeningen=[
                 ("rij", [("\\(\\sqrt{49}\\)", "\\(7\\)"),
                          ("\\(\\sqrt{50}\\)", "\\(5\\sqrt{2}\\)"),
                          ("\\(\\sqrt{12} + \\sqrt{27}\\)", "\\(5\\sqrt{3}\\)"),
                          ("\\(\\sqrt{8} \\cdot \\sqrt{2}\\)", "\\(4\\)"),
                          ("\\(\\sqrt{\\frac{16}{25}}\\)", "\\(\\frac{4}{5}\\)"),
                          ("\\(3\\sqrt{5} - \\sqrt{5}\\)", "\\(2\\sqrt{5}\\)")],
                  "Vereenvoudig", W),
                 ("rij", [("\\(\\sqrt[3]{125}\\)", "\\(5\\)"),
                          ("\\(\\sqrt[3]{-27}\\)", "\\(-3\\)"),
                          ("\\(\\sqrt{72}\\)", "\\(6\\sqrt{2}\\)"),
                          ("\\(\\sqrt{2} \\cdot \\sqrt{18}\\)", "\\(6\\)")],
                  "Nog eens", W),
             ]),
        dict(kop="Wortels: toon je tussenstappen",
             opdracht="Schrijf telkens op hoe je aan je antwoord komt.",
             oefeningen=[
                 ("open", "Toon met tussenstappen hoe je \\(\\sqrt{12} + \\sqrt{27}\\) vereenvoudigt.",
                  "\\(\\sqrt{12} = \\sqrt{4 \\cdot 3} = 2\\sqrt{3}\\) en \\(\\sqrt{27} = \\sqrt{9 \\cdot 3} = "
                  "3\\sqrt{3}\\). Samen \\(2\\sqrt{3} + 3\\sqrt{3} = 5\\sqrt{3}\\).", 3),
                 ("open", "Maak de noemer rationaal: \\(\\frac{6}{\\sqrt{3}}\\).",
                  "\\(\\frac{6}{\\sqrt{3}} = \\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}\\).", 2),
                 ("open", "Geef een tegenvoorbeeld bij de bewering \\(\\sqrt{a + b} = \\sqrt{a} + \\sqrt{b}\\).",
                  "Neem \\(a = 9\\) en \\(b = 16\\): \\(\\sqrt{25} = 5\\), maar \\(3 + 4 = 7\\). De bewering is "
                  "dus fout.", 3),
             ]),
        dict(kop="Wetenschappelijke notatie",
             opdracht="Schrijf om of reken uit.",
             oefeningen=[
                 ("rij", [("\\(43\\,000\\)", "\\(4{,}3 \\cdot 10^{4}\\)"),
                          ("\\(0{,}0052\\)", "\\(5{,}2 \\cdot 10^{-3}\\)"),
                          ("\\(6{,}1 \\cdot 10^{5}\\)", "\\(610\\,000\\)"),
                          ("\\(2{,}4 \\cdot 10^{-2}\\)", "\\(0{,}024\\)"),
                          ("\\(\\left(3 \\cdot 10^{4}\\right)\\left(2 \\cdot 10^{3}\\right)\\)", "\\(6 \\cdot 10^{7}\\)"),
                          ("\\(\\frac{8 \\cdot 10^{6}}{4 \\cdot 10^{2}}\\)", "\\(2 \\cdot 10^{4}\\)")],
                  "Omzetten", WW),
                 ("kort", "Waarom is \\(45 \\cdot 10^{3}\\) geen correcte wetenschappelijke notatie?",
                  "\\(45\\) ligt niet tussen \\(1\\) en \\(10\\); correct is \\(4{,}5 \\cdot 10^{4}\\).", WL),
                 ("open", "Een lichtjaar is ongeveer \\(9{,}46 \\cdot 10^{12}\\) km. Hoeveel km is drie "
                          "lichtjaar? Geef het antwoord in wetenschappelijke notatie.",
                  "\\(3 \\cdot 9{,}46 \\cdot 10^{12} = 28{,}38 \\cdot 10^{12} = 2{,}838 \\cdot 10^{13}\\) km.", 3),
             ]),
        dict(kop="De bewerkingseigenschappen",
             opdracht="Noem de eigenschap die je herkent.",
             oefeningen=[
                 ("rij", [("\\(3 \\cdot 5 = 5 \\cdot 3\\)", "commutativiteit"),
                          ("\\((2 + 3) + 4 = 2 + (3 + 4)\\)", "associativiteit"),
                          ("\\(a(b + c) = ab + ac\\)", "distributiviteit")],
                  "Eigenschap", WW),
                 ("open", "Waarom rond je pas op het einde van een berekening af?",
                  "Afronden onderweg vervalst het resultaat: hoe onnauwkeuriger je tussenresultaten, hoe "
                  "meer je eindantwoord afwijkt. Werk dus zo lang mogelijk exact.", 2),
             ]),
    ])


# ============================================================
zet("getallen-ordenen-afronden-en-intervallen",
    titel="Getallen ordenen, afronden en intervallen",
    reeksen=[
        dict(kop="Ordenen",
             opdracht="Zet van klein naar groot.",
             oefeningen=[
                 ("open", "\\(0{,}7\\) · \\(\\frac{3}{4}\\) · \\(0{,}68\\) · \\(\\frac{7}{10}\\)",
                  "\\(0{,}68 < 0{,}7 = \\frac{7}{10} < \\frac{3}{4}\\)", 2),
                 ("open", "\\(-2{,}5\\) · \\(-3\\) · \\(-2{,}05\\) · \\(0\\)",
                  "\\(-3 < -2{,}5 < -2{,}05 < 0\\)", 2),
                 ("open", "\\(\\sqrt{2}\\) · \\(1{,}5\\) · \\(1{,}41\\) · \\(\\frac{3}{2}\\)",
                  "\\(1{,}41 < \\sqrt{2} < 1{,}5 = \\frac{3}{2}\\)", 2),
                 ("open", "Hoe vergelijk je \\(\\frac{3}{7}\\) en \\(\\frac{4}{9}\\) zonder rekenmachine?",
                  "Gelijknamig maken: \\(\\frac{3}{7} = \\frac{27}{63}\\) en \\(\\frac{4}{9} = \\frac{28}{63}\\), "
                  "dus \\(\\frac{3}{7} < \\frac{4}{9}\\).", 3),
             ]),
        dict(kop="Het juiste teken",
             opdracht="Vul \\(<\\), \\(>\\) of \\(=\\) in.",
             oefeningen=[
                 ("rij", [("\\(-10 \\;\\square\\; {-3}\\)", "\\(<\\)"),
                          ("\\(-0{,}5 \\;\\square\\; {-1{,}5}\\)", "\\(>\\)"),
                          ("\\(\\frac{2}{3} \\;\\square\\; 0{,}67\\)", "\\(<\\)"),
                          ("\\(\\frac{7}{5} \\;\\square\\; 1{,}4\\)", "\\(=\\)"),
                          ("\\(\\sqrt{2} \\;\\square\\; 1{,}5\\)", "\\(<\\)"),
                          ("\\(-5 \\;\\square\\; {-2}\\)", "\\(<\\)")],
                  "Teken", W),
                 ("waar", "\\(3 \\leq 3\\)", True),
                 ("waar", "\\(x > 3\\) betekent dat \\(3\\) zelf ook een oplossing is.", False),
             ]),
        dict(kop="Afronden",
             opdracht="Rond af zoals gevraagd.",
             oefeningen=[
                 ("rij", [("\\(3{,}4567\\) op \\(2\\) decimalen", "\\(3{,}46\\)"),
                          ("\\(12\\,849\\) op honderdtallen", "\\(12\\,800\\)"),
                          ("\\(0{,}00472\\) op \\(3\\) beduidende cijfers", "\\(0{,}00472\\)"),
                          ("\\(2{,}5\\) op een geheel getal", "\\(3\\)"),
                          ("\\(149{,}95\\) op \\(1\\) decimaal", "\\(150{,}0\\)"),
                          ("\\(0{,}0996\\) op \\(2\\) decimalen", "\\(0{,}10\\)")],
                  "Afgerond", WW),
                 ("kort", "Rond \\(1\\,999\\) af op honderdtallen.", "\\(2\\,000\\)", W),
             ]),
        dict(kop="Waarom afronden oppast",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Een winkel verkoopt \\(3\\) stuks voor \\(10\\) euro. Wat kost één stuk, "
                          "afgerond op een cent, en waarom klopt drie keer dat bedrag niet precies?",
                  "\\(10 : 3 = 3{,}333\\ldots\\) dus \\(3{,}33\\) euro. Drie keer \\(3{,}33\\) is \\(9{,}99\\): "
                  "door het afronden gaat er een cent verloren.", 3),
                 ("open", "Waarom rond je bij een eindantwoord pas af en niet tussenin?",
                  "Elke tussentijdse afronding voegt een foutje toe, en die fouten stapelen op. "
                  "Het eindantwoord wordt dan onnauwkeuriger dan nodig.", 3),
             ]),
        dict(kop="Intervallen noteren",
             opdracht="Schrijf het interval op in haakjesnotatie.",
             oefeningen=[
                 ("rij", [("alle \\(x\\) met \\(2 < x \\leq 7\\)", "\\(\\left]2, 7\\right]\\)"),
                          ("alle \\(x\\) vanaf \\(-3\\) tot en met \\(0\\)", "\\(\\left[-3, 0\\right]\\)"),
                          ("alle \\(x\\) met \\(x < 5\\)", "\\(\\left]-\\infty, 5\\right[\\)"),
                          ("alle \\(x\\) met \\(x \\geq 1\\)", "\\(\\left[1, +\\infty\\right[\\)"),
                          ("alle \\(x\\) tussen \\(-1\\) en \\(1\\), grenzen niet erbij", "\\(\\left]-1, 1\\right[\\)"),
                          ("alle reële getallen", "\\(\\left]-\\infty, +\\infty\\right[\\)")],
                  "Interval", WW),
                 ("rij", [("\\(\\left[-2, 8\\right]\\)", "gesloten"),
                          ("\\(\\left]0, 1\\right[\\)", "open"),
                          ("\\(\\left[2, 5\\right[\\)", "halfopen")],
                  "Soort", W),
             ]),
        dict(kop="Doorsnede en unie",
             opdracht="Reken uit en schrijf het resultaat als interval.",
             oefeningen=[
                 ("kort", "\\(\\left[0, 6\\right] \\cap \\left]4, 9\\right[\\)", "\\(\\left]4, 6\\right]\\)", WW),
                 ("kort", "\\(\\left]-\\infty, 2\\right[ \\cup \\left[2, +\\infty\\right[\\)",
                  "\\(\\mathbb{R}\\), dus \\(\\left]-\\infty, +\\infty\\right[\\)", WW),
                 ("kort", "\\(\\left]1, 5\\right[ \\cap \\left[5, 9\\right]\\)", "\\(\\emptyset\\)", WW),
                 ("open", "Waarom staat er bij \\(+\\infty\\) altijd een haakje naar buiten?",
                  "Oneindig is geen getal, dus het kan nooit tot het interval behoren.", 2),
             ]),
        dict(kop="Van tekst naar interval",
             opdracht="Welk interval hoort bij de situatie?",
             oefeningen=[
                 ("rij", [("een korting vanaf \\(50\\) euro", "\\(\\left[50, +\\infty\\right[\\)"),
                          ("een temperatuur tussen \\(-2\\) en \\(8\\) graden, grenzen meegerekend", "\\(\\left[-2, 8\\right]\\)"),
                          ("een snelheid van meer dan \\(50\\) km/u", "\\(\\left]50, +\\infty\\right[\\)"),
                          ("een leeftijd van hoogstens \\(12\\) jaar", "\\(\\left]-\\infty, 12\\right]\\)")],
                  "Interval", WW),
                 ("open", "Een pretpark laat kinderen toe die minstens \\(1{,}20\\) m groot zijn maar kleiner "
                          "dan \\(1{,}80\\) m. Schrijf dat als interval en zeg welke soort het is.",
                  "\\(\\left[1{,}20;\\ 1{,}80\\right[\\), een halfopen interval: \\(1{,}20\\) doet mee, "
                  "\\(1{,}80\\) niet.", 3),
             ]),
    ])


# ============================================================
zet("logica-bewerkingen-en-waarheidstabellen",
    titel="Logica: bewerkingen en waarheidstabellen",
    reeksen=[
        dict(kop="Waar of vals?",
             opdracht="\\(p\\) is waar, \\(q\\) is vals. Bepaal de waarheidswaarde.",
             oefeningen=[
                 ("rij", [("\\(p \\wedge q\\)", "vals"), ("\\(p \\vee q\\)", "waar"),
                          ("\\(\\neg p\\)", "vals"), ("\\(\\neg q\\)", "waar"),
                          ("\\(p \\Rightarrow q\\)", "vals"), ("\\(q \\Rightarrow p\\)", "waar"),
                          ("\\(p \\Leftrightarrow q\\)", "vals"), ("\\(\\neg p \\vee q\\)", "vals")],
                  "Waarheidswaarde", WW),
                 ("open", "Waarom is \\(q \\Rightarrow p\\) waar als \\(q\\) vals is?",
                  "Een implicatie is alleen vals als het eerste deel waar is en het tweede niet. Met een "
                  "vals eerste deel belooft de implicatie niets, dus ze is waar.", 3),
             ]),
        dict(kop="Zet om in symbolen",
             opdracht="Gebruik \\(\\neg\\), \\(\\wedge\\), \\(\\vee\\), \\(\\Rightarrow\\) en \\(\\Leftrightarrow\\).",
             oefeningen=[
                 ("rij", [("\\(p\\) is waar en \\(q\\) is vals", "\\(p \\wedge \\neg q\\)"),
                          ("\\(p\\) of \\(q\\), of allebei", "\\(p \\vee q\\)"),
                          ("als \\(p\\), dan \\(q\\)", "\\(p \\Rightarrow q\\)"),
                          ("\\(p\\) dan en slechts dan als \\(q\\)", "\\(p \\Leftrightarrow q\\)"),
                          ("niet \\(p\\) en niet \\(q\\)", "\\(\\neg p \\wedge \\neg q\\)")],
                  "In symbolen", WW),
                 ("kort", "Hoeveel rijen heeft een waarheidstabel met vier uitspraken?",
                  "\\(2^{4} = 16\\)", W),
             ]),
        dict(kop="Een waarheidstabel invullen",
             opdracht="Vul de tabel aan met W (waar) of V (vals).",
             oefeningen=[
                 ("tabel", ["\\(p\\)", "\\(q\\)", "\\(p \\wedge q\\)", "\\(p \\vee q\\)", "\\(p \\Rightarrow q\\)"],
                  [["W", "W", None, None, None], ["W", "V", None, None, None],
                   ["V", "W", None, None, None], ["V", "V", None, None, None]],
                  "rij 1: W, W, W · rij 2: V, W, V · rij 3: V, W, W · rij 4: V, V, W",
                  "50px"),
             ]),
        dict(kop="Nog een waarheidstabel",
             opdracht="Vul ook deze aan met W of V.",
             oefeningen=[
                 ("tabel", ["\\(p\\)", "\\(q\\)", "\\(\\neg p\\)", "\\(\\neg p \\vee q\\)"],
                  [["W", "W", None, None], ["W", "V", None, None],
                   ["V", "W", None, None], ["V", "V", None, None]],
                  "rij 1: V, W · rij 2: V, V · rij 3: W, W · rij 4: W, W",
                  "50px"),
                 ("open", "Vergelijk de laatste kolom van beide tabellen. Wat besluit je?",
                  "\\(\\neg p \\vee q\\) heeft exact dezelfde waarden als \\(p \\Rightarrow q\\). De twee "
                  "uitdrukkingen zijn dus logisch gelijkwaardig.", 3),
             ]),
        dict(kop="Tautologie of contradictie?",
             opdracht="Schrijf op of de uitspraak altijd waar, altijd vals of geen van beide is.",
             oefeningen=[
                 ("rij", [("\\(p \\vee \\neg p\\)", "tautologie"),
                          ("\\(p \\wedge \\neg p\\)", "contradictie"),
                          ("\\(p \\Rightarrow p\\)", "tautologie"),
                          ("\\(p \\wedge q\\)", "geen van beide")],
                  "Soort", WW),
                 ("open", "Hoe zie je aan een waarheidstabel dat een uitspraak een tautologie is, en "
                          "hoeveel rijen heb je nodig om haar te weerleggen?",
                  "Alle rijen van de eindkolom geven waar. Eén enkele rij met vals volstaat al om haar te "
                  "weerleggen.", 3),
             ]),
        dict(kop="Omkeren, omgekeerde en contrapositie",
             opdracht="Schrijf de gevraagde vorm op van: als het regent, dan is de straat nat.",
             oefeningen=[
                 ("open", "De omgekeerde implicatie.",
                  "Als de straat nat is, dan regent het.", 2),
                 ("open", "De contrapositie.",
                  "Als de straat niet nat is, dan regent het niet.", 2),
                 ("open", "Welke van de twee is zeker waar als de oorspronkelijke zin waar is?",
                  "De contrapositie. De omgekeerde implicatie hoeft niet waar te zijn: de straat kan ook "
                  "nat zijn van een sproeiwagen.", 3),
             ]),
        dict(kop="Kwantoren ontkennen",
             opdracht="Schrijf de ontkenning in gewone taal.",
             oefeningen=[
                 ("open", "Alle leerlingen van deze klas hebben een fiets. \\(\\left(\\forall\\right)\\)",
                  "Er is minstens één leerling van deze klas die geen fiets heeft.", 2),
                 ("open", "Er bestaat een getal waarvan het kwadraat negatief is. \\(\\left(\\exists\\right)\\)",
                  "Voor elk getal geldt dat het kwadraat niet negatief is.", 2),
                 ("kort", "Wat is de ontkenning van \\(\\forall x: x > 0\\)?",
                  "\\(\\exists x: x \\leq 0\\)", WW),
             ]),
        dict(kop="Logische poorten",
             opdracht="Schrijf op welke poort bij de situatie hoort.",
             oefeningen=[
                 ("rij", [("een lamp die enkel brandt als twee schakelaars samen aan staan", "en-poort"),
                          ("een lamp die brandt zodra één schakelaar aan staat", "of-poort"),
                          ("een schakeling die een \\(1\\) in een \\(0\\) verandert", "niet-poort")],
                  "Poort", WW),
                 ("open", "Een alarm gaat af als de deur open is én het systeem gewapend is, of als de "
                          "paniekknop ingedrukt wordt. Welke poorten heb je nodig, en in welke volgorde?",
                  "Eerst een en-poort voor deur open én gewapend, daarna een of-poort die het resultaat "
                  "daarvan combineert met de paniekknop.", 3),
             ]),
    ])


# ============================================================
zet("redeneren-bewijzen-en-tegenvoorbeelden",
    titel="Redeneren, bewijzen en tegenvoorbeelden",
    reeksen=[
        dict(kop="Geef een tegenvoorbeeld",
             opdracht="Elke bewering hieronder is fout. Schrijf één tegenvoorbeeld op.",
             oefeningen=[
                 ("rij", [("Elk priemgetal is oneven.", "\\(2\\)"),
                          ("Als \\(x^{2} = 9\\), dan is \\(x = 3\\).", "\\(x = -3\\)"),
                          ("Elke vierhoek met vier gelijke zijden is een vierkant.",
                           "een ruit die geen rechte hoeken heeft"),
                          ("Als \\(a > b\\), dan is \\(a^{2} > b^{2}\\).", "\\(a = 1\\) en \\(b = -2\\)"),
                          ("De som van twee oneven getallen is oneven.", "\\(3 + 5 = 8\\)"),
                          ("Elk getal deelbaar door \\(3\\) is deelbaar door \\(9\\).", "\\(6\\)")],
                  "Tegenvoorbeeld", WW),
             ]),
        dict(kop="Nog meer tegenvoorbeelden",
             opdracht="Ook deze beweringen zijn fout. Geef telkens één tegenvoorbeeld.",
             oefeningen=[
                 ("rij", [("\\(\\sqrt{a + b} = \\sqrt{a} + \\sqrt{b}\\)", "\\(a = 9\\), \\(b = 16\\)"),
                          ("\\(a^{2} > 0\\) voor elke \\(a\\)", "\\(a = 0\\)"),
                          ("\\(-a < 0\\) voor elke \\(a\\)", "\\(a = -3\\)"),
                          ("Delen maakt altijd kleiner.", "\\(6 : \\frac{1}{2} = 12\\)")],
                  "Nog eens", WW),
                 ("open", "Waarom volstaat één tegenvoorbeeld om een bewering te weerleggen, "
                          "terwijl honderd voorbeelden ze niet bewijzen?",
                  "Een bewering met elk of alle zegt iets over alle gevallen. Eén geval dat niet klopt, "
                  "maakt ze vals. Maar honderd kloppende gevallen zeggen niets over het honderdeneerste.", 4),
             ]),
        dict(kop="Een bewijs schrijven",
             opdracht="Schrijf het bewijs uit met tussenstappen.",
             oefeningen=[
                 ("open", "Bewijs dat de som van twee even getallen even is.",
                  "Neem twee even getallen \\(2a\\) en \\(2b\\) met \\(a\\) en \\(b\\) geheel. De som is "
                  "\\(2a + 2b = 2(a + b)\\). Omdat \\(a + b\\) geheel is, is de som een veelvoud van "
                  "\\(2\\), dus even.", 4),
                 ("open", "Bewijs dat het product van twee opeenvolgende gehele getallen even is.",
                  "Van twee opeenvolgende getallen \\(n\\) en \\(n + 1\\) is er altijd één even. Een "
                  "product met een even factor is even.", 3),
             ]),
        dict(kop="Nog een bewijs",
             opdracht="Werk stap voor stap uit.",
             oefeningen=[
                 ("open", "Bewijs dat \\((a + b)^{2} = a^{2} + 2ab + b^{2}\\).",
                  "\\((a + b)^{2} = (a + b)(a + b)\\). Haakjes uitwerken geeft "
                  "\\(a \\cdot a + a \\cdot b + b \\cdot a + b \\cdot b\\), en samengenomen "
                  "\\(a^{2} + 2ab + b^{2}\\).", 4),
             ]),
        dict(kop="Waarom mag die stap?",
             opdracht="Noem de eigenschap waarop de stap steunt.",
             oefeningen=[
                 ("rij", [("van \\(x + 3 = 7\\) naar \\(x = 4\\)", "een eigenschap van gelijkheden"),
                          ("van \\(3 \\cdot 7 + 3 \\cdot 3\\) naar \\(3 \\cdot 10\\)", "de distributiviteit"),
                          ("van \\(2 \\cdot 5\\) naar \\(5 \\cdot 2\\)", "de commutativiteit"),
                          ("van \\((2 + 3) + 4\\) naar \\(2 + (3 + 4)\\)", "de associativiteit")],
                  "Eigenschap", WL),
                 ("kort", "Hoeveel is \\(2 + 3 \\cdot 4\\)?", "\\(14\\)", W),
                 ("open", "Waarom werk je in een bewijs met letters en niet met getallen?",
                  "Met letters geldt je redenering voor elk getal. Met één paar getallen geldt ze alleen "
                  "voor dat ene geval, en dat is geen bewijs.", 3),
             ]),
        dict(kop="Nodig of voldoende?",
             opdracht="Schrijf op of de voorwaarde nodig, voldoende of allebei is.",
             oefeningen=[
                 ("rij", [("deelbaar zijn door \\(4\\) om even te zijn", "voldoende"),
                          ("aanwezig zijn om te slagen", "nodig"),
                          ("een vierkant zijn om een rechthoek te zijn", "voldoende"),
                          ("even zijn om deelbaar te zijn door \\(2\\)", "nodig en voldoende")],
                  "Soort", WW),
                 ("open", "Bij welke logische bewerking is de voorwaarde zowel nodig als voldoende, "
                          "en waarom?",
                  "Bij de equivalentie \\(p \\Leftrightarrow q\\): de pijl gaat in beide richtingen, dus "
                  "\\(p\\) volgt uit \\(q\\) en \\(q\\) volgt uit \\(p\\).", 3),
             ]),
        dict(kop="Soorten redeneren",
             opdracht="Schrijf op of het inductief of deductief is.",
             oefeningen=[
                 ("rij", [("Ik tel de eerste tien priemgetallen en vermoed een patroon.", "inductief"),
                          ("Alle vierkanten zijn rechthoeken, dit is een vierkant, dus het is een "
                           "rechthoek.", "deductief"),
                          ("Bij elke driehoek die ik meet komt \\(180^{\circ}\\) uit, dus dat zal altijd "
                           "zo zijn.", "inductief"),
                          ("Uit de stelling van Pythagoras volgt dat \\(c = 5\\).", "deductief"),
                          ("Deze vijf leerlingen zijn moe, dus de hele klas is moe.", "inductief"),
                          ("\\(x + 3 = 7\\), dus \\(x = 4\\).", "deductief")],
                  "Soort redenering", WW),
             ]),
        dict(kop="Inductief is geen bewijs",
             opdracht="Schrijf je antwoord uit.",
             oefeningen=[
                 ("open", "Waarom is een inductieve redenering in de wiskunde nooit een bewijs?",
                  "Ze besluit uit een aantal gevallen iets over alle gevallen. Dat kan een goed vermoeden "
                  "opleveren, maar zekerheid geeft alleen een deductief bewijs dat voor elk geval geldt.", 4),
             ]),
        dict(kop="Schaalverandering",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de zijde van een vierkant gaat \\(\\times 3\\): de oppervlakte gaat", "\\(\\times 9\\)"),
                          ("de ribbe van een kubus gaat \\(\\times 2\\): het volume gaat", "\\(\\times 8\\)"),
                          ("de zijde gaat \\(\\times 2\\): de omtrek gaat", "\\(\\times 2\\)")],
                  "Factor", W),
                 ("open", "Iemand beweert dat een foto twee keer zo breed ook twee keer zoveel inkt "
                          "kost. Weerleg dat met een berekening.",
                  "Twee keer zo breed betekent meestal ook twee keer zo hoog, dus de oppervlakte gaat "
                  "\\(\\times 2^{2} = 4\\). Een foto van \\(10 \\times 15\\) cm heeft \\(150\\) cm², een "
                  "foto van \\(20 \\times 30\\) cm heeft \\(600\\) cm².", 3),
             ]),
    ])


# ============================================================
zet("ruimtefiguren-vlakke-voorstellingen-en-vectoren",
    titel="Ruimtefiguren, vlakke voorstellingen en vectoren",
    reeksen=[
        dict(kop="Ruimtefiguren herkennen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een balk: hoekpunten, ribben, grensvlakken", "\\(8\\), \\(12\\), \\(6\\)"),
                          ("een driezijdig prisma: hoekpunten, ribben, grensvlakken", "\\(6\\), \\(9\\), \\(5\\)"),
                          ("een vierzijdige piramide: hoekpunten, ribben, grensvlakken", "\\(5\\), \\(8\\), \\(5\\)"),
                          ("de formule van Euler", "\\(h - r + g = 2\\)"),
                          ("de ontwikkeling van een cilinder", "twee cirkels en een rechthoek"),
                          ("de ontwikkeling van een kegel", "een cirkel en een cirkelsector")],
                  "Vul aan", WL),
                 ("kort", "Controleer de formule van Euler bij de balk.", "\\(8 - 12 + 6 = 2\\)", WW),
             ]),
        dict(kop="Rechten en vlakken",
             opdracht="Schrijf de onderlinge ligging op.",
             oefeningen=[
                 ("rij", [("twee ribben van een kubus die elkaar in een hoekpunt raken", "snijdend"),
                          ("een ribbe van het bovenvlak en een ribbe van het ondervlak die niet "
                           "in hetzelfde zijvlak liggen", "kruisend"),
                          ("het bovenvlak en het ondervlak van een kubus", "evenwijdig"),
                          ("de doorsnede van twee snijdende vlakken", "een rechte"),
                          ("de doorsnede van twee snijdende rechten", "een punt")],
                  "Ligging", WW),
                 ("waar", "Twee vlakken kunnen kruisend zijn.", False),
             ]),
        dict(kop="Rekenen aan ruimtefiguren",
             opdracht="Reken uit. Gebruik \\(\\pi \\approx 3{,}14\\) en rond af op één decimaal.",
             oefeningen=[
                 ("rij", [("volume balk \\(4 \\times 5 \\times 6\\)", "\\(120\\)"),
                          ("volume cilinder \\(r = 3\\), \\(h = 10\\)", "\\(282{,}7\\)"),
                          ("volume kegel \\(r = 5\\), \\(h = 12\\)", "\\(314{,}2\\)"),
                          ("oppervlakte bol \\(r = 6\\)", "\\(452{,}4\\)"),
                          ("volume kubus met ribbe \\(7\\)", "\\(343\\)"),
                          ("oppervlakte kubus met ribbe \\(7\\)", "\\(294\\)")],
                  "Resultaat", WW),
             ]),
        dict(kop="Twee vraagstukken over volume",
             opdracht="Schrijf je berekening uit.",
             oefeningen=[
                 ("open", "Een cilindervormige regenton heeft een diameter van \\(60\\) cm en een hoogte "
                          "van \\(90\\) cm. Hoeveel liter gaat erin? Rond af op een liter.",
                  "\\(r = 30\\) cm. \\(V = \\pi \\cdot 30^{2} \\cdot 90 = \\pi \\cdot 81\\,000 \\approx "
                  "254\\,469\\) cm³. Eén liter is \\(1\\,000\\) cm³, dus ongeveer \\(254\\) liter.", 4),
                 ("kort", "Wat gebeurt er met het volume van een kubus als je elke ribbe verdubbelt?",
                  "\\(\\times 2^{3} = 8\\)", WW),
             ]),
        dict(kop="Vectoren berekenen",
             opdracht="Reken met \\(\\vec{u} = (3, -2)\\) en \\(\\vec{v} = (-1, 5)\\).",
             oefeningen=[
                 ("rij", [("\\(\\vec{u} + \\vec{v}\\)", "\\((2, 3)\\)"),
                          ("\\(\\vec{u} - \\vec{v}\\)", "\\((4, -7)\\)"),
                          ("\\(2\\vec{u}\\)", "\\((6, -4)\\)"),
                          ("\\(-\\vec{v}\\)", "\\((1, -5)\\)"),
                          ("\\(3\\vec{u} + \\vec{v}\\)", "\\((8, -1)\\)"),
                          ("\\(\\left|\\vec{u}\\right|\\)", "\\(\\sqrt{13}\\)")],
                  "Resultaat", WW),
                 ("rij", [("\\(\\vec{u} + \\left(-\\vec{u}\\right)\\)", "\\(\\vec{0}\\)"),
                          ("\\(\\frac{1}{2}\\vec{u}\\)", "\\(\\left(1{,}5;\\ -1\\right)\\)"),
                          ("\\(-2\\vec{v}\\)", "\\((2, -10)\\)")],
                  "Nog eens", WW),
             ]),
        dict(kop="Vectoren in een situatie",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("kort", "Een punt \\(A(2, 1)\\) wordt verschoven over \\((-4, 3)\\). Waar komt het terecht?",
                  "\\((-2, 4)\\)", WW),
                 ("open", "Twee vectoren zijn evenwijdig als de ene een veelvoud is van de andere. Zijn "
                          "\\((2, 6)\\) en \\((-3, -9)\\) evenwijdig? Toon het.",
                  "Ja: \\((-3, -9) = -1{,}5 \\cdot (2, 6)\\), dus ze zijn evenwijdig.", 3),
             ]),
        dict(kop="Vectoren in de natuurkunde",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Twee krachten van \\(5\\) N werken op hetzelfde punt: één naar het noorden, "
                          "één naar het zuiden. Wat is de som, en wat betekent dat voor het voorwerp?",
                  "De nulvector \\(\\vec{0}\\): de krachten heffen elkaar op, dus het voorwerp blijft in "
                  "evenwicht.", 3),
                 ("open", "Een boot vaart met \\(6\\) km/u naar het noorden; de stroming duwt met "
                          "\\(8\\) km/u naar het oosten. Hoe snel vaart de boot werkelijk?",
                  "De twee vectoren staan loodrecht, dus Pythagoras: \\(\\sqrt{6^{2} + 8^{2}} = "
                  "\\sqrt{100} = 10\\) km/u, schuin naar het noordoosten.", 4),
             ]),
    ])


# ============================================================
zet("schaalverandering-en-gelijkvormige-figuren",
    titel="Schaalverandering en gelijkvormige figuren",
    reeksen=[
        dict(kop="Schaal lezen",
             opdracht="Reken uit hoe groot het in het echt is.",
             oefeningen=[
                 ("rij", [("schaal \\(1 : 25\\,000\\), op de kaart \\(7\\) cm", "\\(1{,}75\\) km"),
                          ("schaal \\(1 : 100\\), op het plan \\(4{,}5\\) cm", "\\(4{,}5\\) m"),
                          ("schaal \\(1 : 200\\), op het plan \\(8\\) cm", "\\(16\\) m")],
                  "Antwoord", WW),
                 ("open", "Leg uit waarom een schaal \\(1 : 25\\,000\\) kleiner is dan \\(1 : 1\\,000\\), "
                          "terwijl \\(25\\,000\\) het grootste getal is.",
                  "Hoe groter het tweede getal, hoe meer de werkelijkheid verkleind is. Bij "
                  "\\(1 : 25\\,000\\) stelt één centimeter \\(250\\) meter voor, bij \\(1 : 1\\,000\\) maar "
                  "tien meter.", 3),
             ]),
        dict(kop="De andere kant op",
             opdracht="Reken uit hoe groot het op de tekening is.",
             oefeningen=[
                 ("rij", [("schaal \\(1 : 50\\,000\\), in het echt \\(12\\) km", "\\(24\\) cm"),
                          ("schaal \\(2 : 1\\), voorwerp van \\(3\\) mm", "\\(6\\) mm"),
                          ("schaal \\(1 : 20\\), in het echt \\(3\\) m", "\\(15\\) cm")],
                  "Antwoord", WW),
             ]),
        dict(kop="Lengte, oppervlakte en volume",
             opdracht="Vul de tabel aan met de factor.",
             oefeningen=[
                 ("tabel", ["\\(k\\)", "lengte \\(\\times\\)", "oppervlakte \\(\\times\\)", "volume \\(\\times\\)"],
                  [["\\(2\\)", None, None, None], ["\\(3\\)", None, None, None],
                   ["\\(\\frac{1}{2}\\)", None, None, None], ["\\(10\\)", None, None, None]],
                  "\\(k = 2\\): \\(2\\), \\(4\\), \\(8\\) · \\(k = 3\\): \\(3\\), \\(9\\), \\(27\\) · "
                  "\\(k = \\frac{1}{2}\\): \\(\\frac{1}{2}\\), \\(\\frac{1}{4}\\), \\(\\frac{1}{8}\\) · "
                  "\\(k = 10\\): \\(10\\), \\(100\\), \\(1\\,000\\)", "70px"),
                 ("waar", "Bij \\(k = 2\\) wordt het volume ook \\(\\times 2\\).", False),
             ]),
        dict(kop="Rekenen met de factor",
             opdracht="Schrijf je berekening uit.",
             oefeningen=[
                 ("open", "Een maquette is op schaal \\(1 : 50\\). Het echte gebouw heeft een gevel van "
                          "\\(200\\) m². Hoeveel is dat op de maquette?",
                  "De oppervlakte wordt gedeeld door \\(50^{2} = 2\\,500\\). \\(200 : 2\\,500 = 0{,}08\\) m², "
                  "dus \\(800\\) cm².", 3),
                 ("open", "Een flesje van \\(0{,}5\\) liter wordt in alle richtingen twee keer zo groot "
                          "gemaakt. Hoeveel liter gaat er dan in?",
                  "Het volume wordt \\(2^{3} = 8\\) keer zo groot: \\(4\\) liter.", 2),
             ]),
        dict(kop="Waarom die macht?",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een foto wordt op dubbele breedte afgedrukt, met dezelfde vorm. Hoeveel keer "
                          "zoveel inkt is er nodig, en waarom?",
                  "Vier keer zoveel: de inkt volgt de oppervlakte, en die gaat met \\(k^{2} = 2^{2} = 4\\).", 3),
                 ("kort", "Met welke factor gaat het volume bij \\(k = 4\\)?", "\\(\\times 64\\)", W),
             ]),
        dict(kop="Gelijkvormige driehoeken",
             opdracht="Reken de ontbrekende maten uit.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Driehoek \\(ABC\\) is gelijkvormig met driehoek \\(DEF\\). "
                  "\\(\\left|AB\\right| = 6\\), \\(\\left|BC\\right| = 8\\), \\(\\left|AC\\right| = 10\\) "
                  "en \\(\\left|DE\\right| = 9\\).</em></p>"),
                 ("kort", "Wat is \\(k\\) van \\(ABC\\) naar \\(DEF\\)?", "\\(1{,}5\\)", W),
                 ("kort", "Hoe lang is \\(\\left|EF\\right|\\)?", "\\(12\\)", W),
                 ("kort", "Hoe lang is \\(\\left|DF\\right|\\)?", "\\(15\\)", W),
                 ("kort", "Hoeveel keer zo groot is de oppervlakte van \\(DEF\\)?", "\\(\\times 2{,}25\\)", WW),
             ]),
        dict(kop="Welk kenmerk?",
             opdracht="Schrijf op welk gelijkvormigheidskenmerk je gebruikt: HH, ZHZ of ZZZ.",
             oefeningen=[
                 ("rij", [("twee hoeken van de ene zijn gelijk aan twee hoeken van de andere", "HH"),
                          ("de drie zijden staan in dezelfde verhouding", "ZZZ"),
                          ("twee zijden in verhouding en de hoek ertussen gelijk", "ZHZ"),
                          ("de stok en de boom bij een schaduwmeting", "HH")],
                  "Kenmerk", WW),
             ]),
        dict(kop="De derde hoek",
             opdracht="Reken uit en leg uit.",
             oefeningen=[
                 ("kort", "Een driehoek heeft hoeken van \\(40^{\circ}\\) en \\(60^{\circ}\\). "
                          "Hoe groot is de derde?", "\\(80^{\circ}\\)", W),
                 ("open", "Waarom volstaan twee gelijke hoeken, en waarom vraagt de vakfiche dat je het "
                          "kenmerk erbij noemt?",
                  "De hoekensom is \\(180^{\circ}\\), dus de derde hoek ligt vast zodra je er twee kent. "
                  "Het kenmerk is de verantwoording: zonder kenmerk weet je niet waarom je die verhouding "
                  "mag opstellen.", 4),
             ]),
        dict(kop="Schaduwmeting",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Een boom werpt een schaduw van \\(12\\) m. Een stok van \\(1{,}5\\) m werpt op "
                          "hetzelfde moment een schaduw van \\(2\\) m. Hoe hoog is de boom?",
                  "De driehoeken zijn gelijkvormig: \\(\\frac{h}{12} = \\frac{1{,}5}{2}\\), dus "
                  "\\(h = 9\\) m.", 3),
                 ("open", "Noem de twee voorwaarden waaraan gelijkvormige figuren voldoen.",
                  "Hun overeenkomstige hoeken zijn gelijk, en hun overeenkomstige zijden staan in dezelfde "
                  "verhouding.", 3),
             ]),
    ])


# ============================================================
zet("pythagoras-en-de-goniometrische-verhoudingen",
    titel="Pythagoras en de goniometrische verhoudingen",
    reeksen=[
        dict(kop="De schuine zijde",
             opdracht="Reken uit. Rond af op één decimaal waar nodig.",
             oefeningen=[
                 ("rij", [("rechthoekszijden \\(9\\) en \\(12\\)", "\\(15\\)"),
                          ("rechthoekszijden \\(7\\) en \\(24\\)", "\\(25\\)"),
                          ("rechthoekszijden \\(8\\) en \\(15\\)", "\\(17\\)"),
                          ("rechthoekszijden \\(5\\) en \\(5\\)", "\\(\\sqrt{50} \\approx 7{,}1\\)")],
                  "Hoe lang is ze?", WW),
             ]),
        dict(kop="De andere rechthoekszijde",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("schuine zijde \\(13\\), rechthoekszijde \\(5\\)", "\\(12\\)"),
                          ("schuine zijde \\(10\\), rechthoekszijde \\(6\\)", "\\(8\\)"),
                          ("schuine zijde \\(26\\), rechthoekszijde \\(24\\)", "\\(10\\)")],
                  "Hoe lang is ze?", WW),
                 ("waar", "In een rechthoekige driehoek kan een rechthoekszijde langer zijn dan de "
                          "schuine zijde.", False),
             ]),
        dict(kop="Rechthoekig of niet?",
             opdracht="Toon je berekening met de omgekeerde stelling.",
             oefeningen=[
                 ("open", "Is een driehoek met zijden \\(6\\), \\(8\\) en \\(11\\) rechthoekig?",
                  "\\(6^{2} + 8^{2} = 36 + 64 = 100\\), maar \\(11^{2} = 121\\). Omdat "
                  "\\(100 \\neq 121\\) is de driehoek niet rechthoekig.", 3),
             ]),
        dict(kop="Nog een drietal",
             opdracht="Toon ook hier je berekening.",
             oefeningen=[
                 ("open", "Is een driehoek met zijden \\(20\\), \\(21\\) en \\(29\\) rechthoekig?",
                  "\\(400 + 441 = 841\\) en \\(29^{2} = 841\\). Ja, de hoek tegenover \\(29\\) is "
                  "recht.", 3),
             ]),
        dict(kop="De afstand tussen twee punten",
             opdracht="Gebruik \\(\\left|AB\\right| = \\sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}\\).",
             oefeningen=[
                 ("rij", [("\\(A(0, 0)\\) en \\(B(6, 8)\\)", "\\(10\\)"),
                          ("\\(A(2, 3)\\) en \\(B(5, 7)\\)", "\\(5\\)"),
                          ("\\(A(-1, 2)\\) en \\(B(3, -1)\\)", "\\(5\\)")],
                  "Afstand", WW),
             ]),
        dict(kop="In de ruimte",
             opdracht="Pas Pythagoras twee keer toe.",
             oefeningen=[
                 ("open", "Een balk is \\(3\\) bij \\(4\\) bij \\(12\\). Hoe lang is de "
                          "ruimtediagonaal?",
                  "Eerst het grondvlak: \\(\\sqrt{3^{2} + 4^{2}} = 5\\). Dan met de hoogte: "
                  "\\(\\sqrt{5^{2} + 12^{2}} = \\sqrt{169} = 13\\).", 4),
                 ("kort", "Hoe lang is de ruimtediagonaal van een kubus met ribbe \\(2\\)?",
                  "\\(2\\sqrt{3} \\approx 3{,}46\\)", WW),
             ]),
        dict(kop="Sinus, cosinus en tangens",
             opdracht="Vul aan. Werk in een rechthoekige driehoek met scherpe hoek \\(\\alpha\\).",
             oefeningen=[
                 ("rij", [("\\(\\sin \\alpha =\\)", "\\(\\frac{\\text{overstaande}}{\\text{schuine}}\\)"),
                          ("\\(\\cos \\alpha =\\)", "\\(\\frac{\\text{aanliggende}}{\\text{schuine}}\\)"),
                          ("\\(\\tan \\alpha =\\)", "\\(\\frac{\\text{overstaande}}{\\text{aanliggende}}\\)")],
                  "Welke zijden?", WL),
                 ("rij", [("\\(\\sin 30^{\\circ}\\)", "\\(0{,}5\\)"),
                          ("\\(\\cos 60^{\\circ}\\)", "\\(0{,}5\\)"),
                          ("\\(\\tan 45^{\\circ}\\)", "\\(1\\)")],
                  "Welk getal?", W),
             ]),
        dict(kop="De grondformule",
             opdracht="Gebruik \\(\\sin^{2}\\alpha + \\cos^{2}\\alpha = 1\\).",
             oefeningen=[
                 ("kort", "\\(\\sin \\alpha = 0{,}8\\) en \\(\\alpha\\) is scherp. Wat is "
                          "\\(\\cos \\alpha\\)?", "\\(0{,}6\\)", W),
                 ("kort", "\\(\\cos \\alpha = \\frac{5}{13}\\). Wat is \\(\\sin \\alpha\\)?",
                  "\\(\\frac{12}{13}\\)", W),
             ]),
        dict(kop="Waarom die formule?",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de grondformule rechtstreeks uit Pythagoras volgt.",
                  "In een rechthoekige driehoek is \\(a^{2} + b^{2} = c^{2}\\). Deel alles door "
                  "\\(c^{2}\\): \\(\\left(\\frac{a}{c}\\right)^{2} + \\left(\\frac{b}{c}\\right)^{2} = 1\\), "
                  "en dat zijn net \\(\\sin^{2}\\alpha\\) en \\(\\cos^{2}\\alpha\\).", 4),
             ]),
        dict(kop="Een hoek berekenen",
             opdracht="Rond af op \\(0{,}1^{\\circ}\\).",
             oefeningen=[
                 ("open", "De overstaande zijde is \\(5\\) en de aanliggende \\(12\\). Hoe groot is "
                          "\\(\\alpha\\)?",
                  "\\(\\tan \\alpha = \\frac{5}{12} \\approx 0{,}4167\\), dus "
                  "\\(\\alpha \\approx 22{,}6^{\\circ}\\).", 3),
                 ("open", "Er geldt \\(\\sin \\alpha = 0{,}6\\). Hoe groot is \\(\\alpha\\)?",
                  "\\(\\alpha \\approx 36{,}9^{\\circ}\\).", 2),
             ]),
        dict(kop="Een zijde berekenen",
             opdracht="Schrijf eerst op welk goniometrisch getal je kiest.",
             oefeningen=[
                 ("open", "Een ladder van \\(4\\) m staat onder \\(70^{\\circ}\\) tegen een muur. Tot "
                          "op welke hoogte reikt ze?",
                  "De ladder is de schuine zijde en de hoogte de overstaande, dus sinus: "
                  "\\(4 \\cdot \\sin 70^{\\circ} \\approx 3{,}76\\) m.", 3),
                 ("open", "Een helling stijgt \\(8\\) m over een horizontale afstand van \\(100\\) m. "
                          "Hoeveel procent is dat, en hoeveel graden?",
                  "\\(\\frac{8}{100} = 8\\,\\%\\). De hoek is \\(\\arctan 0{,}08 \\approx "
                  "4{,}6^{\\circ}\\).", 3),
             ]),
        dict(kop="Toepassen",
             opdracht="Maak een schets en reken uit.",
             oefeningen=[
                 ("teken", "Een boom staat \\(20\\) m van je af. Je kijkt onder \\(35^{\\circ}\\) "
                           "omhoog naar de top; je ogen zitten \\(1{,}6\\) m hoog. Teken de situatie.",
                  "Een rechthoekige driehoek met de horizontale zijde \\(20\\) m, de hoek van "
                  "\\(35^{\\circ}\\) bij het oog, en de verticale zijde die je zoekt, plus "
                  "\\(1{,}6\\) m voor de ooghoogte.", 45),
                 ("open", "Reken nu de hoogte van de boom uit.",
                  "\\(20 \\cdot \\tan 35^{\\circ} \\approx 14{,}0\\) m, plus \\(1{,}6\\) m "
                  "ooghoogte, dus ongeveer \\(15{,}6\\) m.", 3),
             ]),
    ])


# ============================================================
zet("formules-omvormen",
    titel="Formules omvormen",
    reeksen=[
        dict(kop="Vorm om naar de gevraagde letter",
             opdracht="Schrijf de omgevormde formule op.",
             oefeningen=[
                 ("rij", [("\\(A = l \\cdot b\\), naar \\(b\\)", "\\(b = \\frac{A}{l}\\)"),
                          ("\\(P = 2(l + b)\\), naar \\(l\\)", "\\(l = \\frac{P}{2} - b\\)"),
                          ("\\(v = \\frac{s}{t}\\), naar \\(t\\)", "\\(t = \\frac{s}{v}\\)")],
                  "Omgevormd", WL),
             ]),
        dict(kop="Nog eens omvormen",
             opdracht="Schrijf de omgevormde formule op.",
             oefeningen=[
                 ("rij", [("\\(A = \\pi r^{2}\\), naar \\(r\\)", "\\(r = \\sqrt{\\frac{A}{\\pi}}\\)"),
                          ("\\(F = m \\cdot a\\), naar \\(a\\)", "\\(a = \\frac{F}{m}\\)"),
                          ("\\(C = \\frac{5}{9}(F - 32)\\), naar \\(F\\)", "\\(F = \\frac{9C}{5} + 32\\)")],
                  "Omgevormd", WL),
             ]),
        dict(kop="Stap voor stap",
             opdracht="Schrijf elke tussenstap op.",
             oefeningen=[
                 ("open", "Vorm \\(y = 3x + 7\\) om naar \\(x\\).",
                  "\\(y - 7 = 3x\\), dus \\(x = \\frac{y - 7}{3}\\).", 3),
                 ("kort", "Vorm \\(V = \\frac{1}{3}\\pi r^{2} h\\) om naar \\(h\\).",
                  "\\(h = \\frac{3V}{\\pi r^{2}}\\)", WL),
             ]),
        dict(kop="Mag dat zomaar?",
             opdracht="Antwoord en verantwoord.",
             oefeningen=[
                 ("open", "Bij \\(y = a \\cdot x\\) deel je beide kanten door \\(x\\). Welke voorwaarde "
                          "hoort daarbij, en waarom?",
                  "\\(x \\neq 0\\), want delen door \\(0\\) is niet gedefinieerd.", 3),
                 ("waar", "Door een gelijkheid aan beide kanten met \\((-1)\\) te vermenigvuldigen keert "
                          "er een teken om.", False),
             ]),
        dict(kop="Invullen en uitrekenen",
             opdracht="Vul in en reken uit.",
             oefeningen=[
                 ("open", "Zet \\(25\\) °C om naar graden Fahrenheit met \\(F = \\frac{9C}{5} + 32\\).",
                  "\\(\\frac{9 \\cdot 25}{5} + 32 = 45 + 32 = 77\\) °F.", 2),
                 ("open", "Een cirkel heeft \\(A = 78{,}5\\) cm². Hoe groot is \\(r\\)? Gebruik "
                          "\\(\\pi \\approx 3{,}14\\).",
                  "\\(r = \\sqrt{\\frac{78{,}5}{3{,}14}} = \\sqrt{25} = 5\\) cm.", 3),
             ]),
        dict(kop="Uit het dagelijks leven",
             opdracht="Schrijf je berekening uit.",
             oefeningen=[
                 ("open", "Een auto rijdt \\(150\\) km in \\(1\\) uur \\(15\\) minuten. Wat is de "
                          "gemiddelde snelheid?",
                  "\\(1\\) uur \\(15\\) min is \\(1{,}25\\) uur. "
                  "\\(v = \\frac{150}{1{,}25} = 120\\) km/u.", 3),
                 ("open", "Een rechthoek heeft \\(P = 46\\) cm en \\(l = 14\\) cm. Hoe breed is ze?",
                  "\\(46 = 2(14 + b)\\), dus \\(23 = 14 + b\\) en \\(b = 9\\) cm.", 3),
             ]),
        dict(kop="Uit de natuurwetenschappen",
             opdracht="Vorm om naar de gevraagde letter.",
             oefeningen=[
                 ("rij", [("\\(\\rho = \\frac{m}{V}\\), naar \\(V\\)", "\\(V = \\frac{m}{\\rho}\\)"),
                          ("\\(U = I \\cdot R\\), naar \\(I\\)", "\\(I = \\frac{U}{R}\\)"),
                          ("\\(p = \\frac{F}{A}\\), naar \\(F\\)", "\\(F = p \\cdot A\\)"),
                          ("\\(P = \\frac{E}{t}\\), naar \\(t\\)", "\\(t = \\frac{E}{P}\\)")],
                  "Omgevormd", WL),
             ]),
        dict(kop="Rekenen met die formules",
             opdracht="Vul in en reken uit.",
             oefeningen=[
                 ("kort", "Hoeveel weegt \\(3\\) l water? Gebruik \\(\\rho = 1\\) kg/l.",
                  "\\(3\\) kg", W),
                 ("kort", "Er geldt \\(U = 230\\) V en \\(R = 46\\) ohm. Hoe groot is \\(I\\)?",
                  "\\(5\\) A", W),
                 ("open", "Een toestel van \\(2\\,000\\) W draait \\(30\\) minuten. Hoeveel kWh "
                          "verbruikt het?",
                  "\\(E = P \\cdot t = 2 \\text{ kW} \\cdot 0{,}5 \\text{ h} = 1\\) kWh.", 3),
             ]),
        dict(kop="Evenredigheid",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("\\(y = 4x\\): welk soort evenredigheid?", "recht evenredig"),
                          ("\\(y = \\frac{12}{x}\\): welk soort?", "omgekeerd evenredig"),
                          ("bij recht evenredig blijft dit gelijk", "\\(\\frac{y}{x}\\)"),
                          ("bij omgekeerd evenredig blijft dit gelijk", "\\(x \\cdot y\\)")],
                  "Antwoord", WL),
             ]),
        dict(kop="Wat gebeurt er dan?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("\\(y = 4x\\), als \\(x\\) verdubbelt", "\\(y\\) verdubbelt"),
                          ("\\(y = \\frac{12}{x}\\), als \\(x\\) verdubbelt", "\\(y\\) halveert"),
                          ("\\(E_{k} = \\frac{1}{2}mv^{2}\\), als \\(v\\) verdubbelt",
                           "\\(E_{k}\\) wordt \\(\\times 4\\)")],
                  "Antwoord", WL),
                 ("open", "Vier werkmensen doen een klus in zes dagen. Hoeveel dagen doen zes "
                          "werkmensen erover, als ze even snel werken?",
                  "Het product blijft gelijk: \\(4 \\cdot 6 = 24\\) werkdagen. Met zes mensen: "
                  "\\(\\frac{24}{6} = 4\\) dagen.", 3),
             ]),
    ])


# ============================================================
zet("eerstegraadsvergelijkingen-en-ongelijkheden",
    titel="Eerstegraadsvergelijkingen en -ongelijkheden",
    reeksen=[
        dict(kop="Los op",
             opdracht="Schrijf de oplossing op.",
             oefeningen=[
                 ("rij", [("\\(3x + 5 = 20\\)", "\\(x = 5\\)"),
                          ("\\(7 - 2x = 1\\)", "\\(x = 3\\)"),
                          ("\\(4(x - 3) = 8\\)", "\\(x = 5\\)")],
                  "Wat is \\(x\\)?", W),
             ]),
        dict(kop="Nog eens oplossen",
             opdracht="Schrijf de oplossing op.",
             oefeningen=[
                 ("rij", [("\\(\\frac{x}{4} + 2 = 5\\)", "\\(x = 12\\)"),
                          ("\\(5x - 3 = 2x + 9\\)", "\\(x = 4\\)"),
                          ("\\(2(x + 1) = 3(x - 2)\\)", "\\(x = 8\\)")],
                  "Wat is \\(x\\)?", W),
             ]),
        dict(kop="Met breuken",
             opdracht="Schrijf al je tussenstappen op.",
             oefeningen=[
                 ("open", "Los op: \\(\\frac{x - 1}{3} + 2 = \\frac{x}{2}\\).",
                  "Vermenigvuldig alles met \\(6\\): \\(2(x - 1) + 12 = 3x\\), dus "
                  "\\(2x + 10 = 3x\\) en \\(x = 10\\).", 4),
             ]),
        dict(kop="Wat betekent dat?",
             opdracht="Antwoord in een volle zin.",
             oefeningen=[
                 ("open", "Wat betekent het als je bij het oplossen \\(0 = 5\\) uitkomt?",
                  "Er is geen enkele oplossing: de vergelijking is strijdig, \\(V = \\emptyset\\).", 2),
                 ("open", "En als je \\(0 = 0\\) uitkomt?",
                  "Elke \\(x\\) is een oplossing: de vergelijking is een identiteit, "
                  "\\(V = \\mathbb{R}\\).", 2),
             ]),
        dict(kop="Ongelijkheden",
             opdracht="Los op en schrijf de oplossing als interval.",
             oefeningen=[
                 ("rij", [("\\(2x + 1 > 9\\)", "\\(x > 4\\), dus \\(\\left]4, +\\infty\\right[\\)"),
                          ("\\(-3x \\geq 12\\)", "\\(x \\leq -4\\), dus \\(\\left]-\\infty, -4\\right]\\)"),
                          ("\\(\\frac{x}{2} - 1 < 3\\)", "\\(x < 8\\), dus \\(\\left]-\\infty, 8\\right[\\)")],
                  "Oplossing", WL),
             ]),
        dict(kop="Nog drie ongelijkheden",
             opdracht="Los op en schrijf de oplossing als interval.",
             oefeningen=[
                 ("rij", [("\\(5 - x \\leq 2\\)", "\\(x \\geq 3\\), dus \\(\\left[3, +\\infty\\right[\\)"),
                          ("\\(4x + 3 < x - 6\\)", "\\(x < -3\\), dus \\(\\left]-\\infty, -3\\right[\\)"),
                          ("\\(-2(x - 1) > 6\\)", "\\(x < -2\\), dus \\(\\left]-\\infty, -2\\right[\\)")],
                  "Oplossing", WL),
             ]),
        dict(kop="De omkeerregel",
             opdracht="Antwoord en verantwoord.",
             oefeningen=[
                 ("open", "Waarom keert het teken om bij \\(-3x \\geq 12\\)?",
                  "Je deelt beide leden door een negatief getal; dan keert de volgorde van de getallen "
                  "om en moet het ongelijkheidsteken mee omdraaien.", 3),
                 ("waar", "Bij \\(x + 7 < 10\\) moet het teken omkeren.", False),
             ]),
        dict(kop="Op de getallenas",
             opdracht="Teken de oplossing met een open of een vol bolletje aan de grens.",
             oefeningen=[
                 ("teken", "Teken de oplossing van \\(x \\geq -1\\).",
                  "Een vol bolletje op \\(-1\\) en een streep naar rechts: "
                  "\\(\\left[-1, +\\infty\\right[\\).", 30),
             ]),
        dict(kop="En nog een",
             opdracht="Let op het soort bolletje.",
             oefeningen=[
                 ("teken", "Teken de oplossing van \\(x < 2\\).",
                  "Een open bolletje op \\(2\\) en een streep naar links: "
                  "\\(\\left]-\\infty, 2\\right[\\).", 30),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Stel een vergelijking op en los ze op.",
             oefeningen=[
                 ("open", "Een taxi vraagt \\(3{,}50\\) euro opstapgeld en \\(1{,}80\\) euro per "
                          "kilometer. Hoeveel kilometer rijd je voor \\(30{,}50\\) euro?",
                  "\\(3{,}50 + 1{,}80x = 30{,}50\\), dus \\(1{,}80x = 27\\) en \\(x = 15\\) km.", 3),
                 ("open", "Lotte is drie keer zo oud als haar broer. Samen zijn ze \\(32\\). Hoe oud "
                          "is elk?",
                  "\\(x + 3x = 32\\), dus \\(4x = 32\\) en \\(x = 8\\). De broer is \\(8\\) en Lotte "
                          "is \\(24\\).", 3),
             ]),
        dict(kop="Nog twee vraagstukken",
             opdracht="Stel een vergelijking of een ongelijkheid op.",
             oefeningen=[
                 ("open", "Een rechthoek is \\(4\\) cm langer dan breed en heeft \\(P = 36\\) cm. Hoe "
                          "groot is ze?",
                  "\\(2(b + 4 + b) = 36\\), dus \\(4b + 8 = 36\\), \\(b = 7\\) en \\(l = 11\\) cm.", 3),
                 ("open", "Een abonnement kost \\(12\\) euro per maand plus \\(0{,}05\\) euro per "
                          "minuut. Vanaf hoeveel minuten betaal je meer dan \\(20\\) euro?",
                  "\\(12 + 0{,}05x > 20\\), dus \\(0{,}05x > 8\\) en \\(x > 160\\) minuten.", 3),
             ]),
        dict(kop="Grafisch lezen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Een stijgende rechte snijdt de \\(x\\)-as in \\(-2\\). Voor welke \\(x\\) is "
                          "\\(f(x) > 0\\)?", "\\(x > -2\\)", WW),
                 ("kort", "Een dalende rechte snijdt de \\(x\\)-as in \\(5\\). Voor welke \\(x\\) is "
                          "\\(f(x) < 0\\)?", "\\(x > 5\\)", WW),
             ]),
    ])


# ============================================================
zet("stelsels-van-twee-vergelijkingen",
    titel="Stelsels van twee vergelijkingen",
    reeksen=[
        dict(kop="Los op met substitutie",
             opdracht="Werk uit en schrijf het koppel \\((x, y)\\) op.",
             oefeningen=[
                 ("open", "\\(\\begin{cases} y = 2x + 1 \\\\ 3x + y = 11 \\end{cases}\\)",
                  "\\(3x + 2x + 1 = 11\\), dus \\(5x = 10\\) en \\(x = 2\\); \\(y = 5\\). "
                  "Oplossing \\((2, 5)\\).", 3),
                 ("open", "\\(\\begin{cases} x = y - 3 \\\\ 2x + y = 9 \\end{cases}\\)",
                  "\\(2(y - 3) + y = 9\\), dus \\(3y = 15\\) en \\(y = 5\\); \\(x = 2\\). "
                  "Oplossing \\((2, 5)\\).", 3),
             ]),
        dict(kop="Los op met combinatie",
             opdracht="Werk uit en schrijf het koppel \\((x, y)\\) op.",
             oefeningen=[
                 ("open", "\\(\\begin{cases} 2x + 3y = 16 \\\\ 2x - y = 0 \\end{cases}\\)",
                  "Trek de tweede van de eerste af: \\(4y = 16\\), dus \\(y = 4\\). Vul in in de "
                  "tweede: \\(2x - 4 = 0\\), dus \\(x = 2\\). Oplossing \\((2, 4)\\).", 4),
                 ("open", "\\(\\begin{cases} 3x + 2y = 12 \\\\ x - 2y = 4 \\end{cases}\\)",
                  "Tel op: \\(4x = 16\\), dus \\(x = 4\\); dan geeft \\(4 - 2y = 4\\) dat "
                  "\\(y = 0\\). Oplossing \\((4, 0)\\).", 3),
             ]),
        dict(kop="Een stelsel dat je eerst moet klaarmaken",
             opdracht="Vermenigvuldig eerst een vergelijking.",
             oefeningen=[
                 ("open", "\\(\\begin{cases} 5x + 2y = 1 \\\\ 3x - 4y = 11 \\end{cases}\\)",
                  "Vermenigvuldig de eerste met \\(2\\): \\(10x + 4y = 2\\). Tel op bij de tweede: "
                  "\\(13x = 13\\), dus \\(x = 1\\); dan geeft \\(5 + 2y = 1\\) dat \\(y = -2\\). "
                  "Oplossing \\((1, -2)\\).", 4),
             ]),
        dict(kop="Met gelijkstelling",
             opdracht="Stel de rechterleden gelijk.",
             oefeningen=[
                 ("open", "\\(\\begin{cases} y = 4x - 3 \\\\ y = 2x + 7 \\end{cases}\\)",
                  "\\(4x - 3 = 2x + 7\\), dus \\(2x = 10\\) en \\(x = 5\\); \\(y = 17\\). "
                  "Oplossing \\((5, 17)\\).", 3),
                 ("kort", "Welke methode gebruik je als in beide vergelijkingen \\(y\\) alleen staat?",
                  "de gelijkstellingsmethode", WL),
             ]),
        dict(kop="Hoeveel oplossingen?",
             opdracht="Schrijf op: één oplossing, geen oplossing of oneindig veel.",
             oefeningen=[
                 ("rij", [("\\(y = 2x + 1\\) en \\(y = 2x + 4\\)", "geen oplossing"),
                          ("\\(y = 2x + 1\\) en \\(y = 3x - 2\\)", "één oplossing"),
                          ("\\(y = 2x + 1\\) en \\(2y = 4x + 2\\)", "oneindig veel")],
                  "Hoeveel?", WW),
             ]),
        dict(kop="Nog drie stelsels bekijken",
             opdracht="Schrijf op: één oplossing, geen oplossing of oneindig veel.",
             oefeningen=[
                 ("rij", [("\\(x + y = 5\\) en \\(x + y = 7\\)", "geen oplossing"),
                          ("\\(x - y = 0\\) en \\(x + y = 4\\)", "één oplossing"),
                          ("\\(3x + 3y = 9\\) en \\(x + y = 3\\)", "oneindig veel")],
                  "Hoeveel?", WW),
             ]),
        dict(kop="Wat zie je op de grafiek?",
             opdracht="Antwoord in een volle zin.",
             oefeningen=[
                 ("open", "Wat betekent geen oplossing als je de twee rechten tekent?",
                  "De rechten zijn evenwijdig en vallen niet samen, dus ze snijden elkaar nergens.", 2),
                 ("open", "En wat zie je bij oneindig veel oplossingen?",
                  "De twee rechten vallen samen: elk punt van de rechte is een oplossing.", 2),
             ]),
        dict(kop="Het soort benoemen",
             opdracht="Vul aan met bepaald, strijdig of onbepaald.",
             oefeningen=[
                 ("rij", [("er komt \\(0 = 5\\) uit", "strijdig"),
                          ("er komt \\(0 = 0\\) uit", "onbepaald"),
                          ("er komt \\(x = 3\\) uit", "bepaald")],
                  "Welk soort?", WW),
             ]),
        dict(kop="Een vraagstuk met prijzen",
             opdracht="Stel een stelsel op en los het op.",
             oefeningen=[
                 ("open", "Drie broodjes en twee koffies kosten \\(13\\) euro. Eén broodje en vier "
                          "koffies kosten \\(11\\) euro. Wat kost elk?",
                  "\\(3b + 2k = 13\\) en \\(b + 4k = 11\\). Uit de tweede: "
                  "\\(b = 11 - 4k\\). Invullen: \\(33 - 12k + 2k = 13\\), dus \\(10k = 20\\) en "
                  "\\(k = 2\\); \\(b = 3\\). Een broodje kost \\(3\\) euro, een koffie \\(2\\) euro.", 5),
             ]),
        dict(kop="Een vraagstuk met tickets",
             opdracht="Stel een stelsel op en los het op.",
             oefeningen=[
                 ("open", "Een zaal telt \\(120\\) plaatsen. Een ticket vooraan kost \\(15\\) euro, "
                          "achteraan \\(9\\) euro. Alles is uitverkocht en de opbrengst is "
                          "\\(1\\,320\\) euro. Hoeveel tickets van elke soort?",
                  "\\(v + a = 120\\) en \\(15v + 9a = 1\\,320\\). Uit de "
                  "eerste: \\(a = 120 - v\\). Invullen: \\(15v + 1\\,080 - 9v = 1\\,320\\), dus "
                  "\\(6v = 240\\) en \\(v = 40\\); \\(a = 80\\).", 5),
             ]),
    ])


# ============================================================
zet("tweedegraadsvergelijkingen",
    titel="Tweedegraadsvergelijkingen",
    reeksen=[
        dict(kop="Ontbinden",
             opdracht="Ontbind in factoren.",
             oefeningen=[
                 ("rij", [("\\(x^{2} - 9\\)", "\\((x - 3)(x + 3)\\)"),
                          ("\\(x^{2} + 6x + 9\\)", "\\((x + 3)^{2}\\)"),
                          ("\\(x^{2} - 5x + 6\\)", "\\((x - 2)(x - 3)\\)")],
                  "Ontbonden", WL),
                 ("open", "Los op door te ontbinden: \\(x^{2} - 7x + 12 = 0\\).",
                  "\\((x - 3)(x - 4) = 0\\), dus \\(x = 3\\) of \\(x = 4\\).", 3),
             ]),
        dict(kop="Nog drie ontbinden",
             opdracht="Ontbind in factoren.",
             oefeningen=[
                 ("rij", [("\\(x^{2} + 2x - 15\\)", "\\((x + 5)(x - 3)\\)"),
                          ("\\(2x^{2} - 8x\\)", "\\(2x(x - 4)\\)"),
                          ("\\(x^{2} - 4x + 4\\)", "\\((x - 2)^{2}\\)")],
                  "Ontbonden", WL),
             ]),
        dict(kop="De discriminant",
             opdracht="Bereken \\(D\\) en zeg hoeveel oplossingen er zijn.",
             oefeningen=[
                 ("tabel", ["vergelijking", "\\(D\\)", "aantal oplossingen"],
                  [["\\(x^{2} - 6x + 5 = 0\\)", None, None],
                   ["\\(x^{2} + 4x + 4 = 0\\)", None, None],
                   ["\\(x^{2} + x + 3 = 0\\)", None, None]],
                  "\\(D = 16\\), twee · \\(D = 0\\), één · \\(D = -11\\), geen", "110px"),
             ]),
        dict(kop="Nog drie keer de discriminant",
             opdracht="Bereken \\(D\\) en zeg hoeveel oplossingen er zijn.",
             oefeningen=[
                 ("tabel", ["vergelijking", "\\(D\\)", "aantal oplossingen"],
                  [["\\(2x^{2} - 3x - 2 = 0\\)", None, None],
                   ["\\(x^{2} - 2x - 8 = 0\\)", None, None],
                   ["\\(3x^{2} + 2x + 1 = 0\\)", None, None]],
                  "\\(D = 25\\), twee · \\(D = 36\\), twee · \\(D = -8\\), geen", "110px"),
             ]),
        dict(kop="Met de formule",
             opdracht="Schrijf je tussenstappen op.",
             oefeningen=[
                 ("open", "Schrijf de formule voor de oplossingen op en los \\(x^{2} - 6x + 5 = 0\\) "
                          "ermee op.",
                  "\\(x = \\frac{-b \\pm \\sqrt{D}}{2a}\\). Hier is \\(D = 36 - 20 = 16\\) en "
                  "\\(\\sqrt{D} = 4\\), dus \\(x = \\frac{6 \\pm 4}{2}\\): \\(x = 5\\) of \\(x = 1\\).", 4),
                 ("open", "Los op: \\(2x^{2} - 3x - 2 = 0\\).",
                  "\\(D = 9 + 16 = 25\\), \\(\\sqrt{D} = 5\\), \\(x = \\frac{3 \\pm 5}{4}\\): "
                  "\\(x = 2\\) of \\(x = -0{,}5\\).", 3),
             ]),
        dict(kop="Zonder de formule",
             opdracht="Los op door te ontbinden of door de wortel te trekken.",
             oefeningen=[
                 ("rij", [("\\(x^{2} = 36\\)", "\\(x = 6\\) of \\(x = -6\\)"),
                          ("\\(x^{2} - 9x = 0\\)", "\\(x = 0\\) of \\(x = 9\\)"),
                          ("\\(x^{2} + 4 = 0\\)", "geen reële oplossing")],
                  "Oplossing", WL),
                 ("open", "Waarom mag je bij \\(x^{2} = 9x\\) niet door \\(x\\) delen?",
                  "Omdat \\(x\\) nul kan zijn; je zou de oplossing \\(x = 0\\) kwijtspelen.", 2),
             ]),
        dict(kop="Som en product",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de som van de wortels", "\\(-\\frac{b}{a}\\)"),
                          ("het product van de wortels", "\\(\\frac{c}{a}\\)"),
                          ("\\(x^{2} - 7x + 10 = 0\\): som en product", "\\(7\\) en \\(10\\)"),
                          ("de wortels daarvan", "\\(2\\) en \\(5\\)")],
                  "Antwoord", WL),
             ]),
        dict(kop="Nog eens som en product",
             opdracht="Vul aan en stel zelf een vergelijking op.",
             oefeningen=[
                 ("rij", [("\\(x^{2} + 3x - 10 = 0\\): som en product", "\\(-3\\) en \\(-10\\)"),
                          ("de wortels daarvan", "\\(2\\) en \\(-5\\)")],
                  "Antwoord", WL),
                 ("open", "Stel een tweedegraadsvergelijking op met wortels \\(4\\) en \\(-1\\).",
                  "De som is \\(3\\) en het product \\(-4\\), dus \\(x^{2} - 3x - 4 = 0\\).", 3),
             ]),
        dict(kop="Twee vraagstukken",
             opdracht="Stel een vergelijking op, los ze op en toets je oplossingen.",
             oefeningen=[
                 ("open", "Een rechthoek heeft \\(A = 60\\) cm² en is \\(7\\) cm langer dan breed. Hoe "
                          "groot is ze?",
                  "\\(b(b + 7) = 60\\), dus \\(b^{2} + 7b - 60 = 0\\). \\(D = 49 + 240 = 289\\), "
                  "\\(\\sqrt{D} = 17\\), \\(b = \\frac{-7 + 17}{2} = 5\\). De rechthoek is \\(5\\) bij "
                  "\\(12\\) cm.", 5),
                 ("open", "Een steen valt van een toren. De hoogte is \\(h = 45 - 5t^{2}\\). Na hoeveel "
                          "seconden raakt hij de grond?",
                  "\\(45 - 5t^{2} = 0\\), dus \\(t^{2} = 9\\) en \\(t = 3\\) seconden; de negatieve "
                  "wortel heeft hier geen betekenis.", 4),
             ]),
    ])


# ============================================================
zet("het-functiebegrip-en-de-eerstegraadsfunctie",
    titel="Het functiebegrip en de eerstegraadsfunctie",
    reeksen=[
        dict(kop="Is het een functie?",
             opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("bij elke leerling hoort één geboortedatum", "ja"),
                          ("bij elke geboortedatum hoort één leerling", "nee, meerdere"),
                          ("\\(y = 3x - 1\\)", "ja"),
                          ("\\(x^{2} + y^{2} = 25\\)", "nee, twee \\(y\\) bij één \\(x\\)")],
                  "Functie of niet?", WW),
             ]),
        dict(kop="Nog drie verbanden",
             opdracht="Schrijf ja of nee, en zeg kort waarom.",
             oefeningen=[
                 ("rij", [("bij elk huisnummer hoort één straat", "ja"),
                          ("bij elke kleur hoort één leerling", "nee, meerdere"),
                          ("\\(y = \\sqrt{x}\\) met \\(x \\geq 0\\)", "ja")],
                  "Functie of niet?", WW),
             ]),
        dict(kop="Domein en bereik",
             opdracht="Schrijf je antwoord in een volle zin.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen het domein en het bereik?",
                  "Het domein is de verzameling van alle toegelaten \\(x\\)-waarden; het bereik is de "
                  "verzameling van alle \\(y\\)-waarden die er daadwerkelijk uitkomen.", 3),
                 ("open", "Geef het domein van \\(f(x) = \\frac{1}{x - 2}\\). Welke waarde valt weg, "
                          "en waarom?",
                  "Alle re\u00eble getallen behalve \\(2\\), dus \\(\\mathbb{R} \\setminus \\{2\\}\\). "
                  "Bij \\(x = 2\\) staat er \\(0\\) onder de breukstreep, en delen door \\(0\\) kan niet.", 3),
             ]),
        dict(kop="Beelden berekenen",
             opdracht="Bij \\(f(x) = -2x + 6\\).",
             oefeningen=[
                 ("rij", [("\\(f(0)\\)", "\\(6\\)"), ("\\(f(3)\\)", "\\(0\\)"),
                          ("\\(f(-1)\\)", "\\(8\\)"), ("\\(f(\\frac{1}{2})\\)", "\\(5\\)")],
                  "Antwoord", W),
                 ("open", "Voor welke \\(x\\) is \\(f(x) = 10\\)?",
                  "\\(-2x + 6 = 10\\) geeft \\(-2x = 4\\) en \\(x = -2\\).", 3),
             ]),
        dict(kop="Een tabel afwerken",
             opdracht="Bij \\(g(x) = 3x - 4\\).",
             oefeningen=[
                 ("tabel", ["\\(x\\)", "\\(-2\\)", "\\(0\\)", "\\(2\\)", "\\(4\\)"],
                  [["\\(g(x)\\)", None, None, None, None]],
                  "\\(-10\\), \\(-4\\), \\(2\\), \\(8\\)", W),
                 ("open", "Hoeveel stijgt \\(g(x)\\) telkens als \\(x\\) twee eenheden groter wordt? "
                          "Waar zie je dat getal in het voorschrift?",
                  "Zes eenheden, want \\(2 \\cdot 3 = 6\\). Het getal \\(3\\) is de "
                  "richtingscoëfficiënt \\(a\\).", 3),
             ]),
        dict(kop="Dezelfde functie lezen",
             opdracht="Bij \\(f(x) = -2x + 6\\).",
             oefeningen=[
                 ("rij", [("de richtingscoëfficiënt \\(a\\)", "\\(-2\\)"),
                          ("het snijpunt met de \\(y\\)-as", "\\((0, 6)\\)"),
                          ("de nulwaarde", "\\(x = 3\\)")],
                  "Antwoord", WW),
                 ("open", "Is \\(f\\) stijgend of dalend? Leg uit aan de hand van \\(a\\).",
                  "Dalend: \\(a = -2\\), dus negatief. Per eenheid naar rechts zakt de grafiek twee "
                  "eenheden.", 3),
             ]),
        dict(kop="Stijgend, dalend of constant",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Hoe verloopt de grafiek van \\(f(x) = 5 - \\frac{x}{4}\\)?",
                  ["stijgend", "dalend", "constant"], 1),
                 ("waar", "De grafiek van \\(f(x) = 7\\) is een horizontale rechte.", True),
                 ("waar", "Elke eerstegraadsfunctie heeft precies één nulwaarde.", True),
             ]),
        dict(kop="De grafiek tekenen",
             opdracht="Twee punten en een lat volstaan.",
             oefeningen=[
                 ("teken", "Teken de grafiek van \\(f(x) = -2x + 6\\) in een assenstelsel.",
                  "Een dalende rechte door \\((0, 6)\\) en \\((3, 0)\\).", 60),
             ]),
        dict(kop="Een voorschrift opstellen",
             opdracht="Schrijf het voorschrift op.",
             oefeningen=[
                 ("open", "Een rechte gaat door \\((0, 4)\\) en \\((2, 10)\\).",
                  "\\(a = \\frac{10 - 4}{2 - 0} = 3\\), dus \\(y = 3x + 4\\).", 3),
                 ("open", "Een rechte gaat door \\((1, 5)\\) en \\((4, -1)\\).",
                  "\\(a = \\frac{-1 - 5}{4 - 1} = -2\\). Invullen van \\((1, 5)\\): \\(5 = -2 + b\\), "
                  "dus \\(b = 7\\) en \\(y = -2x + 7\\).", 4),
             ]),
        dict(kop="Ligt het punt op de rechte?",
             opdracht="Vul de \\(x\\)-waarde in en vergelijk.",
             oefeningen=[
                 ("rij", [("\\((2, 9)\\) op \\(y = 4x + 1\\)", "ja"),
                          ("\\((-1, 3)\\) op \\(y = 4x + 1\\)", "nee, \\(-3\\)"),
                          ("\\((5, 0)\\) op \\(y = 2x - 10\\)", "ja")],
                  "Antwoord", WL),
             ]),
        dict(kop="Recht evenredig of niet?",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("\\(f(x) = 4x\\)", "recht evenredig"),
                          ("\\(f(x) = 4x + 1\\)", "niet, \\(b \\neq 0\\)"),
                          ("\\(f(x) = \\frac{4}{x}\\)", "omgekeerd evenredig")],
                  "Antwoord", WL),
                 ("waar", "De grafiek van \\(f(x) = ax\\) gaat door de oorsprong.", True),
             ]),
        dict(kop="Een kostfunctie",
             opdracht="Schrijf de functie op en reken uit.",
             oefeningen=[
                 ("open", "Een gsm-abonnement kost \\(15\\) euro per maand plus \\(0{,}10\\) euro per "
                          "sms. Schrijf de kostfunctie en bereken de kost bij \\(80\\) sms'en.",
                  "\\(k(x) = 15 + 0{,}10x\\). Bij \\(x = 80\\): \\(15 + 8 = 23\\) euro.", 3),
                 ("open", "Wat is bij die kostfunctie het domein, als je enkel hele sms'en kan sturen?",
                  "De natuurlijke getallen vanaf \\(0\\), dus \\(x \\in \\mathbb{N}\\). Een halve sms "
                  "of een negatief aantal bestaat niet.", 3),
             ]),
        dict(kop="Twee abonnementen vergelijken",
             opdracht="Stel een ongelijkheid op.",
             oefeningen=[
                 ("open", "Abonnement A kost \\(15 + 0{,}10x\\) en B kost \\(20 + 0{,}05x\\). Vanaf "
                          "hoeveel sms'en is B voordeliger?",
                  "\\(15 + 0{,}10x > 20 + 0{,}05x\\) geeft \\(0{,}05x > 5\\) en \\(x > 100\\). Vanaf "
                  "\\(101\\) sms'en is B goedkoper.", 4),
                 ("open", "Bij hoeveel sms'en kosten A en B precies hetzelfde, en hoeveel betaal je dan?",
                  "Bij \\(x = 100\\): beide kosten \\(25\\) euro. Dat is het snijpunt \\((100, 25)\\) "
                  "van de twee rechten.", 3),
                 ("open", "Je stuurt gemiddeld \\(60\\) sms'en per maand. Welk abonnement kies je, "
                          "en hoeveel scheelt dat op een jaar?",
                  "A kost \\(15 + 6 = 21\\) euro, B kost \\(20 + 3 = 23\\) euro. A is goedkoper, "
                  "en \\(2 \\cdot 12 = 24\\) euro per jaar.", 4),
             ]),
    ])


# ============================================================
zet("de-tweedegraadsfunctie-en-haar-parabool",
    titel="De tweedegraadsfunctie en haar parabool",
    reeksen=[
        dict(kop="De vorm van de parabool",
             opdracht="Vul aan voor \\(f(x) = ax^{2} + bx + c\\).",
             oefeningen=[
                 ("rij", [("\\(a > 0\\)", "dalparabool, opent naar boven"),
                          ("\\(a < 0\\)", "bergparabool, opent naar beneden"),
                          ("de \\(x\\) van de top", "\\(\\frac{-b}{2a}\\)"),
                          ("het snijpunt met de \\(y\\)-as", "\\((0, c)\\)")],
                  "Vul aan.", WL),
             ]),
        dict(kop="Wat de discriminant zegt",
             opdracht="Vul aan voor \\(f(x) = ax^{2} + bx + c\\).",
             oefeningen=[
                 ("rij", [("\\(D > 0\\)", "twee snijpunten met de \\(x\\)-as"),
                          ("\\(D = 0\\)", "\u00e9\u00e9n snijpunt, de top raakt de as"),
                          ("\\(D < 0\\)", "geen snijpunt met de \\(x\\)-as")],
                  "Vul aan.", WL),
             ]),
        dict(kop="Waarom de symmetrieas?",
             opdracht="Schrijf je antwoord in een volle zin.",
             oefeningen=[
                 ("open", "Waarom ligt de top altijd op de symmetrieas?",
                  "Ze is symmetrisch om de verticale rechte \\(x = \\frac{-b}{2a}\\), en de top is het "
                  "enige punt dat op die as ligt.", 3),
                 ("open", "Twee punten van een parabool hebben dezelfde \\(y\\)-waarde: "
                          "\\((1, 8)\\) en \\((7, 8)\\). Waar ligt de symmetrieas?",
                  "In het midden: \\(x = \\frac{1 + 7}{2} = 4\\). Twee punten op dezelfde hoogte "
                  "liggen spiegelgelijk rond de as.", 3),
             ]),
        dict(kop="Toppen en nulpunten",
             opdracht="Bereken de top en de nulpunten.",
             oefeningen=[
                 ("tabel", ["functie", "top", "nulpunten"],
                  [["\\(f(x) = x^{2} - 4x + 3\\)", None, None],
                   ["\\(f(x) = -x^{2} + 6x - 5\\)", None, None],
                   ["\\(f(x) = x^{2} + 2x + 5\\)", None, None],
                   ["\\(f(x) = x^{2} - 9\\)", None, None]],
                  "Top en nulpunten: \\((2, -1)\\) met \\(1\\) en \\(3\\) \u00b7 "
                  "\\((3, 4)\\) met \\(1\\) en \\(5\\) \u00b7 \\((-1, 4)\\) zonder "
                  "nulpunten \u00b7 \\((0, -9)\\) met \\(-3\\) en \\(3\\)", "150px"),
             ]),
        dict(kop="De parabool schetsen",
             opdracht="Zet de drie punten er eerst op, dan pas de kromme.",
             oefeningen=[
                 ("teken", "Schets de parabool van \\(f(x) = x^{2} - 4x + 3\\): zet de top, de "
                           "nulpunten en het snijpunt met de \\(y\\)-as erop.",
                  "Een dalparabool met top \\((2, -1)\\), nulpunten \\((1, 0)\\) en \\((3, 0)\\), en "
                  "\\((0, 3)\\) op de \\(y\\)-as.", 65),
             ]),
        dict(kop="Van topvorm naar top",
             opdracht="Lees de top af zonder te rekenen.",
             oefeningen=[
                 ("rij", [("\\(f(x) = (x - 4)^{2} + 1\\)", "\\((4, 1)\\)"),
                          ("\\(f(x) = (x + 1)^{2} - 2\\)", "\\((-1, -2)\\)"),
                          ("\\(f(x) = -2(x - 3)^{2}\\)", "\\((3, 0)\\)"),
                          ("\\(f(x) = x^{2} + 5\\)", "\\((0, 5)\\)")],
                  "De top", WW),
             ]),
        dict(kop="Van gewone vorm naar topvorm",
             opdracht="Bereken eerst de top, schrijf dan de topvorm op.",
             oefeningen=[
                 ("open", "Schrijf \\(f(x) = x^{2} - 6x + 11\\) in topvorm.",
                  "Top-\\(x\\): \\(\\frac{6}{2} = 3\\); \\(f(3) = 9 - 18 + 11 = 2\\). Dus "
                  "\\(f(x) = (x - 3)^{2} + 2\\).", 4),
                 ("open", "Schrijf \\(f(x) = x^{2} + 4x + 1\\) in topvorm.",
                  "Top-\\(x\\): \\(\\frac{-4}{2} = -2\\); \\(f(-2) = 4 - 8 + 1 = -3\\). Dus "
                  "\\(f(x) = (x + 2)^{2} - 3\\).", 4),
             ]),
        dict(kop="De verschuivingen herkennen",
             opdracht="Vertrek telkens van de basisparabool \\(y = x^{2}\\).",
             oefeningen=[
                 ("rij", [("\\(y = x^{2} - 5\\)", "\\(5\\) omlaag"),
                          ("\\(y = (x + 3)^{2}\\)", "\\(3\\) naar links"),
                          ("\\(y = -x^{2}\\)", "gespiegeld om de \\(x\\)-as"),
                          ("\\(y = 4x^{2}\\)", "smaller, steiler")],
                  "Wat verandert er?", WL),
                 ("waar", "De factor \\(a\\) verschuift de top van \\(y = ax^{2}\\).", False),
             ]),
        dict(kop="Opening en extremum",
             opdracht="Kruis aan of antwoord kort.",
             oefeningen=[
                 ("kies", "Welke functie heeft een maximum?",
                  ["\\(f(x) = 2x^{2} - 7\\)", "\\(f(x) = -3x^{2} + 1\\)",
                   "\\(f(x) = x^{2} + 4x\\)"], 1),
                 ("rij", [("\\(f(x) = x^{2} - 4x + 3\\)", "minimum \\(-1\\)"),
                          ("\\(f(x) = -x^{2} + 6x - 5\\)", "maximum \\(4\\)")],
                  "Minimum of maximum, en welke waarde?", WL),
             ]),
        dict(kop="Teken van de functie",
             opdracht="Bij \\(f(x) = x^{2} - 4x + 3\\).",
             oefeningen=[
                 ("open", "Voor welke \\(x\\) is \\(f(x) < 0\\)?",
                  "Tussen de nulpunten: voor \\(x \\in \\left]1, 3\\right[\\).", 2),
                 ("open", "Voor welke \\(x\\) is \\(f(x) > 0\\)?",
                  "Buiten de nulpunten: voor \\(x \\in \\left]-\\infty, 1\\right[ \\cup "
                  "\\left]3, +\\infty\\right[\\).", 2),
                 ("open", "Wat is de kleinste waarde die \\(f\\) kan aannemen, en bij welke \\(x\\)?",
                  "De \\(y\\)-waarde van de top: \\(-1\\), bij \\(x = 2\\).", 2),
             ]),
        dict(kop="Stijgen en dalen",
             opdracht="Antwoord met een interval.",
             oefeningen=[
                 ("open", "Waar daalt \\(f(x) = x^{2} - 4x + 3\\), en waar stijgt ze?",
                  "Dalend op \\(\\left]-\\infty, 2\\right]\\), stijgend op "
                  "\\(\\left[2, +\\infty\\right[\\).", 3),
                 ("waar", "Een parabool die naar onder opent, stijgt links van haar top.", True),
             ]),
        dict(kop="Een bal omhoog",
             opdracht="De hoogte in meter na \\(t\\) seconden is \\(h(t) = -5t^{2} + 20t\\).",
             oefeningen=[
                 ("open", "Na hoeveel seconden is de bal het hoogst, en hoe hoog komt hij?",
                  "De \\(t\\) van de top is \\(\\frac{-20}{2 \\cdot (-5)} = 2\\) seconden. "
                  "\\(h(2) = -20 + 40 = 20\\) meter.", 4),
                 ("open", "Wanneer raakt de bal weer de grond?",
                  "\\(-5t^{2} + 20t = 0\\) geeft \\(-5t(t - 4) = 0\\), dus \\(t = 0\\) of "
                  "\\(t = 4\\). Hij valt na \\(4\\) seconden.", 3),
             ]),
        dict(kop="De weide van de boer",
             opdracht="Werk uit met een tweedegraadsfunctie.",
             oefeningen=[
                 ("open", "Een boer heeft \\(40\\) meter draad voor een rechthoekige weide tegen een "
                          "muur, dus hij omheint maar drie zijden. Welke afmetingen geven de grootste "
                          "oppervlakte?",
                  "Noem de zijden loodrecht op de muur \\(x\\). De derde zijde is \\(40 - 2x\\) en "
                  "\\(A = x(40 - 2x) = -2x^{2} + 40x\\), met top bij \\(x = 10\\). Dus \\(10\\) "
                  "bij \\(20\\) meter, met \\(200\\) vierkante meter.", 6),
                 ("open", "Dezelfde boer zet nu een weide midden in de wei, dus met vier zijden "
                          "omheind. Welke afmetingen geven dan de grootste oppervlakte?",
                  "Nu is \\(2x + 2y = 40\\), dus \\(y = 20 - x\\) en "
                  "\\(A = x(20 - x) = -x^{2} + 20x\\). De top ligt bij \\(x = 10\\), dus een "
                  "vierkant van \\(10\\) bij \\(10\\) meter, met \\(100\\) vierkante meter.", 5),
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
