"""Argumentatie, feiten en meningen, en drogredenen — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom die binnen nl_argumentatie van dubbele finaliteit passen, zonder de vragen over begrippen die daar niet in staan."""
from ..beyond_nederlands_themas import argumentatie as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
VRAGEN += [
    koppel("Welke drogreden zit in elke uitspraak?", [
        ["\"Dat zegt iemand die zelf nooit op tijd komt.\"", "persoonlijke aanval"],
        ["\"Een bekende zanger zegt het, dus het klopt.\"", "beroep op een autoriteit"],
        ["\"Als we dit toelaten, mag straks alles.\"", "hellend vlak"],
        ["\"Dit is waar, want het is gewoon zo.\"", "cirkelredenering"],
    ], ["feit"], "Vier drogredenen die op een argument lijken maar niets bewijzen."),
]
