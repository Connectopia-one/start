# -*- coding: utf-8 -*-
"""Ready aardrijkskunde: België (gewesten, provincies en hun hoofdsteden, buurlanden,
talen, rivieren, kust en Ardennen). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "België"
UITLEG_1 = "Vlaanderen, Wallonië, Brussel en de provincies."
UITLEG_2 = "Buurlanden, rivieren, de kust en de Ardennen."

DEEL_1 = [
    mk("Wat is de hoofdstad van België?", ["Brussel", "Antwerpen", "Gent", "Luik"], 0, "Brussel is de hoofdstad van België."),
    inv("België heeft ___ provincies.", "10", "5 in Vlaanderen en 5 in Wallonië. Brussel hoort bij geen enkele provincie.", 10),
    mk("Welke drie gewesten heeft België?", ["Vlaanderen, Wallonië en Brussel", "Gent, Luik en Brugge", "Noord, Zuid en Midden", "Antwerpen, Limburg en Namen"], 0, "Het Vlaams Gewest, het Waals Gewest en het Brussels Hoofdstedelijk Gewest."),
    mk("Wat is de hoofdstad van de provincie Limburg?", ["Hasselt", "Genk", "Tongeren", "Maasmechelen"], 0, "Hasselt is de hoofdstad van Limburg."),
    mk("Wat is de hoofdstad van West-Vlaanderen?", ["Brugge", "Kortrijk", "Oostende", "Ieper"], 0, "Brugge is de hoofdstad van West-Vlaanderen."),
    inv("De hoofdstad van Oost-Vlaanderen is ___.", ["Gent"], "Gent ligt waar de Schelde en de Leie samenkomen."),
    wn("Antwerpen is zowel een stad als een provincie.", True, "De stad Antwerpen is de hoofdstad van de provincie Antwerpen."),
    mk("Wat is de hoofdstad van Vlaams-Brabant?", ["Leuven", "Mechelen", "Aalst", "Waver"], 0, "Leuven is de hoofdstad van Vlaams-Brabant."),
    mk("Welke provincie ligt in Wallonië?", ["Luik", "Limburg", "Antwerpen", "West-Vlaanderen"], 0, "Luik, Namen, Henegouwen, Luxemburg en Waals-Brabant liggen in Wallonië."),
    wn("In Vlaanderen spreekt men vooral Nederlands.", True, "In Wallonië spreekt men vooral Frans."),
    mk("Hoeveel officiële talen heeft België?", ["1", "2", "3", "4"], 2, "Nederlands, Frans en Duits."),
    wn("In het oosten van België spreken sommige mensen Duits.", True, "In de Oostkantons, vlak bij Duitsland, is Duits de taal."),
    inv("In Brussel spreken veel mensen Nederlands en ___.", ["Frans"], "Brussel is tweetalig: Nederlands en Frans."),
    wn("Luxemburg is enkel een land en geen Belgische provincie.", False, "Er is een land Luxemburg en ook een Belgische provincie Luxemburg."),
    mk("Wat is de hoofdstad van de provincie Namen?", ["Namen", "Charleroi", "Bergen", "Aarlen"], 0, "De stad Namen is de hoofdstad van de provincie Namen."),
    mk("In welke provincie ligt Genk?", ["Limburg", "Antwerpen", "Luik", "Henegouwen"], 0, "Genk ligt in Limburg, net als Hasselt."),
    wn("Mechelen is de hoofdstad van de provincie Antwerpen.", False, "Mechelen ligt in de provincie Antwerpen, maar de hoofdstad is Antwerpen."),
    mk("Hoeveel provincies liggen er in Vlaanderen?", ["3", "5", "7", "10"], 1, "West-Vlaanderen, Oost-Vlaanderen, Antwerpen, Vlaams-Brabant en Limburg."),
    inv("België is verdeeld in provincies, en die zijn verdeeld in ___. (g...)", ["gemeenten", "gemeentes"], "Elke stad of dorp hoort bij een gemeente."),
    wn("De koning van België woont in Brussel.", True, "Het koninklijk paleis staat in Brussel."),
]

DEEL_2 = [
    mk("Welk land is GEEN buurland van België?", ["Spanje", "Nederland", "Duitsland", "Frankrijk"], 0, "De buurlanden zijn Nederland, Duitsland, Luxemburg en Frankrijk."),
    inv("België heeft ___ buurlanden.", "4", "Nederland, Duitsland, Luxemburg en Frankrijk.", 4),
    mk("Aan welke zee ligt België?", ["de Noordzee", "de Middellandse Zee", "de Zwarte Zee", "de Oostzee"], 0, "De Belgische kust ligt aan de Noordzee."),
    wn("Oostende ligt aan de kust.", True, "Oostende is een bekende kuststad in West-Vlaanderen."),
    mk("Welke rivier stroomt door Antwerpen?", ["de Schelde", "de Maas", "de Rijn", "de Seine"], 0, "De Schelde loopt door Antwerpen naar de Noordzee."),
    mk("Welke rivier stroomt door Luik en Namen?", ["de Maas", "de Schelde", "de Leie", "de Demer"], 0, "De Maas komt uit Frankrijk en stroomt door Namen en Luik naar Nederland."),
    wn("De Demer stroomt door Hasselt.", True, "De Demer stroomt door Hasselt, Diest en Aarschot."),
    mk("Waar is België het hoogst?", ["in de Ardennen", "aan de kust", "in Antwerpen", "in Brussel"], 0, "Het hoogste punt, het Signaal van Botrange, ligt in de Ardennen."),
    wn("Aan de kust is het land heel bergachtig.", False, "Aan de kust is het land vlak, met duinen en een strand."),
    mk("Wat vind je aan de Belgische kust?", ["strand en duinen", "hoge bergen", "een woestijn", "vulkanen"], 0, "Langs de kust liggen strand en duinen."),
    inv("De Ardennen hebben veel heuvels en ___. (b...)", ["bossen", "bos"], "Er liggen grote bossen en er stromen beken en rivieren door diepe dalen."),
    wn("De haven van Antwerpen is een van de grootste havens van Europa.", True, "Daar komen schepen van over de hele wereld aan."),
    mk("Welk land ligt ten oosten van België?", ["Duitsland", "Frankrijk", "Engeland", "Spanje"], 0, "Duitsland ligt aan de oostkant van België."),
    mk("Welke kustgemeente ligt het dichtst bij Frankrijk?", ["De Panne", "Knokke-Heist", "Oostende", "Blankenberge"], 0, "De Panne ligt helemaal in het westen, vlak bij de Franse grens."),
    wn("De Kempen liggen aan de kust.", False, "De Kempen liggen in de provincies Antwerpen en Limburg, met veel heide en bossen."),
    mk("Hoe heet het vlakke, lage land met dijken langs de kust en de Schelde?", ["polders", "Ardennen", "bergen", "woestijn"], 0, "Polders zijn laaggelegen land, vroeger door de zee overspoeld."),
    inv("Een rivier stroomt uiteindelijk naar de ___.", ["zee"], "De Schelde en de Maas stromen naar de Noordzee."),
    wn("Frankrijk ligt ten noorden van België.", False, "Frankrijk ligt ten zuiden. Nederland ligt ten noorden."),
    mk("Welke streek ligt in het zuiden van België?", ["de Ardennen", "de Kempen", "de polders", "de kust"], 0, "De Ardennen liggen in het zuiden en zuidoosten."),
    wn("Je kan met de trein van Brussel naar Parijs.", True, "Er rijden snelle treinen tussen Brussel en Parijs."),
]
