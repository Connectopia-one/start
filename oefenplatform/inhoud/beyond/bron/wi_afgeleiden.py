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
        vraag=r"Wat berekent een differentiequotiënt \(\dfrac{f(b) - f(a)}{b - a}\)?",
        opties=[
            "de gemiddelde verandering over een interval",
            "de verandering op één welbepaald ogenblik",
            "het verschil tussen twee functiewaarden",
            r"de oppervlakte onder de grafiek van \(f\)",
        ],
        antwoord=0,
        uitleg=r"Je deelt het verschil in functiewaarden door het verschil in \(x\). Enkel het "
        r"verschil van de functiewaarden is de teller alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat stelt \(f'(a)\) meetkundig voor?",
        opties=[
            "de richtingscoëfficiënt van de raaklijn in dat punt",
            "de hoogte van de grafiek in dat welbepaalde punt",
            "de afstand van dat punt tot de horizontale as",
            r"de oppervlakte tussen de grafiek en de \(x\)-as",
        ],
        antwoord=0,
        uitleg="De raaklijn is de rechte die de kromme in dat punt het best benadert, en haar "
        "helling is de afgeleide.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x) = x^{2}\). Hoeveel is \(f'(3)\)? Schrijf het getal.",
        antwoord=["6", "zes"],
        uitleg=r"\(f'(x) = 2x\), en \(2 \cdot 3 = 6\).",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide in een punt is de limiet van het differentiequotiënt.",
        antwoord=True,
        uitleg=r"\(f'(a) = \lim\limits_{h \to 0} \dfrac{f(a+h) - f(a)}{h}\): je laat het tweede punt "
        r"naar het eerste kruipen. De koorde wordt dan de raaklijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\left(x^{n}\right)'\)?",
        opties=[
            r"\(n\,x^{n-1}\)",
            r"\(n\,x^{n+1}\)",
            r"\(x^{n-1}\)",
            r"\((n-1)\,x^{n}\)",
        ],
        antwoord=0,
        uitleg="De exponent komt vooraan en gaat zelf met één omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\left(\sin x\right)'\)?",
        opties=[
            r"\(\cos x\)",
            r"\(-\cos x\)",
            r"\(-\sin x\)",
            r"\(\tan x\)",
        ],
        antwoord=0,
        uitleg=r"En \(\left(\cos x\right)' = -\sin x\). Dat minteken is het detail dat het vaakst wegvalt.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\left(e^{x}\right)' = x\,e^{x-1}\).",
        antwoord=False,
        uitleg=r"De machtsregel geldt alleen als \(x\) in de basis staat, niet in de exponent. "
        r"\(\left(e^{x}\right)' = e^{x}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(\left(\ln x\right)' = \dfrac{1}{\ \ }\). Wat komt er in de noemer? Schrijf het antwoord.",
        antwoord=["x"],
        uitleg=r"Daarom is de logaritmische functie overal stijgend op haar domein: \(\dfrac{1}{x}\) "
        r"is daar altijd positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de productregel voor afgeleiden?",
        opties=[
            r"\(\left(u\,v\right)' = u'v + u\,v'\)",
            r"\(\left(u\,v\right)' = u'v'\)",
            r"\(\left(u\,v\right)' = u'v - u\,v'\)",
            r"\(\left(u\,v\right)' = \dfrac{u' + v'}{u\,v}\)",
        ],
        antwoord=0,
        uitleg="Het minteken hoort bij de quotiëntregel, niet bij de productregel.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide van een product is het product van de afgeleiden.",
        antwoord=False,
        uitleg=r"Probeer het met \(x \cdot x\): de afgeleide is \(2x\), niet \(1 \cdot 1\). Daarvoor "
        r"bestaat net de productregel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat staat er in de noemer van \(\left(\dfrac{u}{v}\right)'\)?",
        opties=[
            r"\(v^{2}\)",
            r"\(u^{2}\)",
            r"\(v\)",
            r"\(u\,v\)",
        ],
        antwoord=0,
        uitleg=r"Voluit: \(\left(\dfrac{u}{v}\right)' = \dfrac{u'v - u\,v'}{v^{2}}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\left(5x + 2\right)'\)? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="De afgeleide van een rechte is haar richtingscoëfficiënt, en die van een constante is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zegt de kettingregel voor \(\left(f(g(x))\right)'\)?",
        opties=[
            r"\(f'(g(x)) \cdot g'(x)\)",
            r"\(f'(g(x)) + g'(x)\)",
            r"\(\dfrac{g'(x)}{f(g(x))}\)",
            r"\(f'(g(x))\)",
        ],
        antwoord=0,
        uitleg="Je leidt af van buiten naar binnen en vermenigvuldigt onderweg. De binnenste "
        "afgeleide vergeten is de klassieke fout.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgeleide van een constante functie is nul.",
        antwoord=True,
        uitleg="De grafiek is een horizontale rechte, dus de helling is overal nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je stelt de raaklijn op aan \(f(x) = x^{2}\) in \(x = 3\). Welke vergelijking krijg je?",
        opties=[
            r"\(y = 6x - 9\)",
            r"\(y = 6x + 9\)",
            r"\(y = 3x - 9\)",
            r"\(y = 9x - 6\)",
        ],
        antwoord=0,
        uitleg=r"De helling is \(f'(3) = 6\) en het raakpunt is \((3,\ 9)\). Invullen geeft "
        r"\(9 = 18 + q\), dus \(q = -9\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op de verticale as van een hellinggrafiek?",
        opties=[
            r"\(f'(x)\), de afgeleide functie",
            r"\(f(x)\), de functiewaarden zelf",
            "de oppervlakte onder de oorspronkelijke grafiek",
            "het verschil tussen twee opeenvolgende waarden",
        ],
        antwoord=0,
        uitleg="Een hellinggrafiek is gewoon de grafiek van de afgeleide functie.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Waar \(f\) een vloeiend maximum heeft, snijdt \(f'\) de \(x\)-as.",
        antwoord=True,
        uitleg="In de top loopt de raaklijn horizontaal, dus is de afgeleide daar nul en wisselt ze "
        "van teken.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x) = x^{3}\). Hoeveel is \(f'(2)\)? Schrijf het getal.",
        antwoord=["12", "twaalf"],
        uitleg=r"\(f'(x) = 3x^{2}\), en \(3 \cdot 4 = 12\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een functie \(s(t)\) geeft de afgelegde weg in functie van de tijd. Wat is \(s'(t)\)?",
        opties=[
            "de snelheid op dat ogenblik",
            "de versnelling op dat ogenblik",
            "de gemiddelde snelheid over de rit",
            "de totale afstand van de hele rit",
        ],
        antwoord=0,
        uitleg="De afgeleide van de snelheid is op haar beurt de versnelling. De gemiddelde "
        "snelheid is het differentiequotiënt over het hele interval.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is \(\left(\cos x\right)'\)?",
        opties=[
            r"\(-\sin x\)",
            r"\(\sin x\)",
            r"\(-\cos x\)",
            r"\(\tan x\)",
        ],
        antwoord=0,
        uitleg="Sinus wordt cosinus, en cosinus wordt min sinus. Pas na vier keer afleiden sta je "
        "weer bij het begin.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat weet je als \(f'(x) > 0\) op een interval?",
        opties=[
            "de functie stijgt op dat interval",
            "de functie is positief op dat interval",
            "de grafiek is hol op dat interval",
            "de functie heeft daar een maximum",
        ],
        antwoord=0,
        uitleg="Het teken van de afgeleide gaat over de richting, niet over de hoogte. Een "
        "stijgende functie kan best negatieve waarden hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f'(a) = 0\) en \(f'\) wisselt daar van plus naar min. Wat heeft \(f\) in \(a\)?",
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
        vraag=r"Neem \(f(x) = x^{3} - 3x\). Hoeveel extrema heeft die functie? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"\(f'(x) = 3x^{2} - 3\) is nul in \(-1\) en in \(1\), en wisselt daar telkens van teken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elk punt waar \(f'(x) = 0\) is een extremum.",
        antwoord=False,
        uitleg=r"Bij \(f(x) = x^{3}\) is \(f'(0) = 0\), maar de functie blijft stijgen. Zonder "
        r"tekenwissel is er geen extremum.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat weet je als \(f''(x) > 0\) op een interval?",
        opties=[
            "de grafiek is daar hol, met de holle kant naar boven",
            "de grafiek is daar bol, met de holle kant naar onder",
            "de functie stijgt daar op het hele interval",
            "de functie heeft daar een buigpunt liggen",
        ],
        antwoord=0,
        uitleg="Een positieve tweede afgeleide betekent dat de helling toeneemt, dus de kromme "
        "buigt naar boven open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de buigpunten van een functie?",
        opties=[
            r"waar \(f''(x) = 0\) en \(f''\) van teken wisselt",
            r"waar \(f'(x) = 0\) en \(f'\) van teken wisselt",
            r"waar \(f(x) = 0\) en \(f\) van teken wisselt",
            r"waar \(f''\) haar grootste waarde heeft",
        ],
        antwoord=0,
        uitleg="Zonder tekenwissel is het geen buigpunt, net zoals bij de extrema met de eerste afgeleide.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een buigpunt is \(f'\) altijd nul.",
        antwoord=False,
        uitleg="Dat kan, maar hoeft niet. Een buigpunt kan midden op een stijgend stuk liggen; "
        "alleen de kromming verandert er.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(f'\) heeft twee nulwaarden. In hoeveel stukken verdelen die de getallenas in het tekenschema? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Twee grenzen geven drie intervallen: links, tussen en rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f'(a) = 0\) en \(f''(a) > 0\). Wat besluit je?",
        opties=[
            r"in \(a\) ligt een minimum",
            r"in \(a\) ligt een maximum",
            r"in \(a\) ligt een buigpunt",
            r"in \(a\) is \(f\) niet afleidbaar",
        ],
        antwoord=0,
        uitleg="Dat is de tweede-afgeleidetest: de grafiek is daar hol, dus het vlakke punt is het "
        "laagste van zijn omgeving.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De stelling van Rolle eist dat \(f(a) = f(b)\) in de twee uiteinden.",
        antwoord=True,
        uitleg="Pas dan kan je besluiten dat er ergens tussenin een punt ligt met een horizontale "
        "raaklijn.",
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
        uitleg=r"Er is dus een \(c\) met \(f'(c) = \dfrac{f(b) - f(a)}{b - a}\). Rolle is het "
        r"bijzondere geval waarin de koorde horizontaal loopt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x) = x^{2}\). Hoeveel is de gemiddelde verandering tussen \(1\) en \(3\)? Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\(\dfrac{9 - 1}{3 - 1} = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een extremumprobleem met context?",
        opties=[
            "zelf een veranderlijke kiezen en het functievoorschrift opstellen",
            "meteen de afgeleide nemen van de gegeven getallen",
            "een tabel maken met alle mogelijke uitkomsten naast elkaar gezet",
            "meteen de tweede afgeleide gelijkstellen aan nul",
        ],
        antwoord=0,
        uitleg="Zonder voorschrift valt er niets af te leiden. Pas daarna bereken je de extrema en "
        "controleer je of het een maximum of een minimum is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een extremumprobleem met context moet je nagaan of je oplossing in het praktisch domein ligt.",
        antwoord=True,
        uitleg="Een negatieve lengte of een breedte groter dan de beschikbare omheining is "
        "wiskundig misschien een oplossing, maar in de opgave niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er allemaal in een samenvattende tabel bij een functieonderzoek?",
        opties=[
            r"het teken van \(f'\) en \(f''\), met stijgen, dalen, hol, bol, extrema en buigpunten",
            r"enkel het teken van \(f'\), met het stijgen, het dalen en de extrema",
            r"enkel de nulwaarden van \(f\) en haar snijpunt met de verticale as",
            "de limieten op oneindig en de vergelijkingen van alle asymptoten samen",
        ],
        antwoord=0,
        uitleg="De tabel zet alles onder elkaar zodat je de grafiek kan schetsen zonder één punt te "
        "berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een functie stijgt, maar steeds trager. Wat geldt voor haar afgeleiden?",
        opties=[
            r"\(f' > 0\) en \(f'' < 0\)",
            r"\(f' < 0\) en \(f'' > 0\)",
            r"\(f' > 0\) en \(f'' > 0\)",
            r"\(f' < 0\) en \(f'' < 0\)",
        ],
        antwoord=0,
        uitleg="Stijgen betekent een positieve eerste afgeleide. Trager stijgen betekent dat die "
        "afgeleide zelf daalt, dus de tweede is negatief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functie kan een maximum bereiken in een punt waar ze niet afleidbaar is.",
        antwoord=True,
        uitleg=r"Denk aan een scherpe punt, zoals bij \(f(x) = -|x|\). Daar ligt een maximum zonder "
        r"raaklijn.",
    ),
    dict(
        type="invultekst",
        vraag=r"Neem \(f(x) = x^{3} - 3x\). Bij welke \(x\) ligt het minimum? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg=r"\(f'\) is nul in \(-1\) en \(1\). \(f''(x) = 6x\) is positief in \(1\), dus daar "
        r"ligt het minimum.",
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
        uitleg="Ze zegt wat één extra stuk ongeveer kost. De totale kost gedeeld door het aantal is "
        "de gemiddelde kost.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f'(x) > 0\) op heel het domein. Wat besluit je?",
        opties=[
            "de functie is overal strikt stijgend en dus inverteerbaar",
            "de functie heeft precies één maximum op haar domein",
            "de functie ligt volledig boven de horizontale as",
            "de functie is overal hol, met de holle kant naar boven",
        ],
        antwoord=0,
        uitleg="Strikt stijgend betekent dat elke functiewaarde maar één keer voorkomt, en dat is "
        "net de voorwaarde voor een inverse.",
    ),
]
