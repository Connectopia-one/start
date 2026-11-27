# -*- coding: utf-8 -*-
"""Launchpad wiskunde: eerste tafels (2, 5 en 10) en eerlijk verdelen."""
from lp import K, I, W
import lpprent as P

TITEL = "Tafels van 2, 5 en 10"
UITLEG_1 = "Sprongen van 2, 5 en 10 maken."
UITLEG_2 = "Tafels gebruiken en eerlijk verdelen."

DEEL_1 = [
    I("2, 4, 6, 8, ___", 10, "Telkens 2 erbij: 8 + 2 = 10.", 10),
    I("5, 10, 15, 20, ___", 25, "Telkens 5 erbij: 20 + 5 = 25.", 25),
    I("10, 20, 30, 40, ___", 50, "Telkens 10 erbij: 40 + 10 = 50.", 50),
    I("12, 14, 16, ___", 18, "Telkens 2 erbij: 16 + 2 = 18.", 18),
    I("35, 40, 45, ___", 50, "Telkens 5 erbij: 45 + 5 = 50.", 50),
    I("60, 70, 80, ___", 90, "Telkens 10 erbij: 80 + 10 = 90.", 90),
    K("Welk getal hoort NIET in de rij van 2?", "7", ["6", "8", "4"], "7 is oneven. De rij van 2 heeft enkel even getallen.", 7),
    K("Welk getal hoort in de rij van 5?", "30", ["32", "27", "18"], "5, 10, 15, 20, 25, 30.", 30),
    K("Welk getal hoort in de rij van 10?", "70", ["75", "17", "71"], "Getallen van de rij van 10 eindigen op 0.", 70),
    K("Hoeveel ogen hebben 3 kinderen samen?", "6", ["5", "3", "9"], "2 + 2 + 2 = 6.", 6),
    W("In de rij van 10 eindigt elk getal op 0.", True, "10, 20, 30, 40, ... eindigen allemaal op 0."),
    W("15 hoort in de rij van 2.", False, "15 is oneven. Het hoort wel in de rij van 5."),
    W("In de rij van 5 eindigt elk getal op 0 of 5.", True, "5, 10, 15, 20, ... eindigen op 5 of 0."),
    W("20, 18, 16, 14 is de rij van 2 terug.", True, "Telkens 2 eraf."),
    W("40 hoort niet in de rij van 10.", False, "40 hoort er wel in: 10, 20, 30, 40."),
    W("De rij van 5 gaat 5, 10, 20, 25.", False, "15 ontbreekt: 5, 10, 15, 20, 25."),
    I("Hoeveel vingers hebben 4 handen samen? ___", 20, "5 + 5 + 5 + 5 = 20.", 20),
    I("Hoeveel schoenen hebben 5 kinderen samen? ___", 10, "2 + 2 + 2 + 2 + 2 = 10.", 10),
    I("Je hebt 3 briefjes van 10 euro. Hoeveel euro is dat? ___", 30, "10 + 10 + 10 = 30.", 30),
    K("Welke rij gaat telkens 5 terug?", "25, 20, 15", ["25, 23, 21", "25, 15, 5", "25, 24, 23"], "Telkens 5 eraf: 25, 20, 15."),
]

DEEL_2 = [
    I("3 × 2 = ___", 6, "3 keer 2: 2 + 2 + 2 = 6.", 6),
    I("4 × 5 = ___", 20, "4 keer 5: 5 + 5 + 5 + 5 = 20.", 20),
    I("6 × 10 = ___", 60, "6 keer 10 = 60.", 60),
    I("5 × 2 = ___", 10, "5 keer 2 = 10.", 10),
    I("7 × 5 = ___", 35, "5, 10, 15, 20, 25, 30, 35.", 35),
    I("9 × 10 = ___", 90, "9 keer 10 = 90.", 90),
    K("8 × 2 = ...", "16", ["10", "14", "18"], "8 keer 2: 2, 4, 6, 8, 10, 12, 14, 16.", 16),
    K("2 × 5 = ...", "10", ["7", "25", "12"], "2 keer 5: 5 + 5 = 10.", 10),
    K("Welke som hoort bij 4 × 2?", "2 + 2 + 2 + 2", ["4 + 2", "4 + 4 + 4 + 4", "2 + 2 + 2"], "4 keer 2 is 4 keer de 2."),
    K("Je verdeelt 10 koekjes eerlijk over 2 kinderen. Hoeveel krijgt elk kind?", "5", ["4", "2", "8"], "5 + 5 = 10.", 5),
    W("3 × 10 = 30", True, "10 + 10 + 10 = 30."),
    W("6 × 2 = 14", False, "6 × 2 = 12."),
    W("5 × 5 = 25", True, "5 + 5 + 5 + 5 + 5 = 25."),
    W("10 × 2 = 12", False, "10 × 2 = 20."),
    I("Je verdeelt 20 knikkers eerlijk over 2 zakjes. Hoeveel per zakje? ___", 10, "10 + 10 = 20.", 10),
    I("Je verdeelt 15 stickers eerlijk over 3 kinderen. Hoeveel krijgt elk kind? ___", 5, "5 + 5 + 5 = 15.", 5),
    K("In 1 doos zitten 10 eieren. Hoeveel eieren zitten in 4 dozen?", "40", ["14", "44", "30"], "4 × 10 = 40.", 40),
    K("Een fiets heeft 2 wielen. Hoeveel wielen hebben 7 fietsen?", "14", ["9", "12", "16"], "7 × 2 = 14.", 14),
    W("4 × 5 is evenveel als 5 × 4.", True, "Allebei 20."),
    W("Eerlijk verdelen betekent dat iedereen evenveel krijgt.", True, "Bij eerlijk verdelen krijgt iedereen hetzelfde."),
]

PRENT_1 = [
    I("Tel per 2. Hoeveel eendjes zie je?", 8, "2, 4, 6, 8.", 8, prent=P.groep("tafels-eendjes-8", "lp-eendje", 8, per=2)),
    I("Tel per 5. Hoeveel sterren zie je?", 15, "5, 10, 15.", 15, prent=P.groep("tafels-sterren-15", "lp-ster", 15, per=5)),
    W("Hier zijn 2 rijen van 10 snoepjes. Dat zijn 20 snoepjes.", True, "2 × 10 = 20.", prent=P.groep("tafels-snoepjes-20", "lp-snoepje", 20, per=10)),
    K("Welke som past bij de prent?", "5 × 2", ["2 × 2", "5 × 5", "10 × 2"], "5 rijen van 2 ballonnen.", None, prent=P.groep("tafels-ballonnen-10", "lp-ballon", 10, per=2)),
]
PRENT_2 = [
    I("In elke rij liggen 2 blokjes. Hoeveel rijen zijn er?", 6, "12 blokjes, 2 per rij: 6 rijen.", 6, prent=P.groep("tafels-blokjes-12", "lp-blokje", 12, per=2)),
    K("Welke som past bij de prent?", "5 × 5", ["5 × 2", "2 × 5", "10 × 5"], "5 rijen van 5 knikkers: 25.", None, prent=P.groep("tafels-knikkers-25", "lp-knikker", 25, per=5)),
    I("Je verdeelt deze beertjes eerlijk over 2 kinderen. Hoeveel krijgt elk kind?", 5, "10 beertjes over 2: elk 5.", 5, prent=P.groep("tafels-beertjes-10", "lp-beertje", 10, per=5)),
    W("Bij deze prent past 3 × 5 = 15.", False, "3 rijen van 10 bloemen: 3 × 10 = 30.", prent=P.groep("tafels-bloemen-30", "lp-bloem", 30, per=10)),
]
