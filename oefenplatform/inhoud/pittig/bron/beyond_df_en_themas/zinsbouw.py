"""Zinsbouw, zinsdelen en de voorwaardelijke bijzin — pittig (Engels, Beyond dubbele finaliteit), A2+. Enkel zero en first conditional."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the advice from a school nurse.\n\nIf you don't sleep enough, you can't concentrate in class. "
        "Teenagers need about nine hours of sleep, but many of them only get seven. Put your phone away an hour before bed, "
        "because the blue light keeps you awake. If you go to bed at the same time every night, you will fall asleep more easily. "
        "Don't drink cola in the evening! Although it is hard, try it for a week.",
        [
            tabel("Welk soort zin is dit?", [
                ("Put your phone away an hour before bed.", "bevelend"),
                ("Teenagers need about nine hours of sleep.", "bevestigend"),
                ("Don't drink cola in the evening!", "bevelend"),
            ], "Een bevel heeft geen onderwerp.", kolommen=["bevestigend", "bevelend"]),
            keuze("« If you go to bed at the same time every night, you will fall asleep more easily » is een [[*first conditional|zero conditional]].",
                  "Present simple na if, will in de hoofdzin."),
            keuze("Het voegwoord « because » geeft een [[*reden|tegenstelling|gevolg]].", "Because: omdat."),
            keuze("« Although it is hard » betekent [[*hoewel het moeilijk is|omdat het moeilijk is|als het moeilijk is]].",
                  "Although kondigt een tegenstelling aan."),
            inv("Hoeveel uur slaap hebben tieners volgens de tekst nodig? Schrijf het getal.", ["9", "nine", "negen"],
                "About nine hours."),
        ],
    ),
    tabel("Zero of first conditional?", [
        ("If you mix red and blue, you get purple.", "zero"),
        ("If you study, you will pass.", "first"),
        ("If water reaches 0 °C, it freezes.", "zero"),
        ("If it snows, we will build a snowman.", "first"),
    ], "Zero: altijd waar, twee keer present. First: een mogelijk gevolg met will.",
       kolommen=["zero", "first"]),
    mk("« If you ___ late again, the teacher will be angry. » Welke vorm past?",
       ["are", "will be", "would be", "were being"], 0, "Na if de present simple."),
    mk("« We will go to the beach ___ it rains. » We gaan, behalve als het regent. Welk voegwoord past?",
       ["unless", "if", "because", "so"], 0, "Unless betekent tenzij."),
    mk("Wat is het lijdend voorwerp in « The teacher gave the pupils a difficult test »?",
       ["a difficult test", "the pupils", "the teacher gave", "gave the pupils"], 0,
       "Wat geeft de leraar? Een moeilijke toets. Aan wie? De leerlingen: het meewerkend voorwerp."),
    mk("Welke zin heeft de juiste Engelse woordorde?",
       ["I visited my aunt last weekend.", "I visited last weekend my aunt.",
        "Last weekend visited I my aunt.", "I my aunt visited last weekend."], 0,
       "Onderwerp, werkwoord, lijdend voorwerp, daarna de tijd."),
    keuze("« Everybody [[*knows|know]] the answer. »", "Everybody is enkelvoud."),
    keuze("« My parents [[*work|works]] in a hospital. »", "Parents is meervoud."),
    keuze("« I didn't see [[*anybody|nobody]] in the park. »", "Geen dubbele ontkenning in het Engels."),
    keuze("« She was tired, [[*so|because]] she went to bed early. »", "So kondigt het gevolg aan."),
    keuze("« He went to work [[*although|because]] he felt ill. »", "Een tegenstelling: hoewel."),
    inv("Vul één voegwoord in: « You can borrow my bike ___ you bring it back tonight. » (als)", ["if"], "If voor een voorwaarde."),
    inv("Vul één voegwoord in: « I stayed at home ___ I was ill. » (omdat)", ["because"], "Because voor een reden."),
    inv("Wat is de persoonsvorm in « My best friend has moved to Ghent »?", ["has"], "Has is het vervoegde werkwoord."),
    koppel("Koppel elk voegwoord aan zijn betekenis.", [
        ["but", "maar"], ["while", "terwijl"], ["although", "hoewel"], ["unless", "tenzij"],
    ], ["omdat"], "Omdat is because."),
    sorteer("Nevenschikkend of onderschikkend voegwoord?", ["nevenschikkend", "onderschikkend"], [
        ["and", "nevenschikkend"], ["because", "onderschikkend"], ["or", "nevenschikkend"],
        ["if", "onderschikkend"], ["but", "nevenschikkend"], ["when", "onderschikkend"],
    ], "Onderschikkend begint een bijzin."),
    volgorde("Zet de zinsdelen in de juiste Engelse volgorde.", [
        "My sister", "bought", "a new phone", "yesterday",
    ], "Onderwerp, werkwoord, lijdend voorwerp, tijd."),
    tabel("Is deze zin juist?", [
        ("If it will rain, we will stay inside.", F),
        ("The news is very good today.", J),
        ("I don't know nothing about it.", F),
        ("Unless you hurry, you will miss the bus.", J),
    ], "Na if geen will; geen dubbele ontkenning."),
    mk("« What a beautiful garden! » Wat voor zin is dit?",
       ["een uitroepende zin", "een vragende zin", "een bevelende zin", "een ontkennende zin"], 0,
       "What a ...! drukt verwondering uit."),
    sleep("If you [[heat]] ice, it [[melts]]. If you [[leave]] the ice cream in the sun, it [[will melt]].",
          ["will heat", "melted"], "Een zero conditional en daarna een first conditional."),
    tabel("Bevestigend, ontkennend of vragend?", [
        ("Does he speak French?", "vragend"),
        ("They haven't arrived.", "ontkennend"),
        ("The shop opens at nine.", "bevestigend"),
    ], "Kijk naar not en naar de plaats van het hulpwerkwoord.",
       kolommen=["bevestigend", "ontkennend", "vragend"]),
    mk("Wat is het meewerkend voorwerp in « Can you send me the photos? »?",
       ["me", "the photos", "you", "send"], 0, "Aan wie stuur je de foto's? Aan mij."),
    keuze("In « Tomorrow I will call you » staat het bijwoord van tijd [[*vooraan|achteraan]]; dat mag ook in het Engels.",
          "Een bijwoord van tijd kan vooraan of achteraan staan."),
    inv("Vul de juiste vorm in van « to be »: « If the weather ___ bad, the trip will be cancelled. » Eén woord.", ["is"],
        "Na if de present simple."),
    keuze("« You can stay up late [[*as long as|unless]] you are quiet. » Je mag, op voorwaarde dat je stil bent.", "As long as: zolang, op voorwaarde dat."),
    open_("Leg in het Nederlands uit waarom « If I will see him, I will tell him » fout is, en verbeter de zin.",
          "Na if gebruik je in een first conditional de present simple, niet will. Juist is: « If I see him, I will tell him. »"),
]
