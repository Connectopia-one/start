# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van Nederlands 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Dezelfde leerstof en dezelfde woorden, maar andere zinnen en andere
situaties. Bij lezen staat er daarom telkens een eigen tekstje in de bundel:
een leesvraag hoort op een echte tekst te staan, niet op het begrip alleen.
Wie hier iets bijschrijft, legt het eerst naast `../../start/nederlands.json`
en `../../start/nederlands-spelling.json`.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

W = "120px"
WW = "180px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Lukt een oefening niet? Sla ze over en kom er op het einde op terug.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-lezen"] = dict(
    vak="Nederlands", titel="Lezen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waar zoek je wat?",
             opdracht="Elke soort tekst heeft zijn eigen doel.",
             oefeningen=[
                 ("rij", [("hoe je lasagne maakt", "een recept"),
                          ("wat een woord betekent", "een woordenboek"),
                          ("het nieuws van gisteren", "een krant"),
                          ("hoe je een kast in elkaar zet", "een handleiding")],
                  "In welke soort tekst zoek je dit?", WW),
                 ("kies", "In welke tekst wil de schrijver je vooral iets doen kopen?",
                  ["een verslag", "een reclametekst", "een recept", "een dagboek"], 1),
                 ("waar", "In een informatieve tekst gaat het vooral om feiten.", True),
                 ("open", "Noem twee dingen waaraan je ziet dat een tekst een verhaal is en "
                          "geen informatieve tekst.",
                  "Bijvoorbeeld: er zijn personages, er gebeurt iets na elkaar, er staat "
                  "gesprek in, het is verzonnen, er is spanning.", 3),
             ]),

        dict(kop="Signaalwoorden",
             opdracht="Een signaalwoord verklapt hoe twee stukken tekst samenhangen.",
             oefeningen=[
                 ("rij", [("want", "een reden"), ("daarna", "een volgorde"),
                          ("maar", "een tegenstelling"), ("bijvoorbeeld", "een voorbeeld")],
                  "Wat geeft het woord aan?", WW),
                 ("kies", "\"Hij had honger, daarom kocht hij een broodje.\" Wat geeft "
                          "\"daarom\" aan?",
                  ["een tegenstelling", "een gevolg", "een tijdstip", "een voorbeeld"], 1),
                 ("open", "Vul aan: \"Ik wou gaan fietsen, … het regende de hele namiddag.\"",
                  "maar (ook goed: alleen, jammer genoeg)", 1),
             ]),

        dict(kop="Feit of mening",
             opdracht="Een feit kan je nakijken, een mening is wat iemand vindt.",
             oefeningen=[
                 ("rij", [("Hasselt ligt in Limburg.", "feit"),
                          ("Limburg is de mooiste provincie.", "mening"),
                          ("Een jaar heeft twaalf maanden.", "feit"),
                          ("Wiskunde is saai.", "mening")],
                  "Feit of mening?", W),
                 ("waar", "Aan woorden als \"volgens mij\" en \"ik vind\" herken je vaak een mening.",
                  True),
                 ("open", "Schrijf zelf één feit en één mening over je school.",
                  "Bijvoorbeeld. Feit: onze school heeft drie speelplaatsen. "
                  "Mening: de speelplaats is te klein.", 3),
             ]),

        dict(kop="Beeldspraak en moeilijke woorden",
             opdracht="Soms betekent een zin niet wat er letterlijk staat.",
             oefeningen=[
                 ("kies", "Wat betekent \"in de wolken zijn\"?",
                  ["heel blij zijn", "heel moe zijn", "verdrietig zijn", "in de war zijn"], 0),
                 ("kies", "\"Hij deed die nacht geen oog dicht.\" Wat betekent dat?",
                  ["Hij sliep niet.", "Hij keek weg.", "Hij kon niet zien.", "Hij huilde."], 0),
                 ("open", "Je komt in een tekst een woord tegen dat je niet kent. Schrijf twee "
                          "dingen op die je dan kan doen.",
                  "Bijvoorbeeld: verder lezen en uit de zin afleiden wat het betekent, "
                  "het opzoeken in een woordenboek, het aan iemand vragen, "
                  "kijken of je er een bekend woord in herkent.", 3),
                 ("waar", "Als je één gegeven snel wil terugvinden, lees je de tekst het best "
                          "woord voor woord van begin tot einde.", False),
             ]),

        dict(kop="Lees deze tekst",
             opdracht="Lees eerst de hele tekst. Daarna pas de vragen.",
             oefeningen=[
                 ("tekst",
                  "<p style='background:#f2f4ee;border-radius:14px;padding:14px 18px;"
                  "line-height:1.6'>De bibliotheek van Hasselt is verhuisd naar een nieuw "
                  "gebouw aan de Kunstlaan. Er zijn nu drie leeszalen en een apart hoekje "
                  "voor strips. Wie boeken wil lenen, heeft een lidkaart nodig. Die kaart is "
                  "gratis zolang je jonger bent dan achttien. De bib is open van dinsdag tot "
                  "en met zaterdag.</p>"),
                 ("open", "Waar staat de nieuwe bibliotheek?", "Aan de Kunstlaan, in Hasselt.", 1),
                 ("open", "Op welke twee dagen is de bib zeker gesloten?",
                  "Op zondag en op maandag.", 1),
                 ("open", "Voor wie is de lidkaart gratis?",
                  "Voor iedereen die jonger is dan achttien.", 1),
                 ("kies", "Wat is de hoofdgedachte van deze tekst?",
                  ["De bib is verhuisd, en wat je moet weten om er te lenen.",
                   "Strips zijn heel populair bij kinderen.",
                   "In Hasselt wordt veel gebouwd.",
                   "Een lidkaart is duur geworden."], 0),
                 ("waar", "In de tekst staat hoeveel boeken je tegelijk mag lenen.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-schrijven"] = dict(
    vak="Nederlands", titel="Schrijven",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Meervouden",
             opdracht="Sommige meervouden volgen geen regel: die moet je kennen.",
             oefeningen=[
                 ("rij", [("de koe", "de koeien"), ("het schip", "de schepen"),
                          ("de lade", "de laden of de lades"), ("het lied", "de liederen"),
                          ("de stoel", "de stoelen"), ("het glas", "de glazen")],
                  "Zet in het meervoud.", WW),
                 ("waar", "\"Eieren\" is het meervoud van \"ei\".", True),
                 ("kies", "Welk meervoud is juist?",
                  ["museums", "museumen", "musea", "museaën"], 2),
             ]),

        dict(kop="Werkwoorden in de zin",
             opdracht="Kijk eerst wie er iets doet, en dan pas naar de tijd.",
             oefeningen=[
                 ("rij", [("Ik … het raam. (sluiten)", "sluit"),
                          ("Wij … in de tuin. (spelen)", "spelen"),
                          ("Zij … een brief. (schrijven)", "schrijft"),
                          ("Jullie … te laat. (komen)", "komen")],
                  "Vul het werkwoord in, in de tegenwoordige tijd.", W),
                 ("rij", [("gisteren (wandelen), ik", "wandelde"),
                          ("gisteren (fietsen), wij", "fietsten"),
                          ("gisteren (lachen), zij", "lachte"),
                          ("gisteren (bouwen), ik", "bouwde")],
                  "Zet in de verleden tijd.", W),
                 ("open", "Schrijf deze zin in de toekomende tijd: \"Wij gaan naar zee.\"",
                  "Wij zullen naar zee gaan. (Ook goed: Wij gaan morgen naar zee.)", 1),
                 ("waar", "In de zin \"Zij loopt naar school\" staat het werkwoord in het meervoud.",
                  False),
             ]),

        dict(kop="Hoofdletters en leestekens",
             opdracht="Zet de zin helemaal juist over op de lijn.",
             oefeningen=[
                 ("open", "Schrijf juist over: \"op maandag gaan we naar brussel\"",
                  "Op maandag gaan we naar Brussel.", 1),
                 ("open", "Schrijf juist over: \"wie komt er mee naar de film vroeg lotte\"",
                  "\"Wie komt er mee naar de film?\" vroeg Lotte.", 2),
                 ("kies", "Welke zin heeft de juiste leestekens?",
                  ["Ik kocht brood, kaas en melk.", "Ik kocht brood kaas en melk.",
                   "Ik kocht brood, kaas, en melk.", "Ik kocht, brood, kaas en melk."], 0),
                 ("waar", "Achter een vraag hoort een vraagteken en niet een uitroepteken.", True),
                 ("open", "Welk leesteken zet je in het midden van deze zin, en waarom? "
                          "\"Het regende … toch gingen we buiten spelen.\"",
                  "Een punt of een puntkomma; ook \"maar\" met een komma ervoor kan. "
                  "Het zijn twee zinnen die tegenover elkaar staan.", 2),
             ]),

        dict(kop="Een tekst opbouwen",
             opdracht="Denk eerst na over wat er eerst komt, en schrijf dan pas.",
             oefeningen=[
                 ("waar", "Een alinea begint op een nieuwe regel en gaat over één onderwerp.", True),
                 ("rij", [("begin", "wie, waar en wanneer"),
                          ("midden", "het probleem of de gebeurtenis"),
                          ("einde", "hoe het afloopt")],
                  "Wat hoort er in dat deel van een verhaal?", WW),
                 ("kies", "Je schrijft een mail aan de directeur van je school. Hoe begin je?",
                  ["Hey!", "Geachte mevrouw", "Dag jij", "Hallo daar"], 1),
                 ("open", "Schrijf de eerste twee zinnen van een verslag over een uitstap met "
                          "de klas. Zet erin wie, waar en wanneer.",
                  "Bijvoorbeeld: Op vrijdag 12 mei gingen wij met het vijfde leerjaar naar het "
                  "natuurpark in Genk. We vertrokken om negen uur met de bus.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-spreken-en-luisteren"] = dict(
    vak="Nederlands", titel="Spreken en luisteren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Luisteren naar een ander",
             opdracht="Goed luisteren is iets dat je doet, niet iets dat vanzelf gebeurt.",
             oefeningen=[
                 ("kies", "Iemand vertelt iets en jij weet al wat je wil antwoorden. Wat doe je?",
                  ["Je onderbreekt, anders vergeet je het.",
                   "Je laat de ander uitspreken en antwoordt daarna.",
                   "Je kijkt naar je gsm tot hij klaar is.",
                   "Je begint over iets anders."], 1),
                 ("open", "Je hebt iets niet goed verstaan. Schrijf op wat je dan zegt.",
                  "Bijvoorbeeld: Sorry, dat heb ik niet goed verstaan. Kan je dat nog eens zeggen?", 2),
                 ("waar", "Iemand aankijken terwijl hij spreekt, toont dat je luistert.", True),
                 ("open", "Wat is samenvatten? Leg het uit in één zin.",
                  "Kort in je eigen woorden zeggen wat iemand verteld heeft, zonder alles te "
                  "herhalen.", 2),
             ]),

        dict(kop="Een spreekbeurt geven",
             opdracht="Denk aan je publiek: zij horen het voor de eerste keer.",
             oefeningen=[
                 ("rij", [("te snel praten", "moeilijk te volgen"),
                          ("naar de grond kijken", "je publiek haakt af"),
                          ("een volle dia met tekst", "niemand leest mee"),
                          ("stilstaan bij je punt", "iedereen kan mee")],
                  "Wat is het gevolg?", WW),
                 ("kies", "Wat zet je het best op een dia bij je spreekbeurt?",
                  ["je hele tekst, woord voor woord", "een paar kernwoorden en een beeld",
                   "niets, een dia leidt af", "zoveel mogelijk informatie"], 1),
                 ("open", "Noem drie dingen die je klaarzet vóór je spreekbeurt begint.",
                  "Bijvoorbeeld: je kaartjes met kernwoorden, je beelden of dia's, "
                  "iets om te tonen, je tijd afspreken, één keer luidop oefenen.", 3),
                 ("waar", "Snel praten maakt een spreekbeurt levendiger en dus makkelijker "
                          "te volgen.", False),
             ]),

        dict(kop="Een gesprek voeren",
             opdracht="Ook als je het niet eens bent, blijf je beleefd.",
             oefeningen=[
                 ("open", "Wat is een argument? Leg het uit in één zin.",
                  "Een reden die je geeft om uit te leggen waarom je iets vindt.", 2),
                 ("open", "Jij vindt dat er langer mag gespeeld worden op de speelplaats. "
                          "Schrijf één argument op.",
                  "Bijvoorbeeld: na een halfuur bewegen kunnen we ons weer beter concentreren "
                  "in de klas.", 2),
                 ("kies", "In een groepsgesprek heeft iemand nog niets gezegd. Wat doe je?",
                  ["niets, hij zwijgt zelf wel",
                   "je vraagt hem wat hij ervan vindt",
                   "je zegt dat hij moet meedoen",
                   "je praat wat luider"], 1),
                 ("rij", [("Ik ben het daar niet mee eens, want …", "beleefd"),
                          ("Dat is echt dom.", "niet beleefd"),
                          ("Dat had ik zo nog niet bekeken.", "beleefd"),
                          ("Jij snapt er niets van.", "niet beleefd")],
                  "Beleefd of niet beleefd in een discussie?", WW),
             ]),

        dict(kop="Bellen en vragen stellen",
             opdracht="Aan de telefoon ziet de ander je niet, dus zeg je meer dan gewoonlijk.",
             oefeningen=[
                 ("open", "Je belt naar de sportclub om te vragen wanneer de training begint. "
                          "Schrijf de eerste twee zinnen die je zegt.",
                  "Bijvoorbeeld: Goedemiddag, u spreekt met Sara Peeters. Ik bel om te vragen "
                  "hoe laat de training op woensdag begint.", 3),
                 ("kies", "Welke vraag houdt een gesprek het best op gang?",
                  ["Vond je het leuk?", "Wat vond je het leukste eraan?",
                   "Was het saai?", "Ben je moe?"], 1),
                 ("waar", "Aan de telefoon wacht je het best tot de ander vraagt wie je bent.",
                  False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-taalsysteem-en-taalgebruik"] = dict(
    vak="Nederlands", titel="Taalsysteem en taalgebruik",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Woordsoorten",
             opdracht="Schrijf bij elk woord welke soort het is.",
             oefeningen=[
                 ("rij", [("zwemmen", "werkwoord"), ("tafel", "zelfstandig naamwoord"),
                          ("snel", "bijvoeglijk naamwoord"), ("onder", "voorzetsel"),
                          ("zij", "persoonlijk voornaamwoord"), ("drie", "telwoord")],
                  "Welke woordsoort is het?", WW),
                 ("kies", "Welk woord is een voorzetsel?",
                  ["tussen", "lopen", "mooi", "hij"], 0),
                 ("waar", "De, het en een zijn lidwoorden, geen voornaamwoorden.", True),
             ]),

        dict(kop="Zinsdelen",
             opdracht="Vraag je telkens af: wie of wat doet het, en wat wordt er gedaan?",
             oefeningen=[
                 ("rij", [("De buurman wast zijn auto.", "de buurman"),
                          ("Mijn zus zingt mooi.", "mijn zus"),
                          ("Gisteren vertrok de trein te laat.", "de trein"),
                          ("In de tuin bloeien de rozen.", "de rozen")],
                  "Wat is het onderwerp?", WW),
                 ("rij", [("Ik lees een strip.", "een strip"),
                          ("Zij bakt een taart.", "een taart"),
                          ("De hond apporteert de bal.", "de bal")],
                  "Wat is het lijdend voorwerp?", WW),
                 ("open", "Maak zelf een zin met \"de kat\" als onderwerp en \"een muis\" als "
                          "lijdend voorwerp.",
                  "Bijvoorbeeld: De kat vangt een muis.", 2),
             ]),

        dict(kop="Woorden bouwen",
             opdracht="Een samenstelling is één woord gemaakt van twee hele woorden.",
             oefeningen=[
                 ("rij", [("voetbal", "samenstelling"), ("vriendelijk", "geen samenstelling"),
                          ("boekentas", "samenstelling"), ("snelheid", "geen samenstelling")],
                  "Samenstelling of niet?", WW),
                 ("rij", [("regenjas", "2"), ("computer", "3"),
                          ("aardappel", "3"), ("school", "1")],
                  "Hoeveel lettergrepen?", "70px"),
                 ("kies", "Welk woord is een verkleinwoord?",
                  ["huisje", "huizen", "behuizing", "huiselijk"], 0),
                 ("waar", "\"Snelheid\" is gemaakt van twee hele woorden, dus het is een "
                          "samenstelling.", False),
             ]),

        dict(kop="Uitdrukkingen en gezegden",
             opdracht="Deze zinnen betekenen niet wat er letterlijk staat.",
             oefeningen=[
                 ("rij", [("de kat uit de boom kijken", "eerst afwachten"),
                          ("de koe bij de horens vatten", "meteen aanpakken"),
                          ("ergens geen kaas van gegeten hebben", "er niets van kennen")],
                  "Wat betekent het?", WW),
                 ("kies", "Wat betekent \"een appeltje voor de dorst\"?",
                  ["iets bewaren voor later", "een gezond tussendoortje",
                   "een klein probleem", "een lange wandeling"], 0),
                 ("open", "Schrijf een uitdrukking op die jij kent, en leg erbij uit wat ze "
                          "betekent.",
                  "Bijvoorbeeld: \"de plank misslaan\" betekent dat je er helemaal naast zit.", 3),
                 ("open", "Welk woord hoort niet in dit rijtje, en waarom? "
                          "&nbsp;lepel &middot; vork &middot; mes &middot; stoel",
                  "Stoel. De andere drie zijn bestek, iets waarmee je eet.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-literatuur"] = dict(
    vak="Nederlands", titel="Literatuur",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Soorten verhalen",
             opdracht="Elk soort verhaal heeft zijn eigen kenmerken.",
             oefeningen=[
                 ("rij", [("dieren die praten, met een les op het einde", "een fabel"),
                          ("een heks, een prins en een goede afloop", "een sprookje"),
                          ("goden die de wereld verklaren", "een mythe"),
                          ("waargebeurd, met echte namen en jaartallen", "non-fictie")],
                  "Welk soort tekst is het?", WW),
                 ("kies", "Wat is een sage of een legende meestal?",
                  ["een verhaal dat aan een echte plaats of persoon vasthangt",
                   "een verzonnen dierenverhaal", "een gedicht zonder rijm",
                   "een handleiding"], 0),
                 ("waar", "In een sprookje mag er iets gebeuren dat in het echt niet kan.", True),
                 ("open", "Schrijf de titel op van een boek dat je graag gelezen hebt, en zet "
                          "er in één zin bij waarover het gaat.",
                  "Elk antwoord is goed zolang er een titel staat en één zin over de inhoud.", 3),
             ]),

        dict(kop="Wie is wie in een boek",
             opdracht="De schrijver, de verteller en de hoofdpersoon zijn drie verschillende dingen.",
             oefeningen=[
                 ("rij", [("bedenkt en schrijft het boek", "de schrijver of auteur"),
                          ("maakt de tekeningen", "de illustrator"),
                          ("het verhaal gaat vooral over hem of haar", "de hoofdpersoon"),
                          ("staat achteraan en vertelt waarover het gaat", "de flaptekst")],
                  "Hoe noem je dat?", WW),
                 ("waar", "De verteller van een verhaal is altijd de schrijver zelf.", False),
                 ("open", "Wat bedoelt men met \"waar speelt het verhaal zich af\"? "
                          "Leg het uit in je eigen woorden.",
                  "De plaats waar het verhaal gebeurt, bijvoorbeeld een school, een bos of "
                  "een ander land. Soms hoort de tijd er ook bij.", 2),
             ]),

        dict(kop="Gedichten",
             opdracht="Een gedicht zegt veel in weinig woorden.",
             oefeningen=[
                 ("rij", [("maan", "laan, aan, gaan, traan"), ("boom", "droom, stroom, room"),
                          ("licht", "gedicht, zicht, dicht")],
                  "Schrijf een woord op dat hierop rijmt.", WW),
                 ("waar", "Een gedicht moet altijd rijmen.", False),
                 ("kies", "Wat is een kenmerk van veel gedichten?",
                  ["het staat in korte regels onder elkaar",
                   "het is altijd langer dan een verhaal",
                   "er staan nooit moeilijke woorden in",
                   "het eindigt altijd goed"], 0),
                 ("open", "Schrijf twee regels die op elkaar rijmen. Ze mogen over eender wat "
                          "gaan.", "Elk antwoord is goed zolang de twee regels rijmen.", 3),
             ]),

        dict(kop="Spanning en hoofdgedachte",
             opdracht="Waarom blijf je doorlezen?",
             oefeningen=[
                 ("open", "Wat is een cliffhanger? Leg het uit in één zin.",
                  "Een hoofdstuk dat stopt op een spannend moment, zodat je wil weten hoe het "
                  "verdergaat.", 2),
                 ("open", "Wat is de hoofdgedachte van een verhaal? Leg het uit in één zin.",
                  "Waar het verhaal eigenlijk over gaat, de boodschap die de schrijver "
                  "meegeeft.", 2),
                 ("kies", "Wat maakt een verhaal spannend?",
                  ["je weet nog niet hoe het afloopt", "er staan veel moeilijke woorden in",
                   "het is heel lang", "er zijn veel tekeningen"], 0),
                 ("waar", "Een toneelstuk lees je vooral als gesprek, met de naam van het "
                          "personage ervoor.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-spelling"] = dict(
    vak="Nederlands", titel="Spelling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Open en gesloten lettergrepen",
             opdracht="Verdeel het woord eerst in stukjes en luister naar de klank.",
             oefeningen=[
                 ("rij", [("de poot", "de poten"), ("de pot", "de potten"),
                          ("de zaak", "de zaken"), ("de zak", "de zakken"),
                          ("de neus", "de neuzen"), ("het huis", "de huizen")],
                  "Zet in het meervoud.", WW),
                 ("waar", "In \"bo-men\" is de eerste lettergreep open, dus schrijf je maar één o.",
                  True),
                 ("open", "Waarom schrijf je \"bommen\" met dubbele m en \"bomen\" met één? "
                          "Leg het uit in je eigen woorden.",
                  "In \"bom-men\" is de eerste lettergreep gesloten en kort, daarom verdubbelt "
                  "de m. In \"bo-men\" is ze open en lang, dus één m en één o.", 3),
             ]),

        dict(kop="De stam van een werkwoord",
             opdracht="De stam vind je door -en weg te halen van het hele werkwoord.",
             oefeningen=[
                 ("rij", [("wandelen", "wandel"), ("praten", "praat"),
                          ("leven", "leef"), ("razen", "raas"),
                          ("zwemmen", "zwem"), ("geven", "geef")],
                  "Wat is de stam?", W),
                 ("waar", "De stam van \"leven\" is \"lev\".", False),
             ]),

        dict(kop="Ik, jij en hij",
             opdracht="Bij hij, zij en het komt er een t bij. Bij jij achter het werkwoord niet.",
             oefeningen=[
                 ("rij", [("ik … (antwoorden)", "antwoord"), ("jij … (antwoorden)", "antwoordt"),
                          ("… jij? (antwoorden)", "antwoord"), ("hij … (antwoorden)", "antwoordt")],
                  "Vul de juiste vorm in.", WW),
                 ("rij", [("ik … (worden)", "word"), ("zij … (worden)", "wordt"),
                          ("ik … (vinden)", "vind"), ("… jij dat? (vinden)", "vind")],
                  "Vul de juiste vorm in.", W),
                 ("waar", "In de vraag \"Wat word jij later?\" hoort er geen t achter word.", True),
                 ("open", "Leg uit waarom er in \"Word jij boos?\" geen t staat, maar in "
                          "\"Jij wordt boos.\" wel.",
                  "Staat jij achter het werkwoord, dan valt de t weg. Staat jij ervoor, dan "
                  "blijft ze staan.", 3),
             ]),

        dict(kop="Verleden tijd en 't kofschip",
             opdracht="Luister naar de laatste klank van de stam, niet naar de letter.",
             oefeningen=[
                 ("rij", [("ik (koken)", "kookte"), ("ik (leren)", "leerde"),
                          ("ik (blaffen)", "blafte"), ("ik (razen)", "raasde"),
                          ("ik (stoppen)", "stopte"), ("ik (wonen)", "woonde")],
                  "Zet in de verleden tijd.", WW),
                 ("open", "Waarom is het \"ik verhuisde\" en niet \"ik verhuiste\", terwijl er "
                          "een s in staat?",
                  "De stam is verhuis, maar je hoort aan het einde een z-klank (verhuizen). "
                  "Bij 't kofschip luister je naar de klank, niet naar de letter.", 3),
                 ("rij", [("ik heb (hopen)", "gehoopt"), ("wij hebben (fietsen)", "gefietst"),
                          ("zij heeft (leren)", "geleerd"), ("ik heb (bouwen)", "gebouwd")],
                  "Vul het voltooid deelwoord in.", WW),
                 ("waar", "Elk voltooid deelwoord eindigt op -en.", False),
             ]),

        dict(kop="Verkleinwoorden en hoofdletters",
             opdracht="Een verkleinwoord is altijd \"het\".",
             oefeningen=[
                 ("rij", [("de stoel", "het stoeltje"), ("de boom", "het boompje"),
                          ("de koning", "het koninkje"), ("het raam", "het raampje")],
                  "Maak er een verkleinwoord van.", WW),
                 ("waar", "Namen van maanden krijgen in het Nederlands een hoofdletter.", False),
                 ("open", "Schrijf juist over: \"volgende week dinsdag gaan sofie en ik naar "
                          "antwerpen\"",
                  "Volgende week dinsdag gaan Sofie en ik naar Antwerpen.", 2),
             ]),
    ],
)
