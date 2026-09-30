# -*- coding: utf-8 -*-
"""De vragen voor "Stelsels van twee eerstegraadsvergelijkingen".

Nieuw geschreven voor dubbele finaliteit. In de doorstroomversie zitten de
stelsels samen met de tweedegraadsvergelijkingen in één thema; de DF-fiche kent
geen tweedegraadsvergelijkingen en geeft de stelsels juist veel ruimte, met de
drie oplossingsmethodes en met het grafische verband erbij.

Deel 1 gaat over wat een stelsel is, wat een oplossing is en hoe je er een
oplost met substitutie en gelijkstelling. Deel 2 gaat over de
combinatiemethode, over de stelsels zonder of met oneindig veel oplossingen,
over het grafische beeld en over vraagstukken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een stelsel van twee eerstegraadsvergelijkingen met twee onbekenden?",
        opties=[
            "twee vergelijkingen die tegelijk moeten kloppen",
            "twee vergelijkingen die je na elkaar oplost",
            "een vergelijking met twee mogelijke antwoorden",
            "een vergelijking waarin een onbekende twee keer staat",
        ],
        antwoord=0,
        uitleg="Je zoekt de waarden van x en y waarvoor de eerste én de tweede vergelijking kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de oplossing van zo'n stelsel eruit?",
        opties=[
            "als een koppel getallen (x, y)",
            "als één getal",
            "als twee losse getallen zonder verband",
            "als een breuk",
        ],
        antwoord=0,
        uitleg="De oplossingenverzameling schrijf je als een koppel, bijvoorbeeld V is de verzameling met (2, 3) erin.",
    ),
    dict(
        type="waarofniet",
        vraag="Het koppel (2, 3) betekent dat x gelijk is aan 2 en y gelijk aan 3.",
        antwoord=True,
        uitleg="In een koppel staat de x altijd eerst en de y tweede. De volgorde is afgesproken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Klopt het koppel (4, 1) voor het stelsel x + y = 5 en x − y = 3?",
        opties=[
            "ja, want het klopt in allebei de vergelijkingen",
            "nee, want het klopt alleen in de eerste",
            "nee, want het klopt alleen in de tweede",
            "nee, want er zijn geen oplossingen",
        ],
        antwoord=0,
        uitleg="4 plus 1 is 5 en 4 min 1 is 3. Allebei kloppen, dus het koppel is de oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij de substitutiemethode?",
        opties=[
            "je schrijft één onbekende uit en vult die in de andere vergelijking in",
            "je telt de twee vergelijkingen bij elkaar op",
            "je tekent de twee rechten en leest het snijpunt af",
            "je stelt de twee rechterleden aan elkaar gelijk",
        ],
        antwoord=0,
        uitleg="Substitueren is invullen. Uit één vergelijking haal je bijvoorbeeld y, en die uitdrukking zet je in de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op met substitutie: y = 2x en x + y = 9. Wat is x?",
        opties=["3", "2", "9", "6"],
        antwoord=0,
        uitleg="Vul y is 2x in: x plus 2x is 3x, en 3x is 9, dus x is 3. Dan is y gelijk aan 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij de gelijkstellingsmethode?",
        opties=[
            "je schrijft in allebei de vergelijkingen dezelfde onbekende uit en stelt die gelijk",
            "je maakt de twee vergelijkingen even lang",
            "je vermenigvuldigt de twee vergelijkingen met elkaar",
            "je vervangt in beide vergelijkingen x door y",
        ],
        antwoord=0,
        uitleg="Staat er twee keer y is iets, dan moeten die twee uitdrukkingen aan elkaar gelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op met gelijkstelling: y = x + 1 en y = 3x − 5. Wat is x?",
        opties=["3", "2", "4", "1"],
        antwoord=0,
        uitleg="x plus 1 is 3x min 5, dus 6 is 2x en x is 3. Dan is y gelijk aan 4.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stelsel heeft altijd precies één oplossing.",
        antwoord=False,
        uitleg="Er zijn ook stelsels zonder oplossing en stelsels met oneindig veel oplossingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je je oplossing achteraf in allebei de vergelijkingen?",
        opties=[
            "omdat een koppel pas klopt als het in de twee vergelijkingen past",
            "omdat de eerste vergelijking altijd de belangrijkste is",
            "omdat je anders de koppelvoorstelling niet mag opschrijven",
            "omdat het rekentoestel het anders niet aanvaardt",
        ],
        antwoord=0,
        uitleg="Een rekenfout onderweg merk je pas als je invult. Invullen kost weinig tijd en vangt veel fouten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je de vergelijking 2x + y = 7 om zodat y alleen staat?",
        opties=["y = 7 − 2x", "y = 2x − 7", "y = 7 + 2x", "y = 2x + 7"],
        antwoord=0,
        uitleg="Breng 2x naar de andere kant. Wat je aftrekt aan de ene kant, trek je ook af aan de andere.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de methode waarbij je een onbekende uitschrijft en invult in de andere vergelijking?",
        antwoord=["substitutie", "de substitutiemethode", "substitutiemethode"],
        uitleg="Substitueren betekent letterlijk vervangen: je vervangt y door de uitdrukking die eraan gelijk is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een stelsel mag je een vergelijking langs beide kanten met hetzelfde getal vermenigvuldigen.",
        antwoord=True,
        uitleg="Zolang je links en rechts hetzelfde doet, blijft de vergelijking gelijkwaardig. Dat is de basis van de combinatiemethode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kaarten en drie broodjes kosten 13 euro. Welke vergelijking hoort daarbij, met k de prijs van een kaart en b die van een broodje?",
        opties=["2k + 3b = 13", "k + b = 13", "2k = 3b", "6kb = 13"],
        antwoord=0,
        uitleg="Het aantal stuks komt vóór de onbekende, en samen is dat het totaalbedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: x = 5 en 2x + y = 13. Wat is y?",
        opties=["3", "8", "13", "5"],
        antwoord=0,
        uitleg="2 maal 5 is 10, en 10 plus y is 13, dus y is 3.",
    ),
    dict(
        type="waarofniet",
        vraag="Het koppel (1, 2) en het koppel (2, 1) zijn dezelfde oplossing.",
        antwoord=False,
        uitleg="De volgorde in een koppel ligt vast: eerst x, dan y. Wissel je ze om, dan bedoel je iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan je één vergelijking met twee onbekenden niet oplossen?",
        opties=[
            "omdat er oneindig veel koppels aan voldoen",
            "omdat je niet met twee letters tegelijk mag rekenen",
            "omdat een vergelijking maar één letter mag bevatten",
            "omdat het antwoord dan altijd nul is",
        ],
        antwoord=0,
        uitleg="Bij x plus y is 5 hoort elk koppel dat samen 5 geeft. Pas een tweede voorwaarde kiest er één uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het getal dat vóór een onbekende staat, zoals de 3 in 3x?",
        antwoord=["de coëfficiënt", "coëfficiënt", "coefficient"],
        uitleg="De coëfficiënt zegt met hoeveel de onbekende vermenigvuldigd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vorm is de algemene vorm van een eerstegraadsvergelijking met twee onbekenden?",
        opties=["ax + by = c", "ax² + bx = c", "ax + b = 0", "x = ay + b²"],
        antwoord=0,
        uitleg="De onbekenden staan in de eerste graad, elk met hun eigen coëfficiënt, en rechts staat een getal.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag zelf kiezen welke onbekende je eerst uitschrijft bij substitutie.",
        antwoord=True,
        uitleg="Kies de onbekende die het makkelijkst alleen komt te staan, meestal een met coëfficiënt 1.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij de combinatiemethode?",
        opties=[
            "je telt de twee vergelijkingen op of trekt ze af zodat een onbekende wegvalt",
            "je vermenigvuldigt de twee vergelijkingen met elkaar",
            "je vult de ene vergelijking in de andere in",
            "je tekent de twee rechten in hetzelfde assenstelsel",
        ],
        antwoord=0,
        uitleg="Zorg eerst dat een onbekende in beide vergelijkingen dezelfde coëfficiënt heeft, met een tegengesteld teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op met combinatie: x + y = 10 en x − y = 4. Wat is x?",
        opties=["7", "3", "6", "14"],
        antwoord=0,
        uitleg="Tel de twee op: de y valt weg en 2x is 14, dus x is 7. Dan is y gelijk aan 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: 2x + y = 8 en 2x − y = 4. Wat is y?",
        opties=["2", "3", "6", "12"],
        antwoord=0,
        uitleg="Trek de tweede van de eerste af: 2y is 4, dus y is 2. Dan is x gelijk aan 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een strijdig stelsel?",
        opties=[
            "een stelsel zonder enkele oplossing",
            "een stelsel met twee oplossingen",
            "een stelsel met oneindig veel oplossingen",
            "een stelsel waarin de onbekenden van plaats wisselen",
        ],
        antwoord=0,
        uitleg="De twee vergelijkingen spreken elkaar tegen. De oplossingenverzameling is dan de lege verzameling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het stelsel x + y = 5 en x + y = 8 strijdig?",
        opties=[
            "omdat dezelfde som niet tegelijk 5 en 8 kan zijn",
            "omdat er geen coëfficiënten bij x staan",
            "omdat 5 en 8 geen veelvouden van elkaar zijn",
            "omdat er te weinig onbekenden zijn",
        ],
        antwoord=0,
        uitleg="Werk je het uit met combinatie, dan krijg je 0 is 3. Dat klopt nooit, dus er is geen oplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een strijdig stelsel schrijf je als oplossingenverzameling de lege verzameling.",
        antwoord=True,
        uitleg="Er is geen enkel koppel dat aan allebei de vergelijkingen voldoet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel oplossingen heeft het stelsel x + y = 5 en 2x + 2y = 10?",
        opties=[
            "oneindig veel",
            "geen enkele",
            "precies één",
            "precies twee",
        ],
        antwoord=0,
        uitleg="De tweede vergelijking is de eerste maal twee. Ze zeggen hetzelfde, dus elk koppel dat aan de eerste voldoet, voldoet ook aan de tweede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je tekent de twee vergelijkingen als rechten. Wat betekent één snijpunt?",
        opties=[
            "het stelsel heeft precies één oplossing",
            "het stelsel is strijdig",
            "het stelsel heeft oneindig veel oplossingen",
            "de rechten vallen samen",
        ],
        antwoord=0,
        uitleg="De coördinaten van het snijpunt zijn precies het koppel dat aan allebei de vergelijkingen voldoet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je op de grafiek bij een strijdig stelsel?",
        opties=[
            "twee evenwijdige rechten",
            "twee snijdende rechten",
            "twee samenvallende rechten",
            "één rechte door de oorsprong",
        ],
        antwoord=0,
        uitleg="Evenwijdige rechten hebben dezelfde richtingscoëfficiënt en snijden elkaar nooit, dus er is geen gemeenschappelijk punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je op de grafiek bij een stelsel met oneindig veel oplossingen?",
        opties=[
            "twee samenvallende rechten",
            "twee evenwijdige rechten",
            "twee rechten die elkaar in twee punten snijden",
            "twee loodrechte rechten",
        ],
        antwoord=0,
        uitleg="Ze liggen precies op elkaar, dus elk punt van de rechte is een gemeenschappelijk punt.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee rechten met dezelfde richtingscoëfficiënt maar een ander snijpunt met de y-as snijden elkaar ergens.",
        antwoord=False,
        uitleg="Ze zijn evenwijdig en blijven even ver van elkaar. Het stelsel is dan strijdig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stelsel zonder oplossing?",
        antwoord=["strijdig", "een strijdig stelsel", "strijdig stelsel"],
        uitleg="Strijdig betekent dat de twee vergelijkingen elkaar tegenspreken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee broodjes en een soep kosten 9 euro; een broodje en een soep kosten 6 euro. Hoeveel kost een broodje?",
        opties=["3 euro", "4 euro", "2 euro", "6 euro"],
        antwoord=0,
        uitleg="Trek de tweede van de eerste af: er blijft één broodje over, en 9 min 6 is 3. Een soep kost dan 3 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klas van 25 leerlingen telt 7 jongens meer dan meisjes. Hoeveel meisjes zijn er?",
        opties=["9", "16", "11", "18"],
        antwoord=0,
        uitleg="Met j plus m is 25 en j min m is 7 krijg je 2j is 32, dus 16 jongens en 9 meisjes.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vraagstuk schrijf je eerst op wat x en wat y voorstelt.",
        antwoord=True,
        uitleg="Zonder die afspraak weet je achteraf niet wat je uitkomst betekent, en kan een lezer je oplossing niet volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je werkt een stelsel uit met combinatie en komt uit op 0 = 0. Wat betekent dat?",
        opties=[
            "het stelsel heeft oneindig veel oplossingen",
            "het stelsel is strijdig",
            "x en y zijn allebei nul",
            "je hebt een rekenfout gemaakt",
        ],
        antwoord=0,
        uitleg="Alles is weggevallen en er blijft een ware uitspraak over. De twee vergelijkingen zeggen dus hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je werkt een stelsel uit en komt uit op 0 = 7. Wat betekent dat?",
        opties=[
            "het stelsel heeft geen oplossing",
            "het stelsel heeft oneindig veel oplossingen",
            "x is gelijk aan 7",
            "y is gelijk aan 7",
        ],
        antwoord=0,
        uitleg="Er blijft een uitspraak over die nooit waar is, dus er bestaat geen koppel dat past. Het stelsel is strijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kies je best de combinatiemethode in plaats van substitutie?",
        opties=[
            "als een onbekende in beide vergelijkingen dezelfde coëfficiënt heeft",
            "als er in één vergelijking een onbekende alleen staat",
            "als de getallen breuken zijn",
            "als er maar één onbekende in het stelsel staat",
        ],
        antwoord=0,
        uitleg="Dan valt die onbekende in één stap weg. Staat er ergens al y is iets, dan is substitutie sneller.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waar de twee rechten van een stelsel elkaar kruisen?",
        antwoord=["het snijpunt", "snijpunt"],
        uitleg="De coördinaten van het snijpunt vormen de oplossing van het stelsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stelsel grafisch oplossen geeft altijd een exact antwoord.",
        antwoord=False,
        uitleg="Tekenen geeft een goede schatting van het snijpunt, maar voor een exact koppel reken je het na.",
    ),
]
