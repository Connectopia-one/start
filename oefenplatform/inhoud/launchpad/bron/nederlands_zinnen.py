# -*- coding: utf-8 -*-
"""Launchpad Nederlands: zinnen maken (hoofdletter, punt, vraagteken, woordvolgorde)."""
from lp import K, I, W
import lpprent as P

TITEL = "Zinnen maken"
UITLEG_1 = "Een zin begint met een hoofdletter en eindigt met een punt."
UITLEG_2 = "Woorden in de goede volgorde zetten."

DEEL_1 = [
    K("Welke zin is goed geschreven?", "Ik eet een appel.", ["ik eet een appel.", "Ik eet een appel", "ik eet een appel"], "Hoofdletter vooraan, punt achteraan.", None),
    K("Welke zin over de kat is goed geschreven?", "De kat slaapt.", ["de kat slaapt.", "De kat slaapt", "de Kat slaapt"], "Hoofdletter vooraan, punt achteraan.", None),
    K("Welk teken komt achter een vraag?", "?", [".", "!", ","], "Achter een vraag zet je een vraagteken.", None),
    K("Welk teken komt achter een gewone zin?", ".", ["?", "!", ","], "Achter een gewone zin zet je een punt.", None),
    K("Welke zin is een vraag?", "Ga je mee?", ["Ik ga mee.", "Ga mee!", "Wij gaan mee."], "Een vraag eindigt met een vraagteken.", None),
    K("Welk woord krijgt altijd een hoofdletter?", "Lotte", ["fiets", "school", "boek"], "Een naam krijgt een hoofdletter.", None),
    K("Welke naam van een stad schrijf je goed?", "Gent", ["gent", "gEnt", "GENt"], "De naam van een stad begint met een hoofdletter, de rest zijn kleine letters.", None),
    K("Hoe begint een zin?", "met een hoofdletter", ["met een punt", "met een vraagteken", "met een kleine letter"], "Elke zin begint met een hoofdletter.", None),
    W("'de zon schijnt.' is goed geschreven.", False, "De eerste letter moet een hoofdletter zijn: De zon schijnt."),
    W("'Waar woon jij?' is een vraag.", True, "Er staat een vraagteken achter."),
    W("Een naam schrijf je met een hoofdletter.", True, "Mia, Tom, Brussel: allemaal met een hoofdletter."),
    W("Achter een vraag zet je een punt.", False, "Achter een vraag zet je een vraagteken."),
    W("'Ik heb honger.' is een goede zin.", True, "Hoofdletter vooraan, punt achteraan."),
    W("'Hoe heet jij.' is goed geschreven.", False, "Het is een vraag, dus: Hoe heet jij?"),
    I("Hoeveel woorden staan in de zin 'Ik lees een boek.'? ___", 4, "Ik - lees - een - boek: 4 woorden.", 4),
    I("Hoeveel woorden staan in de zin 'De hond rent.'? ___", 3, "De - hond - rent: 3 woorden.", 3),
    I("Hoeveel woorden staan in de zin 'Mama drinkt een kop thee.'? ___", 5, "Mama - drinkt - een - kop - thee: 5 woorden.", 5),
    W("'Mag ik mee spelen?' eindigt met een vraagteken.", True, "Het is een vraag."),
    W("Tussen twee woorden laat je geen ruimte.", False, "Tussen woorden laat je een kleine ruimte."),
    W("Een zin kan uit twee woorden bestaan.", True, "Bijvoorbeeld: Tom lacht."),
]

