# -*- coding: utf-8 -*-
"""Ready wiskunde: Breuken en kommagetallen (noemer tot 20, gelijknamige breuken
optellen en aftrekken, breuk van een getal, kommagetallen tot op een honderdste).
Doel einde 4de leerjaar, Vlaamse overheid."""
from vr import mk, inv, wn

TITEL = "Breuken en kommagetallen"
UITLEG_1 = 'Wat is een breuk? Teller boven, noemer onder.'
UITLEG_2 = 'Een breuk van een getal, en kommagetallen.'

DEEL_1 = [
    mk("Een pizza is in 8 gelijke stukken verdeeld. Je eet er 3. Welk deel heb je gegeten?", ["3/8", "8/3", "3/5", "5/8"], 0, "Het geheel heeft 8 stukken (noemer) en je nam er 3 (teller): 3/8."),
    mk("Hoe heet het getal onder de breukstreep?", ["de teller", "de noemer", "de som", "het deel"], 1, "De noemer staat onder en noemt in hoeveel gelijke stukken je verdeelt."),
    wn("In de breuk 2/5 is 5 de teller.", False, "5 staat onder de breukstreep, dus 5 is de noemer. 2 is de teller."),
    inv("1/4 + 2/4 = ___/4", "3", "Dezelfde noemer: tel de tellers op. 1 + 2 = 3, dus 3/4.", 3),
    inv("5/6 − 2/6 = ___/6", "3", "Dezelfde noemer: trek de tellers af. 5 − 2 = 3, dus 3/6.", 3),
    mk("Welke breuk is het grootst?", ["1/8", "1/4", "1/2", "1/10"], 2, "Hoe minder stukken, hoe groter elk stuk. Een half is groter dan een kwart of een achtste."),
    wn("3/7 is groter dan 5/7.", False, "Bij dezelfde noemer is de breuk met de grootste teller het grootst. 5/7 is groter."),
    mk("Hoeveel achtsten zijn samen één geheel?", ["4", "8", "10", "16"], 1, "8/8 = 1 geheel."),
    inv("2/10 + 3/10 + 5/10 = ___/10", "10", "2 + 3 + 5 = 10, dus 10/10. Dat is precies één geheel.", 10),
    wn("2/4 is evenveel als 1/2.", True, "Twee kwarten zijn samen een half."),
    mk("Welke breuk is evenveel als 1/2?", ["3/6", "2/6", "1/6", "4/6"], 0, "3 van de 6 stukken is de helft."),
    mk("Een reep chocolade heeft 12 blokjes. Jan eet 5/12 op. Hoeveel blokjes blijven er over?", ["5", "7", "12", "17"], 1, "12 − 5 = 7 blokjes, dat is 7/12.", 7),
    inv("Een taart is in 6 stukken gesneden. Mama eet 1/6 en papa 2/6. Welk deel is opgegeten? ___/6", "3", "1/6 + 2/6 = 3/6. Dat is de helft van de taart.", 3),
    wn("Bij 1/3 + 1/3 tel je ook de noemers op: 2/6.", False, "Enkel de tellers tel je op. 1/3 + 1/3 = 2/3."),
    mk("Hoeveel is 7/9 − 4/9?", ["3/9", "3/0", "11/9", "3/18"], 0, "De noemer blijft 9, de tellers trek je af: 7 − 4 = 3."),
    mk("Welk deel van een uur is 15 minuten?", ["1/2", "1/3", "1/4", "1/15"], 2, "Een uur heeft 60 minuten. 60 : 4 = 15, dus een kwartier is 1/4."),
    inv("Hoeveel twintigsten zijn samen evenveel als 1 geheel? ___", "20", "20/20 = 1 geheel.", 20),
    wn("1/5 is kleiner dan 1/3.", True, "Bij vijf gelijke stukken is elk stuk kleiner dan bij drie gelijke stukken."),
    mk("Welke breuk hoort bij 'drie vierde'?", ["4/3", "3/4", "3/40", "34"], 1, "Drie (teller) vierde (noemer): 3/4."),
    wn("4/4 is één geheel.", True, "Als je alle 4 stukken neemt, heb je het hele ding."),
]

