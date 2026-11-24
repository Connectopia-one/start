"""Atmosfeer — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom plus één eigen vraag."""
from ..beyond_ak_themas import atmosfeer as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[12]) + [
    tabel("Breedteligging, hoogteligging of ligging tegenover de zee?", [
        ("het is in Quito, op de evenaar maar hoog in de Andes, mild", "hoogteligging"),
        ("in Oslo is het gemiddeld kouder dan in Rome", "breedteligging"),
        ("in Brest zijn de winters zachter dan in Warschau", "ligging tegenover de zee"),
    ], "Drie geografische factoren voor de temperatuur.",
       kolommen=["breedteligging", "hoogteligging", "ligging tegenover de zee"]),
]
