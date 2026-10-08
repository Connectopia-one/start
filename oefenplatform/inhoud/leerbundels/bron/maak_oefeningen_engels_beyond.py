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
