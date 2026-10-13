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
        dict(kop="Tellen met de productregel",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("\\(4\\) broeken en \\(6\\) hemden: aantal combinaties", "\\(24\\)"),
                          ("op hoeveel volgordes kan je \\(5\\) boeken zetten", "\\(120\\)"),
                          ("een code van \\(4\\) cijfers, cijfers mogen herhalen", "\\(10\\,000\\)"),
                          ("twee dobbelstenen gooien", "\\(36\\)"),
                          ("een munt en een dobbelsteen gooien", "\\(12\\)")],
                  "Hoeveel mogelijkheden?", WW),
             ]),
        dict(kop="Tellen zonder herhaling",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("een code van \\(4\\) verschillende cijfers", "\\(5\\,040\\)"),
                          ("hoeveel paren kan je kiezen uit \\(6\\) mensen", "\\(15\\)"),
                          ("hoeveel keuzes van \\(3\\) uit \\(5\\), volgorde telt mee", "\\(60\\)")],
                  "Hoeveel mogelijkheden?", WW),
             ]),
        dict(kop="Telt de volgorde mee?",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Reken na: hoeveel paren kan je kiezen uit \\(6\\) mensen? Toon de berekening.",
                  "\\(\\frac{6 \\cdot 5}{2} = 15\\). Je deelt door \\(2\\) omdat het paar "
                  "AB hetzelfde is als BA.", 3),
                 ("open", "Leg het verschil uit tussen een geval waarin de volgorde meetelt en een "
                          "waarin ze niet meetelt. Geef bij elk een voorbeeld.",
                  "Bij een podium met goud, zilver en brons telt de volgorde mee: ABC is iets anders "
                  "dan BAC. Bij het kiezen van drie klasgenoten voor een werkgroep telt ze niet mee: "
                  "dezelfde drie zijn dezelfde groep.", 4),
             ]),
        dict(kop="Som, product of complement?",
             opdracht="Noteer welke telregel je nodig hebt.",
             oefeningen=[
                 ("rij", [("eerst een voorgerecht, dan een hoofdgerecht kiezen", "productregel"),
                          ("een rode of een blauwe trui, niet allebei", "somregel"),
                          ("minstens \\(1\\) keer kop bij \\(3\\) munten", "complementregel")],
                  "Welke regel?", WL),
             ]),
        dict(kop="De complementregel gebruiken",
             opdracht="Toon je berekening.",
             oefeningen=[
                 ("open", "Bereken met de complementregel hoeveel van de \\(8\\) uitkomsten van drie "
                          "munten minstens \\(\u00e9\u00e9n\\) keer kop bevatten.",
                  "Alleen MMM bevat geen kop, dus \\(8 - 1 = 7\\) uitkomsten.", 3),
             ]),
        dict(kop="Een venndiagram invullen",
             opdracht="Werk met de formule \\(|A \\cup B| = |A| + |B| - |A \\cap B|\\).",
             oefeningen=[
                 ("open", "In een klas van \\(25\\) spelen er \\(14\\) voetbal, \\(11\\) "
                          "basket en \\(5\\) allebei. Hoeveel spelen er geen van beide?",
                  "\\(14 + 11 - 5 = 20\\) spelen er iets, dus \\(25 - 20 = 5\\) geen van beide.", 4),
             ]),
        dict(kop="Koffie of thee",
             opdracht="Werk met dezelfde formule.",
             oefeningen=[
                 ("open", "Van \\(40\\) mensen drinken er \\(28\\) koffie, \\(17\\) thee en "
                          "\\(9\\) allebei. Hoeveel drinken er enkel thee?",
                  "\\(17 - 9 = 8\\) drinken enkel thee.", 3),
             ]),
        dict(kop="Een boomdiagram tekenen",
             opdracht="Teken alle takken en tel de bladeren.",
             oefeningen=[
                 ("teken", "Teken het boomdiagram van twee keer een munt gooien en zet bij elk "
                           "blad de uitkomst.",
                  "Vier bladeren: KK, KM, MK, MM. Dat is \\(2 \\cdot 2 = 4\\).", 55),
             ]),
        dict(kop="Strategie herkennen",
             opdracht="Schrijf bij elke aanpak welke strategie je gebruikt.",
             oefeningen=[
                 ("rij", [("je noemt het onbekende aantal \\(x\\)", "variabelen invoeren"),
                          ("je maakt een schets van de situatie", "tekenen"),
                          ("je probeert eerst het geval met \\(2\\) in plaats van \\(100\\)",
                           "een eenvoudiger geval bekijken")],
                  "Welke strategie?", WL),
             ]),
        dict(kop="Nog drie strategie\u00ebn",
             opdracht="Schrijf bij elke aanpak welke strategie je gebruikt.",
             oefeningen=[
                 ("rij", [("je zet alles in een tabel", "systematisch opsommen"),
                          ("je werkt van het antwoord terug naar de vraag", "achterwaarts werken"),
                          ("je splitst de vraag in drie kleinere vragen",
                           "opsplitsen in deelproblemen")],
                  "Welke strategie?", WL),
                 ("waar", "Een vraagstuk heeft altijd maar \u00e9\u00e9n oplossingsweg.", False),
             ]),
        dict(kop="Terugwerken",
             opdracht="Draai elke stap om.",
             oefeningen=[
                 ("rij", [("ik tel er \\(7\\) bij en krijg \\(23\\)", "\\(16\\)"),
                          ("ik verdubbel en trek \\(4\\) af, en krijg \\(18\\)", "\\(11\\)"),
                          ("ik deel door \\(3\\) en tel er \\(5\\) bij, en krijg \\(11\\)",
                           "\\(18\\)"),
                          ("ik neem er \\(20\\,\\%\\) af en krijg \\(40\\)", "\\(50\\)")],
                  "Welk getal dacht ik?", WW),
             ]),
        dict(kop="Korting terugrekenen",
             opdracht="Toon je berekening.",
             oefeningen=[
                 ("open", "Een trui kost na \\(25\\,\\%\\) korting \\(45\\) euro. Wat was de "
                          "oude prijs?",
                  "\\(45\\) euro is \\(75\\,\\%\\) van de oude prijs, dus "
                  "\\(45 : 0{,}75 = 60\\) euro.", 3),
             ]),
        dict(kop="Schatten en controleren",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Een rekenmachine geeft \\(1\\,480\\) euro als prijs voor \\(4\\) "
                          "boeken. Waarom weet je meteen dat er een fout zit?",
                  "Een boek van bijna \\(370\\) euro is onmogelijk. Een schatting vooraf, "
                  "\\(4 \\cdot 20 = 80\\) euro, had dat meteen getoond.", 3),
                 ("waar", "Een negatieve leeftijd als uitkomst mag je gewoon laten staan.", False),
             ]),
        dict(kop="Wat controleer je?",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("waar", "Een antwoord zonder eenheid is af.", False),
                 ("open", "Noem twee vragen die je jezelf stelt bij het controleren van een antwoord.",
                  "Is dit een antwoord op de vraag? Klopt de grootteorde, en staat de eenheid erbij?", 3),
             ]),
        dict(kop="Twee denkpuzzels",
             opdracht="Los op met een systematische aanpak.",
             oefeningen=[
                 ("open", "Hoeveel keer schrijf je het cijfer \\(9\\) als je de getallen \\(1\\) "
                          "tot en met \\(100\\) opschrijft?",
                  "In de eenheden: \\(9, 19, 29, \\ldots, 99\\), dat zijn er \\(10\\). In de "
                  "tientallen: \\(90\\) tot en met \\(99\\), ook \\(10\\). Samen "
                  "\\(20\\).", 4),
                 ("open", "Een slak klimt overdag \\(3\\) meter omhoog in een put van \\(10\\) "
                          "meter en zakt 's nachts \\(2\\) meter terug. Na "
                          "hoeveel dagen is ze boven?",
                  "Elke volle dag wint ze \\(1\\) meter. Na \\(7\\) dagen staat ze op "
                  "\\(7\\) meter; op dag \\(8\\) klimt ze \\(3\\) meter en is ze op "
                  "\\(10\\) meter, dus boven. Antwoord: \\(8\\) dagen.", 4),
             ]),
    ])


# ============================================================
zet("gegevens-weergeven-en-samenvatten",
    titel="Gegevens weergeven en samenvatten",
    reeksen=[
        dict(kop="Een reeks samenvatten",
             opdracht="Werk met deze tien waarden: \\(12, 15, 15, 18, 20, 21, 24, 25, 25, 25\\).",
             oefeningen=[
                 ("rij", [("de som", "\\(200\\)"), ("het gemiddelde \\(\\bar{x}\\)", "\\(20\\)"),
                          ("de mediaan", "\\(20{,}5\\)"), ("de modus", "\\(25\\)"),
                          ("het bereik", "\\(13\\)"), ("het aantal waarden \\(n\\)", "\\(10\\)")],
                  "Wat is het resultaat?", W),
             ]),
        dict(kop="De mediaan van een even aantal",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit hoe je de mediaan van tien waarden bepaalt.",
                  "Het gemiddelde van de vijfde en de zesde: \\(\\frac{20 + 21}{2} = 20{,}5\\).", 3),
             ]),
        dict(kop="Gemiddelde naast mediaan",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Het gemiddelde is \\(20\\) en de mediaan \\(20{,}5\\). Wat zegt dat over "
                          "de verdeling?",
                  "Ze liggen dicht bij elkaar: de verdeling is vrij symmetrisch, zonder uitschieter.", 3),
             ]),
        dict(kop="Categorisch of numeriek?",
             opdracht="Schrijf bij elk gegeven welk soort het is.",
             oefeningen=[
                 ("rij", [("de lengte in centimeter", "numeriek"),
                          ("de haarkleur", "categorisch"),
                          ("het aantal broers en zussen", "numeriek"),
                          ("het vervoermiddel naar school", "categorisch")],
                  "Welk soort?", WL),
             ]),
        dict(kop="Relatieve frequentie",
             opdracht="Reken uit in procent.",
             oefeningen=[
                 ("rij", [("\\(20\\) van de \\(50\\)", "\\(40\\,\\%\\)"),
                          ("\\(9\\) van de \\(36\\)", "\\(25\\,\\%\\)"),
                          ("\\(14\\) van de \\(56\\)", "\\(25\\,\\%\\)")],
                  "Hoeveel procent?", WW),
             ]),
        dict(kop="Waarom in procent?",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom rekenen we relatieve frequenties uit in plaats van gewoon de "
                          "aantallen te vergelijken?",
                  "Zo leg je een klas van \\(20\\) naast een school van \\(600\\).", 3),
             ]),
        dict(kop="Klassen maken",
             opdracht="Toon je redenering.",
             oefeningen=[
                 ("open", "Hoeveel klassen van \\(10\\) cm heb je nodig voor lengtes van \\(150\\) "
                          "tot \\(190\\) cm? Schrijf ze allemaal op.",
                  "Vier, telkens \\(10\\) cm breed, van \\(\\left[150, 160\\right[\\) tot en met "
                  "\\(\\left[180, 190\\right[\\).", 3),
                 ("waar", "In een frequentietabel is de som van de frequenties gelijk aan \\(n\\).", True),
             ]),
        dict(kop="Wanneer welk kengetal?",
             opdracht="Schrijf op welk kengetal je kiest en waarom.",
             oefeningen=[
                 ("open", "De lonen in een bedrijf waar de directeur tien keer zoveel verdient als de rest.",
                  "De mediaan: dat ene hoge loon trekt het gemiddelde omhoog.", 3),
                 ("open", "De meest verkochte schoenmaat in een winkel.",
                  "De modus: je wil de maat die het vaakst voorkomt.", 2),
             ]),
        dict(kop="Nog twee keuzes",
             opdracht="Schrijf op welk kengetal je kiest en waarom.",
             oefeningen=[
                 ("open", "De gemiddelde temperatuur van een maand.",
                  "Het gemiddelde: alle waarden liggen dicht bij elkaar en elke dag telt even zwaar mee.", 2),
                 ("waar", "Een uitschieter verandert de mediaan meestal sterker dan het gemiddelde.", False),
                 ("waar", "De modus bestaat ook bij categorische gegevens.", True),
             ]),
        dict(kop="Spreiding berekenen",
             opdracht="Werk met dezelfde tien waarden als in reeks 1.",
             oefeningen=[
                 ("open", "Bereken \\(Q_{1}\\) en \\(Q_{3}\\), en de interkwartielafstand.",
                  "\\(Q_{1} = 15\\) (derde waarde), \\(Q_{3} = 25\\) (achtste), dus \\(10\\).", 3),
                 ("rij", [("de variatiebreedte", "\\(13\\)"),
                          ("de interkwartielafstand", "\\(10\\)")],
                  "Welke waarde?", W),
             ]),
        dict(kop="Twee klassen vergelijken",
             opdracht="Leg uit in volle zinnen.",
             oefeningen=[
                 ("open", "Twee klassen hebben allebei een gemiddelde van \\(60\\,\\%\\). Klas A "
                          "heeft een standaardafwijking van \\(4\\), klas B van \\(15\\). Wat "
                          "betekent dat?",
                  "In klas A liggen de punten dicht bij het gemiddelde, in klas B ver uiteen. Hetzelfde "
                  "gemiddelde zegt dus niets over de spreiding.", 4),
             ]),
        dict(kop="De boxplot",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Waarvoor dient een boxplot?",
                  "Hij toont het minimum, \\(Q_{1}\\), de mediaan, \\(Q_{3}\\) en het maximum in "
                  "één beeld, dus meteen de spreiding.", 3),
                 ("waar", "Op een boxplot zie je hoeveel gegevens erachter zitten.", False),
             ]),
        dict(kop="Grafieken kiezen",
             opdracht="Schrijf op welke grafiek past.",
             oefeningen=[
                 ("rij", [("het verloop van de temperatuur over een jaar", "een lijngrafiek"),
                          ("het aandeel van vier partijen in een parlement", "een cirkeldiagram"),
                          ("het aantal leerlingen per studierichting", "een staafdiagram")],
                  "Welke grafiek kies je?", WW),
             ]),
        dict(kop="Nog drie grafieken",
             opdracht="Schrijf op welke grafiek past.",
             oefeningen=[
                 ("rij", [("de spreiding van punten in twee klassen", "twee boxplots"),
                          ("het verband tussen lengte en gewicht", "een puntenwolk"),
                          ("hoe vaak elke score voorkomt", "een histogram")],
                  "Welke grafiek kies je?", WW),
                 ("waar", "Bij een histogram staan de staven los van elkaar.", False),
             ]),
        dict(kop="Een misleidende grafiek",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Een staafdiagram begint niet bij \\(0\\) maar bij \\(90\\). Waarom is dat "
                          "misleidend?",
                  "Je ziet alleen het topje van de staven, dus de verhouding ertussen klopt niet meer.", 3),
                 ("open", "Noem twee dingen waar je nog op let als je een diagram leest.",
                  "De eenheid, en hoeveel gegevens erachter zitten: \\(67\\,\\%\\) van drie is iets "
                  "anders dan van drieduizend.", 3),
                 ("open", "Een krant schrijft: de verkoop steeg van \\(98\\) naar \\(100\\) stuks, "
                          "en zet beide staven op een as die bij \\(97\\) begint. Hoeveel procent is de "
                          "echte stijging, en hoeveel keer zo hoog lijkt de tweede staaf?",
                  "Ongeveer \\(2\\,\\%\\); op die as lijkt ze drie keer zo hoog.", 4),
             ]),
    ])


