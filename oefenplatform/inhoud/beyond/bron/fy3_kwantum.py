# -*- coding: utf-8 -*-
"""Kwantumfysica: het foto-elektrisch effect en dualiteit — 🌍 Beyond, fysica.

Deel 1 gaat over het foto-elektrisch effect: wat er gebeurt, waarom de
frequentie beslist en de intensiteit niet, de drempelfrequentie, de energie
van een foton met E = h · f, en de toepassingen van de fotocel tot de
zonnecel. Daaruit volgt dat licht een deeltjeskarakter heeft. Deel 2 gaat over
de andere kant: het experiment van Davisson en Germer dat een elektron een
golfkarakter geeft, de dualiteit van licht en materie, de golffunctie als
waarschijnlijkheidsgolf met de Kopenhaagse interpretatie, het orbitaal als
waarschijnlijkheidsgebied, de Schrödingervergelijking en het
onzekerheidsbeginsel van Heisenberg.

De rode draad is dat licht en materie elk twee gezichten hebben, en dat je
telkens moet kijken welk model het verschijnsel verklaart. Een vraag naar
"wat is licht nu echt" heeft dus geen enkel antwoord van de twee.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij het foto-elektrisch effect?",
        opties=[
            "licht slaat elektronen uit een metaaloppervlak los",
            "licht laat een metaaloppervlak zelf licht uitzenden",
            "licht verwarmt een metaaloppervlak tot het gloeit",
            "licht maakt van een metaaloppervlak een magneet",
        ],
        antwoord=0,
        uitleg="Het licht geeft zijn energie aan een elektron in één keer door. Het "
        "elektron komt dan los van het metaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt het af of er elektronen loskomen?",
        opties=[
            "van de frequentie van het licht",
            "van de intensiteit van het licht",
            "van de kleur van het metaal",
            "van de tijd dat je het licht laat schijnen",
        ],
        antwoord=0,
        uitleg=r"Onder de drempelfrequentie \(f_{0}\) komt er niets los, hoe fel je ook "
        r"schijnt. Dat was met een golfmodel alleen niet te verklaren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de laagste frequentie waarbij er elektronen loskomen?",
        antwoord=["de drempelfrequentie", "drempelfrequentie", "grensfrequentie"],
        uitleg=r"Onder \(f_{0}\) heeft een foton te weinig energie om een elektron los te "
        r"maken. Ze hangt af van het metaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een grotere intensiteit van het licht, boven de drempelfrequentie?",
        opties=[
            "er komen meer elektronen los, met dezelfde energie",
            "er komen evenveel elektronen los, met meer energie",
            "er komen meer elektronen los, elk met meer energie",
            "er verandert niets aan het aantal of de energie",
        ],
        antwoord=0,
        uitleg="Meer intensiteit betekent meer fotonen, niet krachtigere fotonen. De energie "
        "per elektron hangt alleen van de frequentie af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de energie van een foton?",
        opties=[
            r"\(E = h\,f\)",
            r"\(E = \dfrac{h}{f}\)",
            r"\(E = h\,\lambda\)",
            r"\(E = \dfrac{f}{h}\)",
        ],
        antwoord=0,
        uitleg=r"\(h = 6{,}63 \times 10^{-34}\ \text{J}\cdot\text{s}\) is de constante van "
        r"Planck. Een hogere \(f\) geeft dus een energierijker foton.",
    ),
    dict(
        type="invultekst",
        vraag="Welke constante staat in de formule van de energie van een foton?",
        antwoord=["van Planck", "Planck", "h"],
        uitleg=r"Ze is \(h = 6{,}63 \times 10^{-34}\ \text{J}\cdot\text{s}\). Op het examen "
        r"staat ze in de bijlage.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een metaal heeft \(f_{0} = 6 \times 10^{14}\) Hz. Wat gebeurt er bij licht van \(4 \times 10^{14}\) Hz?",
        opties=[
            "er komt geen enkel elektron los",
            "er komen elektronen los met weinig energie",
            "er komen elektronen los als je fel genoeg schijnt",
            "er komen elektronen los na een lange tijd wachten",
        ],
        antwoord=0,
        uitleg="Elk foton heeft daar minder energie dan het elektron nodig heeft. Twee "
        "fotonen samen helpen niet, want het elektron neemt er één op.",
    ),
    dict(
        type="waarofniet",
        vraag="Het foto-elektrisch effect laat zien dat licht ook een deeltjeskarakter heeft.",
        antwoord=True,
        uitleg="Alleen met pakketjes energie kan je de drempelfrequentie verklaren. Die "
        "pakketjes heten fotonen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen werken met het foto-elektrisch effect? Kruis alles aan wat juist is.",
        opties=[
            "een zonnepaneel op een dak",
            "een fotocel in een bewegingsdetector",
            "een rookdetector die met licht werkt",
            "een gloeilamp aan het plafond",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een gloeilamp werkt net de andere kant op: elektriciteit wordt licht. De "
        "eerste drie maken van licht een stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een zonnecel?",
        opties=[
            "het licht maakt ladingen los die een stroom vormen",
            "het licht verwarmt een vloeistof die een turbine drijft",
            "het licht laat een magneet in een spoel bewegen",
            "het licht verandert de weerstand van een draad",
        ],
        antwoord=0,
        uitleg="Het is het foto-elektrisch effect in een halfgeleider. Een zonneboiler werkt "
        "wel met warmte in plaats van met losse ladingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Blauw licht heeft een energierijker foton dan rood licht.",
        antwoord=True,
        uitleg=r"Blauw heeft een hogere \(f\), en \(E = h\,f\). Daarom kan blauw licht "
        r"elektronen losmaken waar rood dat niet lukt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het foto-elektrisch effect zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de frequentie beslist of er elektronen loskomen",
            "de intensiteit beslist hoeveel elektronen er loskomen",
            "de intensiteit beslist of er elektronen loskomen",
            "er is altijd een lange wachttijd voor het eerste elektron",
        ],
        antwoord=[0, 1],
        uitleg="De elektronen komen zo goed als meteen los, zonder wachttijd. En de "
        "intensiteit kan de drempelfrequentie niet vervangen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is \(E\) van een foton met \(f = 5 \times 10^{14}\) Hz? Neem \(h = 6{,}63 \times 10^{-34}\) J·s.",
        opties=[
            r"ongeveer \(3{,}3 \times 10^{-19}\) J",
            r"ongeveer \(3{,}3 \times 10^{-20}\) J",
            r"ongeveer \(1{,}3 \times 10^{-48}\) J",
            r"ongeveer \(7{,}5 \times 10^{47}\) J",
        ],
        antwoord=0,
        uitleg=r"\(E = h\,f = 6{,}63 \times 10^{-34} \times 5 \times 10^{14} "
        r"= 3{,}3 \times 10^{-19}\) J.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verklaart het klassieke golfmodel het foto-elektrisch effect niet?",
        opties=[
            "het voorspelt dat fel rood licht ook elektronen losmaakt",
            "het voorspelt dat licht helemaal geen energie vervoert",
            "het voorspelt dat er altijd te veel elektronen loskomen",
            "het voorspelt dat licht niet door een metaal kan gaan",
        ],
        antwoord=0,
        uitleg="Een golf zou energie langzaam kunnen opsparen tot het genoeg is. In de "
        "praktijk gebeurt dat niet, en dat vraagt om fotonen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het foto-elektrisch effect neemt één elektron de energie van meerdere fotonen samen op.",
        antwoord=False,
        uitleg="Het neemt de energie van één foton op, alles of niets. Net daarom bestaat er "
        "een scherpe drempelfrequentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat blijft er over van de energie van een foton nadat het elektron los is?",
        opties=[
            "het verschil wordt kinetische energie van het elektron",
            "het verschil wordt opnieuw als licht uitgezonden",
            "het verschil verdwijnt zonder spoor",
            "het verschil wordt lading van het elektron",
        ],
        antwoord=0,
        uitleg=r"\(E_{k} = h\,f - W\): een deel gaat naar het losmaken zelf en de rest naar "
        r"de beweging. Daarom vliegen de elektronen bij blauw licht sneller weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband bestaat er tussen de energie van een foton en de golflengte?",
        opties=[
            r"een kleinere \(\lambda\) geeft een energierijker foton",
            r"een grotere \(\lambda\) geeft een energierijker foton",
            r"\(\lambda\) heeft met de energie niets te maken",
            r"\(E\) is recht evenredig met \(\lambda\)",
        ],
        antwoord=0,
        uitleg=r"\(E = \dfrac{h\,c}{\lambda}\), want een kleine \(\lambda\) hoort bij een "
        r"hoge \(f\). Daarom is gammastraling zo energierijk en een radiogolf niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om de minimale fotonenergie voor een metaal te bepalen? Kruis alles aan wat juist is.",
        opties=[
            "de drempelfrequentie van dat metaal",
            "de constante van Planck",
            "de intensiteit van het licht",
            "de kleur van het metaaloppervlak",
        ],
        antwoord=[0, 1],
        uitleg=r"\(E_{\min} = h\,f_{0}\), dus je vermenigvuldigt die twee. De intensiteit "
        r"zegt alleen hoeveel fotonen er aankomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een fotocel in een bewegingsdetector zendt zelf licht uit om te meten.",
        antwoord=False,
        uitleg="De cel zet net licht om in een stroom; de bron staat ernaast of ertegenover. "
        "Valt de lichtbundel weg, dan valt de stroom weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een rookdetector met licht af als er rook in zit?",
        opties=[
            "de rook verstrooit de bundel en de fotocel krijgt minder licht",
            "de rook verwarmt de fotocel tot ze een stroom geeft",
            "de rook geeft zelf licht af dat de fotocel opvangt",
            "de rook maakt de lucht in de detector elektrisch geladen",
        ],
        antwoord=0,
        uitleg="De cel merkt die verandering en zet het alarm aan. Het is dus het "
        "foto-elektrisch effect dat de wacht houdt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat liet het experiment van Davisson en Germer zien?",
        opties=[
            "dat een bundel elektronen zich als een golf gedraagt",
            "dat een bundel licht zich als een deeltje gedraagt",
            "dat elektronen in een atoom op vaste banen lopen",
            "dat elektronen geen massa blijken te hebben",
        ],
        antwoord=0,
        uitleg="Ze stuurden elektronen op een nikkelplaatje en kregen een "
        "buigingspatroon. Dat kan alleen een golf geven.",
    ),
    dict(
        type="invultekst",
        vraag="Op welk metaal stuurden Davisson en Germer hun elektronenbundel?",
        antwoord=["nikkel", "op nikkel", "een nikkelplaatje"],
        uitleg="De regelmatige rijen atomen werkten als een rooster. Het patroon erachter "
        "verraadde het golfkarakter van de elektronen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de dualiteit van licht en materie?",
        opties=[
            "ze gedragen zich soms als een golf en soms als een deeltje",
            "ze gedragen zich altijd als een golf en nooit als een deeltje",
            "licht is een golf en materie is altijd een deeltje",
            "ze bestaan elk uit twee soorten deeltjes samen",
        ],
        antwoord=0,
        uitleg="Welk gezicht je ziet, hangt af van de proef die je doet. Beide modellen zijn "
        "nodig en geen van de twee is het hele verhaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen van licht verklaart het golfmodel het best? Kruis alles aan wat juist is.",
        opties=[
            "interferentie bij de proef van Young",
            "buiging rond een smalle opening",
            "breking bij de overgang naar glas",
            "de drempelfrequentie bij een fotocel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De drempelfrequentie heb je het deeltjesmodel voor nodig. De eerste drie "
        "zijn typisch golfgedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschrijft de golffunctie van een deeltje?",
        opties=[
            "de kans om het deeltje op een bepaalde plaats te vinden",
            "de baan die het deeltje precies zal volgen",
            "de snelheid die het deeltje op elk ogenblik heeft",
            "de massa die het deeltje op elke plaats heeft",
        ],
        antwoord=0,
        uitleg="Ze is dus een waarschijnlijkheidsgolf en geen spoor. Een vaste baan bestaat "
        "in de kwantumfysica niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de golffunctie bij een meting, volgens de Kopenhaagse interpretatie?",
        opties=[
            "ze valt samen tot één uitkomst",
            "ze wordt groter en spreidt verder uit",
            "ze blijft precies zoals ze was",
            "ze splitst zich in twee nieuwe golffuncties",
        ],
        antwoord=0,
        uitleg="Voor de meting is er enkel een kansverdeling, erna één plaats. De meting "
        "zelf hoort dus bij het verhaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de kwantumfysica is de plaats van een elektron in een atoom een kansverdeling.",
        antwoord=True,
        uitleg="Er is geen vaste baan, enkel een gebied waar je het met een zekere kans "
        "vindt. Dat gebied heet een orbitaal.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het gebied waar een elektron zich met grote kans bevindt?",
        antwoord=["een orbitaal", "orbitaal", "waarschijnlijkheidsgebied"],
        uitleg="Het is geen baan maar een wolk van kansen. De vorm ervan volgt uit de "
        "Schrödingervergelijking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de Schrödingervergelijking?",
        opties=[
            "om de golffunctie van een deeltje te bepalen",
            "om de massa van een deeltje te bepalen",
            "om de energie van een foton te bepalen",
            "om de snelheid van het licht te bepalen",
        ],
        antwoord=0,
        uitleg="Uit die golffunctie volgen de kansen en de energieën. Voor het atoom geeft "
        "ze precies de vormen van de orbitalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het onzekerheidsbeginsel van Heisenberg?",
        opties=[
            "plaats en impuls zijn niet samen scherp te kennen",
            "plaats en impuls zijn nooit afzonderlijk te meten",
            "een meting geeft altijd een verkeerde uitkomst",
            "een deeltje heeft geen plaats en geen impuls",
        ],
        antwoord=0,
        uitleg=r"\(\Delta x \cdot \Delta p \geq \dfrac{h}{4\pi}\): hoe scherper je het ene "
        r"kent, hoe vager het andere wordt. Dat is de natuur zelf, niet het toestel.",
    ),
    dict(
        type="waarofniet",
        vraag="Het onzekerheidsbeginsel komt doordat onze meettoestellen nog niet nauwkeurig genoeg zijn.",
        antwoord=False,
        uitleg="Het is een eigenschap van de natuur, niet van de apparatuur. Een beter "
        "toestel maakt er dus geen einde aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een elektron zijn juist volgens de kwantumfysica? Kruis alles aan wat juist is.",
        opties=[
            "het heeft een golfkarakter én een deeltjeskarakter",
            "zijn plaats in een atoom is een kansverdeling",
            "het volgt rond de kern een vaste cirkelbaan",
            "zijn plaats en impuls zijn samen scherp te kennen",
        ],
        antwoord=[0, 1],
        uitleg="De vaste cirkelbaan was een ouder model. Plaats en impuls samen scherp "
        "kennen botst op het onzekerheidsbeginsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom merken we de golfkant van een voetbal niet?",
        opties=[
            "zijn golflengte is onvoorstelbaar klein door zijn grote massa",
            "zijn golflengte is onvoorstelbaar groot door zijn grote massa",
            "een voetbal heeft helemaal geen golfkarakter",
            "een voetbal beweegt daarvoor veel te langzaam",
        ],
        antwoord=0,
        uitleg=r"De Broglie: \(\lambda = \dfrac{h}{m\,v}\), dus een grote \(m\) geeft een "
        r"piepkleine \(\lambda\). Bij een elektron is ze wel meetbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook een elektron kan een buigingspatroon geven, net als licht.",
        antwoord=True,
        uitleg="Dat is precies wat Davisson en Germer zagen. Een elektronenmicroscoop maakt "
        "er gebruik van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een kansverdeling voor de plaats van een elektron?",
        opties=[
            "sommige plaatsen zijn veel waarschijnlijker dan andere",
            "alle plaatsen in het atoom zijn even waarschijnlijk",
            "het elektron is op alle plaatsen tegelijk aanwezig",
            "het elektron heeft geen plaats tot je het maakt",
        ],
        antwoord=0,
        uitleg="De wolk is dus dichter waar de kans groter is. Meet je, dan vind je het op "
        "één van die plaatsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verschijnselen vragen het deeltjesmodel van licht? Kruis alles aan wat juist is.",
        opties=[
            "het foto-elektrisch effect",
            "de drempelfrequentie van een metaal",
            "het patroon van strepen bij twee spleten",
            "de breking van licht in water",
        ],
        antwoord=[0, 1],
        uitleg="De laatste twee horen bij het golfmodel. Het deeltjesmodel is nodig zodra "
        "licht zijn energie in pakketjes afgeeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Licht is in werkelijkheid alleen een golf, en het deeltjesmodel is enkel een rekentruc.",
        antwoord=False,
        uitleg="Beide modellen beschrijven echt gedrag, elk in zijn eigen proef. Dat samen "
        "noemt men de dualiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in het tweespletenexperiment als je de elektronen één per één afvuurt?",
        opties=[
            "na lang wachten staat er toch een patroon van strepen",
            "er komt nooit een patroon van strepen",
            "elk elektron maakt zelf meteen het hele patroon",
            "de elektronen botsen op elkaar en vormen twee vlekken",
        ],
        antwoord=0,
        uitleg="Elk elektron landt op één plek, maar de kansen vormen samen de strepen. Dat "
        "is de golffunctie aan het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan je van een elektron geen baan tekenen zoals van een planeet?",
        opties=[
            "plaats en snelheid zijn niet samen scherp te kennen",
            "een elektron beweegt daarvoor veel te snel",
            "een elektron staat in een atoom helemaal stil",
            "een elektron heeft geen massa en dus geen baan",
        ],
        antwoord=0,
        uitleg="Een baan vraagt net die twee tegelijk. Daarom spreekt men van een orbitaal "
        "en niet van een baan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de proef van Young en het experiment van Davisson en Germer gemeen?",
        opties=[
            "ze laten allebei een golfkarakter zien",
            "ze laten allebei een deeltjeskarakter zien",
            "ze werken allebei met een metaalplaatje",
            "ze meten allebei de energie van een foton",
        ],
        antwoord=0,
        uitleg="De eerste bij licht, de tweede bij materie. Samen vormen ze de ene helft van "
        "de dualiteit.",
    ),
]
