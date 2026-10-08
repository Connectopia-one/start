# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Engels 🌍 Beyond dubbele finaliteit.

De fiches Engels 1 en Engels 2 van deze graad staan op ERK A2+, met concrete
woordenschat uit het dagelijkse leven. Deze bundels hergebruiken daarom de
reeksen van `maak_oefeningen_engels_beyond.py` die op dat niveau bruikbaar
zijn, en zetten er oefeningen bij op de woordenschat van deze fiche.

Wat de fiche niet vraagt, staat er ook niet in, ook niet als oefening: de
gerund, de semi-auxiliaries, de indirecte rede, de passieve vorm en de past
perfect.

Eén bundel per thema, niet per deel. De sleutels dragen het voorvoegsel
"oefenbundel-" en het achtervoegsel "-beyond-dubbele-finaliteit".
"""
import copy
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel
import maak_oefeningen_engels_beyond as door

VAK = "Engels"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
NIVEAU = "-beyond-dubbele-finaliteit"
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

HOE_LEZEN = door.HOE_LEZEN

OEFENBUNDELS = {}


def reeks(slug, kop, weg=()):
    for r in door.OEFENBUNDELS["oefenbundel-" + slug + "-beyond"]["reeksen"]:
        if r["kop"] == kop:
            r = copy.deepcopy(r)
            if weg:
                r["oefeningen"] = [o for i, o in enumerate(r["oefeningen"], 1) if i not in weg]
            return r
    raise KeyError(f"{slug}: {kop}")


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("een-engelse-tekst-lezen",
    titel="Een Engelse tekst lezen",
    onder="Een tekst en {aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE_LEZEN,
    reeksen=[
        dict(kop="The text", opdracht="Lees deze tekst. Alle vragen gaan hierover.",
             oefeningen=[
                 ("tekst",
                  "<h3 style='margin:0 0 .4em'>A shop with no prices</h3>"
                  "<p>In a small town near Leeds, a shop opened last March where nothing has a "
                  "price tag. Customers take what they need and pay what they can. The owner, "
                  "Tom Whelan, used to work in a supermarket.</p>"
                  "<p>„Every evening we threw away food that was still fine”, he says. „Bread, "
                  "fruit, yoghurt. It made me angry.” Now five supermarkets give him what they "
                  "cannot sell, and he puts it on his shelves.</p>"
                  "<p>The shop is open from Tuesday to Saturday, from ten in the morning until "
                  "four. About two hundred people come every week. Some pay nothing, some pay "
                  "five pounds, and a few pay more than the food is worth.</p>"
                  "<p>„People think this is only for poor families”, Tom says. „It is not. It is "
                  "for anyone who hates waste.”</p>"),
             ]),
        dict(kop="Questions",
             opdracht="Antwoord in het Nederlands.",
             oefeningen=[
                 ("kort", "Wat is er bijzonder aan deze winkel?",
                  "er staan geen prijzen op: je betaalt wat je kan", WL),
                 ("kort", "Waar werkte Tom Whelan vroeger?", "in een supermarkt", WW),
                 ("kort", "Waarom begon hij deze winkel?",
                  "er werd elke avond eten weggegooid dat nog goed was", WL),
                 ("kort", "Hoeveel supermarkten leveren hem voedsel?", "vijf", W),
                 ("kort", "Op welke dagen en uren is de winkel open?",
                  "van dinsdag tot zaterdag, van tien tot vier", WL),
                 ("kort", "Hoeveel mensen komen er per week?", "ongeveer tweehonderd", W),
                 ("waar", "Volgens Tom is de winkel alleen voor arme gezinnen.", False),
             ]),
        dict(kop="Words from the text",
             opdracht="Zoek het Engelse woord in de tekst.",
             oefeningen=[
                 ("rij", [("een prijskaartje", "a price tag"), ("een klant", "a customer"),
                          ("de eigenaar", "the owner"), ("een rek", "a shelf"),
                          ("verspilling", "waste"), ("weggooien", "to throw away")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat is het meervoud van <em>shelf</em>?", "shelves", W),
             ]),
        reeks("een-engelse-tekst-analyseren", "Reading between the lines", weg=(1,)),
    ])

# ============================================================
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    reeksen=[
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Which text type?"),
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Fact or opinion?"),
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Register", weg=(4,)),
        reeks("tekstsoorten-en-de-bedoeling-van-een-tekst", "Linking words", weg=(6,)),
        dict(kop="Where would you read it?",
             opdracht="Schrijf waar je deze tekst tegenkomt.",
             oefeningen=[
                 ("rij", [("Mix the flour with 200 ml of milk.", "in a recipe / cookbook"),
                          ("Trains to Leeds are delayed by 20 minutes.", "on a station screen / an app"),
                          ("Buy one, get one free — this week only!", "in an advertisement"),
                          ("Chapter two: the house on the hill", "in a novel"),
                          ("Please keep this door closed.", "on a sign")],
                  "Waar lees je dit?", WL),
             ]),
    ])

# ============================================================
zet("de-engelstalige-wereld-gewoontes-en-reizen",
    titel="De Engelstalige wereld: gewoontes en reizen",
    reeksen=[
        dict(kop="The English-speaking world",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de hoofdstad van Schotland", "Edinburgh"),
                          ("de hoofdstad van Ierland", "Dublin"),
                          ("de hoofdstad van Australië", "Canberra"),
                          ("de hoofdstad van Canada", "Ottawa")],
                  "Welke stad?", WW),
                 ("kort", "Uit welke vier delen bestaat het Verenigd Koninkrijk?",
                  "Engeland, Schotland, Wales en Noord-Ierland", WL),
                 ("kort", "Met welke munt betaal je in het Verenigd Koninkrijk?",
                  "the pound (sterling)", WW),
                 ("waar", "In Ierland betaal je met de euro.", True),
             ]),
        dict(kop="Customs",
             opdracht="Vertaal of leg uit.",
             oefeningen=[
                 ("rij", [("Bonfire Night", "5 november, vuurwerk en vreugdevuren"),
                          ("Boxing Day", "26 december, de dag na Kerstmis"),
                          ("Thanksgiving", "een Amerikaanse feestdag in november"),
                          ("a bank holiday", "een officiële vrije dag")],
                  "Wat is het?", WL),
                 ("kort", "Aan welke kant van de weg rijdt men in het Verenigd Koninkrijk?",
                  "links", W),
                 ("open", "Noem twee dingen die in Britse beleefdheid opvallen.",
                  "Men zegt heel vaak please, thank you en sorry, men schuift netjes aan in de "
                  "rij, men stelt vragen voorzichtig (<em>would you mind…?</em>) en men praat "
                  "graag over het weer.", 3),
             ]),
        dict(kop="Travelling",
             opdracht="Vertaal.",
             oefeningen=[
                 ("rij", [("een heen-en-terugticket", "a return ticket"),
                          ("een enkele reis", "a single ticket"),
                          ("de bagage", "the luggage"), ("instappen", "to board"),
                          ("vertraging", "a delay"), ("een jeugdherberg", "a youth hostel")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... a room", "book"), ("to ... in at the hotel", "check"),
                          ("to ... the train", "catch"), ("to ... a taxi", "take")],
                  "Welk werkwoord?", W),
             ]),
        dict(kop="At the counter",
             opdracht="Schrijf wat je zegt, in het Engels.",
             oefeningen=[
                 ("open", "Je wil een retourtje naar York voor vandaag.",
                  "A return to York for today, please. / Could I have a day return to York, "
                  "please?", 2),
                 ("open", "Je vraagt hoe laat de volgende trein vertrekt.",
                  "What time does the next train leave? / When is the next train?", 2),
                 ("open", "Je zegt dat je kamer gereserveerd is op jouw naam.",
                  "I have a reservation under the name of ... / I have booked a room in the "
                  "name of ...", 2),
                 ("open", "Je vraagt vriendelijk of ze trager kunnen spreken.",
                  "Could you speak a bit more slowly, please? / Sorry, could you repeat that, "
                  "please?", 2),
             ]),
    ])

# ============================================================
zet("schrijven-spreken-en-je-beleving-bij-een-tekst",
    titel="Schrijven, spreken en je beleving bij een tekst",
    reeksen=[
        dict(kop="An email",
             opdracht="Vul het juiste stuk in.",
             oefeningen=[
                 ("rij", [("de aanhef als je de naam niet kent", "Dear Sir or Madam,"),
                          ("de aanhef als je de naam wel kent", "Dear Mr Jones,"),
                          ("het slot bij de eerste", "Yours faithfully,"),
                          ("het slot bij de tweede", "Yours sincerely,"),
                          ("een informeel slot", "Best wishes, / See you soon,")],
                  "Wat schrijf je?", WL),
                 ("open", "Schrijf de eerste zin van een mail waarin je een kamer reserveert "
                          "voor twee nachten in juli.",
                  "I am writing to book a double room for two nights in July. / I would like to "
                  "reserve a room for two nights in July.", 2),
             ]),
        dict(kop="Useful phrases",
             opdracht="Schrijf de Engelse uitdrukking.",
             oefeningen=[
                 ("rij", [("Mag ik iets vragen?", "Can I ask you something?"),
                          ("Het spijt me, ik begrijp het niet.", "Sorry, I do not understand."),
                          ("Kunt u dat herhalen?", "Could you repeat that, please?"),
                          ("Ik ben het ermee eens.", "I agree."),
                          ("Ik ben het er niet mee eens.", "I do not agree. / I disagree."),
                          ("Wat vind jij ervan?", "What do you think?")],
                  "Welke Engelse zin?", WL),
             ]),
        dict(kop="Giving your opinion",
             opdracht="Schrijf in het Engels, met een reden erbij.",
             oefeningen=[
                 ("open", "Zeg wat je van het boek of de film vond die je het laatst zag. "
                          "Gebruik <em>I thought</em> en <em>because</em>.",
                  "Een eigen antwoord van twee zinnen met een mening en een reden, "
                  "bijvoorbeeld: I thought the film was too long, because nothing happened in "
                  "the first hour.", 3),
                 ("open", "Raad een vriend een boek aan. Gebruik <em>you should</em> en "
                          "<em>if you like</em>.",
                  "Een eigen antwoord, bijvoorbeeld: You should read this one if you like "
                  "stories about the sea. It is short and the ending is a surprise.", 3),
                 ("rij", [("In my opinion, ...", "naar mijn mening"),
                          ("I would rather ...", "ik zou liever"),
                          ("On the one hand ... on the other hand ...", "enerzijds, anderzijds"),
                          ("To be honest, ...", "eerlijk gezegd")],
                  "Wat betekent het?", WL),
             ]),
        dict(kop="Spelling and punctuation",
             opdracht="Verbeter de fout.",
             oefeningen=[
                 ("rij", [("i live in belgium", "I live in Belgium."),
                          ("Their going to be late.", "They're going to be late."),
                          ("Its raining again.", "It's raining again."),
                          ("She dont know.", "She doesn't know."),
                          ("on monday we have english", "On Monday we have English.")],
                  "Hoe hoort het?", WL),
                 ("kort", "Waarom krijgen <em>Monday</em> en <em>English</em> een hoofdletter?",
                  "dagen, maanden, talen en landen krijgen er altijd een in het Engels", WL),
             ]),
    ])


# ============================================================
zet("woordvelden-dagelijks-leven-eten-en-wonen",
    titel="Woordvelden: dagelijks leven, eten en wonen",
    reeksen=[
        reeks("woordvelden-wonen-eten-en-vrije-tijd", "At home"),
        reeks("woordvelden-wonen-eten-en-vrije-tijd", "Food"),
        reeks("woordvelden-wonen-eten-en-vrije-tijd", "Phrasal verbs"),
        dict(kop="Family and daily life",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een familielid", "a relative"), ("een neef of nicht", "a cousin"),
                          ("uitslapen", "to have a lie-in"), ("het toilet", "the loo / toilet"),
                          ("de verwarmingsketel", "the boiler"),
                          ("de wasmachine", "the washing machine")],
                  "Welk Engels woord?", WW),
                 ("rij", [("to ... the bed", "make"), ("to ... the bin out", "take"),
                          ("to ... the dishes", "do"), ("to ... the dog", "walk")],
                  "Welk werkwoord?", W),
                 ("open", "Schrijf drie Engelse zinnen over je ochtend, met <em>first</em>, "
                          "<em>then</em> en <em>after that</em>.",
                  "Een eigen antwoord met drie volledige zinnen, bijvoorbeeld: First I get up "
                  "at half past six. Then I have breakfast with my sister. After that I cycle "
                  "to school.", 4),
             ]),
    ])

# ============================================================
zet("woordvelden-gezondheid-natuur-en-duurzaamheid",
    titel="Woordvelden: gezondheid, natuur en duurzaamheid",
    reeksen=[
        reeks("woordvelden-gezondheid-natuur-en-duurzaamheid", "At the doctor's"),
        reeks("woordvelden-gezondheid-natuur-en-duurzaamheid", "Nature", weg=(2,)),
        reeks("woordvelden-gezondheid-natuur-en-duurzaamheid", "Sustainability", weg=(3,)),
        dict(kop="At the chemist's",
             opdracht="Schrijf wat je zegt of wat het woord betekent.",
             oefeningen=[
                 ("rij", [("een pijnstiller", "a painkiller"), ("een zalf", "an ointment"),
                          ("hoestsiroop", "cough syrup"), ("een verband", "a bandage"),
                          ("zonnecrème", "sun cream")],
                  "Welk Engels woord?", WW),
                 ("open", "Zeg in het Engels dat je al drie dagen keelpijn hebt en vraag wat "
                          "je kan nemen.",
                  "I have had a sore throat for three days. What can I take for it?", 3),
             ]),
    ])

# ============================================================
zet("woordvelden-school-werk-geld-en-verkeer",
    titel="Woordvelden: school, werk, geld en verkeer",
    reeksen=[
        reeks("woordvelden-school-werk-geld-en-verkeer", "School"),
        reeks("woordvelden-school-werk-geld-en-verkeer", "Work", weg=(3,)),
        reeks("woordvelden-school-werk-geld-en-verkeer", "Money"),
        reeks("woordvelden-school-werk-geld-en-verkeer", "On the road"),
        dict(kop="In a shop",
             opdracht="Schrijf de Engelse zin.",
             oefeningen=[
                 ("rij", [("Hoeveel kost dit?", "How much is this?"),
                          ("Mag ik dit passen?", "Can I try this on?"),
                          ("Heeft u dit in een andere maat?", "Do you have this in another size?"),
                          ("Kan ik met kaart betalen?", "Can I pay by card?"),
                          ("Mag ik een kassabon?", "Could I have a receipt, please?")],
                  "Welke Engelse zin?", WL),
             ]),
    ])

# ============================================================
zet("woordvelden-kunst-geschiedenis-en-de-samenleving",
    titel="Woordvelden: kunst, geschiedenis en de samenleving",
    reeksen=[
        reeks("woordvelden-kunst-literatuur-politiek-en-reizen", "Art and literature", weg=(2,)),
        reeks("woordvelden-kunst-literatuur-politiek-en-reizen", "Politics and society"),
        dict(kop="History",
             opdracht="Schrijf het Engelse woord.",
             oefeningen=[
                 ("rij", [("een eeuw", "a century"), ("een oorlog", "a war"),
                          ("de Middeleeuwen", "the Middle Ages"),
                          ("een koningin", "a queen"), ("een kasteel", "a castle"),
                          ("een uitvinding", "an invention")],
                  "Welk Engels woord?", WW),
                 ("kort", "Wat betekent <em>the 19th century</em> in jaartallen?",
                  "van 1801 tot 1900", WW),
             ]),
        dict(kop="At the museum",
             opdracht="Schrijf de Engelse zin of het woord.",
             oefeningen=[
                 ("rij", [("Hoeveel kost de toegang?", "How much is the entrance fee?"),
                          ("Is er een rondleiding?", "Is there a guided tour?"),
                          ("Mag ik hier foto's nemen?", "Am I allowed to take photos here?"),
                          ("Hoe laat sluit het museum?", "What time does the museum close?")],
                  "Welke Engelse zin?", WL),
                 ("rij", [("een tentoonstelling", "an exhibition"), ("een schilderij", "a painting"),
                          ("een beeld", "a statue"), ("het publiek", "the audience")],
                  "Welk Engels woord?", WW),
             ]),
    ])

# ============================================================
zet("woordvelden-wetenschap-techniek-en-taal",
    titel="Woordvelden: wetenschap, techniek en taal",
    reeksen=[
        reeks("woordvelden-wetenschap-techniek-en-taal", "Science and technology"),
        reeks("woordvelden-wetenschap-techniek-en-taal", "False friends"),
        reeks("woordvelden-wetenschap-techniek-en-taal", "British or American?"),
        dict(kop="On the computer",
             opdracht="Schrijf het Engelse woord of de zin.",
             oefeningen=[
                 ("rij", [("een bestand opslaan", "to save a file"),
                          ("een map", "a folder"), ("verwijderen", "to delete"),
                          ("een rekenblad", "a spreadsheet"),
                          ("een wachtwoord instellen", "to set a password"),
                          ("de instellingen", "the settings")],
                  "Welk Engels woord?", WW),
                 ("open", "Schrijf in het Engels dat je wachtwoord niet werkt en dat je het "
                          "wil opnieuw instellen.",
                  "My password does not work. I would like to reset it.", 2),
             ]),
    ])

# ============================================================
zet("naamwoorden-lidwoorden-en-hoeveelheden",
    titel="Naamwoorden, lidwoorden en hoeveelheden",
    reeksen=[
        reeks("naamwoorden-lidwoorden-en-hoeveelheden", "Plurals", weg=(2,)),
        reeks("naamwoorden-lidwoorden-en-hoeveelheden", "Countable or uncountable?"),
        reeks("naamwoorden-lidwoorden-en-hoeveelheden", "A, an, the or nothing?"),
        reeks("naamwoorden-lidwoorden-en-hoeveelheden", "How much, how many"),
        reeks("naamwoorden-lidwoorden-en-hoeveelheden", "The genitive"),
    ])

# ============================================================
zet("voornaamwoorden-en-betrekkelijke-bijzinnen",
    titel="Voornaamwoorden en betrekkelijke bijzinnen",
    reeksen=[
        reeks("voornaamwoorden-en-betrekkelijke-bijzinnen", "Which pronoun?"),
        reeks("voornaamwoorden-en-betrekkelijke-bijzinnen", "Relative clauses", weg=(2, 3)),
        reeks("voornaamwoorden-en-betrekkelijke-bijzinnen", "Combine the sentences", weg=(3,)),
        reeks("voornaamwoorden-en-betrekkelijke-bijzinnen", "Some, any, no"),
        dict(kop="Subject or object?",
             opdracht="Vul het juiste voornaamwoord in.",
             oefeningen=[
                 ("rij", [("... is my sister.", "She"), ("I saw ... yesterday.", "him / them"),
                          ("Give it to ... .", "me"), ("... are late.", "They"),
                          ("Between you and ... .", "me")],
                  "Welk woord?", W),
             ]),
    ])

# ============================================================
zet("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    titel="Bijvoeglijke naamwoorden, bijwoorden en voorzetsels",
    reeksen=[
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels", "Comparatives"),
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels", "Adjective or adverb?",
              weg=(3,)),
        reeks("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels", "Prepositions"),
        dict(kop="Describing people and places",
             opdracht="Schrijf het tegengestelde.",
             oefeningen=[
                 ("rij", [("cheap", "expensive"), ("crowded", "empty"), ("polite", "rude"),
                          ("safe", "dangerous"), ("early", "late"), ("boring", "exciting")],
                  "Wat is het tegengestelde?", WW),
                 ("open", "Beschrijf je eigen straat in drie Engelse zinnen, met minstens drie "
                          "bijvoeglijke naamwoorden.",
                  "Een eigen antwoord met drie volledige zinnen, bijvoorbeeld: My street is "
                  "quiet and narrow. The houses are old but well kept. There is a small shop "
                  "on the corner.", 4),
             ]),
    ])

# ============================================================
zet("de-tegenwoordige-tijden-en-de-present-perfect",
    titel="De tegenwoordige tijden en de present perfect",
    reeksen=[
        reeks("de-tegenwoordige-tijden-en-de-present-perfect", "Simple or continuous?"),
        reeks("de-tegenwoordige-tijden-en-de-present-perfect", "Present perfect"),
        dict(kop="Questions in the present",
             opdracht="Maak een vraag.",
             oefeningen=[
                 ("rij", [("She works at the bakery.", "Does she work at the bakery?"),
                          ("They are waiting outside.", "Are they waiting outside?"),
                          ("He has finished.", "Has he finished?"),
                          ("You live in Genk.", "Do you live in Genk?")],
                  "Welke vraag?", WL),
                 ("kort", "Waarom is het <em>Does she work</em> en niet <em>Does she "
                          "works</em>?", "na does gaat het werkwoord in de basisvorm", WL),
             ]),
    ])

# ============================================================
zet("de-verleden-tijden",
    titel="De verleden tijden",
    reeksen=[
        reeks("de-verleden-tijden", "Irregular verbs", weg=(2,)),
        reeks("de-verleden-tijden", "Past simple or past continuous?"),
        reeks("de-verleden-tijden", "Used to and would", weg=(2,)),
        dict(kop="Last weekend",
             opdracht="Schrijf in de past simple.",
             oefeningen=[
                 ("rij", [("I (go) to my grandmother's.", "went"),
                          ("We (eat) pizza.", "ate"), ("She (not come) with us.", "did not come"),
                          ("(you / see) the match?", "Did you see"),
                          ("It (be) very cold.", "was")],
                  "Welke vorm?", WW),
                 ("open", "Schrijf vier Engelse zinnen over je laatste weekend, in de past "
                          "simple.",
                  "Een eigen antwoord met vier volledige zinnen in de verleden tijd, "
                  "bijvoorbeeld: On Saturday I worked in the shop. In the evening we watched a "
                  "film. On Sunday I slept late. Then I did my homework.", 4),
             ]),
    ])

# ============================================================
zet("de-toekomende-tijd-en-de-modale-hulpwerkwoorden",
    titel="De toekomende tijd en de modale hulpwerkwoorden",
    reeksen=[
        reeks("de-toekomst-de-modale-hulpwerkwoorden-en-de-gerund", "Which future?"),
        reeks("de-toekomst-de-modale-hulpwerkwoorden-en-de-gerund", "Modal verbs"),
        dict(kop="Plans",
             opdracht="Schrijf in het Engels.",
             oefeningen=[
                 ("open", "Schrijf drie zinnen over je plannen voor de zomer, met <em>I am "
                          "going to</em>.",
                  "Een eigen antwoord met drie volledige zinnen, bijvoorbeeld: I am going to "
                  "work in a shop in July. I am going to visit my cousin in Spain. I am not "
                  "going to study until August.", 4),
                 ("rij", [("Je belooft iets.", "I will ..."),
                          ("Je ziet een ongeluk gebeuren.", "It is going to ..."),
                          ("Je hebt morgen om drie uur de tandarts.",
                           "I am seeing the dentist at three tomorrow.")],
                  "Welke vorm gebruik je?", WL),
             ]),
    ])

# ============================================================
zet("zinsbouw-zinsdelen-en-de-voorwaardelijke-bijzin",
    titel="Zinsbouw, zinsdelen en de voorwaardelijke bijzin",
    reeksen=[
        reeks("zinsbouw-indirecte-rede-en-de-passieve-vorm", "Questions and negatives"),
        reeks("zinsbouw-indirecte-rede-en-de-passieve-vorm", "Conditionals", weg=(3,)),
        dict(kop="Word order",
             opdracht="Zet de woorden in de juiste orde.",
             oefeningen=[
                 ("rij", [("often / she / goes / to the gym", "She often goes to the gym."),
                          ("yesterday / we / the film / watched", "We watched the film yesterday."),
                          ("never / I / have / been / there", "I have never been there."),
                          ("usually / do / you / what / at weekends / do",
                           "What do you usually do at weekends?")],
                  "Welke zin?", WL),
                 ("kort", "Waar staat een bijwoord van frequentie zoals <em>often</em>?",
                  "voor het hoofdwerkwoord, maar na het werkwoord to be", WL),
             ]),
        dict(kop="Parts of a sentence",
             opdracht="Onderstreep in gedachten en schrijf het gevraagde deel op.",
             oefeningen=[
                 ("rij", [("My brother bought a new bike last week. (onderwerp)", "My brother"),
                          ("My brother bought a new bike last week. (lijdend voorwerp)",
                           "a new bike"),
                          ("My brother bought a new bike last week. (bepaling van tijd)",
                           "last week"),
                          ("She gave her sister the keys. (meewerkend voorwerp)", "her sister")],
                  "Welk deel?", WL),
             ]),
    ])
