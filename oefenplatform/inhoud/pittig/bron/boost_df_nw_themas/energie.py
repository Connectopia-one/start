"""Energieomzettingen, vermogen en rendement — pittig (🚀 Boost dubbele finaliteit, natuurwetenschappen).

Pittige vragen van natuurwetenschappen 🚀 Boost doorstroom zonder arbeid en
zonder de formules van de energievormen, plus eigen vragen over systemen, de
energiebalans, koeling en isolatie."""
from ..boost_do_nw_themas import energie as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 9, 10, 11, 17, 18, 19, 20, 21, 22, 23, 24, 26])
VRAGEN += [
    casus("Een laptop neemt in één uur 180 000 J elektrische energie op. Daarvan gaat 54 000 J naar het scherm, de processor en de luidsprekers; de rest wordt warmte.", [
        inv("Hoeveel joule is ongewenste energie?", ["126000", "126 000", "126 000 J"],
            "180 000 − 54 000 = 126 000 J."),
        inv("Hoeveel procent is het rendement?", ["30", "30 %"],
            "54 000 / 180 000 = 0,30 = 30 %."),
        inv("Wat is het vermogen van de laptop, in watt?", ["50", "50 W"],
            "P = E / t = 180 000 J / 3600 s = 50 W."),
        tabel("Klopt dit over de laptop?",
              [("Daarom heeft hij een ventilator nodig.", J), ("Zijn rendement kan nooit 100 % zijn.", J), ("De warmte verdwijnt zomaar uit het heelal.", F)],
              "De warmte gaat naar de omgeving: energie blijft behouden."),
    ]),
    sorteer("Is het systeem open, gesloten of geïsoleerd?", ["open", "gesloten", "geïsoleerd"],
            [("een pot soep zonder deksel op het vuur", "open"), ("een dichte blikken doos in de zon", "gesloten"), ("een ideale thermosfles met deksel", "geïsoleerd"), ("je lichaam dat eet en zweet", "open"), ("een dichtgeschroefde fles in de koelkast", "gesloten")],
            "Open: energie en materie; gesloten: enkel energie; geïsoleerd: niets."),
    tabel("Klopt dit over isolatie en koeling?",
          [("Een geïsoleerd dak laat minder warmte naar buiten.", J), ("Een koelkast zet elektrische energie om in warmte in de keuken.", J), ("Met isolatie moet je meer verwarmen.", F)],
          "Isoleren beperkt het verlies; koelen verplaatst warmte en kost energie."),
    volgorde("Rangschik de energieomzettingen in een fietsdynamo die een lampje laat branden.",
             ["chemische energie in je spieren", "kinetische energie van het wiel", "elektrische energie", "stralingsenergie van het lampje"],
             "Van je spieren tot het licht, met telkens wat warmte erbij."),
    mk("Een ledlamp van 8 W en een gloeilamp van 60 W geven evenveel licht. Wat besluit je?",
       ["de ledlamp heeft een hoger rendement", "de gloeilamp geeft meer nuttige energie", "beide lampen hebben hetzelfde rendement", "de ledlamp maakt meer warmte dan licht"], 0,
       "Met minder energie evenveel licht: minder ongewenste warmte."),
    inv("Een toestel van 1500 W staat 20 minuten aan. Hoeveel kWh verbruikt het?", ["0,5", "0.5", "0,5 kWh"],
        "1,5 kW · 1/3 h = 0,5 kWh."),
    keuze("In een geïsoleerd systeem blijft de totale energie [[*gelijk|groter worden|kleiner worden]].",
          "Er gaat niets in of uit: de energie verandert enkel van vorm."),
    tabel("Welke eenheid hoort bij welke grootheid?",
          [("joule", "energie"), ("kilowattuur", "energie"), ("watt", "vermogen"), ("kilocalorie", "energie")],
          "Vermogen is energie per tijd.", ["energie", "vermogen"]),
    tabel("Klopt dit over de wet van behoud van energie?",
          [("Energie kan niet verdwijnen, enkel van vorm veranderen.", J), ("Bij elke omzetting wordt een deel ongewenste energie.", J), ("Een machine kan meer nuttige energie geven dan ze opneemt.", F)],
          "Wat erin gaat, komt eruit: nuttig plus ongewenst."),
]
