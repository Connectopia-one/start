# -*- coding: utf-8 -*-
"""De vragen voor "Telproblemen met boom- en venndiagram".

Uit de bouwsteen Data en onzekerheid: telproblemen oplossen met een
boomdiagram of een venndiagram, en redeneren met de somregel, de productregel
en de complementregel. De fiche vraagt uitdrukkelijk dat je die regels
redeneert vanuit het diagram en ze niet als abstracte formules toepast, dus de
vragen vertrekken telkens van een situatie.

Deel 1 is het tellen met een boomdiagram en de productregel. Deel 2 is het
venndiagram met de somregel, de complementregel en de doorsnede.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een boomdiagram?",
        opties=[
            "om alle mogelijke uitkomsten van opeenvolgende keuzes te tonen",
            "om te tonen hoeveel elementen twee groepen gemeen hebben",
            "om gegevens in klassen te verdelen en te tellen",
            "om de spreiding van een reeks getallen te tonen",
        ],
        antwoord=0,
        uitleg="Elke tak is één keuze; een pad van boven naar onder is één uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de productregel?",
        opties=[
            "je vermenigvuldigt het aantal keuzes van elke stap met elkaar",
            "je telt het aantal keuzes van elke stap bij elkaar op",
            "je trekt de dubbels af van het totaal aantal keuzes",
            "je deelt het totaal door het aantal stappen",
        ],
        antwoord=0,
        uitleg="Bij twee keuzes na elkaar splitst elke tak opnieuw, dus de aantallen vermenigvuldigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kiest een broek uit 4 en een trui uit 6. Hoeveel combinaties zijn er?",
        opties=["24", "10", "12", "46"],
        antwoord=0,
        uitleg="De productregel: 4 maal 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een slot heeft drie cijferschijven met elk de cijfers 0 tot en met 9. Hoeveel codes zijn er?",
        opties=["1000", "30", "720", "100"],
        antwoord=0,
        uitleg="10 maal 10 maal 10. De cijfers mogen zich herhalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit twee keer met een gewone dobbelsteen. Hoeveel verschillende uitkomsten zijn er?",
        opties=["36", "12", "21", "18"],
        antwoord=0,
        uitleg="6 maal 6. In het boomdiagram splitst elke tak in zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vijf lopers strijden om goud, zilver en brons. Hoeveel volgordes zijn mogelijk op het podium?",
        opties=["60", "125", "15", "10"],
        antwoord=0,
        uitleg="5 maal 4 maal 3: wie goud haalt, kan geen zilver meer halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen trekken met en zonder terugleggen?",
        opties=[
            "zonder terugleggen daalt het aantal keuzes bij elke stap",
            "zonder terugleggen blijft het aantal keuzes gelijk",
            "met terugleggen is er maar één uitkomst mogelijk",
            "er is geen verschil in het aantal uitkomsten",
        ],
        antwoord=0,
        uitleg="Bij terugleggen splitst elke tak telkens in evenveel takken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel takken vertrekken er uit het beginpunt van een boomdiagram?",
        opties=[
            "evenveel als er keuzes zijn in de eerste stap",
            "evenveel als er uitkomsten zijn in het geheel",
            "altijd twee, want een boom splitst in tweeën",
            "evenveel als er stappen na elkaar komen",
        ],
        antwoord=0,
        uitleg="De volgende splitsing hoort bij de tweede stap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom past een boomdiagram niet meer bij tien opeenvolgende muntworpen?",
        opties=[
            "er zouden 1024 paden zijn, dat tekent niemand nog uit",
            "een munt heeft te weinig mogelijke uitkomsten per worp",
            "bij een munt geldt de productregel niet",
            "een boomdiagram werkt enkel met dobbelstenen",
        ],
        antwoord=0,
        uitleg="Je gebruikt dan enkel de productregel: 2 tot de tiende macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een menu heeft 3 voorgerechten, 4 hoofdgerechten en 2 desserts. Hoeveel menu's kan je samenstellen?",
        opties=["24", "9", "14", "12"],
        antwoord=0,
        uitleg="3 maal 4 maal 2.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietsslot heeft vier schijven met elk zes tekens. Hoeveel codes zijn er?",
        opties=["1296", "24", "360", "4096"],
        antwoord=0,
        uitleg="6 tot de vierde macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit twee dobbelstenen. In hoeveel van de 36 uitkomsten is de som 7?",
        opties=["6", "5", "7", "4"],
        antwoord=0,
        uitleg="1 met 6, 2 met 5, 3 met 4, en die drie ook omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tel je bij een boomdiagram de paden en niet de takken?",
        opties=[
            "één pad van boven naar onder is één volledige uitkomst",
            "takken horen bij tussenstappen en tellen dubbel mee",
            "er zijn altijd evenveel paden als takken",
            "takken kan je niet tellen als er veel stappen zijn",
        ],
        antwoord=0,
        uitleg="Een tak is één keuze, een pad is de hele reeks keuzes.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij twee keuzes na elkaar vermenigvuldig je de aantallen.",
        antwoord=True,
        uitleg="Dat is de productregel, die je in het boomdiagram ziet als takken die opnieuw splitsen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij trekken zonder terugleggen blijft het aantal keuzes elke stap gelijk.",
        antwoord=False,
        uitleg="Wat je getrokken hebt, ligt eruit, dus er blijft telkens één keuze minder over.",
    ),
    dict(
        type="waarofniet",
        vraag="Een boomdiagram toont elke mogelijke uitkomst precies één keer.",
        antwoord=True,
        uitleg="Daarom kan je de paden gewoon optellen zonder voor dubbels op te letten.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor elk telprobleem is een boomdiagram de beste aanpak.",
        antwoord=False,
        uitleg="Bij veel stappen wordt de tekening onhandelbaar en gebruik je enkel de regels.",
    ),
    dict(
        type="invultekst",
        vraag="Je kiest een trui uit 5 en een broek uit 3. Hoeveel combinaties zijn er?",
        antwoord=["15"],
        uitleg="De productregel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel uitkomsten zijn er als je drie keer met een munt gooit?",
        antwoord=["8"],
        uitleg="2 maal 2 maal 2.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de regel waarbij je de aantallen keuzes vermenigvuldigt?",
        antwoord=["productregel", "de productregel"],
        uitleg="De somregel telt juist op.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een venndiagram?",
        opties=[
            "om te tonen welke elementen twee groepen gemeen hebben",
            "om opeenvolgende keuzes in stappen uit te schrijven",
            "om de spreiding van meetwaarden te tonen",
            "om een verband tussen twee variabelen te tekenen",
        ],
        antwoord=0,
        uitleg="De overlapping van de twee kringen is de doorsnede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de doorsnede van twee groepen?",
        opties=[
            "de elementen die in allebei de groepen zitten",
            "de elementen die in minstens één groep zitten",
            "de elementen die in geen van de groepen zitten",
            "de elementen die maar in één groep zitten",
        ],
        antwoord=0,
        uitleg="In het venndiagram is dat het stuk waar de kringen elkaar overlappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat twee groepen disjunct zijn?",
        opties=[
            "ze hebben geen enkel element gemeen",
            "ze hebben precies één element gemeen",
            "ze zijn samen even groot als het geheel",
            "de ene zit volledig in de andere",
        ],
        antwoord=0,
        uitleg="De kringen raken elkaar dan niet, en je mag gewoon optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de somregel bij twee groepen die elkaar overlappen?",
        opties=[
            "tel de twee groepen op en trek de doorsnede er één keer af",
            "tel de twee groepen gewoon bij elkaar op",
            "tel de twee groepen op en tel de doorsnede erbij",
            "vermenigvuldig de twee groepen met elkaar",
        ],
        antwoord=0,
        uitleg="Wie in allebei zit, heb je anders twee keer geteld.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klas van 25 doen er 14 aan voetbal en 11 aan zwemmen; 5 doen allebei. Hoeveel doen er minstens één van de twee?",
        opties=["20", "25", "30", "15"],
        antwoord=0,
        uitleg="14 plus 11 is 25, min de 5 die dubbel geteld zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="In diezelfde klas van 25 doen er 20 minstens één sport. Hoeveel doen er geen van beide?",
        opties=["5", "0", "10", "4"],
        antwoord=0,
        uitleg="Dat is de complementregel: het geheel min de groep die wel meedoet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de complementregel?",
        opties=[
            "het aantal dat niet aan de voorwaarde voldoet is het geheel min het aantal dat er wel aan voldoet",
            "het aantal dat aan twee voorwaarden voldoet is het product van de twee aantallen",
            "het aantal in de doorsnede is de som van de twee groepen",
            "het geheel is altijd gelijk aan de som van de twee groepen",
        ],
        antwoord=0,
        uitleg="In het venndiagram is dat het stuk buiten de kringen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is het aantal in de vereniging gewoon de som van de twee groepen?",
        opties=[
            "als de groepen disjunct zijn en dus niets gemeen hebben",
            "als de ene groep volledig in de andere zit",
            "als de twee groepen even groot zijn",
            "als de doorsnede precies de helft is",
        ],
        antwoord=0,
        uitleg="Zonder overlapping is er niets dubbel geteld en hoef je niets af te trekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van 40 leerlingen leren er 22 Frans en 18 Duits, en 6 leren allebei. Hoeveel leren er geen van de twee?",
        opties=["6", "0", "4", "12"],
        antwoord=0,
        uitleg="22 plus 18 min 6 is 34, en 40 min 34 is 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het handig om eerst de doorsnede in te vullen in een venndiagram?",
        opties=[
            "dan kan je de andere vakjes eruit afleiden zonder dubbel te tellen",
            "dan hoef je het totaal niet meer te kennen",
            "dan valt de complementregel weg",
            "dan zijn de twee groepen automatisch disjunct",
        ],
        antwoord=0,
        uitleg="De rest van elke kring is het aantal van die groep min de doorsnede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van 30 mensen eten er 18 vlees en 14 vis; 7 eten allebei. Hoeveel eten er enkel vis?",
        opties=["7", "14", "11", "9"],
        antwoord=0,
        uitleg="14 min de 7 in de doorsnede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel getallen van 1 tot en met 20 zijn deelbaar door 2 of door 3?",
        opties=["13", "16", "10", "17"],
        antwoord=0,
        uitleg="10 door 2, 6 door 3, en 3 door allebei: 10 plus 6 min 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het soms sneller te tellen wat er niet aan de voorwaarde voldoet?",
        opties=[
            "die groep is vaak veel kleiner, en het geheel min die groep geeft het antwoord",
            "die groep is altijd precies de helft van het geheel",
            "zo hoef je de productregel niet meer te gebruiken",
            "de doorsnede telt dan niet meer mee",
        ],
        antwoord=0,
        uitleg="Bij minstens één keer zes in vier worpen tel je makkelijker de worpen zonder zes.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij twee groepen die elkaar overlappen, mag je de aantallen gewoon optellen.",
        antwoord=False,
        uitleg="Dan tel je de doorsnede twee keer. Trek ze één keer af.",
    ),
    dict(
        type="waarofniet",
        vraag="In een venndiagram staat buiten de kringen wie aan geen van de voorwaarden voldoet.",
        antwoord=True,
        uitleg="Dat vakje vind je met de complementregel.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij disjuncte groepen is de doorsnede leeg.",
        antwoord=True,
        uitleg="Daarom valt de aftrekking in de somregel weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een venndiagram is de gewone keuze om opeenvolgende keuzes te tellen.",
        antwoord=False,
        uitleg="Daarvoor gebruik je een boomdiagram; een venndiagram toont overlappende groepen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je twee groepen die niets gemeen hebben?",
        antwoord=["disjunct", "disjuncte groepen"],
        uitleg="Hun doorsnede is leeg.",
    ),
    dict(
        type="invultekst",
        vraag="Van 30 leerlingen spelen er 12 piano en 9 gitaar, en 4 allebei. Hoeveel spelen er minstens één instrument?",
        antwoord=["17"],
        uitleg="12 plus 9 min 4.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het deel waar twee kringen van een venndiagram elkaar overlappen?",
        antwoord=["doorsnede", "de doorsnede"],
        uitleg="Alles samen heet de vereniging.",
    ),
]
