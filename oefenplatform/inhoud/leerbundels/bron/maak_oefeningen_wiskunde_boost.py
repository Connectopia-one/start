# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij wiskunde gevorderd 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere getallen, andere situaties, en opdrachten die je enkel op papier
kan maken (een tabel aanvullen, een redenering uitschrijven, een schets maken).
Wie hier iets bijschrijft, legt het eerst naast
`../../boost-doorstroom/wiskunde-gevorderd.json` én naast de leerbundel, want de
oefenbundel is de tweede dekkingscontrole op de theorie.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom". Het voorvoegsel is nodig omdat leerbundels en oefenbundels
in dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen. Het achtervoegsel houdt ze uit elkaar van Boost dubbele finaliteit.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Wiskunde gevorderd"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf je tussenstappen op. Een antwoord zonder berekening is niet na te kijken, ook niet door jezelf.",
    "Zet bij elk antwoord de eenheid, als er een is. Een getal zonder eenheid is in een vraagstuk zelden een antwoord.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


# ============================================================
OEFENBUNDELS["oefenbundel-een-opgave-aanpakken-van-context-naar-wiskunde-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Een opgave aanpakken: van context naar wiskunde",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Mathematiseren of demathematiseren?",
             opdracht="Schrijf bij elke stap welke van de twee je aan het doen bent.",
             oefeningen=[
                 ("rij", [("je noemt het aantal kilometer x en schrijft de kost als 0,30x + 15", "mathematiseren"),
                          ("je rekent 7,3 uit en antwoordt dat er 8 bussen nodig zijn", "demathematiseren"),
                          ("je tekent de ladder als een rechthoekige driehoek", "mathematiseren"),
                          ("je rondt 4,7 meter af tot een ladder van 5 meter", "demathematiseren")],
                  "Welke stap?", WW),
             ]),
        dict(kop="Welke heuristiek?",
             opdracht="Schrijf bij elke aanpak welke heuristiek uit de lijst van de fiche je gebruikt.",
             oefeningen=[
                 ("rij", [("je noemt de leeftijd van de jongste broer x", "variabelen invoeren"),
                          ("je knipt 'hoeveel kost een schoolreis' op in bus, inkom en eten", "opsplitsen in deelproblemen"),
                          ("je schrijft alle vier de kleuren met alle drie de maten uit", "alle mogelijkheden opschrijven"),
                          ("je berekent maar één helft van de figuur en verdubbelt", "gebruik maken van symmetrie")],
                  "Welke heuristiek?", WL),
                 ("rij", [("je vertrekt van de eindprijs en rekent terug naar de beginprijs", "terugrekenen"),
                          ("je bekijkt de verschillen tussen 3, 8, 15, 24", "patronen en regelmaat ontdekken"),
                          ("je probeert 10, ziet dat het te groot is, en probeert 8", "schatten, slim gissen, testen en controleren")],
                  "Welke heuristiek?", WL),
             ]),
        dict(kop="De vier stappen op een rij",
             opdracht="Vul de vier stappen in, in de juiste volgorde.",
             oefeningen=[
                 ("tabel", ["stap", "naam"],
                  [["1", None], ["2", None], ["3", None], ["4", None]],
                  "1 begrijp het probleem · 2 maak een plan · 3 voer het plan uit · 4 reflecteer", "230px"),
             ]),
        dict(kop="Reflecteren",
             opdracht="Bij elke uitkomst: schrijf op waarom ze niet kan kloppen, en wat er waarschijnlijk misging.",
             oefeningen=[
                 ("open", "Een zwembad van 25 m op 10 m op 2 m zou 500 liter water bevatten.",
                  "500 liter is een halve kubieke meter, en het bad is 500 m³. De eenheid ging mis: "
                  "500 m³ is 500 000 liter.", 4),
                 ("open", "Een auto legt 90 km af in 45 minuten; iemand berekent 2 km per uur.",
                  "45 minuten is 0,75 uur, en 90 gedeeld door 0,75 is 120 km/u. Er is gedeeld door 45 "
                  "in plaats van door 0,75.", 4),
                 ("open", "De oppervlakte van een tuin komt uit op min 12 m².",
                  "Een oppervlakte kan niet negatief zijn. Waarschijnlijk is er een lengte afgetrokken "
                  "die er bij moest, of zijn twee maten verwisseld.", 4),
             ]),
        dict(kop="Schatten eerst",
             opdracht="Schat eerst met ronde getallen, schrijf je schatting op, en reken daarna precies.",
             oefeningen=[
                 ("rij", [("schatting van 49 · 31", "ongeveer 1500"),
                          ("exact 49 · 31", "1519"),
                          ("schatting van 198 : 4", "ongeveer 50"),
                          ("exact 198 : 4", "49,5")],
                  "Antwoord", W),
             ]),
        dict(kop="Zelf oplossen",
             opdracht="Werk met de vier stappen. Schrijf minstens je plan en je controle op.",
             oefeningen=[
                 ("open", "Na 25 % korting betaal je 60 euro. Wat was de oude prijs?",
                  "60 euro is 75 % van de oude prijs, dus de oude prijs is 60 : 0,75 = 80 euro. "
                  "Controle: 25 % van 80 is 20, en 80 − 20 = 60.", 6),
                 ("open", "Welk getal volgt in de rij 3, 8, 15, 24, 35? Leg uit hoe je het vindt.",
                  "De verschillen zijn 5, 7, 9, 11, dus het volgende verschil is 13 en het getal is 48.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een schets maken telt als een volwaardige oplossingsstrategie.", True),
                 ("waar", "Een goede schatting vervangt de exacte berekening.", False),
                 ("waar", "Eén tegenvoorbeeld volstaat om een uitspraak te weerleggen.", True),
                 ("waar", "Drie voorbeelden die kloppen, bewijzen dat een eigenschap altijd geldt.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-logica-symbolen-waarheidstabellen-en-poorten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Logica: symbolen, waarheidstabellen en poorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Is het een uitspraak?",
             opdracht="Duid aan of de zin een logische uitspraak is.",
             oefeningen=[
                 ("kies", "Negen is een priemgetal.", ["wel een uitspraak", "geen uitspraak"], 0),
                 ("kies", "Sluit de deur achter je.", ["wel een uitspraak", "geen uitspraak"], 1),
                 ("kies", "Antwerpen ligt in Wallonië.", ["wel een uitspraak", "geen uitspraak"], 0),
                 ("kies", "Waar woon jij?", ["wel een uitspraak", "geen uitspraak"], 1),
             ]),
        dict(kop="In symbolen",
             opdracht="p is 'het sneeuwt' en q is 'de school is dicht'. Schrijf elke zin in symbolen.",
             oefeningen=[
                 ("rij", [("het sneeuwt en de school is dicht", "p ∧ q"),
                          ("het sneeuwt niet", "¬p"),
                          ("als het sneeuwt, is de school dicht", "p ⇒ q"),
                          ("het sneeuwt of de school is dicht", "p ∨ q")],
                  "In symbolen", W),
                 ("rij", [("het is niet zo dat het sneeuwt en de school dicht is", "¬(p ∧ q)"),
                          ("de school is dicht als en slechts als het sneeuwt", "q ⇔ p")],
                  "In symbolen", WW),
             ]),
        dict(kop="De waarheidstabel invullen",
             opdracht="Vul 1 voor waar en 0 voor vals in.",
             oefeningen=[
                 ("tabel", ["p", "q", "p ∧ q", "p ∨ q", "p ⇒ q"],
                  [["1", "1", None, None, None],
                   ["1", "0", None, None, None],
                   ["0", "1", None, None, None],
                   ["0", "0", None, None, None]],
                  "rij 1: 1, 1, 1 · rij 2: 0, 1, 0 · rij 3: 0, 1, 1 · rij 4: 0, 0, 1", "90px"),
             ]),
        dict(kop="Hoeveel rijen?",
             opdracht="Schrijf op hoeveel rijen de waarheidstabel telt.",
             oefeningen=[
                 ("rij", [("twee variabelen", "4"), ("drie variabelen", "8"),
                          ("vier variabelen", "16"), ("vijf variabelen", "32")],
                  "Aantal rijen", W),
             ]),
        dict(kop="Tautologie, contradictie of geen van beide?",
             opdracht="Vul de waarheidstabel in op je kladblad en beslis daarna.",
             oefeningen=[
                 ("rij", [("p ∨ ¬p", "tautologie"), ("p ∧ ¬p", "contradictie"),
                          ("p ⇒ p", "tautologie"), ("p ∧ q", "geen van beide")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Kwantoren en negatie",
             opdracht="Schrijf de negatie van elke uitspraak in gewone taal.",
             oefeningen=[
                 ("rij", [("alle zwanen zijn wit", "minstens één zwaan is niet wit"),
                          ("er bestaat een even priemgetal", "geen enkel priemgetal is even"),
                          ("alle leerlingen waren aanwezig", "minstens één leerling was afwezig")],
                  "De negatie", WL),
                 ("kort", "Welk symbool betekent 'voor alle'?", "∀", W),
                 ("kort", "Welk symbool betekent 'er bestaat'?", "∃", W),
             ]),
        dict(kop="Nodig of voldoende?",
             opdracht="'Als een getal deelbaar is door 6, dan is het deelbaar door 3.' Duid aan.",
             oefeningen=[
                 ("kies", "Deelbaar zijn door 3 om deelbaar te zijn door 6.",
                  ["nodig maar niet voldoende", "voldoende maar niet nodig"], 0),
                 ("kies", "Deelbaar zijn door 6 om deelbaar te zijn door 3.",
                  ["nodig maar niet voldoende", "voldoende maar niet nodig"], 1),
             ]),
        dict(kop="Tegenvoorbeelden",
             opdracht="Geef één tegenvoorbeeld dat de uitspraak weerlegt.",
             oefeningen=[
                 ("kort", "Elk getal deelbaar door 4 is deelbaar door 8.", "12 (of 4, 20, 28)", WW),
                 ("kort", "Elk priemgetal is oneven.", "2", W),
                 ("kort", "De wortel van een som is de som van de wortels.", "√(9 + 16) = 5, niet 7", WL),
             ]),
        dict(kop="Welke poort?",
             opdracht="Schrijf bij elke schakeling welke poort past.",
             oefeningen=[
                 ("rij", [("de motor start alleen als de sleutel én de rem ingedrukt zijn", "een EN-poort"),
                          ("het licht gaat aan bij beweging of bij een druk op de knop", "een OF-poort"),
                          ("het signaal wordt omgekeerd van 0 naar 1", "een NIET-poort")],
                  "Welke poort?", WW),
             ]),
        dict(kop="Wat mag mee op het examen?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Het formularium uit bijlage 1 mag je gebruiken.", True),
                 ("waar", "De lijst met bewijzen mag je gebruiken.", False),
                 ("waar", "De stelling van Pythagoras staat in de lijst met bewijzen.", True),
                 ("waar", "De som van de hoeken in een vierhoek staat in de lijst met bewijzen.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-reele-getallen-wortels-en-machten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Reële getallen, wortels en machten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Tot welke verzameling?",
             opdracht="Schrijf de kleinste verzameling waartoe het getal behoort: ℕ, ℤ, ℚ of ℝ.",
             oefeningen=[
                 ("rij", [("12", "ℕ"), ("min 5", "ℤ"), ("0,75", "ℚ"), ("√7", "ℝ")],
                  "Verzameling", W),
                 ("rij", [("π", "ℝ"), ("22/7", "ℚ"), ("√49", "ℕ"), ("min 0,2", "ℚ")],
                  "Verzameling", W),
             ]),
        dict(kop="Rationaal of irrationaal?",
             opdracht="Duid aan wat het is.",
             oefeningen=[
                 ("kies", "0,272727… met een eindeloos herhalend 27", ["rationaal", "irrationaal"], 0),
                 ("kies", "√8", ["rationaal", "irrationaal"], 1),
                 ("kies", "√64", ["rationaal", "irrationaal"], 0),
                 ("kies", "3,14159265358979… (π)", ["rationaal", "irrationaal"], 1),
             ]),
        dict(kop="Breuk, kommagetal, procent",
             opdracht="Vul de tabel aan. Vereenvoudig elke breuk.",
             oefeningen=[
                 ("tabel", ["breuk", "kommagetal", "procent"],
                  [["1/4", None, None], [None, "0,6", None], [None, None, "12,5 %"], ["7/10", None, None]],
                  "1/4 → 0,25 → 25 % · 3/5 → 0,6 → 60 % · 1/8 → 0,125 → 12,5 % · 7/10 → 0,7 → 70 %",
                  "150px"),
             ]),
        dict(kop="Wortels vereenvoudigen",
             opdracht="Haal het grootste volkomen kwadraat uit de wortel.",
             oefeningen=[
                 ("rij", [("√8", "2√2"), ("√27", "3√3"), ("√48", "4√3"), ("√75", "5√3")],
                  "Vereenvoudigd", W),
             ]),
        dict(kop="Rekenen met wortels",
             opdracht="Reken uit en vereenvoudig.",
             oefeningen=[
                 ("rij", [("√2 · √8", "4"), ("√6 · √6", "6"), ("√5 + √5", "2√5"),
                          ("√(16 + 9)", "5")],
                  "Antwoord", W),
                 ("rij", [("1/√3 wortelvrij", "√3/3"), ("2/√2 wortelvrij", "√2"),
                          ("√(a²) met a = min 4", "4")],
                  "Antwoord", WW),
             ]),
        dict(kop="Machten",
             opdracht="Schrijf zo eenvoudig mogelijk.",
             oefeningen=[
                 ("rij", [("a⁵ · a²", "a⁷"), ("a⁸ : a³", "a⁵"), ("(a²)⁴", "a⁸"), ("(3a)²", "9a²")],
                  "Antwoord", W),
                 ("rij", [("7⁰", "1"), ("2⁻⁴", "1/16"), ("5⁻²", "1/25"), ("(2a)⁴", "16a⁴")],
                  "Antwoord", W),
             ]),
        dict(kop="Welke eigenschap?",
             opdracht="Schrijf op welke rekeneigenschap er gebruikt wordt.",
             oefeningen=[
                 ("rij", [("4 · (10 + 3) = 4 · 10 + 4 · 3", "distributiviteit"),
                          ("(5 + 7) + 3 = 5 + (7 + 3)", "associativiteit"),
                          ("6 · 9 = 9 · 6", "commutativiteit")],
                  "Welke eigenschap?", WW),
             ]),
        dict(kop="Fouten zoeken",
             opdracht="Bij elke bewering: klopt ze? Zo niet, schrijf op wat het juiste antwoord is.",
             oefeningen=[
                 ("open", "√(25 + 144) = 5 + 12 = 17.",
                  "Fout. De wortel van een som is niet de som van de wortels. √169 = 13.", 3),
                 ("open", "a³ · a⁴ = a¹².",
                  "Fout. Bij vermenigvuldigen tel je de exponenten op: a⁷.", 3),
                 ("open", "(2a)³ = 2a³.",
                  "Fout. Elke factor krijgt de exponent: 8a³.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Elk geheel getal is ook een rationaal getal.", True),
                 ("waar", "Elk reëel getal kan je als breuk van twee gehele getallen schrijven.", False),
                 ("waar", "√a · √b is gelijk aan √(ab).", True),
                 ("waar", "Een negatieve exponent maakt het getal zelf negatief.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-ordenen-afronden-intervallen-en-wetenschappelijke-notatie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Ordenen, afronden, intervallen en wetenschappelijke notatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk teken?",
             opdracht="Schrijf < of > tussen de twee getallen.",
             oefeningen=[
                 ("rij", [("min 7 en min 2", "<"), ("0,45 en 0,5", "<"),
                          ("min 1 en 0", "<"), ("3/4 en 0,7", ">")],
                  "Teken", W),
             ]),
        dict(kop="Ordenen van klein naar groot",
             opdracht="Zet ze eerst allemaal in dezelfde vorm en schrijf ze dan op volgorde.",
             oefeningen=[
                 ("open", "0,7 — 2/3 — 68 % — 0,71",
                  "2/3 is 0,666…, dus: 2/3 — 68 % — 0,7 — 0,71.", 3),
                 ("open", "min 0,5 — min 1/4 — min 0,75 — 0",
                  "min 0,75 — min 0,5 — min 1/4 — 0.", 3),
             ]),
        dict(kop="Afronden",
             opdracht="Rond af op twee cijfers na de komma. Kijk naar het eerste cijfer dat wegvalt.",
             oefeningen=[
                 ("rij", [("5,6349", "5,63"), ("5,6351", "5,64"), ("0,9962", "1,00"), ("12,3450", "12,35")],
                  "Afgerond", W),
             ]),
        dict(kop="Schatten",
             opdracht="Schat op honderdtallen of op tientallen, zoals gevraagd.",
             oefeningen=[
                 ("rij", [("38 · 52 op honderdtallen", "ongeveer 2000"),
                          ("29 · 31 op honderdtallen", "ongeveer 900"),
                          ("812 : 4 op tientallen", "ongeveer 200")],
                  "Schatting", WW),
             ]),
        dict(kop="Intervallen lezen",
             opdracht="Schrijf in gewone taal wat het interval betekent.",
             oefeningen=[
                 ("rij", [("[1, 6]", "alle getallen van 1 tot 6, grenzen erbij"),
                          ("]0, 4[", "alle getallen tussen 0 en 4, grenzen niet erbij"),
                          ("[2, 9[", "van 2 tot 9, met 2 erbij en 9 niet")],
                  "Betekenis", WL),
             ]),
        dict(kop="Intervallen schrijven",
             opdracht="Schrijf de verzameling als interval.",
             oefeningen=[
                 ("rij", [("alle x groter dan 4", "]4, +∞["),
                          ("alle x kleiner dan of gelijk aan 0", "]−∞, 0]"),
                          ("alle x tussen min 1 en 5, grenzen erbij", "[−1, 5]"),
                          ("alle x groter dan of gelijk aan min 2", "[−2, +∞[")],
                  "Interval", WW),
             ]),
        dict(kop="Wetenschappelijke notatie",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["gewoon getal", "wetenschappelijke notatie"],
                  [["73 000", None], [None, "9,1 · 10⁻⁵"], ["0,00408", None], [None, "2 · 10⁷"]],
                  "73 000 → 7,3 · 10⁴ · 9,1 · 10⁻⁵ → 0,000091 · 0,00408 → 4,08 · 10⁻³ · "
                  "2 · 10⁷ → 20 000 000", "210px"),
             ]),
        dict(kop="Correct of niet?",
             opdracht="Duid aan of het een correcte wetenschappelijke notatie is.",
             oefeningen=[
                 ("kies", "34,2 · 10³", ["correct", "niet correct"], 1),
                 ("kies", "3,42 · 10⁴", ["correct", "niet correct"], 0),
                 ("kies", "0,5 · 10⁶", ["correct", "niet correct"], 1),
                 ("kies", "8 · 10⁻²", ["correct", "niet correct"], 0),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij oneindig wijst het haakje altijd naar buiten.", True),
                 ("waar", "Het interval [5, 5] is leeg.", False),
                 ("waar", "Een negatieve exponent betekent dat het getal negatief is.", False),
                 ("waar", "Je rondt best pas op het einde van een berekening af.", True),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Een weegschaal geeft 3,7 kg en rondt af op honderd gram. Tussen welke "
                          "waarden ligt het echte gewicht?",
                  "Tussen 3,65 kg en 3,75 kg.", 4),
                 ("open", "Waarom gebruiken wetenschappers machten van tien in plaats van rijen nullen?",
                  "Omdat je dan even makkelijk over een atoom als over een sterrenstelsel schrijft, "
                  "zonder nullen te tellen, en omdat je de grootteorde meteen ziet.", 4),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-rechten-vlakken-en-gelijkvormigheid-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Rechten, vlakken en gelijkvormigheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Onderlinge ligging",
             opdracht="Schrijf bij elk paar hoe ze ten opzichte van elkaar liggen.",
             oefeningen=[
                 ("rij", [("twee rechten die elkaar niet snijden en niet in één vlak liggen", "kruisend"),
                          ("twee rechten in één vlak zonder snijpunt", "evenwijdig"),
                          ("twee vlakken die elkaar raken", "snijdend, met een rechte als doorsnede"),
                          ("een rechte en een vlak met één gemeenschappelijk punt", "de rechte snijdt het vlak")],
                  "Ligging", WL),
             ]),
        dict(kop="Een balk tellen",
             opdracht="Vul de aantallen in.",
             oefeningen=[
                 ("tabel", ["figuur", "zijvlakken", "ribben", "hoekpunten"],
                  [["balk", None, None, None], ["kubus", None, None, None]],
                  "allebei 6 zijvlakken, 12 ribben en 8 hoekpunten", "110px"),
             ]),
        dict(kop="Tekenen en aanzichten",
             opdracht="Beantwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet het platte patroon van een opengevouwen ruimtefiguur?", "de ontwikkeling", WW),
                 ("kort", "Welke drie aanzichten noemt de fiche?", "voor-, boven- en zijaanzicht", WL),
                 ("open", "Wat blijft er in het cavalièreperspectief behouden dat in een echt "
                          "perspectief verloren gaat?",
                  "Evenwijdige ribben blijven evenwijdig getekend. In een echt perspectief lopen ze "
                  "naar een verdwijnpunt.", 4),
             ]),
        dict(kop="Verzamelingen",
             opdracht="A = {1, 2, 3, 4, 5} en B = {4, 5, 6}. Schrijf de verzameling op.",
             oefeningen=[
                 ("rij", [("A ∩ B", "{4, 5}"), ("A ∪ B", "{1, 2, 3, 4, 5, 6}"),
                          ("A \\ B", "{1, 2, 3}"), ("B \\ A", "{6}")],
                  "Verzameling", WW),
             ]),
        dict(kop="Gelijkvormigheidskenmerken",
             opdracht="Schrijf welk kenmerk je gebruikt: HH, ZZZ of ZHZ.",
             oefeningen=[
                 ("rij", [("twee driehoeken met hoeken 40° en 70° gemeen", "HH"),
                          ("zijden 3-4-5 en 9-12-15", "ZZZ"),
                          ("zijden 4 en 6 met de hoek van 50° ertussen, en 8 en 12 met 50° ertussen", "ZHZ")],
                  "Kenmerk", W),
             ]),
        dict(kop="Factor k",
             opdracht="Vul in wat er met lengte, oppervlakte en volume gebeurt.",
             oefeningen=[
                 ("tabel", ["factor k", "lengte maal", "oppervlakte maal", "volume maal"],
                  [["2", None, None, None], ["3", None, None, None],
                   ["4", None, None, None], ["5", None, None, None]],
                  "2 → 2, 4, 8 · 3 → 3, 9, 27 · 4 → 4, 16, 64 · 5 → 5, 25, 125", "100px"),
             ]),
        dict(kop="Rekenen met schaal",
             opdracht="Reken om. Zet het antwoord in de gevraagde eenheid.",
             oefeningen=[
                 ("rij", [("schaal 1 : 50, op de maquette 9 cm, in het echt in meter", "4,5 m"),
                          ("schaal 1 : 200, op het plan 6 cm, in het echt in meter", "12 m"),
                          ("schaal 1 : 25 000, op de kaart 12 cm, in het echt in km", "3 km")],
                  "In het echt", WW),
             ]),
        dict(kop="Toepassen",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Een affiche van 20 op 30 cm wordt vergroot tot 60 op 90 cm. Hoeveel keer "
                          "meer papier heb je nodig?",
                  "De factor is 3, dus de oppervlakte wordt 9 keer zo groot.", 4),
                 ("open", "Een modelauto op schaal 1 : 20 weegt 60 gram. De echte auto is van "
                          "hetzelfde materiaal. Hoeveel weegt die ongeveer?",
                  "Het gewicht volgt het volume, dus maal 20³ = 8000. Dat is 480 000 gram, dus "
                  "ongeveer 480 kg.", 5),
                 ("open", "Een driehoek heeft zijden 6, 8 en 10. Een gelijkvormige driehoek heeft als "
                          "kleinste zijde 15. Hoe lang zijn de twee andere zijden?",
                  "De factor is 2,5, dus 20 en 25.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Twee vlakken kunnen elkaar in één punt snijden.", False),
                 ("waar", "Twee driehoeken met dezelfde drie hoeken zijn altijd gelijkvormig.", True),
                 ("waar", "Gelijkvormige figuren zijn altijd even groot.", False),
                 ("waar", "Bij een schaal 1 : 100 is de tekening honderd keer kleiner.", True),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-pythagoras-en-de-rechthoekige-driehoek-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Pythagoras en de rechthoekige driehoek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De ontbrekende zijde",
             opdracht="Bereken de gevraagde zijde. Schrijf je berekening erbij.",
             oefeningen=[
                 ("rij", [("rechthoekszijden 5 en 12, schuine zijde", "13"),
                          ("rechthoekszijden 8 en 15, schuine zijde", "17"),
                          ("schuine zijde 25, één zijde 7, andere zijde", "24"),
                          ("schuine zijde 10, één zijde 6, andere zijde", "8")],
                  "Lengte", W),
             ]),
        dict(kop="Is de driehoek rechthoekig?",
             opdracht="Reken na met de omgekeerde stelling en duid aan.",
             oefeningen=[
                 ("kies", "zijden 8, 15 en 17", ["rechthoekig", "niet rechthoekig"], 0),
                 ("kies", "zijden 6, 7 en 9", ["rechthoekig", "niet rechthoekig"], 1),
                 ("kies", "zijden 7, 24 en 25", ["rechthoekig", "niet rechthoekig"], 0),
                 ("kies", "zijden 5, 6 en 8", ["rechthoekig", "niet rechthoekig"], 1),
             ]),
        dict(kop="Afstand tussen twee punten",
             opdracht="Bereken de afstand. Gebruik de formule met de verschillen.",
             oefeningen=[
                 ("rij", [("A(0, 0) en B(3, 4)", "5"), ("A(1, 1) en B(4, 5)", "5"),
                          ("A(−3, 2) en B(3, 10)", "10"), ("A(2, 7) en B(2, 1)", "6")],
                  "Afstand", W),
             ]),
        dict(kop="SOSCASTOA",
             opdracht="Schrijf op welk goniometrisch getal je nodig hebt.",
             oefeningen=[
                 ("rij", [("je kent de schuine zijde en de hoek, je zoekt de overstaande", "sinus"),
                          ("je kent de schuine zijde en de hoek, je zoekt de aanliggende", "cosinus"),
                          ("je kent de aanliggende en de hoek, je zoekt de overstaande", "tangens")],
                  "Welk getal?", W),
             ]),
        dict(kop="Waarden invullen",
             opdracht="Vul de tabel aan met exacte waarden of met 0, 1 of 0,5.",
             oefeningen=[
                 ("tabel", ["hoek", "sinus", "cosinus", "tangens"],
                  [["0°", None, None, None], ["30°", None, None, None],
                   ["45°", None, None, None], ["90°", None, None, None]],
                  "0°: 0, 1, 0 · 30°: 0,5, √3/2, √3/3 · 45°: √2/2, √2/2, 1 · 90°: 1, 0, bestaat niet",
                  "110px"),
             ]),
        dict(kop="De grondformule gebruiken",
             opdracht="De hoek is scherp. Bereken het gevraagde.",
             oefeningen=[
                 ("rij", [("sin α = 0,6, dan is cos α", "0,8"),
                          ("cos α = 0,8, dan is sin α", "0,6"),
                          ("sin α = 0,28, dan is cos α", "0,96")],
                  "Antwoord", W),
                 ("kort", "Hoe schrijf je de grondformule?", "sin²α + cos²α = 1", WW),
             ]),
        dict(kop="Toepassen",
             opdracht="Maak eerst een schets met de gegevens erop.",
             oefeningen=[
                 ("open", "Een ladder van 13 meter staat met de voet 5 meter van de muur. Hoe hoog "
                          "reikt hij?",
                  "√(169 − 25) = √144 = 12 meter.", 5),
                 ("open", "Een balk is 6 bij 8 bij 24 cm. Hoe lang is de ruimtediagonaal?",
                  "Grondvlakdiagonaal √(36 + 64) = 10, dan √(100 + 576) = √676 = 26 cm.", 6),
                 ("open", "Je staat 40 meter van een toren en kijkt onder 35° naar de top. Welke "
                          "formule gebruik je, en wat reken je uit?",
                  "De tangens: hoogte = 40 · tan 35°, dus ongeveer 28 meter. (Je ooghoogte komt er "
                  "nog bij.)", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De stelling van Pythagoras geldt in elke driehoek.", False),
                 ("waar", "De schuine zijde is altijd de langste zijde.", True),
                 ("waar", "De cosinus van een scherpe hoek kan groter zijn dan 1.", False),
                 ("waar", "Twee complementaire hoeken zijn samen 90 graden.", True),
                 ("waar", "De goniometrische cirkel heeft straal 1.", True),
                 ("waar", "Een afstand tussen twee punten kan negatief zijn.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-sinusregel-cosinusregel-en-vectoren-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Sinusregel, cosinusregel en vectoren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De derde hoek",
             opdracht="Bereken de ontbrekende hoek van de driehoek.",
             oefeningen=[
                 ("rij", [("35° en 80°", "65°"), ("90° en 27°", "63°"),
                          ("110° en 22°", "48°"), ("60° en 60°", "60°")],
                  "Derde hoek", W),
             ]),
        dict(kop="Welke regel?",
             opdracht="Schrijf welke regel je gebruikt: de sinusregel, de cosinusregel of 180 graden.",
             oefeningen=[
                 ("rij", [("je kent twee zijden en de hoek ertussen", "de cosinusregel"),
                          ("je kent de drie zijden", "de cosinusregel"),
                          ("je kent een zijde met de hoek ertegenover, plus nog één hoek", "de sinusregel"),
                          ("je kent twee hoeken en zoekt de derde", "180 graden")],
                  "Welke regel?", WW),
             ]),
        dict(kop="Kan dit een driehoek zijn?",
             opdracht="Gebruik de driehoeksongelijkheid en duid aan.",
             oefeningen=[
                 ("kies", "zijden 3, 4 en 9", ["kan wel", "kan niet"], 1),
                 ("kies", "zijden 5, 6 en 10", ["kan wel", "kan niet"], 0),
                 ("kies", "zijden 2, 2 en 5", ["kan wel", "kan niet"], 1),
                 ("kies", "zijden 7, 7 en 7", ["kan wel", "kan niet"], 0),
             ]),
        dict(kop="De formules opschrijven",
             opdracht="Schrijf de formule volledig uit.",
             oefeningen=[
                 ("kort", "De cosinusregel", "a² = b² + c² − 2bc · cos α", WL),
                 ("kort", "De sinusregel", "a/sin α = b/sin β = c/sin γ", WL),
                 ("open", "Wat gebeurt er met de cosinusregel als α gelijk is aan 90 graden, en "
                          "hoe heet het resultaat?",
                  "cos 90° is 0, dus de laatste term valt weg en er blijft a² = b² + c² over: de "
                  "stelling van Pythagoras.", 4),
             ]),
        dict(kop="Vectoren: de drie kenmerken",
             opdracht="Vul in.",
             oefeningen=[
                 ("tabel", ["kenmerk", "wat het is"],
                  [["richting", None], ["zin", None], ["grootte", None]],
                  "richting: de rechte waarop de vector ligt · zin: welke van de twee kanten · "
                  "grootte: de lengte, ook norm genoemd", "260px"),
             ]),
        dict(kop="De norm berekenen",
             opdracht="Bereken de norm van de vector met deze coördinaten.",
             oefeningen=[
                 ("rij", [("(6, 8)", "10"), ("(−3, 4)", "5"), ("(9, 12)", "15"), ("(8, 0)", "8")],
                  "Norm", W),
             ]),
        dict(kop="Vectoren tussen punten",
             opdracht="Bereken de coördinaten van de vector, en daarna zijn norm.",
             oefeningen=[
                 ("rij", [("van A(1, 1) naar B(5, 4)", "(4, 3), norm 5"),
                          ("van A(0, 2) naar B(6, 10)", "(6, 8), norm 10"),
                          ("van A(3, 5) naar B(3, 12)", "(0, 7), norm 7")],
                  "Vector en norm", WL),
             ]),
        dict(kop="Rekenen met vectoren",
             opdracht="Reken uit of leg uit.",
             oefeningen=[
                 ("rij", [("(2, 5) + (3, −1)", "(5, 4)"), ("(1, 4) + (−1, −4)", "(0, 0), de nulvector"),
                          ("min 2 maal (3, −1)", "(−6, 2)")],
                  "Antwoord", WW),
                 ("open", "Twee krachten van 6 en 8 newton staan loodrecht op elkaar. Hoe groot is "
                          "de resulterende kracht, en hoe reken je dat uit?",
                  "Met de kop-staartmethode krijg je een rechthoekige driehoek, dus Pythagoras: "
                  "√(36 + 64) = 10 newton.", 5),
                 ("open", "Wat zegt de formule van Chasles-Möbius, en waarvoor gebruik je ze?",
                  "De vector van A naar B is gelijk aan die van A naar C plus die van C naar B, via "
                  "elk tussenpunt. Je gebruikt ze om een omweg in stukken te knippen.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De norm van een vector kan negatief zijn.", False),
                 ("waar", "Twee vectoren met dezelfde richting, zin en grootte zijn gelijk, ook als "
                          "ze elders in het vlak liggen.", True),
                 ("waar", "De som van twee vectoren is altijd langer dan elk van de twee.", False),
                 ("waar", "Vermenigvuldigen met min 2 draait de zin van de vector om.", True),
                 ("waar", "De sinusregel werkt enkel in rechthoekige driehoeken.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-formules-omvormen-en-eerstegraadsvergelijkingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Formules omvormen en eerstegraadsvergelijkingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Haakjes uitwerken",
             opdracht="Werk uit en neem gelijksoortige termen samen.",
             oefeningen=[
                 ("rij", [("4(x + 3)", "4x + 12"), ("−3(x − 2)", "−3x + 6"),
                          ("(x + 5)(x + 1)", "x² + 6x + 5"), ("(x − 4)²", "x² − 8x + 16")],
                  "Uitgewerkt", WW),
                 ("rij", [("(x + 7)(x − 7)", "x² − 49"), ("2(x + 1) + 3(x − 4)", "5x − 10")],
                  "Uitgewerkt", WW),
             ]),
        dict(kop="Ontbinden in factoren",
             opdracht="Schrijf als een product.",
             oefeningen=[
                 ("rij", [("8x + 12", "4(2x + 3)"), ("x² − 25", "(x + 5)(x − 5)"),
                          ("x² + 8x + 16", "(x + 4)²"), ("3x² − 6x", "3x(x − 2)")],
                  "Ontbonden", WW),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht="Los op. Schrijf minstens één tussenstap op.",
             oefeningen=[
                 ("rij", [("4x + 7 = 31", "x = 6"), ("6x − 5 = 2x + 11", "x = 4"),
                          ("3(x − 2) = 15", "x = 7"), ("x/4 + 3 = 8", "x = 20")],
                  "Oplossing", W),
             ]),
        dict(kop="Bijzondere gevallen",
             opdracht="Los op en schrijf op wat het betekent.",
             oefeningen=[
                 ("open", "2(x + 3) = 2x + 6",
                  "Je krijgt 0 = 0: elke waarde van x is een oplossing.", 3),
                 ("open", "3x + 1 = 3x + 5",
                  "Je krijgt 0 = 4, wat niet klopt: er is geen enkele oplossing.", 3),
             ]),
        dict(kop="Ongelijkheden",
             opdracht="Los op en schrijf de oplossingenverzameling als interval.",
             oefeningen=[
                 ("rij", [("2x + 1 > 9", "x > 4, dus ]4, +∞["),
                          ("−4x ≥ 12", "x ≤ −3, dus ]−∞, −3]"),
                          ("−x + 2 < 5", "x > −3, dus ]−3, +∞["),
                          ("3x ≤ 15", "x ≤ 5, dus ]−∞, 5]")],
                  "Oplossing en interval", WL),
             ]),
        dict(kop="Formules omvormen",
             opdracht="Vorm om naar de gevraagde letter.",
             oefeningen=[
                 ("rij", [("ρ = m / V, naar V", "V = m / ρ"),
                          ("U = I · R, naar I", "I = U / R"),
                          ("F = m · g, naar g", "g = F / m"),
                          ("O = z², naar z", "z = √O")],
                  "Omgevormd", WW),
                 ("rij", [("x = x₀ + v · t, naar v", "v = (x − x₀) / t"),
                          ("E = ½ m v², naar m", "m = 2E / v²"),
                          ("c = n / V, naar n", "n = c · V")],
                  "Omgevormd", WW),
             ]),
        dict(kop="Rekenen met die formules",
             opdracht="Vul in en reken uit. Zet de eenheid erbij.",
             oefeningen=[
                 ("rij", [("massa van 5 liter olie met dichtheid 0,9 kg/l", "4,5 kg"),
                          ("weerstand bij 24 volt en 4 ampère", "6 ohm"),
                          ("zijde van een vierkant met oppervlakte 81", "9"),
                          ("massa bij een zwaartekracht van 50 N en g = 10 N/kg", "5 kg")],
                  "Antwoord", WW),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Kies een onbekende, schrijf op waar ze voor staat, los op en controleer.",
             oefeningen=[
                 ("open", "Een taxi vraagt 5 euro opstap en 2 euro per kilometer. Je betaalt "
                          "31 euro. Hoeveel kilometer heb je gereden?",
                  "5 + 2x = 31, dus 2x = 26 en x = 13 kilometer. Controle: 5 + 26 = 31.", 6),
                 ("open", "Abonnement A kost 15 euro plus 0,05 euro per minuut, B kost 5 euro plus "
                          "0,15 euro per minuut. Vanaf hoeveel minuten is A goedkoper?",
                  "15 + 0,05x = 5 + 0,15x geeft 10 = 0,10x, dus x = 100. Vanaf meer dan 100 minuten "
                  "is A goedkoper.", 6),
                 ("open", "De som van drie opeenvolgende even getallen is 66. Welke getallen zijn het?",
                  "x + (x + 2) + (x + 4) = 66, dus 3x = 60 en x = 20. De getallen zijn 20, 22 en 24.", 6),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij delen door een positief getal draait het ongelijkheidsteken om.", False),
                 ("waar", "Je mag beide leden van een gelijkheid met min 1 vermenigvuldigen.", True),
                 ("waar", "Je mag beide leden delen door een letter die nul kan zijn.", False),
                 ("waar", "Bij de kinetische energie is de energie recht evenredig met de snelheid.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-stelsels-en-tweedegraadsvergelijkingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stelsels en tweedegraadsvergelijkingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Stelsels oplossen",
             opdracht="Los op. Schrijf erbij welke methode je koos.",
             oefeningen=[
                 ("rij", [("x + y = 14 en x − y = 6", "x = 10, y = 4"),
                          ("y = 4x en x + y = 20", "x = 4, y = 16"),
                          ("2x + y = 11 en y = x + 2", "x = 3, y = 5"),
                          ("x + 2y = 13 en x − y = 1", "x = 5, y = 4")],
                  "Oplossing", WW),
             ]),
        dict(kop="Bepaald, strijdig of onbepaald?",
             opdracht="Los op en schrijf op welk soort stelsel het is.",
             oefeningen=[
                 ("open", "x + y = 5 en 2x + 2y = 10",
                  "Je krijgt 0 = 0: onbepaald, oneindig veel oplossingen. De rechten vallen samen.", 4),
                 ("open", "x + y = 5 en x + y = 9",
                  "Je krijgt 0 = 4: strijdig, geen oplossing. De rechten zijn evenwijdig.", 4),
                 ("open", "x + y = 5 en x − y = 1",
                  "Bepaald: x = 3 en y = 2. De rechten snijden in één punt.", 4),
             ]),
        dict(kop="Vraagstukken met twee onbekenden",
             opdracht="Noteer eerst waar elke letter voor staat.",
             oefeningen=[
                 ("open", "Drie broden en twee melk kosten 11 euro; één brood en twee melk kosten "
                          "7 euro. Wat kost een brood, en wat kost een pak melk?",
                  "3b + 2m = 11 en b + 2m = 7. Aftrekken geeft 2b = 4, dus b = 2 euro en m = 2,50 euro.", 6),
                 ("open", "Twee getallen zijn samen 40 en verschillen 12. Welke zijn het?",
                  "x + y = 40 en x − y = 12, dus 2x = 52, x = 26 en y = 14.", 5),
             ]),
        dict(kop="Onvolledige vierkantsvergelijkingen",
             opdracht="Los op zonder de formule.",
             oefeningen=[
                 ("rij", [("x² − 36 = 0", "6 en −6"), ("x² = 81", "9 en −9"),
                          ("x² − 7x = 0", "0 en 7"), ("2x² − 8 = 0", "2 en −2")],
                  "Oplossingen", WW),
             ]),
        dict(kop="De discriminant",
             opdracht="Bereken D en schrijf op hoeveel reële oplossingen er zijn.",
             oefeningen=[
                 ("rij", [("x² − 6x + 9 = 0", "D = 0, één oplossing"),
                          ("x² − 5x + 6 = 0", "D = 1, twee oplossingen"),
                          ("x² + 2x + 5 = 0", "D = −16, geen oplossing"),
                          ("2x² − 3x − 2 = 0", "D = 25, twee oplossingen")],
                  "D en aantal", WL),
             ]),
        dict(kop="Ontbinden en de nulwaarden",
             opdracht="Ontbind en schrijf de nulwaarden op.",
             oefeningen=[
                 ("rij", [("x² − 49", "(x + 7)(x − 7), nulwaarden 7 en −7"),
                          ("x² + 10x + 25", "(x + 5)², nulwaarde −5"),
                          ("x² − 7x + 12", "(x − 3)(x − 4), nulwaarden 3 en 4")],
                  "Ontbinding en nulwaarden", WL),
             ]),
        dict(kop="Tweedegraadsvraagstukken",
             opdracht="Stel eerst de vergelijking op, los dan op, en controleer bij het verhaal.",
             oefeningen=[
                 ("open", "Een rechthoek is 2 meter langer dan breed en heeft een oppervlakte van "
                          "48 m². Hoe breed is hij?",
                  "x(x + 2) = 48, dus x² + 2x − 48 = 0 met oplossingen 6 en −8. De breedte is 6 m; "
                  "min 8 valt weg want een breedte kan niet negatief zijn.", 6),
                 ("open", "Het product van twee opeenvolgende gehele getallen is 72. Welke zijn het?",
                  "x(x + 1) = 72 geeft x² + x − 72 = 0 met oplossingen 8 en −9. Dus 8 en 9, of −9 en −8.", 6),
             ]),
        dict(kop="Ongelijkheden van de tweede graad",
             opdracht="Schrijf de oplossingenverzameling als interval.",
             oefeningen=[
                 ("rij", [("x² < 16", "]−4, 4["), ("x² ≤ 25", "[−5, 5]"),
                          ("x² > 9", "]−∞, −3[ ∪ ]3, +∞[")],
                  "Interval", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De oplossing van een stelsel is een koppel getallen.", True),
                 ("waar", "Een strijdig stelsel hoort bij twee samenvallende rechten.", False),
                 ("waar", "Een vierkantsvergelijking heeft altijd twee reële oplossingen.", False),
                 ("waar", "x² + 4 is te ontbinden als (x + 2)(x − 2).", False),
                 ("waar", "Grafisch oplossen geeft altijd een exact antwoord.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-functies-en-de-rechte-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Functies en de rechte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Is het een functie?",
             opdracht="Duid aan. Denk aan de verticalelijntest.",
             oefeningen=[
                 ("kies", "een rechte met voorschrift y = 2x − 1", ["wel een functie", "geen functie"], 0),
                 ("kies", "de verticale rechte x = 3", ["wel een functie", "geen functie"], 1),
                 ("kies", "de parabool y = x²", ["wel een functie", "geen functie"], 0),
                 ("kies", "een cirkel rond de oorsprong", ["wel een functie", "geen functie"], 1),
             ]),
        dict(kop="Functiewaarden",
             opdracht="Voor f(x) = 5x − 3. Vul in.",
             oefeningen=[
                 ("rij", [("f(0)", "−3"), ("f(2)", "7"), ("f(−1)", "−8"),
                          ("de x waarvoor f(x) = 17", "4")],
                  "Antwoord", W),
             ]),
        dict(kop="Wat voor groei?",
             opdracht="Bekijk de verschillen en schrijf op of het lineair is of niet.",
             oefeningen=[
                 ("rij", [("1 → 5, 2 → 9, 3 → 13", "lineair, telkens +4"),
                          ("1 → 2, 2 → 8, 3 → 18", "niet lineair"),
                          ("1 → 10, 2 → 7, 3 → 4", "lineair, telkens −3")],
                  "Soort groei", WL),
             ]),
        dict(kop="De richtingscoëfficiënt",
             opdracht="Bereken de rico uit de twee punten.",
             oefeningen=[
                 ("rij", [("(0, 1) en (3, 10)", "3"), ("(2, 8) en (6, 4)", "−1"),
                          ("(1, 5) en (5, 5)", "0"), ("(−2, 0) en (2, 8)", "2")],
                  "rico", W),
             ]),
        dict(kop="De vergelijking opstellen",
             opdracht="Schrijf het voorschrift van de rechte.",
             oefeningen=[
                 ("rij", [("rico 5, door (0, −2)", "y = 5x − 2"),
                          ("rico 3, door (2, 10)", "y = 3x + 4"),
                          ("door (0, 4) en (2, 10)", "y = 3x + 4"),
                          ("door (1, 1) en (3, 7)", "y = 3x − 2")],
                  "Voorschrift", WW),
             ]),
        dict(kop="Snijpunten",
             opdracht="Bereken beide snijpunten met de assen.",
             oefeningen=[
                 ("rij", [("y = 2x − 10", "(5, 0) en (0, −10)"),
                          ("y = −x + 6", "(6, 0) en (0, 6)"),
                          ("y = 4x + 8", "(−2, 0) en (0, 8)")],
                  "Snijpunten", WL),
             ]),
        dict(kop="Lineair of recht evenredig?",
             opdracht="Duid aan wat het verband is.",
             oefeningen=[
                 ("kies", "y = 7x", ["recht evenredig", "wel lineair, niet recht evenredig"], 0),
                 ("kies", "y = 7x + 2", ["recht evenredig", "wel lineair, niet recht evenredig"], 1),
                 ("kies", "de kost van benzine aan 1,80 euro per liter",
                  ["recht evenredig", "wel lineair, niet recht evenredig"], 0),
                 ("kies", "een taxirit met 4 euro opstap en 1,50 euro per km",
                  ["recht evenredig", "wel lineair, niet recht evenredig"], 1),
             ]),
        dict(kop="Modellen opstellen",
             opdracht="Schrijf het voorschrift, met erbij wat a en b betekenen.",
             oefeningen=[
                 ("open", "Een wandelaar vertrekt op kilometerpaal 3 en loopt 5 km per uur.",
                  "s = 5t + 3. a = 5 is de snelheid, b = 3 de beginpositie.", 4),
                 ("open", "Een zaal huren kost 120 euro plus 3 euro per stoel.",
                  "k = 3n + 120. a = 3 is de prijs per stoel, b = 120 de vaste kost.", 4),
                 ("open", "Een bestelwagen van 30 000 euro wordt in 12 jaar lineair tot nul "
                          "afgeschreven. Schrijf het voorschrift en de waarde na 5 jaar.",
                  "w = 30000 − 2500t. Na 5 jaar: 30000 − 12500 = 17 500 euro.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij een functie mogen bij dezelfde x twee verschillende y-waarden horen.", False),
                 ("waar", "Een rechte met rico nul loopt horizontaal.", True),
                 ("waar", "Evenwijdige rechten hebben dezelfde richtingscoëfficiënt.", True),
                 ("waar", "Het domein van f(x) = 1/x bevat ook het getal nul.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-de-parabool-transformaties-en-functiekenmerken-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De parabool, transformaties en functiekenmerken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Opening en top",
             opdracht="Schrijf op of de parabool naar boven of naar beneden opent, en waar de top ligt.",
             oefeningen=[
                 ("rij", [("y = (x − 4)² + 1", "naar boven, top (4, 1)"),
                          ("y = −(x + 2)² + 5", "naar beneden, top (−2, 5)"),
                          ("y = 3(x − 1)² − 7", "naar boven, top (1, −7)"),
                          ("y = −2(x + 3)²", "naar beneden, top (−3, 0)")],
                  "Opening en top", WL),
             ]),
        dict(kop="Nulwaarden",
             opdracht="Bereken de nulwaarden, of schrijf op dat er geen zijn.",
             oefeningen=[
                 ("rij", [("f(x) = x² − 25", "5 en −5"), ("f(x) = x² + 1", "geen"),
                          ("f(x) = (x − 3)²", "3, dubbel"), ("f(x) = x² − 4x", "0 en 4")],
                  "Nulwaarden", WW),
             ]),
        dict(kop="De symmetrieas",
             opdracht="Schrijf de vergelijking van de symmetrieas.",
             oefeningen=[
                 ("rij", [("nulwaarden −1 en 7", "x = 3"), ("nulwaarden 2 en 10", "x = 6"),
                          ("top (−5, 2)", "x = −5"), ("nulwaarden −4 en 4", "x = 0")],
                  "Symmetrieas", W),
             ]),
        dict(kop="Wat doet de transformatie?",
             opdracht="Vertrek van y = x² en schrijf op wat er met de grafiek gebeurt.",
             oefeningen=[
                 ("rij", [("y = x² + 4", "vier omhoog"), ("y = (x − 6)²", "zes naar rechts"),
                          ("y = (x + 1)²", "één naar links"), ("y = −x²", "gespiegeld om de horizontale as")],
                  "Wat gebeurt er?", WL),
                 ("rij", [("y = 4x²", "smaller, verticaal uitgerekt"),
                          ("y = 0,25x²", "breder, samengedrukt")],
                  "Wat gebeurt er?", WL),
             ]),
        dict(kop="Domein en bereik",
             opdracht="Schrijf domein en bereik op.",
             oefeningen=[
                 ("tabel", ["functie", "domein", "bereik"],
                  [["f(x) = x²", None, None], ["f(x) = (x − 2)² + 3", None, None],
                   ["f(x) = −x² + 1", None, None], ["f(x) = 1/x", None, None]],
                  "x²: ℝ en y ≥ 0 · (x−2)²+3: ℝ en y ≥ 3 · −x²+1: ℝ en y ≤ 1 · "
                  "1/x: ℝ zonder 0, en y ≠ 0", "170px"),
             ]),
        dict(kop="Stijgen en dalen",
             opdracht="Schrijf op waar de functie daalt en waar ze stijgt.",
             oefeningen=[
                 ("rij", [("f(x) = x² − 6x", "daalt links van 3, stijgt rechts van 3"),
                          ("f(x) = −x² + 8x", "stijgt links van 4, daalt rechts van 4")],
                  "Verloop", WL),
             ]),
        dict(kop="Welke vorm gebruik je?",
             opdracht="Schrijf op welke vorm van het voorschrift je het snelst het gevraagde geeft.",
             oefeningen=[
                 ("rij", [("je zoekt de nulwaarden", "de productvorm a(x − x₁)(x − x₂)"),
                          ("je zoekt de top", "de topvorm a(x − p)² + q"),
                          ("je zoekt het snijpunt met de y-as", "de vorm ax² + bx + c")],
                  "Welke vorm?", WL),
             ]),
        dict(kop="Voorschrift opstellen",
             opdracht="Schrijf een voorschrift dat aan de voorwaarde voldoet.",
             oefeningen=[
                 ("rij", [("nulwaarden 3 en 8", "f(x) = (x − 3)(x − 8)"),
                          ("nulwaarden −2 en 5", "f(x) = (x + 2)(x − 5)"),
                          ("top (2, −4), opent naar boven", "f(x) = (x − 2)² − 4")],
                  "Voorschrift", WL),
             ]),
        dict(kop="De hyperbool",
             opdracht="Over f(x) = 12/x.",
             oefeningen=[
                 ("rij", [("f(3)", "4"), ("f(−6)", "−2"), ("de x waarvoor f(x) = 2", "6")],
                  "Antwoord", W),
                 ("open", "Waarom heeft deze functie geen nulwaarde, en wat doet de grafiek bij de "
                          "verticale as?",
                  "Een breuk met teller 12 wordt nooit nul. De grafiek nadert de verticale as maar "
                  "raakt hem nooit, want x = 0 hoort niet bij het domein.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Elke parabool snijdt de x-as in twee punten.", False),
                 ("waar", "Een parabool die naar boven opent heeft een minimum maar geen maximum.", True),
                 ("waar", "Het tekenverloop toont waar de functie stijgt en daalt.", False),
                 ("waar", "Uit de grafiek van een parabool kan je haar voorschrift afleiden.", True),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-telproblemen-met-boom-en-venndiagram-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Telproblemen met boom- en venndiagram",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De productregel",
             opdracht="Reken uit hoeveel mogelijkheden er zijn.",
             oefeningen=[
                 ("rij", [("3 jassen en 5 mutsen", "15"), ("2 soepen, 4 hoofdgerechten, 3 desserts", "24"),
                          ("een code van 4 cijfers van 0 tot 9", "10 000"),
                          ("vier keer met een munt gooien", "16")],
                  "Aantal", W),
             ]),
        dict(kop="Met of zonder terugleggen",
             opdracht="Reken uit en schrijf erbij of er teruggelegd wordt.",
             oefeningen=[
                 ("rij", [("uit 6 lopers de eerste drie plaatsen", "120, zonder terugleggen"),
                          ("drie keer een cijfer van 1 tot 6 kiezen, herhaling mag", "216, met terugleggen"),
                          ("uit 5 kaarten er 2 na elkaar trekken zonder terugleggen", "20, zonder terugleggen")],
                  "Aantal en soort", WL),
             ]),
        dict(kop="Een boomdiagram tekenen",
             opdracht="Teken het diagram in de ruimte hiernaast en tel daarna de paden.",
             oefeningen=[
                 ("open", "Je kiest eerst een voorgerecht uit 2 en daarna een hoofdgerecht uit 3. "
                          "Teken het boomdiagram en tel de paden.",
                  "Uit het beginpunt vertrekken 2 takken, elk splitst in 3: samen 6 paden.", 8),
             ]),
        dict(kop="De somregel",
             opdracht="Bereken hoeveel er minstens aan één voorwaarde voldoen.",
             oefeningen=[
                 ("rij", [("20 leerlingen, 12 voetbal, 9 tennis, 4 allebei", "17"),
                          ("50 mensen, 30 koffie, 25 thee, 10 allebei", "45"),
                          ("36 leerlingen, 20 Spaans, 16 Duits, 5 allebei", "31")],
                  "Minstens één", W),
             ]),
        dict(kop="De complementregel",
             opdracht="Bereken hoeveel er aan geen van beide voldoen.",
             oefeningen=[
                 ("rij", [("20 leerlingen, 17 doen minstens één sport", "3"),
                          ("50 mensen, 45 drinken minstens één van beide", "5"),
                          ("36 leerlingen, 31 volgen minstens één taal", "5")],
                  "Geen van beide", W),
             ]),
        dict(kop="Het venndiagram invullen",
             opdracht="Van 28 leerlingen spelen er 15 voetbal, 13 basket en 6 allebei. Vul in.",
             oefeningen=[
                 ("tabel", ["vakje", "aantal"],
                  [["enkel voetbal", None], ["allebei", None], ["enkel basket", None],
                   ["geen van beide", None]],
                  "enkel voetbal 9 · allebei 6 · enkel basket 7 · geen van beide 6", "150px"),
             ]),
        dict(kop="Slim tellen",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Hoeveel getallen van 1 tot en met 30 zijn deelbaar door 2 of door 5?",
                  "15 door 2, 6 door 5, 3 door allebei (10, 20, 30): 15 + 6 − 3 = 18.", 5),
                 ("open", "Je gooit drie keer met een munt. Hoeveel uitkomsten hebben minstens één "
                          "kop? Tel liever het tegendeel.",
                  "Er zijn 8 uitkomsten; precies 1 heeft geen enkele kop. Dus 8 − 1 = 7.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij twee overlappende groepen mag je de aantallen gewoon optellen.", False),
                 ("waar", "Bij disjuncte groepen is de doorsnede leeg.", True),
                 ("waar", "Een boomdiagram toont elke uitkomst precies één keer.", True),
                 ("waar", "Een venndiagram is het gereedschap voor opeenvolgende keuzes.", False),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-statistiek-voorstellingen-centrum-en-spreiding-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Statistiek: voorstellingen, centrum en spreiding",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort gegevens?",
             opdracht="Schrijf: numeriek, categorisch geordend of categorisch niet-geordend.",
             oefeningen=[
                 ("rij", [("het gewicht van elke schooltas in kilogram", "numeriek"),
                          ("de kleur van de fietsen op de speelplaats", "categorisch niet-geordend"),
                          ("een beoordeling als zwak, voldoende of goed", "categorisch geordend"),
                          ("de gemeente waar elke leerling woont", "categorisch niet-geordend")],
                  "Welke soort?", WL),
             ]),
        dict(kop="De frequentietabel aanvullen",
             opdracht="Een klas van 20 leerlingen. Vul de relatieve frequenties in, in procent.",
             oefeningen=[
                 ("tabel", ["vervoer", "absolute frequentie", "relatieve frequentie"],
                  [["fiets", "8", None], ["bus", "6", None], ["te voet", "4", None], ["auto", "2", None]],
                  "fiets 40 % · bus 30 % · te voet 20 % · auto 10 %, samen 100 %", "170px"),
             ]),
        dict(kop="Klassenmiddens",
             opdracht="Bereken het klassenmidden.",
             oefeningen=[
                 ("rij", [("van 0 tot 10", "5"), ("van 30 tot 40", "35"),
                          ("van 150 tot 160", "155"), ("van 12 tot 18", "15")],
                  "Klassenmidden", W),
             ]),
        dict(kop="Welk diagram?",
             opdracht="Schrijf welk diagram het best past.",
             oefeningen=[
                 ("rij", [("de temperatuur per maand over een jaar", "lijndiagram"),
                          ("het aandeel van elk vervoermiddel in het geheel", "cirkeldiagram"),
                          ("de lengtes van 80 leerlingen in klassen van 5 cm", "histogram"),
                          ("de vijf kwartielwaarden van een reeks", "boxplot")],
                  "Diagram", WW),
             ]),
        dict(kop="Centrummaten berekenen",
             opdracht="De reeks is 4, 7, 7, 9, 13, 20. Bereken.",
             oefeningen=[
                 ("rij", [("het rekenkundig gemiddelde", "10"), ("de mediaan", "8"),
                          ("de modus", "7"), ("de variatiebreedte", "16")],
                  "Antwoord", W),
             ]),
        dict(kop="Nog een reeks",
             opdracht="De reeks is 3, 5, 8, 8, 11. Bereken.",
             oefeningen=[
                 ("rij", [("het gemiddelde", "7"), ("de mediaan", "8"),
                          ("de modus", "8"), ("de variatiebreedte", "8")],
                  "Antwoord", W),
             ]),
        dict(kop="Kwartielen en boxplot",
             opdracht="De gerangschikte reeks is 2, 4, 6, 8, 10, 12, 14, 16. Bereken.",
             oefeningen=[
                 ("rij", [("de mediaan", "9"), ("het eerste kwartiel", "5"),
                          ("het derde kwartiel", "13"), ("de interkwartielafstand", "8")],
                  "Antwoord", W),
             ]),
        dict(kop="Gemiddelde of mediaan?",
             opdracht="Schrijf welke maat het eerlijkste beeld geeft, en waarom.",
             oefeningen=[
                 ("open", "De lonen in een klein bedrijf: 2000, 2100, 2200, 2300 en 15 000 euro.",
                  "De mediaan (2200), want dat ene hoge loon trekt het gemiddelde tot 4720 euro "
                  "en dat verdient niemand.", 4),
                 ("open", "De punten van tien leerlingen die allemaal tussen 12 en 16 liggen.",
                  "Het gemiddelde mag: er zijn geen uitschieters, dus gemiddelde en mediaan liggen "
                  "dicht bij elkaar.", 4),
             ]),
        dict(kop="Spreiding vergelijken",
             opdracht="Schrijf je antwoord in één of twee zinnen.",
             oefeningen=[
                 ("open", "Klas A en klas B hebben allebei een gemiddelde van 13, maar A heeft een "
                          "standaardafwijking van 1 en B van 4. Wat betekent dat?",
                  "In A liggen de punten dicht bij 13, in B liggen ze veel verder uit elkaar: daar "
                  "zitten zowel hoge als lage punten.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij een histogram raken de staven elkaar.", True),
                 ("waar", "Een reeks kan twee modi hebben.", True),
                 ("waar", "De interkwartielafstand is gevoelig voor één uitschieter.", False),
                 ("waar", "Alle relatieve frequenties samen geven 100 procent.", True),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-misleiding-met-cijfers-en-verbanden-in-een-puntenwolk-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Misleiding met cijfers, en verbanden in een puntenwolk",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Procent of procentpunt?",
             opdracht="Vul allebei de getallen in.",
             oefeningen=[
                 ("tabel", ["van", "naar", "procentpunt", "procent"],
                  [["10 %", "15 %", None, None], ["40 %", "50 %", None, None],
                   ["20 %", "16 %", None, None]],
                  "10→15: 5 procentpunt, 50 % groei · 40→50: 10 procentpunt, 25 % groei · "
                  "20→16: 4 procentpunt minder, 20 % daling", "120px"),
             ]),
        dict(kop="Rekenen met kortingen",
             opdracht="Reken uit. Let op dat procenten van verschillende bedragen niet optellen.",
             oefeningen=[
                 ("rij", [("200 euro, +10 %, daarna −10 %", "198 euro"),
                          ("50 euro, +20 %, daarna −20 %", "48 euro"),
                          ("80 euro, −25 %, daarna −20 %", "48 euro")],
                  "Eindprijs", WW),
             ]),
        dict(kop="Waar zit de misleiding?",
             opdracht="Schrijf in één zin wat er mis is met de voorstelling.",
             oefeningen=[
                 ("open", "Een staafdiagram waarvan de verticale as van 95 tot 100 loopt.",
                  "De as begint niet bij nul, dus een verschil van één procentpunt lijkt enorm.", 3),
                 ("open", "Een as met de stappen 0, 1, 2, 5, 10, 50 op gelijke afstanden.",
                  "De as is foutief geijkt: gelijke afstanden tonen ongelijke sprongen, dus een "
                  "kromme kan recht lijken.", 3),
                 ("open", "Een verkoopgrafiek van 2020 tot 2024 waarin 2022 ontbreekt.",
                  "Er zijn gegevens weggelaten; net dat jaar kan de getoonde stijging tegenspreken.", 3),
                 ("open", "Twee blokken in perspectief waarvan de ene twee keer zo hoog is.",
                  "Het oog vergelijkt volumes in plaats van hoogtes, dus het verschil lijkt veel "
                  "groter dan twee keer.", 3),
             ]),
        dict(kop="Welke vraag stel je?",
             opdracht="Schrijf de eerste vraag op die je bij deze bewering stelt.",
             oefeningen=[
                 ("open", "Negen op de tien gebruikers zijn tevreden.",
                  "Hoeveel gebruikers zijn er bevraagd, en door wie? Tien zelfgekozen mensen zeggen "
                  "iets anders dan duizend willekeurige.", 3),
                 ("open", "De verkoop steeg met 50 procent.",
                  "Van hoeveel naar hoeveel? Van 2 naar 3 is ook 50 procent.", 3),
             ]),
        dict(kop="De correlatiecoëfficiënt",
             opdracht="Schrijf op welke waarde het best past: ongeveer 1, 0,8, 0, −0,8 of −1.",
             oefeningen=[
                 ("rij", [("alle punten precies op een stijgende rechte", "1"),
                          ("een wolk zonder duidelijke richting", "0"),
                          ("een duidelijk dalende wolk met wat spreiding", "−0,8"),
                          ("alle punten precies op een dalende rechte", "−1")],
                  "Waarde", W),
             ]),
        dict(kop="Correlatie of oorzaak?",
             opdracht="Schrijf op wat de derde factor of de fout in de redenering is.",
             oefeningen=[
                 ("open", "Kinderen met grotere schoenen lezen beter.",
                  "De derde factor is de leeftijd: oudere kinderen hebben grotere voeten én lezen "
                  "beter.", 4),
                 ("open", "Gemeenten met meer brandweerlieden hebben meer schade door brand.",
                  "De derde factor is de grootte van de gemeente. Grote steden hebben meer van allebei.", 4),
                 ("open", "Mensen die ontbijten wegen minder, dus ontbijten maakt slank.",
                  "Correlatie is geen oorzaak. Wie ontbijt, leeft vaak ook verder gezonder; het "
                  "verband kan ook omgekeerd lopen.", 4),
             ]),
        dict(kop="Voorzichtig formuleren",
             opdracht="Herschrijf de uitspraak zodat ze enkel beschrijft wat er gemeten is.",
             oefeningen=[
                 ("open", "Meer slapen zorgt voor betere punten.",
                  "In deze groep haalden leerlingen die meer sliepen, gemiddeld hogere punten.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een grafiek kan kloppen en toch een verkeerde indruk geven.", True),
                 ("waar", "Procent en procentpunt betekenen hetzelfde.", False),
                 ("waar", "Een trendlijn gaat altijd door alle punten van de wolk.", False),
                 ("waar", "Eén uitschieter kan de trendlijn flink verschuiven.", True),
                 ("waar", "Ver buiten het gemeten gebied voorspellen is riskant.", True),
             ]),
    ],
)
