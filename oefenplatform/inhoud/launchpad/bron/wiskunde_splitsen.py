# -*- coding: utf-8 -*-
"""Launchpad wiskunde: splitsen en verliefde harten (samen 10)."""
from lp import K, I, W
import lpprent as P

TITEL = "Splitsen en verliefde harten"
UITLEG_1 = "Een getal splitsen in twee stukken."
UITLEG_2 = "Verliefde harten: twee getallen die samen 10 zijn."

DEEL_1 = [
    I("7 splits je in 3 en ___", 4, "3 + 4 = 7.", 4),
    I("9 splits je in 5 en ___", 4, "5 + 4 = 9.", 4),
    I("6 splits je in 6 en ___", 0, "6 + 0 = 6.", 0),
    I("8 splits je in 2 en ___", 6, "2 + 6 = 8.", 6),
    I("5 splits je in 1 en ___", 4, "1 + 4 = 5.", 4),
    I("10 splits je in 7 en ___", 3, "7 + 3 = 10.", 3),
    K("Hoe kan je 8 splitsen?", "5 en 3", ["5 en 4", "6 en 3", "4 en 3"], "5 + 3 = 8.", None),
    K("Hoe kan je 6 splitsen?", "2 en 4", ["2 en 5", "3 en 4", "1 en 4"], "2 + 4 = 6.", None),
    K("4 en ... is samen 9.", "5", ["4", "6", "3"], "4 + 5 = 9.", 5),
    K("... en 2 is samen 7.", "5", ["4", "6", "9"], "5 + 2 = 7.", 5),
    W("7 kan je splitsen in 4 en 3.", True, "4 + 3 = 7."),
    W("9 kan je splitsen in 6 en 4.", False, "6 + 4 = 10, niet 9. Wel 6 en 3."),
    W("5 kan je splitsen in 0 en 5.", True, "0 + 5 = 5."),
    W("8 kan je splitsen in 4 en 5.", False, "4 + 4 = 8. Met 4 en 5 kom je op 9."),
    I("Je hebt 7 snoepjes in twee handen. In je linkerhand zitten er 2. Hoeveel in je rechterhand? ___", 5, "2 + 5 = 7.", 5),
    I("Op een bord liggen 9 koekjes: 6 rond en de rest vierkant. Hoeveel zijn vierkant? ___", 3, "6 + 3 = 9.", 3),
    K("Welke splitsing hoort NIET bij 6?", "3 en 4", ["1 en 5", "2 en 4", "6 en 0"], "3 + 4 = 7, niet 6."),
    K("Welke splitsing hoort bij 10?", "4 en 6", ["4 en 5", "3 en 6", "2 en 7"], "4 + 6 = 10."),
    W("Op hoeveel manieren je 4 ook splitst, samen blijft het altijd 4.", True, "3 en 1, 2 en 2, 4 en 0: samen altijd 4."),
    W("10 splitsen in 5 en 5 is hetzelfde als het dubbel van 5.", True, "5 + 5 = 10, het dubbel van 5."),
]

