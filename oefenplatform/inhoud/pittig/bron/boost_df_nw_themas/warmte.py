"""Warmte, faseovergangen en inwendige energie — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Pittige vragen van natuurwetenschappen 🚀 Boost doorstroom zonder de
specifieke warmtecapaciteit, de latente warmte en het warmtetransport, plus
eigen vragen over warmte tegenover temperatuur, inwendige energie en cohesie."""
from ..boost_do_nw_themas import warmte as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 3, 8, 12, 13, 14, 18, 19, 24])
VRAGEN += [
    casus("Een badkuip met 150 liter water van 35 °C en een kopje met 0,2 liter thee van 80 °C.", [
        tabel("Klopt dit over het bad en de thee?",
              [("De thee heeft de hoogste temperatuur.", J), ("Het badwater bevat de meeste inwendige energie.", J), ("Een hogere temperatuur betekent altijd meer warmte.", F)],
              "Temperatuur is een maat voor de beweging van de deeltjes; de hoeveelheid stof telt mee voor de inwendige energie."),
        mk("Je zet het kopje op de rand van het bad. Wat gebeurt er na een uur?",
           ["De thee is afgekoeld naar de omgeving.", "Het bad is even warm als de thee geworden.", "De thee is opgewarmd tot 80 °C en meer.", "Er verandert niets aan de temperatuur."], 0,
           "Warmte gaat van warm naar koud tot thermisch evenwicht."),
    ]),
    sorteer("Bij welke faseovergang neemt een stof warmte op en bij welke geeft ze warmte af?", ["neemt op", "geeft af"],
            [("smelten", "neemt op"), ("stollen", "geeft af"), ("verdampen", "neemt op"), ("condenseren", "geeft af"), ("sublimeren", "neemt op"), ("desublimeren", "geeft af")],
            "Naar een minder geordende fase kost warmte; terug geeft warmte vrij."),
    koppel("Welke faseovergang zie je?",
           [("rijp op het gras na een koude nacht", "desublimeren"), ("een ijsblokje in je drank", "smelten"), ("droogijs dat dampt", "sublimeren"), ("druppels op een koud blikje", "condenseren")],
           ["stollen"], "Zes faseovergangen tussen vast, vloeibaar en gas."),
    tabel("Klopt dit over cohesiekrachten?",
          [("Ze houden de deeltjes van een stof bij elkaar.", J), ("Ze zijn het sterkst in een vaste stof.", J), ("In een gas zijn ze het sterkst.", F)],
          "In een gas bewegen de deeltjes vrij, de cohesie is er bijna weg."),
    mk("Je stookt het vuur onder een pot kokend water hoger. Wat gebeurt er met de temperatuur van het water?",
       ["Ze blijft 100 °C.", "Ze stijgt tot ver boven 100 °C.", "Ze daalt, want er verdampt meer water.", "Ze stijgt elke minuut met één graad."], 0,
       "Tijdens het koken gaat extra warmte naar het verdampen, niet naar een hogere temperatuur."),
    casus("Je mengt 2 liter water van 20 °C met 2 liter water van 60 °C in een goed geïsoleerde kan.", [
        inv("Wat wordt de eindtemperatuur, in °C?", ["40", "40 °C"],
            "Evenveel water: de eindtemperatuur ligt precies in het midden."),
        tabel("Klopt dit over de warmtebalans?",
              [("De warme helft geeft evenveel warmte af als de koude opneemt.", J), ("Ze steunt op de wet van behoud van energie.", J), ("Er gaat warmte verloren in een perfecte isolatie.", F)],
              "Afgegeven warmte = opgenomen warmte."),
    ]),
    tabel("Klopt dit over het smelten van ijs bij 0 °C?",
          [("De temperatuur blijft 0 °C tot al het ijs gesmolten is.", J), ("De inwendige energie stijgt tijdens het smelten.", J), ("De deeltjes komen los uit hun vaste plaats.", J), ("De temperatuur stijgt tijdens het smelten.", F)],
          "Alle warmte gaat naar het losmaken van de deeltjes."),
    volgorde("Rangschik de fasen van water van laagste naar hoogste inwendige energie, bij dezelfde massa.",
             ["ijs van −10 °C", "ijs van 0 °C", "water van 0 °C", "water van 100 °C", "stoom van 100 °C"],
             "Opwarmen en faseovergangen naar vloeistof en gas verhogen de inwendige energie."),
    tabel("Gaat deze uitspraak over warmte of over temperatuur?",
          [("meet je met een thermometer", "temperatuur"), ("is energie die overgaat door een temperatuurverschil", "warmte"), ("druk je uit in joule", "warmte"), ("druk je uit in graden Celsius", "temperatuur")],
          "Warmte is energie in beweging, temperatuur een maat voor de beweging van de deeltjes.", ["warmte", "temperatuur"]),
    mk("Een auto heeft een koelsysteem met water rond de motor. Wat doet dat water?",
       ["Het voert warmte van de motor af.", "Het brengt extra brandstof naar de motor.", "Het maakt de motor zwaarder en stabieler.", "Het zet warmte om in elektrische energie."], 0,
       "Water neemt veel warmte op en brengt die naar de radiator."),
    sleep("Zweet koelt je af doordat het [[verdampt]]. Daarvoor neemt het [[warmte]] op uit je huid. In vochtige lucht verdampt het [[trager]] en koel je minder goed af.",
          ["condenseert", "sneller"], "Verdampen kost warmte."),
    keuze("Een stof die stolt, [[*geeft warmte af aan|neemt warmte op uit|wisselt geen warmte uit met]] haar omgeving.",
          "Daarom beregenen fruitboeren hun bomen bij nachtvorst."),
    inv("Een smeltcurve toont een vlak stuk van minuut 4 tot minuut 11. Hoeveel minuten duurt het smelten?", ["7", "7 minuten"],
        "11 − 4 = 7 minuten blijft de temperatuur gelijk."),
    tabel("Klopt dit over de zee en het klimaat?",
          [("Aan de kust is het in de winter zachter dan in het binnenland.", J), ("Zeewater geeft zijn warmte traag en lang af.", J), ("De zee warmt in de zomer sneller op dan het land.", F)],
          "Water warmt traag op en koelt traag af."),
    tabel("Klopt dit over een brandwonde?",
          [("Je houdt ze onder koud stromend water.", J), ("Het stromende water blijft warmte uit de huid wegnemen.", J), ("IJs rechtstreeks op de wonde is altijd het best.", F)],
          "Lauw tot koel stromend water, geen ijs."),
    casus("Een fles frisdrank van 25 °C gaat in een koelbox met veel ijsblokjes van 0 °C.", [
        tabel("Klopt dit over de fles in de koelbox?",
              [("De frisdrank geeft warmte af aan het ijs.", J), ("Het ijs smelt en blijft daarbij 0 °C.", J), ("Het ijs geeft koude af aan de fles.", F)],
              "Er bestaat geen 'koude' die stroomt: warmte gaat van warm naar koud."),
        mk("Waarom blijft de frisdrank zo lang koud?",
           ["Het smeltende ijs neemt warmte op.", "Ijs maakt de fles dikker.", "De koelbox maakt zelf kou aan.", "De frisdrank verliest al haar suiker."], 0,
           "Smelten kost warmte zonder dat de temperatuur stijgt."),
    ]),
    keuze("Temperatuur hangt samen met de [[*kinetische energie|massa|kleur]] van de deeltjes.",
          "Hoe sneller de deeltjes bewegen, hoe hoger de temperatuur."),
]