DEEL_2 = [
    mk("Hoeveel is 1/2 van 30?", ["10", "15", "20", "60"], 1, "Een half is delen door 2: 30 : 2 = 15.", 15),
    inv("1/4 van 20 = ___", "5", "Delen door de noemer: 20 : 4 = 5.", 5),
    mk("Hoeveel is 3/4 van 20?", ["5", "15", "12", "60"], 1, "20 : 4 = 5, en dan 3 keer: 5 × 3 = 15.", 15),
    inv("2/5 van 25 = ___", "10", "25 : 5 = 5, en dan 2 keer: 5 × 2 = 10.", 10),
    mk("Een klas heeft 24 kinderen. 1/3 komt met de fiets. Hoeveel kinderen zijn dat?", ["3", "8", "12", "21"], 1, "24 : 3 = 8 kinderen.", 8),
    wn("1/10 van 50 is 10.", False, "1/10 van 50 is 50 : 10 = 5."),
    inv("Lisa heeft 40 knikkers. Ze geeft 3/8 weg. Hoeveel knikkers geeft ze weg?", "15", "40 : 8 = 5, en dan 3 keer: 15 knikkers.", 15),
    mk("Hoe schrijf je 'drie tienden' als kommagetal?", ["3,0", "0,3", "0,03", "30"], 1, "Tienden staan op de eerste plaats na de komma: 0,3."),
    mk("Hoe schrijf je 1/100 als kommagetal?", ["0,1", "0,01", "1,00", "100"], 1, "Honderdsten staan op de tweede plaats na de komma: 0,01."),
    inv("In 4,72 staat de 7 op de plaats van de ___.", ["tienden", "tiende"], "Eerste cijfer na de komma: tienden. Tweede cijfer: honderdsten."),
    wn("0,5 is evenveel als 1/2.", True, "0,5 is vijf tienden, en 5/10 is de helft."),
    mk("Welk getal is het grootst?", ["0,9", "0,09", "0,19", "0,8"], 0, "Kijk eerst naar de tienden: 0,9 heeft 9 tienden, de andere hebben er 0, 1 of 8."),
    wn("2,5 is groter dan 2,45.", True, "Vergelijk de tienden: 2,5 heeft 5 tienden en 2,45 maar 4 tienden."),
    wn("0,30 is groter dan 0,3.", False, "Een nul achteraan verandert niets: 0,30 = 0,3."),
    inv("1,25 + 0,50 = ___", ["1,75", "1.75"], "Komma onder komma. 25 honderdsten + 50 honderdsten = 75 honderdsten: 1,75.", 1.75),
    mk("Hoeveel is 3,60 − 1,20?", ["2,40", "2,60", "4,80", "2,04"], 0, "3,60 − 1 = 2,60, en dan nog 0,20 eraf: 2,40.", 2.4),
    mk("Welk kommagetal ligt tussen 1,3 en 1,4?", ["1,35", "1,45", "1,25", "13,5"], 0, "1,35 ligt tussen 1,30 en 1,40."),
    inv("Een appel kost 0,45 euro. Een peer kost 0,35 euro. Hoeveel betaal je samen? ___ euro", ["0,80", "0,8", "0.80", "0.8"], "45 cent + 35 cent = 80 cent, dat is 0,80 euro.", 0.8),
    wn("1/4 van 12 is meer dan 1/2 van 12.", False, "1/4 van 12 = 3 en 1/2 van 12 = 6. Een half is meer."),
    wn("In 6,08 staat de 0 op de plaats van de tienden.", True, "6,08: 0 tienden en 8 honderdsten."),
]
