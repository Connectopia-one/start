# -*- coding: utf-8 -*-
"""Launchpad wiskunde: klok (uur en half uur), dagen, maanden en seizoenen."""
from lp import K, I, W
import lpprent as P

TITEL = "Klok, dagen en maanden"
UITLEG_1 = "De klok lezen: hele uren en halve uren."
UITLEG_2 = "De dagen van de week en de maanden van het jaar."

DEEL_1 = [
    K("De grote wijzer staat op 12, de kleine op 3. Hoe laat is het?", "3 uur", ["12 uur", "half 3", "half 4"], "Grote wijzer op 12: een heel uur. De kleine wijst het uur aan.", None),
    K("De grote wijzer staat op 12, de kleine op 8. Hoe laat is het?", "8 uur", ["12 uur", "half 8", "half 9"], "Grote wijzer op 12, kleine op 8: 8 uur.", None),
    K("De grote wijzer staat op 6, de kleine tussen 4 en 5. Hoe laat is het?", "half 5", ["half 4", "6 uur", "4 uur"], "Grote wijzer op 6 is half. De kleine is al halfweg naar 5: half 5.", None),
    K("De grote wijzer staat op 6, de kleine tussen 9 en 10. Hoe laat is het?", "half 10", ["half 9", "9 uur", "6 uur"], "Halfweg naar 10: half 10.", None),
    K("Welke wijzer toont het uur?", "de kleine wijzer", ["de grote wijzer", "allebei even veel", "geen van beide"], "De kleine wijzer toont het uur, de grote de minuten.", None),
    K("Het is 7 uur. Hoe laat is het 1 uur later?", "8 uur", ["6 uur", "half 8", "9 uur"], "7 + 1 = 8.", None),
    K("Het is half 3. Hoe laat is het een half uur later?", "3 uur", ["half 4", "2 uur", "4 uur"], "Na half 3 komt 3 uur.", None),
    K("Het is 10 uur. Hoe laat was het 2 uur geleden?", "8 uur", ["12 uur", "9 uur", "half 10"], "10 − 2 = 8.", None),
    W("Bij een heel uur staat de grote wijzer op 12.", True, "Grote wijzer op 12: precies een uur."),
    W("Bij half staat de grote wijzer op 3.", False, "Bij half staat de grote wijzer op 6, onderaan."),
    W("Half 6 is een half uur voor 6 uur.", True, "Half 6 komt net voor 6 uur."),
    W("Half 4 is hetzelfde als 4 uur.", False, "Half 4 is een half uur vroeger dan 4 uur."),
    W("Een uur duurt langer dan een half uur.", True, "Een uur is twee halve uren."),
    W("Op een klok staan de getallen 1 tot en met 20.", False, "Op een klok staan 1 tot en met 12."),
    I("Een film begint om 2 uur en duurt 2 uur. Om hoeveel uur is hij gedaan? ___", 4, "2 + 2 = 4: om 4 uur.", 4),
    I("Je slaapt van 8 uur 's avonds tot 7 uur 's morgens. Hoeveel uur is dat? ___", 11, "8 tot 12 is 4 uur, 12 tot 7 is 7 uur: 11 uur.", 11),
    I("Hoeveel halve uren zitten in 1 uur? ___", 2, "Een half uur en nog een half uur.", 2),
    I("Hoeveel uren heeft één dag en nacht? ___", 24, "Een dag en een nacht samen zijn 24 uur.", 24),
    W("Op school begin je meestal 's morgens.", True, "De meeste scholen beginnen tussen 8 en 9 uur 's morgens."),
    W("Middageten is om 12 uur 's nachts.", False, "Middageten is rond 12 uur 's middags."),
]

