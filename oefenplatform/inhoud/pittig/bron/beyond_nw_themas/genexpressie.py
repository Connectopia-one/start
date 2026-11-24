"""Genexpressie en DNA-technologie — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt.
"""
from ..beyond_bio_themas import genexpressie as G, dnatechnologie as T, mutaties as M

VRAGEN = (
    [G.VRAGEN[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 22, 23, 25)]
    + [M.VRAGEN[i] for i in (5, 8)]
    + [T.VRAGEN[i] for i in (0, 1, 2, 3, 8, 12, 18)]
)
