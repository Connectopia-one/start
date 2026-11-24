"""Woordvelden wetenschap, techniek, sport en taalbeschouwing — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the message from a school club.\n\n« Science and Sports Club – this week\n"
        "Monday: we carry out an experiment in the lab. Bring your own device, but make sure the battery is charged!\n"
        "Wednesday: football match against Riverside School on the big pitch. Last time it was a draw (2–2).\n"
        "Friday: board games and chess in the library. Don't forget: the library closes at five. »",
        [
            keuze("Op maandag doen ze een [[*proef in het labo|wedstrijd op het veld]].", "Carry out an experiment in the lab."),
            keuze("Je moet ervoor zorgen dat je toestel [[*opgeladen|uitgeschakeld]] is.", "The battery is charged."),
            keuze("De vorige match tegen Riverside eindigde [[*gelijk|met winst|met verlies]].", "A draw: gelijkspel."),
            keuze("Op vrijdag zijn ze in [[*de bibliotheek|de boekhandel]].", "Library is een valse vriend: bibliotheek."),
            mk("Wat doen ze op vrijdag?",
               ["gezelschapsspellen en schaken", "een proef in het labo met hun toestel", "voetballen tegen een andere school", "een wandeltocht maken in het bos"], 0,
               "Board games and chess."),
        ],
    ),
    sorteer("Is dit woord of deze spelling Brits of Amerikaans?", ["Brits", "Amerikaans"], [
        ["autumn", "Brits"], ["fall", "Amerikaans"], ["colour", "Brits"], ["color", "Amerikaans"], ["a biscuit", "Brits"], ["a cookie", "Amerikaans"],
    ], "Elke variant heeft eigen woorden en een eigen spelling."),
    koppel("Koppel elke valse vriend aan zijn echte betekenis.", [
        ["eventually", "uiteindelijk"], ["actually", "eigenlijk"], ["sympathetic", "meelevend"], ["to realise", "beseffen"],
    ], ["eventueel"], "Eventueel is possibly."),
    koppel("Koppel elk voorvoegsel of achtervoegsel aan zijn betekenis.", [
        ["un-", "niet"], ["re-", "opnieuw"], ["-less", "zonder"], ["-ful", "vol van"],
    ], ["groot"], "Un-happy, re-write, care-less, help-ful."),
    mk("« I didn't ___ that the shop was closed. » Ik besefte het niet. Wat past?",
       ["realise", "control", "charge", "download"], 0, "To realise: beseffen."),
    mk("Hoe zeg je « De boekhandel is om de hoek »?",
       ["The bookshop is around the corner.", "The library is around the corner.", "The bookcase is around the corner.", "The bookshelf is around the corner."], 0,
       "Een boekhandel is a bookshop."),
    mk("« ___ going to rain today. » Welke vorm past?",
       ["It's", "Its", "It", "It is is"], 0, "It's = it is."),
    mk("« Is this ___ bag? » Welke vorm past?",
       ["your", "you're", "you are", "yours'"], 0, "Bezittelijk: your."),
    mk("Welk woord is een samenstelling?",
       ["sunglasses", "quickly", "teacher", "carelessly"], 0, "Sun + glasses: twee woorden samen."),
    mk("Wat is het omgekeerde van « useful »?",
       ["useless", "unuseful", "disuseful", "reuseful"], 0, "-ful tegenover -less."),
    inv("Maak het omgekeerde van « possible » met een voorvoegsel. Eén woord.", ["impossible"], "Im-possible."),
    inv("Maak het omgekeerde van « agree » met een voorvoegsel. Eén woord.", ["disagree"], "Dis-agree."),
    inv("Hoe zeg je toetsenbord in het Engels? Eén woord.", ["keyboard", "a keyboard"], "A keyboard."),
    inv("Hoe zeg je scheidsrechter in het Engels? Eén woord.", ["referee", "a referee"], "A referee."),
    keuze("« We need to do more [[*research|researches]] on this topic. »", "Research is ontelbaar."),
    keuze("« Can I borrow your [[*charger|password]]? My phone is dead. »", "De lader: the charger."),
    keuze("« [[*Their|There]] house is next to the park. »", "Bezittelijk: their."),
    keuze("« [[*Who's|Whose]] going to win the match tomorrow? »", "Who's = who is."),
    keuze("« Please [[*check|control]] your answers before you hand in the test. »", "Nakijken is to check."),
    keuze("« That [[*makes|does]] sense! »", "To make sense: logisch zijn."),
    tabel("Is deze zin juist (taal en techniek)?", [
        ("The dog wagged its tail.", J), ("I'm going to the library to buy a book.", F),
        ("My battery is empty, I need my charger.", J), ("We are going to there house.", F),
    ], "In een library leen je boeken; their house."),
    tabel("Is dit een synoniem van « big »?", [
        ("large", J), ("small", F), ("huge", J), ("little", F),
    ], "Een synoniem heeft dezelfde betekenis; small is een antoniem."),
    sleep("You need a [[username]] and a [[password]] to log in. Then you can [[download]] the file.",
          ["screenshot", "referee"], "Username, password, download."),
    mk("Wat betekent « It was a draw » na een voetbalmatch?",
       ["Het was gelijkspel.", "Het was een mooie tekening.", "Onze ploeg heeft gewonnen.", "De scheidsrechter floot af."], 0,
       "A draw: gelijkspel; to draw betekent ook tekenen."),
    open_("Leg in het Nederlands uit waarom « library » een valse vriend is.",
          "Het lijkt op librairie of boekhandel, maar het betekent bibliotheek.",
          "Een boekhandel is a bookshop."),
    mk("Wat is « a spreadsheet »?",
       ["een rekenblad op de computer", "een laken voor op een groot bed", "een groot scherm in de klas", "een bestand met foto's"], 0,
       "Een rekenblad, zoals in Excel."),
]
