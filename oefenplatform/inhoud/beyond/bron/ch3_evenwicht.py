# -*- coding: utf-8 -*-
"""Chemisch evenwicht en de wet van Le Chatelier — 🌍 Beyond, chemie.

Deel 1 gaat over wat een chemisch evenwicht is: een dynamisch evenwicht waarbij
de heen- en de terugreactie even snel verlopen, het verschil met een aflopende
reactie en met geen reactie, en de evenwichtsconstante met het reactiequotiënt.
Deel 2 gaat over het verstoren van een evenwicht: de wet van Le Chatelier-Van
't Hoff bij een verandering van concentratie, volume of druk, temperatuur en
katalysator, en over het rendement en de omzettingsgraad.

De vragen beschrijven de grafiek of de proef in woorden, want een grafiek staat
in een vraag op het scherm niet. De coëfficiënten van een evenwichtsreactie
staan telkens in de vraag zelf.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een chemisch evenwicht dynamisch is?",
        opties=[
            "de heen- en de terugreactie blijven doorgaan, even snel",
            "de twee reacties zijn beide volledig gestopt",
            "de concentraties blijven voortdurend veranderen",
            "de reactie verloopt alleen van links naar rechts",
        ],
        antwoord=0,
        uitleg="Van buitenaf lijkt er niets te gebeuren, want de concentraties blijven "
        "gelijk. Binnenin reageren de deeltjes gewoon door, in beide richtingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een chemisch evenwicht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de concentraties blijven constant",
            "er zijn nog van alle stoffen aanwezig",
            "de reagentia zijn volledig opgebruikt",
            "de snelheid van beide reacties is nul",
        ],
        antwoord=[0, 1],
        uitleg="Bij een aflopende reactie is minstens één beginstof op. Bij een evenwicht "
        "blijft er van alles iets over.",
    ),
    dict(
        type="invultekst",
        vraag="Welk teken gebruik je in een vergelijking voor een evenwichtsreactie?",
        antwoord=["⇌", "dubbele pijl", "een dubbele pijl"],
        uitleg="Twee pijlen in tegengestelde richting. Een enkele pijl staat voor een "
        "aflopende reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je in het labo zien dat een reactie een evenwicht is en niet aflopend?",
        opties=[
            "er blijft van elke beginstof iets over, hoelang je ook wacht",
            "de reactie gaat sneller als je het mengsel verwarmt",
            "er komt een gas vrij tijdens het verloop van de reactie",
            "de kleur van het mengsel verandert tijdens de reactie",
        ],
        antwoord=0,
        uitleg="Je kan ook een product toevoegen: gaat het mengsel dan de andere kant op, "
        "dan is de terugreactie mogelijk en is het een evenwicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een evenwicht zijn de concentraties van reagentia en producten altijd gelijk aan elkaar.",
        antwoord=False,
        uitleg="Ze zijn constant, niet gelijk. Vaak ligt het evenwicht sterk aan één "
        "kant, en dat zie je in de waarde van de evenwichtsconstante.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je de evenwichtsconstante voor het evenwicht A + 2 B ⇌ C?",
        opties=[
            "K is [C] gedeeld door [A] maal [B]²",
            "K is [A] maal [B]² gedeeld door [C]",
            "K is [C] gedeeld door [A] maal [B]",
            "K is [C]² gedeeld door [A] maal [B]",
        ],
        antwoord=0,
        uitleg="De producten komen in de teller, de reagentia in de noemer, elk tot de "
        "macht van hun coëfficiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je als de evenwichtsconstante van een reactie heel groot is?",
        opties=[
            "het evenwicht ligt sterk aan de kant van de producten",
            "het evenwicht ligt sterk aan de kant van de reagentia",
            "de reactie verloopt heel snel naar het evenwicht toe",
            "de reactie heeft een lage activeringsenergie nodig",
        ],
        antwoord=0,
        uitleg="Een grote teller betekent veel product in het evenwicht. Over de snelheid "
        "zegt K niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de evenwichtsconstante zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze verandert enkel met de temperatuur",
            "ze heeft de producten in de teller",
            "ze verandert als je een reagens toevoegt",
            "ze wordt groter als je een katalysator gebruikt",
        ],
        antwoord=[0, 1],
        uitleg="Voeg je stof toe, dan verschuift het evenwicht tot K weer uitkomt. De "
        "waarde zelf blijft dus gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de uitdrukking die je met K vergelijkt om te weten welke kant een mengsel op gaat?",
        antwoord=["reactiequotiënt", "het reactiequotiënt", "Q"],
        uitleg="Q heeft dezelfde vorm als K, maar met de concentraties van dat ogenblik. "
        "Is Q kleiner dan K, dan gaat de reactie naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het reactiequotiënt Q is kleiner dan de evenwichtsconstante K. Wat gebeurt er?",
        opties=[
            "de reactie verloopt verder naar rechts, naar meer product",
            "de reactie verloopt verder naar links, naar meer reagens",
            "het mengsel is al in evenwicht en verandert niet meer",
            "de evenwichtsconstante wordt groter tot ze gelijk zijn",
        ],
        antwoord=0,
        uitleg="Er is te weinig product ten opzichte van het evenwicht. De heenreactie "
        "haalt dus de achterstand in tot Q gelijk is aan K.",
    ),
    dict(
        type="waarofniet",
        vraag="In de uitdrukking van de evenwichtsconstante staan de coëfficiënten als exponent.",
        antwoord=True,
        uitleg="Bij N₂ + 3 H₂ ⇌ 2 NH₃ wordt dat [NH₃]² gedeeld door [N₂] maal [H₂]³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de omzettingsgraad van een reactie?",
        opties=[
            "het deel van een beginstof dat werkelijk gereageerd heeft",
            "het deel van de energie dat tijdens de reactie vrijkomt",
            "de verhouding tussen de twee snelheden in het evenwicht",
            "de tijd die nodig is om het evenwicht te bereiken",
        ],
        antwoord=0,
        uitleg="Heeft 0,2 mol van de 1 mol gereageerd, dan is de omzettingsgraad 20 "
        "procent. Bij een aflopende reactie zou dat 100 procent zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zegt een hoge evenwichtsconstante niets over de snelheid?",
        opties=[
            "K gaat over de verhouding in het evenwicht, niet over de weg ernaartoe",
            "K is enkel gemeten bij hoge temperatuur en dus niet bruikbaar",
            "K hangt af van de activeringsenergie van de heenreactie",
            "K wordt groter zodra de reactie sneller begint te lopen",
        ],
        antwoord=0,
        uitleg="Het evenwicht van water en waterstofgas met zuurstofgas ligt bijvoorbeeld "
        "ver naar rechts, en toch gebeurt er zonder vlam niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken gelden voor het ogenblik waarop een evenwicht bereikt wordt? Kruis alles aan wat juist is.",
        opties=[
            "de snelheid van de heenreactie is gelijk aan die van de terugreactie",
            "de concentraties veranderen vanaf dan niet meer",
            "de snelheid van beide reacties is vanaf dan nul",
            "alle reagentia zijn vanaf dan opgebruikt",
        ],
        antwoord=[0, 1],
        uitleg="In het begin is de heenreactie het snelst. Terwijl er product bijkomt, "
        "wordt de terugreactie sneller, tot de twee gelijk zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid verandert de waarde van de evenwichtsconstante?",
        antwoord=["temperatuur", "de temperatuur", "T"],
        uitleg="Alleen de temperatuur. Concentratie, druk en een katalysator verschuiven "
        "het evenwicht wel, maar laten K ongemoeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een evenwicht van een gekleurde stof met een kleurloze stof blijft de kleur gelijk. Wat betekent dat?",
        opties=[
            "de verhouding tussen de twee stoffen verandert niet meer",
            "de reactie is helemaal stilgevallen in de beker",
            "er is geen enkele reactie opgetreden in het mengsel",
            "de gekleurde stof is volledig opgebruikt tijdens de proef",
        ],
        antwoord=0,
        uitleg="De kleur is een maat voor de concentratie. Blijft die gelijk, dan is het "
        "evenwicht bereikt, al blijven de deeltjes reageren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mengsel waarin niets gebeurt, is altijd een chemisch evenwicht.",
        antwoord=False,
        uitleg="Het kan ook zijn dat er geen reactie mogelijk is, of dat de drempel te "
        "hoog is. Bij een evenwicht moet je de terugreactie kunnen aantonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een evenwicht heeft K gelijk aan 1. Wat weet je dan?",
        opties=[
            "teller en noemer zijn in het evenwicht ongeveer even groot",
            "het evenwicht ligt helemaal aan de kant van de producten",
            "het evenwicht ligt helemaal aan de kant van de reagentia",
            "er is in het mengsel geen enkele reactie opgetreden",
        ],
        antwoord=0,
        uitleg="Zo'n evenwicht ligt ongeveer in het midden. Een K van duizend ligt rechts "
        "en een K van een duizendste links.",
    ),
    dict(
        type="waarofniet",
        vraag="Een chemisch evenwicht kan je van twee kanten bereiken: vanuit de reagentia of vanuit de producten.",
        antwoord=True,
        uitleg="Je komt bij dezelfde verhouding uit, zolang de temperatuur gelijk is. Dat "
        "is een goede manier om een evenwicht aan te tonen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reactie die in een evenwicht van rechts naar links verloopt?",
        antwoord=["terugreactie", "de terugreactie", "terug"],
        uitleg="De heenreactie gaat van links naar rechts. In het evenwicht zijn hun "
        "snelheden gelijk.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Le Chatelier-Van 't Hoff?",
        opties=[
            "een verstoord evenwicht verschuift zo dat het de verstoring tegenwerkt",
            "een verstoord evenwicht komt altijd bij dezelfde verhouding uit",
            "een verstoord evenwicht valt uiteen in een aflopende reactie",
            "een verstoord evenwicht verschuift altijd naar de kant van de producten",
        ],
        antwoord=0,
        uitleg="Voeg je iets toe, dan wordt het deels weggewerkt. Neem je iets weg, dan "
        "wordt het deels bijgemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je voegt extra reagens toe aan een evenwicht. Welke kant gaat het op?",
        opties=[
            "naar rechts, naar meer producten",
            "naar links, naar meer reagentia",
            "het blijft precies waar het was",
            "het valt uiteen tot er niets overblijft",
        ],
        antwoord=0,
        uitleg="Het evenwicht werkt de verhoging tegen door een deel van dat reagens weg "
        "te werken. Zo komt K weer uit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kant gaat een evenwicht op als je een product wegneemt?",
        antwoord=["naar rechts", "rechts", "naar de producten"],
        uitleg="Het evenwicht maakt het weggenomen product deels bij. Daarom haalt men in "
        "de industrie het product voortdurend uit het mengsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je maakt het volume van een gasevenwicht kleiner. Welke kant gaat het op?",
        opties=[
            "naar de kant met het minste aantal mol gas",
            "naar de kant met het meeste aantal mol gas",
            "naar de kant met de grootste molaire massa",
            "het evenwicht blijft onveranderd staan",
        ],
        antwoord=0,
        uitleg="Minder volume betekent meer druk. Het evenwicht werkt dat tegen door het "
        "aantal gasdeeltjes te verkleinen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een katalysator verschuift het evenwicht naar de kant van de producten.",
        antwoord=False,
        uitleg="Hij versnelt de heen- en de terugreactie evenveel. Het evenwicht komt dus "
        "sneller, maar op dezelfde plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verstoringen doen een gasevenwicht verschuiven? Kruis alles aan wat juist is.",
        opties=[
            "het volume van het vat verkleinen",
            "de temperatuur verhogen",
            "een katalysator toevoegen",
            "het vat van vorm veranderen bij gelijk volume",
        ],
        antwoord=[0, 1],
        uitleg="Alleen iets dat de concentraties of de constante verandert, verschuift "
        "het evenwicht. Een katalysator doet dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verhoogt de temperatuur van een exo-energetisch evenwicht. Welke kant gaat het op?",
        opties=[
            "naar links, want de endo-energetische richting werkt de warmte weg",
            "naar rechts, want een hogere temperatuur versnelt de heenreactie",
            "naar rechts, want de evenwichtsconstante wordt altijd groter",
            "het evenwicht verschuift niet, enkel de snelheid verandert",
        ],
        antwoord=0,
        uitleg="Warmte toevoegen is als een stof toevoegen aan de kant waar ze vrijkomt. "
        "Het evenwicht werkt dat tegen en gaat de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een temperatuurverandering bij een evenwicht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de evenwichtsconstante krijgt een andere waarde",
            "het evenwicht verschuift naar één kant",
            "de evenwichtsconstante blijft dezelfde",
            "enkel de snelheid verandert, niet de ligging",
        ],
        antwoord=[0, 1],
        uitleg="De temperatuur is de enige verstoring die K zelf verandert. Daarom krijg "
        "je bij elke temperatuur een andere verhouding.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verstoring verandert de waarde van de evenwichtsconstante?",
        antwoord=["temperatuur", "de temperatuur", "warmte"],
        uitleg="Concentratie en druk verschuiven het evenwicht, maar K blijft gelijk. Bij "
        "een andere temperatuur hoort een andere K.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het evenwicht N₂ + 3 H₂ ⇌ 2 NH₃ verhoog je de druk. Wat gebeurt er met de hoeveelheid ammoniak?",
        opties=[
            "ze neemt toe, want rechts staan minder mol gas",
            "ze neemt af, want rechts staan meer mol gas",
            "ze blijft gelijk, want druk doet hier niets",
            "ze neemt eerst toe en daarna weer af",
        ],
        antwoord=0,
        uitleg="Links staan vier mol gas, rechts twee. Daarom werkt de industrie bij hoge "
        "druk om meer ammoniak te krijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een evenwicht tussen stoffen met links en rechts evenveel mol gas verschuift niet door een drukverandering.",
        antwoord=True,
        uitleg="De verstoring werkt dan aan beide kanten gelijk. Alleen een verschil in "
        "aantal gasdeeltjes maakt druk belangrijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het rendement van een reactie?",
        opties=[
            "de werkelijke opbrengst gedeeld door de theoretische opbrengst",
            "de theoretische opbrengst gedeeld door de werkelijke opbrengst",
            "de hoeveelheid energie die bij de reactie vrijkomt",
            "het aantal mol product gedeeld door het aantal mol reagens",
        ],
        antwoord=0,
        uitleg="Haal je 8 gram van de 10 gram die mogelijk was, dan is het rendement 80 "
        "procent. Bij een evenwicht blijft dat altijd onder de honderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom haalt men in de industrie het product voortdurend uit een evenwichtsmengsel?",
        opties=[
            "zo blijft het evenwicht naar rechts werken en reageert er meer weg",
            "zo wordt de evenwichtsconstante van de reactie groter",
            "zo verloopt de reactie bij een lagere temperatuur",
            "zo hoeft er geen katalysator meer gebruikt te worden",
        ],
        antwoord=0,
        uitleg="Door het product weg te nemen blijft Q kleiner dan K. De heenreactie "
        "blijft dus doorlopen in plaats van stil te vallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een verstoord evenwicht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de snelheden van heen- en terugreactie zijn even tijdelijk verschillend",
            "na een tijd zijn de twee snelheden weer gelijk",
            "de evenwichtsconstante verandert bij elke verstoring",
            "het evenwicht komt nooit meer terug na een verstoring",
        ],
        antwoord=[0, 1],
        uitleg="Dat is net wat verschuiven betekent: de ene reactie loopt even voor, tot "
        "de concentraties weer bij K uitkomen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het deel van een beginstof dat werkelijk gereageerd heeft?",
        antwoord=["omzettingsgraad", "de omzettingsgraad", "omzetting"],
        uitleg="Bij een evenwicht blijft die altijd onder de honderd procent, want er "
        "blijft van elke beginstof iets over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je voegt een katalysator toe aan een evenwicht dat nog niet bereikt is. Wat merk je?",
        opties=[
            "het evenwicht wordt sneller bereikt, op dezelfde plaats",
            "het evenwicht wordt bereikt met meer product dan ervoor",
            "het evenwicht wordt bereikt met minder product dan ervoor",
            "het evenwicht wordt nooit meer bereikt in het mengsel",
        ],
        antwoord=0,
        uitleg="Beide richtingen worden evenveel versneld. De eindverhouding hangt alleen "
        "van K af, en die is niet veranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gekleurd evenwicht wordt lichter als je het verwarmt. Wat weet je dan?",
        opties=[
            "de reactie naar de kleurloze kant is endo-energetisch",
            "de reactie naar de kleurloze kant is exo-energetisch",
            "de evenwichtsconstante is onafhankelijk van de temperatuur",
            "de gekleurde stof is volledig opgebruikt bij het verwarmen",
        ],
        antwoord=0,
        uitleg="Warmte toevoegen duwt het evenwicht naar de kant die energie opneemt. Dat "
        "is hier de kleurloze kant.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het toevoegen van een reagens verandert ook de evenwichtsconstante.",
        antwoord=False,
        uitleg="Het evenwicht verschuift juist om K weer te laten uitkomen. Alleen een "
        "andere temperatuur geeft een andere K.",
    ),
    dict(
        type="waarofniet",
        vraag="De ligging van een evenwicht kan je met druk, concentratie en temperatuur beïnvloeden.",
        antwoord=True,
        uitleg="Die drie werken alle drie, al werkt druk enkel bij een verschil in aantal "
        "mol gas. Een katalysator verschuift niets.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kant gaat een evenwicht op als je de druk van een gasmengsel verlaagt?",
        antwoord=["naar meer gas", "naar meer mol", "meer gasdeeltjes"],
        uitleg="Het evenwicht werkt de lagere druk tegen door meer gasdeeltjes te maken. "
        "Dat is de kant met het grootste aantal mol gas.",
    ),
]
