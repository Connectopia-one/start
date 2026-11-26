# -*- coding: utf-8 -*-
"""Ready wiskunde: Meetkunde (rechte, scherpe en stompe hoeken, vlakke figuren en
ruimtefiguren, evenwijdig en loodrecht, spiegelen en symmetrieas, aanzichten,
plaats bepalen in een rooster). Doel einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Meetkunde"
UITLEG_1 = 'Hoeken en platte figuren.'
UITLEG_2 = 'Kubus, bol, cilinder en spiegelen.'

DEEL_1 = [
    mk("Welke hoek is even groot als de hoek van een blad papier?", ["een scherpe hoek", "een rechte hoek", "een stompe hoek", "een gestrekte hoek"], 1, "De hoek van een blad is een rechte hoek."),
    mk("Hoe heet een hoek die kleiner is dan een rechte hoek?", ["een stompe hoek", "een scherpe hoek", "een grote hoek", "een gestrekte hoek"], 1, "Kleiner dan recht noem je scherp."),
    wn("Een stompe hoek is groter dan een rechte hoek.", True, "Stomp betekent groter dan recht, maar kleiner dan een gestrekte hoek."),
    mk("Hoeveel hoeken heeft een driehoek?", ["2", "3", "4", "6"], 1, "Drie zijden en drie hoeken: daar komt de naam vandaan."),
    inv("Een vierkant heeft ___ rechte hoeken.", "4", "Alle vier de hoeken van een vierkant zijn recht.", 4),
    wn("Een rechthoek heeft vier even lange zijden.", False, "Bij een rechthoek zijn telkens de tegenover elkaar liggende zijden even lang. Vier even lange zijden en vier rechte hoeken: dat is een vierkant."),
    mk("Welke figuur heeft geen hoeken?", ["een vierkant", "een driehoek", "een cirkel", "een rechthoek"], 2, "Een cirkel is rond en heeft geen hoeken."),
    mk("Hoe noem je twee lijnen die elkaar nooit raken, hoe ver je ze ook doortrekt?", ["loodrecht", "evenwijdig", "schuin", "gebogen"], 1, "Evenwijdige lijnen lopen altijd even ver van elkaar, zoals de rails van een trein."),
    wn("Loodrechte lijnen maken samen een rechte hoek.", True, "Zoals de rand van een tafel en de tafelpoot."),
    inv("Een zeshoek heeft ___ zijden.", "6", "Zes hoeken en zes zijden.", 6),
    mk("Welke lijnen zijn evenwijdig?", ["de twee lange zijden van een rechthoek", "twee zijden van een driehoek", "de wijzers om drie uur", "de lijnen van een kruis"], 0, "De twee lange zijden van een rechthoek lopen naast elkaar en raken elkaar nooit."),
    wn("Een driehoek kan twee rechte hoeken hebben.", False, "Met twee rechte hoeken sluit de figuur niet. Een driehoek heeft hoogstens één rechte hoek."),
    mk("Om drie uur maken de wijzers van een klok een ...", ["scherpe hoek", "rechte hoek", "stompe hoek", "volle hoek"], 1, "De grote wijzer staat op 12 en de kleine op 3: dat is een rechte hoek."),
    inv("Een vijfhoek heeft ___ hoeken.", "5", "Vijfhoek: vijf hoeken en vijf zijden.", 5),
    wn("Een ruit heeft vier even lange zijden.", True, "Een ruit heeft vier even lange zijden, maar de hoeken zijn niet altijd recht."),
    mk("Welke figuur heeft 4 zijden die even lang zijn en 4 rechte hoeken?", ["een rechthoek", "een ruit", "een vierkant", "een trapezium"], 2, "Een vierkant heeft vier even lange zijden en vier rechte hoeken."),
    mk("Om tien over twaalf maken de wijzers een ...", ["scherpe hoek", "rechte hoek", "stompe hoek", "gestrekte hoek"], 0, "De wijzers staan op 12 en op 2. Dat is een kleine, scherpe hoek."),
    wn("Een rechthoek heeft evenwijdige zijden.", True, "De tegenover elkaar liggende zijden van een rechthoek zijn evenwijdig."),
    inv("Hoeveel zijden hebben 2 driehoeken samen? ___", "6", "2 × 3 = 6 zijden.", 6),
    wn("Een cirkel is een veelhoek.", False, "Een veelhoek heeft rechte zijden en hoeken. Een cirkel heeft geen van beide."),
]

DEEL_2 = [
    mk("Welke is een ruimtefiguur?", ["een cirkel", "een kubus", "een vierkant", "een driehoek"], 1, "Een kubus kan je vastnemen, zoals een dobbelsteen. De andere figuren zijn plat."),
    mk("Welke vorm heeft een voetbal?", ["een kubus", "een cilinder", "een bol", "een piramide"], 2, "Een voetbal is rond aan alle kanten: een bol."),
    inv("Een kubus heeft ___ vlakken.", "6", "Kijk naar een dobbelsteen: 6 vlakken, met 1 tot 6 ogen.", 6),
    mk("Welke vorm heeft een blikje frisdrank?", ["een balk", "een cilinder", "een bol", "een kegel"], 1, "Een blikje is rond met een platte boven- en onderkant: een cilinder."),
    wn("Een balk heeft allemaal vierkante vlakken.", False, "Een balk heeft rechthoekige vlakken, zoals een schoenendoos. Bij een kubus zijn ze allemaal vierkant."),
    mk("Welke vorm heeft een ijshoorntje?", ["een cilinder", "een bol", "een kegel", "een kubus"], 2, "Een ijshoorntje loopt van rond naar een punt: een kegel."),
    wn("Een symmetrieas verdeelt een figuur in twee gelijke spiegelbeelden.", True, "Als je de figuur op de as plooit, vallen beide helften precies op elkaar."),
    mk("Hoeveel symmetrieassen heeft een vierkant?", ["1", "2", "4", "0"], 2, "Twee assen van midden naar midden en twee langs de diagonalen: 4."),
    mk("Welke hoofdletter heeft een verticale symmetrieas?", ["F", "A", "R", "G"], 1, "Plooi je de A van boven naar beneden in het midden, dan vallen de helften op elkaar."),
    wn("De letter P heeft een symmetrieas.", False, "De P heeft geen as waarbij beide helften op elkaar vallen."),
    inv("Een rechthoek die geen vierkant is, heeft ___ symmetrieassen.", "2", "Eén van boven naar onder en één van links naar rechts. De diagonalen werken niet.", 2),
    mk("Je kijkt recht van boven op een cilinder. Wat zie je?", ["een rechthoek", "een cirkel", "een driehoek", "een vierkant"], 1, "Het bovenaanzicht van een cilinder is een cirkel."),
    mk("Je kijkt van voren naar een cilinder die rechtop staat. Wat zie je?", ["een cirkel", "een rechthoek", "een driehoek", "een vijfhoek"], 1, "Het vooraanzicht van een staande cilinder is een rechthoek."),
    wn("Het bovenaanzicht van een kubus is een vierkant.", True, "Elk vlak van een kubus is een vierkant, dus ook wat je van boven ziet."),
    mk("In een rooster staan de letters bovenaan en de cijfers links. Wat betekent C4?", ["kolom 4, rij C", "kolom C, rij 4", "4 vakjes naar links", "4 keer C"], 1, "Eerst de letter (kolom), dan het cijfer (rij): kolom C, rij 4."),
    inv("Je staat op vakje B2 en gaat 2 vakjes naar rechts. Dan sta je op ___2.", "D", "Na B komt C, en dan D. Het cijfer blijft hetzelfde: D2."),
    wn("Een spiegelbeeld is altijd kleiner dan de figuur zelf.", False, "Spiegelen verandert de grootte niet, enkel de richting."),
    mk("Hoeveel hoekpunten heeft een kubus?", ["4", "6", "8", "12"], 2, "4 hoekpunten boven en 4 onder: 8.", 8),
    wn("Een bol heeft één plat vlak.", False, "Een bol is overal rond en heeft geen enkel plat vlak."),
    wn("Een piramide met een vierkant grondvlak heeft 4 driehoekige zijvlakken.", True, "Vier driehoeken komen samen in de top, en onderaan ligt het vierkant."),
]