# ============================================================
zet("verbanden-tussen-twee-grootheden",
    titel="Verbanden tussen twee grootheden",
    reeksen=[
        dict(kop="Welk verband?",
             opdracht="Schrijf op: recht evenredig, omgekeerd evenredig, lineair of geen van de drie.",
             oefeningen=[
                 ("rij", [("\\(y = 5x\\)", "recht evenredig"),
                          ("\\(y = 5x + 2\\)", "lineair"),
                          ("\\(y = \\frac{20}{x}\\)", "omgekeerd evenredig")],
                  "Welk verband?", WW),
             ]),
        dict(kop="Nog drie verbanden",
             opdracht="Schrijf op: recht evenredig, omgekeerd evenredig, lineair of geen van de drie.",
             oefeningen=[
                 ("rij", [("\\(y = x^{2}\\)", "geen van de drie"),
                          ("de prijs van benzine per liter", "recht evenredig"),
                          ("een taxi met opstapgeld", "lineair")],
                  "Welk verband?", WW),
                 ("open", "Wat is het verschil tussen recht evenredig en lineair?",
                  "Recht evenredig is een bijzonder geval van lineair: de grafiek gaat door de oorsprong, "
                  "dus \\(y = ax\\). Bij \\(y = ax + b\\) met \\(b \\neq 0\\) doet ze dat niet.", 3),
             ]),
        dict(kop="Een tabel aanvullen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["\\(x\\)", "\\(1\\)", "\\(2\\)", "\\(4\\)", "\\(5\\)", "\\(8\\)"],
                  [["\\(y\\) recht evenredig, \\(y = 3x\\)", None, None, None, None, None]],
                  "\\(3, 6, 12, 15, 24\\)", "55px"),
                 ("tabel", ["\\(x\\)", "\\(1\\)", "\\(2\\)", "\\(4\\)", "\\(5\\)", "\\(10\\)"],
                  [["\\(y\\) omgekeerd evenredig, \\(x \\cdot y = 20\\)", None, None, None, None, None]],
                  "\\(20, 10, 5, 4, 2\\)", "55px"),
             ]),
        dict(kop="Het voorschrift zoeken",
             opdracht="Toon je redenering.",
             oefeningen=[
                 ("open", "In een tabel staat: \\(x = 2\\) geeft \\(y = 7\\), \\(x = 4\\) geeft "
                          "\\(y = 13\\) en \\(x = 6\\) geeft \\(y = 19\\). Welk verband is dit? "
                          "Schrijf het voorschrift.",
                  "Lineair: per stap van \\(2\\) in \\(x\\) stijgt \\(y\\) met \\(6\\), dus "
                  "\\(a = 3\\). Invullen van \\((2, 7)\\): \\(7 = 6 + b\\), dus \\(b = 1\\) "
                  "en \\(y = 3x + 1\\).", 4),
             ]),
        dict(kop="Puntenwolk en samenhang",
             opdracht="Hoe noemen we dit?",
             oefeningen=[
                 ("rij", [("de punten lopen van linksonder naar rechtsboven", "positieve samenhang"),
                          ("de punten lopen van linksboven naar rechtsonder", "negatieve samenhang"),
                          ("de punten liggen willekeurig verspreid", "geen samenhang")],
                  "Hoe noemen we dit?", WW),
             ]),
        dict(kop="Nog drie begrippen",
             opdracht="Hoe noemen we dit?",
             oefeningen=[
                 ("rij", [("de punten liggen bijna op één rechte", "sterke samenhang"),
                          ("de rechte die het best door de wolk loopt", "de trendlijn"),
                          ("een punt dat ver van de wolk ligt", "een uitschieter")],
                  "Hoe noemen we dit?", WW),
             ]),
        dict(kop="De correlatieco\u00ebffici\u00ebnt lezen",
             opdracht="Schrijf op wat \\(r\\) je vertelt.",
             oefeningen=[
                 ("rij", [("\\(r = 0{,}95\\)", "sterk stijgend"),
                          ("\\(r = -0{,}8\\)", "sterk dalend"),
                          ("\\(r = 0{,}1\\)", "bijna geen verband"),
                          ("\\(r = -1\\)", "perfect dalend")],
                  "Wat zegt dit?", WL),
             ]),
        dict(kop="Teken en grootte",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("waar", "\\(r = -1\\) is zwakker dan \\(r = 0{,}5\\).", False),
                 ("waar", "\\(r\\) zegt enkel iets over een lineair verband.", True),
             ]),
        dict(kop="De grenzen van r",
             opdracht="Schrijf je antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Tussen welke twee waarden ligt \\(r\\) altijd, en wat betekent elk uiterste?",
                  "\\(-1 \\leq r \\leq 1\\). Bij \\(-1\\) liggen alle punten op een dalende "
                  "rechte, bij \\(1\\) op een stijgende.", 3),
             ]),
        dict(kop="IJsjes en verdrinkingen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "In een stad stijgt het aantal ijsjes én het aantal verdrinkingen in "
                          "dezelfde maanden. Mag je besluiten dat ijsjes gevaarlijk zijn?",
                  "Nee. Er is wel samenhang, maar geen oorzakelijk verband: de warmte is de derde factor "
                  "die allebei verklaart.", 3),
             ]),
        dict(kop="Waarom samenhang geen oorzaak is",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem twee redenen waarom een samenhang nog geen oorzaak is.",
                  "Er kan een derde factor zijn die beide be\u00efnvloedt, en de richting kan omgekeerd "
                  "zijn dan je denkt. Daarbij kan een verband ook toeval zijn.", 4),
             ]),
        dict(kop="Een oorzaak aantonen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Hoe toon je een oorzakelijk verband dan wel aan?",
                  "Met een opgezet experiment: je verandert \u00e9\u00e9n ding en houdt de rest gelijk.", 3),
             ]),
        dict(kop="Voorspellen met de trendlijn",
             opdracht="Werk uit.",
             oefeningen=[
                 ("open", "Een trendlijn door de wolk van lengte en schoenmaat heeft als vergelijking "
                          "\\(y = 0{,}26x - 3{,}5\\). Welke maat verwacht je bij \\(172\\) cm?",
                  "\\(0{,}26 \\cdot 172 - 3{,}5 = 44{,}72 - 3{,}5 \\approx 41\\).", 3),
                 ("open", "Waarom gebruik je diezelfde rechte beter niet voor iemand van \\(60\\) cm?",
                  "Dat ligt ver buiten de gemeten waarden; daar kan het verband heel anders lopen. De "
                  "rechte zou maat \\(12\\) voorspellen.", 3),
             ]),
        dict(kop="De drukker",
             opdracht="Werk uit.",
             oefeningen=[
                 ("open", "Een drukker rekent \\(25\\) euro opstartkost plus \\(0{,}40\\) euro per "
                          "affiche. Schrijf de formule en bereken de prijs voor \\(150\\) affiches.",
                  "\\(p(x) = 25 + 0{,}40x\\). Bij \\(x = 150\\): \\(25 + 60 = 85\\) euro.", 3),
                 ("open", "Bij welke oplage kost één affiche minder dan \\(0{,}60\\) euro, "
                          "alles meegerekend?",
                  "\\(\\frac{25 + 0{,}40x}{x} < 0{,}60\\) geeft \\(25 < 0{,}20x\\) en "
                  "\\(x > 125\\). Vanaf \\(126\\) affiches.", 4),
                 ("open", "Is de prijs per affiche recht evenredig met de oplage? Leg uit.",
                  "Nee. De totale prijs is lineair maar niet recht evenredig, want er staat "
                  "\\(25\\) euro opstartkost bij. De prijs per affiche daalt juist naarmate je er "
                  "meer drukt.", 4),
             ]),
    ])


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}


