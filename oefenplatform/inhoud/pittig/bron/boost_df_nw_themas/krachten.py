"""Kracht als vector en bewegingstoestand — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Pittige vragen van natuurwetenschappen 🚀 Boost doorstroom zonder vrije val,
worp en veerconstante, plus eigen vragen over de vier kenmerken van een kracht,
het samenstellen van krachten en het traagheidsbeginsel in het verkeer."""
from ..boost_do_nw_themas import krachten as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 11, 12, 13, 14, 18, 23, 24, 25, 26])
VRAGEN += [
    casus("Een bus rijdt met 50 km/h en remt plots hard. Een staande passagier valt naar voren. In de koffer schuift een losse valies tegen de achterbank.", [
        tabel("Klopt dit over de passagier?",
              [("De passagier wil door zijn traagheid verder bewegen.", J), ("Een kracht duwt de passagier naar voren.", F), ("Een gordel of een handgreep geeft de kracht om mee te vertragen.", J)],
              "Zonder kracht blijft een voorwerp bewegen zoals het bewoog."),
        mk("In welke zin werkt de resulterende kracht op de bus tijdens het remmen?",
           ["tegen de rijrichting", "in de rijrichting", "loodrecht omhoog", "er werkt dan geen kracht"], 0,
           "Vertragen vraagt een kracht tegen de beweging in."),
        tabel("Waarom moet de lading van een vrachtwagen goed vastzitten?",
              [("Door haar traagheid schuift ze bij het remmen door.", J), ("Een zware lading heeft meer traagheid.", J), ("Vastmaken is enkel nodig bij lichte lading.", F)],
              "Hoe groter de massa, hoe groter de traagheid."),
    ]),
    tabel("Welk kenmerk van de kracht verandert hier?",
          [("Je duwt harder tegen de kar.", "grootte"), ("Je duwt de kar naar links in plaats van naar rechts, op dezelfde lijn.", "zin"), ("Je duwt niet meer horizontaal maar schuin naar beneden.", "richting"), ("Je duwt bovenaan in plaats van onderaan de kar.", "aangrijpingspunt")],
          "Een kracht heeft vier kenmerken: grootte, richting, zin en aangrijpingspunt.",
          ["grootte", "richting", "zin", "aangrijpingspunt"]),
    inv("Twee krachten van 120 N en 50 N werken op hetzelfde punt, op één lijn, in tegengestelde zin. Hoe groot is de resultante in newton?", ["70", "70 N"],
        "120 − 50 = 70 N, in de zin van de grootste kracht."),
    inv("Twee krachten van 9 N en 12 N werken loodrecht op elkaar in hetzelfde punt. Hoe groot is de resultante in newton?", ["15", "15 N"],
        "√(81 + 144) = √225 = 15 N."),
    sorteer("Wat doet de resulterende kracht met de beweging?", ["verandert de beweging", "verandert de beweging niet"],
            [("de resultante is nul", "verandert de beweging niet"), ("een fietser trapt harder dan de wrijving", "verandert de beweging"), ("een auto rijdt met constante snelheid rechtdoor", "verandert de beweging niet"), ("een bal wordt opzij getrapt", "verandert de beweging"), ("een boek ligt stil op de tafel", "verandert de beweging niet")],
            "Een resulterende kracht doet versnellen, vertragen of van richting veranderen."),
    tabel("Klopt dit over remmen op een natte weg?",
          [("De wrijvingskracht tussen band en weg is kleiner.", J), ("De remafstand wordt langer.", J), ("Een zwaardere vrachtwagen stopt even snel met dezelfde remkracht.", F)],
          "Minder wrijving en meer massa betekenen een langere remweg."),
    koppel("Welke kracht hoort bij welke omschrijving?",
           [("zwaartekracht", "de aarde trekt aan een voorwerp, zonder contact"), ("normaalkracht", "een oppervlak duwt loodrecht terug"), ("wrijvingskracht", "werkt de beweging langs een oppervlak tegen"), ("stuwkracht", "duwt een raket of vliegtuig vooruit")],
           ["veerconstante"], "Elke kracht heeft haar eigen oorzaak."),
    mk("Een skydiver met open scherm daalt aan 5 m/s, elke seconde even snel. Wat geldt voor de krachten op hem?",
       ["Luchtweerstand en zwaartekracht zijn even groot.", "De zwaartekracht op hem is volledig verdwenen.", "De luchtweerstand is veel groter dan de zwaartekracht.", "Er werkt geen enkele kracht meer op de skydiver."], 0,
       "Constante snelheid: de resulterende kracht is nul."),
    sleep("Een schaatser glijdt over glad ijs en remt bijna niet af, omdat de [[wrijvingskracht]] heel klein is. Door haar [[traagheid]] blijft ze bewegen. Om te stoppen heeft ze een kracht [[tegen]] de beweging in nodig.",
          ["zwaartekracht", "mee"], "Het traagheidsbeginsel in actie."),
    tabel("Een kist staat stil op een helling. Welke krachten werken erop?",
          [("de zwaartekracht", J), ("de normaalkracht van de helling", J), ("de wrijvingskracht die wegglijden tegenhoudt", J), ("een stuwkracht naar boven", F)],
          "Stilstand: de krachten heffen elkaar op."),
    tabel("Welke krachten werken op een vliegtuig dat op gelijke hoogte en met constante snelheid vliegt?",
          [("de stuwkracht naar voren", J), ("de luchtweerstand naar achteren", J), ("de zwaartekracht naar beneden", J), ("een resulterende kracht naar voren", F)],
          "Constante snelheid op gelijke hoogte: alle krachten heffen elkaar op."),
    keuze("Het gewicht van een voorwerp meet je in [[*newton|kilogram|meter]].",
          "Gewicht is een kracht; massa meet je in kilogram."),
    inv("Drie kinderen duwen een kar in dezelfde zin met 40 N, 35 N en 25 N. Hoe groot is de resultante in newton?", ["100", "100 N"],
        "Zelfde richting en zin: optellen."),
    mk("Waarom draag je in de auto een gordel?",
       ["Door je traagheid schiet je anders door.", "De gordel maakt je lichaam een stuk lichter.", "De gordel verhoogt de zwaartekracht op je.", "Zonder gordel rijdt de auto altijd trager."], 0,
       "De gordel geeft de kracht die jou samen met de auto doet vertragen."),
]
