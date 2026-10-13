# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Engels 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

Net als de vragen op het scherm dekt dit **alleen het schriftelijke Engels**:
lezen, schrijven, woordenschat en grammatica. Luisteren en spreken staan er
niet in; daar heb je geluid en een gesprekspartner voor nodig. Wat je zonder
scherm kan oefenen, staat als tip bij de leerbundel.

Het ERK-niveau is B1+ tot B2. De oefeningen zijn met opzet ándere opgaven dan
die van het hoofdstuk op het scherm: waar het scherm vraagt wat een woord
betekent, vraagt de bundel om het zelf te schrijven of in een zin te zetten.
Wie hier iets bijschrijft, legt het eerst naast `../../beyond/engels.json` en
naast de leerbundel van hetzelfde thema in `maak_engels_beyond.py`.

Een leesvraag hoort op een echte Engelse tekst te staan, dus de leesbundels
dragen hun eigen tekst mee.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Engels"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NIVEAU = "-beyond"
VOOR = "oefenbundel-"

W = "150px"
WW = "220px"
WL = "280px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Ken je een woord niet? Kijk eerst of het op een Nederlands of Duits woord lijkt.",
    "Schrijf je antwoord in het Engels, tenzij er uitdrukkelijk iets anders staat.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

HOE_LEZEN = [
    "Lees de tekst eerst helemaal door. Je moet niet elk woord kennen.",
    "Onderstreep de woorden die je niet kent en probeer ze te raden uit de zin eromheen.",
    "Kom bij elke vraag terug naar de tekst.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("een-engelse-tekst-analyseren",
    titel="Een Engelse tekst analyseren",
    onder="Twee teksten en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="Text A", opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>The library that lends tools</h3>"
                  "<p>On a side street in Sheffield, between a bakery and a shuttered pub, "
                  "there is a library where nobody reads. Members borrow drills, tile cutters "
                  "and sewing machines instead of novels. For eighteen pounds a year they can "
                  "take out three items at a time.</p>"
                  "<p>„Most people use a drill for about thirteen minutes in its entire life”, "
                  "says Hannah Price, who started the place in 2019 with forty donated tools. "
                  "„The rest of the time it sits in a cupboard. That seemed like a waste of "
                  "money and of metal.”</p>"
                  "<p>The library now holds over nine hundred items and has eleven hundred "
                  "members. It is run by two part-time staff and about thirty volunteers, and "
                  "it breaks even — just. Grants cover the rent; the membership fees pay for "
                  "repairs.</p>"
                  "<p>Not everything works. Expensive power tools come back damaged more often "
                  "than Price expected, and the waiting list for a wallpaper steamer in spring "
                  "can be six weeks long. „We are not a shop”, she says. „If you need it "
                  "tomorrow, we are probably the wrong answer. If you need it once, we are "
                  "exactly the right one.”</p>"),
             ]),
        dict(kop="Understanding the text",
             opdracht="Antwoord in het Nederlands, tenzij er iets anders staat.",
             oefeningen=[
                 ("kort", "Wat lenen de leden hier uit?",
                  "gereedschap: boormachines, tegelsnijders, naaimachines", WL),
                 ("kort", "Hoeveel kost een lidmaatschap per jaar?", "achttien pond", W),
                 ("kort", "Hoeveel voorwerpen mag je tegelijk meenemen?", "drie", W),
                 ("kort", "In welk jaar begon Hannah Price, en met hoeveel stuks?",
                  "in 2019, met veertig geschonken stuks", WL),
                 ("open", "Met welk argument verdedigt Price het idee? Geef het in één zin.",
                  "Een boormachine wordt in haar hele leven maar een kwartier gebruikt en staat "
                  "de rest van de tijd in een kast, dus dat is verspilling van geld en van "
                  "materiaal.", 3),
                 ("open", "Noem de twee problemen die de tekst zelf toegeeft.",
                  "Duur elektrisch gereedschap komt vaker beschadigd terug dan verwacht, en in "
                  "het voorjaar kan je zes weken op een behangafstomer wachten.", 3),
             ]),
        dict(kop="Words from the text",
             opdracht="Zoek het Engelse woord of de uitdrukking in de tekst.",
             oefeningen=[
                 ("rij", [("gesloten, met de luiken dicht", "shuttered"),
                          ("uitlenen", "to lend"), ("ontlenen", "to borrow"),
                          ("quitte spelen", "to break even"),
                          ("een subsidie", "a grant"),
                          ("de wachtlijst", "the waiting list")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat is het verschil tussen <em>lend</em> en <em>borrow</em>?",
                  "lend is uitlenen (jij geeft), borrow is ontlenen (jij krijgt)", WL),
             ]),
        dict(kop="Text B", opdracht="Lees ook deze korte tekst.",
             oefeningen=[
                 ("tekst",
                  "<p><em>I joined in January and I have used the place four times. The staff "
                  "are friendly and the prices are unbeatable. That said, two of the four tools "
                  "I borrowed needed fixing before I could use them, and nobody warned me. Bring "
                  "your own extension lead, too. Still cheaper than buying, and I will renew.</em></p>"),
                 ("kies", "Welk oordeel geeft de schrijver?",
                  ["volledig positief", "gemengd, maar overwegend positief",
                   "gemengd, maar overwegend negatief", "volledig negatief"], 1),
                 ("kort", "Welke twee punten van kritiek geeft hij?",
                  "twee van de vier stukken moesten eerst hersteld worden, zonder waarschuwing, "
                  "en je moet zelf een verlengsnoer meebrengen", WL),
                 ("kort", "Welke woordgroep toont dat hij toch terugkomt?",
                  "I will renew", WW),
             ]),
        dict(kop="Reading between the lines",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Tekst A is journalistiek, tekst B is een recensie. Noem twee "
                          "verschillen die je in de taal zelf kan aanwijzen.",
                  "Tekst A werkt met cijfers, een naam en citaten tussen aanhalingstekens, en "
                  "staat in de derde persoon. Tekst B staat in de ik-vorm, geeft meningen "
                  "(friendly, unbeatable) en spreekt de lezer aan (bring your own).", 4),
                 ("open", "Welke informatie zou je nog willen voor je zelf lid wordt?",
                  "Een eigen antwoord, bijvoorbeeld: hoeveel stuks er echt beschikbaar zijn, "
                  "hoe de herstellingen geregeld worden, wat er gebeurt als je iets breekt, en "
                  "of er iets gelijkaardigs in de eigen stad bestaat.", 3),
             ]),
    ])

# ============================================================
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    reeksen=[
        dict(kop="Which text type?",
             opdracht="Schrijf de tekstsoort: informative, persuasive, prescriptive, "
                      "argumentative, narrative of literary.",
             oefeningen=[
                 ("rij", [("a safety poster telling you to wear a helmet", "persuasive"),
                          ("a recipe for banana bread", "prescriptive"),
                          ("a news report about a flood", "informative"),
                          ("a short story about a lighthouse keeper", "narrative"),
                          ("a letter to the editor against a new motorway", "argumentative"),
                          ("a poem about the sea", "literary")],
                  "Welke tekstsoort?", WW),
                 ("kies", "Een advertentie wil vooral",
                  ["informeren", "overtuigen", "voorschrijven", "ontspannen"], 1),
             ]),
        dict(kop="Fact or opinion?",
             opdracht="Schrijf F of O.",
             oefeningen=[
                 ("rij", [("The bridge was opened in 1964.", "F"),
                          ("The bridge is the ugliest building in town.", "O"),
                          ("Three out of four pupils cycle to school.", "F"),
                          ("Cycling is clearly the best way to get around.", "O"),
                          ("The council spent £2.1 million on the project.", "F")],
                  "F of O?", "58px"),
                 ("kort", "Welke woorden in zin 2 en 4 verraden een mening?",
                  "ugliest en clearly the best", WL),
             ]),
        dict(kop="Register",
             opdracht="Schrijf formal of informal, en geef de andere versie.",
             oefeningen=[
                 ("rij", [("I would be grateful if you could confirm.", "formal: Can you let me know?"),
                          ("Thanks a lot, see you soon!", "informal: Thank you, I look forward to meeting you."),
                          ("We regret to inform you that...", "formal: Sorry, but..."),
                          ("Drop me a line.", "informal: Please contact me.")],
                  "Formal of informal, en de andere versie?", WL),
                 ("kort", "Hoe sluit je een formele mail af als je de naam niet kent?",
                  "Yours faithfully", WW),
                 ("kort", "En als je de naam wél kent?", "Yours sincerely", WW),
             ]),
        dict(kop="Linking words",
             opdracht="Vul het passende verbindingswoord in.",
             oefeningen=[
                 ("rij", [("... the rain, the match went ahead.", "Despite"),
                          ("The bus was late; ..., we missed the train.", "therefore / as a result"),
                          ("She studied hard; ..., she failed.", "however / nevertheless"),
                          ("... you leave now, you will catch it.", "If"),
                          ("He stayed home ... he was ill.", "because")],
                  "Welk woord?", WW),
                 ("open", "Herschrijf met <em>although</em>: <em>It was raining. We went "
                          "anyway.</em>",
                  "Although it was raining, we went anyway.", 2),
             ]),
        dict(kop="Summing up",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Schrijf in één Engelse zin waarover een tekst gaat die je deze week "
                          "gelezen hebt (een artikel, een post, een hoofdstuk).",
                  "Een eigen antwoord van één zin, met een onderwerp en een werkwoord, "
                  "bijvoorbeeld: The article explains why some cities are banning cars from "
                  "the centre.", 2),
                 ("open", "Noem drie dingen waarop je let om te beslissen of een bron "
                          "betrouwbaar is.",
                  "Wie de tekst schreef en met welk belang, of er bronnen of cijfers bij staan, "
                  "hoe oud de tekst is, of andere bronnen hetzelfde zeggen, en of de taal "
                  "neutraal is of overdreven.", 3),
             ]),
    ])