DEEL_2 = [
    I("Verliefde harten: 1 en ___", 9, "1 + 9 = 10.", 9),
    I("Verliefde harten: 3 en ___", 7, "3 + 7 = 10.", 7),
    I("Verliefde harten: 6 en ___", 4, "6 + 4 = 10.", 4),
    I("Verliefde harten: 8 en ___", 2, "8 + 2 = 10.", 2),
    I("Verliefde harten: 5 en ___", 5, "5 + 5 = 10.", 5),
    I("Verliefde harten: 0 en ___", 10, "0 + 10 = 10.", 10),
    K("Welk getal is het verliefde hart van 2?", "8", ["7", "9", "2"], "2 + 8 = 10.", 8),
    K("Welk getal is het verliefde hart van 9?", "1", ["0", "2", "9"], "9 + 1 = 10.", 1),
    K("Welke twee getallen zijn verliefde harten?", "3 en 7", ["3 en 6", "4 en 5", "2 en 9"], "3 + 7 = 10."),
    K("Welke twee getallen zijn GEEN verliefde harten?", "6 en 5", ["6 en 4", "1 en 9", "2 en 8"], "6 + 5 = 11, niet 10."),
    W("4 en 6 zijn verliefde harten.", True, "4 + 6 = 10."),
    W("7 en 4 zijn verliefde harten.", False, "7 + 4 = 11. Het verliefde hart van 7 is 3."),
    W("Het verliefde hart van 10 is 0.", True, "10 + 0 = 10."),
    W("2 en 7 zijn verliefde harten.", False, "2 + 7 = 9. Het verliefde hart van 2 is 8."),
    I("10 − 6 = ___", 4, "6 en 4 zijn verliefde harten: 10 − 6 = 4.", 4),
    I("10 − 3 = ___", 7, "3 en 7 zijn verliefde harten: 10 − 3 = 7.", 7),
    K("Je hebt 10 euro. Je koopt iets van 7 euro. Hoeveel krijg je terug?", "3 euro", ["4 euro", "2 euro", "7 euro"], "7 en 3 zijn verliefde harten.", None),
    K("Hoe helpt een verliefd hart bij 8 + 5?", "8 + 2 = 10, dan nog 3", ["8 + 5 = 10, dan nog 3", "8 + 3 = 10, dan nog 2", "5 + 5 = 10, dan nog 8"], "Het verliefde hart van 8 is 2. Je splitst 5 in 2 en 3."),
    W("Verliefde harten helpen je om over 10 te rekenen.", True, "Eerst naar 10, dan de rest erbij."),
    W("Het verliefde hart van 5 is 6.", False, "5 + 5 = 10, dus het verliefde hart van 5 is 5."),
]

PRENT_1 = [
    I("7 eendjes: links 3. Hoeveel staan er rechts?", 4, "3 + 4 = 7.", 4, prent=P.twee_groepen("splits-eend-3-4", ("lp-eendje", 3), ("lp-eendje", 4))),
    K("Welke splitsing zie je?", "9 = 5 + 4", ["9 = 6 + 3", "9 = 5 + 5", "8 = 5 + 3"], "Links 5 sterren, rechts 4.", None, prent=P.twee_groepen("splits-ster-5-4", ("lp-ster", 5), ("lp-ster", 4))),
    I("Je verstopt 5 van deze knikkers in je hand. Hoeveel zie je er nog?", 3, "8 = 5 + 3.", 3, prent=P.groep("splits-knikkers-8", "lp-knikker", 8)),
    W("Deze prent toont: 6 is 2 en 3.", False, "Je ziet 2 snoepjes en 4 snoepjes: 6 is 2 en 4.", prent=P.twee_groepen("splits-snoep-2-4", ("lp-snoepje", 2), ("lp-snoepje", 4))),
]
PRENT_2 = [
    I("Je plukt 3 van deze bloemen. Hoeveel blijven er staan?", 7, "3 en 7 zijn verliefde harten: 10 − 3 = 7.", 7, prent=P.groep("splits-bloemen-10", "lp-bloem", 10)),
    W("Het aantal beertjes links en rechts zijn verliefde harten.", True, "6 + 4 = 10.", prent=P.twee_groepen("splits-beer-6-4", ("lp-beertje", 6), ("lp-beertje", 4))),
    K("Hoeveel blokjes moeten erbij om 10 te hebben?", "2", ["3", "1", "8"], "8 en 2 zijn verliefde harten.", 2, prent=P.groep("splits-blokjes-8", "lp-blokje", 8)),
    W("Dit zijn samen 10 eendjes.", False, "7 + 2 = 9 eendjes.", prent=P.twee_groepen("splits-eend-7-2", ("lp-eendje", 7), ("lp-eendje", 2))),
]
