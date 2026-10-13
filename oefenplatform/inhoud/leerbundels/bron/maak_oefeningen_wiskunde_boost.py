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
                 ("rij", [(r"je noemt het aantal kilometer \(x\) en schrijft de kost als \(0{,}30x + 15\)",
                           "mathematiseren"),
                          (r"je rekent \(7{,}3\) uit en antwoordt dat er \(8\) bussen nodig zijn",
                           "demathematiseren"),
                          ("je tekent de ladder als een rechthoekige driehoek", "mathematiseren"),
                          (r"je rondt \(4{,}7\) meter af tot een ladder van \(5\) meter", "demathematiseren")],
                  "Welke stap?", WW),
             ]),
        dict(kop="Vraagstuk of probleem?",
             opdracht="Schrijf vraagstuk of probleem.",
             oefeningen=[
                 ("rij", [("een oefening op de oppervlakte van een rechthoek", "vraagstuk"),
                          ("een opgave waarvoor je zowel een stelsel als Pythagoras nodig hebt", "probleem"),
                          (r"\(3x + 5 = 20\) oplossen", "vraagstuk"),
                          ("hoeveel verf, hoeveel behang en hoeveel geld je nodig hebt voor een kamer",
                           "probleem")],
                  "Welk soort?", WW),
             ]),
        dict(kop="Welke heuristiek?",
             opdracht="Schrijf bij elke aanpak welke heuristiek uit de lijst van de fiche je gebruikt.",
             oefeningen=[
                 ("rij", [(r"je noemt de leeftijd van de jongste broer \(x\)", "variabelen invoeren"),
                          ("je knipt 'hoeveel kost een schoolreis' op in bus, inkom en eten",
                           "opsplitsen in deelproblemen"),
                          ("je schrijft alle vier de kleuren met alle drie de maten uit",
                           "alle mogelijkheden opschrijven"),
                          ("je berekent maar één helft van de figuur en verdubbelt",
                           "gebruik maken van symmetrie")],
                  "Welke heuristiek?", WL),
             ]),
        dict(kop="Nog drie heuristieken",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("rij", [("je vertrekt van de eindprijs en rekent terug naar de beginprijs", "terugrekenen"),
                          (r"je bekijkt de verschillen tussen \(3, 8, 15, 24\)",
                           "patronen en regelmaat ontdekken"),
                          (r"je probeert \(10\), ziet dat het te groot is, en probeert \(8\)",
                           "schatten, slim gissen, testen en controleren")],
                  "Welke heuristiek?", WL),
             ]),
        dict(kop="De vier stappen op een rij",
             opdracht="Vul de vier stappen in, in de juiste volgorde.",
             oefeningen=[
                 ("tabel", ["stap", "naam"],
                  [["1", None], ["2", None], ["3", None], ["4", None]],
                  "1 begrijp het probleem · 2 maak een plan · 3 voer het plan uit · 4 reflecteer", "230px"),
             ]),
        dict(kop="Bij welke stap hoort dit?",
             opdracht="Schrijf het nummer van de stap (1 tot 4).",
             oefeningen=[
                 ("rij", [("onderstrepen wat gegeven is en wat gevraagd wordt", "1"),
                          ("nagaan of de eenheid van je antwoord klopt", "4"),
                          ("beslissen dat je met de tangens gaat werken", "2"),
                          ("je tussenstappen één per regel opschrijven", "3")],
                  "Stap", W),
             ]),
        dict(kop="Reflecteren",
             opdracht="Bij elke uitkomst: schrijf op waarom ze niet kan kloppen, en wat er waarschijnlijk misging.",
             oefeningen=[
                 ("open", r"Een zwembad van \(25\) m op \(10\) m op \(2\) m zou \(500\) liter water bevatten.",
                  r"\(500\) liter is een halve kubieke meter, en het bad is \(500\) m\(^{3}\). De eenheid "
                  r"ging mis: \(500\) m\(^{3}\) is \(500\,000\) liter.", 4),
                 ("open", r"Een auto legt \(90\) km af in \(45\) minuten; iemand berekent \(2\) km/u.",
                  r"\(45\) minuten is \(0{,}75\) uur, en \(90 : 0{,}75 = 120\) km/u. Er is gedeeld door "
                  r"\(45\) in plaats van door \(0{,}75\).", 4),
                 ("open", r"De oppervlakte van een tuin komt uit op \(-12\) m\(^{2}\).",
                  "Een oppervlakte kan niet negatief zijn. Waarschijnlijk is er een lengte afgetrokken "
                  "die er bij moest, of zijn twee maten verwisseld.", 4),
             ]),
        dict(kop="Schatten eerst",
             opdracht="Schat eerst met ronde getallen, schrijf je schatting op, en reken daarna precies.",
             oefeningen=[
                 ("rij", [(r"schatting van \(49 \cdot 31\)", r"ongeveer \(1500\)"),
                          (r"exact \(49 \cdot 31\)", r"\(1519\)"),
                          (r"schatting van \(198 : 4\)", r"ongeveer \(50\)"),
                          (r"exact \(198 : 4\)", r"\(49{,}5\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Nog twee onmogelijke uitkomsten",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("open", r"Een klas van \(24\) leerlingen zou gemiddeld \(0{,}3\) broer of zus hebben, "
                          r"terwijl niemand enig kind is.",
                  r"Als niemand enig kind is, heeft elke leerling er minstens één, dus het gemiddelde moet "
                  r"minstens \(1\) zijn. Waarschijnlijk is er gedeeld door het verkeerde aantal.", 4),
                 ("open", r"Een korting van \(30\%\) op \(80\) euro zou \(104\) euro opleveren.",
                  r"Na een korting betaal je minder, niet meer. Hier is \(80 \cdot 1{,}3\) gerekend in "
                  r"plaats van \(80 \cdot 0{,}7 = 56\) euro.", 4),
             ]),
        dict(kop="Nog vier schattingen",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("rij", [(r"schatting van \(19 \cdot 21\)", r"ongeveer \(400\)"),
                          (r"exact \(19 \cdot 21\)", r"\(399\)"),
                          (r"schatting van \(802 : 4\)", r"ongeveer \(200\)"),
                          (r"exact \(802 : 4\)", r"\(200{,}5\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Zelf oplossen",
             opdracht="Werk met de vier stappen. Schrijf minstens je plan en je controle op.",
             oefeningen=[
                 ("open", r"Na \(25\%\) korting betaal je \(60\) euro. Wat was de oude prijs?",
                  r"\(60\) euro is \(75\%\) van de oude prijs, dus de oude prijs is \(60 : 0{,}75 = 80\) "
                  r"euro. Controle: \(25\%\) van \(80\) is \(20\), en \(80 - 20 = 60\).", 6),
                 ("open", r"Welk getal volgt in de rij \(3, 8, 15, 24, 35\)? Leg uit hoe je het vindt.",
                  r"De verschillen zijn \(5, 7, 9, 11\), dus het volgende verschil is \(13\) en het getal "
                  r"is \(48\).", 5),
             ]),
        dict(kop="Schrijf de formule op",
             opdracht="Mathematiseer: zet de zin om in een formule. Schrijf erbij waar je letter voor staat.",
             oefeningen=[
                 ("rij", [("een taxi vraagt 5 euro opstap en 2 euro per kilometer",
                           r"\(k = 5 + 2x\), met \(x\) het aantal kilometer"),
                          ("de omtrek van een rechthoek die 3 cm langer is dan breed",
                           r"\(P = 2x + 2(x + 3) = 4x + 6\)"),
                          ("de helft van een getal, verminderd met zeven",
                           r"\(\tfrac{x}{2} - 7\)")],
                  "Formule", WL),
             ]),
        dict(kop="Nog twee opgaven",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("open", r"Een ladder van \(5\) m staat met de voet \(1{,}5\) m van de muur. Hoe hoog "
                          r"reikt hij? Rond af op een centimeter.",
                  r"Pythagoras: \(h = \sqrt{5^{2} - 1{,}5^{2}} = \sqrt{22{,}75} \approx 4{,}77\) m. "
                  r"Controle: \(4{,}77\) is net iets minder dan \(5\), zoals het hoort.", 6),
                 ("open", "Een weekje kamperen kost 120 euro reis, 18 euro per nacht voor de plaats en "
                          "25 euro per dag voor eten. Hoeveel kost zeven nachten?",
                  r"Opsplitsen in deelproblemen: \(120 + 7 \cdot 18 + 7 \cdot 25 = 120 + 126 + 175 = 421\) "
                  r"euro.", 6),
             ]),
        dict(kop="De vier vaardigheden",
             opdracht="Vul in welke vaardigheid de fiche bedoelt.",
             oefeningen=[
                 ("tabel", ["Wat je doet", "Welke vaardigheid?"],
                  [["een grafiek begrijpen en beschrijven", None],
                   ["vlot hoofdrekenen", None],
                   ["een hoek meten met een geodriehoek", None],
                   ["een rekenapp gebruiken bij een berekening", None]],
                  "taalvaardigheid · rekenvaardigheid · meet- en tekenvaardigheid · ICT-vaardigheid", "210px"),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een schets maken telt als een volwaardige oplossingsstrategie.", True),
                 ("waar", "Een goede schatting vervangt de exacte berekening.", False),
                 ("waar", "Eén tegenvoorbeeld volstaat om een uitspraak te weerleggen.", True),
                 ("waar", "Drie voorbeelden die kloppen, bewijzen dat een eigenschap altijd geldt.", False),
                 ("waar", "Bij een probleem mag je leerstof uit meerdere hoofdstukken combineren.", True),
                 ("waar", "Op het examen komen enkel opgaven met context voor.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom hoort reflecteren bij het oplossen en niet erna?",
                  "Omdat je dan nog merkt dat je uitkomst niet kan kloppen, en omdat je ziet of je aanpak "
                  "ook elders bruikbaar is. Wie pas achteraf reflecteert, levert een fout antwoord in.", 5),
                 ("open", "Waarom vraagt de fiche dat je je tussenstappen verantwoordt?",
                  "Omdat een lezer dan kan volgen welke eigenschap je toepast en waar het misloopt. Een "
                  "antwoord zonder redenering is niet na te kijken, ook niet door jezelf.", 5),
             ]),
        dict(kop="Doordenkers",
             opdracht="Neem je tijd.",
             oefeningen=[
                 ("open", r"Iemand beweert: 'elk oneven getal in het kwadraat is oneven'. Hoe toon je aan "
                          r"dat dit waar is, en waarom volstaan drie voorbeelden niet?",
                  r"Voorbeelden illustreren maar bewijzen niet. Een redenering wel: een oneven getal is "
                  r"\(2n + 1\), en \((2n+1)^{2} = 4n^{2} + 4n + 1\), dus opnieuw één meer dan een viervoud, "
                  r"en dat is oneven.", 6),
                 ("open", r"Iemand beweert: 'als je een getal kwadrateert, wordt het groter'. Geef een "
                          r"tegenvoorbeeld en leg uit waarom één genoeg is.",
                  r"Neem \(0{,}5\): \(0{,}5^{2} = 0{,}25\), kleiner dus. Eén geval waarin het niet opgaat, "
                  r"breekt de uitspraak, want ze beweerde dat het altijd zo is.", 6),
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
             opdracht="\\(p\\) is 'het sneeuwt' en \\(q\\) is 'de school is dicht'. Schrijf elke zin in symbolen.",
             oefeningen=[
                 ("rij", [("het sneeuwt en de school is dicht", "\\(p \\land q\\)"),
                          ("het sneeuwt niet", "\\(\\neg p\\)"),
                          ("als het sneeuwt, is de school dicht", "\\(p \\Rightarrow q\\)"),
                          ("het sneeuwt of de school is dicht", "\\(p \\lor q\\)")],
                  "In symbolen", W),
                 ("rij", [("het is niet zo dat het sneeuwt en de school dicht is", "\\(\\neg(p \\land q)\\)"),
                          ("de school is dicht als en slechts als het sneeuwt", "\\(q \\Leftrightarrow p\\)")],
                  "In symbolen", WW),
             ]),
        dict(kop="De waarheidstabel invullen",
             opdracht="Vul 1 voor waar en 0 voor vals in.",
             oefeningen=[
                 ("tabel", ["\\(p\\)", "\\(q\\)", "\\(p \\land q\\)", "\\(p \\lor q\\)", "\\(p \\Rightarrow q\\)"],
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
                 ("rij", [("\\(p \\lor \\neg p\\)", "tautologie"), ("\\(p \\land \\neg p\\)", "contradictie"),
                          ("\\(p \\Rightarrow p\\)", "tautologie"), ("\\(p \\land q\\)", "geen van beide")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Kwantoren en negatie",
             opdracht="Schrijf de negatie van elke uitspraak in gewone taal.",
             oefeningen=[
                 ("rij", [("alle zwanen zijn wit", "minstens één zwaan is niet wit"),
                          ("er bestaat een even priemgetal", "geen enkel priemgetal is even"),
                          ("alle leerlingen waren aanwezig", "minstens één leerling was afwezig")],
                  "De negatie", WL),
                 ("kort", "Welk symbool betekent 'voor alle'?", "\\(\\forall\\)", W),
                 ("kort", "Welk symbool betekent 'er bestaat'?", "\\(\\exists\\)", W),
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
                 ("kort", "De wortel van een som is de som van de wortels.", r"\(\sqrt{9 + 16} = 5\), niet \(7\)", WL),
             ]),
        dict(kop="Welke poort?",
             opdracht="Schrijf bij elke schakeling welke poort past.",
             oefeningen=[
                 ("rij", [("de motor start alleen als de sleutel én de rem ingedrukt zijn", "een EN-poort"),
                          ("het licht gaat aan bij beweging of bij een druk op de knop", "een OF-poort"),
                          ("het signaal wordt omgekeerd van 0 naar 1", "een NIET-poort")],
                  "Welke poort?", WW),
             ]),
        dict(kop="Nog vier in symbolen",
             opdracht=r"Zelfde \(p\) en \(q\). Schrijf elke zin in symbolen.",
             oefeningen=[
                 ("rij", [("het sneeuwt niet en de school is niet dicht", r"\(\neg p \land \neg q\)"),
                          ("het is niet zo dat het sneeuwt of dat de school dicht is",
                           r"\(\neg(p \lor q)\)"),
                          ("als de school niet dicht is, sneeuwt het niet", r"\(\neg q \Rightarrow \neg p\)"),
                          ("als de school dicht is, sneeuwt het", r"\(q \Rightarrow p\)")],
                  "In symbolen", WW),
             ]),
        dict(kop="Zelfde waarheidswaarde?",
             opdracht=r"Heeft de vorm altijd dezelfde waarheidswaarde als \(p \Rightarrow q\)? Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [(r"\(q \Rightarrow p\)", "nee, dat is het omgekeerde"),
                          (r"\(\neg p \Rightarrow \neg q\)", "nee, dat is het tegengestelde"),
                          (r"\(\neg q \Rightarrow \neg p\)", "ja, dat is de contrapositie")],
                  "Ja of nee?", WL),
             ]),
        dict(kop="De wetten van De Morgan",
             opdracht="Schrijf de gelijkwaardige vorm, zonder haakjes rond de negatie.",
             oefeningen=[
                 ("rij", [(r"\(\neg(p \land q)\)", r"\(\neg p \lor \neg q\)"),
                          (r"\(\neg(p \lor q)\)", r"\(\neg p \land \neg q\)")],
                  "Gelijkwaardig met", WW),
             ]),
        dict(kop="De omgekeerde poorten",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", r"Welke poort voert \(\neg(p \land q)\) uit?",
                  ["een NEN-poort", "een NOF-poort", "een OF-poort", "twee NIET-poorten"], 0),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom is \(p \Rightarrow q\) waar zodra \(p\) vals is?",
                  r"Een implicatie is een belofte over de gevallen waarin \(p\) klopt. Is \(p\) vals, dan "
                  r"is er niets beloofd en kan de belofte niet gebroken zijn, dus geldt ze als waar.", 5),
                 ("open", r"Waarom volstaat één tegenvoorbeeld om een uitspraak met \(\forall\) te "
                          r"weerleggen, terwijl honderd voorbeelden ze niet bewijzen?",
                  r"\(\forall\) beweert dat het in élk geval opgaat, dus één geval waarin het misgaat maakt "
                  r"de uitspraak vals. Voorbeelden tonen alleen de gevallen die je zelf koos; de gevallen "
                  r"die je niet bekeek, kunnen nog altijd tegenspreken.", 6),
             ]),
        dict(kop="Doordenkers",
             opdracht="Neem je tijd.",
             oefeningen=[
                 ("open", r"Iemand zegt dat de ontkenning van 'alle leerlingen slaagden' gelijk is aan 'geen "
                          r"enkele leerling slaagde'. Wat is er mis, en wat is de juiste ontkenning?",
                  r"De negatie van \(\forall\) is \(\exists\) met een negatie erachter, niet \(\forall\) met "
                  r"een negatie. De juiste ontkenning is: minstens één leerling slaagde niet.", 5),
                 ("open", r"Vul de waarheidstabel van \(\neg(p \land q)\) en van \(\neg p \land \neg q\) in "
                          r"en zeg in welke rij ze verschillen.",
                  r"Ze verschillen in de rijen waar precies één van de twee waar is. Is \(p\) waar en \(q\) "
                  r"vals, dan is \(\neg(p \land q)\) waar (niet allebei) maar \(\neg p \land \neg q\) vals "
                  r"(want \(p\) is wel waar).", 6),
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
             opdracht=r"Schrijf de kleinste verzameling waartoe het getal behoort: \(\mathbb{N}\), \(\mathbb{Z}\), \(\mathbb{Q}\) of \(\mathbb{R}\).",
             oefeningen=[
                 ("rij", [(r"\(12\)", r"\(\mathbb{N}\)"), (r"\(-5\)", r"\(\mathbb{Z}\)"),
                          (r"\(0{,}75\)", r"\(\mathbb{Q}\)"), (r"\(\sqrt{7}\)", r"\(\mathbb{R}\)")],
                  "Verzameling", W),
                 ("rij", [(r"\(\pi\)", r"\(\mathbb{R}\)"), (r"\(\tfrac{22}{7}\)", r"\(\mathbb{Q}\)"),
                          (r"\(\sqrt{49}\)", r"\(\mathbb{N}\)"), (r"\(-0{,}2\)", r"\(\mathbb{Q}\)")],
                  "Verzameling", W),
             ]),
        dict(kop="Rationaal of irrationaal?",
             opdracht="Duid aan wat het is.",
             oefeningen=[
                 ("kies", r"\(0{,}272727\ldots\) met een eindeloos herhalend \(27\)", ["rationaal", "irrationaal"], 0),
                 ("kies", r"\(\sqrt{8}\)", ["rationaal", "irrationaal"], 1),
                 ("kies", r"\(\sqrt{64}\)", ["rationaal", "irrationaal"], 0),
                 ("kies", r"\(3{,}14159265358979\ldots\) (\(\pi\))", ["rationaal", "irrationaal"], 1),
             ]),
        dict(kop="Breuk, kommagetal, procent",
             opdracht="Vul de tabel aan. Vereenvoudig elke breuk.",
             oefeningen=[
                 ("tabel", ["breuk", "kommagetal", "procent"],
                  [[r"\(\tfrac{1}{4}\)", None, None], [None, r"\(0{,}6\)", None],
                   [None, None, r"\(12{,}5 \%\)"], [r"\(\tfrac{7}{10}\)", None, None]],
                  r"\(\tfrac{1}{4} \to 0{,}25 \to 25 \%\) · \(\tfrac{3}{5} \to 0{,}6 \to 60 \%\) · "
                  r"\(\tfrac{1}{8} \to 0{,}125 \to 12{,}5 \%\) · \(\tfrac{7}{10} \to 0{,}7 \to 70 \%\)",
                  "150px"),
             ]),
        dict(kop="Wortels vereenvoudigen",
             opdracht="Haal het grootste volkomen kwadraat uit de wortel.",
             oefeningen=[
                 ("rij", [(r"\(\sqrt{8}\)", r"\(2\sqrt{2}\)"), (r"\(\sqrt{27}\)", r"\(3\sqrt{3}\)"),
                          (r"\(\sqrt{48}\)", r"\(4\sqrt{3}\)"), (r"\(\sqrt{75}\)", r"\(5\sqrt{3}\)")],
                  "Vereenvoudigd", W),
             ]),
        dict(kop="Nog vier wortels",
             opdracht="Zelfde werkwijze, iets grotere getallen.",
             oefeningen=[
                 ("rij", [(r"\(\sqrt{32}\)", r"\(4\sqrt{2}\)"), (r"\(\sqrt{45}\)", r"\(3\sqrt{5}\)"),
                          (r"\(\sqrt{98}\)", r"\(7\sqrt{2}\)"), (r"\(\sqrt{200}\)", r"\(10\sqrt{2}\)")],
                  "Vereenvoudigd", W),
             ]),
        dict(kop="Derdemachtswortels",
             opdracht="Welk getal tot de derde macht geeft dit?",
             oefeningen=[
                 ("rij", [(r"\(\sqrt[3]{8}\)", r"\(2\)"), (r"\(\sqrt[3]{27}\)", r"\(3\)"),
                          (r"\(\sqrt[3]{216}\)", r"\(6\)"), (r"\(\sqrt[3]{1000}\)", r"\(10\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Rekenen met wortels",
             opdracht="Reken uit en vereenvoudig.",
             oefeningen=[
                 ("rij", [(r"\(\sqrt{2} \cdot \sqrt{8}\)", r"\(4\)"), (r"\(\sqrt{6} \cdot \sqrt{6}\)", r"\(6\)"),
                          (r"\(\sqrt{5} + \sqrt{5}\)", r"\(2\sqrt{5}\)"), (r"\(\sqrt{16 + 9}\)", r"\(5\)")],
                  "Antwoord", W),
                 ("rij", [(r"\(\sqrt{3} \cdot \sqrt{27}\)", r"\(9\)"), (r"\(2\sqrt{7} + 3\sqrt{7}\)", r"\(5\sqrt{7}\)"),
                          (r"\(\sqrt{a^{2}}\) met \(a = -4\)", r"\(4\)")],
                  "Antwoord", WW),
             ]),
        dict(kop="De noemer wortelvrij maken",
             opdracht="Vermenigvuldig teller en noemer met dezelfde wortel.",
             oefeningen=[
                 ("rij", [(r"\(\dfrac{1}{\sqrt{3}}\)", r"\(\dfrac{\sqrt{3}}{3}\)"),
                          (r"\(\dfrac{2}{\sqrt{2}}\)", r"\(\sqrt{2}\)"),
                          (r"\(\dfrac{5}{\sqrt{5}}\)", r"\(\sqrt{5}\)"),
                          (r"\(\dfrac{3}{\sqrt{6}}\)", r"\(\dfrac{\sqrt{6}}{2}\)")],
                  "Wortelvrij", WW),
             ]),
        dict(kop="Machten",
             opdracht="Schrijf zo eenvoudig mogelijk.",
             oefeningen=[
                 ("rij", [(r"\(a^{5} \cdot a^{2}\)", r"\(a^{7}\)"), (r"\(\dfrac{a^{8}}{a^{3}}\)", r"\(a^{5}\)"),
                          (r"\(\left(a^{2}\right)^{4}\)", r"\(a^{8}\)"), (r"\((3a)^{2}\)", r"\(9a^{2}\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Exponent nul en negatieve exponenten",
             opdracht="Schrijf het antwoord zonder negatieve exponent.",
             oefeningen=[
                 ("rij", [(r"\(7^{0}\)", r"\(1\)"), (r"\(2^{-4}\)", r"\(\tfrac{1}{16}\)"),
                          (r"\(5^{-2}\)", r"\(\tfrac{1}{25}\)"), (r"\((2a)^{4}\)", r"\(16a^{4}\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Machten met letters",
             opdracht="Pas de rekenregels toe en schrijf zonder negatieve exponent.",
             oefeningen=[
                 ("rij", [(r"\(\left(2a^{2}\right)^{3}\)", r"\(8a^{6}\)"),
                          (r"\(a^{-3} \cdot a^{5}\)", r"\(a^{2}\)"),
                          (r"\(\left(a^{3}b\right)^{2}\)", r"\(a^{6}b^{2}\)"),
                          (r"\(\dfrac{a^{4}}{a^{6}}\)", r"\(\dfrac{1}{a^{2}}\)")],
                  "Antwoord", WW),
             ]),
        dict(kop="Welke eigenschap?",
             opdracht="Schrijf op welke rekeneigenschap er gebruikt wordt.",
             oefeningen=[
                 ("rij", [(r"\(4 \cdot (10 + 3) = 4 \cdot 10 + 4 \cdot 3\)", "distributiviteit"),
                          (r"\((5 + 7) + 3 = 5 + (7 + 3)\)", "associativiteit"),
                          (r"\(6 \cdot 9 = 9 \cdot 6\)", "commutativiteit")],
                  "Welke eigenschap?", WW),
             ]),
        dict(kop="Fouten zoeken",
             opdracht="Bij elke bewering: klopt ze? Zo niet, schrijf op wat het juiste antwoord is.",
             oefeningen=[
                 ("open", r"\(\sqrt{25 + 144} = 5 + 12 = 17\).",
                  r"Fout. De wortel van een som is niet de som van de wortels: \(\sqrt{169} = 13\).", 3),
                 ("open", r"\(a^{3} \cdot a^{4} = a^{12}\).",
                  r"Fout. Bij vermenigvuldigen tel je de exponenten op: \(a^{7}\).", 3),
             ]),
        dict(kop="Nog twee fouten",
             opdracht="Zelfde opdracht: klopt het, en zo niet, wat is het juiste antwoord?",
             oefeningen=[
                 ("open", r"\((2a)^{3} = 2a^{3}\).",
                  r"Fout. Elke factor krijgt de exponent: \(8a^{3}\).", 3),
                 ("open", r"\(3^{-2} = -9\).",
                  r"Fout. Een negatieve exponent keert om, ze maakt het getal niet negatief: \(3^{-2} = \tfrac{1}{9}\).", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", r"Elk getal uit \(\mathbb{Z}\) zit ook in \(\mathbb{Q}\).", True),
                 ("waar", r"Elk getal uit \(\mathbb{R}\) kan je als breuk van twee gehele getallen schrijven.", False),
                 ("waar", r"\(\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}\) voor positieve \(a\) en \(b\).", True),
                 ("waar", "Een negatieve exponent maakt het getal zelf negatief.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom volstaan de rationale getallen niet om de getallenas te vullen?",
                  r"Omdat er lengtes bestaan die geen breuk zijn. De schuine zijde van een rechthoekige driehoek met rechthoekszijden \(1\) meet \(\sqrt{2}\), en dat getal laat geen enkele breuk exact weergeven. Daar blijft dus een gat in \(\mathbb{Q}\).", 4),
                 ("open", "Hoe zie je aan de decimale vorm of een getal rationaal of irrationaal is?",
                  r"Stopt ze (\(0{,}125\)) of herhaalt ze zich (\(0{,}333\ldots\)), dan is het getal rationaal. Is ze onbegrensd én niet-repeterend, zoals bij \(\pi\), dan is het irrationaal.", 4),
             ]),
        dict(kop="Doordenkers",
             opdracht="Denk eerst na, schrijf daarna je redenering op.",
             oefeningen=[
                 ("open", r"Waarom is \(\sqrt{a^{2}}\) niet altijd gelijk aan \(a\)?",
                  r"Omdat een vierkantswortel nooit negatief is. Is \(a = -4\), dan is \(\sqrt{a^{2}} = \sqrt{16} = 4\), en dat is \(-a\). In het algemeen geldt \(\sqrt{a^{2}} = |a|\).", 5),
                 ("open", r"\(\dfrac{1}{\sqrt{5}}\) en \(\dfrac{\sqrt{5}}{5}\) zien er anders uit. Waarom is het toch hetzelfde getal?",
                  r"Omdat je teller en noemer met \(\sqrt{5}\) vermenigvuldigd hebt, en \(\dfrac{\sqrt{5}}{\sqrt{5}} = 1\). Vermenigvuldigen met \(1\) verandert de waarde niet, alleen de schrijfwijze. Allebei zijn ze ongeveer \(0{,}447\).", 5),
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
                 ("rij", [("\\(-7\\) en \\(-2\\)", "<"), ("\\(0{,}45\\) en \\(0{,}5\\)", "<"),
                          ("\\(-1\\) en \\(0\\)", "<"), ("\\(\\tfrac{3}{4}\\) en \\(0{,}7\\)", ">")],
                  "Teken", W),
             ]),
        dict(kop="Ordenen van klein naar groot",
             opdracht="Zet ze eerst allemaal in dezelfde vorm en schrijf ze dan op volgorde.",
             oefeningen=[
                 ("open", "\\(0{,}7\\) — \\(\\tfrac{2}{3}\\) — \\(68\\%\\) — \\(0{,}71\\)",
                  "\\(\\tfrac{2}{3}\\) is \\(0{,}666\\)…, dus: \\(\\tfrac{2}{3}\\) — \\(68\\%\\) — \\(0{,}7\\) — \\(0{,}71\\).", 3),
                 ("open", "\\(-0{,}5\\) — \\(-\\tfrac{1}{4}\\) — \\(-0{,}75\\) — \\(0\\)",
                  "\\(-0{,}75\\) — \\(-0{,}5\\) — \\(-\\tfrac{1}{4}\\) — \\(0\\).", 3),
             ]),
        dict(kop="Afronden",
             opdracht="Rond af op twee cijfers na de komma. Kijk naar het eerste cijfer dat wegvalt.",
             oefeningen=[
                 ("rij", [("\\(5{,}6349\\)", "\\(5{,}63\\)"), ("\\(5{,}6351\\)", "\\(5{,}64\\)"), ("\\(0{,}9962\\)", "\\(1{,}00\\)"), ("\\(12{,}3450\\)", "\\(12{,}35\\)")],
                  "Afgerond", W),
             ]),
        dict(kop="Schatten",
             opdracht="Schat op honderdtallen of op tientallen, zoals gevraagd.",
             oefeningen=[
                 ("rij", [("\\(38 \\cdot 52\\) op honderdtallen", "ongeveer \\(2000\\)"),
                          ("\\(29 \\cdot 31\\) op honderdtallen", "ongeveer \\(900\\)"),
                          ("\\(812 : 4\\) op tientallen", "ongeveer \\(200\\)")],
                  "Schatting", WW),
             ]),
        dict(kop="Intervallen lezen",
             opdracht="Schrijf in gewone taal wat het interval betekent.",
             oefeningen=[
                 ("rij", [("\\(\\left[1, 6\\right]\\)", "alle getallen van \\(1\\) tot \\(6\\), grenzen erbij"),
                          ("\\(\\left]0, 4\\right[\\)", "alle getallen tussen \\(0\\) en \\(4\\), grenzen niet erbij"),
                          ("\\(\\left[2, 9\\right[\\)", "van \\(2\\) tot \\(9\\), met \\(2\\) erbij en \\(9\\) niet")],
                  "Betekenis", WL),
             ]),
        dict(kop="Intervallen schrijven",
             opdracht="Schrijf de verzameling als interval.",
             oefeningen=[
                 ("rij", [("alle \\(x\\) groter dan \\(4\\)", "\\(\\left]4, +\\infty\\right[\\)"),
                          ("alle \\(x\\) kleiner dan of gelijk aan \\(0\\)", "\\(\\left]-\\infty, 0\\right]\\)"),
                          ("alle \\(x\\) tussen \\(-1\\) en \\(5\\), grenzen erbij", "\\(\\left[-1, 5\\right]\\)"),
                          ("alle \\(x\\) groter dan of gelijk aan \\(-2\\)", "\\(\\left[-2, +\\infty\\right[\\)")],
                  "Interval", WW),
             ]),
        dict(kop="Wetenschappelijke notatie",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["gewoon getal", "wetenschappelijke notatie"],
                  [["\\(73\\,000\\)", None], [None, "\\(9{,}1 \\cdot 10^{-5}\\)"], ["\\(0{,}00408\\)", None], [None, "\\(2 \\cdot 10^{7}\\)"]],
                  "\\(73\\,000\\) → \\(7{,}3 \\cdot 10^{4} \\cdot 9{,}1 \\cdot 10^{-5}\\) → \\(0{,}000091 \\cdot 0{,}00408\\) → \\(4{,}08 \\cdot 10^{-3}\\) \\(\\cdot\\) "
                  "\\(2 \\cdot 10^{7}\\) → \\(20\\,000\\,000\\)", "210px"),
             ]),
        dict(kop="Correct of niet?",
             opdracht="Duid aan of het een correcte wetenschappelijke notatie is.",
             oefeningen=[
                 ("kies", "\\(34{,}2 \\cdot 10^{3}\\)", ["correct", "niet correct"], 1),
                 ("kies", "\\(3{,}42 \\cdot 10^{4}\\)", ["correct", "niet correct"], 0),
                 ("kies", "\\(0{,}5 \\cdot 10^{6}\\)", ["correct", "niet correct"], 1),
                 ("kies", "\\(8 \\cdot 10^{-2}\\)", ["correct", "niet correct"], 0),
             ]),
        dict(kop="Nog vier tekens",
             opdracht=r"Schrijf \(<\), \(>\) of \(=\) tussen de twee getallen.",
             oefeningen=[
                 ("rij", [(r"\(-3{,}1\) en \(-3{,}01\)", r"\(<\)"),
                          (r"\(\tfrac{1}{2}\) en \(0{,}5\)", r"\(=\)"),
                          (r"\(0{,}089\) en \(0{,}1\)", r"\(<\)"),
                          (r"\(-\tfrac{2}{5}\) en \(-0{,}5\)", r"\(>\)")],
                  "Teken", W),
             ]),
        dict(kop="Afronden op één cijfer na de komma",
             opdracht="Kijk telkens naar het eerste cijfer dat wegvalt.",
             oefeningen=[
                 ("rij", [(r"\(4{,}449\)", r"\(4{,}4\)"), (r"\(4{,}451\)", r"\(4{,}5\)"),
                          (r"\(0{,}96\)", r"\(1{,}0\)"), (r"\(-2{,}37\)", r"\(-2{,}4\)")],
                  "Afgerond", W),
             ]),
        dict(kop="Rangschikken",
             opdracht="Zet van klein naar groot.",
             oefeningen=[
                 ("rij", [(r"\(0{,}3\) — \(\tfrac{1}{4}\) — \(28\%\)",
                           r"\(\tfrac{1}{4}\) — \(28\%\) — \(0{,}3\)"),
                          (r"\(-1\) — \(-1{,}5\) — \(-0{,}5\)", r"\(-1{,}5\) — \(-1\) — \(-0{,}5\)"),
                          (r"\(\tfrac{7}{8}\) — \(0{,}9\) — \(88\%\)",
                           r"\(\tfrac{7}{8}\) — \(88\%\) — \(0{,}9\)")],
                  "Van klein naar groot", WL),
             ]),
        dict(kop="Wetenschappelijke notatie: terugrekenen",
             opdracht="Schrijf het als een gewoon getal.",
             oefeningen=[
                 ("rij", [(r"\(4 \cdot 10^{3}\)", r"\(4000\)"),
                          (r"\(6{,}2 \cdot 10^{5}\)", r"\(620\,000\)"),
                          (r"\(7 \cdot 10^{-2}\)", r"\(0{,}07\)"),
                          (r"\(1{,}5 \cdot 10^{-4}\)", r"\(0{,}00015\)")],
                  "Gewoon getal", WW),
             ]),
        dict(kop="Open, halfopen of gesloten?",
             opdracht="Schrijf welk soort interval het is.",
             oefeningen=[
                 ("rij", [(r"\(\left]2, 7\right[\)", "open"),
                          (r"\(\left[2, 7\right]\)", "gesloten"),
                          (r"\(\left[2, 7\right[\)", "halfopen"),
                          (r"\(\left]-\infty, 7\right]\)", "halfopen")],
                  "Welk soort?", WW),
             ]),
        dict(kop="Fouten zoeken",
             opdracht="Zoek de fout en schrijf op hoe het wel moet.",
             oefeningen=[
                 ("open", r"Iemand rondt \(2{,}3449\) af op twee cijfers na de komma en krijgt "
                          r"\(2{,}35\).",
                  r"Die persoon rondde twee keer af: eerst naar \(2{,}345\) en dan naar \(2{,}35\). Je "
                  r"kijkt maar naar één cijfer, het eerste dat wegvalt, en dat is \(4\): dus \(2{,}34\).", 4),
                 ("open", r"Iemand schrijft \(\left[3, +\infty\right]\).",
                  r"Bij oneindig wijst het haakje altijd naar buiten, want oneindig is geen getal en kan "
                  r"er dus niet bij horen: \(\left[3, +\infty\right[\).", 4),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom rond je pas op het einde van een berekening af, en niet bij elke "
                          "tussenstap?",
                  "Omdat elke afronding een kleine fout invoert en die fouten zich opstapelen. Rond je "
                  "drie keer af, dan kan je uitkomst er procenten naast zitten.", 5),
                 ("open", r"Waarom is een afgerond getal eerder een bereik dan een punt?",
                  r"Omdat alle getallen die op dezelfde waarde afronden, hetzelfde afgeronde getal geven. "
                  r"Een weegschaal die \(2{,}5\) kg toont en op honderd gram afrondt, kan alles tussen "
                  r"\(2{,}45\) en \(2{,}55\) kg wegen.", 5),
             ]),
        dict(kop="Doordenkers",
             opdracht="Neem je tijd.",
             oefeningen=[
                 ("open", r"Ligt er een getal tussen \(0{,}999\) en \(1\)? Zo ja, geef er een.",
                  r"Ja. Tussen twee verschillende reële getallen ligt er altijd nog een, bijvoorbeeld het "
                  r"gemiddelde: \(0{,}9995\). Dat houdt nooit op.", 5),
                 ("open", r"Hoeveel getallen bevat het interval \(\left[4, 4\right]\), en hoeveel "
                          r"\(\left]4, 4\right[\)?",
                  r"Het eerste bevat precies één getal, namelijk \(4\) zelf. Het tweede is leeg: er is geen "
                  r"enkel getal dat strikt tussen \(4\) en \(4\) ligt.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij oneindig wijst het haakje altijd naar buiten.", True),
                 ("waar", "Het interval \\(\\left[5, 5\\right]\\) is leeg.", False),
                 ("waar", "Een negatieve exponent betekent dat het getal negatief is.", False),
                 ("waar", "Je rondt best pas op het einde van een berekening af.", True),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Een weegschaal geeft \\(3{,}7\\) kg en rondt af op honderd gram. Tussen welke "
                          "waarden ligt het echte gewicht?",
                  "Tussen \\(3{,}65\\) kg en \\(3{,}75\\) kg.", 4),
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
                  "allebei \\(6\\) zijvlakken, \\(12\\) ribben en \\(8\\) hoekpunten", "110px"),
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
             opdracht=r"\(A = \{1, 2, 3, 4, 5\}\) en \(B = \{4, 5, 6\}\). Schrijf de verzameling op.",
             oefeningen=[
                 ("rij", [(r"\(A \cap B\)", r"\(\{4, 5\}\)"), (r"\(A \cup B\)", r"\(\{1, 2, 3, 4, 5, 6\}\)"),
                          (r"\(A \setminus B\)", r"\(\{1, 2, 3\}\)"), (r"\(B \setminus A\)", r"\(\{6\}\)")],
                  "Verzameling", WW),
             ]),
        dict(kop="Nog vier verzamelingen",
             opdracht=r"\(C = \{2, 4, 6, 8\}\) en \(D = \{1, 2, 3, 4\}\). Schrijf de verzameling op.",
             oefeningen=[
                 ("rij", [(r"\(C \cap D\)", r"\(\{2, 4\}\)"),
                          (r"\(C \cup D\)", r"\(\{1, 2, 3, 4, 6, 8\}\)"),
                          (r"\(C \setminus D\)", r"\(\{6, 8\}\)"),
                          (r"\(D \setminus C\)", r"\(\{1, 3\}\)")],
                  "Verzameling", WW),
             ]),
        dict(kop="Gelijkvormigheidskenmerken",
             opdracht="Schrijf welk kenmerk je gebruikt: HH, ZZZ of ZHZ.",
             oefeningen=[
                 ("rij", [("twee driehoeken met hoeken \\(40^\\circ\\) en \\(70^\\circ\\) gemeen", "HH"),
                          ("zijden \\(3\\)-\\(4\\)-\\(5\\) en \\(9\\)-\\(12\\)-\\(15\\)", "ZZZ"),
                          ("zijden \\(4\\) en \\(6\\) met de hoek van \\(50^\\circ\\) ertussen, en \\(8\\) en \\(12\\) met \\(50^\\circ\\) ertussen", "ZHZ")],
                  "Kenmerk", W),
             ]),
        dict(kop="Factor k",
             opdracht="Vul in wat er met lengte, oppervlakte en volume gebeurt.",
             oefeningen=[
                 ("tabel", ["factor k", "lengte maal", "oppervlakte maal", "volume maal"],
                  [["\\(2\\)", None, None, None], ["\\(3\\)", None, None, None],
                   ["\\(4\\)", None, None, None], ["\\(5\\)", None, None, None]],
                  "\\(2\\) → \\(2\\), \\(4\\), \\(8 \\cdot 3\\) → \\(3\\), \\(9\\), \\(27 \\cdot 4\\) → \\(4\\), \\(16\\), \\(64 \\cdot 5\\) → \\(5\\), \\(25\\), \\(125\\)", "100px"),
             ]),
        dict(kop="Rekenen met schaal",
             opdracht="Reken om. Zet het antwoord in de gevraagde eenheid.",
             oefeningen=[
                 ("rij", [("schaal \\(1 : 50\\), op de maquette \\(9\\) cm, in het echt in meter", "\\(4{,}5\\) m"),
                          ("schaal \\(1 : 200\\), op het plan \\(6\\) cm, in het echt in meter", "\\(12\\) m"),
                          ("schaal \\(1 : 25\\,000\\), op de kaart \\(12\\) cm, in het echt in km", "\\(3\\) km")],
                  "In het echt", WW),
             ]),
        dict(kop="Toepassen",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Een affiche van \\(20\\) op \\(30\\) cm wordt vergroot tot \\(60\\) op \\(90\\) cm. Hoeveel keer "
                          "meer papier heb je nodig?",
                  "De factor is \\(3\\), dus de oppervlakte wordt \\(9\\) keer zo groot.", 4),
                 ("open", "Een modelauto op schaal \\(1 : 20\\) weegt \\(60\\) gram. De echte auto is van "
                          "hetzelfde materiaal. Hoeveel weegt die ongeveer?",
                  "Het gewicht volgt het volume, dus maal \\(20^{3} = 8000\\). Dat is \\(480\\,000\\) gram, dus "
                  "ongeveer \\(480\\) kg.", 5),
                 ("open", "Een driehoek heeft zijden \\(6\\), \\(8\\) en \\(10\\). Een gelijkvormige driehoek heeft als "
                          "kleinste zijde \\(15\\). Hoe lang zijn de twee andere zijden?",
                  "De factor is \\(2{,}5\\), dus \\(20\\) en \\(25\\).", 4),
             ]),
        dict(kop="Nog vier liggingen",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("rij", [("twee vlakken zonder enig gemeenschappelijk punt", "evenwijdig"),
                          ("een rechte waarvan elk punt in het vlak ligt", "de rechte ligt in het vlak"),
                          ("twee rechten met precies één gemeenschappelijk punt", "snijdend"),
                          ("twee rechten met alle punten gemeen", "samenvallend")],
                  "Ligging", WL),
             ]),
        dict(kop="Ruimtefiguren herkennen",
             opdracht="Schrijf vlak of ruimte.",
             oefeningen=[
                 ("rij", [("een cirkel", "vlak"), ("een bol", "ruimte"),
                          ("een piramide", "ruimte"), ("een vierkant", "vlak")],
                  "Vlak of ruimte?", W),
             ]),
        dict(kop="De gelijkvormigheidsfactor berekenen",
             opdracht=r"Bereken \(k\), de factor van de eerste naar de tweede figuur.",
             oefeningen=[
                 ("rij", [(r"zijden \(4\) en \(10\)", r"\(k = 2{,}5\)"),
                          (r"zijden \(12\) en \(3\)", r"\(k = 0{,}25\)"),
                          (r"zijden \(7\) en \(7\)", r"\(k = 1\), de figuren zijn gelijk")],
                  "Factor", WW),
             ]),
        dict(kop="Terugrekenen met schaal",
             opdracht="Reken van de werkelijkheid naar de tekening.",
             oefeningen=[
                 ("rij", [(r"schaal \(1 : 100\), in het echt \(8\) m, op het plan in cm", r"\(8\) cm"),
                          (r"schaal \(1 : 50\), in het echt \(3\) m, op de maquette in cm", r"\(6\) cm"),
                          (r"schaal \(1 : 10\,000\), in het echt \(5\) km, op de kaart in cm",
                           r"\(50\) cm")],
                  "Op de tekening", WW),
             ]),
        dict(kop="Fouten zoeken",
             opdracht="Zoek de fout en schrijf op hoe het wel moet.",
             oefeningen=[
                 ("open", r"Iemand zegt dat een schaal \(1 : 200\) betekent dat de tekening "
                          r"\(200\) keer groter is dan het gebouw.",
                  r"Het is net omgekeerd: wat op de tekening \(1\) is, is in het echt \(200\). Het "
                  r"gebouw is dus \(200\) keer groter dan de tekening.", 4),
                 ("open", r"Iemand verdubbelt de ribben van een kubus en zegt dat de inhoud "
                          r"verdubbelt.",
                  r"De inhoud wordt \(2^{3} = 8\) keer zo groot. Lengte werkt één keer, oppervlakte "
                  r"twee keer en volume drie keer.", 4),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom kunnen twee vlakken elkaar nooit in precies één punt snijden?",
                  "Zodra twee vlakken één punt gemeen hebben, hebben ze meteen een hele rechte gemeen. "
                  "Denk aan twee muren van een kamer: ze ontmoeten elkaar in een lijn.", 5),
                 ("open", "Waarom zou een reus van drie keer een mens niet kunnen bestaan?",
                  r"Zijn gewicht volgt het volume en wordt \(3^{3} = 27\) keer zo groot, maar de "
                  r"doorsnede van zijn botten volgt de oppervlakte en wordt maar \(3^{2} = 9\) keer zo "
                  r"groot. De botten zouden het gewicht niet dragen.", 6),
             ]),
        dict(kop="Doordenkers",
             opdracht="Neem je tijd.",
             oefeningen=[
                 ("open", r"Een bol krijgt een twee keer zo grote straal. Hoeveel keer meer verf heb je "
                          r"nodig om hem te schilderen, en hoeveel keer meer water past erin?",
                  r"Verf volgt de oppervlakte: \(2^{2} = 4\) keer zoveel. Water volgt het volume: "
                  r"\(2^{3} = 8\) keer zoveel.", 5),
                 ("open", r"Twee driehoeken hebben dezelfde drie hoeken. Zijn ze gelijkvormig? Zijn ze "
                          r"gelijk? Leg allebei de antwoorden uit.",
                  r"Gelijkvormig: ja, dat is het kenmerk HH, en twee gelijke hoeken volstaan al. Gelijk: "
                  r"niet noodzakelijk, want de hoeken leggen de vorm vast en niet de grootte. Dat is pas "
                  r"zo als de factor \(k = 1\) is.", 6),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Twee vlakken kunnen elkaar in één punt snijden.", False),
                 ("waar", "Twee driehoeken met dezelfde drie hoeken zijn altijd gelijkvormig.", True),
                 ("waar", "Gelijkvormige figuren zijn altijd even groot.", False),
                 ("waar", "Bij een schaal \\(1 : 100\\) is de tekening honderd keer kleiner.", True),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-pythagoras-en-de-rechthoekige-driehoek-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Pythagoras en de rechthoekige driehoek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De schuine zijde berekenen",
             opdracht="Bereken de schuine zijde. Schrijf je berekening erbij.",
             oefeningen=[
                 ("rij", [(r"\(a = 5\), \(b = 12\)", r"\(13\)"),
                          (r"\(a = 8\), \(b = 15\)", r"\(17\)"),
                          (r"\(a = 20\), \(b = 21\)", r"\(29\)"),
                          (r"\(a = 1\), \(b = 1\)", r"\(\sqrt{2}\)"),
                          (r"\(a = 2\), \(b = 3\)", r"\(\sqrt{13}\)")],
                  r"schuine zijde \(c\)", W),
             ]),
        dict(kop="Aftrekken in plaats van optellen",
             opdracht=r"Je kent de schuine zijde \(c\) en één rechthoekszijde. Bereken de andere.",
             oefeningen=[
                 ("rij", [(r"\(c = 25\), \(a = 7\)", r"\(24\)"),
                          (r"\(c = 10\), \(a = 6\)", r"\(8\)"),
                          (r"\(c = 26\), \(a = 24\)", r"\(10\)"),
                          (r"\(c = 5\), \(a = 3\)", r"\(4\)")],
                  r"zijde \(b\)", W),
             ]),
        dict(kop="Is de driehoek rechthoekig?",
             opdracht="Reken na met de omgekeerde stelling en duid aan.",
             oefeningen=[
                 ("kies", r"zijden \(8\), \(15\) en \(17\)", ["rechthoekig", "niet rechthoekig"], 0),
                 ("kies", r"zijden \(6\), \(7\) en \(9\)", ["rechthoekig", "niet rechthoekig"], 1),
                 ("kies", r"zijden \(7\), \(24\) en \(25\)", ["rechthoekig", "niet rechthoekig"], 0),
                 ("kies", r"zijden \(5\), \(6\) en \(8\)", ["rechthoekig", "niet rechthoekig"], 1),
                 ("kies", r"zijden \(9\), \(40\) en \(41\)", ["rechthoekig", "niet rechthoekig"], 0),
             ]),
        dict(kop="Afstand tussen twee punten",
             opdracht="Bereken de afstand. Gebruik de formule met de verschillen.",
             oefeningen=[
                 ("rij", [(r"\(A(0, 0)\) en \(B(3, 4)\)", r"\(5\)"),
                          (r"\(A(1, 1)\) en \(B(4, 5)\)", r"\(5\)"),
                          (r"\(A(-3, 2)\) en \(B(3, 10)\)", r"\(10\)"),
                          (r"\(A(2, 7)\) en \(B(2, 1)\)", r"\(6\)"),
                          (r"\(A(-1, -1)\) en \(B(2, 3)\)", r"\(5\)")],
                  "Afstand", W),
             ]),
        dict(kop="SOSCASTOA",
             opdracht="Schrijf op welk goniometrisch getal je nodig hebt.",
             oefeningen=[
                 ("rij", [("je kent de schuine zijde en de hoek, je zoekt de overstaande", r"\(\sin\alpha\)"),
                          ("je kent de schuine zijde en de hoek, je zoekt de aanliggende", r"\(\cos\alpha\)"),
                          ("je kent de aanliggende en de hoek, je zoekt de overstaande", r"\(\tan\alpha\)"),
                          ("je kent de twee rechthoekszijden en je zoekt de hoek", r"\(\tan\alpha\)")],
                  "Welk getal?", W),
             ]),
        dict(kop="Formules uit het hoofd",
             opdracht="Schrijf de formule op.",
             oefeningen=[
                 ("open", "De stelling van Pythagoras", r"\(a^{2} + b^{2} = c^{2}\)", 1),
                 ("open", "De grondformule van de goniometrie",
                  r"\(\sin^{2}\alpha + \cos^{2}\alpha = 1\)", 1),
                 ("open", r"De tangens uit \(\sin\alpha\) en \(\cos\alpha\)",
                  r"\(\tan\alpha = \tfrac{\sin\alpha}{\cos\alpha}\)", 1),
                 ("open", r"De afstand tussen \(A(x_{1}, y_{1})\) en \(B(x_{2}, y_{2})\)",
                  r"\(\left|AB\right| = \sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}\)", 1),
             ]),
        dict(kop="Waarden invullen",
             opdracht="Vul de tabel aan met de exacte waarden.",
             oefeningen=[
                 ("tabel", [r"\(\alpha\)", r"\(\sin\alpha\)", r"\(\cos\alpha\)", r"\(\tan\alpha\)"],
                  [[r"\(0^\circ\)", None, None, None], [r"\(30^\circ\)", None, None, None],
                   [r"\(45^\circ\)", None, None, None], [r"\(60^\circ\)", None, None, None],
                   [r"\(90^\circ\)", None, None, None]],
                  r"\(0^\circ\): \(0\), \(1\), \(0\) · \(30^\circ\): \(\tfrac{1}{2}\), "
                  r"\(\tfrac{\sqrt{3}}{2}\), \(\tfrac{\sqrt{3}}{3}\) · \(45^\circ\): "
                  r"\(\tfrac{\sqrt{2}}{2}\), \(\tfrac{\sqrt{2}}{2}\), \(1\) · \(60^\circ\): "
                  r"\(\tfrac{\sqrt{3}}{2}\), \(\tfrac{1}{2}\), \(\sqrt{3}\) · \(90^\circ\): "
                  r"\(1\), \(0\), bestaat niet",
                  "110px"),
             ]),
        dict(kop="De grondformule gebruiken",
             opdracht="De hoek is scherp. Bereken het gevraagde.",
             oefeningen=[
                 ("rij", [(r"\(\sin\alpha = 0{,}6\), dan is \(\cos\alpha\)", r"\(0{,}8\)"),
                          (r"\(\cos\alpha = 0{,}8\), dan is \(\sin\alpha\)", r"\(0{,}6\)"),
                          (r"\(\sin\alpha = 0{,}28\), dan is \(\cos\alpha\)", r"\(0{,}96\)"),
                          (r"\(\cos\alpha = \tfrac{1}{2}\), dan is \(\sin\alpha\)", r"\(\tfrac{\sqrt{3}}{2}\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De stelling van Pythagoras geldt in elke driehoek.", False),
                 ("waar", "De schuine zijde is altijd de langste zijde.", True),
                 ("waar", r"Er bestaat een scherpe hoek met \(\cos\alpha = 1{,}2\).", False),
                 ("waar", r"Twee complementaire hoeken zijn samen \(90^\circ\).", True),
                 ("waar", r"De goniometrische cirkel heeft straal \(1\).", True),
                 ("waar", "Een afstand tussen twee punten kan negatief zijn.", False),
                 ("waar", r"\(\tan 45^\circ = 1\).", True),
             ]),
        dict(kop="Exact of benaderd?",
             opdracht="Duid aan welk antwoord het exacte is.",
             oefeningen=[
                 ("kies", r"de diagonaal van een vierkant met zijde \(1\)",
                  [r"\(\sqrt{2}\)", r"\(1{,}41\)"], 0),
                 ("kies", r"\(\sin 60^\circ\)", [r"\(\tfrac{\sqrt{3}}{2}\)", r"\(0{,}87\)"], 0),
                 ("kies", r"de schuine zijde bij \(a = 2\) en \(b = 3\)",
                  [r"\(\sqrt{13}\)", r"\(3{,}61\)"], 0),
             ]),
        dict(kop="Toepassen",
             opdracht="Maak eerst een schets met de gegevens erop.",
             oefeningen=[
                 ("open", r"Een ladder van \(13\) meter staat met de voet \(5\) meter van de muur. "
                          r"Hoe hoog reikt hij?",
                  r"\(\sqrt{169 - 25} = \sqrt{144} = 12\) meter.", 5),
                 ("open", r"Een balk is \(6\) bij \(8\) bij \(24\) cm. Hoe lang is de ruimtediagonaal?",
                  r"Grondvlakdiagonaal \(\sqrt{36 + 64} = 10\), dan \(\sqrt{100 + 576} = \sqrt{676} = 26\) cm.", 6),
             ]),
        dict(kop="Zelf de werkwijze opschrijven",
             opdracht="Schrijf op welke formule je gebruikt en wat je uitrekent.",
             oefeningen=[
                 ("open", r"Je staat \(40\) meter van een toren en kijkt onder \(35^\circ\) naar de top. "
                          r"Welke formule gebruik je, en wat reken je uit?",
                  r"De tangens: hoogte \(= 40 \cdot \tan 35^\circ\), dus ongeveer \(28\) meter. "
                  r"(Je ooghoogte komt er nog bij.)", 5),
                 ("open", r"Een televisie heeft een diagonaal van \(40\) inch en een beeldverhouding "
                          r"\(16 : 9\). Hoe reken je de breedte uit? Schrijf de werkwijze op.",
                  r"Stel de breedte \(16k\) en de hoogte \(9k\). Dan is "
                  r"\((16k)^{2} + (9k)^{2} = 40^{2}\), dus \(337k^{2} = 1600\) en \(k \approx 2{,}18\). "
                  r"De breedte is \(16k \approx 34{,}9\) inch.", 6),
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
                 ("rij", [(r"\(35^\circ\) en \(80^\circ\)", r"\(65^\circ\)"),
                          (r"\(90^\circ\) en \(27^\circ\)", r"\(63^\circ\)"),
                          (r"\(110^\circ\) en \(22^\circ\)", r"\(48^\circ\)"),
                          (r"\(60^\circ\) en \(60^\circ\)", r"\(60^\circ\)"),
                          (r"\(18^\circ\) en \(101^\circ\)", r"\(61^\circ\)")],
                  "Derde hoek", W),
             ]),
        dict(kop="Welke regel?",
             opdracht=r"Schrijf welke regel je gebruikt: de sinusregel, de cosinusregel of \(180^\circ\).",
             oefeningen=[
                 ("rij", [("je kent twee zijden en de hoek ertussen", "de cosinusregel"),
                          ("je kent de drie zijden", "de cosinusregel"),
                          ("je kent een zijde met de hoek ertegenover, plus nog één hoek", "de sinusregel"),
                          ("je kent twee hoeken en zoekt de derde", r"\(180^\circ\) min de twee"),
                          ("je kent twee zijden en een hoek die er niet tussen ligt", "de sinusregel")],
                  "Welke regel?", WW),
             ]),
        dict(kop="Kan dit een driehoek zijn?",
             opdracht="Gebruik de driehoeksongelijkheid en duid aan.",
             oefeningen=[
                 ("kies", r"zijden \(3\), \(4\) en \(9\)", ["kan wel", "kan niet"], 1),
                 ("kies", r"zijden \(5\), \(6\) en \(10\)", ["kan wel", "kan niet"], 0),
                 ("kies", r"zijden \(2\), \(2\) en \(5\)", ["kan wel", "kan niet"], 1),
                 ("kies", r"zijden \(7\), \(7\) en \(7\)", ["kan wel", "kan niet"], 0),
                 ("kies", r"zijden \(1\), \(8\) en \(8\)", ["kan wel", "kan niet"], 0),
             ]),
        dict(kop="De formules opschrijven",
             opdracht="Schrijf de formule volledig uit.",
             oefeningen=[
                 ("open", "De cosinusregel", r"\(a^{2} = b^{2} + c^{2} - 2bc\cos\alpha\)", 1),
                 ("open", "De sinusregel",
                  r"\(\tfrac{a}{\sin\alpha} = \tfrac{b}{\sin\beta} = \tfrac{c}{\sin\gamma}\)", 1),
                 ("open", r"De norm van de vector \((x, y)\)", r"\(\sqrt{x^{2} + y^{2}}\)", 1),
                 ("open", r"Wat gebeurt er met de cosinusregel als \(\alpha = 90^\circ\), en hoe heet "
                          r"het resultaat?",
                  r"\(\cos 90^\circ = 0\), dus de laatste term valt weg en er blijft "
                  r"\(a^{2} = b^{2} + c^{2}\) over: de stelling van Pythagoras.", 4),
             ]),
        dict(kop="Eerst nadenken, dan rekenen",
             opdracht="Schrijf op in welke volgorde je rekent. Je hoeft niets uit te rekenen.",
             oefeningen=[
                 ("open", r"Je kent de zijden \(7\) en \(9\) en de hoek van \(40^\circ\) ertussen, en "
                          r"je zoekt alle hoeken.",
                  r"Eerst met de cosinusregel de derde zijde, daarna met de sinusregel een tweede "
                  r"hoek, en de derde hoek volgt uit \(180^\circ\).", 4),
                 ("open", r"In een stomphoekige driehoek vindt je rekentoestel bij \(\sin\alpha = 0{,}6\) "
                          r"de hoek \(37^\circ\). Waarom is dat hier misschien niet het juiste antwoord?",
                  r"Supplementaire hoeken hebben dezelfde sinus, dus \(143^\circ\) past er ook bij. "
                  r"De langste zijde verraadt welke hoek de grootste is.", 4),
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
                 ("rij", [(r"\((6, 8)\)", r"\(10\)"), (r"\((-3, 4)\)", r"\(5\)"),
                          (r"\((9, 12)\)", r"\(15\)"), (r"\((8, 0)\)", r"\(8\)"),
                          (r"\((1, 1)\)", r"\(\sqrt{2}\)")],
                  "Norm", W),
             ]),
        dict(kop="Vectoren tussen punten",
             opdracht="Bereken de coördinaten van de vector, en daarna zijn norm.",
             oefeningen=[
                 ("rij", [(r"van \(A(1, 1)\) naar \(B(5, 4)\)", r"\((4, 3)\), norm \(5\)"),
                          (r"van \(A(0, 2)\) naar \(B(6, 10)\)", r"\((6, 8)\), norm \(10\)"),
                          (r"van \(A(3, 5)\) naar \(B(3, 12)\)", r"\((0, 7)\), norm \(7\)"),
                          (r"van \(A(-2, 1)\) naar \(B(3, 13)\)", r"\((5, 12)\), norm \(13\)")],
                  "Vector en norm", WL),
             ]),
        dict(kop="Rekenen met vectoren",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\((2, 5) + (3, -1)\)", r"\((5, 4)\)"),
                          (r"\((1, 4) + (-1, -4)\)", r"\((0, 0)\), de nulvector"),
                          (r"\(-2 \cdot (3, -1)\)", r"\((-6, 2)\)"),
                          (r"\(3 \cdot (2, -2)\)", r"\((6, -6)\)")],
                  "Antwoord", WW),
             ]),
        dict(kop="Toepassen",
             opdracht="Maak eerst een schets met de gegevens erop.",
             oefeningen=[
                 ("open", r"Twee krachten van \(6\) en \(8\) newton staan loodrecht op elkaar. Hoe groot "
                          r"is de resulterende kracht, en hoe reken je dat uit?",
                  r"Met de kop-staartmethode krijg je een rechthoekige driehoek, dus Pythagoras: "
                  r"\(\sqrt{36 + 64} = 10\) newton.", 5),
                 ("open", "Wat zegt de formule van Chasles-Möbius, en waarvoor gebruik je ze?",
                  r"De vector van \(A\) naar \(B\) is gelijk aan die van \(A\) naar \(C\) plus die van "
                  r"\(C\) naar \(B\), via elk tussenpunt. Je gebruikt ze om een omweg in stukken te knippen.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De norm van een vector kan negatief zijn.", False),
                 ("waar", "Twee vectoren met dezelfde richting, zin en grootte zijn gelijk, ook als "
                          "ze elders in het vlak liggen.", True),
                 ("waar", "De som van twee vectoren is altijd langer dan elk van de twee.", False),
                 ("waar", r"Vermenigvuldigen met \(-2\) draait de zin van de vector om.", True),
                 ("waar", "De sinusregel werkt enkel in rechthoekige driehoeken.", False),
                 ("waar", "De langste zijde ligt tegenover de grootste hoek.", True),
                 ("waar", r"\(\cos 90^\circ = 1\).", False),
             ]),
        dict(kop="Welke hoort bij welke?",
             opdracht="Duid het juiste antwoord aan.",
             oefeningen=[
                 ("kies", "de grootte van een vector heet ook", ["de norm", "de zin"], 0),
                 ("kies", "een vector met grootte één heet", ["een eenheidsvector", "de nulvector"], 0),
                 ("kies", "de vector zonder richting en zonder zin is", ["de nulvector", "de eenheidsvector"], 0),
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
                 ("rij", [(r"\(4(x + 3)\)", r"\(4x + 12\)"),
                          (r"\(-3(x - 2)\)", r"\(-3x + 6\)"),
                          (r"\((x + 5)(x + 1)\)", r"\(x^{2} + 6x + 5\)"),
                          (r"\((x - 4)^{2}\)", r"\(x^{2} - 8x + 16\)"),
                          (r"\((x + 7)(x - 7)\)", r"\(x^{2} - 49\)")],
                  "Uitgewerkt", WW),
                 ("rij", [(r"\(2(x + 1) + 3(x - 4)\)", r"\(5x - 10\)"),
                          (r"\(5 - 2(x - 3)\)", r"\(11 - 2x\)"),
                          (r"\((2x + 1)(x - 3)\)", r"\(2x^{2} - 5x - 3\)")],
                  "Uitgewerkt", WW),
             ]),
        dict(kop="Ontbinden in factoren",
             opdracht="Schrijf als een product.",
             oefeningen=[
                 ("rij", [(r"\(8x + 12\)", r"\(4(2x + 3)\)"),
                          (r"\(x^{2} - 25\)", r"\((x + 5)(x - 5)\)"),
                          (r"\(x^{2} + 8x + 16\)", r"\((x + 4)^{2}\)"),
                          (r"\(3x^{2} - 6x\)", r"\(3x(x - 2)\)"),
                          (r"\(9x^{2} - 1\)", r"\((3x + 1)(3x - 1)\)")],
                  "Ontbonden", WW),
             ]),
        dict(kop="Vergelijkingen oplossen",
             opdracht="Los op. Schrijf minstens één tussenstap op.",
             oefeningen=[
                 ("rij", [(r"\(4x + 7 = 31\)", r"\(x = 6\)"),
                          (r"\(6x - 5 = 2x + 11\)", r"\(x = 4\)"),
                          (r"\(3(x - 2) = 15\)", r"\(x = 7\)"),
                          (r"\(\tfrac{x}{4} + 3 = 8\)", r"\(x = 20\)"),
                          (r"\(7 - x = 2x + 1\)", r"\(x = 2\)")],
                  "Oplossing", W),
             ]),
        dict(kop="Welke stap zet je eerst?",
             opdracht="Duid aan waarmee je begint.",
             oefeningen=[
                 ("kies", r"\(3(x - 2) = 15\)", ["haakjes uitwerken", "delen door 3"], 0),
                 ("kies", r"\(\tfrac{x}{4} + 3 = 8\)", [r"\(3\) aftrekken", "met 4 vermenigvuldigen"], 0),
                 ("kies", r"\(-5x > 20\)", ["delen door \\(-5\\) en het teken omdraaien",
                                            "delen door \\(-5\\) en het teken laten staan"], 0),
                 ("kies", r"\(2x - 7 = x + 3\)", [r"\(x\) naar links brengen", "delen door 2"], 0),
             ]),
        dict(kop="Met een noemer",
             opdracht="Werk eerst de noemers weg, en los dan op.",
             oefeningen=[
                 ("rij", [(r"\(\tfrac{x}{2} + \tfrac{x}{3} = 5\)", r"\(x = 6\)"),
                          (r"\(\tfrac{x - 1}{4} = 3\)", r"\(x = 13\)"),
                          (r"\(\tfrac{2x}{5} = 4\)", r"\(x = 10\)"),
                          (r"\(\tfrac{x}{3} - \tfrac{x}{6} = 2\)", r"\(x = 12\)")],
                  "Oplossing", W),
             ]),
        dict(kop="Bijzondere gevallen",
             opdracht="Los op en schrijf op wat het betekent.",
             oefeningen=[
                 ("open", r"\(2(x + 3) = 2x + 6\)",
                  r"Je krijgt \(0 = 0\): elke waarde van \(x\) is een oplossing.", 3),
                 ("open", r"\(3x + 1 = 3x + 5\)",
                  r"Je krijgt \(0 = 4\), wat niet klopt: er is geen enkele oplossing, dus \(\emptyset\).", 3),
             ]),
        dict(kop="Ongelijkheden",
             opdracht="Los op en schrijf de oplossingenverzameling als interval.",
             oefeningen=[
                 ("rij", [(r"\(2x + 1 > 9\)", r"\(x > 4\), dus \(\left]4, +\infty\right[\)"),
                          (r"\(-4x \geq 12\)", r"\(x \leq -3\), dus \(\left]-\infty, -3\right]\)"),
                          (r"\(-x + 2 < 5\)", r"\(x > -3\), dus \(\left]-3, +\infty\right[\)"),
                          (r"\(3x \leq 15\)", r"\(x \leq 5\), dus \(\left]-\infty, 5\right]\)"),
                          (r"\(-2x > 6\)", r"\(x < -3\), dus \(\left]-\infty, -3\right[\)")],
                  "Oplossing en interval", WL),
             ]),
        dict(kop="Formules omvormen",
             opdracht="Vorm om naar de gevraagde letter.",
             oefeningen=[
                 ("rij", [(r"\(\rho = \tfrac{m}{V}\), naar \(V\)", r"\(V = \tfrac{m}{\rho}\)"),
                          (r"\(U = I \cdot R\), naar \(I\)", r"\(I = \tfrac{U}{R}\)"),
                          (r"\(F = m \cdot g\), naar \(g\)", r"\(g = \tfrac{F}{m}\)"),
                          (r"\(A = z^{2}\), naar \(z\)", r"\(z = \sqrt{A}\)")],
                  "Omgevormd", WW),
                 ("rij", [(r"\(x = x_{0} + v \cdot t\), naar \(v\)", r"\(v = \tfrac{x - x_{0}}{t}\)"),
                          (r"\(E_{k} = \tfrac{1}{2}mv^{2}\), naar \(m\)", r"\(m = \tfrac{2E_{k}}{v^{2}}\)"),
                          (r"\(c = \tfrac{n}{V}\), naar \(n\)", r"\(n = c \cdot V\)"),
                          (r"\(y = ax + b\), naar \(x\)", r"\(x = \tfrac{y - b}{a}\)")],
                  "Omgevormd", WW),
             ]),
        dict(kop="Rekenen met die formules",
             opdracht="Vul in en reken uit. Zet de eenheid erbij.",
             oefeningen=[
                 ("rij", [(r"massa van \(5\) liter olie met \(\rho = 0{,}9\) kg/l", r"\(4{,}5\) kg"),
                          (r"weerstand bij \(U = 24\) volt en \(I = 4\) ampère", r"\(6\) ohm"),
                          (r"zijde van een vierkant met oppervlakte \(81\)", r"\(9\)"),
                          (r"massa bij \(F = 50\) N en \(g = 10\) N/kg", r"\(5\) kg"),
                          (r"druk bij \(F = 60\) N op \(A = 0{,}2\) m²", r"\(300\) Pa")],
                  "Antwoord", WW),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Kies een onbekende, schrijf op waar ze voor staat, los op en controleer.",
             oefeningen=[
                 ("open", r"Een taxi vraagt \(5\) euro opstap en \(2\) euro per kilometer. Je betaalt "
                          r"\(31\) euro. Hoeveel kilometer heb je gereden?",
                  r"\(5 + 2x = 31\), dus \(2x = 26\) en \(x = 13\) kilometer. Controle: \(5 + 26 = 31\).", 6),
                 ("open", r"Abonnement A kost \(15\) euro plus \(0{,}05\) euro per minuut, B kost \(5\) euro "
                          r"plus \(0{,}15\) euro per minuut. Vanaf hoeveel minuten is A goedkoper?",
                  r"\(15 + 0{,}05x = 5 + 0{,}15x\) geeft \(10 = 0{,}10x\), dus \(x = 100\). Vanaf meer dan "
                  r"\(100\) minuten is A goedkoper.", 6),
                 ("open", r"De som van drie opeenvolgende even getallen is \(66\). Welke getallen zijn het?",
                  r"\(x + (x + 2) + (x + 4) = 66\), dus \(3x = 60\) en \(x = 20\). De getallen zijn \(20\), "
                  r"\(22\) en \(24\).", 6),
             ]),
        dict(kop="Grafisch kijken",
             opdracht="Antwoord in één of twee zinnen.",
             oefeningen=[
                 ("open", r"Hoe los je \(2x + 1 = x + 4\) grafisch op?",
                  r"Teken \(y = 2x + 1\) en \(y = x + 4\) en zoek het snijpunt. De \(x\)-waarde daarvan, "
                  r"\(x = 3\), is de oplossing.", 4),
                 ("open", r"Waar lees je de oplossing van \(f(x) > 0\) af?",
                  r"Uit het tekenverloop: daar waar de grafiek boven de \(x\)-as ligt.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij delen door een positief getal draait het ongelijkheidsteken om.", False),
                 ("waar", r"Je mag beide leden van een gelijkheid met \(-1\) vermenigvuldigen.", True),
                 ("waar", "Je mag beide leden delen door een letter die nul kan zijn.", False),
                 ("waar", r"Bij \(E_{k} = \tfrac{1}{2}mv^{2}\) is de energie recht evenredig met \(v\).", False),
                 ("waar", r"\(3x + 5x = 8x\).", True),
                 ("waar", r"\(-2(x - 5) = -2x - 10\).", False),
                 ("waar", r"Komt er \(0 = 0\) uit, dan is elke \(x\) een oplossing.", True),
             ]),
    ],
)


# ============================================================
OEFENBUNDELS["oefenbundel-stelsels-en-tweedegraadsvergelijkingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stelsels en tweedegraadsvergelijkingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke methode ligt hier het meest voor de hand?",
             opdracht="Schrijf substitutie, combinatie of gelijkstelling.",
             oefeningen=[
                 ("rij", [(r"\(y = 3x\) en \(x + y = 12\)", "substitutie"),
                          (r"\(x + y = 9\) en \(x - y = 3\)", "combinatie"),
                          (r"\(y = 2x + 1\) en \(y = 5x - 8\)", "gelijkstelling"),
                          (r"\(2x + 3y = 12\) en \(2x - 3y = 0\)", "combinatie")],
                  "Methode", WW),
             ]),
        dict(kop="Stelsels met substitutie",
             opdracht="Los op met de substitutiemethode.",
             oefeningen=[
                 ("rij", [(r"\(y = 4x\) en \(x + y = 20\)", r"\((4, 16)\)"),
                          (r"\(y = x + 2\) en \(2x + y = 11\)", r"\((3, 5)\)"),
                          (r"\(x = 2y\) en \(x + 3y = 25\)", r"\((10, 5)\)"),
                          (r"\(y = 10 - x\) en \(3x + y = 18\)", r"\((4, 6)\)")],
                  "Oplossing", WW),
             ]),
        dict(kop="Stelsels met combinatie",
             opdracht="Los op door de vergelijkingen op te tellen of af te trekken.",
             oefeningen=[
                 ("rij", [(r"\(x + y = 14\) en \(x - y = 6\)", r"\((10, 4)\)"),
                          (r"\(x + 2y = 13\) en \(x - y = 1\)", r"\((5, 4)\)"),
                          (r"\(3x + y = 17\) en \(x + y = 7\)", r"\((5, 2)\)"),
                          (r"\(2x + 3y = 16\) en \(2x - y = 0\)", r"\((2, 4)\)")],
                  "Oplossing", WW),
             ]),
        dict(kop="Bepaald, strijdig of onbepaald?",
             opdracht="Los op en schrijf erbij welk soort stelsel het is, en hoe de rechten liggen.",
             oefeningen=[
                 ("open", r"\(\left\{\begin{array}{l} x + y = 5 \\ 2x + 2y = 10 \end{array}\right.\)",
                  r"Je krijgt \(0 = 0\): onbepaald, oneindig veel oplossingen. De rechten vallen samen.", 3),
                 ("open", r"\(\left\{\begin{array}{l} x + y = 5 \\ x + y = 9 \end{array}\right.\)",
                  r"Je krijgt \(0 = 4\): strijdig, geen oplossing, \(S = \emptyset\). De rechten zijn evenwijdig.", 3),
             ]),
        dict(kop="Van tekening naar soort",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Twee rechten van een stelsel lopen evenwijdig en vallen niet samen. "
                          "Welk soort stelsel is het?",
                  ["bepaald", "strijdig", "onbepaald", "dat hangt van de methode af"], 1),
             ]),
        dict(kop="Nog een stelsel om te benoemen",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("open", r"\(\left\{\begin{array}{l} x + y = 5 \\ x - y = 1 \end{array}\right.\)",
                  r"Bepaald: \((3, 2)\). De rechten snijden in één punt.", 3),
             ]),
        dict(kop="Onvolledige vierkantsvergelijkingen",
             opdracht="Los op zonder de formule.",
             oefeningen=[
                 ("rij", [(r"\(x^{2} - 36 = 0\)", r"\(6\) en \(-6\)"),
                          (r"\(x^{2} = 81\)", r"\(9\) en \(-9\)"),
                          (r"\(x^{2} - 7x = 0\)", r"\(0\) en \(7\)"),
                          (r"\(2x^{2} - 8 = 0\)", r"\(2\) en \(-2\)")],
                  "Oplossingen", WW),
             ]),
        dict(kop="Nog vier onvolledige",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("rij", [(r"\(x^{2} - 121 = 0\)", r"\(11\) en \(-11\)"),
                          (r"\(3x^{2} = 75\)", r"\(5\) en \(-5\)"),
                          (r"\(x^{2} + 4x = 0\)", r"\(0\) en \(-4\)"),
                          (r"\(x^{2} + 16 = 0\)", r"geen reële oplossing")],
                  "Oplossingen", WW),
             ]),
        dict(kop="Vraagstukken met twee onbekenden",
             opdracht="Noteer eerst waar elke letter voor staat.",
             oefeningen=[
                 ("open", "Drie broden en twee pakken melk kosten 11 euro; één brood en twee pakken "
                          "melk kosten 7 euro. Wat kost een brood, en wat kost een pak melk?",
                  r"\(3b + 2m = 11\) en \(b + 2m = 7\). Aftrekken geeft \(2b = 4\), dus \(b = 2\) euro "
                  r"en \(m = 2{,}50\) euro.", 6),
                 ("open", "Twee getallen zijn samen 40 en verschillen 12. Welke zijn het?",
                  r"\(x + y = 40\) en \(x - y = 12\), dus \(2x = 52\), \(x = 26\) en \(y = 14\).", 5),
             ]),
        dict(kop="De discriminant berekenen",
             opdracht=r"Bereken \(D = b^{2} - 4ac\) en schrijf op hoeveel reële oplossingen er zijn.",
             oefeningen=[
                 ("rij", [(r"\(x^{2} - 6x + 9 = 0\)", r"\(D = 0\), één oplossing"),
                          (r"\(x^{2} - 5x + 6 = 0\)", r"\(D = 1\), twee oplossingen"),
                          (r"\(x^{2} + 2x + 5 = 0\)", r"\(D = -16\), geen oplossing"),
                          (r"\(2x^{2} - 3x - 2 = 0\)", r"\(D = 25\), twee oplossingen")],
                  "D en aantal", WL),
             ]),
        dict(kop="Nog twee vraagstukken",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("open", "In een stal staan kippen en konijnen: samen 20 dieren en 56 poten. "
                          "Hoeveel van elk?",
                  r"\(k + n = 20\) en \(2k + 4n = 56\). Uit de eerste \(k = 20 - n\), invullen geeft "
                  r"\(40 + 2n = 56\), dus \(n = 8\) konijnen en \(k = 12\) kippen.", 6),
                 ("open", "Een vader is nu drie keer zo oud als zijn dochter. Samen zijn ze 48 jaar. "
                          "Hoe oud is elk?",
                  r"\(v = 3d\) en \(v + d = 48\), dus \(4d = 48\): de dochter is 12 en de vader 36.", 5),
             ]),
        dict(kop="Van teken naar grafiek",
             opdracht=r"Vul aan: hoe ligt de parabool tegenover de \(x\)-as?",
             oefeningen=[
                 ("tabel", ["Discriminant", "Aantal nulwaarden", "De parabool"],
                  [[r"\(D > 0\)", None, None], [r"\(D = 0\)", None, None], [r"\(D < 0\)", None, None]],
                  r"\(D > 0\): twee nulwaarden, de parabool snijdt de \(x\)-as. \(D = 0\): één, ze raakt "
                  r"de \(x\)-as. \(D < 0\): geen, ze ligt er helemaal naast.", WL),
             ]),
        dict(kop="Met de formule oplossen",
             opdracht=r"Gebruik \(x = \dfrac{-b \pm \sqrt{D}}{2a}\).",
             oefeningen=[
                 ("rij", [(r"\(x^{2} - 5x + 6 = 0\)", r"\(2\) en \(3\)"),
                          (r"\(x^{2} + x - 12 = 0\)", r"\(3\) en \(-4\)"),
                          (r"\(2x^{2} - 7x + 3 = 0\)", r"\(3\) en \(\tfrac{1}{2}\)")],
                  "Oplossingen", WW),
             ]),
        dict(kop="Ontbinden en de nulwaarden",
             opdracht="Ontbind en schrijf de nulwaarden op.",
             oefeningen=[
                 ("rij", [(r"\(x^{2} - 49\)", r"\((x + 7)(x - 7)\), nulwaarden \(7\) en \(-7\)"),
                          (r"\(x^{2} + 10x + 25\)", r"\((x + 5)^{2}\), nulwaarde \(-5\)"),
                          (r"\(x^{2} - 7x + 12\)", r"\((x - 3)(x - 4)\), nulwaarden \(3\) en \(4\)")],
                  "Ontbinding en nulwaarden", WL),
             ]),
        dict(kop="Nog drie ontbindingen",
             opdracht="Zelfde werkwijze.",
             oefeningen=[
                 ("rij", [(r"\(x^{2} - 1\)", r"\((x + 1)(x - 1)\), nulwaarden \(1\) en \(-1\)"),
                          (r"\(x^{2} - 8x + 16\)", r"\((x - 4)^{2}\), nulwaarde \(4\)"),
                          (r"\(x^{2} + 5x + 6\)", r"\((x + 2)(x + 3)\), nulwaarden \(-2\) en \(-3\)")],
                  "Ontbinding en nulwaarden", WL),
             ]),
        dict(kop="Fouten zoeken",
             opdracht="Zoek de fout en schrijf op hoe het wel moet.",
             oefeningen=[
                 ("open", r"Iemand schrijft \(x^{2} + 9 = (x + 3)(x - 3)\).",
                  r"Dat laatste geeft uitgewerkt \(x^{2} - 9\). Alleen een verschil van twee kwadraten "
                  r"ontbindt zo; \(x^{2} + 9\) heeft in \(\mathbb{R}\) geen nulwaarden.", 4),
                 ("open", r"Iemand lost \(x^{2} < 9\) op en schrijft \(x < 3\).",
                  r"De negatieve kant ontbreekt: \(x\) moet tussen \(-3\) en \(3\) liggen, dus "
                  r"\(\left]-3, 3\right[\).", 4),
             ]),
        dict(kop="Ongelijkheden van de tweede graad",
             opdracht="Schrijf de oplossingenverzameling als interval.",
             oefeningen=[
                 ("rij", [(r"\(x^{2} < 16\)", r"\(\left]-4, 4\right[\)"),
                          (r"\(x^{2} \leq 25\)", r"\(\left[-5, 5\right]\)"),
                          (r"\(x^{2} > 9\)", r"\(\left]-\infty, -3\right[ \cup \left]3, +\infty\right[\)")],
                  "Interval", WL),
             ]),
        dict(kop="Tweedegraadsvraagstukken",
             opdracht="Stel eerst de vergelijking op, los dan op, en controleer bij het verhaal.",
             oefeningen=[
                 ("open", r"Een rechthoek is 2 meter langer dan breed en heeft een oppervlakte van "
                          r"\(48\) m\(^{2}\). Hoe breed is hij?",
                  r"\(x(x + 2) = 48\), dus \(x^{2} + 2x - 48 = 0\) met oplossingen \(6\) en \(-8\). De "
                  r"breedte is 6 m; \(-8\) valt weg want een breedte kan niet negatief zijn.", 6),
                 ("open", "Het product van twee opeenvolgende gehele getallen is 72. Welke zijn het?",
                  r"\(x(x + 1) = 72\) geeft \(x^{2} + x - 72 = 0\) met oplossingen \(8\) en \(-9\). Dus "
                  r"8 en 9, of \(-9\) en \(-8\).", 6),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Waarom helpt ontbinden je aan de oplossingen van \(x^{2} - 5x + 6 = 0\)?",
                  r"Omdat \(x^{2} - 5x + 6 = (x - 2)(x - 3)\), en een product is nul zodra minstens één "
                  r"factor nul is. Dus \(x = 2\) of \(x = 3\).", 5),
                 ("open", r"Wat betekent het als je tijdens het oplossen van een stelsel \(0 = 0\) "
                          r"overhoudt?",
                  "Allebei de onbekenden zijn weggevallen en wat overblijft klopt altijd: het stelsel is "
                  "onbepaald, de twee rechten vallen samen en er zijn oneindig veel oplossingen.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", r"De oplossing van een stelsel is een koppel \((x, y)\), niet één getal.", True),
                 ("waar", "Een strijdig stelsel hoort bij twee samenvallende rechten.", False),
                 ("waar", "Een vierkantsvergelijking heeft altijd twee reële oplossingen.", False),
                 ("waar", r"\(x^{2} + 4\) is te ontbinden als \((x + 2)(x - 2)\).", False),
                 ("waar", "Grafisch oplossen geeft altijd een exact antwoord.", False),
                 ("waar", "De drie algebraïsche methodes geven altijd dezelfde oplossing.", True),
             ]),
        dict(kop="Doordenkers",
             opdracht="Neem je tijd.",
             oefeningen=[
                 ("open", r"Voor welke waarde van \(c\) heeft \(x^{2} - 6x + c = 0\) precies één "
                          r"oplossing?",
                  r"Eén oplossing betekent \(D = 0\), dus \(36 - 4c = 0\) en \(c = 9\). De vergelijking "
                  r"is dan \((x - 3)^{2} = 0\).", 5),
                 ("open", "Een stelsel van twee vergelijkingen in twee onbekenden kan geen, één of "
                          "oneindig veel oplossingen hebben. Waarom kan het er nooit precies twee hebben?",
                  "Elke vergelijking is een rechte. Twee verschillende rechten snijden in hoogstens één "
                  "punt; vallen ze samen, dan hebben ze alle punten gemeen. Precies twee gemeenschappelijke "
                  "punten kan dus niet.", 6),
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
                 ("kies", r"een rechte met voorschrift \(y = 2x - 1\)",
                  ["wel een functie", "geen functie"], 0),
                 ("kies", r"de verticale rechte \(x = 3\)", ["wel een functie", "geen functie"], 1),
                 ("kies", r"de parabool \(y = x^{2}\)", ["wel een functie", "geen functie"], 0),
                 ("kies", "een cirkel rond de oorsprong", ["wel een functie", "geen functie"], 1),
                 ("kies", r"de horizontale rechte \(y = 4\)", ["wel een functie", "geen functie"], 0),
             ]),
        dict(kop="Functiewaarden",
             opdracht=r"Voor \(f(x) = 5x - 3\). Vul in.",
             oefeningen=[
                 ("rij", [(r"\(f(0)\)", r"\(-3\)"), (r"\(f(2)\)", r"\(7\)"),
                          (r"\(f(-1)\)", r"\(-8\)"), (r"\(f(10)\)", r"\(47\)"),
                          (r"de \(x\) waarvoor \(f(x) = 17\)", r"\(4\)")],
                  "Antwoord", W),
             ]),
        dict(kop="Wat voor groei?",
             opdracht="Bekijk de verschillen en schrijf op of het lineair is of niet.",
             oefeningen=[
                 ("rij", [(r"\(1 \to 5\), \(2 \to 9\), \(3 \to 13\)", r"lineair, telkens \(+4\)"),
                          (r"\(1 \to 2\), \(2 \to 8\), \(3 \to 18\)", "niet lineair"),
                          (r"\(1 \to 10\), \(2 \to 7\), \(3 \to 4\)", r"lineair, telkens \(-3\)"),
                          (r"\(1 \to 3\), \(2 \to 6\), \(3 \to 12\)", "niet lineair")],
                  "Soort groei", WL),
             ]),
        dict(kop="De richtingscoëfficiënt",
             opdracht="Bereken de rico uit de twee punten.",
             oefeningen=[
                 ("rij", [(r"\((0, 1)\) en \((3, 10)\)", r"\(3\)"),
                          (r"\((2, 8)\) en \((6, 4)\)", r"\(-1\)"),
                          (r"\((1, 5)\) en \((5, 5)\)", r"\(0\)"),
                          (r"\((-2, 0)\) en \((2, 8)\)", r"\(2\)"),
                          (r"\((0, 0)\) en \((4, 10)\)", r"\(\tfrac{5}{2}\)")],
                  "rico", W),
             ]),
        dict(kop="Stijgt of daalt?",
             opdracht="Duid aan wat de rechte doet van links naar rechts.",
             oefeningen=[
                 ("kies", r"\(y = -3x + 1\)", ["ze daalt", "ze stijgt"], 0),
                 ("kies", r"\(y = \tfrac{1}{2}x - 4\)", ["ze daalt", "ze stijgt"], 1),
             ]),
        dict(kop="De vergelijking opstellen",
             opdracht="Schrijf het voorschrift van de rechte.",
             oefeningen=[
                 ("rij", [(r"rico \(5\), door \((0, -2)\)", r"\(y = 5x - 2\)"),
                          (r"rico \(3\), door \((2, 10)\)", r"\(y = 3x + 4\)"),
                          (r"door \((0, 4)\) en \((2, 10)\)", r"\(y = 3x + 4\)"),
                          (r"door \((1, 1)\) en \((3, 7)\)", r"\(y = 3x - 2\)"),
                          (r"rico \(-2\), door \((3, 1)\)", r"\(y = -2x + 7\)")],
                  "Voorschrift", WW),
             ]),
        dict(kop="Van tabel naar voorschrift",
             opdracht="De groei is lineair. Schrijf het voorschrift.",
             oefeningen=[
                 ("rij", [(r"\(0 \to 2\), \(1 \to 5\), \(2 \to 8\)", r"\(y = 3x + 2\)"),
                          (r"\(0 \to 7\), \(1 \to 5\), \(2 \to 3\)", r"\(y = -2x + 7\)"),
                          (r"\(0 \to 0\), \(1 \to 4\), \(2 \to 8\)", r"\(y = 4x\)")],
                  "Voorschrift", WW),
             ]),
        dict(kop="Snijpunten",
             opdracht="Bereken beide snijpunten met de assen.",
             oefeningen=[
                 ("rij", [(r"\(y = 2x - 10\)", r"\((5, 0)\) en \((0, -10)\)"),
                          (r"\(y = -x + 6\)", r"\((6, 0)\) en \((0, 6)\)"),
                          (r"\(y = 4x + 8\)", r"\((-2, 0)\) en \((0, 8)\)"),
                          (r"\(y = 3x - 9\)", r"\((3, 0)\) en \((0, -9)\)")],
                  "Snijpunten", WL),
             ]),
        dict(kop="Lineair of recht evenredig?",
             opdracht="Duid aan wat het verband is.",
             oefeningen=[
                 ("kies", r"\(y = 7x\)", ["recht evenredig", "wel lineair, niet recht evenredig"], 0),
                 ("kies", r"\(y = 7x + 2\)", ["recht evenredig", "wel lineair, niet recht evenredig"], 1),
                 ("kies", r"de kost van benzine aan \(1{,}80\) euro per liter",
                  ["recht evenredig", "wel lineair, niet recht evenredig"], 0),
                 ("kies", r"een taxirit met \(4\) euro opstap en \(1{,}50\) euro per km",
                  ["recht evenredig", "wel lineair, niet recht evenredig"], 1),
             ]),
        dict(kop="Modellen opstellen",
             opdracht=r"Schrijf het voorschrift, met erbij wat \(a\) en \(b\) betekenen.",
             oefeningen=[
                 ("open", r"Een wandelaar vertrekt op kilometerpaal \(3\) en loopt \(5\) km per uur.",
                  r"\(s = 5t + 3\). \(a = 5\) is de snelheid, \(b = 3\) de beginpositie.", 4),
                 ("open", r"Een zaal huren kost \(120\) euro plus \(3\) euro per stoel.",
                  r"\(k = 3n + 120\). \(a = 3\) is de prijs per stoel, \(b = 120\) de vaste kost.", 4),
                 ("open", r"Een bestelwagen van \(30\,000\) euro wordt in \(12\) jaar lineair tot nul "
                          r"afgeschreven. Schrijf het voorschrift en de waarde na \(5\) jaar.",
                  r"\(w = 30\,000 - 2\,500t\). Na \(5\) jaar: \(30\,000 - 12\,500 = 17\,500\) euro.", 5),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in één of twee zinnen.",
             oefeningen=[
                 ("open", r"Waarom hoort bij een grafiek altijd een ijk op de assen?",
                  "Zonder getallen op de assen kan je geen enkele waarde aflezen; dan toont de "
                  "tekening alleen nog een vorm.", 3),
                 ("open", r"Waarom is een taxirit met opstapgeld wel lineair maar niet recht evenredig?",
                  "Door de opstapprijs gaat de rechte niet door de oorsprong, dus tweemaal zoveel "
                  "kilometer kost geen tweemaal zoveel geld.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", r"Bij een functie mogen bij dezelfde \(x\) twee verschillende \(y\)-waarden horen.",
                  False),
                 ("waar", "Een rechte met rico nul loopt horizontaal.", True),
                 ("waar", "Evenwijdige rechten hebben dezelfde richtingscoëfficiënt.", True),
                 ("waar", r"Het domein van \(f(x) = \tfrac{1}{x}\) bevat ook het getal \(0\).", False),
                 ("waar", r"Bij \(y = x^{2}\) hoort \(y = 4\) bij twee verschillende \(x\)-waarden.", True),
                 ("waar", r"De afhankelijke variabele staat op de \(x\)-as.", False),
                 ("waar", r"Bij \(y = ax + b\) is \(b\) het snijpunt met de \(y\)-as.", True),
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
                 ("rij", [(r"\(y = (x - 4)^{2} + 1\)", r"boven, top \((4, 1)\)"),
                          (r"\(y = -(x + 2)^{2} + 5\)", r"beneden, top \((-2, 5)\)"),
                          (r"\(y = 3(x - 1)^{2} - 7\)", r"boven, top \((1, -7)\)"),
                          (r"\(y = -2(x + 3)^{2}\)", r"beneden, top \((-3, 0)\)")],
                  "Opening en top", WL),
             ]),
        dict(kop="Nulwaarden",
             opdracht="Bereken de nulwaarden, of schrijf op dat er geen zijn.",
             oefeningen=[
                 ("rij", [(r"\(f(x) = x^{2} - 25\)", r"\(5\) en \(-5\)"),
                          (r"\(f(x) = x^{2} + 1\)", "geen"),
                          (r"\(f(x) = (x - 3)^{2}\)", r"\(3\), dubbel"),
                          (r"\(f(x) = x^{2} - 4x\)", r"\(0\) en \(4\)")],
                  "Nulwaarden", WW),
             ]),
        dict(kop="De symmetrieas",
             opdracht="Schrijf de vergelijking van de symmetrieas.",
             oefeningen=[
                 ("rij", [(r"nulwaarden \(-1\) en \(7\)", r"\(x = 3\)"),
                          (r"nulwaarden \(2\) en \(10\)", r"\(x = 6\)"),
                          (r"top \((-5, 2)\)", r"\(x = -5\)"),
                          (r"nulwaarden \(-4\) en \(4\)", r"\(x = 0\)")],
                  "Symmetrieas", W),
             ]),
        dict(kop="Het snijpunt met de verticale as",
             opdracht=r"Vul \(x = 0\) in en schrijf het snijpunt met de \(y\)-as op.",
             oefeningen=[
                 ("rij", [(r"\(f(x) = x^{2} - 2x - 8\)", r"\((0, -8)\)"),
                          (r"\(f(x) = 2x^{2} + 5\)", r"\((0, 5)\)"),
                          (r"\(f(x) = (x - 3)^{2}\)", r"\((0, 9)\)"),
                          (r"\(f(x) = -x^{2} + 4x - 1\)", r"\((0, -1)\)")],
                  "Snijpunt", WW),
             ]),
        dict(kop="Van topvorm naar kenmerken",
             opdracht="Vul de top en het bereik aan.",
             oefeningen=[
                 ("tabel", ["voorschrift", "top", "bereik"],
                  [[r"\(y = (x - 1)^{2} + 3\)", None, None],
                   [r"\(y = -(x + 2)^{2} + 1\)", None, None],
                   [r"\(y = 2(x - 4)^{2}\)", None, None]],
                  r"\((1, 3)\) en \(\left[3, +\infty\right[\) · "
                  r"\((-2, 1)\) en \(\left]-\infty, 1\right]\) · "
                  r"\((4, 0)\) en \(\left[0, +\infty\right[\)", "160px"),
             ]),
        dict(kop="Wat doet de transformatie?",
             opdracht=r"Vertrek van \(y = x^{2}\) en schrijf op wat er met de grafiek gebeurt.",
             oefeningen=[
                 ("rij", [(r"\(y = x^{2} + 4\)", "vier omhoog"),
                          (r"\(y = (x - 6)^{2}\)", "zes naar rechts"),
                          (r"\(y = (x + 1)^{2}\)", "één naar links"),
                          (r"\(y = -x^{2}\)", "gespiegeld om de horizontale as")],
                  "Wat gebeurt er?", WL),
                 ("rij", [(r"\(y = 4x^{2}\)", "smaller, verticaal uitgerekt"),
                          (r"\(y = 0{,}25x^{2}\)", "breder, samengedrukt")],
                  "Wat gebeurt er?", WL),
             ]),
        dict(kop="Minimum of maximum",
             opdracht="Schrijf op of de functie een minimum of een maximum heeft, en welke waarde dat is.",
             oefeningen=[
                 ("rij", [(r"\(f(x) = (x - 2)^{2} + 7\)", r"minimum \(7\)"),
                          (r"\(f(x) = -(x + 1)^{2} + 3\)", r"maximum \(3\)"),
                          (r"\(f(x) = x^{2} - 9\)", r"minimum \(-9\)")],
                  "Extremum", WW),
             ]),
        dict(kop="Stijgen en dalen",
             opdracht="Schrijf op waar de functie daalt en waar ze stijgt.",
             oefeningen=[
                 ("rij", [(r"\(f(x) = x^{2} - 6x\)", r"daalt links van \(3\), stijgt rechts"),
                          (r"\(f(x) = -x^{2} + 8x\)", r"stijgt links van \(4\), daalt rechts")],
                  "Verloop", WL),
                 ("rij", [(r"\(f(x) = (x + 2)^{2} - 5\)",
                           r"daalt links van \(-2\), stijgt rechts"),
                          (r"\(f(x) = -3(x - 1)^{2}\)",
                           r"stijgt links van \(1\), daalt rechts")],
                  "Verloop", WL),
             ]),
        dict(kop="Domein en bereik",
             opdracht="Schrijf domein en bereik op.",
             oefeningen=[
                 ("tabel", ["functie", "domein", "bereik"],
                  [[r"\(f(x) = x^{2}\)", None, None],
                   [r"\(f(x) = (x - 2)^{2} + 3\)", None, None],
                   [r"\(f(x) = -x^{2} + 1\)", None, None],
                   [r"\(f(x) = \dfrac{1}{x}\)", None, None]],
                  r"\(\mathbb{R}\) en \(\left[0, +\infty\right[\) · "
                  r"\(\mathbb{R}\) en \(\left[3, +\infty\right[\) · "
                  r"\(\mathbb{R}\) en \(\left]-\infty, 1\right]\) · "
                  r"\(\mathbb{R} \setminus \{0\}\) en \(\mathbb{R} \setminus \{0\}\)", "170px"),
             ]),
        dict(kop="Welke vorm gebruik je?",
             opdracht="Schrijf op welke vorm van het voorschrift je het snelst het gevraagde geeft.",
             oefeningen=[
                 ("rij", [("je zoekt de nulwaarden", r"de productvorm \(a(x - x_{1})(x - x_{2})\)"),
                          ("je zoekt de top", r"de topvorm \(a(x - p)^{2} + q\)"),
                          (r"je zoekt het snijpunt met de \(y\)-as", r"de vorm \(ax^{2} + bx + c\)")],
                  "Welke vorm?", WL),
             ]),
        dict(kop="Voorschrift opstellen",
             opdracht="Schrijf een voorschrift dat aan de voorwaarde voldoet.",
             oefeningen=[
                 ("rij", [(r"nulwaarden \(3\) en \(8\)", r"\(f(x) = (x - 3)(x - 8)\)"),
                          (r"nulwaarden \(-2\) en \(5\)", r"\(f(x) = (x + 2)(x - 5)\)"),
                          (r"top \((2, -4)\), opent naar boven", r"\(f(x) = (x - 2)^{2} - 4\)"),
                          (r"top \((0, 6)\), opent naar beneden", r"\(f(x) = -x^{2} + 6\)")],
                  "Voorschrift", WL),
             ]),
        dict(kop="Functiewaarden",
             opdracht=r"Bereken, met \(f(x) = x^{2} - 3x + 2\).",
             oefeningen=[
                 ("rij", [(r"\(f(0)\)", r"\(2\)"), (r"\(f(1)\)", r"\(0\)"),
                          (r"\(f(-2)\)", r"\(12\)"), (r"\(f(4)\)", r"\(6\)")],
                  "Functiewaarde", W),
             ]),
        dict(kop="De hyperbool",
             opdracht=r"Over \(f(x) = \dfrac{12}{x}\).",
             oefeningen=[
                 ("rij", [(r"\(f(3)\)", r"\(4\)"), (r"\(f(-6)\)", r"\(-2\)"),
                          (r"de \(x\) waarvoor \(f(x) = 2\)", r"\(6\)")],
                  "Antwoord", W),
                 ("open", "Waarom heeft deze functie geen nulwaarde, en wat doet de grafiek bij de "
                          "verticale as?",
                  r"Een breuk met teller \(12\) wordt nooit nul. De grafiek nadert de verticale as "
                  r"maar raakt hem nooit.", 4),
             ]),
        dict(kop="Kies het juiste antwoord",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", r"De grafiek van \(y = (x - 5)^{2}\) ligt ten opzichte van \(y = x^{2}\)",
                  ["vijf naar links", "vijf naar rechts", "vijf omhoog"], 1),
                 ("kies", r"Het domein van \(f(x) = \dfrac{4}{x}\) is",
                  [r"\(\mathbb{R}\)", r"\(\mathbb{R} \setminus \{0\}\)",
                   r"\(\left]0, +\infty\right[\)"], 1),
             ]),
        dict(kop="Uitleggen",
             opdracht="Schrijf je uitleg in volle zinnen.",
             oefeningen=[
                 ("open", r"Leg uit waarom \(f(x) = x^{2} + 4\) geen nulwaarde heeft.",
                  r"Een kwadraat is nooit negatief, dus \(x^{2} + 4 \geq 4\): nooit nul.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", r"Elke parabool snijdt de \(x\)-as in twee punten.", False),
                 ("waar", "Een parabool die naar boven opent heeft een minimum maar geen maximum.", True),
                 ("waar", "Het tekenverloop toont waar de functie stijgt en daalt.", False),
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
                 ("rij", [("3 jassen en 5 mutsen", r"\(3 \cdot 5 = 15\)"),
                          ("2 soepen, 4 hoofdgerechten, 3 desserts", r"\(2 \cdot 4 \cdot 3 = 24\)"),
                          ("een code van 4 cijfers van 0 tot 9", r"\(10^{4} = 10\,000\)"),
                          ("vier keer met een munt gooien", r"\(2^{4} = 16\)")],
                  "Aantal", WW),
                 ("rij", [("een nummerplaat van 3 letters en 3 cijfers",
                           r"\(26^{3} \cdot 10^{3} = 17\,576\,000\)"),
                          ("een wachtwoord van 2 tekens uit 36", r"\(36^{2} = 1296\)")],
                  "Aantal", WW),
             ]),
        dict(kop="Schrijf als macht",
             opdracht="Schrijf de berekening als een macht en reken ze uit.",
             oefeningen=[
                 ("rij", [("zes keer met een munt gooien", r"\(2^{6} = 64\)"),
                          ("drie dobbelstenen gooien", r"\(6^{3} = 216\)"),
                          ("vijf schijven met elk 4 tekens", r"\(4^{5} = 1024\)")],
                  "Macht", WW),
             ]),
        dict(kop="Een boomdiagram tekenen",
             opdracht="Teken het diagram in de ruimte hiernaast en tel daarna de paden.",
             oefeningen=[
                 ("open", "Je kiest eerst een voorgerecht uit 2 en daarna een hoofdgerecht uit 3. "
                          "Teken het boomdiagram en tel de paden.",
                  r"Uit het beginpunt vertrekken \(2\) takken, elk splitst in \(3\): samen "
                  r"\(2 \cdot 3 = 6\) paden.", 8),
             ]),
        dict(kop="Met of zonder terugleggen",
             opdracht="Reken uit en schrijf erbij of er teruggelegd wordt.",
             oefeningen=[
                 ("rij", [("uit 6 lopers de eerste drie plaatsen",
                           r"\(6 \cdot 5 \cdot 4 = 120\), zonder terugleggen"),
                          ("drie keer een cijfer van 1 tot 6 kiezen, herhaling mag",
                           r"\(6^{3} = 216\), met terugleggen"),
                          ("uit 5 kaarten er 2 na elkaar trekken zonder terugleggen",
                           r"\(5 \cdot 4 = 20\), zonder terugleggen"),
                          ("uit 8 boeken er 2 kiezen voor de eerste en de tweede plank",
                           r"\(8 \cdot 7 = 56\), zonder terugleggen")],
                  "Aantal en soort", WL),
             ]),
        dict(kop="De somregel",
             opdracht="Bereken hoeveel er minstens aan één voorwaarde voldoen.",
             oefeningen=[
                 ("rij", [("20 leerlingen, 12 voetbal, 9 tennis, 4 allebei", r"\(12 + 9 - 4 = 17\)"),
                          ("50 mensen, 30 koffie, 25 thee, 10 allebei", r"\(30 + 25 - 10 = 45\)"),
                          ("36 leerlingen, 20 Spaans, 16 Duits, 5 allebei", r"\(20 + 16 - 5 = 31\)")],
                  "Minstens één", WW),
             ]),
        dict(kop="De complementregel",
             opdracht="Bereken hoeveel er aan geen van beide voldoen.",
             oefeningen=[
                 ("rij", [("20 leerlingen, 17 doen minstens één sport", r"\(20 - 17 = 3\)"),
                          ("50 mensen, 45 drinken minstens één van beide", r"\(50 - 45 = 5\)"),
                          ("36 leerlingen, 31 volgen minstens één taal", r"\(36 - 31 = 5\)")],
                  "Geen van beide", WW),
             ]),
        dict(kop="Hoeveel horen er enkel bij de ene groep?",
             opdracht="Trek de doorsnede van die groep af.",
             oefeningen=[
                 ("rij", [("30 mensen, 18 vlees, 14 vis, 7 allebei: enkel vis", r"\(14 - 7 = 7\)"),
                          ("25 kinderen, 14 een hond, 11 een kat, 5 allebei: enkel een hond",
                           r"\(14 - 5 = 9\)"),
                          ("40 leerlingen, 22 Frans, 18 Duits, 6 allebei: enkel Duits",
                           r"\(18 - 6 = 12\)")],
                  "Enkel", WW),
             ]),
        dict(kop="Het venndiagram invullen",
             opdracht="Van 28 leerlingen spelen er 15 voetbal, 13 basket en 6 allebei. Vul in.",
             oefeningen=[
                 ("tabel", ["vakje", "aantal"],
                  [["enkel voetbal", None], ["allebei", None], ["enkel basket", None],
                   ["geen van beide", None]],
                  r"\(9\) · \(6\) · \(7\) · \(6\)", "150px"),
             ]),
        dict(kop="Schrijf het in tekens",
             opdracht="Schrijf de zin met de tekens van de verzamelingen.",
             oefeningen=[
                 ("rij", [("de doorsnede van A en B", r"\(A \cap B\)"),
                          ("de vereniging van A en B", r"\(A \cup B\)"),
                          ("het aantal elementen van B", r"\(\left|B\right|\)"),
                          ("A en B zijn disjunct", r"\(A \cap B = \emptyset\)")],
                  "In tekens", WW),
             ]),
        dict(kop="Rekenen met de somregel",
             opdracht="Gebruik de somregel.",
             oefeningen=[
                 ("rij", [(r"\(\left|A\right| = 12\), \(\left|B\right| = 9\), "
                           r"\(\left|A \cap B\right| = 4\): bereken \(\left|A \cup B\right|\)",
                           r"\(17\)"),
                          (r"\(\left|A\right| = 20\), \(\left|B\right| = 15\), \(A \cap B = \emptyset\): "
                           r"bereken \(\left|A \cup B\right|\)", r"\(35\)"),
                          (r"\(\left|A \cup B\right| = 30\), \(\left|A\right| = 18\), "
                           r"\(\left|B\right| = 20\): bereken \(\left|A \cap B\right|\)", r"\(8\)")],
                  "Uitkomst", W),
             ]),
        dict(kop="Slim tellen",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Hoeveel getallen van 1 tot en met 30 zijn deelbaar door 2 of door 5?",
                  r"\(15\) door \(2\), \(6\) door \(5\), \(3\) door allebei (\(10\), \(20\), \(30\)): "
                  r"\(15 + 6 - 3 = 18\).", 5),
                 ("open", "Je gooit drie keer met een munt. Hoeveel uitkomsten hebben minstens één "
                          "kop? Tel liever het tegendeel.",
                  r"Er zijn \(2^{3} = 8\) uitkomsten en precies \(1\) heeft geen enkele kop: "
                  r"\(8 - 1 = 7\).", 5),
             ]),
        dict(kop="Welk gereedschap?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Je kiest een voorgerecht, een hoofdgerecht en een dessert",
                  ["boomdiagram en productregel", "venndiagram en somregel"], 0),
                 ("kies", "Je wil weten hoeveel leerlingen Frans én Duits volgen",
                  ["boomdiagram en productregel", "venndiagram en somregel"], 1),
                 ("kies", "Je wil weten hoeveel er aan geen van beide voorwaarden voldoen",
                  ["de productregel", "de complementregel", "de machtsregel"], 1),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij twee overlappende groepen mag je de aantallen gewoon optellen.", False),
                 ("waar", r"Bij disjuncte groepen is \(A \cap B = \emptyset\).", True),
                 ("waar", "Een boomdiagram toont elke uitkomst precies één keer.", True),
                 ("waar", "Een venndiagram is het gereedschap voor opeenvolgende keuzes.", False),
                 ("waar", "Bij trekken zonder terugleggen daalt het aantal keuzes bij elke stap.", True),
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
        dict(kop="Relatieve frequenties",
             opdracht="Schrijf als breuk en als percent.",
             oefeningen=[
                 ("rij", [("12 op 48", r"\(\frac{12}{48} = 25\,\%\)"),
                          ("7 op 20", r"\(\frac{7}{20} = 35\,\%\)"),
                          ("15 op 25", r"\(\frac{15}{25} = 60\,\%\)"),
                          ("9 op 60", r"\(\frac{9}{60} = 15\,\%\)")],
                  "Breuk en percent", WW),
             ]),
        dict(kop="De frequentietabel aanvullen",
             opdracht="Een klas van 20 leerlingen. Vul de relatieve frequenties in, in procent.",
             oefeningen=[
                 ("tabel", ["vervoer", "absolute frequentie", "relatieve frequentie"],
                  [["fiets", "8", None], ["bus", "6", None], ["te voet", "4", None], ["auto", "2", None]],
                  r"\(40\,\%\) · \(30\,\%\) · \(20\,\%\) · \(10\,\%\), samen \(100\,\%\)", "170px"),
             ]),
        dict(kop="Klassenmiddens",
             opdracht="Bereken het klassenmidden.",
             oefeningen=[
                 ("rij", [(r"\(\left[0, 10\right[\)", r"\(5\)"), (r"\(\left[30, 40\right[\)", r"\(35\)"),
                          (r"\(\left[150, 160\right[\)", r"\(155\)"),
                          (r"\(\left[12, 18\right[\)", r"\(15\)")],
                  "Klassenmidden", W),
             ]),
        dict(kop="Welk diagram?",
             opdracht="Schrijf welk diagram het best past.",
             oefeningen=[
                 ("rij", [("de temperatuur per maand over een jaar", "lijndiagram"),
                          ("het aandeel van elk vervoermiddel in het geheel", "cirkeldiagram"),
                          ("de lengtes van 80 leerlingen in klassen van 5 cm", "histogram"),
                          ("de vijf kengetallen van een reeks", "boxplot")],
                  "Diagram", WW),
             ]),
        dict(kop="Schrijf het teken",
             opdracht="Schrijf het teken dat bij de maat hoort.",
             oefeningen=[
                 ("rij", [("het rekenkundig gemiddelde", r"\(\bar{x}\)"),
                          ("het derde kwartiel", r"\(Q_{3}\)"),
                          ("de interkwartielafstand", r"\(Q_{3} - Q_{1}\)"),
                          ("de standaardafwijking", r"\(\sigma\)")],
                  "Teken", W),
             ]),
        dict(kop="Centrummaten berekenen",
             opdracht=r"De reeks is \(4,\ 7,\ 7,\ 9,\ 13,\ 20\). Bereken.",
             oefeningen=[
                 ("rij", [(r"\(\bar{x}\)", r"\(\frac{60}{6} = 10\)"), ("de mediaan", r"\(\frac{7 + 9}{2} = 8\)"),
                          ("de modus", r"\(7\)"), ("de variatiebreedte", r"\(20 - 4 = 16\)")],
                  "Antwoord", WW),
             ]),
        dict(kop="Nog een reeks",
             opdracht=r"De reeks is \(3,\ 5,\ 8,\ 8,\ 11\). Bereken.",
             oefeningen=[
                 ("rij", [(r"\(\bar{x}\)", r"\(\frac{35}{5} = 7\)"), ("de mediaan", r"\(8\)"),
                          ("de modus", r"\(8\)"), ("de variatiebreedte", r"\(11 - 3 = 8\)")],
                  "Antwoord", WW),
             ]),
        dict(kop="Even of oneven",
             opdracht="Bereken de mediaan en let op het aantal waarden.",
             oefeningen=[
                 ("rij", [(r"\(1,\ 4,\ 9\)", r"\(4\)"), (r"\(2,\ 6,\ 7,\ 11\)", r"\(\frac{6 + 7}{2} = 6{,}5\)"),
                          (r"\(5,\ 5,\ 8,\ 12,\ 30\)", r"\(8\)")],
                  "Mediaan", WW),
             ]),
        dict(kop="Kwartielen en boxplot",
             opdracht=r"De gerangschikte reeks is \(2,\ 4,\ 6,\ 8,\ 10,\ 12,\ 14,\ 16\). Bereken.",
             oefeningen=[
                 ("rij", [(r"\(Q_{2}\)", r"\(\frac{8 + 10}{2} = 9\)"), (r"\(Q_{1}\)", r"\(5\)"),
                          (r"\(Q_{3}\)", r"\(13\)"), (r"\(Q_{3} - Q_{1}\)", r"\(13 - 5 = 8\)")],
                  "Antwoord", WW),
             ]),
        dict(kop="Gemiddelde of mediaan?",
             opdracht="Schrijf welke maat het eerlijkste beeld geeft, en waarom.",
             oefeningen=[
                 ("open", r"De lonen in een klein bedrijf: \(2000\), \(2100\), \(2200\), \(2300\) en "
                          r"\(15\,000\) euro.",
                  r"De mediaan (\(2200\)), want dat ene hoge loon trekt \(\bar{x}\) tot \(4720\) euro en "
                  r"dat verdient niemand.", 3),
                 ("open", r"De punten van tien leerlingen die allemaal tussen \(12\) en \(16\) liggen.",
                  "Het gemiddelde mag: er zijn geen uitschieters, dus gemiddelde en mediaan liggen "
                  "dicht bij elkaar.", 3),
             ]),
        dict(kop="Spreiding vergelijken",
             opdracht="Schrijf je antwoord in één of twee zinnen.",
             oefeningen=[
                 ("open", r"Klas A en klas B hebben allebei \(\bar{x} = 13\), maar A heeft "
                          r"\(\sigma = 1\) en B heeft \(\sigma = 4\). Wat betekent dat?",
                  r"In A liggen de punten dicht bij \(13\), in B liggen ze veel verder uit elkaar: daar "
                  r"zitten zowel hoge als lage punten.", 3),
                 ("open", r"Leg uit waarom \(Q_{3} - Q_{1}\) minder gevoelig is voor een uitschieter dan "
                          r"de variatiebreedte.",
                  r"\(Q_{3} - Q_{1}\) kijkt enkel naar de middelste helft; de uiterste waarden vallen "
                  r"erbuiten. De variatiebreedte vertrekt juist van die uitersten.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Bij een histogram raken de staven elkaar.", True),
                 ("waar", "Een reeks kan twee modi hebben.", True),
                 ("waar", r"\(Q_{3} - Q_{1}\) is gevoelig voor één uitschieter.", False),
                 ("waar", r"Alle relatieve frequenties samen geven \(100\,\%\).", True),
                 ("waar", r"\(Q_{2}\) is een ander woord voor de mediaan.", True),
                 ("waar", "De modus werkt ook bij categorische gegevens.", True),
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
                  [[r"\(10\,\%\)", r"\(15\,\%\)", None, None],
                   [r"\(40\,\%\)", r"\(50\,\%\)", None, None],
                   [r"\(20\,\%\)", r"\(16\,\%\)", None, None]],
                  r"\(5\) procentpunt en \(50\,\%\) groei · \(10\) procentpunt en \(25\,\%\) groei · "
                  r"\(4\) procentpunt minder en \(20\,\%\) daling", "120px"),
             ]),
        dict(kop="Percentages nemen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(25\,\%\) van \(80\)", r"\(20\)"), (r"\(12\,\%\) van \(150\)", r"\(18\)"),
                          (r"\(140\,\%\) van \(60\)", r"\(84\)"), (r"\(5\,\%\) van \(240\)", r"\(12\)")],
                  "Uitkomst", W),
             ]),
        dict(kop="Rekenen met kortingen",
             opdracht="Reken uit. Let op dat procenten van verschillende bedragen niet optellen.",
             oefeningen=[
                 ("rij", [(r"\(200\) euro, \(+10\,\%\), daarna \(-10\,\%\)",
                           r"\(200 \cdot 1{,}10 \cdot 0{,}90 = 198\) euro"),
                          (r"\(50\) euro, \(+20\,\%\), daarna \(-20\,\%\)",
                           r"\(50 \cdot 1{,}20 \cdot 0{,}80 = 48\) euro"),
                          (r"\(80\) euro, \(-25\,\%\), daarna \(-20\,\%\)",
                           r"\(80 \cdot 0{,}75 \cdot 0{,}80 = 48\) euro")],
                  "Eindprijs", WL),
             ]),
        dict(kop="Waar zit de misleiding?",
             opdracht="Schrijf in één zin wat er mis is met de voorstelling.",
             oefeningen=[
                 ("open", r"Een staafdiagram waarvan de verticale as van \(95\) tot \(100\) loopt.",
                  "De as begint niet bij nul, dus een verschil van één procentpunt lijkt enorm.", 3),
                 ("open", r"Een as met de stappen \(0,\ 1,\ 2,\ 5,\ 10,\ 50\) op gelijke afstanden.",
                  "De as is foutief geijkt: gelijke afstanden tonen ongelijke sprongen, dus een "
                  "kromme kan recht lijken.", 3),
             ]),
        dict(kop="Nog twee voorstellingen",
             opdracht="Zelfde opdracht: schrijf in één zin wat er mis is.",
             oefeningen=[
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
                 ("open", r"De verkoop steeg met \(50\,\%\).",
                  r"Van hoeveel naar hoeveel? Van \(2\) naar \(3\) is ook \(50\,\%\).", 3),
             ]),
        dict(kop="De correlatiecoëfficiënt",
             opdracht=r"Schrijf op welke waarde van \(r\) het best past.",
             oefeningen=[
                 ("rij", [("alle punten precies op een stijgende rechte", r"\(r = 1\)"),
                          ("een wolk zonder duidelijke richting", r"\(r \approx 0\)"),
                          ("een duidelijk dalende wolk met wat spreiding", r"\(r \approx -0{,}8\)"),
                          ("alle punten precies op een dalende rechte", r"\(r = -1\)")],
                  "Waarde", WW),
             ]),
        dict(kop="Kies het juiste antwoord",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", r"Tussen welke grenzen ligt \(r\) altijd?",
                  [r"\(-1 \leq r \leq 1\)", r"\(0 \leq r \leq 1\)", r"\(-100 \leq r \leq 100\)"], 0),
                 ("kies", r"Een partij gaat van \(30\,\%\) naar \(33\,\%\). Dat is",
                  [r"\(3\) procentpunt en \(10\,\%\) groei", r"\(3\,\%\) en \(10\) procentpunt groei"], 0),
                 ("kies", "Een trendlijn",
                  ["gaat door alle punten", "vat de wolk samen en gaat vaak door geen enkel punt"], 1),
             ]),
        dict(kop="Correlatie of oorzaak?",
             opdracht="Schrijf op wat de derde factor of de fout in de redenering is.",
             oefeningen=[
                 ("open", "Kinderen met grotere schoenen lezen beter.",
                  "De derde factor is de leeftijd: oudere kinderen hebben grotere voeten én lezen "
                  "beter.", 3),
                 ("open", "Gemeenten met meer brandweerlieden hebben meer schade door brand.",
                  "De derde factor is de grootte van de gemeente. Grote steden hebben meer van allebei.", 3),
                 ("open", "Mensen die ontbijten wegen minder, dus ontbijten maakt slank.",
                  "Correlatie is geen oorzaak. Wie ontbijt, leeft vaak ook verder gezonder; het "
                  "verband kan ook omgekeerd lopen.", 3),
             ]),
        dict(kop="Voorzichtig formuleren",
             opdracht="Herschrijf de uitspraak zodat ze enkel beschrijft wat er gemeten is.",
             oefeningen=[
                 ("open", "Meer slapen zorgt voor betere punten.",
                  "In deze groep haalden leerlingen die meer sliepen, gemiddeld hogere punten.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een grafiek kan kloppen en toch een verkeerde indruk geven.", True),
                 ("waar", "Procent en procentpunt betekenen hetzelfde.", False),
                 ("waar", "Een trendlijn gaat altijd door alle punten van de wolk.", False),
                 ("waar", "Eén uitschieter kan de trendlijn flink verschuiven.", True),
                 ("waar", "Ver buiten het gemeten gebied voorspellen is riskant.", True),
                 ("waar", r"Een cirkeldiagram waarvan de delen samen \(118\,\%\) geven, klopt niet.", True),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-opgave-aanpakken-van-context-naar-wiskunde-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Kijk in welke richting je vertaalt: van de werkelijkheid naar wiskunde is "
                    "mathematiseren, van je uitkomst terug naar de werkelijkheid is demathematiseren.",
             waarom=[None]),
        dict(aanpak="Bij een vraagstuk weet je meteen welke bewerking je nodig hebt. Bij een probleem "
                    "moet je zelf nog uitzoeken welke leerstof erbij komt kijken.",
             waarom=[None]),
        dict(aanpak="Een heuristiek is een manier om vooruit te komen als je het antwoord nog niet "
                    "ziet. Zoek bij elke zin welke stap daar gezet wordt.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Let erop dat terugrekenen bij het einde begint, en dat patronen "
                    "zoeken naar de verschillen tussen de getallen kijkt.",
             waarom=[None]),
        dict(aanpak="De vier stappen van Polya volgen altijd dezelfde volgorde. Leer ze als rijtje, dan "
                    "weet je bij een moeilijke opgave waar je staat.",
             waarom=[None]),
        dict(aanpak="Vraag je bij elke handeling af wat je op dat moment aan het doen bent: lezen, "
                    "kiezen, rekenen of nakijken.",
             waarom=[None]),
        dict(aanpak="Reflecteren is nagaan of je uitkomst kán kloppen. Kijk naar de grootteorde, naar "
                    "het teken en naar de eenheid.",
             waarom=[
                 r"De fout zit in de eenheid: \(1\) m\(^{3}\) is \(1000\) liter. Die controle doe je "
                 r"altijd voor je je antwoord opschrijft.",
                 r"Een tijd in minuten moet eerst naar uren. Delen door \(45\) geeft km per minuut, niet "
                 r"km per uur.",
                 None,
             ]),
        dict(aanpak="Schat eerst met ronde getallen. Je schatting is je controle: ligt je exacte "
                    "antwoord er ver vandaan, dan zit er een fout in.",
             waarom=[None]),
        dict(aanpak="Vraag je bij elke uitkomst af welke grens ze overschrijdt: kan een gemiddelde zo "
                    "laag zijn, kan een korting de prijs doen stijgen?",
             waarom=[
                 None,
                 r"Een korting van \(30\%\) betekent dat je nog \(70\%\) betaalt, dus "
                 r"\(\cdot\, 0{,}7\). Wie \(\cdot\, 1{,}3\) rekent, telt de korting er net bij.",
             ]),
        dict(aanpak="Zelfde werkwijze: eerst ronden, dan exact. Let op de getallen die net onder of net "
                    "boven een rond getal liggen.",
             waarom=[None]),
        dict(aanpak="Werk de vier stappen af en schrijf zeker je plan en je controle op. De controle is "
                    "op het examen punten waard.",
             waarom=[
                 r"Let op de valkuil: \(25\%\) van \(60\) erbij tellen geeft \(75\) en niet \(80\). Je "
                 r"moet rekenen met het percentage van de óude prijs.",
                 None,
             ]),
        dict(aanpak="Mathematiseren betekent: geef het onbekende een letter, schrijf erbij waarvoor ze "
                    "staat, en zet de zin dan pas om.",
             waarom=[None]),
        dict(aanpak="Lees de opgave twee keer: eerst om te weten wat gevraagd wordt, dan om de "
                    "gegevens eruit te halen.",
             waarom=[
                 r"Let op welke zijde de schuine is: de ladder zelf. Dus trek je af, je telt niet op.",
                 None,
             ]),
        dict(aanpak="De vier vaardigheden lopen door elke opgave heen: lezen, rekenen, meten en "
                    "tekenen, en het juiste gereedschap gebruiken.",
             waarom=[None]),
        dict(aanpak="Let bij deze uitspraken op de woorden altijd, enkel en volstaat. Daar zit meestal "
                    "het verschil tussen waar en niet waar.",
             waarom=[
                 None,
                 "Een schatting is een controle, geen antwoord. Ze zegt je of je uitkomst in de juiste "
                 "grootteorde ligt.",
                 None,
                 "Voorbeelden illustreren, ze bewijzen niet. Het geval dat je niet bekeek, kan nog "
                 "altijd tegenspreken.",
                 None,
                 "Er komen ook zuiver wiskundige opgaven voor, zonder verhaal eromheen.",
             ]),
        dict(aanpak="Schrijf in volle zinnen. Een antwoord dat enkel zegt wat je deed, zonder waarom, "
                    "levert maar de helft van de punten op.",
             waarom=[None, None]),
        dict(aanpak="Hier gaat het om het verschil tussen tonen en bewijzen. Eén tegenvoorbeeld breekt "
                    "een uitspraak; honderd voorbeelden bewijzen er geen.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-logica-symbolen-waarheidstabellen-en-poorten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Een uitspraak is een zin waarvan je kan zeggen of ze waar of vals is. Een vraag of "
                    "een bevel kan dat niet.",
             waarom=[
                 "Negen is geen priemgetal, maar dat doet er niet toe: de zin is wel waar of vals, dus "
                 "ze is een uitspraak.",
                 None,
                 "De zin is vals, en net daarom is het een uitspraak.",
                 None,
             ]),
        dict(aanpak="Vertaal woord voor woord: en wordt de wig naar beneden, of de wig naar boven, als "
                    "… dan de dubbele pijl naar rechts, niet het haakje.",
             waarom=[None, None]),
        dict(aanpak="Vul een waarheidstabel kolom per kolom in, niet rij per rij. Eerst de losse "
                    "variabelen, dan de samengestelde vormen.",
             waarom=[None]),
        dict(aanpak="Elke variabele verdubbelt het aantal rijen: twee tot de macht het aantal "
                    "variabelen.",
             waarom=[None]),
        dict(aanpak="Een tautologie is in elke rij waar, een contradictie in elke rij vals. Alles "
                    "daartussen is geen van beide.",
             waarom=[None]),
        dict(aanpak="De negatie van alle is minstens één niet, en de negatie van er bestaat is geen "
                    "enkele. Draai de kwantor om, niet alleen het werkwoord.",
             waarom=[None, None, None]),
        dict(aanpak="Nodig betekent: zonder dat lukt het niet. Voldoende betekent: daarmee is het al "
                    "zeker.",
             waarom=[
                 r"Deelbaar door \(3\) moet, maar volstaat niet: \(9\) is deelbaar door \(3\) en niet "
                 r"door \(6\).",
                 None,
             ]),
        dict(aanpak="Zoek bij een tegenvoorbeeld het geval dat net buiten de regel valt. Vaak is dat "
                    "het kleinste getal, nul, of een getal tussen nul en één.",
             waarom=[
                 None,
                 r"\(2\) is het enige even priemgetal, en daarmee het tegenvoorbeeld.",
                 None,
             ]),
        dict(aanpak="Vertaal de zin eerst naar en of of: moeten beide voorwaarden kloppen, of volstaat "
                    "er één?",
             waarom=[None]),
        dict(aanpak="Let op waar de negatie staat: vóór de haakjes slaat ze op het geheel, erbinnen op "
                    "elk deel apart.",
             waarom=[None]),
        dict(aanpak="Er zijn drie varianten van een implicatie, en maar één ervan zegt hetzelfde: de "
                    "contrapositie, waar je allebei ontkent én omdraait.",
             waarom=[None]),
        dict(aanpak="De Morgan in één zin: haal de negatie binnen de haakjes en wissel en met of.",
             waarom=[None]),
        dict(aanpak="Een N vooraan betekent dat de uitkomst van de poort omgekeerd wordt.",
             waarom=[None]),
        dict(aanpak="Schrijf in volle zinnen en gebruik de vaktermen. Een uitleg met alleen een "
                    "voorbeeld erin telt niet als uitleg.",
             waarom=[None, None]),
        dict(aanpak="Neem je tijd en vul bij twijfel de tabel echt in. Je ziet dan zelf in welke rij "
                    "twee vormen uit elkaar gaan.",
             waarom=[None, None]),
        dict(aanpak="Kijk na wat er precies in bijlage 1 staat en wat niet; dat scheelt op het examen "
                    "veel uit het hoofd leren.",
             waarom=[
                 None,
                 "De bewijzen moet je zelf kennen. Enkel het formularium mag mee.",
                 None,
                 "De hoekensom van een vierhoek leid je zelf af uit die van een driehoek.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-reele-getallen-wortels-en-machten-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De verzamelingen zitten in elkaar: elk natuurlijk getal is ook geheel, elk geheel "
                    "getal is ook rationaal. Gevraagd wordt telkens de kléinste.",
             waarom=[
                 None,
                 r"Let op \(\sqrt{49}\): dat is gewoon \(7\), dus een natuurlijk getal. Een wortel maakt "
                 r"een getal niet automatisch irrationaal.",
             ]),
        dict(aanpak="Een getal is rationaal als je het als breuk kan schrijven. Aan de decimale vorm "
                    "zie je het: stopt ze of herhaalt ze zich, dan is ze rationaal.",
             waarom=[
                 r"Een repeterende decimale vorm is altijd een breuk: hier \(\tfrac{27}{99} = \tfrac{3}{11}\).",
                 None,
                 r"\(\sqrt{64} = 8\), dus een geheel getal en zeker rationaal.",
                 None,
             ]),
        dict(aanpak="Werk altijd via het kommagetal: een breuk wordt een kommagetal door te delen, en "
                    "een kommagetal wordt een procent door honderd te vermenigvuldigen.",
             waarom=[None]),
        dict(aanpak="Zoek het grootste volkomen kwadraat dat in het getal past, haal dat eruit en laat "
                    "de rest onder de wortel staan.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Ga de kwadraten af van groot naar klein: 100, 81, 64, 49, 36, "
                    "25, 16, 9, 4.",
             waarom=[None]),
        dict(aanpak="Zoek het getal dat je drie keer met zichzelf moet vermenigvuldigen. Leer de "
                    "derdemachten van 1 tot 10 uit het hoofd.",
             waarom=[None]),
        dict(aanpak="Vermenigvuldigen onder de wortel mag, optellen niet. Twee gelijke wortels tel je "
                    "op zoals je gelijke letters optelt.",
             waarom=[
                 r"\(\sqrt{16+9}\) is \(\sqrt{25} = 5\): eerst optellen onder de wortel, niet de wortels "
                 r"apart nemen.",
                 r"\(\sqrt{a^{2}}\) is de absolute waarde van \(a\), dus \(4\) en niet \(-4\).",
             ]),
        dict(aanpak="Vermenigvuldig teller en noemer met dezelfde wortel. Je verandert de schrijfwijze, "
                    "niet de waarde.",
             waarom=[None]),
        dict(aanpak="Vier regels: bij vermenigvuldigen tel je de exponenten op, bij delen trek je ze "
                    "af, bij een macht van een macht vermenigvuldig je ze, en bij een product krijgt "
                    "elke factor de exponent.",
             waarom=[None]),
        dict(aanpak="Exponent nul geeft altijd één. Een negatieve exponent keert het getal om, ze maakt "
                    "het niet negatief.",
             waarom=[None]),
        dict(aanpak="Zelfde regels, nu met letters erbij. Werk stap voor stap en schrijf nooit meteen "
                    "het eindantwoord neer.",
             waarom=[None]),
        dict(aanpak="Drie namen om uit elkaar te houden: distributiviteit verdeelt, associativiteit "
                    "verplaatst de haakjes, commutativiteit wisselt de volgorde.",
             waarom=[None]),
        dict(aanpak="Bij een foutenzoeker schrijf je altijd ook het juiste antwoord op. Enkel fout "
                    "zeggen is het halve werk.",
             waarom=[None, None]),
        dict(aanpak="Let op de twee klassiekers: een exponent buiten de haakjes geldt voor élke factor, "
                    "en een minteken in de exponent is geen minteken voor het getal.",
             waarom=[None, None]),
        dict(aanpak="Deze vier uitspraken gaan over de regels die je net gebruikte. Zoek bij elke "
                    "uitspraak een voorbeeld of een tegenvoorbeeld.",
             waarom=[None, None, None, None]),
        dict(aanpak="Schrijf je uitleg in volle zinnen en met een voorbeeld erbij. De vraag is niet wat "
                    "de regel is, maar waarom ze geldt.",
             waarom=[None, None]),
        dict(aanpak="Deze twee vragen draaien om hetzelfde idee: dezelfde waarde kan er anders "
                    "uitzien, en een regel kan een uitzondering hebben bij negatieve getallen.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-ordenen-afronden-intervallen-en-wetenschappelijke-notatie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zet de getallen eerst in dezelfde vorm, meestal als kommagetal. Bij negatieve "
                    "getallen is het grootste cijfer net het kleinste getal.",
             waarom=[None]),
        dict(aanpak="Schrijf alles als kommagetal met evenveel cijfers na de komma. Dan zie je de "
                    "volgorde in één oogopslag.",
             waarom=[None, None]),
        dict(aanpak="Kijk alleen naar het eerste cijfer dat wegvalt: vijf of meer naar boven, vier of "
                    "minder naar beneden. Rond nooit in twee stappen af.",
             waarom=[None]),
        dict(aanpak="Vervang elk getal door het dichtste ronde getal en reken dan pas. De schatting is "
                    "je controle, niet je antwoord.",
             waarom=[None]),
        dict(aanpak="Een vierkant haakje neemt de grens mee, een haakje dat naar buiten wijst laat ze "
                    "weg.",
             waarom=[None]),
        dict(aanpak="Vertaal woord voor woord: groter dan geeft een open haakje, groter dan of gelijk "
                    "aan een vierkant haakje. Bij oneindig wijst het haakje altijd naar buiten.",
             waarom=[None]),
        dict(aanpak="Wetenschappelijke notatie is altijd één cijfer vóór de komma, maal een macht van "
                    "tien. De exponent telt hoeveel plaatsen de komma schuift.",
             waarom=[None]),
        dict(aanpak="Controleer één ding: staat er precies één cijfer van 1 tot 9 vóór de komma?",
             waarom=[
                 r"\(34{,}2\) heeft twee cijfers vóór de komma. Correct is \(3{,}42 \cdot 10^{4}\).",
                 None,
                 r"\(0{,}5\) heeft een nul vóór de komma. Correct is \(5 \cdot 10^{5}\).",
                 None,
             ]),
        dict(aanpak="Zelfde werkwijze als daarnet, nu met het isgelijkteken erbij. Een breuk en een "
                    "kommagetal kunnen precies hetzelfde getal zijn.",
             waarom=[None]),
        dict(aanpak="Zelfde regel, nu op één cijfer na de komma. Bij een negatief getal rond je naar "
                    "het getal dat verder van nul ligt als het cijfer vijf of meer is.",
             waarom=[None]),
        dict(aanpak="Zet opnieuw alles in dezelfde vorm. Bij negatieve getallen keert de volgorde om.",
             waarom=[None]),
        dict(aanpak="Een positieve exponent schuift de komma naar rechts, een negatieve naar links. Het "
                    "getal in de exponent is het aantal plaatsen.",
             waarom=[None]),
        dict(aanpak="Twee open haakjes maken een open interval, twee vierkante een gesloten, en één van "
                    "elk een halfopen.",
             waarom=[None]),
        dict(aanpak="Zoek bij elke fout welke regel precies geschonden wordt, en schrijf daarna het "
                    "juiste antwoord op.",
             waarom=[None, None]),
        dict(aanpak="Antwoord in volle zinnen. Beide vragen gaan over hetzelfde: afronden kost "
                    "nauwkeurigheid, dus doe je het zo laat mogelijk.",
             waarom=[None, None]),
        dict(aanpak="Deze twee vragen gaan over de dichtheid van de reële getallen: tussen twee "
                    "getallen ligt er altijd nog een.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak de regel na die je net gebruikte, en zoek desnoods een "
                    "tegenvoorbeeld.",
             waarom=[
                 None,
                 r"Het interval \(\left[5, 5\right]\) bevat precies één getal, namelijk \(5\). Leeg is "
                 r"\(\left]5, 5\right[\).",
                 None,
                 None,
             ]),
        dict(aanpak="Schrijf je redenering uit. Bij afronden hoort een bereik, en bij een macht van "
                    "tien hoort de grootteorde.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-rechten-vlakken-en-gelijkvormigheid-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Tel bij elk paar de gemeenschappelijke punten: geen, één, of allemaal. Daarbij "
                    "komt in de ruimte nog de vraag of ze in één vlak liggen.",
             waarom=[None]),
        dict(aanpak="Tel bij een ruimtefiguur systematisch: eerst de vlakken, dan de ribben, dan de "
                    "hoekpunten.",
             waarom=[None]),
        dict(aanpak="Een ontwikkeling is het platte patroon, een aanzicht is wat je uit één richting "
                    "ziet, en een perspectief is een ruimtelijke tekening.",
             waarom=[None, None, None]),
        dict(aanpak="De doorsnede houdt wat in allebei zit, de unie alles samen, en het verschil wat in "
                    "de eerste zit en niet in de tweede.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Let op het verschil tussen A zonder B en B zonder A: die twee "
                    "zijn niet hetzelfde.",
             waarom=[None]),
        dict(aanpak="Drie kenmerken: twee gelijke hoeken (HH), drie zijden in dezelfde verhouding "
                    "(ZZZ), of twee zijden in verhouding met de hoek ertussen (ZHZ).",
             waarom=[None]),
        dict(aanpak="Onthoud de drie machten: lengte maal k, oppervlakte maal k kwadraat, volume maal k "
                    "tot de derde.",
             waarom=[None]),
        dict(aanpak="Zet de schaal eerst om naar dezelfde eenheid, reken dan pas. Schrijf de eenheid "
                    "altijd bij je antwoord.",
             waarom=[None]),
        dict(aanpak="Zoek eerst de factor k, en kijk dan of de vraag over lengte, oppervlakte of "
                    "volume gaat.",
             waarom=[
                 None,
                 "Gewicht volgt het volume, dus de factor gaat tot de derde macht. Dat is waarom een "
                 "schaalmodel zo licht aanvoelt.",
                 None,
             ]),
        dict(aanpak="Zelfde werkwijze als in de eerste reeks. Let op dat samenvallend en evenwijdig "
                    "niet hetzelfde zijn.",
             waarom=[None]),
        dict(aanpak="Een vlakke figuur ligt helemaal in één vlak; een ruimtefiguur heeft dikte.",
             waarom=[None]),
        dict(aanpak="De factor k is de nieuwe lengte gedeeld door de oude. Kleiner dan één betekent "
                    "verkleinen.",
             waarom=[None]),
        dict(aanpak="Nu de andere richting: deel de echte maat door de schaal. Zet eerst alles in "
                    "dezelfde eenheid.",
             waarom=[None]),
        dict(aanpak="Zoek bij elke fout de regel die geschonden wordt. De twee klassiekers zijn de "
                    "richting van een schaal en de macht bij volume.",
             waarom=[None, None]),
        dict(aanpak="Antwoord in volle zinnen. Deze twee vragen draaien om hetzelfde idee: wat met de "
                    "macht meegaat, groeit veel sneller.",
             waarom=[None, None]),
        dict(aanpak="Dezelfde drie machten, nu bij een bol en bij gelijke hoeken. Vraag je telkens af "
                    "of het om lengte, oppervlakte of volume gaat.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak na welke regel ze gebruikt, en zoek bij twijfel een "
                    "tegenvoorbeeld of een tekening.",
             waarom=[
                 None,
                 None,
                 "Gelijkvormig betekent dezelfde vorm, niet dezelfde grootte. Gelijk zijn ze pas als de "
                 "factor één is.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-pythagoras-en-de-rechthoekige-driehoek-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek eerst welke zijde de schuine is: altijd die tegenover de rechte hoek. Die "
                    "staat alleen aan de andere kant van het isgelijkteken.",
             waarom=[None]),
        dict(aanpak="Ken je de schuine zijde al, dan trek je af in plaats van op te tellen. Vergeet "
                    "achteraan de wortel niet.",
             waarom=[None]),
        dict(aanpak="Tel de kwadraten van de twee kortste zijden op en vergelijk met het kwadraat van "
                    "de langste. Gelijk betekent rechthoekig.",
             waarom=[None, None, None, None, None]),
        dict(aanpak="Teken het verschil in x en in y als twee rechthoekszijden. De afstand is dan de "
                    "schuine zijde.",
             waarom=[None]),
        dict(aanpak="Noteer eerst welke twee zijden in het spel zijn ten opzichte van de hoek: "
                    "overstaand, aanliggend of schuin. Daaruit volgt het goniometrisch getal.",
             waarom=[None]),
        dict(aanpak="Deze vier formules moet je uit het hoofd kennen; ze staan niet in het "
                    "formularium.",
             waarom=[None, None, None, None]),
        dict(aanpak="Leer deze tabel als één geheel. De sinus loopt op van nul naar één, de cosinus "
                    "net omgekeerd.",
             waarom=[None]),
        dict(aanpak="Vul in de grondformule in wat je kent en los op naar het andere. Bij een scherpe "
                    "hoek neem je de positieve wortel.",
             waarom=[None]),
        dict(aanpak="Loop bij elke uitspraak na welke voorwaarde erbij hoort, en zoek bij twijfel een "
                    "tegenvoorbeeld.",
             waarom=[
                 "Pythagoras geldt alleen in een rechthoekige driehoek. In een andere driehoek gebruik je "
                 "de cosinusregel.",
                 None,
                 r"Sinus en cosinus van een scherpe hoek liggen altijd tussen \(0\) en \(1\): het is een "
                 r"verhouding van een rechthoekszijde tot de langste zijde.",
                 None,
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Een exact antwoord laat de wortel of de breuk staan. Een benaderd antwoord heeft "
                    "al een afronding ondergaan.",
             waarom=[None, None, None]),
        dict(aanpak="Maak eerst een schets met de gegevens erop. Bij een ruimtefiguur werk je in twee "
                    "stappen: eerst de diagonaal van het grondvlak, dan de ruimtediagonaal.",
             waarom=[None, None]),
        dict(aanpak="Schrijf hier vooral je werkwijze op. Welke formule je kiest en waarom, is de helft "
                    "van de punten.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-sinusregel-cosinusregel-en-vectoren-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De drie hoeken van een driehoek zijn samen honderdtachtig graden. Trek de twee "
                    "gekende hoeken daarvan af.",
             waarom=[None]),
        dict(aanpak="De vuistregel: zit de hoek tússen de twee gekende zijden, of ken je alle drie de "
                    "zijden, dan de cosinusregel. In alle andere gevallen de sinusregel.",
             waarom=[None]),
        dict(aanpak="De driehoeksongelijkheid: de twee kortste zijden samen moeten langer zijn dan de "
                    "langste. Precies gelijk volstaat niet.",
             waarom=[
                 r"\(3 + 4 = 7\), en dat is korter dan \(9\). De twee zijden raken elkaar dan nooit.",
                 None,
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Deze formules staan in het formularium, maar je moet weten wat elke letter "
                    "voorstelt. Oefen ze toch uit het hoofd.",
             waarom=[None, None, None, None]),
        dict(aanpak="Schrijf eerst je plan op: welke regel eerst, en wat je daarmee vindt. Pas daarna "
                    "reken je.",
             waarom=[None, None]),
        dict(aanpak="Een vector heeft drie kenmerken samen. Twee vectoren zijn pas gelijk als alle "
                    "drie overeenkomen.",
             waarom=[None]),
        dict(aanpak="De norm is gewoon Pythagoras op de twee coördinaten. Ze is nooit negatief.",
             waarom=[None]),
        dict(aanpak="Trek de coördinaten van het beginpunt af van die van het eindpunt: eindpunt min "
                    "beginpunt.",
             waarom=[None]),
        dict(aanpak="Optellen doe je per coördinaat. Vermenigvuldigen met een getal doet dat met beide "
                    "coördinaten.",
             waarom=[None]),
        dict(aanpak="Maak eerst een schets met de vectoren kop aan staart. Dan zie je welke driehoek er "
                    "ontstaat.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak na of ze altijd geldt. Eén tegenvoorbeeld is genoeg om ze "
                    "te breken.",
             waarom=[
                 "Een norm is een lengte, en een lengte is nooit negatief.",
                 None,
                 "Wijzen twee vectoren tegen elkaar in, dan is de som juist korter, en bij elkaars "
                 "tegengestelde zelfs de nulvector.",
                 None,
                 "De sinusregel geldt in élke driehoek. Pythagoras is degene die een rechte hoek "
                 "vraagt.",
                 None,
                 r"\(\cos 90^\circ = 0\). Het is \(\sin 90^\circ\) dat \(1\) is.",
             ]),
        dict(aanpak="Drie vaktermen om uit elkaar te houden: de norm is de lengte, de eenheidsvector "
                    "heeft lengte één, en de nulvector heeft lengte nul.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-formules-omvormen-en-eerstegraadsvergelijkingen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Werk elk haakje apart uit en let op het teken ervoor. Neem daarna pas gelijksoortige "
                    "termen samen.",
             waarom=[
                 "De drie merkwaardige producten herken je aan hun vorm: een som in het kwadraat, een "
                 "verschil in het kwadraat, en een som maal een verschil.",
                 "Een minteken vóór een haakje keert élke term binnen dat haakje om.",
             ]),
        dict(aanpak="Zoek altijd eerst een gemeenschappelijke factor. Blijft er dan nog iets staan, kijk "
                    "dan of het een merkwaardig product is.",
             waarom=[None]),
        dict(aanpak="Breng alles met x naar de ene kant en alle getallen naar de andere. Wat je links "
                    "doet, doe je ook rechts.",
             waarom=[None]),
        dict(aanpak="Er is vaak meer dan één weg, maar één ervan is korter. Kijk of je kan delen vóór "
                    "je haakjes uitwerkt.",
             waarom=[
                 r"Hier mag je ook meteen delen door \(3\); dat gaat sneller. Allebei kloppen ze.",
                 None,
                 "Vermenigvuldigen of delen door een negatief getal draait het ongelijkheidsteken om. "
                 "Dat is de klassieke valkuil.",
                 None,
             ]),
        dict(aanpak="Vermenigvuldig elke term met de kleinste gemene veelvoud van de noemers. Dan ben "
                    "je de breuken in één keer kwijt.",
             waarom=[None]),
        dict(aanpak="Vallen alle onbekenden weg, kijk dan wat er overblijft: iets dat altijd klopt, of "
                    "iets dat nooit klopt.",
             waarom=[None, None]),
        dict(aanpak="Los op zoals een vergelijking, met één uitzondering: bij delen door een negatief "
                    "getal draait het teken om.",
             waarom=[None]),
        dict(aanpak="Omvormen is dezelfde bewerking op beide leden. Breng de gevraagde letter alleen te "
                    "staan.",
             waarom=[None, None]),
        dict(aanpak="Vul eerst in, reken dan pas, en zet de eenheid bij je antwoord. Die eenheid is op "
                    "het examen punten waard.",
             waarom=[None]),
        dict(aanpak="Schrijf eerst op waar je letter voor staat. Vergeet de controle niet: vul je "
                    "antwoord terug in het verhaal in.",
             waarom=[None, None, None]),
        dict(aanpak="Een vergelijking oplossen is grafisch het snijpunt zoeken; een ongelijkheid "
                    "oplossen is kijken waar de grafiek boven of onder de as ligt.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak na welke regel ze gebruikt. Let vooral op de tekens en op "
                    "de machten.",
             waarom=[
                 "Het teken draait alleen om bij een negatief getal.",
                 None,
                 "Die letter kan nul zijn, en delen door nul mag niet. Je zou dan oplossingen "
                 "verliezen.",
                 r"Verdubbel je \(v\), dan wordt \(E_{k}\) vier keer zo groot. De energie is evenredig "
                 r"met het kwadraat van de snelheid.",
                 None,
                 r"Het minteken geldt voor élke term: \(-2x + 10\).",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-stelsels-en-tweedegraadsvergelijkingen-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Kijk naar de vorm: staat er al een letter alleen, dan substitutie; staan er twee "
                    "letters alleen, dan gelijkstelling; zijn de coëfficiënten gelijk of tegengesteld, "
                    "dan combinatie.",
             waarom=[None]),
        dict(aanpak="Vul de uitdrukking voor de ene letter in de andere vergelijking in. Je houdt dan "
                    "één vergelijking met één onbekende over.",
             waarom=[None]),
        dict(aanpak="Tel de twee vergelijkingen op of trek ze van elkaar af, zodat één letter wegvalt. "
                    "Vermenigvuldig er eerst eentje mee als dat nodig is.",
             waarom=[None]),
        dict(aanpak="Vallen beide letters weg, lees dan wat er overblijft: altijd waar betekent "
                    "onbepaald, nooit waar betekent strijdig.",
             waarom=[None, None]),
        dict(aanpak="Vertaal de ligging van de rechten naar het soort stelsel: snijdend is bepaald, "
                    "evenwijdig is strijdig, samenvallend is onbepaald.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Schrijf er altijd bij hoe de rechten liggen; dat is de helft van "
                    "het antwoord.",
             waarom=[None]),
        dict(aanpak="Staat er geen term met x alleen, dan heb je de formule niet nodig: haal x buiten "
                    "haakjes, of neem de wortel aan beide kanten.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Let op het teken: het kwadraat van een reëel getal is nooit "
                    "negatief.",
             waarom=[None]),
        dict(aanpak="Noteer eerst waar elke letter voor staat. Twee onbekenden vragen twee "
                    "vergelijkingen.",
             waarom=[None, None]),
        dict(aanpak="Haal eerst a, b en c uit de vergelijking, met hun teken. Reken dan pas de "
                    "discriminant uit.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze: letters kiezen, twee vergelijkingen opstellen, oplossen, en "
                    "terugvertalen naar het verhaal.",
             waarom=[None, None]),
        dict(aanpak="De discriminant vertelt je hoe de parabool tegenover de x-as ligt, nog voor je een "
                    "oplossing berekent.",
             waarom=[None]),
        dict(aanpak="Schrijf a, b en c eerst apart op. De fout zit bijna altijd in een vergeten "
                    "minteken.",
             waarom=[None]),
        dict(aanpak="Zoek twee getallen met het product c en de som b. Dat gaat vaak sneller dan de "
                    "formule.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Een kwadraat van een tweeterm geeft maar één nulwaarde, een "
                    "verschil van kwadraten geeft er twee.",
             waarom=[None]),
        dict(aanpak="Zoek bij elke fout welke regel geschonden wordt, en schrijf het juiste antwoord "
                    "op.",
             waarom=[None, None]),
        dict(aanpak="Teken de parabool erbij. Bij kleiner dan zoek je het stuk onder de as, bij groter "
                    "dan de twee stukken erbuiten.",
             waarom=[None]),
        dict(aanpak="Stel de vergelijking op, los op, en kijk daarna of elke oplossing in het verhaal "
                    "kan. Een lengte of een aantal kan niet negatief zijn.",
             waarom=[None, None]),
        dict(aanpak="Antwoord in volle zinnen. Deze twee vragen draaien om de betekenis achter de "
                    "techniek.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak na of ze altijd geldt, en zoek bij twijfel een "
                    "tegenvoorbeeld of een tekening.",
             waarom=[
                 None,
                 "Strijdig hoort bij evenwijdige rechten die níet samenvallen. Samenvallende rechten "
                 "geven een onbepaald stelsel.",
                 r"Bij \(D < 0\) is er geen enkele reële oplossing, bij \(D = 0\) juist één.",
                 r"Uitgewerkt geeft dat \(x^{2} - 4\). Een som van twee kwadraten ontbindt niet in "
                 r"\(\mathbb{R}\).",
                 "Grafisch lees je af, en aflezen is bij benadering. Voor een exact antwoord moet je "
                 "rekenen.",
                 None,
             ]),
        dict(aanpak="Deze twee vragen draaien om de discriminant en om de meetkundige betekenis van een "
                    "stelsel. Neem je tijd.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-functies-en-de-rechte-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De verticalelijntest: leg je potlood verticaal op de grafiek en schuif. Raakt hij "
                    "ergens twee punten tegelijk, dan is het geen functie.",
             waarom=[
                 None,
                 r"Bij \(x = 3\) horen alle \(y\)-waarden tegelijk, dus hoort er geen één antwoord bij "
                 r"één invoer.",
                 None,
                 r"Een verticale lijn snijdt een cirkel in twee punten, dus horen er bij één \(x\) twee "
                 r"\(y\)-waarden.",
                 "Hier hoort bij elke x hetzelfde antwoord, en dat mag: één antwoord per invoer is de "
                 "enige eis.",
             ]),
        dict(aanpak="Vervang x door het getal en reken uit. Wordt de functiewaarde gegeven, dan los je "
                    "net omgekeerd een vergelijking op.",
             waarom=[None]),
        dict(aanpak="Kijk naar de verschillen tussen opeenvolgende waarden. Blijven die gelijk, dan is "
                    "de groei lineair.",
             waarom=[None]),
        dict(aanpak="De rico is het verschil in y gedeeld door het verschil in x. Let op de volgorde: "
                    "allebei van hetzelfde punt vertrekken.",
             waarom=[None]),
        dict(aanpak="Het teken van de rico beslist: positief stijgt, negatief daalt, nul blijft "
                    "horizontaal.",
             waarom=[None, None]),
        dict(aanpak="Zoek eerst de rico, vul dan een punt in om b te vinden. Twee punten geven je "
                    "allebei.",
             waarom=[None]),
        dict(aanpak="De waarde bij nul is b, en het verschil per stap is a. Daarmee heb je het "
                    "voorschrift al.",
             waarom=[None]),
        dict(aanpak="Voor het snijpunt met de y-as vul je nul in voor x; voor het snijpunt met de x-as "
                    "stel je y gelijk aan nul.",
             waarom=[None]),
        dict(aanpak="Recht evenredig is lineair mét b gelijk aan nul: de grafiek gaat door de "
                    "oorsprong.",
             waarom=[None, None, None, None]),
        dict(aanpak="Schrijf bij elk model wat a en b in het verhaal betekenen: a is het tempo per "
                    "eenheid, b is de beginwaarde.",
             waarom=[None, None, None]),
        dict(aanpak="Antwoord in één of twee zinnen. Deze vragen gaan over wat een grafiek nog zegt als "
                    "je de getallen weglaat.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak na of ze uit de definitie volgt, en zoek bij twijfel een "
                    "tegenvoorbeeld.",
             waarom=[
                 "Dat is net de definitie van een functie: bij elke invoer hoort precies één uitvoer.",
                 None,
                 None,
                 "Delen door nul mag niet, dus nul valt uit het domein.",
                 r"\(2\) en \(-2\) geven allebei \(4\). Dat mag: wat niet mag, is twee uitvoerwaarden "
                 r"bij één invoer.",
                 "De afhankelijke variabele staat op de verticale as; de onafhankelijke op de "
                 "horizontale.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-de-parabool-transformaties-en-functiekenmerken-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="In de topvorm lees je alles af: het teken vóór het kwadraat geeft de opening, en "
                    "de twee getallen geven de top. Let op: het getal in de haakjes keert van teken om.",
             waarom=[None]),
        dict(aanpak="Nulwaarden zoek je door de functiewaarde nul te stellen. Ontbind of neem de wortel "
                    "aan beide kanten.",
             waarom=[None]),
        dict(aanpak="De symmetrieas loopt door de top, dus precies in het midden tussen de twee "
                    "nulwaarden.",
             waarom=[None]),
        dict(aanpak="Vul nul in voor x. Wat overblijft is de constante term, en dat is meteen het "
                    "snijpunt met de verticale as.",
             waarom=[None]),
        dict(aanpak="Het bereik begint of eindigt bij de y-waarde van de top, naargelang de parabool "
                    "naar boven of naar beneden opent.",
             waarom=[None]),
        dict(aanpak="Een getal buiten het kwadraat verschuift verticaal, een getal binnen de haakjes "
                    "horizontaal en in de omgekeerde richting.",
             waarom=[None, None]),
        dict(aanpak="Opent de parabool naar boven, dan is de top het laagste punt en dus een minimum. "
                    "Naar beneden geeft een maximum.",
             waarom=[None]),
        dict(aanpak="De parabool keert om in de top. Links en rechts van de symmetrieas doet ze het "
                    "omgekeerde.",
             waarom=[None, None]),
        dict(aanpak="Het domein van een veelterm is heel R. Het bereik lees je af uit de top en de "
                    "opening.",
             waarom=[None]),
        dict(aanpak="Elke vorm van hetzelfde voorschrift toont iets anders. Kies de vorm waarin het "
                    "gevraagde al zichtbaar is.",
             waarom=[None]),
        dict(aanpak="Vertrek van de vorm die bij de gegevens past: de productvorm bij nulwaarden, de "
                    "topvorm bij een top.",
             waarom=[None]),
        dict(aanpak="Vul in en reken stap voor stap uit. Let bij een negatief getal op dat het kwadraat "
                    "positief wordt.",
             waarom=[None]),
        dict(aanpak="Bij een hyperbool deel je telkens. Let op wat er gebeurt als x heel klein of heel "
                    "groot wordt.",
             waarom=[None, None]),
        dict(aanpak="Lees eerst wat er precies verschuift of wegvalt, en kies dan pas.",
             waarom=[None, None]),
        dict(aanpak="Schrijf je uitleg in volle zinnen en vertrek van een eigenschap, niet van een "
                    "voorbeeld.",
             waarom=[None]),
        dict(aanpak="Loop bij elke uitspraak na of ze altijd geldt. Een tekening erbij helpt.",
             waarom=[
                 r"Bij \(D < 0\) snijdt de parabool de as niet, en bij \(D = 0\) raakt ze hem in één "
                 r"punt.",
                 None,
                 "Het tekenverloop toont waar de functie positief of negatief is. Stijgen en dalen lees "
                 "je af in het verloopschema.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-telproblemen-met-boom-en-venndiagram-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Bij opeenvolgende keuzes vermenigvuldig je het aantal mogelijkheden per stap. Tel "
                    "eerst de stappen, dan de keuzes per stap.",
             waarom=[None, None]),
        dict(aanpak="Blijft het aantal keuzes elke stap gelijk, dan is het een macht: het aantal keuzes "
                    "tot de macht het aantal stappen.",
             waarom=[None]),
        dict(aanpak="Teken van links naar rechts één laag per keuze. Het aantal eindpunten is het "
                    "antwoord.",
             waarom=[None]),
        dict(aanpak="Vraag je af of wat je koos opnieuw gekozen kan worden. Zo niet, dan daalt het "
                    "aantal keuzes bij elke stap met één.",
             waarom=[None]),
        dict(aanpak="Wie bij allebei hoort, is twee keer geteld. Tel de twee groepen op en trek de "
                    "overlap er één keer af.",
             waarom=[None]),
        dict(aanpak="Trek van het totaal af hoeveel er aan minstens één voorwaarde voldoen. Wat "
                    "overblijft, voldoet aan geen van beide.",
             waarom=[None]),
        dict(aanpak="Enkel de ene groep is die groep min de overlap. Teken desnoods het venndiagram "
                    "erbij.",
             waarom=[None]),
        dict(aanpak="Begin altijd bij het middenstuk, de overlap. Daarna vul je de buitenste delen in "
                    "door af te trekken.",
             waarom=[None]),
        dict(aanpak="Leer de tekens als woorden: de doorsnede is en, de vereniging is of, de "
                    "verticale strepen tellen.",
             waarom=[None]),
        dict(aanpak="De somregel werkt ook de andere kant op: uit drie van de vier getallen volgt het "
                    "vierde.",
             waarom=[None]),
        dict(aanpak="Zoek bij elk telprobleem of je beter het gevraagde telt of net het tegendeel. "
                    "Minstens één wijst bijna altijd op het tegendeel tellen.",
             waarom=[None, None]),
        dict(aanpak="Twee soorten problemen, twee gereedschappen: opeenvolgende keuzes vragen een "
                    "boomdiagram, overlappende groepen een venndiagram.",
             waarom=[None, None, None]),
        dict(aanpak="Loop bij elke uitspraak na welke regel ze gebruikt, en teken bij twijfel een klein "
                    "voorbeeld.",
             waarom=[
                 "Dan tel je de overlap twee keer. Trek ze één keer af.",
                 None,
                 None,
                 "Een venndiagram is net voor overlappende groepen. Opeenvolgende keuzes teken je in een "
                 "boomdiagram.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-statistiek-voorstellingen-centrum-en-spreiding-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je af of je met de gegevens kan rekenen (numeriek), en zo niet, of er een "
                    "volgorde in zit (geordend) of niet.",
             waarom=[None]),
        dict(aanpak="Een relatieve frequentie is het deel op het geheel. Vereenvoudig de breuk en "
                    "vermenigvuldig met honderd voor het percentage.",
             waarom=[None]),
        dict(aanpak="Controleer altijd je totaal: alle relatieve frequenties samen moeten honderd "
                    "procent geven.",
             waarom=[None]),
        dict(aanpak="Het klassenmidden is het gemiddelde van de twee grenzen: optellen en delen door "
                    "twee.",
             waarom=[None]),
        dict(aanpak="Kies je diagram naar de vraag: een verloop in de tijd is een lijn, een verdeling "
                    "van het geheel is een cirkel, klassen zijn een histogram.",
             waarom=[None]),
        dict(aanpak="Leer de symbolen samen met hun naam; op het examen staat vaak alleen het teken in "
                    "de vraag.",
             waarom=[None]),
        dict(aanpak="Rangschik de reeks altijd eerst. Het gemiddelde rekent met alle waarden, de "
                    "mediaan kijkt alleen naar het midden.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze. Hier vallen mediaan en modus toevallig samen; dat hoeft niet.",
             waarom=[None]),
        dict(aanpak="Bij een oneven aantal is de mediaan de middelste waarde; bij een even aantal het "
                    "gemiddelde van de twee middelste.",
             waarom=[None]),
        dict(aanpak="Deel de gerangschikte reeks in vier gelijke stukken. Q2 is de mediaan, Q1 en Q3 "
                    "zijn de medianen van de helften.",
             waarom=[None]),
        dict(aanpak="De vuistregel: bij uitschieters kies je de mediaan, want die laat zich niet "
                    "meetrekken.",
             waarom=[None, None]),
        dict(aanpak="Spreiding zegt hoe ver de waarden van het centrum liggen. Twee reeksen met "
                    "hetzelfde gemiddelde kunnen er heel anders uitzien.",
             waarom=[None, None]),
        dict(aanpak="Loop bij elke uitspraak na wat de maat precies meet, en of ze ook bij woorden "
                    "werkt of enkel bij getallen.",
             waarom=[
                 None,
                 "Komen twee waarden even vaak voor en vaker dan de rest, dan zijn er twee modi.",
                 "Net niet: de interkwartielafstand kijkt alleen naar de middelste helft, en een "
                 "uitschieter valt daarbuiten.",
                 None,
                 None,
                 "De modus is de meest voorkomende waarde, en dat werkt ook bij kleuren of merken. "
                 "Gemiddelde en mediaan vragen wel getallen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-misleiding-met-cijfers-en-verbanden-in-een-puntenwolk-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Procentpunt is het verschil tussen twee percentages; procent is de groei ten "
                    "opzichte van de beginwaarde. Reken ze allebei apart uit.",
             waarom=[None]),
        dict(aanpak="Zet het percentage om naar een kommagetal en vermenigvuldig. Boven honderd procent "
                    "wordt het getal groter.",
             waarom=[None]),
        dict(aanpak="Vermenigvuldig de factoren na elkaar. Opslag en korting van evenveel procent "
                    "heffen elkaar niet op, want ze rekenen op een ander bedrag.",
             waarom=[None]),
        dict(aanpak="Kijk bij elke grafiek eerst naar de assen: waar begint de as, en staan de stappen "
                    "op gelijke afstand?",
             waarom=[None, None]),
        dict(aanpak="Kijk ook naar wat er ontbreekt en naar het soort beeld dat gebruikt wordt. Een "
                    "tekening in drie dimensies overdrijft altijd.",
             waarom=[None, None]),
        dict(aanpak="Vraag bij elk cijfer twee dingen: hoeveel mensen of gevallen zitten erachter, en "
                    "van welke beginwaarde vertrekt de groei?",
             waarom=[None, None]),
        dict(aanpak="De correlatiecoëfficiënt zegt twee dingen tegelijk: het teken geeft de richting, "
                    "de grootte geeft hoe dicht de punten bij de rechte liggen.",
             waarom=[None]),
        dict(aanpak="Let bij elke vraag op het verschil tussen een beschrijving en een belofte. Een "
                    "trendlijn beschrijft, ze voorspelt geen enkel punt.",
             waarom=[None, None, None]),
        dict(aanpak="Zoek bij elk verband naar een derde factor die allebei verklaart, of naar een "
                    "omgekeerde richting.",
             waarom=[None, None, None]),
        dict(aanpak="Schrijf enkel op wat gemeten is, in welke groep, en zonder een oorzaak te "
                    "beweren.",
             waarom=[None]),
        dict(aanpak="Loop bij elke uitspraak na of ze over de cijfers zelf gaat of over de voorstelling "
                    "ervan.",
             waarom=[
                 None,
                 "Procentpunt is het verschil tussen twee percentages, procent is de relatieve groei. "
                 "Van 30 naar 33 is 3 procentpunt en 10 procent.",
                 None,
                 None,
                 None,
                 None,
             ]),
    ],
)
