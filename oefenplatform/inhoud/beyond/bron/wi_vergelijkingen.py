# -*- coding: utf-8 -*-
"""Vergelijkingen en ongelijkheden oplossen.

Uit de analysefiche G1. De fiche is hier streng in wat algebraïsch moet en wat
grafisch mag: vergelijkingen los je grafisch én algebraïsch op, ongelijkheden
grafisch, en alleen tweedegraadsongelijkheden ook algebraïsch.

Deel 1 zijn de vergelijkingen, met de bestaansvoorwaarden die bij wortels en
logaritmen horen. Deel 2 zijn de ongelijkheden en het tekenverloop.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarmee komen de oplossingen van een vergelijking van de vorm f van x is nul overeen op de grafiek?",
        opties=[
            "de snijpunten met de horizontale as",
            "het snijpunt met de verticale as",
            "de hoogste punten van de grafiek",
            "de punten waar de grafiek vlak loopt",
        ],
        antwoord=0,
        uitleg="De oplossingen zijn net de nulwaarden, en die zie je waar de grafiek de x-as snijdt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af als je f van x is g van x grafisch oplost?",
        opties=[
            "de x-waarden van de gemeenschappelijke punten",
            "de y-waarden van de gemeenschappelijke punten",
            "de snijpunten van beide grafieken met de y-as",
            "de afstand tussen de twee grafieken in elk punt",
        ],
        antwoord=0,
        uitleg="Op een snijpunt zijn beide functiewaarden gelijk. De oplossing is de x, niet de y.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel reële oplossingen heeft x kwadraat is negen? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="Drie en min drie. Alleen de wortel nemen en min drie vergeten is hier de klassieke fout.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vergelijking grafisch oplossen geeft altijd een exact antwoord.",
        antwoord=False,
        uitleg="Grafisch lees je meestal een benadering af. Wil je exact werken, dan moet je algebraïsch oplossen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de bestaansvoorwaarde bij de vierkantswortel uit x min drie?",
        opties=[
            "x is groter dan of gelijk aan drie",
            "x is strikt groter dan het getal drie",
            "x is kleiner dan of gelijk aan drie",
            "x is verschillend van het getal drie",
        ],
        antwoord=0,
        uitleg="Wat onder een even wortel staat, mag niet negatief zijn. Nul mag wel, want de wortel uit nul bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt beide leden van een irrationale vergelijking gekwadrateerd. Wat moet je zeker nog doen?",
        opties=[
            "elke gevonden oplossing in de oorspronkelijke vergelijking controleren",
            "elke gevonden oplossing van teken laten veranderen voor je ze noteert",
            "nog een tweede keer kwadrateren om de wortel helemaal weg te werken",
            "de bestaansvoorwaarde achteraf laten vallen, want je kwadrateerde al",
        ],
        antwoord=0,
        uitleg="Kwadrateren is geen gelijkwaardige bewerking: het kan oplossingen bijmaken die in de oorspronkelijke vergelijking niet kloppen.",
    ),
    dict(
        type="waarofniet",
        vraag="Door te kwadrateren kan je oplossingen bijkrijgen die niet aan de oorspronkelijke vergelijking voldoen.",
        antwoord=True,
        uitleg="Min twee en twee hebben hetzelfde kwadraat. Na kwadrateren kan een negatief lid dus onzichtbaar meeglippen.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: twee tot de macht x is acht. Schrijf de waarde van x.",
        antwoord=["3", "drie"],
        uitleg="Acht is twee tot de derde, dus x is drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de bestaansvoorwaarde bij de logaritme van x min twee?",
        opties=[
            "x is strikt groter dan het getal twee",
            "x is groter dan of gelijk aan twee",
            "x is strikt groter dan het getal nul",
            "x is verschillend van het getal twee",
        ],
        antwoord=0,
        uitleg="Het argument van een logaritme moet strikt positief zijn. Nul mag hier dus niet, anders dan bij een wortel.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de logaritme van x gelijk is aan de logaritme van y, en beide bestaan, dan is x gelijk aan y.",
        antwoord=True,
        uitleg="De logaritmische functie is strikt stijgend, dus elke waarde hoort bij precies één argument.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vertelt de discriminant van een tweedegraadsvergelijking je?",
        opties=[
            "hoeveel reële oplossingen ze heeft",
            "hoe groot de grootste oplossing is",
            "waar de top van de parabool ligt",
            "of de parabool naar boven opent",
        ],
        antwoord=0,
        uitleg="Positief geeft twee oplossingen, nul geeft er één, negatief geen enkele. De opening lees je af aan het teken van a.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de discriminant van x kwadraat plus twee x plus één? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Vier min vier is nul, dus er is precies één oplossing: min één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van: de wortel uit x plus één is gelijk aan x min één?",
        opties=["x is drie", "x is nul", "x is één", "x is vier"],
        antwoord=0,
        uitleg="Kwadrateren geeft x kwadraat min drie x is nul, dus nul of drie. Nul valt weg, want dan zou de wortel min één moeten zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="In die vergelijking is nul ook een geldige oplossing.",
        antwoord=False,
        uitleg="Vul nul in: links staat de wortel uit één, dus één, rechts min één. Dat klopt niet. Nul is een valse oplossing van het kwadrateren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel reële oplossingen heeft de vergelijking sinus x is nul?",
        opties=[
            "oneindig veel",
            "precies twee",
            "precies één",
            "geen enkele",
        ],
        antwoord=0,
        uitleg="De sinusfunctie is periodiek, dus de nulwaarden herhalen zich telkens na pi.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe los je drie tot de macht twee x is drie tot de macht x plus vier op?",
        opties=[
            "de exponenten gelijkstellen, dat geeft x is vier",
            "de grondtallen gelijkstellen, dat geeft x is drie",
            "van beide leden de logaritme van vier nemen",
            "beide leden door het getal drie delen, dan is x twee",
        ],
        antwoord=0,
        uitleg="Bij gelijke grondtallen moeten de exponenten gelijk zijn: twee x is x plus vier, dus x is vier.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke vergelijking van de vorm f van x is nul heeft minstens één reële oplossing.",
        antwoord=False,
        uitleg="Neem x kwadraat plus één. Die functie wordt nooit nul, want haar grafiek blijft boven de x-as.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: vijf x min twintig is nul. Schrijf de waarde van x.",
        antwoord=["4", "vier"],
        uitleg="Twintig gedeeld door vijf is vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stap kan je oplossingen doen verliezen?",
        opties=[
            "beide leden delen door een uitdrukking met x",
            "bij beide leden hetzelfde getal optellen",
            "beide leden met het getal twee vermenigvuldigen",
            "de termen binnen één lid van plaats wisselen",
        ],
        antwoord=0,
        uitleg="Die uitdrukking kan nul zijn, en dan gooi je net die oplossing weg. Breng alles naar één lid en ontbind in plaats daarvan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost een vergelijking op met de grafische rekenapp. Wat noteer je als oplossing?",
        opties=[
            "de x-waarden van de snijpunten",
            "de y-waarden van de snijpunten",
            "de coördinaten van beide toppen",
            "de hellingen van de twee grafieken",
        ],
        antwoord=0,
        uitleg="De oplossingenverzameling bestaat uit x-waarden. De y-waarde hoort bij het punt, niet bij de oplossing.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent f van x groter dan nul op de grafiek?",
        opties=[
            "de grafiek ligt boven de horizontale as",
            "de grafiek ligt boven de verticale as",
            "de grafiek stijgt op dat hele stuk",
            "de grafiek ligt onder de horizontale as",
        ],
        antwoord=0,
        uitleg="Het teken van de functiewaarde is de hoogte ten opzichte van de x-as. Stijgen is iets anders: dat gaat over de richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent f van x kleiner dan g van x op de grafiek?",
        opties=[
            "de grafiek van f ligt onder die van g",
            "de grafiek van f ligt boven die van g",
            "de grafiek van f daalt sneller dan die van g",
            "de grafiek van f snijdt die van g in twee punten",
        ],
        antwoord=0,
        uitleg="Je leest af op welke intervallen de ene kromme onder de andere loopt. De snijpunten zijn de grenzen.",
    ),
    dict(
        type="invultekst",
        vraag="De oplossing van x kwadraat min vier kleiner dan of gelijk aan nul is een interval. Schrijf de linkergrens.",
        antwoord=["-2", "min 2"],
        uitleg="De nulwaarden zijn min twee en twee, en tussen de nulwaarden is de dalparabool negatief. De oplossing is dus min twee tot en met twee.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je beide leden van een ongelijkheid door een negatief getal deelt, draait het ongelijkheidsteken om.",
        antwoord=True,
        uitleg="Twee is kleiner dan vier, maar min twee is groter dan min vier. Dat omdraaien vergeten is de meest gemaakte fout van dit hoofdstuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van x kwadraat min vijf x plus zes groter dan nul?",
        opties=[
            "x kleiner dan twee, of x groter dan drie",
            "x groter dan twee en x kleiner dan drie",
            "x kleiner dan drie, of x groter dan twee",
            "x groter dan twee, of x groter dan drie",
        ],
        antwoord=0,
        uitleg="De nulwaarden zijn twee en drie, en a is positief, dus de parabool ligt boven de x-as buiten dat interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tweedegraadsfunctie heeft positieve a en twee nulwaarden. Waar is ze negatief?",
        opties=[
            "tussen de twee nulwaarden in",
            "buiten de twee nulwaarden",
            "links van de kleinste nulwaarde",
            "nergens, want a is positief",
        ],
        antwoord=0,
        uitleg="Bij een dalparabool duikt de grafiek net tussen de nulwaarden onder de x-as.",
    ),
    dict(
        type="waarofniet",
        vraag="De ongelijkheid x kwadraat plus één groter dan nul geldt voor elke reële x.",
        antwoord=True,
        uitleg="Een kwadraat is nooit negatief, dus de som met één is altijd minstens één. De discriminant is negatief en de parabool ligt volledig boven de as.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel reële oplossingen heeft x kwadraat kleiner dan nul? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg="Een kwadraat is nooit strikt negatief, dus de oplossingenverzameling is leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noteer je dat x tussen min twee en twee ligt, grenzen inbegrepen?",
        opties=[
            "als een gesloten interval van min twee tot twee",
            "als een open interval van min twee tot twee",
            "als de vereniging van twee losse intervallen",
            "als het interval van nul tot en met twee",
        ],
        antwoord=0,
        uitleg="Grenzen inbegrepen betekent vierkante haken aan beide kanten. Bij een strikte ongelijkheid zouden ze open staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ongelijkheid van de vijfde graad moet je op het examen algebraïsch kunnen oplossen.",
        antwoord=False,
        uitleg="Ongelijkheden los je grafisch op. Alleen de tweedegraadsongelijkheid moet je ook algebraïsch aankunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van twee x min zes groter dan nul?",
        opties=[
            "x groter dan drie",
            "x kleiner dan drie",
            "x groter dan zes",
            "x kleiner dan min drie",
        ],
        antwoord=0,
        uitleg="Zes erbij en door twee delen. Je deelt door een positief getal, dus het teken blijft staan.",
    ),
    dict(
        type="invultekst",
        vraag="De oplossing van drie x plus negen kleiner dan nul is x kleiner dan een getal. Welk getal?",
        antwoord=["-3", "min 3"],
        uitleg="Negen eraf en door drie delen geeft x kleiner dan min drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een tweedegraadsongelijkheid?",
        opties=[
            "alles naar één lid brengen zodat er nul overblijft",
            "beide leden door de coëfficiënt van x kwadraat delen",
            "de wortel trekken uit beide leden van de ongelijkheid",
            "het ongelijkheidsteken meteen laten omdraaien",
        ],
        antwoord=0,
        uitleg="Pas met nul in het andere lid kan je nulwaarden zoeken en een tekenschema maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ongelijkheid heeft hoogstens twee oplossingen.",
        antwoord=False,
        uitleg="De oplossing van een ongelijkheid is meestal een heel interval, dus oneindig veel getallen. Een vergelijking heeft losse oplossingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van: x min één, maal x plus twee, kleiner dan nul?",
        opties=[
            "x tussen min twee en één",
            "x tussen min één en twee",
            "x kleiner dan min twee of groter dan één",
            "x kleiner dan min één of groter dan twee",
        ],
        antwoord=0,
        uitleg="Een product is negatief als de factoren een verschillend teken hebben, en dat is net tussen de nulwaarden min twee en één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tweedegraadsfunctie heeft negatieve a en twee nulwaarden. Waar is ze positief?",
        opties=[
            "tussen de twee nulwaarden in",
            "buiten de twee nulwaarden",
            "rechts van de grootste nulwaarde",
            "nergens, want a is negatief",
        ],
        antwoord=0,
        uitleg="Bij een bergparabool ligt net het middenstuk boven de x-as.",
    ),
    dict(
        type="waarofniet",
        vraag="De oplossing van f van x groter dan of gelijk aan g van x lees je af waar de grafiek van f boven of op die van g ligt.",
        antwoord=True,
        uitleg="De snijpunten horen er dan bij, want daar zijn de twee functiewaarden gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel nulwaarden zet je in het tekenschema van x kwadraat min negen? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="Min drie en drie. Die twee verdelen de getallenas in de drie stukken van het schema.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je een ongelijkheid niet zomaar met x vermenigvuldigen?",
        opties=[
            "omdat het teken van x niet gekend is",
            "omdat x een onbekende en geen getal is",
            "omdat vermenigvuldigen oplossingen bijmaakt",
            "omdat de graad daardoor te hoog wordt",
        ],
        antwoord=0,
        uitleg="Is x negatief, dan moet het ongelijkheidsteken omdraaien, en is x nul, dan klopt er niets meer. Breng alles naar één lid in plaats daarvan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van x kwadraat groter dan of gelijk aan negen?",
        opties=[
            "x kleiner dan of gelijk aan min drie, of x groter dan of gelijk aan drie",
            "x groter dan of gelijk aan min drie en kleiner dan of gelijk aan drie",
            "x groter dan of gelijk aan drie, en verder niets",
            "x groter dan of gelijk aan negen, of kleiner dan min negen",
        ],
        antwoord=0,
        uitleg="Breng alles naar één lid: x kwadraat min negen groter dan of gelijk aan nul. Buiten de nulwaarden min drie en drie ligt de dalparabool boven de as.",
    ),
]
