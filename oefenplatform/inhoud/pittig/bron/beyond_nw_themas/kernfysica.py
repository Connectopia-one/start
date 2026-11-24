"""Kernfysica en radioactiviteit — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen fysica Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt:
nucliden, isotopen, stabiliteit, halveringstijd, verval, splijting en fusie,
soorten straling en bescherming.
"""
from ..beyond_fys_themas import kern as K, straling as S

VRAGEN = (
    [K.VRAGEN[i] for i in (0, 1, 2, 3, 5, 6, 7, 9, 11, 12, 14, 15, 16, 17, 20, 21, 23, 24, 26)]
    + [S.VRAGEN[i] for i in (4, 5, 14, 15, 16, 18, 27)]
)
