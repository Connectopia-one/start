# -*- coding: utf-8 -*-
"""Exponentiële en logaritmische functies, en groeimodellen.

Het onderdeel "Exponentiële functies" van de analysefiche G1. Dat valt daar in
twee stukken uiteen: de kenmerken van de functie zelf, in opgaven zonder
context, en de groeimodellen, uitdrukkelijk in opgaven mét context.

Deel 1 is de functie en haar grafiek, deel 2 zijn de groeimodellen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van de functie a tot de macht x?",
        opties=[
            "alle reële getallen",
            "alle positieve getallen",
            "alle getallen groter dan a",
            "alle gehele getallen",
        ],
        antwoord=0,
        uitleg="Je mag elke exponent nemen, ook negatieve en gebroken. Het bereik is wel beperkt: alleen positieve waarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van de functie a tot de macht x?",
        opties=[
            "de strikt positieve getallen",
            "alle reële getallen zonder meer",
            "de getallen groter dan of gelijk aan nul",
            "de getallen tussen nul en het grondtal a",
        ],
        antwoord=0,
        uitleg="Een macht van een positief grondtal wordt nooit nul of negatief, hoe klein de exponent ook is.",
    ),
    dict(
        type="invultekst",
        vraag="Elke grafiek van a tot de macht x gaat door hetzelfde punt op de verticale as. Welke y-waarde? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="Elk grondtal tot de macht nul is één, dus alle grafieken snijden de y-as in één.",
    ),
    dict(
        type="waarofniet",
        vraag="De functie a tot de macht x daalt als a tussen nul en één ligt.",
        antwoord=True,
        uitleg="Een half tot de macht drie is een achtste: hoe groter de exponent, hoe kleiner de uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke horizontale asymptoot heeft twee tot de macht x?",
        opties=[
            "de rechte y is nul",
            "de rechte y is één",
            "de rechte y is twee",
            "de rechte x is nul",
        ],
        antwoord=0,
        uitleg="Voor x naar min oneindig kruipen de waarden naar nul, zonder die ooit te bereiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke horizontale asymptoot heeft twee tot de macht x, plus vijf?",
        opties=[
            "de rechte y is vijf",
            "de rechte y is nul",
            "de rechte y is zeven",
            "de rechte x is vijf",
        ],
        antwoord=0,
        uitleg="De hele grafiek, en dus ook haar asymptoot, schuift vijf omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag="De grafiek van een exponentiële functie snijdt haar horizontale asymptoot.",
        antwoord=False,
        uitleg="Ze nadert die rechte wel oneindig dicht, maar bereikt haar nooit.",
    ),
    dict(
        type="invultekst",
        vraag="Neem drie tot de macht x. Hoeveel is de functiewaarde in twee? Schrijf het getal.",
        antwoord=["9", "negen"],
        uitleg="Drie in het kwadraat is negen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke transformatie brengt je van twee tot de macht x naar twee tot de macht x, min vier?",
        opties=[
            "vier eenheden naar beneden",
            "vier eenheden naar rechts",
            "vier eenheden naar links",
            "een verticale uitrekking met vier",
        ],
        antwoord=0,
        uitleg="De min vier staat buiten de macht, dus hij werkt op de functiewaarde. De asymptoot zakt mee naar y is min vier.",
    ),
    dict(
        type="waarofniet",
        vraag="Een exponentiële functie met positief grondtal kan negatieve waarden aannemen.",
        antwoord=False,
        uitleg="Niet zonder transformatie. Pas als je de grafiek spiegelt of ver genoeg laat zakken, komen er negatieve waarden bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Door welk tweede bijzonder punt gaat de grafiek van a tot de macht x altijd?",
        opties=[
            "het punt één en a",
            "het punt a en één",
            "het punt één en één",
            "het punt nul en a",
        ],
        antwoord=0,
        uitleg="Voor x gelijk aan één is de functiewaarde het grondtal zelf. Daarmee lees je a rechtstreeks van de grafiek af.",
    ),
    dict(
        type="invultekst",
        vraag="De grafiek van a tot de macht x gaat door het punt één en vijf. Wat is het grondtal? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="In x gelijk aan één is de functiewaarde net het grondtal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laat men het getal één niet toe als grondtal van een exponentiële functie?",
        opties=[
            "omdat de grafiek dan een horizontale rechte wordt",
            "omdat de functie dan nergens gedefinieerd zou zijn",
            "omdat de functie dan negatieve waarden aanneemt",
            "omdat de functie dan twee asymptoten zou krijgen",
        ],
        antwoord=0,
        uitleg="Eén tot eender welke macht blijft één. Dat is een constante functie en die groeit niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De exponentiële functie met grondtal e is stijgend.",
        antwoord=True,
        uitleg="e is ongeveer 2,718 en dus groter dan één, en bij een grondtal groter dan één stijgt de functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een tabel staat bij elke stap van één in x dezelfde vermenigvuldigingsfactor. Welk model past?",
        opties=[
            "een exponentieel model",
            "een lineair model",
            "een tweedegraadsmodel",
            "een periodiek model",
        ],
        antwoord=0,
        uitleg="Een vaste factor wijst op exponentiële groei. Een vaste optelling per stap wijst op lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je spiegelt de grafiek van twee tot de macht x om de horizontale as. Wat wordt het bereik?",
        opties=[
            "de strikt negatieve getallen",
            "de strikt positieve getallen",
            "alle reële getallen samen",
            "de getallen tussen min één en nul",
        ],
        antwoord=0,
        uitleg="Alle functiewaarden wisselen van teken, dus wat positief was wordt negatief.",
    ),
    dict(
        type="waarofniet",
        vraag="De logaritmische functie heeft een verticale asymptoot.",
        antwoord=True,
        uitleg="Voor x die naar nul kruipt, duikt de logaritme naar min oneindig. De y-as is dus een verticale asymptoot.",
    ),
    dict(
        type="invultekst",
        vraag="Het domein van de logaritmische functie bestaat uit alle getallen strikt groter dan welk getal? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Alleen strikt positieve argumenten hebben een logaritme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Door welk punt gaat de grafiek van de logaritmische functie altijd?",
        opties=[
            "het punt één en nul",
            "het punt nul en één",
            "het punt nul en nul",
            "het punt één en één",
        ],
        antwoord=0,
        uitleg="De logaritme van één is nul bij elk grondtal. Dat is het spiegelbeeld van het punt nul en één van de exponentiële functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe liggen de grafiek van de exponentiële functie en die van de logaritmische functie met hetzelfde grondtal ten opzichte van elkaar?",
        opties=[
            "ze zijn elkaars spiegelbeeld om de eerste bissectrice",
            "ze zijn elkaars spiegelbeeld om de horizontale as",
            "ze lopen evenwijdig op een vaste afstand van elkaar",
            "ze snijden elkaar in precies twee vaste punten",
        ],
        antwoord=0,
        uitleg="Het zijn elkaars inverse functies, en inverse functies spiegelen altijd om de rechte y is x.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een bedrag groeit met drie procent per jaar. Wat is de groeifactor per jaar?",
        opties=["1,03", "0,03", "3", "1,3"],
        antwoord=0,
        uitleg="Bij een toename van p procent is de groeifactor één plus p gedeeld door honderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hoeveelheid daalt met twintig procent per jaar. Wat is de groeifactor?",
        opties=["0,8", "1,2", "0,2", "min 0,8"],
        antwoord=0,
        uitleg="Er blijft tachtig procent over, dus je vermenigvuldigt met nul komma acht. Een groeifactor is nooit negatief.",
    ),
    dict(
        type="invultekst",
        vraag="Een model luidt: tweehonderd maal 1,05 tot de macht x. Wat is de beginwaarde? Schrijf het getal.",
        antwoord=["200", "tweehonderd"],
        uitleg="Voor x gelijk aan nul is de macht één, dus blijft de factor vooraan over.",
    ),
    dict(
        type="waarofniet",
        vraag="Een groeifactor kleiner dan één betekent dat de hoeveelheid afneemt.",
        antwoord=True,
        uitleg="Vermenigvuldigen met een getal tussen nul en één maakt kleiner. Bij precies één blijft alles gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groeifactor is 1,12 per jaar. Met hoeveel procent groeit de hoeveelheid per jaar?",
        opties=[
            "twaalf procent erbij",
            "honderd twaalf procent erbij",
            "twaalf procent eraf",
            "een komma twaalf procent erbij",
        ],
        antwoord=0,
        uitleg="Trek één af en vermenigvuldig met honderd. Nul komma twaalf is twaalf procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent de groeifactor per maand. Hoe bereken je de groeifactor per jaar?",
        opties=[
            "je verheft de maandfactor tot de macht twaalf",
            "je vermenigvuldigt de maandfactor met twaalf",
            "je telt twaalf keer de maandfactor bij elkaar op",
            "je deelt de maandfactor door het getal twaalf",
        ],
        antwoord=0,
        uitleg="Twaalf keer vermenigvuldigen met dezelfde factor is die factor tot de twaalfde macht. Optellen of maal twaalf hoort bij lineaire groei.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stijging met tien procent, gevolgd door een daling met tien procent, brengt je terug bij de beginwaarde.",
        antwoord=False,
        uitleg="Je vermenigvuldigt met 1,1 en daarna met 0,9, samen met 0,99. Je verliest dus één procent.",
    ),
    dict(
        type="invultekst",
        vraag="Een aantal gaat in één stap van honderd naar honderdvijftig. Wat is de groeifactor? Schrijf het getal.",
        antwoord=["1,5", "1.5"],
        uitleg="Honderdvijftig gedeeld door honderd is anderhalf, dus een toename van vijftig procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de verdubbelingstijd van een exponentieel groeiproces?",
        opties=[
            "de tijd die nodig is om twee keer zo groot te worden",
            "de tijd waarna de groeifactor zelf verdubbeld is",
            "het dubbel van de tijd die één stap in beslag neemt",
            "de tijd waarna het groeipercentage verdubbeld is",
        ],
        antwoord=0,
        uitleg="Bij exponentiële groei is die tijd altijd even lang, waar je ook begint te meten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een halveringstijd hoort bij een groeifactor kleiner dan één.",
        antwoord=True,
        uitleg="Halveren is afnemen, en afnemen betekent een factor tussen nul en één. Radioactief verval is het bekendste voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vorm heeft een lineair groeimodel?",
        opties=[
            "a maal x plus b",
            "b maal a tot de macht x",
            "a maal x in het kwadraat",
            "de logaritme van x plus b",
        ],
        antwoord=0,
        uitleg="Bij lineaire groei komt er elke tijdseenheid hetzelfde getal bij. Bij exponentiële groei vermenigvuldig je telkens.",
    ),
    dict(
        type="invultekst",
        vraag="Je zet geld op een rekening met vijf procent samengestelde intrest per jaar. Wat is de groeifactor? Schrijf het getal.",
        antwoord=["1,05", "1.05"],
        uitleg="Samengestelde intrest betekent dat je elk jaar met dezelfde factor vermenigvuldigt, dus hier met 1,05.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je na hoeveel jaar een bedrag met groeifactor 1,05 verdubbeld is?",
        opties=[
            "met een logaritme, want de onbekende staat in de exponent",
            "door het getal twee te delen door de groeifactor 1,05",
            "door honderd te delen door vijf, en dus twintig jaar",
            "door de vierkantswortel te trekken uit het getal twee",
        ],
        antwoord=0,
        uitleg="Je lost 1,05 tot de macht t is twee op, en dat gaat alleen met een logaritme. Honderd delen door het percentage is enkel een ruwe vuistregel.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij exponentiële groei komt er elke tijdseenheid evenveel bij.",
        antwoord=False,
        uitleg="Er komt elke tijdseenheid hetzelfde percentage bij, dus in absolute aantallen steeds meer. Een vaste toename hoort bij lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rij getallen past bij exponentiële groei?",
        opties=[
            "3, 6, 12, 24",
            "3, 6, 9, 12",
            "3, 5, 8, 12",
            "3, 9, 15, 21",
        ],
        antwoord=0,
        uitleg="Telkens maal twee. De tweede en de vierde rij hebben een vaste toename en zijn dus lineair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stof heeft een halveringstijd van vijf jaar. Hoeveel blijft er over na tien jaar?",
        opties=[
            "een kwart",
            "de helft",
            "een vijfde",
            "niets meer",
        ],
        antwoord=0,
        uitleg="Twee halveringstijden na elkaar: eerst de helft, dan de helft daarvan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuiver exponentieel model voorspelt een groei die nooit stopt.",
        antwoord=True,
        uitleg="Wiskundig blijft de functie stijgen. In werkelijkheid loopt groei vast op voedsel, ruimte of geld, dus het model geldt maar op een beperkt stuk.",
    ),
    dict(
        type="invultekst",
        vraag="De groeifactor per jaar is twee. Wat is de groeifactor per twee jaar? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="Twee keer verdubbelen is vermenigvuldigen met twee in het kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kies je een lineair model in plaats van een exponentieel?",
        opties=[
            "als de verandering per tijdseenheid even groot blijft",
            "als de verandering per tijdseenheid sneller en sneller gaat",
            "als de hoeveelheid na een tijd niet meer verandert",
            "als de hoeveelheid om de zoveel tijd verdubbelt",
        ],
        antwoord=0,
        uitleg="Een vast bedrag sparen per maand is lineair. Intrest op intrest is exponentieel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een groeimodel vaak een praktisch domein?",
        opties=[
            "omdat een negatieve tijd meestal geen betekenis heeft",
            "omdat de functie buiten dat domein niet bestaat",
            "omdat de groeifactor na een tijd negatief wordt",
            "omdat de grafiek anders geen asymptoot zou hebben",
        ],
        antwoord=0,
        uitleg="De exponentiële functie bestaat wiskundig voor elke x, maar in de context tel je pas vanaf het begin van de meting.",
    ),
]