# ============================================================
zet("woordvelden-wonen-eten-en-vrije-tijd",
    titel="Woordvelden: wonen, eten en vrije tijd",
    reeksen=[
        dict(kop="At home",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("de huur", "the rent"), ("de huurder", "the tenant"),
                          ("de huisbaas", "the landlord"), ("het gelijkvloers", "the ground floor"),
                          ("de zolder", "the attic"), ("de kelder", "the cellar / basement")],
                  "Welk Engels woord?", WW),
                 ("rij", [("een rijhuis", "a terraced house"),
                          ("een halfopen bebouwing", "a semi-detached house"),
                          ("een vrijstaand huis", "a detached house"),
                          ("een flat", "a flat (UK) / an apartment (US)")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat is het verschil tussen <em>house</em> en <em>home</em>?",
                  "house is het gebouw, home is waar je thuis bent", WL),
             ]),
        dict(kop="Food",
             opdracht="Vul aan of vertaal.",
             oefeningen=[
                 ("rij", [("een voorgerecht", "a starter"), ("het hoofdgerecht", "the main course"),
                          ("het nagerecht", "the dessert / pudding"),
                          ("om mee te nemen", "takeaway"), ("gekruid, pikant", "spicy")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... the table", "lay / set"), ("to ... the washing-up", "do"),
                          ("to ... a recipe", "follow"), ("to ... a reservation", "make")],
                  "Welk werkwoord hoort erbij?", W),
                 ("kies", "Welk woord hoort er niet bij?",
                  ["kettle", "saucepan", "frying pan", "spanner"], 3),
             ]),
        dict(kop="Free time",
             opdracht="Schrijf het Engelse woord of de uitdrukking.",
             oefeningen=[
                 ("rij", [("een hobby, een bezigheid", "a pastime"),
                          ("een wandeltocht", "a hike"), ("een scheidsrechter", "a referee"),
                          ("een ploeg", "a team"), ("het publiek", "the audience"),
                          ("een voorstelling", "a performance")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... yoga", "do"), ("to ... football", "play"),
                          ("to ... jogging", "go"), ("to ... part in a race", "take")],
                  "Welk werkwoord?", W),
                 ("open", "Schrijf twee Engelse zinnen over wat je in je vrije tijd doet, met "
                          "<em>I usually</em> en <em>I hardly ever</em>.",
                  "Een eigen antwoord met twee volledige zinnen, bijvoorbeeld: I usually play "
                  "volleyball on Wednesdays. I hardly ever watch television during the week.",
                  3),
             ]),
        dict(kop="Phrasal verbs",
             opdracht="Vul het juiste partikel in: up, out, on, off, in.",
             oefeningen=[
                 ("rij", [("Please tidy ... your room.", "up"),
                          ("We ran ... of milk.", "out"),
                          ("I will pick you ... at eight.", "up"),
                          ("Turn ... the lights before you leave.", "off"),
                          ("Try ... these shoes.", "on"),
                          ("She gave ... after two weeks.", "up")],
                  "Welk woordje?", "70px"),
             ]),
    ])

# ============================================================
zet("woordvelden-gezondheid-natuur-en-duurzaamheid",
    titel="Woordvelden: gezondheid, natuur en duurzaamheid",
    reeksen=[
        dict(kop="At the doctor's",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("keelpijn", "a sore throat"), ("koorts", "a temperature / fever"),
                          ("een voorschrift", "a prescription"), ("een pleister", "a plaster"),
                          ("de apotheek", "the chemist's / pharmacy"),
                          ("een huisarts", "a GP")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... a cold", "catch"), ("to ... better", "get"),
                          ("to ... an appointment", "make"), ("to ... painkillers", "take")],
                  "Welk werkwoord?", W),
                 ("kort", "Wat is het verschil tussen <em>ill</em> en <em>sick</em> in Brits "
                          "Engels?", "ill is ziek, sick is misselijk of moeten overgeven", WL),
             ]),
        dict(kop="Wellbeing",
             opdracht="Vertaal of vul aan.",
             oefeningen=[
                 ("rij", [("uitgeput", "exhausted"), ("gespannen", "stressed"),
                          ("ontspannen", "relaxed"), ("overweldigd", "overwhelmed"),
                          ("evenwichtig eten", "a balanced diet")],
                  "Welk Engels woord?", WW),
                 ("open", "Schrijf in twee Engelse zinnen één raad voor iemand die slecht "
                          "slaapt. Gebruik <em>should</em> en <em>try to</em>.",
                  "Een eigen antwoord, bijvoorbeeld: You should go to bed at the same time "
                  "every night. Try to keep your phone out of the bedroom.", 3),
             ]),
        dict(kop="Nature",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een eekhoorn", "a squirrel"), ("een egel", "a hedgehog"),
                          ("een uil", "an owl"), ("een beek", "a stream"),
                          ("een weide", "a meadow"), ("een haag", "a hedge")],
                  "Welk Engels woord?", WW),
                 ("kies", "Welk woord hoort er niet bij?",
                  ["oak", "beech", "willow", "gravel"], 3),
                 ("rij", [("een soort", "a species"), ("uitsterven", "to become extinct"),
                          ("een leefgebied", "a habitat"), ("bedreigd", "endangered")],
                  "Welk Engels woord?", WW),
             ]),
        dict(kop="Sustainability",
             opdracht="Vertaal en gebruik.",
             oefeningen=[
                 ("rij", [("afval", "waste"), ("hergebruiken", "to reuse"),
                          ("recycleren", "to recycle"), ("de uitstoot", "emissions"),
                          ("hernieuwbare energie", "renewable energy"),
                          ("de koolstofvoetafdruk", "the carbon footprint")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat betekent <em>single-use plastic</em>?",
                  "plastic voor eenmalig gebruik, wegwerpplastic", WL),
                 ("open", "Schrijf drie Engelse zinnen over wat jouw school zou kunnen doen om "
                          "minder afval te maken.",
                  "Een eigen antwoord met drie volledige zinnen, bijvoorbeeld: The school could "
                  "put a water fountain in every corridor. Pupils should bring a reusable "
                  "bottle. We could sort paper and plastic in every classroom.", 4),
             ]),
    ])

# ============================================================
zet("woordvelden-school-werk-geld-en-verkeer",
    titel="Woordvelden: school, werk, geld en verkeer",
    reeksen=[
        dict(kop="School",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een vak", "a subject"), ("een uurrooster", "a timetable"),
                          ("een rapport", "a report"), ("huiswerk", "homework"),
                          ("de pauze", "the break"), ("slagen voor een examen", "to pass an exam")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat betekent <em>to sit an exam</em>?",
                  "een examen afleggen, niet slagen", WL),
                 ("kort", "En <em>to fail</em>?", "niet slagen, zakken", W),
                 ("waar", "<em>Homework</em> is onteltbaar: je zegt nooit <em>homeworks</em>.",
                  True),
             ]),
        dict(kop="Work",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("solliciteren", "to apply for a job"),
                          ("een sollicitatiegesprek", "a job interview"),
                          ("een vacature", "a vacancy / a job opening"),
                          ("een loon", "a salary / wages"),
                          ("ontslagen worden", "to be made redundant / to be fired"),
                          ("deeltijds", "part-time")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat is een <em>CV</em> voluit?", "a curriculum vitae", WW),
                 ("open", "Schrijf de eerste twee zinnen van een Engelse sollicitatiemail voor "
                          "een vakantiejob in een boekenwinkel.",
                  "Een eigen antwoord, bijvoorbeeld: Dear Sir or Madam, I am writing to apply "
                  "for the summer job advertised on your website. I am seventeen years old and "
                  "I am in my fifth year at secondary school.", 3),
             ]),
        dict(kop="Money",
             opdracht="Vertaal of vul aan.",
             oefeningen=[
                 ("rij", [("een korting", "a discount"), ("een lening", "a loan"),
                          ("sparen", "to save up"), ("een kassabon", "a receipt"),
                          ("terugbetalen", "to refund"), ("het wisselgeld", "the change")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... money", "spend"), ("to ... a bill", "pay"),
                          ("to ... in cash", "pay"), ("to ... a bargain", "get")],
                  "Welk werkwoord?", W),
                 ("kies", "Welk woord hoort er niet bij?",
                  ["savings", "interest", "budget", "pavement"], 3),
             ]),
        dict(kop="On the road",
             opdracht="Schrijf het Engelse woord, en let op het verschil met het Amerikaans.",
             oefeningen=[
                 ("rij", [("het voetpad", "the pavement (UK) / sidewalk (US)"),
                          ("de snelweg", "the motorway (UK) / highway (US)"),
                          ("de file", "the traffic jam"),
                          ("een vrachtwagen", "a lorry (UK) / truck (US)"),
                          ("de benzine", "petrol (UK) / gas (US)"),
                          ("een rotonde", "a roundabout")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat is een <em>zebra crossing</em>?", "een zebrapad", WW),
                 ("kort", "Wat betekent <em>rush hour</em>?", "het spitsuur", WW),
             ]),
    ])

# ============================================================
zet("woordvelden-kunst-literatuur-politiek-en-reizen",
    titel="Woordvelden: kunst, literatuur, politiek en reizen",
    reeksen=[
        dict(kop="Art and literature",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een schilderij", "a painting"), ("een tentoonstelling", "an exhibition"),
                          ("een beeldhouwwerk", "a sculpture"), ("een meesterwerk", "a masterpiece"),
                          ("een roman", "a novel"), ("een hoofdstuk", "a chapter")],
                  "Welk Engels woord?", WW),
                 ("rij", [("de verhaallijn", "the plot"), ("een personage", "a character"),
                          ("de verteller", "the narrator"), ("de omgeving, de tijd en plaats",
                                                             "the setting")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat is het verschil tussen <em>fiction</em> en <em>non-fiction</em>?",
                  "fiction is verzonnen, non-fiction gaat over de werkelijkheid", WL),
             ]),
        dict(kop="Politics and society",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("een verkiezing", "an election"), ("stemmen", "to vote"),
                          ("een wet", "a law / an act"), ("de regering", "the government"),
                          ("een burger", "a citizen"), ("betogen", "to protest / demonstrate")],
                  "Welk Engels woord?", WW),
                 ("kort", "Hoe heet het parlement van het Verenigd Koninkrijk?",
                  "the Houses of Parliament (Commons en Lords)", WL),
                 ("open", "Schrijf in twee Engelse zinnen je mening over de stemgerechtigde "
                          "leeftijd van zestien jaar. Gebruik <em>In my opinion</em> en "
                          "<em>because</em>.",
                  "Een eigen antwoord met twee volledige zinnen en een reden, bijvoorbeeld: In "
                  "my opinion, sixteen-year-olds should be allowed to vote. Decisions about "
                  "climate and education affect them for longer than anyone else.", 3),
             ]),
        dict(kop="Travel",
             opdracht="Vertaal of vul aan.",
             oefeningen=[
                 ("rij", [("een heen-en-terugticket", "a return ticket"),
                          ("de bagage", "the luggage"), ("instappen", "to board"),
                          ("vertraging", "a delay"), ("een verblijf", "a stay"),
                          ("een rondleiding", "a guided tour")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... a flight", "book"), ("to ... in at a hotel", "check"),
                          ("to ... off a plane", "get"), ("to ... the train", "catch")],
                  "Welk werkwoord?", W),
                 ("waar", "<em>Luggage</em> is onteltbaar, dus <em>two luggages</em> bestaat "
                          "niet.", True),
             ]),
    ])

