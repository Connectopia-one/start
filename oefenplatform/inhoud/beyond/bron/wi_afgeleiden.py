# -*- coding: utf-8 -*-
"""Afgeleiden en het verloop van een functie.

Het tweede stuk van het onderdeel "Limieten en afgeleiden" van de
analysefiche G1. De fiche bouwt het begrip in drie stappen op: eerst de
gemiddelde verandering, dan de afgeleide in een punt als richtingscoëfficiënt
van de raaklijn, en pas daarna de afgeleide functie met haar rekenregels.

Deel 1 is de afgeleide zelf en het rekenwerk.
Deel 2 is het verloop van een functie met de eerste en de tweede afgeleide,
en de extremumproblemen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat berekent een differentiequotiënt?",
        opties=[
            "de gemiddelde verandering over een interval",
            "de verandering op één welbepaald ogenblik",
            "het verschil tussen twee functiewaarden",
            "de oppervlakte onder de grafiek van f",
        ],
        antwoord=0,
        uitleg="Je deelt het verschil in functiewaarden door het verschil in x. Enkel het verschil van de functiewaarden is de teller alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de afgeleide van een functie in een punt meetkundig voor?",
        opties=[
            "de richtingscoëfficiënt van de raaklijn in dat punt",
            "de hoogte van de grafiek in dat welbepaalde punt",
            "de afstand van dat punt tot de horizontale as",
            "de oppervlakte tussen de grafiek en de x-as",
        ],
        antwoord=0,
        uitleg="De raaklijn is de rechte die de kromme in dat punt het best benadert, en haar helling is de afgeleide.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x kwadraat. Hoeveel is de afgeleide in x gelijk aan drie? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg="De afgeleide functie is twee x, en twee maal drie is zes.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide in een punt is de limiet van het differentiequotiënt.",
        antwoord=True,
        uitleg="Je laat het tweede punt naar het eerste kruipen. De koorde wordt dan de raaklijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de afgeleide van x tot de macht n?",
        opties=[
            "n maal x tot de macht n min één",
            "n maal x tot de macht n plus één",
            "x tot de macht n min één",
            "n min één, maal x tot de macht n",
        ],
        antwoord=0,
        uitleg="De exponent komt vooraan en gaat zelf met één omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de afgeleide van de sinus van x?",
        opties=[
            "de cosinus van x",
            "min de cosinus van x",
            "min de sinus van x",
            "de tangens van x",
        ],
        antwoord=0,
        uitleg="En de afgeleide van de cosinus is min de sinus. Dat minteken is het detail dat het vaakst wegvalt.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide van e tot de macht x is x maal e tot de macht x min één.",
        antwoord=False,
        uitleg="De machtsregel geldt alleen als x in de basis staat, niet in de exponent. De afgeleide van e tot de macht x is e tot de macht x zelf.",
    ),
    dict(
        type="invultekst",
        vraag="De afgeleide van de natuurlijke logaritme van x is één gedeeld door wat? Schrijf het antwoord.",
        antwoord=["x"],
        uitleg="Daarom is de logaritmische functie overal stijgend op haar domein: één op x is daar altijd positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de productregel voor afgeleiden?",
        opties=[
            "de afgeleide van de eerste maal de tweede, plus de eerste maal de afgeleide van de tweede",
            "de afgeleide van de eerste maal de afgeleide van de tweede, zonder meer",
            "de afgeleide van de eerste maal de tweede, min de eerste maal de afgeleide van de tweede",
            "de som van de twee afgeleiden, gedeeld door het product van de twee functies",
        ],
        antwoord=0,
        uitleg="Het minteken hoort bij de quotiëntregel, niet bij de productregel.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide van een product is het product van de afgeleiden.",
        antwoord=False,
        uitleg="Probeer het met x maal x: de afgeleide is twee x, niet één maal één. Daarvoor bestaat net de productregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de noemer van de quotiëntregel?",
        opties=[
            "de noemer van de breuk, in het kwadraat",
            "de teller van de breuk, in het kwadraat",
            "de noemer van de breuk, zonder meer",
            "het product van teller en noemer samen",
        ],
        antwoord=0,
        uitleg="De teller is de afgeleide van de teller maal de noemer, min de teller maal de afgeleide van de noemer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de afgeleide van vijf x plus twee? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="De afgeleide van een rechte is haar richtingscoëfficiënt, en die van een constante is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de kettingregel?",
        opties=[
            "de afgeleide van de buitenste functie, maal de afgeleide van de binnenste",
            "de afgeleide van de buitenste functie, plus die van de binnenste functie",
            "de afgeleide van de binnenste functie, gedeeld door de buitenste functie",
            "de afgeleide van de buitenste functie, met de binnenste onveranderd erin",
        ],
        antwoord=0,
        uitleg="Je leidt af van buiten naar binnen en vermenigvuldigt onderweg. De binnenste afgeleide vergeten is de klassieke fout.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide van een constante functie is nul.",
        antwoord=True,
        uitleg="De grafiek is een horizontale rechte, dus de helling is overal nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je stelt de raaklijn op aan de grafiek van x kwadraat in het punt met x gelijk aan drie. Welke vergelijking krijg je?",
        opties=[
            "y is zes x min negen",
            "y is zes x plus negen",
            "y is drie x min negen",
            "y is negen x min zes",
        ],
        antwoord=0,
        uitleg="De helling is zes en het raakpunt is drie en negen. Invullen geeft negen is achttien plus q, dus q is min negen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op de verticale as van een hellinggrafiek?",
        opties=[
            "de afgeleide van de oorspronkelijke functie",
            "de functiewaarden van de oorspronkelijke functie",
            "de oppervlakte onder de oorspronkelijke grafiek",
            "het verschil tussen twee opeenvolgende waarden",
        ],
        antwoord=0,
        uitleg="Een hellinggrafiek is gewoon de grafiek van de afgeleide functie.",
    ),
    dict(
        type="waarofniet",
        vraag="Waar de functie een vloeiend maximum heeft, snijdt haar afgeleide de x-as.",
        antwoord=True,
        uitleg="In de top loopt de raaklijn horizontaal, dus is de afgeleide daar nul en wisselt ze van teken.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x tot de derde. Hoeveel is de afgeleide in x gelijk aan twee? Schrijf het getal.",
        antwoord=["12", "twaalf"],
        uitleg="De afgeleide functie is drie x kwadraat, en drie maal vier is twaalf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een functie geeft de afgelegde weg in functie van de tijd. Wat is dan haar afgeleide?",
        opties=[
            "de snelheid op dat ogenblik",
            "de versnelling op dat ogenblik",
            "de gemiddelde snelheid over de rit",
            "de totale afstand van de hele rit",
        ],
        antwoord=0,
        uitleg="De afgeleide van de snelheid is op haar beurt de versnelling. De gemiddelde snelheid is het differentiequotiënt over het hele interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de afgeleide van de cosinus van x?",
        opties=[
            "min de sinus van x",
            "de sinus van x",
            "min de cosinus van x",
            "de tangens van x",
        ],
        antwoord=0,
        uitleg="Sinus wordt cosinus, en cosinus wordt min sinus. Pas na vier keer afleiden sta je weer bij het begin.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat weet je als de afgeleide op een interval positief is?",
        opties=[
            "de functie stijgt op dat interval",
            "de functie is positief op dat interval",
            "de grafiek is hol op dat interval",
            "de functie heeft daar een maximum",
        ],
        antwoord=0,
        uitleg="Het teken van de afgeleide gaat over de richting, niet over de hoogte. Een stijgende functie kan best negatieve waarden hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="De afgeleide is nul in a en wisselt daar van plus naar min. Wat heeft de functie in a?",
        opties=[
            "een maximum",
            "een minimum",
            "een buigpunt",
            "een nulwaarde",
        ],
        antwoord=0,
        uitleg="Eerst stijgen en dan dalen betekent een top. Van min naar plus zou een minimum geven.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x tot de derde min drie x. Hoeveel extrema heeft die functie? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="De afgeleide drie x kwadraat min drie is nul in min één en in één, en wisselt daar telkens van teken.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk punt waar de afgeleide nul is, is een extremum.",
        antwoord=False,
        uitleg="Bij x tot de derde is de afgeleide nul in nul, maar de functie blijft stijgen. Zonder tekenwissel is er geen extremum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je als de tweede afgeleide op een interval positief is?",
        opties=[
            "de grafiek is daar hol, met de holle kant naar boven",
            "de grafiek is daar bol, met de holle kant naar onder",
            "de functie stijgt daar op het hele interval",
            "de functie heeft daar een buigpunt liggen",
        ],
        antwoord=0,
        uitleg="Een positieve tweede afgeleide betekent dat de helling toeneemt, dus de kromme buigt naar boven open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de buigpunten van een functie?",
        opties=[
            "waar de tweede afgeleide nul is en van teken wisselt",
            "waar de eerste afgeleide nul is en van teken wisselt",
            "waar de functie zelf nul is en van teken wisselt",
            "waar de tweede afgeleide haar grootste waarde heeft",
        ],
        antwoord=0,
        uitleg="Zonder tekenwissel is het geen buigpunt, net zoals bij de extrema met de eerste afgeleide.",
    ),
    dict(
        type="waarofniet",
        vraag="In een buigpunt is de eerste afgeleide altijd nul.",
        antwoord=False,
        uitleg="Dat kan, maar hoeft niet. Een buigpunt kan midden op een stijgend stuk liggen; alleen de kromming verandert er.",
    ),
    dict(
        type="invultekst",
        vraag="De afgeleide heeft twee nulwaarden. In hoeveel stukken verdelen die de getallenas in het tekenschema? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Twee grenzen geven drie intervallen: links, tussen en rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="De eerste afgeleide is nul in a en de tweede afgeleide is daar positief. Wat besluit je?",
        opties=[
            "in a ligt een minimum",
            "in a ligt een maximum",
            "in a ligt een buigpunt",
            "in a is de functie niet afleidbaar",
        ],
        antwoord=0,
        uitleg="Dat is de tweede-afgeleidetest: de grafiek is daar hol, dus het vlakke punt is het laagste van zijn omgeving.",
    ),
    dict(
        type="waarofniet",
        vraag="De stelling van Rolle eist dat de functiewaarden in de twee uiteinden gelijk zijn.",
        antwoord=True,
        uitleg="Pas dan kan je besluiten dat er ergens tussenin een punt ligt met een horizontale raaklijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de middelwaardestelling van Lagrange?",
        opties=[
            "ergens is de raaklijn evenwijdig met de koorde tussen de uiteinden",
            "ergens tussen de uiteinden is de afgeleide zeker gelijk aan nul",
            "de functie bereikt tussen de uiteinden zeker haar grootste waarde",
            "de gemiddelde verandering is gelijk aan het gemiddelde van de waarden",
        ],
        antwoord=0,
        uitleg="Er is dus een punt waar de ogenblikkelijke verandering gelijk is aan de gemiddelde. Rolle is het bijzondere geval waarin de koorde horizontaal loopt.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x kwadraat. Hoeveel is de gemiddelde verandering tussen één en drie? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg="Negen min één is acht, gedeeld door drie min één is vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een extremumprobleem met context?",
        opties=[
            "zelf een veranderlijke kiezen en het functievoorschrift opstellen",
            "meteen de afgeleide nemen van de gegeven getallen",
            "een tabel maken met alle mogelijke uitkomsten naast elkaar gezet",
            "meteen de tweede afgeleide gelijkstellen aan het getal nul",
        ],
        antwoord=0,
        uitleg="Zonder voorschrift valt er niets af te leiden. Pas daarna bereken je de extrema en controleer je of het een maximum of een minimum is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een extremumprobleem met context moet je nagaan of je oplossing in het praktisch domein ligt.",
        antwoord=True,
        uitleg="Een negatieve lengte of een breedte groter dan de beschikbare omheining is wiskundig misschien een oplossing, maar in de opgave niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er allemaal in een samenvattende tabel bij een functieonderzoek?",
        opties=[
            "het teken van de eerste en de tweede afgeleide, met stijgen, dalen, hol, bol, extrema en buigpunten",
            "enkel het teken van de eerste afgeleide, met het stijgen, het dalen en de extrema die daaruit volgen",
            "enkel de nulwaarden van de functie en haar snijpunt met de verticale as",
            "de limieten op oneindig en de vergelijkingen van alle asymptoten samen",
        ],
        antwoord=0,
        uitleg="De tabel zet alles onder elkaar zodat je de grafiek kan schetsen zonder één punt te berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een functie stijgt, maar steeds trager. Wat geldt voor haar afgeleiden?",
        opties=[
            "de eerste is positief en de tweede is negatief",
            "de eerste is negatief en de tweede is positief",
            "de eerste en de tweede zijn allebei positief",
            "de eerste en de tweede zijn allebei negatief",
        ],
        antwoord=0,
        uitleg="Stijgen betekent een positieve eerste afgeleide. Trager stijgen betekent dat die afgeleide zelf daalt, dus de tweede is negatief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie kan een maximum bereiken in een punt waar ze niet afleidbaar is.",
        antwoord=True,
        uitleg="Denk aan een scherpe punt, zoals bij min de absolute waarde van x. Daar ligt een maximum zonder raaklijn.",
    ),
    dict(
        type="invultekst",
        vraag="Neem x tot de derde min drie x. Bij welke x ligt het minimum? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="De afgeleide is nul in min één en één. De tweede afgeleide zes x is positief in één, dus daar ligt het minimum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf kent zijn totale kost in functie van het aantal stuks. Wat is de marginale kost?",
        opties=[
            "de afgeleide van de totale kost",
            "de totale kost gedeeld door het aantal",
            "de kleinste kost die het bedrijf kan halen",
            "het verschil tussen de kost en de opbrengst",
        ],
        antwoord=0,
        uitleg="Ze zegt wat één extra stuk ongeveer kost. De totale kost gedeeld door het aantal is de gemiddelde kost.",
    ),
    dict(
        type="meerkeuze",
        vraag="De afgeleide van een functie is overal positief. Wat besluit je?",
        opties=[
            "de functie is overal strikt stijgend en dus inverteerbaar",
            "de functie heeft precies één maximum op haar domein",
            "de functie ligt volledig boven de horizontale as",
            "de functie is overal hol, met de holle kant naar boven",
        ],
        antwoord=0,
        uitleg="Strikt stijgend betekent dat elke functiewaarde maar één keer voorkomt, en dat is net de voorwaarde voor een inverse.",
    ),
]
