"""Geosfeer en platentektoniek — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom over de geosfeer en de platentektoniek."""
from ..beyond_ak_themas import geosfeer as _B, platentektoniek as _P
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[10, 15, 17, 21, 28]) + kies(_P.VRAGEN, enkel=[1, 2, 7, 9, 21])
