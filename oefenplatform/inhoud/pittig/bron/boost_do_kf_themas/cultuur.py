"""Kunst als deel van een cultuur — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen kb_cultuur: cultuur in de enge en de brede
betekenis, cultuuruitingen en kunstuitingen, natuur, en de vijf kunstcriteria.
Met een zelfgetekend stadsplein."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL, ROOD

PL = Prent("stadsplein", "Een zaterdag op het plein", "een plein met een standbeeld, een regenboog, een marktkraam, een bushokje en een kerk, letters A tot E")
PL.rect(0, 470, 1000, 170, "#e9e4d4", GRIJS, 0, 0)
# E: regenboog aan de hemel
for i, kl in enumerate((ROOD, ORANJE, GEEL, LICHTGROEN, BLAUW)):
    PL.pad(f"M {560 + i * 12} 260 A {170 - i * 12} {150 - i * 12} 0 0 1 {900 - i * 12} 260", "none", kl, 10)
# A: kerk
PL.rect(60, 230, 170, 240, GRIJS, DONKER, 0, 3); PL.pad("M 60 230 L 145 120 L 230 230 Z", GRIJS, DONKER, 3)
PL.lijn(145, 70, 145, 120, DONKER, 4); PL.lijn(130, 88, 160, 88, DONKER, 4)
PL.rect(120, 380, 50, 90, "#8a6a4a", DONKER, 20, 2)
# B: standbeeld op sokkel
PL.rect(300, 400, 120, 70, GRIJS, DONKER, 2, 3)
PL.cirkel(360, 290, 18, "#6b7f5a", DONKER, 3)
PL.rect(340, 310, 40, 60, "#6b7f5a", DONKER, 6, 3)
PL.lijn(340, 320, 318, 280, "#6b7f5a", 8); PL.lijn(380, 320, 395, 360, "#6b7f5a", 8)
PL.lijn(350, 370, 348, 400, "#6b7f5a", 9); PL.lijn(370, 370, 372, 400, "#6b7f5a", 9)
# C: marktkraam met kazen
PL.rect(480, 380, 180, 90, "#ffffff", DONKER, 2, 3)
for k in range(6):
    PL.rect(480 + k * 30, 340, 30, 40, ROOD if k % 2 == 0 else "#ffffff", DONKER, 0, 2)
PL.cirkel(530, 410, 20, GEEL, DONKER, 2); PL.cirkel(600, 410, 20, GEEL, DONKER, 2)
# D: bushokje
PL.rect(760, 330, 190, 140, "#dff0f7", DONKER, 4, 3); PL.rect(750, 315, 210, 20, DONKER, DONKER, 2, 2)
PL.rect(790, 420, 120, 14, "#8a6a4a", DONKER, 2, 2)
LET = {"A": (145, 300), "B": (360, 440), "C": (570, 450), "D": (855, 380), "E": (730, 140)}
for t, (x, y) in LET.items():
    PL.letter(x, y, t)
U = "stadsplein.svg"
Z = {"A": [Prent.zone(55, 60, 180, 415)], "B": [Prent.zone(295, 270, 135, 205)], "C": [Prent.zone(475, 335, 195, 140)],
     "D": [Prent.zone(745, 310, 220, 165)], "E": [Prent.zone(550, 90, 360, 180)]}

GRAFFITI = ("Lees de situatie.\n\n"
            "Op een grijze muur langs het station spuit een kunstenares een reusachtig portret van een oude buurtbewoonster. "
            "Ze werkt drie weken, met een hoogtewerker en tientallen kleuren. Voorbijgangers blijven staan, sommigen worden er stil van. "
            "Een verzamelaar biedt de stad 50 000 euro voor de muur. Een buurman vindt het lelijk en wil dat het wordt overgeschilderd.")

VRAGEN = [
    klik("Bekijk het plein. Klik op wat geen cultuur is.", U, Z["E"], "Een regenboog is natuur: geen mens maakte hem."),
    klik("Klik op alle dingen die cultuur zijn in de brede betekenis, maar die je meestal geen kunst noemt.", U, Z["C"] + Z["D"],
         "Een marktkraam en een bushokje zijn door mensen gemaakt, maar het zijn geen kunstuitingen."),
    klik("Klik op alle dingen die je ook kunstuitingen kan noemen.", U, Z["A"] + Z["B"], "De kerk is architectuur, het ruiterbeeld beeldhouwkunst."),
    casus(GRAFFITI, [
        sorteer("Welk kunstcriterium hoort bij dit argument?", ["vakmanschap", "emotionele lading", "economische waarde", "esthetische waarde"],
                [("drie weken werk met tientallen kleuren", "vakmanschap"), ("voorbijgangers worden er stil van", "emotionele lading"), ("een bod van 50 000 euro", "economische waarde"), ("de buurman vindt het lelijk", "esthetische waarde")],
                "Elk argument steunt op een ander criterium."),
        mk("De buurman vindt het werk lelijk. Bewijst dat dat het geen kunst is?",
           ["nee, smaak verschilt en andere criteria tellen ook", "ja, want wat lelijk is, kan nooit echt kunst zijn", "ja, want één buurman beslist hier voor de hele straat", "nee, want alles wat op een muur gespoten wordt, is kunst"],
           0, "De criteria zijn argumenten, geen vijf voorwaarden."),
        keuze("Het criterium dat hier het minst aan bod komt, is de [[*originaliteit|emotionele lading|economische waarde]].", "Over vernieuwing staat er niets in de tekst."),
        open_("Is dit portret kunst? Geef je oordeel met twee kunstcriteria.",
              "Ja. Het vakmanschap is groot: drie weken werk op een hoogtewerker met tientallen kleuren. En de emotionele lading is sterk: voorbijgangers worden er stil van."),
    ]),
    sorteer("Enge of brede betekenis van cultuur?", ["enge betekenis", "alleen brede betekenis"],
            [("een opera", "enge betekenis"), ("een begroeting", "alleen brede betekenis"), ("een museumstuk", "enge betekenis"), ("de verkeersregels", "alleen brede betekenis"), ("een roman", "enge betekenis"), ("een eetgewoonte", "alleen brede betekenis")],
            "De enge betekenis blijft bij kunst, wetenschap en erfgoed."),
    tabel("Is dit cultuur?",
          [("een volkslied", J), ("een aardbeving", F), ("een taal", J), ("een zonsondergang", F), ("een recept", J)],
          "Cultuur is wat mensen maken en doorgeven."),
    keuze("Elke kunstuiting is een cultuuruiting, maar [[*niet elke cultuuruiting is kunst|elke cultuuruiting is kunst|geen cultuuruiting is kunst]].", "Een recept is cultuur, maar meestal geen kunst."),
    koppel("Koppel het kunstcriterium aan de vraag die erbij hoort.",
           [("vakmanschap", "Hoe moeilijk is het na te maken?"), ("originaliteit", "Wat is er nieuw aan?"), ("emotionele lading", "Wat maakt het bij mensen los?"), ("economische waarde", "Hoeveel is het waard?")],
           ["Hoe oud is het?"],
           "Ouderdom is geen kunstcriterium."),
    mk("Een kunstenaar zet een fietswiel op een krukje en noemt het kunst. Welk criterium is het sterkste argument?",
       ["originaliteit", "vakmanschap", "esthetische waarde", "economische waarde"],
       0, "Het idee is vernieuwend; ambacht of schoonheid is er weinig."),
    tabel("Klopt dit over de kunstcriteria?",
          [("Er zijn vijf kunstcriteria.", J), ("Een werk moet alle criteria halen.", F), ("Wat mooi heet, verandert met de tijd.", J), ("De criteria geven een sluitend antwoord.", F)],
          "Ze geven argumenten, geen sluitend antwoord."),
    keuze("Een berg is natuur, het wandelpad op die berg is [[*cultuur|natuur|kunst]].", "Cultuur is wat de mens toevoegt."),
    mk("Waarom is de economische waarde een zwak criterium?",
       ["ook rommel kan duur verkocht worden", "kunstwerken worden in werkelijkheid nooit verkocht", "de prijs van een kunstwerk is altijd geheim", "enkel heel oude kunst heeft een echte prijs"],
       0, "De markt beslist niet wat kunst is."),
    inv("Hoe heet het criterium dat zegt dat kunst mooi is? Twee woorden.", ["esthetische waarde", "de esthetische waarde"], "De esthetische waarde."),
    mk("Een kopie van de Mona Lisa, perfect nageschilderd. Welk criterium haalt ze niet?",
       ["originaliteit", "vakmanschap", "esthetische waarde", "emotionele lading"],
       0, "Een kopie is niet vernieuwend, ook al is het vakmanschap groot."),
    sorteer("Natuur, cultuur of ook kunst?", ["natuur", "cultuur, geen kunst", "ook kunst"],
            [("een vulkaan", "natuur"), ("een processie", "cultuur, geen kunst"), ("een fresco", "ook kunst"), ("een bushalte", "cultuur, geen kunst"), ("een sterrenhemel", "natuur"), ("een symfonie", "ook kunst")],
            "Of iets kunst is, beredeneer je met de criteria."),
    keuze("Een handgeweven tapijt met een traditioneel patroon haalt vooral het criterium [[*vakmanschap|originaliteit]].", "Het weven vraagt jaren oefening; het patroon is niet nieuw."),
    mk("Twee vrienden ruziën of een tattoo kunst is. Wat is de beste aanpak?",
       ["de vijf criteria één voor één bespreken", "wie het luidst roept, heeft uiteindelijk gelijk", "de prijs van de tattoo opzoeken en vergelijken", "alleen kijken of de tattoo mooi is of niet"],
       0, "Zo wordt een smaakruzie een gesprek met argumenten."),
    inv("Hoe heet het criterium dat zegt dat kunst een ambacht is? Eén woord.", ["vakmanschap"], "Het vakmanschap: technische beheersing."),
    tabel("Kan je dit criterium min of meer nameten?",
          [("economische waarde", J), ("vakmanschap", J), ("esthetische waarde", F), ("emotionele lading", F)],
          "Prijs en techniek zijn na te gaan; smaak en gevoel niet."),
    keuze("Kunstbeschouwing begint met het begrip cultuur, omdat [[*een kunstwerk niet los te lezen is van zijn cultuur|cultuur altijd kunst is|kunst ouder is dan cultuur]].", "Een kunstwerk ontstaat in een cultuur."),
    mk("Welke uitspraak gebruikt de brede betekenis van cultuur?",
       ["De Japanse cultuur kent veel buigingen.", "Zij gaat elke week naar een cultuuravond in de opera.", "De minister van Cultuur opent een museum.", "Het cultuurcentrum toont een tentoonstelling."],
       0, "Buigingen zijn een gewoonte: brede betekenis."),
    open_("Leg uit waarom een kerk uit de twaalfde eeuw zowel een cultuuruiting als een kunstuiting is.",
          "Ze is door mensen gebouwd, dus het is cultuur. En ze wordt beschouwd als architectuur, met vakmanschap en esthetische waarde, dus het is ook kunst."),
    inv("Hoe heet het criterium dat zegt dat kunst vernieuwend is? Eén woord.", ["originaliteit", "de originaliteit"], "De originaliteit."),
    keuze("Wie 'cultuur' zegt en een museum bedoelt, gebruikt de [[*enge|brede]] betekenis.", "De enge betekenis: kunst, wetenschap en erfgoed."),
    tabel("Is dit een kunstcriterium?",
          [("vakmanschap", J), ("ouderdom", F), ("emotionele lading", J), ("bekendheid van de maker", F), ("originaliteit", J)],
          "Een nieuw werk kan evengoed kunst zijn."),
    keuze("De impressionisten werden eerst uitgelachen en hangen nu in elk museum. Dat toont dat de [[*esthetische waarde|economische waarde|originaliteit]] verschuift met de tijd.", "Wat mooi heet, verandert per periode."),
    mk("Een reclamefilmpje voor frisdrank. Wat is het zeker?",
       ["een cultuuruiting", "een kunstuiting die alle vijf de criteria haalt", "natuur, want er speelt water in mee", "niets, want reclame valt buiten de cultuur"],
       0, "Door mensen gemaakt: cultuur. Of het kunst is, beslissen de criteria."),
]
