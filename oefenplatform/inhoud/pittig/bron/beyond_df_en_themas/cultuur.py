"""De Engelstalige wereld: gewoontes, landen en reizen — pittig (Engels, Beyond dubbele finaliteit), A2+."""
from ..beyond_en_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Read Lien's message from London.\n\n« Hi Mum! I arrived by train yesterday. The weather is lovely, so everybody is talking about it! "
        "My B&B is small but clean, and breakfast is included. This morning I took a sightseeing tour on an open bus. "
        "In the shops I pay in pounds, so I'm glad I changed some money. Tomorrow I'm going on a day trip to the seaside. See you in a fortnight! »",
        [
            keuze("Lien slaapt in een kamer [[*met ontbijt|zonder ontbijt]].", "B&B en breakfast is included."),
            keuze("Lien komt terug over [[*twee weken|veertien dagen na kerst|een week]].", "A fortnight: twee weken."),
            keuze("Iedereen praat over het weer. Dat is in het Verenigd Koninkrijk [[*gewoon|onbeleefd]].", "Small talk over het weer is een vriendelijke opening."),
            mk("Waar gaat Lien morgen naartoe?",
               ["naar de kust", "naar het platteland in Wales", "naar het centrum van Londen", "naar het buitenland met de trein"], 0,
               "The seaside is de kust."),
            mk("Waarom is Lien blij dat ze geld wisselde?",
               ["Ze betaalt er met ponden.", "Ze betaalt er met euro's in de winkels.", "De bus is er heel duur voor toeristen.", "Haar B&B vraagt een borg in dollars."], 0,
               "In the shops I pay in pounds."),
        ],
    ),
    tabel("Klopt dit over de Engelstalige wereld?", [
        ("In Ierland betaal je met de euro.", J), ("Glasgow is de hoofdstad van Schotland.", F),
        ("In de VS geef je in een restaurant meestal een fooi.", J), ("Great Britain is hetzelfde als het Verenigd Koninkrijk.", F),
    ], "Edinburgh is de hoofdstad; Noord-Ierland hoort niet bij Great Britain."),
    sorteer("Brits of Amerikaans?", ["Brits", "Amerikaans"], [
        ["Thanksgiving in november", "Amerikaans"], ["Boxing Day", "Brits"], ["the NHS", "Brits"],
        ["freshman year", "Amerikaans"], ["a one-way ticket", "Amerikaans"], ["a bank holiday", "Brits"],
    ], "Elk land heeft zijn eigen gewoontes en woorden."),
    koppel("Koppel elk woord aan zijn betekenis.", [
        ["luggage", "bagage"], ["abroad", "in het buitenland"], ["a delay", "een vertraging"], ["the border", "de grens"],
    ], ["het perron"], "Platform is het perron."),
    koppel("Koppel elk reiswoord aan zijn betekenis.", [
        ["a coach", "een reisbus"], ["a city break", "een korte stadsreis"], ["accommodation", "een verblijf"], ["a seaside resort", "een badplaats"],
    ], ["een braadpan"], "A frying pan is een braadpan en hoort in de keuken."),
    inv("Welke stad is de hoofdstad van Noord-Ierland? Eén woord.", ["Belfast"], "Belfast."),
    mk("Je wil van Londen naar Brighton en weer terug. Welk ticket vraag je?",
       ["a return ticket", "a single ticket", "a one-way ticket to Brighton", "a boarding pass for Brighton"], 0,
       "Heen en terug: a return."),
    mk("Hoe zeg je « We gaan met de bus naar school »?",
       ["We go to school by bus.", "We go to school with the bus.", "We go with bus to the school.", "We go to school on the bus by."], 0,
       "By bus, zonder lidwoord."),
    mk("Hoe zeg je « Ik ga te voet »?",
       ["I go on foot.", "I go by foot.", "I go with the foot.", "I go by the feet."], 0, "On foot, niet by."),
    mk("Een Amerikaan schrijft « 04/07/2027 ». Welke datum bedoelt hij?",
       ["7 april 2027", "4 juli 2027", "7 juli 2027", "4 april 2027 of 4 juli"], 0, "In de VS komt de maand eerst."),
    mk("Een verkeersbord in Engeland toont « 30 ». Wat betekent dat?",
       ["30 mijl per uur", "30 kilometer per uur", "30 meter tot het kruispunt", "30 minuten parkeren"], 0,
       "Snelheid in miles per hour."),
    mk("Je zit in een pub in Engeland. Hoe bestel je meestal?",
       ["aan de toog, en je betaalt meteen", "aan tafel, en je betaalt bij het weggaan", "via een ober die je wenkt", "telefonisch vooraf"], 0,
       "In een pub bestel je aan de toog."),
    mk("Je bent in de VS en de rekening is 40 dollar. Wat is een gewone fooi?",
       ["6 à 8 dollar", "geen fooi", "40 dollar extra", "1 dollar, meer niet"], 0, "Vijftien tot twintig procent."),
    inv("Hoe noem je een inwoner van Schotland in het Engels? Eén woord.", ["Scot", "a Scot", "Scotsman"], "A Scot."),
    inv("Hoeveel landen vormen samen het Verenigd Koninkrijk? Geef het getal.", ["4", "vier"],
        "Engeland, Schotland, Wales en Noord-Ierland."),
    inv("Hoe zeg je koffer in het Engels? Eén woord.", ["suitcase"], "A suitcase."),
    inv("Hoe zeg je platteland in het Engels? Twee woorden met the.", ["the countryside"], "The countryside."),
    keuze("« We booked [[*a room|a book]] in a small hotel. »", "To book a room: een kamer reserveren."),
    keuze("« We need a lot of [[*luggage|luggages]] for this trip. »", "Luggage is ontelbaar."),
    keuze("« Last summer we went [[*abroad|to abroad]] for the first time. »", "To go abroad, zonder voorzetsel."),
    keuze("« The train had a long [[*delay|journey]], so we arrived two hours late. »", "A delay: een vertraging."),
    keuze("Op Boxing Day, [[*26 december|25 december|1 januari]], is het in het Verenigd Koninkrijk een vrije dag.", "De dag na Kerstmis."),
    tabel("Hoort dit bij lichaamstaal?", [
        ("iemand aankijken als je spreekt", J), ("de woorden die je kiest", F), ("met je armen gekruist staan", J),
    ], "Lichaamstaal zegt iets zonder woorden."),
    sleep("We took the [[ferry]] from Calais to Dover. At the [[border]] we showed our passports.",
          ["platform", "cottage"], "Een veerboot steekt het water over; aan de grens toon je je paspoort."),
    volgorde("Zet de stappen van een vliegreis in de juiste volgorde.", [
        "book a ticket", "pack your suitcase", "go to the airport", "show your boarding pass", "get on the plane",
    ], "Eerst boeken, dan inpakken, dan naar de luchthaven en instappen."),
    open_("Noem in het Nederlands één verschil tussen een Britse en een Vlaamse school.",
          "Op veel Britse scholen dragen de leerlingen een uniform, in Vlaanderen bijna nooit.",
          "Een uniform is in het Verenigd Koninkrijk heel gewoon."),
]
