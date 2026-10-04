# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Gassen, temperatuur en de gaswetten.

Hoort bij "druk - gaswetten" van de vakfiche fysica 2de graad
doorstroomfinaliteit, het tweede van twee thema's voor dat onderdeel van 15 %.

Deel 1 gaat over het deeltjesmodel: hoe een gas druk uitoefent, wat het
absolute nulpunt betekent voor de druk, het volume en de kinetische energie
van de deeltjes, en het omrekenen tussen graden Celsius en kelvin. Deel 2 gaat
over de gaswetten: de afzonderlijke wetten bij constante temperatuur, druk of
volume, de algemene gaswet p.V/T = constant, de ideale gaswet p.V = n.R.T en
het lezen en omzetten van p(V)-, p(T)- en V(T)-grafieken.

De gasconstante R = 8,31 J/(mol.K), de normdruk 1013 hPa en de
normtemperatuur 273,15 K staan bij de constanten van het examen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat de druk van een gas op de wand van zijn vat? Kruis alles aan wat juist is.",
        opties=[
            "de deeltjes botsen tegen de wand",
            "het gewicht van het gas drukt op de wand",
            "hoe sneller de deeltjes gaan, hoe groter de druk",
            "de wand duwt het gas zelf samen",
        ],
        antwoord=[0, 2],
        uitleg="Elk deeltje dat tegen de wand botst, duwt er even tegen, en samen geeft dat een constante druk. Snellere deeltjes botsen harder en vaker, dus stijgt de druk met de temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je warmt een gas op in een gesloten vat van vast volume. Wat gebeurt er met de druk?",
        opties=["ze wordt groter", "ze wordt kleiner", "ze blijft gelijk", "ze wordt nul"],
        antwoord=0,
        uitleg="Warmer betekent sneller bewegende deeltjes, dus meer en hardere botsingen op de wand. De druk stijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kelvin is 25 °C?",
        opties=["298 K", "248 K", "25 K", "273 K"],
        antwoord=0,
        uitleg="Tel 273,15 op bij de graden Celsius: 25 + 273,15 = 298,15 K, dus ongeveer 298 K.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel graden Celsius is 200 K?",
        opties=["−73 °C", "73 °C", "473 °C", "−473 °C"],
        antwoord=0,
        uitleg="Trek 273,15 af: 200 − 273,15 = −73,15 °C.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het absolute nulpunt voor een ideaal gas? Kruis alles aan wat juist is.",
        opties=[
            "de kinetische energie van de deeltjes is nul",
            "de druk van het gas is nul",
            "de massa van de deeltjes is nul",
            "het gas weegt niets meer",
        ],
        antwoord=[0, 1],
        uitleg="Bij 0 K staan de deeltjes stil in het model, dus botsen ze niet meer: geen kinetische energie en geen druk. Ook het volume van een ideaal gas zou nul zijn. Hun massa blijft wel bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel graden Celsius is het absolute nulpunt?",
        opties=["−273,15 °C", "0 °C", "273,15 °C", "−100 °C"],
        antwoord=0,
        uitleg="0 K is −273,15 °C. Lager dan dat kan niet, want de deeltjes kunnen niet langzamer dan stil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom neemt de luchtdruk af als je hoger komt in de atmosfeer?",
        opties=[
            "er zit minder lucht boven je",
            "de lucht is er kouder",
            "de zwaartekracht is er nul",
            "er zitten minder soorten gas in de lucht",
        ],
        antwoord=0,
        uitleg="De luchtdruk komt van het gewicht van alle lucht erboven. Hoger zit er minder lucht boven je, dus is de druk kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een ideaal gas zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de deeltjes hebben zelf geen volume in het model",
            "de deeltjes trekken elkaar niet aan in het model",
            "een ideaal gas bestaat in het echt niet",
            "een ideaal gas kan niet van druk veranderen",
        ],
        antwoord=[0, 1],
        uitleg="Het model vergeet het eigen volume en de aantrekking tussen de deeltjes. Echte gassen volgen het goed bij lage druk en hoge temperatuur, maar geen enkel gas is precies ideaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de vier toestandsgrootheden van een gas?",
        opties=[
            "druk, volume, temperatuur en stofhoeveelheid",
            "druk, massa, temperatuur en kracht",
            "druk, volume, massa en energie",
            "kracht, oppervlakte, volume en warmte",
        ],
        antwoord=0,
        uitleg="p, V, T en n. Samen staan ze in de ideale gaswet p.V = n.R.T.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat lucht uit een fietsband ontsnappen. Wat gebeurt er in het vat?",
        opties=[
            "er blijven minder deeltjes over, dus daalt de druk",
            "de deeltjes gaan sneller bewegen",
            "de temperatuur van de band stijgt",
            "het volume van de band wordt groter",
        ],
        antwoord=0,
        uitleg="Minder deeltjes in hetzelfde volume geeft minder botsingen per seconde op de wand. De stofhoeveelheid n daalt, en daarmee de druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas staat op een overdruk van 1,5 bar. Hoe groot is de totale druk ongeveer?",
        opties=["2,5 bar", "1,5 bar", "0,5 bar", "3,0 bar"],
        antwoord=0,
        uitleg="Overdruk is wat er boven de luchtdruk van ongeveer 1 bar zit, dus 1,5 + 1,0 = 2,5 bar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een temperatuursverschil van 20 °C is hetzelfde als een temperatuursverschil van 20 K.",
        antwoord=True,
        uitleg="De stappen van de twee schalen zijn even groot, enkel hun nulpunt ligt anders. Bij een verschil valt dat weg.",
    ),
    dict(
        type="waarofniet",
        vraag="In de gaswetten mag je de temperatuur in graden Celsius invullen.",
        antwoord=False,
        uitleg="De temperatuur moet in kelvin, want de wetten gaan uit van het absolute nulpunt. Met graden Celsius kom je zelfs op een deling door nul bij 0 °C.",
    ),
    dict(
        type="waarofniet",
        vraag="De deeltjes van een gas bewegen bij een hogere temperatuur gemiddeld sneller.",
        antwoord=True,
        uitleg="De absolute temperatuur is een maat voor de gemiddelde kinetische energie van de deeltjes. Warmer betekent dus sneller.",
    ),
    dict(
        type="waarofniet",
        vraag="De druk van een gas hangt niet af van het aantal deeltjes in het vat.",
        antwoord=False,
        uitleg="In p.V = n.R.T staat n. Meer deeltjes in hetzelfde volume bij dezelfde temperatuur geeft een grotere druk, zoals bij het oppompen van een band.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gas neemt altijd het hele volume van zijn vat in.",
        antwoord=True,
        uitleg="De deeltjes bewegen vrij door elkaar en vullen de hele ruimte. Daarom kan je van een gas niet apart een volume meten zoals bij een vloeistof.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de SI-eenheid van absolute temperatuur? Schrijf de naam van de eenheid.",
        antwoord=["kelvin", "de kelvin", "K"],
        uitleg="De kelvin, met symbool K zonder gradenteken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel kelvin is 0 °C? Schrijf het getal.",
        antwoord=["273,15", "273", "273.15"],
        uitleg="273,15 K. Dat getal heet ook de normtemperatuur.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een druk die groter is dan de luchtdruk? Schrijf het woord.",
        antwoord=["overdruk", "de overdruk"],
        uitleg="Overdruk. Een manometer op een fietspomp geeft meestal de overdruk aan.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor de stofhoeveelheid van een gas?",
        antwoord=["n"],
        uitleg="n, met als eenheid de mol. Die staat in de ideale gaswet p.V = n.R.T.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat blijft gelijk bij een isotherm proces van een vaste hoeveelheid gas?",
        opties=["de temperatuur", "de druk", "het volume", "de energie"],
        antwoord=0,
        uitleg="Iso betekent gelijk en therm hoort bij warmte, dus de temperatuur blijft gelijk. Dan geldt p . V = constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat blijft gelijk bij een isobaar proces?",
        opties=["de druk", "het volume", "de temperatuur", "de massa van het vat"],
        antwoord=0,
        uitleg="Baar hoort bij druk, dus de druk blijft gelijk. Dan geldt V / T = constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat blijft gelijk bij een isochoor proces?",
        opties=["het volume", "de druk", "de temperatuur", "de stofhoeveelheid en de druk"],
        antwoord=0,
        uitleg="Choor hoort bij ruimte, dus het volume blijft gelijk. Dan geldt p / T = constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas van 3,0 L bij 2,0 bar wordt bij gelijke temperatuur samengedrukt tot 1,0 L. Wat is de nieuwe druk?",
        opties=["6,0 bar", "0,67 bar", "1,5 bar", "3,0 bar"],
        antwoord=0,
        uitleg="Bij constante temperatuur is p.V constant: 2,0 . 3,0 = p . 1,0, dus p = 6,0 bar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas van 2,0 L bij 300 K wordt bij gelijke druk opgewarmd tot 450 K. Wat is het nieuwe volume?",
        opties=["3,0 L", "1,3 L", "4,5 L", "2,7 L"],
        antwoord=0,
        uitleg="Bij constante druk is V/T constant: 2,0 / 300 = V / 450, dus V = 3,0 L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gesloten vat staat op 1,0 bar bij 290 K en wordt opgewarmd tot 580 K. Wat is de nieuwe druk?",
        opties=["2,0 bar", "0,50 bar", "1,5 bar", "4,0 bar"],
        antwoord=0,
        uitleg="Bij vast volume is p/T constant: de temperatuur in kelvin verdubbelt, dus de druk ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule is de ideale gaswet?",
        opties=["p . V = n . R . T", "p . V = constant", "p / T = constant", "p = ρ . g . h"],
        antwoord=0,
        uitleg="p.V = n.R.T, met R = 8,31 J/(mol.K). De andere vormen gelden enkel voor een vaste hoeveelheid gas met één grootheid constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een p(V)-grafiek bij constante temperatuur geeft:",
        opties=[
            "een kromme die daalt zonder de assen te raken",
            "een rechte door de oorsprong",
            "een horizontale rechte",
            "een stijgende rechte",
        ],
        antwoord=0,
        uitleg="p en V zijn omgekeerd evenredig, dus hun product blijft gelijk. Dat geeft een kromme die steeds vlakker daalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een V(T)-grafiek bij constante druk, met T in kelvin, geeft:",
        opties=[
            "een rechte door de oorsprong",
            "een kromme die daalt",
            "een horizontale rechte",
            "een kromme die stijgt",
        ],
        antwoord=0,
        uitleg="V/T blijft constant, dus V is recht evenredig met T. In kelvin gaat die rechte door de oorsprong, want bij 0 K zou het volume nul zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de algemene gaswet p.V/T = constant zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze geldt voor een vaste hoeveelheid gas",
            "de temperatuur moet in kelvin staan",
            "ze geldt enkel bij constante druk",
            "ze geldt enkel bij constante temperatuur",
        ],
        antwoord=[0, 1],
        uitleg="Zolang er geen gas bij komt of weggaat, mogen p, V en T alle drie veranderen. De afzonderlijke gaswetten zijn gevallen waarin één ervan gelijk blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas zit op 2,0 bar in 5,0 L bij 300 K en gaat naar 4,0 bar in 2,5 L. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het product p.V blijft gelijk",
            "de temperatuur is nog altijd 300 K",
            "de temperatuur is verdubbeld",
            "het gas heeft deeltjes verloren",
        ],
        antwoord=[0, 1],
        uitleg="2,0 . 5,0 = 10 en 4,0 . 2,5 = 10, dus p.V blijft gelijk. Volgens p.V/T = constant blijft T dan ook gelijk: het is een isotherm proces.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een isotherm proces zijn de druk en het volume omgekeerd evenredig.",
        antwoord=True,
        uitleg="p.V blijft gelijk, dus halveer je het volume, dan verdubbelt de druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een p(T)-grafiek bij vast volume, met T in kelvin, is een rechte door de oorsprong.",
        antwoord=True,
        uitleg="p/T blijft constant, dus p is recht evenredig met T. Bij 0 K zou de druk nul zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spuitbus mag in de zon liggen, want de druk in een gesloten vat verandert niet met de temperatuur.",
        antwoord=False,
        uitleg="Bij vast volume is p/T constant, dus de druk stijgt mee met de temperatuur. Daarom staat er op een spuitbus dat ze niet boven 50 °C mag komen.",
    ),
    dict(
        type="waarofniet",
        vraag="De gasconstante R is voor elk gas een andere waarde.",
        antwoord=False,
        uitleg="De universele gasconstante R = 8,31 J/(mol.K) geldt voor elk gas. Een specifieke gasconstante per kilogram verschilt wel van gas tot gas.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een p(V)-grafiek omzetten naar een p(T)-grafiek als je weet welke grootheid constant gehouden werd.",
        antwoord=True,
        uitleg="Met p.V/T = constant reken je elk punt om. Je moet wel weten of de temperatuur, de druk of het volume vastgehouden werd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een proces van een gas waarbij de temperatuur gelijk blijft?",
        antwoord=["isotherm", "een isotherm proces", "isothermisch"],
        uitleg="Een isotherm proces. Dan geldt p . V = constant.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de gasconstante R? Schrijf het getal in J/(mol.K).",
        antwoord=["8,31", "8.31", "8,31 J/mol.K"],
        uitleg="8,31 J/(mol.K). Die waarde staat bij de constanten van het examen.",
    ),
    dict(
        type="invultekst",
        vraag="Een gas van 4,0 L bij 1,0 bar wordt bij gelijke temperatuur samengedrukt tot 2,0 bar. Hoeveel liter blijft er over? Schrijf het getal.",
        antwoord=["2", "2,0", "2 L"],
        uitleg="p.V blijft gelijk: 1,0 . 4,0 = 2,0 . V, dus V = 2,0 L.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een proces waarbij het volume van het gas gelijk blijft?",
        antwoord=["isochoor", "een isochoor proces", "isochoorisch"],
        uitleg="Een isochoor proces. Dan geldt p / T = constant.",
    ),
]
