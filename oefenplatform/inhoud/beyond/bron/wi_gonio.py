# -*- coding: utf-8 -*-
"""Goniometrie en de goniometrische functies.

Het onderdeel "Goniometrische functies en goniometrie" van de analysefiche G1.
Dat bestaat uit drie stukken: driehoeken oplossen met de sinus- en de
cosinusregel, de goniometrische cirkel met de radiaal, en de algemene
sinusfunctie met haar kenmerken en de goniometrische formules.

Deel 1 is de meetkunde: driehoeken, de cirkel en de radiaal.
Deel 2 is de sinusfunctie en het rekenwerk met goniometrische formules.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel graden is de som van de hoeken in een driehoek?",
        opties=[r"\(180^\circ\)", r"\(90^\circ\)", r"\(270^\circ\)", r"\(360^\circ\)"],
        antwoord=0,
        uitleg=r"Ken je twee hoeken, dan volgt de derde daar meteen uit: "
        r"\(\widehat{C} = 180^\circ - \widehat{A} - \widehat{B}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wanneer gebruik je de sinusregel \(\dfrac{a}{\sin A} = \dfrac{b}{\sin B}\)?",
        opties=[
            "als je een zijde kent samen met de hoek ertegenover",
            "als je de drie zijden van de driehoek al kent",
            "als je twee zijden kent en ook de hoek ertussen",
            "als de driehoek ergens een rechte hoek bevat",
        ],
        antwoord=0,
        uitleg="De sinusregel koppelt telkens een zijde aan de hoek ertegenover. Zonder zo'n paar kom je er niet mee verder.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel graden is \(\pi\) radialen? Schrijf het getal.",
        antwoord=["180", "honderdtachtig"],
        uitleg=r"Een halve cirkel is \(\pi\) radialen en ook \(180^\circ\). Daaruit volgt elke andere omzetting.",
    ),
    dict(
        type="waarofniet",
        vraag="De cosinusregel is een veralgemening van de stelling van Pythagoras.",
        antwoord=True,
        uitleg=r"Bij \(\widehat{A} = 90^\circ\) is \(\cos A = 0\), dus valt de laatste term weg en "
        r"blijft \(a^{2} = b^{2} + c^{2}\) over.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe luidt de cosinusregel voor zijde \(a\) tegenover hoek \(A\)?",
        opties=[
            r"\(a^{2} = b^{2} + c^{2} - 2bc\cos A\)",
            r"\(a^{2} = b^{2} + c^{2} + 2bc\cos A\)",
            r"\(a^{2} = b^{2} - c^{2} - 2bc\cos A\)",
            r"\(a = b + c - 2bc\cos A\)",
        ],
        antwoord=0,
        uitleg="De hoek in de formule is altijd de hoek tegenover de zijde die je zoekt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel radialen is \(90^\circ\)?",
        opties=[
            r"\(\dfrac{\pi}{2}\)",
            r"\(\dfrac{\pi}{3}\)",
            r"\(\dfrac{\pi}{4}\)",
            r"\(2\pi\)",
        ],
        antwoord=0,
        uitleg=r"\(\pi\) radialen is \(180^\circ\), dus de helft daarvan is \(\dfrac{\pi}{2}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Eén radiaal is ongeveer \(57^\circ\).",
        antwoord=True,
        uitleg=r"\(\dfrac{180}{\pi} \approx 57{,}3\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel graden is \(2\pi\) radialen? Schrijf het getal.",
        antwoord=["360", "driehonderdzestig"],
        uitleg=r"\(2\pi\) radialen is een volledige omwenteling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke straal heeft de goniometrische cirkel?",
        opties=[r"\(1\)", r"\(2\)", r"\(\pi\)", r"\(180\)"],
        antwoord=0,
        uitleg=r"Door de straal op \(1\) te zetten, zijn de coördinaten van het beeldpunt meteen "
        r"\((\cos\alpha,\ \sin\alpha)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Op de goniometrische cirkel is \(\cos\alpha\) de \(y\)-coördinaat van het beeldpunt.",
        antwoord=False,
        uitleg=r"\(\cos\alpha\) is de \(x\)-coördinaat en \(\sin\alpha\) de \(y\)-coördinaat. Die "
        r"twee verwisselen is de klassieke fout.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke hoek tussen \(0^\circ\) en \(180^\circ\) is \(\sin\alpha = 1\)?",
        opties=[
            r"\(90^\circ\)",
            r"\(0^\circ\)",
            r"\(60^\circ\)",
            r"\(180^\circ\)",
        ],
        antwoord=0,
        uitleg=r"Het beeldpunt ligt dan bovenaan de cirkel, met \(y\)-coördinaat \(1\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\sin 30^\circ\)? Schrijf het als breuk.",
        antwoord=["1/2"],
        uitleg=r"\(30^\circ\) is een van de hoeken die je uit het hoofd moet kennen. "
        r"\(\cos 60^\circ\) is hetzelfde getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent twee zijden van een driehoek en de hoek ertussen. Welke regel gebruik je?",
        opties=[
            "de cosinusregel",
            "de sinusregel",
            "de stelling van Pythagoras",
            "de som van de hoeken",
        ],
        antwoord=0,
        uitleg="Er is geen zijde met haar overstaande hoek bekend, dus de sinusregel kan niet. De cosinusregel wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je de drie zijden van een driehoek kent, kan je met de sinusregel meteen een hoek berekenen.",
        antwoord=False,
        uitleg="De sinusregel heeft altijd één gekende hoek nodig. Met drie zijden begin je met de cosinusregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de grondformule van de goniometrie?",
        opties=[
            r"\(\sin^{2}x + \cos^{2}x = 1\)",
            r"\(\sin^{2}x - \cos^{2}x = 1\)",
            r"\(\sin x + \cos x = 1\)",
            r"\(\dfrac{\sin x}{\cos x} = 1\)",
        ],
        antwoord=0,
        uitleg=r"Ze volgt rechtstreeks uit Pythagoras op de goniometrische cirkel met straal \(1\). "
        r"\(\dfrac{\sin x}{\cos x}\) is de tangens.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\cos 0^\circ\)?",
        opties=[r"\(1\)", r"\(0\)", r"\(-1\)", r"\(\tfrac{1}{2}\)"],
        antwoord=0,
        uitleg=r"Het beeldpunt ligt dan helemaal rechts op de cirkel, met \(x\)-coördinaat \(1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin\alpha\) kan groter zijn dan \(1\).",
        antwoord=False,
        uitleg=r"De sinus is een coördinaat op een cirkel met straal \(1\), dus "
        r"\(-1 \leq \sin\alpha \leq 1\). De tangens kent die grens niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel graden is \(\dfrac{\pi}{3}\) radialen? Schrijf het getal.",
        antwoord=["60", "zestig"],
        uitleg=r"\(\dfrac{180}{3} = 60\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee hoeken zijn tegengesteld: \(\alpha\) en \(-\alpha\). Wat geldt voor hun goniometrische getallen?",
        opties=[
            "dezelfde cosinus, tegengestelde sinus",
            "dezelfde sinus, tegengestelde cosinus",
            "allebei dezelfde sinus en cosinus",
            "allebei een tegengestelde sinus en cosinus",
        ],
        antwoord=0,
        uitleg=r"Het beeldpunt spiegelt om de horizontale as, dus \(\cos(-\alpha) = \cos\alpha\) en "
        r"\(\sin(-\alpha) = -\sin\alpha\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zet je een hoek in graden om naar radialen?",
        opties=[
            r"vermenigvuldigen met \(\dfrac{\pi}{180}\)",
            r"vermenigvuldigen met \(\dfrac{180}{\pi}\)",
            r"vermenigvuldigen met \(\dfrac{2\pi}{100}\)",
            r"delen door \(\pi\), dan maal \(60\)",
        ],
        antwoord=0,
        uitleg="De andere kant op doe je net het omgekeerde. Zet altijd eerst je rekenapp in de juiste stand.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de amplitude van \(y = 3\sin x\)?",
        opties=[r"\(3\)", r"\(1\)", r"\(6\)", r"\(2\pi\)"],
        antwoord=0,
        uitleg="De amplitude is de factor voor de sinus, dus de afstand van de evenwichtslijn tot de top.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de periode van \(y = \sin 2x\)?",
        opties=[r"\(\pi\)", r"\(2\pi\)", r"\(4\pi\)", r"\(\tfrac{1}{2}\)"],
        antwoord=0,
        uitleg=r"De gewone periode \(2\pi\) wordt gedeeld door de factor voor \(x\), dus hier door \(2\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Welke evenwichtslijn heeft de grafiek van \(y = \sin x + 4\)? Schrijf de \(y\)-waarde.",
        antwoord=["4", "vier"],
        uitleg=r"De hele grafiek schuift vier omhoog, dus ze schommelt rond de rechte \(y = 4\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De periode van \(y = \sin x\) is \(2\pi\).",
        antwoord=True,
        uitleg="Na één volledige omwenteling op de goniometrische cirkel begint het beeld opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat doet \(c\) in \(y = a\sin(bx - c) + d\)?",
        opties=[
            "het zorgt voor een horizontale verschuiving",
            "het zorgt voor een verticale verschuiving",
            "het bepaalt de amplitude van de grafiek",
            "het bepaalt de periode van de grafiek",
        ],
        antwoord=0,
        uitleg=r"Dat heet de faseverschuiving. Het getal \(d\) schuift verticaal en bepaalt de evenwichtslijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het bereik van \(y = 2\sin x + 1\)?",
        opties=[
            r"\([-1,\ 3]\)",
            r"\([-2,\ 2]\)",
            r"\([0,\ 3]\)",
            r"\([-3,\ 3]\)",
        ],
        antwoord=0,
        uitleg=r"\(\sin x\) loopt van \(-1\) tot \(1\), maal \(2\) geeft \(-2\) tot \(2\), plus "
        r"\(1\) schuift alles één omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag="De amplitude van een sinusfunctie kan negatief zijn.",
        antwoord=False,
        uitleg="De amplitude is een afstand, dus altijd positief. Een negatieve factor voor de sinus spiegelt de grafiek wel om de evenwichtslijn.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel keer korter is de periode van \(y = \sin 3x\) dan die van \(y = \sin x\)? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"De factor voor \(x\) perst de grafiek samen: ze doorloopt haar beeld drie keer zo snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je de grondformule van de goniometrie het vaakst?",
        opties=[
            "om de ene goniometrische functie in de andere om te zetten",
            "om de zijden van een willekeurige driehoek te berekenen",
            "om graden naar radialen om te zetten en terug",
            "om de periode van een sinusfunctie te vinden",
        ],
        antwoord=0,
        uitleg=r"Ken je \(\sin x\), dan haal je \(\cos x = \pm\sqrt{1 - \sin^{2}x}\) eruit. Dat "
        r"teken bepaal je met het kwadrant.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sin(-x) = -\sin x\).",
        antwoord=True,
        uitleg="De sinus is een oneven functie: haar grafiek is symmetrisch om de oorsprong. De cosinus is even.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee hoeken zijn supplementair, hun som is dus \(180^\circ\). Wat geldt dan?",
        opties=[
            "dezelfde sinus, tegengestelde cosinus",
            "dezelfde cosinus, tegengestelde sinus",
            "allebei dezelfde sinus en cosinus",
            "de sinus van de ene is de cosinus van de andere",
        ],
        antwoord=0,
        uitleg=r"Het beeldpunt spiegelt om de verticale as: \(\sin(180^\circ - \alpha) = \sin\alpha\) "
        r"en \(\cos(180^\circ - \alpha) = -\cos\alpha\). Het laatste antwoord hoort bij "
        r"complementaire hoeken.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel nulwaarden heeft \(y = \sin x\) op \([0,\ 2\pi]\), de grenzen inbegrepen? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"In \(0\), in \(\pi\) en in \(2\pi\). De grafiek kruist de as dus drie keer op dat interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de verdubbelingsformule voor de sinus?",
        opties=[
            r"\(\sin 2x = 2\sin x\cos x\)",
            r"\(\sin 2x = 2\sin x\)",
            r"\(\sin 2x = 2\sin^{2}x\)",
            r"\(\sin 2x = \sin x + \cos x\)",
        ],
        antwoord=0,
        uitleg="Ze volgt uit de somformule met twee gelijke hoeken. Gewoon maal twee werkt niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\cos 2x = 2\cos x\).",
        antwoord=False,
        uitleg=r"De juiste formule is \(\cos 2x = \cos^{2}x - \sin^{2}x\). Een goniometrisch getal "
        r"is geen factor die je zomaar buiten haalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen de formules van Simpson?",
        opties=[
            "ze zetten een som van sinussen om in een product",
            "ze zetten een product van sinussen om in een macht",
            "ze berekenen de oppervlakte onder een sinusgrafiek",
            "ze zetten graden om in radialen en omgekeerd",
        ],
        antwoord=0,
        uitleg="Ze heten daarom ook de som-naar-productformules. Handig om een vergelijking te ontbinden in factoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de frequentie van een periodieke functie?",
        opties=[
            "het aantal volledige schommelingen per eenheid",
            "de hoogte van de top boven de evenwichtslijn",
            "de tijd die één volledige schommeling duurt",
            "de verschuiving ten opzichte van de gewone sinus",
        ],
        antwoord=0,
        uitleg=r"De frequentie is \(f = \dfrac{1}{T}\). De hoogte van de top is de amplitude.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sinusfunctie is een geschikt model voor het getij aan de kust.",
        antwoord=True,
        uitleg="Het water stijgt en daalt met een vaste periode rond een gemiddeld peil. Dat is precies wat een sinusfunctie beschrijft.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de grootste waarde van \(y = 5\sin x\)? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"\(\sin x\) wordt hoogstens \(1\), dus de functie hoogstens \(5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee hoeken zijn complementair, hun som is dus \(90^\circ\). Wat geldt dan?",
        opties=[
            "de sinus van de ene is de cosinus van de andere",
            "ze hebben allebei precies dezelfde sinus",
            "ze hebben allebei een tegengestelde cosinus",
            "hun sinussen zijn samen gelijk aan één",
        ],
        antwoord=0,
        uitleg=r"\(\sin(90^\circ - \alpha) = \cos\alpha\). In een rechthoekige driehoek zijn de twee "
        r"scherpe hoeken complementair, en daar zie je het meteen: de overstaande zijde van de ene "
        r"is de aanliggende van de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bewijs je een goniometrische identiteit?",
        opties=[
            "door één lid te herleiden tot het andere met bekende formules",
            "door in beide leden een paar hoeken in te vullen die kloppen",
            "door beide leden te kwadrateren tot ze gelijk worden",
            "door de grafieken van beide leden te laten tekenen",
        ],
        antwoord=0,
        uitleg="Enkele hoeken invullen toont alleen dat ze daar klopt, niet dat ze altijd klopt. Een grafiek is een aanwijzing, geen bewijs.",
    ),
]
