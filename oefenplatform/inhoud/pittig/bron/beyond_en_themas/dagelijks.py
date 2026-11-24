"""Woordvelden: wonen, eten en vrije tijd — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the advert.\n\n"
    "ROOM TO LET – Leeds city centre\n"
    "Large, fully furnished room in a semi-detached house, within walking distance of the university. "
    "You will share the kitchen and bathroom with two friendly flatmates. Rent: £450 a month, bills included, "
    "due on the first of the month. Chores are shared on a weekly rota. No smokers, no pets. "
    "The landlord lives next door and fixes problems quickly. Available from 1 September for at least six months."
)

TEKST2 = (
    "Read the message.\n\n"
    "Hi Jess! Fancy coming round on Saturday? The match was called off, so I'm free. "
    "I thought we could get a takeaway – there's a great Indian place down the road – "
    "and watch a film. Don't worry about dessert, Mum made a huge chocolate cake (you know I've got a sweet tooth!). "
    "Oh, and could you bring your speakers? Mine are broken. Let me know! Ben"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat dit in de advertentie (over wonen en vrije tijd)?",
                [
                    ("De kamer heeft al meubels.", J),
                    ("Elektriciteit en water betaal je apart.", F),
                    ("Je deelt de keuken met twee anderen.", J),
                    ("Je mag een kat meebrengen.", F),
                ],
                "Fully furnished, bills included, two flatmates, no pets.",
            ),
            mk(
                "Wat betekent « Chores are shared on a weekly rota »?",
                ["De klusjes gaan per week om beurt", "De huur wordt per week betaald", "De keuken is per week van een ander", "Er wordt wekelijks gepoetst door een firma"],
                0,
                "Chores zijn huishoudelijke klusjes; a rota is een beurtrol.",
            ),
            inv(
                "Hoeveel maanden moet je minstens blijven? Schrijf het getal.",
                ["6", "zes"],
                "For at least six months.",
            ),
            keuze(
                "De verhuurder woont [[*naast de deur|in hetzelfde huis]].",
                "Next door is het huis ernaast.",
            ),
            mk(
                "Wie is « the landlord » in deze advertentie?",
                ["De verhuurder", "Een van de huisgenoten", "De huurder", "De buurman van de universiteit"],
                0,
                "The landlord verhuurt; the tenant huurt.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Waarom is Ben zaterdag vrij?",
                ["De match is afgelast", "Hij heeft die dag vakantie", "Hij is al een week ziek thuis", "Zijn ploeg heeft al gewonnen"],
                0,
                "To call off is afgelasten.",
            ),
            mk(
                "Wat stelt Ben voor om te eten?",
                ["Indiaas afhaaleten", "Samen zelf koken bij hem thuis", "Uit eten gaan in een restaurant", "Alleen de taart van zijn mama"],
                0,
                "A takeaway is eten dat je afhaalt.",
            ),
            keuze(
                "Ben eet [[*graag zoet|liever hartig]].",
                "I've got a sweet tooth.",
            ),
            inv(
                "Wat moet Jess meebrengen? Antwoord met het Engelse woord uit het bericht.",
                ["speakers", "her speakers", "your speakers", "luidsprekers"],
                "Could you bring your speakers?",
            ),
        ],
    ),
    tabel(
        "Klopt deze vertaling (over wonen en vrije tijd)?",
        [
            ("the ground floor – het gelijkvloers", J),
            ("the first floor (Brits) – het gelijkvloers", F),
            ("crisps (Brits) – chips uit een zakje", J),
            ("a fortnight – een maand", F),
        ],
        "The first floor is de eerste verdieping; a fortnight is twee weken.",
    ),
    koppel(
        "Koppel elk Engels woord aan de juiste vertaling.",
        [
            ("tenant", "huurder"),
            ("lodger", "inwonende kamerhuurder"),
            ("neighbour", "buur"),
            ("flatmate", "huisgenoot"),
        ],
        ["verhuurder"],
        "Landlord zou de verhuurder zijn.",
    ),
    sorteer(
        "Hoort dit bij het huishouden of bij sport?",
        ["Huishouden", "Sport"],
        [
            ("the washing-up", "Huishouden"),
            ("the hoovering", "Huishouden"),
            ("the referee", "Sport"),
            ("a draw", "Sport"),
            ("the laundry", "Huishouden"),
        ],
        "The referee is de scheidsrechter, a draw een gelijkspel.",
    ),
    mk(
        "In een restaurant: hoe vraag je beleefd om de rekening?",
        ["Could we have the bill, please?", "Give me the bill right now, waiter.", "Where is the money for the meal?", "We want to pay you the meal now."],
        0,
        "Could we have … please? is beleefd en vast.",
    ),
    mk(
        "« I'd like my steak rare. » Hoe wil deze klant zijn steak?",
        ["Kort gebakken", "Goed doorbakken", "Halfdoorbakken", "Zonder saus"],
        0,
        "Rare, medium, well done.",
    ),
    mk(
        "« Liverpool beat Chelsea three nil. » Wie won?",
        ["Liverpool", "Chelsea", "Niemand", "Dat staat er niet"],
        0,
        "To beat someone is iemand verslaan.",
    ),
    mk(
        "« Last year I took up yoga. » Wat deed de spreker?",
        ["Ze begon met yoga", "Ze stopte met yoga", "Ze gaf yogales", "Ze zag yoga op tv"],
        0,
        "To take up is beginnen met; to give up is stoppen.",
    ),
    mk(
        "« We get on really well with our neighbours. » Wat betekent dat?",
        ["We komen goed overeen met de buren", "We gaan vaak samen met de buren uit eten", "We wonen heel dicht bij de buren", "We hebben altijd ruzie met de buren"],
        0,
        "To get on well with someone.",
    ),
    mk(
        "« Could you load the dishwasher? » Wat moet je doen?",
        ["De vaatwasser vullen", "De vaatwasser leegmaken", "De vaatwasser herstellen", "De vaatwasser kopen"],
        0,
        "To load is vullen, to unload leegmaken.",
    ),
    keuze(
        "Op een Engelse menukaart staat het voorgerecht onder [[*starters|mains]].",
        "Starter, main course, dessert.",
    ),
    keuze(
        "« Still water » is water [[*zonder bubbels|met bubbels]].",
        "Sparkling water heeft bubbels.",
    ),
    inv(
        "Vul aan met één Engels woord: « We're moving ___ next month. » (verhuizen)",
        ["house"],
        "To move house is verhuizen.",
    ),
    inv(
        "Vul aan met één Engels woord: « She works ___ at the gym three times a week. » (fitnessen)",
        ["out"],
        "To work out is trainen in een fitness.",
    ),
    mk(
        "« The flat is within walking distance of the shops. » Wat betekent dat?",
        ["Je gaat te voet", "Je moet de bus nemen naar de winkels", "De winkels liggen in hetzelfde gebouw", "Er zijn geen winkels in de buurt"],
        0,
        "Within walking distance: op wandelafstand.",
    ),
    keuze(
        "« A cosy living room » is een [[*gezellige|koude]] woonkamer.",
        "Cosy betekent knus en gezellig.",
    ),
    tabel(
        "Klopt deze betekenis (over wonen en vrije tijd)?",
        [
            ("the referee – de scheidsrechter", J),
            ("to give up running – beginnen met lopen", F),
            ("a fan – ook een ventilator", J),
        ],
        "To give up is stoppen met.",
    ),
    inv(
        "Vul aan met één Engels woord: « I'm ___ to peanuts, so I can't eat this cake. »",
        ["allergic"],
        "Allergic to: allergisch aan.",
    ),
    mk(
        "« Let's hang out at the park after school. » Wat stelt de spreker voor?",
        ["Samen rondhangen", "In het park gaan sporten", "Na school huiswerk maken", "Kleren ophangen in het park"],
        0,
        "To hang out is samen tijd doorbrengen.",
    ),
    sleep(
        "Mijn [[flatmate]] doet nooit de [[washing-up]]. De huur is [[due]] op de eerste van de maand.",
        ["landlord", "draw"],
        "Due betekent te betalen.",
    ),
    volgorde(
        "Zet de gangen van een Brits diner in de juiste volgorde.",
        ["starter", "main course", "dessert"],
        "Dessert heet in Groot-Brittannië ook pudding.",
    ),
    open_(
        "Schrijf in het Engels twee zinnen waarin je een vriend uitnodigt om zaterdag samen te koken bij jou thuis.",
        "Hi Sam, fancy coming round on Saturday? We could cook a curry together at my place, and my flatmate will make dessert.",
    ),
]
