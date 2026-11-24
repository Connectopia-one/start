"""Tekstsoorten, tekstverbanden en verwijswoorden — pittig (🚀 Boost, Engels).

Eigen vragen op echte Engelse zinnen en tekstjes. Dezelfde vragen voor
doorstroom en dubbele finaliteit."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

T1 = (
    "Read the text.\n\n"
    "(1) Every year, millions of plastic bottles end up in the sea. "
    "(2) They break into tiny pieces, which fish and birds eat. "
    "(3) As a result, many animals become ill. "
    "(4) For example, a dead whale on a Scottish beach had 100 kilos of plastic in its stomach. "
    "(5) So, the next time you buy a drink, take your own bottle. "
    "(6) It is cheaper, and it helps the animals too."
)

VRAGEN = [
    casus(T1, [
        mk("Welke tekstsoort is dit vooral?",
           ["een betogende tekst", "een verhalende tekst", "een beschrijvende tekst", "een prescriptieve tekst"], 0,
           "De schrijver wil je overtuigen om je eigen fles mee te nemen."),
        koppel("Welk verband leggen de signaalwoorden in deze tekst?",
               [("As a result (zin 3)", "gevolg"), ("For example (zin 4)", "voorbeeld"), ("So (zin 5)", "conclusie")],
               ["tegenstelling"], "Signaalwoorden tonen hoe zinnen samenhangen."),
        inv("Naar welk woord verwijst They in zin 2? Schrijf het Engelse woord.", ["bottles", "plastic bottles", "the bottles"],
            "They verwijst naar de plastic bottles uit zin 1."),
        inv("Naar welk woord verwijst its in zin 4?", ["whale", "a dead whale", "the whale", "dead whale"],
            "Its stomach: de maag van de walvis."),
        tabel("Klopt dit over de opbouw?",
              [("Zin 1 tot 3 tonen een probleem en zijn gevolg.", J), ("Zin 4 geeft een voorbeeld.", J), ("Zin 5 en 6 geven een oplossing.", J), ("De tekst eindigt met een vraag.", F)],
              "Probleem, gevolg, voorbeeld, oplossing."),
    ]),
    sorteer("Welke tekstsoort is dit?", ["informatief", "prescriptief", "narratief", "argumentatief"],
            [("a recipe for pancakes", "prescriptief"), ("a news report about a fire", "informatief"), ("a short story about a lost dog", "narratief"), ("a letter asking the mayor to build a skatepark", "argumentatief"), ("the rules of a board game", "prescriptief"), ("a fairy tale", "narratief")],
            "Prescriptief: zegt wat je moet doen; narratief: vertelt; argumentatief: overtuigt; informatief: informeert."),
    koppel("Welk signaalwoord hoort bij welk verband?",
           [("however", "tegenstelling"), ("because", "oorzaak"), ("therefore", "gevolg"), ("first", "opsomming of volgorde"), ("for instance", "voorbeeld")],
           ["vergelijking"], "Signaalwoorden helpen je de opbouw te volgen."),
    keuze("'I love summer. [[*However|Because|For example]], I hate the heat.'",
          "De tweede zin zegt iets tegengestelds."),
    keuze("'The roads were icy. [[*Therefore|Although|Then]], the school bus was late.'",
          "Het gladde wegdek is de oorzaak, de vertraging het gevolg."),
    keuze("'We went to the beach [[*because|but|so]] it was a sunny day.'",
          "Het mooie weer is de reden."),
    tabel("Naar wie of wat verwijst het vetgedrukte woord? 'Tom gave his sister a book. She loved it.'",
          [("She", "the sister"), ("it", "the book"), ("his", "Tom")],
          "Volg de verwijswoorden terug naar de vorige zin.", ["the sister", "the book", "Tom"]),
    volgorde("Zet de zinnen van dit verhaaltje in de juiste volgorde.",
             ["First, Emma woke up late.", "Then she missed the bus.", "After that, she ran to school.", "Finally, she arrived just in time."],
             "First, then, after that, finally: signaalwoorden van tijd."),
    mk("'Mix the flour and the eggs. Add some milk. Bake for 20 minutes.' Welke tekstsoort is dit?",
       ["prescriptief", "narratief", "argumentatief", "beschrijvend"], 0,
       "Een recept zegt stap voor stap wat je moet doen."),
    tabel("Lees: 'Smartphones are useful. On the other hand, they can be addictive.' Klopt dit?",
          [("De tweede zin geeft een tegenstelling.", J), ("On the other hand betekent 'daarnaast nog'.", F), ("De schrijver weegt voor- en nadelen af.", J)],
          "On the other hand = anderzijds."),
    sleep("In een betoog geeft de schrijver zijn [[mening]] en ondersteunt hij die met [[argumenten]]. Aan het einde volgt vaak een [[conclusie]].",
          ["recept", "dialoog"], "De opbouw van een argumentatieve tekst."),
    casus("Read the text.\n\n(1) My grandfather grew up on a small farm in Ireland. (2) He had six brothers, and they all had to help with the cows. (3) In 1965, he moved to London to work in a factory. (4) There, he met my grandmother. (5) They still tell this story every Christmas.", [
        mk("Tot welke tekstsoort hoort dit levensverhaal?",
           ["een verhalende tekst", "een betogende tekst", "een prescriptieve tekst", "een reclametekst"], 0,
           "De tekst vertelt een levensverhaal in de verleden tijd."),
        inv("Naar welke plaats verwijst There in zin 4?", ["London", "london", "in London"],
            "There verwijst naar London in zin 3."),
        inv("Naar wie verwijst They in zin 5? Schrijf het in het Engels, twee woorden met and.", ["my grandfather and my grandmother", "grandfather and grandmother", "my grandparents", "grandparents"],
            "They = de grootvader en de grootmoeder."),
    ]),
    sorteer("Welk signaalwoord drukt een tegenstelling uit en welk een gevolg?", ["tegenstelling", "gevolg"],
            [("but", "tegenstelling"), ("so", "gevolg"), ("although", "tegenstelling"), ("as a result", "gevolg"), ("however", "tegenstelling")],
            "Tegenstelling: but, although, however; gevolg: so, as a result, therefore."),
    mk("Een tekst begint met: 'Did you know that cats sleep for 16 hours a day?' Waarom begint de schrijver zo?",
       ["om je te boeien", "om je een bevel te geven", "om een recept uit te leggen", "om een gedicht te beginnen"], 0,
       "Een vraag of een verrassend feit trekt de aandacht."),
    tabel("Lees: 'Ben and Sam play football. He is the goalkeeper.' Wat is het probleem?",
          [("Je weet niet naar wie He verwijst.", J), ("Met 'Sam is the goalkeeper' is het duidelijk.", J), ("He verwijst altijd naar de eerste naam.", F)],
          "Een verwijswoord moet duidelijk naar één persoon wijzen."),
    keuze("'Firstly, it is cheap. [[*Secondly|Finally|However]], it is good for the environment.'",
          "Een opsomming van argumenten."),
    mk("Welke tekstsoort is een weerbericht?",
       ["informatief", "narratief", "argumentatief", "prescriptief"], 0,
       "Het geeft informatie over het weer."),
    tabel("Lees: 'In conclusion, school uniforms should be allowed.' Klopt dit?",
          [("Dit staat waarschijnlijk aan het einde van de tekst.", J), ("Het is een mening.", J), ("Het is het eerste argument.", F)],
          "In conclusion kondigt het besluit aan."),
    casus("Read the text.\n\n(1) Should pupils have homework at the weekend? (2) Some teachers say yes, because it helps pupils remember what they learnt. (3) However, many parents disagree. (4) They want their children to have time for sport and family. (5) In my opinion, a little homework is fine, but not more than one hour.", [
        mk("Wat doet zin 3 ten opzichte van zin 2?",
           ["Ze geeft een tegengestelde mening.", "Ze geeft een voorbeeld bij zin 2.", "Ze herhaalt zin 2 in andere woorden.", "Ze geeft het gevolg van zin 2."], 0,
           "However kondigt de andere kant aan."),
        inv("Naar wie verwijst They in zin 4? Schrijf het Engelse woord.", ["parents", "many parents", "the parents"],
            "They verwijst naar many parents in zin 3."),
        tabel("Klopt dit over de tekst?",
              [("De schrijver geeft zijn eigen mening in zin 5.", J), ("De tekst begint met een vraag.", J), ("De schrijver wil helemaal geen huiswerk.", F)],
              "In my opinion: een beetje huiswerk mag."),
        keuze("Deze tekst is vooral [[*argumentatief|narratief|prescriptief]].",
              "Hij weegt meningen af en geeft een eigen standpunt."),
    ]),
    keuze("'She was hungry, [[*so|but|because]] she made a sandwich.'",
          "Honger is de oorzaak, de sandwich het gevolg."),
    tabel("'My brother has a dog. My brother walks the dog every day. My brother's dog is old.' Welk verwijswoord vervangt het herhaalde deel?",
          [("My brother (tweede keer)", "He"), ("the dog (tweede keer)", "it"), ("My brother's (derde zin)", "His")],
          "Verwijswoorden voorkomen herhaling.", ["He", "it", "His"]),
]
