"""De verleden tijden — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the story.\n\n"
    "(1) It was a stormy night in November. (2) Anna was reading in bed when the lights suddenly went out. "
    "(3) She got up and looked out of the window. (4) A tree had fallen onto the power line. "
    "(5) While she was looking for a torch, somebody knocked on the door. (6) It was her neighbour, who had brought candles. "
    "(7) When I was young, my grandmother used to tell me this story every winter."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Wat gebeurde er eerst?",
                ["De boom viel om", "Anna keek uit het raam", "Het licht ging plots uit", "Iemand klopte op de deur"],
                0,
                "Had fallen (past perfect) is nog vroeger dan de andere gebeurtenissen.",
            ),
            keuze(
                "« Anna was reading » in zin 2 beschrijft [[*wat bezig was toen iets anders gebeurde|een gewoonte van Anna]].",
                "Past continuous plus when plus past simple.",
            ),
            keuze(
                "De buurvrouw had de kaarsen meegebracht [[*voor ze aanklopte|nadat ze aanklopte]].",
                "Had brought: nog vroeger.",
            ),
            mk(
                "Wat zegt « used to tell » in zin 7?",
                ["Vroeger een gewoonte", "Ze vertelt het nog altijd", "Ze vertelde het maar één keer", "Ze was gewoon vermoeid"],
                0,
                "Used to: vroeger regelmatig, nu niet meer.",
            ),
            tabel(
                "Welke tijd staat in deze zin?",
                [
                    ("zin 3: She got up …", "Past simple"),
                    ("zin 4: A tree had fallen …", "Past perfect"),
                    ("zin 5: While she was looking …", "Past continuous"),
                ],
                "Simple: afgerond; continuous: bezig; perfect: nog vroeger.",
                kolommen=["Past simple", "Past continuous", "Past perfect"],
            ),
        ],
    ),
    sleep(
        "Last year we [[flew]] to Canada. We [[saw]] bears and [[took]] hundreds of photos.",
        ["flied", "seed", "taked"],
        "Fly, flew; see, saw; take, took.",
    ),
    tabel(
        "Is deze verleden tijd juist?",
        [
            ("I thought", J),
            ("she teached", F),
            ("we planned", J),
            ("they catched", F),
            ("he fell", J),
        ],
        "Teach wordt taught, catch wordt caught.",
    ),
    mk(
        "« ___ you go to the concert on Saturday? » Welke vorm past?",
        ["Did", "Were", "Have", "Do"],
        0,
        "Vraag in de past simple: did + hele werkwoord.",
    ),
    mk(
        "« We didn't ___ the answer. » Welke vorm past?",
        ["know", "knew", "known", "knowed"],
        0,
        "Na didn't: het hele werkwoord.",
    ),
    mk(
        "« My parents ___ in Antwerp in 1990. » Welke vorm past?",
        ["got married", "have got married", "are married", "had got married since"],
        0,
        "In 1990: afgesloten tijd, past simple.",
    ),
    mk(
        "« When the teacher came in, the pupils ___. » Wat betekent « were talking »?",
        ["Ze waren al aan het praten", "Ze begonnen pas te praten", "Ze praatten nooit", "Ze hadden al gepraat en zwegen"],
        0,
        "De past continuous: het was al bezig.",
    ),
    mk(
        "« When the teacher came in, the pupils stopped talking. » Wat gebeurde er?",
        ["Ze zwegen toen", "Ze waren al stil", "Ze begonnen te praten", "Ze praatten verder"],
        0,
        "Twee opeenvolgende handelingen in de past simple.",
    ),
    mk(
        "« By the time the firemen arrived, the house ___ down. » Welke vorm past?",
        ["had burnt", "burns", "has burnt", "was burn"],
        0,
        "By the time: past perfect.",
    ),
    mk(
        "« I ___ in Spain for two years before I moved to Belgium. » Welke vorm past?",
        ["had lived", "have lived", "live", "am living"],
        0,
        "Vóór een ander moment in het verleden: past perfect.",
    ),
    keuze(
        "« I [[*used to|use to]] play the violin, but I gave up. »",
        "Used to in een bevestigende zin.",
    ),
    keuze(
        "« Did you [[*use to|used to]] live here? »",
        "Na did: use to, zonder d.",
    ),
    keuze(
        "« He [[*was|were]] working late when the alarm went off. »",
        "Bij he: was.",
    ),
    keuze(
        "« She [[*stopped|stoped]] the car at the red light. »",
        "Eén klinker plus één medeklinker: verdubbelen.",
    ),
    inv(
        "Vul de past simple in van « to begin »: « The lesson ___ at nine. »",
        ["began"],
        "Begin, began, begun.",
    ),
    inv(
        "Vul de past simple in van « to choose »: « She ___ the blue dress. »",
        ["chose"],
        "Choose, chose, chosen.",
    ),
    inv(
        "Vul het voltooid deelwoord in: « They had never ___ (to fly) before. »",
        ["flown"],
        "Fly, flew, flown.",
    ),
    koppel(
        "Koppel elk werkwoord aan zijn verleden tijd.",
        [
            ("to bring", "brought"),
            ("to think", "thought"),
            ("to feel", "felt"),
            ("to leave", "left"),
        ],
        ["leaved"],
        "Allemaal onregelmatig.",
    ),
    sorteer(
        "Regelmatig of onregelmatig?",
        ["Regelmatig", "Onregelmatig"],
        [
            ("to arrive", "Regelmatig"),
            ("to spend", "Onregelmatig"),
            ("to try", "Regelmatig"),
            ("to forget", "Onregelmatig"),
            ("to carry", "Regelmatig"),
        ],
        "Spent en forgot zijn onregelmatig; tried en carried krijgen -ied.",
    ),
    tabel(
        "Is deze zin juist (over de verleden tijden)?",
        [
            ("I was born in 2010.", J),
            ("I am born in 2010.", F),
            ("While I was cooking, he set the table.", J),
            ("We didn't saw anything.", F),
        ],
        "To be born staat in het verleden; na didn't het hele werkwoord.",
    ),
    mk(
        "« She was always borrowing my clothes! » Wat klinkt er in deze zin door?",
        ["Ergernis", "Bewondering", "Dankbaarheid", "Verdriet"],
        0,
        "Always met de continuous vorm drukt vaak ergernis uit.",
    ),
    mk(
        "« What were you doing at 10 p.m. last night? » Wat wil de vraagsteller weten?",
        ["Waarmee je toen bezig was", "Wat je de hele dag deed", "Waarom je laat thuiskwam", "Wat je morgen gaat doen"],
        0,
        "Past continuous: bezig op een moment in het verleden.",
    ),
    keuze(
        "« He told me he [[*had lost|has lost]] his wallet. »",
        "In indirecte rede schuift de tijd een stap terug.",
    ),
    inv(
        "Vul de past simple in van « to spend »: « We ___ too much money on holiday. »",
        ["spent"],
        "Spend, spent, spent.",
    ),
    volgorde(
        "Zet de gebeurtenissen in de volgorde waarin ze echt gebeurden: « When I got to the station, the train had left, so I took a taxi. »",
        ["de trein vertrok", "ik kwam aan in het station", "ik nam een taxi"],
        "Had left is nog vroeger dan got to.",
    ),
    open_(
        "Leg in het Nederlands het verschil uit tussen « When I arrived, they ate » en « When I arrived, they had eaten ».",
        "In de eerste zin begonnen ze te eten toen ik aankwam. In de tweede zin was het eten al voorbij toen ik aankwam: de past perfect zegt dat het nog vroeger gebeurde.",
    ),
]
