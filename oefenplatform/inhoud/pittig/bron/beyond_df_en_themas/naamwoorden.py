"""Naamwoorden, lidwoorden en hoeveelheden — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the shopping list and the note.\n\nShopping list: two loaves of bread, a bottle of milk, six potatoes, some cheese, a few tomatoes.\n"
        "Note from Mum: We don't need much sugar, there is still a lot in the cupboard. Don't forget the children's birthday cards! "
        "And please buy an umbrella: yours is broken.",
        [
            tabel("Telbaar of ontelbaar in het Engels?", [
                ("bread", "ontelbaar"), ("potato", "telbaar"), ("cheese", "ontelbaar"), ("tomato", "telbaar"),
            ], "Ontelbaar gebruik je met some, much of een maat zoals a loaf of.", kolommen=["telbaar", "ontelbaar"]),
            keuze("« two loaves of bread »: het enkelvoud van loaves is [[*loaf|loave|loafs]].", "De f wordt v in het meervoud."),
            keuze("Mama schrijft « much sugar » omdat sugar [[*ontelbaar|telbaar]] is.", "Much bij ontelbare woorden."),
            keuze("« the children's birthday cards » zijn de kaarten [[*voor de kinderen|van één kind]].",
                  "Children is al een meervoud: de apostrof komt voor de s."),
            keuze("Mama schrijft « an umbrella » omdat umbrella met een [[*klinkerklank|medeklinker]] begint.", "An voor een klinkerklank."),
        ],
    ),
    tabel("Is het meervoud juist?", [
        ("one tooth, two teeth", J), ("one wife, two wifes", F), ("one city, two cities", J), ("one mouse, two mouses", F),
    ], "Wife wordt wives; mouse wordt mice."),
    mk("« There aren't ___ eggs left. We need to buy some. » Welk woord past?",
       ["many", "much", "a little", "any of"], 0, "Eggs is telbaar en meervoud: many."),
    mk("« Can you give me ___ advice? » Welk woord past?",
       ["some", "an", "many", "a few"], 0, "Advice is ontelbaar: some advice."),
    mk("Hoe zeg je « de fiets van mijn ouders »?",
       ["my parents' bike", "my parent's bike", "the bike of my parents's", "my parentses bike"], 0,
       "Bij een meervoud op -s komt enkel een apostrof."),
    mk("Hoe zeg je « de poot van de tafel »?",
       ["the table leg", "the table's leg's", "the leg's table", "the tables leg"], 0,
       "Bij voorwerpen zet je de twee naamwoorden gewoon na elkaar."),
    keuze("« She wants to be [[*an|a]] engineer. »", "An voor een klinkerklank."),
    keuze("« He is [[*a|an]] university student. »", "University begint met de klank « joe »: a."),
    keuze("« [[*The|–]] sun is shining. »", "Er is maar één zon: the."),
    keuze("« I love [[*–|the]] chocolate. » Je spreekt over chocolade in het algemeen.", "In het algemeen geen lidwoord."),
    keuze("« My jeans [[*are|is]] too short. »", "Jeans is altijd meervoud."),
    keuze("« The news [[*is|are]] on at eight. »", "News is ontelbaar en enkelvoud."),
    inv("Schrijf het meervoud van « leaf ».", ["leaves"], "De f wordt v."),
    inv("Schrijf het rangtelwoord bij « nine ».", ["ninth"], "De e valt weg."),
    inv("Schrijf het rangtelwoord bij « twenty ». Eén woord.", ["twentieth"], "De y wordt ie, dan -th."),
    koppel("Koppel elke hoeveelheid aan het woord dat erbij past.", [
        ["a bottle of", "water"], ["a slice of", "bread"], ["a pair of", "shoes"], ["a piece of", "information"],
    ], ["children"], "Children kan je gewoon tellen."),
    sorteer("Much of many?", ["much", "many"], [
        ["money", "much"], ["people", "many"], ["homework", "much"], ["questions", "many"],
        ["traffic", "much"], ["cars", "many"],
    ], "Many bij telbare meervouden, much bij ontelbare woorden."),
    tabel("Is deze zin juist (over naamwoorden en lidwoorden)?", [
        ("I have a few money.", F), ("There is a little milk left.", J),
        ("We went to the bed late.", F), ("The Netherlands is a small country.", J),
    ], "A few bij telbare woorden; to go to bed zonder lidwoord."),
    mk("Hoe lees je « 2008 » als jaartal?",
       ["two thousand and eight", "twenty eight", "two hundred and eight", "twenty and zero eight"], 0,
       "Jaartallen vanaf 2000 lees je meestal als two thousand and ..."),
    inv("Hoe schrijf je « 1/2 » in woorden in het Engels? Twee woorden.", ["a half", "one half"], "A half of one half."),
    sleep("There are [[plenty of]] chairs, so everybody can sit. We only have [[a little]] juice, so drink slowly.",
          ["much", "a few"], "Plenty of: meer dan genoeg. A little: een beetje, bij ontelbaar."),
    tabel("Lidwoord of geen lidwoord?", [
        ("Belgium", "geen lidwoord"), ("United Kingdom", "the"), ("Mount Everest", "geen lidwoord"),
    ], "Gewone landnamen zonder lidwoord; namen met « kingdom » of « states » met the.",
       kolommen=["the", "geen lidwoord"]),
    mk("« Whose bags are these? » — « They're the ___ bags. » (van de meisjes)",
       ["girls'", "girl's", "girls's", "girles'"], 0, "Meervoud op -s: enkel een apostrof."),
    keuze("« We need [[*a couple of|much]] volunteers for Saturday. »", "Volunteers is telbaar: a couple of."),
    tabel("Klopt dit over people?", [
        ("people is een meervoud", J),
        ("je zegt « many people »", J),
        ("je zegt « the people is nice »", F),
    ], "People is een meervoud: the people are nice."),
    open_("Leg in het Nederlands uit waarom je « an hour » zegt maar « a house ».",
          "Je kijkt naar de klank, niet naar de letter. In hour hoor je de h niet, dus begint het met een klinkerklank en zeg je an. In house hoor je de h wel, dus zeg je a."),
]
