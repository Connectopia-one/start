# -*- coding: utf-8 -*-
"""Launchpad wiskunde: getallen tot 100 (tientallen en eenheden, buren, ordenen, sprongen)."""
from lp import K, I, W
import lpprent as P

TITEL = "Getallen tot 100"
UITLEG_1 = "Tientallen en eenheden tot 100."
UITLEG_2 = "Buren, volgorde en sprongen van 10."

DEEL_1 = [
    K("4 tientallen en 6 eenheden is ...", "46", ["64", "10", "406"], "4 T = 40, plus 6 E: 46.", 46),
    K("Hoeveel tientallen heeft 73?", "7", ["3", "73", "10"], "73 = 7 tientallen en 3 eenheden.", 7),
    K("Hoeveel eenheden heeft 58?", "8", ["5", "58", "13"], "58 = 5 tientallen en 8 eenheden.", 8),
    I("30 + 4 = ___", 34, "3 tientallen en 4 eenheden: 34.", 34),
    I("60 + 9 = ___", 69, "6 tientallen en 9 eenheden: 69.", 69),
    I("80 + 0 = ___", 80, "8 tientallen en 0 eenheden: 80.", 80),
    W("10 tientallen is 100.", True, "10 × 10 = 100: honderd."),
    W("In 25 zitten 5 tientallen.", False, "25 = 2 tientallen en 5 eenheden."),
    K("Hoe schrijf je vijfenveertig?", "45", ["54", "405", "40"], "Vijfenveertig: eerst hoor je de 5, maar je schrijft 4 tientallen en 5 eenheden: 45.", 45),
    K("Hoe schrijf je achtendertig?", "38", ["83", "308", "48"], "Achtendertig = 3 tientallen en 8 eenheden: 38.", 38),
    K("Hoe zeg je 92?", "tweeënnegentig", ["negenentwintig", "negentig", "twaalf"], "92 = 9 tientallen en 2 eenheden: tweeënnegentig."),
    I("Hoeveel tientallen heeft 100? ___", 10, "100 = 10 tientallen.", 10),
    W("In 61 zitten 6 tientallen en 1 eenheid.", True, "60 + 1 = 61."),
    W("Zesenzeventig schrijf je als 67.", False, "Zesenzeventig schrijf je als 76."),
    K("Welk getal heeft 2 tientallen en 9 eenheden?", "29", ["92", "11", "27"], "20 + 9 = 29.", 29),
    K("50 + 7 = ...", "57", ["75", "12", "507"], "5 tientallen en 7 eenheden.", 57),
    I("Hoeveel eenheden zijn 3 tientallen? ___", 30, "1 tiental is 10 eenheden, dus 3 tientallen zijn 30 eenheden.", 30),
    I("7 tientallen en 7 eenheden = ___", 77, "70 + 7 = 77.", 77),
    W("Het getal 40 heeft 0 eenheden.", True, "40 = 4 tientallen en 0 eenheden."),
    W("Negenennegentig is het grootste getal met twee cijfers.", True, "99 is het grootste. Daarna komt 100, met drie cijfers."),
]

DEEL_2 = [
    K("Wat is de grote buur van 39?", "40", ["38", "49", "30"], "39 + 1 = 40.", 40),
    K("Wat is de kleine buur van 70?", "69", ["71", "60", "79"], "70 − 1 = 69.", 69),
    I("Tel verder met sprongen van 10: 15, 25, 35, ___", 45, "Telkens 10 erbij: 35 + 10 = 45.", 45),
    I("Tel terug met sprongen van 10: 90, 80, 70, ___", 60, "Telkens 10 eraf: 70 − 10 = 60.", 60),
    K("Welk getal ligt tussen 56 en 58?", "57", ["55", "59", "67"], "56, 57, 58.", 57),
    K("Welk getal is het grootste?", "81", ["18", "79", "80"], "81 heeft 8 tientallen en 1 eenheid, meer dan 80 en 79.", 81),
    K("Welk getal is het kleinste?", "19", ["91", "29", "21"], "19 heeft maar 1 tiental.", 19),
    W("64 is meer dan 46.", True, "64 heeft 6 tientallen, 46 maar 4."),
    W("Na 59 komt 70.", False, "Na 59 komt 60."),
    K("Welk teken past? 37 ... 73", "<", [">", "="], "37 is minder dan 73."),
    K("Welk teken past? 90 ... 89", ">", ["<", "="], "90 is meer dan 89."),
    I("Tel met sprongen van 5: 20, 25, 30, ___", 35, "30 + 5 = 35.", 35),
    I("Welk getal is 10 meer dan 47? ___", 57, "Een tiental erbij: 47 + 10 = 57.", 57),
    W("Na 99 komt 100.", True, "99 + 1 = 100."),
    W("De kleine buur van 50 is 51.", False, "De kleine buur van 50 is 49."),
    K("Zet van klein naar groot.", "12, 21, 50, 65", ["65, 50, 21, 12", "21, 12, 50, 65", "12, 50, 21, 65"], "Kijk eerst naar de tientallen."),
    K("Welk getal ligt het dichtst bij 50?", "48", ["40", "60", "35"], "48 ligt maar 2 van 50.", 48),
    K("Welk getal is 10 minder dan 63?", "53", ["73", "62", "43"], "63 − 10 = 53.", 53),
    W("Tussen 30 en 40 liggen 9 getallen.", True, "31, 32, 33, 34, 35, 36, 37, 38, 39: dat zijn er 9."),
    W("Tel je met sprongen van 10 vanaf 4, dan kom je op 14, 24, 34.", True, "Telkens komt er een tiental bij, de eenheden blijven 4."),
]

PRENT_1 = [
    I("Elke volle rij heeft 10 knikkers. Hoeveel knikkers zie je?", 23, "2 volle rijen is 20, en nog 3: 23.", 23, prent=P.groep("tot100-knikkers-23", "lp-knikker", 23, per=10)),
    W("Hier liggen 3 rijen van 10 sterren. Dat zijn 13 sterren.", False, "3 rijen van 10 is 30, niet 13.", prent=P.groep("tot100-sterren-30", "lp-ster", 30, per=10)),
    K("Elke volle rij heeft 10 snoepjes. Hoeveel zijn het er?", "41", ["14", "40", "42"], "4 tientallen en 1 eenheid: 41.", 41, prent=P.groep("tot100-snoepjes-41", "lp-snoepje", 41, per=10)),
    I("Elke volle rij heeft 10 ballonnen. Hoeveel ballonnen zie je?", 25, "2 tientallen en 5 eenheden: 25.", 25, prent=P.groep("tot100-ballonnen-25", "lp-ballon", 25, per=10)),
]
PRENT_2 = [
    I("Hoeveel euro is dit samen?", 35, "10 + 10 + 10 = 30, en nog 5: 35.", 35, prent=P.munten("tot100-geld-35", [10, 10, 10, 5])),
    K("Hoeveel geld zie je, in euro?", "42", ["24", "40", "22"], "20 + 20 = 40, en nog 2: 42.", 42, prent=P.munten("tot100-geld-42", [20, 20, 2])),
    W("Dit is samen 30 euro.", False, "4 briefjes van 10: 40 euro.", prent=P.munten("tot100-geld-40", [10, 10, 10, 10])),
    I("Elke rij heeft 10 blokjes. Hoeveel blokjes zie je?", 50, "5 rijen van 10: 50.", 50, prent=P.groep("tot100-blokjes-50", "lp-blokje", 50, per=10)),
]
