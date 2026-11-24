"""De toekomst, de modale hulpwerkwoorden en de gerund — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the school rules.\n\n"
    "SCHOOL TRIP TO LONDON – RULES\n"
    "1. You must stay with your group at all times.\n"
    "2. You are not allowed to leave the hotel without a teacher.\n"
    "3. You don't have to bring food; all meals are included.\n"
    "4. You should bring a raincoat, as it might rain.\n"
    "5. Avoid spending all your pocket money on the first day.\n"
    "6. The coach leaves at 6.30 a.m. sharp, so you had better be on time."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Is dit verplicht, verboden, een raad of niet nodig?",
                [
                    ("bij je groep blijven", "Verplicht"),
                    ("zonder leraar het hotel verlaten", "Verboden"),
                    ("eten meebrengen", "Niet nodig"),
                    ("een regenjas meenemen", "Raad"),
                ],
                "Must, not allowed to, don't have to, should.",
                kolommen=["Verplicht", "Verboden", "Raad", "Niet nodig"],
            ),
            keuze(
                "« It might rain » betekent dat regen [[*mogelijk|zeker]] is.",
                "Might is een zwakke mogelijkheid.",
            ),
            keuze(
                "Na « avoid » staat [[*spending|to spend]], omdat avoid een gerund vraagt.",
                "Avoid, enjoy, mind, finish + -ing.",
            ),
            mk(
                "Waarom staat er « leaves » bij de bus, hoewel het over de toekomst gaat?",
                ["Het is een vast uur", "Het is een gewoonte van elke dag", "Het is een fout in de regels", "Het gebeurt nu"],
                0,
                "Bij een vast uurrooster: present simple.",
            ),
        ],
    ),
    tabel(
        "Will of going to?",
        [
            ("Look at that car! It ___ crash!", "is going to"),
            ("— I'm cold. — I ___ close the window.", "will"),
            ("We ___ visit Spain this summer; we've booked the flights.", "are going to"),
        ],
        "Will bij een beslissing op het moment; going to bij een plan of iets dat je ziet aankomen.",
        kolommen=["will", "is going to", "are going to"],
    ),
    sleep(
        "Sorry, I [[can't]] come tonight. I [[have to]] study for my exam. Maybe we [[could]] meet tomorrow?",
        ["mustn't", "should to", "cans"],
        "Can't: niet kunnen; have to: moeten; could: voorstel.",
    ),
    mk(
        "« You mustn't touch the paintings. » Wat betekent dat?",
        ["Het is verboden", "Het hoeft niet", "Het is aangeraden", "Het mag eventueel"],
        0,
        "Mustn't is een verbod; don't have to is niet nodig.",
    ),
    mk(
        "« She can't have stolen it; she was with me all day. » Wat bedoelt de spreker?",
        ["Het is onmogelijk", "Ze heeft het zeker gedaan", "Ze heeft misschien gestolen", "Ze mocht het niet doen"],
        0,
        "Can't have + deelwoord: onmogelijke conclusie over het verleden.",
    ),
    mk(
        "« You should have told me earlier! » Wat bedoelt de spreker?",
        ["Een verwijt", "Een raad voor morgen", "Een belofte", "Een vraag om toestemming"],
        0,
        "Should have + deelwoord: het was beter geweest.",
    ),
    mk(
        "« Would you mind ___ the music down? » Welke vorm past?",
        ["turning", "to turn", "turn", "turned"],
        0,
        "Na mind: gerund.",
    ),
    mk(
        "« I hope ___ you again soon. » Welke vorm past?",
        ["to see", "seeing", "see", "seen"],
        0,
        "Na hope: infinitief met to.",
    ),
    mk(
        "« My parents made me ___ my room. » Welke vorm past?",
        ["tidy", "to tidy", "tidying", "tidied"],
        0,
        "Na make en let: infinitief zonder to.",
    ),
    mk(
        "« I'm looking forward to ___ you. » Welke vorm past?",
        ["meeting", "meet", "met", "be meet"],
        0,
        "To is hier een voorzetsel, dus gerund.",
    ),
    mk(
        "« I'd rather ___ at home tonight. » Welke vorm past?",
        ["stay", "to stay", "staying", "stayed at"],
        0,
        "Would rather + infinitief zonder to.",
    ),
    tabel(
        "Gerund of infinitief met to?",
        [
            ("She finished ___ (write) her essay.", "writing"),
            ("They agreed ___ (help) us.", "to help"),
            ("He suggested ___ (go) by train.", "going"),
            ("We can't afford ___ (buy) a car.", "to buy"),
        ],
        "Finish en suggest + -ing; agree en afford + to.",
        kolommen=["writing", "to help", "going", "to buy"],
    ),
    keuze(
        "« I stopped [[*to buy|buying]] a coffee on my way to work. » De spreker stopte om koffie te kopen.",
        "Stop to: stoppen om; stop -ing: ophouden met.",
    ),
    keuze(
        "« [[*Don't forget|Not forget]] your passport! »",
        "Ontkennende imperatief: don't + werkwoord.",
    ),
    keuze(
        "« By next June, I [[*will have finished|will finish since]] my studies. »",
        "Will have + deelwoord: voltooid in de toekomst.",
    ),
    keuze(
        "« [[*Shall|Will]] we go for a walk? » is een voorstel.",
        "Shall we …? stelt iets voor.",
    ),
    inv(
        "Vul aan: « I won't be ___ to come; I'm working. » (in staat)",
        ["able"],
        "To be able to.",
    ),
    inv(
        "Vul de gerund in: « ___ (eat) too much sugar is bad for your teeth. »",
        ["Eating", "eating"],
        "Een gerund als onderwerp.",
    ),
    inv(
        "Vul aan: « You'd ___ hurry, or you'll miss the train. »",
        ["better"],
        "Had better: sterke raad.",
    ),
    sorteer(
        "Een zekere of een onzekere uitspraak?",
        ["Zeker", "Onzeker"],
        [
            ("It will rain tomorrow.", "Zeker"),
            ("It may rain tomorrow.", "Onzeker"),
            ("It must be raining; everyone has an umbrella.", "Zeker"),
            ("It could rain later.", "Onzeker"),
        ],
        "Will en must (conclusie) zijn sterk; may en could laten ruimte.",
    ),
    koppel(
        "Koppel elke zin aan wat ze uitdrukt.",
        [
            ("Can I borrow your pen?", "toestemming vragen"),
            ("You ought to apologise.", "een raad"),
            ("I can speak three languages.", "een vaardigheid"),
            ("You needn't hurry.", "het is niet nodig"),
        ],
        ["een verbod"],
        "Ought to lijkt sterk op should.",
    ),
    mk(
        "« When I was six, I could already read. » Wat betekent could hier?",
        ["Kon", "Zou kunnen", "Mocht", "Moest"],
        0,
        "Could is de verleden tijd van can: een vaardigheid in het verleden.",
    ),
    mk(
        "Welke zin met can is juist?",
        ["She can swim very well.", "She cans swim very well.", "She can to swim very well.", "She can swims very well."],
        0,
        "Modale werkwoorden krijgen geen s en geen to erna.",
    ),
    keuze(
        "« Students are [[*allowed|allow]] to use a calculator in the exam. »",
        "To be allowed to: mogen.",
    ),
    mk(
        "« He left without ___ a word. » Welke vorm past?",
        ["saying", "to say", "say", "said"],
        0,
        "Na een voorzetsel: gerund.",
    ),
    inv(
        "Vul aan met de verleden vorm van have to: « Last year we ___ to wear a uniform. »",
        ["had"],
        "Must heeft geen verleden tijd: had to.",
    ),
    open_(
        "Leg in het Nederlands het verschil uit tussen « You mustn't go » en « You don't have to go ».",
        "You mustn't go is een verbod: je mag niet gaan. You don't have to go betekent dat het niet nodig is: je moet niet gaan, maar het mag wel.",
    ),
]
