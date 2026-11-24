"""Chemische bindingen en roosters — pittig (🚀 Boost doorstroom, chemie).

Pittige vragen over bindingen, Lewisstructuren en roosters van natuurwetenschappen Boost doorstroom (met hun prenten); het oxidatiegetal en binair/ternair staan bij de naamgeving."""
from ..boost_do_nw_themas import binding as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [i for i in range(len(N.VRAGEN)) if i not in (14, 15)])
VRAGEN += [
    sorteer("Ionbinding, atoombinding of metaalbinding?", ["Ionbinding", "Atoombinding", "Metaalbinding"],
            [("MgO", "Ionbinding"), ("CO₂", "Atoombinding"), ("Cu", "Metaalbinding"), ("KCl", "Ionbinding"), ("NH₃", "Atoombinding"), ("Al", "Metaalbinding")],
            "Metaal met niet-metaal geeft een ionbinding, twee niet-metalen een atoombinding, metaalatomen onder elkaar een metaalbinding."),
    mk("Waarom is koper plooibaar, maar breekt een kristal keukenzout als je erop slaat?",
       ["Metaallagen schuiven over elkaar; in een ionrooster stoten gelijke ladingen af.", "Koper heeft een hoger smeltpunt dan keukenzout en wordt nooit bros.", "Keukenzout bevat moleculen die bij een slag uit elkaar vallen.", "In koper zitten geen elektronen, zodat de atomen vrij kunnen bewegen."], 0,
       "Schuift een ionrooster een laag op, dan komen plus naast plus te liggen en splijt het."),
]
