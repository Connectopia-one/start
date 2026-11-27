# -*- coding: utf-8 -*-
"""Launchpad wiskunde: getallen tot 20 (tellen, buren, meer en minder, tientallen en eenheden)."""
from lp import K, I, W
import lpprent as P

TITEL = "Getallen tot 20"
UITLEG_1 = "Tellen tot 20 en de buren van een getal."
UITLEG_2 = "Meer of minder, en 1 tiental en eenheden."

DEEL_1 = [
    K("Welk getal komt na 7?", "8", ["6", "9", "5"], "Na 7 komt 8.", 8),
    K("Welk getal komt voor 10?", "9", ["11", "8", "12"], "Voor 10 komt 9.", 9),
    I("Tel verder: 3, 4, 5, ___", 6, "Na 5 komt 6.", 6),
    I("Tel verder: 12, 13, 14, ___", 15, "Na 14 komt 15.", 15),
    K("Wat is de kleine buur van 15?", "14", ["16", "13", "5"], "De kleine buur is 1 minder: 14.", 14),
    K("Wat is de grote buur van 11?", "12", ["10", "13", "21"], "De grote buur is 1 meer: 12.", 12),
    W("Na 19 komt 20.", True, "19, 20. Klopt!"),
    W("Voor 6 komt 7.", False, "Voor 6 komt 5. Na 6 komt 7."),
    I("Tel terug: 10, 9, 8, ___", 7, "Terugtellen: na 8 komt 7.", 7),
    I("Tel terug: 18, 17, 16, ___", 15, "Na 16 komt bij terugtellen 15.", 15),
    K("Welk getal ligt tussen 12 en 14?", "13", ["11", "15", "16"], "12, 13, 14.", 13),
    K("Welk getal ligt tussen 4 en 6?", "5", ["3", "7", "8"], "4, 5, 6.", 5),
    W("Tussen 8 en 10 ligt 9.", True, "8, 9, 10."),
    W("17 is de kleine buur van 16.", False, "De kleine buur van 16 is 15. 17 is de grote buur."),
    K("Welk getal is het kleinste?", "3", ["13", "8", "10"], "3 is het kleinste getal.", 3),
    K("Welk getal is het grootste?", "18", ["8", "11", "15"], "18 is het grootste getal.", 18),
    I("Tel met sprongen van 2: 2, 4, 6, ___", 8, "Telkens 2 erbij: 6 + 2 = 8.", 8),
    I("Tel met sprongen van 2: 10, 12, 14, ___", 16, "14 + 2 = 16.", 16),
    W("0 is minder dan 1.", True, "Nul is niets, dat is minder dan 1."),
    W("Je zegt twintig voor het getal 12.", False, "12 zeg je twaalf. Twintig is 20."),
]

DEEL_2 = [
    K("13 is 1 tiental en ... eenheden.", "3", ["1", "13", "30"], "13 = 10 + 3: 1 tiental en 3 eenheden.", 3),
    K("1 tiental en 7 eenheden is ...", "17", ["71", "8", "70"], "10 + 7 = 17.", 17),
    I("10 + 5 = ___", 15, "1 tiental en 5 eenheden is 15.", 15),
    I("10 + 9 = ___", 19, "1 tiental en 9 eenheden is 19.", 19),
    K("Hoeveel eenheden heeft 20?", "0", ["2", "20", "10"], "20 = 2 tientallen en 0 eenheden.", 0),
    K("Welk getal is meer dan 14?", "16", ["12", "9", "14"], "16 komt na 14, dus 16 is meer.", 16),
    W("11 is meer dan 9.", True, "11 komt na 9, dus 11 is meer."),
    W("15 is minder dan 12.", False, "15 is meer dan 12."),
    K("Welk teken past? 8 ... 5", ">", ["<", "="], "8 is meer dan 5, dus 8 > 5. De open kant wijst naar het grootste getal."),
    K("Welk teken past? 7 ... 7", "=", ["<", ">"], "7 is evenveel als 7."),
    K("Welk teken past? 4 ... 9", "<", [">", "="], "4 is minder dan 9, dus 4 < 9."),
    I("Welk getal is 2 meer dan 10? ___", 12, "10 + 2 = 12.", 12),
    I("Welk getal is 3 minder dan 20? ___", 17, "20 − 3 = 17.", 17),
    W("1 tiental is evenveel als 10 eenheden.", True, "Een tiental zijn tien eenheden samen."),
    W("16 heeft 6 tientallen.", False, "16 heeft 1 tiental en 6 eenheden."),
    K("Zet in volgorde van klein naar groot.", "4, 9, 14, 19", ["19, 14, 9, 4", "9, 4, 19, 14", "4, 14, 9, 19"], "4 is het kleinste en 19 het grootste."),
    K("Welk getal is even?", "12", ["7", "15", "9"], "Even getallen kan je eerlijk in 2 verdelen: 12 = 6 + 6.", 12),
    K("Welk getal is oneven?", "11", ["10", "14", "8"], "11 kan je niet eerlijk in 2 verdelen: er blijft 1 over.", 11),
    W("Het dubbel van 6 is 12.", True, "6 + 6 = 12."),
    W("De helft van 10 is 4.", False, "De helft van 10 is 5: 5 + 5 = 10."),
]

PRENT_1 = [
    I("Hoeveel ballonnen zie je?", 7, "Een rij van 5 en nog 2: 7.", 7, prent=P.groep("tot20-ballonnen-7", "lp-ballon", 7)),
    I("Hoeveel eendjes zie je?", 12, "Twee rijen van 5 is 10, en nog 2: 12.", 12, prent=P.groep("tot20-eendjes-12", "lp-eendje", 12)),
    K("Hoeveel sterren zie je?", "9", ["8", "10", "6"], "Een rij van 5 en nog 4: 9.", 9, prent=P.groep("tot20-sterren-9", "lp-ster", 9)),
    W("Er liggen 15 knikkers.", True, "Drie rijen van 5: 15.", prent=P.groep("tot20-knikkers-15", "lp-knikker", 15)),
]
PRENT_2 = [
    I("Hoeveel blokjes zie je?", 13, "Twee rijen van 5 is 10, en nog 3: 13.", 13, prent=P.groep("tot20-blokjes-13", "lp-blokje", 13)),
    W("Er zitten 8 beertjes.", False, "Een rij van 5 en nog 1: 6 beertjes.", prent=P.groep("tot20-beertjes-6", "lp-beertje", 6)),
    I("Hoeveel snoepjes zie je?", 18, "Drie rijen van 5 is 15, en nog 3: 18.", 18, prent=P.groep("tot20-snoepjes-18", "lp-snoepje", 18)),
    K("Waarvan zijn er meer?", "eendjes", ["autootjes", "evenveel"], "5 eendjes en 3 autootjes: meer eendjes.", None, prent=P.twee_groepen("tot20-eend-auto", ("lp-eendje", 5), ("lp-speelgoedauto", 3))),
]
