"""Voortplanting, zwangerschap en vruchtbaarheid — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt.
"""
from ..beyond_bio_themas import bevruchting as B, gametogenese as G, vruchtbaarheid as V

VRAGEN = (
    [B.VRAGEN[i] for i in (0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 22, 23, 25, 26, 27)]
    + [G.VRAGEN[i] for i in (4, 5)]
    + [V.VRAGEN[i] for i in (3, 5, 6, 8)]
)