DEEL_2 = [
    K("Welke dag komt na maandag?", "dinsdag", ["zondag", "woensdag", "vrijdag"], "Maandag, dinsdag, woensdag, ...", None),
    K("Welke dag komt voor vrijdag?", "donderdag", ["zaterdag", "woensdag", "maandag"], "Donderdag, vrijdag.", None),
    K("Welke dagen zijn het weekend?", "zaterdag en zondag", ["vrijdag en zaterdag", "maandag en dinsdag", "zondag en maandag"], "Zaterdag en zondag zijn weekend.", None),
    K("Welke maand komt na januari?", "februari", ["maart", "december", "juni"], "Januari, februari, maart.", None),
    K("In welke maand vieren we Kerstmis?", "december", ["november", "januari", "april"], "Kerstmis is op 25 december.", None),
    K("Welke maand is de eerste van het jaar?", "januari", ["februari", "september", "december"], "Het jaar begint op 1 januari.", None),
    K("Welke maand komt voor mei?", "april", ["juni", "maart", "juli"], "April, mei, juni.", None),
    K("In welke maand begint het nieuwe schooljaar?", "september", ["augustus", "oktober", "januari"], "Het schooljaar start op 1 september.", None),
    I("Hoeveel dagen heeft een week? ___", 7, "Maandag tot en met zondag: 7 dagen.", 7),
    I("Hoeveel maanden heeft een jaar? ___", 12, "Januari tot en met december: 12 maanden.", 12),
    I("Hoeveel seizoenen heeft een jaar? ___", 4, "Lente, zomer, herfst en winter.", 4),
    I("Vandaag is het woensdag. Over hoeveel dagen is het zaterdag? ___", 3, "Donderdag, vrijdag, zaterdag: 3 dagen.", 3),
    W("Na zondag komt maandag.", True, "Na zondag begint een nieuwe week."),
    W("Woensdag komt na donderdag.", False, "Woensdag komt voor donderdag."),
    W("December is de laatste maand van het jaar.", True, "Na december begint een nieuw jaar."),
    W("Een jaar heeft 10 maanden.", False, "Een jaar heeft 12 maanden."),
    W("Gisteren is de dag voor vandaag.", True, "Gisteren, vandaag, morgen."),
    W("Morgen is de dag voor vandaag.", False, "Morgen is de dag na vandaag."),
    K("Vandaag is het dinsdag. Welke dag was het gisteren?", "maandag", ["woensdag", "zondag", "donderdag"], "De dag voor dinsdag is maandag.", None),
    K("In welk seizoen vallen de blaadjes van de bomen?", "de herfst", ["de lente", "de zomer", "de winter"], "In de herfst kleuren de blaadjes en vallen ze.", None),
]

PRENT_1 = [
    K("Welk uur toont de klok?", "3 uur", ["half 3", "12 uur", "9 uur"], "De grote wijzer staat op 12, de kleine op 3.", None, prent=P.klok("klok-3-00", 3, 0)),
    I("Hoe laat is het? Schrijf het uur.", ["8 uur", "acht uur", "8", "8u", "20 uur"], "De grote wijzer staat op 12, de kleine op 8: 8 uur.", None, prent=P.klok("klok-8-00", 8, 0)),
    K("Hoe laat is het op deze klok?", "half 6", ["half 5", "6 uur", "5 uur"], "De grote wijzer staat op 6. De kleine staat tussen 5 en 6: half 6.", None, prent=P.klok("klok-5-30", 5, 30)),
    W("Het is 10 uur.", True, "Grote wijzer op 12, kleine op 10.", prent=P.klok("klok-10-00", 10, 0)),
]
PRENT_2 = [
    W("Het is half 12.", False, "De grote wijzer staat op 12: het is 12 uur.", prent=P.klok("klok-12-00", 12, 0)),
    K("Lees de klok. Hoe laat is het?", "half 2", ["half 1", "1 uur", "6 uur"], "Grote wijzer op 6, de kleine tussen 1 en 2: half 2.", None, prent=P.klok("klok-1-30", 1, 30)),
    K("Kijk naar de klok. Hoe laat is het één uur later?", "8 uur", ["6 uur", "half 8", "7 uur"], "Nu is het 7 uur. Een uur later is het 8 uur.", None, prent=P.klok("klok-7-00", 7, 0)),
    I("Hoe laat is het? Schrijf het op.", ["half 10", "half tien", "9.30", "9:30", "9u30"], "Grote wijzer op 6, de kleine tussen 9 en 10: half 10.", None, prent=P.klok("klok-9-30", 9, 30)),
]
