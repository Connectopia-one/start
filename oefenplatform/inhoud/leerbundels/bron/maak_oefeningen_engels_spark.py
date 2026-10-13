# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Engels ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof, alleen met andere vragen. Dezelfde pdf gaat dus bij allebei.

Net als de vragen op het scherm dekt dit **enkel de schriftelijke onderdelen**
van het examen: lezen, schrijven, woordenschat en grammatica. Spreken en
luisteren staan er niet in.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Wie hier iets bijschrijft, legt het eerst naast `../../spark/engels.json`.

Een leesvraag hoort op een echt tekstje in die taal te staan en niet op het
begrip alleen. De leesbundel draagt daarom zijn eigen Engelse tekst mee, een
andere dan die van de vragen online.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel, svg

SPARK = "✨ Spark — 1ste en 2de middelbaar"

W = "150px"
WW = "220px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Ken je een woord niet? Kijk eerst of het op een Nederlands woord lijkt.",
    "Schrijf Engelse woorden voluit, met hoofdletter waar het hoort.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-een-engelse-tekst-lezen-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Een Engelse tekst lezen",
    onder="Een tekst en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=[
        "Lees de tekst eerst helemaal door. Je moet niet elk woord kennen.",
        "Onderstreep de woorden die je niet kent en probeer ze eerst te raden.",
        "Kom bij elke vraag terug naar de tekst.",
        "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
    ],
    reeksen=[
        dict(kop="Reading",
             opdracht="Lees deze tekst. De vragen erna gaan alleen hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>The walking bus</h3>"
                  "<p>Every morning at half past seven, twelve children meet at the church in "
                  "Ledbury. They do not wait for a bus. They walk to school together, with two "
                  "parents in front and one at the back. They call it the walking bus.</p>"
                  "<p>&#8222;We started last October&#8221;, says Mrs Price, one of the parents. "
                  "&#8222;There were too many cars at the school gate. Now there are fewer cars, "
                  "and the children arrive awake.&#8221;</p>"
                  "<p>However, not everything is easy. The walking bus goes out in the rain as "
                  "well, and in December it is still dark at half past seven. Every child "
                  "therefore wears a yellow jacket. &#8222;My feet were wet for a whole "
                  "week&#8221;, says Owen, twelve. &#8222;But I would not go by car again. You "
                  "talk to your friends on the way.&#8221;</p>"
                  "<p>The school now has three walking buses, one from each side of the town. "
                  "About one child in five walks with them. In June the school will ask the "
                  "parents whether they want more.</p>"),
             ]),

        dict(kop="Wat staat er in de tekst",
             opdracht="Antwoord in het Nederlands, tenzij er iets anders staat.",
             oefeningen=[
                 ("kort", "Hoeveel kinderen komen er 's morgens samen bij de kerk?", "twaalf", W),
                 ("kort", "Hoe laat vertrekken ze?", "om half acht", W),
                 ("kort", "Hoe oud is Owen?", "twaalf jaar", W),
                 ("open", "Waarom zijn de ouders met de walking bus begonnen? Geef de reden uit "
                          "de tekst.",
                  "Er stonden te veel auto's aan de schoolpoort. Nu zijn er minder auto's, en de "
                  "kinderen komen wakker op school aan.", 4),
                 ("open", "Noem twee nadelen die in de tekst staan.",
                  "Ze gaan ook op stap als het regent, en in december is het om half acht nog "
                  "donker. Owen had een hele week natte voeten.", 4),
                 ("kort", "Schrijf het onderwerp van deze tekst in enkele woorden.",
                  "samen te voet naar school", WW),
             ]),

        dict(kop="Woorden raden uit de tekst",
             opdracht="Gebruik de zin eromheen. Sla je woordenboek pas daarna open.",
             oefeningen=[
                 ("rij", [("the school gate", "de schoolpoort"), ("however", "nochtans, toch"),
                          ("therefore", "daarom"), ("fewer", "minder"),
                          ("awake", "wakker"), ("a whole week", "een hele week")],
                  "Wat betekent dit in de tekst?", WW),
                 ("open", "&#8222;They call it the walking bus.&#8221; Naar wat verwijst 'it' in "
                          "deze zin?",
                  "Naar wat ze elke ochtend doen: samen te voet naar school gaan.", 3),
                 ("kort", "&#8222;About one child in five walks with them.&#8221; Hoeveel "
                          "kinderen van de honderd is dat?", "twintig", W),
                 ("waar", "Een Engels woord dat op een Nederlands woord lijkt, betekent altijd "
                          "hetzelfde.", False),
             ]),

        dict(kop="Strategie",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je moet uit een lange tekst alleen halen hoeveel een schoolreis "
                          "kost. Hoe pak je dat aan?",
                  "Je leest gericht: je weet dat je een bedrag zoekt, dus je loopt de tekst af "
                  "tot je een getal met euro of pond tegenkomt. Je hoeft de hele tekst niet te "
                  "vertalen.", 4),
                 ("rij", [("according to a recent study", "er komt een bron of een cijfer"),
                          ("in my opinion", "er komt een mening, geen feit"),
                          ("you must not", "er komt een verbod"),
                          ("this article is about", "er komt het onderwerp")],
                  "Wat kondigt dit aan?", WW),
                 ("waar", "'A.m.' betekent 's avonds en 'p.m.' 's ochtends.", False),
                 ("open", "Je kent één woord in een zin niet en je hebt nog vier vragen te gaan. "
                          "Wat doe je?",
                  "Je kijkt eerst of je het uit de zin eromheen kan raden, en of je de vraag ook "
                  "zonder dat woord kan beantwoorden. Alleen als het echt nodig is, zoek je het "
                  "op.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstsoorten-signaalwoorden-en-verwijswoorden-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Tekstsoorten, signaalwoorden en verwijswoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke tekstsoort",
             opdracht="Kijk naar de werkwoordsvorm en naar wat de tekst van je wil.",
             oefeningen=[
                 ("rij", [("Peel the potatoes. Then boil them for twenty minutes.", "prescriptief"),
                          ("I think our school should start at nine.", "opini&#235;rend"),
                          ("Cardiff has about 360,000 inhabitants.", "informatief"),
                          ("Once upon a time, a fox lived under an old bridge.", "narratief"),
                          ("The moon was a silver coin above the roofs.", "literair")],
                  "Welke tekstsoort is dit?", WW),
                 ("open", "Waarom is het nuttig om te weten wat voor soort tekst je leest?",
                  "Je weet dan wat je moet zoeken: bij een instructie de stappen, bij een "
                  "informatieve tekst de feiten, bij een mening de argumenten. Je leest "
                  "gerichter en sneller.", 4),
                 ("kort", "Hoe noemen we een tekst die uitlegt wat of hoe je iets moet doen?",
                  "prescriptief", W),
             ]),

        dict(kop="Het communicatiemodel",
             opdracht="Drie vragen bij elke tekst: van wie, waarom en voor wie?",
             oefeningen=[
                 ("open", "&#8222;Keep out of reach of children. Use before the date on the "
                          "box.&#8221; Van wie is deze tekst, waarom is hij gemaakt en voor wie "
                          "is hij bedoeld?",
                  "Van de fabrikant, om te zeggen hoe je het bewaart en gebruikt, voor wie het "
                  "product koopt.", 4),
                 ("kort", "&#8222;Ten tips for your first camping trip.&#8221; Voor wie is deze "
                          "tekst bedoeld?", "voor wie voor het eerst gaat kamperen", WW),
                 ("waar", "Hoeveel bladzijden een tekst telt, hoort bij het communicatiemodel.",
                  False),
             ]),

        dict(kop="Signaalwoorden",
             opdracht="Schrijf de betekenis én het verband.",
             oefeningen=[
                 ("rij", [("first", "eerst"), ("then", "daarna"), ("after that", "vervolgens"),
                          ("finally", "ten slotte")],
                  "Wat betekent dit?"),
                 ("rij", [("because", "reden: omdat"), ("so", "gevolg: dus"),
                          ("but", "tegenstelling: maar"), ("however", "tegenstelling: nochtans"),
                          ("for example", "voorbeeld: bijvoorbeeld"),
                          ("in addition", "toevoeging: bovendien")],
                  "Wat betekent dit, en welk verband kondigt het aan?", WW),
                 ("rij", [("I stayed at home ___ it was raining.", "because"),
                          ("He missed the train, ___ he was late.", "so"),
                          ("She is small, ___ she runs very fast.", "but / however")],
                  "Vul het passende signaalwoord in.", WW),
                 ("kies", "Welk woord is g&#233;&#233;n signaalwoord?",
                  ["however", "because", "very", "finally"], 2),
             ]),

        dict(kop="Verwijswoorden",
             opdracht="Schrijf naar wie of wat het vette woord verwijst.",
             oefeningen=[
                 ("rij", [("Tom was late again. <b>He</b> had missed the bus.", "Tom"),
                          ("My aunts live in Cork. <b>They</b> have a shop <b>there</b>.",
                           "mijn tantes / in Cork"),
                          ("Lucy lost her keys. She found <b>them</b> in the car.",
                           "de sleutels"),
                          ("We went to the market. <b>It</b> was crowded.", "de markt")],
                  "Naar wie of wat verwijst het vette woord?", WW),
                 ("open", "Waarom gebruikt een schrijver verwijswoorden in plaats van telkens "
                          "hetzelfde woord te herhalen?",
                  "Omdat de tekst anders houterig wordt. Een verwijswoord houdt de zinnen aan "
                  "elkaar zonder dat je steeds hetzelfde moet lezen.", 3),
                 ("open", "Wat doe je als een verwijswoord in je eigen tekst onduidelijk is?",
                  "Je schrijft het woord waarnaar het verwijst opnieuw voluit, of je zet de "
                  "zinnen dichter bij elkaar zodat er geen twijfel meer is.", 3),
             ]),

        dict(kop="Woorden afleiden uit hun vorm",
             opdracht="Schrijf de betekenis in het Nederlands.",
             oefeningen=[
                 ("rij", [("unfair", "oneerlijk"), ("impossible", "onmogelijk"),
                          ("disagree", "het oneens zijn"), ("useful", "nuttig"),
                          ("incorrect", "onjuist")],
                  "Wat betekent dit woord?", WW),
                 ("waar", "De voorvoegsels un-, im- en dis- draaien de betekenis van een woord om.",
                  True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-schrijven-berichten-uitnodigingen-en-mails-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Schrijven: berichten, uitnodigingen en mails",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vaste zinnen",
             opdracht="Schrijf de Engelse zin voluit.",
             oefeningen=[
                 ("rij", [("Hartelijk dank.", "Thank you very much."),
                          ("Het spijt me, ik kan niet komen.", "I'm sorry, I can't come."),
                          ("Geen probleem.", "That's all right. / No problem."),
                          ("Ik zou graag&#8230;", "I would like to&#8230;")],
                  "Hoe schrijf je dat in het Engels?", WW),
                 ("rij", [("Kan je me helpen, alsjeblieft?", "Could you help me, please?"),
                          ("Proficiat!", "Congratulations!"),
                          ("Tot binnenkort.", "See you soon.")],
                  "Hoe schrijf je dat in het Engels?", WW),
                 ("kort", "Wat betekent 'I look forward to hearing from you' ?",
                  "ik kijk uit naar je antwoord", WW),
             ]),

        dict(kop="Formeel of informeel",
             opdracht="Denk aan wie de ontvanger is.",
             oefeningen=[
                 ("rij", [("aan je beste vriend", "Hi Tom, &#8230; Bye!"),
                          ("aan de directeur", "Dear Mr Jones, &#8230; Kind regards,"),
                          ("aan iemand van wie je de naam niet kent",
                           "Dear Sir or Madam, &#8230; Yours faithfully,")],
                  "Welke aanhef en welke slotgroet passen?", WW),
                 ("rij", [("Send me the form now.", "Could you please send me the form?"),
                          ("You have to come to my party.", "Would you like to come to my party?"),
                          ("Give me your address.", "Could you give me your address, please?")],
                  "Schrijf dit beleefd.", WW),
                 ("waar", "'Mate' kan je gerust gebruiken in een mail aan een onbekende "
                          "volwassene.", False),
             ]),

        dict(kop="Zelf schrijven",
             opdracht="Schrijf hieronder. Kleine fouten mogen, zolang je boodschap duidelijk is.",
             oefeningen=[
                 ("open", "Schrijf in het Engels een uitnodiging van drie zinnen voor je "
                          "verjaardagsfeest. Zet er zeker in: wat, wanneer, hoe laat en waar.",
                  "Bijvoorbeeld: &#8222;Hi Emma! I am having a birthday party on Saturday 12 "
                  "October at four o'clock, at my house in Oak Street 8. Would you like to "
                  "come?&#8221;", 6),
                 ("open", "Schrijf in het Engels een korte mail (drie zinnen) aan een zwemclub om "
                          "te vragen hoeveel het lidgeld kost. Gebruik een formele aanhef.",
                  "Bijvoorbeeld: &#8222;Dear Sir or Madam, My name is Lotte and I would like to "
                  "join your swimming club. Could you tell me how much the membership costs? "
                  "Kind regards, Lotte&#8221;", 6),
                 ("open", "Je hebt een koptelefoon gekocht die niet werkt. Schrijf twee Engelse "
                          "zinnen aan de winkel: wat je kocht en wat je wil.",
                  "Bijvoorbeeld: &#8222;I bought these headphones in your shop last week, but the "
                  "left one does not work. Could I have a new pair?&#8221;", 5),
             ]),

        dict(kop="Nakijken",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Er staat 'Write about 80 words' en jij schrijft er 30. Waarop verlies "
                          "je punten, ook al is elk woord juist?",
                  "Op taakvoltooiing: de opgegeven lengte hoort bij de opdracht, en met 30 "
                  "woorden krijg je je boodschap niet volledig over.", 4),
                 ("open", "Wat doe je als laatste, vóór je je tekst indient?",
                  "Je leest hem helemaal na: staan alle gevraagde onderdelen erin, klopt de "
                  "lengte, en heb je overal dezelfde toon volgehouden?", 4),
                 ("open", "Je zit vast omdat je een woord niet kent. Wat doe je?",
                  "Je omschrijft het met woorden die je wel kent, of je kiest een zin die "
                  "hetzelfde zegt met andere woorden. Je laat de zin niet half staan.", 4),
                 ("rij", [("i went to londen", "I went to London"),
                          ("my freind", "my friend"),
                          ("congratulation", "congratulations"),
                          ("becouse", "because")],
                  "Verbeter de spelling.", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-engelstalige-landen-en-literaire-teksten-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Engelstalige landen en literaire teksten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waar spreekt men Engels",
             opdracht="Schrijf je antwoord in het Engels, met hoofdletter.",
             oefeningen=[
                 ("rij", [("Ireland", "Irish"), ("Scotland", "Scottish"),
                          ("Belgium", "Belgian"), ("Spain", "Spanish"),
                          ("the United Kingdom", "British")],
                  "Welke nationaliteit hoort bij dit land?", WW),
                 ("kort", "Hoe heet de hoofdstad van Schotland?", "Edinburgh", W),
                 ("open", "Noem drie landen buiten het Verenigd Koninkrijk waar Engels de taal "
                          "van het dagelijkse leven is.",
                  "Bijvoorbeeld Ierland, de Verenigde Staten, Canada, Australi&#235; en "
                  "Nieuw-Zeeland.", 3),
                 ("waar", "In Ierland betaal je met pond.", False),
             ]),

        dict(kop="Gewoontes en verschillen",
             opdracht="Antwoord in het Nederlands.",
             oefeningen=[
                 ("rij", [("Halloween", "31 oktober"),
                          ("Thanksgiving", "vierde donderdag van november, in de Verenigde Staten"),
                          ("Bonfire Night", "5 november, in het Verenigd Koninkrijk"),
                          ("Saint Patrick's Day", "17 maart, in Ierland")],
                  "Wanneer en waar wordt dit gevierd?", WW),
                 ("kort", "In welke maand valt Kerstmis in Australi&#235; midden in de zomer?",
                  "december", W),
                 ("open", "Een Amerikaanse tekst zegt: 'It was 70 degrees and we drove three "
                          "miles.' Waarom mag je daar niet 70 graden Celsius van maken?",
                  "Omdat de Verenigde Staten in Fahrenheit meten. 70 graden Fahrenheit is "
                  "ongeveer 21 graden Celsius, en een mile is ongeveer 1,6 kilometer.", 4),
                 ("open", "Je leest: 'Take the lift to the first floor.' Waarom kan dat in "
                          "Londen iets anders betekenen dan in New York?",
                  "In het Brits is the first floor de eerste verdieping boven de begane grond; "
                  "in het Amerikaans is the first floor de begane grond zelf.", 4),
             ]),

        dict(kop="Brits of Amerikaans",
             opdracht="Schrijf het woord dat hetzelfde betekent in de andere variant.",
             oefeningen=[
                 ("rij", [("lift", "elevator"), ("biscuit", "cookie"), ("autumn", "fall"),
                          ("holiday", "vacation"), ("flat", "apartment")],
                  "Brits woord links, Amerikaans woord rechts.", WW),
                 ("rij", [("colour", "color"), ("theatre", "theater"), ("travelling", "traveling")],
                  "Hoe schrijft een Amerikaan dit?", WW),
                 ("waar", "Wie 'color' schrijft in plaats van 'colour', maakt een schrijffout.",
                  False),
             ]),

        dict(kop="Reageren op een literaire tekst",
             opdracht="Lees het gedicht en antwoord eronder.",
             oefeningen=[
                 ("tekst",
                  "<p><i>The street is empty tonight.<br>Nobody waits at the door.<br>"
                  "The rain keeps falling on the same stone.</i></p>"),
                 ("kort", "Waarover gaat dit gedicht, in &#233;&#233;n woord?", "eenzaamheid", W),
                 ("open", "Schrijf in het Engels twee zinnen over dit gedicht: welk gevoel het "
                          "oproept, en waarom.",
                  "Bijvoorbeeld: &#8222;This poem makes me feel sad, because nobody is waiting "
                  "for the person. The rain makes it even quieter.&#8221;", 5),
                 ("open", "Een verhaal stopt met: 'He looked at the empty box and closed the "
                          "door.' Schrijf een geloofwaardig einde van twee zinnen.",
                  "Bijvoorbeeld: hij begreep dat iemand de doos al had leeggehaald, en hij ging "
                  "het aan zijn zus vragen. Geloofwaardig betekent: het past bij wat er al "
                  "gebeurd is, dus geen draak die uit het niets komt.", 5),
                 ("kies", "Welke tekst is g&#233;&#233;n literaire tekst?",
                  ["a poem", "a song", "a school report", "a short story"], 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-mensen-familie-gevoelens-en-gezondheid-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Woordenschat: mensen, familie, gevoelens en gezondheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Familie",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("de zus van je moeder", "aunt"), ("de zoon van je tante", "cousin"),
                          ("de dochter van je broer", "niece"), ("je kleinkind", "grandchild"),
                          ("een enig kind", "an only child")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("waar", "'Nephew' en 'niece' zijn de kinderen van je broer of zus.", True),
                 ("kort", "Wat betekent 'twins' ?", "een tweeling", W),
                 ("open", "Wat is het verschil tussen 'a cousin' en 'a nephew' ?",
                  "'A cousin' is het kind van je tante of oom. 'A nephew' is het zoontje van je "
                  "broer of zus.", 3),
             ]),

        dict(kop="Gevoelens en karakter",
             opdracht="Schrijf de betekenis of het juiste woord.",
             oefeningen=[
                 ("rij", [("proud", "trots"), ("worried", "bezorgd"), ("nervous", "zenuwachtig"),
                          ("disappointed", "teleurgesteld"), ("relieved", "opgelucht"),
                          ("jealous", "jaloers")],
                  "Wat betekent dit woord?", WW),
                 ("kies", "Je verveelt je. Wat schrijf je?",
                  ["I am boring.", "I am bored.", "I am a bore.", "I bore."], 1),
                 ("kort", "Vul aan: 'She is afraid ___ spiders.'", "of", W),
                 ("open", "Waarom mag je 'sympathetic' niet vertalen als 'sympathiek'?",
                  "Omdat het meelevend of begripvol betekent. Wil je zeggen dat iemand "
                  "sympathiek is, dan schrijf je 'nice' of 'likeable'.", 3),
                 ("rij", [("friendly", "karakter"), ("tall", "uiterlijk"),
                          ("shy", "karakter"), ("blond", "uiterlijk")],
                  "Zegt dit iets over het karakter of over het uiterlijk?", W),
             ]),

        dict(kop="Gezondheid en lichaam",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("keelpijn", "a sore throat"), ("hoofdpijn", "a headache"),
                          ("buikpijn", "stomach ache"), ("koorts hebben", "to have a fever"),
                          ("een apotheek", "a chemist's / a pharmacy")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("rij", [("elbow", "elleboog"), ("knee", "knie"), ("thumb", "duim"),
                          ("ankle", "enkel"), ("cheek", "wang"), ("chin", "kin")],
                  "Welk lichaamsdeel is dit?", W),
                 ("rij", [("tooth", "teeth"), ("foot", "feet"), ("child", "children")],
                  "Schrijf het meervoud.", W),
                 ("kort", "Vul aan: 'Her hair ___ very long.' (is of are)", "is", W),
                 ("kort", "Vul aan: 'Take this medicine ___ a day.' (twee keer)", "twice", W),
             ]),

        dict(kop="Persoonlijke gegevens",
             opdracht="Antwoord in het Nederlands.",
             oefeningen=[
                 ("rij", [("first name", "voornaam"), ("surname", "achternaam"),
                          ("date of birth", "geboortedatum"),
                          ("place of birth", "geboorteplaats"), ("nationality", "nationaliteit")],
                  "Wat vul je hier in?", WW),
                 ("kort", "Welke nationaliteit schrijf je als je in Belgi&#235; woont? Antwoord "
                          "in het Engels.", "Belgian", W),
                 ("open", "Beschrijf in het Engels in twee zinnen hoe je beste vriend of "
                          "vriendin eruitziet.",
                  "Bijvoorbeeld: &#8222;She has long dark hair and green eyes. She is quite tall "
                  "and she wears glasses.&#8221; Waar iemand woont, hoort niet bij een "
                  "beschrijving van het uiterlijk.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-eten-wonen-kleding-en-dagelijkse-dingen-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Woordenschat: eten, wonen, kleding en dagelijkse dingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eten en drinken",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("een wortel", "a carrot"), ("een ui", "an onion"),
                          ("een peer", "a pear"), ("een druif", "a grape"),
                          ("bloem (om te bakken)", "flour"), ("een lepel", "a spoon")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("kort", "Waarom is 'a grape' een valse vriend?",
                  "het is een druif, geen grapefruit", WW),
                 ("open", "Een Brit bestelt 'fish and chips'. Wat krijgt hij op zijn bord, en wat "
                          "zou een Amerikaan ervoor zeggen?",
                  "Vis met frieten. Een Amerikaan zegt 'french fries' voor frieten; bij hem zijn "
                  "'chips' de chips uit een zakje.", 4),
                 ("rij", [("brood", "two slices of bread"), ("water", "three glasses of water"),
                          ("rijst", "two bowls of rice")],
                  "Hoe tel je dit? Schrijf de hele woordgroep.", WW),
                 ("kort", "Wat vraagt een gastheer met 'Would you like some more soup?'",
                  "wil je nog wat soep", WW),
                 ("kort", "Hoe vraagt een Brit in een restaurant om de rekening?",
                  "the bill, please", WW),
             ]),

        dict(kop="Wonen",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("a cellar", "een kelder"), ("an attic", "een zolder"),
                          ("a wardrobe", "een kleerkast"), ("a bookcase", "een boekenkast"),
                          ("a curtain", "een gordijn"), ("a hall", "een gang of hal")],
                  "Wat betekent dit woord?", WW),
                 ("kort", "Hoe noemt een Brit een appartement?", "a flat", W),
                 ("rij", [("het licht uitzetten", "to turn off the light"),
                          ("de radio aanzetten", "to turn on the radio")],
                  "Hoe zeg je dat in het Engels?", WW),
             ]),

        dict(kop="Kleding en materialen",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("een trui (Brits)", "a jumper"), ("een rok", "a skirt"),
                          ("sportschoenen (Brits)", "trainers"), ("een riem", "a belt"),
                          ("een bril", "glasses")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("kies", "Welke zin is juist?",
                  ["My trouser is new.", "My trousers are new.", "My trousers is new.",
                   "My trouser are new."], 1),
                 ("rij", [("cotton", "katoen"), ("wool", "wol"), ("leather", "leder"),
                          ("wood", "hout")],
                  "Van welk materiaal is dit?", W),
                 ("kort", "Vul aan: 'She is ___ a red coat.' (heeft aan)", "wearing", W),
             ]),

        dict(kop="Elke dag, en de winkel",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("opstaan", "to get up"), ("je tanden poetsen", "to brush your teeth"),
                          ("je aankleden", "to get dressed"),
                          ("de afwas doen", "to do the washing-up"),
                          ("de was doen", "to do the washing")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("rij", [("a baker's", "een bakkerij"), ("a butcher's", "een slagerij"),
                          ("a newsagent's", "een krantenwinkel"),
                          ("a library", "een bibliotheek"), ("a bookshop", "een boekhandel")],
                  "Welke winkel of plaats is dit?", WW),
                 ("open", "Waarom zijn 'a library' en 'a magazine' valse vrienden?",
                  "'A library' is een bibliotheek en niet een boekhandel; 'a magazine' is een "
                  "tijdschrift en niet een magazijn.", 4),
                 ("kort", "Een winkel is open 'from 9 a.m. to 8 p.m.' Van hoe laat tot hoe laat "
                          "is dat?", "van 9 uur 's ochtends tot 8 uur 's avonds", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-school-beroepen-sport-en-vrije-tijd-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Woordenschat: school, beroepen, sport en vrije tijd",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Instructietaal",
             opdracht="Dit staat in de opdracht zelf. Schrijf wat je moet doen.",
             oefeningen=[
                 ("rij", [("Tick the correct answer.", "kruis het juiste antwoord aan"),
                          ("Underline the verbs.", "onderstreep de werkwoorden"),
                          ("Cross out the wrong word.", "streep het foute woord door"),
                          ("Match the words with the pictures.", "koppel de woorden aan de prenten"),
                          ("Fill in the gaps.", "vul de leegtes in"),
                          ("Put the sentences in the right order.",
                           "zet de zinnen in de juiste volgorde")],
                  "Wat moet je doen?", WW),
                 ("open", "Er staat 'Answer in full sentences.' en de vraag is 'Do you like "
                          "tea?'. Wat schrijf je, en wat schrijf je niet?",
                  "Je schrijft 'Yes, I do.' of 'No, I don't.' en niet alleen 'yes' of 'no'.", 3),
                 ("kort", "Wat betekent 'about' in 'Write about 80 words' ?", "ongeveer", W),
             ]),

        dict(kop="School",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("een leerling", "a pupil"), ("een directeur (Brits)", "a headteacher"),
                          ("een vak", "a subject"), ("een uurrooster", "a timetable"),
                          ("een speelplaats", "a playground"), ("een punt of cijfer", "a mark")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("kort", "Waarvoor staat de afkorting PE?", "physical education", WW),
                 ("waar", "'Homework' krijgt in het meervoud een -s: homeworks.", False),
                 ("kort", "Schrijf voluit in het Engels: 24 leerlingen.",
                  "twenty-four pupils", WW),
             ]),

        dict(kop="Beroepen",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een verpleegkundige", "a nurse"), ("een loodgieter", "a plumber"),
                          ("een advocaat", "a lawyer"), ("een winkelbediende", "a shop assistant"),
                          ("een brandweerman", "a firefighter")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("kort", "Vul aan: 'We are ___ ___ a shop assistant.' (wij zoeken)",
                  "looking for", W),
             ]),

        dict(kop="Sport, vrije tijd en multimedia",
             opdracht="Let op het lidwoord en op de vorm van het werkwoord.",
             oefeningen=[
                 ("rij", [("tennis", "I play tennis."), ("de piano", "I play the piano."),
                          ("zwemmen", "I go swimming."), ("fietsen", "I go cycling.")],
                  "Maak er een Engelse zin van met 'I'.", WW),
                 ("kies", "Wat is 'a draw' ?",
                  ["een wedstrijd", "een gelijkspel", "een overwinning", "een ploeg"], 1),
                 ("rij", [("to download", "binnenhalen van het internet"),
                          ("to upload", "naar het internet sturen"),
                          ("to share", "delen"), ("to follow", "volgen")],
                  "Wat betekent dit?", WW),
                 ("open", "Waarom kan je 'download' en 'upload' niet door elkaar gebruiken?",
                  "'Down' is omlaag en 'up' is omhoog: downloaden is iets binnenhalen, uploaden "
                  "is iets versturen. Het zijn elkaars tegengestelde.", 3),
                 ("kort", "Wat betekent 'to post' op sociale media?",
                  "iets plaatsen of publiceren", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-woordenschat-getallen-tijd-weer-reizen-en-landen-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Woordenschat: getallen, tijd, weer, reizen en landen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoe laat is het",
             opdracht="Eerst in cijfers, dan voluit in het Engels.",
             oefeningen=[
                 ("fig", [(svg.klok(8, 15), "8.15"),
                          (svg.klok(5, 50), "5.50"),
                          (svg.klok(7, 30), "7.30")],
                  "Schrijf in cijfers hoe laat het is."),
                 ("rij", [("8.15", "a quarter past eight"), ("5.50", "ten to six"),
                          ("7.30", "half past seven")],
                  "Schrijf nu voluit in het Engels hoe laat het is. Past is erover, to is ervoor.",
                  WW),
                 ("kort", "Hoe laat is 'half past seven' in het Nederlands?", "half acht", W),
                 ("waar", "'Noon' is twaalf uur 's middags en 'midnight' twaalf uur 's nachts.",
                  True),
                 ("open", "Een afspraak staat op '7 p.m.' en jij komt om zeven uur 's ochtends. "
                          "Wat ging er mis?",
                  "P.m. is na de middag, dus de afspraak was om zeven uur 's avonds. A.m. is "
                  "v&#243;&#243;r de middag.", 3),
             ]),

        dict(kop="Dagen, maanden en getallen",
             opdracht="Schrijf je antwoord in het Engels, met hoofdletter waar het hoort.",
             oefeningen=[
                 ("rij", [("woensdag", "Wednesday"), ("donderdag", "Thursday"),
                          ("februari", "February"), ("augustus", "August"),
                          ("de herfst (Brits)", "autumn")],
                  "Hoe schrijf je dat in het Engels?", WW),
                 ("rij", [("5", "fifth"), ("9", "ninth"), ("12", "twelfth"), ("20", "twentieth")],
                  "Schrijf het rangtelwoord.", W),
                 ("rij", [("eieren", "a few eggs"), ("melk", "a little milk"),
                          ("boeken", "many books"), ("water", "much water")],
                  "Vul aan met a few, a little, many of much.", WW),
                 ("kort", "Hoeveel is 'a dozen' ?", "twaalf", W),
                 ("waar", "Dagen en maanden schrijf je in het Engels met een kleine letter.",
                  False),
             ]),

        dict(kop="Het weer",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("bewolkt", "cloudy"), ("winderig", "windy"), ("mistig", "foggy"),
                          ("ijskoud", "freezing"), ("een bui", "a shower")],
                  "Hoe zeg je dat in het Engels?", WW),
                 ("kort", "Vul aan: 'Look outside, it ___ ___.' (het regent nu)",
                  "is raining", W),
                 ("open", "Wat is het verschil tussen 'it often rains here' en 'it is raining' ?",
                  "Het eerste is een gewoonte: het regent hier vaak. Het tweede gebeurt op dit "
                  "moment.", 3),
             ]),

        dict(kop="Reizen en landen",
             opdracht="Schrijf het Engelse woord of de betekenis.",
             oefeningen=[
                 ("rij", [("met de trein", "by train"), ("met de fiets", "by bike"),
                          ("te voet", "on foot")],
                  "Hoe zeg je dat in het Engels?", W),
                 ("rij", [("a return ticket", "een ticket heen en terug"),
                          ("a single ticket", "een enkele reis"),
                          ("a boarding pass", "een instapkaart"),
                          ("luggage", "bagage"), ("a platform", "een perron"),
                          ("delayed", "vertraagd")],
                  "Wat betekent dit?", WW),
                 ("open", "Schrijf in het Engels hoe je aan een onbekende de weg vraagt naar het "
                          "museum, en geef daarna een antwoord van &#233;&#233;n zin.",
                  "Bijvoorbeeld: &#8222;Excuse me, how do I get to the museum?&#8221; &#8212; "
                  "&#8222;Go straight on and turn left at the church.&#8221;", 5),
                 ("rij", [("Belgium", "Belgian"), ("France", "French"), ("Spain", "Spanish")],
                  "Welke nationaliteit hoort hierbij?", W),
                 ("kort", "Wat zegt een Amerikaan in plaats van 'holiday' ?", "vacation", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-grammatica-naamwoorden-lidwoorden-en-voornaamwoorden-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Grammatica: naamwoorden, lidwoorden en voornaamwoorden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het meervoud",
             opdracht="Schrijf het meervoud.",
             oefeningen=[
                 ("rij", [("a dish", "dishes"), ("a bus", "buses"), ("a city", "cities"),
                          ("a day", "days"), ("a leaf", "leaves"), ("a wife", "wives"),
                          ("a woman", "women"), ("a mouse", "mice")],
                  "Schrijf het meervoud.", W),
                 ("waar", "'Advice' en 'information' krijgen in het meervoud een -s.", False),
                 ("kort", "Hoe zeg je in het Engels 'een goede raad' ?",
                  "a piece of advice", WW),
             ]),

        dict(kop="A, an of the",
             opdracht="Vul het juiste lidwoord in, of schrijf een streepje als er geen hoort.",
             oefeningen=[
                 ("rij", [("___ apple", "an"), ("___ hour", "an"), ("___ university", "a"),
                          ("___ elephant", "an"), ("___ teacher", "a")],
                  "A of an?", W),
                 ("open", "Waarom is het 'an hour' maar 'a university' ?",
                  "Het gaat om de klank en niet om de letter: de h van hour zwijgt, en "
                  "university begint met een joe-klank.", 3),
                 ("kort", "Vertaal: 'Zij is lerares.'", "She is a teacher.", WW),
             ]),

        dict(kop="Dit, dat, mijn, welk",
             opdracht="Vul in of verbeter.",
             oefeningen=[
                 ("rij", [("___ book here is mine.", "This"), ("___ books over there are new.",
                                                               "Those"),
                          ("___ bag is this?", "Whose"), ("___ is your favourite subject?",
                                                          "What")],
                  "Vul in: this, that, these, those, whose of what.", W),
                 ("open", "Wanneer gebruik je 'which' en wanneer 'what' ?",
                  "'Which' als er een beperkte keuze is, bijvoorbeeld 'Which colour, red or "
                  "blue?'. 'What' als de keuze open is, bijvoorbeeld 'What is your name?'.", 4),
                 ("rij", [("The dog wagged ___ tail.", "its"), ("___ raining again.", "It's")],
                  "Its of it's?", W),
             ]),

        dict(kop="Voornaamwoorden en vergelijken",
             opdracht="Vul in of schrijf de juiste vorm.",
             oefeningen=[
                 ("rij", [("I", "me / mine"), ("he", "him / his"), ("she", "her / hers"),
                          ("we", "us / ours"), ("they", "them / theirs")],
                  "Schrijf de voorwerpsvorm en het bezittelijk voornaamwoord.", WW),
                 ("kies", "Welke zin is juist?",
                  ["Tom helped I.", "Tom helped me.", "Tom helped mine.", "Tom helped my."], 1),
                 ("rij", [("big", "bigger / the biggest"), ("easy", "easier / the easiest"),
                          ("expensive", "more expensive / the most expensive"),
                          ("good", "better / the best"), ("bad", "worse / the worst")],
                  "Schrijf de comparative en de superlative.", WW),
                 ("waar", "'More better' is de juiste vergrotende trap van 'good'.", False),
                 ("kort", "Vul aan: 'She is as tall ___ her brother.'", "as", W),
             ]),

        dict(kop="Voorzetsels",
             opdracht="Vul at, on of in aan.",
             oefeningen=[
                 ("rij", [("___ nine o'clock", "at"), ("___ Monday", "on"), ("___ May", "in"),
                          ("___ 2027", "in"), ("___ the third of May", "on")],
                  "At, on of in?", W),
                 ("kort", "Vul aan: 'The cat is ___ the table.' (op)", "on", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-grammatica-werkwoorden-tijden-en-zinsbouw-spark"] = dict(
    vak="Engels", niveau=SPARK, titel="Grammatica: werkwoorden, tijden en zinsbouw",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De present simple",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("rij", [("I ___ (to work)", "work"), ("she ___ (to work)", "works"),
                          ("he ___ (to go)", "goes"), ("they ___ (to live)", "live"),
                          ("it ___ (to cost)", "costs")],
                  "Schrijf de persoonsvorm.", W),
                 ("kies", "Welke zin is juist?",
                  ["Does she lives in Ghent?", "Does she live in Ghent?",
                   "Do she live in Ghent?", "Does she living in Ghent?"], 1),
                 ("kort", "Verbeter: 'He doesn't likes tea.'", "He doesn't like tea.", WW),
                 ("open", "Waarom is het 'The books on the table are mine' en niet 'is mine'?",
                  "Omdat de persoonsvorm het onderwerp volgt, en dat is 'the books', een "
                  "meervoud. 'The table' staat er alleen toevallig vlak voor.", 4),
             ]),

        dict(kop="Simple of continuous",
             opdracht="Vul de juiste tijd in en leg bij de laatste vraag uit waarom.",
             oefeningen=[
                 ("rij", [("Look, it ___ (to rain)!", "is raining"),
                          ("She ___ (to read) every evening.", "reads"),
                          ("I ___ (to write) a letter right now.", "am writing"),
                          ("We ___ (to go) to school by bike.", "go")],
                  "Present simple of present continuous?", WW),
                 ("waar", "Je zegt 'I am knowing the answer'.", False),
                 ("open", "Wanneer gebruik je de present continuous?",
                  "Voor iets dat op dit moment bezig is. Voor een gewoonte gebruik je de present "
                  "simple.", 3),
             ]),

        dict(kop="Verleden en toekomende tijd",
             opdracht="Vul de juiste vorm in.",
             oefeningen=[
                 ("rij", [("to see", "saw"), ("to take", "took"), ("to bring", "brought"),
                          ("to think", "thought"), ("to buy", "bought"), ("to be (I)", "was")],
                  "Schrijf de past simple.", W),
                 ("kort", "Verbeter: 'I have went to London.'", "I have gone to London.", WW),
                 ("rij", [("ago", "past simple"), ("yesterday", "past simple"),
                          ("last week", "past simple"), ("tomorrow", "future simple, met will")],
                  "Welke tijd kondigt dit signaalwoord aan?", WW),
                 ("kort", "Vul aan: 'She ___ ___ fifteen in June.' (zij wordt)", "will be", W),
                 ("waar", "Na 'will' komt het werkwoord zonder 'to'.", True),
             ]),

        dict(kop="Soorten zinnen",
             opdracht="Schrijf de zinssoort, of maak de gevraagde zin.",
             oefeningen=[
                 ("rij", [("Close the door, please.", "bevelend"),
                          ("What a beautiful day!", "uitroepend"),
                          ("Do you like coffee?", "vragend"),
                          ("My sister lives in Antwerp.", "mededelend"),
                          ("I don't like fish.", "ontkennend")],
                  "Welke zinssoort is dit?", WW),
                 ("open", "Waarom heeft een bevelende zin geen onderwerp?",
                  "Omdat je rechtstreeks tegen iemand spreekt: het werkwoord staat vooraan en "
                  "'you' is vanzelfsprekend.", 3),
                 ("kort", "Maak ontkennend: 'They are happy.'", "They are not happy.", WW),
             ]),

        dict(kop="Enkelvoudig of samengesteld",
             opdracht="Tel de persoonsvormen.",
             oefeningen=[
                 ("rij", [("The dog barked.", "enkelvoudig"),
                          ("He was tired, so he went to bed early.", "samengesteld"),
                          ("When I came home, my sister was cooking.", "samengesteld"),
                          ("She walked to the station.", "enkelvoudig")],
                  "Enkelvoudig of samengesteld?", WW),
                 ("rij", [("I was tired, ___ I went to bed early.", "so"),
                          ("I stayed at home ___ it was raining.", "because"),
                          ("___ I came home, the door was open.", "When")],
                  "Vul het juiste voegwoord in.", WW),
                 ("kies", "Welk woord is g&#233;&#233;n voegwoord?",
                  ["and", "but", "very", "because"], 2),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        print("  ", naam)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-engelse-tekst-lezen-spark"] = dict(
    reeksen=[
        dict(aanpak="Lees de tekst eerst één keer helemaal, zonder te stoppen bij woorden die je niet "
                    "kent. Pas daarna lees je met de vragen ernaast.",
             waarom=[]),
        dict(aanpak="De antwoorden staan in de tekst. Zoek de zin, en schrijf in het Nederlands wat er "
                    "staat; je hoeft de tekst niet woord voor woord te vertalen.",
             waarom=[None, None, None, None, None, None]),
        dict(aanpak="Raad een onbekend woord eerst uit de zin eromheen: wat zou er logisch kunnen "
                    "staan? Zoek het pas op als je er echt niet uit komt.",
             waarom=[
                 None,
                 "It verwijst terug naar iets wat er net stond. Zoek dus naar het laatste ding waar de "
                 "zin ervoor over ging.",
                 "One in five is één op vijf. Twintig van de honderd, dus twintig procent.",
                 "Pas op met valse vrienden: eventually betekent uiteindelijk en niet eventueel, actually "
                 "betekent eigenlijk en niet actueel.",
             ]),
        dict(aanpak="Een leesstrategie is kiezen hoe je leest. Zoek je één gegeven, dan scan je; wil je "
                    "de hoofdgedachte, dan lees je de inleiding en het slot.",
             waarom=[
                 None,
                 None,
                 "A.m. komt van ante meridiem, vóór de middag; p.m. van post meridiem, ná de middag. "
                 "7 a.m. is zeven uur 's ochtends.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-signaalwoorden-en-verwijswoorden-spark"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elke tekst af wat hij van je wil: iets laten doen, iets laten weten, "
                    "je overtuigen, of je meenemen in een verhaal.",
             waarom=[
                 "Let op de werkwoordsvorm: een gebiedende wijs (peel, boil) wijst op een instructie, "
                 "I think op een mening, en een verleden tijd met personages op een verhaal.",
                 None,
                 None,
             ]),
        dict(aanpak="Het communicatiemodel is drie vragen: wie zegt het, waarom, en tegen wie? Het "
                    "antwoord op die drie staat zelden letterlijk in de tekst, je leidt het af.",
             waarom=[
                 None,
                 None,
                 "Het aantal bladzijden zegt niets over zender, doel of ontvanger. Dat is een kenmerk "
                 "van het boek, niet van de boodschap.",
             ]),
        dict(aanpak="Een signaalwoord zegt wat er gaat komen. Leer ze per verband: volgorde, reden, "
                    "gevolg, tegenstelling, voorbeeld, toevoeging.",
             waarom=[
                 None,
                 "Because geeft de reden, so het gevolg. In Engels staat because vóór de oorzaak en so "
                 "vóór het gevolg, net zoals omdat en dus.",
                 None,
                 "Very versterkt alleen een woord; het legt geen verband tussen twee stukken tekst. Dat "
                 "is wat een signaalwoord wel doet.",
             ]),
        dict(aanpak="Zoek bij een verwijswoord altijd terug: naar welk woord of welke zin verwijst het? "
                    "Meestal staat dat vlak ervoor.",
             waarom=[
                 "He en she zijn voor personen, it voor dingen en dieren, they voor meervoud, en there "
                 "verwijst naar een plaats.",
                 None,
                 None,
             ]),
        dict(aanpak="Veel Engelse woorden kan je zelf uitrekenen: zoek het woord dat erin zit en kijk "
                    "wat het voorvoegsel of achtervoegsel ermee doet.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-berichten-uitnodigingen-en-mails-spark"] = dict(
    reeksen=[
        dict(aanpak="Vaste zinnen leer je als één geheel, niet woord per woord. Zeg ze hardop, dan "
                    "blijven ze beter hangen.",
             waarom=[None, None, None]),
        dict(aanpak="Kijk eerst wie de ontvanger is. Daaruit volgt de aanhef, de slotgroet én de "
                    "woordkeuze; die drie horen bij elkaar te passen.",
             waarom=[
                 None,
                 "Beleefd vragen doe je in het Engels met could, would of please. Een gebiedende wijs "
                 "zonder please klinkt er harder dan in het Nederlands.",
                 "Mate is Brits vriendentaal, zoals maat of gast. In een formele mail schrijf je Dear "
                 "Mr Jones of Dear Sir or Madam.",
             ]),
        dict(aanpak="Vink af wat gevraagd wordt (wat, wanneer, waar, hoe laat) voor je begint, en "
                    "schrijf dan pas. Een korte juiste zin is beter dan een lange met fouten.",
             waarom=[None, None, None]),
        dict(aanpak="Nakijken is deel van de opdracht. Lees je tekst nog één keer met de opgave "
                    "ernaast, niet alleen op spelling.",
             waarom=[
                 None,
                 None,
                 None,
                 "Let op de klassiekers: I krijgt altijd een hoofdletter, net als landen en talen "
                 "(London, English).",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-engelstalige-landen-en-literaire-teksten-spark"] = dict(
    reeksen=[
        dict(aanpak="Een nationaliteit krijgt in het Engels altijd een hoofdletter, ook midden in de "
                    "zin. Let op de uitgangen: -ish, -ian, -ese.",
             waarom=[
                 None,
                 None,
                 None,
                 "Ierland betaalt met de euro. Het pond is van het Verenigd Koninkrijk, waar "
                 "Noord-Ierland wel bij hoort.",
             ]),
        dict(aanpak="Let bij elk verschil op wat het voor jou als lezer betekent: een datum, een maat "
                    "of een verdieping kan iets anders zijn dan je denkt.",
             waarom=[
                 None,
                 "Australië ligt op het zuidelijk halfrond, dus de seizoenen liggen omgekeerd. Kerstmis "
                 "valt er midden in de zomervakantie.",
                 None,
                 None,
             ]),
        dict(aanpak="Brits en Amerikaans verschillen in woorden én in spelling. Beide zijn juist; "
                    "houd binnen één tekst wel één van de twee aan.",
             waarom=[
                 None,
                 None,
                 "Color is de gewone Amerikaanse spelling. Fout is het pas als je in dezelfde tekst door "
                 "elkaar colour en color schrijft.",
             ]),
        dict(aanpak="Bij een literaire tekst wordt niet naar één juist antwoord gevraagd maar naar wat "
                    "jij erin leest. Zeg er daarom altijd bij waaruit je het haalt.",
             waarom=[
                 None,
                 None,
                 "Geloofwaardig betekent: het past bij wat er al gebeurd is in het verhaal. Een einde "
                 "dat uit het niets komt, telt niet.",
                 "Een schoolrapport wil enkel iets meedelen. Een gedicht, een lied en een kortverhaal "
                 "gebruiken taal ook om iets te laten voelen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-woordenschat-mensen-familie-gevoelens-en-gezondheid-spark"] = dict(
    reeksen=[
        dict(aanpak="Teken bij familiewoorden gerust een stamboompje. Je ziet dan meteen wie langs "
                    "welke kant hoort.",
             waarom=[
                 None,
                 None,
                 None,
                 "Hou die twee uit elkaar: cousin gaat opzij in de stamboom (het kind van je tante of "
                 "oom), nephew en niece gaan een trapje omlaag (het kind van je broer of zus).",
             ]),
        dict(aanpak="Let bij gevoelswoorden op de uitgang: -ed zegt hoe jij je voelt, -ing zegt hoe "
                    "iets ís.",
             waarom=[
                 None,
                 "I am bored betekent ik verveel me. I am boring betekent ik ben saai. Daar zit het "
                 "verschil tussen -ed en -ing.",
                 "Veel Engelse gevoelswoorden hebben een vast voorzetsel: afraid of, proud of, worried "
                 "about, good at. Leer die er meteen bij.",
                 None,
                 None,
             ]),
        dict(aanpak="Pijn zeg je in het Engels met ache of sore, niet met pain. En let op de "
                    "onregelmatige meervouden van lichaamsdelen.",
             waarom=[
                 None,
                 None,
                 None,
                 "Hair is in het Engels een ontelbaar woord, net als water of bread. Daarom staat er is "
                 "en niet are.",
                 "Once, twice, three times: bij twee keer bestaat er een eigen woord, vanaf drie keer "
                 "gebruik je times.",
             ]),
        dict(aanpak="De woorden van een formulier leer je als groep, want je vindt ze op elk formulier "
                    "terug.",
             waarom=[
                 "Surname is je achternaam, al lijkt sur op het Franse sur. First name en surname staan "
                 "vaak in die volgorde op een formulier.",
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-woordenschat-eten-wonen-kleding-en-dagelijkse-dingen-spark"] = dict(
    reeksen=[
        dict(aanpak="Let bij eten op twee dingen: de valse vrienden, en het feit dat je sommige "
                    "woorden niet kan tellen (water, rijst, brood).",
             waarom=[
                 None,
                 None,
                 None,
                 "Een ontelbaar woord tel je met een maat ervoor: a slice of, a glass of, a bowl of. "
                 "Two breads bestaat niet.",
                 None,
                 None,
             ]),
        dict(aanpak="Woonwoorden zijn vaak Brits-Amerikaans verschillend. Leer de Britse vorm, want de "
                    "examens werken met Brits Engels.",
             waarom=[None, None, None]),
        dict(aanpak="Let op de kledingstukken die in het Engels altijd meervoud zijn: trousers, jeans, "
                    "glasses, shorts.",
             waarom=[
                 None,
                 "Trousers bestaat alleen in het meervoud, net als glasses en jeans. Dus are en niet "
                 "is. Wil je er één bedoelen, dan schrijf je a pair of trousers.",
                 None,
                 "Aanhebben is to wear. To put on is aantrekken, de beweging zelf.",
             ]),
        dict(aanpak="Een winkel eindigt in het Brits vaak op 's: a baker's, a butcher's. Het is "
                    "eigenlijk de winkel ván de bakker.",
             waarom=[None, None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-woordenschat-school-beroepen-sport-en-vrije-tijd-spark"] = dict(
    reeksen=[
        dict(aanpak="Instructietaal is de taal van de opgave zelf. Ken je die niet, dan verlies je "
                    "punten op een oefening die je eigenlijk kon.",
             waarom=[None, None, None]),
        dict(aanpak="Schoolwoorden verschillen tussen Brits en Amerikaans. Leer de Britse vorm, en let "
                    "op de woorden die geen meervoud hebben.",
             waarom=[
                 None,
                 None,
                 "Homework, information en advice zijn ontelbaar in het Engels: nooit een -s. Wil je er "
                 "één bedoelen, dan schrijf je a piece of homework.",
                 "Getallen van 21 tot 99 krijgen een koppelteken: twenty-four, thirty-seven.",
             ]),
        dict(aanpak="Een beroep krijgt in het Engels altijd een lidwoord: she is a nurse, niet she is "
                    "nurse.",
             waarom=[None, None]),
        dict(aanpak="Onthoud de drie vaste combinaties: play bij een balsport of een instrument, go bij "
                    "een sport op -ing, do bij de rest.",
             waarom=[
                 "Bij een instrument staat er the (I play the piano), bij een sport niet (I play "
                 "tennis).",
                 None,
                 None,
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-woordenschat-getallen-tijd-weer-reizen-en-landen-spark"] = dict(
    reeksen=[
        dict(aanpak="In het Engels zeg je het uur vanuit het hele uur: past als de wijzer erover is, to "
                    "als hij er nog voor staat.",
             waarom=[
                 None,
                 None,
                 "Opletten: half past seven is half acht, niet half zeven. De Engelsen tellen vanaf het "
                 "uur dat geweest is.",
                 None,
                 None,
             ]),
        dict(aanpak="Dagen, maanden en nationaliteiten krijgen in het Engels altijd een hoofdletter. "
                    "Rangtelwoorden eindigen op -th, op een handvol na.",
             waarom=[
                 None,
                 "Drie onregelmatige: first, second, third. Daarna -th, met de spellingsknikken fifth, "
                 "ninth, twelfth en twentieth.",
                 "A few en many horen bij wat je kan tellen, a little en much bij wat je niet kan "
                 "tellen.",
                 None,
                 None,
             ]),
        dict(aanpak="Weerwoorden eindigen vaak op -y: rainy, windy, cloudy, foggy. Let op of de vraag "
                    "naar nu vraagt of naar gewoonlijk.",
             waarom=[None, None, None]),
        dict(aanpak="Vervoermiddelen gaan met by, behalve te voet: on foot. Leer de stationswoorden als "
                    "groep, je vindt ze op elk bord terug.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-grammatica-naamwoorden-lidwoorden-en-voornaamwoorden-spark"] = dict(
    reeksen=[
        dict(aanpak="Het meervoud is meestal -s, maar let op vier groepen: woorden op s/sh/ch krijgen "
                    "-es, een medeklinker plus y wordt -ies, f wordt ves, en een handvol is "
                    "onregelmatig.",
             waarom=[
                 None,
                 None,
                 "Advice, information, news en furniture zijn ontelbaar: nooit een -s. Eén ervan noem je "
                 "met a piece of.",
             ]),
        dict(aanpak="A of an kies je op de klánk van het volgende woord, niet op de letter. Spreek het "
                    "woord hardop uit en luister.",
             waarom=[
                 None,
                 None,
                 "Een beroep krijgt in het Engels altijd a of an: she is a teacher. Zonder lidwoord "
                 "klinkt het fout.",
             ]),
        dict(aanpak="This en these zijn dichtbij, that en those veraf. En denk aan de apostrof: it's is "
                    "it is, its is van hem of haar.",
             waarom=[
                 None,
                 None,
                 "Een ezelsbruggetje: kan je het uitspreken als it is, dan schrijf je it's. Anders its, "
                 "zonder apostrof.",
             ]),
        dict(aanpak="Een voornaamwoord verandert van vorm naargelang het vooraan of achteraan de zin "
                    "staat. En vergelijken doe je met -er bij korte woorden, met more bij lange.",
             waarom=[
                 None,
                 None,
                 "Tot twee lettergrepen: -er en -est. Langer: more en the most. Good, bad en far zijn "
                 "onregelmatig.",
                 "Good wordt better, en dan staat more er nooit meer bij. More better is dubbelop.",
                 "As … as zegt dat twee dingen gelijk zijn. Than gebruik je als er een verschil is: "
                 "taller than her brother.",
             ]),
        dict(aanpak="De tijdsvoorzetsels gaan van groot naar klein: in voor een jaar of een maand, on "
                    "voor een dag of een datum, at voor een uur.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-grammatica-werkwoorden-tijden-en-zinsbouw-spark"] = dict(
    reeksen=[
        dict(aanpak="Zoek eerst het onderwerp. Is het he, she of it, dan komt er een -s bij. Dat ene "
                    "lettertje is de meest gemaakte fout van heel het jaar.",
             waarom=[
                 None,
                 "Die -s zit al in does. Daarom staat het andere werkwoord in de grondvorm: does she "
                 "live, niet does she lives.",
                 None,
                 None,
             ]),
        dict(aanpak="Vraag je af of het nú bezig is (continuous) of altijd zo is (simple). Een "
                    "signaalwoord als now, look of at the moment wijst op continuous.",
             waarom=[
                 None,
                 "Werkwoorden van weten, vinden en voelen (know, like, want, believe) staan nooit in de "
                 "continuous. Je zegt I know the answer.",
                 None,
             ]),
        dict(aanpak="De onregelmatige werkwoorden moet je gewoon kennen; oefen ze in drie kolommen. En "
                    "let op het verschil tussen de past simple en de voltooide tijd.",
             waarom=[
                 None,
                 "Na have komt de derde vorm, het voltooid deelwoord: gone. Went is de tweede vorm en "
                 "staat alleen, zonder have.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Je herkent de zinssoort aan wat de zin doet en aan het leesteken: een punt, een "
                    "vraagteken of een uitroepteken.",
             waarom=[None, None, None]),
        dict(aanpak="Tel de persoonsvormen: één is enkelvoudig, meer dan één is samengesteld. Een "
                    "voegwoord verbindt de deelzinnen.",
             waarom=[
                 None,
                 None,
                 "Very versterkt alleen een woord, het verbindt geen twee deelzinnen. And, but, because "
                 "en so doen dat wel.",
             ]),
    ],
)
