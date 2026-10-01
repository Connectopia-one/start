# -*- coding: utf-8 -*-
"""Machtswortels, machten met rationale exponent en logaritmen.

Het eerste onderdeel van de analysefiche G1. Het is rekengereedschap: zonder
de rekenregels hieronder kan je de exponentiële en logaritmische functies van
de latere thema's niet aan.

Deel 1 is machten en n-de machtswortels, deel 2 is de logaritme.

Alles staat voluit in woorden geschreven, zonder wiskundige symbolen, want het
oefenplatform toont de vraagtekst als gewone tekst.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke andere schrijfwijze heeft a tot de macht één derde?",
        opties=[
            "de derdemachtswortel uit a",
            "het getal a vermenigvuldigd met drie",
            "het getal a gedeeld door het getal drie",
            "het getal a tot de derde macht verheven",
        ],
        antwoord=0,
        uitleg="Een macht met exponent één op n is per afspraak de n-de machtswortel. Dus a tot de macht één derde is de derdemachtswortel uit a.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is acht tot de macht twee derde?",
        opties=["vier", "zestien", "zes", "twaalf"],
        antwoord=0,
        uitleg="Eerst de derdemachtswortel uit acht, dat is twee. Daarna kwadrateren geeft vier.",
    ),
    dict(
        type="waarofniet",
        vraag="De n-de machtswortel uit een negatief getal bestaat in de reële getallen alleen als n oneven is.",
        antwoord=True,
        uitleg="Een even macht van een reëel getal is nooit negatief, dus de vierkantswortel of de vierdemachtswortel uit een negatief getal bestaat niet in R. De derdemachtswortel uit min acht bestaat wel: min twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vermenigvuldigt twee machten met hetzelfde grondtal. Wat doe je met de exponenten?",
        opties=[
            "je telt ze bij elkaar op",
            "je vermenigvuldigt ze met elkaar",
            "je trekt de kleinste van de grootste af",
            "je deelt de ene door de andere",
        ],
        antwoord=0,
        uitleg="a tot de macht m maal a tot de macht n is a tot de macht m plus n. Optellen dus. Bij delen trek je af, bij een macht van een macht vermenigvuldig je.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is zestien tot de macht een half? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="Exponent een half betekent de vierkantswortel. De vierkantswortel uit zestien is vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is a tot de macht min n gelijk?",
        opties=[
            "één gedeeld door a tot de macht n",
            "min één keer a tot de macht n",
            "de n-de machtswortel uit min a",
            "nul min het getal a tot de macht n",
        ],
        antwoord=0,
        uitleg="Een negatieve exponent betekent omkeren, niet van teken veranderen. Twee tot de macht min drie is dus één achtste, niet min acht.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk getal behalve nul tot de macht nul is gelijk aan één.",
        antwoord=True,
        uitleg="Dat volgt uit de rekenregel voor delen: a tot de macht n gedeeld door a tot de macht n is enerzijds één en anderzijds a tot de macht nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je de vierkantswortel uit vijftig zo eenvoudig mogelijk?",
        opties=[
            "vijf keer de vierkantswortel uit twee",
            "twee keer de vierkantswortel uit vijf",
            "tien keer de vierkantswortel uit vijf",
            "vijf keer de vierkantswortel uit tien",
        ],
        antwoord=0,
        uitleg="Vijftig is vijfentwintig maal twee. De wortel uit vijfentwintig is vijf en komt buiten het wortelteken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is zevenentwintig tot de macht twee derde? Schrijf het getal.",
        antwoord=["9", "negen"],
        uitleg="De derdemachtswortel uit zevenentwintig is drie, en drie in het kwadraat is negen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is het product a maal b, samen tot de macht n verheven, gelijk?",
        opties=[
            "a tot de macht n maal b tot de macht n",
            "a tot de macht n plus b tot de macht n",
            "het product a maal b maal het getal n",
            "a tot de macht n gedeeld door b tot de n",
        ],
        antwoord=0,
        uitleg="Een macht verdeelt zich over een product en over een quotiënt, maar nooit over een som.",
    ),
    dict(
        type="waarofniet",
        vraag="De vierkantswortel uit a plus b is gelijk aan de vierkantswortel uit a plus de vierkantswortel uit b.",
        antwoord=False,
        uitleg="Probeer het met negen en zestien: de wortel uit vijfentwintig is vijf, maar drie plus vier is zeven. Een wortel verdeelt zich niet over een som.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is a tot de macht m op n gelijk?",
        opties=[
            "de n-de machtswortel uit a tot de macht m",
            "de m-de machtswortel uit a tot de macht n",
            "het quotiënt van a tot de m en a tot de n",
            "het getal a maal het quotiënt van m en n",
        ],
        antwoord=0,
        uitleg="De noemer van de exponent wordt de wortelexponent, de teller blijft de macht. Zo is acht tot twee derde de derdemachtswortel uit vierenzestig, dus vier.",
    ),
    dict(
        type="invultekst",
        vraag="Schrijf twee tot de macht min drie als een breuk.",
        antwoord=["1/8"],
        uitleg="Twee tot de macht min drie is één gedeeld door twee tot de derde, dus één achtste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verheft a kwadraat tot de derde macht. Wat krijg je?",
        opties=[
            "a tot de zesde macht",
            "a tot de vijfde macht",
            "a tot de achtste macht",
            "a tot de negende macht",
        ],
        antwoord=0,
        uitleg="Bij een macht van een macht vermenigvuldig je de exponenten: twee maal drie is zes.",
    ),
    dict(
        type="waarofniet",
        vraag="Vier tot de macht drie halven is gelijk aan zes.",
        antwoord=False,
        uitleg="De wortel uit vier is twee, en twee tot de derde is acht. Het antwoord is dus acht, niet zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de vijfdemachtswortel uit tweeëndertig?",
        opties=["twee", "vier", "zes", "acht"],
        antwoord=0,
        uitleg="Twee tot de vijfde is tweeëndertig, dus de vijfdemachtswortel is twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je maakt de noemer rationaal in de breuk één gedeeld door de wortel uit drie. Wat krijg je?",
        opties=[
            "de wortel uit drie gedeeld door drie",
            "drie gedeeld door de wortel uit drie",
            "de wortel uit drie maal het getal drie",
            "één gedeeld door het getal drie",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt teller en noemer met de wortel uit drie. De noemer wordt dan drie.",
    ),
    dict(
        type="waarofniet",
        vraag="De derdemachtswortel uit min acht is gelijk aan min twee.",
        antwoord=True,
        uitleg="Min twee tot de derde is min acht. Bij een oneven wortelexponent mag het grondtal negatief zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is vierenzestig tot de macht één zesde? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="Twee tot de zesde is vierenzestig, dus de zesdemachtswortel uit vierenzestig is twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor welke grondtallen is een macht met een rationale exponent zonder voorbehoud gedefinieerd?",
        opties=[
            "voor grondtallen groter dan of gelijk aan nul",
            "voor alle reële getallen zonder uitzondering",
            "voor alle gehele getallen behalve het getal nul",
            "enkel voor grondtallen die kleiner zijn dan nul",
        ],
        antwoord=0,
        uitleg="Bij een negatief grondtal zou dezelfde exponent, anders geschreven, twee verschillende uitkomsten geven. Daarom blijft een rationale exponent beperkt tot niet-negatieve grondtallen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent de logaritme van x met grondtal a?",
        opties=[
            "de exponent waartoe je a verheft om x te krijgen",
            "het getal waarmee je a vermenigvuldigt om x te krijgen",
            "de wortelexponent waarmee je uit x het getal a trekt",
            "het aantal keren dat het getal a in het getal x past",
        ],
        antwoord=0,
        uitleg="Een logaritme is een exponent. De logaritme van acht met grondtal twee is drie, want twee tot de derde is acht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is de logaritme van een product gelijk, bij hetzelfde grondtal?",
        opties=[
            "de som van de twee logaritmen",
            "het product van de twee logaritmen",
            "het verschil van de twee logaritmen",
            "het quotiënt van de twee logaritmen",
        ],
        antwoord=0,
        uitleg="Omdat machten bij vermenigvuldigen hun exponenten optellen, worden logaritmen van een product opgeteld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de logaritme van acht met grondtal twee? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="Twee tot de derde is acht.",
    ),
    dict(
        type="waarofniet",
        vraag="De logaritme van honderd met grondtal tien is gelijk aan twee.",
        antwoord=True,
        uitleg="Tien in het kwadraat is honderd. Als er geen grondtal bij staat, bedoelt men grondtal tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk grondtal hoort bij de natuurlijke logaritme, geschreven als ln?",
        opties=[
            "het getal e",
            "het getal tien",
            "het getal twee",
            "het getal één",
        ],
        antwoord=0,
        uitleg="De natuurlijke logaritme heeft als grondtal het getal e, ongeveer 2,718. Eén kan nooit een grondtal zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de natuurlijke logaritme van e? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="e tot de eerste macht is e, dus de natuurlijke logaritme van e is één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is de logaritme van x gedeeld door y gelijk, bij hetzelfde grondtal?",
        opties=[
            "de logaritme van x min de logaritme van y",
            "de logaritme van x maal de logaritme van y",
            "de logaritme van x plus de logaritme van y",
            "de logaritme van x gedeeld door die van y",
        ],
        antwoord=0,
        uitleg="Delen van machten trekt exponenten af, dus wordt de logaritme van een quotiënt een verschil.",
    ),
    dict(
        type="waarofniet",
        vraag="De logaritme van a plus b is gelijk aan de logaritme van a plus de logaritme van b.",
        antwoord=False,
        uitleg="Die rekenregel geldt voor een product, niet voor een som. De logaritme van een som kan je niet splitsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is de logaritme van x tot de macht n gelijk?",
        opties=[
            "n maal de logaritme van x",
            "de logaritme van x tot de macht n",
            "de logaritme van x gedeeld door n",
            "de logaritme van x plus het getal n",
        ],
        antwoord=0,
        uitleg="De exponent komt vooraan te staan. Dat is net de regel waarmee je een onbekende uit een exponent haalt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de logaritme van eenentachtig met grondtal drie? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="Drie tot de vierde is eenentachtig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rekenapp kent alleen log en ln. Hoe bereken je de logaritme van x met grondtal a?",
        opties=[
            "de logaritme van x gedeeld door die van a",
            "de logaritme van x min de logaritme van a",
            "de logaritme van x maal de logaritme van a",
            "de logaritme van a gedeeld door die van x",
        ],
        antwoord=0,
        uitleg="Dat is het veranderen van grondtal: je deelt twee logaritmen met hetzelfde nieuwe grondtal door elkaar. Let op de volgorde.",
    ),
    dict(
        type="waarofniet",
        vraag="De logaritme van een negatief getal bestaat niet in de reële getallen.",
        antwoord=True,
        uitleg="Een macht van een positief grondtal is altijd positief, dus geen enkele exponent geeft een negatieve uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke waarde benadert het getal e het best?",
        opties=["2,718", "3,142", "1,618", "2,236"],
        antwoord=0,
        uitleg="e is ongeveer 2,718. De tweede is pi, de derde de gulden snede en de vierde de wortel uit vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost de vergelijking twee tot de macht x is tweeëndertig op. Wat is x?",
        opties=["vijf", "vier", "zes", "zestien"],
        antwoord=0,
        uitleg="Tweeëndertig is twee tot de vijfde, dus x is vijf. Je kan het ook schrijven als de logaritme van tweeëndertig met grondtal twee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de logaritme van één met grondtal vijf? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Vijf tot de macht nul is één, dus de logaritme van één is nul. Dat geldt bij elk toegelaten grondtal.",
    ),
    dict(
        type="waarofniet",
        vraag="De logaritme van één is nul, welk toegelaten grondtal je ook kiest.",
        antwoord=True,
        uitleg="Elk grondtal tot de macht nul geeft één, dus de logaritme van één is altijd nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is tien tot de macht de logaritme van zeven met grondtal tien?",
        opties=["zeven", "tien", "één", "zeventig"],
        antwoord=0,
        uitleg="De logaritme met grondtal tien en de macht van tien heffen elkaar op. Je houdt het getal zelf over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke vergelijking heb je een logaritme nodig om ze op te lossen?",
        opties=[
            "drie tot de macht x is gelijk aan twintig",
            "drie maal x in het kwadraat is gelijk aan twaalf",
            "drie maal x min vijf is gelijk aan zestien",
            "x in het kwadraat min negen is gelijk aan nul",
        ],
        antwoord=0,
        uitleg="Alleen bij de eerste staat de onbekende in de exponent. Een logaritme is net het gereedschap dat ze daar weghaalt.",
    ),
    dict(
        type="waarofniet",
        vraag="De logaritme van zestien met grondtal twee is gelijk aan acht.",
        antwoord=False,
        uitleg="Twee tot de vierde is zestien, dus de logaritme is vier. Acht zou betekenen dat twee tot de achtste zestien is, en dat is tweehonderdzesenvijftig.",
    ),
    dict(
        type="invultekst",
        vraag="Tien tot welke macht is nul komma nul nul één? Schrijf het getal.",
        antwoord=["-3", "min 3"],
        uitleg="Nul komma nul nul één is één duizendste, dus tien tot de macht min drie.",
    ),
]
