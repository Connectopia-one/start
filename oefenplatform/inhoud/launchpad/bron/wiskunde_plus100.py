# -*- coding: utf-8 -*-
"""Launchpad wiskunde: optellen en aftrekken tot 100 (eerst zonder, dan met brug)."""
from lp import K, I, W
import lpprent as P

TITEL = "Optellen en aftrekken tot 100"
UITLEG_1 = "Tientallen erbij en eraf."
UITLEG_2 = "Over het tiental heen rekenen."

DEEL_1 = [
    I("30 + 20 = ___", 50, "3 T + 2 T = 5 T: 50.", 50),
    I("70 − 40 = ___", 30, "7 T − 4 T = 3 T: 30.", 30),
    I("45 + 3 = ___", 48, "5 + 3 = 8, dus 48.", 48),
    I("67 − 5 = ___", 62, "7 − 5 = 2, dus 62.", 62),
    I("23 + 40 = ___", 63, "23 + 40: de tientallen 2 + 4 = 6, dus 63.", 63),
    I("88 − 30 = ___", 58, "8 T − 3 T = 5 T, dus 58.", 58),
    I("34 + 25 = ___", 59, "34 + 20 = 54, en nog 5: 59.", 59),
    I("76 − 24 = ___", 52, "76 − 20 = 56, en nog 4 eraf: 52.", 52),
    K("52 + 6 = ...", "58", ["57", "59", "112"], "2 + 6 = 8, dus 58.", 58),
    K("90 − 50 = ...", "40", ["30", "50", "45"], "9 T − 5 T = 4 T.", 40),
    K("41 + 37 = ...", "78", ["77", "68", "88"], "41 + 30 = 71, en nog 7: 78.", 78),
    K("Welke som is 60?", "40 + 20", ["40 + 30", "30 + 20", "50 + 20"], "4 T + 2 T = 6 T.", None),
    W("60 + 30 = 90", True, "6 T + 3 T = 9 T."),
    W("55 − 5 = 45", False, "55 − 5 = 50."),
    W("12 + 12 = 24", True, "Het dubbel van 12 is 24."),
    W("100 − 50 = 60", False, "De helft van 100 is 50, dus 100 − 50 = 50."),
    I("Een boek heeft 45 bladzijden. Je las er al 20. Hoeveel moet je nog lezen? ___", 25, "45 − 20 = 25.", 25),
    I("In de klas liggen 32 potloden en 6 stiften. Hoeveel zijn het er samen? ___", 38, "32 + 6 = 38.", 38),
    W("Bij 43 + 10 verandert enkel het tiental.", True, "43 + 10 = 53: de 4 wordt een 5, de 3 blijft."),
    W("80 − 1 = 70", False, "80 − 1 = 79."),
]

DEEL_2 = [
    I("38 + 5 = ___", 43, "38 + 2 = 40, en nog 3: 43.", 43),
    I("47 + 6 = ___", 53, "47 + 3 = 50, en nog 3: 53.", 53),
    I("52 − 7 = ___", 45, "52 − 2 = 50, en nog 5 eraf: 45.", 45),
    I("61 − 4 = ___", 57, "61 − 1 = 60, en nog 3 eraf: 57.", 57),
    I("29 + 13 = ___", 42, "29 + 10 = 39, en nog 3: 42.", 42),
    I("74 − 16 = ___", 58, "74 − 10 = 64, en nog 6 eraf: 58.", 58),
    I("56 + 28 = ___", 84, "56 + 20 = 76, en nog 8: 84.", 84),
    I("93 − 45 = ___", 48, "93 − 40 = 53, en nog 5 eraf: 48.", 48),
    K("26 + 8 = ...", "34", ["33", "24", "35"], "26 + 4 = 30, en nog 4: 34.", 34),
    K("43 − 9 = ...", "34", ["36", "33", "44"], "43 − 3 = 40, en nog 6 eraf: 34.", 34),
    K("65 + 17 = ...", "82", ["72", "81", "83"], "65 + 10 = 75, en nog 7: 82.", 82),
    K("Hoe reken je 37 + 6 slim?", "37 + 3 + 3", ["37 + 6 + 3", "30 + 6 + 3", "37 + 4 + 3"], "Eerst naar 40 (37 + 3), dan nog 3: 43."),
    W("19 + 19 = 38", True, "20 + 20 = 40, en 2 minder: 38."),
    W("50 − 8 = 48", False, "50 − 8 = 42."),
    W("27 + 5 = 32", True, "27 + 3 = 30, en nog 2: 32."),
    W("81 − 3 = 79", False, "81 − 3 = 78."),
    I("Oma is 68 jaar. Opa is 7 jaar ouder. Hoe oud is opa? ___", 75, "68 + 7 = 75.", 75),
    I("Een strip kost 9 euro. Je hebt 30 euro. Hoeveel hou je over? ___", 21, "30 − 9 = 21.", 21),
    W("Als 46 + 7 = 53, dan is 53 − 7 = 46.", True, "Plus en min horen bij elkaar."),
    W("99 + 1 = 90", False, "99 + 1 = 100."),
]

PRENT_1 = [
    I("Hoeveel euro is dit samen?", 35, "20 + 10 = 30, en nog 5: 35.", 35, prent=P.munten("plus100-geld-35", [20, 10, 5])),
    K("Hoeveel geld zie je, in euro?", "70", ["60", "80", "52"], "50 + 20 = 70.", 70, prent=P.munten("plus100-geld-70", [50, 20])),
    I("Elke rij heeft 10 knikkers. Er komen er 5 bij. Hoeveel zijn het er dan?", 35, "30 + 5 = 35.", 35, prent=P.groep("plus100-knikkers-30", "lp-knikker", 30, per=10)),
    W("Samen is dit 60 euro.", True, "20 + 20 + 20 = 60.", prent=P.munten("plus100-geld-60", [20, 20, 20])),
]
PRENT_2 = [
    I("Tel het geld. Hoeveel euro is het?", 74, "50 + 10 + 10 = 70, en nog 2 + 2: 74.", 74, prent=P.munten("plus100-geld-74", [50, 10, 10, 2, 2])),
    W("Dit is samen 25 euro.", False, "20 + 5 + 1 = 26 euro.", prent=P.munten("plus100-geld-26", [20, 5, 1])),
    K("Elke rij heeft 10 sterren. Je geeft er 8 weg. Hoeveel blijven er?", "32", ["42", "48", "31"], "40 − 8 = 32.", 32, prent=P.groep("plus100-sterren-40", "lp-ster", 40, per=10)),
    I("Je betaalt 30 euro van dit geld. Hoeveel euro hou je over?", 20, "50 − 30 = 20.", 20, prent=P.munten("plus100-geld-50", [10, 10, 10, 10, 10])),
]
