# -*- coding: utf-8 -*-
"""Launchpad wiskunde: optellen en aftrekken tot 10 en tot 20."""
from lp import K, I, W
import lpprent as P

TITEL = "Optellen en aftrekken tot 20"
UITLEG_1 = "Erbij en eraf tot 10."
UITLEG_2 = "Erbij en eraf tot 20, ook over de 10."

DEEL_1 = [
    I("3 + 4 = ___", 7, "3 en er komen 4 bij: 7.", 7),
    I("5 + 5 = ___", 10, "5 + 5 = 10.", 10),
    I("8 − 3 = ___", 5, "8 en er gaan 3 af: 5.", 5),
    I("9 − 9 = ___", 0, "Alles eraf: 0.", 0),
    I("6 + 2 = ___", 8, "6, 7, 8.", 8),
    I("7 − 4 = ___", 3, "7 − 4 = 3.", 3),
    K("Welke som is 6?", "2 + 4", ["3 + 4", "1 + 4", "6 + 1"], "2 + 4 = 6.", None),
    K("Welke som is 9?", "10 − 1", ["10 − 2", "8 − 1", "9 − 1"], "10 − 1 = 9.", None),
    K("4 + ... = 10", "6", ["5", "4", "7"], "4 + 6 = 10.", 6),
    K("... − 2 = 5", "7", ["3", "6", "8"], "7 − 2 = 5.", 7),
    W("3 + 5 = 8", True, "3 + 5 = 8. Juist!"),
    W("10 − 4 = 5", False, "10 − 4 = 6."),
    W("2 + 7 is hetzelfde als 7 + 2.", True, "Bij optellen mag je wisselen: allebei 9."),
    W("6 − 0 = 0", False, "Er gaat niets af, dus 6 − 0 = 6."),
    I("Lien heeft 5 knikkers. Ze krijgt er 3 bij. Hoeveel heeft ze nu? ___", 8, "5 + 3 = 8.", 8),
    I("Er zitten 9 vogels op een tak. 4 vliegen weg. Hoeveel blijven er? ___", 5, "9 − 4 = 5.", 5),
    K("Wat is het dubbel van 4?", "8", ["6", "4", "10"], "4 + 4 = 8.", 8),
    K("Welke som past bij: 7 appels, 2 worden opgegeten?", "7 − 2", ["7 + 2", "2 − 7", "2 + 7"], "Er gaan er af, dus min."),
    W("5 + 4 is meer dan 8.", True, "5 + 4 = 9, en 9 is meer dan 8."),
    W("1 + 1 + 1 = 4", False, "1 + 1 + 1 = 3."),
]

DEEL_2 = [
    I("10 + 6 = ___", 16, "1 tiental en 6 eenheden: 16.", 16),
    I("13 + 4 = ___", 17, "3 + 4 = 7, dus 13 + 4 = 17.", 17),
    I("18 − 5 = ___", 13, "8 − 5 = 3, dus 18 − 5 = 13.", 13),
    I("8 + 5 = ___", 13, "8 + 2 = 10, en nog 3 erbij: 13.", 13),
    I("9 + 7 = ___", 16, "9 + 1 = 10, en nog 6: 16.", 16),
    I("14 − 6 = ___", 8, "14 − 4 = 10, en nog 2 eraf: 8.", 8),
    I("12 − 9 = ___", 3, "12 − 2 = 10, en nog 7 eraf: 3.", 3),
    K("7 + 6 = ...", "13", ["12", "14", "11"], "7 + 3 = 10, en nog 3: 13.", 13),
    K("15 − 7 = ...", "8", ["7", "9", "12"], "15 − 5 = 10, en nog 2 eraf: 8.", 8),
    K("Hoe reken je 8 + 6 slim?", "8 + 2 + 4", ["8 + 3 + 4", "6 + 6 + 1", "8 + 1 + 6"], "Eerst naar 10: 8 + 2 = 10, dan nog 4: 14."),
    W("9 + 9 = 18", True, "Het dubbel van 9 is 18."),
    W("16 − 8 = 9", False, "16 − 8 = 8, want 8 + 8 = 16."),
    W("20 − 10 = 10", True, "Twee tientallen min één tiental: 10."),
    W("6 + 7 = 12", False, "6 + 7 = 13."),
    I("Mo heeft 12 stickers. Hij geeft er 5 weg. Hoeveel houdt hij? ___", 7, "12 − 5 = 7.", 7),
    I("In de bus zitten 8 kinderen. Er stappen 7 kinderen bij op. Hoeveel zijn er nu? ___", 15, "8 + 7 = 15.", 15),
    K("Welke som is 11?", "5 + 6", ["5 + 5", "4 + 6", "6 + 6"], "5 + 6 = 11.", None),
    K("... + 9 = 17", "8", ["7", "9", "6"], "8 + 9 = 17.", 8),
    W("Als 7 + 8 = 15, dan is 15 − 8 = 7.", True, "Plus en min horen bij elkaar."),
    W("19 − 9 = 1", False, "19 − 9 = 10."),
]

PRENT_1 = [
    I("Hoeveel ballonnen zijn het samen?", 7, "4 + 3 = 7.", 7, prent=P.twee_groepen("plus20-ballon-4-3", ("lp-ballon", 4), ("lp-ballon", 3))),
    I("Hoeveel sterren zijn het samen?", 13, "8 + 2 = 10, en nog 3: 13.", 13, prent=P.twee_groepen("plus20-ster-8-5", ("lp-ster", 8), ("lp-ster", 5))),
    I("Hier zwemmen 9 eendjes. Er zwemmen er 3 weg. Hoeveel blijven er?", 6, "9 − 3 = 6.", 6, prent=P.groep("plus20-eendjes-9", "lp-eendje", 9)),
    W("Bij deze prent past 6 + 6 = 12.", True, "6 snoepjes en 6 snoepjes: 12.", prent=P.twee_groepen("plus20-snoep-6-6", ("lp-snoepje", 6), ("lp-snoepje", 6))),
]
PRENT_2 = [
    I("Je geeft 5 van deze knikkers weg. Hoeveel hou je over?", 9, "14 − 5 = 9.", 9, prent=P.groep("plus20-knikkers-14", "lp-knikker", 14)),
    K("Welke som past bij de prent?", "7 + 4", ["7 + 3", "6 + 4", "4 + 4"], "Links 7 autootjes, rechts 4.", None, prent=P.twee_groepen("plus20-auto-7-4", ("lp-speelgoedauto", 7), ("lp-speelgoedauto", 4))),
    W("Als 2 beertjes weggaan, blijven er 7.", False, "Er zijn 10 beertjes. 10 − 2 = 8.", prent=P.groep("plus20-beertjes-10", "lp-beertje", 10)),
    I("Hoeveel blokjes zijn het samen?", 18, "Het dubbel van 9 is 18.", 18, prent=P.twee_groepen("plus20-blok-9-9", ("lp-blokje", 9), ("lp-blokje", 9))),
]
