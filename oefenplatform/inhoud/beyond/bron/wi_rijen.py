# -*- coding: utf-8 -*-
"""Rijen en hun limiet.

Het laatste onderdeel van de analysefiche G1. De fiche koppelt rijen
uitdrukkelijk aan de functies van de vorige thema's: een rekenkundige rij
hoort bij lineaire groei en een eerstegraadsfunctie, een meetkundige rij bij
exponentiële groei.

Deel 1 zijn de twee soorten rijen, hun voorschriften en hun somformules.
Deel 2 zijn de limieten: convergentie, divergentie en de som van een
oneindige meetkundige rij.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een rekenkundige rij?",
        opties=[
            "een rij waarin je telkens hetzelfde getal optelt",
            "een rij waarin je telkens met hetzelfde getal vermenigvuldigt",
            "een rij waarin elke term het kwadraat is van de vorige",
            "een rij waarin de termen om beurten positief en negatief zijn",
        ],
        antwoord=0,
        uitleg="Dat vaste getal heet het verschil van de rij. Telkens vermenigvuldigen geeft een meetkundige rij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een meetkundige rij?",
        opties=[
            "een rij waarin je telkens met hetzelfde getal vermenigvuldigt",
            "een rij waarin je telkens hetzelfde getal optelt",
            "een rij waarin de termen de omtrek van figuren voorstellen",
            "een rij waarin elke term het gemiddelde van de buren is",
        ],
        antwoord=0,
        uitleg="Dat vaste getal heet de reden van de rij.",
    ),
    dict(
        type="invultekst",
        vraag="Neem de rij drie, zeven, elf, vijftien. Wat is het verschil? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="Elke term is vier meer dan de vorige.",
    ),
    dict(
        type="waarofniet",
        vraag="Een recursief voorschrift berekent elke term uit de vorige term.",
        antwoord=True,
        uitleg="Daarom heb je er ook altijd een beginterm bij nodig. Een expliciet voorschrift geeft de n-de term rechtstreeks.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt het expliciete voorschrift van een rekenkundige rij?",
        opties=[
            "de eerste term plus n min één, maal het verschil",
            "de eerste term plus n, maal het verschil van de rij",
            "de eerste term maal het verschil tot de macht n",
            "de eerste term plus het verschil, tot de macht n",
        ],
        antwoord=0,
        uitleg="Om bij de n-de term te komen, tel je het verschil n min één keer op bij de eerste term.",
    ),
    dict(
        type="meerkeuze",
        vraag="Neem de rij drie, zeven, elf. Wat is de tiende term?",
        opties=["negenendertig", "drieënveertig", "zevenendertig", "dertig"],
        antwoord=0,
        uitleg="Drie plus negen maal vier is negenendertig. Negen stappen, niet tien, want de eerste term staat er al.",
    ),
    dict(
        type="waarofniet",
        vraag="De rij twee, zes, achttien, vierenvijftig is een rekenkundige rij.",
        antwoord=False,
        uitleg="Het verschil groeit telkens, maar de factor blijft drie. Het is dus een meetkundige rij.",
    ),
    dict(
        type="invultekst",
        vraag="Neem de rij twee, zes, achttien, vierenvijftig. Wat is de reden? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="Elke term is drie keer de vorige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de som van de eerste n termen van een rekenkundige rij?",
        opties=[
            "n maal het gemiddelde van de eerste en de laatste term",
            "n maal het verschil van de eerste en de laatste term",
            "de eerste term maal n, plus het verschil maal n",
            "de laatste term maal n, gedeeld door het getal twee",
        ],
        antwoord=0,
        uitleg="Je legt de rij twee keer naast elkaar, een keer vooruit en een keer achteruit. Elk paar geeft dan dezelfde som.",
    ),
    dict(
        type="waarofniet",
        vraag="De punten van een rekenkundige rij liggen op een rechte.",
        antwoord=True,
        uitleg="Het verschil is de richtingscoëfficiënt. Daarom hoort een rekenkundige rij bij lineaire groei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Neem de rij twee, zes, achttien. Wat is de vijfde term?",
        opties=[
            "honderdtweeënzestig",
            "vierenvijftig",
            "tweehonderdzestien",
            "honderdacht",
        ],
        antwoord=0,
        uitleg="Twee maal drie tot de vierde is twee maal eenentachtig, dus honderdtweeënzestig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van de getallen één tot en met tien? Schrijf het getal.",
        antwoord=["55", "vijfenvijftig"],
        uitleg="Tien maal het gemiddelde van één en tien, dus tien maal vijf komma vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soort groei hoort bij een meetkundige rij?",
        opties=[
            "exponentiële groei",
            "lineaire groei",
            "kwadratische groei",
            "logaritmische groei",
        ],
        antwoord=0,
        uitleg="Een vaste factor per stap is net wat een exponentiële functie doet. Een vast verschil hoort bij lineaire groei.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meetkundige rij met reden één stijgt steeds sneller.",
        antwoord=False,
        uitleg="Met reden één blijft elke term gelijk aan de vorige. De rij is dan constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heb je nodig om de som van de eerste n termen van een meetkundige rij te berekenen?",
        opties=[
            "de eerste term, de reden en het aantal termen",
            "enkel de eerste en de laatste term van de rij",
            "enkel het verschil tussen twee opeenvolgende termen",
            "de reden en de limiet van de rij op oneindig",
        ],
        antwoord=0,
        uitleg="In de formule staat de reden tot de macht n, dus het aantal termen telt mee. De formule werkt niet als de reden één is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer daalt een rekenkundige rij?",
        opties=[
            "als het verschil negatief is",
            "als de eerste term negatief is",
            "als het verschil kleiner is dan één",
            "als het aantal termen oneven is",
        ],
        antwoord=0,
        uitleg="Alleen het teken van het verschil beslist. Een rij die begint bij min honderd met verschil drie stijgt gewoon.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een meetkundige rij met een negatieve reden wisselen de termen van teken.",
        antwoord=True,
        uitleg="Zo'n rij heet alternerend: om beurten positief en negatief.",
    ),
    dict(
        type="invultekst",
        vraag="Een rij heeft als voorschrift vier n min één. Wat is de eerste term? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="Vul n gelijk aan één in: vier min één is drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zet geld op een rekening met samengestelde intrest. Welke rij vormen de jaarlijkse saldo's?",
        opties=[
            "een meetkundige rij",
            "een rekenkundige rij",
            "een alternerende rij",
            "een rij zonder vast patroon",
        ],
        antwoord=0,
        uitleg="Elk jaar vermenigvuldig je met dezelfde groeifactor. Bij enkelvoudige intrest zou je elk jaar hetzelfde bedrag optellen, en dan is ze rekenkundig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verloopt een meetkundige rij met een reden groter dan één en een positieve eerste term?",
        opties=[
            "ze stijgt, met een toenemende stijging",
            "ze stijgt, met een afnemende stijging",
            "ze stijgt met telkens evenveel per stap",
            "ze daalt naar nul toe zonder die te halen",
        ],
        antwoord=0,
        uitleg="Elke stap wordt groter dan de vorige, want je vermenigvuldigt telkens een groter getal met dezelfde factor.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een rij convergeert?",
        opties=[
            "haar termen naderen een vast eindig getal",
            "haar termen worden steeds groter en groter",
            "haar termen wisselen voortdurend van teken",
            "haar termen zijn vanaf een bepaalde plaats gelijk",
        ],
        antwoord=0,
        uitleg="Dat getal is de limiet van de rij. Gaat ze naar oneindig of blijft ze springen, dan divergeert ze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de limiet van een meetkundige rij waarvan de reden tussen min één en één ligt?",
        opties=["nul", "één", "de eerste term", "oneindig"],
        antwoord=0,
        uitleg="Telkens met een getal kleiner dan één vermenigvuldigen maakt de termen almaar kleiner.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de limiet van de rij één gedeeld door n? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Hoe groter n, hoe kleiner de breuk. Ze wordt nooit nul, maar komt er onbeperkt dicht bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rekenkundige rij met verschil twee convergeert.",
        antwoord=False,
        uitleg="Ze blijft met twee per stap toenemen en gaat dus naar oneindig. Alleen een rekenkundige rij met verschil nul convergeert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een alternerende rij?",
        opties=[
            "een rij waarvan de termen om beurten positief en negatief zijn",
            "een rij waarvan de termen om beurten stijgen en dalen in waarde",
            "een rij die uit twee verschillende rijen is samengesteld",
            "een rij die om beurten geheel en gebroken is in haar termen",
        ],
        antwoord=0,
        uitleg="Je herkent ze aan een factor min één tot de macht n in het voorschrift.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de limiet van de rij min één tot de macht n?",
        opties=[
            "die bestaat niet, want de rij blijft springen",
            "de limiet is nul, want de termen heffen elkaar op",
            "de limiet is één, want dat is de grootste waarde",
            "de limiet is min één, want dat is de kleinste waarde",
        ],
        antwoord=0,
        uitleg="De termen blijven heen en weer gaan tussen min één en één en naderen dus geen enkel getal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een divergente rij kan naar plus oneindig gaan.",
        antwoord=True,
        uitleg="Divergent betekent alleen dat er geen eindige limiet is. Naar oneindig gaan of blijven springen zijn allebei vormen van divergentie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is één plus een half plus een vierde plus een achtste, en zo verder tot in het oneindige? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="Een meetkundige rij met eerste term één en reden een half. De som is één gedeeld door één min een half.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de som van een oneindige meetkundige rij?",
        opties=[
            "de eerste term gedeeld door één min de reden",
            "de eerste term gedeeld door de reden min één",
            "de eerste term vermenigvuldigd met de reden",
            "de reden gedeeld door één min de eerste term",
        ],
        antwoord=0,
        uitleg="De reden tot de macht n kruipt naar nul, dus uit de gewone somformule blijft dat over.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke oneindige meetkundige rij heeft een eindige som.",
        antwoord=False,
        uitleg="Alleen als de absolute waarde van de reden kleiner is dan één. Bij reden twee groeit de som onbeperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Onder welke voorwaarde bestaat de som van een oneindige meetkundige rij?",
        opties=[
            "de absolute waarde van de reden is kleiner dan één",
            "de absolute waarde van de reden is groter dan één",
            "de eerste term van de rij is kleiner dan één",
            "het aantal termen van de rij is eindig en gekend",
        ],
        antwoord=0,
        uitleg="Pas dan worden de termen zo snel klein dat de som naar een vast getal kruipt.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de limiet van de rij twee n plus één, gedeeld door n? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="Splits op in twee plus één op n. De tweede term kruipt naar nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de somrij van een rij?",
        opties=[
            "de rij van de som van de eerste n termen",
            "de rij van de verschillen tussen de termen",
            "de rij van alle termen bij elkaar opgeteld",
            "de rij van de gemiddelden van de termen",
        ],
        antwoord=0,
        uitleg="Haar n-de term is de som tot en met de n-de term van de oorspronkelijke rij.",
    ),
    dict(
        type="waarofniet",
        vraag="De somrij van een meetkundige rij met reden een half convergeert.",
        antwoord=True,
        uitleg="De absolute waarde van de reden is kleiner dan één, dus de som nadert een vast getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de limiet van twee tot de macht n?",
        opties=[
            "plus oneindig",
            "nul",
            "twee",
            "die bestaat niet, want de rij springt",
        ],
        antwoord=0,
        uitleg="Bij een reden groter dan één groeien de termen onbeperkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rekenregel geldt voor de limiet van een som van twee convergente rijen?",
        opties=[
            "de limiet van de som is de som van de limieten",
            "de limiet van de som is het product van de limieten",
            "de limiet van de som is de grootste van de limieten",
            "de limiet van de som bestaat in dat geval nooit",
        ],
        antwoord=0,
        uitleg="Dezelfde rekenregels als bij limieten van functies, zolang beide limieten eindig zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Het getal nul komma negen negen negen, met oneindig veel negens, is gelijk aan één.",
        antwoord=True,
        uitleg="Het is de som van een meetkundige rij met eerste term negen tienden en reden een tiende, en die som is precies één.",
    ),
    dict(
        type="invultekst",
        vraag="Neem de rij één, een derde, een negende. Wat is de reden? Schrijf ze als breuk.",
        antwoord=["1/3"],
        uitleg="Elke term is een derde van de vorige.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal stuitert telkens tot zeventig procent van de vorige hoogte. Wat kan je berekenen?",
        opties=[
            "de totale afgelegde hoogte, want de reden ligt onder één",
            "niets, want de bal blijft oneindig lang stuiteren",
            "enkel de hoogte van de eerste tien sprongen",
            "de totale hoogte, maar enkel als je stopt bij één meter",
        ],
        antwoord=0,
        uitleg="Nul komma zeven ligt tussen nul en één, dus de oneindige som bestaat. Oneindig veel sprongen kunnen samen een eindige hoogte geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom spreek je bij een rij alleen over de limiet op oneindig?",
        opties=[
            "omdat een rij alleen in de natuurlijke getallen gedefinieerd is",
            "omdat een rij altijd uit oneindig veel losse termen bestaat",
            "omdat een rij nooit een eindige limiet kan hebben",
            "omdat een rij geen grafiek met een kromme oplevert",
        ],
        antwoord=0,
        uitleg="Er zijn geen tussenwaarden om naartoe te kruipen: tussen de derde en de vierde term ligt niets. Alleen n die onbeperkt groeit heeft zin.",
    ),
]
