"""Veilig en duurzaam werken, meten, grootheden en eenheden — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Overgenomen uit de pittige vragen chemie, biologie en fysica Beyond (zelfde
leerstof, zelfde prenten): pictogrammen en H- en P-zinnen, veilig en duurzaam
werken, meetinstrumenten aflezen, beduidende cijfers, voorvoegsels,
SI-eenheden en verbanden.
"""
from ..beyond_chem_themas import veilig as C
from ..beyond_bio_themas import veilig as B
from ..beyond_fys_themas import meten as F

VRAGEN = (
    [C.VRAGEN[i] for i in (0, 1, 2, 3, 7, 8, 9, 10, 11, 12, 14, 15, 16, 21)]
    + [B.VRAGEN[i] for i in (6, 7, 10, 13, 26)]
    + [F.VRAGEN[i] for i in (0, 1, 2, 4, 5, 6, 8, 18, 20, 26, 27)]
)
