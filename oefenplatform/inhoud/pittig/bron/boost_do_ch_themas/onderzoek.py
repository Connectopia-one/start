"""Veilig werken, meten en onderzoek — pittig (🚀 Boost doorstroom, chemie).

Dezelfde soort vragen als bij natuurwetenschappen Boost doorstroom (glaswerk, pictogrammen, H- en P-zinnen, eenheden, beduidende cijfers en de onderzoeksstappen), met hun prenten."""
from ..boost_do_nw_themas import veilig as V, onderzoek as O
from ._kies import kies

VRAGEN = kies(V.VRAGEN, [0, 1, 2, 5, 6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 23, 24, 25, 26]) + kies(O.VRAGEN, [5, 6, 7, 8, 12, 13, 14, 17, 18, 21, 25, 27])
