"""DNA, replicatie en celdelingen — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt.
"""
from ..beyond_bio_themas import dna as D, celdeling as C

VRAGEN = (
    [D.VRAGEN[i] for i in (0, 1, 2, 3, 6, 7, 8, 9, 10, 16, 18, 19, 22, 23, 24, 25)]
    + [C.VRAGEN[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 20, 22)]
)
