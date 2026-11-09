# -*- coding: utf-8 -*-
"""Afgeleiden: helling en raaklijn.

Wiskunde basis, derde graad. De fiche vraagt: het informele limietbegrip,
het differentiequotiënt als gemiddelde verandering, de richtingscoëfficiënt
als helling, de raaklijn, de afgeleide in een punt als limiet van het
differentiequotiënt en als richtingscoëfficiënt van de raaklijn, benaderen
met een tabel, grafisch bepalen en met ICT, de vergelijking van de raaklijn
opstellen. Daarna het grafisch verband tussen een functie en haar afgeleide
functie: hellinggrafiek, stijgen en dalen, extrema, tekenverloop van f'.

Afgeleiden berekenen met rekenregels (som, product, kettingregel) vraagt
deze fiche niet. Waar een afgeleide nodig is, staat ze gegeven of volgt ze
uit een tabel of een raaklijn.

Deel 1: differentiequotiënt, raaklijn en afgeleide in een punt.
Deel 2: afgeleide functie en hellinggrafiek.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is het differentiequotiënt van \(f\) over \([a, b]\)?",
        opties=[r"\(\dfrac{f(b) - f(a)}{b - a}\)", r"\(\dfrac{b - a}{f(b) - f(a)}\)", r"\(f(b) - f(a)\)", r"\(\dfrac{f(b) + f(a)}{2}\)"],
        antwoord=0,
        uitleg=r"Het differentiequotiënt is de gemiddelde verandering: de toename van \(f\) gedeeld door de toename van \(x\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken het differentiequotiënt van \(f(x) = x^{2}\) over \([1, 4]\). Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"\(\dfrac{f(4) - f(1)}{4 - 1} = \dfrac{16 - 1}{3} = 5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een auto staat na \(2\) uur op \(150\) km van de start en na \(5\) uur op \(390\) km. Wat is de gemiddelde snelheid in km/h over dat interval? Schrijf het getal.",
        antwoord=["80", "tachtig"],
        uitleg=r"\(\dfrac{390 - 150}{5 - 2} = \dfrac{240}{3} = 80\). Een gemiddelde snelheid is een differentiequotiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat stelt het differentiequotiënt over \([a, b]\) voor op de grafiek?",
        opties=[
            r"de richtingscoëfficiënt van de rechte door \((a, f(a))\) en \((b, f(b))\)",
            r"de richtingscoëfficiënt van de raaklijn in \((a, f(a))\)",
            r"de oppervlakte onder de grafiek tussen \(a\) en \(b\)",
            r"de afstand tussen \((a, f(a))\) en \((b, f(b))\)",
        ],
        antwoord=0,
        uitleg=r"Die rechte door twee punten van de grafiek heet een koorde. Haar helling is de gemiddelde verandering.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de afgeleide \(f'(a)\) in een punt?",
        opties=[
            r"de limiet van het differentiequotiënt over \([a, a + h]\) als \(h\) naar \(0\) gaat",
            r"het differentiequotiënt over \([0, a]\)",
            r"de functiewaarde \(f(a)\)",
            r"de oppervlakte onder de grafiek tot \(a\)",
        ],
        antwoord=0,
        uitleg=r"Je laat het interval steeds kleiner worden. De gemiddelde verandering wordt dan de ogenblikkelijke verandering.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De afgeleide in een punt is de richtingscoëfficiënt van de raaklijn aan de grafiek in dat punt.",
        antwoord=True,
        uitleg=r"Als de koorde steeds korter wordt, nadert ze de raaklijn. Haar helling nadert de afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel van differentiequotiënten van \(f\) over \([2, 2 + h]\): \(h = 0{,}1\): \(4{,}1\); \(h = 0{,}01\): \(4{,}01\); \(h = 0{,}001\): \(4{,}001\). Wat is \(f'(2)\)?",
        opties=[r"\(4\)", r"\(4{,}1\)", r"\(2\)", r"\(0\)"],
        antwoord=0,
        uitleg=r"Hoe kleiner \(h\), hoe dichter het quotiënt bij \(4\) komt. Dat is het informele limietbegrip.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(3) < 0\), dan daalt de grafiek van \(f\) in de buurt van \(x = 3\).",
        antwoord=True,
        uitleg=r"Een negatieve afgeleide is een negatieve helling: de raaklijn loopt naar beneden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(3) = 10\) en \(g'(3) = 2\), dan is \(f(3)\) groter dan \(g(3)\).",
        antwoord=False,
        uitleg=r"De afgeleide zegt hoe snel de functie verandert, niet hoe groot de functiewaarde is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De raaklijn aan de grafiek van \(f\) in \(x = 1\) gaat door \((1, 3)\) en \((3, 7)\). Hoeveel is \(f'(1)\)?",
        opties=[r"\(2\)", r"\(3\)", r"\(4\)", r"\(\dfrac{1}{2}\)"],
        antwoord=0,
        uitleg=r"De richtingscoëfficiënt van de raaklijn is \(\dfrac{7 - 3}{3 - 1} = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe luidt de vergelijking van een rechte door \((x_{1}, y_{1})\) met richtingscoëfficiënt \(m\)?",
        opties=[r"\(y - y_{1} = m(x - x_{1})\)", r"\(y + y_{1} = m(x + x_{1})\)", r"\(y = mx + x_{1}\)", r"\(y - x_{1} = m(x - y_{1})\)"],
        antwoord=0,
        uitleg=r"Voor een raaklijn is het punt \((a, f(a))\) en \(m = f'(a)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Gegeven: \(f(2) = 5\) en \(f'(2) = 3\). Wat is de vergelijking van de raaklijn in \(x = 2\)?",
        opties=[r"\(y = 3x - 1\)", r"\(y = 3x + 5\)", r"\(y = 5x - 7\)", r"\(y = 3x + 1\)"],
        antwoord=0,
        uitleg=r"\(y - 5 = 3(x - 2) \iff y = 3x - 6 + 5 = 3x - 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Gegeven: \(f(-1) = 4\) en \(f'(-1) = -2\). Wat is de vergelijking van de raaklijn in \(x = -1\)?",
        opties=[r"\(y = -2x + 2\)", r"\(y = -2x + 4\)", r"\(y = -2x - 6\)", r"\(y = 4x + 2\)"],
        antwoord=0,
        uitleg=r"\(y - 4 = -2(x + 1) \iff y = -2x - 2 + 4 = -2x + 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In de top van een parabool is de raaklijn verticaal.",
        antwoord=False,
        uitleg=r"In de top gaat stijgen over in dalen of omgekeerd. De helling is daar \(0\): de raaklijn is horizontaal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De afstand \(s(t)\) in meter van een fietser na \(t\) seconden. Wat betekent \(s'(10) = 6\)?",
        opties=[
            r"Op het tijdstip \(10\) s rijdt de fietser \(6\) m/s.",
            r"Na \(10\) s heeft de fietser \(6\) m afgelegd.",
            r"Na \(6\) s heeft de fietser \(10\) m afgelegd.",
            r"Gemiddeld reed de fietser \(6\) m/s over de eerste \(10\) s.",
        ],
        antwoord=0,
        uitleg=r"De afgeleide van de afstand is de ogenblikkelijke snelheid op dat moment, niet het gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(K(q)\) is de totale kost in euro om \(q\) stuks te maken. Hoe heet \(K'(q)\)?",
        opties=[r"de marginale kost", r"de gemiddelde kost", r"de vaste kost", r"de totale opbrengst"],
        antwoord=0,
        uitleg=r"De marginale kost is ongeveer de extra kost van één stuk meer.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken de gemiddelde verandering van \(f(x) = 2^{x}\) over \([0, 3]\), afgerond op twee cijfers na de komma.",
        antwoord=["2,33", "2.33"],
        uitleg=r"\(\dfrac{2^{3} - 2^{0}}{3 - 0} = \dfrac{8 - 1}{3} = \dfrac{7}{3} \approx 2{,}33\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De gemiddelde verandering over \([a, b]\) is altijd gelijk aan de afgeleide in het midden van dat interval.",
        antwoord=False,
        uitleg=r"Dat klopt voor een parabool, maar niet in het algemeen. Bij \(2^{x}\) over \([0, 3]\) is \(f'(1{,}5) \approx 1{,}96\), niet \(2{,}33\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rechte \(y = -0{,}5x + 3\). Wat is haar helling?",
        opties=[r"\(-0{,}5\)", r"\(3\)", r"\(0{,}5\)", r"\(6\)"],
        antwoord=0,
        uitleg=r"In \(y = mx + q\) is \(m\) de richtingscoëfficiënt, de helling.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor een rechte \(f(x) = mx + q\) is de afgeleide in elk punt gelijk aan \(m\).",
        antwoord=True,
        uitleg=r"Een rechte is overal even steil. De raaklijn in elk punt is de rechte zelf, met richtingscoëfficiënt \(m\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is een hellinggrafiek van \(f\)?",
        opties=[
            r"de grafiek van de afgeleide functie \(f'\)",
            r"de grafiek van \(f\) zelf, maar steiler",
            r"de raaklijn aan \(f\) in één punt",
            r"de grafiek van \(-f\)",
        ],
        antwoord=0,
        uitleg=r"Bij elke \(x\) zet je de helling van \(f\) in dat punt uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waar \(f'(x) > 0\), is de functie \(f\) ...",
        opties=[r"stijgend", r"dalend", r"positief", r"constant"],
        antwoord=0,
        uitleg=r"Een positieve afgeleide is een positieve helling. Of \(f\) zelf positief is, zegt \(f'\) niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het tekenverloop van \(f'\): \(+\) voor \(x < 2\), \(0\) in \(x = 2\), \(-\) voor \(x > 2\). Wat heeft \(f\) in \(x = 2\)?",
        opties=[r"een maximum", r"een minimum", r"een nulwaarde", r"een verticale asymptoot"],
        antwoord=0,
        uitleg=r"Eerst stijgen, dan dalen: in \(x = 2\) bereikt \(f\) een maximum.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het tekenverloop van \(f'\): \(-\) voor \(x < -1\), \(0\) in \(x = -1\), \(+\) voor \(x > -1\). Wat heeft \(f\) in \(x = -1\)?",
        opties=[r"een minimum", r"een maximum", r"een nulwaarde", r"geen extremum"],
        antwoord=0,
        uitleg=r"Eerst dalen, dan stijgen: een minimum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Waar de grafiek van \(f'\) de \(x\)-as snijdt en van teken wisselt, heeft \(f\) een extremum.",
        antwoord=True,
        uitleg=r"Daar gaat stijgen over in dalen of omgekeerd.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Waar \(f\) een nulwaarde heeft, heeft \(f'\) ook een nulwaarde.",
        antwoord=False,
        uitleg=r"\(f(x) = 2x\) heeft een nulwaarde in \(0\), maar \(f'(x) = 2\) is nooit nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f\) is een dalparabool met top in \(x = 3\). Hoe ziet de hellinggrafiek eruit?",
        opties=[
            r"een stijgende rechte die de \(x\)-as snijdt in \(3\)",
            r"een dalende rechte die de \(x\)-as snijdt in \(3\)",
            r"een dalparabool met top in \(3\)",
            r"een horizontale rechte op hoogte \(3\)",
        ],
        antwoord=0,
        uitleg=r"Links van de top is de helling negatief, in de top \(0\), rechts positief, en ze neemt gelijkmatig toe.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De hellinggrafiek van \(f\) is de horizontale rechte \(y = 2\). Wat voor grafiek heeft \(f\)?",
        opties=[r"een stijgende rechte met richtingscoëfficiënt \(2\)", r"een horizontale rechte op hoogte \(2\)", r"een dalparabool", r"een dalende rechte"],
        antwoord=0,
        uitleg=r"Een constante helling \(2\) hoort bij een rechte die overal even steil stijgt.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als de hellinggrafiek overal onder de \(x\)-as ligt, dan daalt \(f\) overal.",
        antwoord=True,
        uitleg=r"Overal een negatieve helling betekent overal dalen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op een interval is \(f'\) positief en stijgend. Hoe verloopt \(f\) daar?",
        opties=[r"toenemende stijging", r"afnemende stijging", r"toenemende daling", r"constante stijging"],
        antwoord=0,
        uitleg=r"\(f\) stijgt omdat \(f' > 0\), en steeds steiler omdat de helling groeit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op een interval is \(f'\) positief en dalend. Hoe verloopt \(f\) daar?",
        opties=[r"afnemende stijging", r"toenemende stijging", r"afnemende daling", r"constante stijging"],
        antwoord=0,
        uitleg=r"\(f\) stijgt nog, maar de helling wordt kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De snelheid \(v(t)\) is de afgeleide van de afgelegde weg \(s(t)\). Wat betekent \(v(t) = 0\) op een moment?",
        opties=[
            r"Op dat moment staat het voorwerp even stil.",
            r"Het voorwerp is terug bij de start.",
            r"Het voorwerp heeft nog geen weg afgelegd.",
            r"Het voorwerp rijdt op topsnelheid.",
        ],
        antwoord=0,
        uitleg=r"Een helling \(0\) bij \(s(t)\) betekent dat de afstand op dat moment niet verandert.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De versnelling is de afgeleide van de snelheid.",
        antwoord=True,
        uitleg=r"Versnelling zegt hoe snel de snelheid verandert, zoals snelheid zegt hoe snel de afstand verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f'\) snijdt de \(x\)-as in \(-2\) en \(4\). \(f'\) is positief voor \(x < -2\) en voor \(x > 4\), negatief ertussen. Welke uitspraak is juist?",
        opties=[
            r"\(f\) heeft een maximum in \(-2\) en een minimum in \(4\).",
            r"\(f\) heeft een minimum in \(-2\) en een maximum in \(4\).",
            r"\(f\) heeft nulwaarden in \(-2\) en \(4\).",
            r"\(f\) stijgt tussen \(-2\) en \(4\).",
        ],
        antwoord=0,
        uitleg=r"In \(-2\): van stijgen naar dalen, een maximum. In \(4\): van dalen naar stijgen, een minimum.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f\) daalt tot \(x = 1\), stijgt daarna tot \(x = 5\) en daalt daarna weer. Welk tekenverloop heeft \(f'\)?",
        opties=[
            r"\(-\) voor \(x < 1\), \(+\) tussen \(1\) en \(5\), \(-\) voor \(x > 5\)",
            r"\(+\) voor \(x < 1\), \(-\) tussen \(1\) en \(5\), \(+\) voor \(x > 5\)",
            r"\(-\) voor \(x < 5\), \(+\) voor \(x > 5\)",
            r"overal \(+\)",
        ],
        antwoord=0,
        uitleg=r"Dalen hoort bij \(-\), stijgen bij \(+\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(x) = 0\) in een punt, dan heeft \(f\) daar zeker een maximum of minimum.",
        antwoord=False,
        uitleg=r"\(f(x) = x^{3}\) heeft \(f'(0) = 0\), maar stijgt voor en na \(0\). Er moet een tekenwissel zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De totale kost \(K(q)\) stijgt eerst steeds trager en daarna steeds sneller. Hoe verloopt de marginale kost \(K'(q)\)?",
        opties=[r"eerst dalend, daarna stijgend", r"eerst stijgend, daarna dalend", r"altijd constant", r"altijd negatief"],
        antwoord=0,
        uitleg=r"Trager stijgen betekent een kleinere helling, sneller stijgen een grotere helling.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee functies die enkel verschillen door een verticale verschuiving, hebben dezelfde hellinggrafiek.",
        antwoord=True,
        uitleg=r"Een verschuiving naar boven of beneden verandert de steilheid nergens.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met een rekenapp vind je voor \(f(x) = x^{3} - 3x\) dat \(f'(2) = 9\). Wat betekent dat?",
        opties=[
            r"In \(x = 2\) heeft de raaklijn aan de grafiek richtingscoëfficiënt \(9\).",
            r"De functiewaarde in \(x = 2\) is \(9\).",
            r"De grafiek snijdt de \(x\)-as in \(9\).",
            r"De gemiddelde verandering over \([0, 2]\) is \(9\).",
        ],
        antwoord=0,
        uitleg=r"\(f(2) = 8 - 6 = 2\) is de functiewaarde. \(f'(2) = 9\) is de helling in dat punt.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie heeft een maximum waar haar hellinggrafiek van negatief naar positief gaat.",
        antwoord=False,
        uitleg=r"Van negatief naar positief: eerst dalen, dan stijgen. Dat is een minimum.",
    ),
]
