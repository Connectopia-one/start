"""onderzoek — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Hergebruikt de pittige vragen van natuurwetenschappen 🚀 Boost doorstroom (met
hun prenten), zonder wat de fiche van de dubbele finaliteit niet vraagt."""
from ..boost_do_nw_themas import onderzoek as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [i for i in range(len(N.VRAGEN)) if i != 3])
VRAGEN += [
    tabel("Welk verband zie je in de tabel?",
          [("massa 1, 2, 3 kg en zwaartekracht 10, 20, 30 N", "recht evenredig"), ("aantal arbeiders 2, 4, 8 en duur 12, 6, 3 dagen", "omgekeerd evenredig"), ("leeftijd 10, 20, 30 jaar en schoenmaat 34, 42, 42", "geen van beide")],
          "Recht evenredig: het quotiënt blijft gelijk; omgekeerd evenredig: het product blijft gelijk.",
          ["recht evenredig", "omgekeerd evenredig", "geen van beide"]),
]
