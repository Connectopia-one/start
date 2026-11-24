"""Druk bij vaste stoffen en in vloeistoffen — pittig (🚀 Boost doorstroom, fysica).

Vragen over druk van natuurwetenschappen Boost doorstroom, plus eigen vragen over p = F/A, eenheden, hydrostatische druk en de hydraulische pers uit fy_druk."""
from ..boost_do_nw_themas import druk as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 7, 8, 9, 10, 12, 24, 27])
VRAGEN += [
    casus("Een olifant van 4000 kg staat op vier poten, elk met een zool van 0,10 m². Een dame van 50 kg staat op één naaldhak van 1,0 cm² (= 0,00010 m²). Neem g = 10 N/kg.", [
        inv("Hoe groot is de druk van de olifant op de grond, in kPa?", ["100", "100 kPa"],
            "F = 40 000 N over 0,40 m² geeft 100 000 Pa = 100 kPa."),
        inv("Hoe groot is de druk onder de naaldhak, in kPa?", ["5000", "5000 kPa"],
            "F = 500 N over 0,00010 m² geeft 5 000 000 Pa = 5000 kPa."),
        mk("Wat besluit je uit die twee drukken?",
           ["De naaldhak geeft vijftig keer meer druk.", "De olifant geeft de grootste druk, want hij is het zwaarst.", "Ze geven dezelfde druk, want ze staan allebei stil.", "Je kan druk niet vergelijken bij een verschillende massa."], 0,
           "5000 kPa tegenover 100 kPa: het kleine oppervlak wint van de grote kracht."),
    ]),
    tabel("Zet om. Klopt dit?",
          [("1013 hPa = 101 300 Pa", J), ("2,5 bar = 250 000 Pa", J), ("50 kPa = 5000 Pa", F), ("1 mbar = 100 Pa", J)],
          "hecto = 100, kilo = 1000, 1 bar = 100 000 Pa, 1 mbar = 1 hPa."),
    volgorde("Rangschik van kleinste naar grootste druk.",
             ["800 Pa", "12 hPa", "3 kPa", "0,5 bar"],
             "Alles in pascal: 800, 1200, 3000 en 50 000 Pa."),
    inv("Hoe groot is de hydrostatische druk op 20 m diepte in zeewater met ρ = 1030 kg/m³ en g = 10 N/kg, in kPa?", ["206", "206 kPa"],
        "p = ρ · g · h = 1030 · 10 · 20 = 206 000 Pa = 206 kPa."),
    mk("Een duiker zit op 10 m diepte in een meer. Hoe groot is de totale druk ongeveer, met een luchtdruk van 100 kPa en g = 10 N/kg?",
       ["200 kPa", "100 kPa", "10 kPa", "1100 kPa"], 0,
       "Hydrostatisch 1000 · 10 · 10 = 100 kPa, plus 100 kPa luchtdruk."),
    tabel("Drie vazen met een verschillende vorm zijn tot dezelfde hoogte met water gevuld. Klopt dit?",
          [("De druk op de bodem is in de drie vazen gelijk.", J), ("De vaas met het meeste water heeft de grootste bodemdruk.", F), ("Met olie in plaats van water wordt de bodemdruk kleiner.", J)],
          "Enkel ρ, g en h tellen; olie heeft een kleinere massadichtheid dan water."),
    casus("Bij een hydraulische lift duw je met 200 N op een zuiger van 0,010 m². De grote zuiger heeft een oppervlakte van 0,50 m².", [
        inv("Hoe groot is de druk in de olie, in pascal?", ["20000", "20 000", "20000 Pa"],
            "p = 200 / 0,010 = 20 000 Pa."),
        inv("Hoe groot is de kracht op de grote zuiger, in newton?", ["10000", "10 000", "10000 N"],
            "F = p · A = 20 000 · 0,50 = 10 000 N."),
        tabel("Klopt dit over de hydraulische lift?",
              [("De druk is bij beide zuigers even groot.", J), ("De grote zuiger gaat even ver omhoog als de kleine omlaag.", F), ("Je wint kracht, maar verliest afstand.", J)],
              "De grote zuiger levert vijftig keer meer kracht en komt vijftig keer minder ver."),
    ]),
    sleep("Hoe dieper je duikt, hoe [[groter]] de druk. Op dezelfde diepte is de druk in alle [[richtingen]] even groot. Een dam is daarom onderaan [[dikker]] dan bovenaan.",
          ["kleiner", "dunner"], "De hydrostatische druk groeit met de diepte en werkt naar alle kanten."),
    koppel("Welke toepassing hoort bij welk principe?",
           [("sneeuwschoenen", "groot oppervlak, kleine druk"), ("een punaise", "klein oppervlak, grote druk"), ("een remsysteem van een auto", "beginsel van Pascal"), ("oorpijn bij diep duiken", "hydrostatische druk")],
           [], "Elke toepassing steunt op p = F/A, p = ρ · g · h of het beginsel van Pascal."),
    keuze("Een kracht van 1 N op 1 m² geeft een druk van [[*1 Pa|1 bar|1 hPa]].",
          "De pascal is per afspraak één newton per vierkante meter."),
    mk("Waarom heeft een tractor brede banden?",
       ["om de druk op de akker te verkleinen", "om de zwaartekracht op de tractor te verkleinen", "om de massa van de tractor beter te verdelen over de as", "om de druk op de akker zo groot mogelijk te maken"], 0,
       "Een groter contactoppervlak geeft bij dezelfde kracht een kleinere druk, zodat de tractor minder wegzakt."),
    inv("Een duikbril met een glas van 0,0040 m² zit op een diepte waar de waterdruk 50 kPa is. Hoe groot is de kracht van het water op het glas, in newton?", ["200", "200 N"],
        "F = p · A = 50 000 · 0,0040 = 200 N."),
    tabel("Klopt dit over een waterkolom van 10 m hoog?",
          [("Ze geeft ongeveer dezelfde druk als de luchtdruk.", J), ("Haar druk hangt af van de breedte van de kolom.", F), ("In kwik is een veel lagere kolom nodig voor dezelfde druk.", J)],
          "1000 · 10 · 10 = 100 kPa, ongeveer 1 bar; kwik heeft een veel grotere massadichtheid."),
]
