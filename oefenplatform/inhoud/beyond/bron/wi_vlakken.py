# -*- coding: utf-8 -*-
"""Rechten en vlakken in de ruimte.

Het tweede stuk van het onderdeel "Analytische ruimtemeetkunde" van fiche G3.
De vectoren uit het vorige thema worden hier vergelijkingen, en met die
vergelijkingen ga je ligging, afstand en hoek na.

Een vlak noemen we \\(\\alpha\\), zijn normaalvector \\(\\vec{n}\\), en een
richtingsvector van een rechte \\(\\vec{v}\\).

Deel 1 zijn de vergelijkingen zelf: vectorieel, parametrisch en cartesisch,
voor een rechte en voor een vlak, met de drie bij drie determinant.
Deel 2 is de onderlinge ligging van rechten en vlakken, en de afstanden en
hoeken die daarbij horen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat heb je nodig om de vergelijking van een rechte in de ruimte op te stellen?",
        opties=[
            r"een punt en een richtingsvector \(\vec{v}\)",
            r"een punt en een normaalvector van die rechte",
            r"twee richtingsvectoren die niet evenwijdig zijn",
            r"drie punten die niet op één rechte liggen",
        ],
        antwoord=0,
        uitleg=r"Het punt zegt waar ze ligt, \(\vec{v}\) welke kant ze op loopt. Twee punten volstaan ook, want daar haal je \(\vec{v}\) uit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de rol van de parameter \(t\) in \(\overrightarrow{OP} = \overrightarrow{OP_{0}} + t \cdot \vec{v}\)?",
        opties=[
            r"elke waarde van \(t\) geeft een ander punt van de rechte",
            r"ze geeft de lengte aan van de richtingsvector zelf",
            r"ze geeft de hoek aan die de rechte met de assen maakt",
            r"ze bepaalt het aantal snijpunten met de drie assen",
        ],
        antwoord=0,
        uitleg=r"Laat je \(t\) alle waarden van \(\mathbb{R}\) doorlopen, dan krijg je de hele rechte.",
    ),
    dict(
        type="invultekst",
        vraag=r"Uit hoeveel parametrische vergelijkingen bestaat de beschrijving van een rechte in de ruimte? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"Eén per coördinaat: \(x = x_{0} + at\), \(y = y_{0} + bt\) en \(z = z_{0} + ct\), alle drie met dezelfde \(t\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een rechte in de ruimte heeft één cartesische vergelijking.",
        antwoord=False,
        uitleg=r"Ze heeft er twee: een rechte in de ruimte is de doorsnede van twee vlakken. In het vlak is het er wel maar één.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ziet de cartesische vergelijking van een vlak eruit?",
        opties=[
            r"\(ax + by + cz + d = 0\)",
            r"\(y = ax + b\)",
            r"\(x^{2} + y^{2} = r^{2}\)",
            r"\(x = a\), \(y = b\), \(z = c\)",
        ],
        antwoord=0,
        uitleg=r"Eén vergelijking van de eerste graad in drie onbekenden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat lees je rechtstreeks af uit \(a\), \(b\) en \(c\) in \(ax + by + cz + d = 0\)?",
        opties=[
            r"een normaalvector \(\vec{n}(a, b, c)\) van het vlak",
            r"een richtingsvector die in het vlak ligt",
            r"het punt waar het vlak de \(z\)-as snijdt",
            r"de afstand van het vlak tot de oorsprong",
        ],
        antwoord=0,
        uitleg=r"De drie coëfficiënten zijn precies de coördinaten van een vector die loodrecht op het vlak staat.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vlak ligt vast door één punt en twee richtingsvectoren die niet evenwijdig zijn.",
        antwoord=True,
        uitleg=r"Zijn de twee richtingsvectoren wel evenwijdig, dan krijg je maar een rechte.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel parameters staan er in de parametrische vergelijkingen van een vlak? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"Eén per richtingsvector, dus \(s\) en \(t\). Een rechte heeft er maar één.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe stel je met een determinant van orde \(3\) de cartesische vergelijking van een vlak op?",
        opties=[
            r"je stelt de determinant gelijk aan \(0\)",
            r"je stelt de determinant gelijk aan \(1\)",
            r"je berekent de determinant en deelt door \(3\)",
            r"je neemt de determinant van \(\vec{n}\) alleen",
        ],
        antwoord=0,
        uitleg=r"In de determinant staan \(\overrightarrow{P_{0}P}\) naar een onbekend punt en de twee richtingsvectoren. Nul betekent dat ze in één vlak liggen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Drie punten die op eenzelfde rechte liggen, bepalen samen één vlak.",
        antwoord=False,
        uitleg=r"Door zo'n rechte gaan oneindig veel vlakken. De drie punten mogen niet op één rechte liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ga je van de parametrische naar de cartesische vergelijkingen van een rechte?",
        opties=[
            r"je werkt de parameter \(t\) weg uit de vergelijkingen",
            r"je vult \(t = 0\) in",
            r"je telt de drie vergelijkingen bij elkaar op",
            r"je berekent de determinant van de coëfficiënten",
        ],
        antwoord=0,
        uitleg=r"Je drukt \(t\) uit in één vergelijking en vult die in de twee andere in. Er blijven twee vergelijkingen over.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel punten die niet op eenzelfde rechte liggen, bepalen één vlak? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"Daarom staat een tafel met drie poten nooit te wiebelen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de cartesische vergelijking van het vlak door de \(x\)-as en de \(y\)-as?",
        opties=[
            r"\(z = 0\)",
            r"\(x = 0\)",
            r"\(x + y = 0\)",
            r"\(x + y + z = 0\)",
        ],
        antwoord=0,
        uitleg=r"Alle punten van dat vlak hebben derde coördinaat nul. De \(z\)-as is er de normaal van.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een rechte heeft oneindig veel richtingsvectoren.",
        antwoord=True,
        uitleg=r"Elk veelvoud \(k \cdot \vec{v}\) met \(k \neq 0\) is er ook een.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe controleer je of een punt op een rechte ligt?",
        opties=[
            r"je vult zijn coördinaten in de vergelijkingen in",
            r"je berekent de afstand van dat punt tot de oorsprong",
            r"je vergelijkt zijn coördinaten met \(\vec{v}\)",
            r"je telt zijn coördinaten op en kijkt of je \(0\) krijgt",
        ],
        antwoord=0,
        uitleg=r"Bij de parametrische vorm moet er voor alle drie dezelfde waarde van \(t\) uitkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je kent een punt van een vlak en een normaalvector \(\vec{n}\) ervan. Wat kan je opstellen?",
        opties=[
            r"de cartesische vergelijking van dat vlak",
            r"enkel de parametrische vergelijkingen ervan",
            r"niets, want je hebt twee richtingsvectoren nodig",
            r"enkel de vectoriële vergelijking van dat vlak",
        ],
        antwoord=0,
        uitleg=r"\(\vec{n}\) geeft \(a\), \(b\) en \(c\); het punt bepaalt \(d\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In het vlak heeft een rechte precies één cartesische vergelijking.",
        antwoord=True,
        uitleg=r"Daar is het \(ax + by + c = 0\). Pas in de ruimte heb je er twee nodig.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een vlak heeft als vergelijking \(2x - 3y + z - 5 = 0\). Wat is de eerste coördinaat van \(\vec{n}\)? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"\(\vec{n}(2, -3, 1)\): de coëfficiënten van \(x\), \(y\) en \(z\) samen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom stel je die determinant van orde \(3\) gelijk aan \(0\)?",
        opties=[
            r"omdat de drie vectoren dan in eenzelfde vlak liggen",
            r"omdat de drie vectoren dan loodrecht op elkaar staan",
            r"omdat de drie vectoren dan allemaal even lang zijn",
            r"omdat het vlak dan door de oorsprong moet gaan",
        ],
        antwoord=0,
        uitleg=r"Een determinant die niet nul is, betekent dat de drie vectoren de hele ruimte opspannen. Precies dat mag niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je hebt \(ax + by + cz + d = 0\) en wil de parametrische vergelijkingen. Hoe pak je dat aan?",
        opties=[
            r"je zoekt een punt en twee richtingsvectoren van het vlak",
            r"je zoekt \(\vec{n}\) en gebruikt die als parameter",
            r"je stelt elke coördinaat gelijk aan een eigen parameter",
            r"je berekent de determinant van \(a\), \(b\) en \(c\)",
        ],
        antwoord=0,
        uitleg=r"Twee van de drie onbekenden mag je vrij kiezen. Die twee vrijheidsgraden worden \(s\) en \(t\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Welke onderlinge liggingen kunnen twee rechten in de ruimte hebben?",
        opties=[
            r"samenvallend, evenwijdig, snijdend of kruisend",
            r"enkel evenwijdig of snijdend, meer bestaat er niet",
            r"samenvallend, snijdend of loodrecht op elkaar",
            r"evenwijdig, loodrecht of met een scherpe hoek",
        ],
        antwoord=0,
        uitleg=r"Kruisend bestaat alleen in de ruimte: in het vlak snijden twee niet-evenwijdige rechten elkaar altijd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn kruisende rechten?",
        opties=[
            r"rechten die niet evenwijdig zijn en toch geen snijpunt hebben",
            r"rechten die elkaar in precies één punt snijden in de ruimte",
            r"rechten die loodrecht op elkaar staan zonder elkaar te raken",
            r"rechten die evenwijdig lopen maar niet samenvallen",
        ],
        antwoord=0,
        uitleg=r"Ze liggen niet in eenzelfde vlak. Denk aan twee wegen boven elkaar met een brug ertussen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel mogelijke onderlinge liggingen heeft een rechte ten opzichte van een vlak? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"Ze ligt in het vlak, ze is er evenwijdig mee zonder erin te liggen, of ze snijdt het.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee rechten in de ruimte die elkaar niet snijden, zijn evenwijdig.",
        antwoord=False,
        uitleg=r"Ze kunnen ook kruisen. In het vlak zou het wel kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ga je na of twee vlakken evenwijdig zijn?",
        opties=[
            r"je kijkt of \(\vec{n_{1}} = k \cdot \vec{n_{2}}\)",
            r"je kijkt of \(\vec{n_{1}} \perp \vec{n_{2}}\)",
            r"je berekent \(\vec{n_{1}} \cdot \vec{n_{2}}\) en vergelijkt met \(1\)",
            r"je vergelijkt \(d\) van beide vergelijkingen",
        ],
        antwoord=0,
        uitleg=r"Dezelfde richting loodrecht erop betekent dezelfde stand.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee vlakken zijn evenwijdig. Wanneer vallen ze samen?",
        opties=[
            r"als je de ene vergelijking uit de andere kan vermenigvuldigen",
            r"als \(\|\vec{n_{1}}\| = \|\vec{n_{2}}\|\)",
            r"als \(d = 0\) bij allebei",
            r"als ze allebei door de oorsprong gaan",
        ],
        antwoord=0,
        uitleg=r"Dan is het twee keer hetzelfde vlak, enkel anders opgeschreven. Anders liggen ze er netjes naast.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee vlakken die niet evenwijdig zijn, snijden elkaar volgens een rechte.",
        antwoord=True,
        uitleg=r"Nooit in één punt: de doorsnede van twee verschillende vlakken is altijd een rechte of niets.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe groot is de afstand tussen twee samenvallende vlakken? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg=r"Het is hetzelfde vlak, dus er zit niets tussen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de hoek tussen twee vlakken?",
        opties=[
            r"als de hoek tussen \(\vec{n_{1}}\) en \(\vec{n_{2}}\)",
            r"als de hoek tussen hun twee richtingsvectoren",
            r"als de som van hun hoeken met het grondvlak",
            r"als het verschil van hun laatste twee termen",
        ],
        antwoord=0,
        uitleg=r"Je rekent met \(\cos \theta = \dfrac{\vec{n_{1}} \cdot \vec{n_{2}}}{\|\vec{n_{1}}\| \cdot \|\vec{n_{2}}\|}\) en neemt de scherpe hoek van de twee die je zo krijgt.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De hoek tussen twee rechten vind je uit het scalair product van hun richtingsvectoren.",
        antwoord=True,
        uitleg=r"Ook bij kruisende rechten, al snijden ze elkaar dan niet: de hoek hangt enkel van de richtingen af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de afstand van een punt \(P\) tot een vlak \(\alpha: ax + by + cz + d = 0\)?",
        opties=[
            r"\(d(P, \alpha) = \dfrac{|a x_{P} + b y_{P} + c z_{P} + d|}{\sqrt{a^{2} + b^{2} + c^{2}}}\)",
            r"\(d(P, \alpha) = \dfrac{a x_{P} + b y_{P} + c z_{P} + d}{a^{2} + b^{2} + c^{2}}\)",
            r"\(d(P, \alpha) = |a x_{P} + b y_{P} + c z_{P} + d|\)",
            r"\(d(P, \alpha) = \|\overrightarrow{OP}\|\)",
        ],
        antwoord=0,
        uitleg=r"Je meet langs de loodlijn uit \(P\) op het vlak: de afstand is altijd de kortste, en die loopt loodrecht.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe groot is de afstand tussen twee snijdende rechten? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg=r"Ze hebben een punt gemeen, dus de kortste afstand is nul.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer behoort een rechte volledig tot een vlak?",
        opties=[
            r"als twee van haar punten in het vlak liggen",
            r"als \(\vec{v} = \vec{n}\)",
            r"als ze het vlak in precies één punt snijdt",
            r"als \(\vec{v} \perp \vec{n}\)",
        ],
        antwoord=0,
        uitleg=r"Twee punten volstaan. Enkel \(\vec{v} \perp \vec{n}\) maakt haar evenwijdig, meer niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee evenwijdige rechten liggen altijd in eenzelfde vlak.",
        antwoord=True,
        uitleg=r"Door twee evenwijdige rechten gaat precies één vlak. Bij kruisende rechten lukt dat net niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ga je na of een rechte evenwijdig is met een vlak?",
        opties=[
            r"je kijkt of \(\vec{v} \perp \vec{n}\)",
            r"je kijkt of \(\vec{v} \parallel \vec{n}\)",
            r"je berekent de afstand van de rechte tot de oorsprong",
            r"je vult een punt van het vlak in de rechte in",
        ],
        antwoord=0,
        uitleg=r"Dus \(\vec{v} \cdot \vec{n} = 0\). Ligt er dan ook nog een punt van de rechte in het vlak, dan ligt ze er helemaal in.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de afstand tussen twee evenwijdige vlakken?",
        opties=[
            r"je neemt een punt van het ene en zijn afstand tot het andere",
            r"je neemt het verschil van \(\vec{n_{1}}\) en \(\vec{n_{2}}\)",
            r"je neemt de afstand van beide vlakken tot de oorsprong",
            r"je neemt het midden tussen de twee vlakken in de ruimte",
        ],
        antwoord=0,
        uitleg=r"Welk punt je kiest maakt niet uit: bij evenwijdige vlakken is die afstand overal dezelfde.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee kruisende rechten liggen in eenzelfde vlak.",
        antwoord=False,
        uitleg=r"Net niet, en dat is precies wat kruisend betekent. Door twee kruisende rechten gaat geen enkel vlak.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe groot is de hoek tussen twee evenwijdige vlakken, in graden? Schrijf het cijfer.",
        antwoord=["0", "nul"],
        uitleg=r"Hun normaalvectoren wijzen dezelfde kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer staat een rechte loodrecht op een vlak?",
        opties=[
            r"als \(\vec{v} \parallel \vec{n}\)",
            r"als \(\vec{v} \perp \vec{n}\)",
            r"als ze het vlak snijdt in een punt van de \(x\)-as",
            r"als ze evenwijdig loopt met een zijde van dat vlak",
        ],
        antwoord=0,
        uitleg=r"\(\vec{n}\) staat zelf al loodrecht op het vlak, dus de rechte moet zijn richting volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een hellend dakvlak en de verticale gevel eronder. Wat is de hoek tussen die twee vlakken?",
        opties=[
            r"de hoek tussen \(\vec{n_{1}}\) en \(\vec{n_{2}}\), als scherpe hoek genomen",
            r"de hoek die het dak maakt met de horizontale grond eronder",
            r"de hellingshoek plus \(90^{\circ}\)",
            r"altijd \(90^{\circ}\), want een gevel staat recht",
        ],
        antwoord=0,
        uitleg=r"Je stelt beide vlakken op met hun vergelijking en rekent met de normaalvectoren. De hellingshoek met de grond is een andere hoek.",
    ),
]