UITLEGBLADEN["oefenbundel-de-reele-getallen-wortels-en-machten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De verzamelingen zitten in elkaar: elk natuurlijk getal is ook geheel, elk geheel "
                    "getal is ook rationaal, en elk rationaal getal is ook reëel. Gevraagd wordt de "
                    "kleinste verzameling, dus de meest naar binnen gelegen die past.",
             waarom=[
                 "Reken een wortel altijd eerst uit: \\(\\sqrt{9}\\) is \\(3\\) en \\(\\sqrt[3]{8}\\) is "
                 "\\(2\\), dus zijn die natuurlijk. Een wortelteken maakt een getal dus niet automatisch "
                 "irrationaal.",
                 "De pijl staat verkeerd: \\(\\mathbb{Q} \\subset \\mathbb{R}\\). Elke breuk is een reëel "
                 "getal, maar niet elk reëel getal is een breuk.",
                 None,
                 "De sleutel is of je het getal als breuk van twee gehele getallen kan schrijven. Kan dat, "
                 "dan stopt of herhaalt de decimale uitbreiding; kan het niet, dan loopt ze oneindig "
                 "zonder patroon.",
             ]),
        dict(aanpak="Drie vormen van hetzelfde getal: breuk, kommagetal en procent. Van breuk naar komma "
                    "deel je teller door noemer, van komma naar procent maal honderd, van procent naar "
                    "komma gedeeld door honderd.",
             waarom=[
                 "Let op de laatste twee: \\(\\frac{2}{9} = 0{,}222\\ldots\\) herhaalt zich, en elke breuk "
                 "doet dat of stopt. \\(\\pi\\) herhaalt zich niet, en net dat maakt het irrationaal.",
                 "\\(18\\,\\%\\) van \\(350\\) is \\(0{,}18 \\cdot 350 = 63\\). Procent betekent per "
                 "honderd, dus vermenigvuldigen met het kommagetal is altijd de kortste weg.",
                 "Zet alles in dezelfde vorm voor je vergelijkt: \\(\\frac{2}{3} \\approx 0{,}667\\) en "
                 "\\(\\frac{3}{4} = 0{,}75\\). Breuken en kommagetallen door elkaar vergelijken op het "
                 "oog gaat bijna altijd mis.",
             ]),
        dict(aanpak="Drie rekenregels dekken bijna alles: bij vermenigvuldigen tel je de exponenten op, "
                    "bij delen trek je ze af, en bij een macht van een macht vermenigvuldig je ze. Een "
                    "negatieve exponent betekent één gedeeld door, en een exponent nul geeft altijd één.",
             waarom=[
                 "Bij \\(\\left(2a^{3}\\right)^{2}\\) moet je ook de \\(2\\) kwadrateren: dat geeft "
                 "\\(4a^{6}\\), niet \\(2a^{6}\\). Een exponent buiten de haakjes geldt voor alles "
                 "binnenin.",
                 "Let op het verschil tussen \\((-3)^{2} = 9\\) en \\(-3^{2} = -9\\), en op "
                 "\\(\\left(\\frac{1}{2}\\right)^{-1} = 2\\): een negatieve exponent zet de breuk om.",
             ]),
        dict(aanpak="De fouten bij machten zitten bijna altijd op dezelfde twee plaatsen: optellen "
                    "verwarren met vermenigvuldigen, en de haakjes niet goed lezen.",
             waarom=[
                 "\\(2^{3} + 2^{3}\\) is \\(8 + 8 = 16\\), en dat is \\(2^{4}\\), niet \\(2^{6}\\). "
                 "Optellen van machten mag je nooit met de rekenregels doen; die gelden enkel bij "
                 "vermenigvuldigen en delen.",
                 "Een geheugensteun: een kwadraat is nooit negatief, dus een negatief antwoord betekent "
                 "dat het minteken buiten de macht stond.",
             ]),
        dict(aanpak="Haal uit het getal onder de wortel het grootste volkomen kwadraat: "
                    "\\(\\sqrt{50} = \\sqrt{25 \\cdot 2} = 5\\sqrt{2}\\). Optellen mag enkel bij "
                    "gelijke wortels, net zoals bij gelijke termen met \\(x\\).",
             waarom=[
                 "\\(\\sqrt{12} + \\sqrt{27}\\) kan je pas optellen nadat je beide vereenvoudigd hebt tot "
                 "\\(2\\sqrt{3}\\) en \\(3\\sqrt{3}\\). En \\(3\\sqrt{5} - \\sqrt{5} = 2\\sqrt{5}\\), "
                 "precies zoals \\(3x - x = 2x\\).",
                 "Bij een derdemachtswortel mag het getal onder de wortel wel negatief zijn: "
                 "\\(\\sqrt[3]{-27} = -3\\), want \\((-3)^{3} = -27\\). Bij een vierkantswortel kan dat "
                 "niet.",
             ]),
        dict(aanpak="Schrijf bij een wortel altijd je ontbinding op. Dat kost één regel en haalt de meeste "
                    "fouten eruit, en op een examen staan daar punten op.",
             waarom=[
                 None,
                 "Dit heet de noemer rationaal maken: je vermenigvuldigt teller en noemer met "
                 "\\(\\sqrt{3}\\), zodat de wortel uit de noemer verdwijnt. De waarde van de breuk "
                 "verandert niet, want je deelt door \\(\\frac{\\sqrt{3}}{\\sqrt{3}} = 1\\).",
                 "Eén tegenvoorbeeld is genoeg om een bewering te weerleggen, en dat is een echt bewijs. "
                 "Dezelfde fout zit ook in \\(\\sqrt{a} \\cdot \\sqrt{b}\\) verwarren met "
                 "\\(\\sqrt{a + b}\\): vermenigvuldigen mag wel onder de wortel, optellen niet.",
             ]),
        dict(aanpak="In wetenschappelijke notatie staat er precies één cijfer voor de komma, en dat cijfer "
                    "is niet nul. De exponent zegt hoeveel plaatsen de komma opschuift: positief naar "
                    "rechts, negatief naar links.",
             waarom=[
                 "Bij vermenigvuldigen tel je de exponenten op en vermenigvuldig je de getallen vooraan; "
                 "bij delen het omgekeerde. \\(3 \\cdot 2 = 6\\) en \\(10^{4} \\cdot 10^{3} = 10^{7}\\).",
                 "Het getal vooraan moet tussen \\(1\\) en \\(10\\) liggen. Schuif je de komma één plaats "
                 "naar links, dan gaat de exponent één omhoog: \\(4{,}5 \\cdot 10^{4}\\).",
                 "Let op de laatste stap: \\(28{,}38\\) ligt niet tussen \\(1\\) en \\(10\\), dus moet de "
                 "komma nog één plaats opschuiven en de exponent van \\(12\\) naar \\(13\\).",
             ]),
        dict(aanpak="De drie eigenschappen in gewone taal: commutativiteit is van plaats wisselen, "
                    "associativiteit is anders groeperen, distributiviteit is het haakje uitwerken.",
             waarom=[
                 "Opgelet: aftrekken en delen zijn niet commutatief. \\(5 - 3\\) is niet \\(3 - 5\\), en "
                 "daarom mag je die twee niet van plaats wisselen.",
                 "Een voorbeeld maakt het concreet: rond je \\(\\frac{1}{3}\\) eerst af op \\(0{,}33\\) en "
                 "vermenigvuldig je daarna met \\(300\\), dan krijg je \\(99\\) in plaats van \\(100\\).",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-getallen-ordenen-afronden-en-intervallen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zet alles in dezelfde vorm voor je ordent: breuken naar kommagetallen, of alles "
                    "gelijknamig. Bij negatieve getallen ligt het getal met het grootste cijfer het verst "
                    "links, dus het kleinst.",
             waarom=[
                 "\\(\\frac{7}{10}\\) is precies \\(0{,}7\\), dus staat er een isgelijkteken en geen "
                 "kleiner dan. Gelijke getallen in twee vormen moet je ook als gelijk opschrijven.",
                 "Dit is de klassieke valkuil met negatieve getallen: \\(-3\\) is kleiner dan \\(-2{,}5\\), "
                 "al lijkt \\(3\\) groter dan \\(2{,}5\\). Op de getallenas ligt \\(-3\\) verder naar "
                 "links.",
                 "\\(\\sqrt{2} \\approx 1{,}4142\\), dus net iets groter dan \\(1{,}41\\) en kleiner dan "
                 "\\(1{,}5\\). En \\(\\frac{3}{2}\\) is precies \\(1{,}5\\).",
                 "Gelijknamig maken werkt altijd: \\(7 \\cdot 9 = 63\\) is de gemeenschappelijke noemer. "
                 "Een snellere truc is kruiselings vermenigvuldigen: \\(3 \\cdot 9 = 27\\) tegen "
                 "\\(4 \\cdot 7 = 28\\), dus is de tweede breuk groter.",
             ]),
        dict(aanpak="Lees het teken als een snavel die naar het kleinste getal wijst. Bij \\(\\leq\\) en "
                    "\\(\\geq\\) hoort de grens er wel bij, bij \\(<\\) en \\(>\\) niet.",
             waarom=[
                 "\\(\\frac{2}{3} = 0{,}666\\ldots\\) en dat is kleiner dan \\(0{,}67\\). En "
                 "\\(\\frac{7}{5} = 1{,}4\\) precies, dus daar staat een isgelijkteken.",
                 "\\(\\leq\\) betekent kleiner dan óf gelijk aan, en \\(3\\) is gelijk aan \\(3\\). Eén "
                 "van de twee voorwaarden is genoeg.",
                 "\\(x > 3\\) laat \\(3\\) net buiten; wil je \\(3\\) erbij, dan schrijf je "
                 "\\(x \\geq 3\\). Daar hangt verderop de open of gesloten haakjes van een interval aan "
                 "vast.",
             ]),
        dict(aanpak="Kijk naar het eerste cijfer dat wegvalt: is dat \\(5\\) of meer, dan rond je naar "
                    "boven af. Beduidende cijfers tel je vanaf het eerste cijfer dat niet nul is.",
             waarom=[
                 "Twee om op te letten: \\(149{,}95\\) op één decimaal geeft \\(150{,}0\\), en die nul laat "
                 "je staan, want ze toont je nauwkeurigheid. En \\(0{,}0996\\) op twee decimalen geeft "
                 "\\(0{,}10\\), niet \\(0{,}1\\).",
                 "\\(1\\,999\\) ligt dichter bij \\(2\\,000\\) dan bij \\(1\\,900\\). Afronden kan dus ook "
                 "het aantal cijfers doen toenemen.",
             ]),
        dict(aanpak="Afronden kost altijd iets. Bij een vraag naar waarom het niet klopt, reken je gewoon "
                    "terug: neem je afgeronde antwoord en kijk wat je ermee uitkomt.",
             waarom=[
                 "Winkels lossen dat op door naar boven af te ronden of door een stukprijs te vermijden. "
                 "Reken bij zulke vragen altijd je antwoord terug, dan zie je het verschil meteen.",
                 "Een voorbeeld: \\(\\frac{2}{3} \\cdot 3\\) is exact \\(2\\), maar met \\(0{,}67\\) "
                 "gerekend krijg je \\(2{,}01\\). Bij drie of vier stappen loopt dat snel op.",
             ]),
        dict(aanpak="Een vierkant haakje betekent dat de grens meedoet, een haakje naar buiten dat ze "
                    "wegvalt. Lees de tekst dus woord voor woord: tot en met is erbij, tot is niet erbij.",
             waarom=[
                 "Bij oneindig staat het haakje altijd naar buiten, want oneindig is geen getal dat erbij "
                 "kan horen. Alle reële getallen schrijf je als "
                 "\\(\\left]-\\infty, +\\infty\\right[\\).",
                 "Gesloten is beide grenzen erbij, open geen van beide, halfopen precies één van de twee. "
                 "De namen zeggen niets over de grootte van het interval.",
             ]),
        dict(aanpak="Teken de twee intervallen boven elkaar op een getallenas. De doorsnede is het stuk "
                    "waar beide lijnen liggen, de unie alles wat door minstens één van de twee gedekt is.",
             waarom=[
                 "Bij de linkergrens \\(4\\) neem je het strengste van de twee: het ene interval sluit "
                 "\\(4\\) uit, dus blijft hij uitgesloten. Bij de rechtergrens \\(6\\) doet alleen het "
                 "eerste interval mee, en dat neemt \\(6\\) wel mee.",
                 "Hier sluiten de twee precies op elkaar aan: \\(2\\) hoort bij het tweede interval, dus "
                 "ontbreekt er niets en krijg je alle reële getallen.",
                 "Hier is er geen enkel getal dat in beide zit: het eerste stopt vóór \\(5\\), het tweede "
                 "begint bij \\(5\\). De doorsnede is dan de lege verzameling.",
                 None,
             ]),
        dict(aanpak="Let bij een tekst op drie woordparen: vanaf en meer dan, tot en tot en met, minstens "
                    "en hoogstens. Het eerste van elk paar neemt de grens mee, het tweede niet, behalve "
                    "bij hoogstens, dat ook meeneemt.",
             waarom=[
                 "Vanaf \\(50\\) euro betekent dat \\(50\\) meedoet, meer dan \\(50\\) km/u betekent dat "
                 "\\(50\\) net niet meedoet. Dat ene woord bepaalt welk haakje je schrijft.",
                 "Minstens \\(1{,}20\\) neemt de grens mee, kleiner dan \\(1{,}80\\) niet. Een kind van "
                 "precies \\(1{,}80\\) mag dus niet mee, en dat is net wat de aanduiding aan de ingang "
                 "bedoelt.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-logica-bewerkingen-en-waarheidstabellen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vul telkens de waarden in en gebruik de regels: en is enkel waar als beide waar zijn, "
                    "of is waar zodra er één waar is, en een implicatie is enkel vals als het eerste deel "
                    "waar is en het tweede vals.",
             waarom=[
                 "Let op \\(q \\Rightarrow p\\): die is waar, want het eerste deel is vals. En "
                 "\\(\\neg p \\vee q\\) is vals, want \\(\\neg p\\) is vals en \\(q\\) ook.",
                 "Een beeld dat helpt: als ik zeg dat je een ijsje krijgt als je slaagt, en je slaagt niet, "
                 "dan heb ik mijn belofte niet gebroken, wat er ook gebeurt. Daarom is een implicatie met "
                 "een vals eerste deel waar.",
             ]),
        dict(aanpak="Vertaal woord voor woord. Niet wordt \\(\\neg\\), en wordt \\(\\wedge\\), of wordt "
                    "\\(\\vee\\), als dan wordt \\(\\Rightarrow\\), en dan en slechts dan als wordt "
                    "\\(\\Leftrightarrow\\).",
             waarom=[
                 "Het of van de wiskunde is inclusief: \\(p \\vee q\\) is ook waar als beide waar zijn. "
                 "Wil je het of van soep of dessert, dan heb je een andere bewerking nodig.",
                 "Elke uitspraak kan waar of vals zijn, dus verdubbelt het aantal rijen bij elke uitspraak "
                 "erbij: \\(2\\), \\(4\\), \\(8\\), \\(16\\). Met tien uitspraken zit je al aan "
                 "\\(1\\,024\\) rijen.",
             ]),
        dict(aanpak="Werk een tabel kolom per kolom af, niet rij per rij: eerst alle hulpkolommen, dan de "
                    "eindkolom. Dan hoef je per vakje maar aan één regel te denken.",
             waarom=[
                 "Zet de rijen altijd in dezelfde orde (WW, WV, VW, VV), dan kan je twee tabellen naast "
                 "elkaar vergelijken. Dat heb je bij de volgende reeks nodig.",
             ]),
        dict(aanpak="Dezelfde werkwijze, en let daarna op de eindkolom: twee uitdrukkingen met precies "
                    "dezelfde eindkolom zijn logisch gelijkwaardig.",
             waarom=[
                 None,
                 "Dat is een nuttige gelijkwaardigheid: een implicatie kan je altijd herschrijven als "
                 "\\(\\neg p \\vee q\\). In de informatica gebruikt men dat om voorwaarden te "
                 "vereenvoudigen.",
             ]),
        dict(aanpak="Kijk naar de eindkolom: alles waar is een tautologie, alles vals een contradictie, "
                    "en een mengeling geen van de twee.",
             waarom=[
                 "\\(p \\vee \\neg p\\) is altijd waar, want een uitspraak is waar of ze is het niet. "
                 "\\(p \\wedge \\neg p\\) is altijd vals, want beide tegelijk kan niet.",
                 "Dit verschil is groot: bewijzen vraagt alle rijen, weerleggen één rij. Daarom is een "
                 "tegenvoorbeeld zoveel makkelijker te vinden dan een bewijs.",
             ]),
        dict(aanpak="Drie vormen bij één implicatie: de omgekeerde wisselt de twee delen, de contrapositie "
                    "wisselt ze én ontkent beide. Enkel de contrapositie is altijd even waar als het "
                    "origineel.",
             waarom=[
                 "Let op: hier is enkel de orde gewisseld, zonder ontkenningen. Dat is de omgekeerde "
                 "implicatie, en die hoeft niet waar te zijn.",
                 "Bij de contrapositie draai je om én ontken je beide delen. Dat is precies dezelfde "
                 "uitspraak als het origineel, anders geformuleerd.",
                 "Die sproeiwagen is het tegenvoorbeeld. Dit is ook de fout achter veel foute "
                 "redeneringen in het echte leven: uit als A dan B besluiten dat uit B ook A volgt.",
             ]),
        dict(aanpak="Een ontkenning draait de kwantor om: de ontkenning van alle is er is minstens één die "
                    "niet, en de ontkenning van er bestaat is voor alle geldt niet.",
             waarom=[
                 "Let op: de ontkenning is niet dat geen enkele leerling een fiets heeft. Eén leerling "
                 "zonder fiets volstaat al om de uitspraak te weerleggen.",
                 "In dit geval is de ontkenning ook de ware uitspraak: een kwadraat is nooit negatief. De "
                 "oorspronkelijke uitspraak is dus vals.",
                 "Bij het ontkennen van \\(>\\) hoort \\(\\leq\\) en niet \\(<\\): niet groter dan nul "
                 "betekent kleiner dan óf gelijk aan nul.",
             ]),
        dict(aanpak="Een logische poort is de logica in een schakeling. Een en-poort hoort bij "
                    "\\(\\wedge\\), een of-poort bij \\(\\vee\\) en een niet-poort bij \\(\\neg\\).",
             waarom=[
                 "Een en-poort is in de praktijk twee schakelaars achter elkaar, een of-poort twee "
                 "schakelaars naast elkaar. Dat is precies de serie- en de parallelschakeling uit de "
                 "fysica.",
                 "De orde is belangrijk: \\((\\text{deur} \\wedge \\text{gewapend}) \\vee "
                 "\\text{paniekknop}\\). Zou je de haakjes anders zetten, dan zou het alarm ook afgaan "
                 "bij een open deur zonder dat het systeem gewapend is.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-redeneren-bewijzen-en-tegenvoorbeelden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek bij elke bewering het geval dat de regel breekt. Denk daarbij altijd aan de drie "
                    "verdachten: nul, één en de negatieve getallen. Daar sneuvelen de meeste beweringen.",
             waarom=[
                 "Let op \\(a > b\\) met \\(a = 1\\) en \\(b = -2\\): dan is \\(a^{2} = 1\\) en "
                 "\\(b^{2} = 4\\), dus klopt de bewering niet. En \\(2\\) is het enige even priemgetal, "
                 "dus het eeuwige tegenvoorbeeld bij uitspraken over priemgetallen.",
             ]),
        dict(aanpak="Dezelfde zoektocht naar de uitzondering. Vraag je telkens af: wat als het getal nul "
                    "is, negatief is, of kleiner dan één?",
             waarom=[
                 "Twee om te onthouden: \\(a^{2} > 0\\) faalt bij \\(a = 0\\), en delen door een getal "
                 "kleiner dan één maakt juist groter. \\(6 : \\frac{1}{2}\\) is hetzelfde als \\(6 \\cdot "
                 "2\\), dus \\(12\\).",
                 "Dat verschil is de kern van bewijzen: een bewering over alle gevallen kan je enkel "
                 "bewijzen met een redenering die voor elk geval geldt, en weerleggen met één enkel "
                 "geval. Daarom zijn tegenvoorbeelden zo waardevol.",
             ]),
        dict(aanpak="Een bewijs schrijf je in drie delen: je neemt een willekeurig geval met letters, je "
                    "rekent, en je besluit. Begin dus met neem en eindig met dus.",
             waarom=[
                 "Het essentiële woord is \\(2(a + b)\\): zodra je de \\(2\\) buiten de haakjes kan "
                 "halen, staat er een veelvoud van twee en ben je klaar. Dat is wat even betekent.",
                 "Hier bewijs je zonder te rekenen, met een eigenschap: van twee opeenvolgende getallen is "
                 "er altijd precies één even. Een kort bewijs is niet minder waard dan een lang bewijs.",
             ]),
        dict(aanpak="Werk de haakjes uit, term voor term, en neem daarna gelijke termen samen. Schrijf elke "
                    "tussenstap op: in een bewijs zijn de stappen het antwoord.",
             waarom=[
                 "De \\(2ab\\) ontstaat doordat \\(ab\\) en \\(ba\\) hetzelfde zijn en dus samengenomen "
                 "kunnen worden. Precies daar wordt de klassieke fout gemaakt: "
                 "\\((a + b)^{2}\\) is niet \\(a^{2} + b^{2}\\).",
             ]),
        dict(aanpak="Bij elke stap in een berekening hoort een eigenschap. Vraag je af: heb ik iets van "
                    "plaats gewisseld, anders gegroepeerd, een haakje uitgewerkt, of aan beide kanten van "
                    "het isgelijkteken hetzelfde gedaan?",
             waarom=[
                 "Distributiviteit werkt in twee richtingen: haakjes uitwerken en een gemeenschappelijke "
                 "factor buiten haakjes brengen. Hier is het de tweede richting.",
                 "\\(14\\), want vermenigvuldigen gaat voor optellen. Wie van links naar rechts rekent, "
                 "komt op \\(20\\) uit; de voorrang van de bewerkingen is dus ook een afspraak waar je "
                 "een stap op mag steunen.",
                 "Dat is het verschil tussen een voorbeeld en een bewijs. Letters staan voor elk getal, en "
                 "daarom draagt een berekening met letters het hele bewijs.",
             ]),
        dict(aanpak="Nodig betekent: zonder dit lukt het niet. Voldoende betekent: hiermee lukt het zeker. "
                    "Vraag je dus altijd twee dingen af, in beide richtingen.",
             waarom=[
                 "Deelbaar door \\(4\\) is voldoende om even te zijn, maar niet nodig: \\(6\\) is even en "
                 "niet deelbaar door \\(4\\). Een vierkant zijn is voldoende om een rechthoek te zijn, "
                 "maar niet nodig.",
                 "Daarom staat bij een equivalentie ook dan en slechts dan als. In een bewijs moet je zo'n "
                 "uitspraak dus in twee richtingen aantonen.",
             ]),
        dict(aanpak="Inductief gaat van voorbeelden naar een vermoeden, deductief van een regel naar een "
                    "geval. Vraag je af of de redenering naar boven veralgemeent of naar beneden toepast.",
             waarom=[
                 "Let op de derde: ook al klopt het resultaat (een driehoek heeft wel degelijk "
                 "\\(180^{\\circ}\\)), de redenering is inductief. Een juist besluit uit een zwakke "
                 "redenering blijft een zwakke redenering.",
             ]),
        dict(aanpak="Dezelfde gedachte als bij het tegenvoorbeeld, nu omgekeerd bekeken: hoeveel kloppende "
                    "gevallen je ook hebt, ze dekken nooit alle gevallen.",
             waarom=[
                 "Een mooi voorbeeld: \\(n^{2} + n + 41\\) geeft een priemgetal voor \\(n = 0\\) tot "
                 "\\(39\\), en loopt bij \\(n = 40\\) mis. Veertig kloppende gevallen zijn dus geen "
                 "bewijs.",
             ]),
        dict(aanpak="Bij een schaalfactor \\(k\\) gaat een lengte maal \\(k\\), een oppervlakte maal "
                    "\\(k^{2}\\) en een volume maal \\(k^{3}\\). Dat is de regel achter deze hele reeks.",
             waarom=[
                 "Zie de drie machten naast elkaar: omtrek is een lengte, dus \\(k\\); oppervlakte "
                 "\\(k^{2} = 9\\); volume \\(k^{3} = 8\\).",
                 "Reken de verhouding na: \\(600\\) gedeeld door \\(150\\) is \\(4\\), dus vier keer "
                 "zoveel inkt en niet twee keer. Daarom kost een foto op dubbel formaat ook flink meer "
                 "dan het dubbele.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-ruimtefiguren-vlakke-voorstellingen-en-vectoren-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Tel bij een ruimtefiguur telkens in dezelfde orde: hoekpunten, ribben, grensvlakken. "
                    "De formule van Euler is daarna je controle, want \\(h - r + g\\) moet altijd \\(2\\) "
                    "geven bij een figuur zonder gaten.",
             waarom=[
                 "Bij een prisma of een piramide kan je het tellen in plaats van onthouden: een vierzijdige "
                 "piramide heeft vier hoekpunten van het grondvlak plus de top, vier ribben onderaan plus "
                 "vier naar de top, en vier zijvlakken plus het grondvlak.",
                 "\\(8 - 12 + 6 = 2\\), dus de telling klopt. Gebruik die controle altijd: komt er geen "
                 "\\(2\\) uit, dan heb je iets dubbel of te weinig geteld.",
             ]),
        dict(aanpak="Twee rechten in de ruimte kunnen snijdend, evenwijdig of kruisend zijn. Kruisend "
                    "betekent dat ze in geen enkel vlak samen liggen, en dat kan enkel in de ruimte.",
             waarom=[
                 "De doorsnede zakt één dimensie: twee vlakken snijden in een rechte, twee rechten in een "
                 "punt. Dat helpt je om te controleren of je antwoord van de juiste soort is.",
                 "Twee vlakken snijden elkaar in een rechte of ze zijn evenwijdig; een derde mogelijkheid "
                 "is er niet. Kruisend bestaat enkel bij rechten.",
             ]),
        dict(aanpak="Hou de formules apart naar wat ze meten. Volume van een prisma of cilinder is "
                    "grondvlak maal hoogte; bij een kegel of piramide komt daar \\(\\frac{1}{3}\\) bij. "
                    "Oppervlakte van een bol is \\(4\\pi r^{2}\\), volume \\(\\frac{4}{3}\\pi r^{3}\\).",
             waarom=[
                 "Let op de kegel: \\(\\frac{1}{3} \\cdot \\pi \\cdot 25 \\cdot 12 = 100\\pi \\approx "
                 "314{,}2\\). Vergeet je die \\(\\frac{1}{3}\\), dan kom je op het drievoud uit, en dat "
                 "is de meest gemaakte fout in deze reeks. De kubus met ribbe \\(7\\) laat het verschil "
                 "tussen volume (\\(343\\)) en oppervlakte (\\(6 \\cdot 49 = 294\\)) mooi zien.",
             ]),
        dict(aanpak="Bij een vraagstuk over inhoud reken je eerst het volume in kubieke centimeter en zet "
                    "je dat daarna om: \\(1\\,000\\) cm³ is één liter, en \\(1\\) m³ is \\(1\\,000\\) "
                    "liter.",
             waarom=[
                 "Let op het begin: er staat een diameter van \\(60\\) cm, dus de straal is \\(30\\). Wie "
                 "met \\(60\\) rekent, komt op vier keer te veel uit, want de straal staat in het "
                 "kwadraat.",
                 "Een lengte maal twee geeft een volume maal acht, want er zijn drie richtingen die elk "
                 "verdubbelen. Daarom is een dubbel zo grote pot niet twee maar acht keer zo vol.",
             ]),
        dict(aanpak="Met vectoren reken je per coördinaat: optellen betekent de eerste bij de eerste en de "
                    "tweede bij de tweede. Een getal voor de vector vermenigvuldigt beide coördinaten.",
             waarom=[
                 "De lengte reken je met Pythagoras: \\(\\sqrt{3^{2} + (-2)^{2}} = \\sqrt{13}\\). Een "
                 "lengte is nooit negatief, ook al zijn de coördinaten dat wel.",
                 "Een vector plus zijn tegengestelde geeft altijd de nulvector. En een factor "
                 "\\(\\frac{1}{2}\\) halveert beide coördinaten; een negatieve factor draait de richting "
                 "om.",
             ]),
        dict(aanpak="Een verschuiving tel je gewoon bij de coördinaten van het punt op. Twee vectoren zijn "
                    "evenwijdig als je de ene met één getal uit de andere krijgt.",
             waarom=[
                 "\\((2 + (-4),\\ 1 + 3) = (-2, 4)\\). Let op het negatieve getal: naar links verschuiven "
                 "betekent aftrekken bij de eerste coördinaat.",
                 "Controleer het altijd met beide coördinaten: \\(-3 : 2 = -1{,}5\\) en \\(-9 : 6 = "
                 "-1{,}5\\). Komen de twee verhoudingen niet overeen, dan zijn ze niet evenwijdig.",
             ]),
        dict(aanpak="Een kracht en een snelheid zijn vectoren, dus je telt ze als vectoren op. Liggen ze "
                    "op één lijn, dan tel je op of trek je af; staan ze loodrecht, dan gebruik je "
                    "Pythagoras.",
             waarom=[
                 "Dat de som nul is, betekent niet dat er geen krachten werken. Er werken twee krachten en "
                 "ze heffen elkaar op, en net dat is evenwicht.",
                 "Reken na: \\(36 + 64 = 100\\), dus \\(10\\) km/u. Mooi om te zien dat de boot sneller "
                 "vaart dan hij zelf kan, maar niet in de richting waarin hij gericht staat.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-schaalverandering-en-gelijkvormige-figuren-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Bij schaal \\(1 : n\\) is één centimeter op papier \\(n\\) centimeter in het echt. "
                    "Reken dus eerst in centimeter en zet daarna om naar meter of kilometer.",
             waarom=[
                 "Reken de eerste na: \\(7 \\cdot 25\\,000 = 175\\,000\\) cm, en \\(175\\,000\\) cm is "
                 "\\(1\\,750\\) m, dus \\(1{,}75\\) km. Werk altijd in centimeter tot het einde.",
                 "Het is de breuk die je vergelijkt, niet het getal onderaan. Een grote schaal toont een "
                 "klein gebied met veel detail, een kleine schaal een groot gebied met weinig detail.",
             ]),
        dict(aanpak="De omgekeerde richting: nu deel je door de schaal. Van het echte formaat naar het plan "
                    "wordt het altijd kleiner, behalve bij een vergrotende schaal zoals \\(2 : 1\\).",
             waarom=[
                 "Let op de tweede: \\(2 : 1\\) is een vergroting, zoals bij een tekening van een insect "
                 "of een schroefje. Dan wordt de tekening juist groter dan het voorwerp.",
             ]),
        dict(aanpak="Eén regel voor deze hele bundel: bij schaalfactor \\(k\\) gaat een lengte maal "
                    "\\(k\\), een oppervlakte maal \\(k^{2}\\) en een volume maal \\(k^{3}\\).",
             waarom=[
                 "Let op de rij met \\(k = \\frac{1}{2}\\): verkleinen volgt dezelfde regel, dus het "
                 "volume wordt \\(\\frac{1}{8}\\). Een half zo grote maquette heeft dus acht keer minder "
                 "materiaal nodig.",
                 "Het volume gaat maal \\(2^{3} = 8\\). Alle drie de richtingen worden dubbel, en daarom "
                 "komt de factor drie keer voor.",
             ]),
        dict(aanpak="Zoek eerst \\(k\\), kijk daarna of de vraag over een lengte, een oppervlakte of een "
                    "volume gaat, en kies dan de juiste macht van \\(k\\).",
             waarom=[
                 "Let op de richting: van echt naar maquette verklein je, dus deel je door \\(50^{2}\\). "
                 "En zet \\(0{,}08\\) m² om naar \\(800\\) cm², want \\(1\\) m² is \\(10\\,000\\) cm².",
                 "Twee keer zo groot in alle richtingen, dus \\(0{,}5 \\cdot 8 = 4\\) liter. Een flesje dat "
                 "er dubbel zo groot uitziet, bevat dus acht keer zoveel.",
             ]),
        dict(aanpak="De vraag naar waarom is telkens dezelfde: hoeveel richtingen worden er groter? Eén "
                    "bij een lengte, twee bij een oppervlakte, drie bij een volume.",
             waarom=[
                 "Dezelfde vorm betekent dat ook de hoogte verdubbelt. Twee richtingen maal twee geeft "
                 "oppervlakte maal vier, en inkt volgt de oppervlakte.",
                 "\\(4^{3} = 64\\). Ook mooi om te zien hoe snel dat loopt: een figuur tien keer zo groot "
                 "heeft duizend keer zoveel inhoud.",
             ]),
        dict(aanpak="Zoek bij gelijkvormige driehoeken eerst \\(k\\) uit twee zijden die bij elkaar horen. "
                    "Daarna vermenigvuldig je elke andere zijde met diezelfde \\(k\\).",
             waarom=[
                 "\\(k = \\frac{\\left|DE\\right|}{\\left|AB\\right|} = \\frac{9}{6} = 1{,}5\\). Let op de "
                 "richting: van \\(ABC\\) naar \\(DEF\\) is het \\(1{,}5\\), de andere kant op "
                 "\\(\\frac{2}{3}\\).",
                 "\\(8 \\cdot 1{,}5 = 12\\). Let op welke zijde bij welke hoort: \\(BC\\) hoort bij "
                 "\\(EF\\), want de letters staan in dezelfde orde.",
                 "\\(10 \\cdot 1{,}5 = 15\\). Je kan het ook controleren met Pythagoras, want "
                 "\\(6, 8, 10\\) is een rechthoekige driehoek, en \\(9, 12, 15\\) dus ook.",
                 "\\(k^{2} = 1{,}5^{2} = 2{,}25\\). De oppervlakte gaat dus niet maal \\(1{,}5\\), al zijn "
                 "alle zijden maal \\(1{,}5\\) gegaan.",
             ]),
        dict(aanpak="Drie kenmerken, drie soorten gegevens: twee hoeken (HH), drie zijden in verhouding "
                    "(ZZZ), of twee zijden in verhouding met de hoek ertussen (ZHZ). Kijk dus eerst wat je "
                    "in de opgave gegeven hebt.",
             waarom=[
                 "Bij een schaduwmeting is het altijd HH: de zonnestralen vallen onder dezelfde hoek, en "
                 "stok en boom staan beide rechtop. Twee gelijke hoeken, dus gelijkvormig.",
             ]),
        dict(aanpak="De hoekensom van een driehoek is \\(180^{\\circ}\\). Daardoor volgt de derde hoek "
                    "altijd uit de twee andere, en daarom volstaan twee hoeken voor gelijkvormigheid.",
             waarom=[
                 "\\(180 - 40 - 60 = 80\\) graden.",
                 "Dat is ook waarom HH bestaat en niet HHH: de derde hoek voegt geen informatie toe. Het "
                 "kenmerk noemen is het bewijsstuk van je oplossing.",
             ]),
        dict(aanpak="Zet bij een gelijkvormigheidsvraagstuk de twee verhoudingen naast elkaar en let erop "
                    "dat je telkens dezelfde soort maat boven de streep zet: hoogte bij hoogte, schaduw "
                    "bij schaduw.",
             waarom=[
                 "Reken na: \\(\\frac{1{,}5}{2} = 0{,}75\\), en \\(12 \\cdot 0{,}75 = 9\\) m. Zo meet men "
                 "al duizenden jaren de hoogte van een boom of een toren, zonder te klimmen.",
                 "Die twee voorwaarden horen samen: gelijke hoeken zonder verhouding geeft geen "
                 "gelijkvormigheid bij een vierhoek, en een verhouding zonder gelijke hoeken ook niet. "
                 "Bij driehoeken volgt het ene wel uit het andere, en net daarom zijn driehoeken zo "
                 "handig.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-pythagoras-en-de-goniometrische-verhoudingen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De stelling van Pythagoras: \\(a^{2} + b^{2} = c^{2}\\), met \\(c\\) de schuine "
                    "zijde. Zoek je de schuine zijde, dan tel je de twee kwadraten op en neem je de "
                    "wortel.",
             waarom=[
                 "De eerste drie zijn bekende drietallen: \\(9, 12, 15\\) (het drievoud van \\(3, 4, 5\\)), "
                 "\\(7, 24, 25\\) en \\(8, 15, 17\\). Komt er bij jou geen mooi getal uit, zoals bij "
                 "\\(5\\) en \\(5\\), dan is dat geen fout: \\(\\sqrt{50} = 5\\sqrt{2}\\).",
             ]),
        dict(aanpak="Zoek je een rechthoekszijde, dan trek je af in plaats van op te tellen: "
                    "\\(a^{2} = c^{2} - b^{2}\\). Kijk dus altijd eerst welke van de drie de schuine zijde "
                    "is: dat is de langste, en ze ligt tegenover de rechte hoek.",
             waarom=[
                 "Ook hier bekende drietallen: \\(5, 12, 13\\), \\(6, 8, 10\\) en \\(10, 24, 26\\). "
                 "Controleer je antwoord altijd: de uitkomst moet kleiner zijn dan de schuine zijde.",
                 "De schuine zijde is altijd de langste, want ze ligt tegenover de grootste hoek. Komt er "
                 "bij jou iets anders uit, dan heb je de formule omgekeerd gebruikt.",
             ]),
        dict(aanpak="Met de omgekeerde stelling controleer je of een driehoek rechthoekig is: tel de "
                    "kwadraten van de twee kortste zijden op en vergelijk met het kwadraat van de langste.",
             waarom=[
                 "Belangrijk: je moet het kwadraat van de lángste zijde apart nemen. Vergelijk je de "
                 "verkeerde twee, dan kan een driehoek er rechthoekig uitzien terwijl hij het niet is.",
             ]),
        dict(aanpak="Dezelfde werkwijze. Reken beide kanten uit en zet er een conclusie bij: gelijk "
                    "betekent rechthoekig, niet gelijk betekent niet rechthoekig.",
             waarom=[
                 "\\(20, 21, 29\\) is minder bekend maar wel een echt Pythagorees drietal. Zeg er ook bij "
                 "wáár de rechte hoek zit: altijd tegenover de langste zijde.",
             ]),
        dict(aanpak="De afstandsformule is Pythagoras in een assenstelsel: het verschil in \\(x\\) en het "
                    "verschil in \\(y\\) zijn de rechthoekszijden.",
             waarom=[
                 "Let op de negatieve getallen bij de derde: \\(3 - (-1) = 4\\) en \\(-1 - 2 = -3\\), dus "
                 "\\(\\sqrt{16 + 9} = 5\\). Een verschil mag negatief zijn, want het kwadraat maakt het "
                 "toch positief.",
             ]),
        dict(aanpak="Een ruimtediagonaal reken je in twee stappen: eerst de diagonaal van het grondvlak, "
                    "en die gebruik je daarna als rechthoekszijde samen met de hoogte.",
             waarom=[
                 "Met de tussenstap van \\(5\\) komt er een mooi getal uit: \\(\\sqrt{25 + 144} = 13\\). "
                 "In één formule staat er \\(\\sqrt{3^{2} + 4^{2} + 12^{2}}\\), en dat is hetzelfde.",
                 "Bij een kubus met ribbe \\(a\\) is de ruimtediagonaal altijd \\(a\\sqrt{3}\\), want "
                 "\\(\\sqrt{a^{2} + a^{2} + a^{2}} = a\\sqrt{3}\\).",
             ]),
        dict(aanpak="Onthoud de drie verhoudingen met SOS CAS TOA: sinus is overstaand op schuin, cosinus "
                    "aanliggend op schuin, tangens overstaand op aanliggend. Overstaand en aanliggend zijn "
                    "altijd ten opzichte van de hoek die je bekijkt.",
             waarom=[
                 "Sinus en cosinus zijn nooit groter dan \\(1\\), want de schuine zijde is de langste. "
                 "Krijg je \\(\\sin \\alpha = 1{,}4\\), dan heb je de zijden verwisseld.",
                 "\\(\\sin 30^{\\circ} = \\cos 60^{\\circ} = 0{,}5\\), en dat is geen toeval: de twee "
                 "hoeken zijn samen \\(90^{\\circ}\\), dus is het overstaande van de ene het aanliggende "
                 "van de andere.",
             ]),
        dict(aanpak="Uit \\(\\sin^{2}\\alpha + \\cos^{2}\\alpha = 1\\) volgt de ene uit de andere: "
                    "\\(\\cos \\alpha = \\sqrt{1 - \\sin^{2}\\alpha}\\) voor een scherpe hoek.",
             waarom=[
                 "\\(1 - 0{,}64 = 0{,}36\\), en \\(\\sqrt{0{,}36} = 0{,}6\\). Je ziet hier de driehoek "
                 "\\(3, 4, 5\\) terug.",
                 "\\(1 - \\frac{25}{169} = \\frac{144}{169}\\), en de wortel daarvan is "
                 "\\(\\frac{12}{13}\\). Nu zie je de driehoek \\(5, 12, 13\\).",
             ]),
        dict(aanpak="Een formule onthouden is één ding, zien waar ze vandaan komt is beter. Vertrek hier "
                    "van Pythagoras en deel alles door \\(c^{2}\\).",
             waarom=[
                 "Daarom heet ze de grondformule: ze is Pythagoras in een andere jas. Dat verklaart ook "
                 "waarom er \\(1\\) rechts staat: \\(\\frac{c^{2}}{c^{2}} = 1\\).",
             ]),
        dict(aanpak="Zoek je een hoek, dan gebruik je de inverse toets: \\(\\arcsin\\), \\(\\arccos\\) of "
                    "\\(\\arctan\\) (op je rekentoestel \\(\\sin^{-1}\\) en zo). Kijk altijd of je "
                    "toestel in graden staat en niet in radialen.",
             waarom=[
                 "Je hebt de overstaande en de aanliggende zijde, dus is tangens het juiste getal. Staat "
                 "je toestel in radialen, dan krijg je \\(0{,}39\\) in plaats van \\(22{,}6^{\\circ}\\); "
                 "dat is de meest gemaakte fout hier.",
                 "Kleine controle: \\(0{,}6\\) ligt tussen \\(0{,}5\\) (dat is \\(30^{\\circ}\\)) en "
                 "\\(0{,}707\\) (dat is \\(45^{\\circ}\\)), dus moet de hoek tussen \\(30\\) en "
                 "\\(45\\) graden liggen.",
             ]),
        dict(aanpak="Schrijf eerst op welke zijden je kent en welke je zoekt, en kies dán het "
                    "goniometrische getal. Met de schuine zijde erbij is het sinus of cosinus, zonder de "
                    "schuine zijde is het tangens.",
             waarom=[
                 "De ladder is altijd de schuine zijde, want ze is de langste. Vraagt men de afstand van de "
                 "voet tot de muur, dan heb je cosinus nodig: \\(4 \\cdot \\cos 70^{\\circ} \\approx "
                 "1{,}37\\) m.",
                 "Let op het verschil: procent is de verhouding zelf, de hoek is de arctangens daarvan. "
                 "Daarom staat op een verkeersbord een percentage en geen graden; \\(8\\,\\%\\) is dus "
                 "geen \\(8\\) graden.",
             ]),
        dict(aanpak="Maak altijd eerst een schets met de gegevens erop. Bij een hoogtemeting hoort de "
                    "ooghoogte erbij, en dat is net het stuk dat men vergeet.",
             waarom=[
                 "Zet op je schets waar de rechte hoek zit en welke zijde je zoekt. Die ene tekening haalt "
                 "bij dit soort vraagstukken de meeste fouten eruit.",
                 "De berekening geeft de hoogte bóven je ogen, dus moet je de \\(1{,}6\\) m erbij tellen. "
                 "Wie dat vergeet, heeft een boom die anderhalve meter te klein is.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-formules-omvormen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Omvormen is de gezochte letter alleen zetten. Doe aan beide kanten hetzelfde en werk "
                    "van buiten naar binnen: eerst wat erbij of eraf staat, dan wat ermee vermenigvuldigd "
                    "of erdoor gedeeld wordt.",
             waarom=[
                 "Bij \\(P = 2(l + b)\\) deel je eerst door \\(2\\) en haal je daarna \\(b\\) weg. Werk je "
                 "eerst het haakje uit, dan kan het ook, maar het duurt langer.",
             ]),
        dict(aanpak="Staat de letter in het kwadraat, dan neem je als laatste de wortel; staat ze in een "
                    "breuk, dan vermenigvuldig je eerst met de noemer. De omgekeerde bewerking is altijd "
                    "je volgende stap.",
             waarom=[
                 "Bij \\(C = \\frac{5}{9}(F - 32)\\) vermenigvuldig je eerst met \\(\\frac{9}{5}\\) en zet "
                 "je daarna \\(32\\) over. Dat is de omgekeerde weg van de formule zelf, en de orde van "
                 "de stappen draait dus ook om.",
             ]),
        dict(aanpak="Schrijf elke tussenstap op één regel. Dat maakt het nakijken mogelijk, en op een "
                    "examen staan er punten op de stappen.",
             waarom=[
                 None,
                 "Hier staan drie dingen in de weg: de \\(\\frac{1}{3}\\), de \\(\\pi\\) en de "
                 "\\(r^{2}\\). Vermenigvuldig met \\(3\\) en deel daarna door \\(\\pi r^{2}\\); de orde "
                 "maakt hier niet uit, want het zijn alleen vermenigvuldigingen.",
             ]),
        dict(aanpak="Elke stap mag, op één voorwaarde na: je mag nooit delen door iets wat nul kan zijn. "
                    "Zet die voorwaarde erbij als het om een letter gaat.",
             waarom=[
                 "Daarom staat er bij zo'n omvorming vaak uitdrukkelijk \\(x \\neq 0\\). In de fysica is "
                 "dat niet alleen theorie: delen door een tijd van nul seconden betekent dat er geen tijd "
                 "verstreken is, en dan bestaat de snelheid niet.",
                 "Bij een gelíjkheid is er geen teken om te keren: \\(x = 3\\) wordt \\(-x = -3\\), en dat "
                 "is dezelfde uitspraak. Bij een ongelíjkheid keert het teken wél om: uit "
                 "\\(x > 3\\) volgt \\(-x < -3\\).",
             ]),
        dict(aanpak="Vul eerst in en reken daarna uit, niet omgekeerd. Schrijf de formule op, zet de "
                    "getallen erin en respecteer de voorrang van de bewerkingen.",
             waarom=[
                 "\\(\\frac{9 \\cdot 25}{5} = 45\\), en pas daarna komt \\(+32\\) erbij. Wie eerst "
                 "\\(25 + 32\\) doet, krijgt een heel ander antwoord.",
                 "Dit is de omgevormde formule uit reeks 2 in actie: \\(\\sqrt{\\frac{A}{\\pi}}\\). Dat er "
                 "een mooi getal uitkomt, is een teken dat je goed gerekend hebt.",
             ]),
        dict(aanpak="Zet bij een vraagstuk eerst de eenheden goed. Minuten moeten uren worden voor je deelt, "
                    "anders klopt de eenheid van je antwoord niet.",
             waarom=[
                 "\\(15\\) minuten is \\(0{,}25\\) uur, dus \\(1{,}25\\) uur. Wie met \\(1{,}15\\) rekent, "
                 "komt op \\(130{,}4\\) km/u uit, en dat is een klassieke fout met tijd.",
                 "Hier vul je in de formule in en los je op naar \\(b\\). Je mag ook eerst omvormen naar "
                 "\\(b = \\frac{P}{2} - l\\); beide wegen geven \\(9\\) cm.",
             ]),
        dict(aanpak="Deze vier formules komen uit de fysica, maar het omvormen is precies hetzelfde. Zoek "
                    "de letter die je wil en pas de omgekeerde bewerking toe.",
             waarom=[
                 "Een geheugensteun die altijd werkt: staat de gezochte letter onderaan in een breuk, dan "
                 "wisselt ze van plaats met het resultaat. Uit \\(\\rho = \\frac{m}{V}\\) volgt dus "
                 "\\(V = \\frac{m}{\\rho}\\), net zoals \\(t = \\frac{s}{v}\\) uit "
                 "\\(v = \\frac{s}{t}\\).",
             ]),
        dict(aanpak="Vul in met de juiste eenheden. Bij kilowattuur moet het vermogen in kilowatt staan en "
                    "de tijd in uren, niet in watt en seconden.",
             waarom=[
                 "Massadichtheid \\(1\\) kg per liter is handig om te onthouden: één liter water is één "
                 "kilogram, en één kubieke meter water is duizend kilogram.",
                 "\\(\\frac{230}{46} = 5\\) A. Dit is de wet van Ohm, omgevormd naar \\(I\\).",
                 "Let op de omzetting: \\(2\\,000\\) W is \\(2\\) kW en \\(30\\) minuten is \\(0{,}5\\) "
                 "uur. In joule zou hetzelfde antwoord \\(3\\,600\\,000\\) J zijn.",
             ]),
        dict(aanpak="Twee soorten verband, twee controles: bij recht evenredig blijft het quotiënt "
                    "\\(\\frac{y}{x}\\) gelijk, bij omgekeerd evenredig blijft het product "
                    "\\(x \\cdot y\\) gelijk.",
             waarom=[
                 "Die twee controles zijn het snelst bruikbaar bij een tabel: deel de twee rijen door "
                 "elkaar, en als dat niet constant is, vermenigvuldig ze. Blijft geen van de twee gelijk, "
                 "dan is het geen van beide verbanden.",
             ]),
        dict(aanpak="Vraag je af in welke macht de letter staat. Staat ze gewoon in de teller, dan volgt "
                    "\\(y\\) rechtstreeks; staat ze in de noemer, dan omgekeerd; staat ze in het kwadraat, "
                    "dan gaat het effect maal vier bij een verdubbeling.",
             waarom=[
                 "De derde is de belangrijkste in de praktijk: twee keer zo snel rijden geeft vier keer "
                 "zoveel bewegingsenergie, en dus ook een veel langere remweg. Daarom weegt snelheid in "
                 "het verkeer zo zwaar.",
                 "Dit is een omgekeerd evenredig verband: het product mens maal dagen blijft gelijk. Let "
                 "wel op dat dit in het echte leven niet oneindig doorgaat; met vierentwintig mensen is "
                 "de klus niet in één dag klaar als ze elkaar in de weg staan.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-eerstegraadsvergelijkingen-en-ongelijkheden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zet alles met \\(x\\) aan de ene kant en alle getallen aan de andere, en deel dan "
                    "door het getal voor \\(x\\). Haakjes werk je eerst uit, of je deelt er meteen door.",
             waarom=[
                 "Bij \\(4(x - 3) = 8\\) is delen door \\(4\\) de kortste weg: dan staat er "
                 "\\(x - 3 = 2\\). Controleer je antwoord altijd door het in te vullen; dat kost tien "
                 "seconden.",
             ]),
        dict(aanpak="Staat er aan beide kanten een \\(x\\), dan breng je ze eerst samen. Staat er een "
                    "breuk, dan vermenigvuldig je alles met de noemer.",
             waarom=[
                 "Bij \\(2(x + 1) = 3(x - 2)\\) werk je beide haakjes uit: \\(2x + 2 = 3x - 6\\), dus "
                 "\\(8 = x\\). Let op het minteken in \\(3(x - 2)\\): dat geeft \\(-6\\) en niet "
                 "\\(+6\\).",
             ]),
        dict(aanpak="Met breuken in de vergelijking vermenigvuldig je elke term met het kleinste "
                    "gemeenschappelijke veelvoud van de noemers. Dan zijn de breuken weg en los je verder "
                    "op zoals altijd.",
             waarom=[
                 "Vergeet de term zonder breuk niet: ook de \\(2\\) moet maal \\(6\\), en dat geeft "
                 "\\(12\\). Precies daar gaat het bij breukvergelijkingen bijna altijd mis.",
             ]),
        dict(aanpak="Komen alle \\(x\\)-en weg, dan zegt de overblijvende gelijkheid je het antwoord: "
                    "iets onwaars betekent geen oplossing, iets waars betekent elke oplossing.",
             waarom=[
                 "\\(0 = 5\\) is nooit waar, dus is er geen enkele \\(x\\) die past. Dat is geen "
                 "rekenfout, dat is het antwoord.",
                 "\\(0 = 0\\) is altijd waar, dus klopt elke \\(x\\). De twee leden waren eigenlijk "
                 "dezelfde uitdrukking, anders opgeschreven.",
             ]),
        dict(aanpak="Een ongelijkheid los je op als een vergelijking, met één extra regel: deel of "
                    "vermenigvuldig je met een negatief getal, dan keert het ongelijkheidsteken om.",
             waarom=[
                 "Bij \\(-3x \\geq 12\\) deel je door \\(-3\\) en wordt \\(\\geq\\) dus \\(\\leq\\): "
                 "\\(x \\leq -4\\). Let ook op het haakje in je interval: bij \\(\\leq\\) hoort een "
                 "vierkant haakje, want de grens doet mee.",
             ]),
        dict(aanpak="Dezelfde werkwijze. Zoek telkens of er ergens door een negatief getal gedeeld wordt, "
                    "want dan moet het teken om.",
             waarom=[
                 "Bij \\(5 - x \\leq 2\\) kan je \\(x\\) naar rechts brengen in plaats van door \\(-1\\) "
                 "te delen: \\(3 \\leq x\\), dus \\(x \\geq 3\\). Dat is vaak veiliger dan de omkeerregel "
                 "toepassen.",
             ]),
        dict(aanpak="De omkeerregel is geen afspraak maar een gevolg: op de getallenas liggen de getallen "
                    "na een vermenigvuldiging met een negatief getal in omgekeerde orde.",
             waarom=[
                 "Een voorbeeld maakt het zichtbaar: \\(2 < 5\\), maar \\(-2 > -5\\). Het omkeren gebeurt "
                 "dus niet omdat het zo hoort, maar omdat de orde echt omslaat.",
                 "Hier gebeurt er niets met de factor voor \\(x\\): je trekt alleen \\(7\\) af. Het teken "
                 "keert enkel om bij vermenigvuldigen of delen met een negatief getal, niet bij optellen "
                 "of aftrekken.",
             ]),
        dict(aanpak="Op de getallenas zegt het bolletje of de grens meedoet: vol bij \\(\\leq\\) en "
                    "\\(\\geq\\), open bij \\(<\\) en \\(>\\).",
             waarom=[
                 "Vol bolletje, want \\(-1\\) hoort bij de oplossing. Dat is hetzelfde als het vierkante "
                 "haakje in \\(\\left[-1, +\\infty\\right[\\).",
             ]),
        dict(aanpak="Dezelfde regel, nu met een open bolletje. De richting van de streep volgt het teken: "
                    "kleiner dan gaat naar links, groter dan naar rechts.",
             waarom=[None]),
        dict(aanpak="Zet bij een vraagstuk eerst op wat \\(x\\) is, in woorden. Daarna schrijf je de "
                    "vergelijking, los je op en antwoord je in een volle zin met de eenheid erbij.",
             waarom=[
                 "Het vaste bedrag staat los van \\(x\\), de prijs per kilometer gaat ermee maal. Daarom "
                 "is het \\(3{,}50 + 1{,}80x\\) en niet \\(5{,}30x\\).",
                 "Kies de kleinste onbekende als \\(x\\), hier de broer: dan staat er \\(3x\\) voor Lotte "
                 "en vermijd je breuken. Controleer achteraan altijd of de som echt \\(32\\) geeft.",
             ]),
        dict(aanpak="Hetzelfde recept. Let bij een vraag met vanaf of meer dan op dat je een ongelijkheid "
                    "opstelt en geen vergelijking.",
             waarom=[
                 "Zet eerst de breedte als \\(b\\) en de lengte als \\(b + 4\\), en gebruik dan de "
                 "omtrekformule. Controle: \\(2 \\cdot (7 + 11) = 36\\), dus het klopt.",
                 "Meer dan \\(20\\) euro geeft een ongelijkheid met \\(>\\), dus hoort \\(160\\) er net "
                 "niet bij. Bij precies \\(160\\) minuten betaal je exact \\(20\\) euro.",
             ]),
        dict(aanpak="Een rechte is positief boven de \\(x\\)-as en negatief eronder. Zoek dus eerst het "
                    "snijpunt met de \\(x\\)-as en kijk daarna naar welke kant de rechte stijgt of daalt.",
             waarom=[
                 "Stijgend betekent: rechts van het snijpunt ligt de rechte boven de as. Daarom is "
                 "\\(f(x) > 0\\) voor \\(x > -2\\).",
                 "Bij een dalende rechte is het omgekeerd: rechts van het snijpunt zakt ze onder de as. "
                 "Een schetsje van tien seconden voorkomt hier de helft van de fouten.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-stelsels-van-twee-vergelijkingen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Bij substitutie staat er in één vergelijking al een letter alleen. Vul die "
                    "uitdrukking in in de andere vergelijking, los op naar één letter en reken daarna de "
                    "tweede uit.",
             waarom=[
                 "Vul altijd in in de ándere vergelijking. Vul je in in dezelfde, dan krijg je "
                 "\\(0 = 0\\) en ben je niets wijzer.",
                 "Vergeet de tweede letter niet: een oplossing van een stelsel is een koppel, niet één "
                 "getal. Controleer het koppel in beide vergelijkingen.",
             ]),
        dict(aanpak="Bij de combinatiemethode tel je de twee vergelijkingen op of trek je ze van elkaar "
                    "af, zo dat één letter wegvalt. Zoek dus eerst welke letter dezelfde of de "
                    "tegengestelde coëfficiënt heeft.",
             waarom=[
                 "Hier staat \\(2x\\) in beide, dus valt \\(x\\) weg bij aftrekken. Let goed op de tekens: "
                 "\\(3y - (-y)\\) is \\(4y\\) en niet \\(2y\\).",
                 "Hier staan \\(+2y\\) en \\(-2y\\), dus valt \\(y\\) weg bij optellen. Een antwoord van "
                 "\\(0\\) voor \\(y\\) is geen fout: \\((4, 0)\\) is een gewoon koppel.",
             ]),
        dict(aanpak="Valt er niets weg, dan maak je het stelsel eerst klaar: vermenigvuldig een "
                    "vergelijking zo dat de coëfficiënten van één letter gelijk of tegengesteld worden.",
             waarom=[
                 "Vermenigvuldig altijd de hele vergelijking, dus ook het rechterlid: \\(1 \\cdot 2 = 2\\). "
                 "Dat vergeten is de meest gemaakte fout bij deze methode.",
             ]),
        dict(aanpak="Staat in beide vergelijkingen dezelfde letter alleen, dan stel je de rechterleden "
                    "gelijk. Dat is meteen één vergelijking met één onbekende.",
             waarom=[
                 "Vul je \\(x = 5\\) in, gebruik dan beide vergelijkingen als controle: "
                 "\\(4 \\cdot 5 - 3 = 17\\) en \\(2 \\cdot 5 + 7 = 17\\). Komen ze niet overeen, dan zit "
                 "er een rekenfout in.",
                 "Dat is ook wat je grafisch doet: je zoekt waar de twee rechten dezelfde \\(y\\) hebben, "
                 "en dat is hun snijpunt.",
             ]),
        dict(aanpak="Kijk naar de richtingscoëfficiënten: verschillend geeft één oplossing, gelijk met een "
                    "ander beginpunt geeft geen oplossing, en volledig dezelfde vergelijking geeft "
                    "oneindig veel.",
             waarom=[
                 "Bij de derde is \\(2y = 4x + 2\\) hetzelfde als \\(y = 2x + 1\\), gewoon maal twee. "
                 "Herschrijf dus altijd eerst naar dezelfde vorm voor je besluit.",
             ]),
        dict(aanpak="Dezelfde controle, nu met vergelijkingen die niet in de vorm \\(y = \\ldots\\) "
                    "staan. Vereenvoudig of herschrijf ze eerst.",
             waarom=[
                 "\\(3x + 3y = 9\\) is \\(x + y = 3\\) maal drie, dus zijn het dezelfde rechten. En "
                 "\\(x + y\\) kan niet tegelijk \\(5\\) en \\(7\\) zijn, dus daar is er geen oplossing.",
             ]),
        dict(aanpak="Elke uitkomst heeft een beeld: één snijpunt, geen snijpunt of twee rechten die "
                    "samenvallen. Teken bij twijfel de twee rechten ruw, dan zie je het meteen.",
             waarom=[
                 "Evenwijdig én niet samenvallend, dat zijn de twee voorwaarden. Evenwijdige rechten die "
                 "wél samenvallen geven juist oneindig veel oplossingen.",
                 None,
             ]),
        dict(aanpak="Drie woorden voor drie gevallen: bepaald is één oplossing, strijdig is geen "
                    "oplossing, onbepaald is oneindig veel.",
             waarom=[
                 "Dezelfde drie gevallen als bij één vergelijking met één onbekende, en dezelfde signalen: "
                 "\\(0 = 5\\) betekent strijdig, \\(0 = 0\\) betekent onbepaald.",
             ]),
        dict(aanpak="Zet bij een vraagstuk eerst in woorden wat je letters betekenen, met de eenheid erbij. "
                    "Daarna schrijf je per gegeven één vergelijking op.",
             waarom=[
                 "Twee gegevens geven twee vergelijkingen; met één vergelijking kan je dit vraagstuk niet "
                 "oplossen. Controleer je antwoord in beide: "
                 "\\(3 \\cdot 3 + 2 \\cdot 2 = 13\\) en \\(3 + 4 \\cdot 2 = 11\\).",
             ]),
        dict(aanpak="Bij een vraagstuk met aantallen en prijzen is er bijna altijd één vergelijking voor "
                    "het aantal en één voor het geld. Zoek die twee en je hebt je stelsel.",
             waarom=[
                 "Controleer het antwoord op de twee gegevens: \\(40 + 80 = 120\\) plaatsen en "
                 "\\(40 \\cdot 15 + 80 \\cdot 9 = 600 + 720 = 1\\,320\\) euro. Antwoord ook in een volle "
                 "zin: veertig vooraan en tachtig achteraan.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-tweedegraadsvergelijkingen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek eerst een merkwaardig product: een verschil van kwadraten of een volkomen "
                    "kwadraat. Lukt dat niet, zoek dan twee getallen met het product \\(c\\) en de som "
                    "\\(b\\).",
             waarom=[
                 "\\(x^{2} - 9\\) is een verschil van kwadraten, en \\(x^{2} + 6x + 9\\) een volkomen "
                 "kwadraat. Bij \\(x^{2} - 5x + 6\\) zoek je twee getallen met product \\(6\\) en som "
                 "\\(-5\\): dat zijn \\(-2\\) en \\(-3\\).",
                 "Een product is nul zodra één factor nul is, en dat is de hele truc van ontbinden. "
                 "Hier geeft dat \\(x = 3\\) of \\(x = 4\\).",
             ]),
        dict(aanpak="Zoek altijd eerst een gemeenschappelijke factor, voor je iets anders probeert. "
                    "Daarna kijk je naar een merkwaardig product of naar som en product.",
             waarom=[
                 "Bij \\(2x^{2} - 8x\\) haal je \\(2x\\) buiten haakjes; wie hier de discriminant "
                 "gebruikt, maakt het zichzelf veel moeilijker. Bij \\(x^{2} + 2x - 15\\) is het product "
                 "negatief, dus hebben de twee getallen een verschillend teken: \\(+5\\) en \\(-3\\).",
             ]),
        dict(aanpak="De discriminant is \\(D = b^{2} - 4ac\\). Positief geeft twee oplossingen, nul geeft "
                    "er één, negatief geen enkele. Let op de tekens van \\(b\\) en \\(c\\) bij het "
                    "invullen.",
             waarom=[
                 "Een negatieve \\(c\\) maakt \\(-4ac\\) positief, en dan is \\(D\\) altijd positief. Daar "
                 "kan je dus al aan zien dat er twee oplossingen zijn, nog voor je rekent.",
             ]),
        dict(aanpak="Dezelfde berekening. Schrijf telkens eerst \\(a\\), \\(b\\) en \\(c\\) op, dan is het "
                    "invullen nog maar een kleine stap.",
             waarom=[
                 "Bij een negatieve \\(D\\) is er geen reële oplossing, en dat is een volwaardig antwoord. "
                 "De wortel van een negatief getal bestaat niet in \\(\\mathbb{R}\\).",
             ]),
        dict(aanpak="De oplossingsformule is \\(x = \\frac{-b \\pm \\sqrt{D}}{2a}\\). Reken eerst "
                    "\\(D\\), dan \\(\\sqrt{D}\\), en vul pas daarna in. Zo blijft het overzichtelijk.",
             waarom=[
                 "Let op het teken van \\(-b\\): bij \\(b = -6\\) staat er \\(+6\\) in de teller. Daar "
                 "zitten de meeste fouten met deze formule.",
                 "Hier is \\(a = 2\\), dus staat er \\(2a = 4\\) in de noemer. Een oplossing zoals "
                 "\\(-0{,}5\\) of \\(-\\frac{1}{2}\\) is gewoon correct; het hoeven geen gehele getallen "
                 "te zijn.",
             ]),
        dict(aanpak="Staat er geen term met \\(x\\) alleen, dan hoef je de formule niet. Trek de wortel, of "
                    "haal \\(x\\) buiten haakjes: dat is sneller en minder foutgevoelig.",
             waarom=[
                 "Bij \\(x^{2} = 36\\) zijn er twee oplossingen, want ook \\((-6)^{2} = 36\\). Die "
                 "negatieve wortel vergeten is de klassieke fout. En \\(x^{2} + 4 = 0\\) zou "
                 "\\(x^{2} = -4\\) vragen, en dat kan niet.",
                 "Delen door \\(x\\) is delen door iets wat nul kan zijn, en dan verlies je een oplossing. "
                 "Haal in plaats daarvan \\(x\\) buiten haakjes: \\(x(x - 9) = 0\\) houdt beide "
                 "oplossingen.",
             ]),
        dict(aanpak="Som en product van de wortels: de som is \\(-\\frac{b}{a}\\), het product "
                    "\\(\\frac{c}{a}\\). Daarmee kan je wortels zoeken zonder formule, en je antwoord "
                    "altijd controleren.",
             waarom=[
                 "Controleer het bij \\(x^{2} - 7x + 10\\): \\(2 + 5 = 7\\) en \\(2 \\cdot 5 = 10\\). Die "
                 "controle kost vijf seconden en vindt bijna elke rekenfout.",
             ]),
        dict(aanpak="Dezelfde eigenschappen, nu ook omgekeerd gebruikt: ken je de wortels, dan ken je de "
                    "som en het product, en dus de vergelijking.",
             waarom=[
                 "Let op het teken: bij \\(b = +3\\) is de som \\(-3\\). Het minteken in "
                 "\\(-\\frac{b}{a}\\) wordt vaak vergeten.",
                 "Een vergelijking opstellen uit de wortels gaat met "
                 "\\(x^{2} - (\\text{som})x + (\\text{product}) = 0\\): "
                 "\\(x^{2} - 3x - 4 = 0\\). Elk veelvoud daarvan heeft dezelfde wortels.",
             ]),
        dict(aanpak="Bij een vraagstuk met een tweedegraadsvergelijking krijg je vaak twee wortels, maar "
                    "past er maar één in de werkelijkheid. Toets dus altijd je twee oplossingen aan de "
                    "context.",
             waarom=[
                 "De andere wortel is \\(-12\\), en een breedte van min twaalf centimeter bestaat niet. "
                 "Zeg dat er ook uitdrukkelijk bij: dat hoort bij het antwoord.",
                 "Dezelfde toets: \\(t = -3\\) zou betekenen dat de steen drie seconden vóór het "
                 "wegvallen al op de grond lag. Wiskundig is het een oplossing, in deze situatie niet.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-het-functiebegrip-en-de-eerstegraadsfunctie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Eén vraag beslist alles: hoort er bij elke \\(x\\) precies één \\(y\\)? Mag één "
                    "\\(x\\) twee verschillende uitkomsten hebben, dan is het geen functie.",
             waarom=[
                 "Let op de richting: bij elke leerling hoort één geboortedatum, maar bij één "
                 "geboortedatum kunnen meerdere leerlingen horen. Dezelfde gegevens geven dus wel en niet "
                 "een functie, afhankelijk van wat je als \\(x\\) neemt. En \\(x^{2} + y^{2} = 25\\) is "
                 "een cirkel: bij \\(x = 3\\) horen \\(y = 4\\) en \\(y = -4\\).",
             ]),
        dict(aanpak="Dezelfde test. Een handige controle bij een grafiek is de verticale lijn: snijdt een "
                    "verticale rechte de grafiek twee keer, dan is het geen functie.",
             waarom=[
                 "Bij \\(y = \\sqrt{x}\\) hoort per \\(x\\) maar één uitkomst, want de wortel is "
                 "afgesproken als het positieve getal. Daarom is dit wel een functie, al zijn er twee "
                 "getallen met kwadraat \\(x\\).",
             ]),
        dict(aanpak="Domein is wat erin mag, bereik is wat eruit komt. Zoek bij een domein altijd de twee "
                    "verboden: delen door nul en de wortel van een negatief getal.",
             waarom=[
                 "Een geheugensteun: het domein hoort bij de \\(x\\)-as, het bereik bij de \\(y\\)-as.",
                 "Los dus \\(x - 2 = 0\\) op om de verboden waarde te vinden. Bij een breuk met letters is "
                 "dat altijd de eerste stap.",
             ]),
        dict(aanpak="Een beeld berekenen is invullen: zet het getal in de plaats van \\(x\\) en reken uit. "
                    "Zoek je omgekeerd de \\(x\\) bij een gegeven beeld, dan los je een vergelijking op.",
             waarom=[
                 "Let op \\(f(-1)\\): \\(-2 \\cdot (-1) = +2\\), dus \\(f(-1) = 8\\). Twee mintekens "
                 "geven een plus.",
                 "Dit is de omgekeerde vraag: niet \\(f\\) van een getal, maar welk getal \\(10\\) als "
                 "beeld heeft. Zo'n vraag los je altijd op met een vergelijking.",
             ]),
        dict(aanpak="Werk een tabel rij per rij af en kijk daarna naar het patroon: bij een "
                    "eerstegraadsfunctie stijgt of daalt \\(y\\) met een vaste stap.",
             waarom=[
                 "Controleer het patroon: bij elke stap van \\(2\\) in \\(x\\) komt er \\(6\\) bij. Klopt "
                 "dat niet overal, dan zit er een rekenfout in je tabel.",
                 "Dat vaste stijgtempo ís de richtingscoëfficiënt. Daarom kan je \\(a\\) ook uit een tabel "
                 "halen: deel de stap in \\(y\\) door de stap in \\(x\\).",
             ]),
        dict(aanpak="Uit \\(f(x) = ax + b\\) lees je drie dingen af: \\(a\\) is de richtingscoëfficiënt, "
                    "\\(b\\) is de \\(y\\)-waarde in het snijpunt met de \\(y\\)-as, en de nulwaarde vind "
                    "je door \\(f(x) = 0\\) op te lossen.",
             waarom=[
                 "Let op het verschil tussen de nulwaarde (\\(x = 3\\), een getal op de \\(x\\)-as) en het "
                 "snijpunt met de \\(y\\)-as (\\((0, 6)\\), een punt). Die twee worden vaak verwisseld.",
                 "Het teken van \\(a\\) beslist: positief is stijgend, negatief is dalend, nul is "
                 "constant. De grootte van \\(a\\) zegt enkel hoe steil.",
             ]),
        dict(aanpak="Herschrijf de functie zo dat je \\(a\\) kan zien. \\(5 - \\frac{x}{4}\\) is "
                    "\\(-\\frac{1}{4}x + 5\\), dus is \\(a\\) negatief.",
             waarom=[
                 "De \\(x\\) staat achteraan met een minteken, dus is \\(a = -\\frac{1}{4}\\): dalend, en "
                 "wel traag. Dat de \\(5\\) vooraan staat, verandert daar niets aan.",
                 "Bij \\(f(x) = 7\\) is \\(a = 0\\): de functie stijgt noch daalt. Zo'n constante functie "
                 "heeft ook geen nulwaarde, tenzij ze zelf nul is.",
                 "Een eerstegraadsfunctie met \\(a \\neq 0\\) snijdt de \\(x\\)-as precies één keer, want "
                 "een niet-horizontale rechte kruist de as altijd en nooit twee keer.",
             ]),
        dict(aanpak="Voor een rechte heb je twee punten nodig, en de makkelijkste zijn het snijpunt met de "
                    "\\(y\\)-as en de nulwaarde. Zet ze erop en trek de lijn door.",
             waarom=[
                 "Controleer met een derde punt of je lijn klopt, bijvoorbeeld \\((1, 4)\\). Eén "
                 "rekenfoutje in een van de twee punten zet je hele rechte schuin.",
             ]),
        dict(aanpak="Zoek eerst \\(a\\) met \\(a = \\frac{y_{2} - y_{1}}{x_{2} - x_{1}}\\), vul daarna een "
                    "van de twee punten in om \\(b\\) te vinden.",
             waarom=[
                 "Gaat de rechte door een punt op de \\(y\\)-as, dan ken je \\(b\\) meteen: hier is "
                 "\\(b = 4\\). Dat scheelt een stap.",
                 "Let op de mintekens in de breuk: \\(\\frac{-1 - 5}{4 - 1} = \\frac{-6}{3} = -2\\). "
                 "Controleer daarna met het andere punt: "
                 "\\(-2 \\cdot 4 + 7 = -1\\), dus het klopt.",
             ]),
        dict(aanpak="Vul de \\(x\\)-waarde van het punt in het voorschrift in en vergelijk met de "
                    "\\(y\\)-waarde. Komt er iets anders uit, dan ligt het punt niet op de rechte.",
             waarom=[
                 "Bij \\((-1, 3)\\) geeft het voorschrift \\(-3\\) en niet \\(3\\). Zet er dan ook bij wat "
                 "het wél moest zijn, dat hoort bij het antwoord.",
             ]),
        dict(aanpak="Recht evenredig is strenger dan eerstegraads: er mag geen constante bijkomen. In "
                    "\\(f(x) = ax\\) moet \\(b\\) dus nul zijn.",
             waarom=[
                 "\\(\\frac{4}{x}\\) is zelfs geen eerstegraadsfunctie: de \\(x\\) staat in de noemer, en "
                 "dat geeft een omgekeerd evenredig verband met een hyperbool als grafiek.",
                 "Dat is de grafische test voor recht evenredig: de rechte moet door \\((0, 0)\\) gaan. "
                 "Bij \\(x = 0\\) is immers \\(y = 0\\).",
             ]),
        dict(aanpak="Zet in een kostfunctie het vaste bedrag als \\(b\\) en de prijs per stuk als \\(a\\). "
                    "Zo staat het vraagstuk meteen in de vorm \\(ax + b\\).",
             waarom=[
                 "Let op de eenheden: \\(0{,}10\\) euro per sms, dus \\(80\\) sms'en kosten \\(8\\) euro "
                 "en niet \\(80\\) cent per stuk gerekend als \\(0{,}80\\).",
                 "Een mooi voorbeeld van een domein dat uit de werkelijkheid komt in plaats van uit de "
                 "formule: rekenkundig mag \\(x = 2{,}5\\), maar in de praktijk niet.",
             ]),
        dict(aanpak="Twee tarieven vergelijken is twee functies vergelijken. Stel ze gelijk voor het "
                    "omslagpunt en gebruik een ongelijkheid voor de vraag vanaf wanneer.",
             waarom=[
                 "Let op het antwoord in hele sms'en: \\(x > 100\\) betekent dat B pas vanaf \\(101\\) "
                 "echt goedkoper is. Bij precies \\(100\\) is het gelijk.",
                 "Dat snijpunt is het omslagpunt van je vraagstuk. Grafisch zie je het als het punt waar de "
                 "twee rechten elkaar kruisen; links daarvan is A goedkoper, rechts B.",
                 "Hier staat het nut van die vergelijking: \\(60\\) ligt onder \\(100\\), dus A. Reken het "
                 "verschil ook op een jaar, want daar wordt zo'n keuze pas zichtbaar.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-de-tweedegraadsfunctie-en-haar-parabool-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vier gegevens uit één voorschrift: het teken van \\(a\\) geeft de opening, "
                    "\\(\\frac{-b}{2a}\\) geeft de \\(x\\) van de top, \\(c\\) geeft het snijpunt met de "
                    "\\(y\\)-as, en de discriminant zegt hoeveel nulpunten er zijn.",
             waarom=[
                 "Een geheugensteun voor de opening: een blije mond \\((a > 0)\\) opent naar boven en heeft "
                 "een minimum, een trieste mond \\((a < 0)\\) opent naar beneden en heeft een maximum.",
             ]),
        dict(aanpak="De discriminant zegt hier hoeveel keer de parabool de \\(x\\)-as raakt of snijdt, en "
                    "dat zijn precies de oplossingen van \\(f(x) = 0\\).",
             waarom=[
                 "\\(D < 0\\) betekent niet dat de parabool niet bestaat: ze ligt gewoon volledig boven of "
                 "volledig onder de \\(x\\)-as. Welke van de twee, zegt het teken van \\(a\\).",
             ]),
        dict(aanpak="Een parabool is symmetrisch om een verticale rechte door de top. Daarom liggen twee "
                    "punten met dezelfde \\(y\\)-waarde altijd even ver aan weerszijden van die as.",
             waarom=[
                 "Dat verklaart ook de formule: het midden van de twee nulpunten is "
                 "\\(\\frac{-b}{2a}\\), want de twee nulpunten liggen op "
                 "\\(\\frac{-b \\pm \\sqrt{D}}{2a}\\), symmetrisch rond dat midden.",
                 "Hiermee kan je de top vinden zonder de formule, als je twee punten op dezelfde hoogte "
                 "kent. Dat werkt ook met de twee nulpunten: het midden daarvan is de top-\\(x\\).",
             ]),
        dict(aanpak="Werk in vaste orde: eerst de top-\\(x\\) met \\(\\frac{-b}{2a}\\), dan de top-\\(y\\) "
                    "door die \\(x\\) in te vullen, dan de nulpunten met de discriminant of door te "
                    "ontbinden.",
             waarom=[
                 "De rij zonder nulpunten is geen vergissing: de top ligt daar boven de \\(x\\)-as bij een "
                 "dalparabool, dus raakt ze de as nooit. Reken de top-\\(y\\) altijd uit met het "
                 "voorschrift en niet met een formule uit het hoofd.",
             ]),
        dict(aanpak="Schets met drie soorten punten: de top, de nulpunten en het snijpunt met de "
                    "\\(y\\)-as. Spiegel dat laatste punt over de symmetrieas, dan heb je er gratis een "
                    "vierde.",
             waarom=[
                 "Het spiegelpunt van \\((0, 3)\\) is hier \\((4, 3)\\), want de symmetrieas ligt op "
                 "\\(x = 2\\). Met vier punten wordt je kromme meteen veel netter.",
             ]),
        dict(aanpak="In de topvorm \\(f(x) = a(x - p)^{2} + q\\) is de top \\((p, q)\\). Let op het teken: "
                    "er staat min \\(p\\) in de formule, dus \\((x + 1)^{2}\\) geeft \\(p = -1\\).",
             waarom=[
                 "Dat tekenverschil is de hele valkuil van deze reeks: \\((x + 1)^{2} - 2\\) heeft top "
                 "\\((-1, -2)\\) en niet \\((1, -2)\\). De \\(a\\) ervoor verandert de top niet, enkel de "
                 "opening en de steilte.",
             ]),
        dict(aanpak="Van gewone vorm naar topvorm: bereken de top, en vul die in in "
                    "\\(a(x - p)^{2} + q\\). Je hoeft dus niet te kwadraatafsplitsen als je de top al kan "
                    "berekenen.",
             waarom=[
                 "Controleer je topvorm door hem uit te werken: \\((x - 3)^{2} + 2 = x^{2} - 6x + 9 + 2\\), "
                 "en dat is het oorspronkelijke voorschrift.",
                 "Let op het teken in de haakjes: de top ligt op \\(x = -2\\), dus staat er "
                 "\\((x + 2)^{2}\\). Een negatieve top-\\(x\\) geeft een plus in de haakjes.",
             ]),
        dict(aanpak="Vergelijk elk voorschrift met \\(y = x^{2}\\). Een getal buiten de haakjes verschuift "
                    "verticaal, een getal binnen de haakjes horizontaal, een minteken spiegelt, en een "
                    "factor maakt smaller of breder.",
             waarom=[
                 "De horizontale verschuiving gaat tegen je gevoel in: \\((x + 3)^{2}\\) schuift naar "
                 "links en niet naar rechts. Reken het na met één punt, dan zie je het.",
                 "De factor \\(a\\) verandert enkel de steilte en de opening; de top van \\(y = ax^{2}\\) "
                 "blijft in de oorsprong. Verschuiven doen \\(p\\) en \\(q\\).",
             ]),
        dict(aanpak="Een dalparabool heeft een minimum, een bergparabool een maximum, en die waarde is "
                    "altijd de \\(y\\)-waarde van de top. Kijk dus eerst naar het teken van \\(a\\).",
             waarom=[
                 "Alleen bij \\(a < 0\\) is er een maximum. De twee andere opties hebben een positieve "
                 "\\(a\\) en dus een minimum, hoe groot de rest van het voorschrift ook is.",
                 "Zeg bij zo'n antwoord altijd twee dingen: of het een minimum of een maximum is, en welke "
                 "waarde het heeft. De bijhorende \\(x\\) is de top-\\(x\\).",
             ]),
        dict(aanpak="Het teken van een parabool lees je af van haar grafiek: bij een dalparabool is ze "
                    "negatief tussen de nulpunten en positief erbuiten. Schets dus eerst ruw.",
             waarom=[
                 "Tussen de nulpunten duikt een dalparabool onder de as. Let op de open haakjes: in de "
                 "nulpunten zelf is \\(f(x)\\) precies nul en dus niet kleiner dan nul.",
                 "Buiten de nulpunten bestaat uit twee stukken, en die verbind je met een unieteken. Eén "
                 "interval zou hier niet kloppen.",
                 "De kleinste waarde van een dalparabool is altijd de top-\\(y\\). Zeg er ook bij bij "
                 "welke \\(x\\) dat gebeurt, want dat is wat men in een vraagstuk nodig heeft.",
             ]),
        dict(aanpak="Een parabool keert om in haar top: links daarvan gaat ze één kant op, rechts de "
                    "andere. Bij een dalparabool eerst dalen, dan stijgen; bij een bergparabool omgekeerd.",
             waarom=[
                 "De top-\\(x\\) is de grens tussen de twee intervallen. Je mag hem in beide intervallen "
                 "meenemen, want in de top zelf stijgt of daalt de functie niet.",
                 "Een bergparabool stijgt links van haar top tot ze haar maximum haalt en daalt daarna. "
                 "Precies omgekeerd aan een dalparabool.",
             ]),
        dict(aanpak="Bij een worp is de top het hoogste punt en zijn de nulpunten de momenten op "
                    "grondhoogte. Vertaal de vraag dus eerst naar top of nulpunt.",
             waarom=[
                 "Let op het dubbele minteken in \\(\\frac{-20}{2 \\cdot (-5)}\\): dat geeft \\(+2\\). "
                 "Antwoord in beide eenheden: twee seconden na de worp, op twintig meter hoogte.",
                 "Hier hoef je de discriminant niet: haal \\(t\\) buiten haakjes. De oplossing \\(t = 0\\) "
                 "is het moment van de worp zelf, dus is \\(t = 4\\) het antwoord op de vraag.",
             ]),
        dict(aanpak="Bij een optimalisatievraagstuk schrijf je de oppervlakte als functie van één letter, "
                    "en dan is de top je antwoord. Begin dus met de omtrekvoorwaarde in één letter om te "
                    "zetten.",
             waarom=[
                 "Let op dat er maar drie zijden omheind worden: tweemaal \\(x\\) plus de zijde "
                 "\\(40 - 2x\\). Daarom is de beste vorm hier geen vierkant maar een rechthoek die twee "
                 "keer zo breed is als diep, en haal je \\(200\\) m² uit dezelfde veertig meter draad.",
                 "Met vier zijden is het vierkant wel de beste vorm, en de oppervlakte zakt naar de helft. "
                 "Die vergelijking is net het mooie van deze twee oefeningen: dezelfde draad, de dubbele "
                 "weide, enkel omdat de muur een zijde gratis geeft.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-telproblemen-en-problemen-oplossen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De productregel: moet je achter elkaar kiezen, dan vermenigvuldig je de aantallen. "
                    "Vraag je telkens af hoeveel keuzes je bij elke stap hebt.",
             waarom=[
                 "Let op het verschil: bij \\(5\\) boeken in een rij heb je \\(5 \\cdot 4 \\cdot 3 \\cdot "
                 "2 \\cdot 1 = 120\\) mogelijkheden, want een boek dat al staat kan je niet nog eens "
                 "kiezen. Bij een code van \\(4\\) cijfers die mogen herhalen is het "
                 "\\(10 \\cdot 10 \\cdot 10 \\cdot 10\\), en de nul telt mee als cijfer.",
             ]),
        dict(aanpak="Zonder herhaling zakt het aantal keuzes bij elke stap met één. Telt de volgorde niet "
                    "mee, dan deel je daarna nog door het aantal manieren waarop je dezelfde keuze kan "
                    "ordenen.",
             waarom=[
                 "\\(10 \\cdot 9 \\cdot 8 \\cdot 7 = 5\\,040\\) voor de code, \\(5 \\cdot 4 \\cdot 3 = "
                 "60\\) als de volgorde meetelt, en \\(\\frac{6 \\cdot 5}{2} = 15\\) voor de paren, want "
                 "daar telt ze niet mee.",
             ]),
        dict(aanpak="Vraag je bij elk telprobleem eerst af of de volgorde meetelt. Dat ene antwoord beslist "
                    "of je deelt of niet, en het is de meest gemaakte fout bij tellen.",
             waarom=[
                 "Je deelt door \\(2\\) omdat elk paar twee keer geteld wordt. Bij groepjes van drie zou "
                 "je door \\(3 \\cdot 2 \\cdot 1 = 6\\) delen.",
                 "Een geheugensteun: bij een podium, een code of een rij telt de volgorde mee; bij een "
                 "groep, een team of een handvol kaarten niet.",
             ]),
        dict(aanpak="Drie regels, drie signalen: en wijst op vermenigvuldigen, of op optellen, en minstens "
                    "op de complementregel, waarbij je het tegendeel aftrekt van het totaal.",
             waarom=[
                 "Let op het woord minstens: dat zijn vaak veel gevallen, en het tegendeel (geen enkele) "
                 "is er meestal maar één. Dan is aftrekken veel korter dan optellen.",
             ]),
        dict(aanpak="Bij de complementregel reken je het tegendeel uit en trek je dat van het totaal af. "
                    "Zoek dus eerst het totaal aantal mogelijkheden.",
             waarom=[
                 "Het totaal is \\(2^{3} = 8\\), want elke munt heeft twee uitkomsten. Alleen MMM heeft "
                 "geen kop, dus blijven er \\(7\\) over. Alle gevallen één per één optellen zou hier "
                 "zeven berekeningen vragen.",
             ]),
        dict(aanpak="Bij twee overlappende groepen gebruik je \\(|A \\cup B| = |A| + |B| - |A \\cap B|\\): "
                    "wie bij beide hoort, is twee keer geteld en moet er één keer af.",
             waarom=[
                 "Let op de laatste stap: de vraag is hoeveel er geen van beide spelen, dus moet je nog "
                 "van het klastotaal aftrekken. Een venndiagram met drie vakjes maakt dat meteen zichtbaar.",
             ]),
        dict(aanpak="Dezelfde formule, nu met een andere vraag. Enkel thee betekent thee min de overlap, "
                    "niet het totaal aantal theedrinkers.",
             waarom=[
                 "Lees het woordje enkel goed: \\(17\\) drinken thee, maar \\(9\\) daarvan drinken ook "
                 "koffie. Een venndiagram voorkomt deze fout.",
             ]),
        dict(aanpak="Een boomdiagram tekent elke keuze als een splitsing. Het aantal bladeren is het "
                    "antwoord, en dat moet hetzelfde zijn als wat de productregel geeft.",
             waarom=[
                 "Zo zie je waarom de productregel werkt: twee takken, en uit elke tak weer twee. Bij drie "
                 "munten zouden er acht bladeren zijn.",
             ]),
        dict(aanpak="Bij elke strategie hoort een handeling. Vraag je af wat je concreet dóét: iets "
                    "benoemen, iets tekenen, iets vereenvoudigen of iets opsommen.",
             waarom=[
                 "Een eenvoudiger geval bekijken is de krachtigste van de drie: zie je het patroon bij "
                 "\\(2\\) en \\(3\\), dan ken je het vaak ook bij \\(100\\).",
             ]),
        dict(aanpak="Dezelfde vraag, met drie andere strategieën. Je mag ze ook combineren; dat is net wat "
                    "een goede probleemoplosser doet.",
             waarom=[
                 "Systematisch opsommen is traag maar betrouwbaar, en het geeft je vaak het patroon dat je "
                 "daarna sneller laat werken.",
                 "Bijna elk vraagstuk kan op meerdere manieren. Jouw weg mag anders zijn dan die van je "
                 "buur; wat moet kloppen, is de redenering.",
             ]),
        dict(aanpak="Terugwerken is elke bewerking in omgekeerde orde ongedaan maken: optellen wordt "
                    "aftrekken, verdubbelen wordt halveren. Begin bij het resultaat en werk naar het "
                    "begin.",
             waarom=[
                 "Let op de laatste: \\(20\\,\\%\\) eraf betekent dat er \\(80\\,\\%\\) overblijft, dus "
                 "\\(40 : 0{,}8 = 50\\). Wie \\(20\\,\\%\\) bij \\(40\\) optelt, komt op \\(48\\) uit, en "
                 "dat is fout.",
             ]),
        dict(aanpak="Bij een korting terugrekenen vraag je je af welk percentage je nog betaalt, en daarmee "
                    "deel je. Nooit het kortingspercentage bij de nieuwe prijs optellen.",
             waarom=[
                 "Controleer het altijd vooruit: \\(25\\,\\%\\) van \\(60\\) is \\(15\\), en "
                 "\\(60 - 15 = 45\\). Dat is de snelste manier om te zien of je antwoord klopt.",
             ]),
        dict(aanpak="Schat eerst, reken daarna. Een schatting met ronde getallen kost vijf seconden en "
                    "haalt de grote fouten eruit, ook die van je rekenmachine.",
             waarom=[
                 "Een onmogelijke uitkomst betekent meestal een verkeerde toets: hier is er vermoedelijk "
                 "vermenigvuldigd in plaats van gedeeld.",
                 "Een negatieve leeftijd, een negatieve lengte of een halve bus betekent dat je antwoord "
                 "wiskundig wel kan maar in deze situatie niet past. Zeg dat er dan ook bij.",
             ]),
        dict(aanpak="Een antwoord is pas af als het de gestelde vraag beantwoordt, een eenheid heeft en "
                    "een plausibele grootte.",
             waarom=[
                 "Zonder eenheid is \\(45\\) niets: euro, centimeter of seconden. Op een examen kost dat "
                 "punten, en in de praktijk is het gewoon onbruikbaar.",
                 "Een derde vraag die altijd helpt: heb ik geantwoord op wat er gevraagd werd? Veel punten "
                 "gaan verloren aan een correcte berekening van iets anders dan wat er stond.",
             ]),
        dict(aanpak="Bij een puzzel helpt systematisch opsommen of een eenvoudiger geval. Let bij de laatste "
                    "stap op: dat is waar zulke puzzels hun strik leggen.",
             waarom=[
                 "Let op \\(99\\): daar staat de \\(9\\) twee keer, één keer als eenheid en één keer als "
                 "tiental. Door in twee groepen te tellen, de eenheden en de tientallen, komt dat "
                 "automatisch goed uit.",
                 "Hier is de strik de laatste dag: op dag \\(8\\) is ze boven en zakt ze niet meer terug. "
                 "Wie \\(10\\) door \\(1\\) deelt, komt op \\(10\\) dagen uit en vergeet dat de laatste "
                 "klim de put uit gaat.",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-gegevens-weergeven-en-samenvatten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zet de waarden altijd eerst in stijgende orde, dan liggen mediaan en kwartielen voor "
                    "het grijpen. Gemiddelde is som gedeeld door aantal, mediaan is de middelste, modus is "
                    "de meest voorkomende, bereik is hoogste min laagste.",
             waarom=[
                 "Bij tien waarden is er geen enkele middelste, dus neem je het gemiddelde van de vijfde "
                 "en de zesde: \\(\\frac{20 + 21}{2} = 20{,}5\\). Het bereik is \\(25 - 12 = 13\\).",
             ]),
        dict(aanpak="Bij een even aantal waarden liggen er twee in het midden. Hun gemiddelde is de "
                    "mediaan, ook als dat getal zelf niet in de reeks voorkomt.",
             waarom=[
                 "Reken de plaats uit en niet op het zicht: bij \\(n = 10\\) zijn dat de vijfde en de "
                 "zesde, bij \\(n = 20\\) de tiende en de elfde.",
             ]),
        dict(aanpak="Gemiddelde en mediaan naast elkaar leggen vertelt iets over de vorm van de "
                    "verdeling: liggen ze dicht bij elkaar, dan is ze symmetrisch; trekt het gemiddelde "
                    "weg, dan is er een uitschieter.",
             waarom=[
                 "Een gemiddelde dat veel hoger ligt dan de mediaan wijst op een of enkele hoge "
                 "uitschieters; omgekeerd op lage. Dat is de snelste controle op een reeks.",
             ]),
        dict(aanpak="Numeriek is wat je kan meten of tellen, categorisch is een naam of een groep. Een "
                    "handige test: kan je ermee rekenen en betekent dat gemiddelde iets?",
             waarom=[
                 "Met een postcode of een rugnummer kan je rekenen, maar het gemiddelde ervan betekent "
                 "niets; dat zijn dus categorische gegevens in cijfervorm.",
             ]),
        dict(aanpak="Relatieve frequentie is het deel op het geheel, maal honderd. Deel dus altijd door het "
                    "totaal en niet door het grootste getal.",
             waarom=[
                 "\\(\\frac{20}{50} = 0{,}40\\), dus \\(40\\,\\%\\). En \\(\\frac{9}{36}\\) en "
                 "\\(\\frac{14}{56}\\) geven beide \\(25\\,\\%\\): verschillende aantallen, hetzelfde "
                 "aandeel.",
             ]),
        dict(aanpak="Relatieve frequenties maken groepen van verschillende grootte vergelijkbaar. Dat is "
                    "hun hele nut.",
             waarom=[
                 "Keerzijde: een percentage zonder het aantal erachter kan misleiden. \\(50\\,\\%\\) van "
                 "twee mensen klinkt even sterk als \\(50\\,\\%\\) van tweeduizend, en dat is het niet.",
             ]),
        dict(aanpak="Bij klassen maak je gelijke intervallen die aansluiten zonder te overlappen. Daarom "
                    "schrijf je ze halfopen: de bovengrens hoort bij de volgende klasse.",
             waarom=[
                 "\\(190 - 150 = 40\\), en \\(40 : 10 = 4\\) klassen. Door ze halfopen te schrijven weet "
                 "je zeker waar \\(160\\) cm thuishoort.",
                 "Die controle moet je altijd doen: tel de frequenties op en vergelijk met \\(n\\). Komt "
                 "het niet uit, dan is er een waarde dubbel geteld of vergeten.",
             ]),
        dict(aanpak="Kies je kengetal bij de gegevens: gemiddelde bij symmetrische getallen, mediaan bij "
                    "uitschieters, modus bij categorieën of bij wat het vaakst voorkomt.",
             waarom=[
                 "Daarom spreekt men bij lonen en bij huizenprijzen over de mediaan: het mediane loon "
                 "zegt wat een gewone werknemer verdient, het gemiddelde niet.",
                 "Een winkelier heeft niets aan de gemiddelde schoenmaat van \\(41{,}3\\): die bestaat "
                 "niet. Hij wil weten welke maat hij het meest moet inkopen.",
             ]),
        dict(aanpak="Zelfde vraag, en let bij de waar-of-niet-waarvragen op welk kengetal gevoelig is voor "
                    "uitschieters.",
             waarom=[
                 "Bij temperaturen van een maand liggen de waarden dicht bij elkaar en is er geen "
                 "uitschieter die het gemiddelde vertekent.",
                 "Net omgekeerd: het gemiddelde is veel gevoeliger voor een uitschieter, want elke waarde "
                 "weegt mee. De mediaan kijkt enkel naar de plaats in de rij.",
                 "Een gemiddelde haarkleur bestaat niet, maar de meest voorkomende wel. Daarom is de modus "
                 "het enige kengetal dat ook bij categorische gegevens werkt.",
             ]),
        dict(aanpak="\\(Q_{1}\\) is de mediaan van de onderste helft, \\(Q_{3}\\) die van de bovenste. De "
                    "interkwartielafstand is \\(Q_{3} - Q_{1}\\) en zegt hoe breed de middelste helft van "
                    "de gegevens ligt.",
             waarom=[
                 "Bij tien waarden liggen de kwartielen op de derde en de achtste plaats. Reken de plaats "
                 "uit; gokken op het zicht loopt hier mis.",
                 "De variatiebreedte kijkt enkel naar de twee uiterste waarden en is dus heel gevoelig "
                 "voor een uitschieter; de interkwartielafstand niet, want die kijkt naar de middelste "
                 "helft.",
             ]),
        dict(aanpak="Hetzelfde gemiddelde met een andere spreiding geeft een heel ander beeld. Daarom "
                    "hoort bij elk gemiddelde een maat voor de spreiding.",
             waarom=[
                 "Concreet: in klas A zit bijna iedereen tussen \\(56\\) en \\(64\\,\\%\\), in klas B zit "
                 "men van \\(30\\) tot \\(90\\,\\%\\). Dezelfde klasgemiddelde, een heel andere klas.",
             ]),
        dict(aanpak="Een boxplot toont vijf getallen: minimum, \\(Q_{1}\\), mediaan, \\(Q_{3}\\) en "
                    "maximum. De doos is de middelste helft van de gegevens.",
             waarom=[
                 "Daarom zijn twee boxplots naast elkaar zo nuttig: je ziet in één oogopslag welke groep "
                 "hoger ligt én welke meer spreiding heeft.",
                 "Het aantal gegevens zie je niet op een boxplot: eenzelfde doos kan van tien of van "
                 "duizend waarden komen. Zet \\(n\\) er dus altijd bij.",
             ]),
        dict(aanpak="Kies je grafiek naar de vraag: verloop in de tijd vraagt een lijngrafiek, aandelen van "
                    "een geheel een cirkeldiagram, vergelijking tussen categorieën een staafdiagram.",
             waarom=[
                 "Een cirkeldiagram mag je enkel gebruiken als de delen samen een geheel vormen; anders "
                 "suggereert het iets wat er niet is.",
             ]),
        dict(aanpak="Zelfde keuze, met drie andere grafieken: boxplots voor spreiding, een puntenwolk voor "
                    "het verband tussen twee grootheden, een histogram voor de verdeling van één "
                    "numerieke grootheid.",
             waarom=[
                 "Een puntenwolk is de enige van de drie die twee grootheden tegen elkaar zet. De andere "
                 "twee tonen één grootheid.",
                 "Bij een histogram staan de staven tegen elkaar, want de klassen sluiten aan. Bij een "
                 "staafdiagram staan ze los, want de categorieën zijn gescheiden. Dat is het verschil "
                 "tussen die twee.",
             ]),
        dict(aanpak="Een grafiek lezen begint bij de assen: waar begint de verticale as, welke eenheid "
                    "staat erbij, en hoeveel gegevens zitten erachter?",
             waarom=[
                 "Een afgekapte as is de meest voorkomende truc in kranten en reclame. Het verschil ziet "
                 "er dan veel groter uit dan het is.",
                 "Een derde punt om op te letten: het soort grafiek. Een cirkeldiagram voor iets dat geen "
                 "geheel vormt, of een lijngrafiek door categorieën, misleidt ook.",
                 "Reken de stijging na: \\(\\frac{2}{98} \\approx 2\\,\\%\\). Op een as die bij \\(97\\) "
                 "begint, is de eerste staaf één eenheid hoog en de tweede drie, dus lijkt ze drie keer "
                 "zo hoog. Zo wordt \\(2\\,\\%\\) een beeld van \\(200\\,\\%\\).",
             ]),
    ]
)


UITLEGBLADEN["oefenbundel-verbanden-tussen-twee-grootheden-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Kijk naar de vorm van het voorschrift: \\(y = ax\\) is recht evenredig, "
                    "\\(y = ax + b\\) lineair, \\(y = \\frac{a}{x}\\) omgekeerd evenredig, en al de rest "
                    "geen van de drie.",
             waarom=[
                 "Het enige verschil tussen de eerste twee is de \\(+2\\). Juist die constante haalt de "
                 "grafiek van de oorsprong weg en maakt het verband niet meer recht evenredig.",
             ]),
        dict(aanpak="Bij een situatie in woorden vraag je je af of er een vast bedrag bijkomt. Zo ja, dan "
                    "is het lineair en niet recht evenredig.",
             waarom=[
                 "\\(y = x^{2}\\) is kwadratisch: dubbele \\(x\\) geeft vier keer zoveel \\(y\\). Bij "
                 "benzine betaal je per liter zonder opstapkost, dus recht evenredig; bij een taxi met "
                 "opstapgeld niet.",
                 "Een geheugensteun: recht evenredig is het bijzondere geval van lineair met \\(b = 0\\). "
                 "Elke recht evenredige functie is dus lineair, maar niet omgekeerd.",
             ]),
        dict(aanpak="Vul een tabel aan met de eigenschap van het verband: bij recht evenredig blijft "
                    "\\(\\frac{y}{x}\\) gelijk, bij omgekeerd evenredig blijft \\(x \\cdot y\\) gelijk.",
             waarom=[
                 "Zoek eerst de constante uit een kolom die je wel hebt, en gebruik die voor de rest. Dan "
                 "hoef je niet per kolom te zoeken.",
                 "Hier blijft het product gelijk, dus deel je die constante door de gegeven \\(x\\). Let "
                 "op: bij omgekeerd evenredig hoort \\(x = 0\\) nooit bij het domein.",
             ]),
        dict(aanpak="Zoek uit een tabel het voorschrift in twee stappen: eerst \\(a\\) als de stap in "
                    "\\(y\\) gedeeld door de stap in \\(x\\), dan \\(b\\) door één punt in te vullen.",
             waarom=[
                 "Controleer met een tweede punt: \\(3 \\cdot 6 + 1 = 19\\), en dat klopt met de tabel. "
                 "Wie \\(b\\) vergeet, komt op \\(y = 3x\\) uit en dat geeft \\(6\\) in plaats van "
                 "\\(7\\).",
             ]),
        dict(aanpak="Een puntenwolk lees je op de richting: stijgend is positieve samenhang, dalend "
                    "negatieve, geen richting betekent geen samenhang.",
             waarom=[
                 "Positief of negatief zegt niets over goed of slecht: het gaat enkel over de richting van "
                 "het verband.",
             ]),
        dict(aanpak="Drie begrippen bij een puntenwolk: hoe sterk de samenhang is, de trendlijn die er het "
                    "best door loopt, en een uitschieter die ver van de wolk ligt.",
             waarom=[
                 "Een uitschieter kan de trendlijn flink verdraaien. Kijk er altijd naar en vraag je af of "
                 "het een meetfout is of een echt geval.",
             ]),
        dict(aanpak="De correlatiecoëfficiënt \\(r\\) zegt twee dingen in één getal: het teken geeft de "
                    "richting en de grootte geeft de sterkte.",
             waarom=[
                 "\\(r = -1\\) is een perfect verband, al staat er een minteken: alle punten liggen op een "
                 "dalende rechte. Dicht bij nul betekent geen lineair verband.",
             ]),
        dict(aanpak="Lees het teken en de grootte apart. Vergelijk de sterkte altijd op de absolute "
                    "waarde van \\(r\\).",
             waarom=[
                 "\\(\\left|-1\\right| = 1\\) en dat is het sterkst mogelijke verband, veel sterker dan "
                 "\\(0{,}5\\). Het minteken zegt alleen dat het dalend is.",
                 "Een boogvormige wolk kan een heel sterk verband zijn met een \\(r\\) rond nul. Daarom "
                 "kijk je altijd ook naar de puntenwolk zelf en niet enkel naar \\(r\\).",
             ]),
        dict(aanpak="\\(r\\) ligt altijd tussen \\(-1\\) en \\(1\\). Komt er bij jou iets buiten dat "
                    "bereik uit, dan is er een rekenfout.",
             waarom=[
                 "In de praktijk haalt men bijna nooit exact \\(1\\) of \\(-1\\); dat zou betekenen dat "
                 "elk punt precies op de rechte ligt.",
             ]),
        dict(aanpak="Bij een samenhang hoort altijd de vraag: zou er een derde factor kunnen zijn? Vind je "
                    "die, dan heb je de uitleg zonder oorzakelijk verband.",
             waarom=[
                 "De warme zomermaanden verklaren beide: meer ijsjes én meer mensen in het water. Dit is "
                 "het klassieke voorbeeld, en het patroon komt in het nieuws vaker voor dan je denkt.",
             ]),
        dict(aanpak="Er zijn drie manieren waarop een samenhang geen oorzaak is: een derde factor, een "
                    "omgekeerde richting, of gewoon toeval. Noem er bij zo'n vraag minstens twee.",
             waarom=[
                 "De omgekeerde richting wordt vaak vergeten: slapen mensen slecht omdat ze stress hebben, "
                 "of hebben ze stress omdat ze slecht slapen? Uit de cijfers alleen weet je dat niet.",
             ]),
        dict(aanpak="Een oorzaak toon je niet met cijfers uit observatie maar met een proef waarin je één "
                    "ding verandert en de rest gelijk houdt.",
             waarom=[
                 "Kan je geen proef doen, bijvoorbeeld omdat het onethisch is, dan gebruikt men meerdere "
                 "onafhankelijke studies en zoekt men een verklarend mechanisme. Zo is het verband tussen "
                 "roken en longkanker vastgesteld.",
             ]),
        dict(aanpak="Een trendlijn gebruik je om te voorspellen, maar enkel binnen het bereik waarin je "
                    "gemeten hebt. Buiten dat bereik zegt de rechte niets.",
             waarom=[
                 "Vul in en rond af naar een bestaande maat: \\(41{,}2\\) wordt maat \\(41\\). Een "
                 "schoenmaat met een komma bestaat niet.",
                 "Dat heet extrapoleren, en het is de klassieke fout met trendlijnen: een baby van "
                 "\\(60\\) cm met schoenmaat \\(12\\) is onmogelijk. Een rechte die binnen het "
                 "meetbereik mooi klopt, mag je er niet buiten doortrekken.",
             ]),
        dict(aanpak="Zet de situatie eerst in een formule met een vast deel en een deel per stuk. Een vraag "
                    "over de prijs per stuk vraagt daarna een deling door \\(x\\).",
             waarom=[
                 "\\(25\\) is het vaste deel, \\(0{,}40x\\) het variabele. Bij \\(150\\) affiches is dat "
                 "\\(25 + 60 = 85\\) euro.",
                 "Let op het antwoord in hele affiches: \\(x > 125\\) betekent vanaf \\(126\\). Bij "
                 "precies \\(125\\) affiches kost één affiche exact \\(0{,}60\\) euro.",
                 "Mooi om te zien: de totale prijs stijgt lineair, maar de prijs per stuk daalt, want de "
                 "opstartkost wordt over meer affiches verdeeld. Dat is precies waarom drukwerk per stuk "
                 "goedkoper wordt bij een grotere oplage.",
             ]),
    ]
)
