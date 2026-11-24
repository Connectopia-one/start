"""Wetenschappelijk onderzoek en STEM — pittig (🚀 Boost doorstroom, biologie).

Pittige vragen over de onderzoekscyclus, veilig werken en glaswerk van natuurwetenschappen Boost doorstroom (met hun prenten), plus eigen vragen over de microscoop en het preparaat uit bi_onderzoek."""
from ..boost_do_nw_themas import onderzoek as O, veilig as V
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(O.VRAGEN, [11, 12, 13, 14, 16, 18, 21, 24, 25, 27]) + kies(V.VRAGEN, [0, 1, 2, 10, 16, 19, 20, 23])
VRAGEN += [
    casus("Femke bekijkt een preparaat van ui-opperhuid onder de lichtmicroscoop. Ze gebruikt een oculair van 10 keer en begint met een objectief van 4 keer. Daarna draait ze naar het objectief van 40 keer.", [
        inv("Hoeveel keer is de totale vergroting met het objectief van 40 keer?", ["400", "400 keer", "400x"],
            "Oculair maal objectief: 10 · 40 = 400."),
        tabel("Klopt dit over wat Femke ziet?",
              [("Met het objectief van 40 keer ziet ze een kleiner stukje van het preparaat.", J), ("Ze begint met het zwakste objectief omdat het beeldveld dan het grootst is.", J), ("Met een sterkere vergroting wordt het beeld vanzelf lichter.", F)],
              "Hoe sterker de vergroting, hoe kleiner en donkerder het beeldveld."),
        mk("Femke ziet een perfect rond, donker omrand bolletje zonder kern. Wat is het waarschijnlijk?",
           ["een luchtbel onder het dekglaasje", "een celkern van een ui-cel", "een bladgroenkorrel van de ui", "een mitochondrion in het cytoplasma"], 0,
           "Een luchtbel is rond met een dikke donkere rand; ze kan op een cel lijken."),
    ]),
    tabel("Waarom doe je dit bij het maken van een preparaat?",
          [("een dekglaasje erop leggen", "vlak houden en uitdrogen voorkomen"), ("een kleurstof toevoegen", "meer contrast"), ("het dekglaasje schuin laten zakken", "luchtbellen vermijden")],
          "Elke stap maakt het beeld duidelijker.", ["vlak houden en uitdrogen voorkomen", "meer contrast", "luchtbellen vermijden"]),
    mk("Je kijkt door een oculair van 15 keer met een objectief van 10 keer. Hoeveel keer is de totale vergroting?",
       ["150 keer", "25 keer", "1,5 keer", "1500 keer"], 0,
       "Vermenigvuldig de twee vergrotingen: 15 · 10 = 150."),
    casus("Ruben wil weten of kiemende tuinkers sneller groeit bij meer licht. Hij zet drie potjes met elk 20 zaadjes op een plek met weinig, middelmatig en veel licht. Hij geeft ze evenveel water en meet na een week de lengte.", [
        koppel("Welke variabele is dit?",
               [("de hoeveelheid licht", "onafhankelijke variabele"), ("de lengte na een week", "afhankelijke variabele"), ("de hoeveelheid water", "constante variabele")],
               ["hypothese", "controlegroep"], "Wat je zelf instelt, wat je meet en wat je gelijk houdt."),
        tabel("Klopt dit over de proef van Ruben?",
              [("Hij zet de hoeveelheid licht op de horizontale as van zijn grafiek.", J), ("Twintig zaadjes per potje maakt zijn resultaat betrouwbaarder dan één zaadje.", J), ("Als het potje met veel licht ook warmer staat, is zijn proef nog eerlijk.", F)],
              "Een eerlijke proef verandert maar één ding tegelijk."),
        mk("Wat is een goede hypothese voor Ruben?",
           ["Tuinkers groeit sneller naarmate ze meer licht krijgt.", "Tuinkers is een plant die vooral in de moestuin groeit.", "Ik wil weten wat er met tuinkers gebeurt bij licht.", "Tuinkers smaakt veel beter met veel licht."], 0,
           "Een hypothese is een toetsbare verwachting over het verband."),
    ]),
    tabel("Wat hoort bij elke as van een grafiek?",
          [("de naam van de grootheid", J), ("de eenheid", J), ("een gelijkmatige schaalverdeling", J), ("de naam van de onderzoeker", F)],
          "Grootheid, eenheid en een eerlijke schaal maken een grafiek leesbaar."),
    sleep("De vergroting van een lichtmicroscoop is de vergroting van het [[oculair]] maal die van het [[objectief]]. Je begint met het [[zwakste]] objectief.",
          ["sterkste", "dekglaasje"], "Zo vind je het preparaat het makkelijkst terug."),
]
