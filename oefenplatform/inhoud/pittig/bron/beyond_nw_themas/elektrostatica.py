"""Elektrostatica — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen fysica Beyond (zelfde leerstof, zelfde
prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen valt
(geen rekenwerk met de elementaire lading of de veldsterkte).
"""
from ..beyond_fys_themas import lading as L, veld as V

VRAGEN = (
    [L.VRAGEN[i] for i in range(28) if i not in (10, 11, 12, 23)]
    + [V.VRAGEN[i] for i in (10, 11, 12, 24)]
)
