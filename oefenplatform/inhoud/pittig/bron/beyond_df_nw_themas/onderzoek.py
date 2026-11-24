"""Onderzoekend werken, meten en veilig werken — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen natuurwetenschappen Beyond over onderzoek, ontwerpen, voorvoegsels en verbanden binnen nwd_onderzoek, plus eigen vragen over veilig werken en meten."""
from ..beyond_nw_themas import onderzoek as O, veilig as V
from ..beyond_fys_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(O.VRAGEN, [0, 1, 2, 3, 4, 5, 8, 12, 13, 14, 17, 18, 19, 20, 23]) + kies(V.VRAGEN, [9, 12, 23, 25, 27]) + [
    tabel("Welk meettoestel kies je?", [
        ("je wil \\(2\\) kg aardappelen wegen", "balans tot \\(5\\) kg"),
        ("je wil \\(0{,}35\\) g zout afwegen", "balans tot op \\(0{,}01\\) g"),
        ("je wil een verschil van een halve graad zien", "thermometer met streepjes per tiende graad"),
    ], "Kies een toestel met een passend meetbereik en een fijne genoeg verdeling.",
        kolommen=["balans tot \\(5\\) kg", "balans tot op \\(0{,}01\\) g", "thermometer met streepjes per tiende graad"]),
    inv("Hoeveel milliliter is \\(0{,}25\\) L?", ["250", "250 mL"], "Milli is een duizendste: \\(0{,}25 \\cdot 1000 = 250\\) mL."),
    sorteer("Is dit veilig werken in het labo of niet?", ["veilig", "niet veilig"], [
        ["lange haren vastbinden bij de bunsenbrander", "veilig"], ["glasscherven met een borstel en blad opruimen", "veilig"],
        ["een toestel bedienen met natte handen", "niet veilig"], ["een gemorst product laten liggen tot na de les", "niet veilig"],
        ["restproducten sorteren volgens het etiket", "veilig"],
    ], "Veilig werken beschermt jou en wie na jou komt."),
    mk("Je leest een maatcilinder af. Het oppervlak van de vloeistof is gebogen. Hoe lees je correct af?",
       ["op ooghoogte, aan de onderkant van de meniscus", "van bovenaf, aan de bovenkant van de rand", "schuin van onderen, aan de hoogste druppel", "op ooghoogte, aan de bovenste rand van de buis"], 0,
       "Van boven of van onder kijken geeft een parallaxfout."),
    keuze("Voor je een stof afweegt in een bekerglas, zet je de balans met het lege bekerglas [[*op nul|uit|op de hoogste stand]].", "Dan lees je enkel de massa van de stof af."),
    tabel("Klopt dit over H- en P-zinnen?", [
        ("Een H-zin beschrijft het gevaar van de stof.", J),
        ("« Draag een veiligheidsbril » is een H-zin.", F),
        ("Een P-zin zegt welke voorzorgen je neemt.", J),
    ], "H van hazard, P van precaution."),
]
