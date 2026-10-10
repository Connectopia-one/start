# -*- coding: utf-8 -*-
"""Wetenschappelijk onderzoek, ontwerpen en STEM — 🌍 Beyond, fysica.

Deel 1 gaat over de stappen van een wetenschappelijk onderzoek: het probleem
definiëren en afbakenen, een onderzoeksvraag en een hypothese opstellen, een
onderzoeksplan maken, data verzamelen en analyseren, een conclusie trekken die
echt een antwoord op de vraag is, en achteraf reflecteren en communiceren.
Daar hoort het werken met één variabele en een controleproef bij. Deel 2 gaat
over het ontwerpen van een oplossing: het probleem definiëren, criteria
opstellen, opsplitsen in deelproblemen, oplossingen bedenken en samenvoegen,
evalueren en bijsturen, en over de wisselwerking tussen wetenschappen,
technologie, wiskunde en de maatschappij.

De rode draad is dat een goede vraag en een eerlijke proef samen de uitkomst
betrouwbaar maken, en dat een resultaat dat je hypothese tegenspreekt geen
mislukking is maar een antwoord.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een onderzoeksvraag?",
        opties=[
            "de vraag die je met je onderzoek wil beantwoorden",
            "het antwoord dat je vooraf verwacht",
            "de lijst van stappen die je gaat zetten",
            "de conclusie die je achteraf in je verslag opschrijft",
        ],
        antwoord=0,
        uitleg="Ze is zo nauw opgesteld dat je ze met metingen kan beantwoorden. Het "
        "verwachte antwoord is je hypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "een verwachting die je vooraf opstelt en kan nagaan",
            "een conclusie die uit je metingen volgt",
            "een vraag die je met je onderzoek stelt",
            "een regel die zeker waar blijkt te zijn",
        ],
        antwoord=0,
        uitleg="Ze moet weerlegbaar zijn, want anders kan je ze niet nagaan. Komt ze niet "
        "uit, dan heb je nog altijd iets geleerd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stap waarin je vastlegt hoe je je onderzoek zal uitvoeren?",
        antwoord=["het onderzoeksplan", "onderzoeksplan", "een onderzoeksplan"],
        uitleg="Daarin staat wat je meet, waarmee en hoe vaak. Zo kan iemand anders je proef "
        "overdoen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderzoeksvraag is bruikbaar voor een proef?",
        opties=[
            "hoe hangt de periode van een slinger af van zijn lengte?",
            "is fysica een moeilijker vak dan wiskunde?",
            "zijn slingers interessanter dan veren?",
            "wat vinden mensen van een slingeruurwerk?",
        ],
        antwoord=0,
        uitleg="Ze noemt twee grootheden die je kan meten. De andere drie vragen naar een "
        "mening en niet naar een meting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een wetenschappelijk onderzoek? Kruis alles aan wat juist is.",
        opties=[
            "het probleem definiëren en afbakenen",
            "een onderzoeksvraag en een hypothese opstellen",
            "data verzamelen en analyseren",
            "de metingen aanpassen tot ze bij de hypothese passen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Metingen aanpassen is geen stap maar bedrog. Je besluit volgt uit de data en "
        "niet uit je verwachting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verander je in een proef maar één grootheid tegelijk?",
        opties=[
            "anders weet je niet welke verandering het verschil veroorzaakte",
            "anders duurt de proef veel te lang om af te werken",
            "anders heb je veel meer meetinstrumenten nodig",
            "anders kan je de resultaten niet in een tabel zetten",
        ],
        antwoord=0,
        uitleg="Alles wat je niet onderzoekt, houd je gelijk. Dan ligt het gevonden verband "
        "echt bij die ene grootheid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grootheid die je in een proef bewust verandert?",
        antwoord=["de onafhankelijke variabele", "onafhankelijke variabele", "de variabele"],
        uitleg="Wat daardoor verandert, is de afhankelijke variabele. De rest houd je "
        "constant.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meting die je hypothese tegenspreekt, is een geldig resultaat.",
        antwoord=True,
        uitleg="Je hypothese was een verwachting en geen eis. Je past je besluit aan, niet je "
        "meting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting meerdere keren?",
        opties=[
            "om toevallige afwijkingen uit je resultaat te halen",
            "om je meetinstrument langer in gebruik te houden",
            "om meer getallen in je tabel te kunnen zetten",
            "om de hypothese alsnog te laten uitkomen",
        ],
        antwoord=0,
        uitleg="Je neemt dan het gemiddelde van je metingen. Wijkt één meting sterk af, dan "
        "zoek je eerst waar dat aan ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een controleproef?",
        opties=[
            "om te vergelijken met een opstelling waarin je niets verandert",
            "om de meetinstrumenten vooraf te ijken",
            "om de proef sneller te laten verlopen",
            "om de hypothese achteraf alsnog bevestigd te krijgen",
        ],
        antwoord=0,
        uitleg="Zonder zo'n vergelijking weet je niet of het verschil van jouw ingreep komt. "
        "Ze hoort dus bij het onderzoeksplan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat moet een goede conclusie doen?",
        opties=[
            "de onderzoeksvraag beantwoorden op basis van de data",
            "de hypothese bevestigen, wat de data ook zeggen",
            "de volgende onderzoeksvraag al meteen stellen",
            "alle metingen nog eens één voor één opsommen",
        ],
        antwoord=0,
        uitleg="Ze verwijst naar wat je gemeten hebt en gaat niet verder dan dat. Het hele "
        "verslag van je metingen hoort in de resultaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een conclusie mag verder gaan dan wat je gemeten hebt.",
        antwoord=False,
        uitleg="Alles wat je beweert, moet uit je data volgen. Wil je meer besluiten, dan "
        "heb je eerst meer metingen nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens horen in een goed verslag van een proef? Kruis alles aan wat juist is.",
        opties=[
            "welke instrumenten je gebruikt hebt",
            "welke grootheden je constant gehouden hebt",
            "de meetwaarden met hun eenheid",
            "welk cijfer je op de proef hoopt te halen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Met die eerste drie kan iemand anders je proef overdoen. Dat overdoen is net "
        "wat een resultaat betrouwbaar maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laat je andere mensen je resultaten nalezen?",
        opties=[
            "zij zien fouten en andere verklaringen die jij gemist hebt",
            "zij kunnen je metingen aanvullen met de hunne",
            "zij mogen beslissen of je hypothese uitkomt",
            "zij moeten het verslag voor jou samenvatten",
        ],
        antwoord=0,
        uitleg="Communiceren en reflecteren horen bij het onderzoek zelf. Daarom wordt een "
        "artikel eerst door vakgenoten gelezen voor het verschijnt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je meet de valtijd \(t\) van een bal vanaf verschillende hoogtes \(h\). Wat zet je op de horizontale as?",
        opties=[
            r"de hoogte \(h\), want die kies je zelf",
            r"de valtijd \(t\), want die meet je",
            "de massa van de bal, want die blijft gelijk",
            "het nummer van de meting, want dat loopt op",
        ],
        antwoord=0,
        uitleg=r"De grootheid die jij instelt, komt op de horizontale as, dus tekenen we "
        r"\(t(h)\). Wat je daarbij meet, komt op de verticale.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeksvraag moet zo breed mogelijk opgesteld zijn.",
        antwoord=False,
        uitleg="Een te brede vraag kan je met één proef niet beantwoorden. Daarom bak je het "
        "probleem eerst af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een hypothese zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze wordt opgesteld voor je begint te meten",
            "ze moet met een proef na te gaan zijn",
            "ze kan door de resultaten weerlegd worden",
            "ze moet altijd juist blijken te zijn",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een hypothese die niet weerlegd kan worden, is wetenschappelijk waardeloos. "
        "Weerlegd worden hoort er dus net bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met een meting die sterk van de rest afwijkt?",
        opties=[
            "je zoekt de oorzaak en vermeldt wat je ermee doet",
            "je laat ze zonder vermelding uit je tabel weg",
            "je neemt ze mee alsof er niets aan de hand is",
            "je past ze aan tot ze bij de andere past",
        ],
        antwoord=0,
        uitleg="Soms is er een duidelijke reden, zoals een verkeerd bereik. Weglaten zonder "
        "reden maakt je resultaat onbetrouwbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een onderzoek herhaalbaar moet zijn?",
        opties=[
            "iemand anders moet met jouw plan hetzelfde kunnen vinden",
            "je moet je eigen proef precies tien keer doen",
            "je moet elk jaar dezelfde proef opnieuw doen",
            "je moet je proef met twee instrumenten tegelijk doen",
        ],
        antwoord=0,
        uitleg="Daarom schrijf je je werkwijze volledig op. Een resultaat dat niemand kan "
        "overdoen, weegt in de wetenschap niet mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Reflecteren over je gekozen methode hoort bij het onderzoek zelf.",
        antwoord=True,
        uitleg="Je vraagt je af wat beter kon en wat je resultaat beperkt. Dat is net de stap "
        "die een volgend onderzoek mogelijk maakt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij het ontwerpen van een oplossing?",
        opties=[
            "het probleem helder definiëren",
            "een eerste model in elkaar zetten",
            "de kostprijs van het materiaal opzoeken",
            "de oplossing aan anderen voorstellen",
        ],
        antwoord=0,
        uitleg="Zonder scherp probleem weet je niet wanneer je klaar bent. Daarna stel je de "
        "criteria op waaraan je oplossing moet voldoen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn criteria bij een ontwerp?",
        opties=[
            "de eisen waaraan je oplossing moet voldoen",
            "de materialen die je bij het bouwen gaat gebruiken",
            "de stappen die je gaat zetten",
            "de problemen die je laat liggen",
        ],
        antwoord=0,
        uitleg="Ze zijn zo opgesteld dat je ze achteraf kan nagaan, bijvoorbeeld een massa "
        "onder een kilo. Zo kan je verschillende ontwerpen eerlijk vergelijken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kleinere stukken waarin je een groot probleem opsplitst?",
        antwoord=["deelproblemen", "deelprobleem", "subproblemen"],
        uitleg="Elk stuk los je apart op en daarna voeg je ze samen. Dat samenvoegen is de "
        "totaaloplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een probleemoplossende strategie? Kruis alles aan wat juist is.",
        opties=[
            "het probleem definiëren",
            "criteria voor de oplossing opstellen",
            "het probleem in deelproblemen splitsen",
            "de criteria laten vallen als de oplossing ze niet haalt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je stuurt je oplossing bij, niet je criteria. Anders haal je ze altijd en "
        "zegt dat niets meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je ontwerp niet aan een criterium voldoet?",
        opties=[
            "je stuurt het ontwerp bij en test opnieuw",
            "je schrapt dat criterium uit de lijst",
            "je kiest meteen een volledig nieuw probleem",
            "je laat het ontwerp zoals het is",
        ],
        antwoord=0,
        uitleg="Evalueren en bijsturen hoort bij het ontwerpen. Soms moet je daarvoor terug "
        "naar een eerdere stap.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een ontwerp volstaat het soms om een bestaand systeem aan te passen.",
        antwoord=True,
        uitleg="Een volledig nieuw systeem bouwen is vaak niet nodig. Welk van de twee je "
        "kiest, volgt uit het probleem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de letters van STEM?",
        opties=[
            "wetenschappen, technologie, techniek en wiskunde",
            "school, techniek, energie en materialen",
            "wetenschappen, techniek, elektriciteit en mechanica",
            "systemen, technologie, energie en meten",
        ],
        antwoord=0,
        uitleg="In het Engels zijn dat science, technology, engineering en mathematics. Bij "
        "een STEM-opdracht zet je die samen in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bekijk je een probleem vanuit verschillende STEM-disciplines?",
        opties=[
            "elk vak brengt een stuk van de oplossing aan",
            "zo duurt het ontwerpen minder lang",
            "zo heb je minder materiaal nodig",
            "zo hoef je geen criteria op te stellen",
        ],
        antwoord=0,
        uitleg="Een goede totaaloplossing heeft kennis uit meerdere hoeken nodig. Wiskunde "
        "levert het rekenwerk, techniek de uitvoering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelde wiskunde tijdens de coronacrisis?",
        opties=[
            "de verspreiding van het virus in kaart brengen",
            "het vaccin in een labo ontwikkelen",
            "het vaccin koel houden tijdens het vervoer",
            "de spuitjes in een fabriek maken",
        ],
        antwoord=0,
        uitleg="Wetenschap gaf het vaccin en technologie het koelen en vervoeren. De drie "
        "waren samen nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke taken vroegen tijdens de coronacrisis technologische kennis? Kruis alles aan wat juist is.",
        opties=[
            "het vaccin op een heel lage temperatuur bewaren",
            "het vaccin op grote schaal produceren",
            "het vaccin over de hele wereld vervoeren",
            "de werking van het virus op een cel uitleggen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat laatste was wetenschappelijke kennis. De drie andere vroegen toestellen "
        "en processen, dus technologie.",
    ),
    dict(
        type="waarofniet",
        vraag="Maatschappelijke uitdagingen zijn een reden om nieuwe technieken en materialen te ontwikkelen.",
        antwoord=True,
        uitleg="Denk aan de energieomslag of aan de zorg voor een ouder wordende bevolking. "
        "De vraag uit de maatschappij stuurt het onderzoek mee.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je moet een koeltas ontwerpen die een drankje \(4\) h koel houdt. Wat is daarin een criterium?",
        opties=[
            r"de temperatuur blijft na \(4\) h onder \(8\ ^\circ\text{C}\)",
            "de koeltas moet mooi en opvallend zijn",
            "de koeltas moet uit karton gemaakt worden",
            "de koeltas moet snel en zonder gereedschap in elkaar gezet zijn",
        ],
        antwoord=0,
        uitleg="Een criterium is meetbaar, zodat je achteraf kan nagaan of je het haalt. "
        "Mooi en opvallend is een mening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fysicakennis helpt bij het ontwerpen van zo'n koeltas?",
        opties=[
            "hoe warmte door geleiding, stroming en straling verplaatst",
            "hoe een elektrische kring in serie geschakeld wordt",
            "hoe een slinger zijn eigenfrequentie krijgt",
            "hoe een kern bij alfaverval verandert",
        ],
        antwoord=0,
        uitleg="Je houdt alle drie die wegen tegen, zoals in een thermosfles. Daarom werkt "
        "een spiegelende laag in de wand zo goed.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een deelprobleem oplossen zonder na te gaan of het in de totaaloplossing past.",
        antwoord=False,
        uitleg="De stukken moeten op het einde samenwerken. Daarom hoort het samenvoegen "
        "zelf bij de strategie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je nadat je een gegeven oplossing geëvalueerd hebt?",
        opties=[
            "je stuurt ze bij waar ze de criteria niet haalt",
            "je sluit het ontwerp af hoe het ook uitpakte",
            "je schrijft de criteria achteraf opnieuw",
            "je begint met een volledig ander probleem",
        ],
        antwoord=0,
        uitleg="Ontwerpen gaat in rondes: maken, testen, verbeteren. Elke ronde brengt je "
        "dichter bij alle criteria samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen helpen je een ontwerp te evalueren? Kruis alles aan wat juist is.",
        opties=[
            "haalt het elk criterium dat we opgesteld hebben?",
            "waar zit de zwakste schakel in het geheel?",
            "wat zou de volgende versie beter doen?",
            "wie van de groep heeft het minste gedaan?",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste vraag gaat over mensen en niet over het ontwerp. De eerste drie "
        "leveren een volgende versie op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een onderzoek naar zonnepanelen ook een maatschappelijke zaak?",
        opties=[
            "de keuzes die eruit volgen raken ieders energie en kosten",
            "zonnepanelen zijn enkel een technisch vraagstuk voor ingenieurs",
            "zonnepanelen hebben met wiskunde niets te maken",
            "onderzoek staat altijd los van de samenleving",
        ],
        antwoord=0,
        uitleg="Wetenschap, technologie en wiskunde werken er samen aan een vraag die de "
        "hele samenleving aangaat. Die wisselwerking gaat in twee richtingen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel waarin je de oplossingen van alle deelproblemen samenbrengt?",
        antwoord=["de totaaloplossing", "totaaloplossing", "het geheel"],
        uitleg="Pas daar zie je of de stukken samenwerken. Daarom test je ook het geheel en "
        "niet enkel de onderdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ontwerpt een brug van spaghetti die zoveel mogelijk moet dragen. Welke fysicakennis zet je in?",
        opties=[
            "het evenwicht van krachten en het moment van een kracht",
            "de gaswetten en de algemene gaswet",
            "de halveringstijd van een radionuclide",
            "het foto-elektrisch effect bij een metaaloppervlak",
        ],
        antwoord=0,
        uitleg=r"Je kijkt waar de krachten samenkomen, \(\sum \vec{F} = \vec{0}\), en waar "
        r"het moment \(M = F\,d\) het grootst is. Daar versterk je de constructie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een STEM-opdracht volstaat het om één discipline grondig in te zetten.",
        antwoord=False,
        uitleg="Juist het samenbrengen van wetenschappen, technologie en wiskunde geeft een "
        "goede oplossing. Eén discipline laat een deel van het probleem liggen.",
    ),
]
