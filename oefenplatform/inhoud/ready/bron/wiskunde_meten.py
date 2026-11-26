# -*- coding: utf-8 -*-
"""Ready wiskunde: Meten en geld (lengte km tot mm, gewicht kg en g, inhoud l en ml,
oppervlakte in m², dm², cm², omtrek en oppervlakte van vierkant en rechthoek,
volume met kubusjes, rekenen met euro en cent). Doel einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Meten en geld"
UITLEG_1 = "Lengte: 1 km = 1 000 m, 1 m = 100 cm, 1 cm = 10 mm. Gewicht: 1 kg = 1 000 g. Inhoud: 1 l = 1 000 ml. Geld: 1 euro = 100 cent."
UITLEG_2 = "Omtrek is de lengte van de rand: tel alle zijden op. Oppervlakte is hoeveel vierkantjes erin passen: lengte × breedte. Volume: tel de kubusjes."

DEEL_1 = [
    mk("Hoeveel meter is 1 kilometer?", ["10 m", "100 m", "1 000 m", "10 000 m"], 2, "Kilo betekent duizend: 1 km = 1 000 m."),
    inv("1 m = ___ cm", "100", "Centi betekent honderdste: er gaan 100 cm in 1 m.", 100),
    inv("3 cm = ___ mm", "30", "1 cm = 10 mm, dus 3 cm = 30 mm.", 30),
    mk("Hoeveel gram is 2 kg?", ["20 g", "200 g", "2 000 g", "20 000 g"], 2, "1 kg = 1 000 g, dus 2 kg = 2 000 g."),
    inv("1 l = ___ ml", ["1 000", "1000"], "Milli betekent duizendste: 1 l = 1 000 ml.", 1000),
    wn("Een halve liter is 500 ml.", True, "De helft van 1 000 ml is 500 ml."),
    mk("Wat meet je best in kilogram?", ["de lengte van een potlood", "het gewicht van een zak aardappelen", "de inhoud van een glas", "de afstand naar Brussel"], 1, "Kilogram is een maat voor gewicht."),
    mk("Welke lengte past bij de hoogte van een deur?", ["2 mm", "2 cm", "2 m", "2 km"], 2, "Een deur is ongeveer 2 meter hoog."),
    wn("250 cm is meer dan 2 m.", True, "2 m = 200 cm, en 250 cm is meer."),
    wn("1 kg veren is lichter dan 1 kg ijzer.", False, "Allebei wegen ze 1 kg. Het ijzer neemt wel minder plaats in."),
    inv("1 m 35 cm = ___ cm", "135", "1 m = 100 cm, en daar komen 35 cm bij: 135 cm.", 135),
    mk("Hoeveel kost het samen: een boek van 7,50 euro en een pen van 1,80 euro?", ["8,30 euro", "9,30 euro", "9,80 euro", "8,80 euro"], 1, "7,50 + 1,80: 7 + 1 = 8 euro, 50 + 80 = 130 cent = 1,30 euro. Samen 9,30 euro.", 9.3),
    inv("Je betaalt 5 euro voor een ijsje van 3,40 euro. Hoeveel krijg je terug? ___ euro", ["1,60", "1.60", "1,6"], "Van 3,40 naar 4 is 0,60. Van 4 naar 5 is 1. Samen 1,60 euro.", 1.6),
    wn("2 euro is evenveel als 200 cent.", True, "1 euro = 100 cent, dus 2 euro = 200 cent."),
    mk("Welke munten maken samen precies 1 euro?", ["50 cent + 20 cent + 20 cent", "50 cent + 20 cent + 20 cent + 10 cent", "50 cent + 50 cent + 10 cent", "20 cent + 20 cent + 20 cent"], 1, "50 + 20 + 20 + 10 = 100 cent = 1 euro."),
    inv("2 km 500 m = ___ m", ["2 500", "2500"], "2 km = 2 000 m, en daar komt 500 m bij: 2 500 m.", 2500),
    wn("Een fles water van 1,5 l bevat 150 ml.", False, "1,5 l = 1 500 ml."),
    mk("Een pakje boter weegt 250 g. Hoeveel pakjes zijn samen 1 kg?", ["2", "4", "5", "10"], 1, "4 × 250 g = 1 000 g = 1 kg.", 4),
    inv("Hoeveel cent is 3,05 euro? ___ cent", "305", "3 euro = 300 cent, en daar komen 5 cent bij: 305 cent.", 305),
    wn("Een kilometer is korter dan 900 meter.", False, "1 km = 1 000 m, en dat is meer dan 900 m."),
]

DEEL_2 = [
    mk("Een vierkant heeft zijden van 5 cm. Wat is de omtrek?", ["10 cm", "20 cm", "25 cm", "15 cm"], 1, "Een vierkant heeft 4 gelijke zijden: 4 × 5 cm = 20 cm."),
    inv("Een rechthoek is 6 cm lang en 4 cm breed. De omtrek is ___ cm.", "20", "6 + 4 + 6 + 4 = 20 cm.", 20),
    mk("Een rechthoek is 6 cm lang en 4 cm breed. Wat is de oppervlakte?", ["10 cm²", "20 cm²", "24 cm²", "24 cm"], 2, "Lengte × breedte: 6 × 4 = 24. Oppervlakte schrijf je in cm²."),
    inv("Een vierkant heeft zijden van 3 m. De oppervlakte is ___ m².", "9", "3 × 3 = 9 m².", 9),
    wn("Omtrek en oppervlakte zijn hetzelfde.", False, "Omtrek is de lengte van de rand. Oppervlakte is hoeveel plaats de figuur binnenin inneemt."),
    mk("Welke maat past bij de oppervlakte van een klaslokaal?", ["60 cm²", "60 dm²", "60 m²", "60 km²"], 2, "Een klaslokaal is ongeveer 8 m bij 7 of 8 m. Dat geeft zo'n 60 m²."),
    wn("Oppervlakte schrijf je met een kleine 2: bijvoorbeeld cm².", True, "De kleine 2 toont dat het om vierkante centimeters gaat."),
    mk("Hoeveel cm² past er in 1 dm²?", ["10", "100", "1 000", "20"], 1, "1 dm = 10 cm. Een vierkant van 10 cm bij 10 cm bevat 100 vierkantjes van 1 cm²."),
    inv("Een blok is gebouwd met 3 rijen van 4 kubusjes, en dat 2 lagen hoog. Hoeveel kubusjes zijn het? ___", "24", "Eén laag: 3 × 4 = 12. Twee lagen: 2 × 12 = 24 kubusjes.", 24),
    mk("Hoe bereken je de omtrek van een rechthoek van 8 m bij 3 m?", ["8 × 3", "8 + 3", "8 + 3 + 8 + 3", "8 × 3 × 2"], 2, "Omtrek is alle zijden samen: 8 + 3 + 8 + 3 = 22 m."),
    wn("Een vierkant van 4 cm bij 4 cm heeft een omtrek van 16 cm en een oppervlakte van 16 cm².", True, "Omtrek 4 × 4 = 16 cm. Oppervlakte 4 × 4 = 16 cm². Toevallig hetzelfde getal, maar een andere maat."),
    mk("Een tuin is 10 m lang en 5 m breed. Papa zet er een hek rond. Hoeveel meter hek heeft hij nodig?", ["15 m", "30 m", "50 m", "25 m"], 1, "Rond de tuin is de omtrek: 10 + 5 + 10 + 5 = 30 m."),
    inv("Een vloer is 4 m lang en 3 m breed. Hoeveel m² tegels heb je nodig? ___ m²", "12", "Oppervlakte: 4 × 3 = 12 m².", 12),
    wn("Een rechthoek van 2 cm bij 8 cm heeft een grotere oppervlakte dan een vierkant van 4 cm bij 4 cm.", False, "2 × 8 = 16 cm² en 4 × 4 = 16 cm². Ze zijn even groot."),
    mk("Wat meet je in kubusjes?", ["de omtrek", "de oppervlakte", "het volume", "de lengte"], 2, "Het volume is hoeveel ruimte iets inneemt. Dat meet je met kubusjes."),
    inv("Drie schriften van 2,50 euro kosten samen ___ euro.", ["7,50", "7.50", "7,5"], "3 × 2 euro = 6 euro en 3 × 50 cent = 1,50 euro. Samen 7,50 euro.", 7.5),
    mk("Een snoepje kost 15 cent. Hoeveel kosten 10 snoepjes?", ["1,05 euro", "1,50 euro", "15 euro", "0,25 euro"], 1, "10 × 15 cent = 150 cent = 1,50 euro.", 1.5),
    wn("Met een briefje van 10 euro kan je 3 boeken van 3,50 euro kopen.", False, "3 × 3,50 = 10,50 euro. Dat is meer dan 10 euro."),
    inv("Een rechthoek heeft een oppervlakte van 20 cm². Hij is 5 cm lang. Hoe breed is hij? ___ cm", "4", "Lengte × breedte = 20, en 5 × 4 = 20. Dus 4 cm breed.", 4),
    wn("Een kubus van 2 bij 2 bij 2 kubusjes bestaat uit 8 kubusjes.", True, "2 × 2 = 4 per laag, en 2 lagen: 8 kubusjes."),
]
