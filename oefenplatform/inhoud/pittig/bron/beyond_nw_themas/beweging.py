"""Kracht en beweging — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen fysica Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt.
"""
from ..beyond_fys_themas import beweging as B, newton as N

VRAGEN = (
    [B.VRAGEN[i] for i in (0, 1, 2, 5, 6, 7, 10, 21, 22, 25, 26)]
    + [N.VRAGEN[i] for i in (0, 1, 2, 3, 4, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26)]
)
