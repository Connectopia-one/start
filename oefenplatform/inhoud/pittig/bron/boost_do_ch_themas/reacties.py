"""Chemische reacties en energie — pittig (🚀 Boost doorstroom, chemie).

Klikvragen op energiediagrammen en vragen over kloppend maken van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen over behoud van massa en energieomzettingen uit ch_reacties."""
from ..boost_do_nw_themas import stoffen as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26])
VRAGEN += [
    casus("Bij de verbranding van propaan geldt: … C₃H₈ + … O₂ → … CO₂ + … H₂O.", [
        mk("Welke coëfficiënten maken de vergelijking kloppend?",
           ["1, 5, 3, 4", "1, 3, 3, 4", "1, 5, 3, 8", "2, 5, 6, 4"], 0,
           "Drie C geven 3 CO₂, acht H geven 4 H₂O; rechts staan dan 6 + 4 = 10 O-atomen, dus 5 O₂."),
        tabel("Klopt dit over deze reactie?",
              [("Het is een exo-energetische reactie.", J), ("Je mag de index van C₃H₈ veranderen om sneller kloppend te maken.", F), ("Links en rechts staan evenveel zuurstofatomen.", J)],
              "Een index verandert de stof zelf; enkel coëfficiënten mag je aanpassen."),
    ]),
    inv("Twaalf gram magnesium reageert volledig met acht gram zuurstofgas. Hoeveel gram magnesiumoxide ontstaat er?", ["20", "20 g", "twintig"],
        "Wet van behoud van massa: 12 g + 8 g = 20 g."),
    mk("Een kaars brandt op en weegt achteraf veel minder. Waarom klopt de wet van behoud van massa toch?",
       ["De producten zijn gassen die in de lucht verdwijnen.", "Bij een verbranding wordt massa omgezet in licht.", "De wet geldt enkel voor reacties in vloeistoffen en vaste stoffen.", "Het kaarsvet verdampt zonder te reageren."], 0,
       "In een gesloten vat zou je zien dat de massa gelijk blijft."),
    tabel("Waaraan merk je dat er een chemische reactie gebeurd is?",
          [("Er ontstaat een gas dat er eerst niet was.", J), ("De kleur verandert blijvend.", J), ("Suiker lost op in water.", F), ("Er komt warmte of licht vrij.", J)],
          "Oplossen is een vermenging: de suiker blijft suiker."),
    koppel("Welke energieomzetting hoort bij elk voorbeeld?",
           [("een batterij doet een lampje branden", "chemisch naar elektrisch"), ("water ontleden met een batterij", "elektrisch naar chemisch"), ("fotosynthese", "licht naar chemisch"), ("een kaars brandt", "chemisch naar warmte en licht")],
           ["kernenergie naar beweging", "geluid naar chemisch"], "Bij elke reactie verandert energie van vorm."),
    mk("Tijdens een reactie in een bekerglas stijgt de temperatuur van 20 naar 34 °C. Wat besluit je?",
       ["De reactie is exo-energetisch.", "De reactie is endo-energetisch.", "Er gebeurt geen chemische reactie.", "De reactieproducten liggen hoger in het energiediagram."], 0,
       "Er komt warmte vrij naar de omgeving: exo-energetisch."),
    keuze("Het energieverschil tussen reagentia en reactieproducten heet de [[*reactie-energie|activeringsenergie|chemische binding]].",
          "In het energiediagram is dat de pijl tussen beide niveaus."),
    tabel("Klopt dit over de wet van behoud van massa?",
          [("Atomen worden anders geschikt, maar niet gemaakt of vernietigd.", J), ("Als er een gas ontstaat, verdwijnt er massa.", F), ("In een gesloten vat blijft de massa gelijk.", J)],
          "Ook een gas heeft massa; het ontsnapt enkel als het vat open is."),
    inv("Welke coëfficiënt hoort voor Fe in … Fe + 3 O₂ → 2 Fe₂O₃?", ["4", "vier"],
        "Rechts staan 2 · 2 = 4 ijzeratomen, dus links 4 Fe."),
    mk("Een reactie heeft een energiediagram waarin de producten hoger liggen dan de reagentia. Welke reactie kan dat zijn?",
       ["de fotosynthese", "de verbranding van hout", "een handwarmer die warm wordt", "een ontploffend vuurwerk"], 0,
       "De producten bevatten meer energie: de reactie heeft energie opgenomen, hier lichtenergie."),
]
