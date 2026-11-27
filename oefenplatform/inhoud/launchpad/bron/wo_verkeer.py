# -*- coding: utf-8 -*-
"""Launchpad WO: verkeer en veiligheid (voetganger, oversteken, gordel, fietshelm, gevaar thuis)."""
from lp import K, I, W
import lpprent as P

TITEL = "Verkeer en veilig zijn"
UITLEG_1 = "Veilig stappen en oversteken."
UITLEG_2 = "Veilig in de auto, op de fiets en thuis."

DEEL_1 = [
    K("Waar stap je als voetganger?", "op het voetpad", ["op de rijbaan", "op het fietspad", "midden op de straat"], "Het voetpad is voor voetgangers.", None),
    K("Waar steek je het best over?", "op het zebrapad", ["tussen geparkeerde auto's", "in een bocht", "achter een bus"], "Op het zebrapad zien de chauffeurs je.", None),
    K("Wat doe je voor je oversteekt?", "links, rechts en nog eens links kijken", ["snel lopen zonder kijken", "je ogen sluiten", "op je gsm kijken"], "Kijk goed of er niets aankomt.", None),
    K("Het voetgangerslicht is rood. Wat doe je?", "wachten", ["oversteken", "lopen", "rennen"], "Bij rood wacht je.", None),
    K("Het voetgangerslicht is groen. Wat doe je?", "goed kijken en dan oversteken", ["blijven staan", "terug naar huis gaan", "gaan zitten"], "Ook bij groen kijk je eerst.", None),
    K("Waarom draag je een fluohesje?", "zodat je goed gezien wordt", ["omdat het warm is", "omdat het mooi is bij regen", "om sneller te gaan"], "Fluo valt op, ook in het donker.", None),
    K("Wie helpt kinderen oversteken aan school?", "de gemachtigde opzichter", ["de bakker", "de postbode", "de dokter"], "Een gemachtigde opzichter houdt het verkeer tegen.", None),
    K("Wat betekent een rood verkeerslicht voor auto's?", "stoppen", ["sneller rijden", "toeteren", "draaien"], "Rood betekent stop.", None),
    W("Je steekt over tussen geparkeerde auto's.", False, "Daar zien de chauffeurs je niet. Steek over op het zebrapad."),
    W("Bij een rood licht wacht je.", True, "Rood = wachten."),
    W("In het donker zie je een fluohesje goed.", True, "Fluo en reflecterende strepen vallen op."),
    W("Je speelt best met een bal op de straat.", False, "Op straat rijden auto's. Speel in de tuin of op een speelplein."),
    W("Een zebrapad heeft witte strepen.", True, "Witte strepen op de weg, zoals een zebra."),
    W("Je kijkt alleen naar links voor je oversteekt.", False, "Je kijkt links, rechts en nog eens links."),
    W("Met een volwassene aan de hand stappen is veiliger.", True, "Kleine kinderen geven een volwassene een hand in het verkeer."),
    W("Oranje licht betekent: snel nog oversteken.", False, "Oranje betekent: opletten, het licht wordt rood."),
    I("Hoeveel kleuren heeft een verkeerslicht voor auto's? ___", 3, "Rood, oranje en groen.", 3),
    I("Hoeveel kleuren heeft het voetgangerslicht? ___", 2, "Rood en groen.", 2),
    K("Welke kleur heeft een fluohesje vaak?", "fluogeel", ["zwart", "donkerblauw", "bruin"], "Fluogeel of fluo-oranje valt op.", None),
    K("Wat zie je bij een zebrapad?", "witte strepen op de weg", ["een rode muur", "een groen gazon", "een zandbak"], "Witte strepen.", None),
]

