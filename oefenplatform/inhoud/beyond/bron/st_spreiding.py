# -*- coding: utf-8 -*-
"""Spreidingsmaten en de boxplot.

De fiche noemt vier spreidingsmaten bij naam: variatiebreedte, kwartielen,
interkwartielafstand en standaardafwijking. En ze noemt de boxplot bij de
grafische voorstellingen, waardoor die twee onderdelen hier samenkomen: een
boxplot is niets anders dan vijf kengetallen in beeld.

De regel van anderhalve interkwartielafstand voor uitschieters staat níét in
het formularium van deze fiche. Ze staat wel in elk handboek en elke rekenapp
tekent haar snorharen erop, dus ze staat hier als vuistregel en nooit als een
formule die een kind uit het hoofd moet kennen.

Eén valkuil bij het berekenen van de kwartielen: voor Q1 neem je de mediaan
van de onderste helft en voor Q3 die van de bovenste helft. Bij een oneven
aantal gegevens laat je de mediaan zelf buiten die twee helften. Handboeken
verschillen hierin; wij volgen de methode die de rekenapps gebruiken.

Deel 1 is de variatiebreedte, de kwartielen en de interkwartielafstand.
Deel 2 is de standaardafwijking en de boxplot.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de variatiebreedte van een dataset?",
        opties=[
            "het verschil tussen de grootste en de kleinste waarde",
            "het verschil tussen het derde en het eerste kwartiel",
            "het gemiddelde van de grootste en de kleinste waarde",
            "het aantal verschillende waarden in de dataset",
        ],
        antwoord=0,
        uitleg="De eenvoudigste spreidingsmaat, maar ook de meest gevoelige: één uitschieter bepaalt ze volledig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de variatiebreedte van 2, 4, 6, 8, 10, 12, 14 en 16?",
        opties=["veertien", "zestien", "achttien", "acht"],
        antwoord=0,
        uitleg="Zestien min twee is veertien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het tweede kwartiel van een dataset?",
        opties=[
            "de mediaan",
            "het gemiddelde",
            "de modus",
            "de variatiebreedte",
        ],
        antwoord=0,
        uitleg="Q2 is een ander woord voor de mediaan: de helft van de gegevens ligt eronder.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kwart van de gegevens ligt onder het eerste kwartiel.",
        antwoord=True,
        uitleg="Daarom heet het een kwartiel. Boven het derde kwartiel ligt ook een kwart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de interkwartielafstand?",
        opties=[
            "het derde kwartiel min het eerste kwartiel",
            "de grootste waarde min de kleinste waarde",
            "het derde kwartiel plus het eerste kwartiel",
            "de mediaan min het eerste kwartiel",
        ],
        antwoord=0,
        uitleg="Ze beschrijft de breedte van de middelste helft van de gegevens en laat de staarten buiten beschouwing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 en 11: wat is de mediaan?",
        opties=["zes", "vijf", "zeven", "vijf komma vijf"],
        antwoord=0,
        uitleg="Elf waarden, dus de zesde. Dat is zes.",
    ),
    dict(
        type="invultekst",
        vraag="Bij 1 tot en met 11 is Q1 gelijk aan 3 en Q3 gelijk aan 9. Wat is de interkwartielafstand? Geef het getal in cijfers.",
        antwoord=["6"],
        uitleg="Negen min drie is zes.",
    ),
    dict(
        type="waarofniet",
        vraag="De interkwartielafstand is minder gevoelig voor uitschieters dan de variatiebreedte.",
        antwoord=True,
        uitleg="Ze kijkt enkel naar de middelste helft, dus een extreme waarde aan de rand doet haar niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij 2, 4, 6, 8, 10, 12, 14 en 16: wat is de mediaan?",
        opties=["negen", "acht", "tien", "acht komma vijf"],
        antwoord=0,
        uitleg="Acht waarden, dus het gemiddelde van de vierde en de vijfde: acht en tien geven negen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij diezelfde dataset 2 tot 16 met stap twee: wat is het eerste kwartiel?",
        opties=["vijf", "vier", "zes", "drie"],
        antwoord=0,
        uitleg="De onderste helft is 2, 4, 6 en 8, en haar mediaan is het gemiddelde van vier en zes, dus vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="De variatiebreedte kan negatief zijn.",
        antwoord=False,
        uitleg="Nooit. De grootste waarde is minstens gelijk aan de kleinste, dus het verschil is nul of positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een interkwartielafstand van nul?",
        opties=[
            "de middelste helft van de gegevens heeft allemaal dezelfde waarde",
            "de dataset bevat geen enkele waarde",
            "alle waarden in de dataset zijn verschillend",
            "de mediaan ligt precies in het midden van het bereik",
        ],
        antwoord=0,
        uitleg="Q1 en Q3 vallen dan samen. Dat gebeurt bij een dataset waar heel veel waarden gelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee klassen hebben dezelfde mediaan maar klas A heeft een interkwartielafstand van 2 en klas B van 8. Wat besluit je?",
        opties=[
            "de resultaten van klas B liggen veel verder uit elkaar",
            "klas B heeft een hogere mediaan dan klas A",
            "klas A heeft meer uitschieters dan klas B",
            "de twee klassen zijn niet te vergelijken",
        ],
        antwoord=0,
        uitleg="Hetzelfde midden, een heel andere spreiding. Dat is precies wat een spreidingsmaat moet laten zien.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het tweede kwartiel met een ander woord? Eén woord.",
        antwoord=["mediaan", "de mediaan"],
        uitleg="Q2 is de mediaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een oneven aantal gegevens laat je de mediaan buiten de twee helften waarmee je Q1 en Q3 berekent.",
        antwoord=True,
        uitleg="Zo doen de rekenapps het ook. Handboeken verschillen hierin, dus vermeld altijd welke methode je gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel procent van de gegevens ligt tussen Q1 en Q3?",
        opties=["vijftig procent", "vijfentwintig procent", "vijfenzeventig procent", "honderd procent"],
        antwoord=0,
        uitleg="Een kwart ligt onder Q1 en een kwart boven Q3, dus de helft zit ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de variatiebreedte vaak een slechte maat voor spreiding?",
        opties=[
            "ze gebruikt enkel de twee meest extreme waarden",
            "ze gebruikt alle waarden en wordt daardoor te groot",
            "ze kan niet met ICT berekend worden bij grote datasets",
            "ze is niet in dezelfde eenheid als de gegevens",
        ],
        antwoord=0,
        uitleg="Duizend waarden tussen tien en twaalf plus één van duizend geven een variatiebreedte van 990. Dat zegt niets over de duizend.",
    ),
    dict(
        type="waarofniet",
        vraag="Het eerste kwartiel is altijd groter dan de mediaan.",
        antwoord=False,
        uitleg="Omgekeerd. De kwartielen liggen in de orde Q1, Q2, Q3, dus Q1 is kleiner dan of gelijk aan de mediaan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel kwartielen verdelen een dataset in vier gelijke delen? Geef het getal in cijfers.",
        antwoord=["3", "drie"],
        uitleg="Drie kwartielen geven vier delen, net zoals drie knippen een lint in vier stukken verdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zoekt Q1 van een onsorteerde lijst en neemt de waarde op een kwart van de lijst. Wat gaat er mis?",
        opties=[
            "hij moet eerst rangschikken, anders betekent die plaats niets",
            "hij moet een kwart van de som nemen in plaats van de plaats",
            "hij moet de mediaan ervan aftrekken na het rangschikken",
            "hij moet door het aantal waarden delen in plaats van door vier",
        ],
        antwoord=0,
        uitleg="Rangschikken is bij elke positiemaat de eerste stap. Dat geldt voor de mediaan en voor de kwartielen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat meet de standaardafwijking van een dataset?",
        opties=[
            "hoeveel de waarden gemiddeld van het gemiddelde afwijken",
            "het verschil tussen de grootste en de kleinste waarde",
            "het verschil tussen het gemiddelde en de mediaan",
            "het aantal waarden dat boven het gemiddelde ligt",
        ],
        antwoord=0,
        uitleg="Ze gebruikt alle waarden, in tegenstelling tot de variatiebreedte en de interkwartielafstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke eenheid staat de standaardafwijking?",
        opties=[
            "in dezelfde eenheid als de gegevens",
            "in de eenheid van de gegevens in het kwadraat",
            "altijd in procent, zonder eenheid",
            "in de eenheid van de gegevens gedeeld door het aantal",
        ],
        antwoord=0,
        uitleg="Daarom is ze bruikbaarder dan de variantie, die in de eenheid in het kwadraat staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een standaardafwijking van nul betekent dat alle waarden gelijk zijn.",
        antwoord=True,
        uitleg="Geen spreiding kan enkel als er geen verschil tussen de waarden is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool gebruikt de bijlage voor de steekproefstandaardafwijking?",
        opties=["de letter s", "de letter sigma", "de letter n", "de letter p"],
        antwoord=0,
        uitleg="s voor de steekproef, sigma voor de populatie. Dat onderscheid wordt op het examen nagekeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vijf getallen staan in een boxplot?",
        opties=[
            "het minimum, de drie kwartielen en het maximum",
            "het gemiddelde, de mediaan, de modus, Q1 en Q3",
            "het minimum, het gemiddelde, de mediaan, de modus en het maximum",
            "de vijf meest voorkomende waarden van de dataset",
        ],
        antwoord=0,
        uitleg="Die vijf heten samen de vijf kengetallen. Het gemiddelde staat er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de doos van een boxplot voor?",
        opties=[
            "het gebied van Q1 tot Q3, dus de middelste helft",
            "het gebied van het minimum tot het maximum",
            "het gebied rond het gemiddelde plus en min de standaardafwijking",
            "het gebied waar de uitschieters liggen",
        ],
        antwoord=0,
        uitleg="De streep in de doos is de mediaan. De breedte van de doos is de interkwartielafstand.",
    ),
    dict(
        type="invultekst",
        vraag="Welk kengetal stelt de streep binnen de doos van een boxplot voor? Eén woord.",
        antwoord=["mediaan", "de mediaan"],
        uitleg="De mediaan, dus Q2.",
    ),
    dict(
        type="waarofniet",
        vraag="Een boxplot waarvan de streep niet in het midden van de doos staat, wijst op een scheve verdeling.",
        antwoord=True,
        uitleg="Ligt de mediaan dicht bij Q1, dan hangt de verdeling scheef naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de vuistregel om een uitschieter in een boxplot aan te duiden?",
        opties=[
            "een waarde die verder dan anderhalve interkwartielafstand buiten de doos ligt",
            "een waarde die meer dan twee keer het gemiddelde bedraagt",
            "elke waarde die buiten de doos van de boxplot valt",
            "de grootste en de kleinste waarde van elke dataset",
        ],
        antwoord=0,
        uitleg="De snorharen stoppen bij die grens, en wat erbuiten valt, wordt als los punt getekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij Q1 gelijk aan 10 en Q3 gelijk aan 20, waar liggen de grenzen voor uitschieters?",
        opties=[
            "onder min vijf en boven vijfendertig",
            "onder nul en boven dertig",
            "onder vijf en boven vijfentwintig",
            "onder tien en boven twintig",
        ],
        antwoord=0,
        uitleg="De interkwartielafstand is tien, anderhalf keer tien is vijftien. Dus tien min vijftien en twintig plus vijftien.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit een boxplot kan je aflezen hoeveel gegevens er in de dataset zitten.",
        antwoord=False,
        uitleg="Nee. Elk deel bevat per definitie een kwart van de gegevens, maar hoeveel dat er zijn, zegt een boxplot niet. Daarvoor heb je n nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn twee boxplots naast elkaar zo handig om groepen te vergelijken?",
        opties=[
            "je ziet in één beeld het centrum, de spreiding en de uitschieters",
            "je ziet in één beeld het gemiddelde en de standaardafwijking",
            "je ziet in één beeld hoeveel gegevens elke groep bevat",
            "je ziet in één beeld of de verdeling normaal is",
        ],
        antwoord=0,
        uitleg="Op dezelfde as leest een boxplot zich in één oogopslag. Het aantal gegevens zet je er het best bij in de tekst.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk getal vermenigvuldig je de interkwartielafstand voor de grenzen van de uitschieters? Geef het getal als decimaal.",
        antwoord=["1,5", "1.5"],
        uitleg="Anderhalf. Die vuistregel staat niet in het formularium, maar elke rekenapp gebruikt ze.",
    ),
    dict(
        type="waarofniet",
        vraag="De standaardafwijking is gevoeliger voor uitschieters dan de interkwartielafstand.",
        antwoord=True,
        uitleg="Ze gebruikt alle waarden en kwadrateert de afwijkingen, dus één extreme waarde weegt zwaar door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dataset heeft een gemiddelde van 50 en een standaardafwijking van 2. Een waarde van 70 is dan wat?",
        opties=[
            "een uitzonderlijke waarde, tien standaardafwijkingen boven het gemiddelde",
            "een gewone waarde, want 70 ligt dicht bij 50",
            "precies de bovengrens van het normale bereik",
            "onmogelijk, want 70 ligt buiten het bereik van de dataset",
        ],
        antwoord=0,
        uitleg="Twintig gedeeld door twee is tien. Boven drie standaardafwijkingen is een waarde al heel zeldzaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je volgens de fiche de spreidingsmaten bij een grote dataset?",
        opties=[
            "met ICT, dus met de rekenapps van de examencommissie",
            "met de hand, want een rekenapp geeft geen kwartielen",
            "door enkel de variatiebreedte te nemen, die volstaat",
            "door de dataset eerst in klassen te groeperen",
        ],
        antwoord=0,
        uitleg="De fiche zegt het letterlijk: je berekent met ICT centrummaten en spreidingsmaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee datasets met hetzelfde gemiddelde hebben altijd dezelfde standaardafwijking.",
        antwoord=False,
        uitleg="Helemaal niet. Negen, tien en elf hebben hetzelfde gemiddelde als nul, tien en twintig, met een heel andere spreiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boxplot heeft een korte linkersnorhaar en een heel lange rechtersnorhaar. Hoe beschrijf je die verdeling?",
        opties=[
            "scheef naar rechts, met uitgespreide hoge waarden",
            "scheef naar links, met uitgespreide lage waarden",
            "symmetrisch, want de doos is in het midden",
            "zonder spreiding, want de doos is smal",
        ],
        antwoord=0,
        uitleg="De lange kant is de staart. Rechts lang betekent scheef naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke spreidingsmaat zou je kiezen bij een dataset met enkele extreme uitschieters?",
        opties=[
            "de interkwartielafstand, want die is robuust",
            "de variatiebreedte, want die gebruikt de uiterste waarden",
            "de standaardafwijking, want die gebruikt alle waarden",
            "de modus, want die is niet gevoelig voor uitschieters",
        ],
        antwoord=0,
        uitleg="Net zoals je daar de mediaan boven het gemiddelde verkiest. De modus is trouwens geen spreidingsmaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling meldt een standaardafwijking van min drie. Wat zeg je?",
        opties=[
            "een standaardafwijking kan niet negatief zijn, er zit een rekenfout in",
            "dat betekent dat de waarden onder het gemiddelde liggen",
            "dat kan, bij een dalende reeks is de spreiding negatief",
            "hij moet het minteken weglaten en verder rekenen",
        ],
        antwoord=0,
        uitleg="Ze is de wortel uit een som van kwadraten, dus altijd nul of positief. Vaak is de wortel vergeten of het teken verkeerd ingetikt.",
    ),
]
