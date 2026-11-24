"""Naamwoorden, lidwoorden en hoeveelheden — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text and answer the questions.\n\n"
    "Our school trip to Scotland was great. We left on the fifth of June, by coach, with forty-two pupils and four teachers. "
    "The hotel was a ten-minute walk from the castle. Unfortunately, the luggage of two girls got lost, "
    "so the teachers gave them some advice about buying a few things in town. "
    "We didn't have much free time, but there were plenty of activities."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            keuze(
                "In « a ten-minute walk » staat minute in het [[*enkelvoud|meervoud]], omdat het een samenstelling is.",
                "In een samenstelling met een getal blijft het naamwoord enkelvoud.",
            ),
            keuze(
                "« Luggage » en « advice » zijn [[*ontelbaar|telbaar]].",
                "Je zegt dus some advice, geen advices.",
            ),
            mk(
                "Waarom staat er « much free time » en niet « many free time »?",
                ["Time is hier ontelbaar", "Time is een meervoud", "Much past altijd na didn't", "Many is Amerikaans Engels"],
                0,
                "Much bij ontelbare woorden, many bij telbare.",
            ),
            inv(
                "Schrijf de datum uit de tekst in het Nederlands, bv. 1 januari.",
                ["5 juni", "vijf juni", "5/6"],
                "The fifth of June is Brits.",
            ),
        ],
    ),
    tabel(
        "Is dit meervoud juist?",
        [
            ("two wives", J),
            ("three mouses", F),
            ("four photos", J),
            ("five sheeps", F),
            ("two crises", J),
        ],
        "Mice en sheep zijn onregelmatig; photos zonder e; crisis wordt crises.",
    ),
    sleep(
        "Two [[children]] lost their [[teeth]] while their [[feet]] were in the water.",
        ["childs", "tooths", "foots"],
        "Children, teeth, feet: onregelmatig meervoud.",
    ),
    mk(
        "Welke bezitsvorm is juist voor « de kamer van mijn twee zussen »?",
        ["my sisters' room", "my sister's room", "my sisters's room", "my sister room"],
        0,
        "Meervoud op -s: de apostrof komt achter de s.",
    ),
    mk(
        "Welke bezitsvorm is juist voor « het speelgoed van de kinderen »?",
        ["the children's toys", "the childrens' toys", "the childrens toys", "the children toys's"],
        0,
        "Children eindigt niet op s: 's erachter.",
    ),
    mk(
        "Welke zin over het nieuws is juist?",
        ["The news was shocking.", "The news were shocking.", "The newses was shocking.", "A news was shocking."],
        0,
        "News is enkelvoud.",
    ),
    mk(
        "Welke zin over de politie is juist?",
        ["The police are looking for him.", "The police is looking for him.", "The polices are looking for him.", "A police are looking for him."],
        0,
        "Police is meervoud.",
    ),
    mk(
        "Welke zin over meubels is juist?",
        ["I need some new furniture.", "I need some new furnitures.", "I need a new furniture.", "I need many new furniture."],
        0,
        "Furniture is ontelbaar.",
    ),
    tabel(
        "A of an?",
        [
            ("___ honest answer", "an"),
            ("___ European country", "a"),
            ("___ hour", "an"),
            ("___ useful tip", "a"),
        ],
        "Het gaat om de eerste klank: honest en hour beginnen met een klinker, European en useful met een j-klank.",
        kolommen=["a", "an"],
    ),
    tabel(
        "Hoort er hier « the » of geen lidwoord?",
        [
            ("She plays ___ violin in an orchestra.", "the"),
            ("We travelled to ___ Spain.", "geen"),
            ("___ cats are independent animals.", "geen"),
            ("___ sun is shining.", "the"),
        ],
        "The bij instrumenten en unieke dingen; geen lidwoord bij landen en algemene uitspraken.",
        kolommen=["the", "geen"],
    ),
    tabel(
        "Much of many?",
        [
            ("How ___ students failed?", "many"),
            ("How ___ sugar do you take?", "much"),
            ("There isn't ___ traffic today.", "much"),
            ("I haven't got ___ friends here.", "many"),
        ],
        "Many bij telbaar, much bij ontelbaar.",
        kolommen=["much", "many"],
    ),
    keuze(
        "« I have a few friends in London » betekent dat ik er [[*enkele|bijna geen]] vrienden heb.",
        "A few is enkele; few zonder a is weinig.",
    ),
    keuze(
        "« There is little hope » betekent dat er [[*weinig|wat]] hoop is.",
        "Little zonder a is weinig; a little is een beetje.",
    ),
    keuze(
        "« Have you got [[*any|some]] questions? » vraagt de leraar zonder iets te verwachten.",
        "Any in een gewone vraag.",
    ),
    keuze(
        "« Would you like [[*some|any]] tea? » is een aanbod.",
        "Bij een aanbod gebruik je some, ook in een vraag.",
    ),
    inv(
        "Schrijf het rangtelwoord bij « twenty-one », in letters.",
        ["twenty-first", "twenty first"],
        "One wordt first.",
    ),
    inv(
        "Schrijf in cijfers: « two thousand three hundred and forty ».",
        ["2340", "2,340", "2.340", "2 340"],
        "Brits Engels zet and voor de tientallen.",
    ),
    mk(
        "Welke zin over de bezoekers is juist?",
        ["Three hundred people came.", "Three hundreds people came.", "Three hundreds of people came.", "Three hundred of people came."],
        0,
        "Na een getal blijft hundred enkelvoud.",
    ),
    mk(
        "« Hundreds of people » betekent …",
        ["honderden mensen", "precies honderd mensen", "driehonderd mensen", "een honderdste van de mensen"],
        0,
        "Zonder getal ervoor: hundreds of, thousands of.",
    ),
    mk(
        "Welk meervoud van hero is juist?",
        ["heroes", "heros", "heroies", "heroen"],
        0,
        "Hero, potato en tomato krijgen -es.",
    ),
    sorteer(
        "Telbaar of ontelbaar?",
        ["Telbaar", "Ontelbaar"],
        [
            ("information", "Ontelbaar"),
            ("suitcase", "Telbaar"),
            ("advice", "Ontelbaar"),
            ("idea", "Telbaar"),
            ("homework", "Ontelbaar"),
        ],
        "Bij ontelbare woorden gebruik je a piece of.",
    ),
    inv(
        "Vul aan met één Engels woord: « Can you lend me a ___ of scissors? »",
        ["pair"],
        "Scissors en trousers telt men in pairs.",
    ),
    inv(
        "Vul aan: « The roof ___ the house was damaged in the storm. »",
        ["of"],
        "Bij dingen gebruik je meestal of.",
    ),
    mk(
        "Welke zin over je haar is juist?",
        ["My hair is wet.", "My hairs are wet.", "My hair are wet.", "My hairs is wet."],
        0,
        "Hair over het hele hoofd is ontelbaar.",
    ),
    keuze(
        "« I'll be back in [[*half an hour|a half hour of]] » is correct Brits Engels.",
        "Half an hour: een half uur.",
    ),
    volgorde(
        "Zet deze hoeveelheden van weinig naar veel.",
        ["no milk", "a little milk", "some milk", "plenty of milk"],
        "Plenty of is ruim genoeg.",
    ),
    open_(
        "Leg in het Nederlands uit waarom je « an hour » maar « a house » schrijft.",
        "Het lidwoord hangt af van de eerste klank. In hour hoor je de h niet, dus begint het met een klinkerklank en schrijf je an. In house hoor je de h wel, dus schrijf je a.",
    ),
]
