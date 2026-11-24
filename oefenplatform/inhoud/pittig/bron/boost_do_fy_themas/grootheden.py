"""Grootheden, eenheden en nauwkeurig meten — pittig (🚀 Boost doorstroom, fysica).

Klikvragen op grafieken van verbanden en vragen over SI-eenheden, voorvoegsels, wetenschappelijke notatie, beduidende cijfers en meetbereik van natuurwetenschappen Boost doorstroom."""
from ..boost_do_nw_themas import onderzoek as O, veilig as V
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(O.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 21, 26]) + kies(V.VRAGEN, [6, 7, 8, 9, 17, 18, 24, 25])
VRAGEN += [
    casus("Een leerling meet de lengte van een potlood vijf keer met een lat in millimeter: 152 mm, 151 mm, 153 mm, 152 mm en 152 mm.", [
        inv("Wat is de gemiddelde lengte in mm?", ["152", "152 mm"],
            "(152 + 151 + 153 + 152 + 152) : 5 = 760 : 5 = 152 mm."),
        inv("Schrijf die lengte in meter.", ["0,152", "0.152", "0,152 m"],
            "152 mm = 0,152 m, want 1 m = 1000 mm."),
        tabel("Klopt dit over de meting?",
              [("Meerdere keren meten maakt toevallige fouten kleiner.", J), ("Met een lat in mm kan je tot op een tiende millimeter nauwkeurig meten.", F), ("Het resultaat heeft drie beduidende cijfers.", J)],
              "De nauwkeurigheid wordt bepaald door de kleinste schaalverdeling."),
    ]),
    tabel("Welke SI-eenheid hoort bij de grootheid?",
          [("kracht", "N"), ("energie", "J"), ("vermogen", "W"), ("druk", "Pa")],
          "Newton, joule, watt en pascal.", ["N", "J", "W", "Pa"]),
    mk("Een auto rijdt 90 km/h. Hoeveel is dat in m/s?",
       ["25 m/s", "90 m/s", "324 m/s", "1,5 m/s"], 0,
       "Deel door 3,6: 90 : 3,6 = 25 m/s."),
    sorteer("Recht evenredig of omgekeerd evenredig?", ["Recht evenredig", "Omgekeerd evenredig"],
            [("de afgelegde weg en de tijd bij constante snelheid", "Recht evenredig"), ("de reistijd en de snelheid voor een vaste afstand", "Omgekeerd evenredig"), ("het gewicht en de massa", "Recht evenredig"), ("de druk en het volume van een gas bij gelijke temperatuur", "Omgekeerd evenredig")],
            "Recht evenredig: het quotiënt blijft gelijk; omgekeerd evenredig: het product blijft gelijk."),
    inv("Schrijf 0,00072 m in wetenschappelijke notatie. Welk getal staat er vooraan, voor de macht van tien?", ["7,2", "7.2"],
        "0,00072 m = 7,2 · 10⁻⁴ m."),
    tabel("Hoeveel beduidende cijfers heeft dit resultaat?",
          [("0,0450 m", "3"), ("2300 kg, gemeten tot op 100 kg", "2"), ("9,81 m/s²", "3"), ("1,0 s", "2")],
          "Nullen vooraan tellen niet mee; een nul achter de komma wel.", ["2", "3"]),
]
