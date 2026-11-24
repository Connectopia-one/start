"""De tegenwoordige tijden en de present perfect — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the e-mail.\n\n"
    "Hi Lucas,\n"
    "Greetings from Dublin! I have been here for three weeks now and I am really enjoying it. "
    "I am staying with a host family near the city centre. Every morning I take the bus to my language school, "
    "which starts at nine. I have already made some good friends, but I haven't visited the famous library yet. "
    "This weekend we are going to the coast. I have never seen cliffs that high!\n"
    "Write soon,\nNora"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Waarom staat er « I have been here for three weeks »?",
                ["Ze is er nog steeds", "Ze is al terug thuis", "Het was een korte trip", "Ze gaat er pas naartoe"],
                0,
                "De present perfect met for: het begon in het verleden en loopt nog.",
            ),
            mk(
                "Wat zegt « Every morning I take the bus »?",
                ["Een gewoonte", "Iets dat nu gebeurt", "Een plan voor later", "Iets van vroeger"],
                0,
                "Every morning: present simple.",
            ),
            tabel(
                "Staat dit in de mail?",
                [
                    ("Nora heeft de bibliotheek al bezocht.", F),
                    ("Nora logeert bij een gastgezin.", J),
                    ("Nora heeft al vrienden gemaakt.", J),
                    ("Nora heeft al eerder zulke hoge kliffen gezien.", F),
                ],
                "Haven't visited … yet; I have never seen.",
            ),
            keuze(
                "« This weekend we are going to the coast » gaat over [[*een afgesproken plan|iets dat nu gebeurt]].",
                "De present continuous kan een vast plan voor de nabije toekomst zijn.",
            ),
        ],
    ),
    tabel(
        "Present simple of present continuous?",
        [
            ("Listen! Somebody ___ (knock) at the door.", "is knocking"),
            ("My dad ___ (cook) dinner on Sundays.", "cooks"),
            ("The sun ___ (rise) in the east.", "rises"),
            ("Be quiet, the baby ___ (sleep).", "is sleeping"),
        ],
        "Nu bezig: continuous; gewoonte of feit: simple.",
        kolommen=["cooks", "rises", "is knocking", "is sleeping"],
    ),
    sleep(
        "She [[doesn't]] like horror films, but she [[does]] like thrillers. [[Does]] your brother like them?",
        ["don't", "do", "is"],
        "Bij he, she, it: does. Emphatic does voor nadruk.",
    ),
    mk(
        "« I ___ what you mean. » Welke vorm past?",
        ["understand", "am understanding", "understands", "am understand"],
        0,
        "Understand staat normaal niet in de continuous vorm.",
    ),
    mk(
        "« The museum ___ at 10 a.m. tomorrow. » Welke vorm past?",
        ["opens", "is opening now", "has opened", "open"],
        0,
        "Een vast uurrooster: present simple.",
    ),
    mk(
        "« ___ there any tickets left for tonight? » Welke vorm past?",
        ["Are", "Is", "Do", "Has"],
        0,
        "Tickets is meervoud: are there.",
    ),
    mk(
        "« My cousin ___ to Australia, so we won't see her this year. » Welke vorm past?",
        ["has gone", "has been", "goes", "is go"],
        0,
        "Has gone: ze is er nog.",
    ),
    mk(
        "« I ___ to Rome three times, and I'd love to go back. » Welke vorm past?",
        ["have been", "have gone", "went yesterday", "am going"],
        0,
        "Have been: geweest en weer terug.",
    ),
    mk(
        "« We ___ for the bus for 40 minutes and it still hasn't come! » Welke vorm past?",
        ["have been waiting", "are waiting since", "waited", "wait"],
        0,
        "Present perfect continuous: het loopt nog en duurt al.",
    ),
    mk(
        "« I ___ my phone last night. » Welke vorm past?",
        ["lost", "have lost", "have been losing", "am losing"],
        0,
        "Last night is een afgesloten tijd: past simple.",
    ),
    tabel(
        "Juist of fout?",
        [
            ("I've known him since we were kids.", J),
            ("She has finished her essay last week.", F),
            ("Have you ever eaten sushi?", J),
            ("I am knowing the answer.", F),
        ],
        "Last week vraagt de past simple; know staat niet in de continuous.",
    ),
    tabel(
        "For of since bij de present perfect?",
        [
            ("He has worked here ___ six months.", "for"),
            ("I haven't eaten ___ breakfast.", "since"),
            ("They have been friends ___ ages.", "for"),
        ],
        "For bij een duur, since bij een beginpunt.",
        kolommen=["for", "since"],
    ),
    keuze(
        "« I've [[*just|yet]] finished; the paint is still wet. »",
        "Just: net.",
    ),
    keuze(
        "« Have you finished your homework [[*yet|already]]? » vraagt de moeder.",
        "Yet in een vraag of ontkenning, achteraan.",
    ),
    keuze(
        "« It's the best book I've [[*ever|never]] read. »",
        "Ever na een overtreffende trap.",
    ),
    keuze(
        "« She [[*studies|studys]] law at university. »",
        "Consonant + y wordt -ies.",
    ),
    inv(
        "Vul het voltooid deelwoord in van « to write »: « Have you ___ to your grandmother? »",
        ["written"],
        "Write, wrote, written.",
    ),
    inv(
        "Vul het voltooid deelwoord in van « to buy »: « We have ___ a new car. »",
        ["bought"],
        "Buy, bought, bought.",
    ),
    inv(
        "Vul aan: « How long ___ she been living in Ghent? »",
        ["has"],
        "How long has she been living …?",
    ),
    koppel(
        "Koppel de zin aan wat ze uitdrukt.",
        [
            ("I've lived here all my life.", "het begon vroeger en loopt nog"),
            ("I live here.", "een feit of gewoonte"),
            ("I'm living with friends this month.", "een tijdelijke situatie"),
            ("I've just moved in.", "het is net gebeurd"),
        ],
        ["iets afgesloten in het verleden"],
        "Elke tijd heeft een eigen betekenis.",
    ),
    sorteer(
        "Present perfect of past simple?",
        ["Present perfect", "Past simple"],
        [
            ("since 2010", "Present perfect"),
            ("two days ago", "Past simple"),
            ("already", "Present perfect"),
            ("in 1999", "Past simple"),
            ("ever", "Present perfect"),
        ],
        "Een afgesloten tijdstip vraagt de past simple.",
    ),
    mk(
        "Wat is het verschil tussen « I've painted the room » en « I've been painting the room »?",
        ["Het eerste is klaar", "Er is geen verschil tussen beide", "Het tweede is al lang geleden", "Het eerste is nog bezig"],
        0,
        "De continuous vorm legt de nadruk op de bezigheid, die nog niet af hoeft te zijn.",
    ),
    mk(
        "« This is the first time I ___ a horse. » Welke vorm past?",
        ["have ridden", "ride", "am riding", "was riding on"],
        0,
        "Na this is the first time: present perfect.",
    ),
    keuze(
        "« I [[*do|am]] want to come, but I can't! » De spreker legt nadruk op willen.",
        "Emphatic do versterkt het werkwoord.",
    ),
    mk(
        "« He ___ three goals so far this season. » Welke vorm past?",
        ["has scored", "scored last", "scores now", "is scoring"],
        0,
        "So far: tot nu toe, de periode loopt nog.",
    ),
    volgorde(
        "Zet de woorden in de juiste volgorde: « (has / already / she / left) ».",
        ["She", "has", "already", "left"],
        "Already staat tussen have en het deelwoord.",
    ),
    open_(
        "Leg in het Nederlands uit waarom « I have seen him yesterday » fout is en verbeter de zin.",
        "Yesterday is een afgesloten tijdstip in het verleden. Daarbij gebruik je de past simple en niet de present perfect. Juist is: I saw him yesterday.",
    ),
]
