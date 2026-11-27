# -*- coding: utf-8 -*-
"""Launchpad wiskunde: vlakke figuren, blokken en plaats in de ruimte."""
from lp import K, I, W
import lpprent as P

TITEL = "Vormen en ruimte"
UITLEG_1 = "Cirkel, vierkant, rechthoek en driehoek herkennen."
UITLEG_2 = "Links, rechts, boven, onder en blokken."

DEEL_1 = [
    I("Hoeveel hoeken heeft een driehoek? ___", 3, "Drie hoeken: daarom heet het een driehoek.", 3),
    I("Hoeveel hoeken heeft een vierkant? ___", 4, "Een vierkant heeft 4 hoeken.", 4),
    I("Hoeveel hoeken heeft een cirkel? ___", 0, "Een cirkel is helemaal rond: geen hoeken.", 0),
    I("Hoeveel zijden heeft een rechthoek? ___", 4, "Een rechthoek heeft 4 zijden.", 4),
    K("Welke vorm is helemaal rond?", "een cirkel", ["een vierkant", "een driehoek", "een rechthoek"], "Een cirkel heeft geen hoeken.", None),
    K("Welke vorm heeft 4 even lange zijden?", "een vierkant", ["een rechthoek", "een driehoek", "een cirkel"], "Bij een vierkant zijn alle zijden even lang.", None),
    K("Welke vorm heeft 3 zijden?", "een driehoek", ["een vierkant", "een cirkel", "een rechthoek"], "Drie zijden en drie hoeken.", None),
    K("Welke vorm heeft een deur?", "een rechthoek", ["een cirkel", "een driehoek", "een vierkant"], "Een deur is langer dan breed: een rechthoek.", None),
    K("Welke vorm heeft een wiel?", "een cirkel", ["een driehoek", "een vierkant", "een rechthoek"], "Een wiel is rond.", None),
    K("Welke vorm heeft een stuk pizza meestal?", "een driehoek", ["een cirkel", "een vierkant", "een rechthoek"], "Een punt pizza lijkt op een driehoek.", None),
    W("Een vierkant heeft 4 hoeken.", True, "Een vierkant heeft 4 hoeken en 4 zijden."),
    W("Een driehoek heeft 4 zijden.", False, "Een driehoek heeft 3 zijden."),
    W("Een cirkel heeft geen hoeken.", True, "Een cirkel is helemaal rond."),
    W("Een rechthoek heeft 3 hoeken.", False, "Een rechthoek heeft 4 hoeken."),
    W("Bij een rechthoek zijn twee zijden langer dan de andere twee.", True, "Twee lange en twee korte zijden."),
    W("Een munt is een driehoek.", False, "Een munt is rond: een cirkel."),
    I("Hoeveel hoeken hebben 2 driehoeken samen? ___", 6, "3 + 3 = 6.", 6),
    I("Hoeveel hoeken hebben een vierkant en een driehoek samen? ___", 7, "4 + 3 = 7.", 7),
    W("Een vierkant is ook een soort rechthoek.", True, "Een vierkant heeft 4 rechte hoeken, net zoals een rechthoek. Alleen zijn alle zijden even lang."),
    W("Een schoolbord is meestal een cirkel.", False, "Een schoolbord is meestal een rechthoek."),
]

