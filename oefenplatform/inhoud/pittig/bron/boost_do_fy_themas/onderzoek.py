"""Veilig werken, meten en onderzoek — pittig (🚀 Boost doorstroom, fysica).

Vragen over veilig werken in het labo, verbanden in grafieken en de stappen van onderzoek en ontwerp van natuurwetenschappen Boost doorstroom (met hun prenten)."""
from ..boost_do_nw_themas import onderzoek as O, veilig as V
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(O.VRAGEN, [11, 12, 13, 14, 15, 16, 18, 19, 22, 23, 24, 25, 27]) + kies(V.VRAGEN, [0, 1, 2, 5, 10, 16, 19, 23])
VRAGEN += [
    casus("Jonas onderzoekt of de lengte van een slinger invloed heeft op de tijd van één slingering. Hij meet bij vier lengtes telkens de tijd voor tien slingeringen en deelt door tien.", [
        koppel("Welke variabele is dit?",
               [("de lengte van de slinger", "onafhankelijke variabele"), ("de tijd van één slingering", "afhankelijke variabele"), ("de massa van het gewichtje", "constante variabele")],
               ["hypothese", "besluit"], "Wat je instelt, wat je meet en wat je gelijk houdt."),
        mk("Waarom meet Jonas tien slingeringen en deelt hij door tien?",
           ["Zo weegt de fout bij starten en stoppen minder door.", "Omdat één slingering te snel gaat om ooit te kunnen meten.", "Omdat de slinger na tien keer vanzelf stilvalt.", "Zo hoeft hij de lengte van de slinger niet te meten."], 0,
           "De reactietijd telt maar één keer mee, verdeeld over tien slingeringen."),
        tabel("Klopt dit over de proef van Jonas?",
              [("Hij zet de lengte op de horizontale as.", J), ("Hij verandert bij elke meting ook het gewichtje.", F), ("Hij herhaalt elke meting een paar keer.", J)],
              "Een eerlijke proef verandert één ding tegelijk."),
    ]),
    mk("Een leerling besluit na één meting: 'Zwaardere voorwerpen vallen sneller.' Wat is het grootste probleem?",
       ["Eén meting is te weinig om een besluit op te bouwen.", "Hij heeft het in het verkeerde lokaal gemeten.", "Hij gebruikte geen wetenschappelijke notatie.", "Een besluit mag nooit over vallende voorwerpen gaan."], 0,
       "Herhalen en meerdere voorwerpen vergelijken is nodig; in vacuüm vallen ze zelfs even snel."),
    tabel("Klopt dit over een goed onderzoek?",
          [("Een hypothese moet je kunnen toetsen.", J), ("Een resultaat dat je hypothese tegenspreekt, laat je weg.", F), ("Je beschrijft je werkwijze zodat anderen het kunnen herhalen.", J)],
          "Ook een verworpen hypothese is een geldig resultaat."),
    sleep("In een onderzoek stel je eerst een [[onderzoeksvraag]] en een [[hypothese]] op. Na de metingen trek je een [[besluit]].",
          ["grafiek", "eenheid"], "De stappen van een onderzoek."),
    tabel("Wat hoort in de reflectie van een onderzoeksverslag?",
          [("hoe betrouwbaar je resultaat is", J), ("wat je de volgende keer anders zou doen", J), ("hoeveel het materiaal gekost heeft", F)],
          "In de reflectie kijk je kritisch terug op je werkwijze."),
]
