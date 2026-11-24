"""Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom die binnen nl_bronnen van dubbele finaliteit passen, zonder de vragen over begrippen die daar niet in staan."""
from ..beyond_nederlands_themas import bronnen as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22])
VRAGEN += [
    mk("Je zoekt informatie over een nieuwe regel voor het rijbewijs. Welke bron raadpleeg je het eerst?",
       ["de officiële site van de overheid", "een filmpje van een onbekende influencer", "een reactie onder een krantenartikel", "een bericht dat een vriend doorstuurde"], 0,
       "Een officiële bron is de oorspronkelijke afzender van de regel."),
]
