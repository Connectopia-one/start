# -*- coding: utf-8 -*-
"""Launchpad Nederlands: kijken en luisteren, een kort verhaaltje begrijpen en ordenen."""
from lp import K, I, W
import lpprent as P

TITEL = "Verhaaltjes begrijpen"
UITLEG_1 = "Een kort verhaaltje lezen of laten voorlezen."
UITLEG_2 = "Wat gebeurt eerst, wat daarna en wat op het einde?"

V1 = "Sara gaat naar het park met haar hond Max. Max rent achter een bal. Daarna drinken ze water."
V2 = "Het sneeuwt. Ben maakt een sneeuwman. Hij zet er een wortel op als neus."
DEEL_1 = [
    K(f"'{V1}' Wie gaat naar het park?", "Sara", ["Ben", "mama", "Max alleen"], "Sara gaat met haar hond.", None),
    K(f"'{V1}' Hoe heet de hond?", "Max", ["Sara", "Bobby", "Rex"], "De hond heet Max.", None),
    K(f"'{V1}' Waar rent Max achter?", "een bal", ["een kat", "een fiets", "een vogel"], "Max rent achter een bal.", None),
    K(f"'{V1}' Wat doen ze op het einde?", "water drinken", ["slapen", "eten", "zwemmen"], "Daarna drinken ze water.", None),
    W(f"'{V1}' Sara gaat naar de zee.", False, "Sara gaat naar het park."),
    W(f"'{V1}' Max is een hond.", True, "Haar hond Max."),
    K(f"'{V2}' Welk weer is het?", "het sneeuwt", ["het regent", "de zon schijnt", "het waait"], "Er staat: het sneeuwt.", None),
    K(f"'{V2}' Wat maakt Ben?", "een sneeuwman", ["een zandkasteel", "een tekening", "een taart"], "Ben maakt een sneeuwman.", None),
    K(f"'{V2}' Wat gebruikt Ben als neus?", "een wortel", ["een appel", "een steen", "een tak"], "Een wortel als neus.", None),
    W(f"'{V2}' Het is zomer.", False, "Het sneeuwt, dus het is winter."),
    W(f"'{V2}' De sneeuwman krijgt een neus.", True, "Een wortel als neus."),
    K("Lies valt van haar fiets. Ze heeft pijn aan haar knie. Hoe voelt Lies zich?", "verdrietig", ["blij", "boos op de fiets", "moe"], "Als je valt en pijn hebt, ben je verdrietig.", None),
    K("Tim krijgt een cadeau voor zijn verjaardag. Hoe voelt Tim zich?", "blij", ["bang", "verdrietig", "boos"], "Een cadeau maakt je blij.", None),
    K("Het onweert. Mila kruipt onder haar deken. Hoe voelt Mila zich?", "bang", ["blij", "moe", "trots"], "Onder de deken kruipen doe je als je bang bent.", None),
    W("Als iemand huilt, is die vaak verdrietig.", True, "Huilen doe je vaak als je verdrietig bent."),
    W("Als iemand lacht, is die boos.", False, "Lachen doe je als je blij bent."),
    W("Luisteren doe je met je oren.", True, "Je oren horen wat iemand vertelt."),
    W("Als iemand iets vertelt, praat je er het best door.", False, "Je luistert eerst, dan mag jij iets zeggen."),
    K("Waar gaat een verhaal over een kasteel en een draak meestal over?", "een sprookje", ["een recept", "het weerbericht", "een boodschappenlijstje"], "Kastelen en draken vind je in sprookjes.", None),
    K("Wat staat op de voorkant van een boek?", "de titel", ["het einde", "de laatste bladzijde", "het nummer van de bladzijde"], "Op de voorkant staat de titel.", None),
]

