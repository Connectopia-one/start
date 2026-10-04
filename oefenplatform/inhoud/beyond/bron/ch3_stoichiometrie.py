# -*- coding: utf-8 -*-
"""Stoichiometrie, overmaat en de algemene gaswet — 🌍 Beyond, chemie.

Deel 1 gaat over het uitbalanceren van een reactievergelijking en over het
rekenen met de verhoudingen die eruit volgen: van mol naar mol, van mol naar
massa en terug. Deel 2 gaat over een reactie waarbij de ene stof eerst
opgebruikt is: het limiterend of beperkend reagens en de overmaat, en over
gassen met de algemene gaswet, de normomstandigheden en het molair volume.

De coëfficiënten staan telkens in de vraag, want op het examen krijgt het kind
een reactievergelijking die het eerst zelf moet uitbalanceren. De getallen zijn
zo gekozen dat ze zonder rekentoestel uitkomen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom moet een reactievergelijking uitgebalanceerd zijn?",
        opties=[
            "er mogen geen atomen bijkomen of verdwijnen tijdens een reactie",
            "de reactie verloopt anders te snel om te kunnen meten",
            "de molaire massa van de stoffen moet links en rechts gelijk zijn",
            "de energie van de reactie moet links en rechts gelijk zijn",
        ],
        antwoord=0,
        uitleg="Bij een chemische reactie worden bindingen verbroken en gemaakt, maar de "
        "atomen zelf blijven bestaan. Dat is de wet van het behoud van massa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de uitgebalanceerde vergelijking voor het verbranden van methaan?",
        opties=[
            "CH₄ + 2 O₂ → CO₂ + 2 H₂O",
            "CH₄ + O₂ → CO₂ + H₂O",
            "CH₄ + 3 O₂ → CO₂ + 2 H₂O",
            "2 CH₄ + O₂ → 2 CO₂ + H₂O",
        ],
        antwoord=0,
        uitleg="Links en rechts: één koolstof, vier waterstof en vier zuurstof. Begin bij "
        "koolstof en waterstof en zet de zuurstof het laatst goed.",
    ),
    dict(
        type="invultekst",
        vraag="Welke coëfficiënt hoort voor O₂ in de reactie C₃H₈ + … O₂ → 3 CO₂ + 4 H₂O?",
        antwoord=["5", "vijf"],
        uitleg="Rechts staan zes plus vier, dus tien zuurstofatomen. Tien gedeeld door "
        "twee geeft vijf moleculen O₂.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de reactie N₂ + 3 H₂ → 2 NH₃ reageert 1 mol stikstofgas. Hoeveel ammoniak ontstaat er?",
        opties=[
            "2 mol",
            "1 mol",
            "3 mol",
            "6 mol",
        ],
        antwoord=0,
        uitleg="De coëfficiënten geven de verhouding: 1 op 3 op 2. Per mol stikstofgas "
        "ontstaan er dus twee mol ammoniak.",
    ),
    dict(
        type="waarofniet",
        vraag="De coëfficiënten van een reactievergelijking geven de verhouding in mol.",
        antwoord=True,
        uitleg="Niet in gram: dat zou alleen kloppen als alle stoffen dezelfde molaire "
        "massa hadden. Reken dus eerst om naar mol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel mol zuurstofgas is er nodig om 4 mol waterstofgas te laten reageren in 2 H₂ + O₂ → 2 H₂O?",
        opties=[
            "2 mol",
            "4 mol",
            "1 mol",
            "8 mol",
        ],
        antwoord=0,
        uitleg="De verhouding is 2 op 1. Voor vier mol waterstofgas is dus twee mol "
        "zuurstofgas nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een stoichiometrische berekening met massa's?",
        opties=[
            "de gegeven massa omrekenen naar een stofhoeveelheid in mol",
            "de gegeven massa delen door de coëfficiënt van de vergelijking",
            "de molaire massa van alle stoffen bij elkaar optellen",
            "de massa van de reactieproducten eerst links invullen",
        ],
        antwoord=0,
        uitleg="De verhouding uit de vergelijking geldt in mol. Daarom reken je eerst om, "
        "dan met de verhouding, en pas daarna terug naar gram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de reactie 2 Mg + O₂ → 2 MgO zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "per 2 mol magnesium is er 1 mol zuurstofgas nodig",
            "er ontstaat evenveel mol magnesiumoxide als er magnesium reageert",
            "per mol magnesium is er een mol zuurstofgas nodig",
            "er ontstaat dubbel zoveel magnesiumoxide als er magnesium reageert",
        ],
        antwoord=[0, 1],
        uitleg="De verhouding is 2 op 1 op 2. Magnesium en magnesiumoxide staan dus in "
        "verhouding één op één.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol water ontstaat er uit 3 mol waterstofgas in 2 H₂ + O₂ → 2 H₂O?",
        antwoord=["3", "3 mol", "drie"],
        uitleg="Waterstofgas en water staan in verhouding 2 op 2, dus één op één. Uit "
        "drie mol waterstofgas komt drie mol water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel gram magnesiumoxide ontstaat er uit 2 mol magnesium, met M(MgO) 40 g/mol?",
        opties=[
            "80 gram",
            "40 gram",
            "20 gram",
            "120 gram",
        ],
        antwoord=0,
        uitleg="Twee mol magnesium geeft twee mol magnesiumoxide, en twee maal 40 is 80 "
        "gram.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag de formule van een stof aanpassen om een vergelijking uit te balanceren.",
        antwoord=False,
        uitleg="Nooit: de formule van een stof staat vast. Je zet alleen coëfficiënten "
        "voor de formules.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de uitgebalanceerde vergelijking voor de vorming van aluminiumoxide?",
        opties=[
            "4 Al + 3 O₂ → 2 Al₂O₃",
            "2 Al + 3 O₂ → Al₂O₃",
            "Al + O₂ → Al₂O₃",
            "2 Al + O₂ → 2 Al₂O₃",
        ],
        antwoord=0,
        uitleg="Rechts staan vier aluminium en zes zuurstof. Links moeten dat dus vier Al "
        "en drie O₂ zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij de ontleding CaCO₃ → CaO + CO₂ ontleedt 100 gram kalksteen, met M 100 g/mol. Hoeveel mol CO₂ ontstaat er?",
        opties=[
            "1 mol",
            "2 mol",
            "0,5 mol",
            "100 mol",
        ],
        antwoord=0,
        uitleg="Honderd gram is één mol, en de verhouding is één op één. Er komt dus één "
        "mol koolstofdioxide vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een berekening van massa naar massa? Kruis alles aan wat juist is.",
        opties=[
            "eerst omrekenen van gram naar mol",
            "daarna de verhouding uit de vergelijking gebruiken",
            "eerst de massa's links en rechts gelijkstellen",
            "daarna de coëfficiënten bij de massa's optellen",
        ],
        antwoord=[0, 1],
        uitleg="Gram, mol, verhouding, mol, gram: dat is de hele weg. De verhouding geldt "
        "nooit rechtstreeks tussen massa's.",
    ),
    dict(
        type="invultekst",
        vraag="Welke coëfficiënt hoort voor H₂O in de reactie CH₄ + 2 O₂ → CO₂ + … H₂O?",
        antwoord=["2", "twee"],
        uitleg="Methaan heeft vier waterstofatomen, en elke watermolecule gebruikt er "
        "twee. Dus twee moleculen water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom balanceer je de zuurstof bij een verbranding meestal het laatst?",
        opties=[
            "zuurstof komt in meerdere producten voor en past zich het makkelijkst aan",
            "zuurstof heeft de grootste molaire massa van alle stoffen",
            "zuurstof reageert altijd in een verhouding van één op één",
            "zuurstof staat altijd rechts in de reactievergelijking",
        ],
        antwoord=0,
        uitleg="Als koolstof en waterstof goed staan, ligt het aantal zuurstofatomen "
        "rechts vast. Dan volgt de coëfficiënt links er zo uit.",
    ),
    dict(
        type="waarofniet",
        vraag="In een uitgebalanceerde vergelijking staat links en rechts evenveel atomen van elk element.",
        antwoord=True,
        uitleg="Dat is net wat uitbalanceren betekent. Het aantal moleculen hoeft "
        "natuurlijk niet gelijk te zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel mol zuurstofgas is nodig om 1 mol propaan C₃H₈ volledig te verbranden?",
        opties=[
            "5 mol",
            "3 mol",
            "4 mol",
            "7 mol",
        ],
        antwoord=0,
        uitleg="Er ontstaan drie CO₂ en vier H₂O, samen tien zuurstofatomen. Dat zijn "
        "vijf moleculen O₂.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een aflopende reactie blijft er altijd van elke beginstof iets over.",
        antwoord=False,
        uitleg="Een aflopende reactie gaat door tot minstens één beginstof op is. Die "
        "stof heet het limiterend reagens.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol waterstofgas is nodig voor 2 mol ammoniak in N₂ + 3 H₂ → 2 NH₃?",
        antwoord=["3", "3 mol", "drie"],
        uitleg="De verhouding tussen waterstofgas en ammoniak is 3 op 2. Voor twee mol "
        "ammoniak is dus drie mol waterstofgas nodig.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het limiterend reagens?",
        opties=[
            "de stof die als eerste opgebruikt is en de reactie stopzet",
            "de stof waarvan het meeste overblijft na de reactie",
            "de stof met de grootste coëfficiënt in de vergelijking",
            "de stof met de kleinste molaire massa in de reactie",
        ],
        antwoord=0,
        uitleg="Het beperkend reagens bepaalt hoeveel product er maximaal kan ontstaan. "
        "Van de andere stof blijft er dan iets over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat 2 mol H₂ reageren met 2 mol O₂ volgens 2 H₂ + O₂ → 2 H₂O. Welke stof is in overmaat?",
        opties=[
            "het zuurstofgas",
            "het waterstofgas",
            "geen van de twee stoffen",
            "beide stoffen even veel",
        ],
        antwoord=0,
        uitleg="Voor twee mol waterstofgas is maar één mol zuurstofgas nodig. Er blijft "
        "dus één mol zuurstofgas over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mol water ontstaat er uit 2 mol H₂ en 2 mol O₂ volgens 2 H₂ + O₂ → 2 H₂O?",
        antwoord=["2", "2 mol", "twee"],
        uitleg="Het waterstofgas is beperkend: twee mol ervan geeft twee mol water. Het "
        "overschot aan zuurstofgas doet niet meer mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je het limiterend reagens bij een reactie?",
        opties=[
            "je deelt van elke stof het aantal mol door haar coëfficiënt",
            "je neemt de stof met de kleinste massa in gram",
            "je neemt de stof met de grootste molaire massa",
            "je telt het aantal atomen van elke stof bij elkaar op",
        ],
        antwoord=0,
        uitleg="De kleinste uitkomst hoort bij het beperkend reagens. Zo vergelijk je "
        "eerlijk, ook als de coëfficiënten verschillen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het limiterend reagens is altijd de stof waarvan je het minste mol hebt.",
        antwoord=False,
        uitleg="Niet altijd: de coëfficiënten tellen mee. Van een stof met coëfficiënt 3 "
        "heb je drie keer zoveel nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de algemene gaswet?",
        opties=[
            "p maal V is gelijk aan n maal R maal T",
            "p maal V is gelijk aan n gedeeld door R maal T",
            "p gedeeld door V is gelijk aan n maal R maal T",
            "p maal T is gelijk aan n maal R maal V",
        ],
        antwoord=0,
        uitleg="R is de algemene gasconstante en T staat in kelvin. Zo kan je uit druk, "
        "volume en temperatuur het aantal mol berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke eenheid moet de temperatuur in de algemene gaswet staan?",
        opties=[
            "in kelvin",
            "in graden Celsius",
            "in graden Fahrenheit",
            "in joule per mol",
        ],
        antwoord=0,
        uitleg="Nul kelvin is het absolute nulpunt. Reken dus eerst om: 25 °C is 298 K.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de normomstandigheden zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de temperatuur is 0 °C of 273 K",
            "één mol gas neemt er 22,4 liter in",
            "de temperatuur is 25 °C of 298 K",
            "één mol gas neemt er 24,0 liter in",
        ],
        antwoord=[0, 1],
        uitleg="Bij 25 °C hoort een molair volume van ongeveer 24,5 liter. Spreek dus "
        "altijd af welke omstandigheden je bedoelt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk volume neemt 2 mol gas in bij normomstandigheden?",
        antwoord=["44,8 L", "44,8", "44,8 liter"],
        uitleg="Twee keer 22,4 liter. Het molair volume geldt voor elk gas, wat zijn "
        "molaire massa ook is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij de ontleding van 1 mol kalksteen komt 1 mol CO₂ vrij. Welk volume is dat bij normomstandigheden?",
        opties=[
            "22,4 liter",
            "44,8 liter",
            "11,2 liter",
            "1,0 liter",
        ],
        antwoord=0,
        uitleg="Eén mol gas is 22,4 liter bij 0 °C en normale druk. In een warme oven is "
        "dat volume groter.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee verschillende gassen nemen bij dezelfde druk en temperatuur evenveel plaats in per mol.",
        antwoord=True,
        uitleg="Dat is de kern van de wet van Avogadro. De grootte van de moleculen "
        "speelt bij een gas bijna geen rol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het volume van een gas als je de temperatuur verdubbelt bij gelijke druk?",
        opties=[
            "het volume verdubbelt, als je de temperatuur in kelvin rekent",
            "het volume halveert, want de druk blijft gelijk",
            "het volume blijft gelijk, want het aantal mol verandert niet",
            "het volume wordt vier keer groter dan ervoor",
        ],
        antwoord=0,
        uitleg="In pV is nRT staan V en T aan weerszijden van het gelijkheidsteken. "
        "Verdubbelt T, dan moet V ook verdubbelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over overmaat zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "van de stof in overmaat blijft er na de reactie over",
            "de stof in overmaat bepaalt niet hoeveel product er ontstaat",
            "de stof in overmaat is als eerste opgebruikt",
            "de stof in overmaat bepaalt de hoeveelheid product",
        ],
        antwoord=[0, 1],
        uitleg="Het beperkend reagens bepaalt de opbrengst. Daarom werkt men soms met "
        "een overmaat, om zeker te zijn dat de andere stof volledig reageert.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel kelvin is 27 °C?",
        antwoord=["300", "300 K", "300 kelvin"],
        uitleg="Tel 273 bij de temperatuur in graden Celsius op. In de gaswet mag je "
        "nooit met graden Celsius rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt 1 mol N₂ en 6 mol H₂ voor N₂ + 3 H₂ → 2 NH₃. Welke stof is beperkend?",
        opties=[
            "het stikstofgas",
            "het waterstofgas",
            "geen van de twee stoffen",
            "beide stoffen samen",
        ],
        antwoord=0,
        uitleg="Deel door de coëfficiënt: 1 gedeeld door 1 is 1, en 6 gedeeld door 3 is "
        "2. De kleinste uitkomst hoort bij het stikstofgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt men in de industrie soms met een overmaat van de goedkoopste stof?",
        opties=[
            "zo reageert de dure stof zo volledig mogelijk weg",
            "zo verloopt de reactie bij een lagere temperatuur",
            "zo hoeft de vergelijking niet uitgebalanceerd te worden",
            "zo ontstaat er minder afval bij de hele productie",
        ],
        antwoord=0,
        uitleg="De dure stof is dan het beperkend reagens en blijft niet ongebruikt "
        "achter. Het overschot van de goedkope stof wordt vaak hergebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel mol gas zit er in 11,2 liter bij normomstandigheden?",
        opties=[
            "0,5 mol",
            "1,0 mol",
            "2,0 mol",
            "0,25 mol",
        ],
        antwoord=0,
        uitleg="11,2 gedeeld door 22,4 is 0,5 mol. Zo reken je van volume naar "
        "stofhoeveelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij hogere druk neemt een gas bij gelijke temperatuur meer plaats in.",
        antwoord=False,
        uitleg="Het omgekeerde: bij hogere druk wordt het volume kleiner. In pV is nRT "
        "staan p en V aan dezelfde kant.",
    ),
    dict(
        type="waarofniet",
        vraag="De algemene gaswet geldt ook voor een mengsel van gassen, met n het totale aantal mol.",
        antwoord=True,
        uitleg="Lucht is zo'n mengsel. Voor het volume maakt het niet uit welke gassen "
        "erin zitten, alleen hoeveel mol er samen in zitten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stof die als eerste opgebruikt is tijdens een reactie?",
        antwoord=["limiterend reagens", "beperkend reagens", "limiterend"],
        uitleg="Zij bepaalt de maximale opbrengst. De andere stof is dan in overmaat "
        "aanwezig.",
    ),
]
