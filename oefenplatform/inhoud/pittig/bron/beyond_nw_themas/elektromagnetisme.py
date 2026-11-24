"""Elektromagnetisme en inductie — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen fysica Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt
(geen rekenwerk met B, flux of transformatoren).
"""
from ..beyond_fys_themas import magneet as M, magkracht as K, inductie as I

VRAGEN = (
    [M.VRAGEN[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20, 21, 22, 23, 24, 25, 26, 27)]
    + [K.VRAGEN[i] for i in (4, 5, 16)]
    + [I.VRAGEN[i] for i in (6, 7, 8, 21, 25)]
)