DEEL_2 = [
    K("Je gaat buiten spelen. Wat gebeurt eerst?", "Je trekt je jas aan.", ["Je gaat naar buiten.", "Je speelt in de tuin.", "Je komt terug binnen."], "Eerst je jas aan, dan naar buiten.", None),
    K("Er groeit een bloem. Wat gebeurt eerst?", "Je plant een zaadje.", ["Er komt een bloem.", "Er groeit een plantje.", "Je plukt de bloem."], "Eerst het zaadje, dan het plantje, dan de bloem.", None),
    K("Het is avond. Wat gebeurt eerst?", "Je doet je pyjama aan.", ["Je slaapt.", "Je wordt wakker.", "Je ontbijt."], "Pyjama aan, slapen, wakker worden, ontbijten.", None),
    K("Je bakt een taart. Wat gebeurt op het einde?", "Je eet de taart op.", ["Je mengt bloem en eieren.", "Je bakt de taart.", "Je zet de taart in de oven."], "Eerst maken en bakken, op het einde opeten.", None),
    K("Een kip legt een ei. Wat gebeurt op het einde?", "Uit het ei komt een kuiken.", ["De kip legt een ei.", "De kip zit op het ei.", "Het ei wordt warm gehouden."], "Eerst het ei, op het einde het kuiken.", None),
    K("Wat gebeurt in het midden? Eerst: je vult het bad. Op het einde: je droogt je af.", "Je neemt een bad.", ["Je gaat slapen.", "Je kleedt je aan.", "Je eet."], "Bad vullen, in bad gaan, afdrogen.", None),
    K("Wat gebeurt in het midden? Eerst: het sneeuwt. Op het einde: de sneeuwman smelt.", "Je maakt een sneeuwman.", ["De zon gaat onder.", "Het regent.", "Je gaat zwemmen."], "Sneeuw, sneeuwman maken, smelten.", None),
    K("Welk woord gebruik je voor wat eerst gebeurt?", "eerst", ["daarna", "op het einde", "toen pas"], "Eerst, daarna, op het einde.", None),
    W("Eerst doe je je schoenen aan, daarna je sokken.", False, "Eerst je sokken, daarna je schoenen."),
    W("Eerst was je je handen, daarna eet je.", True, "Voor het eten was je je handen."),
    W("Een kuiken komt uit een ei.", True, "Een kip legt een ei en daaruit komt een kuiken."),
    W("Een bloem komt voor het zaadje.", False, "Eerst is er een zaadje, dan groeit de bloem."),
    W("'Op het einde' vertelt wat als laatste gebeurt.", True, "Bijvoorbeeld: op het einde gaat iedereen naar huis."),
    W("'Daarna' vertelt wat eerst gebeurt.", False, "Daarna vertelt wat erna komt."),
    I("Een verhaal heeft een begin, een midden en een einde. Hoeveel delen is dat? ___", 3, "Begin, midden en einde.", 3),
    K("Mama zegt: 'Ruim eerst je speelgoed op, dan mag je tv kijken.' Wat doe je eerst?", "speelgoed opruimen", ["tv kijken", "slapen", "buiten spelen"], "Eerst opruimen, dan tv.", None),
    K("De juf zegt: 'Neem je schrift en schrijf je naam.' Wat neem je eerst?", "je schrift", ["je jas", "je boterhammen", "je fiets"], "Eerst het schrift, dan je naam schrijven.", None),
    K("Wat doet iemand die goed luistert?", "Die kijkt naar wie praat.", ["Die praat er door.", "Die speelt met iets anders.", "Die loopt weg."], "Goed luisteren: stil zijn en kijken naar wie praat.", None),
    W("Je kan een verhaal navertellen in de goede volgorde.", True, "Eerst het begin, dan het midden, dan het einde."),
    W("Bij een verhaal maakt de volgorde niets uit.", False, "Als je de volgorde verandert, klopt het verhaal niet meer."),
]

PRENT_1 = [
    K("Wat gebeurt er op het einde van dit verhaal?", "De sneeuwman is af.", ["Het kind rolt een sneeuwbal.", "Het sneeuwt nog niet.", "Het kind gaat zwemmen."], "Eerst rolt het kind een bal, dan zet het er een tweede op, en op het einde is de sneeuwman af.", None, prent=P.strip("verhaal-sneeuwman", ["lp-sneeuwman-1", "lp-sneeuwman-2", "lp-sneeuwman-3"])),
    I("De prentjes staan door elkaar. Welk prentje komt eerst? Schrijf de letter.", ["C", "c"], "Eerst rolt het kind een grote sneeuwbal: prentje C.", None, prent=P.strip("verhaal-sneeuwman-door-elkaar", ["lp-sneeuwman-2", "lp-sneeuwman-3", "lp-sneeuwman-1"])),
    K("Hoe voelt het kind zich?", "blij", ["bang", "verdrietig", "boos"], "Het kind lacht en springt in de plas: het is blij.", None, prent=P.een("verhaal-plas", "lp-kind-springt-plas")),
    W("Op de prent troost een kind een ander kind dat gevallen is.", True, "De jongen zit bij het meisje dat gevallen is en troost haar.", prent=P.een("verhaal-troosten", "lp-sorry")),
]
PRENT_2 = [
    K("Wat zie je op het laatste prentje?", "een kuiken", ["een ei", "een kip", "een leeg nest"], "Eerst een ei, dan een barst, en op het einde een kuiken.", None, prent=P.strip("verhaal-kuiken", ["lp-kuiken-1", "lp-kuiken-2", "lp-kuiken-3"])),
    I("De prentjes staan door elkaar. Welk prentje toont het begin van het verhaal? Schrijf de letter.", ["B", "b"], "Het verhaal begint met een heel ei: prentje B.", None, prent=P.strip("verhaal-kuiken-door-elkaar", ["lp-kuiken-3", "lp-kuiken-1", "lp-kuiken-2"])),
    W("Het kind op de prent slaapt.", False, "Het kind leest een boek in de zetel.", prent=P.een("verhaal-lezen", "lp-kind-leest")),
    K("Wat doet de mama?", "Ze kookt soep.", ["Ze leest een boek.", "Ze fietst.", "Ze slaapt."], "Ze roert in een pot soep.", None, prent=P.een("verhaal-koken", "lp-mama-kookt")),
]
