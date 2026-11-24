"""Bijvoeglijke naamwoorden, bijwoorden en voorzetsels — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read the review of a small hotel.\n\n« The Seaview is the cheapest hotel in town, but it is not the worst. "
        "Our room was smaller than the one in the photos, and the bed was hardly comfortable. "
        "The staff were very friendly and always helped us quickly. Breakfast is served at eight o'clock in a lovely old room "
        "next to the garden. The beach is in front of the hotel. Next time we will book a bigger room. »",
        [
            keuze("« the cheapest hotel in town » is een [[*overtreffende trap|vergrotende trap]].", "The + -est: overtreffende trap."),
            keuze("« the bed was hardly comfortable » betekent dat het bed [[*nauwelijks comfortabel|heel comfortabel]] was.",
                  "Hardly betekent nauwelijks."),
            keuze("In « they helped us quickly » is quickly een [[*bijwoord|bijvoeglijk naamwoord]].", "Het zegt hoe ze hielpen."),
            keuze("In « the staff were very friendly » is friendly een [[*bijvoeglijk naamwoord|bijwoord]].",
                  "Friendly eindigt op -ly, maar zegt hoe het personeel is."),
            mk("Waar ligt het strand?",
               ["voor het hotel", "achter de tuin van het hotel", "naast de ontbijtzaal in de tuin", "onder het hotel aan de kust"], 0,
               "In front of betekent voor."),
        ],
    ),
    tabel("Is de trap van vergelijking juist?", [
        ("thin, thinner, the thinnest", J), ("busy, busyer, the busyest", F),
        ("famous, more famous, the most famous", J), ("bad, badder, the baddest", F),
    ], "Busy wordt busier; bad wordt worse, the worst."),
    sorteer("Krijgt het woord -er of more?", ["-er", "more"], [
        ["warm", "-er"], ["dangerous", "more"], ["funny", "-er"], ["interesting", "more"], ["fast", "-er"], ["boring", "more"],
    ], "Korte woorden en woorden op -y krijgen -er; lange woorden krijgen more."),
    mk("« My brother is two years ___ than me. » Welk woord past?",
       ["older", "oldest", "more old", "the most old"], 0, "Than vraagt een vergrotende trap; old is kort: older."),
    mk("« This is ___ day of my life! » Welk woord past?",
       ["the happiest", "the most happy", "happier than", "the more happier"], 0, "Overtreffende trap van happy: the happiest."),
    mk("« Your bag isn't ___ mine. » Mijn tas en jouw tas zijn niet even zwaar. Welke woorden passen?",
       ["as heavy as", "heavier as", "as heavier than", "so heavy than"], 0, "Even ... als: as ... as."),
    inv("Schrijf de overtreffende trap van « far » met the. Twee woorden.", ["the furthest", "the farthest"],
        "Far, further, the furthest."),
    inv("Schrijf de vergrotende trap van « little ». Eén woord.", ["less"], "Little, less, the least."),
    inv("Maak een bijwoord van « careful ». Eén woord.", ["carefully"], "Careful + -ly."),
    inv("Maak een bijwoord van « lucky ». Eén woord.", ["luckily"], "De y wordt ily."),
    keuze("« He speaks English [[*well|good]]. »", "Bij een werkwoord hoort het bijwoord well."),
    keuze("« She is a [[*careful|carefully]] driver. »", "Bij een naamwoord hoort een bijvoeglijk naamwoord."),
    keuze("« We [[*hardly|hard]] slept last night, because the baby cried. »", "Hardly: nauwelijks."),
    keuze("« Prices get [[*higher and higher|more and more high]] every year. »", "Kort woord: higher and higher."),
    tabel("Is deze zin juist (bijvoeglijk naamwoord of bijwoord)?", [
        ("She answered the question correctly.", J), ("He runs very quick.", F),
        ("The music is too loudly.", F), ("They are always on time.", J),
    ], "Bij een werkwoord een bijwoord (quickly); na is een bijvoeglijk naamwoord (loud)."),
    volgorde("Zet de woorden in de juiste volgorde: « bag / leather / a / brown / small »", [
        "a", "small", "brown", "leather", "bag",
    ], "Grootte, kleur, materiaal: a small brown leather bag."),
    mk("Waar staat never? Kies de juiste zin.",
       ["She is never late for school.", "She never is late for school.", "Never she is late for school.", "She is late never for school."], 0,
       "Bij to be staat het bijwoord van frequentie erachter."),
    mk("Waar staat usually? Kies de juiste zin.",
       ["We usually have lunch at noon.", "We have usually lunch at noon.", "Usually we have at noon lunch.", "We have lunch usually at noon."], 0,
       "Het bijwoord van frequentie staat voor het hoofdwerkwoord."),
    koppel("Koppel elk voorzetsel aan de juiste tijd.", [
        ["at", "half past seven"], ["on", "Friday"], ["in", "March"], ["during", "the holidays"],
    ], ["yesterday"], "At + uur, on + dag, in + maand, during + periode. Yesterday krijgt geen voorzetsel."),
    sleep("I am interested [[in]] music and I often listen [[to]] the radio. My sister is very good [[at]] drawing.",
          ["on", "for"], "Vaste voorzetsels: interested in, listen to, good at."),
    tabel("Welk voorzetsel past?", [
        ("It depends ___ the weather.", "on"), ("We arrived ___ Paris at night.", "in"),
        ("I'm waiting ___ my friend.", "for"), ("She was afraid ___ the dog.", "of"),
    ], "Depend on, arrive in (stad), wait for, afraid of.", kolommen=["on", "in", "for", "of"]),
    mk("« The cat is sleeping ___ the sofa and the chair. » Welk voorzetsel past?",
       ["between", "under it", "in front", "next"], 0, "Tussen twee dingen: between."),
    mk("« We stayed at home ___ the rain. » Welke groep past?",
       ["because of", "instead", "in front of", "because"], 0, "Wegens + naamwoord: because of."),
    mk("Waar staat enough? Kies de juiste zin.",
       ["Is your sister old enough to drive?", "Is your sister enough old to drive?", "Is your sister old to drive enough?",
        "Is your sister enough old for driving?"], 0, "Enough staat achter een bijvoeglijk naamwoord."),
    mk("« Of all my friends, Tom lives ___ from school. » Welke vorm past?",
       ["the furthest", "further than", "more far", "the most far away"], 0,
       "Meer dan twee: overtreffende trap met the."),
    open_("Leg in het Nederlands het verschil uit tussen « She worked hard » en « She hardly worked ».",
          "In de eerste zin werkte ze veel en goed, in de tweede werkte ze bijna niet.",
          "Hard is zelf een bijwoord; hardly betekent nauwelijks."),
]
