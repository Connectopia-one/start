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
        opties=["180", "90", "270", "360"],
        antwoord=0,
        uitleg="Ken je twee hoeken, dan volgt de derde daar meteen uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je de sinusregel?",
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
        vraag="Hoeveel graden is pi radialen? Schrijf het getal.",
        antwoord=["180", "honderdtachtig"],
        uitleg="Een halve cirkel is pi radialen en ook honderdtachtig graden. Daaruit volgt elke andere omzetting.",
    ),
    dict(
        type="waarofniet",
        vraag="De cosinusregel is een veralgemening van de stelling van Pythagoras.",
        antwoord=True,
        uitleg="Bij een rechte hoek is de cosinus nul, dus valt de laatste term weg en blijft Pythagoras over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de cosinusregel voor zijde a tegenover hoek A?",
        opties=[
            "a kwadraat is b kwadraat plus c kwadraat min twee bc maal de cosinus van A",
            "a kwadraat is b kwadraat plus c kwadraat plus twee bc maal de cosinus van A",
            "a kwadraat is b kwadraat min c kwadraat min twee bc maal de cosinus van A",
            "a is b plus c min twee maal b maal c maal de cosinus van hoek A",
        ],
        antwoord=0,
        uitleg="De hoek in de formule is altijd de hoek tegenover de zijde die je zoekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel radialen is negentig graden?",
        opties=[
            "pi gedeeld door twee",
            "pi gedeeld door drie",
            "pi gedeeld door vier",
            "twee maal pi",
        ],
        antwoord=0,
        uitleg="Pi radialen is honderdtachtig graden, dus de helft daarvan is pi op twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén radiaal is ongeveer zevenenvijftig graden.",
        antwoord=True,
        uitleg="Honderdtachtig gedeeld door pi is ongeveer 57,3.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden is twee pi radialen? Schrijf het getal.",
        antwoord=["360", "driehonderdzestig"],
        uitleg="Twee pi radialen is een volledige omwenteling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke straal heeft de goniometrische cirkel?",
        opties=["één", "twee", "pi", "honderdtachtig"],
        antwoord=0,
        uitleg="Door de straal op één te zetten, zijn de coördinaten van het beeldpunt meteen de cosinus en de sinus.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de goniometrische cirkel is de cosinus van een hoek de y-coördinaat van het beeldpunt.",
        antwoord=False,
        uitleg="De cosinus is de x-coördinaat en de sinus de y-coördinaat. Die twee verwisselen is de klassieke fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor welke hoek tussen nul en honderdtachtig graden is de sinus gelijk aan één?",
        opties=[
            "negentig graden",
            "nul graden",
            "zestig graden",
            "honderdtachtig graden",
        ],
        antwoord=0,
        uitleg="Het beeldpunt ligt dan bovenaan de cirkel, met y-coördinaat één.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de sinus van dertig graden? Schrijf het als breuk.",
        antwoord=["1/2"],
        uitleg="Dertig graden is een van de hoeken die je uit het hoofd moet kennen. De cosinus van zestig graden is hetzelfde getal.",
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
            "de sinus in het kwadraat plus de cosinus in het kwadraat is één",
            "de sinus in het kwadraat min de cosinus in het kwadraat is één",
            "de sinus plus de cosinus van dezelfde hoek is gelijk aan één",
            "de sinus gedeeld door de cosinus van die hoek is gelijk aan één",
        ],
        antwoord=0,
        uitleg="Ze volgt rechtstreeks uit Pythagoras op de goniometrische cirkel met straal één. De sinus gedeeld door de cosinus is de tangens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de cosinus van nul graden?",
        opties=["één", "nul", "min één", "een half"],
        antwoord=0,
        uitleg="Het beeldpunt ligt dan helemaal rechts op de cirkel, met x-coördinaat één.",
    ),
    dict(
        type="waarofniet",
        vraag="De sinus van een hoek kan groter zijn dan één.",
        antwoord=False,
        uitleg="De sinus is een coördinaat op een cirkel met straal één, dus ze blijft altijd tussen min één en één. De tangens kent die grens niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden is pi gedeeld door drie radialen? Schrijf het getal.",
        antwoord=["60", "zestig"],
        uitleg="Honderdtachtig gedeeld door drie is zestig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee hoeken zijn tegengesteld. Wat geldt voor hun goniometrische getallen?",
        opties=[
            "dezelfde cosinus, tegengestelde sinus",
            "dezelfde sinus, tegengestelde cosinus",
            "allebei dezelfde sinus en cosinus",
            "allebei een tegengestelde sinus en cosinus",
        ],
        antwoord=0,
        uitleg="Het beeldpunt spiegelt om de horizontale as, dus de x-coördinaat blijft en de y-coördinaat wisselt van teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zet je een hoek in graden om naar radialen?",
        opties=[
            "vermenigvuldigen met pi en delen door honderdtachtig",
            "vermenigvuldigen met honderdtachtig en delen door pi",
            "vermenigvuldigen met twee pi en delen door honderd",
            "delen door pi en daarna vermenigvuldigen met zestig",
        ],
        antwoord=0,
        uitleg="De andere kant op doe je net het omgekeerde. Zet altijd eerst je rekenapp in de juiste stand.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de amplitude van drie maal de sinus van x?",
        opties=["drie", "één", "zes", "twee pi"],
        antwoord=0,
        uitleg="De amplitude is de factor voor de sinus, dus de afstand van de evenwichtslijn tot de top.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de periode van de sinus van twee x?",
        opties=["pi", "twee pi", "vier pi", "een half"],
        antwoord=0,
        uitleg="De gewone periode twee pi wordt gedeeld door de factor voor x, dus hier door twee.",
    ),
    dict(
        type="invultekst",
        vraag="Welke evenwichtslijn heeft de grafiek van de sinus van x, plus vier? Schrijf de y-waarde.",
        antwoord=["4", "vier"],
        uitleg="De hele grafiek schuift vier omhoog, dus ze schommelt rond de rechte y is vier.",
    ),
    dict(
        type="waarofniet",
        vraag="De periode van de gewone sinusfunctie is twee pi.",
        antwoord=True,
        uitleg="Na één volledige omwenteling op de goniometrische cirkel begint het beeld opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het getal c in a maal de sinus van b maal x min c, plus d?",
        opties=[
            "het zorgt voor een horizontale verschuiving",
            "het zorgt voor een verticale verschuiving",
            "het bepaalt de amplitude van de grafiek",
            "het bepaalt de periode van de grafiek",
        ],
        antwoord=0,
        uitleg="Dat heet de faseverschuiving. Het getal d schuift verticaal en bepaalt de evenwichtslijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van twee maal de sinus van x, plus één?",
        opties=[
            "van min één tot en met drie",
            "van min twee tot en met twee",
            "van nul tot en met drie",
            "van min drie tot en met drie",
        ],
        antwoord=0,
        uitleg="De sinus loopt van min één tot één, maal twee geeft min twee tot twee, plus één schuift alles één omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag="De amplitude van een sinusfunctie kan negatief zijn.",
        antwoord=False,
        uitleg="De amplitude is een afstand, dus altijd positief. Een negatieve factor voor de sinus spiegelt de grafiek wel om de evenwichtslijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel keer korter is de periode van de sinus van drie x dan die van de gewone sinus? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="De factor voor x perst de grafiek samen: ze doorloopt haar beeld drie keer zo snel.",
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
        uitleg="Ken je de sinus, dan haal je er de cosinus uit, op het teken na. Dat teken bepaal je met het kwadrant.",
    ),
    dict(
        type="waarofniet",
        vraag="De sinus van min x is gelijk aan min de sinus van x.",
        antwoord=True,
        uitleg="De sinus is een oneven functie: haar grafiek is symmetrisch om de oorsprong. De cosinus is even.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee hoeken zijn supplementair, hun som is dus honderdtachtig graden. Wat geldt dan?",
        opties=[
            "dezelfde sinus, tegengestelde cosinus",
            "dezelfde cosinus, tegengestelde sinus",
            "allebei dezelfde sinus en cosinus",
            "de sinus van de ene is de cosinus van de andere",
        ],
        antwoord=0,
        uitleg="Het beeldpunt spiegelt om de verticale as: de hoogte blijft, de x-coördinaat keert. Het laatste antwoord hoort bij complementaire hoeken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel nulwaarden heeft de sinus van x tussen nul en twee pi, de grenzen inbegrepen? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="In nul, in pi en in twee pi. De grafiek kruist de as dus drie keer op dat interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de verdubbelingsformule voor de sinus?",
        opties=[
            "de sinus van twee x is twee maal de sinus van x maal de cosinus van x",
            "de sinus van twee x is gewoon twee keer de sinus van de hoek x",
            "de sinus van twee x is de sinus van de hoek x in het kwadraat, maal twee",
            "de sinus van twee x is de sinus van x plus de cosinus van x",
        ],
        antwoord=0,
        uitleg="Ze volgt uit de somformule met twee gelijke hoeken. Gewoon maal twee werkt niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De cosinus van twee x is gelijk aan twee maal de cosinus van x.",
        antwoord=False,
        uitleg="De juiste formule is de cosinus in het kwadraat min de sinus in het kwadraat. Een goniometrisch getal is geen factor die je zomaar buiten haalt.",
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
        uitleg="De frequentie is één gedeeld door de periode. De hoogte van de top is de amplitude.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sinusfunctie is een geschikt model voor het getij aan de kust.",
        antwoord=True,
        uitleg="Het water stijgt en daalt met een vaste periode rond een gemiddeld peil. Dat is precies wat een sinusfunctie beschrijft.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de grootste waarde van vijf maal de sinus van x? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="De sinus wordt hoogstens één, dus de functie hoogstens vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee hoeken zijn complementair, hun som is dus negentig graden. Wat geldt dan?",
        opties=[
            "de sinus van de ene is de cosinus van de andere",
            "ze hebben allebei precies dezelfde sinus",
            "ze hebben allebei een tegengestelde cosinus",
            "hun sinussen zijn samen gelijk aan het getal één",
        ],
        antwoord=0,
        uitleg="In een rechthoekige driehoek zijn de twee scherpe hoeken complementair, en daar zie je het meteen: de overstaande zijde van de ene is de aanliggende van de andere.",
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