DEEL_2 = [
    K("Zet in de goede volgorde: kat / De / slaapt", "De kat slaapt.", ["Slaapt de kat.", "Kat de slaapt.", "De slaapt kat."], "Eerst wie, dan wat hij doet.", None),
    K("Zet in de goede volgorde: speelt / Tom / buiten", "Tom speelt buiten.", ["Buiten Tom speelt.", "Speelt Tom buiten.", "Tom buiten speelt."], "Tom speelt buiten.", None),
    K("Zet in de goede volgorde: eet / Ik / brood", "Ik eet brood.", ["Brood ik eet.", "Eet ik brood.", "Ik brood eet."], "Ik eet brood.", None),
    K("Zet in de goede volgorde: is / De / groot / boom", "De boom is groot.", ["De groot is boom.", "Boom de is groot.", "Groot de boom is."], "De boom is groot.", None),
    K("Maak er een vraag van: Jij komt mee.", "Kom jij mee?", ["Jij komt mee.", "Kom jij mee.", "jij komt mee?"], "Bij een vraag zet je het werkwoord vooraan en een vraagteken achteraan.", None),
    K("Maak er een vraag van: Hij is ziek.", "Is hij ziek?", ["Hij is ziek.", "Is hij ziek.", "hij is ziek?"], "Is hij ziek?", None),
    K("Welk woord past? 'Ik ... naar school.'", "fiets", ["fietsen", "fietst", "fiets je"], "Ik fiets.", None),
    K("Welk woord past? 'Wij ... samen.'", "spelen", ["speel", "speelt", "spelend"], "Wij spelen.", None),
    W("'Rent de hond.' is een goede zin.", False, "Beter: De hond rent."),
    W("'De bal is rond.' is een goede zin.", True, "Alle woorden staan goed."),
    W("'Ik heb een fiets nieuwe.' klopt.", False, "Goed is: Ik heb een nieuwe fiets."),
    W("'Wil jij een koekje?' is een vraag.", True, "Het werkwoord staat vooraan en er staat een vraagteken."),
    W("'Ik ben zeven jaar.' is een goede zin.", True, "Alles staat goed."),
    W("'boek een lees ik' is een goede zin.", False, "Goed is: Ik lees een boek."),
    K("Welke zin past bij een kind dat lacht?", "Het meisje lacht.", ["Het meisje huilt.", "Het meisje slaapt.", "Het meisje is boos."], "Lachen = blij zijn.", None),
    K("Welk woord vertelt wat iemand doet? 'De vogel zingt.'", "zingt", ["De", "vogel", "geen enkel woord"], "Zingen is iets wat je doet.", None),
    K("Welk woord vertelt wie iets doet? 'Papa kookt.'", "Papa", ["kookt", "geen enkel woord", "allebei"], "Papa is degene die kookt.", None),
    K("Welke zin maakt 'De kat slaapt.' langer?", "De kat slaapt in de zon.", ["De kat.", "Slaapt.", "Kat slaapt."], "'in de zon' vertelt er meer bij.", None),
    W("Je kan een zin langer maken met woorden zoals 'in de tuin'.", True, "De hond rent in de tuin."),
    W("Een zin zonder punt is ook af.", False, "Een zin is pas af met een punt, vraagteken of uitroepteken."),
]

PRENT_1 = [
    K("Welke zin past bij de prent en is goed geschreven?", "De hond blaft.", ["de hond blaft.", "De hond blaft", "de Hond blaft"], "Hoofdletter vooraan, punt achteraan.", None, prent=P.een("zin-hond-blaft", "hond-blaft")),
    K("Zet in de goede volgorde: trapt / Het kind / de bal", "Het kind trapt de bal.", ["De bal trapt het kind.", "Trapt het kind de bal.", "Het kind de bal trapt."], "Eerst wie, dan wat het doet.", None, prent=P.een("zin-bal", "voetbal-trappen")),
    W("De zin 'De koe staat in de wei.' past bij de prent.", True, "Je ziet een koe in de wei.", prent=P.een("zin-koe", "koe-wei")),
    I("Hoeveel woorden staan in de zin 'De kat zit.'?", 3, "De - kat - zit: 3 woorden.", 3, prent=P.een("zin-kat", "lp-kat")),
]
PRENT_2 = [
    K("Welke zin is een vraag over de prent?", "Waar vliegt de vogel naartoe?", ["De vogel vliegt weg.", "De vogel vliegt.", "Weg vliegt de vogel."], "Een vraag eindigt met een vraagteken.", None, prent=P.een("zin-vogel", "vogel-vliegt-weg")),
    W("'Wie is er jarig?' is een vraag.", True, "Er staat een vraagteken achter.", prent=P.een("zin-feesthoedje", "lp-feesthoedje")),
    K("Welk woord ontbreekt? 'Ik eet een ...'", "ijsje", ["boek", "bal", "fiets"], "Je ziet een ijsje. Dat kan je eten.", None, prent=P.een("zin-ijsje", "ijsje")),
    W("De zin 'De trein rijdt.' eindigt met een vraagteken.", False, "Het is een gewone zin: hij eindigt met een punt.", prent=P.een("zin-trein", "trein")),
]
