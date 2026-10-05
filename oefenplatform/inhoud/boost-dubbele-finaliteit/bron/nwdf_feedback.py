# -*- coding: utf-8 -*-
"""🚀 Boost dubbele finaliteit — Biologische feedback en homeostase.

Biologie, de kop "Biologische feedback" van de vakfiche natuurwetenschappen
2de graad dubbele finaliteit. Die kop staat er als één geheel, terwijl de
doorstroomfiche de prikkels, het zenuwstelsel en de klieren elk apart zet.
Daarom is dit een eigen thema en niet een lichtere versie van een bestaand.

Deel 1 is het principe: homeostase, de normwaarde, de prikkel, en de weg van
receptor over conductor naar effector, met de twee manieren van
signaaloverdracht en het verschil tussen positieve en negatieve feedback.
Deel 2 zijn de twee feedbacksystemen die de fiche met naam vraagt, de regeling
van de lichaamstemperatuur en van de glucosespiegel in het bloed, plus de drie
voorbeelden die ze erbij noemt: bloeddruk, hartritme bij stress en de
waterhuishouding bij planten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent homeostase?",
        opties=[
            "dat een organisme zijn inwendige milieu binnen nauwe grenzen houdt",
            "dat een organisme zich aanpast aan de omgeving waarin het leeft",
            "dat alle organen van een organisme precies even hard werken",
            "dat een organisme in rust geen energie meer nodig heeft",
        ],
        antwoord=0,
        uitleg="Homeostase is geen stilstand. Je lichaamstemperatuur, je glucosegehalte en je bloeddruk schommelen voortdurend een beetje, maar ze worden telkens teruggebracht naar hun normwaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een biologisch feedbacksysteem zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het gebruikt het gevolg van een proces om dat proces bij te sturen",
            "het vergelijkt de gemeten waarde met een normwaarde",
            "het houdt het inwendige milieu binnen grenzen die leefbaar zijn",
            "het werkt alleen zolang het organisme volledig stil ligt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een feedbacksysteem meet, vergelijkt met de normwaarde en stuurt bij. Dat gebeurt dag en nacht, ook terwijl je beweegt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prikkel is elke verandering in het inwendige of het uitwendige milieu.",
        antwoord=True,
        uitleg="Koude lucht op je huid is een uitwendige prikkel, een dalend glucosegehalte in je bloed een inwendige. Beide zetten een feedbacksysteem in gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een receptor in een feedbacksysteem?",
        opties=[
            "hij vangt de prikkel op en zet hem om in een signaal",
            "hij voert de reactie uit waarmee het lichaam bijstuurt",
            "hij vergelijkt het signaal met de normwaarde van het lichaam",
            "hij brengt het signaal naar het orgaan dat moet reageren",
        ],
        antwoord=0,
        uitleg="Receptoren zijn vaak zintuigcellen, bijvoorbeeld de warmte- en koudereceptoren in je huid. Vergelijken doet het controlecentrum, uitvoeren doet de effector.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de waarde waarrond een feedbacksysteem het inwendige milieu houdt?",
        antwoord="normwaarde",
        uitleg="Voor de lichaamstemperatuur ligt die normwaarde rond 37 graden. Wijkt de gemeten waarde daarvan af, dan grijpt het systeem in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is in een feedbacksysteem de taak van de conductor?",
        opties=[
            "het signaal doorgeven van de receptor naar de effector",
            "de prikkel opvangen en omzetten in een bruikbaar signaal",
            "de reactie uitvoeren waarmee het evenwicht hersteld wordt",
            "de normwaarde van het inwendige milieu vastleggen",
        ],
        antwoord=0,
        uitleg="Het zenuwstelsel en de hormonen zijn de conductoren van het lichaam: zij vervoeren het signaal. Zintuigcellen zijn receptoren, spieren en klieren effectoren.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij negatieve feedback versterkt het lichaam de verandering die het gemeten heeft.",
        antwoord=False,
        uitleg="Negatieve feedback werkt de verandering juist tegen: stijgt je glucosegehalte, dan volgt een reactie die het weer doet dalen. Versterken is positieve feedback.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organen of cellen kunnen in een feedbacksysteem de effector zijn? Kruis alles aan wat juist is.",
        opties=[
            "de zweetklieren in de huid",
            "de spiertjes in de wand van een bloedvat",
            "de cellen van de alvleesklier die een hormoon afgeven",
            "de warmtereceptoren vlak onder de huid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Spieren en klieren zijn de effectoren: zij voeren de reactie uit. Receptoren horen aan het begin van de weg en voeren zelf niets uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de signaaloverdracht in een feedbacksysteem zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een zenuwsignaal gaat elektrisch via de zenuwbanen",
            "een hormoon gaat chemisch mee met het bloed",
            "een zenuwsignaal werkt sneller dan een hormoon",
            "een hormoon bereikt alleen de cellen die de zenuwen aanwijzen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een zenuwsignaal is snel en gaat naar een nauwkeurig doel. Een hormoon gaat met het bloed mee, werkt langzamer, maar bereikt alle cellen die er gevoelig voor zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de feedback die de gemeten verandering juist versterkt?",
        antwoord=["positieve feedback", "positief"],
        uitleg="Bij positieve feedback neemt het gevolg de oorzaak nog mee: bij een bloeding lokken de eerste stollingsstoffen nog meer stolling uit tot de wonde dicht is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke volgorde doorloopt een feedbacksysteem?",
        opties=[
            "prikkel, receptor, conductor, effector, reactie",
            "prikkel, effector, conductor, receptor, reactie",
            "receptor, prikkel, effector, conductor, reactie",
            "conductor, receptor, prikkel, reactie, effector",
        ],
        antwoord=0,
        uitleg="De prikkel komt binnen bij de receptor, het signaal gaat via de conductor naar de effector, en die voert de reactie uit. Die reactie verandert de prikkel zelf weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Spieren en klieren noemen we effectoren omdat zij de reactie uitvoeren.",
        antwoord=True,
        uitleg="Een spier trekt samen, een klier geeft een stof af. Dat is de reactie waarmee het lichaam het evenwicht herstelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen positieve en negatieve feedback?",
        opties=[
            "negatieve feedback werkt de verandering tegen, positieve versterkt ze",
            "negatieve feedback is schadelijk voor het lichaam, positieve is nuttig",
            "negatieve feedback verloopt via hormonen, positieve via de zenuwen",
            "negatieve feedback komt bij dieren voor, positieve bij planten",
        ],
        antwoord=0,
        uitleg="De woorden zeggen niets over goed of slecht. Negatief betekent dat de reactie de afwijking afremt, positief dat ze de afwijking juist groter maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze voorbeelden zijn negatieve feedback? Kruis alles aan wat juist is.",
        opties=[
            "je gaat zweten wanneer je lichaamstemperatuur stijgt",
            "je alvleesklier geeft insuline af wanneer je glucosegehalte stijgt",
            "de huidmondjes van een plant gaan dicht bij te veel waterverlies",
            "de weeën bij een bevalling worden steeds krachtiger",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie duwen de waarde terug naar de normwaarde. De weeën versterken elkaar tot de bevalling voorbij is, en dat is positieve feedback.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de cellen in een zintuig die een prikkel opvangen?",
        antwoord=["zintuigcellen", "zintuigcel"],
        uitleg="Zintuigcellen zijn de receptoren van het lichaam. In je huid zitten er die warmte en koude meten, in je oog die licht opvangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol speelt het controlecentrum in een feedbacksysteem?",
        opties=[
            "het vergelijkt de gemeten waarde met de normwaarde en beslist",
            "het vangt de prikkels uit de omgeving van het lichaam op",
            "het voert de reactie uit zodra het een signaal binnenkrijgt",
            "het maakt de hormonen die het signaal moeten vervoeren",
        ],
        antwoord=0,
        uitleg="Bij de mens zijn de hersenen en de hersenstam het controlecentrum. Zij krijgen het signaal binnen, vergelijken het met de normwaarde en sturen de effectoren aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een feedbacksysteem komt pas in werking als het evenwicht in het lichaam helemaal verstoord is.",
        antwoord=False,
        uitleg="Het meet voortdurend. Een kleine afwijking van de normwaarde is al genoeg om bij te sturen, en juist daardoor blijft de verstoring klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een bloeding lokken de eerste stollingsstoffen nog meer stolling uit. Welke feedback is dat?",
        opties=[
            "positieve feedback, want het gevolg versterkt de oorzaak",
            "negatieve feedback, want het gevolg remt de oorzaak af",
            "geen feedback, want er komt geen enkele receptor aan te pas",
            "negatieve feedback, want het lichaam keert terug naar de normwaarde",
        ],
        antwoord=0,
        uitleg="Positieve feedback versterkt zichzelf en stopt pas als het doel bereikt is, hier wanneer de wonde dicht is. Daarom komt ze in het lichaam veel minder vaak voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een organisme biologische feedback nodig om zich te handhaven?",
        opties=[
            "omdat zijn cellen alleen werken binnen nauwe grenzen van temperatuur en samenstelling",
            "omdat het anders geen enkele prikkel uit zijn omgeving zou opvangen",
            "omdat het zonder feedback geen energie uit zijn voeding kan halen",
            "omdat zijn organen anders allemaal tegelijk zouden moeten werken",
        ],
        antwoord=0,
        uitleg="Enzymen en celprocessen werken maar in een smalle marge. Loopt de temperatuur of het glucosegehalte te ver uit, dan vallen die processen stil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een schema van een feedbacksysteem staat een pijl met een minteken van een klier naar de hersenen. Wat betekent die pijl?",
        opties=[
            "de klier remt met haar hormoon het controlecentrum af",
            "de klier stimuleert het controlecentrum om meer hormoon te vragen",
            "de klier geeft op dat ogenblik geen enkel hormoon meer af",
            "de hersenen sturen een remmend signaal naar die klier toe",
        ],
        antwoord=0,
        uitleg="Een pijl geeft de richting van de invloed, een minteken zegt dat die invloed remmend is. Hier gaat de pijl van de klier naar de hersenen, dus remt de klier het centrum af.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar zitten de receptoren die meten of je het warm of koud hebt?",
        opties=[
            "in de huid, als warmte- en koudereceptoren",
            "in de lever, die de temperatuur van het bloed meet",
            "in de zweetklieren, die op vochtigheid reageren",
            "in de bloedvaten van de armen en de benen",
        ],
        antwoord=0,
        uitleg="De huid is het grensvlak met de omgeving, en daar zitten warmte- en koudereceptoren. Zij sturen hun signaal naar de hersenen, die het met de normwaarde vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet je lichaam als je het te warm krijgt? Kruis alles aan wat juist is.",
        opties=[
            "de bloedvaten in de huid verwijden zich",
            "de zweetklieren geven meer zweet af",
            "je huid wordt roder dan gewoonlijk",
            "je begint te rillen met je spieren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verwijde bloedvaten brengen meer warm bloed naar de huid, waar de warmte weg kan. Rillen is juist de reactie op koude: dan maken je spieren extra warmte.",
    ),
    dict(
        type="waarofniet",
        vraag="Zweet koelt je af doordat het water verdampt en daarvoor warmte van je lichaam opneemt.",
        antwoord=True,
        uitleg="Verdampen vraagt energie. Die energie haalt het zweet uit je huid, en zo verlies je warmte. In vochtige lucht verdampt zweet slechter en werkt het koelen minder goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de bloedvaten in je huid als je het koud hebt?",
        opties=[
            "ze vernauwen, zodat er minder warmte langs de huid verloren gaat",
            "ze verwijden, zodat er meer warm bloed naar de huid stroomt",
            "ze blijven precies even wijd, want alleen de zweetklieren reageren",
            "ze vernauwen, zodat je huid warmer aanvoelt dan je binnenkant",
        ],
        antwoord=0,
        uitleg="Vernauwde bloedvaten houden het warme bloed in je binnenste. Daarom worden je handen bleek en koud terwijl je organen op temperatuur blijven.",
    ),
    dict(
        type="invultekst",
        vraag="Welke klieren in je huid geven zweet af als je het te warm hebt?",
        antwoord=["zweetklieren", "zweetklier"],
        uitleg="De zweetklieren zijn hier de effector: zij voeren de reactie uit die het lichaam afkoelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon laat het glucosegehalte in je bloed dalen?",
        opties=[
            "insuline, uit de alvleesklier",
            "glucagon, uit de alvleesklier",
            "glycogeen, uit de lever zelf",
            "adrenaline, uit de bijnieren",
        ],
        antwoord=0,
        uitleg="Insuline zet de lever en de spiercellen aan om glucose uit het bloed te halen en op te slaan. Glucagon doet net het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organen en cellen spelen mee in de regeling van je glucosespiegel? Kruis alles aan wat juist is.",
        opties=[
            "de alvleesklier, die insuline en glucagon maakt",
            "de lever, die glucose opslaat en weer vrijgeeft",
            "de spiercellen, die glucose uit het bloed opnemen",
            "de zweetklieren, die glucose met het zweet afvoeren",
        ],
        antwoord=[0, 1, 2],
        uitleg="De alvleesklier is de klier die de hormonen afgeeft, de lever en de spiercellen zijn de effectoren. Zweet voert geen glucose af.",
    ),
    dict(
        type="waarofniet",
        vraag="Glucagon zorgt ervoor dat de lever glucose uit het bloed opslaat als glycogeen.",
        antwoord=False,
        uitleg="Dat is het werk van insuline. Glucagon laat het opgeslagen glycogeen juist weer afbreken tot glucose, zodat het gehalte in het bloed stijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt net gegeten en je glucosegehalte stijgt. Wat doet de lever onder invloed van insuline?",
        opties=[
            "ze haalt glucose uit het bloed en slaat het op als glycogeen",
            "ze breekt glycogeen af en geeft glucose aan het bloed",
            "ze maakt zelf insuline bij om de stijging op te vangen",
            "ze voert de glucose met de gal naar de darm af",
        ],
        antwoord=0,
        uitleg="De lever is hier de effector. Door glucose als glycogeen op te slaan daalt het gehalte in het bloed weer naar de normwaarde.",
    ),
    dict(
        type="invultekst",
        vraag="Als welke stof slaat de lever glucose op wanneer er te veel van in je bloed zit?",
        antwoord=["glycogeen"],
        uitleg="Glycogeen is een lange keten van glucosemoleculen. De lever kan die keten weer afbreken zodra je lichaam glucose nodig heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een paar uur niet gegeten en je glucosegehalte daalt onder de normwaarde. Wat gebeurt er?",
        opties=[
            "de alvleesklier geeft glucagon af en de lever breekt glycogeen af",
            "de alvleesklier geeft insuline af en de lever slaat glucose op",
            "de spiercellen nemen extra glucose uit het bloed op",
            "de lever maakt extra glycogeen uit de glucose in het bloed",
        ],
        antwoord=0,
        uitleg="Een te laag gehalte is de prikkel. Glucagon is het signaal, de lever de effector, en het vrijgegeven glucose brengt het gehalte terug omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag="De alvleesklier maakt zowel insuline als glucagon.",
        antwoord=True,
        uitleg="Dezelfde klier maakt de twee hormonen die elkaar tegenwerken. Welk hormoon ze afgeeft, hangt af van het glucosegehalte dat ze meet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de regeling van de glucosespiegel een voorbeeld van negatieve feedback?",
        opties=[
            "omdat de reactie het gehalte terugbrengt naar de normwaarde",
            "omdat een te hoog gehalte schadelijk is voor het lichaam",
            "omdat er twee hormonen bij betrokken zijn in plaats van één",
            "omdat de reactie het gehalte nog verder laat stijgen",
        ],
        antwoord=0,
        uitleg="Negatief betekent hier tegenwerkend. Stijgt het gehalte, dan volgt een reactie die het doet dalen, en daalt het, dan volgt een reactie die het doet stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de regeling van de bloeddruk zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "receptoren in de wand van grote bloedvaten meten de druk",
            "de hersenstam stuurt het hart en de bloedvaten bij",
            "bij een te hoge druk vertraagt het hart en verwijden de bloedvaten",
            "bij een te hoge druk gaan de zweetklieren extra zweet afgeven",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bloeddruk werkt met dezelfde schakels als de temperatuurregeling: receptoren in de vaatwand, de hersenstam als controlecentrum, het hart en de bloedvaten als effectoren.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon laat de lever glycogeen weer afbreken tot glucose?",
        antwoord=["glucagon"],
        uitleg="Glucagon komt uit de alvleesklier en werkt op de lever. Het is de tegenhanger van insuline.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met je hartritme bij stress, en waarom?",
        opties=[
            "het versnelt, zodat je spieren meer zuurstof en glucose krijgen",
            "het versnelt, zodat je lichaamstemperatuur sneller kan dalen",
            "het vertraagt, zodat je lichaam energie overhoudt",
            "het blijft gelijk, want stress werkt alleen op je spijsvertering",
        ],
        antwoord=0,
        uitleg="Bij stress maakt je lichaam zich klaar om te handelen. Een sneller hart brengt meer zuurstof en brandstof naar je spieren.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij stress vertraagt je hartritme, zodat je lichaam energie spaart.",
        antwoord=False,
        uitleg="Het omgekeerde gebeurt: je hart gaat sneller slaan. Pas als de stress voorbij is, brengt het lichaam het ritme weer naar zijn normwaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe houdt een plant haar waterhuishouding in evenwicht?",
        opties=[
            "ze sluit haar huidmondjes als ze te veel water dreigt te verliezen",
            "ze neemt met haar bladeren extra water uit de lucht op",
            "ze geeft het overtollige water met haar wortels aan de bodem terug",
            "ze laat haar bladeren vallen zodra de bodem te droog wordt",
        ],
        antwoord=0,
        uitleg="Ook dit is negatieve feedback: te veel waterverlies is de prikkel, de huidmondjes zijn de effector, en door te sluiten gaat het verlies weer naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een schema van de temperatuurregeling staat een pijl van de huid naar de hersenen. Wat stelt die pijl voor?",
        opties=[
            "het signaal van de receptoren naar het controlecentrum",
            "de reactie van de effector op het bevel van de hersenen",
            "de warmte die van de huid naar de hersenen stroomt",
            "het hormoon dat de huid naar de hersenen stuurt",
        ],
        antwoord=0,
        uitleg="De huid meet, dus gaat het signaal van de receptoren naar de hersenen. De pijlen die terugkeren naar de bloedvaten en de zweetklieren zijn de bevelen aan de effectoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij diabetes type 1 maakt de alvleesklier geen insuline meer. Wat loopt er mis in het feedbacksysteem?",
        opties=[
            "het signaal valt weg, dus blijft het glucosegehalte te hoog staan",
            "de receptoren meten het glucosegehalte niet meer in het bloed",
            "de lever slaat te veel glucose op en het gehalte zakt te diep",
            "de effectoren werken door terwijl er geen prikkel meer is",
        ],
        antwoord=0,
        uitleg="Meten gaat nog, maar het hormoon dat de boodschap doorgeeft ontbreekt. De lever en de spiercellen krijgen dus geen bevel om glucose op te nemen, en het gehalte blijft hoog.",
    ),
]
