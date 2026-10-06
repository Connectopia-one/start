# -*- coding: utf-8 -*-
"""De vragen voor "Productiefactoren, productiefunctie en meeropbrengsten"
(🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"het keuzegedrag van de producent in een markt met volkomen concurrentie",
eerste stuk: de productiefactoren, de totale en de marginale productiefunctie,
en de wet van de toe- en afnemende meeropbrengsten. De kosten staan in
[[ec_kosten]], de optimale productiegrootte in [[ec_optimaal]].

Deel 1 gaat over de vier productiefactoren en hun vergoeding, en over het
verschil tussen de korte en de lange termijn.
Deel 2 gaat over de totale productie TP en de marginale productie MP: hoe ze
verlopen, waar het keerpunt ligt, en wat de wet van de toe- en afnemende
meeropbrengsten daarover zegt.

Afspraak in dit thema: TP staat altijd voor de totale productie en MP voor de
marginale productie, en elke reeks cijfers staat voluit in de vraag.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier productiefactoren onderscheidt de economie?",
        opties=[
            "Arbeid, kapitaal, natuur en ondernemerschap",
            "Arbeid, geld, grondstoffen en machines",
            "Kapitaal, winst, loon en intrest",
            "Gezinnen, bedrijven, overheid en buitenland",
        ],
        antwoord=0,
        uitleg="Arbeid, kapitaal, natuur en ondernemerschap zijn de vier. Geld is op zich geen productiefactor: je kan er niets mee maken, je kan er alleen kapitaalgoederen mee kopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de productiefactor kapitaal? Duid alles aan wat juist is.",
        opties=[
            "De machines in een werkplaats",
            "De bedrijfsgebouwen",
            "De vrachtwagens van een transporteur",
            "Het spaargeld op de rekening van de zaakvoerder",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kapitaal zijn de geproduceerde productiemiddelen: machines, gebouwen, voertuigen en gereedschap. Geld op een rekening is financieel kapitaal, geen kapitaalgoed.",
    ),
    dict(
        type="waarofniet",
        vraag="De machines die grondstoffen verwerken, horen bij de productiefactor natuur.",
        antwoord=False,
        uitleg="Machines zijn gemaakt door mensen en horen dus bij kapitaal. Natuur is alles wat er al was zonder dat iemand het maakte: grond, water, ertsen, wind en zon.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de productiefactor die de andere drie samenbrengt en het risico draagt? Schrijf één woord.",
        antwoord=["ondernemerschap", "ondernemer", "ondernemen"],
        uitleg="De ondernemer combineert arbeid, kapitaal en natuur, neemt de beslissingen en draagt het risico. Zijn vergoeding is de winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke koppelingen tussen productiefactor en vergoeding kloppen? Duid alles aan wat juist is.",
        opties=[
            "Arbeid wordt vergoed met loon",
            "Kapitaal wordt vergoed met intrest",
            "Natuur wordt vergoed met pacht",
            "Ondernemerschap wordt vergoed met intrest",
        ],
        antwoord=[0, 1, 2],
        uitleg="Loon, intrest, pacht en winst: samen vormen ze de verdeling van de toegevoegde waarde onder wie meewerkte.",
    ),
    dict(
        type="waarofniet",
        vraag="Geld is een productiefactor, want zonder geld kan een bedrijf niets maken.",
        antwoord=False,
        uitleg="Met geld koop je productiefactoren, maar het produceert zelf niets. Daarom spreekt men van financieel kapitaal, niet van een productiefactor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de korte en de lange termijn in de productietheorie?",
        opties=[
            "Op korte termijn ligt minstens één productiefactor vast, op lange termijn niet",
            "Op korte termijn ligt de prijs vast, op lange termijn niet",
            "Op korte termijn is er winst, op lange termijn niet",
            "De korte termijn duurt een jaar, de lange termijn langer",
        ],
        antwoord=0,
        uitleg="Het gaat niet om weken of jaren maar om wat je kan aanpassen. Een extra werknemer aanwerven kan snel; een tweede fabriek bouwen niet, en dus ligt het kapitaal op korte termijn vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakkerij kan snel een extra bakker aanwerven, maar niet snel een tweede oven plaatsen. Wat volgt daaruit?",
        opties=[
            "Arbeid is hier de variabele factor en kapitaal de vaste factor",
            "Kapitaal is hier de variabele factor en arbeid de vaste factor",
            "Allebei de factoren zijn variabel",
            "Allebei de factoren liggen vast",
        ],
        antwoord=0,
        uitleg="Dat is precies de korte termijn: de hoeveelheid arbeid kan je aanpassen, de kapitaalgoederen niet. Daarom wordt in deze theorie alleen de arbeid gevarieerd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de productiefactor die op korte termijn vastligt? Schrijf één woord.",
        antwoord=["vaste", "vast", "constante"],
        uitleg="De vaste productiefactor kan je op korte termijn niet veranderen. Meestal is dat het kapitaal: gebouwen en machines.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een productiefunctie?",
        opties=[
            "Het verband tussen de ingezette productiefactoren en de hoeveelheid die eruit komt",
            "Het verband tussen de prijs van een goed en de hoeveelheid die verkocht wordt",
            "Het verband tussen de kosten en de opbrengsten van een bedrijf",
            "Het verband tussen het loon en het aantal werknemers",
        ],
        antwoord=0,
        uitleg="De productiefunctie zegt hoeveel je maakt bij een bepaalde inzet. Op korte termijn hangt dat af van één variabele factor, meestal de arbeid.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee bedrijven met dezelfde machines en evenveel werknemers kunnen toch een verschillende productie halen.",
        antwoord=True,
        uitleg="Organisatie, vakkennis en motivatie maken verschil. De productiefunctie van het ene bedrijf ligt dan hoger dan die van het andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over arbeid als productiefactor kloppen? Duid alles aan wat juist is.",
        opties=[
            "Ze omvat zowel lichamelijk als geestelijk werk",
            "Haar vergoeding is het loon",
            "Haar opbrengst stijgt met opleiding en ervaring",
            "Ze is op lange termijn de enige vaste factor",
        ],
        antwoord=[0, 1, 2],
        uitleg="Arbeid is al het menselijke werk, betaald met loon, en productiever naarmate het menselijk kapitaal groeit. Op lange termijn is géén enkele factor vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom streeft een producent volgens de theorie naar maximale winst?",
        opties=[
            "Omdat die veronderstelling zijn beslissingen over produceren goed verklaart",
            "Omdat de wet bedrijven verplicht winst te maken",
            "Omdat een bedrijf anders geen belastingen kan betalen",
            "Omdat de consument dat van een bedrijf verwacht",
        ],
        antwoord=0,
        uitleg="Het is een modelveronderstelling. Ze verklaart waarom een bedrijf bij een bepaalde prijs net die hoeveelheid aanbiedt en niet meer of minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een kapitaalgoed en een intermediair goed?",
        opties=[
            "Een kapitaalgoed blijft bestaan, een intermediair goed gaat op in het product",
            "Een kapitaalgoed is duur, een intermediair goed is goedkoop",
            "Een kapitaalgoed koop je, een intermediair goed huur je",
            "Een kapitaalgoed is tastbaar, een intermediair goed niet",
        ],
        antwoord=0,
        uitleg="De oven van een bakker blijft na duizend broden bestaan; de bloem is na één brood verwerkt. Daarom is de oven een kapitaalgoed en de bloem een intermediair goed.",
    ),
    dict(
        type="waarofniet",
        vraag="Op lange termijn kan een bedrijf al zijn productiefactoren aanpassen.",
        antwoord=True,
        uitleg="Dat is precies wat de lange termijn betekent: ook gebouwen en machines kunnen er dan bij of weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een landbouwer huurt grond. Welke vergoeding betaalt hij, en voor welke productiefactor?",
        opties=[
            "Pacht, voor de factor natuur",
            "Loon, voor de factor arbeid",
            "Intrest, voor de factor kapitaal",
            "Winst, voor de factor ondernemerschap",
        ],
        antwoord=0,
        uitleg="Grond hoort bij natuur, en de vergoeding daarvoor heet pacht of huur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beslissingen horen bij de ondernemer? Duid alles aan wat juist is.",
        opties=[
            "Beslissen wat er geproduceerd wordt",
            "Beslissen hoeveel er geproduceerd wordt",
            "Het risico dragen als het misloopt",
            "Het loon bepalen dat elke sector in het land betaalt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De ondernemer beslist wat, hoeveel en hoe, en draagt het risico. Loonafspraken voor een hele sector worden in overleg gemaakt, niet door één ondernemer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de vergoeding voor het gebruik van grond? Schrijf één woord.",
        antwoord=["pacht", "huur"],
        uitleg="Pacht of huur is de vergoeding voor de productiefactor natuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat de ondernemer apart van de andere drie factoren?",
        opties=[
            "Omdat hij de andere drie combineert en als enige het risico draagt",
            "Omdat hij als enige een vergoeding krijgt",
            "Omdat hij altijd ook eigenaar van het gebouw is",
            "Omdat hij zelf niet meewerkt in het bedrijf",
        ],
        antwoord=0,
        uitleg="De andere drie krijgen een afgesproken vergoeding, ook als het slecht gaat. Wat er daarna overblijft, is winst of verlies, en dat is voor de ondernemer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf schakelt over op zonnepanelen voor zijn eigen stroom. Welke productiefactoren spelen hier mee?",
        opties=[
            "Natuur, want de zon, en kapitaal, want de panelen",
            "Alleen natuur, want de zon levert de energie",
            "Alleen kapitaal, want de panelen zijn gekocht",
            "Alleen arbeid, want iemand plaatste de panelen",
        ],
        antwoord=0,
        uitleg="De zon is natuur, de panelen zijn geproduceerde productiemiddelen en dus kapitaal. Bijna elke productie combineert meerdere factoren.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de totale productie TP?",
        opties=[
            "De hoeveelheid die geproduceerd wordt bij een bepaalde inzet van de variabele factor",
            "De waarde in euro van alles wat een bedrijf in een jaar verkoopt",
            "De productie per werknemer in dat bedrijf",
            "De productie van alle bedrijven in een bedrijfstak samen",
        ],
        antwoord=0,
        uitleg="TP is de hoeveelheid, in stuks of eenheden, die uit een bepaalde inzet komt. Pas als je er een prijs bij zet, krijg je opbrengsten in euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de marginale productie MP?",
        opties=[
            "De extra productie door één eenheid meer van de variabele factor",
            "De gemiddelde productie per eenheid van de variabele factor",
            "De productie van de laatste werkdag van de maand",
            "De hoogste productie die een bedrijf ooit haalde",
        ],
        antwoord=0,
        uitleg="MP is het verschil in TP wanneer je er één werknemer bij zet. Het is dus een verschil, geen gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf produceert met 3 werknemers 90 stuks en met 4 werknemers 112 stuks. Hoe groot is MP van de vierde?",
        opties=[
            "22",
            "28",
            "112",
            "30",
        ],
        antwoord=0,
        uitleg="112 min 90 is 22 stuks. Dat is wat die vierde werknemer er bovenop brengt.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de afkorting MP voor? Schrijf twee woorden.",
        antwoord=["marginale productie", "marginaal product"],
        uitleg="MP is de marginale productie: de extra productie van één eenheid meer van de variabele factor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van de toe- en afnemende meeropbrengsten?",
        opties=[
            "MP stijgt eerst, bereikt een top en daalt daarna",
            "MP daalt vanaf de eerste werknemer",
            "MP stijgt onbeperkt zolang je mensen bijzet",
            "MP blijft gelijk zolang de machines dezelfde blijven",
        ],
        antwoord=0,
        uitleg="In het begin komt er taakverdeling, dus de extra opbrengst stijgt. Daarna wordt de vaste factor te krap en daalt ze: steeds meer mensen op dezelfde machines.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom daalt MP vanaf een bepaald punt?",
        opties=[
            "Omdat er steeds meer variabele factor op dezelfde vaste factor werkt",
            "Omdat de werknemers minder hun best gaan doen",
            "Omdat de prijs van het product dan begint te dalen",
            "Omdat het loon per werknemer dan stijgt",
        ],
        antwoord=0,
        uitleg="Met twintig bakkers op één oven staat men te wachten. De vaste factor wordt de flessenhals, en dat drukt de opbrengst van elke extra werkkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="MP van vijf werknemers is 12, 20, 25, 18 en 9. Wat kan je besluiten? Duid alles aan wat juist is.",
        opties=[
            "De toenemende meeropbrengsten lopen tot de derde werknemer",
            "Vanaf de vierde werknemer zijn er afnemende meeropbrengsten",
            "De totale productie bij vijf werknemers is 84",
            "De totale productie daalt vanaf de vierde werknemer",
        ],
        antwoord=[0, 1, 2],
        uitleg="12 plus 20 plus 25 plus 18 plus 9 is 84. Zolang MP positief blijft, blijft TP stijgen, ook als MP zelf daalt.",
    ),
    dict(
        type="waarofniet",
        vraag="Zolang MP positief is, blijft de totale productie stijgen.",
        antwoord=True,
        uitleg="Elke extra werknemer voegt dan nog iets toe. Pas bij een negatieve MP begint TP te dalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer bereikt TP zijn maximum?",
        opties=[
            "Wanneer MP nul wordt",
            "Wanneer MP zijn maximum bereikt",
            "Wanneer MP begint te dalen",
            "Wanneer MP negatief wordt",
        ],
        antwoord=0,
        uitleg="Zolang MP boven nul ligt, komt er nog productie bij. Is MP nul, dan voegt de volgende werknemer niets meer toe: dat is het toppunt van TP.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een negatieve MP blijft de totale productie gelijk.",
        antwoord=False,
        uitleg="Ze daalt. Die extra werknemer staat de anderen in de weg: er is dan echt te veel variabele factor op een te kleine vaste factor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de productie per eenheid arbeid? Schrijf twee woorden.",
        antwoord=["gemiddelde productie", "gemiddeld product"],
        uitleg="De gemiddelde productie GP is TP gedeeld door het aantal eenheden van de variabele factor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf maakt met 6 werknemers 150 stuks. Hoe groot is de gemiddelde productie?",
        opties=[
            "25 stuks per werknemer",
            "150 stuks per werknemer",
            "6 stuks per werknemer",
            "900 stuks per werknemer",
        ],
        antwoord=0,
        uitleg="150 gedeeld door 6 is 25 stuks per werknemer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dalende MP betekent dat het bedrijf minder produceert dan voordien.",
        antwoord=False,
        uitleg="Het produceert nog altijd méér, alleen groeit de productie trager. Pas bij een negatieve MP daalt de totale productie echt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt MP in het begin?",
        opties=[
            "Door taakverdeling en specialisatie kunnen de werknemers efficiënter werken",
            "Doordat de machines in het begin nieuwer zijn",
            "Doordat de eerste werknemers meer verdienen",
            "Doordat de grondstoffen in het begin goedkoper zijn",
        ],
        antwoord=0,
        uitleg="In je eentje doe je alles; met drie kan ieder zich toeleggen op wat hij best kan. Dat verklaart de toenemende meeropbrengsten aan het begin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over TP en MP kloppen? Duid alles aan wat juist is.",
        opties=[
            "MP is het verschil tussen twee opeenvolgende TP-waarden",
            "TP is de som van alle MP-waarden tot dan toe",
            "TP bereikt zijn top waar MP nul is",
            "MP is altijd groter dan TP",
        ],
        antwoord=[0, 1, 2],
        uitleg="MP en TP horen bij elkaar als verschil en som. MP is bijna altijd veel kleiner dan TP, want TP telt alles op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een restaurant heeft één keuken. Bij 8 koks begint het trager te gaan. Hoe heet dat verschijnsel?",
        opties=[
            "De afnemende meeropbrengsten",
            "De toenemende meeropbrengsten",
            "De schaalvoordelen",
            "De wet van de dalende vraag",
        ],
        antwoord=0,
        uitleg="De vaste factor, hier de keuken, wordt te klein. Elke extra kok voegt dan minder toe dan de vorige.",
    ),
    dict(
        type="waarofniet",
        vraag="De wet van de toe- en afnemende meeropbrengsten geldt alleen op korte termijn.",
        antwoord=True,
        uitleg="De wet veronderstelt dat minstens één factor vastligt. Op lange termijn kan het bedrijf ook zijn keuken of zijn fabriek vergroten, en dan geldt ze niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="TP bij 1 tot 5 werknemers: 10, 26, 48, 60, 65. Bij welke werknemer is MP het grootst?",
        opties=[
            "Bij de derde",
            "Bij de tweede",
            "Bij de vierde",
            "Bij de vijfde",
        ],
        antwoord=0,
        uitleg="De MP-waarden zijn 10, 16, 22, 12 en 5. De grootste sprong, 22, zit bij de derde werknemer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is deze theorie belangrijk voor de kosten van een bedrijf?",
        opties=[
            "Omdat dalende meeropbrengsten de kosten per stuk doen stijgen",
            "Omdat stijgende meeropbrengsten de lonen doen stijgen",
            "Omdat de productie niets met de kosten te maken heeft",
            "Omdat de prijs van het product uit de productiefunctie volgt",
        ],
        antwoord=0,
        uitleg="Als elke extra werknemer minder toevoegt, heb je meer arbeid nodig voor één stuk extra. Daardoor stijgt de marginale kost: zo hangt de kostencurve aan de productiefunctie vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tuinbedrijf verdubbelt op lange termijn zijn machines én zijn personeel, en de productie stijgt met meer dan het dubbele. Hoe heet dat?",
        opties=[
            "Schaalvoordelen",
            "Afnemende meeropbrengsten",
            "Toenemende meeropbrengsten",
            "Een negatieve marginale productie",
        ],
        antwoord=0,
        uitleg="Als álle factoren mee groeien, spreek je van schaalvoordelen. Meeropbrengsten gaan net over één factor die stijgt terwijl de rest vastligt.",
    ),
]
