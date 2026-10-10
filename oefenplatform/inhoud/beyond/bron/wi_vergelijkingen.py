# -*- coding: utf-8 -*-
r"""Vergelijkingen en ongelijkheden oplossen.

Uit de analysefiche G1. De fiche is hier streng in wat algebraïsch moet en wat
grafisch mag: vergelijkingen los je grafisch én algebraïsch op, ongelijkheden
grafisch, en alleen tweedegraadsongelijkheden ook algebraïsch.

Deel 1 zijn de vergelijkingen, met de bestaansvoorwaarden die bij wortels en
logaritmen horen. Deel 2 zijn de ongelijkheden en het tekenverloop.

In echte wiskundige notatie, tussen \( en \); zie oefenplatform/lib/wiskunde.ts.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Waarmee komen de oplossingen van \(f(x)=0\) overeen op de grafiek?",
        opties=[
            r"de snijpunten met de \(x\)-as",
            r"het snijpunt met de \(y\)-as",
            r"de hoogste punten van de grafiek",
            r"de punten waar de grafiek vlak loopt",
        ],
        antwoord=0,
        uitleg=r"De oplossingen zijn net de nulwaarden, en die zie je waar de grafiek de \(x\)-as snijdt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat lees je af als je \(f(x)=g(x)\) grafisch oplost?",
        opties=[
            r"de \(x\)-waarden van de snijpunten",
            r"de \(y\)-waarden van de snijpunten",
            r"de snijpunten van beide grafieken met de \(y\)-as",
            r"de afstand tussen de twee grafieken in elk punt",
        ],
        antwoord=0,
        uitleg=r"Op een snijpunt zijn beide functiewaarden gelijk. De oplossing is de \(x\), niet de \(y\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel reële oplossingen heeft \(x^{2}=9\)? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"\(x=3\) en \(x=-3\). Alleen de wortel nemen en \(-3\) vergeten is hier de klassieke fout.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vergelijking grafisch oplossen geeft altijd een exact antwoord.",
        antwoord=False,
        uitleg=r"Grafisch lees je meestal een benadering af. Wil je exact werken, dan moet je algebraïsch oplossen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de bestaansvoorwaarde bij \(\sqrt{x-3}\)?",
        opties=[r"\(x\geq 3\)", r"\(x>3\)", r"\(x\leq 3\)", r"\(x\neq 3\)"],
        antwoord=0,
        uitleg=r"Wat onder een even wortel staat, mag niet negatief zijn. \(x=3\) mag wel, want \(\sqrt{0}=0\) bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je hebt beide leden van een irrationale vergelijking gekwadrateerd. Wat moet je zeker nog doen?",
        opties=[
            r"elke gevonden oplossing in de oorspronkelijke vergelijking controleren",
            r"elke gevonden oplossing van teken laten veranderen voor je ze noteert",
            r"nog een tweede keer kwadrateren om de wortel helemaal weg te werken",
            r"de bestaansvoorwaarde laten vallen, want je kwadrateerde al",
        ],
        antwoord=0,
        uitleg=r"Kwadrateren is geen gelijkwaardige bewerking: het kan oplossingen bijmaken die in de oorspronkelijke vergelijking niet kloppen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Door te kwadrateren kan je oplossingen bijkrijgen die niet aan de oorspronkelijke vergelijking voldoen.",
        antwoord=True,
        uitleg=r"\(-2\) en \(2\) hebben hetzelfde kwadraat. Na kwadrateren kan een negatief lid dus onzichtbaar meeglippen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(2^{x}=8\). Schrijf de waarde van \(x\).",
        antwoord=["3", "drie"],
        uitleg=r"\(8=2^{3}\), dus \(x=3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de bestaansvoorwaarde bij \(\log(x-2)\)?",
        opties=[r"\(x>2\)", r"\(x\geq 2\)", r"\(x>0\)", r"\(x\neq 2\)"],
        antwoord=0,
        uitleg=r"Het argument van een logaritme moet strikt positief zijn. \(x=2\) mag hier dus niet, anders dan bij een wortel.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(\log x=\log y\) en beide bestaan, dan is \(x=y\).",
        antwoord=True,
        uitleg=r"De logaritmische functie is strikt stijgend, dus elke waarde hoort bij precies één argument.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat vertelt de discriminant \(D=b^{2}-4ac\) je?",
        opties=[
            r"hoeveel reële oplossingen de vergelijking heeft",
            r"hoe groot de grootste oplossing is",
            r"waar de top van de parabool ligt",
            r"of de parabool naar boven opent",
        ],
        antwoord=0,
        uitleg=r"\(D>0\) geeft twee oplossingen, \(D=0\) één, \(D<0\) geen enkele. De opening lees je af aan het teken van \(a\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is de discriminant van \(x^{2}+2x+1\)? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg=r"\(D=4-4=0\), dus er is precies één oplossing: \(x=-1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(\sqrt{x+1}=x-1\).",
        opties=[r"\(x=3\)", r"\(x=0\)", r"\(x=1\)", r"\(x=4\)"],
        antwoord=0,
        uitleg=r"Kwadrateren geeft \(x+1=x^{2}-2x+1\), dus \(x^{2}-3x=0\) en \(x=0\) of \(x=3\). \(x=0\) valt weg, want dan zou \(\sqrt{1}=-1\) moeten zijn.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(x=0\) is een oplossing van \(\sqrt{x+1}=x-1\).",
        antwoord=False,
        uitleg=r"Vul in: links \(\sqrt{1}=1\), rechts \(-1\). Dat klopt niet. \(x=0\) is een valse oplossing die bij het kwadrateren ontstond.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(3^{2x}=3^{x+4}\).",
        opties=[
            r"de exponenten gelijkstellen, dat geeft \(x=4\)",
            r"de grondtallen gelijkstellen, dat geeft \(x=3\)",
            r"van beide leden \(\log 4\) nemen",
            r"beide leden door \(3\) delen, dan is \(x=2\)",
        ],
        antwoord=0,
        uitleg=r"Bij gelijke grondtallen moeten de exponenten gelijk zijn: \(2x=x+4\), dus \(x=4\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke vergelijking van de vorm \(f(x)=0\) heeft minstens één reële oplossing.",
        antwoord=False,
        uitleg=r"Neem \(f(x)=x^{2}+1\). Die wordt nooit \(0\), want haar grafiek blijft boven de \(x\)-as.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \(|x-1|=3\) heeft twee oplossingen.",
        antwoord=True,
        uitleg=r"\(x-1=3\) geeft \(x=4\), en \(x-1=-3\) geeft \(x=-2\). Een absolute waarde splitst in twee gevallen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(\log_{2}(x+3)=\log_{2}(2x-1)\). Schrijf de waarde van \(x\).",
        antwoord=["4", "vier"],
        uitleg=r"Gelijke logaritmen geven \(x+3=2x-1\), dus \(x=4\). Controleer het domein: \(7>0\) en \(7>0\), dus het klopt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke stap kan oplossingen doen verliezen?",
        opties=[
            r"beide leden delen door een uitdrukking met \(x\)",
            r"bij beide leden hetzelfde getal optellen",
            r"beide leden met \(2\) vermenigvuldigen",
            r"de termen binnen één lid van plaats wisselen",
        ],
        antwoord=0,
        uitleg=r"Die uitdrukking kan \(0\) zijn, en dan gooi je net die oplossing weg. Breng alles naar één lid en ontbind in plaats daarvan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke \(m\) heeft \(x^{2}-4x+m=0\) precies één oplossing?",
        opties=[r"\(m=4\)", r"\(m=-4\)", r"\(m=2\)", r"\(m=16\)"],
        antwoord=0,
        uitleg=r"Precies één oplossing wil zeggen \(D=0\): \(16-4m=0\), dus \(m=4\). De vergelijking wordt dan \((x-2)^{2}=0\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(f(x)>0\) op de grafiek?",
        opties=[
            r"de grafiek ligt boven de \(x\)-as",
            r"de grafiek ligt rechts van de \(y\)-as",
            r"de grafiek stijgt op dat hele stuk",
            r"de grafiek ligt onder de \(x\)-as",
        ],
        antwoord=0,
        uitleg=r"Het teken van de functiewaarde is de hoogte ten opzichte van de \(x\)-as. Stijgen is iets anders: dat gaat over de richting.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(f(x)<g(x)\) op de grafiek?",
        opties=[
            r"de grafiek van \(f\) ligt onder die van \(g\)",
            r"de grafiek van \(f\) ligt boven die van \(g\)",
            r"de grafiek van \(f\) daalt sneller dan die van \(g\)",
            r"de grafieken snijden elkaar in twee punten",
        ],
        antwoord=0,
        uitleg=r"Je leest af op welke intervallen de ene kromme onder de andere loopt. De snijpunten zijn de grenzen.",
    ),
    dict(
        type="invultekst",
        vraag=r"De oplossing van \(x^{2}-4\leq 0\) is een interval. Schrijf de linkergrens.",
        antwoord=["-2", "min 2"],
        uitleg=r"De nulwaarden zijn \(-2\) en \(2\), en tussen de nulwaarden ligt de dalparabool onder de as. De oplossing is \(\left[-2,2\right]\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Deel je beide leden van een ongelijkheid door een negatief getal, dan draait het ongelijkheidsteken om.",
        antwoord=True,
        uitleg=r"\(2<4\), maar \(-2>-4\). Dat omdraaien vergeten is de meest gemaakte fout van dit hoofdstuk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(x^{2}-5x+6>0\)?",
        opties=[
            r"\(x<2\) of \(x>3\)",
            r"\(2<x<3\)",
            r"\(x<3\) of \(x>2\)",
            r"\(x>2\) of \(x>3\)",
        ],
        antwoord=0,
        uitleg=r"De nulwaarden zijn \(2\) en \(3\), en \(a>0\), dus de parabool ligt boven de \(x\)-as buiten dat interval.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tweedegraadsfunctie heeft \(a>0\) en twee nulwaarden. Waar is ze negatief?",
        opties=[
            r"tussen de twee nulwaarden in",
            r"buiten de twee nulwaarden",
            r"links van de kleinste nulwaarde",
            r"nergens, want \(a>0\)",
        ],
        antwoord=0,
        uitleg=r"Bij een dalparabool duikt de grafiek net tussen de nulwaarden onder de \(x\)-as.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(x^{2}+1>0\) geldt voor elke \(x\in\mathbb{R}\).",
        antwoord=True,
        uitleg=r"Een kwadraat is nooit negatief, dus de som met \(1\) is altijd minstens \(1\). \(D=-4<0\) en de parabool ligt volledig boven de as.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel reële oplossingen heeft \(x^{2}<0\)? Schrijf het cijfer.",
        antwoord=["0", "nul", "geen"],
        uitleg=r"Een kwadraat is nooit strikt negatief, dus de oplossingenverzameling is leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe noteer je \(-2\leq x\leq 2\) als interval?",
        opties=[
            r"\(\left[-2,2\right]\)",
            r"\(\left]-2,2\right[\)",
            r"\(\left]-\infty,-2\right]\cup\left[2,+\infty\right[\)",
            r"\(\left[0,2\right]\)",
        ],
        antwoord=0,
        uitleg=r"Grenzen inbegrepen betekent vierkante haken die naar binnen wijzen. Bij een strikte ongelijkheid zouden ze omgekeerd staan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een ongelijkheid van de vijfde graad moet je op het examen algebraïsch kunnen oplossen.",
        antwoord=False,
        uitleg=r"Ongelijkheden los je grafisch op. Alleen de tweedegraadsongelijkheid moet je ook algebraïsch aankunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(2x-6>0\)?",
        opties=[r"\(x>3\)", r"\(x<3\)", r"\(x>6\)", r"\(x<-3\)"],
        antwoord=0,
        uitleg=r"\(2x>6\), en delen door \(2\) is delen door een positief getal, dus het teken blijft staan.",
    ),
    dict(
        type="invultekst",
        vraag=r"De oplossing van \(3x+9<0\) is \(x<\) een getal. Welk getal?",
        antwoord=["-3", "min 3"],
        uitleg=r"\(3x<-9\), dus \(x<-3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de eerste stap bij een tweedegraadsongelijkheid?",
        opties=[
            r"alles naar één lid brengen zodat er \(0\) overblijft",
            r"beide leden door \(a\) delen",
            r"de wortel trekken uit beide leden",
            r"het ongelijkheidsteken meteen laten omdraaien",
        ],
        antwoord=0,
        uitleg=r"Pas met \(0\) in het andere lid kan je nulwaarden zoeken en een tekenschema maken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een ongelijkheid heeft hoogstens twee oplossingen.",
        antwoord=False,
        uitleg=r"De oplossing van een ongelijkheid is meestal een heel interval, dus oneindig veel getallen. Een vergelijking heeft losse oplossingen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \((x-1)(x+2)<0\)?",
        opties=[
            r"\(-2<x<1\)",
            r"\(-1<x<2\)",
            r"\(x<-2\) of \(x>1\)",
            r"\(x<-1\) of \(x>2\)",
        ],
        antwoord=0,
        uitleg=r"Een product is negatief als de factoren een verschillend teken hebben, en dat is net tussen de nulwaarden \(-2\) en \(1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tweedegraadsfunctie heeft \(a<0\) en twee nulwaarden. Waar is ze positief?",
        opties=[
            r"tussen de twee nulwaarden in",
            r"buiten de twee nulwaarden",
            r"rechts van de grootste nulwaarde",
            r"nergens, want \(a<0\)",
        ],
        antwoord=0,
        uitleg=r"Bij een bergparabool ligt net het middenstuk boven de \(x\)-as.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De oplossing van \(f(x)\geq g(x)\) lees je af waar de grafiek van \(f\) boven of op die van \(g\) ligt.",
        antwoord=True,
        uitleg=r"De snijpunten horen er dan bij, want daar zijn de twee functiewaarden gelijk.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel nulwaarden zet je in het tekenschema van \(x^{2}-9\)? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"\(-3\) en \(3\). Die twee verdelen de getallenas in de drie stukken van het schema.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom mag je een ongelijkheid niet zomaar met \(x\) vermenigvuldigen?",
        opties=[
            r"omdat het teken van \(x\) niet gekend is",
            r"omdat \(x\) een onbekende en geen getal is",
            r"omdat vermenigvuldigen oplossingen bijmaakt",
            r"omdat de graad daardoor te hoog wordt",
        ],
        antwoord=0,
        uitleg=r"Is \(x<0\), dan moet het teken omdraaien, en is \(x=0\), dan klopt er niets meer. Breng alles naar één lid in plaats daarvan.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(\dfrac{x-1}{x+2}\geq 0\)?",
        opties=[
            r"\(x<-2\) of \(x\geq 1\)",
            r"\(-2<x\leq 1\)",
            r"\(x\leq -2\) of \(x\geq 1\)",
            r"\(x\geq 1\)",
        ],
        antwoord=0,
        uitleg=r"Teller en noemer moeten hetzelfde teken hebben. In \(x=-2\) bestaat de breuk niet, dus die grens blijft open; in \(x=1\) is de breuk \(0\) en dat mag.",
    ),
]
