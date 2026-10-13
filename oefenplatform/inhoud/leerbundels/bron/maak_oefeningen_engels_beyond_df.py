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
        # Niet geleend van de doorstroomfinaliteit: die reeks hoort bij de tekst
        # over de gereedschapsbibliotheek en vraagt naar lid worden.
        dict(kop="Reading between the lines",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom zegt Tom dat zijn winkel niet alleen voor arme gezinnen is?",
                  "Hij wil niemand het gevoel geven dat hij er niet hoort, en hij vindt dat het "
                  "tegengaan van verspilling iedereen aangaat. Komen er ook mensen die genoeg "
                  "geld hebben, dan blijft er meer over voor wie weinig kan betalen.", 3),
                 ("open", "Welke informatie zou je nog willen voor je er zelf zou gaan kopen?",
                  "Een eigen antwoord, bijvoorbeeld: hoe je weet wat een redelijk bedrag is, of "
                  "het eten nog lang genoeg goed blijft, wat er gebeurt als er op een week te "
                  "weinig geld binnenkomt, en of er iets gelijkaardigs in de eigen stad "
                  "bestaat.", 3),
             ]),
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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-engelse-tekst-lezen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de tekst eerst één keer helemaal door zonder woordenboek. Onderstreep "
                   "daarna de cijfers, de namen en de dagen, want daar gaan de vragen over.",
            waarom=[],
        ),
        dict(
            aanpak="Elk antwoord staat letterlijk in de tekst. Zoek dus de plaats terug en "
                   "antwoord met wat daar staat; één korte zin of enkele woorden is genoeg.",
            waarom=[
                "Noem beide helften: er staan geen prijzen op, en je betaalt wat je kan. Dat "
                "tweede is het hele idee van de winkel, dus laat het niet weg.",
                None,
                "Het antwoord zit in zijn citaat: elke avond werd er eten weggegooid dat nog goed "
                "was. Dat hij er kwaad om werd, mag je erbij zeggen.",
                None,
                "Twee dingen in één vraag: de dagen én de uren. Let op from Tuesday to Saturday: "
                "dinsdag en zaterdag zitten erbij, dus niet van woensdag tot vrijdag.",
                None,
                "Niet waar, en Tom zegt het zelf: it is for anyone who hates waste. Zo'n vraag "
                "test of je het citaat aan het einde gelezen hebt.",
            ],
        ),
        dict(
            aanpak="Zoek het Engelse woord in de tekst zelf terug in plaats van het uit je hoofd "
                   "te vertalen. Zo leer je het in zijn context, en dat blijft beter hangen.",
            waarom=[
                "Let op customer: een klant die koopt, terwijl client eerder bij een advocaat of "
                "een boekhouder past. En waste betekent zowel verspilling als afval.",
                "Shelves, want woorden op f of fe worden ves in het meervoud: knife wordt knives, "
                "life wordt lives. Roof is de bekende uitzondering: dat blijft roofs.",
            ],
        ),
        dict(
            aanpak="Hier moet je niet meer zoeken maar zelf nadenken. Antwoord met volle zinnen en "
                   "zet er telkens een reden bij, want zonder reden is het geen antwoord op een "
                   "waarom-vraag.",
            waarom=[
                "Noem dat hij niemand wil uitsluiten en dat verspilling iedereen aangaat. Dat "
                "mensen die kunnen betalen ook komen, houdt de winkel overeind, en dat mag je "
                "erbij zeggen.",
                "Hier is elk goed onderbouwd antwoord juist. Zet er wel bij waarom je dat zou "
                "willen weten, want dan wordt het een argument en geen opsomming.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstsoorten-en-de-bedoeling-van-een-tekst-beyond-dubbele-finaliteit"] = dict(
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
                   "informeel onder vrienden. Formeel is bijna altijd langer en met meer "
                   "hulpwerkwoorden.",
            waarom=[
                "Schrijf telkens de andere versie erbij, want dat is waar de oefening op mikt. I "
                "would be grateful if you could is een beleefdheidsformule; letterlijk vertalen "
                "klinkt in het Nederlands overdreven.",
                "Yours faithfully na Dear Sir or Madam, dus wanneer je de naam niet kent. Een "
                "steuntje: faithfully hoort bij een onbekende, zoals trouw zonder gezicht.",
                "Yours sincerely na Dear Mr Brown. In een mail is Kind regards bijna altijd veilig, "
                "en dat is wat men vandaag het meest schrijft.",
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
            aanpak="Kijk naar de vorm van de zin: een bevel zonder onderwerp hoort bij een recept "
                   "of een bord, een korte mededeling met een cijfer bij een scherm, en een "
                   "aanbieding met een uitroepteken bij een advertentie.",
            waarom=[
                "Let op het verschil tussen de eerste en de laatste: beide zijn een opdracht, maar "
                "mix the flour hoort bij een reeks stappen en please keep this door closed staat "
                "alleen op een bord. De lengte en de plaats verraden de tekstsoort.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-engelstalige-wereld-gewoontes-en-reizen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de landen en hun hoofdsteden uit elkaar, en vooral het Verenigd Koninkrijk "
                   "en Ierland. Dat zijn twee staten, met een andere munt.",
            waarom=[
                "Let op Canberra en Ottawa: niet Sydney en niet Toronto, al zijn die veel groter. "
                "Een hoofdstad is de zetel van de regering, niet de grootste stad.",
                "Engeland, Schotland, Wales en Noord-Ierland. Let op dat Groot-Brittannie enkel de "
                "eerste drie is: Noord-Ierland hoort bij het Verenigd Koninkrijk maar niet bij "
                "Groot-Brittannie, want dat is het eiland.",
                "The pound sterling, met honderd pence erin. Het teken is een doorstreepte L, en "
                "dat komt van het Latijnse libra.",
                "Waar. Ierland is lid van de eurozone, het Verenigd Koninkrijk niet. Noord-Ierland "
                "betaalt dus met ponden en de Republiek Ierland met euro's, al liggen ze op "
                "hetzelfde eiland.",
            ],
        ),
        dict(
            aanpak="Een gewoonte of een feestdag leer je met de datum erbij, want dat is wat men "
                   "vraagt. Let bij beleefdheid op de vorm van de zin en niet enkel op de woorden.",
            waarom=[
                "Bonfire Night is 5 november, de herinnering aan het verijdelde kruitcomplot van "
                "1605. Boxing Day is 26 december, en de naam komt van de dozen met giften die "
                "vroeger werden uitgedeeld. Thanksgiving is de vierde donderdag van november.",
                "Links, dus het stuur zit rechts. Let op bij het oversteken: in Londen staat op het "
                "wegdek look right om die reden.",
                "Noem twee dingen en liefst één over de vorm van een vraag. Would you mind en could "
                "you possibly klinken voorzichtiger dan een gebod, en dat is precies wat Britse "
                "beleefdheid typeert.",
            ],
        ),
        dict(
            aanpak="Reiswoorden komen met een vast werkwoord: book a room, check in, catch the "
                   "train. Leer die combinaties als één geheel.",
            waarom=[
                "Let op a return en a single: heen en terug tegenover enkel heen. Een Amerikaan "
                "zegt round-trip en one-way, en dat is het paar dat je ook moet herkennen.",
                "Book a room, check in at the hotel, catch the train, take a taxi. Let erop dat het "
                "take a taxi is en niet neem een taxi met neem vertaald als catch.",
            ],
        ),
        dict(
            aanpak="Schrijf telkens een hele zin die je echt aan een loket zou zeggen, en zet er "
                   "please bij. Een vraag met could is in het Engels beleefder dan een vraag met "
                   "can.",
            waarom=[
                "Een day return is een retourtje voor dezelfde dag, en dat is meestal goedkoper "
                "dan een gewoon retourtje. Vermeld dus de bestemming én de dag.",
                None,
                "Let op under the name of of in the name of: dat is de vaste wending bij een "
                "reservatie. On my name zegt een Engelsman niet.",
                "Begin met could you en eindig met please, dan klinkt het vriendelijk. En gebruik "
                "more slowly: slowlier bestaat niet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-schrijven-spreken-en-je-beleving-bij-een-tekst-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De aanhef en het slot van een mail horen bij elkaar als een paar. Ken je de "
                   "naam niet, dan Dear Sir or Madam met Yours faithfully; ken je de naam wel, dan "
                   "Dear Mr Jones met Yours sincerely.",
            waarom=[
                "Let op de komma na de aanhef en na het slot, en op de hoofdletter van Dear en "
                "Yours. In Amerikaans Engels staat er na de aanhef een dubbele punt in een zakelijke "
                "brief.",
                "Begin met I am writing to of I would like to: dan weet de lezer in één zin "
                "waarover het gaat. Schrijf ook meteen voor hoeveel nachten en wanneer, want dat is "
                "wat gevraagd wordt.",
            ],
        ),
        dict(
            aanpak="Dit zijn de zinnen die je in een gesprek echt nodig hebt. Leer ze als geheel en "
                   "spreek ze een paar keer luidop uit, want dan komen ze er op het moment zelf ook "
                   "uit.",
            waarom=[
                "Let op Sorry, I do not understand: dat is beleefder dan I do not understand alleen. "
                "En op het verschil tussen I disagree (formeler) en I do not agree, die beide juist "
                "zijn.",
            ],
        ),
        dict(
            aanpak="Bij een mening hoort altijd een reden. Gebruik de wendingen die gevraagd worden "
                   "en schrijf twee volle zinnen; één losse mening zonder reden is geen antwoord.",
            waarom=[
                "Houd het bij twee zinnen met I thought en because. Let op de tijd: thought is "
                "verleden tijd, dus de zinnen erna blijven ook in het verleden.",
                "Na you should komt de infinitief zonder to, en na if you like een naamwoord of een "
                "ing-vorm. Dus you should read this one if you like stories.",
                "Let op I would rather: daarna komt de infinitief zonder to (I would rather stay). "
                "En on the one hand vraagt altijd een on the other hand erna, net als enerzijds en "
                "anderzijds.",
            ],
        ),
        dict(
            aanpak="Kijk bij elke zin naar drie dingen: de hoofdletter vooraan, de punt achteraan "
                   "en de apostrof. En onthoud dat I in het Engels altijd een hoofdletter krijgt.",
            waarom=[
                "Let op de twee lastigste: their is van hen en they're is they are, en its is "
                "bezittelijk terwijl it's gelijk is aan it is. Zet de apostrof enkel waar je ook "
                "they are of it is zou kunnen zeggen.",
                "In het Engels krijgen dagen, maanden, talen, landen en volkeren altijd een "
                "hoofdletter, in het Nederlands niet. Daarom schrijf je English en maandag, maar "
                "Monday en Engels.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-dagelijks-leven-eten-en-wonen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de woorden per paar dat bij elkaar hoort: huurder en huisbaas, zolder en "
                   "kelder. Dat gaat sneller dan een lijst van losse woorden, en bij een toets komt "
                   "het paar vaak samen aan bod.",
            waarom=[
                "Let op tenant en landlord: de huurder betaalt, de huisbaas bezit. En op ground "
                "floor: het gelijkvloers is in het Brits Engels niet de first floor, want dat is "
                "bij ons de eerste verdieping.",
                "Terraced is een rijhuis, semi-detached een halfopen bebouwing en detached een "
                "vrijstaand huis. Flat is Brits, apartment Amerikaans.",
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
                "waterkoker, een kookpot en een pan. Zoek bij zo'n vraag altijd de categorie van "
                "de drie andere.",
            ],
        ),
        dict(
            aanpak="Een phrasal verb betekent samen iets anders dan de twee woorden apart, dus leer "
                   "ze als geheel. Up betekent vaak afwerken of verzamelen, out leeg of weg, off "
                   "uit of weg.",
            waarom=[
                "Let op give up: opgeven, niet weggeven. En run out of: op zijn. Bij pick up met "
                "een voornaamwoord móet het woordje erachter: pick you up, nooit pick up you.",
            ],
        ),
        dict(
            aanpak="Ook hier gaat het vooral om het juiste werkwoord bij het juiste huishoudelijke "
                   "karwei. Make, take, do en walk zijn niet uitwisselbaar, dus leer ze met hun "
                   "zelfstandig naamwoord erbij.",
            waarom=[
                "Let op a cousin: dat is zowel een neef als een nicht, en ook een kozijn. Wil je "
                "het geslacht erbij, dan zeg je my cousin Sarah. A relative is elk familielid.",
                "Make the bed, take the bin out, do the dishes, walk the dog. Let op do the dishes "
                "naast do the washing-up: dat is hetzelfde karwei, en in beide gevallen do.",
                "Houd het bij drie volle zinnen met first, then en after that. Die drie woorden "
                "maken je verhaal meteen overzichtelijk, en dat is wat men bij spreken beloont.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-gezondheid-natuur-en-duurzaamheid-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij de dokter is het woordveld klein maar vol valstrikken, vooral tussen Brits "
                   "en Amerikaans Engels. Leer bij elke klacht ook het werkwoord dat erbij hoort.",
            waarom=[
                "Let op GP: dat staat voor general practitioner, de huisarts. En chemist's is in "
                "Brits Engels de apotheek, terwijl een Amerikaan pharmacy of drugstore zegt.",
                "Vaste combinaties: catch a cold, get better, make an appointment, take painkillers. "
                "Take a cold bestaat niet.",
                "Noem beide betekenissen. In Amerikaans Engels betekent sick gewoon ziek, en dat is "
                "precies waarom de vraag Brits Engels zegt. Een Brit die I feel sick zegt, moet "
                "misschien overgeven.",
            ],
        ),
        dict(
            aanpak="Dierennamen en landschapswoorden moet je gewoon kennen. Het helpt om ze in "
                   "groepjes te leren: wat beweegt, wat groeit, en wat vorm geeft aan het "
                   "landschap.",
            waarom=[
                "Let op an owl met an, want het begint met een klinkerklank. En hedgehog zit in "
                "hedge: letterlijk een haagvarken, want daar leeft hij.",
                "Let op species: dat is zowel enkelvoud als meervoud, dus one species en two "
                "species. Een vaak gemaakte fout is specie, en dat woord bestaat zo niet.",
            ],
        ),
        dict(
            aanpak="Duurzaamheid is een woordveld dat je ook in een tekst of een nieuwsbericht "
                   "tegenkomt. Leer naast het woord ook de drie r's op een rij: reduce, reuse, "
                   "recycle.",
            waarom=[
                "Let op emissions: altijd meervoud in deze betekenis. En carbon footprint is een "
                "beeld: de afdruk die je met je uitstoot achterlaat.",
                "Noem dat het om eenmalig gebruik gaat. Single-use is ook een voorbeeld van hoe het "
                "Engels met een streepje een hele bepaling maakt, zoals in a ten-year-old bike.",
            ],
        ),
        dict(
            aanpak="Aan de apotheek heb je twee dingen nodig: de naam van wat je zoekt, en een hele "
                   "zin om je klacht uit te leggen. Zeg hoe lang je het al hebt, want dat is de "
                   "eerste vraag die je krijgt.",
            waarom=[
                "Let op cough syrup: cough spreek je uit als kof, met een f aan het einde. En "
                "ointment is een zalf, terwijl cream dunner is.",
                "Gebruik de present perfect met for: I have had a sore throat for three days, want "
                "het begon in het verleden en duurt nu nog. I have a sore throat since three days "
                "is de klassieke fout.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-geld-en-verkeer-beyond-dubbele-finaliteit"] = dict(
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
                "omdat je iets fout deed. Salary is een maandloon, wages is loon per uur of per "
                "week.",
                "Curriculum vitae, Latijn voor levensloop. In de Verenigde Staten heet hetzelfde "
                "document a resume.",
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
                   "Engels. Leer ze als paar, want in een tekst kan beide staan en je moet ze alle "
                   "twee herkennen.",
            waarom=[
                "Let op pavement: in Brits Engels het voetpad, in Amerikaans Engels het wegdek "
                "zelf. Dat is dus niet enkel een ander woord maar een andere betekenis, en daar "
                "gaan de meeste fouten.",
                "Een zebrapad, genoemd naar de strepen. In het Verenigd Koninkrijk heet een "
                "zebrapad met lichten een pelican crossing.",
                "Het spitsuur, al duurt het meestal langer dan een uur. In Brits Engels zegt men "
                "ook the rush hour, met the ervoor.",
            ],
        ),
        dict(
            aanpak="In een winkel heb je een handvol vaste vragen nodig. Begin met can I of could "
                   "I, zet please erachter, en je bent beleefd genoeg in elke situatie.",
            waarom=[
                "Let op can I try this on, met het woordje on achteraan: try on is passen, try "
                "alleen is proberen. En op pay by card tegenover pay in cash: twee verschillende "
                "voorzetsels, en die moet je als geheel leren.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-kunst-geschiedenis-en-de-samenleving-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de woorden om een werk te benoemen eerst, want die heb je nodig zodra je "
                   "over een boek, een film of een tentoonstelling moet praten.",
            waarom=[
                "Let op a novel: een roman, niet een novelle. En an exhibition met een h die je "
                "niet hoort; het werkwoord is to exhibit.",
                "Noem beide helften. Let op dat non-fiction niet hetzelfde is als waar: het gaat "
                "over de werkelijkheid, maar een non-fictieboek kan zich vergissen of overtuigen "
                "willen.",
            ],
        ),
        dict(
            aanpak="Politieke woorden lijken sterk op het Nederlands, dus hier gaat het vooral om "
                   "de juiste vorm en het juiste voorzetsel.",
            waarom=[
                "Let op to vote for someone, met for. En an act is de naam van een wet in het "
                "Verenigd Koninkrijk, zoals the Education Act; a law is het begrip in het "
                "algemeen.",
                "De Houses of Parliament, met het House of Commons en het House of Lords. In "
                "Belgie zijn dat de Kamer en de Senaat, en dat verschil is een handige "
                "vergelijking.",
                "Houd het bij twee zinnen met de gevraagde wendingen en één echt argument. Let op "
                "de komma na In my opinion, en op het streepje in sixteen-year-olds.",
            ],
        ),
        dict(
            aanpak="Geschiedeniswoorden komen vaak terug in een tekst over een gebouw of een stad. "
                   "Let vooral op het rekenen met eeuwen, want dat gaat net anders dan je denkt.",
            waarom=[
                "Let op the Middle Ages: altijd meervoud en met hoofdletters. En op a castle met "
                "een t die je niet hoort, zoals in listen en fasten.",
                "Van 1801 tot 1900, want de eerste eeuw liep van het jaar 1 tot 100. Een eeuw heet "
                "dus altijd één nummer hoger dan de jaartallen die erin staan, en dat is de "
                "klassieke rekenfout.",
            ],
        ),
        dict(
            aanpak="In een museum heb je een paar vaste vragen nodig. Begin met how much, is there "
                   "of what time, en je komt er met vier zinnen altijd.",
            waarom=[
                "Let op am I allowed to: dat is beleefder dan can I en vraagt naar de regel, niet "
                "naar je eigen kunnen. Entrance fee is de toegangsprijs; ticket is het bewijs dat "
                "je betaald hebt.",
                "Let op het verschil tussen a statue en a sculpture: een statue beeldt iemand of "
                "iets af, een sculpture is elk gebeeldhouwd werk. En audience is het publiek als "
                "groep.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-woordvelden-wetenschap-techniek-en-taal-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Veel van deze woorden ken je al uit het Nederlands, dus let vooral op wat "
                   "anders is: de onteltbare woorden en de woorden die op het eerste gezicht "
                   "hetzelfde lijken.",
            waarom=[
                "Let op research: onteltbaar, dus geen a research. En a device is een toestel in "
                "het algemeen, terwijl an appliance een huishoudtoestel is.",
                "Let op a file: zowel een bestand als een map of een vijl, afhankelijk van de "
                "context. En to save betekent zowel opslaan als sparen en redden.",
                "Waar. Je zegt a piece of research, some research of a study. Dezelfde regel als "
                "bij homework, information en advice.",
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
        dict(
            aanpak="Computerwoorden ken je meestal al van je toestel zelf. Leer ze met hun "
                   "werkwoord: save a file, set a password, reset it.",
            waarom=[
                "Let op a folder: een map op je computer, terwijl a map een landkaart is. En the "
                "settings is altijd meervoud.",
                "Twee korte zinnen zijn genoeg: My password does not work. I would like to reset "
                "it. Let op to reset: dat is opnieuw instellen, en de verleden tijd blijft reset.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-naamwoorden-lidwoorden-en-hoeveelheden-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De gewone regel is een s erbij, maar let op vier groepen: woorden op f die ves "
                   "worden, woorden op een consonant plus y die ies worden, woorden op s, x, ch of "
                   "sh die es krijgen, en de onregelmatige die je gewoon moet kennen.",
            waarom=[
                "Let op sheep: enkelvoud en meervoud gelijk, net als fish en deer. En op knife dat "
                "knives wordt, terwijl roof gewoon roofs blijft.",
            ],
        ),
        dict(
            aanpak="Een onteltbaar woord heeft geen meervoud en geen a ervoor. Wil je er toch één "
                   "van aanduiden, dan zet je er a piece of of an item of voor.",
            waarom=[
                "Deze zes zijn de klassiekers van elke toets. Advice, information, furniture en "
                "news zijn onteltbaar; suitcase en journey niet. Let op dat het Nederlands hier wel "
                "een meervoud heeft, en dat is net waarom de fout zo vaak gemaakt wordt.",
                "Enkelvoud, ondanks de s: the news is good. Hetzelfde bij mathematics, physics en "
                "politics als vakgebied.",
            ],
        ),
        dict(
            aanpak="Drie vragen helpen je kiezen: is het iets algemeens (dan geen lidwoord), is het "
                   "voor het eerst genoemd (dan a of an), of weten we al welke het is (dan the)? "
                   "Instrumenten krijgen altijd the.",
            waarom=[
                "Let op to go to school zonder lidwoord: het gaat over naar school gaan als "
                "bezigheid. Sta je als ouder bij het gebouw, dan zeg je wel I am at the school. En "
                "the Netherlands krijgt the, net als the United States, omdat het een meervoud is.",
                "Noem dat het om de klank gaat en niet om de letter. Daarom ook an MP3 file, want "
                "de m wordt em uitgesproken, en a one-way ticket, want one begint met een "
                "w-klank.",
            ],
        ),
        dict(
            aanpak="Much bij onteltbaar, many bij telbaar. Little en a little bij onteltbaar, few "
                   "en a few bij telbaar. A lot of kan bij beide en is in een gewone zin het "
                   "veiligst.",
            waarom=[
                "Let op dat much en many vooral in vragen en ontkenningen staan; in een bevestigende "
                "zin klinkt a lot of natuurlijker. Daarom staat er in de laatste a lot of work.",
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
                "zonder s) en managers' (meervoud met s). Bij the roof of the house blijft of "
                "staan, want een huis is geen persoon.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voornaamwoorden-en-betrekkelijke-bijzinnen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk gaatje af welke soort er moet staan: een bezittelijk zonder "
                   "naamwoord erachter (mine), een wederkerend (herself), of een onderwerp dat enkel "
                   "de zin vult (it of there).",
            waarom=[
                "Let op het verschil tussen it en there: it is raining gaat over het weer, there "
                "were twenty people zegt dat er iets aanwezig is. In het Nederlands zeggen we in "
                "beide gevallen het of er, en daar komt de fout.",
                "Its is bezittelijk, it's is een samentrekking van it is of it has. Een handig "
                "steuntje: zet de apostrof enkel waar je ook it is zou kunnen zeggen.",
            ],
        ),
        dict(
            aanpak="Who voor mensen, which voor dingen, whose voor bezit, where voor een plaats. "
                   "That kan who en which vervangen, maar niet in een bijzin tussen komma's.",
            waarom=[
                "Let op whose: dat gebruik je ook voor dingen. En bij de laatste staat er who en "
                "geen that, want die bijzin staat tussen komma's en geeft enkel extra informatie.",
            ],
        ),
        dict(
            aanpak="Zoek het woord dat in beide zinnen voorkomt en vervang het in de tweede zin "
                   "door who of where. Plak die bijzin dan direct achter het woord waar hij bij "
                   "hoort.",
            waarom=[
                None,
                "Where vervangt there, dus dat woordje verdwijnt: niet the house where we lived "
                "there. Je kan ook zeggen the house in which we lived, en dat is formeler.",
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
        dict(
            aanpak="Een voornaamwoord als onderwerp is I, he, she, we, they; als lijdend voorwerp "
                   "of na een voorzetsel is het me, him, her, us, them. Kijk dus of het woord vóór "
                   "of ná het werkwoord staat.",
            waarom=[
                "Let op de laatste: between you and me, want na een voorzetsel komt me. Between you "
                "and I hoor je vaak, ook bij moedertaalsprekers, maar het is fout.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels-beyond-dubbele-finaliteit"] = dict(
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
                   "werkwoord. Gaat het over hóe iets gebeurt, dan hoort er ly bij, behalve na een "
                   "koppelwerkwoord en bij fast en hard.",
            waarom=[
                "Let op fast en hard: die hebben geen ly-vorm als bijwoord. En op the soup tastes "
                "good: taste, look en feel zijn koppelwerkwoorden, dus daar komt een bijvoeglijk "
                "naamwoord achter.",
                "Hard is hevig of zwaar, hardly is nauwelijks. I worked hard en I hardly worked "
                "zeggen dus net het omgekeerde, en dat is een klassieke valstrik.",
            ],
        ),
        dict(
            aanpak="Voorzetsels van tijd volgen een regel: at bij een uur, on bij een dag, in bij "
                   "een maand of jaar. Wat vast aan een bijvoeglijk naamwoord hangt, moet je als "
                   "combinatie leren.",
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
            aanpak="Een tegengestelde leer je altijd samen met het woord zelf: dan heb je er twee "
                   "voor de prijs van één, en kan je een beschrijving veel preciezer maken.",
            waarom=[
                "Let op crowded en empty: vol volk tegenover leeg. En op polite en rude, want rude "
                "is sterker dan onvriendelijk; het betekent echt onbeschoft.",
                "Houd het bij drie volle zinnen en gebruik echt drie verschillende bijvoeglijke "
                "naamwoorden. Zet er een paar uit de reeks hierboven in, dan oefen je ze meteen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-tegenwoordige-tijden-en-de-present-perfect-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De simple present gebruik je voor wat altijd of regelmatig zo is, de present "
                   "continuous voor wat nu bezig is of tijdelijk duurt. Woorden als every day en "
                   "always wijzen naar de simple, woorden als look, now en this week naar de "
                   "continuous.",
            waarom=[
                "Let op de derde: water boils at 100 graden Celsius is een algemene waarheid, dus "
                "simple. En de laatste: they are staying with us this week is tijdelijk, dus "
                "continuous, ook al gebeurt het de hele week.",
                "Noem er twee uit de lijst. Dit zijn de state verbs: ze beschrijven een toestand en "
                "geen bezigheid, dus I am knowing bestaat niet.",
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
                "keys betekent dat ze nog kwijt zijn, I lost my keys kan betekenen dat ik ze daarna "
                "terugvond.",
                "Dit lijstje is het handigst om te onthouden: yesterday, in 2010 en last week zijn "
                "af, dus past simple; since, already en so far lopen door tot nu, dus present "
                "perfect.",
            ],
        ),
        dict(
            aanpak="Staat er al een hulpwerkwoord in de zin (are, has, can), dan zet je dat "
                   "vooraan. Staat er geen, dan haal je do of does erbij en gaat het werkwoord "
                   "terug naar de basisvorm.",
            waarom=[
                "Vergelijk de eerste met de laatste: works wordt does she work, en live wordt do "
                "you live. De s verhuist dus naar does, en bij you is er geen s en wordt het do.",
                "Omdat does de persoonsvorm al draagt. Daarom is het does she work en niet does she "
                "works, net zoals het did you see is en niet did you saw.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-verleden-tijden-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Onregelmatige werkwoorden moet je kennen, maar ze zitten in groepjes: buy, "
                   "catch en bring eindigen alle drie op ought of aught, en choose, write en fall "
                   "hebben een apart deelwoord op en.",
            waarom=[
                "Let op het verschil tussen de eerste groep (verleden tijd en deelwoord gelijk) en "
                "de tweede (deelwoord op en). Bij chose en chosen hoor je dat verschil ook.",
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
            aanpak="Used to beschrijft een gewoonte of een toestand uit het verleden die nu niet "
                   "meer bestaat. Na used to komt de infinitief zonder to erbij.",
            waarom=[
                "Used to play, niet used to played. Let ook op de ontkenning: I did not use to "
                "play, zonder d, want did draagt de verleden tijd al.",
            ],
        ),
        dict(
            aanpak="In de past simple krijgt een regelmatig werkwoord ed, en de onregelmatige "
                   "hebben hun eigen vorm. In een vraag of een ontkenning komt did erbij en gaat "
                   "het werkwoord terug naar de basisvorm.",
            waarom=[
                "Let op did not come en Did you see: na did staat de basisvorm, dus niet did not "
                "came of did you saw. Alleen to be doet het anders: was en were hebben geen did "
                "nodig.",
                "Houd het bij vier volle zinnen die alle in de verleden tijd staan. Begin elke zin "
                "met een tijdsbepaling als on Saturday of in the evening, dan loopt je verhaal "
                "vanzelf.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-toekomende-tijd-en-de-modale-hulpwerkwoorden-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het Engels heeft drie manieren om over de toekomst te praten. Going to voor een "
                   "plan dat vastligt of voor wat je ziet aankomen, will voor een beslissing op het "
                   "moment of een voorspelling, en de present continuous voor een afspraak met een "
                   "tijdstip erbij.",
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
            aanpak="Hier kies je zelf de vorm die bij de situatie past. Loop de drie gevallen uit "
                   "de eerste reeks af: een belofte, iets dat je ziet aankomen, of een afspraak die "
                   "al vastligt.",
            waarom=[
                "Let op de vorm am going to, met de juiste vorm van to be. En op de ontkenning: I "
                "am not going to study, met not tussen am en going.",
                "Deze drie zijn precies de drie regels van de eerste reeks, nu omgekeerd gevraagd. "
                "Bij een afspraak met een uur erbij gebruikt een Engelsman bijna altijd de present "
                "continuous.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zinsbouw-zinsdelen-en-de-voorwaardelijke-bijzin-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een vraag of een ontkenning heeft een hulpwerkwoord nodig. Staat er al een "
                   "(have, can, is), dan zet je dat vooraan. Staat er geen, dan haal je do, does of "
                   "did erbij, en het hoofdwerkwoord gaat terug naar de basisvorm.",
            waarom=[
                "Let op de eerste en de laatste: works wordt does she work (de s verhuist naar "
                "does) en saw wordt did you see (de verleden tijd verhuist naar did). Did you saw "
                "is dus dubbel fout.",
                "Isn't she, dus omgekeerd aan de hoofdzin: een bevestiging krijgt een ontkennende "
                "tag en omgekeerd. Dat is wat het Nederlandse he of niet in een vraagje doet.",
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
        dict(
            aanpak="De gewone orde in het Engels is onderwerp, werkwoord, lijdend voorwerp, en dan "
                   "de bepalingen van plaats en tijd. Een bijwoord van frequentie wringt zich "
                   "tussen het onderwerp en het werkwoord.",
            waarom=[
                "Let op de derde en de vierde: never komt tussen have en been, en in een vraag komt "
                "usually na you. Het Engels zet het lijdend voorwerp vlak achter het werkwoord, dus "
                "niet we watched yesterday the film.",
                "Voor het hoofdwerkwoord (she often goes), maar na een vorm van to be (she is often "
                "late). Bij een hulpwerkwoord komt het ertussen: I have never been.",
            ],
        ),
        dict(
            aanpak="Zoek eerst de persoonsvorm, dan het onderwerp (wie of wat doet het?), dan het "
                   "lijdend voorwerp (wat?). Wat overblijft met een vraag als wanneer of waar, is "
                   "een bepaling.",
            waarom=[
                "Let op het laatste: bij she gave her sister the keys is her sister het meewerkend "
                "voorwerp, want je kan ook zeggen she gave the keys to her sister. Dat omzetten met "
                "to is de beste proef.",
            ],
        ),
    ],
)
