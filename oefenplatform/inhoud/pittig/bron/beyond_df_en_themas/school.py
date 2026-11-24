"""Woordvelden school en werk, geld en verkeer — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the job advert.\n\n« VACANCY – Shop assistant (part-time, 20 hours a week)\n"
        "We are a busy bookshop in the city centre. You will help customers, work at the till and keep the shelves tidy. "
        "Skills: you are friendly, you speak English and Dutch, and you can work in a team. No degree needed. "
        "Pay: £11 an hour, plus a 20% staff discount on all books. "
        "To apply, send your CV and a short letter of application before the deadline of 15 June. »",
        [
            keuze("Het gaat om een [[*deeltijdse|voltijdse]] job.", "Part-time, 20 uur per week."),
            keuze("« work at the till » betekent werken aan [[*de kassa|het rek|de deur]].", "A till: de kassa."),
            mk("Wat moet je hebben om te mogen solliciteren?",
               ["geen diploma", "een universitair diploma", "een rijbewijs voor de bestelwagen", "drie jaar ervaring in een boekhandel"], 0,
               "No degree needed."),
            keuze("Personeel krijgt [[*korting|rente|een lening]] op alle boeken.", "A staff discount."),
            inv("Tot welke datum kan je solliciteren? Schrijf de dag en de maand in het Nederlands, bv. 3 mei.", ["15 juni"],
                "The deadline of 15 June."),
        ],
    ),
    sorteer("Hoort het bij school of bij het verkeer?", ["school", "verkeer"], [
        ["a timetable", "school"], ["a roundabout", "verkeer"], ["a report", "school"],
        ["a pedestrian", "verkeer"], ["homework", "school"], ["a traffic jam", "verkeer"],
    ], "Rooster, rapport en huiswerk tegenover rotonde, voetganger en file."),
    koppel("Koppel elk woord over winkelen aan zijn betekenis.", [
        ["a receipt", "een kassabon"], ["a recipe", "een recept om te koken"], ["a refund", "geld dat je terugkrijgt"], ["a bargain", "een koopje"],
    ], ["de btw"], "VAT is de btw."),
    koppel("Koppel het Britse woord aan het Amerikaanse.", [
        ["petrol", "gas"], ["a lorry", "a truck"], ["a motorway", "a highway"], ["the pavement", "the sidewalk"],
    ], ["a van"], "A van is een bestelwagen, in beide landen."),
    mk("« I can't ___ a new phone. It's too expensive. » Wat past?",
       ["afford", "refund", "commute", "apply for"], 0, "To afford: kunnen betalen."),
    mk("« She ___ her driving test, so now she can drive alone. » Wat past?",
       ["passed", "failed", "took notes on", "was made redundant from"], 0, "To pass: slagen."),
    mk("Tom verloor zijn job omdat de fabriek sloot. Hoe zeg je dat?",
       ["He was made redundant.", "He got a promotion.", "He applied for a new job.", "He met the deadline at work."], 0,
       "Made redundant: je job verliezen omdat hij wegvalt."),
    mk("Waar steek je veilig over als voetganger?",
       ["op a zebra crossing", "op the motorway", "midden op a roundabout", "tussen de auto's in a traffic jam"], 0, "Een zebrapad."),
    mk("Je reed te snel en de politie houdt je tegen. Wat krijg je?",
       ["a fine", "a discount", "a refund", "a bargain"], 0, "A fine: een boete."),
    mk("« I take the train to London every day for work. » Wat doet deze persoon?",
       ["pendelen", "solliciteren", "vakantiewerk doen", "stage lopen"], 0, "To commute."),
    inv("Hoe zeg je voetganger in het Engels? Eén woord.", ["pedestrian", "a pedestrian"], "A pedestrian."),
    inv("Hoe zeg je vrachtwagen in het Brits Engels? Eén woord.", ["lorry", "a lorry"], "A lorry; in de VS a truck."),
    inv("Hoe zeg je klant in het Engels? Eén woord.", ["customer", "a customer"], "A customer."),
    inv("Hoe zeg je vak op school in het Engels? Eén woord.", ["subject", "a subject"], "A subject."),
    inv("Hoe zeg je spitsuur in het Engels? Twee woorden.", ["rush hour"], "Rush hour."),
    keuze("« We have a lot of [[*homework|homeworks]] this week. »", "Homework is ontelbaar."),
    keuze("« My [[*colleague|classmate]] at the office helps me with the computer. »", "Een collega op het werk."),
    keuze("« Can I pay [[*by card|with card by]]? » « Sure. »", "To pay by card; contant is in cash."),
    keuze("« We were stuck in a traffic jam during [[*rush hour|a break]]. »", "Het spitsuur."),
    keuze("« Prices [[*include|refund]] VAT. »", "Prices include VAT."),
    tabel("Is deze zin juist (school, werk en geld)?", [
        ("I have to meet the deadline on Friday.", J), ("She has a lot of homeworks.", F),
        ("He paid in cash.", J), ("I want to apply a job.", F),
    ], "Homework is ontelbaar; to apply for a job."),
    tabel("Is dit een beroep?", [
        ("a plumber", J), ("a canteen", F), ("a nurse", J), ("a timetable", F),
    ], "Loodgieter en verpleegkundige zijn beroepen."),
    volgorde("Zet de stappen om een job te vinden in de juiste volgorde.", [
        "een vacancy vinden", "je CV en een brief sturen", "een interview hebben", "de job krijgen",
    ], "Eerst zoeken, dan solliciteren, dan het gesprek."),
    sleep("I bought this jacket in the [[sales]]. It was a real [[bargain]]: only ten pounds!",
          ["fine", "loan"], "The sales: de solden; a bargain: een koopje."),
    open_("Leg in het Nederlands uit wat het verschil is tussen « a salary » en « a wage ».",
          "Een salary is een vast maandloon, een wage is eerder een uur- of weekloon.",
          "Allebei loon, maar anders betaald."),
    mk("Wat is « a work placement »?",
       ["een stage", "een vaste job", "een werkloosheidsuitkering", "een collega op het werk"], 0, "Ook an internship."),
]
