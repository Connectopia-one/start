# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van Engels 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Dezelfde leerstof en dezelfde woorden, maar een andere richting en een
andere situatie: waar het scherm vraagt wat een woord betekent, vraagt de
bundel om het zelf te schrijven. Zo moet een kind twee keer nadenken in plaats
van twee keer hetzelfde antwoord op te schrijven. Wie hier iets bijschrijft,
legt het dus eerst naast de vragen in `../../start/engels.json`.

Bij een taalvak staat het invulvakje breder dan bij wiskunde: "Wednesday" past
niet in een vakje dat voor een getal van twee cijfers gemaakt is.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

W = "120px"    # een los woord
WW = "170px"   # een lang woord of twee woorden

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Weet je een woord niet meer? Sla het over en kom er op het einde op terug.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-woorden-voor-elke-dag"] = dict(
    vak="Engels", titel="Woorden voor elke dag",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De dagen en de maanden",
             opdracht="Denk aan de hoofdletter: in het Engels krijgen dagen en maanden er altijd een.",
             oefeningen=[
                 ("rij", [("vrijdag", "Friday"), ("zaterdag", "Saturday"),
                          ("dinsdag", "Tuesday"), ("zondag", "Sunday")],
                  "Schrijf de dag in het Engels.", WW),
                 ("rij", [("maart", "March"), ("juni", "June"),
                          ("oktober", "October"), ("januari", "January")],
                  "Schrijf de maand in het Engels.", WW),
                 ("kort", "Welke dag komt na Saturday?", "Sunday", WW),
                 ("kort", "Welke maand komt vlak voor May?", "April", WW),
                 ("waar", "Je mag \"friday\" met een kleine letter schrijven.", False),
                 ("kies", "In welke maand valt Kerstmis?",
                  ["November", "December", "January", "October"], 1),
             ]),

        dict(kop="Getallen",
             opdracht="Let op het verschil tussen -teen (13 tot 19) en -ty (20, 30, 40 …).",
             oefeningen=[
                 ("rij", [("11", "eleven"), ("20", "twenty"), ("40", "forty"),
                          ("60", "sixty"), ("13", "thirteen"), ("100", "a hundred")],
                  "Schrijf het getal voluit in het Engels.", WW),
                 ("rij", [("eighty", "80"), ("nineteen", "19"),
                          ("fifty", "50"), ("seventeen", "17")],
                  "Schrijf het getal in cijfers.", "70px"),
                 ("kies", "Welk getal is het grootst?",
                  ["seventeen", "seventy", "seven", "sixty"], 1),
                 ("waar", "\"Forty\" schrijf je met een u, net als \"four\".", False),
                 ("open", "Schrijf je eigen leeftijd voluit in het Engels, in een hele zin.",
                  "Bijvoorbeeld: I am eleven years old.", 2),
             ]),

        dict(kop="Kleuren en het lichaam",
             opdracht="Schrijf het Engelse woord op de lijn.",
             oefeningen=[
                 ("rij", [("groen", "green"), ("zwart", "black"), ("wit", "white"),
                          ("bruin", "brown"), ("roze", "pink"), ("rood", "red")],
                  "Welke kleur is het?", W),
                 ("rij", [("hand", "hand"), ("hoofd", "head"), ("voet", "foot"),
                          ("arm", "arm"), ("knie", "knee"), ("oog", "eye")],
                  "Welk lichaamsdeel is het?", W),
                 ("kies", "Welk woord is GEEN lichaamsdeel?",
                  ["hand", "hair", "hat", "head"], 2),
                 ("waar", "\"Feet\" is het meervoud van \"foot\".", True),
                 ("kort", "Welke kleur krijg je als je rood en wit mengt? Schrijf het Engelse woord.",
                  "pink", W),
             ]),

        dict(kop="Familie en seizoenen",
             opdracht="Kijk goed of er een enkelvoud of een meervoud gevraagd wordt.",
             oefeningen=[
                 ("rij", [("vader", "father"), ("moeder", "mother"), ("zus", "sister"),
                          ("oom", "uncle"), ("grootvader", "grandfather")],
                  "Schrijf het Engelse woord.", WW),
                 ("kort", "Vul aan: spring, &nbsp;…&nbsp;, autumn, &nbsp;… &nbsp; (de twee seizoenen die ontbreken)",
                  "summer en winter", WW),
                 ("waar", "De broer van je moeder noem je in het Engels je \"uncle\".", True),
                 ("kies", "Je tante en je oom hebben een dochter. Wat is zij voor jou, in het Engels?",
                  ["sister", "aunt", "cousin", "niece"], 2),
                 ("open", "Schrijf drie woorden op die bij jouw familie horen, in het Engels.",
                  "Bijvoorbeeld: mother, father, brother, sister, aunt, uncle, cousin, "
                  "grandmother, grandfather.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mezelf-voorstellen"] = dict(
    vak="Engels", titel="Mezelf voorstellen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat zeg je wanneer?",
             opdracht="Kleur het bolletje van het juiste antwoord, of schrijf het op de lijn.",
             oefeningen=[
                 ("kies", "Je ontmoet iemand voor de eerste keer. Wat zeg je na \"Hello\"?",
                  ["See you!", "Nice to meet you.", "Good night.", "You are welcome."], 1),
                 ("kies", "Je komt 's morgens de klas binnen. Wat zeg je tegen je juf of meester?",
                  ["Good evening", "Good night", "Good morning", "Goodbye"], 2),
                 ("kies", "Iemand geeft je een cadeautje. Wat zeg je?",
                  ["Sorry.", "Thank you.", "Please.", "Excuse me."], 1),
                 ("open", "Iemand zegt \"Thank you\" tegen jou. Schrijf op wat je antwoordt.",
                  "You are welcome. (Of korter: You're welcome.)", 1),
                 ("open", "Iemand vraagt \"How are you?\" Schrijf twee antwoorden die je zou kunnen geven.",
                  "Bijvoorbeeld: I am fine, thanks. &middot; I'm OK. &middot; Not so good.", 2),
                 ("waar", "\"Bye\" en \"Goodbye\" betekenen allebei tot ziens.", True),
             ]),

        dict(kop="Iemand anders voorstellen",
             opdracht="Bij een jongen of man hoort his, bij een meisje of vrouw her.",
             oefeningen=[
                 ("rij", [("This is Tom. … bag is blue.", "His"),
                          ("This is Amy. … dog is small.", "Her"),
                          ("This is my sister. … name is Lisa.", "Her"),
                          ("This is my father. … car is red.", "His")],
                  "Vul aan met his of her.", W),
                 ("waar", "Bij een meisje gebruik je \"his\".", False),
                 ("open", "Vertaal: \"Dit is mijn vriend Sam. Hij is twaalf jaar.\"",
                  "This is my friend Sam. He is twelve (years old).", 2),
                 ("open", "Schrijf drie zinnen in het Engels over je beste vriend of vriendin: "
                          "zijn of haar naam, leeftijd en waar hij of zij woont.",
                  "Bijvoorbeeld: This is my friend Nora. She is eleven years old. "
                  "She lives in Genk.", 4),
             ]),

        dict(kop="Vragen stellen",
             opdracht="Elk vraagwoord vraagt naar iets anders: wie, wanneer, waar, waarom, hoe.",
             oefeningen=[
                 ("rij", [("… is your teacher?", "Who"),
                          ("… is your birthday?", "When"),
                          ("… are you going?", "Where"),
                          ("… do you say that in English?", "How")],
                  "Vul het juiste vraagwoord in.", W),
                 ("kies", "Hoe vraag je waar iemand vandaan komt?",
                  ["Where are you from?", "Where do you go?", "Who are you?", "What are you?"], 0),
                 ("open", "Schrijf twee vragen op die je kan stellen aan iemand die je nog niet kent.",
                  "Bijvoorbeeld: What is your name? &middot; How old are you? &middot; "
                  "Where do you live? &middot; Do you have any brothers or sisters?", 2),
             ]),

        dict(kop="Landen en beleefde woorden",
             opdracht="Landen krijgen in het Engels altijd een hoofdletter.",
             oefeningen=[
                 ("rij", [("Nederland", "the Netherlands"), ("Frankrijk", "France"),
                          ("Duitsland", "Germany"), ("Engeland", "England"),
                          ("Spanje", "Spain"), ("Italië", "Italy")],
                  "Schrijf het land in het Engels.", WW),
                 ("rij", [("alsjeblieft", "please"), ("dank je", "thank you"),
                          ("sorry", "sorry"), ("tot ziens", "goodbye")],
                  "Schrijf het Engelse woord.", WW),
                 ("waar", "\"I am Belgium\" is een juiste manier om te zeggen dat je uit België komt.",
                  False),
                 ("kies", "Wat betekent \"See you tomorrow!\"?",
                  ["Tot morgen!", "Tot ziens!", "Goedemorgen!", "Slaap wel!"], 0),
                 ("open", "Stel jezelf voor in het Engels, in drie zinnen: je naam, je leeftijd "
                          "en waar je woont.",
                  "Bijvoorbeeld: Hello, my name is Lien. I am eleven years old. I live in Hasselt.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-to-be-en-to-have"] = dict(
    vak="Engels", titel="To be en to have",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="To be: am, is en are",
             opdracht="Bij I hoort am, bij he, she en it hoort is, bij de rest are.",
             oefeningen=[
                 ("tabel", ["", "to be"],
                  [["I", None], ["he", None], ["she", None],
                   ["we", None], ["you", None], ["they", None]],
                  "I am &middot; he is &middot; she is &middot; we are &middot; you are &middot; they are"),
                 ("rij", [("The dog … hungry.", "is"), ("My shoes … new.", "are"),
                          ("I … ready.", "am"), ("You … funny.", "are"),
                          ("The films … long.", "are"), ("It … cold today.", "is")],
                  "Vul aan met am, is of are.", W),
                 ("open", "Maak er een vraag van: \"She is at home.\"", "Is she at home?", 1),
                 ("open", "Maak deze zin ontkennend: \"I am late.\"",
                  "I am not late. (Korter: I'm not late.)", 1),
                 ("kies", "Welke zin klopt?",
                  ["The cats is black.", "The cats are black.",
                   "The cats am black.", "The cats be black."], 1),
             ]),

        dict(kop="To have: have en has",
             opdracht="Alleen bij he, she en it wordt have een has.",
             oefeningen=[
                 ("tabel", ["", "to have"],
                  [["I", None], ["he", None], ["it", None],
                   ["we", None], ["she", None], ["they", None]],
                  "I have &middot; he has &middot; it has &middot; we have &middot; she has &middot; they have"),
                 ("rij", [("My sister … a rabbit.", "has"), ("The boys … a new ball.", "have"),
                          ("It … four legs.", "has"), ("We … a big garden.", "have")],
                  "Vul aan met have of has.", W),
                 ("open", "Maak deze zin ontkennend: \"He has a bike.\"",
                  "He doesn't have a bike. (Ook goed: He hasn't got a bike.)", 1),
                 ("kies", "Welke zin klopt?",
                  ["Does she has a pen?", "Do she have a pen?",
                   "Does she have a pen?", "She does have pen?"], 2),
                 ("waar", "Na \"does\" krijgt het werkwoord geen -s meer.", True),
             ]),

        dict(kop="De korte vormen",
             opdracht="De apostrof vervangt de letters die wegvallen.",
             oefeningen=[
                 ("rij", [("isn't", "is not"), ("aren't", "are not"),
                          ("haven't", "have not"), ("she's", "she is")],
                  "Schrijf voluit.", WW),
                 ("rij", [("he is", "he's"), ("they are", "they're"),
                          ("has not", "hasn't"), ("I am", "I'm")],
                  "Schrijf korter, met een apostrof.", W),
                 ("kies", "In welke zin staat de apostrof juist?",
                  ["Its raining.", "It's raining.", "Its' raining.", "It is'nt raining."], 1),
                 ("waar", "\"Its\" zonder apostrof betekent \"het is\".", False),
             ]),

        dict(kop="Alles door elkaar",
             opdracht="Lees eerst wie of wat er vooraan staat, en kies dan pas de vorm.",
             oefeningen=[
                 ("rij", [("She … a headache.", "has"), ("They … in the garden.", "are"),
                          ("I … a new phone.", "have"), ("The film … very long.", "is")],
                  "Vul aan met am, is, are, have of has.", W),
                 ("open", "Schrijf twee zinnen over je huisdier, of over het dier dat je graag "
                          "zou willen. Gebruik één keer to have en één keer to be.",
                  "Bijvoorbeeld: I have a cat. She is black and white.", 3),
                 ("open", "Vertaal: \"Mijn broer heeft twee katten en ze zijn allebei zwart.\"",
                  "My brother has two cats and they are both black.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-tegenwoordige-tijd"] = dict(
    vak="Engels", titel="De tegenwoordige tijd",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De -s bij he, she en it",
             opdracht="Alleen bij he, she en it komt er iets achter het werkwoord.",
             oefeningen=[
                 ("rij", [("he (walk)", "walks"), ("she (watch)", "watches"),
                          ("it (fly)", "flies"), ("he (go)", "goes"),
                          ("she (finish)", "finishes"), ("he (carry)", "carries")],
                  "Schrijf het werkwoord in de juiste vorm.", WW),
                 ("rij", [("My mum … coffee every morning. (drink)", "drinks"),
                          ("We … to music. (listen)", "listen"),
                          ("The bus … at eight. (leave)", "leaves"),
                          ("They … outside. (play)", "play")],
                  "Vul het werkwoord in, in de juiste vorm.", W),
                 ("waar", "\"She studys\" is juist geschreven.", False),
                 ("open", "Hoe schrijf je \"he (try)\" in de tegenwoordige tijd? Schrijf er ook "
                          "bij waarom.",
                  "He tries. Een medeklinker plus -y wordt -ies.", 2),
             ]),

        dict(kop="Vragen maken met do en does",
             opdracht="Na do en does schrijf je het werkwoord zonder -s.",
             oefeningen=[
                 ("rij", [("… you like sport?", "Do"), ("… he work here?", "Does"),
                          ("… your friends play outside?", "Do"), ("… it rain a lot?", "Does")],
                  "Vul aan met Do of Does.", W),
                 ("open", "Maak er een vraag van: \"They live in Genk.\"", "Do they live in Genk?", 1),
                 ("open", "Maak er een vraag van: \"She plays the piano.\"",
                  "Does she play the piano? (De -s valt weg, want die zit al in does.)", 1),
                 ("waar", "Na \"do\" en \"does\" schrijf je het werkwoord zonder -s.", True),
             ]),

        dict(kop="Ontkennen met don't en doesn't",
             opdracht="Denk eraan wie er vooraan staat voor je kiest.",
             oefeningen=[
                 ("rij", [("I … eat meat.", "don't"), ("She … know the way.", "doesn't"),
                          ("We … have time.", "don't"), ("It … matter.", "doesn't")],
                  "Vul aan met don't of doesn't.", W),
                 ("kies", "Welke zin klopt?",
                  ["He don't like fish.", "He doesn't likes fish.",
                   "He doesn't like fish.", "He not like fish."], 2),
                 ("open", "Vertaal: \"Mijn vader werkt niet op zaterdag.\"",
                  "My father doesn't work on Saturday.", 2),
             ]),

        dict(kop="Wanneer gebruik je deze tijd?",
             opdracht="De tegenwoordige tijd gaat over wat telkens opnieuw gebeurt.",
             oefeningen=[
                 ("kies", "Welk woord hoort bij de tegenwoordige tijd?",
                  ["yesterday", "tomorrow", "usually", "last week"], 2),
                 ("rij", [("always", "altijd"), ("never", "nooit"),
                          ("sometimes", "soms"), ("often", "vaak")],
                  "Wat betekent het woord?", WW),
                 ("open", "Schrijf drie zinnen in het Engels over wat je elke dag doet.",
                  "Bijvoorbeeld: I get up at seven. I go to school by bike. "
                  "I always do my homework after dinner.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-zinnen-bouwen"] = dict(
    vak="Engels", titel="Zinnen bouwen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Meervouden",
             opdracht="De meeste krijgen een -s, maar een paar zijn onregelmatig.",
             oefeningen=[
                 ("rij", [("bus", "buses"), ("baby", "babies"), ("tooth", "teeth"),
                          ("woman", "women"), ("knife", "knives"), ("dish", "dishes")],
                  "Schrijf het meervoud.", WW),
                 ("waar", "\"Childrens\" is het meervoud van \"child\".", False),
                 ("kies", "Welk meervoud is onregelmatig, dus zonder -s?",
                  ["books", "mice", "houses", "trees"], 1),
             ]),

        dict(kop="A of an",
             opdracht="Het gaat om de klank waarmee het woord begint, niet om de letter.",
             oefeningen=[
                 ("rij", [("… orange", "an"), ("… house", "a"), ("… egg", "an"),
                          ("… umbrella", "an"), ("… bike", "a"), ("… hour", "an")],
                  "Vul aan met a of an.", W),
                 ("open", "Waarom is het \"a university\" en niet \"an university\"? "
                          "Schrijf het in je eigen woorden.",
                  "Omdat university begint met een j-klank (joe-niversity) en niet met een "
                  "klinkerklank. Het gaat om wat je hoort, niet om de letter.", 2),
             ]),

        dict(kop="De volgorde in een zin",
             opdracht="Eerst wie, dan wat, dan waar, en pas daarna wanneer.",
             oefeningen=[
                 ("kies", "Welke zin heeft de juiste woordvolgorde?",
                  ["She reads in the evening a book.", "She reads a book in the evening.",
                   "In the evening a book she reads.", "A book she reads in the evening."], 1),
                 ("open", "Zet in de juiste volgorde: dog &nbsp;/&nbsp; a &nbsp;/&nbsp; big "
                          "&nbsp;/&nbsp; black", "a big black dog", 1),
                 ("waar", "In het Engels staat de kleur voor het woord: \"a green door\".", True),
                 ("rij", [("… a cat in the garden.", "There is"), ("… three chairs.", "There are"),
                          ("… some milk in the fridge.", "There is"), ("… many people here.", "There are")],
                  "Vul aan met There is of There are.", WW),
             ]),

        dict(kop="Van wie is het, en welk vraagwoord?",
             opdracht="Met 's toon je aan van wie iets is.",
             oefeningen=[
                 ("open", "Schrijf in het Engels, met 's: \"de fiets van mijn broer\"",
                  "my brother's bike", 1),
                 ("rij", [("… is that girl?", "Who"), ("… are you sad?", "Why"),
                          ("… book is this?", "Whose"), ("… is your bike?", "Where")],
                  "Vul het juiste vraagwoord in.", W),
                 ("kies", "Welke zin klopt?",
                  ["She is good in maths.", "She is good at maths.",
                   "She is good on maths.", "She is good of maths."], 1),
                 ("open", "Schrijf twee zinnen over je kamer: één met \"there is\" en één met "
                          "\"there are\".",
                  "Bijvoorbeeld: There is a desk near the window. There are two posters on the wall.", 3),
                 ("open", "Vertaal: \"Er liggen twee boeken op de tafel.\"",
                  "There are two books on the table.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-op-school-en-onderweg"] = dict(
    vak="Engels", titel="Op school en onderweg",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In de klas",
             opdracht="Schrijf het Engelse woord, of wat de zin in het Nederlands betekent.",
             oefeningen=[
                 ("rij", [("pen", "pen"), ("boek", "book"), ("bank", "desk"),
                          ("klas", "classroom"), ("huiswerk", "homework"),
                          ("leerkracht", "teacher")],
                  "Schrijf het Engelse woord.", WW),
                 ("rij", [("Sit down.", "Ga zitten."), ("Stand up.", "Sta op."),
                          ("Listen.", "Luister."), ("Write it down.", "Schrijf het op.")],
                  "Wat zegt de leerkracht?", WW),
                 ("kies", "Je hebt iets niet begrepen. Wat vraag je?",
                  ["Can you repeat that, please?", "Can I go home?",
                   "How much is it?", "What is your name?"], 0),
                 ("open", "Schrijf in het Engels dat je je boek vergeten bent.",
                  "Bijvoorbeeld: I'm sorry, I forgot my book.", 2),
             ]),

        dict(kop="Hoe laat is het?",
             opdracht="Let op: \"half past three\" is bij ons half vier.",
             oefeningen=[
                 ("rij", [("seven o'clock", "7.00 u"), ("half past nine", "9.30 u"),
                          ("quarter past six", "6.15 u"), ("twenty to five", "4.40 u")],
                  "Schrijf het uur in cijfers.", W),
                 ("open", "Hoe zeg je 10.30 u in het Engels?", "half past ten", 1),
                 ("waar", "\"Quarter past\" betekent kwart voor.", False),
             ]),

        dict(kop="De weg vragen",
             opdracht="Denk aan links en rechts: die twee worden het vaakst verwisseld.",
             oefeningen=[
                 ("rij", [("links", "left"), ("rechts", "right"),
                          ("rechtdoor", "straight on"), ("naast", "next to"),
                          ("tegenover", "opposite")],
                  "Schrijf het Engelse woord.", WW),
                 ("kies", "\"Turn right at the traffic lights.\" Wat doe je?",
                  ["Je slaat linksaf aan de lichten.", "Je slaat rechtsaf aan de lichten.",
                   "Je gaat rechtdoor aan de lichten.", "Je stopt aan de lichten."], 1),
                 ("open", "Iemand vraagt je de weg naar het station. Schrijf één zin in het "
                          "Engels om hem te helpen.",
                  "Bijvoorbeeld: Go straight on and turn left at the church.", 2),
             ]),

        dict(kop="Onderweg en het weer",
             opdracht="Nog een laatste reeks woorden die je overal tegenkomt.",
             oefeningen=[
                 ("rij", [("It's raining.", "Het regent."), ("It's snowing.", "Het sneeuwt."),
                          ("It's windy.", "Het waait."), ("It's sunny.", "De zon schijnt.")],
                  "Wat betekent de zin?", WW),
                 ("rij", [("gisteren", "yesterday"), ("vandaag", "today"),
                          ("morgen", "tomorrow"), ("nu", "now")],
                  "Schrijf het Engelse woord.", WW),
                 ("open", "Je staat in een winkel. Hoe vraag je wat iets kost?",
                  "How much is it? (Ook goed: How much does it cost?)", 1),
                 ("waar", "\"I'm late\" betekent dat je te vroeg bent.", False),
                 ("open", "Vertaal: \"De winkel is naast het station.\"",
                  "The shop is next to the station.", 2),
             ]),
    ],
)
