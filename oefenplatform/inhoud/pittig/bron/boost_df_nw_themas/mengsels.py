"""mengsels — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Hergebruikt de pittige vragen van natuurwetenschappen 🚀 Boost doorstroom (met
hun prenten), zonder wat de fiche van de dubbele finaliteit niet vraagt."""
from ..boost_do_nw_themas import mengsels as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, list(range(len(N.VRAGEN))))
