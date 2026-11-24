"""Voornaamwoorden en betrekkelijke bijzinnen — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the e-mail.\n\nHi Emma, Thanks for your message. My cousin Jake, who lives in Dublin, is visiting us next week. "
        "He's bringing his dog, which is very friendly. Do you remember the café where we met last summer? "
        "Let's go there together! Jake doesn't know anybody here, so he'd love to meet you. Is that bag in the photo yours or your sister's? "
        "It looks great. Love, Mia",
        [
            keuze("« who » verwijst naar [[*Jake|Emma|Dublin]].", "Who gebruik je voor personen."),
            keuze("« which is very friendly » gaat over [[*de hond|Jake|het café]].", "Which voor dieren en dingen."),
            keuze("« where » verwijst naar [[*een plaats|een tijdstip|een persoon]].", "Where na een plaats: the café where ..."),
            mk("Waarom staat er « anybody » en niet « nobody »?",
               ["de zin is al ontkennend met doesn't", "anybody is beleefder",
                "nobody bestaat niet in het Engels", "het gaat over meer dan één persoon tegelijk"], 0,
               "Geen dubbele ontkenning: doesn't know anybody."),
            inv("Welk bezittelijk voornaamwoord in de tekst betekent « van jou », zonder naamwoord erna?", ["yours"], "Is that bag yours?"),
        ],
    ),
    tabel("Is deze zin juist (over voornaamwoorden)?", [
        ("Me and Tom are going to the cinema.", F),
        ("The dog wagged its tail.", J),
        ("This is the man which helped me.", F),
        ("Is this pen yours?", J),
    ], "Als onderwerp: Tom and I; voor personen: who of that."),
    mk("« The girl ___ mother is a doctor sits next to me. » Welk woord past?",
       ["whose", "who's", "who", "which"], 0, "Whose geeft bezit: van wie."),
    mk("« I'll never forget the day ___ I met you. » Welk woord past?",
       ["when", "where", "which", "who"], 0, "Na een tijdstip: when."),
    mk("« Can you help ___? » We hebben hulp nodig. Welk woord past?",
       ["us", "we", "our", "ours"], 0, "Na een werkwoord de voorwerpsvorm: us."),
    mk("« ___ is your favourite subject, maths or English? » Welk vraagwoord past?",
       ["Which", "Who", "Whose", "Where"], 0, "Which bij een keuze uit enkele mogelijkheden."),
    keuze("« Look at [[*these|this]] flowers in my hand! »", "Meervoud en dichtbij: these."),
    keuze("« Can you see [[*that|this]] bird on the roof over there? »", "Enkelvoud en ver weg: that."),
    keuze("« They built the treehouse [[*themselves|theirselves]]. »", "They: themselves."),
    keuze("« Is there [[*anything|nothing]] I can do for you? »", "In een vraag: anything."),
    keuze("« [[*Who's|Whose]] coming to the party tonight? »", "Who's = who is."),
    inv("Vul het wederkerend voornaamwoord in: « Help ___ to some cake, Lisa! » Eén woord.", ["yourself"], "Eén persoon, you: yourself."),
    inv("Vul het bezittelijk voornaamwoord in: « We love ___ new house. » Eén woord.", ["our"], "We: our."),
    inv("Vul het vraagwoord in: « ___ many brothers do you have? »", ["How", "how"], "How many bij telbare woorden."),
    koppel("Koppel elk persoonlijk voornaamwoord aan zijn bezittelijke vorm zonder naamwoord.", [
        ["I", "mine"], ["she", "hers"], ["we", "ours"], ["they", "theirs"],
    ], ["your"], "Your heeft nog een naamwoord nodig."),
    sorteer("Welk betrekkelijk voornaamwoord past?", ["who", "which"], [
        ["the nurse ___ helped me", "who"], ["the book ___ I read", "which"],
        ["the boy ___ won the race", "who"], ["the bus ___ goes to Genk", "which"],
    ], "Who voor personen, which voor dingen."),
    tabel("Welk soort voornaamwoord is dit?", [
        ("somebody", "onbepaald"), ("this", "aanwijzend"), ("ourselves (in « we did it ourselves »)", "wederkerend"),
    ], "Somebody is onbepaald, this wijst aan, -selves is wederkerend.",
       kolommen=["onbepaald", "aanwijzend", "wederkerend"]),
    mk("« Paul and Anna called. They said ___ car broke down. » Welk woord past?",
       ["their", "there", "they're", "theirs"], 0, "Bezit bij they: their."),
    volgorde("Zet de woorden in de juiste volgorde voor een vraag: « does / where / work / your father »", [
        "Where", "does", "your father", "work",
    ], "Vraagwoord, does, onderwerp, infinitief."),
    sleep("The woman [[who]] lives next door has a cat [[which]] sleeps all day. That is the reason [[why]] it is so fat!",
          ["where", "whose"], "Who voor personen, which voor dieren, why na reason."),
    tabel("Heb je « do » nodig in deze vraag?", [
        ("Who ___ lives in that house?", F), ("What ___ you want for dinner?", J), ("Who ___ you like most?", J),
    ], "Vraagt het vraagwoord naar het onderwerp, dan geen do."),
    keuze("« Everybody [[*has|have]] a locker at school. »", "Everybody is enkelvoud."),
    mk("Wat betekent « I did it by myself »?",
       ["ik deed het alleen", "ik deed het voor mezelf", "ik deed het met mezelf", "ik deed het naast mezelf"], 0,
       "By myself: zonder hulp."),
    keuze("Bij « jullie » gebruik je in het Engels gewoon [[*you|yous|your]].", "You is enkelvoud en meervoud."),
    inv("Vul het aanwijzend voornaamwoord in: « ___ shoes over there are mine. » Eén woord.", ["Those", "those"],
        "Meervoud en ver weg: those."),
    open_("Leg in het Nederlands het verschil uit tussen « its » en « it's ».",
          "« Its » is een bezittelijk voornaamwoord: van het, bijvoorbeeld the dog wagged its tail. « It's » is de verkorte vorm van it is of it has."),
]