DEEL_2 = [
    K("Wat doe je meteen als je in de auto zit?", "je gordel vastmaken", ["je raam open doen", "je schoenen uitdoen", "op de stoel staan"], "De gordel houdt je veilig.", None),
    K("Waar zitten kleine kinderen in de auto?", "in een kinderzitje achteraan", ["op de schoot van de chauffeur", "in de koffer", "voorin zonder gordel"], "Een kinderzitje achteraan is het veiligst.", None),
    K("Wat zet je op als je fietst?", "een fietshelm", ["een pet", "een koptelefoon", "een feesthoed"], "Een fietshelm beschermt je hoofd.", None),
    K("Wat moet aan een fiets zitten als het donker is?", "lichtjes", ["een bel alleen", "een mand", "een sticker"], "Voor en achter een lichtje, zodat je gezien wordt.", None),
    K("Waarmee laat je horen dat je eraan komt op de fiets?", "met je bel", ["met je rem", "met je lamp", "met je helm"], "Tring tring!", None),
    K("Wat raak je thuis NIET aan?", "een hete kookplaat", ["een knuffel", "een boek", "een kussen"], "Een kookplaat kan je hand verbranden.", None),
    K("Wat doe je als je medicijnen vindt?", "ze aan een volwassene geven", ["ze opeten", "ze verstoppen", "ze proeven"], "Medicijnen zijn geen snoep.", None),
    K("Welk nummer bel je als er brand of een ongeval is?", "112", ["123", "100 000", "911"], "In België en Europa bel je 112.", None),
    W("Een fietshelm beschermt je hoofd.", True, "Als je valt, vangt de helm de klap op."),
    W("In de auto mag je je gordel losmaken als het een korte rit is.", False, "Altijd vast, ook voor een korte rit."),
    W("Een kind gaat het best achteraan in de auto.", True, "Achteraan in een kinderzitje is het veiligst."),
    W("Met een stekker of stopcontact spelen is leuk en veilig.", False, "Elektriciteit is gevaarlijk."),
    W("Lucifers zijn geen speelgoed.", True, "Met vuur spelen is gevaarlijk."),
    W("Je fietst 's avonds best zonder licht.", False, "In het donker heb je licht nodig, anders zien ze je niet."),
    W("112 bel je enkel als er echt iets ergs gebeurd is.", True, "112 is voor noodgevallen."),
    W("Schoonmaakmiddel mag je proeven.", False, "Schoonmaakmiddel is gif. Niet aankomen."),
    I("Hoeveel wielen heeft een fiets? ___", 2, "Een fiets heeft 2 wielen.", 2),
    K("Wie roep je als je je pijn doet op de speelplaats?", "de juf of meester", ["niemand", "een onbekende op straat", "de kat"], "Een volwassene die je kent helpt je.", None),
    K("Een onbekende vraagt of je meegaat. Wat doe je?", "nee zeggen en het aan een volwassene vertellen", ["meegaan", "snoep vragen", "niets zeggen tegen iemand"], "Ga nooit mee met iemand die je niet kent.", None),
    K("Wat is veilig spelen?", "spelen in de tuin", ["spelen op de straat", "spelen bij het spoor", "spelen bij de rivier zonder volwassene"], "In de tuin of op een speelplein is het veilig.", None),
]

PRENT_1 = [
    K("Waar steken ze over?", "op het zebrapad", ["tussen de auto's", "in een bocht", "op het fietspad"], "Op het zebrapad met de witte strepen.", None, prent=P.een("verkeer-zebrapad", "lp-zebrapad")),
    K("Het groene mannetje brandt. Wat doe je?", "kijken en oversteken", ["blijven wachten", "rennen zonder kijken", "terug naar huis"], "Bij groen mag je oversteken, maar je kijkt toch eerst goed.", None, prent=P.een("verkeer-licht", "lp-verkeerslicht")),
    W("Het meisje draagt een fluohesje, zodat ze goed gezien wordt.", True, "Fluo valt op in het verkeer.", prent=P.een("verkeer-fluohesje", "lp-fluohesje")),
    I("Hoeveel wielen zie je aan deze kant van de bus?", 2, "Aan één kant zie je 2 wielen.", 2, prent=P.een("verkeer-schoolbus", "lp-schoolbus")),
]
PRENT_2 = [
    K("Wat draagt het kind op zijn hoofd?", "een fietshelm", ["een pet", "een muts", "niets"], "Een fietshelm beschermt je hoofd.", None, prent=P.een("verkeer-fietser", "lp-kind-fietst")),
    W("Het licht voor de voetgangers staat op rood.", False, "Het groene mannetje brandt.", prent=P.een("verkeer-licht-groen", "lp-verkeerslicht")),
    W("Het kind geeft een volwassene een hand.", True, "Kleine kinderen steken over aan de hand van een volwassene.", prent=P.een("verkeer-hand", "lp-zebrapad")),
    K("Waar gaat het kind naartoe?", "naar school", ["naar het zwembad", "naar bed", "naar de dokter"], "Het kind heeft een boekentas en stapt naar de school.", None, prent=P.een("verkeer-school", "lp-schoolkind")),
]
