"""Anorganische stofklassen en naamgeving — pittig (🚀 Boost doorstroom, chemie).

Klikvragen op formulekaarten en vragen over stofklassen, ionen en namen van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen over zuurvormende en basevormende oxiden uit ch_anorganisch."""
from ..boost_do_nw_themas import namen as N, binding as B
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 10, 11, 12, 15, 16, 17, 19, 20, 21, 23, 26, 27, 28]) + kies(B.VRAGEN, [14, 15])
VRAGEN += [
    sorteer("Zuurvormend of basevormend oxide?", ["Zuurvormend", "Basevormend"],
            [("CO₂", "Zuurvormend"), ("CaO", "Basevormend"), ("SO₂", "Zuurvormend"), ("Na₂O", "Basevormend"), ("P₂O₅", "Zuurvormend")],
            "Een niet-metaaloxide vormt met water een zuur, een metaaloxide een hydroxide."),
    mk("Welke naam hoort bij Fe₂O₃ volgens de stocknotatie?",
       ["ijzer(III)oxide", "ijzer(II)oxide", "diijzertrioxide(II)", "ijzeroxide(VI)"], 0,
       "Drie oxide-ionen geven 6−, verdeeld over twee ijzerionen: elk 3+."),
    koppel("Welke formule hoort bij elke naam?",
           [("natriumsulfaat", "Na₂SO₄"), ("calciumcarbonaat", "CaCO₃"), ("kaliumnitraat", "KNO₃"), ("ammoniumchloride", "NH₄Cl")],
           ["NaSO₃", "CaCO₂"], "Zuurrest en metaalion samen, zodat de ladingen elkaar opheffen."),
    tabel("Klopt dit over zuren?",
          [("Een zuur heeft H vooraan in de formule.", J), ("HCl is een binair zuur.", J), ("H₂SO₄ is een binair zuur.", F)],
          "H₂SO₄ bevat drie elementen, dus is het ternair."),
    inv("Welke lading heeft het koperion in CuCl₂?", ["2+", "+2", "2 plus"],
        "Twee chloride-ionen geven 2−, dus koper is 2+: koper(II)chloride."),
    mk("Wat ontstaat er als je calciumoxide in water brengt?",
       ["calciumhydroxide", "calciumcarbonaat", "waterstofchloride", "zuurstofgas en calcium"], 0,
       "Een basevormend oxide plus water geeft een hydroxide: gebluste kalk."),
    sleep("CO₂ lost op in water en vormt [[koolzuur]]. Een oxide van een niet-metaal is dus [[zuurvormend]]. Een oxide van een metaal is [[basevormend]].",
          ["zout", "binair"], "Oxiden reageren met water tot een zuur of een hydroxide."),
    tabel("Tot welke stofklasse hoort de stof?",
          [("KOH", "hydroxide"), ("HNO₃", "zuur"), ("MgCl₂", "zout"), ("SO₃", "oxide")],
          "Kijk naar OH, H vooraan, metaal met zuurrest of enkel zuurstof erbij.", ["oxide", "hydroxide", "zuur", "zout"]),
]
