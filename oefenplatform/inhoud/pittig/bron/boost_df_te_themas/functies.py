"""Formules en functies in een rekenblad — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Pittige vragen uit Samenleving en economie Beyond (beyond_se_themas/excel.py) die
binnen te_functies vallen, met het rekenblad om op te klikken, aangevuld met
eigen vragen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_se_themas import excel as _x

VRAGEN = [_x.VRAGEN[i] for i in (0, 1, 3, 4, 5, 7, 9, 10, 17, 18, 19, 20, 21, 24, 25, 26, 27)] + [
    tabel("Wat geeft deze formule?",
          [("=2+3*4", "14"), ("=(2+3)*4", "20"), ("=10-4/2", "8"), ("=(10-4)/2", "3")],
          "Eerst maal en delen, dan plus en min. Haakjes gaan voor.",
          kolommen=["3", "8", "14", "20"]),
    tabel("Welke functie gebruik je?",
          [("het aantal cellen met een getal tellen", "AANTAL"), ("getallen met elkaar vermenigvuldigen", "PRODUCT"), ("de datum van vandaag tonen", "VANDAAG"), ("een getal op twee cijfers na de komma afronden", "AFRONDEN")],
          "Elke functie doet één ding.",
          kolommen=["AANTAL", "PRODUCT", "VANDAAG", "AFRONDEN"]),
    inv("Wat geeft =AFRONDEN(7,456;1)? Schrijf het getal.", ["7,5", "7.5"],
        "Het tweede getal zegt hoeveel cijfers na de komma: 7,456 wordt 7,5."),
    tabel("Wat geeft deze tekstfunctie als in A1 de tekst Fietsen staat?",
          [("=LINKS(A1;3)", "Fie"), ("=RECHTS(A1;2)", "en"), ("=HOOFDLETTERS(A1)", "FIETSEN")],
          "LINKS geeft de eerste tekens, RECHTS de laatste.",
          kolommen=["Fie", "en", "FIETSEN"]),
    casus("Lees de situatie.\n\nEen groothandel geeft korting volgens het bedrag van de bestelling in B2:\nvanaf 1 000 euro: 10 % korting\nvanaf 500 euro: 5 % korting\nanders: geen korting\nIn C2 staat =ALS(B2>=1000;10%;ALS(B2>=500;5%;0%))", [
        tabel("Welke korting geeft de formule?",
              [("B2 is 1 200", "10 %"), ("B2 is 750", "5 %"), ("B2 is 300", "0 %"), ("B2 is 500", "5 %")],
              "De eerste voorwaarde die waar is, bepaalt de uitkomst.",
              kolommen=["0 %", "5 %", "10 %"]),
        keuze("Dit is een [[*geneste|absolute|relatieve]] ALS: een ALS in een ALS.",
              "Zo kies je tussen meer dan twee uitkomsten."),
    ]),
    keuze("VERT.ZOEKEN zoekt in de [[*eerste kolom|laatste kolom|eerste rij]] van de tabel; HORIZ.ZOEKEN zoekt in de [[*eerste rij|eerste kolom|laatste rij]].",
          "Verticaal en horizontaal."),
    tabel("Relatief, absoluut of gemengd?",
          [("C2", "relatief"), ("$C$2", "absoluut"), ("$C2", "gemengd"), ("C$2", "gemengd")],
          "Een gemengde verwijzing zet enkel de kolom of enkel de rij vast.",
          kolommen=["relatief", "absoluut", "gemengd"]),
    mk("Je kopieert =A2*$E$1 van B2 naar B3. Wat staat er in B3?",
       ["=A3*$E$1", "=A2*$E$1", "=A3*$E$2", "=B3*$F$1"], 0,
       "A2 schuift mee naar A3; $E$1 blijft vast."),
    keuze("Een zoekfunctie die de waarde niet vindt, geeft [[*een foutmelding|nul|een lege cel]].",
          "Die kan je opvangen met een functie zoals ALS.FOUT."),
    tabel("Klopt dit over functies?",
          [("Een functienaam moet je in hoofdletters typen.", F), ("Dollartekens in een formule betekenen dat het om geld gaat.", F), ("VANDAAG past zich elke dag aan.", J), ("NU geeft de datum en het uur.", J)],
          "Het rekenblad zet de functienaam zelf in hoofdletters. Dollartekens zetten een verwijzing vast."),
]
