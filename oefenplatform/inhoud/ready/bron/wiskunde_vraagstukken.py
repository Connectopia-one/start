# -*- coding: utf-8 -*-
"""Ready wiskunde: Vraagstukken en tabellen (stappenplan voor vraagstukken,
verhoudingstabel, gegevens aflezen uit tabellen en diagrammen, Venndiagram,
redeneren met waar en niet waar). Doel einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Vraagstukken en tabellen"
UITLEG_1 = "Stappenplan: lees de vraag goed, zoek wat je weet en wat je moet vinden, kies de bewerking, reken uit en kijk of het kan kloppen. Verhoudingstabel: wat je links doet, doe je ook rechts."
UITLEG_2 = "Bij een tabel of diagram kijk je eerst naar de titel en naar wat bij de rijen en kolommen staat. In een Venndiagram staat wat bij twee groepen tegelijk hoort in het stuk waar de cirkels overlappen."

DEEL_1 = [
    mk("Wat doe je eerst bij een vraagstuk?", ["meteen rekenen", "de vraag goed lezen", "het antwoord raden", "de getallen optellen"], 1, "Eerst lees je goed wat er gevraagd wordt. Pas dan kies je een bewerking."),
    mk("Een doos bevat 6 eieren. Hoeveel eieren zitten er in 4 dozen?", ["10", "24", "18", "64"], 1, "4 dozen van 6: 4 × 6 = 24 eieren.", 24),
    inv("Een fiets kost 240 euro. Papa betaalt al 90 euro. Hoeveel moet hij nog betalen? ___ euro", "150", "240 − 90 = 150 euro.", 150),
    mk("Juf verdeelt 36 potloden over 9 tafels. Hoeveel potloden krijgt elke tafel?", ["3", "4", "6", "27"], 1, "36 : 9 = 4 potloden.", 4),
    wn("Bij 'Hoeveel meer heeft Sam dan Lies?' moet je aftrekken.", True, "Je zoekt het verschil, en dat vind je met een aftrekking."),
    inv("1 ticket kost 5 euro. 3 tickets kosten 15 euro. 6 tickets kosten ___ euro.", "30", "Twee keer zoveel tickets is twee keer zoveel geld: 2 × 15 = 30 euro.", 30),
    mk("In een verhoudingstabel staat: 2 appels kosten 1 euro. Hoeveel kosten 8 appels?", ["2 euro", "4 euro", "8 euro", "16 euro"], 1, "Van 2 naar 8 appels is × 4. Dan ook de prijs × 4: 4 euro."),
    inv("4 kinderen hebben samen 12 stickers, elk evenveel. 10 kinderen hebben er dan samen ___.", "30", "Elk kind heeft 12 : 4 = 3 stickers. 10 kinderen: 10 × 3 = 30.", 30),
    wn("In een verhoudingstabel mag je links × 3 doen en rechts × 2.", False, "Wat je links doet, moet je rechts ook doen. Anders klopt de verhouding niet meer."),
    mk("Sara is 9 jaar. Haar broer is 4 jaar ouder. Hoe oud is haar broer?", ["5 jaar", "13 jaar", "36 jaar", "12 jaar"], 1, "4 jaar ouder: 9 + 4 = 13 jaar."),
    inv("Een bus vertrekt met 28 mensen. Bij de eerste halte stappen er 9 uit en 5 in. Hoeveel mensen zitten er nu op de bus? ___", "24", "28 − 9 = 19, en dan + 5 = 24.", 24),
    wn("Een antwoord van 500 kinderen in één klas kan kloppen.", False, "Zo'n grote klas bestaat niet. Kijk na of je antwoord kan kloppen en reken opnieuw."),
    mk("Een touw van 20 m wordt in 4 gelijke stukken geknipt. Hoe lang is elk stuk?", ["4 m", "5 m", "16 m", "80 m"], 1, "20 : 4 = 5 m."),
    inv("Max leest 15 bladzijden per dag. Na hoeveel dagen heeft hij een boek van 90 bladzijden uit? ___", "6", "90 : 15 = 6 dagen.", 6),
    mk("Welke bewerking past bij: 'Er zijn 5 rijen met elk 7 stoelen'?", ["5 + 7", "7 − 5", "5 × 7", "7 : 5"], 2, "5 keer 7 stoelen: 5 × 7 = 35."),
    wn("Bij 'eerlijk verdelen' moet je delen.", True, "Eerlijk verdelen over groepen is een deling."),
    mk("Een pak koekjes kost 2 euro. Mama koopt er 3 en betaalt met 10 euro. Hoeveel krijgt ze terug?", ["4 euro", "6 euro", "8 euro", "7 euro"], 0, "3 × 2 = 6 euro. 10 − 6 = 4 euro terug.", 4),
    inv("Een week heeft 7 dagen. Hoeveel dagen zijn 5 weken? ___", "35", "5 × 7 = 35 dagen.", 35),
    wn("Je kan een vraagstuk soms oplossen door een tekening te maken.", True, "Een tekening of schema helpt om te zien wat er gebeurt."),
    wn("Bij 'samen' moet je altijd vermenigvuldigen.", False, "'Samen' betekent vaak optellen. Kijk goed wat er gebeurt in het verhaal."),
]

DEEL_2 = [
    mk("In een tabel staat: maandag 12 bezoekers, dinsdag 18, woensdag 9. Op welke dag kwamen de meeste bezoekers?", ["maandag", "dinsdag", "woensdag", "donderdag"], 1, "18 is het grootste getal: dinsdag."),
    inv("In een tabel staat: maandag 12 bezoekers, dinsdag 18, woensdag 9. Hoeveel bezoekers waren er samen? ___", "39", "12 + 18 + 9 = 39.", 39),
    mk("In een staafdiagram is de staaf van appels het hoogst. Wat betekent dat?", ["Appels komen het minst voor.", "Appels komen het meest voor.", "Appels zijn het duurst.", "Appels zijn rood."], 1, "Hoe hoger de staaf, hoe meer."),
    wn("In een staafdiagram lees je eerst de titel.", True, "De titel zegt waarover het diagram gaat."),
    inv("Een tabel van een klas: 8 kinderen komen te voet, 11 met de fiets, 6 met de auto. Hoeveel meer kinderen komen met de fiets dan te voet? ___", "3", "11 − 8 = 3.", 3),
    mk("Een tabel van een klas: 8 kinderen komen te voet, 11 met de fiets, 6 met de auto. Hoeveel kinderen zitten er in de klas?", ["19", "25", "17", "14"], 1, "8 + 11 + 6 = 25 kinderen.", 25),
    wn("In een staafdiagram moeten alle staven even hoog zijn.", False, "Elke staaf is zo hoog als zijn getal. Daardoor zie je meteen wat het meest voorkomt."),
    mk("Een Venndiagram heeft een cirkel 'heeft een huisdier' en een cirkel 'speelt voetbal'. Waar staat een kind dat beide doet?", ["buiten de cirkels", "enkel in de cirkel huisdier", "in het stuk waar de cirkels overlappen", "enkel in de cirkel voetbal"], 2, "Wie bij beide groepen hoort, staat in het gedeelte dat bij beide cirkels hoort."),
    mk("In een Venndiagram staat Lien buiten beide cirkels 'heeft een huisdier' en 'speelt voetbal'. Wat weet je over Lien?", ["Ze speelt elke week voetbal, maar heeft geen huisdier.", "Ze heeft geen huisdier en speelt geen voetbal.", "Ze heeft een huisdier.", "Ze doet allebei."], 1, "Buiten de cirkels betekent: hoort bij geen van beide groepen."),
    inv("In de cirkel 'even getallen' staan 2, 4, 6 en 8. In de cirkel 'groter dan 5' staan 6, 7, 8 en 9. Hoeveel getallen staan in het overlappende stuk? ___", "2", "6 en 8 zijn even én groter dan 5.", 2),
    wn("Het getal 7 hoort in het overlappende stuk van 'even getallen' en 'groter dan 5'.", False, "7 is groter dan 5, maar 7 is oneven. Het staat enkel in de cirkel 'groter dan 5'."),
    wn("Elk vierkant is ook een rechthoek.", True, "Een vierkant heeft vier rechte hoeken en de overstaande zijden zijn even lang. Het is een bijzondere rechthoek."),
    wn("Elke rechthoek is ook een vierkant.", False, "Een rechthoek heeft niet altijd vier even lange zijden."),
    mk("Welke uitspraak is waar?", ["Alle even getallen eindigen op 5.", "Alle getallen die eindigen op 0 zijn even.", "Alle oneven getallen zijn groter dan 10.", "Het getal 9 is even."], 1, "Een getal dat eindigt op 0 is altijd deelbaar door 2, dus even."),
    mk("In een tabel staat de temperatuur: maandag 6 °C, dinsdag 4 °C, woensdag 9 °C. Hoeveel graden scheelt het tussen de warmste en de koudste dag?", ["3 graden", "5 graden", "9 graden", "2 graden"], 1, "Warmste dag 9 °C, koudste dag 4 °C. 9 − 4 = 5 graden."),
    inv("In een pictogram staat één ☺ voor 5 kinderen. Bij 'zwemmen' staan 4 ☺. Hoeveel kinderen zwemmen graag? ___", "20", "4 × 5 = 20 kinderen.", 20),
    mk("In een lijndiagram stijgt de lijn van maandag naar dinsdag. Wat betekent dat?", ["Er was minder op dinsdag.", "Er was meer op dinsdag.", "Er was even veel.", "Het diagram is fout."], 1, "Een stijgende lijn betekent dat het getal groter wordt."),
    wn("Een tabel heeft rijen en kolommen.", True, "Rijen lopen van links naar rechts, kolommen van boven naar onder."),
    inv("In een tabel staat: 1 pak = 6 flessen, 2 pakken = 12 flessen, 5 pakken = ___ flessen.", "30", "Elk pak heeft 6 flessen: 5 × 6 = 30.", 30),
    wn("Als je in een tabel een getal vergeet, kan de som toch kloppen.", False, "Ontbreekt er een getal, dan wordt je som te klein. Tel alles na."),
]
