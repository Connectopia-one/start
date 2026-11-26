# -*- coding: utf-8 -*-
"""Ready wiskunde: Rekenen en cijferen (optellen en aftrekken tot 10 000,
cijferend vermenigvuldigen en delen met een getal van 1 of 2 cijfers,
rekenvolgorde en haakjes). Doel einde 4de leerjaar, Vlaamse overheid."""
from vr import mk, inv, wn

TITEL = "Rekenen en cijferen"
UITLEG_1 = 'Optellen en aftrekken onder elkaar.'
UITLEG_2 = 'Grote getallen maal en delen, en wat eerst?'

DEEL_1 = [
    mk("Hoeveel is 2 345 + 1 432?", ["3 777", "3 767", "4 777", "3 787"], 0, "Eenheden 5 + 2 = 7, tientallen 4 + 3 = 7, honderdtallen 3 + 4 = 7, duizendtallen 2 + 1 = 3: 3 777.", 3777),
    inv("4 568 + 1 275 = ___", ["5 843", "5843"], "8 + 5 = 13: schrijf 3, 1 door. 6 + 7 + 1 = 14: schrijf 4, 1 door. 5 + 2 + 1 = 8. 4 + 1 = 5. Samen 5 843.", 5843),
    mk("Hoeveel is 6 000 − 2 500?", ["4 500", "3 500", "3 000", "4 000"], 1, "6 000 − 2 000 = 4 000, en dan nog 500 eraf: 3 500.", 3500),
    inv("7 352 − 2 128 = ___", ["5 224", "5224"], "2 − 8 lukt niet: leen een tiental. 12 − 8 = 4, 4 − 2 = 2, 3 − 1 = 2, 7 − 2 = 5. Samen 5 224.", 5224),
    wn("Een aftrekking kijk je na met een optelling.", True, "Is 7 352 − 2 128 = 5 224, dan moet 5 224 + 2 128 weer 7 352 geven."),
    mk("Hoeveel is 3 999 + 1?", ["3 990", "4 000", "3 1000", "4 999"], 1, "Na 3 999 komt 4 000.", 4000),
    inv("Een school heeft 1 245 boeken. Er komen 380 boeken bij. Hoeveel boeken zijn er nu?", ["1 625", "1625"], "1 245 + 380 = 1 625.", 1625),
    mk("Mila spaart 2 400 euro voor een reis. Ze heeft al 1 750 euro. Hoeveel moet ze nog sparen?", ["650 euro", "750 euro", "1 650 euro", "4 150 euro"], 0, "2 400 − 1 750 = 650 euro.", 650),
    wn("Bij optellen mag je de getallen van plaats wisselen.", True, "1 200 + 300 is evenveel als 300 + 1 200."),
    wn("Bij aftrekken mag je de getallen van plaats wisselen.", False, "50 − 20 = 30, maar 20 − 50 is iets helemaal anders."),
    mk("Welke schatting past het best bij 3 980 + 2 010?", ["ongeveer 5 000", "ongeveer 6 000", "ongeveer 7 000", "ongeveer 60 000"], 1, "3 980 is ongeveer 4 000 en 2 010 ongeveer 2 000. Samen ongeveer 6 000."),
    inv("9 000 − 4 ___ = 4 700", "300", "9 000 − 4 700 = 4 300, dus het ontbrekende stuk is 300.", 300),
    mk("Welke bewerking geeft 5 000?", ["2 500 + 2 000", "6 000 − 1 000", "4 000 + 900", "3 500 + 1 400"], 1, "6 000 − 1 000 = 5 000. De andere geven 4 500, 4 900 en 4 900."),
    wn("1 000 − 1 = 999", True, "Eén minder dan 1 000 is 999."),
    inv("2 750 + 2 750 = ___", ["5 500", "5500"], "Het dubbele van 2 750: 2 × 2 000 = 4 000 en 2 × 750 = 1 500. Samen 5 500.", 5500),
    mk("Een boer heeft 1 200 kippen. Hij verkoopt er 450. Hoeveel kippen heeft hij nog?", ["850", "750", "650", "1 650"], 1, "1 200 − 400 = 800, en dan nog 50 eraf: 750.", 750),
    wn("8 400 + 600 = 8 1000", False, "8 400 + 600 = 9 000. Tien honderdtallen worden één duizendtal."),
    mk("Hoeveel is 5 030 − 40?", ["5 070", "4 990", "5 010", "4 970"], 1, "5 030 − 30 = 5 000, en dan nog 10 eraf: 4 990.", 4990),
    inv("Een vliegtuig vliegt 3 600 km heen en 3 600 km terug. Hoeveel km is dat samen?", ["7 200", "7200"], "3 600 + 3 600 = 7 200 km.", 7200),
    wn("Als je 2 000 bij 7 000 optelt, krijg je meer dan 10 000.", False, "7 000 + 2 000 = 9 000. Dat is minder dan 10 000."),
]

