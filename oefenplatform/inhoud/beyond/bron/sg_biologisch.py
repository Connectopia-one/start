# -*- coding: utf-8 -*-
"""Ontwikkeling: de biologische en de psychodynamische benadering.

Twee van de zes benaderingen uit de fiche. Ze staan samen in één thema omdat ze
beide ver van de omgeving af beginnen: de biologische bij de genen, de
psychodynamische bij wat binnen in iemand speelt.

De namen en de lijstjes staan letterlijk in de fiche:

    biologische benadering
        evolutionaire psychologie: Charles Darwin
        rijpingstheorie: Arnold Gesell
        epigenetica: Conrad Waddington
    psychodynamische benadering
        psychoanalyse: Sigmund Freud - 5 fasen, erogene lichaamszone, fixatie
        psychosociale ontwikkelingstheorie: Erik Erikson - 8 fasen, crisis,
            positieve pool, negatieve pool

De fiche vraagt bij elke benadering hetzelfde: wat is ze, wie hoort erbij, en
wat antwoordt ze op de drie basisvragen uit het vorige thema. Die drie vragen
komen hier dus terug.

Deel 1 is de biologische benadering.
Deel 2 is de psychodynamische benadering.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar begint de biologische benadering van ontwikkeling?",
        opties=[
            "bij wat in het lichaam en de genen van iemand zit",
            "bij wat iemand in zijn jeugd heeft meegemaakt",
            "bij de belonigen en straffen die iemand krijgt",
            "bij de cultuur waarin iemand opgroeit",
        ],
        antwoord=0,
        uitleg="De biologische benadering legt het begin van ontwikkeling in het lichaam zelf: genen, rijping en erfelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie theorieën horen volgens de fiche bij de biologische benadering?",
        opties=[
            "de evolutionaire psychologie",
            "de rijpingstheorie",
            "de epigenetica",
            "de psychoanalyse",
            "de sociaal-culturele theorie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie, met Darwin, Gesell en Waddington. De psychoanalyse is psychodynamisch, de sociaal-culturele theorie is systemisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de evolutionaire psychologie?",
        opties=[
            "Charles Darwin",
            "Arnold Gesell",
            "Conrad Waddington",
            "Sigmund Freud",
        ],
        antwoord=0,
        uitleg="Darwin. De evolutionaire psychologie kijkt naar gedrag dat onze voorouders hielp overleven en dat daarom is doorgegeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de rijpingstheorie?",
        opties=[
            "Arnold Gesell",
            "Charles Darwin",
            "Erik Erikson",
            "Conrad Waddington",
        ],
        antwoord=0,
        uitleg="Gesell. Zijn rijpingstheorie zegt dat ontwikkeling van binnenuit komt en een vaste orde volgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de epigenetica?",
        opties=[
            "Conrad Waddington",
            "Arnold Gesell",
            "Charles Darwin",
            "Albert Bandura",
        ],
        antwoord=0,
        uitleg="Waddington. De epigenetica kijkt hoe de omgeving genen aan of uit zet, zonder de genen zelf te veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort de epigenetica bij de biologische benadering en niet bij de omgevingstheorieën?",
        opties=[
            "omdat ze de omgeving laat werken via de genen zelf",
            "omdat ze de omgeving volledig buiten beschouwing laat",
            "omdat ze alleen onderzoek bij dieren gebruikt",
            "omdat ze de hele ontwikkeling bij de geboorte vastlegt",
        ],
        antwoord=0,
        uitleg="De epigenetica vertrekt bij de genen. De omgeving doet mee, maar haar werk loopt langs het aan- en uitzetten van genen.",
    ),
    dict(
        type="invultekst",
        vraag="De theorie van Gesell die zegt dat ontwikkeling van binnenuit en in een vaste orde verloopt, heet de ...",
        antwoord=["rijpingstheorie", "rijping"],
        uitleg="De rijpingstheorie. Ze sluit aan bij het woord rijpen uit het eerste thema.",
    ),
    dict(
        type="waarofniet",
        vraag="De rijpingstheorie van Gesell geeft op de eerste basisvraag eerder het antwoord discontinu, want ze werkt met vaste stappen in een vaste orde.",
        antwoord=True,
        uitleg="Waar. Vaste stappen die je bij elk kind in dezelfde orde ziet, horen bij discontinuïteit.",
    ),
    dict(
        type="waarofniet",
        vraag="De evolutionaire psychologie van Darwin legt vooral de nadruk op nurture.",
        antwoord=False,
        uitleg="Niet waar. Ze legt de nadruk op nature: gedrag dat is doorgegeven omdat het hielp overleven en voortplanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker legt uit dat baby's over de hele wereld bang worden van een plots hard geluid, omdat dat onze voorouders hielp overleven. Welke theorie gebruikt zij?",
        opties=[
            "de evolutionaire psychologie",
            "de rijpingstheorie",
            "de epigenetica",
            "de psychoanalyse",
        ],
        antwoord=0,
        uitleg="Overleven en doorgeven aan de volgende generatie zijn de woorden van de evolutionaire psychologie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker toont dat zware stress bij een moeder tijdens de zwangerschap bepaalde genen van het kind anders doet werken. Welke theorie gebruikt hij?",
        opties=[
            "de epigenetica",
            "de evolutionaire psychologie",
            "de rijpingstheorie",
            "het behaviorisme",
        ],
        antwoord=0,
        uitleg="Genen die door de omgeving anders gaan werken: dat is precies het terrein van de epigenetica.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consultatiebureau heeft een tabel met op welke leeftijd kinderen gemiddeld zitten, kruipen en stappen. Bij welke theorie sluit zo'n tabel het best aan?",
        opties=[
            "de rijpingstheorie",
            "de epigenetica",
            "de evolutionaire psychologie",
            "de sociaal-cognitieve leertheorie",
        ],
        antwoord=0,
        uitleg="Gesell werkte juist met zulke gemiddelde leeftijden, omdat rijping volgens hem bij elk kind dezelfde orde volgt.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de epigenetica verandert de omgeving de genen zelf, zodat de letters van het DNA anders komen te staan.",
        antwoord=False,
        uitleg="Niet waar. De epigenetica gaat over genen die aan of uit gezet worden. Het DNA zelf blijft hetzelfde.",
    ),
    dict(
        type="waarofniet",
        vraag="De drie theorieën van de biologische benadering antwoorden niet alle drie hetzelfde op de drie basisvragen.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt ze juist te vergelijken: de epigenetica laat veel meer plaats voor de omgeving dan de rijpingstheorie.",
    ),
    dict(
        type="invultekst",
        vraag="De tak van de biologische benadering die onderzoekt hoe de omgeving genen aan of uit zet, heet de ...",
        antwoord=["epigenetica"],
        uitleg="De epigenetica, met Conrad Waddington als naam in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zeggen de drie theorieën van de biologische benadering samen over de derde basisvraag?",
        opties=[
            "ze leggen de nadruk op wat universeel is bij alle mensen",
            "ze leggen de nadruk op wat per cultuur verschilt",
            "ze vinden de derde basisvraag niet van toepassing",
            "ze geven er alle drie precies hetzelfde antwoord op",
        ],
        antwoord=0,
        uitleg="Wat in het lichaam en de genen zit, geldt in principe voor alle mensen. De biologische benadering kijkt dus vooral naar het universele.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerkracht zegt over een kleuter: zijn hand is nog niet klaar om te schrijven, dat rijpt nog. Welke benadering hoor je?",
        opties=[
            "de biologische",
            "de psychodynamische",
            "de behavioristische",
            "de systemische",
        ],
        antwoord=0,
        uitleg="Rijpen van het lichaam is een biologisch argument. Oefenen zou een behavioristisch argument zijn.",
    ),
    dict(
        type="invultekst",
        vraag="De naam uit de fiche bij de evolutionaire psychologie is Charles ...",
        antwoord=["Darwin"],
        uitleg="Charles Darwin. De fiche zet bij elke theorie één naam, en die namen wisselen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bezwaar tegen een benadering die ontwikkeling volledig biologisch verklaart?",
        opties=[
            "ze geeft te weinig plaats aan opvoeding en omgeving",
            "ze geeft te veel plaats aan opvoeding en omgeving",
            "ze kan het verschil tussen groeien en rijpen niet maken",
            "ze werkt niet met levensloopfasen of vaste leeftijden",
        ],
        antwoord=0,
        uitleg="Wie alles bij de genen legt, krijgt het moeilijk om uit te leggen waarom twee kinderen met dezelfde genen zo anders opgroeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee tweelingen met hetzelfde DNA groeien op in een ander gezin en krijgen een ander karakter. Welke theorie van de biologische benadering kan dat het best verklaren?",
        opties=[
            "de epigenetica",
            "de rijpingstheorie",
            "de evolutionaire psychologie",
            "geen van de drie",
        ],
        antwoord=0,
        uitleg="De epigenetica laat ruimte voor de omgeving: dezelfde genen kunnen anders aan of uit staan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar kijkt de psychodynamische benadering naar?",
        opties=[
            "naar wat binnen in iemand speelt en drijft",
            "naar het zichtbare gedrag en de gevolgen ervan",
            "naar de systemen rond een kind",
            "naar de genen en de rijping van het lichaam",
        ],
        antwoord=0,
        uitleg="Psychodynamisch betekent dat er krachten binnen in iemand werken en dat die de ontwikkeling in beweging zetten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee theorieën horen volgens de fiche bij de psychodynamische benadering?",
        opties=[
            "de psychoanalyse",
            "de psychosociale ontwikkelingstheorie",
            "de rijpingstheorie",
            "de informatieverwerkingstheorie",
        ],
        antwoord=[0, 1],
        uitleg="De psychoanalyse van Freud en de psychosociale ontwikkelingstheorie van Erikson.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel ontwikkelingsfasen onderscheidt Freud volgens de fiche?",
        opties=[
            "vijf",
            "acht",
            "vier",
            "negen",
        ],
        antwoord=0,
        uitleg="Freud heeft vijf fasen, Erikson acht. Dat verschil wordt vaak gevraagd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel ontwikkelingsfasen onderscheidt Erikson volgens de fiche?",
        opties=[
            "acht",
            "vijf",
            "zes",
            "tien",
        ],
        antwoord=0,
        uitleg="Acht, van de babytijd tot de late volwassenheid. Erikson loopt dus over het hele leven, Freud niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is bij Freud een erogene lichaamszone?",
        opties=[
            "het lichaamsdeel waar in een fase de aandacht op ligt",
            "het lichaamsdeel dat in een fase het snelst groeit",
            "de plaats waar een kind het eerst pijn voelt",
            "de spier die in een fase als eerste rijpt",
        ],
        antwoord=0,
        uitleg="Elke fase van Freud hangt aan een lichaamszone waar het plezier en de aandacht in die periode op gericht zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Freud met een fixatie?",
        opties=[
            "iemand blijft met een stuk van zich in een vroegere fase hangen",
            "iemand slaat een fase volledig over en gaat sneller verder",
            "iemand doorloopt alle fasen precies op de gewone leeftijd",
            "iemand keert na elke fase even terug naar de vorige",
        ],
        antwoord=0,
        uitleg="Bij een fixatie is een fase niet goed afgerond en blijft er iets aan die fase vastzitten, ook later in het leven.",
    ),
    dict(
        type="invultekst",
        vraag="Het woord van Freud voor blijven vasthangen in een fase die niet goed is afgerond, is een ...",
        antwoord=["fixatie"],
        uitleg="Een fixatie. De fiche noemt bij Freud drie begrippen: de vijf fasen, de erogene lichaamszone en de fixatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is bij Erikson een crisis?",
        opties=[
            "een vraag of spanning die in een fase moet worden opgelost",
            "een ramp die de hele ontwikkeling stilzet",
            "een ziekte die in een bepaalde fase vaak voorkomt",
            "een fase die een kind beter zou overslaan",
        ],
        antwoord=0,
        uitleg="Bij Erikson hoort bij elke fase een crisis: een spanning die opgelost moet worden om verder te kunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Elke fase van Erikson heeft twee uitkomsten. Hoe heten die in de fiche?",
        opties=[
            "de positieve en de negatieve pool",
            "de open en de gesloten pool",
            "de eerste en de tweede pool",
            "de hoge en de lage pool",
        ],
        antwoord=0,
        uitleg="Loopt de crisis goed af, dan komt iemand bij de positieve pool. Loopt ze slecht af, dan bij de negatieve.",
    ),
    dict(
        type="invultekst",
        vraag="De twee uitkomsten van een crisis bij Erikson heten de positieve pool en de ... pool.",
        antwoord=["negatieve", "negatieve pool"],
        uitleg="De negatieve pool. Een fase die niet goed afloopt, laat iets achter waar iemand later nog last van kan hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="De fasen van Erikson lopen door tot in de late volwassenheid.",
        antwoord=True,
        uitleg="Waar. Dat is een van de grote verschillen met Freud, bij wie de fasen in de jeugd en de adolescentie liggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Erikson moet een crisis vermeden worden, want ze schaadt de ontwikkeling.",
        antwoord=False,
        uitleg="Niet waar. Een crisis hoort bij de fase en is juist nodig. Ze goed oplossen brengt iemand naar de positieve pool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hulpverlener zoekt bij een volwassene naar iets in zijn vroege kindertijd dat nu nog doorwerkt. Bij welke benadering sluit dat aan?",
        opties=[
            "de psychodynamische",
            "de biologische",
            "de behavioristische",
            "de systemische",
        ],
        antwoord=0,
        uitleg="De vroege jeugd die later doorwerkt is de kern van de psychodynamische benadering, bij Freud en bij Erikson.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk antwoord geven Freud en Erikson op de eerste basisvraag?",
        opties=[
            "eerder discontinu, want ze werken met vaste fasen",
            "eerder continu, want ze werken met langzame groei",
            "ze geven er geen antwoord op",
            "Freud zegt continu, Erikson zegt ook continu",
        ],
        antwoord=0,
        uitleg="Vijf fasen bij Freud, acht bij Erikson, elk met een eigen vraag of zone: dat is discontinue ontwikkeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Freud en Erikson geven op de tweede basisvraag precies hetzelfde antwoord.",
        antwoord=False,
        uitleg="Niet waar. Erikson geeft veel meer plaats aan de mensen rond iemand, en daarom heet zijn theorie psychosociaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Het woord psychosociaal bij Erikson wijst erop dat hij de omgeving rond iemand meerekent.",
        antwoord=True,
        uitleg="Waar. Psycho staat voor wat binnen in iemand speelt, sociaal voor de mensen rond hem.",
    ),
    dict(
        type="invultekst",
        vraag="De theorie van Freud die bij de psychodynamische benadering hoort, heet de ...",
        antwoord=["psychoanalyse"],
        uitleg="De psychoanalyse. Erikson noemde de zijne de psychosociale ontwikkelingstheorie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zestiger kijkt terug op zijn leven en vraagt zich af of het de moeite waard was. Bij welke theorie past dat het best?",
        opties=[
            "de psychosociale ontwikkelingstheorie van Erikson",
            "de psychoanalyse van Freud",
            "de rijpingstheorie van Gesell",
            "de evolutionaire psychologie van Darwin",
        ],
        antwoord=0,
        uitleg="Erikson heeft ook fasen voor de late volwassenheid, met de vraag of iemand vrede neemt met zijn leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee bezwaren worden het vaakst tegen de psychoanalyse van Freud ingebracht?",
        opties=[
            "wat ze beschrijft, is moeilijk met onderzoek te meten",
            "ze steunt vooral op gevallen uit zijn eigen praktijk",
            "ze werkt met te veel fasen om te kunnen onthouden",
            "ze laat de vroege kindertijd volledig buiten beschouwing",
        ],
        antwoord=[0, 1],
        uitleg="Krachten die onbewust binnen in iemand werken, zijn niet rechtstreeks te meten, en Freud bouwde zijn theorie op de mensen die bij hem in behandeling waren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de biologische en de psychodynamische benadering met elkaar gemeen?",
        opties=[
            "ze leggen het begin van ontwikkeling in het individu zelf",
            "ze leggen het begin van ontwikkeling in de cultuur",
            "ze werken beide met bekrachtiging en straf",
            "ze vinden de levensloopfasen beide niet bruikbaar",
        ],
        antwoord=0,
        uitleg="Bij de ene zit de motor in de genen, bij de andere binnen in de persoon. Beide beginnen niet bij de omgeving.",
    ),
]