# ============================================================
zet("woordvelden-wetenschap-techniek-en-taal",
    titel="Woordvelden: wetenschap, techniek en taal",
    reeksen=[
        dict(kop="Science and technology",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een onderzoek", "research"), ("een proef", "an experiment"),
                          ("een uitvinding", "an invention"), ("een toestel", "a device"),
                          ("een scherm", "a screen"), ("een toetsenbord", "a keyboard")],
                  "Welk Engels woord?", WW),
                 ("rij", [("opslaan", "to save"), ("downloaden", "to download"),
                          ("een wachtwoord", "a password"),
                          ("een rekenblad", "a spreadsheet"),
                          ("een bestand", "a file")],
                  "Welk Engels woord?", WW),
                 ("waar", "<em>Research</em> is onteltbaar: je zegt <em>a piece of research</em> "
                          "en niet <em>a research</em>.", True),
             ]),
        dict(kop="False friends",
             opdracht="Schrijf wat het Engelse woord écht betekent.",
             oefeningen=[
                 ("rij", [("actually", "eigenlijk, in werkelijkheid (niet: actueel)"),
                          ("eventually", "uiteindelijk (niet: eventueel)"),
                          ("sympathetic", "meelevend (niet: sympathiek)"),
                          ("to control", "besturen, beheersen (niet: controleren)"),
                          ("a magazine", "een tijdschrift (niet: een magazijn)")],
                  "Wat betekent het?", WL),
                 ("kort", "Hoe zeg je <em>eventueel</em> dan wel in het Engels?",
                  "possibly, if necessary", WW),
                 ("kort", "En <em>controleren</em>?", "to check", W),
             ]),
        dict(kop="Word building",
             opdracht="Maak het gevraagde woord.",
             oefeningen=[
                 ("rij", [("possible → het tegengestelde", "impossible"),
                          ("use → een bijvoeglijk naamwoord", "useful / useless"),
                          ("to decide → een naamwoord", "a decision"),
                          ("to invent → iemand die het doet", "an inventor"),
                          ("care → zonder zorg", "careless"),
                          ("to govern → een naamwoord", "government")],
                  "Welk woord?", WW),
                 ("kort", "Welk voorvoegsel maakt <em>legal</em> tegengesteld?",
                  "il- (illegal)", W),
                 ("kort", "En <em>regular</em>?", "ir- (irregular)", W),
             ]),
        dict(kop="British or American?",
             opdracht="Schrijf het andere woord.",
             oefeningen=[
                 ("rij", [("lift (UK)", "elevator (US)"), ("autumn (UK)", "fall (US)"),
                          ("rubbish (UK)", "garbage / trash (US)"),
                          ("chips (UK)", "fries (US)"), ("holiday (UK)", "vacation (US)"),
                          ("mobile (UK)", "cell phone (US)")],
                  "Welk Amerikaans woord?", WW),
                 ("rij", [("colour", "color (US)"), ("centre", "center (US)"),
                          ("organise", "organize (US)"), ("travelling", "traveling (US)")],
                  "Hoe schrijft men het in de VS?", WW),
             ]),
    ])


# ============================================================
zet("naamwoorden-lidwoorden-en-hoeveelheden",
    titel="Naamwoorden, lidwoorden en hoeveelheden",
    reeksen=[
        dict(kop="Plurals",
             opdracht="Schrijf het meervoud.",
             oefeningen=[
                 ("rij", [("child", "children"), ("knife", "knives"), ("box", "boxes"),
                          ("city", "cities"), ("tooth", "teeth"), ("sheep", "sheep")],
                  "Welk meervoud?", W),
                 ("rij", [("analysis", "analyses"), ("woman", "women"),
                          ("potato", "potatoes"), ("roof", "roofs")],
                  "Welk meervoud?", W),
             ]),
        dict(kop="Countable or uncountable?",
             opdracht="Schrijf C of U, en bij U hoe je er toch één van telt.",
             oefeningen=[
                 ("rij", [("advice", "U: a piece of advice"), ("suitcase", "C"),
                          ("information", "U: a piece of information"), ("journey", "C"),
                          ("furniture", "U: a piece of furniture"), ("news", "U: an item of news")],
                  "C of U?", WW),
                 ("kort", "Is <em>news</em> enkelvoud of meervoud bij het werkwoord?",
                  "enkelvoud: the news is good", WL),
             ]),
        dict(kop="A, an, the or nothing?",
             opdracht="Vul in. Schrijf een streepje als er geen lidwoord hoort.",
             oefeningen=[
                 ("rij", [("She plays ... piano.", "the"), ("He is ... engineer.", "an"),
                          ("... life is short.", "–"), ("I go to ... school by bike.", "–"),
                          ("We visited ... Netherlands.", "the"),
                          ("She had ... hour to spare.", "an")],
                  "Welk lidwoord?", "70px"),
                 ("kort", "Waarom is het <em>an hour</em> maar <em>a university</em>?",
                  "het gaat om de klank: de h is stom, de u klinkt als j", WL),
             ]),
        dict(kop="How much, how many",
             opdracht="Vul in: much, many, a lot of, a few, a little, few of little.",
             oefeningen=[
                 ("rij", [("How ... time do we have?", "much"),
                          ("There were too ... people.", "many"),
                          ("I need ... help, just a bit.", "a little"),
                          ("She has ... friends here, almost none.", "few"),
                          ("We have ... work to do.", "a lot of")],
                  "Welk woord?", WW),
                 ("kort", "Wat is het verschil tussen <em>a few</em> en <em>few</em>?",
                  "a few is enkele (positief), few is weinig, bijna geen", WL),
             ]),
        dict(kop="The genitive",
             opdracht="Herschrijf met 's of met of.",
             oefeningen=[
                 ("rij", [("the bike of my sister", "my sister's bike"),
                          ("the toys of the children", "the children's toys"),
                          ("the roof of the house", "the roof of the house (blijft)"),
                          ("the office of the managers", "the managers' office")],
                  "Hoe schrijf je het?", WL),
             ]),
    ])

# ============================================================
zet("voornaamwoorden-en-betrekkelijke-bijzinnen",
    titel="Voornaamwoorden en betrekkelijke bijzinnen",
    reeksen=[
        dict(kop="Which pronoun?",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("This book is ... (van mij).", "mine"),
                          ("She did it ... (zelf).", "herself"),
                          ("They know each ... .", "other"),
                          ("... is raining.", "It"),
                          ("... were twenty people there.", "There")],
                  "Welk woord?", WW),
                 ("kort", "Wat is het verschil tussen <em>its</em> en <em>it's</em>?",
                  "its is bezittelijk, it's is it is of it has", WL),
             ]),
        dict(kop="Relative clauses",
             opdracht="Vul in: who, which, that, whose of where.",
             oefeningen=[
                 ("rij", [("The man ... lives next door is a vet.", "who / that"),
                          ("The book ... I borrowed was yours.", "which / that"),
                          ("The woman ... car was stolen called the police.", "whose"),
                          ("This is the town ... I grew up.", "where"),
                          ("My brother, ... is a nurse, works nights.", "who")],
                  "Welk woord?", WW),
                 ("open", "Leg uit waarom er in de laatste zin komma's staan en in de eerste "
                          "niet.",
                  "De laatste bijzin is niet-bepalend: hij geeft extra informatie over één "
                  "bekende broer en kan weg. De eerste is bepalend: hij zegt over welke man het "
                  "gaat, dus hij mag niet weg en krijgt geen komma's.", 4),
                 ("waar", "In een niet-bepalende bijzin mag je <em>that</em> gebruiken.",
                  False),
             ]),
        dict(kop="Combine the sentences",
             opdracht="Maak er één zin van met een betrekkelijke bijzin.",
             oefeningen=[
                 ("open", "I met a girl. She speaks four languages.",
                  "I met a girl who speaks four languages.", 2),
                 ("open", "That is the house. We lived there for ten years.",
                  "That is the house where we lived for ten years.", 2),
                 ("open", "He showed me a photo. Its colours had faded.",
                  "He showed me a photo whose colours had faded.", 2),
             ]),
        dict(kop="Some, any, no",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("Is there ... milk left?", "any"),
                          ("I have ... questions for you.", "some"),
                          ("There is ... time to lose.", "no"),
                          ("Would you like ... coffee?", "some"),
                          ("She did not say ... .", "anything")],
                  "Welk woord?", WW),
             ]),
    ])

# ============================================================
zet("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    titel="Bijvoeglijke naamwoorden, bijwoorden en voorzetsels",
    reeksen=[
        dict(kop="Comparatives",
             opdracht="Vul de trappen aan.",
             oefeningen=[
                 ("rij", [("big", "bigger – the biggest"), ("good", "better – the best"),
                          ("careful", "more careful – the most careful"),
                          ("bad", "worse – the worst"), ("easy", "easier – the easiest"),
                          ("far", "further/farther – the furthest/farthest")],
                  "Welke trappen?", WL),
                 ("rij", [("She is ... tall as her brother.", "as"),
                          ("This is the ... film I have seen.", "best"),
                          ("It is much ... than yesterday.", "colder")],
                  "Vul aan.", WW),
             ]),
        dict(kop="Adjective or adverb?",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("rij", [("She sings ... (beautiful).", "beautifully"),
                          ("He drives too ... (fast).", "fast"),
                          ("The soup tastes ... (good).", "good"),
                          ("They worked ... (hard).", "hard"),
                          ("I ... (hard) know him.", "hardly")],
                  "Welke vorm?", WW),
                 ("kort", "Wat is het verschil tussen <em>hard</em> en <em>hardly</em>?",
                  "hard is hard of hevig, hardly is nauwelijks", WL),
                 ("open", "Waarom staat er na <em>taste</em>, <em>look</em> en <em>feel</em> een "
                          "bijvoeglijk naamwoord en geen bijwoord?",
                  "Dat zijn koppelwerkwoorden: ze zeggen iets over het onderwerp zelf, niet "
                  "over de handeling. Daarom is het <em>it looks good</em> en niet <em>it "
                  "looks well</em>.", 4),
             ]),
        dict(kop="Prepositions",
             opdracht="Vul in: in, on, at, for, since, by, during.",
             oefeningen=[
                 ("rij", [("... Monday", "on"), ("... 2019", "in"), ("... six o'clock", "at"),
                          ("... three years", "for"), ("... 2015", "since"),
                          ("... the summer", "during / in")],
                  "Welk voorzetsel?", "70px"),
                 ("rij", [("good ... maths", "at"), ("interested ... history", "in"),
                          ("afraid ... spiders", "of"), ("depend ... the weather", "on"),
                          ("married ... a teacher", "to")],
                  "Welk voorzetsel?", "70px"),
                 ("kort", "Wat is het verschil tussen <em>for</em> en <em>since</em>?",
                  "for noemt de duur, since het startpunt", WL),
             ]),
        dict(kop="Word order",
             opdracht="Zet de bijvoeglijke naamwoorden in de juiste orde.",
             oefeningen=[
                 ("rij", [("(leather / black / old) jacket", "an old black leather jacket"),
                          ("(Italian / small / two) cars", "two small Italian cars"),
                          ("(round / wooden / beautiful) table", "a beautiful round wooden table")],
                  "Welke orde?", WL),
             ]),
    ])

