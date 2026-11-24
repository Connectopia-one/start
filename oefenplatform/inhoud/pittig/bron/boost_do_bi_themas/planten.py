"""Homeostase en waterhuishouding bij planten — pittig (🚀 Boost doorstroom, biologie).

Dezelfde pittige vragen als bij natuurwetenschappen Boost doorstroom (met hun prenten): de leerstof over planten is in beide vakken gelijk."""
from ..boost_do_nw_themas import planten as N
from ._kies import kies

VRAGEN = kies(N.VRAGEN, list(range(len(N.VRAGEN))))
