"""Taalvariëteiten, registers en beleefdheid — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom die binnen nl_varieteiten van dubbele finaliteit passen, zonder de vragen over begrippen die daar niet in staan."""
from ..beyond_nederlands_themas import varieteiten as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
VRAGEN += [
    tabel("Standaardtaal, tussentaal of dialect?", [
        ("\"Ik heb dat niet gezien.\"", "standaardtaal"), ("\"Ik heb da ni gezien, zenne.\"", "tussentaal"),
        ("\"\'k Ei da nie gezien.\" in de streektaal van een dorp", "dialect"),
    ], "Tussentaal ligt tussen de standaardtaal en het dialect in.", kolommen=["standaardtaal", "tussentaal", "dialect"]),
]
