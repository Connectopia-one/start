"""Pittig (🚀 Boost doorstroom, fysica): dezelfde pittige vragen als bij natuurwetenschappen Boost doorstroom (met hun prenten), omdat de leerstof van dit thema in beide vakken gelijk is."""
from ..boost_do_nw_themas import energie as N
from ._kies import kies

VRAGEN = kies(N.VRAGEN, list(range(len(N.VRAGEN))))
