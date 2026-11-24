"""Klimaat nu — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom, met één vraag over de snelheid van klimaatverandering in het verleden."""
from ..beyond_ak_themas import klimaatnu as _B, klimaatgeologisch as _G
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[17]) + kies(_G.VRAGEN, enkel=[12])
VRAGEN[11]["vraag"] = "Draagt dit bij aan het stijgen van de zeespiegel?"
