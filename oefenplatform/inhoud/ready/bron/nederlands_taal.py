# -*- coding: utf-8 -*-
"""Ready Nederlands: Taal en verhalen (opbouw van een verhaal: begin, midden, slot;
personages, plaats en tijd; soorten teksten; een bericht of brief schrijven;
luisteren en spreken; alfabetische volgorde). Doel einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Taal en verhalen"
UITLEG_1 = 'Begin, midden en slot van een verhaal.'
UITLEG_2 = 'Brief, recept, uitnodiging en het alfabet.'

DEEL_1 = [
    mk("Wat vertel je meestal in het begin van een verhaal?", ["hoe het verhaal helemaal afloopt", "wie er meedoet, waar en wanneer", "de les die je eruit leert", "wat de schrijver graag eet"], 1, "In het begin leer je de personages kennen en weet je waar en wanneer het gebeurt."),
    mk("Hoe noem je de personen in een verhaal?", ["schrijvers", "personages", "lezers", "tekenaars"], 1, "De mensen of dieren die in het verhaal meedoen, heten personages."),
    wn("In het slot van een verhaal lees je hoe het afloopt.", True, "Het slot vertelt hoe het probleem opgelost wordt."),
    mk("Een verhaal begint met 'Er was eens'. Wat voor verhaal is het waarschijnlijk?", ["een recept", "een sprookje", "een krantenbericht", "een weerbericht"], 1, "Sprookjes beginnen vaak met 'Er was eens'."),
    inv("In het midden van een verhaal ontstaat er vaak een ___. (Iets wat misloopt)", ["probleem", "probleempje"], "In het midden gebeurt er iets spannends of loopt er iets mis."),
    mk("Wie schrijft een boek?", ["de illustrator", "de schrijver", "de lezer", "de bibliothecaris"], 1, "De schrijver of auteur bedenkt het verhaal. De illustrator maakt de prenten."),
    wn("Een illustrator schrijft het verhaal van een boek.", False, "De illustrator maakt de tekeningen. De schrijver bedenkt het verhaal."),
    mk("Welke zin hoort het best bij het slot van een verhaal?", ["Op een dag kreeg Kato een vreemde brief.", "En zo vond Kato haar kat terug in de schuur.", "Kato woonde met haar ouders in een klein huis bij het donkere bos.", "Plots hoorde Kato een raar geluid."], 1, "Die zin vertelt hoe het afloopt. De andere zinnen passen bij het begin of het midden."),
    wn("Een verhaal moet altijd echt gebeurd zijn.", False, "Veel verhalen zijn verzonnen, zoals sprookjes en fantasieverhalen."),
    mk("In 'Op een koude winterdag liep Bas door het bos' lees je ...", ["enkel wie er in het verhaal meedoet", "wie, wanneer en waar", "hoe het verhaal afloopt", "welk probleem er komt"], 1, "Wie: Bas. Wanneer: op een koude winterdag. Waar: in het bos."),
    inv("In het verhaal 'Roodkapje' is de wolf een ___.", ["personage", "personage."], "De wolf doet mee in het verhaal. Hij is een personage."),
    mk("Waarom zet een schrijver een spannend stuk in het midden?", ["om je te vervelen", "zodat je verder wil lezen", "om het boek dikker te maken", "omdat het moet van de uitgever"], 1, "Spanning zorgt ervoor dat je wil weten hoe het afloopt."),
    wn("Een gedicht heeft vaak korte regels en soms rijm.", True, "Bij rijm klinken de woorden aan het eind van de regels gelijk, zoals muis en huis."),
    mk("Welke woorden rijmen?", ["boom en bal", "kat en hoed", "muis en huis", "vlinder en hond"], 2, "Muis en huis eindigen op dezelfde klank."),
    inv("Welk woord rijmt op 'ster'? Ik zie een ster, heel ___. (iets wat niet dichtbij is)", "ver", "Ster en ver rijmen."),
    wn("In een strip staan nooit tekstballonnen.", False, "In een strip staan de woorden van de personages net in tekstballonnen."),
    mk("Wat is het hoofdpersonage?", ["het personage dat het minst zegt in het hele boek", "het personage waarover het verhaal gaat", "de schrijver van het boek", "het dier op de kaft"], 1, "Het hoofdpersonage is de belangrijkste persoon in het verhaal."),
    wn("De titel van een boek staat meestal op de achterkant.", False, "De titel staat op de voorkant, de kaft. Op de achterkant staat vaak een korte uitleg."),
    mk("Waar vind je een korte uitleg over waarover een boek gaat?", ["op de achterflap", "op de laatste bladzijde", "in de inhoudstafel", "op de rug van het boek"], 0, "Op de achterkant of achterflap lees je een korte uitleg die je nieuwsgierig maakt."),
    wn("In een verhaal mag de tijd verspringen, bijvoorbeeld 'drie dagen later'.", True, "Met zinnen zoals 'de volgende ochtend' of 'drie dagen later' springt de schrijver in de tijd."),
]

DEEL_2 = [
    mk("Wat is het doel van een recept?", ["je laten lachen", "uitleggen hoe je iets klaarmaakt", "vertellen wat er gisteren gebeurde", "iemand uitnodigen"], 1, "Een recept legt stap voor stap uit hoe je iets kookt of bakt."),
    mk("Wat moet zeker op een uitnodiging voor een feestje?", ["je lievelingskleur en je lievelingseten", "wanneer en waar het feest is", "het weerbericht", "een grap"], 1, "De gasten moeten weten wanneer en waar ze moeten komen."),
    wn("Een brief begin je vaak met een aanspreking, zoals 'Lieve oma'.", True, "Bovenaan schrijf je aan wie de brief is: Lieve oma, Beste juf."),
    mk("Hoe eindig je best een brief aan je oma?", ["Tot ziens, de bakker", "Dikke kus, je kleinzoon Jonas", "Einde", "Met vriendelijke groeten, de directeur"], 1, "Je sluit af met een groet en je naam."),
    inv("In een brief schrijf je bovenaan de plaats en de ___ waarop je schrijft.", "datum", "Bijvoorbeeld: Gent, 3 mei."),
    mk("Welke tekst vertelt je wat er gebeurd is in de wereld?", ["een sprookje", "een krantenbericht", "een verzonnen gedicht", "een recept"], 1, "Een krant vertelt over echte gebeurtenissen."),
    wn("Een handleiding legt uit hoe iets werkt.", True, "Bijvoorbeeld hoe je een speelgoedrobot in elkaar zet."),
    mk("Welk woord komt eerst in het woordenboek?", ["kat", "appel", "muis", "boomhut"], 1, "A komt voor b, k en m."),
    mk("Welk woord komt eerst in alfabetische volgorde?", ["bal", "bed", "bos", "bus"], 0, "Ze beginnen allemaal met b. Kijk dan naar de tweede letter: a komt voor e, o en u."),
    inv("Zet in alfabetische volgorde: zon, aap, maan. Het eerste woord is ___.", "aap", "a komt voor m en z."),
    wn("In alfabetische volgorde komt 'tafel' voor 'stoel'.", False, "De s komt voor de t, dus stoel komt eerst."),
    mk("Wat doe je als je goed luistert in een gesprek?", ["Je onderbreekt de ander telkens met je eigen verhaal.", "Je kijkt de ander aan en laat die uitspreken.", "Je speelt met je gsm.", "Je praat zelf heel luid."], 1, "Goed luisteren: aankijken, laten uitspreken en dan pas reageren."),
    wn("Als je een spreekbeurt geeft, spreek je best heel snel.", False, "Spreek rustig en duidelijk, dan kan iedereen je volgen."),
    mk("Je vertelt in de klas over je vakantie. Wat doe je best eerst?", ["meteen het einde vertellen", "zeggen waar en wanneer je weg was", "een grap vertellen over iemand anders", "meteen gaan zitten"], 1, "Begin met waar en wanneer. Dan weten de anderen waarover je vertelt."),
    inv("Een kort bericht op een papiertje aan iemand thuis noem je een ___. (b... of briefje)", ["briefje", "berichtje"], "Bijvoorbeeld: 'Mama, ik ben bij Sam. Tot straks!'"),
    mk("Wat past in een sms aan een vriend om af te spreken?", ["het hele verhaal van je dag op school", "waar en hoe laat jullie afspreken", "je huiswerk", "een lijst met woorden"], 1, "Een kort bericht om af te spreken zegt waar en wanneer."),
    wn("Een gedicht moet altijd rijmen.", False, "Veel gedichten rijmen, maar het hoeft niet."),
    mk("Waarom heeft een informatieve tekst vaak tussenkopjes?", ["om de tekst mooier en kleuriger te maken", "zodat je snel vindt wat je zoekt", "omdat er geen prenten zijn", "om de lezer te verwarren"], 1, "Tussenkopjes zeggen kort waarover elk stukje gaat."),
    wn("Een strip, een sprookje en een fabel zijn allemaal verhalen.", True, "Ze vertellen allemaal een verhaal, elk op hun eigen manier."),
    wn("In een fabel praten dieren soms zoals mensen.", True, "In een fabel spelen dieren de hoofdrol en vaak leer je er iets uit."),
]

# Prentvragen (vraag 21 tot 24), Kim 26/11.
import prent as P
_PLANT = P.p_strip("taal-strip-plant", ["bloem", "zaad", "kiem"])
_IJS = P.p_strip("taal-strip-ijs", ["ijs1", "ijs0", "ijs3"])
PRENT_1 = [
    mk("De prentjes staan door elkaar. Welke volgorde klopt?", ["B, C, A", "A, B, C", "C, A, B", "B, A, C"], 0, "Eerst het zaadje (B), dan het kiemplantje (C), op het einde de bloem (A).", prent=_PLANT),
    inv("Welk prentje hoort bij het begin van het verhaal? Schrijf de letter.", ["C", "c"], "Het verhaal begint met een vol ijsje met drie bolletjes: prentje C.", prent=_IJS),
    mk("Waar staan de woorden 'Er was eens' meestal in een verhaal?", ["in het begin", "in het midden", "op het einde", "in de titel"], 0, "Veel sprookjes beginnen met 'Er was eens'.", prent=P.p_tekst("taal-er-was-eens", ["Er was eens ..."], 34)),
    wn("In het slot van dit verhaal is het ijsje op.", True, "Het laatste prentje toont een leeg hoorntje.", prent=_IJS),
]
_FEEST = P.p_bord("taal-uitnodiging", ["UITNODIGING", "Kom naar mijn verjaardagsfeest!", "zaterdag om 14 uur", "Kerkstraat 3"], 380)
PRENT_2 = [
    inv("Lees de uitnodiging. Op welke dag is het feest?", ["zaterdag"], "In de uitnodiging staat: zaterdag om 14 uur.", prent=_FEEST),
    mk("Wat staat er NIET in de uitnodiging?", ["wat je moet meebrengen", "het uur waarop het begint", "de dag van het feest", "de straat en het huisnummer"], 0, "Dag, uur en adres staan erin. Wat je moet meebrengen, staat er niet in.", prent=_FEEST),
    inv("Lees het recept. Wat doe je bij stap 3?", ["bakken", "bak", "de pannenkoeken bakken"], "Stap 3 is bakken in de pan.", prent=P.p_bord("taal-recept", ["PANNENKOEKEN", "1. bloem en eieren mengen", "2. melk erbij gieten", "3. bakken in de pan"], 380)),
    wn("In het alfabet komt 'koe' voor 'bal'.", False, "De b komt voor de k. Dus eerst bal, dan koe.", prent=P.p_tekst("taal-alfabet", ["koe   bal   zon"], 34)),
]
