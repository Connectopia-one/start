# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Spieren, klieren en hormonen.

Biologie, de kop "Reacties op prikkels" van de vakfiche natuurwetenschappen
2de graad doorstroom, met haar twee onderdelen. Deel 1 gaat over de spieren:
de soorten, de bouw van groot naar klein en de aansturing. Deel 2 gaat over de
klieren: endocrien, exocrien en gemengd, de hormonen en hun doelorganen, en de
regeling van het glucosegehalte in het bloed.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten spierweefsel zijn er?",
        opties=[
            "dwarsgestreept spierweefsel, glad spierweefsel en hartspierweefsel",
            "dwarsgestreept spierweefsel, bindweefsel en hartspierweefsel",
            "glad spierweefsel, kraakbeenweefsel en dwarsgestreept spierweefsel",
            "hartspierweefsel, zenuwweefsel en dwarsgestreept spierweefsel",
        ],
        antwoord=0,
        uitleg="Dwarsgestreepte spieren bewegen het skelet, gladde spieren zitten in de wand van organen en bloedvaten, en het hartspierweefsel komt alleen in het hart voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke spieren zijn willekeurig, dus onder je wil? Kruis alles aan wat juist is.",
        opties=[
            "de spier die je arm buigt",
            "de spier die je been strekt",
            "de kauwspier in je kaak",
            "de spierwand van je darm",
        ],
        antwoord=[0, 1, 2],
        uitleg="De dwarsgestreepte skeletspieren stuur je zelf aan. De gladde spieren van de darm werken onwillekeurig, zonder dat je erbij nadenkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hartspierweefsel werkt onwillekeurig.",
        antwoord=True,
        uitleg="Je kan je hartslag niet met je wil stilleggen. Het hartspierweefsel heeft bovendien een eigen ritme en wordt door het autonome zenuwstelsel bijgestuurd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat de biceps en de triceps elkaars antagonist zijn?",
        opties=[
            "wanneer de ene samentrekt, ontspant de andere",
            "ze trekken altijd precies op hetzelfde moment samen",
            "ze zitten allebei vast aan hetzelfde punt van het bot",
            "ze zijn allebei opgebouwd uit glad spierweefsel",
        ],
        antwoord=0,
        uitleg="Een spier kan alleen trekken, nooit duwen. Daarom werken spieren in paren: de agonist voert de beweging uit en de antagonist voert de omgekeerde beweging uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de spier die de beweging uitvoert, tegenover haar tegenspeler?",
        antwoord="agonist",
        uitleg="De agonist trekt samen en zorgt voor de beweging. De antagonist ontspant daarbij en brengt het lichaamsdeel later weer terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de bouw van een spier in de juiste volgorde, van groot naar klein.",
        opties=[
            "spierbuik, spierbundel, spiervezel, spierfibril",
            "spiervezel, spierbuik, spierfibril, spierbundel",
            "spierfibril, spiervezel, spierbundel, spierbuik",
            "spierbundel, spierbuik, spierfibril, spiervezel",
        ],
        antwoord=0,
        uitleg="De spierbuik zit in een spierschede en bestaat uit bundels; elke bundel bestaat uit vezels, en in elke vezel liggen fibrillen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spiervezel heeft maar één celkern.",
        antwoord=False,
        uitleg="Een dwarsgestreepte spiervezel ontstaat uit meerdere cellen die versmelten en heeft dus veel kernen, vlak onder het sarcolemma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet het celmembraan van een spiervezel?",
        opties=["het sarcolemma", "de spierschede", "de spierfibril", "het spierspoeltje"],
        antwoord=0,
        uitleg="Het sarcolemma is het membraan rond de spiervezel. De spierschede is het bindweefsel rond de hele spierbuik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen horen bij de microscopische bouw van een dwarsgestreepte spier? Kruis alles aan wat juist is.",
        opties=["de Z-plaat", "het actinefilament", "het myosinefilament", "de motorische eindplaat"],
        antwoord=[0, 1, 2],
        uitleg="Z-platen, actine en myosine liggen in de spierfibril zelf. De motorische eindplaat is de plek waar het zenuwuiteinde op de vezel aankomt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het stukje spierfibril tussen twee Z-platen, de functionele eenheid van de spier?",
        antwoord="sarcomeer",
        uitleg="Een sarcomeer is de kleinste eenheid die zelfstandig kan verkorten. Duizenden sarcomeren achter elkaar maken samen de verkorting van de hele spier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een sarcomeer als de spier samentrekt?",
        opties=[
            "de actinefilamenten schuiven tussen de myosinefilamenten en de Z-platen komen dichterbij",
            "de actinefilamenten en de myosinefilamenten worden allebei een flink stuk korter",
            "de Z-platen schuiven uit elkaar en de filamenten raken helemaal van elkaar los",
            "de spierfibrillen vallen uiteen en vormen daarna in de spierbuik nieuwe vezels",
        ],
        antwoord=0,
        uitleg="De filamenten zelf blijven even lang. Ze schuiven langs elkaar, waardoor het sarcomeer korter wordt en de hele spier verkort.",
    ),
    dict(
        type="waarofniet",
        vraag="De donkere banden in een dwarsgestreepte spier danken hun naam aan het myosine dat daar ligt.",
        antwoord=True,
        uitleg="De dikke myosinefilamenten laten minder licht door en vormen de donkere band. Waar alleen actine ligt, is de band licht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe komt het bevel om samen te trekken bij de spiervezel aan?",
        opties=[
            "een motorisch neuron geeft via de motorische eindplaat een neurotransmitter af",
            "een sensorisch neuron brengt het bevel rechtstreeks naar elke spierfibril toe",
            "het bloed brengt het bevel als een hormoon naar elke spiervezel afzonderlijk",
            "de spierschede geeft het bevel in één keer door aan alle bundels samen",
        ],
        antwoord=0,
        uitleg="Aan de motorische eindplaat komt de neurotransmitter vrij. Die laat het sarcolemma depolariseren, en dat zet de samentrekking in gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een motorische eenheid?",
        opties=[
            "één motorisch neuron met alle spiervezels die het aanstuurt",
            "één spiervezel met alle spierfibrillen die erin naast elkaar liggen",
            "één sarcomeer met zijn actinefilamenten en myosinefilamenten erbij",
            "één spierbundel met het bloedvat en de zenuwvezel die erbij horen",
        ],
        antwoord=0,
        uitleg="Hoe fijner de beweging moet zijn, hoe minder vezels één neuron bedient. In de oogspieren zijn de motorische eenheden heel klein, in de dijspier heel groot.",
    ),
    dict(
        type="waarofniet",
        vraag="De spierspoeltjes meten hoe ver een spier uitgerekt is.",
        antwoord=True,
        uitleg="Spierspoeltjes zijn receptoren in de spier zelf. Zij melden de rekking, en die melding is het begin van bijvoorbeeld de kniepeesreflex.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar haalt een spier de energie voor haar werk?",
        opties=[
            "uit de afbraak van glycogeen en glucose in de spiervezel",
            "uit de neurotransmitter die bij de eindplaat vrijkomt",
            "uit de rek van de spierspoeltjes tijdens de beweging",
            "uit het bindweefsel van de spierschede rond de spier",
        ],
        antwoord=0,
        uitleg="Een spier slaat glycogeen op als voorraad. Bij inspanning wordt dat afgebroken tot glucose, en de celademhaling maakt daar energie uit vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over glad spierweefsel zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het ligt in de wand van organen en bloedvaten",
            "het werkt onwillekeurig",
            "het trekt trager samen dan een skeletspier",
            "het vertoont onder de microscoop een duidelijke dwarse streping",
        ],
        antwoord=[0, 1, 2],
        uitleg="Glad spierweefsel ligt in darm, maag en bloedvatwand, werkt buiten je wil om en trekt traag maar lang samen. De dwarse streping is net wat het níét heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spier kan zowel trekken als duwen.",
        antwoord=False,
        uitleg="Een spier kan alleen verkorten en dus trekken. Voor de omgekeerde beweging is een tweede spier nodig, de antagonist.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de plek waar het uiteinde van een motorisch neuron op een spiervezel aankomt?",
        antwoord="motorische eindplaat",
        uitleg="De motorische eindplaat is een synaps tussen zenuw en spier. Daar wordt het zenuwsignaal doorgegeven aan de spiervezel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft spierweefsel veel bloedvaten nodig?",
        opties=[
            "het bloed brengt zuurstof en voedingsstoffen aan en voert afvalstoffen af",
            "het bloed geeft het bevel door om op het juiste ogenblik samen te trekken",
            "het bloed houdt de spierschede rond de spierbuik op de juiste temperatuur",
            "het bloed verbindt de spiervezels mechanisch met het bot waaraan ze trekken",
        ],
        antwoord=0,
        uitleg="Een werkende spier verbruikt veel zuurstof en glucose en maakt veel afval. Zonder een dicht net van bloedvaten houdt ze dat geen minuut vol.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een endocriene en een exocriene klier?",
        opties=[
            "een endocriene klier geeft haar stof af aan het bloed, een exocriene via een afvoerbuis",
            "een endocriene klier geeft haar stof af via een afvoerbuis, een exocriene aan het bloed",
            "een endocriene klier maakt enzymen, een exocriene klier maakt hormonen",
            "een endocriene klier ligt in de huid, een exocriene klier ligt in de buik",
        ],
        antwoord=0,
        uitleg="Endocriene klieren hebben geen afvoerbuis; hun hormoon komt rechtstreeks in het bloed. Exocriene klieren brengen hun product via een buisje naar een oppervlak of holte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klieren zijn exocrien? Kruis alles aan wat juist is.",
        opties=["de traanklier", "de zweetklier", "de talgklier", "de schildklier"],
        antwoord=[0, 1, 2],
        uitleg="Traanklier, zweetklier en talgklier hebben een afvoerbuis naar het oppervlak. De schildklier geeft haar hormoon rechtstreeks aan het bloed en is dus endocrien.",
    ),
    dict(
        type="waarofniet",
        vraag="De alvleesklier is een gemengde klier.",
        antwoord=True,
        uitleg="Ze maakt spijsverteringsenzymen die via een buisje naar de darm gaan, en ook de hormonen insuline en glucagon die rechtstreeks in het bloed komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon maakt de schildklier?",
        opties=["thyroxine", "insuline", "adrenaline", "prolactine"],
        antwoord=0,
        uitleg="Thyroxine regelt de snelheid van de stofwisseling. Insuline komt uit de alvleesklier, adrenaline uit de bijnier en prolactine uit de hypofyse.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de klier onderaan de hersenen die veel andere klieren aanstuurt?",
        antwoord="hypofyse",
        uitleg="De hypofyse maakt onder meer groeihormoon, prolactine en de hormonen die de schildklier en de geslachtsklieren aansturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het sleutel-slotprincipe bij hormonen?",
        opties=[
            "een hormoon past alleen op de membraanreceptor van zijn doelwitcel",
            "een hormoon opent elke cel die het ergens in het bloed tegenkomt",
            "een hormoon werkt alleen wanneer er twee hormonen tegelijk zijn",
            "een hormoon wordt pas aangemaakt als de doelwitcel erom vraagt",
        ],
        antwoord=0,
        uitleg="Een hormoon komt overal in het lichaam, maar alleen cellen met de passende receptor reageren. Dat zijn de doelwitcellen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hormonen werken sneller dan zenuwen.",
        antwoord=False,
        uitleg="Hormonen reizen met het bloed en doen er seconden tot uren over. Een zenuwimpuls is er in een fractie van een seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cellen in de eilandjes van Langerhans maken insuline?",
        opties=["de bètacellen", "de alfacellen", "de spierspoeltjes", "de pigmentcellen"],
        antwoord=0,
        uitleg="De bètacellen maken insuline, de alfacellen maken glucagon. Samen houden ze het glucosegehalte van het bloed in evenwicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je glucosegehalte in het bloed stijgt na een maaltijd. Wat gebeurt er? Kruis alles aan wat juist is.",
        opties=[
            "de bètacellen geven insuline af",
            "de lever slaat glucose op als glycogeen",
            "de lichaamscellen nemen meer glucose op",
            "de alfacellen geven extra glucagon af",
        ],
        antwoord=[0, 1, 2],
        uitleg="Insuline laat de cellen glucose opnemen en de lever glycogeen aanleggen, zodat het gehalte weer daalt. Glucagon komt pas als het gehalte juist te laag wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon laat de lever glycogeen afbreken als je glucosegehalte te laag wordt?",
        antwoord="glucagon",
        uitleg="Glucagon is de tegenhanger van insuline. Het haalt glucose uit de voorraad en laat het gehalte in het bloed weer stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er aan de hand bij diabetes type 1?",
        opties=[
            "het lichaam maakt zelf geen of te weinig insuline meer aan",
            "het lichaam maakt veel te veel insuline aan na elke maaltijd",
            "de lever heeft geen glycogeenvoorraad meer om aan te spreken",
            "de nieren houden alle glucose vast in plaats van ze af te geven",
        ],
        antwoord=0,
        uitleg="Bij type 1 vallen de bètacellen uit. Zonder insuline kunnen de cellen de glucose niet opnemen, en blijft het gehalte in het bloed te hoog.",
    ),
    dict(
        type="waarofniet",
        vraag="Het glucosegehalte in het bloed wordt met een feedbacksysteem geregeld.",
        antwoord=True,
        uitleg="Stijgt het gehalte, dan komt er insuline; daalt het, dan komt er glucagon. Elk hormoon stuurt juist dat bij wat uit evenwicht ging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk effect heeft adrenaline bij stress? Kruis alles aan wat juist is.",
        opties=[
            "de hartslag versnelt",
            "er komt extra glucose vrij in het bloed",
            "het lichaam wordt klaargezet voor inspanning",
            "de spijsvertering wordt juist versneld",
        ],
        antwoord=[0, 1, 2],
        uitleg="Adrenaline uit de bijnier maakt het lichaam klaar om te vechten of te vluchten: sneller hart, meer brandstof. De spijsvertering gaat op dat moment juist op een laag pitje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klier maakt cortisol?",
        opties=["de bijnier", "de thymus", "de speekselklier", "de melkklier"],
        antwoord=0,
        uitleg="Cortisol komt uit de bijnierschors. Het is het hormoon van de langdurige stress en laat onder meer het glucosegehalte stijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="De thymus is een exocriene klier.",
        antwoord=False,
        uitleg="De thymus is endocrien: ze geeft thymosine rechtstreeks aan het bloed af. Een exocriene klier gebruikt juist een afvoerbuis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het doelorgaan van het schildklierstimulerend hormoon uit de hypofyse?",
        opties=["de schildklier", "de bijnier", "de alvleesklier", "de thymus"],
        antwoord=0,
        uitleg="De naam zegt het al: dit hormoon zet de schildklier aan om thyroxine te maken. Zo stuurt de hypofyse andere klieren aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een exocriene klier geeft haar product rechtstreeks aan het bloed af.",
        antwoord=False,
        uitleg="Dat doet een endocriene klier. Een exocriene klier gebruikt een afvoerbuis naar een oppervlak of een holte, zoals de speekselklier naar de mond.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de cel waarop een bepaald hormoon werkt?",
        antwoord="doelwitcel",
        uitleg="Alleen een doelwitcel heeft de receptor waar dat hormoon op past. Alle andere cellen laten het hormoon ongemoeid voorbijgaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft iemand met onbehandelde diabetes vaak dorst hebben en veel plassen?",
        opties=[
            "de nieren voeren de overtollige glucose af en nemen daarbij veel water mee",
            "de nieren houden al het water vast, waardoor het hele lichaam opzwelt",
            "het lichaam maakt extra speeksel aan om de glucose in het bloed te verdunnen",
            "de alvleesklier trekt water uit het bloed om er insuline mee aan te maken",
        ],
        antwoord=0,
        uitleg="Is het glucosegehalte te hoog, dan komt er glucose in de urine. Die trekt water mee, dus je plast veel en krijgt daardoor dorst.",
    ),
    dict(
        type="waarofniet",
        vraag="Een klier is altijd een effector: ze voert een reactie uit nadat ze een signaal kreeg.",
        antwoord=True,
        uitleg="Net als een spier staat een klier aan het einde van de weg van prikkel naar reactie. Haar antwoord is een stof in plaats van een beweging.",
    ),
]