# ============================================================
zet("de-tegenwoordige-tijden-en-de-present-perfect",
    titel="De tegenwoordige tijden en de present perfect",
    reeksen=[
        dict(kop="Simple or continuous?",
             opdracht="Vul de juiste tegenwoordige tijd in.",
             oefeningen=[
                 ("rij", [("She ... (work) in Ghent every day.", "works"),
                          ("Look, it ... (rain)!", "is raining"),
                          ("Water ... (boil) at 100 °C.", "boils"),
                          ("I ... (not understand) this.", "do not understand"),
                          ("They ... (stay) with us this week.", "are staying")],
                  "Welke vorm?", WW),
                 ("kort", "Noem twee werkwoorden die je bijna nooit in de continuous zet.",
                  "know, believe, like, want, need, understand, belong", WL),
             ]),
        dict(kop="Present perfect",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("I ... (live) here for ten years.", "have lived"),
                          ("She ... (just / finish) her essay.", "has just finished"),
                          ("... you ever ... (be) to Wales?", "Have / been"),
                          ("He ... (not see) her since 2020.", "has not seen")],
                  "Welke vorm?", WW),
                 ("open", "Leg het verschil uit tussen <em>I lost my keys</em> en <em>I have "
                          "lost my keys</em>.",
                  "De eerste zin vertelt een afgesloten feit uit het verleden. De tweede zegt "
                  "dat het nu nog telt: de sleutels zijn nog altijd kwijt.", 3),
                 ("rij", [("yesterday", "past simple"), ("since Monday", "present perfect"),
                          ("in 2010", "past simple"), ("already", "present perfect"),
                          ("last week", "past simple"), ("so far", "present perfect")],
                  "Welke tijd hoort erbij?", WW),
             ]),
        dict(kop="Present perfect continuous",
             opdracht="Vul in en zeg waarom.",
             oefeningen=[
                 ("rij", [("I ... (wait) for an hour.", "have been waiting"),
                          ("She ... (write) three emails.", "has written"),
                          ("They ... (paint) all morning.", "have been painting")],
                  "Welke vorm?", WW),
                 ("kort", "Waarop ligt de nadruk bij de continuous?",
                  "op de duur van de bezigheid, niet op het resultaat", WL),
             ]),
    ])

# ============================================================
zet("de-verleden-tijden",
    titel="De verleden tijden",
    reeksen=[
        dict(kop="Irregular verbs",
             opdracht="Vul de drie vormen aan.",
             oefeningen=[
                 ("rij", [("buy", "bought – bought"), ("catch", "caught – caught"),
                          ("choose", "chose – chosen"), ("fall", "fell – fallen"),
                          ("write", "wrote – written"), ("bring", "brought – brought")],
                  "Verleden tijd en deelwoord?", WL),
                 ("rij", [("lie (liggen)", "lay – lain"), ("lay (leggen)", "laid – laid"),
                          ("rise", "rose – risen"), ("raise", "raised – raised")],
                  "Verleden tijd en deelwoord?", WL),
             ]),
        dict(kop="Past simple or past continuous?",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("While I ... (cook), the phone rang.", "was cooking"),
                          ("She ... (leave) at six.", "left"),
                          ("They ... (watch) TV when the lights went out.", "were watching"),
                          ("What ... you ... (do) at nine last night?", "were / doing")],
                  "Welke vorm?", WW),
                 ("open", "Welke tijd kies je voor het decor van een verhaal, en welke voor de "
                          "gebeurtenis?",
                  "De past continuous voor wat al bezig was, het decor, en de past simple voor "
                  "wat er toen gebeurde en het verhaal vooruit duwt.", 3),
             ]),
        dict(kop="Past perfect",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("When we arrived, the film ... (already / start).",
                           "had already started"),
                          ("He told me he ... (never / fly) before.", "had never flown"),
                          ("She ... (finish) before the others arrived.", "had finished")],
                  "Welke vorm?", WW),
                 ("kort", "Waarvoor dient de past perfect?",
                  "voor wat nog vroeger gebeurde dan de rest van het verhaal", WL),
             ]),
        dict(kop="Used to and would",
             opdracht="Herschrijf of vul in.",
             oefeningen=[
                 ("open", "Herschrijf met <em>used to</em>: <em>When I was ten, I played the "
                          "violin every day.</em>",
                  "When I was ten, I used to play the violin every day.", 2),
                 ("kort", "Mag je <em>would</em> ook gebruiken voor een toestand, zoals "
                          "<em>I would live in Ghent</em>?",
                  "nee, would alleen voor herhaalde handelingen, niet voor toestanden", WL),
             ]),
    ])

# ============================================================
zet("de-toekomst-de-modale-hulpwerkwoorden-en-de-gerund",
    titel="De toekomst, de modale hulpwerkwoorden en de gerund",
    reeksen=[
        dict(kop="Which future?",
             opdracht="Vul in: will, going to of present continuous.",
             oefeningen=[
                 ("rij", [("Look at those clouds, it ... rain.", "is going to"),
                          ("I ... have the soup, please.", "will"),
                          ("We ... meet Sara at eight tonight.", "are meeting"),
                          ("I promise I ... help you.", "will"),
                          ("She ... study medicine next year, she has decided.", "is going to")],
                  "Welke vorm?", WW),
                 ("open", "Leg het verschil uit tussen <em>will</em> en <em>going to</em> in "
                          "één zin.",
                  "<em>Going to</em> gebruik je voor een plan dat al vastligt of voor iets dat "
                  "je nu al ziet aankomen, <em>will</em> voor een beslissing op het moment zelf "
                  "of voor een voorspelling.", 3),
             ]),
        dict(kop="Modal verbs",
             opdracht="Vul het passende modale werkwoord in.",
             oefeningen=[
                 ("rij", [("You ... wear a helmet, it is the law.", "must / have to"),
                          ("You ... not be tired, you slept all day.", "cannot"),
                          ("She ... be at home, her car is there.", "must"),
                          ("... I open the window?", "May / Can"),
                          ("You ... have told me earlier.", "should")],
                  "Welk werkwoord?", WW),
                 ("kort", "Wat is het verschil tussen <em>must not</em> en <em>do not have "
                          "to</em>?",
                  "must not is verboden, do not have to is niet verplicht", WL),
             ]),
        dict(kop="Gerund or infinitive?",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("rij", [("I enjoy ... (read).", "reading"), ("She decided ... (leave).", "to leave"),
                          ("He avoided ... (answer).", "answering"),
                          ("They hope ... (win).", "to win"),
                          ("Would you mind ... (wait)?", "waiting"),
                          ("I look forward to ... (hear) from you.", "hearing")],
                  "Welke vorm?", WW),
                 ("kort", "Waarom is het <em>look forward to hearing</em> en niet <em>to "
                          "hear</em>?",
                  "to is hier een voorzetsel, dus volgt de -ing-vorm", WL),
                 ("open", "Geef het verschil tussen <em>I stopped smoking</em> en <em>I stopped "
                          "to smoke</em>.",
                  "<em>Stopped smoking</em> betekent dat je ermee opgehouden bent. "
                  "<em>Stopped to smoke</em> betekent dat je stopte met wat je deed om te "
                  "roken.", 3),
             ]),
    ])

