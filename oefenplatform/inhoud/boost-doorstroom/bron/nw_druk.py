# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Druk en de gaswetten.

Fysica, de koppen "Druk", "Druk op en in vloeistoffen", "Druk op en in
gassen" en "Gaswetten" van de vakfiche natuurwetenschappen 2de graad
doorstroom. Deel 1 gaat over druk op een oppervlak en over de hydrostatische
druk met het beginsel van Pascal; deel 2 over druk bij gassen, de
kelvinschaal en de gaswetten.

De gaswetten (isobaar, isochoor, isotherm en de algemene gaswet) en de
kelvinschaal staan alleen in de uitgebreide fiche (moderne talen en Latijn).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de druk op een oppervlak?",
        opties=[
            "de kracht delen door de oppervlakte",
            "de oppervlakte delen door de kracht",
            "de kracht vermenigvuldigen met de oppervlakte",
            "de kracht optellen bij de oppervlakte",
        ],
        antwoord=0,
        uitleg="Dezelfde kracht op een kleiner oppervlak geeft een grotere druk. Daarom dringt een naald zo gemakkelijk binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van druk?",
        opties=["de pascal", "de newton", "de bar", "de joule"],
        antwoord=0,
        uitleg="Eén pascal is één newton per vierkante meter. Bar, millibar en hectopascal zijn handiger eenheden voor het weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij dezelfde kracht geeft een kleiner oppervlak een grotere druk.",
        antwoord=True,
        uitleg="De kracht wordt dan over minder vierkante centimeter verdeeld. Daarom snijdt een scherp mes beter dan een bot mes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zak je met sneeuwschoenen minder diep weg in de sneeuw?",
        opties=[
            "het zooloppervlak is groter, dus is de druk op de sneeuw kleiner",
            "het zooloppervlak is groter, dus is de kracht op de sneeuw kleiner",
            "je massa wordt kleiner doordat de schoenen zo licht zijn gemaakt",
            "de sneeuw wordt harder op de plaats waar de schoen hem raakt",
        ],
        antwoord=0,
        uitleg="Je gewicht verandert niet, enkel het oppervlak waarover het verdeeld wordt. Een naaldhak doet precies het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de druk die door het gewicht van een vloeistof zelf ontstaat?",
        antwoord="hydrostatische druk",
        uitleg="Ze is groter naarmate je dieper komt. Daarom moet je bij het duiken je oren klaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de hydrostatische druk in een vloeistof af? Kruis alles aan wat juist is.",
        opties=[
            "de diepte in de vloeistof",
            "de massadichtheid van de vloeistof",
            "de zwaarteveldsterkte",
            "de oppervlakte van de bodem",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie zitten alle drie in de formule. Hoe breed of smal het vat is, maakt voor de druk op een bepaalde diepte niets uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De hydrostatische druk op tien meter diepte is groter dan op twee meter diepte.",
        antwoord=True,
        uitleg="Boven je hoofd staat op tien meter vijf keer zo veel water. Elke tien meter water voegt ongeveer één bar toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het beginsel van Pascal?",
        opties=[
            "een drukverandering plant zich in een vloeistof in alle richtingen voort",
            "een drukverandering blijft beperkt tot de plaats waar je ze uitoefent",
            "een drukverandering plant zich alleen naar beneden in de vloeistof voort",
            "een drukverandering maakt de vloeistof plaatselijk een stuk dichter",
        ],
        antwoord=0,
        uitleg="Daarom werkt een hydraulische rem: je duwt op het pedaal en de druk komt onverminderd bij alle vier de wielen aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je tijdens het duiken je oren klaren?",
        opties=[
            "de waterdruk duwt op je trommelvlies en binnen blijft de oude druk staan",
            "het water maakt je trommelvlies slap en dat moet je dan weer opspannen",
            "de koude van het water doet je trommelvlies krimpen bij het dalen",
            "het zout in het water tast het trommelvlies aan als je niets doet",
        ],
        antwoord=0,
        uitleg="Door te klaren laat je lucht in je middenoor, zodat de druk aan beide kanten gelijk wordt. Anders duwt het water je trommelvlies naar binnen.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk toestel meet je de luchtdruk?",
        antwoord="barometer",
        uitleg="Een manometer meet de druk van een gas of vloeistof in een vat of leiding. Een barometer is er speciaal voor de lucht om ons heen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een persoon van 80 kilogram en een van 50 kilogram hebben dezelfde schoenmaat en staan in de modder. Wie zakt het diepst?",
        opties=[
            "de persoon van 80 kilogram, want zijn druk op de modder is groter",
            "de persoon van 50 kilogram, want hij staat minder stevig op de grond",
            "ze zakken precies even diep, want hun schoenoppervlak is gelijk",
            "dat hangt enkel af van hoe lang ze in de modder blijven staan",
        ],
        antwoord=0,
        uitleg="Bij hetzelfde oppervlak bepaalt de kracht de druk. Een grotere massa geeft een grotere zwaartekracht en dus meer druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een duiker ondervindt op grote diepte alleen de hydrostatische druk, niet de luchtdruk.",
        antwoord=False,
        uitleg="De atmosfeer duwt ook op het wateroppervlak. De totale druk is de luchtdruk plus de hydrostatische druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel pascal is één bar?",
        opties=["100 000 pascal", "1 000 pascal", "10 pascal", "1 000 000 pascal"],
        antwoord=0,
        uitleg="Eén bar is 100 kilopascal, en dat is ongeveer de luchtdruk op zeeniveau. In het weerbericht lees je dat als 1000 hectopascal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat een hydraulische pers met een kleine kracht een grote kracht te leveren?",
        opties=[
            "de druk is overal gelijk, maar werkt op een veel groter oppervlak",
            "de druk wordt in de leiding onderweg stelselmatig groter gemaakt",
            "de vloeistof wordt in de pers samengeperst tot een hardere stof",
            "de kracht wordt door de wrijving in de leiding nog eens versterkt",
        ],
        antwoord=0,
        uitleg="Kracht is druk maal oppervlakte. Tien keer meer oppervlak geeft dus tien keer meer kracht, over een tien keer kortere weg.",
    ),
    dict(
        type="waarofniet",
        vraag="De luchtdruk neemt af als je hoger in de bergen gaat.",
        antwoord=True,
        uitleg="Er staat dan minder lucht boven je. Daarom moet je op grote hoogte soms extra zuurstof gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt dezelfde baksteen eerst op zijn platte kant en dan op zijn smalle kant. Wat verandert er?",
        opties=[
            "de druk op de grond, want het contactoppervlak verandert",
            "de kracht op de grond, want de steen weegt anders zwaar",
            "zowel de kracht als de druk, want beide hangen van de stand af",
            "er verandert niets, want het is dezelfde steen die er ligt",
        ],
        antwoord=0,
        uitleg="De zwaartekracht op de steen blijft dezelfde. Op de smalle kant wordt die kracht over minder oppervlak verdeeld, dus is de druk groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de druk op een oppervlak af? Kruis alles aan wat juist is.",
        opties=[
            "van de grootte van de kracht",
            "van de grootte van het oppervlak",
            "van de stand waarin het voorwerp ligt",
            "van de kleur van het voorwerp",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alleen de kracht en de oppervlakte staan in de formule, en de stand speelt mee omdat ze het contactoppervlak bepaalt. De kleur heeft er niets mee te maken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een druk die lager is dan de omgevingsdruk?",
        antwoord="onderdruk",
        uitleg="Bij overdruk is de druk juist hoger dan de omgeving. Een zuignap werkt op onderdruk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een manometer is het toestel waarmee je de luchtdruk buiten meet.",
        antwoord=False,
        uitleg="Een manometer meet de druk van een gas of vloeistof in een vat of leiding, zoals op een gasfles. Voor de buitenlucht gebruik je een barometer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duwt met 200 newton op een oppervlak van 0,5 vierkante meter. Hoe groot is de druk?",
        opties=["400 pascal", "100 pascal", "200 pascal", "40 pascal"],
        antwoord=0,
        uitleg="Je deelt de kracht door de oppervlakte: 200 gedeeld door 0,5. Een kleiner oppervlak geeft dus een grotere druk.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat de druk van een gas volgens het deeltjesmodel?",
        opties=[
            "de deeltjes botsen tegen de wand en duwen daar bij elke botsing op",
            "de deeltjes kleven aan de wand vast en trekken die naar buiten",
            "de deeltjes worden door de wand aangetrokken en drukken erop",
            "de deeltjes liggen stil tegen de wand en wegen daar op de wand",
        ],
        antwoord=0,
        uitleg="Miljarden botsingen per seconde geven samen een gelijkmatige druk. Meer of hardere botsingen betekent meer druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de druk van een gas als je het in een kleiner volume perst, bij gelijke temperatuur?",
        opties=[
            "de druk wordt groter, want de deeltjes botsen vaker tegen de wand",
            "de druk wordt kleiner, want er is minder plaats voor de deeltjes",
            "de druk blijft gelijk, want er zijn nog altijd evenveel deeltjes",
            "de druk wordt eerst groter en daarna weer even klein als ervoor",
        ],
        antwoord=0,
        uitleg="In een kleinere ruimte raakt elk deeltje de wand vaker. Druk en volume zijn omgekeerd evenredig bij gelijke temperatuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Nul kelvin is het absolute nulpunt, waarbij de deeltjes geen kinetische energie meer hebben.",
        antwoord=True,
        uitleg="Dat ligt bij min 273,15 graden Celsius. Lager kan niet, want trager dan stil bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kelvin is 27 graden Celsius?",
        opties=["300 kelvin", "246 kelvin", "27 kelvin", "173 kelvin"],
        antwoord=0,
        uitleg="Je telt 273 bij de graden Celsius op. Omgekeerd trek je 273 van de kelvin af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de temperatuurschaal die bij het absolute nulpunt begint?",
        antwoord="kelvinschaal",
        uitleg="In de gaswetten moet je altijd met kelvin rekenen. Met graden Celsius kloppen de verhoudingen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een isotherm proces?",
        opties=[
            "een proces bij een gelijkblijvende temperatuur",
            "een proces bij een gelijkblijvende druk",
            "een proces bij een gelijkblijvend volume",
            "een proces waarbij alle drie samen veranderen",
        ],
        antwoord=0,
        uitleg="Therm verwijst naar temperatuur. Isobaar is bij gelijke druk en isochoor bij gelijk volume.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een isochoor proces blijft het volume van het gas gelijk.",
        antwoord=True,
        uitleg="Het gas zit dan in een vat dat niet van vorm verandert. Verwarm je het, dan stijgt enkel de druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden zijn toestandsgrootheden van een gas? Kruis alles aan wat juist is.",
        opties=["de druk", "het volume", "de absolute temperatuur", "de massadichtheid van de wand"],
        antwoord=[0, 1, 2],
        uitleg="Samen met de stofhoeveelheid beschrijven die drie de toestand van een gas. Het vat waarin het zit, hoort daar niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verwarmt een gas in een gesloten stalen fles. Wat gebeurt er?",
        opties=[
            "de druk stijgt, want het volume kan niet mee veranderen",
            "het volume stijgt, want warme lucht neemt meer plaats in",
            "de druk daalt, want de deeltjes verspreiden zich verder",
            "er verandert niets, want de fles is helemaal gesloten",
        ],
        antwoord=0,
        uitleg="De deeltjes gaan sneller bewegen en botsen harder tegen de wand. Daarom staat er op een spuitbus dat je ze niet mag verwarmen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een proces waarbij de druk van het gas gelijk blijft?",
        antwoord="isobaar",
        uitleg="Bij een isobaar proces veranderen volume en temperatuur samen. Ze zijn dan recht evenredig met elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas van 2 liter bij 1 bar wordt bij gelijke temperatuur tot 1 liter samengeperst. Wat is de druk?",
        opties=["2 bar", "1 bar", "0,5 bar", "4 bar"],
        antwoord=0,
        uitleg="Druk maal volume blijft gelijk bij een vaste temperatuur. Half het volume geeft dus dubbel de druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reëel gas gedraagt zich precies zoals een ideaal gas, bij elke druk en temperatuur.",
        antwoord=False,
        uitleg="Bij hoge druk of lage temperatuur gaan echte gasdeeltjes elkaar aantrekken en nemen ze zelf plaats in. Dan wijkt het gedrag af van de gaswet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de grafiek van de druk tegenover het volume van een gas uit, bij een vaste temperatuur?",
        opties=[
            "een kromme die daalt, want druk en volume zijn omgekeerd evenredig",
            "een rechte die stijgt, want druk en volume zijn recht evenredig",
            "een vlakke lijn, want de druk blijft onveranderd bij elk volume",
            "een rechte die daalt tot precies nul bij het grootste volume",
        ],
        antwoord=0,
        uitleg="Het product van druk en volume blijft gelijk. Daarom buigt de kromme naar de assen toe zonder ze te raken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gas van 300 kelvin bij 1 bar wordt in een gesloten vat tot 600 kelvin verwarmd. Wat is de druk?",
        opties=["2 bar", "1 bar", "0,5 bar", "300 bar"],
        antwoord=0,
        uitleg="Bij gelijk volume zijn druk en absolute temperatuur recht evenredig. Een verdubbeling van de kelvin verdubbelt dus de druk.",
    ),
    dict(
        type="waarofniet",
        vraag="In de gaswetten moet je de temperatuur in kelvin invullen en niet in graden Celsius.",
        antwoord=True,
        uitleg="De verhoudingen gelden alleen vanaf het absolute nulpunt. Met graden Celsius kom je bij nul graden op een onmogelijke uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom loopt een ballon die je in de koelkast legt, wat leeg?",
        opties=[
            "de deeltjes bewegen trager, dus daalt de druk en krimpt de ballon",
            "er ontsnapt lucht door de koude wand van de ballon naar buiten",
            "de lucht in de ballon wordt vloeibaar bij een lagere temperatuur",
            "het rubber van de ballon wordt bij koude veel elastischer dan ervoor",
        ],
        antwoord=0,
        uitleg="De ballon kan van vorm veranderen, dus past het volume zich aan tot de druk weer in balans is met de buitenlucht. Dat is een isobaar proces.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het absolute nulpunt zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het ligt bij ongeveer min 273 graden Celsius",
            "de kinetische energie van de deeltjes is er nul",
            "een lagere temperatuur bestaat niet",
            "de druk van een gas is er het hoogst",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij stilstaande deeltjes zijn er geen botsingen meer, dus zou de druk nul zijn. Dat is het laagste punt, niet het hoogste.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gas oefent alleen naar beneden druk uit, want de deeltjes vallen naar de bodem.",
        antwoord=False,
        uitleg="De deeltjes bewegen in alle richtingen door elkaar. Daarom duwt de lucht in een ballon de wand overal even hard naar buiten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden Celsius is 273 kelvin?",
        antwoord="0",
        uitleg="Je trekt 273 van de kelvin af. Dat is dus precies het smeltpunt van ijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je pompt een fietsband op en hij wordt warm. Hoe verklaar je dat?",
        opties=[
            "je perst de lucht samen en voert er daarbij energie aan toe",
            "de wrijving van de pomp warmt de lucht in de band op",
            "de lucht in de band gaat chemisch reageren met het rubber",
            "de band geeft warmte af aan de lucht die erin gepompt wordt",
        ],
        antwoord=0,
        uitleg="Samenpersen geeft de deeltjes meer energie, en meer energie betekent een hogere temperatuur. De wrijving in de pomp speelt ook mee, maar is niet de hoofdoorzaak.",
    ),
]
