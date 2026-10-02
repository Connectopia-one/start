# -*- coding: utf-8 -*-
"""🌍 Beyond — Onderzoeksvaardigheden en ontwerpen.

Wetenschappelijk onderzoek en STEM, de koppen "Onderzoeksmethode", "Ontwerp van
een oplossing" en "Interactie tussen STEM-disciplines onderling en met de
maatschappij" uit de vakfiche natuurwetenschappen 3DO. Deel 1 gaat over de
stappen van een wetenschappelijk onderzoek, van probleemstelling tot conclusie.
Deel 2 gaat over het ontwerpen van een oplossing en over de wisselwerking tussen
wetenschap, techniek, wiskunde en de samenleving.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Met welke stap begint een wetenschappelijk onderzoek?",
        opties=[
            "het probleem definiëren en afbakenen",
            "de data van de proef verzamelen",
            "de conclusie van het onderzoek formuleren",
            "over de gekozen methode reflecteren",
        ],
        antwoord=0,
        uitleg="Pas als je weet wat je precies wil onderzoeken, kan je een goede onderzoeksvraag stellen. Zonder afbakening wordt je onderzoek te breed om af te werken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verwachting die je vóór het onderzoek over de uitkomst opschrijft?",
        antwoord=["hypothese", "een hypothese", "de hypothese"],
        uitleg="Een hypothese moet je kunnen testen en kan dus ook fout blijken. Dat ze fout is, maakt een onderzoek niet mislukt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak is een goede onderzoeksvraag?",
        opties=[
            "hoe hangt de valtijd van een bal af van zijn hoogte?",
            "ballen zijn heel interessant om te onderzoeken",
            "ik denk dat een bal behoorlijk snel naar beneden valt",
            "een bal valt uit zichzelf naar beneden",
        ],
        antwoord=0,
        uitleg="Een onderzoeksvraag is een echte vraag en noemt wat je verandert en wat je meet. De andere drie zijn een mening of een vaststelling.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die door het onderzoek weerlegd wordt, maakt het onderzoek waardeloos.",
        antwoord=False,
        uitleg="Ook een weerlegde hypothese levert kennis op, want je weet nu hoe het niet werkt. In je conclusie schrijf je gewoon dat de hypothese niet klopte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort er in een onderzoeksplan? Kruis alles aan wat juist is.",
        opties=[
            "welk materiaal je nodig hebt",
            "welke stappen je in welke orde zet",
            "wat je gaat meten en met welk instrument",
            "wat de uitkomst van het onderzoek is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het plan maak je vóór de metingen, dus de uitkomst kan er nog niet in staan. Die hoort bij de conclusie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de grootheid die je in een proef zelf verandert?",
        opties=[
            "de onafhankelijke variabele",
            "de afhankelijke variabele",
            "de constante variabele",
            "de conclusie",
        ],
        antwoord=0,
        uitleg="Wat je daarna meet, is de afhankelijke variabele. Alles wat je gelijk houdt, noem je de constanten.",
    ),
    dict(
        type="waarofniet",
        vraag="In een goede proef verander je één grootheid en houd je de andere gelijk.",
        antwoord=True,
        uitleg="Verander je er twee tegelijk, dan weet je achteraf niet welke het verschil veroorzaakte. Daarom is dat één van de eerste regels van een onderzoeksplan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting meerdere keren?",
        opties=[
            "om toevallige meetfouten te zien en uit te vlakken",
            "om de hypothese zeker juist te laten uitkomen",
            "om het onderzoek langer te doen duren",
            "om minder materiaal te hoeven gebruiken",
        ],
        antwoord=0,
        uitleg="Eén meting kan er net naast zitten. Door te herhalen zie je hoeveel je resultaten uit elkaar liggen en dus hoe betrouwbaar ze zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de proef zonder de behandeling, waarmee je je resultaat vergelijkt?",
        antwoord=["controleproef", "de controleproef", "blanco"],
        uitleg="Zonder zo'n vergelijking weet je niet of het verschil van jouw ingreep komt. In een labo heet dat ook een blanco.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met de data nadat je ze verzameld hebt?",
        opties=[
            "ze ordenen in een tabel of een grafiek",
            "ze meteen weggooien en opnieuw beginnen",
            "ze aanpassen tot ze bij je hypothese passen",
            "ze onveranderd als je conclusie opschrijven",
        ],
        antwoord=0,
        uitleg="Een grafiek laat een verband veel sneller zien dan een rij getallen. Data aanpassen tot ze passen, is geen wetenschap maar fraude.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meting die niet bij je hypothese past, mag je gewoon weglaten uit je resultaten.",
        antwoord=False,
        uitleg="Alle metingen horen in je verslag, ook de onverwachte. Een uitschieter mag je wel apart bespreken en verklaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan moet een goede conclusie voldoen? Kruis alles aan wat juist is.",
        opties=[
            "ze antwoordt op de onderzoeksvraag",
            "ze steunt op de verzamelde data",
            "ze zegt ook of de hypothese klopte",
            "ze bevestigt altijd de hypothese",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je conclusie is het antwoord op de vraag waarmee je begon. Dat de hypothese fout bleek, mag en moet er net in staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een wetenschappelijk onderzoek? Kruis alles aan wat juist is.",
        opties=[
            "een onderzoeksvraag opstellen",
            "data verzamelen en analyseren",
            "over je methode reflecteren en communiceren",
            "de data kiezen die bij je verwachting passen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die eerste drie staan in de rij stappen van probleemstelling tot communicatie. Selectief met je data omgaan hoort daar nooit bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort reflecteren over je methode bij het onderzoek?",
        opties=[
            "om te zien wat beter kon aan je opzet",
            "om de conclusie achteraf toch nog aan te passen",
            "om het verslag een stuk langer te maken",
            "om de hypothese achteraf te herschrijven",
        ],
        antwoord=0,
        uitleg="Je benoemt daar de zwakke punten van je opzet, zoals een te klein aantal metingen. Zo weet een lezer hoe sterk je besluit staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Communiceren over je onderzoek hoort bij de wetenschappelijke methode.",
        antwoord=True,
        uitleg="Anderen moeten je werk kunnen nalezen en overdoen. Daarom schrijf je zo nauwkeurig op wat je gedaan hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest op een grafiek twee grootheden af die samen stijgen in een rechte door de oorsprong. Wat besluit je?",
        opties=[
            "ze zijn recht evenredig met elkaar",
            "ze zijn omgekeerd evenredig met elkaar",
            "er is geen verband tussen hen",
            "het verband is kwadratisch",
        ],
        antwoord=0,
        uitleg="Een rechte door de oorsprong hoort bij een recht evenredig verband. Gaat de rechte niet door de oorsprong, dan is het verband lineair maar niet recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een tabel met meetgegevens en moet er een verband uit halen. Wat is een goede eerste stap?",
        opties=[
            "de gegevens in een grafiek uitzetten",
            "de gegevens alfabetisch ordenen",
            "de grootste waarde als antwoord nemen",
            "het gemiddelde van alle kolommen nemen",
        ],
        antwoord=0,
        uitleg="Op een grafiek zie je meteen of de punten een rechte, een parabool of een hyperbool vormen. Uit een rij getallen alleen is dat veel moeilijker te zien.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grootheid die je in een proef meet, dus het gevolg van wat je veranderde?",
        antwoord=["afhankelijke variabele", "de afhankelijke variabele"],
        uitleg="Wat je zelf instelt, is de onafhankelijke variabele. Op een grafiek zet je de onafhankelijke op de horizontale as en de afhankelijke op de verticale.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil onderzoeken of plantengroei van de hoeveelheid licht afhangt. Wat houd je gelijk?",
        opties=[
            "de soort plant, de grond en het water",
            "de hoeveelheid licht die elke plant krijgt",
            "de gemeten hoogte van elke plant",
            "de duur van het hele onderzoek per plant",
        ],
        antwoord=0,
        uitleg="Het licht is wat je juist wél verandert, dus dat kan geen constante zijn. De hoogte is wat je meet, dus de afhankelijke variabele.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeksvraag stel je pas op nadat je de metingen gedaan hebt.",
        antwoord=False,
        uitleg="De vraag komt eerst, en pas daarna het plan en de metingen. Anders weet je niet wat je moet meten en waarom.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap als je een oplossing voor een probleem moet ontwerpen?",
        opties=[
            "het probleem duidelijk definiëren",
            "het ontwerp meteen in elkaar zetten",
            "het ontwerp aan anderen voorstellen",
            "het ontwerp evalueren en bijsturen",
        ],
        antwoord=0,
        uitleg="Zonder een scherp omschreven probleem bouw je een oplossing voor de verkeerde vraag. Daarna zet je de criteria op papier.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de eisen waaraan je ontwerp moet voldoen?",
        antwoord=["criteria", "de criteria"],
        uitleg="Criteria kunnen over afmetingen, prijs, veiligheid of duurzaamheid gaan. Pas met criteria kan je achteraf beoordelen of je oplossing werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom splits je een groot probleem op in deelproblemen?",
        opties=[
            "omdat elk stuk apart makkelijker op te lossen is",
            "omdat je dan geen criteria meer nodig hebt",
            "omdat je dan niets meer hoeft te evalueren",
            "omdat je dan geen totaaloplossing meer nodig hebt",
        ],
        antwoord=0,
        uitleg="Daarna voeg je de deeloplossingen weer samen tot één geheel. Die samenvoeging is een stap op zich, want de stukken moeten bij elkaar passen.",
    ),
    dict(
        type="waarofniet",
        vraag="Nadat je je ontwerp geëvalueerd hebt, mag je het nog bijsturen.",
        antwoord=True,
        uitleg="Ontwerpen gaat in rondjes: bouwen, testen, aanpassen, opnieuw testen. Een eerste versie is bijna nooit ook de beste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het ontwerpen van een oplossing? Kruis alles aan wat juist is.",
        opties=[
            "het probleem definiëren",
            "criteria opstellen",
            "de oplossing evalueren en bijsturen",
            "de criteria achteraf aanpassen aan het resultaat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je criteria naar je resultaat toeschrijven, maakt de evaluatie zinloos. Dan voldoet elke oplossing achteraf altijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dienen de criteria aan het einde van een ontwerpproces?",
        opties=[
            "om te beoordelen of je oplossing volstaat",
            "om het probleem opnieuw te gaan definiëren",
            "om de deelproblemen alsnog te bedenken",
            "om het materiaal voor het ontwerp te bestellen",
        ],
        antwoord=0,
        uitleg="Je legt je oplossing naast elk criterium en kijkt of ze eraan voldoet. Lukt dat niet, dan stuur je het ontwerp bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor elk probleem moet je een volledig nieuw systeem ontwerpen.",
        antwoord=False,
        uitleg="Een bestaand systeem aanpassen is vaak sneller, goedkoper en duurzamer. Alleen als dat echt niet volstaat, ontwerp je iets helemaal nieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de letters STEM?",
        opties=[
            "wetenschappen, techniek, engineering en wiskunde",
            "wetenschappen, techniek, economie en maatschappij",
            "statistiek, techniek, elektronica en metingen",
            "wetenschappen, taal, ethiek en maatschappij",
        ],
        antwoord=0,
        uitleg="In het Engels staat het voor science, technology, engineering en mathematics. De vier samen leveren vaak een betere oplossing dan elk apart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke STEM-disciplines waren er nodig om een vaccin tegen corona te ontwikkelen en te verdelen? Kruis alles aan wat juist is.",
        opties=[
            "wetenschappelijke kennis om het vaccin te maken",
            "technologische kennis om het koel te houden",
            "wiskundige kennis om de verspreiding te volgen",
            "geen enkele, het ging alleen maar om geluk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat is precies waarom STEM als één geheel bekeken wordt. Geen van die drie had alleen tot een werkend vaccin bij de mensen geleid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beïnvloedt de samenleving het wetenschappelijk onderzoek?",
        opties=[
            "uitdagingen bepalen mee waar onderzoek naar gaat",
            "de samenleving bepaalt de uitkomst van een proef",
            "de samenleving verandert de natuurwetten zelf",
            "de samenleving heeft er helemaal geen invloed op",
        ],
        antwoord=0,
        uitleg="Klimaat, gezondheid en energie trekken geld en aandacht naar bepaalde onderzoeken. De uitkomst van een proef blijft natuurlijk wel wat ze is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nieuwe techniek kan nieuw wetenschappelijk onderzoek mogelijk maken.",
        antwoord=True,
        uitleg="Een betere microscoop of een snellere computer opent onderzoek dat vroeger onmogelijk was. De wisselwerking werkt dus in twee richtingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ontwerpt een waterfilter voor een school en één criterium is dat hij betaalbaar moet zijn. Wat doe je als je ontwerp te duur uitvalt?",
        opties=[
            "het ontwerp bijsturen met goedkoper materiaal",
            "het criterium over de prijs gewoon laten vallen",
            "het probleem opnieuw definiëren tot het past",
            "het ontwerp zo laten en niet meer evalueren",
        ],
        antwoord=0,
        uitleg="Bijsturen hoort bij het ontwerpproces. Een criterium laten vallen omdat je het niet haalt, maakt je evaluatie waardeloos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bekijk je een probleem het best vanuit meerdere STEM-disciplines?",
        opties=[
            "omdat een totaaloplossing kennis uit meerdere hoeken vraagt",
            "omdat één discipline nooit iets alleen kan oplossen",
            "omdat je dan helemaal geen criteria meer nodig hebt",
            "omdat het verslag er dan wat langer uitziet",
        ],
        antwoord=0,
        uitleg="Een technisch goed idee kan onbetaalbaar of onveilig zijn, en een mooie berekening kan praktisch onhaalbaar zijn. Samen vang je dat op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het stuk van een groot probleem dat je apart oplost?",
        antwoord=["deelprobleem", "een deelprobleem"],
        uitleg="De deeloplossingen voeg je daarna samen tot de totaaloplossing. Dat samenvoegen is zelf ook een ontwerpstap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ontwerp hoeft maar aan één criterium te voldoen om een goede oplossing te zijn.",
        antwoord=False,
        uitleg="Je oplossing moet aan al je criteria voldoen. Daarom schrijf je ze vooraf op, zodat je er achteraf niets kan vergeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen helpen je om criteria voor een ontwerp op te stellen? Kruis alles aan wat juist is.",
        opties=[
            "hoe groot of hoe zwaar mag het worden?",
            "hoeveel mag het kosten?",
            "hoe veilig en hoe duurzaam moet het zijn?",
            "wie krijgt de eer als het werkt?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Criteria gaan over de eisen aan het product zelf. Wie de eer krijgt, verandert niets aan de kwaliteit van de oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt twee ontwerpen die allebei werken. Hoe kies je?",
        opties=[
            "door ze naast je criteria te leggen en te vergelijken",
            "door het ontwerp te kiezen dat er het mooist uitziet",
            "door het ontwerp te kiezen dat je als eerste bedacht",
            "door het ontwerp te kiezen met de langste uitleg",
        ],
        antwoord=0,
        uitleg="Zo wordt de keuze een onderbouwde beslissing en geen gevoel. Soms scoort het ene beter op prijs en het andere op duurzaamheid, en dan weeg je af.",
    ),
    dict(
        type="waarofniet",
        vraag="Het ontwerpproces stopt zodra je eerste versie klaar is.",
        antwoord=False,
        uitleg="Na het bouwen volgt het testen, en na het testen vaak het bijsturen. Pas als je oplossing aan al je criteria voldoet, ben je klaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad wil de luchtkwaliteit verbeteren. Welke STEM-kennis is daarbij nuttig? Kruis alles aan wat juist is.",
        opties=[
            "wetenschappelijke kennis over de stoffen in de lucht",
            "technische kennis over meettoestellen en filters",
            "wiskundige kennis om de metingen te verwerken",
            "geen enkele, dat is enkel een politieke keuze",
        ],
        antwoord=[0, 1, 2],
        uitleg="Welke maatregel er komt, is uiteindelijk wel een politieke keuze, maar die steunt op die drie soorten kennis. Zo werkt de wisselwerking tussen STEM en de samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen onderzoeken en ontwerpen?",
        opties=[
            "onderzoeken antwoordt op een vraag, ontwerpen lost op",
            "onderzoeken gebeurt in een labo en ontwerpen op papier",
            "onderzoeken is wetenschap en ontwerpen is geen STEM",
            "de twee betekenen in de praktijk precies hetzelfde",
        ],
        antwoord=0,
        uitleg="Een onderzoek levert kennis, een ontwerp levert iets dat werkt. Vaak heb je ze samen nodig: je onderzoekt eerst en ontwerpt daarna.",
    ),
]
