# -*- coding: utf-8 -*-
"""Ready Nederlands: Woordsoorten en zinnen (zelfstandig naamwoord, lidwoord,
bijvoeglijk naamwoord, werkwoord; persoonsvorm en onderwerp; soorten zinnen
en leestekens). Doel einde 4de leerjaar, Vlaamse overheid."""
from vr import mk, inv, wn

TITEL = "Woordsoorten en zinnen"
UITLEG_1 = "Zelfstandig naamwoord: een mens, dier of ding (de hond). Lidwoord: de, het, een. Bijvoeglijk naamwoord: zegt hoe iets is (de grote hond). Werkwoord: wat iemand doet."
UITLEG_2 = "De persoonsvorm verandert als je de zin in een andere tijd zet. Het onderwerp is wie of wat iets doet. Een vraagzin eindigt op ?, een uitroep op !, een gewone zin op een punt."

DEEL_1 = [
    mk("Welk woord is een zelfstandig naamwoord?", ["lopen", "fiets", "blauw", "snel"], 1, "Een fiets is een ding. Je kan er 'de' of 'een' voor zetten."),
    mk("Welk lidwoord hoort bij 'huis'?", ["de", "het", "den", "der"], 1, "Je zegt: het huis."),
    inv("___ boom staat in de tuin. (de of het)", ["De", "de"], "Je zegt: de boom."),
    mk("Welk woord is een bijvoeglijk naamwoord?", ["kat", "springen", "zacht", "het"], 2, "Zacht zegt hoe iets is: de zachte kat."),
    wn("'Een' is een lidwoord.", True, "De, het en een zijn de drie lidwoorden."),
    mk("Welk lidwoord hoort bij 'paard'?", ["de", "het", "die", "dat"], 1, "Je zegt: het paard."),
    mk("Wat is het zelfstandig naamwoord in 'De oude man wandelt'?", ["de", "oude", "man", "wandelt"], 2, "De man is een mens. Dat is het zelfstandig naamwoord."),
    wn("In 'het rode boek' is 'rode' een werkwoord.", False, "Rode zegt hoe het boek is. Het is een bijvoeglijk naamwoord."),
    inv("In de zin 'De kleine poes slaapt' is ___ het bijvoeglijk naamwoord.", "kleine", "Kleine zegt hoe de poes is."),
    mk("Wat is het lidwoord bij een verkleinwoord, zoals 'hondje'?", ["altijd de", "altijd het", "soms de, soms het", "geen lidwoord"], 1, "Verkleinwoorden krijgen altijd het: het hondje, het boompje."),
    wn("Bij meervoud gebruik je altijd 'de': de huizen.", True, "Ook al zeg je het huis, in het meervoud wordt het de huizen."),
    mk("Hoeveel zelfstandige naamwoorden staan in 'De jongen eet een appel'?", ["1", "2", "3", "4"], 1, "Jongen en appel: twee zelfstandige naamwoorden."),
    inv("Een woord dat zegt wat iemand doet, is een ___.", "werkwoord", "Lopen, eten, lachen: dat zijn werkwoorden."),
    wn("'Gelukkig' is een lidwoord.", False, "De lidwoorden zijn de, het en een. Gelukkig is een bijvoeglijk naamwoord: een gelukkig kind."),
    mk("Welke rij bevat enkel bijvoeglijke naamwoorden?", ["groot, klein, mooi", "huis, groot, lopen", "de, het, een", "eten, drinken, slapen"], 0, "Groot, klein en mooi zeggen allemaal hoe iets is."),
    wn("'Springen' is een zelfstandig naamwoord.", False, "Springen is iets wat je doet. Het is een werkwoord."),
    mk("Wat is het werkwoord in 'De vogels zingen mooi'?", ["vogels", "zingen", "mooi", "de"], 1, "Zingen is wat de vogels doen."),
    inv("___ meisje speelt met haar pop. (de of het)", ["Het", "het"], "Meisje is een verkleinwoord: het meisje."),
    mk("Welk woord past: 'Ik zie een ... vogel.'", ["vliegen", "gele", "boom", "het"], 1, "Gele zegt hoe de vogel is. Een bijvoeglijk naamwoord past voor het zelfstandig naamwoord."),
    wn("Namen zoals 'Emma' en 'Brussel' zijn ook zelfstandige naamwoorden.", True, "Namen van mensen en plaatsen zijn zelfstandige naamwoorden. Ze krijgen een hoofdletter."),
]

