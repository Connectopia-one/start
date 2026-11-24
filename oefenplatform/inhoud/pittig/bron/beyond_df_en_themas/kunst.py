"""Woordvelden kunst, geschiedenis, literatuur en samenleving — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the poster.\n\n« CITY MUSEUM – New exhibition: 'The Roman Empire'\n"
        "See ancient sculptures, coins and paintings from the first century. Our guide tells you about the emperors, the battles and daily life in Rome. "
        "Entrance fee: £8, free for children under 12. All money from the gift shop goes to a local charity. "
        "Volunteers wanted: can you help us at the weekend? »",
        [
            keuze("De tentoonstelling gaat over [[*het Romeinse Rijk|de Franse Revolutie|het oude Griekenland]].", "The Roman Empire."),
            keuze("« ancient sculptures » zijn [[*heel oude beelden|nieuwe schilderijen]].", "Ancient: heel oud; sculpture: beeld."),
            mk("Wat gebeurt er met het geld van de museumwinkel?",
               ["Het gaat naar een goed doel.", "Het betaalt de gids van de tentoonstelling.", "Het gaat naar de Romeinse keizer.", "Het betaalt de inkom van de kinderen."], 0,
               "Goes to a local charity."),
            keuze("Kinderen onder 12 betalen [[*niets|8 pond|de helft]].", "Free for children under 12."),
            keuze("Het museum zoekt [[*vrijwilligers|kunstenaars|klanten]] voor het weekend.", "Volunteers wanted."),
        ],
    ),
    sorteer("Hoort het bij geschiedenis of bij de politiek van vandaag?", ["geschiedenis", "politiek vandaag"], [
        ["the Roman Empire", "geschiedenis"], ["an election", "politiek vandaag"], ["an ancient battle", "geschiedenis"],
        ["the Prime Minister", "politiek vandaag"], ["an old peace treaty", "geschiedenis"], ["the city council", "politiek vandaag"],
    ], "Oude rijken en veldslagen tegenover verkiezingen en ministers."),
    koppel("Koppel elk woord over boeken aan zijn betekenis.", [
        ["a novel", "een roman"], ["a chapter", "een hoofdstuk"], ["an author", "een schrijver"], ["a biography", "een levensverhaal"],
    ], ["een rijm"], "A rhyme is een rijm."),
    koppel("Koppel elk woord uit recht en samenleving aan zijn betekenis.", [
        ["a judge", "een rechter"], ["a refugee", "een vluchteling"], ["a trade union", "een vakbond"], ["a citizen", "een burger"],
    ], ["een handelsbeurs"], "A trade fair is een handelsbeurs."),
    mk("« The actors ___ the play every evening for two weeks before the first performance. » Wat past?",
       ["rehearse", "elect", "protest", "volunteer"], 0, "To rehearse: repeteren."),
    mk("Wie leidt een orkest?",
       ["the conductor", "the composer of the music", "the playwright", "the audience in the hall"], 0, "Een dirigent is a conductor."),
    mk("« 51% of the people voted yes. » Hoe noem je die 51%?",
       ["the majority", "the minority group", "the media", "the charities"], 0, "Meer dan de helft: de meerderheid."),
    mk("Een schrijver vertelt over zijn eigen leven. Hoe heet dat boek?",
       ["an autobiography", "a biography", "a fiction book or novel", "a short story about life"], 0,
       "Over je eigen leven: an autobiography."),
    mk("« The nineteenth century » zijn de jaren ...",
       ["1800 tot 1899", "1900 tot en met 1999", "1700 tot 1799", "1900 tot 1919"], 0, "De negentiende eeuw: de jaren 1800."),
    mk("Hoe zeg je « Wij hebben gestemd bij de verkiezingen »?",
       ["We voted in the elections.", "We elected in the votes.", "We protested in the elections.", "We voted on the citizens."], 0,
       "To vote: stemmen; an election: een verkiezing."),
    inv("Hoe zeg je gelijkheid in het Engels? Eén woord.", ["equality"], "Equality."),
    inv("Hoe zeg je rechtbank in het Engels? Eén woord.", ["court", "a court"], "A court."),
    inv("Hoe zeg je armoede in het Engels? Eén woord.", ["poverty"], "Poverty."),
    inv("Hoe zeg je keizer in het Engels? Eén woord.", ["emperor", "an emperor", "the emperor"], "The emperor."),
    inv("Hoe zeg je tentoonstelling in het Engels? Eén woord.", ["exhibition", "an exhibition"], "An exhibition."),
    keuze("« The [[*audience|author]] clapped for ten minutes after the concert. »", "Het publiek klapt."),
    keuze("« Harry Potter is [[*fiction|non-fiction]]: the story is not real. »", "Verzonnen verhalen."),
    keuze("« The Mona Lisa is a famous [[*masterpiece|rehearsal]]. »", "Een meesterwerk."),
    keuze("« Thousands of people [[*protested|rehearsed]] in the streets against the new law. »", "To protest: betogen."),
    keuze("« The [[*heir|air]] to the throne is the king's eldest son. »", "Heir: erfgenaam, met een stomme h."),
    tabel("Is deze zin juist (kunst en samenleving)?", [
        ("The painting is in a gallery in London.", J), ("A conductor writes the music.", F),
        ("Everybody should have the same human rights.", J), ("The minority is more than half of the people.", F),
    ], "Een composer schrijft muziek; de minderheid is minder dan de helft."),
    tabel("Hoort dit bij het theater?", [
        ("a stage", J), ("an audience", J), ("a kettle", F), ("a treaty", F),
    ], "Podium en publiek; een waterkoker en een verdrag niet."),
    sleep("The [[author]] wrote her first [[novel]] when she was only twenty. It has twelve [[chapters]].",
          ["judge", "stage"], "Author, novel, chapters."),
    volgorde("Zet deze periodes in de juiste volgorde, van oud naar recent.", [
        "Ancient Rome", "the sixteenth century", "the nineteenth century", "the twenty-first century",
    ], "Van de oudheid naar vandaag."),
    open_("Leg in het Nederlands uit wat een « charity shop » is.",
          "Een winkel die tweedehands spullen verkoopt en het geld aan een goed doel geeft.",
          "Charity: een goed doel."),
    mk("Wat doet a volunteer?",
       ["helpen zonder loon", "betogen voor een hoger loon", "een wet maken in het parlement", "een boek over iemands leven schrijven"], 0,
       "Een vrijwilliger."),
]
