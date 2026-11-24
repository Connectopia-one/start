"""Kunststoffen, nanomaterialen en duurzame chemie — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen chemie Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt.
"""
from ..beyond_chem_themas import kunststoffen as K, nano as N, duurzaam as D

VRAGEN = (
    [K.VRAGEN[i] for i in (0, 1, 2, 3, 5, 8, 9, 12, 13, 15, 24)]
    + [N.VRAGEN[i] for i in (0, 1, 2, 4, 5, 10, 13, 17, 19, 23)]
    + [D.VRAGEN[i] for i in (0, 1, 2, 3, 6, 8, 10, 11, 12)]
)