DEEL_2 = [
    mk("Waar zet je een vraagteken?", ["achter een gewone zin", "achter een vraag", "voor een naam", "in het midden van een woord"], 1, "Een vraag sluit je af met een vraagteken."),
    mk("Welk leesteken hoort achter 'Wat een mooie dag'?", [".", "?", "!", ","], 2, "Het is een uitroep, dus een uitroepteken."),
    inv("Kom jij morgen spelen___ (schrijf het leesteken)", "?", "Het is een vraag, dus een vraagteken."),
    wn("Een zin begint altijd met een hoofdletter.", True, "Elke zin begint met een hoofdletter en eindigt met een leesteken."),
    mk("Wat is het onderwerp in 'De hond blaft'?", ["de hond", "blaft", "de", "hond blaft"], 0, "Wie blaft? De hond. Dat is het onderwerp."),
    mk("Wat is de persoonsvorm in 'Lies fietst naar school'?", ["Lies", "fietst", "naar", "school"], 1, "Zet de zin in de verleden tijd: Lies fietste. Het woord dat verandert, is de persoonsvorm."),
    inv("Het onderwerp in 'Mijn broer speelt gitaar' is mijn ___.", "broer", "Wie speelt gitaar? Mijn broer."),
    wn("Je vindt de persoonsvorm door de zin in een andere tijd te zetten.", True, "Het woord dat verandert van tijd, is de persoonsvorm."),
    mk("Welke zin is een vraagzin?", ["Ik heb honger.", "Heb jij honger?", "Wat een honger!", "Hij heeft honger."], 1, "Heb jij honger? vraagt iets en eindigt op een vraagteken."),
    wn("In 'Morgen gaan we zwemmen' is 'morgen' het onderwerp.", False, "Wie gaat zwemmen? We. Dat is het onderwerp. Morgen zegt wanneer."),
    mk("Wat is de persoonsvorm in 'De kinderen lachen hard'?", ["kinderen", "lachen", "hard", "de"], 1, "Verleden tijd: de kinderen lachten. Lachen verandert, dus dat is de persoonsvorm."),
    inv("Zet de woorden in de juiste volgorde: 'eet – een – Tim – appel'. ___ eet een appel.", "Tim", "Tim eet een appel. De zin begint met een hoofdletter."),
    mk("Welke zin is juist geschreven?", ["de zon schijnt.", "De zon schijnt.", "De zon schijnt", "de zon schijnt"], 1, "Hoofdletter vooraan en een punt achteraan."),
    wn("Een komma zet je soms tussen woorden in een opsomming: appels, peren en bananen.", True, "In een opsomming zet je een komma tussen de woorden, behalve voor en."),
    mk("Waar staan de aanhalingstekens juist?", ["Mama zei: \"Kom eten!\"", "\"Mama zei: Kom eten!\"", "Mama \"zei: Kom eten!\"", "Mama zei: Kom \"eten!\""], 0, "Aanhalingstekens staan rond de woorden die iemand zegt."),
    wn("Een uitroepteken gebruik je achter een gewone mededeling, zoals 'Ik ben negen jaar!'.", False, "Bij een gewone mededeling zet je een punt: Ik ben negen jaar."),
    inv("Hoeveel woorden telt de zin 'Oma bakt een lekkere taart'? ___", "5", "Oma – bakt – een – lekkere – taart: 5 woorden.", 5),
    mk("Wat is het onderwerp in 'In de zomer zwemt Noor in het meer'?", ["de zomer", "Noor", "het meer", "zwemt"], 1, "Wie zwemt? Noor. Dat is het onderwerp, ook al staat het niet vooraan."),
    wn("Het onderwerp staat altijd vooraan in de zin.", False, "Niet altijd. In 'In de zomer zwemt Noor in het meer' staat het onderwerp Noor in het midden."),
    wn("'Wat lief van je!' is een uitroep.", True, "Je roept iets uit met gevoel. Daarom het uitroepteken."),
]
