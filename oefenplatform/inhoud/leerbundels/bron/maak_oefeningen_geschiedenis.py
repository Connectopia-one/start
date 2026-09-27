# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van geschiedenis 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere jaartallen om mee te rekenen, andere bronnen om te beoordelen,
en opdrachten waarbij een kind zelf iets op een tijdlijn zet. Wie hier iets
bijschrijft, legt het eerst naast `../../start/geschiedenis.json`.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

W = "120px"
WW = "180px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag mag je je berekening ernaast zetten.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-tijd-en-tijdlijn"] = dict(
    vak="Geschiedenis", titel="Tijd en tijdlijn",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Rekenen met tijd",
             opdracht="Schrijf je berekening ernaast als dat helpt.",
             oefeningen=[
                 ("rij", [("een decennium", "10 jaar"), ("een halve eeuw", "50 jaar"),
                          ("een kwart eeuw", "25 jaar"), ("een millennium", "1 000 jaar")],
                  "Hoeveel jaar is dat?", WW),
                 ("rij", [("1815 tot 1914", "99 jaar"), ("1945 tot 2026", "81 jaar"),
                          ("1302 tot 1830", "528 jaar"), ("100 v.Chr. tot 100 n.Chr.", "200 jaar")],
                  "Hoeveel jaar zit ertussen?", WW),
                 ("rij", [("1492", "de 15de eeuw"), ("1815", "de 19de eeuw"),
                          ("2026", "de 21ste eeuw"), ("999", "de 10de eeuw")],
                  "In welke eeuw ligt dat jaar?", WW),
                 ("open", "Waarom ligt het jaar 1500 nog in de 15de eeuw en niet in de 16de? "
                          "Leg het uit.",
                  "Een eeuw loopt van jaar 01 tot en met jaar 00. De 15de eeuw loopt dus van "
                  "1401 tot en met 1500; de 16de begint pas in 1501.", 3),
             ]),

        dict(kop="Voor en na Christus",
             opdracht="Jaartallen voor Christus tellen omgekeerd.",
             oefeningen=[
                 ("rij", [("800 v.Chr. of 200 v.Chr.", "800 v.Chr."),
                          ("50 v.Chr. of 50 n.Chr.", "50 v.Chr."),
                          ("1 n.Chr. of 30 v.Chr.", "30 v.Chr.")],
                  "Welk jaartal is het oudste?", WW),
                 ("waar", "Er bestaat geen jaar 0: na 1 v.Chr. komt meteen 1 n.Chr.", True),
                 ("teken", "Teken een tijdlijn en zet deze vier erop: 500 v.Chr., het jaar 1, "
                           "1302 en 2026.",
                  "Van links naar rechts: 500 v.Chr., 1, 1302, 2026. De afstanden hoeven niet "
                  "precies te kloppen, de volgorde wel.", 40),
             ]),

        dict(kop="Bronnen beoordelen",
             opdracht="Wie heeft het geschreven, wanneer, en waarom?",
             oefeningen=[
                 ("rij", [("een dagboek uit 1943", "primaire bron"),
                          ("een geschiedenisboek van dit jaar", "secundaire bron"),
                          ("een Romeinse munt", "primaire bron"),
                          ("een film over de middeleeuwen", "secundaire bron")],
                  "Primaire of secundaire bron?", WW),
                 ("open", "Twee bronnen vertellen iets anders over dezelfde gebeurtenis. "
                          "Wat doe je dan het best?",
                  "Je zoekt nog meer bronnen en je kijkt wie ze geschreven heeft, wanneer, en "
                  "of iemand er belang bij had om het anders voor te stellen.", 3),
                 ("open", "Je wil weten hoe een Romeinse stad eruitzag. Noem twee soorten "
                          "bronnen die je daarbij helpen.",
                  "Bijvoorbeeld: opgravingen en ruïnes, muurschilderingen en mozaïeken, "
                  "voorwerpen uit die tijd, teksten van Romeinse schrijvers, munten.", 3),
                 ("waar", "Alles wat in een geschiedenisboek staat, is zeker precies zo gebeurd.",
                  False),
             ]),

        dict(kop="Periodes",
             opdracht="Historici delen de tijd op om overzicht te houden.",
             oefeningen=[
                 ("open", "Zet deze periodes in de juiste volgorde: middeleeuwen &middot; "
                          "nieuwste tijd &middot; prehistorie &middot; oudheid &middot; nieuwe tijd",
                  "Prehistorie, oudheid, middeleeuwen, nieuwe tijd, nieuwste tijd.", 2),
                 ("open", "Wat is het grote verschil tussen de prehistorie en de geschiedenis?",
                  "In de prehistorie bestond er nog geen schrift. We weten er alleen iets over "
                  "door wat er opgegraven wordt. Vanaf het schrift spreken we van geschiedenis.", 3),
                 ("kies", "Wat is een anachronisme?",
                  ["iets dat in de verkeerde tijd staat, zoals een gsm in een riddertijd",
                   "een heel oud voorwerp", "een tekening van een archeoloog",
                   "een jaartal voor Christus"], 0),
                 ("open", "Wat doet een archeoloog, en wat doet een historicus? Schrijf van "
                          "elk één zin.",
                  "Een archeoloog graaft sporen en voorwerpen op uit de bodem. Een historicus "
                  "onderzoekt vooral geschreven bronnen en legt verbanden.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-de-prehistorie-tot-de-romeinen"] = dict(
    vak="Geschiedenis", titel="Van de prehistorie tot de Romeinen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De prehistorie",
             opdracht="Denk aan hoe mensen aan hun eten kwamen.",
             oefeningen=[
                 ("rij", [("steentijd", "steen, been en hout"),
                          ("bronstijd", "brons, een mengsel van koper en tin"),
                          ("ijzertijd", "ijzer")],
                  "Waarvan maakte men er gereedschap?", WW),
                 ("open", "Wat veranderde er in het leven van de mensen toen ze aan landbouw "
                          "begonnen? Noem twee dingen.",
                  "Ze bleven op één plaats wonen in plaats van rond te trekken, ze temden "
                  "dieren, er ontstonden dorpen, er kwam voorraad en dus ook bezit en "
                  "verschillen tussen mensen.", 3),
                 ("open", "Waarom woonden mensen in de prehistorie graag dicht bij water?",
                  "Ze hadden drinkwater nodig, er kwamen dieren drinken die ze konden jagen, "
                  "er was vis, en over water kon je je makkelijker verplaatsen.", 3),
                 ("waar", "De bronstijd kwam vóór de ijzertijd.", True),
             ]),

        dict(kop="Egypte en Griekenland",
             opdracht="Twee beschavingen waar wij nog altijd iets van merken.",
             oefeningen=[
                 ("rij", [("de rivier van het oude Egypte", "de Nijl"),
                          ("het schrift van de Egyptenaren", "hiërogliefen"),
                          ("de tempel op de Akropolis", "het Parthenon"),
                          ("de stad van de democratie", "Athene")],
                  "Vul aan.", WW),
                 ("open", "Waarom was de Nijl zo belangrijk voor het oude Egypte?",
                  "De rivier overstroomde elk jaar en liet vruchtbaar slib achter, waardoor er "
                  "landbouw mogelijk was in een woestijngebied. Ze diende ook als weg.", 3),
                 ("open", "In het oude Athene mocht lang niet iedereen meestemmen. Wie wel, en "
                          "wie niet?",
                  "Alleen vrije mannen die burger van Athene waren. Vrouwen, slaven en mensen "
                  "van buiten de stad mochten niet meestemmen.", 3),
                 ("kies", "Wat hebben de Grieken bedacht en wat wij nog altijd doen?",
                  ["het theater met toneelstukken", "de boekdrukkunst",
                   "het aquaduct", "de kalender met schrikkeljaren"], 0),
             ]),

        dict(kop="De Romeinen",
             opdracht="Denk aan wat er van hen nog overblijft in onze taal en ons land.",
             oefeningen=[
                 ("rij", [("openbare badhuizen", "de thermen"),
                          ("een rond gebouw voor spelen", "het amfitheater"),
                          ("een brug die water aanvoert", "het aquaduct"),
                          ("een grote boerderij op het platteland", "de villa")],
                  "Hoe heet dat bij de Romeinen?", WW),
                 ("open", "Waarom legden de Romeinen hun wegen zo recht mogelijk aan?",
                  "Zo konden legers en boodschappers zo snel mogelijk van de ene plaats naar "
                  "de andere. Een rechte weg is ook korter en makkelijker te onderhouden.", 3),
                 ("open", "Noem drie dingen die wij vandaag nog van de Romeinen hebben.",
                  "Bijvoorbeeld: ons alfabet, veel woorden uit het Latijn, de namen van "
                  "maanden, rechte wegen, beton en bogen in de bouw, het idee van een stad "
                  "met een plein en openbare gebouwen.", 3),
                 ("waar", "De Romeinen noemden ons gebied Gallia Belgica.", True),
                 ("open", "Wat was een slaaf in de Romeinse tijd? Leg uit in je eigen woorden.",
                  "Iemand die geen vrij mens was maar eigendom van een ander, die moest werken "
                  "zonder loon en zelf niets te zeggen had. Vaak krijgsgevangenen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-de-middeleeuwen-tot-nu"] = dict(
    vak="Geschiedenis", titel="Van de middeleeuwen tot nu",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De middeleeuwen",
             opdracht="De meeste mensen waren boer, en heel weinigen konden lezen.",
             oefeningen=[
                 ("rij", [("de edelman die grond uitleent", "de leenheer"),
                          ("de vereniging van ambachtslieden", "de gilde"),
                          ("de grote kerk van een bisschop", "de kathedraal"),
                          ("iemand die een vak beheerst, zoals smid", "een ambachtsman")],
                  "Hoe noem je dat?", WW),
                 ("open", "Waarom bouwde men een kasteel graag op een heuvel of aan een rivier?",
                  "Vanaf een heuvel zie je de vijand van ver komen en is aanvallen lastig. "
                  "Een rivier is een natuurlijke gracht en zorgt voor water en aanvoer.", 3),
                 ("open", "Waarom waren de Vlaamse steden in de middeleeuwen zo rijk?",
                  "Door de lakennijverheid: wol uit Engeland werd hier tot fijn laken geweven "
                  "en in heel Europa verkocht. De steden lagen ook goed voor de handel.", 3),
                 ("waar", "In de middeleeuwen konden de meeste mensen lezen en schrijven.", False),
             ]),

        dict(kop="Jaartallen op een rij",
             opdracht="Schrijf het juiste jaartal, of wat er toen gebeurde.",
             oefeningen=[
                 ("rij", [("1302", "de Guldensporenslag"),
                          ("1492", "Columbus bereikt Amerika"),
                          ("1830", "België wordt onafhankelijk"),
                          ("1969", "de eerste mens op de maan")],
                  "Wat gebeurde er in dat jaar?", WW),
                 ("rij", [("begin van de Eerste Wereldoorlog", "1914"),
                          ("begin van de Tweede Wereldoorlog", "1939"),
                          ("einde van de Tweede Wereldoorlog", "1945"),
                          ("de Berlijnse Muur valt", "1989")],
                  "In welk jaar?", W),
                 ("open", "Welke van de twee wereldoorlogen duurde het langst? Reken het uit.",
                  "De Eerste: 1914 tot 1918, dus vier jaar. De Tweede duurde van 1939 tot 1945, "
                  "dus zes jaar. De Tweede duurde dus langer.", 3),
             ]),

        dict(kop="De industriële revolutie",
             opdracht="Machines veranderden hoe en waar mensen werkten.",
             oefeningen=[
                 ("open", "Noem drie dingen die veranderden door de industriële revolutie.",
                  "Bijvoorbeeld: machines namen handwerk over, mensen trokken van het "
                  "platteland naar de fabrieksstad, er kwamen fabrieken en mijnen, er werd "
                  "met stoom gewerkt, goederen werden veel goedkoper, en er ontstonden "
                  "lange werkdagen en kinderarbeid.", 3),
                 ("open", "Wat veranderde er voor kinderen toen de leerplicht kwam?",
                  "Ze moesten naar school in plaats van te werken in een fabriek of een mijn. "
                  "Daardoor leerde iedereen lezen en schrijven, ook arme kinderen.", 3),
                 ("waar", "De industriële revolutie kwam op gang door de stoommachine.", True),
                 ("open", "Waarvoor dienden de steenkoolmijnen in Limburg?",
                  "Om steenkool te winnen, de brandstof voor fabrieken, treinen en "
                  "verwarming. Er kwamen veel mensen van elders werken, ook uit het "
                  "buitenland.", 3),
             ]),

        dict(kop="Rechten en samenleven",
             opdracht="Veel van wat vandaag gewoon lijkt, is er pas na lange strijd gekomen.",
             oefeningen=[
                 ("open", "Wat is een democratie? Leg het uit in je eigen woorden.",
                  "Een land waar het volk meebeslist, meestal door te stemmen voor mensen die "
                  "hen vertegenwoordigen, en waar er regels en rechten voor iedereen gelden.", 3),
                 ("open", "Noem twee rechten die er vroeger niet waren en er nu wel zijn.",
                  "Bijvoorbeeld: stemrecht voor vrouwen, leerplicht, verbod op kinderarbeid, "
                  "recht op vakantie, ziekteverzekering.", 3),
                 ("open", "Waarvoor werd de Europese Unie vooral opgericht?",
                  "Om na twee wereldoorlogen samen te werken in plaats van oorlog te voeren. "
                  "Eerst met steenkool en staal, later met handel, een gemeenschappelijke "
                  "markt en de euro.", 3),
                 ("open", "Waarom is het belangrijk om over het verleden te leren? Schrijf "
                          "je eigen antwoord.",
                  "Bijvoorbeeld: om te begrijpen hoe onze wereld geworden is wat ze is, om "
                  "dezelfde fouten niet te herhalen, en om te zien dat dingen kunnen "
                  "veranderen.", 3),
             ]),
    ],
)
