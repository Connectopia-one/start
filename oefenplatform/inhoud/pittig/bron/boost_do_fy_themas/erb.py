"""Eenparig rechtlijnige beweging — pittig (🚀 Boost doorstroom, fysica).

Klikvragen op de x(t)-grafiek en rekenvragen van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen over de positiefunctie, verplaatsing en v(t)-grafieken uit fy_erb."""
from ..boost_do_nw_themas import beweging as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 18, 19, 20, 23, 24, 25, 26])
VRAGEN += [
    casus("Een fietser vertrekt om t₀ = 0 s op positie x₀ = 200 m en rijdt met een constante snelheid van 5,0 m/s in de negatieve zin van de x-as.", [
        mk("Welke positiefunctie hoort bij de fietser?",
           ["x = 200 − 5,0 · t", "x = 200 + 5,0 · t", "x = 5,0 − 200 · t", "x = −200 + 5,0 · t"], 0,
           "x = x₀ + v · (t − t₀) met v = −5,0 m/s."),
        inv("Op welke positie, in meter, is de fietser na 30 s?", ["50", "50 m"],
            "x = 200 − 5,0 · 30 = 200 − 150 = 50 m."),
        inv("Na hoeveel seconden passeert hij de oorsprong?", ["40", "40 s"],
            "0 = 200 − 5,0 · t geeft t = 40 s."),
    ]),
    tabel("Klopt dit over een v(t)-grafiek van een ERB?",
          [("Ze is een horizontale rechte.", J), ("De oppervlakte onder de grafiek is de verplaatsing.", J), ("De helling van de grafiek is de snelheid.", F)],
          "Bij een ERB blijft v constant; de helling van een x(t)-grafiek is de snelheid."),
    mk("Een loper loopt 400 m rond een atletiekpiste en komt terug op zijn vertrekpunt. Wat klopt?",
       ["De afgelegde weg is 400 m, de verplaatsing 0 m.", "De afgelegde weg en de verplaatsing zijn allebei 400 m.", "De afgelegde weg is 0 m, de verplaatsing 400 m.", "De afgelegde weg en de verplaatsing zijn allebei 0 m."], 0,
       "De verplaatsing vergelijkt enkel begin- en eindpositie."),
    mk("Twee x(t)-grafieken zijn rechten. Rechte A is steiler dan rechte B. Wat besluit je?",
       ["Voorwerp A beweegt sneller dan B.", "Voorwerp A is verder van de oorsprong vertrokken.", "Voorwerp A versnelt en B niet.", "Voorwerp A heeft meer massa dan B."], 0,
       "De helling van een x(t)-grafiek is de snelheid."),
    tabel("Is dit een scalaire of een vectoriële grootheid?",
          [("de afgelegde weg", "scalair"), ("de verplaatsing", "vectorieel"), ("de tijd", "scalair"), ("de snelheid", "vectorieel")],
          "Een vector heeft een grootte, een richting, een zin en een aangrijpingspunt.", ["scalair", "vectorieel"]),
    inv("Een trein rijdt eerst 60 km in 1,0 h en dan 90 km in 0,50 h. Wat is zijn gemiddelde snelheid in km/h?", ["100", "100 km/h"],
        "150 km in 1,5 h geeft 100 km/h; je deelt de totale weg door de totale tijd."),
    sleep("Bij een ERB is de [[snelheid]] constant. De x(t)-grafiek is een [[schuine rechte]] en de v(t)-grafiek een [[horizontale rechte]].",
          ["versnelling", "parabool"], "Drie kenmerken van een eenparig rechtlijnige beweging."),
]
