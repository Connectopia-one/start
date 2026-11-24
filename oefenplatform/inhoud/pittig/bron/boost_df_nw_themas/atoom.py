"""atoom — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Hergebruikt de pittige vragen van natuurwetenschappen 🚀 Boost doorstroom (met
hun prenten), zonder wat de fiche van de dubbele finaliteit niet vraagt."""
from ..boost_do_nw_themas import atoom as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [i for i in range(len(N.VRAGEN)) if i != 17])
VRAGEN += [
    tabel("Klopt dit over de elektronenconfiguratie volgens Bohr?",
          [("Natrium heeft 2 elektronen op de eerste schil, 8 op de tweede en 1 op de derde.", J), ("Het aantal valentie-elektronen bepaalt veel van de eigenschappen.", J), ("In het elektron-stipmodel teken je alle elektronen van het atoom.", F)],
          "In het elektron-stipmodel teken je enkel de valentie-elektronen rond het symbool."),
]
