# -*- coding: utf-8 -*-
"""De wisselende woorden bij de grammaticahoofdstukken van Engels, 🚀 Boost.

Zeven thema's, elk deel 1 en deel 2: de naamwoorden en lidwoorden, de
voornaamwoorden, de bijvoeglijke naamwoorden en bijwoorden, de tegenwoordige
tijden, de verleden en toekomende tijden, de modale werkwoorden en de
zinsbouw. Daar zit de leerstof in de **regel**, dus mag het woord wisselen.

De hoofdstukken over teksten, woordvelden, cultuur en schrijven blijven staan
zoals ze staan: daar is het woord zelf de leerstof.

Een variant noemt alleen wat verandert. Waar de uitleg het woord zelf noemt,
schrijft de variant ook een eigen uitleg.
"""

HOOFDSTUKKEN = {
    "Nouns, articles, quantifiers en numerals — deel 1": {
        "Wat is het meervoud van 'child'?": [
            {
                "vraag": "Wat is het meervoud van 'man'?",
                "opties": ["men", "mans", "manes", "mens"],
                "uitleg": "Men is onregelmatig en heeft zelf al geen s nodig. Mens bestaat niet als meervoud van man.",
            },
            {
                "vraag": "Wat is het meervoud van 'foot'?",
                "opties": ["feet", "foots", "footes", "feets"],
                "uitleg": "Feet is onregelmatig en heeft zelf al geen s nodig. Feets bestaat niet.",
            },
            {
                "vraag": "Wat is het meervoud van 'tooth'?",
                "opties": ["teeth", "tooths", "toothes", "teeths"],
                "uitleg": "Teeth is onregelmatig en heeft zelf al geen s nodig. Teeths bestaat niet.",
            },
        ],
        "Welke van deze meervouden zijn onregelmatig?": [
            {
                "opties": ["men", "women", "children", "tables"],
                "antwoord": [0, 1, 2],
                "uitleg": "Man wordt men, woman wordt women en child wordt children. Table krijgt gewoon een s.",
            },
            {
                "opties": ["geese", "oxen", "people", "chairs"],
                "antwoord": [0, 1, 2],
                "uitleg": "Goose wordt geese, ox wordt oxen en person wordt people. Chair krijgt gewoon een s.",
            },
            {
                "opties": ["mice", "feet", "men", "phones"],
                "antwoord": [0, 1, 2],
                "uitleg": "Mouse wordt mice, foot wordt feet en man wordt men. Phone krijgt gewoon een s.",
            },
        ],
        "Schrijf het Engelse meervoud van 'woman'.": [
            {
                "vraag": "Schrijf het Engelse meervoud van 'man'.",
                "antwoord": ["men"],
                "uitleg": "Man wordt men. Je hoort het verschil vooral in de eerste klank.",
            },
            {
                "vraag": "Schrijf het Engelse meervoud van 'mouse'.",
                "antwoord": ["mice"],
                "uitleg": "Mouse wordt mice. Mouses bestaat niet.",
            },
            {
                "vraag": "Schrijf het Engelse meervoud van 'goose'.",
                "antwoord": ["geese"],
                "uitleg": "Goose wordt geese, net zoals foot feet wordt.",
            },
        ],
        "Wat is het meervoud van 'city'?": [
            {
                "vraag": "Wat is het meervoud van 'baby'?",
                "opties": ["babies", "babys", "babyes", "baby"],
                "uitleg": "Een y na een medeklinker wordt ies. Staat er een klinker voor de y, dan blijft ze staan: boy wordt boys.",
            },
            {
                "vraag": "Wat is het meervoud van 'country'?",
                "opties": ["countries", "countrys", "countryes", "country"],
                "uitleg": "Een y na een medeklinker wordt ies. Staat er een klinker voor de y, dan blijft ze staan: day wordt days.",
            },
            {
                "vraag": "Wat is het meervoud van 'party'?",
                "opties": ["parties", "partys", "partyes", "party"],
                "uitleg": "Een y na een medeklinker wordt ies. Staat er een klinker voor de y, dan blijft ze staan: key wordt keys.",
            },
        ],
        "Het meervoud van 'boy' is 'boies'.": [
            {
                "vraag": "Het meervoud van 'day' is 'daies'.",
                "uitleg": "Het is days. De regel met ies geldt alleen als er een medeklinker voor de y staat, zoals in baby en city.",
            },
            {
                "vraag": "Het meervoud van 'key' is 'kies'.",
                "uitleg": "Het is keys. Voor de y staat een klinker, dus blijft ze staan.",
            },
            {
                "vraag": "Het meervoud van 'toy' is 'toies'.",
                "uitleg": "Het is toys. Voor de y staat een klinker, dus blijft ze staan.",
            },
        ],
        "Wat is het meervoud van 'knife'?": [
            {
                "vraag": "Wat is het meervoud van 'wolf'?",
                "opties": ["wolves", "wolfs", "wolfes", "wolve"],
                "uitleg": "Woorden op f of fe krijgen vaak ves: life wordt lives, knife wordt knives. Een paar houden hun f: roof wordt roofs.",
            },
            {
                "vraag": "Wat is het meervoud van 'leaf'?",
                "opties": ["leaves", "leafs", "leafes", "leave"],
                "uitleg": "Woorden op f of fe krijgen vaak ves: life wordt lives, wolf wordt wolves. Een paar houden hun f: roof wordt roofs.",
            },
            {
                "vraag": "Wat is het meervoud van 'shelf'?",
                "opties": ["shelves", "shelfs", "shelfes", "shelve"],
                "uitleg": "Woorden op f of fe krijgen vaak ves: life wordt lives, leaf wordt leaves. Een paar houden hun f: roof wordt roofs.",
            },
        ],
        "Welke woorden blijven in het meervoud precies hetzelfde?": [
            {
                "opties": ["deer", "aircraft", "species", "dog"],
                "antwoord": [0, 1, 2],
                "uitleg": "One deer, two deer. Dog wordt gewoon dogs.",
            },
            {
                "opties": ["sheep", "salmon", "means", "cat"],
                "antwoord": [0, 1, 2],
                "uitleg": "One sheep, two sheep. Cat wordt gewoon cats.",
            },
            {
                "opties": ["fish", "offspring", "series", "bird"],
                "antwoord": [0, 1, 2],
                "uitleg": "One fish, two fish. Bird wordt gewoon birds.",
            },
        ],
        "Schrijf het Engelse meervoud van 'tomato'.": [
            {
                "vraag": "Schrijf het Engelse meervoud van 'potato'.",
                "antwoord": ["potatoes"],
                "uitleg": "Een paar woorden op o krijgen es: tomatoes, potatoes, heroes. De meeste andere krijgen alleen een s: photos, pianos.",
            },
            {
                "vraag": "Schrijf het Engelse meervoud van 'hero'.",
                "antwoord": ["heroes"],
                "uitleg": "Een paar woorden op o krijgen es: tomatoes, potatoes, heroes. De meeste andere krijgen alleen een s: photos, pianos.",
            },
            {
                "vraag": "Schrijf het Engelse meervoud van 'photo'.",
                "antwoord": ["photos"],
                "uitleg": "Photo hoort bij de groep die alleen een s krijgt, net als pianos. Tomato en potato krijgen wel es.",
            },
        ],
        "Welke woorden zijn in het Engels ontelbaar?": [
            {
                "opties": ["luggage", "information", "bread", "table"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij deze drie gebruik je much en little. Table is telbaar: one table, two tables.",
            },
            {
                "opties": ["music", "water", "homework", "book"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij deze drie gebruik je much en little. Book is telbaar: one book, two books.",
            },
            {
                "opties": ["weather", "rice", "knowledge", "cup"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij deze drie gebruik je much en little. Cup is telbaar: one cup, two cups.",
            },
        ],
        "In welke zin staat een samengesteld naamwoord in de juiste vorm?": [
            {
                "opties": [
                    "I bought two shoeboxes.",
                    "I bought two shoesbox.",
                    "I bought two shoebox.",
                    "I bought two shoesboxes.",
                ],
            },
            {
                "opties": [
                    "She has three bookshelves.",
                    "She has three booksshelf.",
                    "She has three bookshelf.",
                    "She has three booksshelves.",
                ],
            },
            {
                "opties": [
                    "We need two toothpicks.",
                    "We need two teethpick.",
                    "We need two toothpick.",
                    "We need two teethpicks.",
                ],
            },
        ],
        "Het woord 'people' is het meervoud van 'person' en krijgt dus geen extra s.": [
            {
                "vraag": "Je zegt three people en niet three peoples.",
                "uitleg": "Peoples bestaat wel, maar dan bedoel je volkeren.",
            },
            {
                "vraag": "'Police' vraagt in het Engels een werkwoord in het meervoud: the police are here.",
                "uitleg": "Police, people en cattle zijn meervoud zonder s.",
            },
            {
                "vraag": "'Children' is al meervoud en krijgt geen extra s.",
                "uitleg": "Childrens bestaat niet, net zoals peoples niet het meervoud van person is.",
            },
        ],
        "Wat is het meervoud van 'analysis'?": [
            {
                "vraag": "Wat is het meervoud van 'crisis'?",
                "opties": ["crises", "crisises", "crisis", "crisis's"],
                "uitleg": "Woorden op -is krijgen -es met een lange e: analysis wordt analyses, basis wordt bases.",
            },
            {
                "vraag": "Wat is het meervoud van 'basis'?",
                "opties": ["bases", "basises", "basis", "basis's"],
                "uitleg": "Woorden op -is krijgen -es met een lange e: crisis wordt crises, analysis wordt analyses.",
            },
            {
                "vraag": "Wat is het meervoud van 'hypothesis'?",
                "opties": ["hypotheses", "hypothesises", "hypothesis", "hypothesis's"],
                "uitleg": "Woorden op -is krijgen -es met een lange e: crisis wordt crises, basis wordt bases.",
            },
        ],
    },
    "Nouns, articles, quantifiers en numerals — deel 2": {
        "Welk lidwoord hoort voor 'hour': … hour?": [
            {
                "vraag": "Welk lidwoord hoort voor 'honest answer': … honest answer?",
                "uitleg": "Je kiest a of an op de klank, niet op de letter. De h van honest zwijgt, dus je hoort een klinker.",
            },
            {
                "vraag": "Welk lidwoord hoort voor 'umbrella': … umbrella?",
                "uitleg": "Je kiest a of an op de klank, niet op de letter. Umbrella begint met een klinkerklank.",
            },
            {
                "vraag": "Welk lidwoord hoort voor 'orange': … orange?",
                "uitleg": "Je kiest a of an op de klank, niet op de letter. Orange begint met een klinkerklank.",
            },
        ],
        "Voor welke woorden hoort 'an'?": [
            {
                "opties": ["egg", "hour", "old car", "European city"],
                "antwoord": [0, 1, 2],
                "uitleg": "European begint met de klank you, dus a European city. Hour begint met een klinkerklank, dus an hour.",
            },
            {
                "opties": ["idea", "honest answer", "engineer", "uniform"],
                "antwoord": [0, 1, 2],
                "uitleg": "Uniform begint met de klank you, dus a uniform. Honest begint met een klinkerklank, dus an honest answer.",
            },
            {
                "opties": ["orange", "island", "hour", "user"],
                "antwoord": [0, 1, 2],
                "uitleg": "User begint met de klank you, dus a user. De drie andere beginnen met een klinkerklank.",
            },
        ],
        "Vul het juiste lidwoord in: she is … engineer.": [
            {
                "vraag": "Vul het juiste lidwoord in: he is … architect.",
                "antwoord": ["an"],
                "uitleg": "Architect begint met een klinkerklank. Bij een beroep hoort in het Engels altijd een lidwoord.",
            },
            {
                "vraag": "Vul het juiste lidwoord in: she is … nurse.",
                "antwoord": ["a"],
                "uitleg": "Nurse begint met een medeklinkerklank, dus a. Bij een beroep hoort in het Engels altijd een lidwoord.",
            },
            {
                "vraag": "Vul het juiste lidwoord in: he is … honest man.",
                "antwoord": ["an"],
                "uitleg": "De h van honest zwijgt, dus je hoort een klinker. Bij een beroep of een omschrijving hoort een lidwoord.",
            },
        ],
        "In welke zin staat 'the' terecht?": [
            {
                "opties": [
                    "The film we saw last night was great.",
                    "The films are my favourite thing.",
                    "I like the sport in general.",
                    "He studies the physics.",
                ],
                "uitleg": "The gebruik je als je een bepaald exemplaar bedoelt. Spreek je algemeen over films, sport of een vak, dan zet je er niets voor.",
            },
            {
                "opties": [
                    "The song you played was lovely.",
                    "The songs are the best thing there is.",
                    "I like the food in general.",
                    "She teaches the maths.",
                ],
                "uitleg": "The gebruik je als je een bepaald exemplaar bedoelt. Spreek je algemeen over liedjes, eten of een vak, dan zet je er niets voor.",
            },
            {
                "opties": [
                    "The letter she wrote was long.",
                    "The letters are my favourite thing.",
                    "I like the art in general.",
                    "He studies the chemistry.",
                ],
                "uitleg": "The gebruik je als je een bepaald exemplaar bedoelt. Spreek je algemeen over brieven, kunst of een vak, dan zet je er niets voor.",
            },
        ],
        "Voor een taal of een schoolvak zet je in het Engels meestal geen lidwoord: I study history.": [
            {
                "vraag": "Je zegt 'I speak English' en niet 'I speak the English'.",
                "uitleg": "Met the erbij bedoel je een bepaald deel: the English of Shakespeare.",
            },
            {
                "vraag": "Voor een schoolvak zoals maths zet je meestal geen lidwoord.",
                "uitleg": "I like maths, I study history. Met the erbij bedoel je een bepaald deel.",
            },
            {
                "vraag": "Je zegt 'I study biology' zonder lidwoord.",
                "uitleg": "Talen en schoolvakken krijgen geen lidwoord, tenzij je een bepaald deel bedoelt.",
            },
        ],
        "Welk woord past: how … water do you need?": [
            {
                "vraag": "Welk woord past: how … sugar do you need?",
                "uitleg": "Much hoort bij ontelbare woorden, many bij telbare. Sugar is ontelbaar.",
            },
            {
                "vraag": "Welk woord past: how … money do you need?",
                "uitleg": "Much hoort bij ontelbare woorden, many bij telbare. Money is ontelbaar.",
            },
            {
                "vraag": "Welk woord past: how … time do you need?",
                "uitleg": "Much hoort bij ontelbare woorden, many bij telbare. Time is ontelbaar.",
            },
        ],
        "Welke woorden horen bij een telbaar naamwoord in het meervoud?": [
            {
                "opties": ["many", "both", "several", "little"],
                "antwoord": [0, 1, 2],
                "uitleg": "Little hoort bij ontelbare woorden: little time, little money. A lot of past bij allebei.",
            },
            {
                "opties": ["a few", "several", "fewer", "much"],
                "antwoord": [0, 1, 2],
                "uitleg": "Much hoort bij ontelbare woorden: much time, much money. A lot of past bij allebei.",
            },
            {
                "opties": ["many", "a couple of", "several", "a little"],
                "antwoord": [0, 1, 2],
                "uitleg": "A little hoort bij ontelbare woorden: a little sugar. A lot of past bij allebei.",
            },
        ],
        "Vul aan met één woord: I don't have … time left.": [
            {
                "vraag": "Vul aan met één woord: I don't have … money left.",
                "antwoord": ["much"],
                "uitleg": "Money is ontelbaar, dus much. In een gewone bevestigende zin zeg je liever a lot of money.",
            },
            {
                "vraag": "Vul aan met één woord: there isn't … milk left.",
                "antwoord": ["much"],
                "uitleg": "Milk is ontelbaar, dus much. In een gewone bevestigende zin zeg je liever a lot of milk.",
            },
            {
                "vraag": "Vul aan met één woord: I don't have … friends here.",
                "antwoord": ["many"],
                "uitleg": "Friends is telbaar en staat in het meervoud, dus many.",
            },
        ],
        "'A few' en 'a little' betekenen hetzelfde en je mag ze door elkaar gebruiken.": [
            {
                "vraag": "'Many' en 'much' betekenen hetzelfde en je mag ze door elkaar gebruiken.",
                "uitleg": "Many hoort bij telbare woorden (many friends) en much bij ontelbare (much sugar).",
            },
            {
                "vraag": "Je mag 'a little sugar' en 'a few sugar' allebei zeggen.",
                "uitleg": "A little hoort bij ontelbare woorden. A few hoort bij telbare: a few friends.",
            },
            {
                "vraag": "'Few' en 'little' horen bij hetzelfde soort naamwoord.",
                "uitleg": "Few hoort bij telbare woorden en little bij ontelbare.",
            },
        ],
        "Welke zin vraagt correct naar een rest melk?": [
            {
                "vraag": "Welke zin vraagt correct naar een rest brood?",
                "opties": [
                    "Is there any bread left?",
                    "Is there some bread left?",
                    "Is there many bread left?",
                    "Is there a few bread left?",
                ],
            },
            {
                "vraag": "Welke zin vraagt correct naar een rest suiker?",
                "opties": [
                    "Is there any sugar left?",
                    "Is there some sugar left?",
                    "Is there many sugar left?",
                    "Is there a few sugar left?",
                ],
            },
            {
                "vraag": "Welke zin vraagt correct naar een rest soep?",
                "opties": [
                    "Is there any soup left?",
                    "Is there some soup left?",
                    "Is there many soup left?",
                    "Is there a few soup left?",
                ],
            },
        ],
        "Hoe schrijf je het rangtelwoord bij 3?": [
            {
                "vraag": "Hoe schrijf je het rangtelwoord bij 5?",
                "opties": ["fifth", "fiveth", "fifeth", "fived"],
                "uitleg": "First, second en third zijn onregelmatig. Bij five valt de ve weg: fifth.",
            },
            {
                "vraag": "Hoe schrijf je het rangtelwoord bij 9?",
                "opties": ["ninth", "nineth", "ninethe", "nined"],
                "uitleg": "Bij nine valt de e weg: ninth. Vanaf vier komt er gewoon th bij: fourth, sixth.",
            },
            {
                "vraag": "Hoe schrijf je het rangtelwoord bij 2?",
                "opties": ["second", "twoth", "twoeth", "twod"],
                "uitleg": "First, second en third zijn onregelmatig. Vanaf vier komt er gewoon th bij: fourth, fifth, sixth.",
            },
        ],
        "Welke rangtelwoorden zijn juist geschreven?": [
            {
                "opties": ["fifth", "twentieth", "thirty-second", "nineth"],
                "antwoord": [0, 1, 2],
                "uitleg": "Nine wordt ninth, niet nineth. Bij twenty wordt de y een ie: twentieth.",
            },
            {
                "opties": ["twelfth", "thirtieth", "forty-third", "twoth"],
                "antwoord": [0, 1, 2],
                "uitleg": "Two wordt second, niet twoth. Twelve wordt twelfth, met een f.",
            },
            {
                "opties": ["eighth", "ninetieth", "sixty-fourth", "threeth"],
                "antwoord": [0, 1, 2],
                "uitleg": "Three wordt third, niet threeth. Eight wordt eighth, met maar één t.",
            },
        ],
    },
    "Pronouns: de zeven soorten — deel 1": {
        "Welke zin over een bezoek aan de cinema is juist?": [
            {
                "vraag": "Welke zin over een bezoek aan het feest is juist?",
                "opties": [
                    "He and I went to the party.",
                    "Him and me went to the party.",
                    "He and me went to the party.",
                    "Him and I went to the party.",
                ],
                "uitleg": "Wie de handeling doet, staat in de onderwerpsvorm: I, you, he, she, we, they. Laat de andere persoon even weg en je hoort het: I went, niet me went.",
            },
            {
                "vraag": "Welke zin over een bezoek aan het museum is juist?",
                "opties": [
                    "She and I visited the museum.",
                    "Her and me visited the museum.",
                    "She and me visited the museum.",
                    "Her and I visited the museum.",
                ],
                "uitleg": "Wie de handeling doet, staat in de onderwerpsvorm. Laat de andere persoon even weg en je hoort het: I visited, niet me visited.",
            },
            {
                "vraag": "Welke zin over een wandeling naar huis is juist?",
                "opties": [
                    "My brother and I walked home.",
                    "My brother and me walked home.",
                    "Me and my brother walks home.",
                    "My brother and me walks home.",
                ],
                "uitleg": "Wie de handeling doet, staat in de onderwerpsvorm. Laat de andere persoon even weg en je hoort het: I walked, niet me walked.",
            },
        ],
        "Welke woorden zijn voorwerpsvormen van het persoonlijk voornaamwoord?": [
            {
                "opties": ["her", "us", "them", "we"],
                "antwoord": [0, 1, 2],
                "uitleg": "De voorwerpsvormen zijn me, you, him, her, it, us, them. We is een onderwerpsvorm.",
            },
            {
                "opties": ["him", "us", "me", "he"],
                "antwoord": [0, 1, 2],
                "uitleg": "De voorwerpsvormen zijn me, you, him, her, it, us, them. He is een onderwerpsvorm.",
            },
            {
                "opties": ["them", "her", "us", "she"],
                "antwoord": [0, 1, 2],
                "uitleg": "De voorwerpsvormen zijn me, you, him, her, it, us, them. She is een onderwerpsvorm.",
            },
        ],
        "Vul het juiste voornaamwoord in: my parents called … yesterday, en het gaat over jezelf.": [
            {
                "vraag": "Vul het juiste voornaamwoord in: the teacher helped … after class, en het gaat over jezelf.",
                "antwoord": ["me"],
                "uitleg": "Na het werkwoord staat de voorwerpsvorm. Het onderwerp van die zin is the teacher.",
            },
            {
                "vraag": "Vul het juiste voornaamwoord in: I saw … at the station, en het gaat over Tom.",
                "antwoord": ["him"],
                "uitleg": "Na het werkwoord staat de voorwerpsvorm: him, niet he.",
            },
            {
                "vraag": "Vul het juiste voornaamwoord in: she thanked … for the help, en het gaat over jou en mij.",
                "antwoord": ["us"],
                "uitleg": "Na het werkwoord staat de voorwerpsvorm: us, niet we.",
            },
        ],
        "Na een voorzetsel gebruik je in het Engels de voorwerpsvorm: this is for her.": [
            {
                "vraag": "Je zegt 'between you and me' en niet 'between you and I'.",
                "uitleg": "Na een voorzetsel staat de voorwerpsvorm, hoe deftig 'and I' ook klinkt.",
            },
            {
                "vraag": "Na een voorzetsel staat 'him' en niet 'he': I went with him.",
                "uitleg": "Voorzetsels nemen altijd de voorwerpsvorm: me, you, him, her, it, us, them.",
            },
            {
                "vraag": "'This present is for us' is juist.",
                "uitleg": "Na for staat de voorwerpsvorm us, niet we.",
            },
        ],
        "Welke zin vraagt correct van wie een boek is?": [
            {
                "vraag": "Welke zin vraagt correct van wie een tas is?",
                "opties": [
                    "Is this her bag?",
                    "Is this hers bag?",
                    "Is this she bag?",
                    "Is this her's bag?",
                ],
                "uitleg": "Her staat voor een naamwoord. Hers staat alleen: is this bag hers? En hers schrijf je nooit met een apostrof.",
            },
            {
                "vraag": "Welke zin vraagt correct van wie een auto is?",
                "opties": [
                    "Is this their car?",
                    "Is this theirs car?",
                    "Is this them car?",
                    "Is this their's car?",
                ],
                "uitleg": "Their staat voor een naamwoord. Theirs staat alleen: is this car theirs? En theirs schrijf je nooit met een apostrof.",
            },
            {
                "vraag": "Welke zin vraagt correct van wie een tafel is?",
                "opties": [
                    "Is this our table?",
                    "Is this ours table?",
                    "Is this us table?",
                    "Is this our's table?",
                ],
                "uitleg": "Our staat voor een naamwoord. Ours staat alleen: is this table ours? En ours schrijf je nooit met een apostrof.",
            },
        ],
        "Welke woorden zijn zelfstandige bezittelijke voornaamwoorden, die alleen kunnen staan?": [
            {
                "opties": ["yours", "ours", "his", "our"],
                "antwoord": [0, 1, 2],
                "uitleg": "Mine, yours, his, hers, ours en theirs staan alleen. Our hoort voor een naamwoord: our house.",
            },
            {
                "opties": ["mine", "ours", "theirs", "my"],
                "antwoord": [0, 1, 2],
                "uitleg": "Mine, yours, his, hers, ours en theirs staan alleen. My hoort voor een naamwoord: my house.",
            },
            {
                "opties": ["hers", "yours", "theirs", "her"],
                "antwoord": [0, 1, 2],
                "uitleg": "Mine, yours, his, hers, ours en theirs staan alleen. Her hoort voor een naamwoord: her house.",
            },
        ],
        "'Its' en 'it's' betekenen hetzelfde.": [
            {
                "vraag": "'Your' en 'you're' betekenen hetzelfde.",
                "uitleg": "Your is bezittelijk: your book. You're is de korte vorm van you are.",
            },
            {
                "vraag": "'Their' en 'they're' betekenen hetzelfde.",
                "uitleg": "Their is bezittelijk: their house. They're is de korte vorm van they are.",
            },
            {
                "vraag": "'Whose' en 'who's' betekenen hetzelfde.",
                "uitleg": "Whose is bezittelijk: whose bag is this? Who's is de korte vorm van who is.",
            },
        ],
        "Welke zin zegt correct dat je jezelf pijn deed?": [
            {
                "vraag": "Welke zin zegt correct dat zij zichzelf pijn deed?",
                "opties": [
                    "She hurt herself.",
                    "She hurt her.",
                    "She hurt hersself.",
                    "She hurt her self.",
                ],
                "uitleg": "Slaat de handeling terug op het onderwerp, dan neem je de wederkerende vorm op -self of -selves.",
            },
            {
                "vraag": "Welke zin zegt correct dat zij zichzelf pijn deden?",
                "opties": [
                    "They hurt themselves.",
                    "They hurt them.",
                    "They hurt theirselves.",
                    "They hurt them selves.",
                ],
                "uitleg": "Slaat de handeling terug op het onderwerp, dan neem je de wederkerende vorm op -self of -selves.",
            },
            {
                "vraag": "Welke zin zegt correct dat hij zichzelf pijn deed?",
                "opties": [
                    "He hurt himself.",
                    "He hurt him.",
                    "He hurt hisself.",
                    "He hurt his self.",
                ],
                "uitleg": "Slaat de handeling terug op het onderwerp, dan neem je de wederkerende vorm op -self of -selves.",
            },
        ],
        "Welke wederkerende voornaamwoorden zijn juist geschreven?": [
            {
                "opties": ["myself", "yourself", "herself", "hisself"],
                "antwoord": [0, 1, 2],
                "uitleg": "Hisself en theirselves bestaan niet. Het is himself en themselves.",
            },
            {
                "opties": ["itself", "yourselves", "themselves", "theirself"],
                "antwoord": [0, 1, 2],
                "uitleg": "Theirself en hisself bestaan niet. Het meervoud gaat op -selves.",
            },
            {
                "opties": ["ourselves", "himself", "yourselves", "ourself"],
                "antwoord": [0, 1, 2],
                "uitleg": "Ourself bestaat niet. Het meervoud gaat op -selves: ourselves, yourselves, themselves.",
            },
        ],
        "In welke zin hoort er géén wederkerend voornaamwoord?": [
            {
                "opties": [
                    "He shaved and left for work.",
                    "She hurt herself on the stairs.",
                    "They introduced themselves.",
                    "I taught myself to swim.",
                ],
                "uitleg": "Shave is in het Engels niet wederkerend. Wij zeggen zich scheren, het Engels zegt gewoon he shaved.",
            },
            {
                "opties": [
                    "They got dressed quickly.",
                    "He cut himself while cooking.",
                    "She taught herself Spanish.",
                    "We introduced ourselves.",
                ],
                "uitleg": "Dress is in het Engels niet wederkerend. Wij zeggen zich aankleden, het Engels zegt gewoon they got dressed.",
            },
            {
                "opties": [
                    "She washed before dinner.",
                    "He burnt himself on the pan.",
                    "They enjoyed themselves.",
                    "I hurt myself yesterday.",
                ],
                "uitleg": "Wash is in het Engels niet wederkerend. Wij zeggen zich wassen, het Engels zegt gewoon she washed.",
            },
        ],
        "Welk aanwijzend voornaamwoord hoort bij iets dat dicht bij je is en waarvan er meer dan één is?": [
            {
                "vraag": "Welk aanwijzend voornaamwoord hoort bij iets dat ver van je is en waarvan er meer dan één is?",
                "opties": ["those", "this", "that", "these"],
            },
            {
                "vraag": "Welk aanwijzend voornaamwoord hoort bij iets dat dicht bij je is en waarvan er maar één is?",
                "opties": ["this", "these", "that", "those"],
            },
            {
                "vraag": "Welk aanwijzend voornaamwoord hoort bij iets dat ver van je is en waarvan er maar één is?",
                "opties": ["that", "this", "these", "those"],
            },
        ],
        "Vul aan met één woord: … shoes over there are mine.": [
            {
                "vraag": "Vul aan met één woord: … books over there are mine.",
                "antwoord": ["those"],
                "uitleg": "Over there zegt dat ze ver zijn, en books is meervoud. Dus those.",
            },
            {
                "vraag": "Vul aan met één woord: … book here is mine.",
                "antwoord": ["this"],
                "uitleg": "Here zegt dat het dichtbij is, en book is enkelvoud. Dus this.",
            },
            {
                "vraag": "Vul aan met één woord: … keys here are mine.",
                "antwoord": ["these"],
                "uitleg": "Here zegt dat ze dichtbij zijn, en keys is meervoud. Dus these.",
            },
        ],
    },
    "Pronouns: de zeven soorten — deel 2": {
        "Welk vragend voornaamwoord vraagt naar een persoon als onderwerp?": [
            {
                "vraag": "Welk vragend voornaamwoord vraagt naar de eigenaar?",
                "opties": ["whose", "who", "which", "what"],
                "uitleg": "Whose bag is this? Who vraagt naar een persoon, which naar een keuze uit een beperkte groep.",
            },
            {
                "vraag": "Welk vragend voornaamwoord vraagt naar een keuze uit een beperkte groep?",
                "opties": ["which", "who", "whose", "what"],
                "uitleg": "Which colour do you want, red or blue? What laat de keuze open.",
            },
            {
                "vraag": "Welk vragend voornaamwoord vraagt naar een plaats?",
                "opties": ["where", "who", "whose", "which"],
                "uitleg": "Where do you live? Who vraagt naar een persoon en whose naar de eigenaar.",
            },
        ],
        "Welke vraagwoorden vragen naar een persoon of een bezit?": [
            {
                "opties": ["who", "whom", "whose", "when"],
                "antwoord": [0, 1, 2],
                "uitleg": "When vraagt naar een tijdstip. Whom is de voorwerpsvorm van who en klinkt formeel: to whom did you speak?",
            },
            {
                "opties": ["who", "whose", "whom", "why"],
                "antwoord": [0, 1, 2],
                "uitleg": "Why vraagt naar een reden. Whom is de voorwerpsvorm van who en klinkt formeel.",
            },
            {
                "opties": ["whom", "whose", "who", "how"],
                "antwoord": [0, 1, 2],
                "uitleg": "How vraagt naar een manier. Whom is de voorwerpsvorm van who en klinkt formeel.",
            },
        ],
        "Vul aan met één vraagwoord: … bag is this? Je vraagt naar de eigenaar.": [
            {
                "vraag": "Vul aan met één vraagwoord: … coat is this? Je vraagt naar de eigenaar.",
                "antwoord": ["whose"],
                "uitleg": "Whose vraagt naar het bezit. Verwar het niet met who's, de korte vorm van who is.",
            },
            {
                "vraag": "Vul aan met één vraagwoord: … lives next door? Je vraagt naar een persoon.",
                "antwoord": ["who"],
                "uitleg": "Who vraagt naar een persoon als onderwerp van de zin.",
            },
            {
                "vraag": "Vul aan met één vraagwoord: … did you go? Je vraagt naar een plaats.",
                "antwoord": ["where"],
                "uitleg": "Where vraagt naar een plaats, when naar een tijd en why naar een reden.",
            },
        ],
        "'Which' gebruik je als er een beperkte keuze is, 'what' als de keuze open is.": [
            {
                "vraag": "'Which colour do you want, red or blue?' is juist omdat de keuze beperkt is.",
                "uitleg": "Bij een open keuze zeg je What colour do you want?",
            },
            {
                "vraag": "'Whom' is de voorwerpsvorm van 'who'.",
                "uitleg": "To whom did you speak? Het klinkt formeel, maar het is correct.",
            },
            {
                "vraag": "'What' laat de keuze open.",
                "uitleg": "What colour do you want? tegenover Which colour do you want, red or blue?",
            },
        ],
        "Welke zin vraagt correct wie er vanavond komt?": [
            {
                "vraag": "Welke zin vraagt correct wie er morgen rijdt?",
                "opties": [
                    "Who's driving tomorrow?",
                    "Whose driving tomorrow?",
                    "Who is's driving tomorrow?",
                    "Whos driving tomorrow?",
                ],
            },
            {
                "vraag": "Welke zin vraagt correct wie er vanavond kookt?",
                "opties": [
                    "Who's cooking tonight?",
                    "Whose cooking tonight?",
                    "Who is's cooking tonight?",
                    "Whos cooking tonight?",
                ],
            },
            {
                "vraag": "Welke zin vraagt correct wie er aan de lijn is?",
                "opties": [
                    "Who's calling, please?",
                    "Whose calling, please?",
                    "Who is's calling, please?",
                    "Whos calling, please?",
                ],
            },
        ],
        "Welk betrekkelijk voornaamwoord hoort bij een persoon?": [
            {
                "vraag": "Welk betrekkelijk voornaamwoord hoort bij een ding?",
                "opties": ["which", "who", "where", "when"],
                "uitleg": "The book which I read. Who hoort bij personen, en that kan bij allebei.",
            },
            {
                "vraag": "Welk betrekkelijk voornaamwoord hoort bij een plaats?",
                "opties": ["where", "who", "which", "whose"],
                "uitleg": "This is the town where I was born. Who hoort bij personen en which bij dingen.",
            },
            {
                "vraag": "Welk betrekkelijk voornaamwoord hoort bij een tijdstip?",
                "opties": ["when", "who", "which", "where"],
                "uitleg": "I remember the day when we met. Where hoort bij een plaats.",
            },
        ],
        "Welke betrekkelijke voornaamwoorden kan je bij een ding gebruiken?": [
            {
                "vraag": "Welke betrekkelijke voornaamwoorden kan je bij een persoon gebruiken?",
                "opties": ["who", "that", "whose", "which"],
                "antwoord": [0, 1, 2],
                "uitleg": "Which houd je voor dingen. Who, that en whose kunnen alle drie bij een persoon.",
            },
            {
                "vraag": "Welke van deze woorden zijn betrekkelijke voornaamwoorden?",
                "opties": ["who", "which", "that", "what"],
                "antwoord": [0, 1, 2],
                "uitleg": "What is geen betrekkelijk voornaamwoord: the film what I saw is fout.",
            },
            {
                "vraag": "Welke woorden kan je gebruiken om een bijzin over een ding te beginnen?",
                "opties": ["which", "that", "whose", "who"],
                "antwoord": [0, 1, 2],
                "uitleg": "Whose kan ook bij een ding: the house whose roof is red. Who houd je voor personen.",
            },
        ],
        "Welk woord hoort in de plaats van de puntjes? This is the town … I was born.": [
            {"vraag": "Welk woord hoort in de plaats van de puntjes? That is the house … she grew up."},
            {"vraag": "Welk woord hoort in de plaats van de puntjes? This is the village … my grandparents lived."},
            {"vraag": "Welk woord hoort in de plaats van de puntjes? That is the school … I studied."},
        ],
        "Welke zin over de dag van een ontmoeting is juist?": [
            {
                "vraag": "Welke zin over het jaar van een verhuizing is juist?",
                "opties": [
                    "I remember the year when we moved.",
                    "I remember the year where we moved.",
                    "I remember the year which we moved.",
                    "I remember the year who we moved.",
                ],
            },
            {
                "vraag": "Welke zin over de zomer van een ontmoeting is juist?",
                "opties": [
                    "I remember the summer when we met.",
                    "I remember the summer where we met.",
                    "I remember the summer which we met.",
                    "I remember the summer who we met.",
                ],
            },
            {
                "vraag": "Welke zin over de nacht van de sneeuw is juist?",
                "opties": [
                    "She recalls the night when it snowed.",
                    "She recalls the night where it snowed.",
                    "She recalls the night which it snowed.",
                    "She recalls the night who it snowed.",
                ],
            },
        ],
        "In het Engels mag je 'what' gebruiken als betrekkelijk voornaamwoord: the film what I saw.": [
            {
                "vraag": "'The book what I read' is correct Engels.",
                "uitleg": "Het moet the book that I read of the book I read zijn.",
            },
            {
                "vraag": "'What' kan een betrekkelijk voornaamwoord zijn bij een ding.",
                "uitleg": "Dat hoor je wel in spreektaal, maar het is fout. Gebruik that of which.",
            },
            {
                "vraag": "'The house what we bought' is correct Engels.",
                "uitleg": "Het moet the house that we bought of the house we bought zijn.",
            },
        ],
        "Welke woorden zijn onbepaalde voornaamwoorden?": [
            {
                "opties": ["everybody", "something", "none", "herself"],
                "antwoord": [0, 1, 2],
                "uitleg": "Herself is wederkerend. Onbepaald zijn ook someone, anything, nobody en each.",
            },
            {
                "opties": ["anybody", "everything", "each", "themselves"],
                "antwoord": [0, 1, 2],
                "uitleg": "Themselves is wederkerend. Onbepaald zijn ook someone, anything en nobody.",
            },
            {
                "opties": ["no one", "everyone", "nothing", "myself"],
                "antwoord": [0, 1, 2],
                "uitleg": "Myself is wederkerend. Onbepaald zijn ook someone, anything en each.",
            },
        ],
        "Welke ontkennende zin over zien is juist?": [
            {
                "vraag": "Welke ontkennende zin over horen is juist?",
                "opties": [
                    "I didn't hear anything.",
                    "I didn't hear nothing.",
                    "I don't heard anything.",
                    "I didn't heard nothing.",
                ],
                "uitleg": "Twee ontkenningen in één zin mag niet in het Engels. Het is didn't ... anything of heard nothing.",
            },
            {
                "vraag": "Welke ontkennende zin over zeggen is juist?",
                "opties": [
                    "She didn't say anything.",
                    "She didn't say nothing.",
                    "She don't said anything.",
                    "She didn't said nothing.",
                ],
                "uitleg": "Twee ontkenningen in één zin mag niet in het Engels. Het is didn't ... anything of said nothing.",
            },
            {
                "vraag": "Welke ontkennende zin over vinden is juist?",
                "opties": [
                    "We didn't find anything.",
                    "We didn't find nothing.",
                    "We don't found anything.",
                    "We didn't found nothing.",
                ],
                "uitleg": "Twee ontkenningen in één zin mag niet in het Engels. Het is didn't ... anything of found nothing.",
            },
        ],
    },
    "Adjectives, adverbs, comparatives en voorzetsels — deel 1": {
        "Een bijvoeglijk naamwoord blijft in het Engels hetzelfde, ook als het naamwoord meervoud is.": [
            {
                "vraag": "Je zegt 'two red cars' en niet 'two reds cars'.",
                "uitleg": "Een bijvoeglijk naamwoord verandert in het Engels nooit van vorm.",
            },
            {
                "vraag": "'Three big houses' is juist Engels.",
                "uitleg": "Big blijft big, ook bij een meervoud.",
            },
            {
                "vraag": "In het Engels krijgt een bijvoeglijk naamwoord nooit een meervouds-s.",
                "uitleg": "Two red cars, three big houses. In het Nederlands verandert het soms wel: een rode auto, twee rode auto's.",
            },
        ],
        "Welke woorden zijn bijwoorden?": [
            {
                "opties": ["slowly", "happily", "badly", "slow"],
                "antwoord": [0, 1, 2],
                "uitleg": "Slow is het bijvoeglijk naamwoord, slowly het bijwoord. Een y na een medeklinker wordt ily: happy wordt happily.",
            },
            {
                "opties": ["loudly", "angrily", "politely", "polite"],
                "antwoord": [0, 1, 2],
                "uitleg": "Polite is het bijvoeglijk naamwoord, politely het bijwoord. Een y na een medeklinker wordt ily: angry wordt angrily.",
            },
            {
                "opties": ["quietly", "simply", "nicely", "nice"],
                "antwoord": [0, 1, 2],
                "uitleg": "Nice is het bijvoeglijk naamwoord, nicely het bijwoord. Bij woorden op -le valt de e weg: simple wordt simply.",
            },
        ],
        "Maak het bijwoord bij 'happy'.": [
            {
                "vraag": "Maak het bijwoord bij 'angry'.",
                "antwoord": ["angrily"],
                "uitleg": "De y wordt i en er komt ly bij. Zo ook bij happy en happily.",
            },
            {
                "vraag": "Maak het bijwoord bij 'easy'.",
                "antwoord": ["easily"],
                "uitleg": "De y wordt i en er komt ly bij. Zo ook bij angry en angrily.",
            },
            {
                "vraag": "Maak het bijwoord bij 'lucky'.",
                "antwoord": ["luckily"],
                "uitleg": "De y wordt i en er komt ly bij. Zo ook bij happy en happily.",
            },
        ],
        "Maak het bijwoord bij 'terrible'.": [
            {
                "vraag": "Maak het bijwoord bij 'simple'.",
                "antwoord": ["simply"],
                "uitleg": "Bij woorden op -le valt de e weg: simple wordt simply, terrible wordt terribly.",
            },
            {
                "vraag": "Maak het bijwoord bij 'gentle'.",
                "antwoord": ["gently"],
                "uitleg": "Bij woorden op -le valt de e weg: gentle wordt gently, simple wordt simply.",
            },
            {
                "vraag": "Maak het bijwoord bij 'possible'.",
                "antwoord": ["possibly"],
                "uitleg": "Bij woorden op -le valt de e weg: possible wordt possibly, terrible wordt terribly.",
            },
        ],
        "Welke zin zegt correct dat iemand goed zingt?": [
            {
                "vraag": "Welke zin zegt correct dat iemand goed kookt?",
                "opties": [
                    "He cooks well.",
                    "He cooks good.",
                    "He cooks goodly.",
                    "He cooks a good.",
                ],
                "uitleg": "Well is het bijwoord bij good. Good zegt iets over een naamwoord: he is a good cook.",
            },
            {
                "vraag": "Welke zin zegt correct dat iemand goed danst?",
                "opties": [
                    "She dances well.",
                    "She dances good.",
                    "She dances goodly.",
                    "She dances a good.",
                ],
                "uitleg": "Well is het bijwoord bij good. Good zegt iets over een naamwoord: she is a good dancer.",
            },
            {
                "vraag": "Welke zin zegt correct dat zij goed spelen?",
                "opties": [
                    "They play well.",
                    "They play good.",
                    "They play goodly.",
                    "They play a good.",
                ],
                "uitleg": "Well is het bijwoord bij good. Good zegt iets over een naamwoord: they are good players.",
            },
        ],
        "Het bijwoord bij 'fast' is 'fastly'.": [
            {
                "vraag": "Het bijwoord bij 'hard' is 'hardly'.",
                "uitleg": "Hardly betekent nauwelijks. Het bijwoord bij hard is gewoon hard: he works hard.",
            },
            {
                "vraag": "Het bijwoord bij 'late' is 'lately'.",
                "uitleg": "Lately betekent de laatste tijd. Het bijwoord bij late is gewoon late: he arrived late.",
            },
            {
                "vraag": "Het bijwoord bij 'early' is 'earlily'.",
                "uitleg": "Early blijft early: she got up early. Earlily bestaat niet.",
            },
        ],
        "Wat betekent 'he has hardly worked'?": [
            {
                "vraag": "Wat betekent 'she has hardly eaten'?",
                "opties": [
                    "zij heeft nauwelijks gegeten",
                    "zij heeft veel gegeten",
                    "zij heeft moeilijk eten",
                    "zij eet nog altijd",
                ],
                "uitleg": "Hard betekent hard, maar hardly betekent nauwelijks.",
            },
            {
                "vraag": "Wat betekent 'I hardly know him'?",
                "opties": [
                    "ik ken hem nauwelijks",
                    "ik ken hem goed",
                    "ik ken hem moeilijk",
                    "ik ken hem al lang",
                ],
                "uitleg": "Hard betekent hard, maar hardly betekent nauwelijks.",
            },
            {
                "vraag": "Wat betekent 'they have hardly slept'?",
                "opties": [
                    "zij hebben nauwelijks geslapen",
                    "zij hebben lang geslapen",
                    "zij hebben moeilijk geslapen",
                    "zij slapen nog",
                ],
                "uitleg": "Hard betekent hard, maar hardly betekent nauwelijks.",
            },
        ],
        "Welk woord is een bijvoeglijk naamwoord, ook al eindigt het op -ly?": [
            {
                "opties": ["lovely", "quickly", "slowly", "badly"],
                "uitleg": "Friendly, lovely, lonely en silly zijn bijvoeglijke naamwoorden. Wil je er een bijwoord van maken, dan zeg je in a lovely way.",
            },
            {
                "opties": ["lonely", "politely", "happily", "loudly"],
                "uitleg": "Friendly, lovely, lonely en silly zijn bijvoeglijke naamwoorden. Wil je er een bijwoord van maken, dan zeg je in a lonely way.",
            },
            {
                "opties": ["silly", "nicely", "angrily", "quietly"],
                "uitleg": "Friendly, lovely, lonely en silly zijn bijvoeglijke naamwoorden. Wil je er een bijwoord van maken, dan zeg je in a silly way.",
            },
        ],
        "Welke zin over een bezoek aan de sportzaal is juist?": [
            {
                "vraag": "Welke zin over een bezoek aan de bibliotheek is juist?",
                "opties": [
                    "She often goes to the library.",
                    "She goes often to the library.",
                    "Often she goes the library.",
                    "She goes to the library often the week.",
                ],
            },
            {
                "vraag": "Welke zin over zwemmen na school is juist?",
                "opties": [
                    "He always swims after school.",
                    "He swims always after school.",
                    "Always he swims the pool.",
                    "He swims after school always the week.",
                ],
            },
            {
                "vraag": "Welke zin over ontbijten is juist?",
                "opties": [
                    "They usually eat breakfast at seven.",
                    "They eat usually breakfast at seven.",
                    "Usually they eat the breakfast seven.",
                    "They eat breakfast usually the day.",
                ],
            },
        ],
        "Welke zin over de smaak van de soep is juist?": [
            {
                "vraag": "Welke zin over de smaak van de taart is juist?",
                "opties": [
                    "The cake tastes delicious.",
                    "The cake tastes deliciously.",
                    "The cake is tasting deliciously.",
                    "The cake tastes a delicious.",
                ],
                "uitleg": "Taste is hier een koppelwerkwoord, dus komt er een bijvoeglijk naamwoord achter.",
            },
            {
                "vraag": "Welke zin over de geur van de bloemen is juist?",
                "opties": [
                    "The flowers smell lovely.",
                    "The flowers smell lovelily.",
                    "The flowers are smelling lovelily.",
                    "The flowers smell a lovely.",
                ],
                "uitleg": "Smell is hier een koppelwerkwoord, dus komt er een bijvoeglijk naamwoord achter.",
            },
            {
                "vraag": "Welke zin over hoe iemand eruitziet is juist?",
                "opties": [
                    "She looks happy today.",
                    "She looks happily today.",
                    "She is looking happily today.",
                    "She looks a happy today.",
                ],
                "uitleg": "Look is hier een koppelwerkwoord, dus komt er een bijvoeglijk naamwoord achter.",
            },
        ],
        "Welke woorden versterken een bijvoeglijk naamwoord?": [
            {
                "opties": ["really", "rather", "incredibly", "much"],
                "antwoord": [0, 1, 2],
                "uitleg": "Much versterkt geen bijvoeglijk naamwoord in een gewone zin. Bij een vergrotende trap kan het wel: much better.",
            },
            {
                "opties": ["very", "fairly", "terribly", "much"],
                "antwoord": [0, 1, 2],
                "uitleg": "Much versterkt geen bijvoeglijk naamwoord in een gewone zin. Bij een vergrotende trap kan het wel: much better.",
            },
            {
                "opties": ["extremely", "quite", "awfully", "much"],
                "antwoord": [0, 1, 2],
                "uitleg": "Much versterkt geen bijvoeglijk naamwoord in een gewone zin. Bij een vergrotende trap kan het wel: much better.",
            },
        ],
        "Welke zin klopt qua betekenis?": [
            {
                "opties": [
                    "She works hard, so she is tired.",
                    "She hardly works, so she is tired from work.",
                    "She works hardly, so she earns a lot.",
                    "She is hard working hardly today.",
                ],
            },
            {
                "opties": [
                    "They study hard, so they pass.",
                    "They hardly study, so they pass easily.",
                    "They study hardly, so they know a lot.",
                    "They are hard studying hardly now.",
                ],
            },
            {
                "opties": [
                    "He trains hard, so he improves.",
                    "He hardly trains, so he improves fast.",
                    "He trains hardly, so he wins often.",
                    "He is hard training hardly today.",
                ],
            },
        ],
    },
    "Adjectives, adverbs, comparatives en voorzetsels — deel 2": {
        "Wat is de vergrotende trap van 'big'?": [
            {
                "vraag": "Wat is de vergrotende trap van 'hot'?",
                "opties": ["hotter", "more hot", "hoter", "hottest"],
                "uitleg": "Een korte klinker met één medeklinker erachter: die medeklinker verdubbelt. Hot wordt hotter, big wordt bigger.",
            },
            {
                "vraag": "Wat is de vergrotende trap van 'thin'?",
                "opties": ["thinner", "more thin", "thiner", "thinnest"],
                "uitleg": "Een korte klinker met één medeklinker erachter: die medeklinker verdubbelt. Thin wordt thinner, big wordt bigger.",
            },
            {
                "vraag": "Wat is de vergrotende trap van 'sad'?",
                "opties": ["sadder", "more sad", "sader", "saddest"],
                "uitleg": "Een korte klinker met één medeklinker erachter: die medeklinker verdubbelt. Sad wordt sadder, hot wordt hotter.",
            },
        ],
        "Bij welke woorden gebruik je 'more' in plaats van -er?": [
            {
                "opties": ["difficult", "important", "comfortable", "tall"],
                "antwoord": [0, 1, 2],
                "uitleg": "Woorden van twee of meer lettergrepen krijgen more. Korte woorden krijgen -er: taller.",
            },
            {
                "opties": ["dangerous", "popular", "surprising", "old"],
                "antwoord": [0, 1, 2],
                "uitleg": "Woorden van twee of meer lettergrepen krijgen more. Korte woorden krijgen -er: older.",
            },
            {
                "opties": ["careful", "modern", "exciting", "young"],
                "antwoord": [0, 1, 2],
                "uitleg": "Woorden van twee of meer lettergrepen krijgen more. Korte woorden krijgen -er: younger.",
            },
        ],
        "Schrijf de vergrotende trap van 'easy'.": [
            {
                "vraag": "Schrijf de vergrotende trap van 'happy'.",
                "antwoord": ["happier"],
                "uitleg": "Twee lettergrepen maar op een y, dus toch -er: happy, happier, happiest. De y wordt i.",
            },
            {
                "vraag": "Schrijf de vergrotende trap van 'busy'.",
                "antwoord": ["busier"],
                "uitleg": "Twee lettergrepen maar op een y, dus toch -er: busy, busier, busiest. De y wordt i.",
            },
            {
                "vraag": "Schrijf de vergrotende trap van 'early'.",
                "antwoord": ["earlier"],
                "uitleg": "Twee lettergrepen maar op een y, dus toch -er: early, earlier, earliest. De y wordt i.",
            },
        ],
        "De overtreffende trap van 'good' is 'goodest'.": [
            {
                "vraag": "De vergrotende trap van 'bad' is 'badder'.",
                "uitleg": "Bad, worse, worst zijn onregelmatig.",
            },
            {
                "vraag": "De overtreffende trap van 'little' is 'littlest'.",
                "uitleg": "Little, less, least zijn onregelmatig.",
            },
            {
                "vraag": "De vergrotende trap van 'good' is 'gooder'.",
                "uitleg": "Good, better, best zijn onregelmatig.",
            },
        ],
        "Wat is de overtreffende trap van 'bad'?": [
            {
                "vraag": "Wat is de overtreffende trap van 'good'?",
                "opties": ["best", "goodest", "better", "most good"],
                "uitleg": "Good, better, best. Better is de vergrotende trap.",
            },
            {
                "vraag": "Wat is de overtreffende trap van 'little'?",
                "opties": ["least", "littlest", "less", "most little"],
                "uitleg": "Little, less, least. Less is de vergrotende trap.",
            },
            {
                "vraag": "Wat is de overtreffende trap van 'far'?",
                "opties": ["furthest", "farrest", "further", "most far"],
                "uitleg": "Far, further, furthest. Further is de vergrotende trap.",
            },
        ],
        "Vul aan met één woord: this book is more interesting … the other one.": [
            {
                "vraag": "Vul aan met één woord: this test is easier … the last one.",
                "antwoord": ["than"],
                "uitleg": "Na een vergrotende trap komt than. Verwar het niet met then, dat daarna betekent.",
            },
            {
                "vraag": "Vul aan met één woord: she is taller … her brother.",
                "antwoord": ["than"],
                "uitleg": "Na een vergrotende trap komt than. Verwar het niet met then, dat daarna betekent.",
            },
            {
                "vraag": "Vul aan met één woord: my bag is heavier … yours.",
                "antwoord": ["than"],
                "uitleg": "Na een vergrotende trap komt than. Verwar het niet met then, dat daarna betekent.",
            },
        ],
        "Welke zin vergelijkt correct twee personen die even groot zijn?": [
            {
                "vraag": "Welke zin vergelijkt correct twee personen die even oud zijn?",
                "opties": [
                    "He is as old as his cousin.",
                    "He is as old than his cousin.",
                    "He is so old as his cousin.",
                    "He is as old like his cousin.",
                ],
            },
            {
                "vraag": "Welke zin vergelijkt correct twee dozen die even zwaar zijn?",
                "opties": [
                    "This box is as heavy as that one.",
                    "This box is as heavy than that one.",
                    "This box is so heavy as that one.",
                    "This box is as heavy like that one.",
                ],
            },
            {
                "vraag": "Welke zin vergelijkt correct twee mensen die even snel lopen?",
                "opties": [
                    "She runs as fast as I do.",
                    "She runs as fast than I do.",
                    "She runs so fast as I do.",
                    "She runs as fast like I do.",
                ],
            },
        ],
        "Voor de overtreffende trap zet je bijna altijd 'the': she is the tallest in the class.": [
            {
                "vraag": "Je zegt 'he is the best player in the team'.",
                "uitleg": "Bij de overtreffende trap hoort the. Bij de vergrotende trap niet.",
            },
            {
                "vraag": "Bij de vergrotende trap zet je geen 'the'.",
                "uitleg": "She is taller than her brother, zonder the. Bij de overtreffende trap wel: the tallest.",
            },
            {
                "vraag": "Voor 'most expensive' hoort 'the'.",
                "uitleg": "Best, tallest, most expensive: er hoort the voor.",
            },
        ],
        "Welk voorzetsel hoort bij een uur: … seven o'clock?": [
            {
                "vraag": "Welk voorzetsel hoort bij een dag: … Monday?",
                "opties": ["on", "at", "in", "for"],
                "uitleg": "At bij een uur, on bij een dag of een datum, in bij een maand, een seizoen of een jaar.",
            },
            {
                "vraag": "Welk voorzetsel hoort bij een maand: … July?",
                "opties": ["in", "at", "on", "for"],
                "uitleg": "At bij een uur, on bij een dag of een datum, in bij een maand, een seizoen of een jaar.",
            },
            {
                "vraag": "Welk voorzetsel hoort bij een jaartal: … 2027?",
                "opties": ["in", "at", "on", "for"],
                "uitleg": "At bij een uur, on bij een dag of een datum, in bij een maand, een seizoen of een jaar.",
            },
        ],
        "Bij welke tijdsaanduidingen hoort 'in'?": [
            {
                "opties": ["March", "the evening", "summer", "Friday"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij een dag hoort on: on Friday. En on Friday evening, want de dag wint.",
            },
            {
                "opties": ["2030", "the afternoon", "winter", "Sunday"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij een dag hoort on: on Sunday. En on Sunday afternoon, want de dag wint.",
            },
            {
                "opties": ["September", "the morning", "spring", "Tuesday"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij een dag hoort on: on Tuesday. En on Tuesday morning, want de dag wint.",
            },
        ],
        "Welke werkwoorden nemen het voorzetsel 'to'?": [
            {
                "opties": ["listen", "reply", "apologise", "enter"],
                "antwoord": [0, 1, 2],
                "uitleg": "Enter neemt niets: we entered the room. Listen to music, reply to a letter, apologise to someone.",
            },
            {
                "opties": ["belong", "explain", "speak", "marry"],
                "antwoord": [0, 1, 2],
                "uitleg": "Marry neemt niets: he married her. Belong to someone, explain something to someone, speak to someone.",
            },
            {
                "opties": ["listen", "happen", "refer", "phone"],
                "antwoord": [0, 1, 2],
                "uitleg": "Phone neemt niets: she phoned me. Listen to music, happen to someone, refer to a book.",
            },
        ],
        "Vul het juiste voorzetsel in: she is very good … maths.": [
            {
                "vraag": "Vul het juiste voorzetsel in: he is very bad … drawing.",
                "antwoord": ["at"],
                "uitleg": "Good at, bad at, maar interested in en afraid of. Die combinaties leer je als één geheel.",
            },
            {
                "vraag": "Vul het juiste voorzetsel in: I am interested … history.",
                "antwoord": ["in"],
                "uitleg": "Interested in, good at, afraid of. Die combinaties leer je als één geheel.",
            },
            {
                "vraag": "Vul het juiste voorzetsel in: she is afraid … spiders.",
                "antwoord": ["of"],
                "uitleg": "Afraid of, good at, interested in. Die combinaties leer je als één geheel.",
            },
        ],
    },
    "De tegenwoordige tijden — deel 1": {
        "Welke zin over boeken op tafel is juist?": [
            {
                "vraag": "Welke zin over appels in de kom is juist?",
                "opties": [
                    "There are three apples in the bowl.",
                    "There is three apples in the bowl.",
                    "There are an apple in the bowl.",
                    "It are three apples in the bowl.",
                ],
            },
            {
                "vraag": "Welke zin over kinderen in de tuin is juist?",
                "opties": [
                    "There are two children in the garden.",
                    "There is two children in the garden.",
                    "There are a child in the garden.",
                    "It are two children in the garden.",
                ],
            },
            {
                "vraag": "Welke zin over stoelen in de kamer is juist?",
                "opties": [
                    "There are four chairs in the room.",
                    "There is four chairs in the room.",
                    "There are a chair in the room.",
                    "It are four chairs in the room.",
                ],
            },
        ],
        "In 'there is some milk in the fridge' hoort 'is' omdat milk ontelbaar is.": [
            {
                "vraag": "In 'there is some bread on the table' hoort 'is' omdat bread ontelbaar is.",
                "uitleg": "Ontelbare woorden nemen de enkelvoudsvorm.",
            },
            {
                "vraag": "Bij een opsomming kijk je naar het eerste woord: there is a knife and two forks.",
                "uitleg": "Het eerste woord is enkelvoud, dus there is.",
            },
            {
                "vraag": "'There is some sugar left' is juist omdat sugar ontelbaar is.",
                "uitleg": "Ontelbare woorden nemen de enkelvoudsvorm.",
            },
        ],
        "Hoe schrijf je de derde persoon enkelvoud van 'to watch'?": [
            {
                "vraag": "Hoe schrijf je de derde persoon enkelvoud van 'to miss'?",
                "opties": ["misses", "miss", "misse", "missies"],
                "uitleg": "Na een sisklank komt es: misses, watches, fixes. Zo ook bij go en do: goes, does.",
            },
            {
                "vraag": "Hoe schrijf je de derde persoon enkelvoud van 'to fix'?",
                "opties": ["fixes", "fixs", "fixe", "fixies"],
                "uitleg": "Na een sisklank komt es: fixes, watches, misses. Zo ook bij go en do: goes, does.",
            },
            {
                "vraag": "Hoe schrijf je de derde persoon enkelvoud van 'to go'?",
                "opties": ["goes", "gos", "goe", "goies"],
                "uitleg": "Go krijgt es, net als do: goes, does. Na een sisklank komt er ook es: watches, misses.",
            },
        ],
        "Schrijf de derde persoon enkelvoud van 'to fly'.": [
            {
                "vraag": "Schrijf de derde persoon enkelvoud van 'to try'.",
                "antwoord": ["tries"],
                "uitleg": "Een y na een medeklinker wordt ies. Staat er een klinker voor, dan blijft de y: he plays.",
            },
            {
                "vraag": "Schrijf de derde persoon enkelvoud van 'to carry'.",
                "antwoord": ["carries"],
                "uitleg": "Een y na een medeklinker wordt ies. Staat er een klinker voor, dan blijft de y: he plays.",
            },
            {
                "vraag": "Schrijf de derde persoon enkelvoud van 'to play'.",
                "antwoord": ["plays"],
                "uitleg": "Voor de y staat een klinker, dus blijft ze staan. Bij een medeklinker ervoor wordt het ies: he flies.",
            },
        ],
        "Welke zinnen staan in een correcte present simple?": [
            {
                "opties": [
                    "She teaches maths.",
                    "He watches the news.",
                    "They work in Brussels.",
                    "He play football.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "He plays football. De s van de derde persoon vergeten is de meest gemaakte fout in het Engels.",
            },
            {
                "opties": [
                    "He carries the bags.",
                    "She goes by bus.",
                    "We live in Hasselt.",
                    "She want a dog.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "She wants a dog. De s van de derde persoon vergeten is de meest gemaakte fout in het Engels.",
            },
            {
                "opties": [
                    "She tries her best.",
                    "He fixes bikes.",
                    "They study Spanish.",
                    "He do his homework.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "He does his homework. De s van de derde persoon vergeten is de meest gemaakte fout in het Engels.",
            },
        ],
        "Welke vraag is juist?": [
            {
                "opties": [
                    "Does he work here?",
                    "Do he works here?",
                    "Does he works here?",
                    "Works he here?",
                ],
            },
            {
                "opties": [
                    "Does she play tennis?",
                    "Do she plays tennis?",
                    "Does she plays tennis?",
                    "Plays she tennis?",
                ],
            },
            {
                "opties": [
                    "Does it start at six?",
                    "Do it starts at six?",
                    "Does it starts at six?",
                    "Starts it at six?",
                ],
            },
        ],
        "In een ontkennende zin zeg je 'she doesn't lives here'.": [
            {
                "vraag": "In een ontkennende zin zeg je 'he doesn't works here'.",
                "uitleg": "Het is he doesn't work here. De s zit al in doesn't.",
            },
            {
                "vraag": "'She doesn't plays tennis' is juist.",
                "uitleg": "Het is she doesn't play tennis. De s zit al in doesn't.",
            },
            {
                "vraag": "Na 'doesn't' krijgt het werkwoord nog een s.",
                "uitleg": "De s zit al in doesn't: she doesn't live here.",
            },
        ],
        "Welke zin staat in een correcte present continuous?": [
            {
                "opties": [
                    "He is reading a book.",
                    "He reading a book.",
                    "He is read a book.",
                    "He reads now a book.",
                ],
            },
            {
                "opties": [
                    "They are playing outside.",
                    "They playing outside.",
                    "They are play outside.",
                    "They play now outside.",
                ],
            },
            {
                "opties": [
                    "I am cooking dinner.",
                    "I cooking dinner.",
                    "I am cook dinner.",
                    "I cook now dinner.",
                ],
            },
        ],
        "Schrijf de -ing-vorm van 'to sit'.": [
            {
                "vraag": "Schrijf de -ing-vorm van 'to run'.",
                "antwoord": ["running"],
                "uitleg": "Eén korte klinker met één medeklinker erachter: die verdubbelt. Run wordt running, sit wordt sitting.",
            },
            {
                "vraag": "Schrijf de -ing-vorm van 'to swim'.",
                "antwoord": ["swimming"],
                "uitleg": "Eén korte klinker met één medeklinker erachter: die verdubbelt. Swim wordt swimming, run wordt running.",
            },
            {
                "vraag": "Schrijf de -ing-vorm van 'to write'.",
                "antwoord": ["writing"],
                "uitleg": "Bij write valt de stomme e weg: writing. Verdubbelen doe je alleen na één korte klinker: sitting.",
            },
        ],
        "Welke -ing-vormen zijn juist geschreven?": [
            {
                "opties": ["making", "dying", "running", "runing"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij make valt de stomme e weg: making. Bij die wordt ie een y: dying. Bij run verdubbelt de n.",
            },
            {
                "opties": ["coming", "tying", "swimming", "comming"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij come valt de stomme e weg: coming. Bij tie wordt ie een y: tying.",
            },
            {
                "opties": ["taking", "lying", "sitting", "takeing"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij take valt de stomme e weg: taking. Bij lie wordt ie een y: lying.",
            },
        ],
        "Welke zin past bij 'Ik werk elke zaterdag in een winkel.'?": [
            {
                "vraag": "Welke zin past bij 'Ik speel elke zondag voetbal.'?",
                "opties": [
                    "I play football every Sunday.",
                    "I am playing football every Sunday.",
                    "I have played football every Sunday.",
                    "I am play football every Sunday.",
                ],
                "uitleg": "Every Sunday maakt er een gewoonte van, dus present simple.",
            },
            {
                "vraag": "Welke zin past bij 'Zij fietst elke ochtend naar school.'?",
                "opties": [
                    "She cycles to school every morning.",
                    "She is cycling to school every morning.",
                    "She has cycled to school every morning.",
                    "She is cycle to school every morning.",
                ],
                "uitleg": "Every morning maakt er een gewoonte van, dus present simple.",
            },
            {
                "vraag": "Welke zin past bij 'Wij eten elke vrijdag frietjes.'?",
                "opties": [
                    "We eat chips every Friday.",
                    "We are eating chips every Friday.",
                    "We have eaten chips every Friday.",
                    "We are eat chips every Friday.",
                ],
                "uitleg": "Every Friday maakt er een gewoonte van, dus present simple.",
            },
        ],
        "Welke zin klopt?": [
            {
                "opties": [
                    "There aren't any apples left.",
                    "There isn't any apples left.",
                    "There aren't an apple left.",
                    "There is not no apples left.",
                ],
                "uitleg": "Apples is meervoud, dus aren't. En in een ontkenning hoort any, niet some.",
            },
            {
                "opties": [
                    "There aren't any chairs left.",
                    "There isn't any chairs left.",
                    "There aren't a chair left.",
                    "There is not no chairs left.",
                ],
                "uitleg": "Chairs is meervoud, dus aren't. En in een ontkenning hoort any, niet some.",
            },
            {
                "opties": [
                    "There aren't any tickets left.",
                    "There isn't any tickets left.",
                    "There aren't a ticket left.",
                    "There is not no tickets left.",
                ],
                "uitleg": "Tickets is meervoud, dus aren't. En in een ontkenning hoort any, niet some.",
            },
        ],
    },
    "De tegenwoordige tijden — deel 2": {
        "Hoe vertaal je 'Ik woon sinds 2020 in Antwerpen.'?": [
            {
                "vraag": "Hoe vertaal je 'Ik ken hem sinds 2019.'?",
                "opties": [
                    "I have known him since 2019.",
                    "I know him since 2019.",
                    "I am knowing him since 2019.",
                    "I knew him since 2019.",
                ],
            },
            {
                "vraag": "Hoe vertaal je 'Zij werkt hier sinds september.'?",
                "opties": [
                    "She has worked here since September.",
                    "She works here since September.",
                    "She is working here since September.",
                    "She worked here since September.",
                ],
            },
            {
                "vraag": "Hoe vertaal je 'Wij leren al drie jaar Engels.'?",
                "opties": [
                    "We have learned English for three years.",
                    "We learn English for three years.",
                    "We are learning English for three years.",
                    "We learned English for three years.",
                ],
            },
        ],
        "Vul in met één woord: she … finished her homework.": [
            {
                "vraag": "Vul in met één woord: he … finished his homework.",
                "antwoord": ["has"],
                "uitleg": "She, he en it nemen has. Alle andere personen nemen have.",
            },
            {
                "vraag": "Vul in met één woord: they … finished their homework.",
                "antwoord": ["have"],
                "uitleg": "She, he en it nemen has. Alle andere personen nemen have.",
            },
            {
                "vraag": "Vul in met één woord: it … stopped raining.",
                "antwoord": ["has"],
                "uitleg": "She, he en it nemen has. Alle andere personen nemen have.",
            },
        ],
        "Welk woord hoort bij een moment waarop iets begon?": [
            {
                "vraag": "Welk woord hoort bij de duur van iets?",
                "opties": ["for", "since", "ago", "during"],
                "uitleg": "For three years, for a week. Since zegt vanaf wanneer: since 2020.",
            },
            {
                "vraag": "Welk woord hoort bij 'Monday' als je het begin bedoelt?",
                "opties": ["since", "for", "ago", "during"],
                "uitleg": "Since Monday zegt vanaf wanneer. For gaat over de duur: for three days.",
            },
            {
                "vraag": "Welk woord hoort bij 'two hours' als je de duur bedoelt?",
                "opties": ["for", "since", "ago", "during"],
                "uitleg": "For two hours zegt hoe lang. Since zegt vanaf wanneer: since Monday.",
            },
        ],
        "Bij welke woorden hoort 'for' en niet 'since'?": [
            {
                "opties": ["three days", "a month", "a long time", "yesterday"],
                "antwoord": [0, 1, 2],
                "uitleg": "For zegt hoe lang, since zegt vanaf wanneer. Yesterday is een moment, dus since.",
            },
            {
                "opties": ["ten minutes", "a year", "ages", "2020"],
                "antwoord": [0, 1, 2],
                "uitleg": "For zegt hoe lang, since zegt vanaf wanneer. 2020 is een moment, dus since.",
            },
            {
                "opties": ["an hour", "two weeks", "a while", "last summer"],
                "antwoord": [0, 1, 2],
                "uitleg": "For zegt hoe lang, since zegt vanaf wanneer. Last summer is een moment, dus since.",
            },
        ],
        "'I have been to London last year' is een juiste zin.": [
            {
                "vraag": "'I have seen that film yesterday' is een juiste zin.",
                "uitleg": "Yesterday is een afgelopen tijd, dus je neemt de past simple: I saw that film yesterday.",
            },
            {
                "vraag": "'She has moved house in 2019' is een juiste zin.",
                "uitleg": "In 2019 is een afgelopen tijd, dus je neemt de past simple: she moved house in 2019.",
            },
            {
                "vraag": "'We have arrived two hours ago' is een juiste zin.",
                "uitleg": "Ago hoort bij een afgelopen tijd, dus je neemt de past simple: we arrived two hours ago.",
            },
        ],
        "Welke vraag over ervaring met sushi is juist?": [
            {
                "vraag": "Welke vraag over ervaring met paardrijden is juist?",
                "opties": [
                    "Have you ever ridden a horse?",
                    "Have you ever rode a horse?",
                    "Did you ever ridden a horse?",
                    "Have you never rode a horse?",
                ],
                "uitleg": "Na have komt het voltooid deelwoord: ridden. Rode is de verleden tijd.",
            },
            {
                "vraag": "Welke vraag over ervaring met vliegen is juist?",
                "opties": [
                    "Have you ever flown to Spain?",
                    "Have you ever flew to Spain?",
                    "Did you ever flown to Spain?",
                    "Have you never flew to Spain?",
                ],
                "uitleg": "Na have komt het voltooid deelwoord: flown. Flew is de verleden tijd.",
            },
            {
                "vraag": "Welke vraag over ervaring met dat boek is juist?",
                "opties": [
                    "Have you ever read that book?",
                    "Have you ever readed that book?",
                    "Did you ever readed that book?",
                    "Have you never readed that book?",
                ],
                "uitleg": "Na have komt het voltooid deelwoord. Bij read blijft de schrijfwijze gelijk, readed bestaat niet.",
            },
        ],
        "Vul aan met één woord: I have … seen that film, dus ik moet het niet nog eens zien.": [
            {
                "vraag": "Vul aan met één woord: she has … finished her work, dus ze kan naar huis.",
                "antwoord": ["already"],
                "uitleg": "Already staat tussen have en het deelwoord. Yet hoort in een vraag of een ontkenning.",
            },
            {
                "vraag": "Vul aan met één woord: we have … eaten, dus we hebben geen honger meer.",
                "antwoord": ["already"],
                "uitleg": "Already staat tussen have en het deelwoord. Yet hoort in een vraag of een ontkenning.",
            },
            {
                "vraag": "Vul aan met één woord: they have … left, dus bellen heeft geen zin meer.",
                "antwoord": ["already"],
                "uitleg": "Already staat tussen have en het deelwoord. Yet hoort in een vraag of een ontkenning.",
            },
        ],
        "'Just' betekent in 'I have just arrived' dat je nog maar net aangekomen bent.": [
            {
                "vraag": "In 'she has just left' betekent just dat ze nog maar net weg is.",
                "uitleg": "Just, already en yet horen alle drie bij de present perfect. Just staat tussen have en het deelwoord.",
            },
            {
                "vraag": "'Already' staat tussen have en het voltooid deelwoord.",
                "uitleg": "I have already finished. Just staat op dezelfde plaats.",
            },
            {
                "vraag": "'Yet' hoort in een vraag of een ontkenning.",
                "uitleg": "Have you finished yet? I haven't finished yet. In een bevestiging gebruik je already.",
            },
        ],
        "Welke zin hoort bij 'Ik ben mijn sleutels kwijt, ik vind ze nu niet.'?": [
            {
                "vraag": "Welke zin hoort bij 'Ik ben mijn portefeuille kwijt, ik vind hem nu niet.'?",
                "opties": [
                    "I have lost my wallet.",
                    "I lost my wallet.",
                    "I am losing my wallet.",
                    "I lose my wallet.",
                ],
                "uitleg": "De present perfect legt het verband met nu: het gevolg is er nog.",
            },
            {
                "vraag": "Welke zin hoort bij 'Hij heeft zijn been gebroken, hij loopt nu met krukken.'?",
                "opties": [
                    "He has broken his leg.",
                    "He broke his leg.",
                    "He is breaking his leg.",
                    "He breaks his leg.",
                ],
                "uitleg": "De present perfect legt het verband met nu: het gevolg is er nog.",
            },
            {
                "vraag": "Welke zin hoort bij 'Zij heeft haar gsm laten vallen, het scherm is nu stuk.'?",
                "opties": [
                    "She has dropped her phone.",
                    "She dropped her phone.",
                    "She is dropping her phone.",
                    "She drops her phone.",
                ],
                "uitleg": "De present perfect legt het verband met nu: het gevolg is er nog.",
            },
        ],
        "Welke zinnen horen in de past simple en niet in de present perfect?": [
            {
                "opties": [
                    "I met him last week.",
                    "They arrived in 2018.",
                    "She left an hour ago.",
                    "I have lived here for years.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Last week, in 2018 en ago noemen een afgesloten moment. For years loopt door tot nu.",
            },
            {
                "opties": [
                    "We visited Rome in 2021.",
                    "He called me yesterday.",
                    "She finished two days ago.",
                    "They have worked here since May.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "In 2021, yesterday en ago noemen een afgesloten moment. Since May loopt door tot nu.",
            },
            {
                "opties": [
                    "I read that book last summer.",
                    "She moved to Ghent in 2020.",
                    "He phoned three hours ago.",
                    "We have known them for ages.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Last summer, in 2020 en ago noemen een afgesloten moment. For ages loopt door tot nu.",
            },
        ],
        "Wat benadrukt 'I have been waiting for an hour'?": [
            {"vraag": "Wat benadrukt 'she has been studying all afternoon'?"},
            {"vraag": "Wat benadrukt 'they have been driving for six hours'?"},
            {"vraag": "Wat benadrukt 'he has been reading all evening'?"},
        ],
        "Welke zin past bij iemand die nu vuile handen heeft?": [
            {
                "vraag": "Welke zin past bij iemand die nu bezweet is van het lopen?",
                "opties": [
                    "I have been running.",
                    "I have run three times.",
                    "I run every week.",
                    "I will be running.",
                ],
            },
            {
                "vraag": "Welke zin past bij iemand die nu verfvlekken op de handen heeft?",
                "opties": [
                    "I have been painting.",
                    "I have painted three rooms.",
                    "I paint every summer.",
                    "I will be painting.",
                ],
            },
            {
                "vraag": "Welke zin past bij iemand die nu rode ogen heeft van het huilen?",
                "opties": [
                    "She has been crying.",
                    "She has cried three times.",
                    "She cries every night.",
                    "She will be crying.",
                ],
            },
        ],
    },
    "Modal auxiliaries, imperative en infinitive — deel 1": {
        "Wat zegt 'she can swim' over haar?": [
            {
                "vraag": "Wat zegt 'he can drive' over hem?",
                "opties": ["hij kan autorijden", "hij mag autorijden van iemand", "hij zal autorijden", "hij rijdt nu"],
            },
            {
                "vraag": "Wat zegt 'she can cook' over haar?",
                "opties": ["ze kan koken", "ze mag koken van iemand", "ze zal koken", "ze kookt nu"],
            },
            {
                "vraag": "Wat zegt 'they can speak Spanish' over hen?",
                "opties": [
                    "zij kunnen Spaans spreken",
                    "zij mogen Spaans spreken van iemand",
                    "zij zullen Spaans spreken",
                    "zij spreken nu Spaans",
                ],
            },
        ],
        "Een modaal hulpwerkwoord krijgt nooit een s in de derde persoon: she can, niet she cans.": [
            {
                "vraag": "Je zegt 'he must go' en niet 'he musts go'.",
                "uitleg": "Can, may, must, should, will en would blijven altijd hetzelfde. Daarna volgt de kale basisvorm.",
            },
            {
                "vraag": "Na een modaal hulpwerkwoord volgt de kale basisvorm.",
                "uitleg": "She can swim, he must go. Ought to is de enige uitzondering en heeft zijn to al vast.",
            },
            {
                "vraag": "'She should leave' is juist en 'she shoulds leave' niet.",
                "uitleg": "Een modaal hulpwerkwoord krijgt nooit een s in de derde persoon.",
            },
        ],
        "Welke zin is de beleefdste manier om iets te vragen?": [
            {
                "opties": [
                    "Could you open the window, please?",
                    "Can you open the window?",
                    "Open the window.",
                    "You must open the window.",
                ],
            },
            {
                "opties": [
                    "Could you wait a moment, please?",
                    "Can you wait a moment?",
                    "Wait a moment.",
                    "You must wait a moment.",
                ],
            },
            {
                "opties": [
                    "Could you pass me the salt, please?",
                    "Can you pass me the salt?",
                    "Pass me the salt.",
                    "You must pass me the salt.",
                ],
            },
        ],
        "Welke woorden zijn modale hulpwerkwoorden?": [
            {
                "opties": ["can", "may", "would", "need"],
                "antwoord": [0, 1, 2],
                "uitleg": "Need is meestal een gewoon werkwoord en neemt to: I need to go. Na een modaal hulpwerkwoord komt geen to.",
            },
            {
                "opties": ["could", "shall", "will", "hope"],
                "antwoord": [0, 1, 2],
                "uitleg": "Hope is een gewoon werkwoord en neemt to: I hope to go. Na een modaal hulpwerkwoord komt geen to.",
            },
            {
                "opties": ["must", "might", "should", "decide"],
                "antwoord": [0, 1, 2],
                "uitleg": "Decide is een gewoon werkwoord en neemt to: I decided to go. Na een modaal hulpwerkwoord komt geen to.",
            },
        ],
        "Wat betekent 'you mustn't park here'?": [
            {
                "vraag": "Wat betekent 'you mustn't smoke here'?",
                "opties": ["hier roken is verboden", "hier roken hoeft niet", "hier mag je roken", "hier rookt bijna niemand"],
            },
            {
                "vraag": "Wat betekent 'you mustn't touch that'?",
                "opties": ["dat aanraken is verboden", "dat aanraken hoeft niet", "dat mag je aanraken", "dat raakt bijna niemand aan"],
            },
            {
                "vraag": "Wat betekent 'you mustn't be late'?",
                "opties": ["te laat komen is verboden", "te laat komen hoeft niet", "je mag te laat komen", "bijna niemand komt te laat"],
            },
        ],
        "Wat betekent 'you don't have to come'?": [
            {
                "vraag": "Wat betekent 'you don't have to wait'?",
                "opties": ["je hoeft niet te wachten", "je mag niet wachten", "je moet zeker wachten", "je wacht beter toch"],
            },
            {
                "vraag": "Wat betekent 'you don't have to pay'?",
                "opties": ["je hoeft niet te betalen", "je mag niet betalen", "je moet zeker betalen", "je betaalt beter toch"],
            },
            {
                "vraag": "Wat betekent 'you don't have to answer'?",
                "opties": ["je hoeft niet te antwoorden", "je mag niet antwoorden", "je moet zeker antwoorden", "je antwoordt beter toch"],
            },
        ],
        "'Mustn't' en 'don't have to' betekenen ongeveer hetzelfde.": [
            {
                "vraag": "'You mustn't come' en 'you don't have to come' betekenen hetzelfde.",
                "uitleg": "Ze zijn bijna elkaars tegendeel. Mustn't is verboden, don't have to is niet nodig.",
            },
            {
                "vraag": "'Mustn't' betekent dat iets niet nodig is.",
                "uitleg": "Mustn't is een verbod. Niet nodig is don't have to.",
            },
            {
                "vraag": "'Don't have to' is een verbod.",
                "uitleg": "Don't have to laat je vrij. Het verbod is mustn't.",
            },
        ],
        "Vul het modale werkwoord in: you … wear a helmet here, het is verplicht.": [
            {
                "vraag": "Vul het modale werkwoord in: you … show your ticket here, het is verplicht.",
                "antwoord": ["must", "have to"],
                "uitleg": "Must of have to. Must klinkt alsof de spreker het zelf oplegt, have to alsof een regel het oplegt.",
            },
            {
                "vraag": "Vul het modale werkwoord in: you … wear a mask here, het is verplicht.",
                "antwoord": ["must", "have to"],
                "uitleg": "Must of have to. Must klinkt alsof de spreker het zelf oplegt, have to alsof een regel het oplegt.",
            },
            {
                "vraag": "Vul het modale werkwoord in: you … be quiet in the library, het is verplicht.",
                "antwoord": ["must", "have to"],
                "uitleg": "Must of have to. Must klinkt alsof de spreker het zelf oplegt, have to alsof een regel het oplegt.",
            },
        ],
        "Hoe zet je 'I must go' in de verleden tijd?": [
            {
                "vraag": "Hoe zet je 'She must work' in de verleden tijd?",
                "opties": ["She had to work", "She musted work", "She must worked", "She would must work"],
            },
            {
                "vraag": "Hoe zet je 'We must wait' in de verleden tijd?",
                "opties": ["We had to wait", "We musted wait", "We must waited", "We would must wait"],
            },
            {
                "vraag": "Hoe zet je 'He must leave' in de verleden tijd?",
                "opties": ["He had to leave", "He musted leave", "He must left", "He would must leave"],
            },
        ],
        "Welke zin geeft een advies?": [
            {
                "opties": [
                    "You should get some rest.",
                    "You must get some rest now.",
                    "You can get some rest.",
                    "You will get some rest.",
                ],
            },
            {
                "opties": [
                    "You should call her back.",
                    "You must call her back now.",
                    "You can call her back.",
                    "You will call her back.",
                ],
            },
            {
                "opties": [
                    "You should take an umbrella.",
                    "You must take an umbrella now.",
                    "You can take an umbrella.",
                    "You will take an umbrella.",
                ],
            },
        ],
        "Wat zegt 'it might rain tomorrow'?": [
            {
                "vraag": "Wat zegt 'she might come later'?",
                "opties": ["het is mogelijk dat ze komt", "ze komt zeker", "ze komt zeker niet", "ze kwam gisteren"],
            },
            {
                "vraag": "Wat zegt 'it might snow tonight'?",
                "opties": ["het is mogelijk dat het sneeuwt", "het sneeuwt zeker", "het sneeuwt zeker niet", "het sneeuwde gisteren"],
            },
            {
                "vraag": "Wat zegt 'he might be at home'?",
                "opties": ["het is mogelijk dat hij thuis is", "hij is zeker thuis", "hij is zeker niet thuis", "hij was gisteren thuis"],
            },
        ],
        "Welke zinnen drukken een mogelijkheid uit?": [
            {
                "opties": ["He may be asleep.", "He might arrive late.", "It could be a mistake.", "He must be asleep."],
                "antwoord": [0, 1, 2],
                "uitleg": "Must be klinkt juist als een zekerheid: het zal wel zo zijn. Dat is een conclusie, geen mogelijkheid.",
            },
            {
                "opties": ["She may know the answer.", "She might forget.", "It could rain later.", "She must know the answer."],
                "antwoord": [0, 1, 2],
                "uitleg": "Must know klinkt juist als een zekerheid: het zal wel zo zijn. Dat is een conclusie, geen mogelijkheid.",
            },
            {
                "opties": ["They may be lost.", "They might call back.", "It could be true.", "They must be lost."],
                "antwoord": [0, 1, 2],
                "uitleg": "Must be klinkt juist als een zekerheid: het zal wel zo zijn. Dat is een conclusie, geen mogelijkheid.",
            },
        ],
    },
    "Modal auxiliaries, imperative en infinitive — deel 2": {
        "Hoe maak je in het Engels een bevel?": [
            {
                "opties": [
                    "je gebruikt de kale basisvorm: open the window",
                    "je zet you ervoor: you open the window",
                    "je zet to ervoor: to open the window",
                    "je zet must ervoor: must open the window",
                ],
            },
            {
                "opties": [
                    "je gebruikt de kale basisvorm: turn left",
                    "je zet you ervoor: you turn left",
                    "je zet to ervoor: to turn left",
                    "je zet must ervoor: must turn left",
                ],
            },
            {
                "opties": [
                    "je gebruikt de kale basisvorm: sit down",
                    "je zet you ervoor: you sit down",
                    "je zet to ervoor: to sit down",
                    "je zet must ervoor: must sit down",
                ],
            },
        ],
        "Hoe maak je een bevel ontkennend?": [
            {"opties": ["don't touch that", "not touch that", "no touch that", "touch not that"]},
            {"opties": ["don't be late", "not be late", "no be late", "be not late"]},
            {"opties": ["don't forget your key", "not forget your key", "no forget your key", "forget not your key"]},
        ],
        "Vul aan met één woord: … go to the cinema tonight. Je stelt iets voor aan jezelf en je vrienden.": [
            {
                "vraag": "Vul aan met één woord: … take the bus. Je stelt iets voor aan jezelf en je vrienden.",
                "uitleg": "Let's is de korte vorm van let us. Het is de gebiedende wijs voor een groep waar je zelf bij hoort.",
            },
            {
                "vraag": "Vul aan met één woord: … start now. Je stelt iets voor aan jezelf en je vrienden.",
                "uitleg": "Let's is de korte vorm van let us. Het is de gebiedende wijs voor een groep waar je zelf bij hoort.",
            },
            {
                "vraag": "Vul aan met één woord: … meet at six. Je stelt iets voor aan jezelf en je vrienden.",
                "uitleg": "Let's is de korte vorm van let us. Het is de gebiedende wijs voor een groep waar je zelf bij hoort.",
            },
        ],
        "De imperatief is in het Engels altijd onbeleefd.": [
            {
                "vraag": "Een instructie in een recept staat nooit in de imperatief.",
                "uitleg": "Mix the eggs, turn left: recepten en instructies staan er juist vol mee.",
            },
            {
                "vraag": "Met 'please' erbij blijft de imperatief onbeleefd.",
                "uitleg": "Please sit down klinkt net vriendelijk.",
            },
            {
                "vraag": "De imperatief heeft in het Engels altijd een onderwerp.",
                "uitleg": "Close the door heeft er geen. Dat is net het kenmerk van de imperatief.",
            },
        ],
        "Na welke werkwoorden komt een infinitief met to?": [
            {
                "opties": ["promise", "agree", "refuse", "finish"],
                "antwoord": [0, 1, 2],
                "uitleg": "Na finish komt een -ing-vorm: I finished reading. Zo werkt het ook bij enjoy, avoid en mind.",
            },
            {
                "opties": ["learn", "offer", "plan", "avoid"],
                "antwoord": [0, 1, 2],
                "uitleg": "Na avoid komt een -ing-vorm: I avoid driving at night. Zo werkt het ook bij enjoy, finish en mind.",
            },
            {
                "opties": ["want", "choose", "expect", "mind"],
                "antwoord": [0, 1, 2],
                "uitleg": "Na mind komt een -ing-vorm: would you mind waiting? Zo werkt het ook bij enjoy, finish en avoid.",
            },
        ],
        "Vul de juiste vorm in: I enjoy … books. Gebruik het werkwoord read.": [
            {
                "vraag": "Vul de juiste vorm in: she finished … the letter. Gebruik het werkwoord write.",
                "antwoord": ["writing"],
                "uitleg": "Na enjoy, finish, avoid en mind komt altijd de -ing-vorm.",
            },
            {
                "vraag": "Vul de juiste vorm in: he avoids … at night. Gebruik het werkwoord drive.",
                "antwoord": ["driving"],
                "uitleg": "Na enjoy, finish, avoid en mind komt altijd de -ing-vorm.",
            },
            {
                "vraag": "Vul de juiste vorm in: would you mind … a moment? Gebruik het werkwoord wait.",
                "antwoord": ["waiting"],
                "uitleg": "Na enjoy, finish, avoid en mind komt altijd de -ing-vorm.",
            },
        ],
        "Na een voorzetsel komt in het Engels altijd de -ing-vorm: he left without saying goodbye.": [
            {
                "vraag": "Na 'after' als voorzetsel komt de -ing-vorm: after finishing his work, he left.",
                "uitleg": "Na een voorzetsel komt altijd de -ing-vorm.",
            },
            {
                "vraag": "'She is good at drawing' is juist omdat at een voorzetsel is.",
                "uitleg": "Na een voorzetsel komt altijd de -ing-vorm.",
            },
            {
                "vraag": "'Instead of waiting, he went home' is juist Engels.",
                "uitleg": "Na het voorzetsel of komt de -ing-vorm.",
            },
        ],
        "Welke zin zegt correct dat iemand jou aan het lachen bracht?": [
            {
                "vraag": "Welke zin zegt correct dat iemand jou liet wachten?",
                "opties": ["She made me wait.", "She made me to wait.", "She made me waiting.", "She made that I waited."],
                "uitleg": "Na make en let komt de kale infinitief: let him go, make her wait.",
            },
            {
                "vraag": "Welke zin zegt correct dat hij hem liet gaan?",
                "opties": ["He let him go.", "He let him to go.", "He let him going.", "He let that he went."],
                "uitleg": "Na make en let komt de kale infinitief: let him go, make her wait.",
            },
            {
                "vraag": "Welke zin zegt correct dat zij hem aan het huilen bracht?",
                "opties": ["She made him cry.", "She made him to cry.", "She made him crying.", "She made that he cried."],
                "uitleg": "Na make en let komt de kale infinitief: let him go, make her wait.",
            },
        ],
        "Na welke werkwoorden komt de kale infinitief, dus zonder to?": [
            {
                "opties": ["let", "make", "can", "want"],
                "antwoord": [0, 1, 2],
                "uitleg": "Want is een gewoon werkwoord en neemt to: I want to go. Na let, make en can komt de kale basisvorm.",
            },
            {
                "opties": ["make", "should", "let", "hope"],
                "antwoord": [0, 1, 2],
                "uitleg": "Hope is een gewoon werkwoord en neemt to: I hope to go. Na make, should en let komt de kale basisvorm.",
            },
            {
                "opties": ["let", "might", "make", "decide"],
                "antwoord": [0, 1, 2],
                "uitleg": "Decide is een gewoon werkwoord en neemt to: I decided to go. Na let, might en make komt de kale basisvorm.",
            },
        ],
        "Wat doet de 'do' in 'I do like your new coat'?": [
            {
                "vraag": "Wat doet de 'do' in 'I do believe you'?",
                "opties": [
                    "hij legt nadruk op believe",
                    "hij maakt er een vraag van",
                    "hij maakt er een ontkenning van",
                    "hij zet de zin in de verleden tijd",
                ],
                "uitleg": "Dat heet de emphatic do. In het Nederlands zou je zeggen: ik geloof je echt.",
            },
            {
                "vraag": "Wat doet de 'does' in 'She does look tired'?",
                "opties": [
                    "hij legt nadruk op look",
                    "hij maakt er een vraag van",
                    "hij maakt er een ontkenning van",
                    "hij zet de zin in de verleden tijd",
                ],
                "uitleg": "Dat heet de emphatic do. Zonder does blijft de zin kloppen, en net daarom geeft hij nadruk.",
            },
            {
                "vraag": "Wat doet de 'did' in 'I did tell you'?",
                "opties": [
                    "hij legt nadruk op tell",
                    "hij maakt er een vraag van",
                    "hij maakt er een ontkenning van",
                    "hij zet de zin in de tegenwoordige tijd",
                ],
                "uitleg": "Dat heet de emphatic do. In het Nederlands zou je zeggen: ik heb het je wel degelijk gezegd.",
            },
        ],
        "Welke zin wenst iemand correct veel plezier op een feest?": [
            {
                "vraag": "Welke zin wenst iemand correct veel plezier op een concert?",
                "opties": [
                    "Enjoy yourself at the concert!",
                    "Enjoy you at the concert!",
                    "Enjoy at the concert!",
                    "Enjoy your at the concert!",
                ],
            },
            {
                "vraag": "Welke zin wenst een groep correct veel plezier op de reis?",
                "opties": [
                    "Enjoy yourselves on the trip!",
                    "Enjoy you on the trip!",
                    "Enjoy on the trip!",
                    "Enjoy your on the trip!",
                ],
            },
            {
                "vraag": "Welke zin nodigt iemand correct uit om zichzelf te bedienen?",
                "opties": [
                    "Help yourself to some cake!",
                    "Help you to some cake!",
                    "Help to some cake!",
                    "Help your to some cake!",
                ],
            },
        ],
        "Welke zin zegt correct dat de rit een uur duurt?": [
            {
                "vraag": "Welke zin zegt correct dat de rit twee uur duurt?",
                "opties": [
                    "It takes two hours to drive there.",
                    "Takes two hours to drive there.",
                    "There takes two hours to drive there.",
                    "It take two hours to drive there.",
                ],
            },
            {
                "vraag": "Welke zin zegt correct dat de wandeling tien minuten duurt?",
                "opties": [
                    "It takes ten minutes to walk home.",
                    "Takes ten minutes to walk home.",
                    "There takes ten minutes to walk home.",
                    "It take ten minutes to walk home.",
                ],
            },
            {
                "vraag": "Welke zin zegt correct dat het werk een week duurt?",
                "opties": [
                    "It takes a week to finish this.",
                    "Takes a week to finish this.",
                    "There takes a week to finish this.",
                    "It take a week to finish this.",
                ],
            },
        ],
    },
    "Zinsdelen, soorten zinnen en bijzinnen — deel 1": {
        "Wat is het onderwerp in 'My little sister reads three books a week'?": [
            {
                "vraag": "Wat is het onderwerp in 'My older brother plays two matches a week'?",
                "opties": ["my older brother", "plays", "two matches", "a week"],
                "uitleg": "Het onderwerp is wie of wat de persoonsvorm doet. Je vindt het door te vragen: wie speelt?",
            },
            {
                "vraag": "Wat is het onderwerp in 'Our new teacher gives three tests a month'?",
                "opties": ["our new teacher", "gives", "three tests", "a month"],
                "uitleg": "Het onderwerp is wie of wat de persoonsvorm doet. Je vindt het door te vragen: wie geeft?",
            },
            {
                "vraag": "Wat is het onderwerp in 'The old baker sells fresh bread every day'?",
                "opties": ["the old baker", "sells", "fresh bread", "every day"],
                "uitleg": "Het onderwerp is wie of wat de persoonsvorm doet. Je vindt het door te vragen: wie verkoopt?",
            },
        ],
        "Wat is de persoonsvorm in 'The children were playing outside'?": [
            {
                "vraag": "Wat is de persoonsvorm in 'The dog was barking loudly'?",
                "opties": ["was", "barking", "the dog", "loudly"],
                "uitleg": "De persoonsvorm is het werkwoord dat met het onderwerp meeverandert. Barking verandert niet mee.",
            },
            {
                "vraag": "Wat is de persoonsvorm in 'My friends are waiting downstairs'?",
                "opties": ["are", "waiting", "my friends", "downstairs"],
                "uitleg": "De persoonsvorm is het werkwoord dat met het onderwerp meeverandert. Waiting verandert niet mee.",
            },
            {
                "vraag": "Wat is de persoonsvorm in 'She has finished her homework'?",
                "opties": ["has", "finished", "she", "her homework"],
                "uitleg": "De persoonsvorm is het werkwoord dat met het onderwerp meeverandert. Finished verandert niet mee.",
            },
        ],
        "Wat is het lijdend voorwerp in 'She wrote a long letter'? Antwoord met de Engelse woorden.": [
            {
                "vraag": "Wat is het lijdend voorwerp in 'He bought a new bike'? Antwoord met de Engelse woorden.",
                "antwoord": ["a new bike", "bike", "new bike"],
                "uitleg": "Het lijdend voorwerp ondergaat de handeling. Je vindt het met: wat kocht hij?",
            },
            {
                "vraag": "Wat is het lijdend voorwerp in 'They painted the old door'? Antwoord met de Engelse woorden.",
                "antwoord": ["the old door", "door", "old door"],
                "uitleg": "Het lijdend voorwerp ondergaat de handeling. Je vindt het met: wat schilderden zij?",
            },
            {
                "vraag": "Wat is het lijdend voorwerp in 'She baked a big cake'? Antwoord met de Engelse woorden.",
                "antwoord": ["a big cake", "cake", "big cake"],
                "uitleg": "Het lijdend voorwerp ondergaat de handeling. Je vindt het met: wat bakte zij?",
            },
        ],
        "Wat is het meewerkend voorwerp in 'He gave his friend a present'?": [
            {
                "vraag": "Wat is het meewerkend voorwerp in 'She sent her sister a card'?",
                "opties": ["her sister", "a card", "she", "sent"],
                "uitleg": "Het meewerkend voorwerp is voor wie of aan wie iets gebeurt. Je kan het ook schrijven als she sent a card to her sister.",
            },
            {
                "vraag": "Wat is het meewerkend voorwerp in 'They offered the guests a drink'?",
                "opties": ["the guests", "a drink", "they", "offered"],
                "uitleg": "Het meewerkend voorwerp is voor wie of aan wie iets gebeurt. Je kan het ook schrijven als they offered a drink to the guests.",
            },
            {
                "vraag": "Wat is het meewerkend voorwerp in 'He showed the teacher his work'?",
                "opties": ["the teacher", "his work", "he", "showed"],
                "uitleg": "Het meewerkend voorwerp is voor wie of aan wie iets gebeurt. Je kan het ook schrijven als he showed his work to the teacher.",
            },
        ],
        "Staat het meewerkend voorwerp achter het lijdend voorwerp, dan komt er 'to' of 'for' voor.": [
            {
                "vraag": "'She sent a card to him' en 'she sent him a card' betekenen hetzelfde.",
                "uitleg": "Zonder voorzetsel staat het meewerkend voorwerp eerst.",
            },
            {
                "vraag": "Zonder voorzetsel staat het meewerkend voorwerp voor het lijdend voorwerp.",
                "uitleg": "He gave his friend a present, of he gave a present to his friend.",
            },
            {
                "vraag": "'He bought a book for his sister' is juist Engels.",
                "uitleg": "Staat het meewerkend voorwerp achteraan, dan komt er to of for voor.",
            },
        ],
        "Welke zin over het leuk vinden van een film is juist?": [
            {
                "vraag": "Welke zin over het leuk vinden van een boek is juist?",
                "opties": [
                    "I like this book very much.",
                    "I like very much this book.",
                    "I very much like this book today here.",
                    "I like this very much book.",
                ],
            },
            {
                "vraag": "Welke zin over het leuk vinden van een liedje is juist?",
                "opties": [
                    "I like this song very much.",
                    "I like very much this song.",
                    "I very much like this song today here.",
                    "I like this very much song.",
                ],
            },
            {
                "vraag": "Welke zin over het leuk vinden van dat spel is juist?",
                "opties": [
                    "I like that game very much.",
                    "I like very much that game.",
                    "I very much like that game today here.",
                    "I like that very much game.",
                ],
            },
        ],
        "Welke zin heeft de bepalingen in de gewone Engelse volgorde?": [
            {
                "opties": [
                    "He played brilliantly at the festival last week.",
                    "He played last week brilliantly at the festival.",
                    "He played at the festival brilliantly last week.",
                    "Last week he played at the festival brilliantly.",
                ],
            },
            {
                "opties": [
                    "They worked hard in the garden all morning.",
                    "They worked all morning hard in the garden.",
                    "They worked in the garden hard all morning.",
                    "All morning they worked in the garden hard.",
                ],
            },
            {
                "opties": [
                    "She spoke calmly in the classroom yesterday.",
                    "She spoke yesterday calmly in the classroom.",
                    "She spoke in the classroom calmly yesterday.",
                    "Yesterday she spoke in the classroom calmly.",
                ],
            },
        ],
        "In het Engels mag je na een bepaling vooraan het onderwerp en de persoonsvorm omwisselen: yesterday went I home.": [
            {
                "vraag": "'Last week went she to London' is juist Engels.",
                "uitleg": "Dat doet het Nederlands wel, het Engels niet. Het blijft last week she went to London.",
            },
            {
                "vraag": "'Tomorrow will come he' is juist Engels.",
                "uitleg": "Het blijft tomorrow he will come. Het Engels wisselt niet om na een bepaling vooraan.",
            },
            {
                "vraag": "Na een bepaling vooraan schuift het onderwerp in het Engels achter de persoonsvorm.",
                "uitleg": "Dat doet het Nederlands. In het Engels blijft het yesterday I went home.",
            },
        ],
        "Hoe maak je van 'She plays tennis' een vraag?": [
            {
                "vraag": "Hoe maak je van 'He works here' een vraag?",
                "opties": ["Does he work here?", "Works he here?", "Does he works here?", "He works here?"],
            },
            {
                "vraag": "Hoe maak je van 'They live in Ghent' een vraag?",
                "opties": ["Do they live in Ghent?", "Live they in Ghent?", "Do they lives in Ghent?", "They live in Ghent?"],
            },
            {
                "vraag": "Hoe maak je van 'She studies French' een vraag?",
                "opties": ["Does she study French?", "Studies she French?", "Does she studies French?", "She studies French?"],
            },
        ],
        "Welke aanhangvraag hoort bij 'You're coming tonight, …?'": [
            {
                "vraag": "Welke aanhangvraag hoort bij 'She's your sister, …?'",
                "opties": ["isn't she", "is she", "doesn't she", "aren't they"],
            },
            {
                "vraag": "Welke aanhangvraag hoort bij 'They live here, …?'",
                "opties": ["don't they", "do they", "aren't they", "isn't it"],
            },
            {
                "vraag": "Welke aanhangvraag hoort bij 'He can swim, …?'",
                "opties": ["can't he", "can he", "doesn't he", "isn't he"],
            },
        ],
        "Welke zin over twee mensen die samen uitgaan is juist?": [
            {
                "vraag": "Welke zin over twee mensen die samen koken is juist?",
                "opties": [
                    "My sister and I are cooking.",
                    "My sister and I is cooking.",
                    "My sister and me is cooking.",
                    "My sister and I am cooking.",
                ],
            },
            {
                "vraag": "Welke zin over twee mensen die samen wachten is juist?",
                "opties": [
                    "Tom and I are waiting outside.",
                    "Tom and I is waiting outside.",
                    "Tom and me is waiting outside.",
                    "Tom and I am waiting outside.",
                ],
            },
            {
                "vraag": "Welke zin over twee mensen die samen vertrekken is juist?",
                "opties": [
                    "My friend and I are leaving now.",
                    "My friend and I is leaving now.",
                    "My friend and me is leaving now.",
                    "My friend and I am leaving now.",
                ],
            },
        ],
        "Welke zin is ontkennend en juist?": [
            {
                "opties": [
                    "He doesn't like coffee.",
                    "He not likes coffee.",
                    "He doesn't likes coffee.",
                    "He likes not coffee.",
                ],
            },
            {
                "opties": [
                    "They don't play football.",
                    "They not play football.",
                    "They don't plays football.",
                    "They play not football.",
                ],
            },
            {
                "opties": [
                    "She doesn't work on Fridays.",
                    "She not works on Fridays.",
                    "She doesn't works on Fridays.",
                    "She works not on Fridays.",
                ],
            },
        ],
    },
    "Zinsdelen, soorten zinnen en bijzinnen — deel 2": {
        "Welke woorden zijn nevenschikkende voegwoorden?": [
            {
                "opties": ["and", "so", "or", "although"],
                "antwoord": [0, 1, 2],
                "uitleg": "Although is onderschikkend: het maakt van het tweede deel een bijzin die niet alleen kan staan.",
            },
            {
                "opties": ["but", "or", "so", "unless"],
                "antwoord": [0, 1, 2],
                "uitleg": "Unless is onderschikkend: het maakt van het tweede deel een bijzin die niet alleen kan staan.",
            },
            {
                "opties": ["and", "but", "so", "while"],
                "antwoord": [0, 1, 2],
                "uitleg": "While is onderschikkend: het maakt van het tweede deel een bijzin die niet alleen kan staan.",
            },
        ],
        "Welk voegwoord past? I stayed at home … it was raining.": [
            {
                "vraag": "Welk voegwoord past? She was late … the train broke down.",
                "uitleg": "Because geeft de reden. So geeft juist het gevolg: the train broke down, so she was late.",
            },
            {
                "vraag": "Welk voegwoord past? He took an umbrella … it looked like rain.",
                "uitleg": "Because geeft de reden. So geeft juist het gevolg: it looked like rain, so he took an umbrella.",
            },
            {
                "vraag": "Welk voegwoord past? We waited outside … the door was locked.",
                "uitleg": "Because geeft de reden. So geeft juist het gevolg: the door was locked, so we waited outside.",
            },
        ],
        "Vul één voegwoord in dat een tegenstelling aangeeft: she was tired, … she kept working.": [
            {
                "vraag": "Vul één voegwoord in dat een tegenstelling aangeeft: it was cold, … we went outside.",
                "uitleg": "But is het gewone woord. Yet kan ook en klinkt iets formeler.",
            },
            {
                "vraag": "Vul één voegwoord in dat een tegenstelling aangeeft: he studied hard, … he failed.",
                "uitleg": "But is het gewone woord. Yet kan ook en klinkt iets formeler.",
            },
            {
                "vraag": "Vul één voegwoord in dat een tegenstelling aangeeft: the film was long, … nobody left.",
                "uitleg": "But is het gewone woord. Yet kan ook en klinkt iets formeler.",
            },
        ],
        "'Although' en 'but' mag je in dezelfde zin samen gebruiken: although she was tired, but she kept working.": [
            {
                "vraag": "'Although it was cold, but we went outside' is juist Engels.",
                "uitleg": "Eén tegenstelling per zin volstaat: although it was cold, we went outside.",
            },
            {
                "vraag": "Je mag 'although' en 'but' in dezelfde zin combineren.",
                "uitleg": "Kies er één: although she was tired, she kept working, of she was tired but she kept working.",
            },
            {
                "vraag": "'Because it was raining, so I stayed at home' is juist Engels.",
                "uitleg": "Eén verband per zin volstaat: because it was raining, I stayed at home.",
            },
        ],
        "Welke woorden zijn onderschikkende voegwoorden?": [
            {
                "opties": ["if", "when", "because", "and"],
                "antwoord": [0, 1, 2],
                "uitleg": "And is nevenschikkend. Onderschikkende voegwoorden zijn ook although, unless, since en until.",
            },
            {
                "opties": ["since", "until", "unless", "but"],
                "antwoord": [0, 1, 2],
                "uitleg": "But is nevenschikkend. Onderschikkende voegwoorden zijn ook if, when, because en although.",
            },
            {
                "opties": ["while", "although", "if", "or"],
                "antwoord": [0, 1, 2],
                "uitleg": "Or is nevenschikkend. Onderschikkende voegwoorden zijn ook unless, since en until.",
            },
        ],
        "Wat betekent 'unless you hurry, you will miss the bus'?": [
            {
                "vraag": "Wat betekent 'unless you study, you will fail'?",
                "opties": [
                    "als je niet studeert, buis je",
                    "als je studeert, buis je",
                    "omdat je studeert, buis je",
                    "terwijl je studeert, buis je",
                ],
                "uitleg": "Unless betekent if not. Er staat dus al een ontkenning in, en je zet er geen tweede bij.",
            },
            {
                "vraag": "Wat betekent 'unless it stops raining, we will stay inside'?",
                "opties": [
                    "als het niet stopt met regenen, blijven we binnen",
                    "als het stopt met regenen, blijven we binnen",
                    "omdat het regent, blijven we binnen",
                    "terwijl het regent, blijven we binnen",
                ],
                "uitleg": "Unless betekent if not. Er staat dus al een ontkenning in, en je zet er geen tweede bij.",
            },
            {
                "vraag": "Wat betekent 'unless he calls, I will leave'?",
                "opties": [
                    "als hij niet belt, vertrek ik",
                    "als hij belt, vertrek ik",
                    "omdat hij belt, vertrek ik",
                    "terwijl hij belt, vertrek ik",
                ],
                "uitleg": "Unless betekent if not. Er staat dus al een ontkenning in, en je zet er geen tweede bij.",
            },
        ],
        "In welke zin staat een betrekkelijke bijzin?": [
            {
                "opties": [
                    "The woman who called is my aunt.",
                    "The woman is my aunt and she called.",
                    "The woman called, so she is my aunt.",
                    "Did the woman call you?",
                ],
            },
            {
                "opties": [
                    "The book that I borrowed is great.",
                    "I borrowed the book and it is great.",
                    "I borrowed the book, so it is great.",
                    "Did you borrow that book?",
                ],
            },
            {
                "opties": [
                    "The house which stands empty is old.",
                    "The house is old and it stands empty.",
                    "The house stands empty, so it is old.",
                    "Is that house still empty?",
                ],
            },
        ],
        "Vul aan met één woord: this is the house … we lived for ten years. Het gaat over een plaats.": [
            {
                "vraag": "Vul aan met één woord: this is the village … I grew up. Het gaat over een plaats.",
                "antwoord": ["where"],
                "uitleg": "Where verwijst naar een plaats, when naar een tijd en why naar een reden.",
            },
            {
                "vraag": "Vul aan met één woord: that is the school … she studied. Het gaat over een plaats.",
                "antwoord": ["where"],
                "uitleg": "Where verwijst naar een plaats, when naar een tijd en why naar een reden.",
            },
            {
                "vraag": "Vul aan met één woord: I remember the day … we met. Het gaat over een tijdstip.",
                "antwoord": ["when"],
                "uitleg": "When verwijst naar een tijd, where naar een plaats en why naar een reden.",
            },
        ],
        "Een bijzin die alleen extra informatie geeft, zet je tussen komma's: my sister, who lives in Ghent, is a vet.": [
            {
                "vraag": "Komma's rond een bijzin betekenen dat de bijzin alleen extra informatie geeft.",
                "uitleg": "Zonder komma's beperkt de bijzin wie je bedoelt.",
            },
            {
                "vraag": "'My brother, who lives in Bruges, is a baker' zegt dat je één broer hebt.",
                "uitleg": "De komma's maken van de bijzin extra informatie. Zonder komma's zou je meer dan één broer hebben.",
            },
            {
                "vraag": "Zonder komma's beperkt een betrekkelijke bijzin wie of wat je bedoelt.",
                "uitleg": "My sister who lives in Ghent betekent dat je meer dan één zus hebt.",
            },
        ],
        "Welke zinnen zijn conditionals zero?": [
            {
                "opties": [
                    "If you heat ice, it melts.",
                    "If you drop a ball, it falls.",
                    "If you turn the key, the engine starts.",
                    "If it snows, we will stay at home.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "De laatste kijkt naar één bepaalde keer in de toekomst, dus dat is een conditional first met will.",
            },
            {
                "opties": [
                    "If you mix red and white, you get pink.",
                    "If the sun shines, the ice melts.",
                    "If you pull this lever, the door opens.",
                    "If she calls, I will answer.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "De laatste kijkt naar één bepaalde keer in de toekomst, dus dat is een conditional first met will.",
            },
            {
                "opties": [
                    "If water freezes, it expands.",
                    "If you touch fire, it burns.",
                    "If you push this switch, the fan turns.",
                    "If they arrive late, we will start without them.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "De laatste kijkt naar één bepaalde keer in de toekomst, dus dat is een conditional first met will.",
            },
        ],
        "Vul aan met één woord: if you study hard, you … pass. Het gaat over één keer, in de toekomst.": [
            {
                "vraag": "Vul aan met één woord: if it rains, we … stay at home. Het gaat over één keer, in de toekomst.",
                "uitleg": "Dat is de conditional first: if plus present simple in de bijzin, en will in de hoofdzin.",
            },
            {
                "vraag": "Vul aan met één woord: if she calls, I … answer. Het gaat over één keer, in de toekomst.",
                "uitleg": "Dat is de conditional first: if plus present simple in de bijzin, en will in de hoofdzin.",
            },
            {
                "vraag": "Vul aan met één woord: if they arrive late, we … start without them. Het gaat over één keer, in de toekomst.",
                "uitleg": "Dat is de conditional first: if plus present simple in de bijzin, en will in de hoofdzin.",
            },
        ],
        "Welke zin is een conditional first?": [
            {
                "opties": [
                    "If it rains, I will take the bus.",
                    "If it rained, I would take the bus.",
                    "If it rains, I take the bus every time.",
                    "If it had rained, I would have taken the bus.",
                ],
            },
            {
                "opties": [
                    "If she calls, I will answer.",
                    "If she called, I would answer.",
                    "If she calls, I answer every time.",
                    "If she had called, I would have answered.",
                ],
            },
            {
                "opties": [
                    "If we leave now, we will be on time.",
                    "If we left now, we would be on time.",
                    "If we leave now, we are on time every time.",
                    "If we had left now, we would have been on time.",
                ],
            },
        ],
    },
    "De verleden en de toekomende tijden — deel 1": {
        "Schrijf de past simple van 'to study'.": [
            {
                "vraag": "Schrijf de past simple van 'to try'.",
                "antwoord": ["tried"],
                "uitleg": "Een y na een medeklinker wordt i en dan komt ed: tried, studied, carried. Staat er een klinker voor, dan blijft de y: played.",
            },
            {
                "vraag": "Schrijf de past simple van 'to carry'.",
                "antwoord": ["carried"],
                "uitleg": "Een y na een medeklinker wordt i en dan komt ed: carried, studied, tried. Staat er een klinker voor, dan blijft de y: played.",
            },
            {
                "vraag": "Schrijf de past simple van 'to play'.",
                "antwoord": ["played"],
                "uitleg": "Voor de y staat een klinker, dus blijft ze staan. Bij een medeklinker ervoor wordt het ied: studied.",
            },
        ],
        "Welke past simple vormen zijn juist geschreven?": [
            {
                "opties": ["planned", "hoped", "cancelled", "planed"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij plan verdubbelt de n. Bij hope was er al een e, dus komt er alleen d bij.",
            },
            {
                "opties": ["dropped", "closed", "travelled", "droped"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij drop verdubbelt de p. Bij close was er al een e, dus komt er alleen d bij.",
            },
            {
                "opties": ["shopped", "smiled", "levelled", "shoped"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij shop verdubbelt de p. Bij smile was er al een e, dus komt er alleen d bij.",
            },
        ],
        "Wat is de past simple van 'to buy'?": [
            {
                "vraag": "Wat is de past simple van 'to bring'?",
                "opties": ["brought", "bringed", "broughted", "branged"],
                "uitleg": "Bring, brought, brought. Net als buy, bought, bought en think, thought, thought.",
            },
            {
                "vraag": "Wat is de past simple van 'to think'?",
                "opties": ["thought", "thinked", "thoughted", "thunk"],
                "uitleg": "Think, thought, thought. Net als buy, bought, bought en bring, brought, brought.",
            },
            {
                "vraag": "Wat is de past simple van 'to teach'?",
                "opties": ["taught", "teached", "taughted", "teachted"],
                "uitleg": "Teach, taught, taught. Net als catch, caught, caught.",
            },
        ],
        "Schrijf de past simple van 'to write'.": [
            {
                "vraag": "Schrijf de past simple van 'to drive'.",
                "antwoord": ["drove"],
                "uitleg": "Drive, drove, driven. De derde vorm driven heb je nodig na have en had.",
            },
            {
                "vraag": "Schrijf de past simple van 'to speak'.",
                "antwoord": ["spoke"],
                "uitleg": "Speak, spoke, spoken. De derde vorm spoken heb je nodig na have en had.",
            },
            {
                "vraag": "Schrijf de past simple van 'to choose'.",
                "antwoord": ["chose"],
                "uitleg": "Choose, chose, chosen. De derde vorm chosen heb je nodig na have en had.",
            },
        ],
        "Welke rijen van drie vormen kloppen helemaal?": [
            {
                "opties": ["eat, ate, eaten", "write, wrote, written", "give, gave, given", "swim, swum, swam"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het is swim, swam, swum. Eerst de verleden tijd, dan het voltooid deelwoord.",
            },
            {
                "opties": ["speak, spoke, spoken", "drive, drove, driven", "choose, chose, chosen", "sing, sung, sang"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het is sing, sang, sung. Eerst de verleden tijd, dan het voltooid deelwoord.",
            },
            {
                "opties": ["break, broke, broken", "fly, flew, flown", "know, knew, known", "ring, rung, rang"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het is ring, rang, rung. Eerst de verleden tijd, dan het voltooid deelwoord.",
            },
        ],
        "In een vraag in de past simple gebruik je 'did' en blijft het werkwoord in de basisvorm.": [
            {
                "vraag": "'Did you go to the party?' is juist, en 'did you went' niet.",
                "uitleg": "De verleden tijd zit al in did, dus het werkwoord blijft in de basisvorm.",
            },
            {
                "vraag": "Na 'didn't' blijft het werkwoord in de basisvorm.",
                "uitleg": "She didn't come, niet she didn't came. De verleden tijd zit al in didn't.",
            },
            {
                "vraag": "In een ontkenning in de past simple gebruik je 'didn't' plus de basisvorm.",
                "uitleg": "They didn't see it, niet they didn't saw it.",
            },
        ],
        "Welke ontkennende zin over gisteren is juist?": [
            {
                "opties": [
                    "He didn't call yesterday.",
                    "He didn't called yesterday.",
                    "He don't called yesterday.",
                    "He not called yesterday.",
                ],
            },
            {
                "opties": [
                    "They didn't win the match.",
                    "They didn't won the match.",
                    "They don't won the match.",
                    "They not won the match.",
                ],
            },
            {
                "opties": [
                    "We didn't see the film.",
                    "We didn't saw the film.",
                    "We don't saw the film.",
                    "We not saw the film.",
                ],
            },
        ],
        "Bij het werkwoord 'to be' gebruik je in een vraag ook 'did': did you was there?": [
            {
                "vraag": "'Did he was at home?' is juist Engels.",
                "uitleg": "To be heeft geen did nodig: was he at home?",
            },
            {
                "vraag": "Bij 'to be' zet je in een ontkenning 'didn't': she didn't was there.",
                "uitleg": "To be heeft geen did nodig: she wasn't there.",
            },
            {
                "vraag": "'Did they were late?' is juist Engels.",
                "uitleg": "To be heeft geen did nodig: were they late?",
            },
        ],
        "Welke vorm van to be hoort bij 'they' in de verleden tijd?": [
            {
                "vraag": "Welke vorm van to be hoort bij 'she' in de verleden tijd?",
                "opties": ["was", "were", "been", "is"],
            },
            {
                "vraag": "Welke vorm van to be hoort bij 'we' in de verleden tijd?",
                "opties": ["were", "was", "been", "are"],
            },
            {
                "vraag": "Welke vorm van to be hoort bij 'it' in de verleden tijd?",
                "opties": ["was", "were", "been", "is"],
            },
        ],
        "Welke zin over lezen en een rinkelende telefoon is juist?": [
            {
                "vraag": "Welke zin over koken en een bel aan de deur is juist?",
                "opties": [
                    "I was cooking when the bell rang.",
                    "I cooked when the bell was ringing.",
                    "I was cook when the bell rang.",
                    "I was cooking when the bell was ring.",
                ],
            },
            {
                "vraag": "Welke zin over fietsen en het begin van de regen is juist?",
                "opties": [
                    "She was cycling when it started to rain.",
                    "She cycled when it was starting to rain.",
                    "She was cycle when it started to rain.",
                    "She was cycling when it was start to rain.",
                ],
            },
            {
                "vraag": "Welke zin over slapen en een klop op de deur is juist?",
                "opties": [
                    "He was sleeping when someone knocked.",
                    "He slept when someone was knocking.",
                    "He was sleep when someone knocked.",
                    "He was sleeping when someone was knock.",
                ],
            },
        ],
        "Welke vraag naar wat iemand om acht uur deed is juist?": [
            {
                "vraag": "Welke vraag naar wat iemand om zes uur deed is juist?",
                "opties": [
                    "What were you doing at six o'clock?",
                    "What did you doing at six o'clock?",
                    "What you were doing at six o'clock?",
                    "What were you do at six o'clock?",
                ],
            },
            {
                "vraag": "Welke vraag naar wat zij gisteravond deden is juist?",
                "opties": [
                    "What were they doing last night?",
                    "What did they doing last night?",
                    "What they were doing last night?",
                    "What were they do last night?",
                ],
            },
            {
                "vraag": "Welke vraag naar wat zij vanmorgen deed is juist?",
                "opties": [
                    "What was she doing this morning?",
                    "What did she doing this morning?",
                    "What she was doing this morning?",
                    "What was she do this morning?",
                ],
                "uitleg": "In een vraag wisselen was en het onderwerp van plaats.",
            },
        ],
        "Welk woord verraadt meteen dat je de past simple nodig hebt?": [
            {
                "opties": ["last week", "since", "already", "yet"],
                "uitleg": "Yesterday, last week en ago noemen een afgesloten moment. Since, already en yet horen bij de present perfect.",
            },
            {
                "opties": ["two days ago", "since", "already", "yet"],
                "uitleg": "Yesterday, last week en ago noemen een afgesloten moment. Since, already en yet horen bij de present perfect.",
            },
            {
                "opties": ["in 2019", "since", "already", "yet"],
                "uitleg": "Yesterday, in 2019 en ago noemen een afgesloten moment. Since, already en yet horen bij de present perfect.",
            },
        ],
    },
    "De verleden en de toekomende tijden — deel 2": {
        "Welke zin over een trein die al weg was is juist?": [
            {
                "vraag": "Welke zin over een film die al begonnen was is juist?",
                "opties": [
                    "The film had already started when we arrived.",
                    "The film has already started when we arrived.",
                    "The film had already start when we arrived.",
                    "The film was already starting when we arrived.",
                ],
            },
            {
                "vraag": "Welke zin over gasten die al vertrokken waren is juist?",
                "opties": [
                    "The guests had already left when I called.",
                    "The guests have already left when I called.",
                    "The guests had already leave when I called.",
                    "The guests were already leave when I called.",
                ],
            },
            {
                "vraag": "Welke zin over een winkel die al dicht was is juist?",
                "opties": [
                    "The shop had already closed when we got there.",
                    "The shop has already closed when we got there.",
                    "The shop had already close when we got there.",
                    "The shop had already closing when we got there.",
                ],
            },
        ],
        "Vul het ontbrekende woord in: by the time she called, I … already gone to bed.": [
            {
                "vraag": "Vul het ontbrekende woord in: by the time we arrived, the film … already started.",
                "uitleg": "Twee momenten in het verleden: het oudste krijgt de past perfect.",
            },
            {
                "vraag": "Vul het ontbrekende woord in: when I got home, my brother … already cooked.",
                "uitleg": "Twee momenten in het verleden: het oudste krijgt de past perfect.",
            },
            {
                "vraag": "Vul het ontbrekende woord in: by the time the bell rang, they … already finished.",
                "uitleg": "Twee momenten in het verleden: het oudste krijgt de past perfect.",
            },
        ],
        "De past perfect gebruik je om te tonen welk van twee dingen in het verleden het eerst gebeurde.": [
            {
                "vraag": "In 'the train had left when we arrived' vertrok de trein het eerst.",
                "uitleg": "De past perfect staat bij wat het eerst gebeurde.",
            },
            {
                "vraag": "Had is dezelfde vorm voor elke persoon.",
                "uitleg": "I had seen, she had seen, they had seen.",
            },
            {
                "vraag": "Zonder verschil in tijd volstaat de past simple.",
                "uitleg": "Twee keer had is dus zelden nodig.",
            },
        ],
        "Welke zin klopt qua volgorde in de tijd? 'When I got home, my brother had cooked dinner.'": [
            {
                "vraag": "Welke zin klopt qua volgorde in de tijd? 'When we arrived, the film had started.'",
                "opties": [
                    "de film begon eerst en daarna kwamen wij aan",
                    "wij kwamen eerst aan en daarna begon de film",
                    "we deden allebei tegelijk iets",
                    "het is nog niet gebeurd",
                ],
                "uitleg": "De past perfect staat bij wat het eerst gebeurde.",
            },
            {
                "vraag": "Welke zin klopt qua volgorde in de tijd? 'When she called, I had gone to bed.'",
                "opties": [
                    "ik ging eerst slapen en daarna belde zij",
                    "zij belde eerst en daarna ging ik slapen",
                    "we deden allebei tegelijk iets",
                    "het is nog niet gebeurd",
                ],
                "uitleg": "De past perfect staat bij wat het eerst gebeurde.",
            },
            {
                "vraag": "Welke zin klopt qua volgorde in de tijd? 'When the bell rang, they had finished the test.'",
                "opties": [
                    "zij waren eerst klaar en daarna ging de bel",
                    "de bel ging eerst en daarna waren zij klaar",
                    "het gebeurde allebei tegelijk",
                    "het is nog niet gebeurd",
                ],
                "uitleg": "De past perfect staat bij wat het eerst gebeurde.",
            },
        ],
        "Welke zinnen hebben terecht een past perfect?": [
            {
                "opties": [
                    "He had never flown before that summer.",
                    "We had eaten before the film started.",
                    "She had lost her ticket, so she could not enter.",
                    "Last week I had cycled to school.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Last week I cycled to school volstaat: er is geen tweede, later moment om mee te vergelijken.",
            },
            {
                "opties": [
                    "They had never met before that day.",
                    "I had packed my bag before the taxi came.",
                    "He had forgotten his password, so he could not log in.",
                    "Yesterday I had read a book.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Yesterday I read a book volstaat: er is geen tweede, later moment om mee te vergelijken.",
            },
            {
                "opties": [
                    "She had never skied before that winter.",
                    "We had left before the rain started.",
                    "He had broken his glasses, so he could not read.",
                    "This morning I had eaten toast.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "This morning I ate toast volstaat: er is geen tweede, later moment om mee te vergelijken.",
            },
        ],
        "Welke zin gebruikt 'will' op de juiste manier?": [
            {
                "opties": [
                    "That box looks heavy. I'll carry it.",
                    "That box looks heavy. I carry it.",
                    "That box looks heavy. I am going to carry it now.",
                    "That box looks heavy. I will to carry it.",
                ],
            },
            {
                "opties": [
                    "The phone is ringing. I'll answer it.",
                    "The phone is ringing. I answer it.",
                    "The phone is ringing. I am going to answer it now.",
                    "The phone is ringing. I will to answer it.",
                ],
            },
            {
                "opties": [
                    "You look cold. I'll close the window.",
                    "You look cold. I close the window.",
                    "You look cold. I am going to close the window now.",
                    "You look cold. I will to close the window.",
                ],
            },
        ],
        "Na 'will' zet je het werkwoord met to ervoor: she will to come.": [
            {
                "vraag": "'He will to help us' is juist Engels.",
                "uitleg": "Het is he will help us. Na will volgt de kale basisvorm.",
            },
            {
                "vraag": "Will krijgt in de derde persoon een s: she wills come.",
                "uitleg": "Will krijgt nooit een s: she will come.",
            },
            {
                "vraag": "'They will to arrive at six' is juist Engels.",
                "uitleg": "Het is they will arrive at six. Na will volgt de kale basisvorm.",
            },
        ],
        "Welke zin past bij een belofte?": [
            {
                "opties": [
                    "I promise I won't be late.",
                    "I promise I don't be late.",
                    "I promise I am not being late.",
                    "I promise I wasn't late.",
                ],
            },
            {
                "opties": [
                    "I promise I won't forget.",
                    "I promise I don't forget.",
                    "I promise I am not forgetting.",
                    "I promise I didn't forget.",
                ],
            },
            {
                "opties": [
                    "I promise I won't say a word.",
                    "I promise I don't say a word.",
                    "I promise I am not saying a word.",
                    "I promise I didn't say a word.",
                ],
            },
        ],
        "Welke zinnen kijken naar de toekomst?": [
            {
                "opties": [
                    "We will find out.",
                    "He is going to study medicine.",
                    "The bus leaves at eight tomorrow.",
                    "She had gone before noon.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij een dienstregeling gebruik je zelfs de present simple. De laatste zin staat in de past perfect.",
            },
            {
                "opties": [
                    "They will call later.",
                    "I am going to buy a bike.",
                    "The shop opens at nine tomorrow.",
                    "We had finished before the bell.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij een openingsuur gebruik je zelfs de present simple. De laatste zin staat in de past perfect.",
            },
            {
                "opties": [
                    "I will think about it.",
                    "She is going to move abroad.",
                    "The film starts at seven tonight.",
                    "He had eaten before we came.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Bij een vast uur gebruik je zelfs de present simple. De laatste zin staat in de past perfect.",
            },
        ],
        "Welke zin over regen en thuisblijven is juist?": [
            {
                "opties": [
                    "If it snows, we will stay at home.",
                    "If it will snow, we will stay at home.",
                    "If it snows, we stay at home tomorrow.",
                    "If it will snow, we stay at home.",
                ],
            },
            {
                "opties": [
                    "If she calls, I will tell her.",
                    "If she will call, I will tell her.",
                    "If she calls, I tell her tomorrow.",
                    "If she will call, I tell her.",
                ],
            },
            {
                "opties": [
                    "If they arrive late, we will start without them.",
                    "If they will arrive late, we will start without them.",
                    "If they arrive late, we start without them tomorrow.",
                    "If they will arrive late, we start without them.",
                ],
            },
        ],
        "Welke zin hoort bij 'Ik had het boek al gelezen voor de film uitkwam.'?": [
            {
                "vraag": "Welke zin hoort bij 'Zij had de brief al geschreven voor hij belde.'?",
                "opties": [
                    "She had already written the letter before he called.",
                    "She has already written the letter before he called.",
                    "She already wrote the letter before he was calling.",
                    "She had already writed the letter before he called.",
                ],
                "uitleg": "Write, wrote, written. Na had komt het voltooid deelwoord.",
            },
            {
                "vraag": "Welke zin hoort bij 'Wij hadden al gegeten voor zij aankwamen.'?",
                "opties": [
                    "We had already eaten before they arrived.",
                    "We have already eaten before they arrived.",
                    "We already ate before they were arriving.",
                    "We had already eated before they arrived.",
                ],
                "uitleg": "Eat, ate, eaten. Na had komt het voltooid deelwoord.",
            },
            {
                "vraag": "Welke zin hoort bij 'Hij had de film al gezien voor het boek uitkwam.'?",
                "opties": [
                    "He had already seen the film before the book came out.",
                    "He has already seen the film before the book came out.",
                    "He already saw the film before the book was coming out.",
                    "He had already saw the film before the book came out.",
                ],
                "uitleg": "See, saw, seen. Na had komt het voltooid deelwoord.",
            },
        ],
        "Welke vraag naar iemands verblijfplaats volgende week is juist?": [
            {
                "vraag": "Welke vraag naar iemands verblijfplaats morgen is juist?",
                "opties": [
                    "Where will you be tomorrow?",
                    "Where you will be tomorrow?",
                    "Where will be you tomorrow?",
                    "Where you be will tomorrow?",
                ],
            },
            {
                "vraag": "Welke vraag naar het uur van aankomst is juist?",
                "opties": [
                    "When will they arrive?",
                    "When they will arrive?",
                    "When will arrive they?",
                    "When they arrive will?",
                ],
            },
            {
                "vraag": "Welke vraag naar iemands plannen voor volgend jaar is juist?",
                "opties": [
                    "What will she do next year?",
                    "What she will do next year?",
                    "What will do she next year?",
                    "What she do will next year?",
                ],
            },
        ],
    },
}
