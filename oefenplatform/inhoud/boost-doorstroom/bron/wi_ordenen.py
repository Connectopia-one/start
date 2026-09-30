# -*- coding: utf-8 -*-
"""De vragen voor "Ordenen, afronden, intervallen en wetenschappelijke notatie".

Het tweede deel van de bouwsteen Getallenleer: reële getallen vergelijken en
ordenen, ze voorstellen op een getallenas, de afrondingsregels, de
intervalnotatie met open, halfopen en gesloten intervallen, en het benaderen,
afronden en schatten van getallen, inclusief de notatie met machten van tien.

Deel 1 is ordenen en afronden. Deel 2 zijn de intervallen en de
wetenschappelijke notatie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk van deze getallen is het grootst?",
        opties=["0,7", "0,68", "0,007", "0,0699"],
        antwoord=0,
        uitleg="Vergelijk cijfer per cijfer vanaf de komma. Zeven tienden is meer dan achtenzestig honderdsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk van deze getallen is het kleinst?",
        opties=["min 5,2", "min 5,02", "min 0,52", "min 4,9"],
        antwoord=0,
        uitleg="Bij negatieve getallen is het getal met de grootste afstand tot nul juist het kleinste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe rond je 3,4567 af op twee cijfers na de komma?",
        opties=["3,46", "3,45", "3,50", "3,456"],
        antwoord=0,
        uitleg="Het derde cijfer na de komma is 6, dus je rondt naar boven af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe rond je 2,3449 af op twee cijfers na de komma?",
        opties=["2,34", "2,35", "2,30", "2,344"],
        antwoord=0,
        uitleg="Je kijkt naar het cijfer van de volgende rang, hier een 4, en dat rondt naar beneden af. Het cijfer daarachter telt niet meer mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke afrondingsregel geldt volgens de vakfiche?",
        opties=[
            "bij 0 tot en met 4 rond je naar beneden af, bij 5 tot en met 9 naar boven",
            "bij 0 tot en met 5 rond je naar beneden af, bij 6 tot en met 9 naar boven",
            "je rondt altijd af naar het dichtstbijzijnde even getal",
            "je rondt altijd naar boven af, om zeker geen tekort te hebben",
        ],
        antwoord=0,
        uitleg="Je kijkt daarvoor naar het cijfer van de rang die volgt op de rang waarop je afrondt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk getal ligt tussen 2,4 en 2,5?",
        opties=["2,47", "2,54", "2,39", "24,7"],
        antwoord=0,
        uitleg="Tussen twee getallen liggen er altijd oneindig veel andere. 2,47 is er één van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe orden je 0,5, de breuk 3 op 5 en 45 procent van klein naar groot?",
        opties=[
            "45 procent, 0,5, drie vijfde",
            "0,5, 45 procent, drie vijfde",
            "drie vijfde, 0,5, 45 procent",
            "45 procent, drie vijfde, 0,5",
        ],
        antwoord=0,
        uitleg="Zet ze eerst in dezelfde vorm: 0,45, dan 0,50, dan 0,60.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze getallen ligt het dichtst bij de wortel van 2?",
        opties=["1,41", "1,14", "1,73", "2,41"],
        antwoord=0,
        uitleg="De wortel van 2 is ongeveer 1,4142. 1,73 hoort bij de wortel van 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het symbool ≤ tussen twee getallen?",
        opties=[
            "het linkergetal is kleiner dan of gelijk aan het rechter",
            "het linkergetal is strikt kleiner dan het rechter",
            "het linkergetal is groter dan of gelijk aan het rechter",
            "de twee getallen liggen even ver van nul",
        ],
        antwoord=0,
        uitleg="Het streepje onder het teken laat gelijkheid toe. Zonder streepje is het strikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een getallenas staat min 3 links van 1. Wat betekent dat?",
        opties=[
            "min 3 is kleiner dan 1",
            "min 3 is groter dan 1, want het ligt verder van nul",
            "min 3 en 1 zijn even groot, alleen van teken verschillend",
            "de getallenas is verkeerd getekend",
        ],
        antwoord=0,
        uitleg="Op een getallenas geldt: hoe verder naar links, hoe kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schat 48 maal 21. Welke schatting ligt het dichtst bij?",
        opties=["ongeveer 1000", "ongeveer 700", "ongeveer 1500", "ongeveer 2000"],
        antwoord=0,
        uitleg="50 maal 20 is 1000. De echte uitkomst is 1008.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom rond je pas op het einde van een berekening af?",
        opties=[
            "omdat afrondingsfouten anders bij elke tussenstap groter worden",
            "omdat je anders je rekenmachine niet meer mag gebruiken",
            "omdat een tussenresultaat nooit een komma mag bevatten",
            "omdat de fiche voorschrijft dat je maar één keer mag afronden",
        ],
        antwoord=0,
        uitleg="Wie in drie stappen telkens afrondt, kan er op het einde procenten naast zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een weegschaal geeft 2,5 kilogram en rondt af op honderd gram. Tussen welke waarden ligt het echte gewicht?",
        opties=[
            "tussen 2,45 en 2,55 kilogram",
            "tussen 2,40 en 2,60 kilogram",
            "tussen 2,50 en 2,55 kilogram",
            "precies op 2,5 kilogram",
        ],
        antwoord=0,
        uitleg="Alles vanaf 2,45 rondt af naar 2,5, en alles onder 2,55 ook.",
    ),
    dict(
        type="waarofniet",
        vraag="Tussen twee verschillende reële getallen ligt altijd nog een ander reëel getal.",
        antwoord=True,
        uitleg="Neem gewoon het gemiddelde van de twee: dat ligt er precies tussenin.",
    ),
    dict(
        type="waarofniet",
        vraag="Min 8 is groter dan min 3, want 8 is groter dan 3.",
        antwoord=False,
        uitleg="Bij negatieve getallen keert de volgorde om: min 8 ligt verder naar links en is dus kleiner.",
    ),
    dict(
        type="waarofniet",
        vraag="Afgerond op één cijfer na de komma is 0,449 gelijk aan 0,4.",
        antwoord=True,
        uitleg="Je kijkt naar het tweede cijfer, een 4, en rondt naar beneden af. De 9 erachter doet niet mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schatting vooraf vervangt de controle achteraf.",
        antwoord=False,
        uitleg="Een schatting zegt of je in de juiste grootteorde zit, niet of je exact juist rekende.",
    ),
    dict(
        type="invultekst",
        vraag="Rond 7,3851 af op twee cijfers na de komma.",
        antwoord=["7,39"],
        uitleg="Het derde cijfer na de komma is 5, dus naar boven.",
    ),
    dict(
        type="invultekst",
        vraag="Welk teken hoort tussen min 4 en min 1? Typ < of >.",
        antwoord=["<"],
        uitleg="Min 4 ligt links van min 1 op de getallenas.",
    ),
    dict(
        type="invultekst",
        vraag="Schat 19 maal 31 op honderdtallen.",
        antwoord=["600", "ongeveer 600"],
        uitleg="20 maal 30 is 600. De echte uitkomst is 589.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het interval ]2, 5[?",
        opties=[
            "alle getallen strikt tussen 2 en 5, de grenzen niet meegerekend",
            "alle getallen van 2 tot en met 5, de grenzen meegerekend",
            "alleen de gehele getallen 3 en 4",
            "alle getallen kleiner dan 2 of groter dan 5",
        ],
        antwoord=0,
        uitleg="De haakjes wijzen naar buiten, dus de grenzen horen er niet bij. Dat heet een open interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het interval [0, 1]?",
        opties=[
            "alle getallen van 0 tot en met 1, allebei de grenzen inbegrepen",
            "alle getallen strikt tussen 0 en 1",
            "alleen de twee getallen 0 en 1",
            "alle getallen kleiner dan of gelijk aan 1",
        ],
        antwoord=0,
        uitleg="Haakjes die naar binnen wijzen nemen de grens mee. Dat heet een gesloten interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je 'alle getallen groter dan of gelijk aan 3' als interval?",
        opties=["[3, +∞[", "]3, +∞[", "[3, +∞]", "]−∞, 3]"],
        antwoord=0,
        uitleg="De 3 hoort erbij, dus een vierkant haakje. Bij oneindig staat er altijd een haakje naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er bij oneindig altijd een haakje dat naar buiten wijst?",
        opties=[
            "omdat oneindig geen getal is en er dus niet bij kan horen",
            "omdat oneindig te groot is om op te schrijven",
            "omdat het interval anders leeg zou zijn",
            "omdat dat alleen bij negatieve oneindig zo is",
        ],
        antwoord=0,
        uitleg="Oneindig is een richting, geen waarde. Je kan het dus niet insluiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk interval hoort bij 'x is kleiner dan 7'?",
        opties=["]−∞, 7[", "]−∞, 7]", "[7, +∞[", "]7, +∞["],
        antwoord=0,
        uitleg="Strikt kleiner, dus de 7 hoort er niet bij, en links loopt het naar min oneindig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je het interval [0, 4[?",
        opties=[
            "een halfopen interval",
            "een open interval",
            "een gesloten interval",
            "een leeg interval",
        ],
        antwoord=0,
        uitleg="Eén grens hoort erbij en de andere niet. Halfopen en halfgesloten betekenen hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de wetenschappelijke notatie van 45 000?",
        opties=[
            "4,5 maal 10 tot de vierde",
            "45 maal 10 tot de derde",
            "4,5 maal 10 tot de derde",
            "0,45 maal 10 tot de vijfde",
        ],
        antwoord=0,
        uitleg="In de wetenschappelijke notatie staat er één cijfer voor de komma, van 1 tot en met 9.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de wetenschappelijke notatie van 0,00072?",
        opties=[
            "7,2 maal 10 tot de macht min 4",
            "7,2 maal 10 tot de macht min 3",
            "72 maal 10 tot de macht min 5",
            "0,72 maal 10 tot de macht min 3",
        ],
        antwoord=0,
        uitleg="De komma moet vier plaatsen naar rechts om 7,2 te krijgen, dus de exponent is min 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze notaties is géén correcte wetenschappelijke notatie?",
        opties=[
            "12 maal 10 tot de derde",
            "1,2 maal 10 tot de vierde",
            "9,99 maal 10 tot de achtste",
            "3 maal 10 tot de macht min 6",
        ],
        antwoord=0,
        uitleg="Het getal vooraan moet tussen 1 en 10 liggen. 12 is te groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 3 maal 10 tot de vijfde als gewoon getal?",
        opties=["300 000", "30 000", "3 000 000", "350 000"],
        antwoord=0,
        uitleg="Vijf nullen achter de 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="De afstand aarde-zon is ongeveer 1,5 maal 10 tot de elfde meter. Hoeveel kilometer is dat?",
        opties=[
            "1,5 maal 10 tot de achtste",
            "1,5 maal 10 tot de tiende",
            "1,5 maal 10 tot de veertiende",
            "1,5 maal 10 tot de twaalfde",
        ],
        antwoord=0,
        uitleg="Een kilometer is duizend meter, dus je deelt door 10 tot de derde: de exponent daalt met 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruiken wetenschappers machten van tien?",
        opties=[
            "omdat heel grote en heel kleine getallen zo leesbaar en vergelijkbaar blijven",
            "omdat een rekenmachine anders geen komma kan weergeven",
            "omdat het verplicht is bij elke meting met een toestel",
            "omdat je zo geen afrondingsfouten meer kan maken",
        ],
        antwoord=0,
        uitleg="Bij 0,000000001 tel je nullen. Bij 10 tot de macht min 9 lees je het in één oogopslag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk interval hoort bij de oplossing van een ongelijkheid die zegt: x ligt tussen min 2 en 3, grenzen inbegrepen?",
        opties=["[−2, 3]", "]−2, 3[", "[−2, 3[", "]−2, 3]"],
        antwoord=0,
        uitleg="Allebei de grenzen erbij, dus allebei de haakjes naar binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een open interval horen de grenzen er niet bij.",
        antwoord=True,
        uitleg="De haakjes wijzen dan naar buiten, zoals in ]1, 4[.",
    ),
    dict(
        type="waarofniet",
        vraag="Het interval [3, 3] is leeg.",
        antwoord=False,
        uitleg="Het bevat precies één getal, namelijk 3 zelf. Het interval ]3, 3[ zou wel leeg zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="In de wetenschappelijke notatie staat er precies één cijfer voor de komma, van 1 tot en met 9.",
        antwoord=True,
        uitleg="Daarom is 45 maal 10 tot de derde niet correct genoteerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve exponent in de wetenschappelijke notatie betekent dat het getal negatief is.",
        antwoord=False,
        uitleg="Het betekent dat het getal klein is, tussen nul en één. Het teken van het getal staat vooraan.",
    ),
    dict(
        type="invultekst",
        vraag="Schrijf 6 200 000 in wetenschappelijke notatie. Typ bijvoorbeeld 3,4 x 10^5.",
        antwoord=["6,2 x 10^6"],
        uitleg="De komma schuift zes plaatsen naar links.",
    ),
    dict(
        type="invultekst",
        vraag="Schrijf 'alle getallen groter dan 5' als interval.",
        antwoord=["]5, +∞[", "]5,+∞[", "]5, oneindig["],
        uitleg="Strikt groter, dus de 5 hoort er niet bij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is 2,5 maal 10 tot de macht min 3 als gewoon getal?",
        antwoord=["0,0025"],
        uitleg="De komma schuift drie plaatsen naar links.",
    ),
]
