# -*- coding: utf-8 -*-
"""De vragen voor "Logica: symbolen, waarheidstabellen en poorten".

Uit de bouwsteen Logica en bewijzen van de vakfiche: de symbolen ∧, ∨, ¬, ⇒, ⇔,
∀ en ∃, de begrippen logische uitspraak, waarheidswaarde, tautologie en
contradictie, het verschil tussen de logische en de omgangstalige 'of' en
'als … dan …', nodige en voldoende voorwaarde, de kwantoren, de logische
poorten met hun symbolen en hun waarheidstabel, en het weerleggen van een
foutieve uitspraak met een tegenvoorbeeld.

Deel 1 zijn de symbolen en de betekenis. Deel 2 zijn de waarheidstabellen, de
poorten en de bewijzen uit de lijst van de fiche.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een logische uitspraak?",
        opties=[
            "een zin waarvan je kan zeggen of hij waar of vals is",
            "een zin die altijd waar is, in elke mogelijke situatie",
            "een zin die begint met een van de symbolen uit de logica",
            "een zin die een vraag stelt over twee of meer getallen",
        ],
        antwoord=0,
        uitleg="'Zeven is een priemgetal' is een uitspraak. 'Hoe laat is het?' niet: daar past geen waarheidswaarde bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool staat voor de conjunctie, dus voor 'en'?",
        opties=["∧", "∨", "¬", "⇒"],
        antwoord=0,
        uitleg="Het dakje ∧ is 'en', het omgekeerde dakje ∨ is 'of'. Ezelsbruggetje: ∧ lijkt op de A van 'and'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool staat voor de disjunctie, dus voor 'of'?",
        opties=["∨", "∧", "⇔", "∀"],
        antwoord=0,
        uitleg="De ∨ is de disjunctie. Ze is waar zodra minstens één van de twee waar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het symbool ¬ voor een uitspraak p?",
        opties=[
            "de negatie: de uitspraak die precies de omgekeerde waarheidswaarde heeft",
            "de implicatie: als p waar is, dan volgt er iets anders uit",
            "de kwantor: p geldt voor alle waarden die je kan invullen",
            "de equivalentie: p en de andere uitspraak zijn altijd samen waar",
        ],
        antwoord=0,
        uitleg="Is p waar, dan is ¬p vals, en omgekeerd. Meer doet de negatie niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verschilt de logische 'of' van de 'of' in de omgangstaal?",
        opties=[
            "in de logica is 'p of q' ook waar als p en q allebei waar zijn",
            "in de logica mag 'of' enkel tussen twee getallen staan, nooit tussen zinnen",
            "in de logica is 'p of q' alleen waar als precies één van de twee waar is",
            "in de logica is 'of' hetzelfde als 'en', in de omgangstaal niet",
        ],
        antwoord=0,
        uitleg="'Koffie of thee?' betekent in het dagelijks leven meestal één van beide. In de logica mag het allebei zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is de implicatie p ⇒ q vals?",
        opties=[
            "alleen als p waar is en q vals",
            "alleen als p vals is en q waar",
            "telkens als p en q verschillende waarheidswaarden hebben",
            "telkens als p vals is, wat q ook is",
        ],
        antwoord=0,
        uitleg="Een belofte breek je alleen door de voorwaarde te vervullen en het gevolg te laten. Is p vals, dan is de implicatie waar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is de equivalentie p ⇔ q waar?",
        opties=[
            "als p en q dezelfde waarheidswaarde hebben",
            "als p en q allebei waar zijn, en anders nooit",
            "als minstens één van de twee uitspraken waar is",
            "als p waar is, ongeacht wat de uitspraak q zegt",
        ],
        antwoord=0,
        uitleg="Allebei waar of allebei vals: dan zijn ze equivalent. Verschillen ze, dan is de equivalentie vals.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een tautologie?",
        opties=[
            "een uitspraak die waar is bij elke mogelijke invulling",
            "een uitspraak die vals is bij elke mogelijke invulling",
            "een uitspraak die soms waar en soms vals is",
            "een uitspraak waarin twee keer hetzelfde symbool staat",
        ],
        antwoord=0,
        uitleg="p ∨ ¬p is een tautologie: het regent of het regent niet, wat er ook gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een contradictie?",
        opties=[
            "een uitspraak die vals is bij elke mogelijke invulling",
            "een uitspraak die waar is bij elke mogelijke invulling",
            "een uitspraak waarover je het oneens kan zijn",
            "een uitspraak met twee negaties er vlak achter elkaar",
        ],
        antwoord=0,
        uitleg="p ∧ ¬p is een contradictie: het regent én het regent niet, dat kan nooit samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de kwantor ∀?",
        opties=[
            "voor elke waarde geldt de uitspraak",
            "er bestaat minstens één waarde waarvoor de uitspraak geldt",
            "er bestaat precies één waarde waarvoor de uitspraak geldt",
            "er bestaat geen enkele waarde waarvoor de uitspraak geldt",
        ],
        antwoord=0,
        uitleg="∀ is de universele kwantor, uit te spreken als 'voor alle'. ∃ is 'er bestaat'.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Als een vierhoek een vierkant is, dan heeft hij vier rechte hoeken.' Wat is hier een nodige voorwaarde om een vierkant te zijn?",
        opties=[
            "vier rechte hoeken hebben",
            "vier even lange zijden hebben",
            "een vierhoek zijn met evenwijdige zijden",
            "een rechthoek zijn met een diagonaal",
        ],
        antwoord=0,
        uitleg="Zonder vier rechte hoeken geen vierkant: dat is nodig. Maar het volstaat niet, want een rechthoek heeft ze ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een voorwaarde voldoende voor een uitspraak?",
        opties=[
            "als ze waar is, is de uitspraak zeker waar",
            "als ze vals is, is de uitspraak zeker vals",
            "als de uitspraak waar is, is ook de voorwaarde waar",
            "als de voorwaarde en de uitspraak elkaar uitsluiten",
        ],
        antwoord=0,
        uitleg="Een vierkant zijn is voldoende om vier rechte hoeken te hebben. Nodig is het niet: een rechthoek volstaat ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak is de negatie van 'alle leerlingen slaagden'?",
        opties=[
            "minstens één leerling slaagde niet",
            "geen enkele leerling slaagde",
            "alle leerlingen slaagden niet",
            "de meeste leerlingen slaagden niet",
        ],
        antwoord=0,
        uitleg="De negatie van ∀ is ∃ met een negatie erachter. Eén tegenvoorbeeld volstaat om 'alle' te breken.",
    ),
    dict(
        type="waarofniet",
        vraag="De uitspraak p ∨ ¬p is een tautologie.",
        antwoord=True,
        uitleg="Wat p ook is, één van de twee is waar. Dus de disjunctie is altijd waar.",
    ),
    dict(
        type="waarofniet",
        vraag="Als p vals is, dan is de implicatie p ⇒ q vals.",
        antwoord=False,
        uitleg="Bij een valse voorwaarde is de implicatie net waar. Ze breekt alleen bij p waar en q vals.",
    ),
    dict(
        type="waarofniet",
        vraag="De symbolen ∧ en ∨ mag je door elkaar gebruiken, want ze betekenen hetzelfde.",
        antwoord=False,
        uitleg="∧ is 'en', ∨ is 'of'. p ∧ q vraagt allebei, p ∨ q neemt genoegen met één.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén tegenvoorbeeld volstaat om een uitspraak met de kwantor ∀ te weerleggen.",
        antwoord=True,
        uitleg="'Alle priemgetallen zijn oneven' sneuvelt op het getal 2.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een uitspraak die bij elke invulling waar is?",
        antwoord=["tautologie", "een tautologie"],
        uitleg="Het omgekeerde, altijd vals, heet een contradictie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool uit de logica betekent 'er bestaat'?",
        antwoord=["∃", "er bestaat"],
        uitleg="∀ is 'voor alle', ∃ is 'er bestaat minstens één'.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de bewerking die de waarheidswaarde van een uitspraak omkeert?",
        antwoord=["negatie", "de negatie", "ontkenning"],
        uitleg="Het symbool ervoor is ¬.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel rijen telt de waarheidstabel van een uitspraak met twee variabelen p en q?",
        opties=["vier", "twee", "drie", "acht"],
        antwoord=0,
        uitleg="Twee variabelen, elk twee waarden: 2 maal 2 is 4 combinaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel rijen telt de waarheidstabel van een uitspraak met drie variabelen?",
        opties=["acht", "zes", "negen", "twaalf"],
        antwoord=0,
        uitleg="Elke variabele verdubbelt het aantal rijen: 2 tot de derde macht is 8.",
    ),
    dict(
        type="meerkeuze",
        vraag="p is waar en q is vals. Wat is de waarheidswaarde van p ∧ q?",
        opties=["vals", "waar", "dat hangt af van de volgorde", "dat is niet te bepalen"],
        antwoord=0,
        uitleg="De conjunctie vraagt allebei. Eén valse maakt het geheel vals.",
    ),
    dict(
        type="meerkeuze",
        vraag="p is waar en q is vals. Wat is de waarheidswaarde van p ∨ q?",
        opties=["waar", "vals", "dat hangt af van de volgorde", "dat is niet te bepalen"],
        antwoord=0,
        uitleg="De disjunctie neemt genoegen met één ware uitspraak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een EN-poort in een schakeling?",
        opties=[
            "ze geeft alleen een signaal door als beide ingangen een signaal krijgen",
            "ze geeft een signaal door zodra één van de ingangen een signaal krijgt",
            "ze keert het signaal om dat op haar ingang binnenkomt",
            "ze geeft alleen een signaal als geen van de ingangen iets krijgt",
        ],
        antwoord=0,
        uitleg="De EN-poort is de conjunctie in de elektronica: uitgang 1 alleen bij ingangen 1 en 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een NIET-poort?",
        opties=[
            "ze keert het signaal om dat op haar ingang binnenkomt",
            "ze geeft een signaal door als beide ingangen actief zijn",
            "ze geeft een signaal door als minstens één ingang actief is",
            "ze blokkeert elk signaal dat op haar ingang binnenkomt",
        ],
        antwoord=0,
        uitleg="De NIET-poort is de negatie: van 0 maakt ze 1 en van 1 maakt ze 0.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lamp brandt alleen als de hoofdschakelaar én de wandschakelaar aan staan. Welke poort past?",
        opties=["een EN-poort", "een OF-poort", "een NIET-poort", "twee NIET-poorten"],
        antwoord=0,
        uitleg="Allebei nodig, dus een conjunctie. Volstond één van de twee, dan was het een OF-poort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een alarm gaat af als de deur opengaat of als het raam opengaat. Welke poort past?",
        opties=["een OF-poort", "een EN-poort", "een NIET-poort", "een EN-poort met negatie"],
        antwoord=0,
        uitleg="Eén van beide volstaat, dus een disjunctie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vertaal je 'het is niet zo dat het regent en waait' in symbolen?",
        opties=["¬(p ∧ q)", "¬p ∧ ¬q", "¬p ∨ q", "p ∧ ¬q"],
        antwoord=0,
        uitleg="De negatie staat voor het hele stuk. Let op: ¬(p ∧ q) is niet hetzelfde als ¬p ∧ ¬q.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand beweert: 'Elk getal dat deelbaar is door 3, is ook deelbaar door 6.' Welk tegenvoorbeeld weerlegt dat?",
        opties=["9", "12", "18", "24"],
        antwoord=0,
        uitleg="9 is deelbaar door 3 maar niet door 6. De andere drie zijn door allebei deelbaar en weerleggen niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand beweert: 'Als je de zijden van een vierkant verdubbelt, verdubbelt de oppervlakte.' Wat toont een tegenvoorbeeld?",
        opties=[
            "een zijde van 2 wordt 4, en de oppervlakte gaat van 4 naar 16",
            "een zijde van 2 wordt 4, en de oppervlakte gaat van 4 naar 8",
            "een zijde van 3 wordt 6, en de omtrek gaat van 12 naar 24",
            "een zijde van 5 wordt 10, en de diagonaal wordt twee keer zo lang",
        ],
        antwoord=0,
        uitleg="De oppervlakte wordt vier keer zo groot, niet twee. Bij het volume zou het zelfs acht keer zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk bewijs staat níét in de lijst met bewijzen van deze vakfiche?",
        opties=[
            "de som van de hoeken in een vierhoek",
            "de irrationaliteit van de vierkantswortel van 2",
            "de stelling van Pythagoras",
            "de sinusregel en de cosinusregel",
        ],
        antwoord=0,
        uitleg="De lijst bevat Pythagoras, de irrationaliteit van wortel 2, de tweedegraadsfuncties, de grondformule en de sinus- en cosinusregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat mag je tijdens het examen gebruiken volgens de vakfiche?",
        opties=[
            "het formularium uit bijlage 1, maar niet de lijst met bewijzen",
            "de lijst met bewijzen uit bijlage 2, maar niet het formularium",
            "allebei de bijlagen, zolang je ze zelf meebrengt",
            "geen van beide bijlagen, alles moet uit het hoofd",
        ],
        antwoord=0,
        uitleg="Het formularium mag mee, de bewijzen niet. Die moet je zelf kunnen aanvullen en verklaren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een waarheidstabel van vier variabelen telt zestien rijen.",
        antwoord=True,
        uitleg="2 tot de vierde macht is 16.",
    ),
    dict(
        type="waarofniet",
        vraag="¬(p ∧ q) betekent hetzelfde als ¬p ∧ ¬q.",
        antwoord=False,
        uitleg="Het eerste zegt: niet allebei. Het tweede zegt: geen van beide. Dat is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Een OF-poort geeft een signaal door zodra minstens één ingang een signaal krijgt.",
        antwoord=True,
        uitleg="Dat is de disjunctie, precies zoals ∨ in de logica.",
    ),
    dict(
        type="waarofniet",
        vraag="Het getal 12 weerlegt de uitspraak dat elk getal deelbaar door 3 ook deelbaar is door 6.",
        antwoord=False,
        uitleg="12 is door allebei deelbaar en past dus juist bij de uitspraak. Je hebt 9 of 15 nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel rijen telt een waarheidstabel met drie variabelen?",
        antwoord=["8", "acht"],
        uitleg="Elke variabele verdubbelt het aantal rijen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke poort keert een signaal om, van 0 naar 1 en omgekeerd?",
        antwoord=["NIET", "de NIET-poort", "NIET-poort"],
        uitleg="In het Engels heet die poort NOT of inverter.",
    ),
    dict(
        type="invultekst",
        vraag="Geef een tegenvoorbeeld bij: elk getal deelbaar door 3 is deelbaar door 6.",
        antwoord=["9", "3", "15"],
        uitleg="Elk oneven veelvoud van 3 doet het: 3, 9, 15, 21 en zo verder.",
    ),
]
