# -*- coding: utf-8 -*-
"""Ready Nederlands: Werkwoorden (tegenwoordige tijd met ik, jij, hij; vraagzin met jij;
verleden tijd van veel gebruikte werkwoorden; voltooid deelwoord met ge-).
Doel einde 4de leerjaar, Vlaamse overheid."""
from vr import mk, inv, wn

TITEL = "Werkwoorden"
UITLEG_1 = 'Ik werk, jij werkt, werk jij?'
UITLEG_2 = 'Vroeger: ik speelde, ik heb gespeeld.'

DEEL_1 = [
    mk("Welk woord is een werkwoord?", ["tafel", "lopen", "groen", "snel"], 1, "Lopen is iets wat je doet. Dat is een werkwoord."),
    mk("Welke vorm is juist: ik ... (werken)", ["werk", "werkt", "werkd", "werken"], 0, "Bij ik schrijf je de stam: ik werk."),
    mk("Welke vorm is juist: hij ... (werken)", ["werk", "werkt", "werkd", "werken"], 1, "Bij hij komt er een t achter de stam: hij werkt."),
    inv("Jij ___ (spelen) buiten.", "speelt", "Bij jij komt er een t achter de stam: jij speelt."),
    mk("Welke vraag is juist geschreven?", ["Speelt jij mee?", "Speel jij mee?", "Speeld jij mee?", "Spelen jij mee?"], 1, "Staat jij achter het werkwoord, dan valt de t weg: speel jij?"),
    wn("In de zin 'Loopt jij naar school?' staat het werkwoord juist.", False, "Jij staat achter het werkwoord, dus geen t: Loop jij naar school?"),
    inv("Ik ___ (worden) groot.", "word", "Bij ik schrijf je de stam: ik word. De stam van worden eindigt op d."),
    mk("Welke vorm is juist: hij ... (worden) negen jaar.", ["word", "wordt", "wort", "worden"], 1, "Hij: stam + t. Stam word + t = wordt."),
    wn("In 'Ik vind mijn sleutel' is vind juist geschreven.", True, "Bij ik schrijf je de stam: vind. Geen t erachter."),
    inv("Zij ___ (lezen) een boek.", "leest", "Zij (één persoon): stam + t. Stam lees + t = leest."),
    mk("Welke vorm is juist: wij ... (zingen)", ["zing", "zingt", "zingen", "zingte"], 2, "Bij wij, jullie en zij (meer personen) schrijf je het hele werkwoord: wij zingen."),
    wn("Bij 'mama en papa' schrijf je het werkwoord met een t: mama en papa kookt.", False, "Mama en papa zijn twee personen. Je schrijft: mama en papa koken."),
    inv("Hoe heet de stam van het werkwoord 'fietsen'? ___", "fiets", "Haal -en weg: fiets. Ik fiets."),
    mk("Welke vorm is juist: het meisje ... (rijden) op een paard.", ["rij", "rijd", "rijdt", "rijden"], 2, "Het meisje is één persoon: stam rijd + t = rijdt."),
    wn("De stam van 'maken' is 'maak'.", True, "Haal -en weg en luister: mak wordt maak, met twee a's."),
    inv("Hij ___ (houden) van chocolade.", "houdt", "Hij: stam houd + t = houdt."),
    mk("Welk woord is geen werkwoord?", ["springen", "eten", "vrolijk", "slapen"], 2, "Vrolijk zegt hoe iemand is. Je kan niet 'vrolijken'."),
    wn("Je hoort de t niet in 'hij vindt', maar je schrijft hem wel.", True, "Hij: stam + t. Je hoort het niet, maar het hoort er wel bij."),
    mk("Welke zin is juist?", ["Word jij morgen negen?", "Wordt jij morgen negen?", "Wort jij morgen negen?", "Worden jij morgen negen?"], 0, "Jij achter het werkwoord: geen t. Word jij?"),
    wn("Jullie lacht is juist.", False, "Bij jullie schrijf je het hele werkwoord: jullie lachen."),
]

DEEL_2 = [
    mk("Welke zin staat in de verleden tijd?", ["Ik speel voetbal.", "Ik speelde voetbal.", "Ik ga voetballen.", "Ik zal voetballen."], 1, "Speelde zegt dat het al gebeurd is."),
    inv("Gisteren ___ (spelen) ik met mijn zus.", "speelde", "Gisteren is voorbij: verleden tijd. Ik speelde."),
    mk("Wat is de verleden tijd van 'ik loop'?", ["ik loopte", "ik liep", "ik lopen", "ik heb loop"], 1, "Lopen verandert van klank: ik liep."),
    mk("Wat is de verleden tijd van 'ik ga'?", ["ik gaade", "ik gong", "ik ging", "ik gade"], 2, "Gaan is een werkwoord dat helemaal verandert: ik ging."),
    inv("Vorige week ___ (zijn) we in de zee.", "waren", "Wij en verleden tijd: we waren."),
    wn("'Ik at een appel' staat in de verleden tijd.", True, "At is de verleden tijd van eten."),
    mk("Wat is de verleden tijd van 'hij schrijft'?", ["hij schrijfte", "hij schreef", "hij schrijven", "hij schrijfde"], 1, "Schrijven verandert van klank: hij schreef."),
    wn("'Morgen fietste ik naar oma' is een juiste zin.", False, "Morgen moet nog komen. Dan zeg je: Morgen fiets ik naar oma."),
    inv("Ik heb een tekening ___ (maken).", "gemaakt", "Bij hebben hoort een voltooid deelwoord: ge + maak + t = gemaakt."),
    mk("Welk voltooid deelwoord is juist: ik heb ... (spelen)", ["gespeeld", "gespeelt", "speelde", "gespelen"], 0, "Maak het langer en luister: de gespeelde match. Je hoort een d, dus gespeeld."),
    mk("Welke zin is juist?", ["Ik ben naar school geloopt.", "Ik ben naar school gelopen.", "Ik heb naar school gelopen.", "Ik ben naar school liep."], 1, "Bij lopen hoort zijn: ik ben gelopen."),
    inv("Wij hebben een liedje ___ (zingen).", "gezongen", "Zingen verandert van klank: we hebben gezongen."),
    wn("Het voltooid deelwoord van 'werken' is 'gewerkt'.", True, "Ge + werk + t = gewerkt."),
    mk("Welk woord is een voltooid deelwoord?", ["fietsen", "fietst", "gefietst", "fietste"], 2, "Gefietst hoort bij 'ik heb gefietst'."),
    wn("Het voltooid deelwoord van 'eten' is 'geeet'.", False, "Eten verandert anders: ik heb gegeten."),
    inv("Gisteren ___ (hebben) ik buikpijn.", "had", "Hebben in de verleden tijd: ik had."),
    mk("Wat is de verleden tijd van 'wij drinken'?", ["wij drinkten", "wij dronken", "wij gedronken", "wij drinkden"], 1, "Drinken verandert van klank: wij dronken."),
    wn("In 'Ik heb gelachen' staat het werkwoord in de tegenwoordige tijd.", False, "Ik heb gelachen is al gebeurd. Het voltooid deelwoord gelachen vertelt over iets van daarnet of vroeger."),
    mk("Welke zin vertelt over iets dat nu gebeurt?", ["Ik zwom in de zee.", "Ik zwem in de zee.", "Ik heb gezwommen.", "Ik zwemde in de zee."], 1, "Ik zwem: dat is nu, de tegenwoordige tijd."),
    wn("'Hij kwam te laat' staat in de verleden tijd.", True, "Kwam is de verleden tijd van komen."),
]
