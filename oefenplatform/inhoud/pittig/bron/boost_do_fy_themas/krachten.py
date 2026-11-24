"""Krachten, krachtenbalans en zwaartekracht — pittig (🚀 Boost doorstroom, fysica).

Klikvragen op de krachtenprent en vragen van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen over veerkracht, wrijving en gewicht uit fy_krachten."""
from ..boost_do_nw_themas import krachten as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, list(range(0, 9)) + list(range(11, 22)) + [23, 24, 25, 26])
VRAGEN += [
    casus("Lotte hangt gewichtjes aan een veer en meet de uitrekking: 1,0 N geeft 2,0 cm, 2,0 N geeft 4,0 cm en 3,0 N geeft 6,0 cm.", [
        inv("Wat is de veerconstante van deze veer, in N/m?", ["50", "50 N/m"],
            "k = F / Δl = 1,0 N / 0,020 m = 50 N/m."),
        tabel("Klopt dit over haar metingen?",
              [("De uitrekking is recht evenredig met de kracht.", J), ("De grafiek F(Δl) is een rechte door de oorsprong.", J), ("Met 5,0 N rekt de veer 5,0 cm uit.", F)],
              "Bij 5,0 N verwacht je 10 cm: de uitrekking verdubbelt als de kracht verdubbelt."),
    ]),
    mk("Een kist van 40 kg staat op een vloer met μ = 0,25. Je duwt horizontaal met 80 N. Wat gebeurt er, met g = 10 N/kg?",
       ["Ze blijft staan: de wrijving kan tot 100 N gaan.", "Ze schuift, want elke duw groter dan nul doet ze bewegen.", "Ze schuift, want de wrijvingskracht is hier maar 10 N.", "Ze komt los van de vloer, want de normaalkracht wint."], 0,
       "Fw = μ · Fn = 0,25 · 400 = 100 N; je duwt minder hard dan dat."),
    tabel("Een astronaut gaat van de aarde naar de maan. Wat verandert er?",
          [("zijn massa", "blijft gelijk"), ("de zwaartekracht op hem", "verandert"), ("zijn gewicht op de grond", "verandert"), ("de hoeveelheid materie in zijn lichaam", "blijft gelijk")],
          "De massa hangt niet af van de plaats; g en dus de zwaartekracht wel.", ["blijft gelijk", "verandert"]),
    inv("Op de maan is g = 1,6 N/kg. Hoe groot is de zwaartekracht op een maanwagentje van 200 kg, in newton?", ["320", "320 N"],
        "Fz = m · g = 200 · 1,6 = 320 N."),
]
