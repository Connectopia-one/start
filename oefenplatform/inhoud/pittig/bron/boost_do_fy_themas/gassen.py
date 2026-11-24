"""Gassen, temperatuur en de gaswetten — pittig (🚀 Boost doorstroom, fysica).

Vragen over luchtdruk en gassen van natuurwetenschappen Boost doorstroom, plus eigen vragen over het deeltjesmodel, kelvin en de gaswetten uit fy_gassen."""
from ..boost_do_nw_themas import druk as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [4, 5, 6, 11] + list(range(13, 24)) + [25, 26])
VRAGEN += [
    casus("Een duiker heeft een fles van 12 L met lucht op 200 bar bij 27 °C. Na een tijd in de zon is de fles 57 °C warm. Het volume van de fles verandert niet.", [
        inv("Hoeveel kelvin is 27 °C? Rond af op een geheel getal.", ["300", "300 K"],
            "27 + 273 = 300 K."),
        mk("Welke gaswet gebruik je voor de fles?",
           ["p / T = constant", "p · V = constant", "V / T = constant", "p · T = constant"], 0,
           "Het volume blijft gelijk: een isochoor proces."),
        inv("Hoe groot is de druk in de warme fles, in bar?", ["220", "220 bar"],
            "200 / 300 = p / 330, dus p = 220 bar."),
    ]),
    koppel("Welke wet hoort bij welk proces van een vaste hoeveelheid gas?",
           [("isotherm", "p · V = constant"), ("isobaar", "V / T = constant"), ("isochoor", "p / T = constant")],
           ["p · T = constant"], "Iso betekent gelijk: temperatuur, druk of volume blijft gelijk."),
    sorteer("Wordt de druk groter of kleiner? Er verandert telkens maar één grootheid.", ["groter", "kleiner"],
            [("het volume halveert bij gelijke temperatuur", "groter"), ("de temperatuur in kelvin daalt bij vast volume", "kleiner"), ("er wordt gas bijgepompt in hetzelfde vat", "groter"), ("het volume verdubbelt bij gelijke temperatuur", "kleiner"), ("het vat wordt verwarmd", "groter")],
            "Gebruik p · V = n · R · T en houd de rest gelijk."),
    inv("Hoeveel mol gas zit er in 0,0249 m³ bij 100 000 Pa en 300 K, met R = 8,31 J/(mol·K)? Rond af op een geheel getal.", ["1", "1,0", "1 mol"],
        "n = p · V / (R · T) = 2490 / 2493 ≈ 1 mol."),
    tabel("Een ballon met helium stijgt hoog in de atmosfeer. Klopt dit?",
          [("De luchtdruk rond de ballon wordt kleiner.", J), ("De ballon zet uit.", J), ("Het aantal heliumdeeltjes in de ballon groeit.", F)],
          "Buiten daalt de druk, dus het gas in de ballon kan verder uitzetten tot hij knapt."),
    mk("Een gas van 6,0 L bij 400 K wordt bij gelijke druk afgekoeld tot 200 K. Hoe groot wordt het volume?",
       ["3,0 L", "12 L", "6,0 L", "1,5 L"], 0,
       "V / T blijft gelijk: de temperatuur in kelvin halveert, dus het volume ook."),
    tabel("Klopt dit over temperatuur in het deeltjesmodel?",
          [("Bij 0 K bewegen de deeltjes niet meer.", J), ("Een temperatuur van −300 °C bestaat.", F), ("Verdubbel je de temperatuur in kelvin, dan verdubbelt de gemiddelde kinetische energie.", J)],
          "De absolute temperatuur is een maat voor de gemiddelde kinetische energie; lager dan −273,15 °C kan niet."),
    sleep("Een gas oefent druk uit doordat de deeltjes tegen de [[wand]] botsen. Warm je het gas op, dan bewegen de deeltjes [[sneller]] en stijgt de druk. De temperatuur vul je in [[kelvin]] in.",
          ["trager", "graden Celsius"], "Het deeltjesmodel verklaart de gaswetten."),
    keuze("Een p(V)-grafiek van een isotherm proces is een [[*hyperbool|rechte door de oorsprong|horizontale rechte]].",
          "p en V zijn omgekeerd evenredig."),
    inv("Een gas van 1,0 bar, 10 L en 300 K gaat naar 2,0 bar en 600 K. Hoe groot is het nieuwe volume in liter?", ["10", "10 L"],
        "p · V / T: 1,0 · 10 / 300 = 2,0 · V / 600, dus V = 10 L."),
    volgorde("Rangschik van koudste naar warmste.",
             ["0 K", "−100 °C", "200 K", "0 °C", "300 K"],
             "Alles in kelvin: 0, 173, 200, 273 en 300 K."),
]
