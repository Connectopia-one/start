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
        vraag="Een verzameling is een groep dingen die bij elkaar horen. Hoe schrijf je de verzameling met 1, 2 en 3 erin?",
        opties=["{1, 2, 3}", "(1, 2, 3)", "[1, 2, 3]"],
        antwoord=0,
        uitleg="Met accolades: {1, 2, 3}. De dingen erin heten de elementen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het teken ∈?",
        opties=["is een element van", "is een deel van", "is gelijk aan"],
        antwoord=0,
        uitleg="3 ∈ {1, 2, 3} lees je als: 3 is een element van die verzameling. Hoort iets er niet bij, dan schrijf je ∉.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak klopt voor A = {2, 4, 6}?",
        opties=["4 ∈ A", "4 ∉ A", "4 ⊂ A"],
        antwoord=0,
        uitleg="4 zit in A, dus 4 ∈ A. Het teken ⊂ gebruik je tussen twee verzamelingen, niet tussen een element en een verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent B ⊂ A?",
        opties=[
            "Elk element van B zit ook in A",
            "B en A hebben niets gemeenschappelijk",
            "B is groter dan A",
        ],
        antwoord=0,
        uitleg="B is een deelverzameling van A: alles wat in B zit, zit ook in A. A mag daarnaast nog meer bevatten.",
    ),
    dict(
        type="meerkeuze",
        vraag="A = {1, 2, 3, 4} en B = {2, 4}. Wat klopt?",
        opties=["B ⊂ A", "A ⊂ B", "A ∈ B"],
        antwoord=0,
        uitleg="Zowel 2 als 4 zit in A, dus B is een deel van A. Omgekeerd niet, want 1 en 3 zitten niet in B.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de doorsnede van {1, 2, 3} en {2, 3, 4}?",
        opties=["{2, 3}", "{1, 2, 3, 4}", "{1, 4}"],
        antwoord=0,
        uitleg="De doorsnede (∩) is wat in allebei zit: 2 en 3. Denk aan het overlappende deel van twee cirkels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de unie van {1, 2} en {2, 5}?",
        opties=["{1, 2, 5}", "{2}", "{1, 5}"],
        antwoord=0,
        uitleg="De unie (∪) is alles samen, zonder iets dubbel te schrijven: {1, 2, 5}. De 2 zit er maar één keer in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk teken staat voor de doorsnede?",
        opties=["∩", "∪", "⊂"],
        antwoord=0,
        uitleg="∩ is de doorsnede en ∪ is de unie. Een ezelsbruggetje: de ∪ van unie ziet eruit als een emmer waar alles in gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="A = {1, 2, 3, 4} en B = {3, 4}. Wat is A \\ B?",
        opties=["{1, 2}", "{3, 4}", "{1, 2, 3, 4}"],
        antwoord=0,
        uitleg="Het verschil A \\ B is wat in A zit maar niet in B: {1, 2}.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je een verzameling zonder elementen?",
        opties=["De lege verzameling", "De nulverzameling", "De open verzameling"],
        antwoord=0,
        uitleg="De lege verzameling, geschreven als ∅ of { }. Let op: {0} is niet leeg, want daar zit één element in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de doorsnede van {1, 3, 5} en {2, 4, 6}?",
        opties=["De lege verzameling", "{1, 2, 3, 4, 5, 6}", "{0}"],
        antwoord=0,
        uitleg="Ze hebben geen enkel element gemeenschappelijk, dus de doorsnede is ∅.",
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
        vraag="Hoeveel elementen heeft de verzameling {3, 5, 5, 7}?",
        antwoord="3",
        uitleg="Drie. In een verzameling telt elk element maar één keer, ook al schrijf je het twee keer op.",
    ),
    dict(
        type="waarofniet",
        vraag="De volgorde waarin je de elementen opschrijft, maakt uit.",
        antwoord=False,
        uitleg="Nee. {1, 2, 3} en {3, 1, 2} zijn dezelfde verzameling. Bij coördinaten als (1, 2) maakt de volgorde wél uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="A = {2, 4, 6, 8}. Hoeveel elementen heeft A?",
        opties=["4", "8", "20"],
        antwoord=0,
        uitleg="Je telt hoeveel dingen erin zitten, niet hoe groot ze zijn: vier elementen.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke verzameling is een deelverzameling van zichzelf.",
        antwoord=True,
        uitleg="Juist. Elk element van A zit inderdaad in A, dus A ⊂ A. Ook de lege verzameling is een deel van elke verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag="A = {1, 2} en B = {1, 2}. Wat klopt?",
        opties=["A en B zijn gelijk", "A ⊂ B maar niet omgekeerd", "Hun doorsnede is leeg"],
        antwoord=0,
        uitleg="Twee verzamelingen zijn gelijk als ze precies dezelfde elementen hebben. Hun doorsnede en hun unie zijn dan allebei {1, 2}.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de unie van {1, 2, 3} en de lege verzameling?",
        opties=["{1, 2, 3}", "De lege verzameling", "{0, 1, 2, 3}"],
        antwoord=0,
        uitleg="Er komt niets bij, dus je houdt {1, 2, 3} over. De doorsnede met de lege verzameling is wél leeg.",
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
        vraag="Van 20 leerlingen doen er 12 aan voetbal en 8 aan zwemmen, en 3 doen allebei. Hoeveel doen er minstens één van de twee?",
        opties=["17", "20", "23"],
        antwoord=0,
        uitleg="12 + 8 = 20, maar dan tel je de 3 die allebei doen dubbel. Dus 20 − 3 = 17. Dat is precies wat een venndiagram zichtbaar maakt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="ℕ is de verzameling natuurlijke getallen en ℤ die van de gehele getallen. Wat klopt?",
        opties=["ℕ ⊂ ℤ", "ℤ ⊂ ℕ", "ℕ ∩ ℤ is leeg"],
        antwoord=0,
        uitleg="Elk natuurlijk getal is ook een geheel getal, dus ℕ zit in ℤ. Omgekeerd niet: −3 is geheel maar niet natuurlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de doorsnede van de even getallen en de veelvouden van 3?",
        opties=["De veelvouden van 6", "De veelvouden van 2", "De lege verzameling"],
        antwoord=0,
        uitleg="Een getal dat door 2 én door 3 deelbaar is, is deelbaar door 6: 6, 12, 18 … Dat is meteen het kleinste gemeenschappelijk veelvoud aan het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="V is de verzameling vierkanten en R die van de rechthoeken. Wat klopt?",
        opties=["V ⊂ R", "R ⊂ V", "V ∩ R is leeg"],
        antwoord=0,
        uitleg="Elk vierkant is een rechthoek, dus V zit in R. Omgekeerd niet: een rechthoek van 3 bij 5 is geen vierkant.",
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
        vraag="E is de verzameling rechten die evenwijdig zijn met rechte a, en S de verzameling rechten die a snijden. Wat is E ∩ S?",
        opties=["De lege verzameling", "Alle rechten", "Enkel rechte a"],
        antwoord=0,
        uitleg="Een rechte die evenwijdig is met a, komt a nooit tegen. Geen enkele rechte kan dus in allebei de groepen zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="A = {1, 2, 3, 4, 5} en B = {4, 5, 6}. Wat is A ∪ B?",
        opties=["{1, 2, 3, 4, 5, 6}", "{4, 5}", "{1, 2, 3}"],
        antwoord=0,
        uitleg="Alles samen, elk element één keer. De 4 en 5 zitten in allebei maar schrijf je maar één keer.",
    ),
    dict(
        type="meerkeuze",
        vraag="A = {1, 2, 3, 4, 5} en B = {4, 5, 6}. Wat is B \\ A?",
        opties=["{6}", "{4, 5}", "{1, 2, 3}"],
        antwoord=0,
        uitleg="Wat in B zit maar niet in A: enkel 6. Let op de volgorde, want A \\ B geeft {1, 2, 3} en dat is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="A \\ B is altijd hetzelfde als B \\ A.",
        antwoord=False,
        uitleg="Nee. Met A = {1, 2} en B = {2, 3} is A \\ B = {1} en B \\ A = {3}. Het verschil is niet commutatief; de doorsnede en de unie wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="A heeft 7 elementen, B heeft 5, en hun doorsnede heeft er 2. Hoeveel elementen heeft de unie?",
        opties=["10", "12", "14"],
        antwoord=0,
        uitleg="7 + 5 = 12, maar de 2 gemeenschappelijke tel je dan dubbel: 12 − 2 = 10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is {1, 2, 3} ∩ {1, 2, 3}?",
        opties=["{1, 2, 3}", "De lege verzameling", "{6}"],
        antwoord=0,
        uitleg="De doorsnede van een verzameling met zichzelf is die verzameling zelf. Hetzelfde geldt voor de unie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel deelverzamelingen heeft {a, b}?",
        opties=["4", "2", "3"],
        antwoord=0,
        uitleg="Vier: ∅, {a}, {b} en {a, b}. De lege verzameling en de verzameling zelf tellen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="P is de verzameling priemgetallen en E die van de even getallen. Wat is P ∩ E?",
        opties=["{2}", "De lege verzameling", "Alle even getallen"],
        antwoord=0,
        uitleg="2 is het enige even priemgetal, want elk ander even getal is deelbaar door 2 en heeft dus meer dan twee delers.",
    ),
    dict(
        type="meerkeuze",
        vraag="D is de verzameling delers van 12 en V die van de veelvouden van 12. Wat zit in D ∩ V?",
        opties=["{12}", "De lege verzameling", "{1, 12}"],
        antwoord=0,
        uitleg="12 is zowel een deler van zichzelf als een veelvoud van zichzelf. Geen enkel ander getal is allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag="G is de verzameling gelijkbenige driehoeken en Z die van de gelijkzijdige. Wat klopt?",
        opties=["Z ⊂ G", "G ⊂ Z", "Hun doorsnede is leeg"],
        antwoord=0,
        uitleg="Een gelijkzijdige driehoek heeft drie gelijke zijden, dus zeker ook twee: hij is ook gelijkbenig. Omgekeerd geldt dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een venndiagram is de linkercirkel volledig ingekleurd behalve het overlappende deel. Welke bewerking is dat?",
        opties=["A \\ B", "A ∩ B", "A ∪ B"],
        antwoord=0,
        uitleg="Alles van A behalve wat het met B deelt: dat is het verschil A \\ B.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van 30 leerlingen volgen er 18 Frans, 14 Duits en 5 allebei. Hoeveel volgen er geen van beide?",
        opties=["3", "2", "5"],
        antwoord=0,
        uitleg="Minstens één taal: 18 + 14 − 5 = 27. Blijft over: 30 − 27 = 3 leerlingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als A ⊂ B, dan is A ∩ B gelijk aan A.",
        antwoord=True,
        uitleg="Juist. Zit alles van A al in B, dan is alles wat ze gemeen hebben precies heel A. En A ∪ B is dan B.",
    ),
    dict(
        type="meerkeuze",
        vraag="{0} en ∅: wat is het verschil?",
        opties=[
            "{0} heeft één element, ∅ heeft er geen",
            "Het is hetzelfde",
            "∅ heeft één element",
        ],
        antwoord=0,
        uitleg="Een doos met een nul erin is niet hetzelfde als een lege doos. Dit is een klassieke strikvraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je wiskundig dat 5 niet in A zit?",
        opties=["5 ∉ A", "5 ∈ A", "5 ⊄ A"],
        antwoord=0,
        uitleg="Een streep door een teken betekent de ontkenning: ∉ is 'is geen element van'. Het teken ⊄ gebruik je tussen twee verzamelingen.",
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
