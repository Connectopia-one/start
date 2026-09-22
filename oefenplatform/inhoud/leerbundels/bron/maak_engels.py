# -*- coding: utf-8 -*-
"""De leerbundels voor Engels, categorie Start (5de en 6de leerjaar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

VAK = "Engels"
BUNDELS = {}

BUNDELS["woorden-voor-elke-dag"] = dict(
    vak=VAK, titel="Woorden voor elke dag",
    onder="De woorden die je het vaakst nodig hebt: getallen, kleuren, dagen, maanden, familie en je lichaam.",
    secties=[
        dict(kop="Tellen", blokken=[
            ("fig", tabel(["1–10", "11–20", "Tientallen"], [
                ["one, two, three, four, five", "eleven, twelve, thirteen", "ten, twenty, thirty"],
                ["six, seven, eight, nine, ten", "fourteen … nineteen, twenty", "forty, fifty, sixty"],
            ]), "Let op het paar dat het vaakst verward wordt: thirteen is 13, thirty is 30."),
            ("p", "Vanaf dertien eindigt bijna alles op <strong>-teen</strong>, en de tientallen op <strong>-ty</strong>. Hoor je het verschil niet, let dan op de klemtoon: thir<em>teen</em>, maar <em>thir</em>ty."),
        ]),
        dict(kop="Kleuren", blokken=[
            ("fig", svg.kleurstalen([
                ("red", "rood", "#c0392b"), ("blue", "blauw", "#2f6fb0"),
                ("yellow", "geel", "#e8b820"), ("green", "groen", "#2f7d4f"),
                ("purple", "paars", "#6c3f97"), ("brown", "bruin", "#7a5230"),
                ("grey", "grijs", "#8d8d8d"), ("pink", "roze", "#e08aa8"),
            ]), "Grey schrijf je in Groot-Brittannië met een e, in Amerika met een a: gray."),
        ]),
        dict(kop="Dagen en maanden", blokken=[
            ("fig", tabel(["Dag", "Nederlands"], [
                ["Monday", "maandag"], ["Tuesday", "dinsdag"], ["Wednesday", "woensdag"],
                ["Thursday", "donderdag"], ["Friday", "vrijdag"],
                ["Saturday", "zaterdag"], ["Sunday", "zondag"],
            ], "70%"), "Wednesday heeft een d die je niet uitspreekt: je zegt ongeveer wensday."),
            ("p", "De maanden: January, February, March, April, May, June, July, August, September, October, November, December."),
            ("weetje", "In het Engels krijgen dagen en maanden <strong>altijd een hoofdletter</strong>. In het Nederlands net niet. Dat is een van de makkelijkste punten om te verdienen op een toets."),
        ]),
        dict(kop="Familie", blokken=[
            ("fig", svg.stamboom(470), "Eén Engels woord, cousin, staat voor neef én nicht."),
            ("p", "Verder: <strong>aunt</strong> is tante, <strong>uncle</strong> is oom, <strong>parents</strong> zijn je ouders en <strong>grandparents</strong> je grootouders."),
        ]),
        dict(kop="Je lichaam", blokken=[
            ("fig", tabel(["Engels", "Nederlands", "Engels", "Nederlands"], [
                ["head", "hoofd", "hand", "hand"],
                ["hair", "haar", "finger", "vinger"],
                ["eye", "oog", "leg", "been"],
                ["ear", "oor", "knee", "knie"],
                ["mouth", "mond", "foot", "voet"],
                ["shoulder", "schouder", "ankle", "enkel"],
            ]), "Foot wordt in het meervoud feet, niet foots."),
        ]),
        dict(kop="Seizoenen en weer", blokken=[
            ("p", "De vier seizoenen: <strong>spring</strong> (lente), <strong>summer</strong> (zomer), <strong>autumn</strong> (herfst) en <strong>winter</strong>."),
            ("p", "Over het weer zeg je: it's raining (het regent), it's snowing (het sneeuwt), it's cold, it's warm, it's windy."),
        ]),
    ],
    onthoud=[
        "thirteen is 13, thirty is 30.",
        "Dagen en maanden krijgen een hoofdletter.",
        "Cousin betekent zowel neef als nicht.",
        "foot wordt feet in het meervoud.",
        "De vier seizoenen: spring, summer, autumn, winter.",
    ])

BUNDELS["mezelf-voorstellen"] = dict(
    vak=VAK, titel="Mezelf voorstellen",
    onder="Zeggen wie je bent, waar je woont en hoe oud je bent — en beleefd blijven.",
    secties=[
        dict(kop="Een eerste gesprek", blokken=[
            ("fig", svg.spreekballonnen([
                ("Sam", "Hello! What is your name?", True),
                ("Lien", "My name is Lien. Nice to meet you.", False),
                ("Sam", "How old are you?", True),
                ("Lien", "I am eleven years old. And you?", False),
            ], 470), "Dit gesprekje bevat bijna alles wat je nodig hebt om jezelf voor te stellen."),
        ]),
        dict(kop="De vier vragen die altijd terugkomen", blokken=[
            ("fig", tabel(["Vraag", "Wat ze vraagt", "Antwoord"], [
                ["What is your name?", "hoe heet je", "My name is …"],
                ["How old are you?", "hoe oud ben je", "I am … years old."],
                ["Where are you from?", "waar kom je vandaan", "I am from Belgium."],
                ["Where do you live?", "waar woon je", "I live in Hasselt."],
            ]), None),
            ("weetje", "In het Nederlands <em>heb</em> je elf jaar, in het Engels <strong>ben</strong> je elf. Zeg dus nooit <em>I have eleven years</em>, maar <strong>I am eleven</strong>."),
        ]),
        dict(kop="Beleefd blijven", blokken=[
            ("fig", tabel(["Engels", "Wanneer"], [
                ["Please", "bij elke vraag — Engelstaligen gebruiken dit veel meer dan wij"],
                ["Thank you", "bij elk bedankje"],
                ["You are welcome", "als antwoord op thank you"],
                ["Sorry / Excuse me", "als je stoort of iets wil vragen"],
                ["Nice to meet you", "als je iemand voor het eerst ontmoet"],
            ]), None),
            ("p", "Een vraag klinkt meteen vriendelijker als je er please aan toevoegt: <strong>Can you spell that, please?</strong>"),
        ]),
        dict(kop="Groeten en afscheid nemen", blokken=[
            ("fig", tabel(["Begroeten", "Afscheid"], [
                ["Hello / Hi", "Goodbye / Bye"],
                ["Good morning (tot de middag)", "See you! (tot ziens)"],
                ["Good afternoon (in de namiddag)", "See you tomorrow!"],
                ["Good evening (’s avonds)", "Good night (bij het slapengaan)"],
            ]), "Good night is dus géén begroeting: dat zeg je pas als je gaat slapen."),
        ]),
        dict(kop="Over iemand anders praten", blokken=[
            ("fig", svg.persoonsvormen([
                ("een jongen|of man", "his", svg.FOREST),
                ("een meisje|of vrouw", "her", svg.AMBER),
                ("iets|of een dier", "its", "#3b6ea5"),
            ], 400), "This is my sister. Her name is Emma."),
            ("p", "Praat je over jezelf, dan is het <strong>my</strong>: my name, my school, my dog."),
        ]),
    ],
    onthoud=[
        "I am eleven — niet I have eleven years.",
        "My name is … / I am from … / I live in …",
        "Please en thank you gebruik je vaker dan in het Nederlands.",
        "Good night zeg je bij het slapengaan, niet bij het begroeten.",
        "his voor een jongen, her voor een meisje, my voor jezelf.",
    ])

BUNDELS["to-be-en-to-have"] = dict(
    vak=VAK, titel="To be en to have",
    onder="De twee werkwoorden die je in bijna elke Engelse zin nodig hebt.",
    secties=[
        dict(kop="To be — zijn", blokken=[
            ("fig", svg.persoonsvormen([
                ("I", "am", svg.FOREST),
                ("he|she|it", "is", svg.AMBER),
                ("we|you|they", "are", "#3b6ea5"),
            ], 470), "Am hoort alleen bij I. Dat is de enige plek waar het staat."),
            ("p", "Een naam of een zelfstandig naamwoord vervang je in je hoofd door he, she, it of they. <em>My brother</em> is he, dus: my brother <strong>is</strong>. <em>My parents</em> zijn they, dus: my parents <strong>are</strong>."),
        ]),
        dict(kop="Korte vormen", blokken=[
            ("fig", tabel(["Volledig", "Kort", "Ontkennend"], [
                ["I am", "I'm", "I'm not"],
                ["he is", "he's", "he isn't"],
                ["we are", "we're", "we aren't"],
                ["they are", "they're", "they aren't"],
            ]), "De apostrof vervangt de letter die wegvalt."),
            ("weetje", "Let op drie woorden die hetzelfde klinken: <strong>they're</strong> (zij zijn), <strong>their</strong> (hun) en <strong>there</strong> (daar). En <strong>it's</strong> is it is, terwijl <strong>its</strong> zonder apostrof zijn of haar betekent."),
        ]),
        dict(kop="Vragen en ontkennen met to be", blokken=[
            ("p", "Bij to be is het makkelijk: voor een vraag draai je gewoon om, voor een ontkenning zet je <strong>not</strong> erachter."),
            ("fig", svg.stappen(["You are ready.|gewone zin", "Are you ready?|omdraaien", "You aren't ready.|not erachter"]),
             "Je hebt hier geen do of does voor nodig."),
        ]),
        dict(kop="To have — hebben", blokken=[
            ("fig", svg.persoonsvormen([
                ("I|we|you|they", "have", svg.FOREST),
                ("he|she|it", "has", svg.AMBER),
            ], 380), "Alleen bij he, she en it wordt have een has."),
            ("p", "Je hoort ook vaak <strong>have got</strong>: I have got a new bike betekent gewoon hetzelfde als I have a new bike."),
        ]),
        dict(kop="Vragen en ontkennen met to have", blokken=[
            ("p", "Hier heb je wél do of does nodig, want to have is een gewoon werkwoord."),
            ("fig", tabel(["", "Vraag", "Ontkenning"], [
                ["I / we / you / they", "Do you have a pen?", "I don't have a pen."],
                ["he / she / it", "Does she have a pen?", "She doesn't have a pen."],
            ]), "Na does of doesn't wordt has weer gewoon have."),
        ]),
    ],
    onthoud=[
        "I am, he/she/it is, we/you/they are.",
        "I/we/you/they have, he/she/it has.",
        "Bij to be draai je om voor een vraag en zet je not erachter.",
        "Bij to have gebruik je do of does.",
        "it's = it is, its = zijn of haar.",
    ])

BUNDELS["de-tegenwoordige-tijd"] = dict(
    vak=VAK, titel="De tegenwoordige tijd",
    onder="Praten over wat je altijd, vaak of nooit doet — en die lastige -s.",
    secties=[
        dict(kop="Wanneer gebruik je ze?", blokken=[
            ("p", "De tegenwoordige tijd gebruik je voor iets dat telkens opnieuw gebeurt, of dat gewoon waar is. <em>We watch television every evening. I live in Genk.</em>"),
            ("p", "Woorden die je waarschuwen dat je ze nodig hebt: <strong>always</strong> (altijd), <strong>often</strong> (vaak), <strong>sometimes</strong> (soms), <strong>never</strong> (nooit), <strong>every day</strong>."),
        ]),
        dict(kop="De regel van de -s", blokken=[
            ("fig", svg.persoonsvormen([
                ("I|we|you|they", "play", svg.FOREST),
                ("he|she|it", "plays", svg.AMBER),
            ], 380), "Alleen bij he, she en it komt er een -s bij. Dat is de fout die het vaakst gemaakt wordt."),
            ("fig", tabel(["Eindigt het werkwoord op…", "Dan", "Voorbeeld"], [
                ["de meeste letters", "-s erbij", "work → works"],
                ["-ch, -sh, -s, -x, -o", "-es erbij", "watch → watches, go → goes"],
                ["medeklinker + -y", "y wordt ies", "study → studies"],
                ["klinker + -y", "gewoon -s", "play → plays"],
            ]), None),
        ]),
        dict(kop="Vragen stellen", blokken=[
            ("fig", svg.persoonsvormen([
                ("I|we|you|they", "Do …?", svg.FOREST),
                ("he|she|it", "Does …?", svg.AMBER),
            ], 380), "Do you like pizza? · Does he speak English?"),
            ("weetje", "Na <strong>does</strong> valt de -s van het werkwoord weg. De -s zit dan al in does. Dus: <em>Does she like music?</em> en niet <em>Does she likes music?</em>"),
        ]),
        dict(kop="Ontkennen", blokken=[
            ("fig", tabel(["", "Ontkenning", "Voorbeeld"], [
                ["I / we / you / they", "don't", "I don't like sport."],
                ["he / she / it", "doesn't", "He doesn't know the answer."],
            ]), "Ook hier: na doesn't geen -s meer aan het werkwoord."),
            ("p", "Staat er al <strong>never</strong> in de zin, dan heb je geen don't meer nodig: <em>I never eat fish.</em>"),
        ]),
        dict(kop="Alles op een rij", blokken=[
            ("fig", tabel(["", "Gewone zin", "Vraag", "Ontkenning"], [
                ["you", "You play.", "Do you play?", "You don't play."],
                ["he", "He plays.", "Does he play?", "He doesn't play."],
            ]), "Merk op dat de -s telkens maar op één plaats tegelijk staat."),
        ]),
    ],
    onthoud=[
        "Bij he, she en it komt er -s achter het werkwoord.",
        "-ch, -sh, -s, -x en -o krijgen -es.",
        "Medeklinker + y wordt -ies: study → studies.",
        "Do bij I/we/you/they, does bij he/she/it.",
        "Na does en doesn't valt de -s weg.",
    ])

BUNDELS["zinnen-bouwen"] = dict(
    vak=VAK, titel="Zinnen bouwen",
    onder="De volgorde van de woorden, meervouden, lidwoorden en vraagwoorden.",
    secties=[
        dict(kop="De volgorde van een zin", blokken=[
            ("fig", svg.woordvolgorde([
                ("wie", "I", "#2f5d50"), ("doet", "go", "#c17f2b"),
                ("wat/waar", "to school", "#3b6ea5"), ("wanneer", "every day", "#6b7260"),
            ], 470), "I go to school every day — de tijd komt achteraan, niet in het midden."),
            ("p", "Dat is meteen het verschil met het Nederlands. Wij zeggen <em>Ik ga elke dag naar school</em>, maar in het Engels komt <strong>every day</strong> op het einde."),
        ]),
        dict(kop="Meervouden", blokken=[
            ("fig", tabel(["Regel", "Voorbeeld"], [
                ["meestal -s erbij", "book → books"],
                ["na -s, -x, -ch, -sh: -es", "box → boxes, watch → watches"],
                ["medeklinker + y wordt ies", "city → cities"],
                ["onregelmatig", "child → children, man → men, woman → women"],
                ["onregelmatig", "foot → feet, tooth → teeth, mouse → mice"],
            ]), "Die laatste twee rijen moet je gewoon vanbuiten leren; er zit geen regel achter."),
        ]),
        dict(kop="a, an en the", blokken=[
            ("p", "Gebruik <strong>a</strong> voor een medeklinkerklank en <strong>an</strong> voor een klinkerklank: a book, a school, maar <strong>an</strong> apple, <strong>an</strong> hour."),
            ("weetje", "Het gaat om de <em>klank</em>, niet om de letter. Hour begint met een h die je niet hoort, dus an hour. En university begint met een joe-klank, dus a university."),
            ("p", "<strong>The</strong> gebruik je als het duidelijk is over welk ding het gaat: <em>the book on the table</em>."),
        ]),
        dict(kop="Van wie is het?", blokken=[
            ("p", "In het Engels hang je een <strong>'s</strong> aan de naam: <em>Sarah's bike</em> is de fiets van Sarah, <em>my mother's car</em> is de auto van mijn moeder."),
            ("p", "Dat is korter dan bij ons, en het staat vooraan in plaats van achteraan."),
        ]),
        dict(kop="Vraagwoorden", blokken=[
            ("fig", tabel(["Vraagwoord", "Vraagt naar", "Voorbeeld"], [
                ["What", "een ding", "What is your name?"],
                ["Who", "een persoon", "Who is that?"],
                ["Where", "een plaats", "Where do you live?"],
                ["When", "een tijdstip", "When does it start?"],
                ["Why", "een reden", "Why are you late?"],
                ["How", "een manier", "How do you say that?"],
                ["Whose", "van wie iets is", "Whose bag is this?"],
            ]), "Zes van de zeven beginnen met wh. Handig geheugensteuntje."),
        ]),
        dict(kop="Bijvoeglijke naamwoorden", blokken=[
            ("p", "Die staan voor het zelfstandig naamwoord, net als bij ons: <em>a red car</em>, <em>an old house</em>. En ze krijgen nooit een meervoud-s: <em>two red cars</em>, niet <em>two reds cars</em>."),
            ("p", "Let ook op vaste combinaties: het is <strong>good at</strong> English, niet good in English."),
        ]),
    ],
    onthoud=[
        "Wie — doet — wat/waar — wanneer. De tijd komt achteraan.",
        "Na -s, -x, -ch en -sh krijgt het meervoud -es.",
        "children, men, women, feet en teeth zijn onregelmatig.",
        "a of an hangt af van de klank, niet van de letter.",
        "'s toont van wie iets is: Sarah's bike.",
        "Bijvoeglijke naamwoorden krijgen nooit een -s.",
    ])

BUNDELS["op-school-en-onderweg"] = dict(
    vak=VAK, titel="Op school en onderweg",
    onder="Taal die je meteen kan gebruiken: in de klas, op straat en in de winkel.",
    secties=[
        dict(kop="In de klas", blokken=[
            ("fig", tabel(["Wat de leerkracht zegt", "Wat het betekent"], [
                ["Open your book.", "Open je boek."],
                ["Close your book.", "Sluit je boek."],
                ["Listen carefully.", "Luister goed."],
                ["Work in pairs.", "Werk per twee."],
                ["Put up your hand.", "Steek je hand op."],
                ["Homework for tomorrow.", "Huiswerk tegen morgen."],
            ]), "Homework blijft altijd enkelvoud: nooit homeworks."),
            ("fig", tabel(["Wat jij zegt", "Wanneer"], [
                ["I don't understand.", "je begrijpt het niet"],
                ["Could you repeat that, please?", "je wil het nog eens horen"],
                ["Can you spell that, please?", "je wil weten hoe het geschreven wordt"],
                ["Can I go to the toilet, please?", "je moet naar het toilet"],
                ["Sorry, I'm late.", "je komt te laat binnen"],
            ]), "Deze vijf zinnen redden je door elk Engels lesuur."),
        ]),
        dict(kop="Spullen op je bank", blokken=[
            ("fig", tabel(["Engels", "Nederlands", "Engels", "Nederlands"], [
                ["pen", "pen", "schoolbag", "boekentas"],
                ["pencil", "potlood", "desk", "bank"],
                ["rubber", "gom", "board", "bord"],
                ["ruler", "lat", "teacher", "leerkracht"],
            ]), "In Amerika zeggen ze eraser in plaats van rubber, en backpack in plaats van schoolbag."),
        ]),
        dict(kop="Hoe laat is het?", blokken=[
            ("fig", svg.naast_elkaar([svg.klok(3, 30), svg.klok(7, 45), svg.klok(8, 15)]),
             "half past three · quarter to eight · quarter past eight"),
            ("p", "Let goed op: <strong>half past three</strong> is half vier bij ons, dus 3.30 u. In het Engels tel je vanaf het uur dat <em>voorbij</em> is, bij ons vanaf het uur dat komt."),
            ("weetje", "Voor de minuten ertussen zeg je past tot en met de helft, en to daarna: ten past four (4.10 u), ten to five (4.50 u)."),
        ]),
        dict(kop="De weg vragen", blokken=[
            ("fig", svg.plattegrond(470), "Opposite betekent tegenover, next to betekent naast."),
            ("fig", tabel(["Engels", "Nederlands"], [
                ["Go straight on.", "Ga rechtdoor."],
                ["Turn left / turn right.", "Sla links / rechts af."],
                ["It's next to the bakery.", "Het is naast de bakker."],
                ["It's opposite the church.", "Het is tegenover de kerk."],
                ["Excuse me, where is the station?", "Pardon, waar is het station?"],
            ]), None),
        ]),
        dict(kop="In de winkel", blokken=[
            ("fig", svg.spreekballonnen([
                ("You", "Excuse me, how much is it?", True),
                ("Shop", "It's four pounds fifty.", False),
                ("You", "Here you are. Thank you.", True),
            ], 470), "How much is it? gaat over de prijs, niet over de hoeveelheid."),
        ]),
        dict(kop="Vandaag, morgen, gisteren", blokken=[
            ("fig", svg.woordvolgorde([
                ("gisteren", "yesterday", "#6b7260"),
                ("vandaag", "today", "#2f5d50"),
                ("morgen", "tomorrow", "#c17f2b"),
            ], 400), "Tomorrow is morgen — niet gisteren, hoe verwarrend het ook klinkt."),
        ]),
    ],
    onthoud=[
        "I don't understand en Could you repeat that? gebruik je het vaakst.",
        "Homework is altijd enkelvoud.",
        "half past three is 3.30 u, dus half vier.",
        "past tot de helft van het uur, to daarna.",
        "left is links, right is rechts, straight on is rechtdoor.",
        "yesterday — today — tomorrow.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)
