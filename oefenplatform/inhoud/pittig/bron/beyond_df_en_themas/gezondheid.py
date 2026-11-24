"""Woordvelden gezondheid, natuur en duurzaamheid — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read Ella's message to her teacher.\n\n« Dear Mr Hill,\n\nI'm sorry, but I can't come to school today. I have a sore throat, a bad cough and a fever. "
        "This morning I went to my GP. She gave me a prescription and told me to take it easy for three days. "
        "I will bring a sick note when I come back. Could you send me the homework?\n\nKind regards,\nElla »",
        [
            keuze("Ella heeft [[*keelpijn|buikpijn|hoofdpijn]] en hoest.", "A sore throat: keelpijn."),
            keuze("Ella ging naar [[*haar huisarts|het ziekenhuis|de apotheek]].", "A GP is een huisarts."),
            mk("Wat kreeg Ella van de dokter?",
               ["een voorschrift voor medicijnen", "een pleister voor haar zere hand", "een afspraak in het ziekenhuis", "een briefje voor de sportles"], 0,
               "A prescription."),
            keuze("« take it easy » betekent hier [[*het rustig aan doen|veel sporten]].", "Een vaste uitdrukking."),
            keuze("Ella brengt later [[*een briefje van de dokter|haar huiswerk]] mee naar school.", "A sick note."),
        ],
    ),
    sorteer("Hoort het bij gezondheid of bij het milieu?", ["gezondheid", "milieu"], [
        ["a rash", "gezondheid"], ["pollution", "milieu"], ["a check-up", "gezondheid"],
        ["emissions", "milieu"], ["a ward", "gezondheid"], ["litter", "milieu"],
    ], "Klachten en ziekenhuiswoorden tegenover afval en uitstoot."),
    sorteer("Dier of boom?", ["dier", "boom"], [
        ["a hedgehog", "dier"], ["an oak", "boom"], ["an owl", "dier"], ["a maple", "boom"], ["a squirrel", "dier"],
    ], "Egel, uil en eekhoorn zijn dieren; eik en esdoorn bomen."),
    koppel("Koppel elk woord over natuurrampen aan zijn betekenis.", [
        ["a drought", "droogte"], ["a flood", "een overstroming"], ["a heatwave", "een hittegolf"], ["an earthquake", "een aardbeving"],
    ], ["een briesje"], "A breeze is een briesje."),
    koppel("Koppel elke uitdrukking over gezondheid aan haar betekenis.", [
        ["to feel blue", "zich triest voelen"], ["to put on weight", "bijkomen"], ["to recover", "genezen"], ["to be stressed out", "overspannen zijn"],
    ], ["uitsterven"], "Uitsterven is to go extinct."),
    mk("Hoe zeg je « Ik heb hoofdpijn » in het Engels?",
       ["I have a headache.", "I have pain in my head.", "I have a sore head pain.", "My head has a pain in it."], 0,
       "I have a headache of my head hurts."),
    mk("« After running ten kilometres, I was completely ___. » Wat past?",
       ["exhausted", "lonely and nervous", "crowded", "evergreen"], 0, "Exhausted: uitgeput."),
    mk("Je snijdt in je vinger. Wat heb je nodig?",
       ["a plaster", "a prescription for pills", "a carbon footprint", "a balanced diet"], 0, "A plaster: een pleister."),
    mk("« The dodo ___ a long time ago. » Wat past?",
       ["went extinct", "recovered", "was recycled", "put on weight"], 0, "To go extinct: uitsterven."),
    mk("Welke energie is hernieuwbaar?",
       ["wind", "petrol from the station", "coal from a mine", "gas from the ground"], 0, "Wind raakt niet op."),
    mk("Op een bord in het park staat « Please do not drop litter. » Wat mag je niet doen?",
       ["afval op de grond gooien", "de dieren in het park voederen", "de bomen omhakken", "op het gras lopen"], 0, "Litter: zwerfvuil."),
    inv("Hoe zeg je huiduitslag in het Engels? Eén woord.", ["rash", "a rash"], "A rash."),
    inv("Hoe zeg je uil in het Engels? Eén woord.", ["owl", "an owl"], "An owl."),
    inv("Hoe zeg je ziekenwagen in het Engels? Eén woord.", ["ambulance", "an ambulance"], "An ambulance."),
    inv("Hoe zeg je duurzaam in het Engels? Eén woord.", ["sustainable"], "Sustainable."),
    inv("Hoe zeg je beek in het Engels? Eén woord.", ["stream", "a stream"], "A stream."),
    keuze("« The weather is sunny today, but the [[*climate|weather]] in Spain is warmer than in Belgium over the year. »",
          "Climate is het gemiddelde over jaren."),
    keuze("« There are many [[*species|specieses]] of birds in this forest. »", "Species is enkelvoud én meervoud."),
    keuze("« She has fully [[*recovered|recycled]] from her operation. »", "To recover: genezen."),
    keuze("« A pine tree is [[*evergreen|deciduous only]]: it stays green all year. »", "Evergreen blijft groen."),
    keuze("« Farmers need bees to pollinate their [[*crops|crowds]]. »", "Crops: gewassen."),
    tabel("Is deze zin juist (gezondheid en natuur)?", [
        ("I have a fever and a cough.", J), ("I have pain in my stomach ache.", F),
        ("We should plant more trees.", J), ("This is a very sustainable pollution.", F),
    ], "A stomach ache zonder pain; pollution is nooit duurzaam."),
    tabel("Is dit goed voor het milieu?", [
        ("recycling bottles", J), ("cutting down forests", F), ("using renewable energy", J), ("dropping litter", F),
    ], "Recyclen en hernieuwbare energie helpen; kappen en zwerfvuil niet."),
    sleep("Mental health is about your [[mind]], physical health is about your [[body]].",
          ["tree", "crop"], "Mental: geestelijk; physical: lichamelijk."),
    open_("Geef in het Engels twee dingen die je kan doen om je carbon footprint kleiner te maken.",
          "I can go to school by bike and I can recycle my waste.",
          "Minder uitstoot: fietsen, recyclen, minder vlees, het licht uitdoen."),
    mk("« Rubbish » in het Brits is in de VS ...",
       ["garbage", "litter bin", "a stream", "emissions"], 0, "Rubbish, waste, garbage: afval."),
]
