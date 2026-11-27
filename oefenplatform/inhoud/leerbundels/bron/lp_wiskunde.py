# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de Launchpad-hoofdstukken wiskunde (1ste en 2de leerjaar).
De vragen op het scherm staan in ../../launchpad/bron/wiskunde_*.py; de oefenbundels
vragen andere getallen.

    python3 lp_wiskunde.py          # alles
    python3 lp_wiskunde.py klok     # één hoofdstuk
"""
import sys
from lp_gemeen import maak, tabel, svg, stippen, munt, LP, HOE, ON, DARK, ORANJE, GROEN
from ready_wiskunde import klok, figuren

V = "Wiskunde"; B = "70px"
H = {}


def L(titel, onder, secties, onthoud):
    return dict(vak=V, niveau=LP, titel=titel, onder=onder, secties=secties, onthoud=onthoud)


def O(titel, reeksen):
    return dict(vak=V, niveau=LP, titel=titel, onder=ON, hoe=HOE, reeksen=reeksen)


H["tot20"] = ("getallen-tot-20-launchpad", "wiskunde-tot20", L("Getallen tot 20", "Tellen, getallen schrijven, buren en de getallenlijn tot 20.", [
    dict(kop="Tellen", blokken=[("p", "Tel elk ding één keer. Wijs met je vinger mee. Het laatste getal dat je zegt, is hoeveel het er zijn."),
        ("fig", stippen(7), "7 stippen: een rijtje van 5 en nog 2")]),
    dict(kop="Tien en nog wat", blokken=[("p", "13 is <strong>1 tiental</strong> en <strong>3 eenheden</strong>: 10 en nog 3."),
        ("fig", stippen(13), "13 = 10 + 3")]),
    dict(kop="Buren", blokken=[("p", "De buren van 8 zijn <strong>7</strong> (één minder) en <strong>9</strong> (één meer)."),
        ("kader", "0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 10 · 11 · 12 · 13 · 14 · 15 · 16 · 17 · 18 · 19 · 20")]),
    dict(kop="Meer of minder", blokken=[("p", "Hoe verder op de getallenlijn, hoe meer. 15 is meer dan 12. We schrijven 15 &gt; 12. De open kant van het teken wijst naar het grootste getal."),
        ("weetje", "Even getallen kan je eerlijk in twee verdelen: 2, 4, 6, 8, 10 ... Oneven getallen niet: 1, 3, 5, 7, 9 ...")]),
], ["Tel elk ding één keer.", "13 = 1 tiental en 3 eenheden.", "Buren: één minder en één meer.", "&gt; en &lt;: de open kant wijst naar het grootste."]),
    O("Getallen tot 20", [
        dict(kop="Hoeveel stippen?", oefeningen=[("fig", [(stippen(6), "6"), (stippen(9), "9"), (stippen(12), "12"), (stippen(17), "17")], "Tel en schrijf het getal.")]),
        dict(kop="Buren", oefeningen=[("rij", [("__ 5 __", "4 en 6"), ("__ 10 __", "9 en 11"), ("__ 14 __", "13 en 15"), ("__ 19 __", "18 en 20")], "Schrijf de buren.", "110px")]),
        dict(kop="Wat ontbreekt?", oefeningen=[("rij", [("3, 4, __, 6", "5"), ("11, 12, __, 14", "13"), ("16, __, 18, 19", "17"), ("20, 19, __, 17", "18")], "", B)]),
        dict(kop="Tien en nog wat", oefeningen=[("rij", [("10 + 4 =", "14"), ("10 + 8 =", "18"), ("10 + 1 =", "11"), ("15 = 10 +", "5")], "", B)]),
        dict(kop="Groter of kleiner?", opdracht="Schrijf &gt; of &lt;.", oefeningen=[("rij", [("7 __ 9", "&lt;"), ("15 __ 11", "&gt;"), ("20 __ 2", "&gt;"), ("13 __ 16", "&lt;")], "", B)]),
        dict(kop="Even of oneven?", oefeningen=[("waar", "8 is even.", True), ("waar", "11 is even.", False), ("waar", "15 is oneven.", True)]),
    ]))

H["tot100"] = ("getallen-tot-100-launchpad", "wiskunde-tot100", L("Getallen tot 100", "Tientallen en eenheden, tellen met sprongen van 10 en getallen vergelijken tot 100.", [
    dict(kop="Tientallen en eenheden", blokken=[("fig", tabel(["T", "E", "getal"], [["4", "7", "47"], ["6", "0", "60"], ["8", "3", "83"]], "50%")),
        ("p", "In 47 staat de <strong>4</strong> voor 4 tientallen (40) en de <strong>7</strong> voor 7 eenheden.")]),
    dict(kop="Sprongen van 10", blokken=[("kader", "10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100"),
        ("p", "Bij +10 verandert enkel het tiental: 34 → 44 → 54.")]),
    dict(kop="Vergelijken", blokken=[("p", "Kijk eerst naar de tientallen. 52 is meer dan 48, want 5 T is meer dan 4 T. Zijn de tientallen gelijk, kijk dan naar de eenheden: 63 &gt; 61.")]),
], ["Eerst T, dan E.", "+10 verandert het tiental.", "Vergelijk eerst de tientallen."]),
    O("Getallen tot 100", [
        dict(kop="Schrijf het getal", oefeningen=[("rij", [("3 T en 5 E", "35"), ("7 T en 2 E", "72"), ("9 T en 0 E", "90"), ("1 T en 8 E", "18")], "", B)]),
        dict(kop="T en E", oefeningen=[("tabel", ["getal", "T", "E"], [["56", None, None], ["81", None, None], ["29", None, None]], "56: 5 T 6 E · 81: 8 T 1 E · 29: 2 T 9 E", "60px")]),
        dict(kop="Spring met 10", oefeningen=[("rij", [("12, 22, __, 42", "32"), ("45, 55, 65, __", "75"), ("90, 80, __, 60", "70")], "", B)]),
        dict(kop="Buren", oefeningen=[("rij", [("__ 40 __", "39 en 41"), ("__ 67 __", "66 en 68"), ("__ 99 __", "98 en 100")], "", "110px")]),
        dict(kop="Groter of kleiner?", opdracht="Schrijf &gt; of &lt;.", oefeningen=[("rij", [("38 __ 83", "&lt;"), ("71 __ 17", "&gt;"), ("54 __ 59", "&lt;"), ("90 __ 89", "&gt;")], "", B)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "In 64 staat de 6 voor 6 tientallen.", True), ("waar", "45 is meer dan 54.", False)]),
    ]))

H["plus20"] = ("optellen-en-aftrekken-tot-20-launchpad", "wiskunde-plus20", L("Optellen en aftrekken tot 20", "Erbij en eraf tot 10, dubbels, en over 10 heen met een tussenstap.", [
    dict(kop="Erbij en eraf", blokken=[("p", "<strong>+</strong> betekent erbij: 4 + 3 = 7. <strong>−</strong> betekent eraf: 9 − 4 = 5."),
        ("fig", stippen(7), "4 + 3 = 7")]),
    dict(kop="Dubbels", blokken=[("fig", tabel(["1 + 1", "2 + 2", "3 + 3", "4 + 4", "5 + 5"], [["2", "4", "6", "8", "10"]], "70%")),
        ("p", "Ken je 6 + 6 = 12, dan weet je ook 6 + 7 = 13.")]),
    dict(kop="Over 10 heen", blokken=[("kader", "8 + 5 = ?<br>8 + <strong>2</strong> = 10, en nog <strong>3</strong>: 13"),
        ("kader", "13 − 5 = ?<br>13 − <strong>3</strong> = 10, en nog <strong>2</strong> eraf: 8")]),
], ["+ is erbij, − is eraf.", "Dubbels helpen.", "Over 10: eerst naar 10, dan de rest."]),
    O("Optellen en aftrekken tot 20", [
        dict(kop="Tot 10", oefeningen=[("rij", [("3 + 4 =", "7"), ("6 + 2 =", "8"), ("9 − 3 =", "6"), ("8 − 5 =", "3"), ("5 + 5 =", "10"), ("10 − 7 =", "3")], "", B)]),
        dict(kop="Dubbels", oefeningen=[("rij", [("7 + 7 =", "14"), ("8 + 8 =", "16"), ("9 + 9 =", "18"), ("6 + 7 =", "13")], "", B)]),
        dict(kop="Over 10", oefeningen=[("rij", [("9 + 4 =", "13"), ("7 + 6 =", "13"), ("8 + 7 =", "15"), ("6 + 9 =", "15")], "", B),
            ("rij", [("12 − 5 =", "7"), ("14 − 6 =", "8"), ("11 − 3 =", "8"), ("16 − 9 =", "7")], "", B)]),
        dict(kop="Rekenverhaal", oefeningen=[("kort", "Er zitten 8 vogels op het dak. Er komen er 5 bij. Hoeveel vogels zijn er nu?", "13", "90px"),
            ("kort", "Je hebt 15 knikkers. Je verliest er 6. Hoeveel heb je er nog?", "9", "90px")]),
    ]))

H["plus100"] = ("optellen-en-aftrekken-tot-100-launchpad", "wiskunde-plus100", L("Optellen en aftrekken tot 100", "Tientallen erbij en eraf, en over het tiental heen rekenen.", [
    dict(kop="Tientallen", blokken=[("p", "30 + 20: 3 T + 2 T = 5 T = <strong>50</strong>. 70 − 40: 7 T − 4 T = 3 T = <strong>30</strong>.")]),
    dict(kop="Eerst T, dan E", blokken=[("kader", "34 + 25 = ?<br>34 + <strong>20</strong> = 54<br>54 + <strong>5</strong> = 59")]),
    dict(kop="Over het tiental", blokken=[("kader", "38 + 5 = ?<br>38 + <strong>2</strong> = 40, en nog <strong>3</strong>: 43"),
        ("kader", "52 − 7 = ?<br>52 − <strong>2</strong> = 50, en nog <strong>5</strong> eraf: 45")]),
], ["3 T + 2 T = 5 T.", "Eerst de tientallen, dan de eenheden.", "Over het tiental: eerst naar het tiental."]),
    O("Optellen en aftrekken tot 100", [
        dict(kop="Met tientallen", oefeningen=[("rij", [("40 + 30 =", "70"), ("80 − 20 =", "60"), ("50 + 40 =", "90"), ("100 − 60 =", "40")], "", B)]),
        dict(kop="Zonder brug", oefeningen=[("rij", [("43 + 5 =", "48"), ("67 − 4 =", "63"), ("52 + 36 =", "88"), ("79 − 25 =", "54")], "", B)]),
        dict(kop="Met brug", oefeningen=[("rij", [("27 + 6 =", "33"), ("48 + 5 =", "53"), ("63 − 8 =", "55"), ("41 − 6 =", "35")], "", B),
            ("rij", [("36 + 27 =", "63"), ("58 + 14 =", "72"), ("72 − 18 =", "54"), ("85 − 39 =", "46")], "", B)]),
        dict(kop="Rekenverhaal", oefeningen=[("kort", "Lien heeft 46 stickers. Ze krijgt er 7 bij. Hoeveel heeft ze nu?", "53", "90px"),
            ("kort", "In de bus zitten 63 mensen. Er stappen er 20 uit. Hoeveel blijven er zitten?", "43", "90px")]),
    ]))

H["splitsen"] = ("splitsen-en-verliefde-harten-launchpad", "wiskunde-splitsen", L("Splitsen en verliefde harten", "Een getal splitsen in twee stukken, en de verliefde harten die samen 10 zijn.", [
    dict(kop="Splitsen", blokken=[("p", "7 kan je splitsen in 3 en 4, in 5 en 2, in 6 en 1 ... Samen blijft het altijd 7."),
        ("fig", tabel(["7"], [["0 en 7"], ["1 en 6"], ["2 en 5"], ["3 en 4"]], "30%"))]),
    dict(kop="Verliefde harten", blokken=[("fig", tabel(["1 ♥ 9", "2 ♥ 8", "3 ♥ 7", "4 ♥ 6", "5 ♥ 5"], [["10", "10", "10", "10", "10"]], "80%")),
        ("weetje", "Verliefde harten helpen bij 10 − 6: het hart van 6 is 4, dus 10 − 6 = 4.")]),
], ["Splitsen: samen blijft het hetzelfde getal.", "Verliefde harten zijn samen 10."]),
    O("Splitsen en verliefde harten", [
        dict(kop="Splits", oefeningen=[("rij", [("8 = 5 +", "3"), ("6 = 2 +", "4"), ("9 = 7 +", "2"), ("5 = 0 +", "5"), ("10 = 4 +", "6"), ("7 = 1 +", "6")], "", B)]),
        dict(kop="Alle splitsingen van 6", oefeningen=[("tabel", ["6", ""], [[None, None], [None, None], [None, None], [None, None]], "0 en 6 · 1 en 5 · 2 en 4 · 3 en 3", "60px")]),
        dict(kop="Verliefde harten", oefeningen=[("rij", [("3 ♥", "7"), ("8 ♥", "2"), ("1 ♥", "9"), ("6 ♥", "4"), ("5 ♥", "5"), ("0 ♥", "10")], "Schrijf het verliefde hart.", B)]),
        dict(kop="Min van 10", oefeningen=[("rij", [("10 − 2 =", "8"), ("10 − 7 =", "3"), ("10 − 5 =", "5"), ("10 − 9 =", "1")], "", B)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "6 en 4 zijn verliefde harten.", True), ("waar", "3 en 8 zijn verliefde harten.", False)]),
    ]))

H["tafels"] = ("tafels-van-2-5-en-10-launchpad", "wiskunde-tafels", L("Tafels van 2, 5 en 10", "Sprongen van 2, 5 en 10, de eerste maaltafels en eerlijk verdelen.", [
    dict(kop="Sprongen", blokken=[("fig", tabel(["van 2", "van 5", "van 10"], [["2 · 4 · 6 · 8 · 10", "5 · 10 · 15 · 20 · 25", "10 · 20 · 30 · 40 · 50"]], "100%"))]),
    dict(kop="Keer", blokken=[("p", "3 × 2 betekent <strong>3 keer 2</strong>: 2 + 2 + 2 = 6. Denk aan 3 kinderen met elk 2 schoenen."),
        ("fig", stippen(6), "3 × 2 = 6")]),
    dict(kop="Eerlijk verdelen", blokken=[("p", "10 koekjes eerlijk verdelen over 2 kinderen: elk kind krijgt er <strong>5</strong>. Iedereen krijgt evenveel.")]),
], ["Rij van 2: even getallen.", "Rij van 5: eindigt op 5 of 0.", "Rij van 10: eindigt op 0.", "3 × 2 = 2 + 2 + 2."]),
    O("Tafels van 2, 5 en 10", [
        dict(kop="Spring verder", oefeningen=[("rij", [("2, 4, 6, __, __", "8, 10"), ("5, 10, 15, __, __", "20, 25"), ("10, 20, 30, __, __", "40, 50")], "", "120px")]),
        dict(kop="Tafel van 2", oefeningen=[("rij", [("2 × 2 =", "4"), ("4 × 2 =", "8"), ("6 × 2 =", "12"), ("9 × 2 =", "18")], "", B)]),
        dict(kop="Tafel van 5", oefeningen=[("rij", [("1 × 5 =", "5"), ("3 × 5 =", "15"), ("6 × 5 =", "30"), ("10 × 5 =", "50")], "", B)]),
        dict(kop="Tafel van 10", oefeningen=[("rij", [("2 × 10 =", "20"), ("5 × 10 =", "50"), ("7 × 10 =", "70"), ("8 × 10 =", "80")], "", B)]),
        dict(kop="Verdelen", oefeningen=[("kort", "12 appels eerlijk over 2 manden. Hoeveel per mand?", "6", "90px"), ("kort", "20 snoepjes eerlijk over 4 kinderen. Hoeveel per kind?", "5", "90px")]),
    ]))

H["meten"] = ("meten-en-geld-launchpad", "wiskunde-meten", L("Meten en geld", "Lang en kort, zwaar en licht, veel en weinig, en betalen met euro.", [
    dict(kop="Meten", blokken=[("fig", tabel(["Wat?", "Waarmee?", "Maat"], [["hoe lang", "meetlat, lintmeter", "meter, centimeter"], ["hoe zwaar", "weegschaal", "kilogram"], ["hoeveel erin past", "maatbeker", "liter"]], "100%"))]),
    dict(kop="Geld", blokken=[("fig", "".join([munt(1), munt(2), munt(5, True), munt(10, True), munt(20, True)]), "munten van 1 en 2 euro, briefjes van 5, 10 en 20 euro"),
        ("p", "Je betaalt 10 euro voor iets van 8 euro. Je krijgt <strong>2 euro</strong> terug, want 8 + 2 = 10.")]),
], ["Meter: lang. Kilogram: zwaar. Liter: veel.", "Teruggeven: tel verder tot wat je gaf."]),
    O("Meten en geld", [
        dict(kop="Waarmee meet je?", oefeningen=[("rij", [("hoe lang je bent", "meetlat"), ("hoe zwaar je bent", "weegschaal"), ("hoeveel melk in een pot", "maatbeker")], "Meetlat, weegschaal of maatbeker?", "150px")]),
        dict(kop="Wat is langer?", oefeningen=[("kies", "Wat is het langst?", ["een potlood", "een tafel", "een gom"], 1), ("kies", "Wat is het zwaarst?", ["een veer", "een boek", "een fiets"], 2)]),
        dict(kop="Meet zelf", oefeningen=[("tabel", ["Wat?", "Hoeveel cm?"], [["je potlood", None], ["je schrift", None], ["je hand", None]], "eigen meting", "90px")]),
        dict(kop="Hoeveel geld?", oefeningen=[("fig", [(munt(2) + munt(2) + munt(1), "5 euro"), (munt(10, True) + munt(5, True), "15 euro"), (munt(20, True) + munt(2), "22 euro")], "Schrijf hoeveel euro.")]),
        dict(kop="Teruggeven", oefeningen=[("rij", [("iets van 7 euro, je geeft 10", "3 euro"), ("iets van 14 euro, je geeft 20", "6 euro"), ("iets van 5 euro, je geeft 5", "0 euro")], "Hoeveel krijg je terug?", "100px")]),
    ]))

H["klok"] = ("klok-dagen-en-maanden-launchpad", "wiskunde-klok", L("Klok, dagen en maanden", "Hele en halve uren lezen, de dagen van de week en de maanden van het jaar.", [
    dict(kop="De klok", blokken=[("p", "De <strong>kleine wijzer</strong> toont het uur. De <strong>grote wijzer</strong> op 12: een heel uur. Op 6: half."),
        ("fig", klok(3, 0) + " " + klok(4, 30), "3 uur en half 5")]),
    dict(kop="Dagen", blokken=[("kader", "maandag · dinsdag · woensdag · donderdag · vrijdag · zaterdag · zondag"), ("p", "Zaterdag en zondag zijn het <strong>weekend</strong>.")]),
    dict(kop="Maanden", blokken=[("fig", tabel(["Winter", "Lente", "Zomer", "Herfst"], [["december, januari, februari", "maart, april, mei", "juni, juli, augustus", "september, oktober, november"]], "100%"))]),
], ["Kleine wijzer = uur.", "Grote wijzer op 6 = half.", "7 dagen, 12 maanden, 4 seizoenen."]),
    O("Klok, dagen en maanden", [
        dict(kop="Hoe laat is het?", oefeningen=[("fig", [(klok(2, 0, 110), "2 uur"), (klok(7, 0, 110), "7 uur"), (klok(9, 30, 110), "half 10"), (klok(11, 30, 110), "half 12")], "Schrijf het uur.")]),
        dict(kop="Teken de wijzers", oefeningen=[("fig", [(klok(None, 0, 110), "5 uur"), (klok(None, 0, 110), "half 2")], "A) 5 uur &nbsp; B) half 2")]),
        dict(kop="Dagen", oefeningen=[("rij", [("na maandag", "dinsdag"), ("voor zaterdag", "vrijdag"), ("na zondag", "maandag")], "", "130px")]),
        dict(kop="Maanden", oefeningen=[("rij", [("na maart", "april"), ("voor juli", "juni"), ("de laatste maand", "december")], "", "130px"),
            ("kort", "In welke maand ben jij jarig?", "eigen antwoord", "140px")]),
    ]))

H["vormen"] = ("vormen-en-ruimte-launchpad", "wiskunde-vormen", L("Vormen en ruimte", "Vlakke vormen, blokken, en links, rechts, boven en onder.", [
    dict(kop="Vlakke vormen", blokken=[("fig", figuren(), "vierkant, rechthoek, driehoek, cirkel en ruit"),
        ("fig", tabel(["vorm", "hoeken", "zijden"], [["vierkant", "4", "4 even lang"], ["rechthoek", "4", "2 lang, 2 kort"], ["driehoek", "3", "3"], ["cirkel", "0", "rond"]], "70%"))]),
    dict(kop="Blokken", blokken=[("fig", tabel(["blok", "lijkt op"], [["kubus", "dobbelsteen"], ["balk", "schoendoos"], ["bol", "bal"], ["cilinder", "blikje"], ["kegel", "ijshoorntje"]], "60%"))]),
    dict(kop="Waar is het?", blokken=[("p", "<strong>boven</strong> en <strong>onder</strong>, <strong>voor</strong> en <strong>achter</strong>, <strong>links</strong> en <strong>rechts</strong>, <strong>tussen</strong> en <strong>naast</strong>.")]),
], ["Driehoek 3 hoeken, vierkant 4, cirkel 0.", "Een bol rolt, een kubus niet.", "Links, rechts, boven, onder."]),
    O("Vormen en ruimte", [
        dict(kop="Hoeveel hoeken?", oefeningen=[("rij", [("driehoek", "3"), ("vierkant", "4"), ("cirkel", "0"), ("rechthoek", "4")], "", B)]),
        dict(kop="Teken", oefeningen=[("teken", "Teken een huis met een vierkant, een driehoek als dak en een rechthoek als deur.", "eigen tekening", 55)]),
        dict(kop="Welk blok?", oefeningen=[("rij", [("een bal", "bol"), ("een dobbelsteen", "kubus"), ("een blikje", "cilinder"), ("een schoendoos", "balk")], "", "110px")]),
        dict(kop="Waar is het?", oefeningen=[("teken", "Teken een tafel. Teken een bal onder de tafel en een lamp boven de tafel. Teken links een stoel.", "eigen tekening", 55)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "Een kubus kan rollen.", False), ("waar", "Een driehoek heeft 3 hoeken.", True)]),
    ]))


if __name__ == "__main__":
    kies = sys.argv[1:] or list(H)
    for k in kies:
        naam, module, leer, oefen = H[k][0], H[k][1].replace("-", "_"), H[k][2], H[k][3] if len(H[k]) > 3 else None
        maak(naam, "wiskunde", leer, oefen, module)
