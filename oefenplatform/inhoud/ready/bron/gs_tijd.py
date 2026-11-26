# -*- coding: utf-8 -*-
"""Ready geschiedenis: Tijd (dag, week, jaar, eeuw; tijdsbalk; vroeger en nu;
stamboom en familie; bronnen). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Tijd en vroeger"
UITLEG_1 = "Jaren, eeuwen en de tijdsbalk."
UITLEG_2 = "Vroeger en nu, en je familie."

DEEL_1 = [
    mk("Hoeveel jaar is een eeuw?", ["10 jaar", "50 jaar", "100 jaar", "1 000 jaar"], 2, "Een eeuw duurt 100 jaar."),
    inv("Een periode van 10 jaar heet een ___. (d...)", ["decennium"], "Tien jaar is een decennium."),
    mk("Wat is een tijdsbalk?", ["een lijn waarop je gebeurtenissen in volgorde zet", "een balk om op te turnen", "een klok aan de muur", "een kalender voor één week"], 0, "Op een tijdsbalk staat wat eerst gebeurde links, wat later gebeurde rechts."),
    wn("Op een tijdsbalk staat wat het langst geleden is meestal links.", True, "Van links naar rechts ga je van vroeger naar later."),
    mk("Welk jaar komt eerst?", ["1950", "2010", "1990", "2026"], 0, "1950 is het langst geleden."),
    inv("In welke eeuw leven we nu? De ___ste eeuw.", ["21", "21ste", "eenentwintig"], "De jaren 2001 tot 2100 vormen de 21ste eeuw.", 21),
    wn("Je oma is later geboren dan jij.", False, "Oma is ouder, dus eerder geboren."),
    mk("Zet in volgorde, van vroeg naar laat: baby, kleuter, volwassene, kind.", ["baby, kleuter, kind, volwassene", "kind, baby, kleuter, volwassene", "volwassene, kind, kleuter, baby", "kleuter, baby, kind, volwassene"], 0, "Eerst ben je baby, dan kleuter, dan kind en later volwassene."),
    mk("Hoeveel jaar is het van 2016 tot 2026?", ["6 jaar", "10 jaar", "16 jaar", "26 jaar"], 1, "2026 − 2016 = 10 jaar."),
    wn("Het jaar 1800 ligt dichter bij nu dan het jaar 1900.", False, "1900 ligt dichter bij nu. 1800 is honderd jaar vroeger."),
    mk("Waarmee kan je te weten komen hoe het vroeger was?", ["met oude foto's en verhalen van oma en opa", "met de weersverwachting", "met een rekenmachine", "met een nieuwe gsm"], 0, "Oude foto's, voorwerpen en verhalen zijn bronnen over vroeger."),
    inv("Iets waaruit je leert over vroeger, zoals een oude brief, heet een ___. (b...)", ["bron"], "Een bron vertelt je iets over het verleden."),
    wn("Een oude munt kan een bron zijn.", True, "Ook voorwerpen vertellen iets over vroeger."),
    mk("Wat betekent 'eeuwenoud'?", ["heel erg oud", "een beetje oud", "nieuw", "van vorig jaar"], 0, "Eeuwenoud is honderden jaren oud."),
    mk("Welke gebeurtenis is het langst geleden?", ["de tijd van de Romeinen", "de eerste mens op de maan", "de uitvinding van de gsm", "jouw geboorte"], 0, "De Romeinen leefden ongeveer 2 000 jaar geleden."),
    wn("De eerste mens op de maan was in 1969.", True, "Neil Armstrong zette in 1969 als eerste mens een voet op de maan."),
    inv("Jan is in 2017 geboren. In 2026 wordt hij ___ jaar.", "9", "2026 − 2017 = 9.", 9),
    wn("In het jaar 1500 bestonden er al auto's.", False, "Auto's bestaan pas sinds ongeveer 140 jaar. In 1500 reed men te paard."),
    mk("Wat komt na de 20ste eeuw?", ["de 21ste eeuw", "de 19de eeuw", "de 10de eeuw", "de 30ste eeuw"], 0, "Na 20 komt 21."),
    wn("Gisteren is ook al geschiedenis.", True, "Alles wat voorbij is, hoort bij het verleden."),
]

DEEL_2 = [
    mk("Wat had een gezin 100 jaar geleden meestal NIET in huis?", ["een televisie", "een tafel", "een bed", "een kast"], 0, "De televisie kwam in België pas in de jaren 1950."),
    mk("Hoe wasten mensen vroeger hun kleren, voor er wasmachines waren?", ["met de hand", "in de afwasmachine van de buren", "met een stofzuiger", "ze wasten nooit"], 0, "Ze schrobden de was met de hand op een wasbord."),
    wn("Je grootouders gingen als kind al naar school.", True, "Ook zij gingen naar school, maar met andere boeken en zonder computers."),
    mk("Hoe schreven kinderen vroeger vaak op school?", ["met een griffel op een lei", "op een laptop van de school", "op een tablet met een pennetje", "met een gsm"], 0, "Ze schreven met een griffel op een leitje dat je kon uitvegen."),
    inv("Een tekening met je ouders, grootouders en overgrootouders heet een ___. (s...)", ["stamboom"], "In een stamboom zie je wie bij je familie hoort."),
    wn("Je overgrootouders zijn de ouders van je grootouders.", True, "Over-groot: nog een generatie verder terug."),
    mk("Wie is de moeder van je vader?", ["je oma", "je tante", "je zus", "je nicht"], 0, "De ouders van je ouders zijn je grootouders."),
    mk("Wat is een generatie?", ["mensen in een familie die ongeveer even oud zijn", "een soort auto", "een feest", "een land"], 0, "Jij en je broers en zussen zijn één generatie, je ouders een andere."),
    wn("Vroeger hadden alle mensen een telefoon in hun broekzak.", False, "Gsm's bestaan pas sinds ongeveer 30 jaar."),
    mk("Hoe gingen veel mensen 150 jaar geleden op reis?", ["met paard en kar", "met het vliegtuig", "met de elektrische auto", "met de raket naar de maan"], 0, "Paard en kar en de stoomtrein waren toen de manieren om te reizen."),
    inv("Een plaats waar je oude voorwerpen kan bekijken, heet een ___. (m...)", ["museum"], "In een museum leer je over vroeger."),
    wn("Speelgoed van vroeger was vaak van hout.", True, "Plastic speelgoed bestaat nog niet zo lang."),
    mk("Wat hebben kinderen vroeger en nu allebei gedaan?", ["buiten spelen", "gamen op een computer", "videobellen", "met een tablet tekenen"], 0, "Buiten spelen deden kinderen altijd al."),
    mk("Waarom kookten mensen vroeger vaak op een kachel of houtvuur?", ["Er was nog geen elektrisch fornuis.", "Ze vonden dat gezelliger dan een restaurant.", "Het was verplicht.", "Ze hadden geen honger."], 0, "Elektrische fornuizen en microgolfovens bestonden nog niet."),
    wn("Je kan je grootouders interviewen om te weten hoe het vroeger was.", True, "Vragen stellen aan ouderen is een goede manier om over vroeger te leren."),
    inv("Je mama en papa zijn je ___. (o...)", ["ouders"], "Je ouders zijn de generatie boven jou."),
    wn("Vroeger was alles beter.", False, "Sommige dingen waren anders of trager, andere waren moeilijker. Dat is geen kwestie van beter of slechter, maar van anders."),
    mk("Welk voorwerp is het nieuwst?", ["een smartphone", "een kaars", "een stoomtrein", "een ganzenveer om te schrijven"], 0, "Smartphones bestaan pas sinds een jaar of twintig."),
    wn("Elektrisch licht bestond al bij de ridders.", False, "Ridders gebruikten kaarsen en fakkels. Elektrisch licht kwam veel later."),
    mk("Wat toont een oude foto van je straat?", ["hoe je straat er vroeger uitzag", "hoe je straat er later uit zal zien", "het weer van vandaag", "de prijs van een huis"], 0, "Vergelijk de oude foto met nu: wat is er veranderd?"),
]


# Prentvragen (vraag 21 tot 24), Kim 26/11.
from vr import mk, inv, wn
import prent as P
PRENT_1 = [
    inv("Welk jaartal hoort bij het vraagteken?", "2020", "De tijdsbalk gaat telkens 10 jaar verder: 2000, 2010, 2020, 2030.", 2020, prent=P.p_tijdsbalk("tijd-balk-2020", [(60, "", "2000"), (180, "", "2010"), (300, "", "?"), (420, "", "2030")])),
    mk("Wat staat het verst in het verleden?", ["de eerste mensen", "de ridders", "mijn geboorte", "vandaag"], 0, "Op de tijdsbalk staat het verleden links. De eerste mensen staan helemaal links.", prent=P.p_tijdsbalk("tijd-balk-perioden", [(75, "eerste mensen", ""), (200, "Romeinen", ""), (310, "ridders", ""), (435, "nu", "")])),
    wn("Op deze tijdsbalk komen de Romeinen na de ridders.", False, "De Romeinen staan links van de ridders: zij leefden eerst.", prent=P.p_tijdsbalk("tijd-balk-romeinen", [(75, "eerste mensen", ""), (200, "Romeinen", ""), (310, "ridders", ""), (435, "nu", "")])),
    mk("Welke eeuw is dit?", ["de 20ste eeuw", "de 19de eeuw", "de 21ste eeuw", "de 10de eeuw"], 0, "De jaren 1900 tot en met 1999 zijn de 20ste eeuw.", prent=P.p_tekst("tijd-eeuw-1900", ["1900 – 1999"])),
]
PRENT_2 = [
    mk("Wat gebruikten mensen vroeger om licht te maken, toen er nog geen elektriciteit was?", ["een kaars", "een lamp", "een gsm", "een zaklamp"], 0, "Vroeger brandde men kaarsen en olielampen.", prent=P.p_dingen("tijd-kaars-lamp", ["kaars", "lamp"], False)),
    inv("Hoe noem je de mama van je mama?", ["oma", "grootmoeder", "bomma", "meme"], "De mama van je mama of papa is je oma.", prent=P.p_stamboom("tijd-stamboom")),
    wn("De gsm is ouder dan de telefoon met de draaischijf.", False, "De telefoon met draaischijf is veel ouder. De gsm kwam pas veel later.", prent=P.p_dingen("tijd-telefoons", ["oude-telefoon", "gsm"], False)),
    inv("Welk voorwerp is het oudste? Schrijf de letter.", ["A"], "Een kaars gebruikt men al heel lang. Een lamp en een gsm zijn uitvindingen van later.", prent=P.p_dingen("tijd-oudste", ["kaars", "gsm", "lamp"])),
]
