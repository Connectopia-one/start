"""Woordvelden dagelijks leven, eten en drinken, wonen — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the advert.\n\n« FLAT TO RENT – Cosy two-bedroom flat on the ground floor of a quiet building. "
        "Fully furnished: new furniture, curtains, a fridge and a washing machine. The boiler was replaced last year. "
        "Small garden with a lawn and a fence. Rent: £850 a month. The landlord lives next door. "
        "No pets. Tenants must keep the garden tidy. »",
        [
            keuze("De flat ligt op [[*het gelijkvloers|de eerste verdieping|de zolder]].", "The ground floor."),
            keuze("« Fully furnished » betekent dat er al [[*meubels|geen meubels]] in staan.", "Furniture: meubels."),
            mk("Wie woont er naast de flat?",
               ["de verhuurder", "de vorige huurder", "een gezin met huisdieren", "de buurman die de tuin doet"], 0,
               "The landlord lives next door."),
            keuze("De huurders moeten [[*de tuin netjes houden|de ketel vervangen|de huur elke week betalen]].", "Keep the garden tidy."),
            mk("Wat staat er in de tuin?",
               ["een grasveld en een afsluiting", "een tuinhuisje en een grote vijver", "een trap naar de kelder", "een vuilnisbak voor de buren"], 0,
               "A lawn and a fence."),
        ],
    ),
    sorteer("Make of do?", ["make", "do"], [
        ["a mistake", "make"], ["the dishes", "do"], ["a decision", "make"], ["the washing-up", "do"], ["a cake", "make"], ["homework", "do"],
    ], "Make bij maken of veroorzaken, do bij uitvoeren."),
    sorteer("Hoort het in de keuken of in de tuin?", ["keuken", "tuin"], [
        ["a kettle", "keuken"], ["a lawn", "tuin"], ["a tap", "keuken"], ["a fence", "tuin"], ["a fridge", "keuken"], ["a shed", "tuin"],
    ], "Een waterkoker en een kraan binnen, een grasveld en een tuinhuisje buiten."),
    koppel("Koppel elke uitdrukking aan haar betekenis.", [
        ["to have a lie-in", "uitslapen"], ["to be fed up with", "er genoeg van hebben"], ["to get on well with", "goed overeenkomen met"], ["to move house", "verhuizen"],
    ], ["afwassen"], "Afwassen is to do the washing-up."),
    koppel("Koppel elk type huis aan zijn betekenis.", [
        ["a detached house", "een vrijstaand huis"], ["a semi-detached house", "een halfopen woning"], ["a terraced house", "een rijhuis"], ["a cottage", "een huisje op het platteland"],
    ], ["een appartement"], "Een appartement is a flat."),
    mk("« I'm so tired. On Saturday I want to ___. » Wat past?",
       ["have a lie-in", "do the laundry", "move house", "tidy up the attic"], 0, "Uitslapen na een vermoeiende week."),
    mk("« Can I have ___ advice about my new flat? » Wat past?",
       ["some", "an", "two", "a few"], 0, "Advice is ontelbaar."),
    mk("Je bent in een snackbar in Londen. Welke vraag krijg je?",
       ["To eat in or take away?", "Do you want to rent a flat?", "Are you the new tenant here?", "Can you do the washing-up?"], 0,
       "Eten om mee te nemen: takeaway."),
    mk("Hoe heten frietjes in het Verenigd Koninkrijk?",
       ["chips", "spices", "snacks", "squash"], 0, "Fish and chips: vis met friet."),
    mk("« The ___ is very new. We bought it last week. » Wat past?",
       ["furniture", "furnitures", "furnitures pieces", "piece furnitures"], 0, "Furniture is ontelbaar en enkelvoud."),
    mk("Waar woon je in een Brits gebouw als je op « the first floor » woont?",
       ["op de eerste verdieping", "op het gelijkvloers", "in de kelder onder het gebouw", "op de zolder van het gebouw"], 0,
       "In het Brits is the first floor de eerste verdieping."),
    inv("Hoe zeg je vork in het Engels? Eén woord.", ["fork", "a fork"], "A fork."),
    inv("Hoe zeg je stofzuiger in het Brits Engels? Eén woord.", ["hoover", "a hoover"], "A hoover."),
    inv("Hoe zeg je kast in de keuken in het Engels? Eén woord.", ["cupboard", "a cupboard"], "A cupboard."),
    inv("Schrijf het meervoud van « hobby ».", ["hobbies"], "Hobbies, met ie."),
    keuze("« We are going to the cinema [[*by bus|with the bus]]. »", "By bus."),
    keuze("« I'm [[*at home|at the home]] tonight. »", "At home, zonder lidwoord."),
    keuze("« Please put the paper [[*in the bin|in the kettle]]. »", "A bin: een vuilnisbak."),
    keuze("« This curry is very [[*spicy|cosy]]. »", "Spicy: pikant."),
    keuze("« My brother never helps with the household [[*chores|tenants]]. »", "Chores: klusjes in huis."),
    tabel("Is deze zin juist (dagelijks leven)?", [
        ("I did a big mistake.", F), ("She gets on well with her neighbours.", J),
        ("We had a snack after school.", J), ("I'm fed up of this weather, I'm fed.", F),
    ], "To make a mistake; to be fed up with."),
    tabel("Is dit een familielid?", [
        ("an aunt", J), ("a landlord", F), ("a nephew", J), ("a neighbour", F),
    ], "Een tante en een neefje zijn familie; een verhuurder en een buur niet."),
    sleep("On Sunday I always [[tidy up]] my room. Then I help my dad with the [[washing-up]] after dinner.",
          ["rent", "loft"], "To tidy up: opruimen. The washing-up: de vaat."),
    inv("Hoe zeg je gordijnen in het Engels? Eén woord.", ["curtains"], "Curtains, meestal in het meervoud."),
    volgorde("Zet de maaltijden van een Britse dag in de juiste volgorde.", [
        "breakfast", "lunch", "dinner",
    ], "Ontbijt, middagmaal, warme maaltijd 's avonds."),
    open_("Leg in het Nederlands uit wat het verschil is tussen « the landlord » en « the tenant ».",
          "De landlord is de eigenaar die verhuurt, de tenant is de huurder die huur betaalt.",
          "Verhuurder tegenover huurder."),
]
