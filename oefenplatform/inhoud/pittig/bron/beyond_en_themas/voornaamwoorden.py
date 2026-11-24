"""Voornaamwoorden en betrekkelijke bijzinnen — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text.\n\n"
    "(1) Mia and her grandfather, who used to be a carpenter, built a treehouse last summer. "
    "(2) They did all the work themselves. "
    "(3) The wood, which they found in an old barn, was free. "
    "(4) Mia's brother Leo wanted to help, but she told him it was her project. "
    "(5) Now the treehouse is the place where all the children of the street meet. "
    "(6) Leo admits that it is better than his."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Naar wie verwijst « who » in zin 1?",
                ["De grootvader", "Mia", "Mia en haar grootvader", "Leo"],
                0,
                "Who used to be a carpenter staat meteen na her grandfather.",
            ),
            mk(
                "Naar wat verwijst « his » in zin 6?",
                ["Naar Leo's boomhut", "Naar de grootvader", "Naar het hout", "Naar de straat"],
                0,
                "His staat voor his treehouse, de boomhut van Leo.",
            ),
            keuze(
                "In zin 3 staat which tussen komma's omdat de bijzin [[*extra uitleg geeft|nodig is om te weten welk hout]].",
                "Een uitbreidende bijzin tussen komma's: which of who, nooit that.",
            ),
            keuze(
                "« Themselves » in zin 2 betekent dat ze het [[*zonder hulp|samen met anderen]] deden.",
                "Themselves versterkt: zij en niemand anders.",
            ),
            inv(
                "Welk betrekkelijk woord in zin 5 verwijst naar een plaats?",
                ["where"],
                "The place where.",
            ),
        ],
    ),
    tabel(
        "Welk voornaamwoord past?",
        [
            ("Our teacher gave ___ a lot of homework. (wij)", "us"),
            ("___ and I went to the cinema. (hij)", "He"),
            ("The prize is ___. (van haar)", "hers"),
        ],
        "Onderwerp: he; voorwerp: us; alleenstaand bezit: hers.",
        kolommen=["us", "He", "hers"],
    ),
    tabel(
        "Who, which of whose?",
        [
            ("The girl ___ phone was stolen called the police.", "whose"),
            ("The film, ___ lasted three hours, was boring.", "which"),
            ("The nurse ___ helped me was very kind.", "who"),
        ],
        "Whose voor bezit, who voor personen, which voor dingen.",
        kolommen=["who", "which", "whose"],
    ),
    sleep(
        "Did you cut [[yourself]]? Be careful, that knife is sharp. We really enjoyed [[ourselves]] at the beach. The cat cleaned [[itself]].",
        ["yourselves", "itsself"],
        "Wederkerend als onderwerp en voorwerp dezelfde zijn.",
    ),
    mk(
        "Welke zin is juist geschreven?",
        ["They're late because their train left from there.", "Their late because there train left from they're.", "There late because they're train left from their.", "They're late because there train left from their."],
        0,
        "They're = they are, their = hun, there = daar.",
    ),
    mk(
        "« Everyone ___ to bring a pen. » Welke vorm past?",
        ["needs", "need", "are needing", "have need"],
        0,
        "Everyone is enkelvoud.",
    ),
    mk(
        "« ___ is that red car? It's my uncle's. » Welk vraagwoord past?",
        ["Whose", "Who's", "Which", "Whom"],
        0,
        "Whose vraagt naar de bezitter.",
    ),
    mk(
        "« ___ coming to the party tonight? » Welke vorm past?",
        ["Who's", "Whose", "Whom", "Which"],
        0,
        "Who's = who is.",
    ),
    mk(
        "In welke zin mag je het betrekkelijke woord weglaten?",
        ["The song that she sang was beautiful.", "The woman who called me last night is my aunt.", "My bike, which is old, broke.", "The man who lives here is ill."],
        0,
        "Weglaten mag als het niet het onderwerp van de bijzin is.",
    ),
    mk(
        "« My sister who lives in Ghent is a nurse. » Wat volgt uit deze zin zonder komma's?",
        ["Ik heb meerdere zussen", "Ik heb maar één zus", "Mijn zus woont niet in Gent", "Mijn zus is geen verpleegster"],
        0,
        "Zonder komma's beperkt de bijzin: de zus die in Gent woont, niet de andere.",
    ),
    keuze(
        "« If anyone calls, tell [[*them|it]] I'm out. » Je gebruikt they voor één persoon van wie je het geslacht niet zegt.",
        "Them als voorwerpsvorm van they.",
    ),
    keuze(
        "« Between you and [[*me|I]], the test was too hard. »",
        "Na een voorzetsel: de voorwerpsvorm.",
    ),
    keuze(
        "« I prefer [[*these|this]] shoes to those. »",
        "Meervoud dichtbij: these.",
    ),
    keuze(
        "« Nobody [[*knows|know]] the answer. »",
        "Nobody is enkelvoud.",
    ),
    inv(
        "Vul aan met één woord: « I'll never forget the day ___ we first met. »",
        ["when", "that"],
        "When bij een tijdstip.",
    ),
    inv(
        "Vul aan met één woord: « Nobody knows the reason ___ she quit her job. »",
        ["why", "that"],
        "The reason why.",
    ),
    inv(
        "Vul aan met één woord: « The colleague with ___ I share an office is on holiday. »",
        ["whom"],
        "Na een voorzetsel: whom.",
    ),
    inv(
        "Vul aan met één woord: « She told me ___ she had seen. » (wat)",
        ["what"],
        "What betekent hier datgene wat.",
    ),
    tabel(
        "Is deze zin juist?",
        [
            ("The book which I lent you is mine.", J),
            ("My father, that is a pilot, travels a lot.", F),
            ("This is the hotel where we stayed.", J),
            ("The students who passed was happy.", F),
        ],
        "Tussen komma's nooit that; students is meervoud.",
    ),
    sorteer(
        "Persoon of ding?",
        ["Persoon", "Ding"],
        [
            ("who", "Persoon"),
            ("which", "Ding"),
            ("whom", "Persoon"),
            ("somebody", "Persoon"),
            ("something", "Ding"),
        ],
        "Who en whom bij personen, which bij dingen.",
    ),
    koppel(
        "Koppel de onderwerpsvorm aan de bezittelijke vorm die alleen staat.",
        [
            ("I", "mine"),
            ("you", "yours"),
            ("we", "ours"),
            ("they", "theirs"),
        ],
        ["its"],
        "Its staat vrijwel nooit alleen.",
    ),
    mk(
        "« The cat hurt ___ paw. » Welke vorm past?",
        ["its", "it's", "its'", "it"],
        0,
        "Its zonder apostrof is bezittelijk.",
    ),
    mk(
        "« Somebody has left ___ umbrella here. » Welke vorm past het best?",
        ["their", "there", "they're", "theirs"],
        0,
        "Their kan ook naar één persoon verwijzen van wie je het geslacht niet kent.",
    ),
    keuze(
        "« Help [[*yourselves|yourself]] to some cake, children! »",
        "Tegen meerdere personen: yourselves.",
    ),
    sleep(
        "That's the boy [[whose]] father is a pilot. He lives in the house [[where]] I was born. The pilot, [[who]] is very nice, gave us a tour.",
        ["which", "what"],
        "Whose voor bezit, where voor plaats, who voor personen.",
    ),
    open_(
        "Leg in het Nederlands het verschil uit tussen « The students, who were tired, went home » en « The students who were tired went home ».",
        "Met komma's gingen alle studenten naar huis, en de bijzin zegt dat ze moe waren. Zonder komma's gingen alleen de studenten die moe waren naar huis; de anderen bleven.",
    ),
]
