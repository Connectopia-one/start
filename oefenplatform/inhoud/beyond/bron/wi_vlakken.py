# -*- coding: utf-8 -*-
"""Rechten en vlakken in de ruimte.

Het tweede stuk van het onderdeel "Analytische ruimtemeetkunde" van fiche G3.
De vectoren uit het vorige thema worden hier vergelijkingen, en met die
vergelijkingen ga je ligging, afstand en hoek na.

Deel 1 zijn de vergelijkingen zelf: vectorieel, parametrisch en cartesisch,
voor een rechte en voor een vlak, met de drie bij drie determinant.
Deel 2 is de onderlinge ligging van rechten en vlakken, en de afstanden en
hoeken die daarbij horen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat heb je nodig om de vergelijking van een rechte in de ruimte op te stellen?",
        opties=[
            "een punt en een richtingsvector",
            "een punt en een normaalvector van die rechte",
            "twee richtingsvectoren die niet evenwijdig zijn",
            "drie punten die niet op één rechte liggen",
        ],
        antwoord=0,
        uitleg="Het punt zegt waar ze ligt, de richtingsvector welke kant ze op loopt. Twee punten volstaan ook, want daar haal je de richtingsvector uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de rol van de parameter in een parametrische vergelijking?",
        opties=[
            "elke waarde ervan geeft een ander punt van de rechte",
            "ze geeft de lengte aan van de richtingsvector zelf",
            "ze geeft de hoek aan die de rechte met de assen maakt",
            "ze bepaalt het aantal snijpunten met de drie assen",
        ],
        antwoord=0,
        uitleg="Laat je de parameter alle reële waarden doorlopen, dan krijg je de hele rechte.",
    ),
    dict(
        type="invultekst",
        vraag="Uit hoeveel parametrische vergelijkingen bestaat de beschrijving van een rechte in de ruimte? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Eén per coördinaat, en alle drie met dezelfde parameter erin.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte in de ruimte heeft één cartesische vergelijking.",
        antwoord=False,
        uitleg="Ze heeft er twee: een rechte in de ruimte is de doorsnede van twee vlakken. In het vlak is het er wel maar één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de cartesische vergelijking van een vlak eruit?",
        opties=[
            "a maal x plus b maal y plus c maal z plus d is nul",
            "y is gelijk aan a maal x plus b, met twee onbekenden",
            "x in het kwadraat plus y in het kwadraat is gelijk aan r in het kwadraat",
            "x is gelijk aan a, y is gelijk aan b, z is gelijk aan c",
        ],
        antwoord=0,
        uitleg="Eén vergelijking van de eerste graad in drie onbekenden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je rechtstreeks af uit de coëfficiënten van x, y en z in die vergelijking?",
        opties=[
            "een normaalvector van het vlak",
            "een richtingsvector die in het vlak ligt",
            "het punt waar het vlak de z-as snijdt",
            "de afstand van het vlak tot de oorsprong",
        ],
        antwoord=0,
        uitleg="De drie coëfficiënten zijn precies de coördinaten van een vector die loodrecht op het vlak staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vlak ligt vast door één punt en twee richtingsvectoren die niet evenwijdig zijn.",
        antwoord=True,
        uitleg="Zijn de twee richtingsvectoren wel evenwijdig, dan krijg je maar een rechte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel parameters staan er in de parametrische vergelijkingen van een vlak? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="Eén per richtingsvector. Een rechte heeft er maar één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe stel je met een drie bij drie determinant de cartesische vergelijking van een vlak op?",
        opties=[
            "je stelt de determinant gelijk aan nul",
            "je stelt de determinant gelijk aan één",
            "je berekent de determinant en deelt door drie",
            "je neemt de determinant van de normaalvector alleen",
        ],
        antwoord=0,
        uitleg="In de determinant staan de verbindingsvector naar een onbekend punt en de twee richtingsvectoren. Nul betekent dat ze in één vlak liggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Drie punten die op eenzelfde rechte liggen, bepalen samen één vlak.",
        antwoord=False,
        uitleg="Door zo'n rechte gaan oneindig veel vlakken. De drie punten mogen niet op één rechte liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je van de parametrische naar de cartesische vergelijkingen van een rechte?",
        opties=[
            "je werkt de parameter weg uit de vergelijkingen",
            "je vult voor de parameter het getal nul in",
            "je telt de drie vergelijkingen bij elkaar op",
            "je berekent de determinant van de coëfficiënten",
        ],
        antwoord=0,
        uitleg="Je drukt de parameter uit in één vergelijking en vult die in de twee andere in. Er blijven twee vergelijkingen over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel punten die niet op eenzelfde rechte liggen, bepalen één vlak? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Daarom staat een tafel met drie poten nooit te wiebelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de cartesische vergelijking van het vlak door de x-as en de y-as?",
        opties=[
            "z is gelijk aan nul",
            "x is gelijk aan nul",
            "x plus y is gelijk aan nul",
            "x plus y plus z is gelijk aan nul",
        ],
        antwoord=0,
        uitleg="Alle punten van dat vlak hebben derde coördinaat nul. De z-as is er de normaal van.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte heeft oneindig veel richtingsvectoren.",
        antwoord=True,
        uitleg="Elk veelvoud van een richtingsvector is er ook een, behalve de nulvector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe controleer je of een punt op een rechte ligt?",
        opties=[
            "je vult zijn coördinaten in de vergelijkingen in",
            "je berekent de afstand van dat punt tot de oorsprong",
            "je vergelijkt zijn coördinaten met de richtingsvector",
            "je telt zijn coördinaten op en kijkt of je nul krijgt",
        ],
        antwoord=0,
        uitleg="Bij de parametrische vorm moet er voor alle drie dezelfde parameterwaarde uitkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een punt van een vlak en een normaalvector ervan. Wat kan je opstellen?",
        opties=[
            "de cartesische vergelijking van dat vlak",
            "enkel de parametrische vergelijkingen ervan",
            "niets, want je hebt twee richtingsvectoren nodig",
            "enkel de vectoriële vergelijking van dat vlak",
        ],
        antwoord=0,
        uitleg="De normaalvector geeft de coëfficiënten, het punt bepaalt de laatste term.",
    ),
    dict(
        type="waarofniet",
        vraag="In het vlak heeft een rechte precies één cartesische vergelijking.",
        antwoord=True,
        uitleg="Daar is het a maal x plus b maal y plus c is nul. Pas in de ruimte heb je er twee nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Een vlak heeft als vergelijking twee x min drie y plus z min vijf is nul. Wat is de eerste coördinaat van een normaalvector? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="De coëfficiënten van x, y en z zijn samen de normaalvector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stel je die drie bij drie determinant gelijk aan nul?",
        opties=[
            "omdat de drie vectoren dan in eenzelfde vlak liggen",
            "omdat de drie vectoren dan loodrecht op elkaar staan",
            "omdat de drie vectoren dan allemaal even lang zijn",
            "omdat het vlak dan door de oorsprong moet gaan",
        ],
        antwoord=0,
        uitleg="Een determinant die niet nul is, betekent dat de drie vectoren de hele ruimte opspannen. Precies dat mag niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt de cartesische vergelijking van een vlak en wil de parametrische. Hoe pak je dat aan?",
        opties=[
            "je zoekt een punt en twee richtingsvectoren van het vlak",
            "je zoekt de normaalvector en gebruikt die als parameter",
            "je stelt elke coördinaat gelijk aan een eigen parameter",
            "je berekent de determinant van de drie coëfficiënten",
        ],
        antwoord=0,
        uitleg="Twee van de drie onbekenden mag je vrij kiezen. Die twee vrijheidsgraden worden je twee parameters.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke onderlinge liggingen kunnen twee rechten in de ruimte hebben?",
        opties=[
            "samenvallend, evenwijdig, snijdend of kruisend",
            "enkel evenwijdig of snijdend, meer bestaat er niet",
            "samenvallend, snijdend of loodrecht op elkaar",
            "evenwijdig, loodrecht of met een scherpe hoek",
        ],
        antwoord=0,
        uitleg="Kruisend bestaat alleen in de ruimte: in het vlak snijden twee niet-evenwijdige rechten elkaar altijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn kruisende rechten?",
        opties=[
            "rechten die niet evenwijdig zijn en toch geen snijpunt hebben",
            "rechten die elkaar in precies één punt snijden in de ruimte",
            "rechten die loodrecht op elkaar staan zonder elkaar te raken",
            "rechten die evenwijdig lopen maar niet samenvallen",
        ],
        antwoord=0,
        uitleg="Ze liggen niet in eenzelfde vlak. Denk aan twee wegen boven elkaar met een brug ertussen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel mogelijke onderlinge liggingen heeft een rechte ten opzichte van een vlak? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Ze ligt in het vlak, ze is er evenwijdig mee zonder erin te liggen, of ze snijdt het.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee rechten in de ruimte die elkaar niet snijden, zijn evenwijdig.",
        antwoord=False,
        uitleg="Ze kunnen ook kruisen. In het vlak zou het wel kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je na of twee vlakken evenwijdig zijn?",
        opties=[
            "je kijkt of hun normaalvectoren veelvouden van elkaar zijn",
            "je kijkt of hun normaalvectoren loodrecht op elkaar staan",
            "je berekent het scalair product van hun normaalvectoren",
            "je vergelijkt de laatste term van beide vergelijkingen",
        ],
        antwoord=0,
        uitleg="Dezelfde richting loodrecht erop betekent dezelfde stand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee vlakken zijn evenwijdig. Wanneer vallen ze samen?",
        opties=[
            "als je de ene vergelijking uit de andere kan vermenigvuldigen",
            "als hun twee normaalvectoren precies even lang zijn geworden",
            "als hun laatste termen allebei gelijk zijn aan nul",
            "als ze allebei door de oorsprong van het stelsel gaan",
        ],
        antwoord=0,
        uitleg="Dan is het twee keer hetzelfde vlak, enkel anders opgeschreven. Anders liggen ze er netjes naast.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee vlakken die niet evenwijdig zijn, snijden elkaar volgens een rechte.",
        antwoord=True,
        uitleg="Nooit in één punt: de doorsnede van twee verschillende vlakken is altijd een rechte of niets.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de afstand tussen twee samenvallende vlakken? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg="Het is hetzelfde vlak, dus er zit niets tussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de hoek tussen twee vlakken?",
        opties=[
            "als de hoek tussen hun normaalvectoren",
            "als de hoek tussen hun twee richtingsvectoren",
            "als de som van hun hoeken met het grondvlak",
            "als het verschil van hun laatste twee termen",
        ],
        antwoord=0,
        uitleg="Je neemt de scherpe hoek van de twee die je zo krijgt.",
    ),
    dict(
        type="waarofniet",
        vraag="De hoek tussen twee rechten vind je uit het scalair product van hun richtingsvectoren.",
        antwoord=True,
        uitleg="Ook bij kruisende rechten, al snijden ze elkaar dan niet: de hoek hangt enkel van de richtingen af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de afstand van een punt tot een vlak?",
        opties=[
            "langs de loodlijn uit dat punt op het vlak",
            "langs de kortste zijde van het vlak naar dat punt",
            "als het verschil van hun twee normaalvectoren",
            "als de afstand van dat punt tot de oorsprong",
        ],
        antwoord=0,
        uitleg="De afstand is altijd de kortste, en die loopt loodrecht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de afstand tussen twee snijdende rechten? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg="Ze hebben een punt gemeen, dus de kortste afstand is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer behoort een rechte volledig tot een vlak?",
        opties=[
            "als twee van haar punten in het vlak liggen",
            "als haar richtingsvector gelijk is aan de normaalvector",
            "als ze het vlak in precies één punt snijdt",
            "als ze loodrecht op de normaalvector van het vlak staat",
        ],
        antwoord=0,
        uitleg="Twee punten volstaan. Enkel loodrecht op de normaalvector staan maakt haar evenwijdig, meer niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee evenwijdige rechten liggen altijd in eenzelfde vlak.",
        antwoord=True,
        uitleg="Door twee evenwijdige rechten gaat precies één vlak. Bij kruisende rechten lukt dat net niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je na of een rechte evenwijdig is met een vlak?",
        opties=[
            "je kijkt of haar richtingsvector loodrecht op de normaalvector staat",
            "je kijkt of haar richtingsvector evenwijdig met de normaalvector is",
            "je berekent de afstand van de rechte tot de oorsprong",
            "je vult een punt van het vlak in de rechte in",
        ],
        antwoord=0,
        uitleg="Het scalair product moet nul zijn. Ligt er dan ook nog een punt van de rechte in het vlak, dan ligt ze er helemaal in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de afstand tussen twee evenwijdige vlakken?",
        opties=[
            "je neemt een punt van het ene en zijn afstand tot het andere",
            "je neemt het verschil van hun twee normaalvectoren",
            "je neemt de afstand van beide vlakken tot de oorsprong",
            "je neemt het midden tussen de twee vlakken in de ruimte",
        ],
        antwoord=0,
        uitleg="Welk punt je kiest maakt niet uit: bij evenwijdige vlakken is die afstand overal dezelfde.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee kruisende rechten liggen in eenzelfde vlak.",
        antwoord=False,
        uitleg="Net niet, en dat is precies wat kruisend betekent. Door twee kruisende rechten gaat geen enkel vlak.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de hoek tussen twee evenwijdige vlakken, in graden? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg="Hun normaalvectoren wijzen dezelfde kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer staat een rechte loodrecht op een vlak?",
        opties=[
            "als haar richtingsvector evenwijdig is met de normaalvector",
            "als haar richtingsvector loodrecht op de normaalvector staat",
            "als ze het vlak snijdt in een punt van de x-as",
            "als ze evenwijdig loopt met een zijde van dat vlak",
        ],
        antwoord=0,
        uitleg="De normaalvector staat zelf al loodrecht op het vlak, dus de rechte moet zijn richting volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hellend dakvlak en de verticale gevel eronder. Wat is de hoek tussen die twee vlakken?",
        opties=[
            "de hoek tussen hun normaalvectoren, als scherpe hoek genomen",
            "de hoek die het dak maakt met de horizontale grond eronder",
            "de som van de hellingshoek en negentig graden",
            "altijd negentig graden, want een gevel staat recht",
        ],
        antwoord=0,
        uitleg="Je stelt beide vlakken op met hun vergelijking en rekent met de normaalvectoren. De hellingshoek met de grond is een andere hoek.",
    ),
]