DEEL_2 = [
    K("Met welke hand schrijven de meeste mensen?", "rechts", ["links", "boven", "onder"], "De meeste mensen schrijven met hun rechterhand.", None),
    K("De lamp hangt ... de tafel.", "boven", ["onder", "naast", "in"], "Een lamp hangt hoog, boven de tafel.", None),
    K("De kat slaapt ... het bed, op de grond.", "onder", ["boven", "op", "achter"], "Op de grond onder het bed.", None),
    K("Welk blok kan rollen?", "een bol", ["een kubus", "een balk", "een piramide"], "Een bol is helemaal rond.", None),
    K("Welk blok heeft de vorm van een dobbelsteen?", "een kubus", ["een bol", "een cilinder", "een kegel"], "Een dobbelsteen is een kubus: 6 vierkante vlakken.", None),
    K("Welk blok lijkt op een blikje?", "een cilinder", ["een kubus", "een bol", "een piramide"], "Een blikje is een cilinder: rond, met een plat vlak boven en onder.", None),
    K("Welk blok lijkt op een schoendoos?", "een balk", ["een bol", "een kegel", "een cilinder"], "Een schoendoos is een balk.", None),
    K("Welk blok lijkt op een ijshoorntje?", "een kegel", ["een kubus", "een balk", "een bol"], "Een ijshoorntje is een kegel: rond onderaan en een punt.", None),
    W("Een bal is een bol.", True, "Een bal is helemaal rond: een bol."),
    W("Een kubus kan goed rollen.", False, "Een kubus heeft platte vlakken en hoeken. Hij rolt niet."),
    W("Een dobbelsteen heeft 6 vlakken.", True, "Een kubus heeft 6 vlakken."),
    W("Je voeten staan boven je hoofd.", False, "Je voeten staan onder, je hoofd boven."),
    W("Als je in de spiegel je rechterhand opsteekt, lijkt het in de spiegel je linkerhand.", True, "Een spiegel draait links en rechts om."),
    W("Een cilinder heeft geen enkel plat vlak.", False, "Een cilinder heeft twee platte vlakken: boven en onder."),
    I("Hoeveel vlakken heeft een kubus? ___", 6, "Boven, onder, voor, achter, links en rechts: 6.", 6),
    I("Je zet 3 blokken op elkaar en dan nog 2. Hoe hoog is de toren in blokken? ___", 5, "3 + 2 = 5.", 5),
    K("Tim staat voor Sara in de rij. Wie staat achteraan?", "Sara", ["Tim", "allebei", "niemand"], "Tim staat vooraan, Sara achter hem.", None),
    K("De bal ligt tussen de stoel en de tafel. Waar ligt hij?", "in het midden", ["op de tafel", "onder de stoel", "ver weg"], "Tussen is in het midden.", None),
    W("Een piramide heeft een punt bovenaan.", True, "Alle schuine vlakken komen bovenaan samen in een punt."),
    W("Boven en onder betekenen hetzelfde.", False, "Boven is hoog, onder is laag."),
]

PRENT_1 = [
    K("Op welk blok lijkt deze bal?", "een bol", ["een kubus", "een kegel", "een cilinder"], "Een bal is helemaal rond: een bol.", None, prent=P.een("vormen-bal", "lp-bal")),
    K("Op welk blok lijkt deze dobbelsteen?", "een kubus", ["een bol", "een balk", "een piramide"], "Een dobbelsteen heeft 6 vierkante vlakken: een kubus.", None, prent=P.een("vormen-dobbelsteen", "lp-dobbelsteen")),
    K("Op welk blok lijkt dit feesthoedje?", "een kegel", ["een cilinder", "een kubus", "een bol"], "Rond onderaan en een punt bovenaan: een kegel.", None, prent=P.een("vormen-feesthoedje", "lp-feesthoedje")),
    W("Dit stuk pizza heeft de vorm van een driehoek.", True, "Het heeft drie hoeken: een driehoek.", prent=P.een("vormen-pizza", "lp-pizzapunt")),
]
PRENT_2 = [
    K("Welke vorm heeft deze deur?", "een rechthoek", ["een cirkel", "een driehoek", "een ruit"], "Een deur is langer dan breed: een rechthoek.", None, prent=P.een("vormen-deur", "lp-deur")),
    K("Welke vorm heeft deze klok?", "een cirkel", ["een vierkant", "een driehoek", "een rechthoek"], "De klok is rond: een cirkel.", None, prent=P.een("vormen-klok", "lp-wandklok")),
    W("Dit boek heeft de vorm van een cirkel.", False, "Het boek heeft 4 hoeken: een rechthoek.", prent=P.een("vormen-boek", "lp-boek")),
    K("Op welk blok lijkt dit glas?", "een cilinder", ["een bol", "een kubus", "een kegel"], "Rond, met een plat vlak onderaan: een cilinder.", None, prent=P.een("vormen-glas", "lp-glas-leeg")),
]
