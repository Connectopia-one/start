# -*- coding: utf-8 -*-
"""De vragen voor "De kosten- en de opbrengstencurven" (🚀 Boost doorstroom,
economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"het keuzegedrag van de producent in een markt met volkomen concurrentie":
het berekenen en het verloop van de kostencurven TCK, TVK, TK, GCK, GVK, GK en
MK, en van de opbrengstencurven TO, GO en MO. De optimale productiegrootte
staat in [[ec_optimaal]], de productiefunctie in [[ec_productie]].

Deel 1 gaat over de kosten: het verschil tussen constante en variabele kosten,
de totale en de gemiddelde kosten, de marginale kost, en hoe die curven
verlopen.
Deel 2 gaat over de opbrengsten: de totale, gemiddelde en marginale opbrengst,
en waarom bij volkomen concurrentie GO en MO allebei gelijk zijn aan de prijs.

Afspraak in dit thema: elke afkorting wordt bij haar eerste gebruik in een
vraag voluit geschreven, en alle cijfers staan in de vraag zelf.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn totale constante kosten TCK?",
        opties=[
            "Kosten die niet veranderen met de geproduceerde hoeveelheid",
            "Kosten die elke maand hetzelfde bedrag blijven",
            "Kosten die het bedrijf niet kan vermijden bij een faillissement",
            "Kosten die altijd door de overheid betaald worden",
        ],
        antwoord=0,
        uitleg="Constante kosten lopen door of je nu één stuk maakt of duizend: huur, verzekering, afschrijving. Of het bedrag maandelijks hetzelfde is, doet er niet toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn constante kosten? Duid alles aan wat juist is.",
        opties=[
            "De huur van de werkplaats",
            "De verzekering van het gebouw",
            "De afschrijving van een machine",
            "De grondstoffen voor elk stuk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Huur, verzekering en afschrijving lopen door, ook bij nul productie. Grondstoffen heb je alleen nodig als je produceert: dat zijn variabele kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn variabele kosten? Duid alles aan wat juist is.",
        opties=[
            "De grondstoffen voor elk stuk",
            "De energie die een machine per stuk verbruikt",
            "De uurlonen van wie per gemaakt stuk betaald wordt",
            "De brandverzekering van de werkplaats",
        ],
        antwoord=[0, 1, 2],
        uitleg="Variabele kosten stijgen mee met de hoeveelheid: grondstoffen, energie per stuk en uurlonen. Produceer je niets, dan zijn ze nul. De verzekering loopt wel gewoon door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de totale kosten TK?",
        opties=[
            "TCK plus TVK",
            "TCK min TVK",
            "TCK maal TVK",
            "TVK gedeeld door de hoeveelheid",
        ],
        antwoord=0,
        uitleg="De totale kosten zijn de som van de constante en de variabele kosten bij die hoeveelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf heeft 2 000 euro constante kosten en 6 euro variabele kost per stuk. Hoe groot zijn TK bij 500 stuks?",
        opties=[
            "5 000 euro",
            "3 000 euro",
            "2 006 euro",
            "8 000 euro",
        ],
        antwoord=0,
        uitleg="500 maal 6 is 3 000 euro variabele kosten, plus 2 000 euro constante kosten is 5 000 euro.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de afkorting TK voor? Schrijf twee woorden.",
        antwoord=["totale kosten", "totale kost"],
        uitleg="TK zijn de totale kosten: de constante plus de variabele kosten samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de gemiddelde kost GK?",
        opties=[
            "De totale kosten gedeeld door de geproduceerde hoeveelheid",
            "Het gemiddelde van de constante en de variabele kosten",
            "De kost van het laatst geproduceerde stuk",
            "De gemiddelde kost van alle bedrijven in de sector",
        ],
        antwoord=0,
        uitleg="GK is de kostprijs per stuk: TK gedeeld door Q. De kost van het laatste stuk is de marginale kost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zelfde bedrijf: 5 000 euro totale kosten bij 500 stuks. Hoe groot is de gemiddelde kost?",
        opties=[
            "10 euro",
            "6 euro",
            "4 euro",
            "100 euro",
        ],
        antwoord=0,
        uitleg="5 000 gedeeld door 500 is 10 euro per stuk.",
    ),
    dict(
        type="waarofniet",
        vraag="De marginale kost MK is de gemiddelde kost van alle geproduceerde stuks samen.",
        antwoord=False,
        uitleg="MK is wat er aan de totale kosten bijkomt als je één eenheid extra maakt. Het is een verschil, geen gemiddelde: dat laatste is GK.",
    ),
    dict(
        type="waarofniet",
        vraag="De constante kosten lopen door, ook als een bedrijf even niets produceert.",
        antwoord=True,
        uitleg="Huur en verzekering betaal je ook bij een stilstaande fabriek. Daarom zijn ze constant: ze hangen niet aan de productie vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de gemiddelde constante kost GCK als de productie stijgt?",
        opties=[
            "Ze daalt voortdurend, want hetzelfde bedrag wordt over meer stuks verdeeld",
            "Ze stijgt voortdurend, want de totale kosten stijgen",
            "Ze blijft gelijk, want de constante kosten blijven gelijk",
            "Ze daalt eerst en stijgt daarna weer",
        ],
        antwoord=0,
        uitleg="2 000 euro over 100 stuks is 20 euro per stuk, over 1 000 stuks nog maar 2 euro. Die daling heet de degressie van de constante kosten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de extra kost van één stuk meer? Schrijf twee woorden.",
        antwoord=["marginale kost", "marginale kosten"],
        uitleg="De marginale kost MK is de stijging van TK bij één eenheid extra.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de curve van de gemiddelde kosten GK meestal?",
        opties=[
            "Eerst dalend, dan stijgend, als een u-vorm",
            "Voortdurend dalend",
            "Voortdurend stijgend",
            "Een rechte horizontale lijn",
        ],
        antwoord=0,
        uitleg="In het begin wordt de constante kost over meer stuks verdeeld, dus GK daalt. Later wegen de stijgende variabele kosten door en gaat GK weer omhoog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de marginale kost kloppen? Duid alles aan wat juist is.",
        opties=[
            "MK hangt alleen af van de variabele kosten",
            "MK daalt eerst en stijgt daarna",
            "MK snijdt GK in het laagste punt van GK",
            "MK is altijd gelijk aan GK",
        ],
        antwoord=[0, 1, 2],
        uitleg="Constante kosten veranderen niet bij een stuk meer, dus ze zitten niet in MK. En de curve van MK snijdt die van GK precies waar GK het laagst is.",
    ),
    dict(
        type="waarofniet",
        vraag="Zolang MK onder GK ligt, stijgt GK.",
        antwoord=False,
        uitleg="Dan daalt GK net. Komt er een stuk bij dat goedkoper is dan het gemiddelde, dan trekt dat het gemiddelde omlaag. Pas als MK boven GK ligt, stijgt GK.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf produceert 100 stuks aan 1 200 euro totale kosten en 101 stuks aan 1 209 euro. Hoe groot is MK van het 101ste stuk?",
        opties=[
            "9 euro",
            "12 euro",
            "11,97 euro",
            "1 209 euro",
        ],
        antwoord=0,
        uitleg="1 209 min 1 200 is 9 euro. Dat is wat dat ene extra stuk extra kostte.",
    ),
    dict(
        type="waarofniet",
        vraag="MK stijgt vanaf een bepaald punt omdat elke extra werknemer minder toevoegt dan de vorige.",
        antwoord=True,
        uitleg="De kostencurve is het spiegelbeeld van de productiefunctie. Zodra de meeropbrengsten afnemen, heb je meer inzet nodig voor één stuk extra, en dus kost dat stuk meer.",
    ),
    dict(
        type="invultekst",
        vraag="Welke afkorting gebruik je voor de gemiddelde variabele kost? Schrijf één woord.",
        antwoord=["GVK", "gvk"],
        uitleg="GVK is de totale variabele kost gedeeld door de hoeveelheid: de variabele kost per stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakkerij betaalt 1 500 euro huur per maand en 0,80 euro grondstof per brood. Welke uitspraken kloppen? Duid alles aan wat juist is.",
        opties=[
            "De huur is een constante kost",
            "De grondstof is een variabele kost",
            "Bij 3 000 broden bedraagt de gemiddelde constante kost 0,50 euro",
            "Bij 3 000 broden bedraagt de gemiddelde kost 0,80 euro",
        ],
        antwoord=[0, 1, 2],
        uitleg="1 500 gedeeld door 3 000 is 0,50 euro constante kost per brood. Samen met 0,80 euro grondstof is de gemiddelde kost 1,30 euro, niet 0,80 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het voor een bedrijf belangrijk om constante en variabele kosten uit elkaar te houden?",
        opties=[
            "Omdat alleen de variabele kosten meespelen in de beslissing over één stuk meer",
            "Omdat alleen de constante kosten in de boekhouding komen",
            "Omdat de overheid alleen de variabele kosten belast",
            "Omdat de klant alleen de constante kosten betaalt",
        ],
        antwoord=0,
        uitleg="Of je dat ene stuk extra maakt, hangt af van wat het extra kost en opbrengt. De huur verandert daar toch niet door.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de totale opbrengst TO?",
        opties=[
            "De prijs maal de verkochte hoeveelheid",
            "De prijs min de kostprijs van een stuk",
            "De winst van het bedrijf in een jaar",
            "De opbrengst van het laatst verkochte stuk",
        ],
        antwoord=0,
        uitleg="TO is prijs maal hoeveelheid. Trek je daar de totale kosten van af, dan krijg je de winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf verkoopt 400 stuks aan 15 euro. Hoe groot is de totale opbrengst?",
        opties=[
            "6 000 euro",
            "415 euro",
            "26,7 euro",
            "600 euro",
        ],
        antwoord=0,
        uitleg="400 maal 15 is 6 000 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de gemiddelde opbrengst GO?",
        opties=[
            "De totale opbrengst gedeeld door de hoeveelheid",
            "De opbrengst van het laatste stuk",
            "De opbrengst min de kosten per stuk",
            "De opbrengst van een gemiddeld bedrijf in de sector",
        ],
        antwoord=0,
        uitleg="GO is TO gedeeld door Q. Omdat TO prijs maal Q is, is GO altijd gewoon de prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is GO bij volkomen concurrentie gelijk aan de prijs?",
        opties=[
            "Omdat TO prijs maal hoeveelheid is, en je die hoeveelheid er weer uitdeelt",
            "Omdat de prijs bij volkomen concurrentie altijd stijgt",
            "Omdat elk bedrijf een andere prijs mag vragen",
            "Omdat de gemiddelde kost gelijk is aan de prijs",
        ],
        antwoord=0,
        uitleg="GO is prijs maal Q, gedeeld door Q. De hoeveelheid valt weg en er blijft de prijs over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de marginale opbrengst MO?",
        opties=[
            "De extra opbrengst van één stuk meer verkopen",
            "De gemiddelde opbrengst per stuk",
            "De opbrengst min de marginale kost",
            "De hoogste prijs die een bedrijf kan vragen",
        ],
        antwoord=0,
        uitleg="MO is de stijging van TO bij één eenheid extra. Bij volkomen concurrentie is dat precies de prijs, want elk stuk brengt evenveel op.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij volkomen concurrentie zijn GO en MO allebei gelijk aan de prijs.",
        antwoord=True,
        uitleg="Het bedrijf is prijsnemer: het krijgt voor elk stuk dezelfde prijs, ongeacht hoeveel het verkoopt. Daarom vallen prijs, GO en MO samen.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de afkorting MO voor? Schrijf twee woorden.",
        antwoord=["marginale opbrengst", "marginale opbrengsten"],
        uitleg="MO is de marginale opbrengst: de extra opbrengst van één stuk meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de curve van TO bij volkomen concurrentie?",
        opties=[
            "Als een stijgende rechte door de oorsprong",
            "Als een stijgende rechte die de verticale as snijdt",
            "Als een dalende rechte",
            "Als een u-vormige curve",
        ],
        antwoord=0,
        uitleg="Elk stuk brengt dezelfde prijs op, dus TO stijgt gelijkmatig. Bij nul stuks is TO nul, dus de rechte vertrekt uit de oorsprong.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt de curve van MO bij volkomen concurrentie?",
        opties=[
            "Als een horizontale rechte op de hoogte van de prijs",
            "Als een stijgende rechte",
            "Als een dalende rechte",
            "Als een u-vormige curve",
        ],
        antwoord=0,
        uitleg="De prijs ligt vast voor dit bedrijf, dus elk extra stuk brengt evenveel op. De MO-curve ligt vlak, op de hoogte van die prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de opbrengsten bij volkomen concurrentie kloppen? Duid alles aan wat juist is.",
        opties=[
            "TO stijgt rechtlijnig met de hoeveelheid",
            "GO is gelijk aan de prijs",
            "MO is gelijk aan de prijs",
            "MO daalt naarmate je meer verkoopt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij volkomen concurrentie blijft de prijs voor dit bedrijf dezelfde. Een dalende MO hoort bij een bedrijf dat zijn prijs moet laten zakken om meer te verkopen, en dat is hier niet zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een landbouwer verkoopt aardappelen op de wereldmarkt aan 0,35 euro per kilo. Wat is zijn MO bij de duizendste kilo?",
        opties=[
            "0,35 euro",
            "350 euro",
            "0,70 euro",
            "Dat hangt af van zijn kosten",
        ],
        antwoord=0,
        uitleg="Hij is prijsnemer: ook de duizendste kilo brengt 0,35 euro op. De kosten spelen hier geen rol, die zitten in MK.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie meer wil verkopen, moet bij volkomen concurrentie zijn prijs verlagen.",
        antwoord=False,
        uitleg="Zijn aandeel in de markt is zo klein dat hij alles kwijtraakt aan de marktprijs. Verlagen hoeft niet, en verhogen kan niet, want dan koopt niemand bij hem.",
    ),
    dict(
        type="invultekst",
        vraag="Welke afkorting gebruik je voor de totale winst? Schrijf één woord.",
        antwoord=["TW", "tw"],
        uitleg="De totale winst TW is de totale opbrengst min de totale kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf heeft TO van 8 000 euro en TK van 7 200 euro. Hoe groot is de winst?",
        opties=[
            "800 euro",
            "15 200 euro",
            "1,11 euro",
            "7 200 euro",
        ],
        antwoord=0,
        uitleg="8 000 min 7 200 is 800 euro winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer maakt een bedrijf verlies?",
        opties=[
            "Wanneer de gemiddelde kost boven de prijs ligt",
            "Wanneer de marginale kost boven de marginale opbrengst ligt",
            "Wanneer de constante kosten hoger zijn dan de variabele",
            "Wanneer de gemiddelde kost daalt",
        ],
        antwoord=0,
        uitleg="Kost elk stuk gemiddeld meer dan het opbrengt, dan verlies je op elk stuk. Dat MK boven MO ligt, betekent alleen dat je over je optimum heen zit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bedrijf met een hoge totale opbrengst maakt zeker winst.",
        antwoord=False,
        uitleg="Als de kosten even hoog of hoger liggen, blijft er niets of een verlies over. Winst is altijd een verschil, nooit een opbrengst alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om de winst bij een bepaalde hoeveelheid te berekenen? Duid alles aan wat juist is.",
        opties=[
            "De prijs per stuk",
            "De geproduceerde hoeveelheid",
            "De totale kosten bij die hoeveelheid",
            "Het aantal concurrenten op de markt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Prijs maal hoeveelheid geeft TO, en daar haal je TK van af. Hoeveel concurrenten er zijn, verandert niets aan die berekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf verkoopt 250 stuks aan 20 euro en heeft 3 000 euro constante en 10 euro variabele kost per stuk. Hoe groot is de winst?",
        opties=[
            "Een verlies van 500 euro",
            "Een winst van 500 euro",
            "Een winst van 2 500 euro",
            "Een verlies van 3 000 euro",
        ],
        antwoord=0,
        uitleg="TO is 250 maal 20 is 5 000 euro. TK is 3 000 plus 250 maal 10 is 5 500 euro. 5 000 min 5 500 geeft 500 euro verlies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tekent men de kosten- en de opbrengstencurven in dezelfde grafiek?",
        opties=[
            "Omdat je dan in één beeld ziet waar de winst het grootst is",
            "Omdat ze allebei in euro per stuk uitgedrukt zijn",
            "Omdat ze allebei uit de productiefunctie volgen",
            "Omdat de overheid dat zo voorschrijft",
        ],
        antwoord=0,
        uitleg="Het verschil tussen de twee is de winst. Door ze samen te zetten, zie je meteen bij welke hoeveelheid dat verschil het grootst is.",
    ),
    dict(
        type="waarofniet",
        vraag="Ligt de prijs precies op de laagste gemiddelde kost, dan maakt het bedrijf geen winst en geen verlies.",
        antwoord=True,
        uitleg="Opbrengst per stuk is dan precies gelijk aan kost per stuk. Dat punt heet het break-evenpunt: alle kosten zijn gedekt, winst is er niet.",
    ),
]