DEEL_2 = [
    mk("Hoeveel is 23 × 4?", ["82", "92", "812", "27"], 1, "20 × 4 = 80 en 3 × 4 = 12. Samen 92.", 92),
    inv("15 × 6 = ___", "90", "10 × 6 = 60 en 5 × 6 = 30. Samen 90.", 90),
    mk("Hoeveel is 125 × 3?", ["365", "375", "355", "128"], 1, "100 × 3 = 300, 20 × 3 = 60, 5 × 3 = 15. Samen 375.", 375),
    inv("12 × 11 = ___", "132", "12 × 10 = 120, en nog één keer 12 erbij: 132.", 132),
    mk("Hoeveel is 24 × 12?", ["248", "288", "268", "36"], 1, "24 × 10 = 240 en 24 × 2 = 48. Samen 288.", 288),
    wn("40 × 30 = 1 200", True, "4 × 3 = 12, en er komen twee nullen bij: 1 200."),
    mk("Hoeveel is 96 : 4?", ["24", "22", "26", "34"], 0, "80 : 4 = 20 en 16 : 4 = 4. Samen 24.", 24),
    inv("84 : 7 = ___", "12", "70 : 7 = 10 en 14 : 7 = 2. Samen 12.", 12),
    mk("Hoeveel is 156 : 12?", ["12", "13", "14", "16"], 1, "12 × 13 = 156. Reken na: 12 × 10 = 120 en 12 × 3 = 36.", 13),
    wn("75 : 5 = 14", False, "75 : 5 = 15, want 15 × 5 = 75."),
    mk("Hoeveel is 3 + 4 × 2?", ["14", "11", "10", "9"], 1, "Eerst vermenigvuldigen: 4 × 2 = 8. Dan optellen: 3 + 8 = 11.", 11),
    inv("(3 + 4) × 2 = ___", "14", "Eerst wat tussen haakjes staat: 3 + 4 = 7. Dan 7 × 2 = 14.", 14),
    mk("Hoeveel is 20 − 12 : 4?", ["2", "17", "8", "5"], 1, "Eerst delen: 12 : 4 = 3. Dan aftrekken: 20 − 3 = 17.", 17),
    wn("Bij 10 − 2 × 3 reken je eerst 10 − 2.", False, "Eerst vermenigvuldigen: 2 × 3 = 6. Dan 10 − 6 = 4."),
    inv("(20 − 5) : 3 = ___", "5", "Eerst tussen haakjes: 20 − 5 = 15. Dan 15 : 3 = 5.", 5),
    mk("Een klas koopt 28 schriften van 3 euro. Hoeveel betalen ze?", ["74 euro", "84 euro", "31 euro", "64 euro"], 1, "28 × 3: 20 × 3 = 60 en 8 × 3 = 24. Samen 84 euro.", 84),
    inv("Een bus heeft 48 plaatsen. Hoeveel plaatsen hebben 5 bussen samen?", "240", "48 × 5: 40 × 5 = 200 en 8 × 5 = 40. Samen 240.", 240),
    mk("Oma verdeelt 120 euro eerlijk over 8 kleinkinderen. Hoeveel krijgt elk?", ["12 euro", "15 euro", "16 euro", "20 euro"], 1, "120 : 8 = 15, want 15 × 8 = 120.", 15),
    wn("2 × 3 + 4 en 2 × (3 + 4) geven dezelfde uitkomst.", False, "2 × 3 + 4 = 6 + 4 = 10. 2 × (3 + 4) = 2 × 7 = 14. Haakjes veranderen de volgorde."),
    wn("Bij 5 × 2 + 1 begin je met de vermenigvuldiging.", True, "Eerst × en :, dan + en −. 5 × 2 = 10, daarna + 1 = 11."),
]
