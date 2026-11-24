"""Heelal — pittig (Beyond dubbele finaliteit). Pittige vragen van Beyond doorstroom, zonder achtergrondstraling, roodverschuiving en het einde van het heelal, plus eigen vragen."""
from ..beyond_ak_themas import heelal as _B
from ..beyond_ak_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, sorteer
from ._kies import kies

VRAGEN = kies(_B.VRAGEN, weg=[6, 7, 8, 10, 28]) + [
    tabel("Klopt dit over het uitdijende heelal?", [
        ("de afstanden tussen de sterrenstelsels worden groter", J),
        ("de aarde ligt in het midden van de uitdijing", F),
        ("verre stelsels verwijderen zich sneller dan nabije", J),
    ], "Elk stelsel ziet de andere van zich weggaan; er is geen middelpunt."),
    inv("Het heelal is ongeveer 13,8 miljard jaar oud en de aarde ongeveer 4,6 miljard jaar. Hoeveel miljard jaar bestond het heelal al voor de aarde ontstond? Schrijf als decimaal getal.", ["9,2", "9.2"],
        "13,8 − 4,6 = 9,2."),
    mk("Je kijkt naar een sterrenstelsel op 2 miljoen lichtjaar. Wat zie je?",
       ["het stelsel zoals het 2 miljoen jaar geleden was",
        "het stelsel zoals het vandaag is, maar wat vager",
        "het stelsel zoals het over 2 miljoen jaar zal zijn",
        "enkel de sterren die 2 miljoen jaar oud zijn"], 0,
       "Het licht was 2 miljoen jaar onderweg."),
    sorteer("Hoort dit bij ons eigen sterrenstelsel of ligt het erbuiten?", ["in de Melkweg", "buiten de Melkweg"], [
        ["de zon", "in de Melkweg"],
        ["de Orionarm", "in de Melkweg"],
        ["het Andromedastelsel", "buiten de Melkweg"],
        ["een supercluster", "buiten de Melkweg"],
    ], "De Melkweg is één van de vele stelsels in de Lokale Groep."),
    keuze("Een ster maakt [[*zelf licht|geen eigen licht]], een planeet [[*weerkaatst het licht van een ster|maakt zelf licht]].",
          "In een ster smelt waterstof samen; een planeet licht enkel op in het licht van haar ster."),
]
