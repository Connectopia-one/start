"""Mengsels, zuivere stoffen en scheidingstechnieken — pittig (🚀 Boost doorstroom, chemie).

Dezelfde pittige vragen als bij natuurwetenschappen Boost doorstroom (met hun prenten): de leerstof over mengsels is in beide vakken gelijk."""
from ..boost_do_nw_themas import mengsels as N
from ._kies import kies

VRAGEN = kies(N.VRAGEN, list(range(len(N.VRAGEN))))
