# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Veilig werken, meten en onderzoek.

Hoort bij "wetenschappelijk onderzoek en STEM" van de vakfiche chemie 2de graad
doorstroomfinaliteit. Eén thema, want dit onderdeel weegt 10 % van het examen.

Deel 1 gaat over veilig en duurzaam werken, de veiligheidspictogrammen en de
P- en H-zinnen, en over het kiezen en aflezen van het juiste glaswerk en
meetinstrument. Deel 2 gaat over grootheden en eenheden, de voorvoegsels van
mega tot nano, de beduidende cijfers, en over de stappen van een
wetenschappelijk onderzoek met de criteria voor een onderzoeksvraag.

De fiche vermeldt dat men op het examen één doel over handelingen simuleert: je
legt de handeling uit in plaats van ze uit te voeren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent het pictogram met de twee druppels die een hand en een plaat aantasten?",
        opties=[
            "bijtend of corrosief",
            "ontvlambaar",
            "oxiderend",
            "gassen onder druk",
        ],
        antwoord=0,
        uitleg="Een bijtende stof veroorzaakt brandwonden op de huid en tast materialen aan. Zwavelzuur en bijtende soda horen daarbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk pictogram staat op een fles die brand kan veroorzaken of verergeren?",
        opties=[
            "het pictogram voor oxiderend",
            "het pictogram voor irriterend",
            "het pictogram voor gassen onder druk",
            "het pictogram voor explosief",
        ],
        antwoord=0,
        uitleg="Een oxiderende stof geeft zuurstof af en voedt zo een brand. Zo'n fles houd je dus weg van brandbare stoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke pictogrammen waarschuwen vooral voor schade aan je gezondheid? Kruis alles aan wat juist is.",
        opties=[
            "het pictogram voor giftig",
            "het pictogram voor langetermijngevaar voor de gezondheid",
            "het pictogram voor gassen onder druk",
            "het pictogram voor gevaar voor het aquatische milieu",
        ],
        antwoord=[0, 1],
        uitleg="Giftig werkt meteen, het langetermijnpictogram wijst op kanker, erfelijke schade of orgaanschade. De twee andere gaan over de fles zelf en over het milieu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de H-zinnen op een etiket?",
        opties=[
            "ze benoemen het gevaar van de stof",
            "ze zeggen hoe je de stof moet bewaren",
            "ze geven de prijs van de stof",
            "ze geven de molaire massa van de stof",
        ],
        antwoord=0,
        uitleg="H staat voor hazard, dus gevaar. De P-zinnen zeggen daarnaast welke voorzorgen je neemt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je morst een product op de labotafel. Wat doe je?",
        opties=[
            "onmiddellijk opkuisen volgens de voorschriften",
            "wachten tot het van zichzelf verdampt",
            "er een blad papier over leggen",
            "verder werken en het aan het einde melden",
        ],
        antwoord=0,
        uitleg="Een gemorst product kan iemand verwonden of met een andere stof reageren. Daarom ruim je het meteen op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen horen bij veilig en duurzaam werken? Kruis alles aan wat juist is.",
        opties=[
            "zuinig omgaan met chemische stoffen",
            "een meetinstrument uitzetten als je niet meet",
            "elektrische toestellen met natte handen bedienen",
            "glasscherven met de hand bij elkaar vegen",
        ],
        antwoord=[0, 1],
        uitleg="Zuinig werken spaart grondstoffen en afval, en een toestel uitzetten spaart energie. De twee andere zijn net onveilig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk glaswerk gebruik je om precies 25,0 mL af te meten?",
        opties=[
            "een volpipet",
            "een maatbeker",
            "een erlenmeyer",
            "een proefbuis",
        ],
        antwoord=0,
        uitleg="Een volpipet is voor één volume gemaakt en dus heel nauwkeurig. Een maatbeker geeft maar een ruwe aanduiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een maatkolf?",
        opties=[
            "een oplossing tot een nauwkeurig volume aanvullen",
            "een vloeistof opwarmen boven een vlam",
            "een neerslag van een vloeistof scheiden",
            "een vaste stof fijnmaken",
        ],
        antwoord=0,
        uitleg="Een maatkolf heeft één streepje op de nek. Vul je tot daar, dan heb je precies het volume dat erop staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee maak je een vaste stof fijn in het labo?",
        opties=[
            "met een mortier en stamper",
            "met een scheitrechter",
            "met een liebigkoeler",
            "met een pipetzuiger",
        ],
        antwoord=0,
        uitleg="In een mortier wrijf je de stof met de stamper fijn. Kleinere deeltjes lossen daarna sneller op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lees je het volume in een maatcilinder correct af?",
        opties=[
            "op ooghoogte, onderaan de holle vloeistofspiegel",
            "van boven af, met de cilinder in je hand",
            "bovenaan de vloeistofspiegel, op tafel",
            "aan de buitenkant van het glas",
        ],
        antwoord=0,
        uitleg="Water vormt een holle spiegel, de meniscus. Je leest het laagste punt af, en op ooghoogte om geen kijkfout te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet een volume van ongeveer 40 mL afmeten. Welk instrument kies je?",
        opties=[
            "een maatcilinder van 50 mL",
            "een maatcilinder van 500 mL",
            "een volpipet van 10 mL",
            "een maatkolf van 1 L",
        ],
        antwoord=0,
        uitleg="Je kiest een instrument waarvan het meetbereik net boven je volume ligt. Een te grote cilinder leest veel grover af.",
    ),
    dict(
        type="waarofniet",
        vraag="In een labo eet en drink je niet.",
        antwoord=True,
        uitleg="Er kunnen sporen van stoffen op je handen of op het glaswerk zitten. Daarom blijft eten en drinken buiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof die je niet kan benoemen, mag je voorzichtig ruiken om ze te herkennen.",
        antwoord=False,
        uitleg="Sommige dampen zijn al bij één keer inademen schadelijk. Een onbekende stof ruik of smaak je nooit.",
    ),
    dict(
        type="waarofniet",
        vraag="Je houdt je altijd aan het meetbereik van een meetinstrument.",
        antwoord=True,
        uitleg="Buiten het bereik is de meting niet geldig en kan het toestel beschadigen. Een balans van 200 g belast je dus niet met een kilo.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bunsenbrander laat je gerust even onbewaakt branden.",
        antwoord=False,
        uitleg="Een open vlam kan altijd iets doen ontvlammen. Je zet hem uit of blijft erbij.",
    ),
    dict(
        type="waarofniet",
        vraag="Chemisch afval giet je niet gewoon in de gootsteen.",
        antwoord=True,
        uitleg="Het kan het water vervuilen of in de leiding reageren. Elk soort afval gaat in zijn eigen vat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het kegelvormige glas met een nauwe hals waarin je kan zwenken zonder te morsen?",
        antwoord=["erlenmeyer", "een erlenmeyer", "de erlenmeyer"],
        uitleg="Door de nauwe hals blijft de vloeistof binnen als je ze ronddraait. Daarom gebruikt men hem bij een titratie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk toestel gebruik je om de massa van een staal te bepalen?",
        antwoord=["balans", "een balans", "de balans"],
        uitleg="Je zet eerst het weegschuitje op nul en weegt dan de stof erin.",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor staat de P in de P-zinnen op een etiket?",
        antwoord=["voorzorg", "precaution", "voorzorgsmaatregel"],
        uitleg="De P-zinnen zeggen wat je moet doen om veilig met de stof om te gaan, de H-zinnen benoemen het gevaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het trechtervormige glas met een kraantje, waarmee je twee vloeistoflagen scheidt?",
        antwoord=["scheitrechter", "een scheitrechter", "de scheitrechter"],
        uitleg="Met het kraantje laat je de onderste laag eruit lopen en stop je op tijd.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van massa?",
        opties=[
            "de kilogram",
            "de gram",
            "de newton",
            "de mol",
        ],
        antwoord=0,
        uitleg="De kilogram is de SI-eenheid, ook al reken je in het labo meestal in gram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van volume?",
        opties=[
            "de kubieke meter",
            "de liter",
            "de milliliter",
            "de kubieke centimeter",
        ],
        antwoord=0,
        uitleg="De kubieke meter is de SI-eenheid. De liter wordt ernaast nog veel gebruikt en is een duizendste kubieke meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorvoegsels staan voor een waarde kleiner dan één? Kruis alles aan wat juist is.",
        opties=[
            "milli",
            "nano",
            "kilo",
            "mega",
        ],
        antwoord=[0, 1],
        uitleg="Milli is een duizendste en nano een miljardste. Kilo is duizend keer en mega een miljoen keer de eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 2,5 mg in gram?",
        opties=[
            "0,0025 g",
            "0,025 g",
            "2500 g",
            "0,25 g",
        ],
        antwoord=0,
        uitleg="Milli betekent een duizendste, dus deel je door duizend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel beduidende cijfers heeft het getal 0,00340?",
        opties=[
            "drie",
            "twee",
            "vijf",
            "zes",
        ],
        antwoord=0,
        uitleg="De nullen vooraan tellen niet mee, de nul achteraan wel. Dus 3, 4 en 0 zijn de beduidende cijfers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je 0,00450 in wetenschappelijke notatie?",
        opties=[
            "4,50.10⁻³",
            "45,0.10⁻⁴",
            "4,50.10³",
            "0,450.10⁻²",
        ],
        antwoord=0,
        uitleg="In de wetenschappelijke notatie staat er één cijfer verschillend van nul voor de komma. De drie beduidende cijfers blijven bewaard.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt het volume van een oplossing en de concentratie wordt gehalveerd. Welk verband is dat?",
        opties=[
            "omgekeerd evenredig",
            "recht evenredig",
            "lineair met een snijpunt",
            "kwadratisch",
        ],
        antwoord=0,
        uitleg="Bij een omgekeerd evenredig verband blijft het product van de twee grootheden constant. Dat product is hier het aantal mol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een wetenschappelijk onderzoek? Kruis alles aan wat juist is.",
        opties=[
            "een onderzoeksvraag opstellen",
            "een hypothese formuleren",
            "de meetwaarden aanpassen aan de hypothese",
            "de conclusie vooraf vastleggen",
        ],
        antwoord=[0, 1],
        uitleg="Een vraag en een hypothese horen bij het begin van het onderzoek. Metingen aanpassen of de conclusie vooraf vastleggen is geen onderzoek meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium dat een onderzoeksvraag enkelvoudig moet zijn?",
        opties=[
            "ze gaat over één onderwerp",
            "ze heeft één woord nodig als antwoord",
            "ze kan met ja of nee beantwoord worden",
            "ze hoort bij één schoolvak",
        ],
        antwoord=0,
        uitleg="Onderzoek je twee dingen tegelijk, dan weet je achteraf niet waaraan het resultaat ligt. Dus splits je de vraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium dat een onderzoeksvraag objectief moet zijn?",
        opties=[
            "ze laat geen overtuiging of mening doorschemeren",
            "ze gaat over een meetbare grootheid",
            "ze is in één zin te noteren",
            "ze is al eens eerder onderzocht",
        ],
        antwoord=0,
        uitleg="Een vraag als waarom is dit middel het beste, legt het antwoord al vast. Een objectieve vraag laat beide uitkomsten open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling stelt als onderzoeksvraag: wanneer werd zuurstof ontdekt? Wat is daar het probleem mee?",
        opties=[
            "het is een opzoekvraag en geen onderzoeksvraag",
            "de vraag is niet objectief geformuleerd",
            "de vraag gaat over te veel onderwerpen",
            "de vraag is niet haalbaar binnen de tijd",
        ],
        antwoord=0,
        uitleg="Het antwoord ligt al in een boek. Een onderzoeksvraag moet je met een proef of met eigen metingen kunnen beantwoorden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grootheid noteer je altijd samen met haar eenheid.",
        antwoord=True,
        uitleg="Zonder eenheid betekent een getal niets: vier kan vier gram of vier kilogram zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meting met een instrument is exact.",
        antwoord=False,
        uitleg="Elk instrument heeft een beperkte nauwkeurigheid, dus is er altijd een onzekerheid. Daarom noteer je het juiste aantal beduidende cijfers.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de horizontale as van een grafiek zet je de grootheid die je zelf instelt.",
        antwoord=True,
        uitleg="Dat is de onafhankelijke variabele. De grootheid die je meet, komt op de verticale as.",
    ),
    dict(
        type="waarofniet",
        vraag="Een weerlegde hypothese betekent dat je onderzoek mislukt is.",
        antwoord=False,
        uitleg="Een hypothese is een verwachting die je toetst. Blijkt ze niet te kloppen, dan heb je iets geleerd en is het onderzoek geslaagd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een centimeter is een honderdste van een meter.",
        antwoord=True,
        uitleg="Centi staat voor 10⁻², dus een honderdste.",
    ),
    dict(
        type="invultekst",
        vraag="Welke waarde hoort bij het voorvoegsel kilo?",
        antwoord=["1000", "10^3", "duizend"],
        uitleg="Kilo staat voor 10³, dus duizend keer de eenheid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is 0,75 L in mL?",
        antwoord=["750", "750 mL"],
        uitleg="Eén liter is duizend milliliter, dus 0,75 keer duizend is 750 mL.",
    ),
    dict(
        type="invultekst",
        vraag="Voor welke discipline staat de M in de afkorting STEM?",
        antwoord=["wiskunde", "de wiskunde", "mathematics"],
        uitleg="STEM staat voor wetenschappen, technologie, ingenieurswetenschappen en wiskunde. Je zet die vier samen in om een probleem op te lossen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een beredeneerde verwachting die je met een proef wil toetsen?",
        antwoord=["hypothese", "een hypothese", "de hypothese"],
        uitleg="Een hypothese is geen gok: je baseert ze op wat je al weet.",
    ),
]
