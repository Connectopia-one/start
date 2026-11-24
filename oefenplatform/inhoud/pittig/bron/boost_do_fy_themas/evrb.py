"""Versnelde beweging, vrije val en verticale worp — pittig (🚀 Boost doorstroom, fysica).

Klikvragen op de v(t)-grafiek en vragen over vrije val en worp van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen uit fy_evrb."""
from ..boost_do_nw_themas import beweging as N, krachten as K
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [7, 8, 9, 10, 11, 12, 17, 21, 22]) + kies(K.VRAGEN, [9, 10, 22, 27])
VRAGEN += [
    casus("Een auto staat stil aan een verkeerslicht. Bij groen versnelt hij 5,0 s lang met 3,0 m/s². Daarna rijdt hij eenparig verder.", [
        inv("Hoe snel rijdt de auto na 5,0 s, in m/s?", ["15", "15 m/s"],
            "v = a · t = 3,0 · 5,0 = 15 m/s."),
        inv("Hoeveel meter legt hij af tijdens het versnellen?", ["37,5", "37.5", "38"],
            "Oppervlakte van de driehoek onder de v(t)-grafiek: ½ · 5,0 · 15 = 37,5 m."),
        tabel("Klopt dit over de beweging van de auto?",
              [("Tijdens de eerste 5 s is de v(t)-grafiek een schuine rechte.", J), ("Na 5 s is de versnelling nul.", J), ("Tijdens de eerste 5 s is de x(t)-grafiek een rechte.", F)],
              "Bij een eenparig versnelde beweging is de x(t)-grafiek een parabool."),
    ]),
    sorteer("Welke beweging hoort bij de grafiek?", ["ERB", "Eenparig versneld", "Eenparig vertraagd"],
            [("een horizontale v(t)-grafiek, niet op nul", "ERB"), ("een stijgende rechte in de v(t)-grafiek", "Eenparig versneld"), ("een dalende rechte in de v(t)-grafiek, naar nul toe", "Eenparig vertraagd"), ("een a(t)-grafiek die op nul ligt, terwijl het voorwerp beweegt", "ERB"), ("een positieve versnelling in de zin van de beweging", "Eenparig versneld")],
            "Lees de helling van v(t) of de waarde van a(t)."),
    mk("Een appel valt uit een boom en raakt na 0,80 s de grond. Hoe snel valt hij dan, met g = 9,81 m/s²?",
       ["7,8 m/s", "12 m/s", "3,1 m/s", "0,80 m/s"], 0,
       "v = g · t = 9,81 · 0,80 = 7,8 m/s."),
    inv("Een steen valt uit stilstand 2,0 s lang. Hoeveel meter valt hij, met g = 10 m/s²?", ["20", "20 m"],
        "h = ½ · g · t² = ½ · 10 · 4,0 = 20 m."),
    tabel("Een bal wordt recht omhoog gegooid. Klopt dit, als je de luchtweerstand verwaarloost?",
          [("In het hoogste punt is de snelheid nul.", J), ("In het hoogste punt is de versnelling nul.", F), ("De bal komt met dezelfde snelheid terug als waarmee hij vertrok.", J), ("Tijdens het stijgen is de beweging eenparig vertraagd.", J)],
          "De zwaartekracht werkt altijd: de versnelling is overal g, ook bovenaan."),
    mk("Een auto rijdt 20 m/s en remt eenparig tot stilstand in 4,0 s. Wat is de versnelling?",
       ["−5,0 m/s²", "5,0 m/s²", "−80 m/s²", "−0,20 m/s²"], 0,
       "a = Δv / Δt = (0 − 20) / 4,0 = −5,0 m/s²."),
    keuze("Bij een vrije val zonder luchtweerstand vallen een hamer en een veer [[*even snel|niet even snel|helemaal niet]].",
          "De valversnelling hangt niet af van de massa."),
    casus("Twee fietsers vertrekken samen. Fietser A rijdt meteen eenparig 6 m/s. Fietser B vertrekt uit stilstand en versnelt met 1 m/s².", [
        inv("Na hoeveel seconden rijden ze even snel?", ["6", "6 s"],
            "B rijdt 1 m/s sneller per seconde: na 6 s rijdt hij ook 6 m/s."),
        tabel("Klopt dit over het moment waarop ze even snel rijden?",
              [("A is dan verder dan B.", J), ("Ze snijden elkaar dan in de x(t)-grafiek.", F), ("Ze snijden elkaar dan in de v(t)-grafiek.", J)],
              "Gelijke snelheid is een snijpunt in v(t); B moet daarna nog inhalen."),
    ]),
    mk("Wat stelt de helling van een v(t)-grafiek voor?",
       ["de versnelling", "de afgelegde weg", "de positie", "de massa"], 0,
       "Helling van v(t) = Δv / Δt = a."),
    inv("Een lift versnelt in 2,0 s van 0 tot 3,0 m/s. Wat is de versnelling in m/s²?", ["1,5", "1.5", "1,5 m/s²"],
        "a = 3,0 / 2,0 = 1,5 m/s²."),
    sleep("Bij een vrije val start het voorwerp uit [[stilstand]] en versnelt het met [[g]], ongeveer [[9,81 m/s²]].",
          ["constante snelheid", "1 m/s²"], "De vrije val is een eenparig versnelde beweging."),
    keuze("Een parachutist met open valscherm valt na een tijdje met een [[*constante snelheid|steeds grotere snelheid|steeds grotere versnelling]].",
          "De luchtweerstand wordt even groot als de zwaartekracht: de resulterende kracht is nul."),
    mk("Een bal valt 3,0 s vrij uit stilstand. Hoe snel gaat hij dan, met g = 10 m/s²?",
       ["30 m/s", "3,3 m/s", "45 m/s", "90 m/s"], 0,
       "v = g · t = 10 · 3,0 = 30 m/s."),
]