# ============================================================
zet("zinsbouw-indirecte-rede-en-de-passieve-vorm",
    titel="Zinsbouw, indirecte rede en de passieve vorm",
    reeksen=[
        dict(kop="Questions and negatives",
             opdracht="Maak er een vraag en een ontkenning van.",
             oefeningen=[
                 ("rij", [("She works here.", "Does she work here? / She does not work here."),
                          ("They have finished.", "Have they finished? / They have not finished."),
                          ("He can swim.", "Can he swim? / He cannot swim."),
                          ("You saw her.", "Did you see her? / You did not see her.")],
                  "Vraag en ontkenning?", WL),
                 ("kort", "Wat is een <em>question tag</em> bij <em>She is coming, ...?</em>",
                  "isn't she?", W),
             ]),
        dict(kop="Reported speech",
             opdracht="Zet over naar de indirecte rede.",
             oefeningen=[
                 ("open", "„I am tired”, she said.",
                  "She said (that) she was tired.", 2),
                 ("open", "„We will call you tomorrow”, they said.",
                  "They said (that) they would call me the next day.", 2),
                 ("open", "„Where do you live?”, he asked.",
                  "He asked where I lived.", 2),
                 ("open", "„Don't touch that”, she told him.",
                  "She told him not to touch that.", 2),
                 ("kort", "Wat gebeurt er met <em>tomorrow</em> en <em>here</em> in de indirecte "
                          "rede?", "ze worden the next day en there", WL),
             ]),
        dict(kop="The passive",
             opdracht="Zet in de passieve vorm.",
             oefeningen=[
                 ("open", "They built the bridge in 1964.",
                  "The bridge was built in 1964.", 2),
                 ("open", "Someone has stolen my bike.",
                  "My bike has been stolen.", 2),
                 ("open", "They are repairing the road.",
                  "The road is being repaired.", 2),
                 ("open", "Wanneer kies je de passieve vorm? Geef twee redenen.",
                  "Als de dader onbekend of onbelangrijk is, of als je de aandacht juist op het "
                  "onderwerp wil leggen. Ook in verslagen en wetenschappelijke teksten, waar de "
                  "handeling telt en niet wie ze deed.", 3),
             ]),
        dict(kop="Conditionals",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("If it rains, we ... (stay) inside.", "will stay"),
                          ("If I ... (have) more time, I would read more.", "had"),
                          ("If she had studied, she ... (pass).", "would have passed"),
                          ("If you heat ice, it ... (melt).", "melts")],
                  "Welke vorm?", WW),
                 ("kort", "Welke conditional gebruik je voor iets dat niet meer te veranderen "
                          "is?", "de derde (third conditional)", WL),
             ]),
    ])

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-engelse-tekst-analyseren-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de tekst eerst één keer helemaal door zonder iets op te zoeken, en "
                   "onderstreep dan de cijfers, de namen en de citaten. Dat zijn de plaatsen waar "
                   "de vragen bijna altijd over gaan.",
            waarom=[],
        ),
        dict(
            aanpak="Zoek bij elke vraag de plaats in de tekst terug en antwoord met wat daar staat, "
                   "niet met wat je er zelf van denkt. Bij de vragen over cijfers staat het antwoord "
                   "letterlijk in de tekst.",
            waarom=[
                None,
                None,
                None,
                "Twee cijfers in één vraag: lees dus verder dan het jaartal. Let erop dat de "
                "veertig stuks geschonken waren en niet aangekocht, want dat hoort bij het "
                "antwoord.",
                "Haal het citaat van Price erbij en zeg wat ze ermee bedoelt. Een goede samenvatting "
                "noemt het cijfer uit het citaat en het besluit dat eruit volgt.",
                "Noem de twee die de tekst zelf toegeeft, niet die je zelf bedenkt. Dat een "
                "journalistiek stuk ook de keerzijde geeft, is precies wat het van een advertentie "
                "onderscheidt.",
            ],
        ),
        dict(
            aanpak="Zoek het Engelse woord in de tekst zelf terug in plaats van het uit je hoofd te "
                   "vertalen. Zo leer je het woord in zijn context, en dat blijft beter hangen.",
            waarom=[
                "Let op to break even: quitte spelen, dus niet winst maken en niet verlies maken. "
                "Een grant is een subsidie die je niet moet terugbetalen, in tegenstelling tot a "
                "loan.",
                "Noem wie wat doet, want dat is het hele verschil. In het Nederlands verwisselen we "
                "lenen ook, maar in het Engels is lend altijd geven en borrow altijd krijgen: I "
                "lend you my drill, you borrow my drill.",
            ],
        ),
        dict(
            aanpak="Een recensie heeft bijna altijd lof en kritiek door elkaar. Zoek dus eerst de "
                   "lovende woorden, dan de kritiek, en kijk waar het zwaarst op weegt. Woorden als "
                   "that said en still markeren de bocht.",
            waarom=[
                "Gemengd maar overwegend positief, en dat zie je aan het slot: still cheaper en I "
                "will renew. Een schrijver die terugkomt, is niet negatief, hoeveel kritiek hij "
                "ook geeft.",
                "Let op dat de tweede kritiek een tip is in de vorm van een opdracht: bring your "
                "own extension lead betekent dat er geen voorzien is.",
                "I will renew is het bewijs. Zo'n toekomstvorm aan het einde van een recensie is de "
                "duidelijkste graadmeter van het eindoordeel.",
            ],
        ),
        dict(
            aanpak="Hier moet je niet meer zoeken maar vergelijken. Kijk naar de persoon (hij of "
                   "ik), naar de soort woorden (cijfers of meningen) en naar wie er aangesproken "
                   "wordt.",
            waarom=[
                "Noem telkens een verschil dat je in de taal kan aanwijzen, niet in de inhoud. Dat "
                "is net wat de vraag wil: twee verschillen die je met je vinger kan aanduiden.",
                "Hier is elk goed onderbouwd antwoord juist. Zet er wel bij waarom je dat zou "
                "willen weten, want dan wordt het een argument en geen opsomming.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-en-de-bedoeling-van-een-tekst-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je telkens af wat de tekst van jou wil: iets weten, iets doen, iets "
                   "vinden, of gewoon meegaan in een verhaal. Dat doel bepaalt de tekstsoort, niet "
                   "het onderwerp.",
            waarom=[
                "Let op het verschil tussen persuasive en prescriptive: een affiche wil je "
                "overtuigen een helm te dragen, een recept zegt stap voor stap wat je moet doen. En "
                "tussen informative en argumentative: een nieuwsbericht brengt feiten, een "
                "lezersbrief verdedigt een standpunt.",
                "Een advertentie wil overtuigen, ook al geeft ze er informatie bij. Die informatie "
                "is het middel en niet het doel, en dat is de vraag die je altijd moet stellen.",
            ],
        ),
        dict(
            aanpak="Een feit kan je nakijken, een mening niet. Zoek dus naar woorden die een "
                   "waardering uitdrukken: een overtreffende trap, clearly, obviously, best, worst.",
            waarom=[
                "De eerste, derde en vijfde noemen een jaartal, een verhouding en een bedrag: alle "
                "drie na te kijken. Let op: een feit hoeft niet juist te zijn om een feit te zijn, "
                "het moet enkel te controleren zijn.",
                "Ugliest is een overtreffende trap van een smaakoordeel, en clearly the best doet "
                "alsof een mening een vaststelling is. Juist dat soort woorden zoek je.",
            ],
        ),
        dict(
            aanpak="Register is de toon: formeel voor wie je niet kent of in een officiële brief, "
                   "informeel onder vrienden. Let op de lengte van de wending: formeel is bijna "
                   "altijd langer en met meer hulpwerkwoorden.",
            waarom=[
                "Schrijf telkens de andere versie erbij, want dat is waar de oefening op mikt. I "
                "would be grateful if you could is een beleefdheidsformule; letterlijk vertalen "
                "klinkt in het Nederlands overdreven.",
                "Yours faithfully na Dear Sir or Madam, dus wanneer je de naam niet kent. Een "
                "steuntje: faithfully hoort bij een onbekende, zoals trouw zonder gezicht.",
                "Yours sincerely na Dear Mr Brown. Let op: Amerikanen schrijven liever Sincerely of "
                "Best regards, en in een mail is Kind regards bijna altijd veilig.",
            ],
        ),
        dict(
            aanpak="Een verbindingswoord moet passen bij de verhouding tussen de twee delen: "
                   "tegenstelling, gevolg, voorwaarde of reden. Lees de zin dus eerst zonder het "
                   "woord en bepaal welke van de vier het is.",
            waarom=[
                "Let op het verschil tussen despite en although: na despite komt een naamwoord "
                "(despite the rain), na although een hele zin (although it was raining). Dat is de "
                "fout die het vaakst gemaakt wordt.",
                "Although komt vooraan en krijgt een komma na de eerste zinshelft. Dit is dezelfde "
                "regel als hierboven: although plus zin, despite plus naamwoord.",
            ],
        ),
        dict(
            aanpak="Twee opdrachten waar je eigen antwoord juist is, zolang het de vorm heeft die "
                   "gevraagd wordt: één volledige Engelse zin, en drie dingen met een reden erbij.",
            waarom=[
                "Houd het bij één zin met een onderwerp en een werkwoord. Begin eventueel met The "
                "article explains, The post argues of The chapter describes, want dat dwingt je "
                "meteen om het doel van de tekst te noemen.",
                "Noem drie zaken en liefst één over de schrijver zelf, want wie iets schrijft en "
                "met welk belang is de vraag die het meest oplevert. Dit sluit aan bij het verschil "
                "tussen feit en mening uit reeks 2.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-wonen-eten-en-vrije-tijd-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de woorden per paar dat bij elkaar hoort: huurder en huisbaas, zolder en "
                   "kelder. Dat gaat sneller dan een lijst van losse woorden, en bij een toets komt "
                   "het paar vaak samen aan bod.",
            waarom=[
                "Let op tenant en landlord: de huurder betaalt, de huisbaas bezit. En op ground "
                "floor: het gelijkvloers is in het Brits Engels niet de first floor, want dat is "
                "bij ons de eerste verdieping.",
                "Let op de bouwwoorden: terraced is een rijhuis, semi-detached een halfopen "
                "bebouwing en detached een vrijstaand huis. Flat is Brits, apartment Amerikaans.",
                "Noem beide: house is het gebouw, home is het gevoel erbij. Daarom zegt men a house "
                "for sale maar I am going home, en nooit I am going house.",
            ],
        ),
        dict(
            aanpak="Bij eten en drinken is de kunst niet het woord maar het werkwoord dat erbij "
                   "hoort. Zulke vaste combinaties leer je als één geheel, want ze zijn niet uit "
                   "het Nederlands te voorspellen.",
            waarom=[
                "Let op pudding: in Brits Engels is dat het nagerecht in het algemeen, niet enkel "
                "pudding zoals bij ons. Takeaway is Brits, takeout is Amerikaans.",
                "Dit zijn vaste combinaties: lay the table, do the washing-up, follow a recipe, "
                "make a reservation. Make the washing-up bestaat niet, al klinkt het logisch.",
                "Spanner is een moersleutel, dus geen keukengerei; de drie andere zijn een "
                "waterkoker, een kookpot en een pan. Zo'n vraag test of je het woordveld kent en "
                "niet enkel de losse woorden.",
            ],
        ),
        dict(
            aanpak="Ook hier gaat het vooral om het juiste werkwoord. De regel die het meest "
                   "oplevert: play bij een spel met een bal of een tegenstander, go bij een "
                   "beweging die op -ing eindigt, do bij de rest.",
            waarom=[
                "Let op audience en performance: audience is het publiek als groep, dus enkelvoud "
                "met een meervoudsgevoel. En a pastime is een bezigheid; het Nederlandse hobby "
                "bestaat ook in het Engels, maar pastime klinkt natuurlijker in een tekst.",
                "Do yoga, play football, go jogging, take part in a race. Het steuntje: go plus "
                "-ing, play plus bal of spel, do plus de rest.",
                "Houd het bij twee volle zinnen met de gevraagde wendingen. Let op de plaats van "
                "usually en hardly ever: die komen vóór het werkwoord, maar ná een vorm van to be.",
            ],
        ),
        dict(
            aanpak="Een phrasal verb betekent samen iets anders dan de twee woorden apart, dus leer "
                   "ze als geheel. Up betekent vaak afwerken of verzamelen, out leeg of weg, off "
                   "uit of weg.",
            waarom=[
                "Let op give up: opgeven, niet weggeven. En run out of: op zijn. Pick you up is "
                "ophalen, en dat up kan ook achteraan: I will pick up the children of I will pick "
                "the children up, maar bij een voornaamwoord móet het erachter: pick you up.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-gezondheid-natuur-en-duurzaamheid-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Bij de dokter is het woordveld klein maar vol valstrikken, vooral tussen Brits "
                   "en Amerikaans Engels. Leer bij elke klacht ook het werkwoord dat erbij hoort.",
            waarom=[
                "Let op GP: dat staat voor general practitioner, de huisarts. En chemist's is in "
                "Brits Engels de apotheek, terwijl een Amerikaan pharmacy of drugstore zegt.",
                "Vaste combinaties: catch a cold, get better, make an appointment, take painkillers. "
                "Take a cold bestaat niet, en in het Nederlands zeggen we net wel pillen nemen, dus "
                "die ene klopt wel.",
                "Noem beide betekenissen. In Amerikaans Engels betekent sick gewoon ziek, en dat is "
                "precies waarom de vraag Brits Engels zegt. Een Brit die I feel sick zegt, moet "
                "misschien overgeven.",
            ],
        ),
        dict(
            aanpak="Deze woorden gaan over hoe je je voelt, en het Engels heeft er meer dan het "
                   "Nederlands. Leer ze op een lijn van rustig naar uitgeput, dan weet je ook welk "
                   "woord te sterk is.",
            waarom=[
                "Let op overwhelmed: overweldigd, dus het gevoel dat alles te veel wordt. Het is "
                "sterker dan stressed en komt vaak met by of with: overwhelmed by the work.",
                "Houd het bij twee zinnen met should en try to. Let erop dat er na should geen to "
                "komt (you should go, niet you should to go), en na try to wel een infinitief.",
            ],
        ),
        dict(
            aanpak="Dierennamen en landschapswoorden moet je gewoon kennen. Het helpt om ze in "
                   "groepjes te leren: wat beweegt, wat groeit, en wat vorm geeft aan het landschap.",
            waarom=[
                "Let op an owl met an, want het begint met een klinkerklank. En hedgehog zit in "
                "hedge: letterlijk een haagvarken, want daar leeft hij.",
                "Gravel is grind, dus geen boom; oak, beech en willow zijn de eik, de beuk en de "
                "wilg. Zoek bij zo'n vraag altijd de categorie van de drie andere.",
                "Let op species: dat is zowel enkelvoud als meervoud, dus one species en two "
                "species. Een vaak gemaakte fout is specie, en dat woord bestaat zo niet.",
            ],
        ),
        dict(
            aanpak="Duurzaamheid is een woordveld dat je ook in een examentekst of een opiniestuk "
                   "tegenkomt. Leer naast het woord ook de drie r's op een rij: reduce, reuse, "
                   "recycle.",
            waarom=[
                "Let op emissions: altijd meervoud in deze betekenis. En carbon footprint is een "
                "beeld: de afdruk die je met je uitstoot achterlaat.",
                "Noem dat het om eenmalig gebruik gaat. Single-use is ook een voorbeeld van hoe het "
                "Engels met een streepje een hele bijvoeglijke bepaling maakt, zoals in a ten-year-"
                "old bike.",
                "Houd het bij drie volle zinnen met een werkwoord. Wissel af tussen could, should en "
                "we could, want een opsomming van drie keer dezelfde opbouw leest zwak.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-geld-en-verkeer-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Bij school zitten de valstrikken in de werkwoorden en in de onteltbare "
                   "woorden. Leer de drie werkwoorden rond een examen samen: sit, pass en fail.",
            waarom=[
                "Let op to pass an exam: slagen, niet afleggen. En een subject is een vak, terwijl "
                "a course een hele opleiding of cursus is.",
                "Afleggen, dus enkel deelnemen. I sat the exam zegt niets over het resultaat, en "
                "dat is precies de fout die men met passed maakt.",
                "Zakken. Let op dat fail ook met een lijdend voorwerp kan: I failed maths, dus ik "
                "was niet geslaagd voor wiskunde.",
                "Waar. Net als information, advice en furniture: altijd enkelvoud, en wil je er één "
                "aanduiden, dan zeg je a piece of homework of an assignment.",
            ],
        ),
        dict(
            aanpak="Dit woordveld heb je nodig zodra je zelf een mail schrijft voor een job. Leer "
                   "naast het woord ook het voorzetsel dat erbij hoort, want dat is wat men fout "
                   "doet.",
            waarom=[
                "Let op to apply for a job, met for. En op het verschil tussen to be made redundant "
                "en to be fired: het eerste is ontslagen omdat de functie verdwijnt, het tweede "
                "omdat je iets fout deed. Salary is een maandloon, wages is loon per uur of per week.",
                "Curriculum vitae, Latijn voor levensloop. In de Verenigde Staten heet hetzelfde "
                "document a resume.",
                "Begin met Dear Sir or Madam als je de naam niet kent, en zeg in de eerste zin "
                "meteen waarvoor je solliciteert en waar je de vacature zag. Een mail die met Hello "
                "begint, leest in een sollicitatie te los.",
            ],
        ),
        dict(
            aanpak="Bij geld zijn er twee dingen om te leren: het woord zelf en het werkwoord dat "
                   "erbij past. Spend gebruik je voor geld, pay voor een rekening of een manier van "
                   "betalen.",
            waarom=[
                "Let op the change: wisselgeld, niet verandering, al is het hetzelfde woord. En a "
                "receipt heeft een stille p; het werkwoord erbij is to receive.",
                "Spend money, pay a bill, pay in cash, get a bargain. Je betaalt dus niet money "
                "maar je spendeert het, en dat is net omgekeerd aan het Nederlands.",
                "Pavement is het voetpad, dus geen geldwoord; savings, interest en budget zijn "
                "spaargeld, intrest en budget. Pavement komt in de volgende reeks terug.",
            ],
        ),
        dict(
            aanpak="Verkeer is het woordveld met het grootste verschil tussen Brits en Amerikaans "
                   "Engels. Leer ze als paar, want in een examentekst kan beide staan en je moet "
                   "ze alle twee herkennen.",
            waarom=[
                "Let op pavement: in Brits Engels het voetpad, in Amerikaans Engels het wegdek "
                "zelf. Dat is dus niet enkel een ander woord maar een andere betekenis, en daar "
                "gaan de meeste fouten.",
                "Een zebrapad, genoemd naar de strepen. In het Verenigd Koninkrijk heet een "
                "zebrapad met lichten een pelican crossing.",
                "Het spitsuur, al duurt het meestal langer dan een uur. Let op: in Brits Engels zegt "
                "men ook the rush hour met the ervoor.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-kunst-literatuur-politiek-en-reizen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Splits dit woordveld in twee: de woorden om een werk te benoemen, en de "
                   "woorden om een verhaal te bespreken. Die tweede groep heb je nodig zodra je "
                   "over een boek of een film moet schrijven.",
            waarom=[
                "Let op a novel: een roman, niet een novelle. En an exhibition met een h die je "
                "niet hoort; het werkwoord is to exhibit.",
                "Deze vier zijn het gereedschap om elk verhaal te bespreken: wat er gebeurt, wie "
                "het meemaakt, wie het vertelt en waar en wanneer het speelt. Let op character: "
                "zowel personage als karakter.",
                "Noem beide helften. Let op dat non-fiction niet hetzelfde is als waar: het gaat "
                "over de werkelijkheid, maar een non-fictieboek kan zich vergissen of overtuigen "
                "willen.",
            ],
        ),
        dict(
            aanpak="Politieke woorden lijken sterk op het Nederlands, dus hier gaat het vooral om "
                   "de juiste vorm en het juiste voorzetsel. Leer government als een enkelvoud dat "
                   "in Brits Engels ook meervoudig gebruikt wordt.",
            waarom=[
                "Let op to vote for someone, met for. En an act is de naam van een wet in het "
                "Verenigd Koninkrijk, zoals the Education Act; a law is het begrip in het algemeen.",
                "De Houses of Parliament, met het House of Commons en het House of Lords. In "
                "Belgie zijn dat de Kamer en de Senaat, en dat verschil is een handige vergelijking.",
                "Houd het bij twee zinnen met de gevraagde wendingen en één echt argument. Let op "
                "de komma na In my opinion, en op het streepje in sixteen-year-olds.",
            ],
        ),
        dict(
            aanpak="Reiswoorden komen vaak met een vast werkwoord: book a flight, check in, catch "
                   "the train. Leer die combinaties, want ze staan in elke dialoog over reizen.",
            waarom=[
                "Let op a return ticket: Brits voor heen en terug, terwijl een Amerikaan a "
                "round-trip ticket zegt. Enkel heen is a single (UK) of a one-way (US).",
                "Book a flight, check in at a hotel, get off a plane, catch the train. Let op get "
                "on en get off voor een trein, bus of vliegtuig, maar get in en get out of voor een "
                "auto.",
                "Waar. Net als information en furniture. Wil je stuks noemen, dan zeg je two pieces "
                "of luggage of two suitcases.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-wetenschap-techniek-en-taal-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Veel van deze woorden ken je al uit het Nederlands, dus let vooral op wat "
                   "anders is: de onteltbare woorden en de woorden die op het eerste gezicht "
                   "hetzelfde lijken.",
            waarom=[
                "Let op research: onteltbaar, dus geen a research. En a device is een toestel in het "
                "algemeen, terwijl an appliance een huishoudtoestel is.",
                "Let op a file: zowel een bestand als een map of een vijl, afhankelijk van de "
                "context. En to save betekent zowel opslaan als sparen en redden.",
                "Waar. Je zegt a piece of research, some research of a study. Dezelfde regel als bij "
                "homework, information en advice.",
            ],
        ),
        dict(
            aanpak="Een false friend lijkt op een Nederlands woord maar betekent iets anders. Leer "
                   "er telkens twee dingen bij: wat het echt betekent, en hoe je het Nederlandse "
                   "woord dan wel zegt.",
            waarom=[
                "Deze vijf staan in bijna elke toets. Actually betekent eigenlijk, niet actueel "
                "(dat is current). Eventually is uiteindelijk, niet eventueel. En to control is "
                "besturen of beheersen, niet nakijken.",
                "Possibly of if necessary. Een zin als we will eventually come betekent dus dat je "
                "zeker komt, en dat is net het omgekeerde van wat men bedoelt.",
                "To check. En nakijken van een taak is to mark of to correct, dus ook daar niet "
                "control gebruiken.",
            ],
        ),
        dict(
            aanpak="Van één woord maak je met een voor- of achtervoegsel een ander woord. Leer de "
                   "achtervoegsels per soort: -ion en -ment maken een naamwoord, -er en -or iemand "
                   "die het doet, -ful en -less een bijvoeglijk naamwoord.",
            waarom=[
                "Let op useful en useless: het ene is nuttig, het andere nutteloos, dus kijk goed "
                "wat er gevraagd wordt. En op government: het werkwoord govern verliest zijn n niet, "
                "maar de uitspraak slikt ze half in.",
                "Il-, want legal begint met een l: illegal. Hetzelfde bij im- voor p, b en m "
                "(impossible), en in- voor de rest (incorrect).",
                "Ir-, want regular begint met een r: irregular. Het voorvoegsel past zich dus aan de "
                "beginklank aan, en dat is de hele regel.",
            ],
        ),
        dict(
            aanpak="Brits en Amerikaans verschillen in woorden en in spelling. De spellingregels "
                   "zijn eenvoudig: our wordt or, re wordt er, ise wordt ize, en een dubbele l "
                   "wordt enkel.",
            waarom=[
                "Let op chips: in Brits Engels zijn dat frieten, in Amerikaans Engels chips uit een "
                "zak (die een Brit crisps noemt). Dat is de verwarring die het vaakst voorkomt.",
                "Kies in een eigen tekst één variant en houd die aan. In Vlaamse examens is Brits "
                "Engels de norm, dus schrijf colour en centre, maar reken een Amerikaanse spelling "
                "niet als fout bij een tekst die je leest.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-naamwoorden-lidwoorden-en-hoeveelheden-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De gewone regel is een s erbij, maar let op vier groepen: woorden op f die ves "
                   "worden, woorden op een consonant plus y die ies worden, woorden op s, x, ch of "
                   "sh die es krijgen, en de onregelmatige die je gewoon moet kennen.",
            waarom=[
                "Let op sheep: enkelvoud en meervoud gelijk, net als fish, deer en aircraft. En op "
                "knife dat knives wordt, terwijl roof gewoon roofs blijft.",
                "Analysis wordt analyses, net als basis, crisis en thesis: de is wordt es. Potato "
                "krijgt es (potatoes), net als tomato en hero, maar piano en photo niet.",
            ],
        ),
        dict(
            aanpak="Een onteltbaar woord heeft geen meervoud en geen a ervoor. Wil je er toch één "
                   "van aanduiden, dan zet je er a piece of of an item of voor.",
            waarom=[
                "Deze zes zijn de klassiekers van elke toets. Advice, information, furniture en news "
                "zijn onteltbaar; suitcase en journey niet. Let op dat het Nederlands hier wel een "
                "meervoud heeft, en dat is net waarom de fout zo vaak gemaakt wordt.",
                "Enkelvoud, ondanks de s: the news is good. Hetzelfde bij mathematics, physics en "
                "politics als vakgebied.",
            ],
        ),
        dict(
            aanpak="Drie vragen helpen je kiezen: is het iets algemeens (dan geen lidwoord), is het "
                   "voor het eerst genoemd (dan a of an), of weten we al welke het is (dan the)? "
                   "Instrumenten krijgen altijd the, en school en bed zonder lidwoord als het om de "
                   "bezigheid gaat.",
            waarom=[
                "Let op to go to school zonder lidwoord: het gaat over naar school gaan als "
                "bezigheid. Sta je als ouder bij het gebouw, dan zeg je wel I am at the school. En "
                "the Netherlands krijgt the, net als the United States, omdat het een meervoud is.",
                "Noem dat het om de klank gaat en niet om de letter. Daarom ook an MP3 file, want "
                "de m wordt em uitgesproken, en a one-way ticket, want one begint met een w-klank.",
            ],
        ),
        dict(
            aanpak="Much bij onteltbaar, many bij telbaar. Little en a little bij onteltbaar, few "
                   "en a few bij telbaar. A lot of kan bij beide en is in een gewone zin het "
                   "veiligst.",
            waarom=[
                "Let op dat much en many vooral in vragen en ontkenningen staan; in een bevestigende "
                "zin klinkt a lot of natuurlijker. Daarom staat er in de laatste a lot of work en "
                "niet much work.",
                "A few is enkele en klinkt positief, few is weinig en klinkt als een klacht. "
                "Hetzelfde verschil bij a little en little: a little help is wat hulp, little help "
                "is bijna geen hulp.",
            ],
        ),
        dict(
            aanpak="De s met apostrof gebruik je bij mensen en dieren, of bij tijd (today's paper). "
                   "Bij dingen neem je of. Staat er al een s van het meervoud, dan komt de apostrof "
                   "erachter.",
            waarom=[
                "Let op de drie vormen naast elkaar: sister's (enkelvoud), children's (meervoud "
                "zonder s) en managers' (meervoud met s). Bij the roof of the house blijft of staan, "
                "want een huis is geen persoon.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voornaamwoorden-en-betrekkelijke-bijzinnen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk gaatje af welke soort er moet staan: een bezittelijk zonder "
                   "naamwoord erachter (mine), een wederkerend (herself), of een onderwerp dat enkel "
                   "de zin vult (it of there).",
            waarom=[
                "Let op het verschil tussen it en there: it is raining gaat over het weer, there "
                "were twenty people zegt dat er iets bestaat of aanwezig is. In het Nederlands zeggen "
                "we in beide gevallen het of er, en daar komt de fout.",
                "Its is bezittelijk, it's is een samentrekking van it is of it has. Een handig "
                "steuntje: zet de apostrof enkel waar je ook it is zou kunnen zeggen.",
            ],
        ),
        dict(
            aanpak="Who voor mensen, which voor dingen, whose voor bezit, where voor een plaats. "
                   "That kan who en which vervangen, maar enkel in een bepalende bijzin.",
            waarom=[
                "Let op whose: dat gebruik je ook voor dingen, dus a photo whose colours had faded. "
                "En bij de laatste staat er who en geen that, want die bijzin staat tussen komma's.",
                "Noem het verschil tussen bepalend en niet-bepalend, en gebruik de proef: kan de "
                "bijzin weg zonder dat je niet meer weet over wie het gaat, dan is hij "
                "niet-bepalend en krijgt hij komma's.",
                "Niet waar. In een niet-bepalende bijzin kan enkel who of which, nooit that. Dat is "
                "de regel die uit de vorige oefening volgt.",
            ],
        ),
        dict(
            aanpak="Zoek het woord dat in beide zinnen voorkomt en vervang het in de tweede zin "
                   "door who, which, where of whose. Plak die bijzin dan direct achter het woord "
                   "waar hij bij hoort.",
            waarom=[
                None,
                "Where vervangt there, dus dat woordje verdwijnt: niet the house where we lived "
                "there. Je kan ook zeggen the house in which we lived, en dat is formeler.",
                "Its wordt whose, ook al gaat het over een ding. Veel leerlingen schrijven hier of "
                "which, en dat kan ook, maar whose is korter en gewoner.",
            ],
        ),
        dict(
            aanpak="Some in een bevestigende zin, any in een vraag of een ontkenning. Een "
                   "uitzondering: bij een aanbod of een verzoek staat er some, ook in een vraag.",
            waarom=[
                "Let op would you like some coffee: een aanbod, dus some en geen any. En op no plus "
                "naamwoord tegenover not plus any: there is no time to lose betekent hetzelfde als "
                "there is not any time to lose.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Korte woorden krijgen er en est, lange krijgen more en most. De grens ligt "
                   "ongeveer bij twee lettergrepen; woorden op y worden ier en iest.",
            waarom=[
                "Let op de onregelmatige: good, better, best en bad, worse, worst. En op big dat "
                "zijn g verdubbelt, want na een korte klinker verdubbel je de slotconsonant.",
                "As tall as voor een gelijkheid, the best met the voor de overtreffende trap, en "
                "much colder voor een versterking. Let op: very colder bestaat niet, bij een "
                "vergrotende trap zeg je much, far of a lot.",
            ],
        ),
        dict(
            aanpak="Een bijvoeglijk naamwoord zegt iets over een naamwoord, een bijwoord over een "
                   "werkwoord. Gaat het over hóe iets gebeurt, dan hoort er ly bij, behalve bij de "
                   "koppelwerkwoorden en bij fast en hard.",
            waarom=[
                "Let op fast en hard: die hebben geen ly-vorm als bijwoord. En op hardly, dat wel "
                "bestaat maar iets heel anders betekent.",
                "Hard is hevig of zwaar, hardly is nauwelijks. I worked hard en I hardly worked "
                "zeggen dus net het omgekeerde, en dat is een klassieke valstrik.",
                "Noem het woord koppelwerkwoord en wat het doet. Bij die werkwoorden gaat het over "
                "het onderwerp zelf: she looks good gaat over hoe ze eruitziet, she looks carefully "
                "over hoe ze kijkt.",
            ],
        ),
        dict(
            aanpak="Voorzetsels van tijd volgen een regel: at bij een uur, on bij een dag, in bij "
                   "een maand of jaar. Voor is het moeilijkst wat vast aan een bijvoeglijk "
                   "naamwoord hangt, en dat moet je als combinatie leren.",
            waarom=[
                "Het steuntje gaat van klein naar groot: at six o'clock, on Monday, in 2019. For "
                "noemt een duur, since een startpunt, en during een periode waarin iets gebeurt.",
                "Deze combinaties zijn niet te voorspellen: good at, interested in, afraid of, "
                "depend on, married to. Leer ze als één geheel, want het Nederlandse voorzetsel "
                "helpt je hier niet.",
                "For plus een duur (for three years), since plus een tijdstip (since 2015). Daarom "
                "hoort since bijna altijd bij een present perfect: I have lived here since 2015.",
            ],
        ),
        dict(
            aanpak="De orde van bijvoeglijke naamwoorden in het Engels is vast: mening, grootte, "
                   "leeftijd, vorm, kleur, herkomst, materiaal, en dan het naamwoord. Een getal "
                   "komt altijd vooraan.",
            waarom=[
                "Loop de orde af en je komt er altijd uit: an old black leather jacket volgt "
                "leeftijd, kleur, materiaal. Een moedertaalspreker kent die regel niet, maar hoort "
                "meteen dat a leather black old jacket fout klinkt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-tegenwoordige-tijden-en-de-present-perfect-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De simple present gebruik je voor wat altijd of regelmatig zo is, de present "
                   "continuous voor wat nu bezig is of tijdelijk duurt. Woorden als every day, "
                   "always en never wijzen naar de simple, woorden als look, now en this week naar "
                   "de continuous.",
            waarom=[
                "Let op de derde: water boils at 100 graden Celsius is een algemene waarheid, dus "
                "simple. En de laatste: they are staying with us this week is tijdelijk, dus "
                "continuous, ook al gebeurt het de hele week.",
                "Noem er twee uit de lijst. Dit zijn de state verbs: ze beschrijven een toestand en "
                "geen bezigheid. I am knowing bestaat dus niet, en de reclameslogan I'm loving it "
                "is bewust fout gekozen omdat het opvalt.",
            ],
        ),
        dict(
            aanpak="De present perfect verbindt het verleden met nu: het gebeurde eerder, maar het "
                   "telt nog. Zodra er een afgesloten tijdstip in de zin staat, kan hij niet meer "
                   "en moet het de past simple zijn.",
            waarom=[
                "Let op for en since bij de eerste en de laatste: for tien jaar lang, since vanaf "
                "een punt. En op de plaats van just en not: die komen tussen have en het "
                "deelwoord.",
                "Noem dat het bij de tweede zin nú nog telt. Dat is de hele kern: I have lost my "
                "keys betekent dat ze nog kwijt zijn, I lost my keys kan betekenen dat ik ze "
                "daarna terugvond.",
                "Dit lijstje is het handigst om te onthouden: yesterday, in 2010 en last week zijn "
                "af, dus past simple; since, already en so far lopen door tot nu, dus present "
                "perfect.",
            ],
        ),
        dict(
            aanpak="De present perfect continuous legt de nadruk op hoe lang je ergens mee bezig "
                   "bent, de gewone present perfect op wat er klaar is. Staat er een aantal in de "
                   "zin, dan is het bijna altijd de gewone vorm.",
            waarom=[
                "Vergelijk de tweede met de andere twee: three emails is een resultaat dat je kan "
                "tellen, dus has written. For an hour en all morning zijn duur, dus de continuous.",
                "Op de duur. Daarom hoort de continuous bij for an hour, all morning en how long, "
                "en de gewone vorm bij een aantal of een afgewerkt resultaat.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-verleden-tijden-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Onregelmatige werkwoorden moet je kennen, maar ze zitten in groepjes: buy, "
                   "catch en bring eindigen alle drie op ought of aught, en choose, write en fall "
                   "hebben een apart deelwoord op en.",
            waarom=[
                "Let op het verschil tussen de eerste groep (verleden tijd en deelwoord gelijk) en "
                "de tweede (deelwoord op en). Bij chose, chosen hoor je dat verschil ook.",
                "Deze vier zijn de lastigste van allemaal. Lie betekent liggen en is onregelmatig "
                "(lay, lain), lay betekent leggen en is regelmatig (laid). Hetzelfde patroon bij "
                "rise, dat vanzelf stijgt, en raise, dat iemand doet stijgen. Let op dat lay ook "
                "de verleden tijd van lie is, en daar komt alle verwarring van.",
            ],
        ),
        dict(
            aanpak="De past continuous is wat al bezig was, de past simple wat er toen gebeurde. "
                   "While hoort bij de continuous, when meestal bij de simple.",
            waarom=[
                "Let op het patroon: de lange handeling in de continuous, de korte die ertussen "
                "komt in de simple. Daarom was cooking en rang, en were watching en went out.",
                "Noem beide helften, want dat is de regel die je bij elk verhaal kan gebruiken. "
                "Een verhaal opent dan ook vaak met een continuous die het decor zet.",
            ],
        ),
        dict(
            aanpak="De past perfect is het verleden van het verleden: iets dat al gebeurd was voor "
                   "het moment waar je verhaal staat. Je hebt dus altijd twee momenten nodig.",
            waarom=[
                "Let op de plaats van already en never: die komen tussen had en het deelwoord. En "
                "op de laatste: she had finished before the others arrived, dus eerst het "
                "afgewerkte, dan het latere.",
                "Noem dat het gaat om wat nog vroeger gebeurde. In een indirecte rede verschuift "
                "alles een stap: he said he had never flown, en dat komt in de bundel over de "
                "indirecte rede terug.",
            ],
        ),
        dict(
            aanpak="Used to en would beschrijven beide een gewoonte uit het verleden die nu niet "
                   "meer bestaat. Het verschil: used to kan ook bij een toestand, would enkel bij "
                   "een handeling die zich herhaalde.",
            waarom=[
                "Na used to komt de infinitief zonder to erbij: used to play, niet used to played. "
                "Let ook op de ontkenning: I did not use to play, zonder d.",
                "Nee, want wonen is een toestand en geen herhaalde handeling. I used to live in "
                "Ghent kan wel, en dat is net het verschil tussen de twee.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-toekomst-de-modale-hulpwerkwoorden-en-de-gerund-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Het Engels heeft drie manieren om over de toekomst te praten. Going to voor "
                   "een plan dat vastligt of voor wat je ziet aankomen, will voor een beslissing "
                   "op het moment of een voorspelling, en de present continuous voor een afspraak "
                   "met een tijdstip erbij.",
            waarom=[
                "Let op de eerste en de laatste: de wolken zie je nu al, en de studiekeuze ligt "
                "vast, dus beide going to. We are meeting Sara at eight is een afspraak in de "
                "agenda, dus de present continuous.",
                "Noem beide helften in één zin. Een handig steuntje: bij I promise of I think hoort "
                "will, bij I have decided hoort going to.",
            ],
        ),
        dict(
            aanpak="Modale werkwoorden zeggen hoe zeker of hoe verplicht iets is. Must voor een "
                   "verplichting of een sterke conclusie, cannot voor een conclusie die niet kan, "
                   "should voor een raad, may en can om toestemming te vragen.",
            waarom=[
                "Let op de derde en de vijfde: must kan ook een conclusie zijn (haar auto staat "
                "daar, dus ze is thuis), en should have plus deelwoord is een verwijt over het "
                "verleden.",
                "Must not is een verbod, do not have to betekent dat het mag maar niet moet. Dat is "
                "het grootste verschil met het Nederlands, waar moet niet beide kan betekenen.",
            ],
        ),
        dict(
            aanpak="Na sommige werkwoorden komt de ing-vorm, na andere de infinitief met to. De "
                   "lijsten moet je kennen, maar er is een regel die altijd geldt: na een "
                   "voorzetsel komt altijd de ing-vorm.",
            waarom=[
                "Enjoy, avoid en mind nemen de ing-vorm; decide en hope nemen to. De laatste twee "
                "hebben een voorzetsel voor zich (mind plus ing, forward to plus ing), en dat "
                "beslist.",
                "Noem dat to hier een voorzetsel is en geen deel van de infinitief. Hetzelfde bij "
                "be used to doing en look forward to meeting.",
                "Noem beide betekenissen. Dezelfde omslag bij remember: I remember locking the door "
                "is een herinnering, I remembered to lock the door is dat je het niet vergat.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zinsbouw-indirecte-rede-en-de-passieve-vorm-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een vraag of een ontkenning heeft een hulpwerkwoord nodig. Staat er al een "
                   "(have, can, is), dan zet je dat vooraan. Staat er geen, dan haal je do, does of "
                   "did erbij, en het hoofdwerkwoord gaat terug naar de infinitief.",
            waarom=[
                "Let op de eerste en de laatste: works wordt does she work (de s verhuist naar "
                "does) en saw wordt did you see (de verleden tijd verhuist naar did). Did you saw "
                "is dus dubbel fout.",
                "Isn't she, dus omgekeerd aan de hoofdzin: een bevestiging krijgt een ontkennende "
                "tag en omgekeerd. Dat is wat het Nederlandse he of niet in een vraagje doet.",
            ],
        ),
        dict(
            aanpak="In de indirecte rede schuift alles een stap naar achteren: de tijd, de persoon "
                   "en de tijds- en plaatswoorden. Bij een vraag verdwijnt de vraagomkering, bij een "
                   "bevel komt er not to of to plus infinitief.",
            waarom=[
                None,
                "Will wordt would en tomorrow wordt the next day. Let ook op you dat me wordt, want "
                "de spreker is veranderd.",
                "Let erop dat de vraagvorm verdwijnt: niet he asked where did I live, maar he asked "
                "where I lived. Dat is de fout die het vaakst gemaakt wordt.",
                "Bij een bevel gebruik je to plus infinitief, en bij een verbod not to. Dus she "
                "told him to leave en she told him not to touch that.",
                "The next day en there. Hetzelfde bij today dat that day wordt, yesterday dat the "
                "day before wordt, en this dat that wordt.",
            ],
        ),
        dict(
            aanpak="In de passieve vorm wordt het lijdend voorwerp het onderwerp. Je neemt de "
                   "juiste vorm van to be en het voltooid deelwoord, en je houdt de tijd van de "
                   "actieve zin aan.",
            waarom=[
                None,
                "Has stolen wordt has been stolen: de present perfect blijft, maar er komt been "
                "bij. Someone verdwijnt, want wie het deed weet je niet.",
                "Are repairing wordt is being repaired: bij een continuous heb je zowel being als "
                "het deelwoord nodig. Dat is de vorm die het meest fout gaat.",
                "Noem twee redenen, en liefst ook dat het in verslagen en wetenschappelijke teksten "
                "de gewone manier van schrijven is. Wil je de dader er toch bij, dan gebruik je by: "
                "the bridge was built by the city.",
            ],
        ),
        dict(
            aanpak="Er zijn vier soorten voorwaardelijke zinnen. De nulde voor wat altijd zo is "
                   "(present plus present), de eerste voor wat echt kan (present plus will), de "
                   "tweede voor wat onwaarschijnlijk is (past plus would), de derde voor wat niet "
                   "meer kan veranderen (past perfect plus would have).",
            waarom=[
                "Let op de laatste: if you heat ice, it melts is de nulde conditional, dus geen "
                "will. En let erop dat er na if nooit will of would staat.",
                "De derde conditional, want die gaat over het verleden: if she had studied, she "
                "would have passed. Ze heeft niet gestudeerd en dat is nu niet meer te veranderen.",
            ],
        ),
    ],
)
