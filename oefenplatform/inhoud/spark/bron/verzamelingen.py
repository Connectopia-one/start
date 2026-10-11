# -*- coding: utf-8 -*-
"""De vragen voor "Verzamelingen" (✨ Spark, wiskunde).

De vakfiche zet hieronder: element en deelverzameling, doorsnede, unie en
verschil, de lege verzameling, het venndiagram, en de notatie die daarbij
hoort (∈, ∉, ⊂, ∩, ∪, \\, ∅).

De fiche vraagt uitdrukkelijk dat je dit toepast op leerstof uit de andere
onderdelen: getallenverzamelingen, de indeling van driehoeken en vierhoeken,
de onderlinge ligging van twee rechten. Daarom gaan de laatste vragen daarover
en niet over verzinsels met appels en peren.

Deel 1 gaat over de begrippen en de tekens. Deel 2 laat ze samenwerken met
meetkunde en getallenleer.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Een verzameling is een groep dingen die bij elkaar horen. Hoe schrijf je de verzameling met \(1\), \(2\) en \(3\) erin?",
        opties=[r"\(\{1, 2, 3\}\)", r"(\(1\), \(2\), \(3\))", r"[\(1\), \(2\), \(3\)]"],
        antwoord=0,
        uitleg=r"Met accolades: \(\{1, 2, 3\}\). De dingen erin heten de elementen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent het teken \(\in\)?",
        opties=["is een element van", "is een deel van", "is gelijk aan"],
        antwoord=0,
        uitleg=r"\(3 \in \{1, 2, 3\}\) lees je als: \(3\) is een element van die verzameling. Hoort iets er niet bij, dan schrijf je \(\notin\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke uitspraak klopt voor \(A = \{2, 4, 6\}\)?",
        opties=[r"\(4 \in A\)", r"\(4 \notin A\)", r"\(4 \subset A\)"],
        antwoord=0,
        uitleg=r"\(4\) zit in \(A\), dus \(4 \in A\). Het teken \(\subset\) gebruik je tussen twee verzamelingen, niet tussen een element en een verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(B \subset A\)?",
        opties=[
            r"Elk element van \(B\) zit ook in \(A\)",
            r"\(B\) en \(A\) hebben niets gemeenschappelijk",
            r"\(B\) is groter dan \(A\)",
        ],
        antwoord=0,
        uitleg=r"\(B\) is een deelverzameling van \(A\): alles wat in \(B\) zit, zit ook in \(A\). \(A\) mag daarnaast nog meer bevatten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A = \{1, 2, 3, 4\}\) en \(B = \{2, 4\}\). Wat klopt?",
        opties=[r"\(B \subset A\)", r"\(A \subset B\)", r"\(A \in B\)"],
        antwoord=0,
        uitleg=r"Zowel \(2\) als \(4\) zit in \(A\), dus \(B\) is een deel van \(A\). Omgekeerd niet, want \(1\) en \(3\) zitten niet in \(B\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de doorsnede van \(\{1, 2, 3\}\) en \(\{2, 3, 4\}\)?",
        opties=[r"\(\{2, 3\}\)", r"\(\{1, 2, 3, 4\}\)", r"\(\{1, 4\}\)"],
        antwoord=0,
        uitleg=r"De doorsnede (\(\cap\)) is wat in allebei zit: \(2\) en \(3\). Denk aan het overlappende deel van twee cirkels.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de unie van \(\{1, 2\}\) en \(\{2, 5\}\)?",
        opties=[r"\(\{1, 2, 5\}\)", r"\(\{2\}\)", r"\(\{1, 5\}\)"],
        antwoord=0,
        uitleg=r"De unie (\(\cup\)) is alles samen, zonder iets dubbel te schrijven: \(\{1, 2, 5\}\). De \(2\) zit er maar één keer in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk teken staat voor de doorsnede?",
        opties=[r"\(\cap\)", r"\(\cup\)", r"\(\subset\)"],
        antwoord=0,
        uitleg=r"\(\cap\) is de doorsnede en \(\cup\) is de unie. Een ezelsbruggetje: de \(\cup\) van unie ziet eruit als een emmer waar alles in gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A = \{1, 2, 3, 4\}\) en \(B = \{3, 4\}\). Wat is \(A \setminus B\)?",
        opties=[r"\(\{1, 2\}\)", r"\(\{3, 4\}\)", r"\(\{1, 2, 3, 4\}\)"],
        antwoord=0,
        uitleg=r"Het verschil \(A \setminus B\) is wat in \(A\) zit maar niet in \(B\): \(\{1, 2\}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je een verzameling zonder elementen?",
        opties=["De lege verzameling", "De nulverzameling", "De open verzameling"],
        antwoord=0,
        uitleg=r"De lege verzameling, geschreven als \(\emptyset\) of \(\{\;\}\). Let op: \(\{0\}\) is niet leeg, want daar zit één element in.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de doorsnede van \(\{1, 3, 5\}\) en \(\{2, 4, 6\}\)?",
        opties=["De lege verzameling", r"\(\{1, 2, 3, 4, 5, 6\}\)", r"\(\{0\}\)"],
        antwoord=0,
        uitleg=r"Ze hebben geen enkel element gemeenschappelijk, dus de doorsnede is \(\emptyset\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een venndiagram?",
        opties=[
            "Om met cirkels te tonen wat verzamelingen gemeen hebben",
            "Om getallen op volgorde te zetten",
            "Om een gemiddelde te berekenen",
        ],
        antwoord=0,
        uitleg="Twee overlappende cirkels: in het midden staat de doorsnede, samen vormen ze de unie.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel elementen heeft de verzameling \(\{3, 5, 5, 7\}\)?",
        antwoord="3",
        uitleg="Drie. In een verzameling telt elk element maar één keer, ook al schrijf je het twee keer op.",
    ),
    dict(
        type="waarofniet",
        vraag="De volgorde waarin je de elementen opschrijft, maakt uit.",
        antwoord=False,
        uitleg=r"Nee. \(\{1, 2, 3\}\) en \(\{3, 1, 2\}\) zijn dezelfde verzameling. Bij coördinaten als (\(1\), \(2\)) maakt de volgorde wél uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A = \{2, 4, 6, 8\}\). Hoeveel elementen heeft \(A\)?",
        opties=[r"\(4\)", r"\(8\)", r"\(20\)"],
        antwoord=0,
        uitleg="Je telt hoeveel dingen erin zitten, niet hoe groot ze zijn: vier elementen.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke verzameling is een deelverzameling van zichzelf.",
        antwoord=True,
        uitleg=r"Juist. Elk element van \(A\) zit inderdaad in \(A\), dus \(A \subset A\). Ook de lege verzameling is een deel van elke verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A = \{1, 2\}\) en \(B = \{1, 2\}\). Wat klopt?",
        opties=[r"\(A\) en \(B\) zijn gelijk", r"\(A \subset B\) maar niet omgekeerd", "Hun doorsnede is leeg"],
        antwoord=0,
        uitleg=r"Twee verzamelingen zijn gelijk als ze precies dezelfde elementen hebben. Hun doorsnede en hun unie zijn dan allebei \(\{1, 2\}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de unie van \(\{1, 2, 3\}\) en de lege verzameling?",
        opties=[r"\(\{1, 2, 3\}\)", "De lege verzameling", r"\(\{0, 1, 2, 3\}\)"],
        antwoord=0,
        uitleg=r"Er komt niets bij, dus je houdt \(\{1, 2, 3\}\) over. De doorsnede met de lege verzameling is wél leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een venndiagram staat een element in het overlappende deel. Wat weet je?",
        opties=[
            "Het zit in allebei de verzamelingen",
            "Het zit in geen van beide",
            "Het zit enkel in de linkercirkel",
        ],
        antwoord=0,
        uitleg="Het overlappende deel is de doorsnede: precies de elementen die in allebei zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Van \(20\) leerlingen doen er \(12\) aan voetbal en \(8\) aan zwemmen, en \(3\) doen allebei. Hoeveel doen er minstens één van de twee?",
        opties=[r"\(17\)", r"\(20\)", r"\(23\)"],
        antwoord=0,
        uitleg=r"\(12 + 8 = 20\), maar dan tel je de \(3\) die allebei doen dubbel. Dus \(20 - 3 = 17\). Dat is precies wat een venndiagram zichtbaar maakt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"\(\mathbb{N}\) is de verzameling natuurlijke getallen en \(\mathbb{Z}\) die van de gehele getallen. Wat klopt?",
        opties=[r"\(\mathbb{N} \subset \mathbb{Z}\)", r"\(\mathbb{Z} \subset \mathbb{N}\)", r"\(\mathbb{N} \cap \mathbb{Z}\) is leeg"],
        antwoord=0,
        uitleg=r"Elk natuurlijk getal is ook een geheel getal, dus \(\mathbb{N}\) zit in \(\mathbb{Z}\). Omgekeerd niet: \(-3\) is geheel maar niet natuurlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de doorsnede van de even getallen en de veelvouden van \(3\)?",
        opties=[r"De veelvouden van \(6\)", r"De veelvouden van \(2\)", "De lege verzameling"],
        antwoord=0,
        uitleg=r"Een getal dat door \(2\) én door \(3\) deelbaar is, is deelbaar door \(6\): \(6\), \(12\), \(18\) … Dat is meteen het kleinste gemeenschappelijk veelvoud aan het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(V\) is de verzameling vierkanten en \(R\) die van de rechthoeken. Wat klopt?",
        opties=[r"\(V \subset R\)", r"\(R \subset V\)", r"\(V \cap R\) is leeg"],
        antwoord=0,
        uitleg=r"Elk vierkant is een rechthoek, dus \(V\) zit in \(R\). Omgekeerd niet: een rechthoek van \(3\) bij \(5\) is geen vierkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zit in de doorsnede van de ruiten en de rechthoeken?",
        opties=["De vierkanten", "De parallellogrammen", "Niets"],
        antwoord=0,
        uitleg="Een ruit heeft vier gelijke zijden, een rechthoek vier rechte hoeken. Allebei tegelijk is precies een vierkant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(E\) is de verzameling rechten die evenwijdig zijn met rechte a, en \(S\) de verzameling rechten die a snijden. Wat is \(E \cap S\)?",
        opties=["De lege verzameling", "Alle rechten", "Enkel rechte a"],
        antwoord=0,
        uitleg="Een rechte die evenwijdig is met a, komt a nooit tegen. Geen enkele rechte kan dus in allebei de groepen zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A = \{1, 2, 3, 4, 5\}\) en \(B = \{4, 5, 6\}\). Wat is \(A \cup B\)?",
        opties=[r"\(\{1, 2, 3, 4, 5, 6\}\)", r"\(\{4, 5\}\)", r"\(\{1, 2, 3\}\)"],
        antwoord=0,
        uitleg=r"Alles samen, elk element één keer. De \(4\) en \(5\) zitten in allebei maar schrijf je maar één keer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A = \{1, 2, 3, 4, 5\}\) en \(B = \{4, 5, 6\}\). Wat is \(B \setminus A\)?",
        opties=[r"\(\{6\}\)", r"\(\{4, 5\}\)", r"\(\{1, 2, 3\}\)"],
        antwoord=0,
        uitleg=r"Wat in \(B\) zit maar niet in \(A\): enkel \(6\). Let op de volgorde, want \(A \setminus B\) geeft \(\{1, 2, 3\}\) en dat is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(A \setminus B\) is altijd hetzelfde als \(B \setminus A\).",
        antwoord=False,
        uitleg=r"Nee. Met \(A = \{1, 2\}\) en \(B = \{2, 3\}\) is \(A \setminus B = \{1\}\) en \(B \setminus A = \{3\}\). Het verschil is niet commutatief; de doorsnede en de unie wel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(A\) heeft \(7\) elementen, \(B\) heeft \(5\), en hun doorsnede heeft er \(2\). Hoeveel elementen heeft de unie?",
        opties=[r"\(10\)", r"\(12\)", r"\(14\)"],
        antwoord=0,
        uitleg=r"\(7 + 5 = 12\), maar de \(2\) gemeenschappelijke tel je dan dubbel: \(12 - 2 = 10\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\{1, 2, 3\} \cap \{1, 2, 3\}\)?",
        opties=[r"\(\{1, 2, 3\}\)", "De lege verzameling", r"\(\{6\}\)"],
        antwoord=0,
        uitleg="De doorsnede van een verzameling met zichzelf is die verzameling zelf. Hetzelfde geldt voor de unie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel deelverzamelingen heeft \(\{a, b\}\)?",
        opties=[r"\(4\)", r"\(2\)", r"\(3\)"],
        antwoord=0,
        uitleg=r"Vier: \(\emptyset\), \(\{a\}\), \(\{b\}\) en \(\{a, b\}\). De lege verzameling en de verzameling zelf tellen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(P\) is de verzameling priemgetallen en \(E\) die van de even getallen. Wat is \(P \cap E\)?",
        opties=[r"\(\{2\}\)", "De lege verzameling", "Alle even getallen"],
        antwoord=0,
        uitleg=r"\(2\) is het enige even priemgetal, want elk ander even getal is deelbaar door \(2\) en heeft dus meer dan twee delers.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(D\) is de verzameling delers van \(12\) en \(V\) die van de veelvouden van \(12\). Wat zit in \(D \cap V\)?",
        opties=[r"\(\{12\}\)", "De lege verzameling", r"\(\{1, 12\}\)"],
        antwoord=0,
        uitleg=r"\(12\) is zowel een deler van zichzelf als een veelvoud van zichzelf. Geen enkel ander getal is allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(G\) is de verzameling gelijkbenige driehoeken en \(Z\) die van de gelijkzijdige. Wat klopt?",
        opties=[r"\(Z \subset G\)", r"\(G \subset Z\)", "Hun doorsnede is leeg"],
        antwoord=0,
        uitleg="Een gelijkzijdige driehoek heeft drie gelijke zijden, dus zeker ook twee: hij is ook gelijkbenig. Omgekeerd geldt dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een venndiagram is de linkercirkel volledig ingekleurd behalve het overlappende deel. Welke bewerking is dat?",
        opties=[r"\(A \setminus B\)", r"\(A \cap B\)", r"\(A \cup B\)"],
        antwoord=0,
        uitleg=r"Alles van \(A\) behalve wat het met \(B\) deelt: dat is het verschil \(A \setminus B\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Van \(30\) leerlingen volgen er \(18\) Frans, \(14\) Duits en \(5\) allebei. Hoeveel volgen er geen van beide?",
        opties=[r"\(3\)", r"\(2\)", r"\(5\)"],
        antwoord=0,
        uitleg=r"Minstens één taal: \(18 + 14 - 5 = 27\). Blijft over: \(30 - 27 = 3\) leerlingen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(A \subset B\), dan is \(A \cap B\) gelijk aan \(A\).",
        antwoord=True,
        uitleg=r"Juist. Zit alles van \(A\) al in \(B\), dan is alles wat ze gemeen hebben precies heel \(A\). En \(A \cup B\) is dan \(B\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(\{0\}\) en \(\emptyset\): wat is het verschil?",
        opties=[
            r"\(\{0\}\) heeft één element, \(\emptyset\) heeft er geen",
            "Het is hetzelfde",
            r"\(\emptyset\) heeft één element",
        ],
        antwoord=0,
        uitleg="Een doos met een nul erin is niet hetzelfde als een lege doos. Dit is een klassieke strikvraag.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe schrijf je wiskundig dat \(5\) niet in \(A\) zit?",
        opties=[r"\(5 \notin A\)", r"\(5 \in A\)", r"\(5 \not\subset A\)"],
        antwoord=0,
        uitleg=r"Een streep door een teken betekent de ontkenning: \(\notin\) is 'is geen element van'. Het teken \(\not\subset\) gebruik je tussen twee verzamelingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een venndiagram handig bij een vraagstuk met twee groepen?",
        opties=[
            "Je ziet meteen wie dubbel geteld wordt",
            "Het rekent vanzelf",
            "Het toont het gemiddelde",
        ],
        antwoord=0,
        uitleg="De meest gemaakte fout bij zulke vraagstukken is de overlap dubbel tellen. In een tekening staat die overlap apart, en dan zie je het.",
    ),
]
