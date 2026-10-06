# -*- coding: utf-8 -*-
"""De vragen voor "De budgetlijn en de optimale goederencombinatie" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"het keuzegedrag van de consument", tweede stuk: de budgetvergelijking, de
budgetlijn, de gevolgen van prijs- en budgetwijzigingen, en het grafisch
afleiden van de optimale goederencombinatie. Het nut en de indifferentiecurve
staan in [[ec_nut]].

Deel 1 gaat over de budgetvergelijking en de budgetlijn: hoe je ze opstelt,
welke combinaties haalbaar zijn, en wat de snijpunten en de helling betekenen.
Deel 2 gaat over wat er verandert bij een ander budget of een andere prijs, en
over het optimum: het raakpunt van de budgetlijn met de hoogst bereikbare
indifferentiecurve.

Afspraak in dit thema: elke opgave geeft de prijzen en het budget in de vraag
zelf, en goed x staat altijd op de horizontale as.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een budgetvergelijking?",
        opties=[
            "Een vergelijking die de uitgaven aan beide goederen gelijkstelt aan het budget",
            "Een vergelijking die het nut van beide goederen aan elkaar gelijkstelt",
            "Een vergelijking die de prijzen van twee goederen met elkaar vergelijkt",
            "Een vergelijking die het inkomen van twee verschillende gezinnen vergelijkt",
        ],
        antwoord=0,
        uitleg="De budgetvergelijking is px maal x plus py maal y is gelijk aan B: wat je aan x uitgeeft plus wat je aan y uitgeeft, is precies je budget.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument heeft 60 euro. Een boek kost 12 euro, een film 6 euro. Hoe luidt de budgetvergelijking?",
        opties=[
            "12x + 6y = 60",
            "12x − 6y = 60",
            "x + y = 60",
            "12 + 6 = 60",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt elke prijs met het aantal stuks en telt op tot je budget: 12 maal het aantal boeken plus 6 maal het aantal films is 60 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zelfde gegevens: 60 euro, boek 12 euro, film 6 euro. Hoeveel boeken kan hij kopen als hij niets anders koopt?",
        opties=[
            "5",
            "10",
            "6",
            "12",
        ],
        antwoord=0,
        uitleg="60 gedeeld door 12 is 5. Dat is het snijpunt van de budgetlijn met de as van de boeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zelfde gegevens. Hij koopt 3 boeken. Hoeveel films kan hij nog betalen?",
        opties=[
            "4",
            "2",
            "6",
            "3",
        ],
        antwoord=0,
        uitleg="3 boeken kosten 36 euro, dus er blijft 24 euro over. 24 gedeeld door 6 is 4 films.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je over een punt dat onder de budgetlijn ligt? Duid alles aan wat juist is.",
        opties=[
            "De consument kan die combinatie betalen",
            "Hij houdt er geld van zijn budget over",
            "Hij kan met dat geld nog meer nut halen",
            "Die combinatie is onbereikbaar voor hem",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onder de lijn blijft er budget over. Zo'n punt is haalbaar maar niet optimaal: met het restje kan hij nog iets kopen en dus nog nut winnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een punt boven de budgetlijn kan de consument niet betalen.",
        antwoord=True,
        uitleg="Boven de lijn kosten de twee goederen samen meer dan zijn budget. Zulke combinaties zijn onbereikbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de lijn met alle combinaties die een consument precies kan betalen? Schrijf één woord.",
        antwoord=["budgetlijn", "budgetrechte"],
        uitleg="De budgetlijn verbindt alle combinaties waarvoor de uitgaven precies gelijk zijn aan het budget.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bepaalt de helling van de budgetlijn?",
        opties=[
            "De verhouding tussen de prijzen van de twee goederen",
            "De grootte van het budget van de consument",
            "Het nut dat de consument aan beide goederen hecht",
            "Het aantal goederen dat in de winkel te koop is",
        ],
        antwoord=0,
        uitleg="De helling is de prijsverhouding px gedeeld door py. Het budget bepaalt alleen hoe ver de lijn van de oorsprong ligt, niet hoe schuin ze loopt.",
    ),
    dict(
        type="waarofniet",
        vraag="Kost een boek 12 euro en een film 6 euro, dan kost één boek extra hem een halve film.",
        antwoord=False,
        uitleg="12 gedeeld door 6 is 2: voor de prijs van één boek krijg je twee films. Eén boek extra kost hem dus twee films. Dat is de alternatieve kost van een boek, uitgedrukt in films.",
    ),
    dict(
        type="waarofniet",
        vraag="De budgetlijn is een rechte lijn zolang de prijzen vastliggen.",
        antwoord=True,
        uitleg="De prijsverhouding verandert dan niet, en dus blijft de helling overal dezelfde. Daarom is het een rechte en geen curve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om een budgetlijn te tekenen? Duid alles aan wat juist is.",
        opties=[
            "Het budget van de consument",
            "De prijs van het eerste goed",
            "De prijs van het tweede goed",
            "De voorkeuren van de consument",
        ],
        antwoord=[0, 1, 2],
        uitleg="Budget en twee prijzen volstaan: daarmee liggen beide snijpunten en de helling vast. De voorkeuren zitten in de indifferentiecurven, niet in de budgetlijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument heeft 100 euro, goed x kost 10 euro en goed y 20 euro. Waar snijdt de budgetlijn de verticale as van y?",
        opties=[
            "Bij 5",
            "Bij 10",
            "Bij 20",
            "Bij 100",
        ],
        antwoord=0,
        uitleg="Als hij alles aan y besteedt: 100 gedeeld door 20 is 5 stuks.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het bedrag dat een consument te besteden heeft? Schrijf één woord.",
        antwoord=["budget", "inkomen"],
        uitleg="Het budget is wat hij kan uitgeven. Samen met de prijzen bepaalt het wat haalbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ligt het optimum altijd óp de budgetlijn en niet eronder?",
        opties=[
            "Omdat hij met het geld dat overblijft nog nut kan winnen",
            "Omdat de winkel hem verplicht alles uit te geven",
            "Omdat sparen in dit model helemaal niet toegelaten wordt",
            "Omdat punten onder de lijn onbereikbaar zijn",
        ],
        antwoord=0,
        uitleg="Zolang er budget overblijft, kan hij er nog iets mee kopen dat nut toevoegt. In dit model geeft hij zijn budget dus volledig uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle punten op de budgetlijn geven de consument evenveel nut.",
        antwoord=False,
        uitleg="Ze kosten allemaal evenveel, maar ze geven niet allemaal evenveel nut. Welk punt het beste is, hangt af van zijn voorkeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin heeft 240 euro voor vlees en groenten. Vlees kost 12 euro per kilo, groenten 4 euro per kilo. Hoeveel kilo groenten kan het kopen bij 10 kilo vlees?",
        opties=[
            "30 kilo",
            "20 kilo",
            "60 kilo",
            "15 kilo",
        ],
        antwoord=0,
        uitleg="10 kilo vlees kost 120 euro, dus er blijft 120 euro over. 120 gedeeld door 4 is 30 kilo groenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de helling van de budgetlijn en de helling van een indifferentiecurve?",
        opties=[
            "De eerste komt van de prijzen, de tweede van de voorkeuren",
            "De eerste komt van de voorkeuren, de tweede van de prijzen",
            "De eerste is altijd steiler dan de tweede",
            "Ze zijn altijd aan elkaar gelijk",
        ],
        antwoord=0,
        uitleg="De markt zegt met de prijzen wat een ruil kóst; de consument zegt met zijn curve wat hij voor die ruil óver heeft. In het optimum vallen die twee precies samen.",
    ),
    dict(
        type="invultekst",
        vraag="Waar in de budgetvergelijking staat het budget? Schrijf twee woorden.",
        antwoord=["rechts", "rechterlid", "in het rechterlid"],
        uitleg="Links staan de uitgaven aan beide goederen, rechts het budget: px maal x plus py maal y is gelijk aan B.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de haalbare combinaties als de prijzen en het budget alle drie verdubbelen?",
        opties=[
            "Er verandert niets aan wat hij kan kopen",
            "De consument kan dubbel zoveel kopen",
            "De consument kan half zoveel kopen",
            "De budgetlijn wordt een stuk steiler dan ze was",
        ],
        antwoord=0,
        uitleg="Deel je de hele vergelijking door 2, dan sta je weer bij de oorspronkelijke. Alleen de verhouding tussen prijzen en budget telt, niet de absolute bedragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de budgetlijn in de theorie? Duid alles aan wat juist is.",
        opties=[
            "Ze toont welke combinaties haalbaar zijn",
            "Ze toont welke combinaties onbereikbaar zijn",
            "Ze toont de ruilverhouding die de markt oplegt",
            "Ze toont welke combinatie de consument het liefst heeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="De budgetlijn zegt alleen wat kán. Wat hij het liefst heeft, lees je af uit zijn indifferentiecurven.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Het budget van een consument stijgt, de prijzen blijven gelijk. Wat gebeurt er met de budgetlijn?",
        opties=[
            "Ze schuift evenwijdig naar buiten, weg van de oorsprong",
            "Ze wordt merkbaar steiler dan voordien",
            "Ze wordt vlakker",
            "Ze blijft precies waar ze is",
        ],
        antwoord=0,
        uitleg="De prijsverhouding verandert niet, dus de helling blijft gelijk. Alleen de afstand tot de oorsprong groeit: een evenwijdige verschuiving naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Alleen de prijs van goed x daalt. Wat gebeurt er met de budgetlijn?",
        opties=[
            "Ze draait rond het snijpunt met de as van y",
            "Ze schuift evenwijdig naar buiten, weg van de oorsprong",
            "Ze draait rond het snijpunt met de as van x",
            "Ze schuift evenwijdig naar binnen",
        ],
        antwoord=0,
        uitleg="Besteedt hij alles aan y, dan verandert er niets: dat snijpunt blijft liggen. Van x kan hij er meer kopen, dus het andere uiteinde schuift naar buiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prijswijziging van één goed verandert de helling van de budgetlijn.",
        antwoord=True,
        uitleg="De helling is de prijsverhouding. Verandert één prijs, dan verandert die verhouding en dus de helling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument heeft 120 euro, x kost 10 euro, y kost 20 euro. De prijs van x zakt naar 6 euro. Hoeveel x kan hij nu maximaal kopen?",
        opties=[
            "20",
            "12",
            "16",
            "6",
        ],
        antwoord=0,
        uitleg="120 gedeeld door 6 is 20 stuks. Vóór de prijsdaling waren dat er 12.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen laten de helling van de budgetlijn ongemoeid? Duid alles aan wat juist is.",
        opties=[
            "Het budget stijgt",
            "Het budget daalt",
            "Beide prijzen stijgen met hetzelfde percentage",
            "Alleen de prijs van goed y stijgt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De helling hangt alleen af van de verhouding tussen de twee prijzen. Verandert één prijs apart, dan kantelt de lijn wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt de optimale goederencombinatie?",
        opties=[
            "Waar de budgetlijn de hoogste bereikbare curve raakt",
            "Waar de budgetlijn een van de indifferentiecurven snijdt",
            "Waar de budgetlijn de verticale as raakt",
            "Waar twee indifferentiecurven elkaar raken",
        ],
        antwoord=0,
        uitleg="In het raakpunt haalt de consument het hoogste nut dat hij kan betalen. Snijdt de lijn een curve, dan ligt er altijd nog een hogere curve binnen bereik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt er in het optimum?",
        opties=[
            "De twee hellingen zijn aan elkaar gelijk",
            "De indifferentiecurve snijdt de budgetlijn op twee plaatsen",
            "Het budget is nog niet volledig besteed",
            "Beide goederen hebben hetzelfde grensnut",
        ],
        antwoord=0,
        uitleg="In het raakpunt vallen de twee hellingen samen: wat de consument voor een ruil over heeft, is precies wat de markt ervoor vraagt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waar de budgetlijn de hoogst bereikbare indifferentiecurve raakt? Schrijf één woord.",
        antwoord=["raakpunt", "optimum", "evenwicht"],
        uitleg="Dat raakpunt is het consumentenoptimum: de beste combinatie die binnen het budget past.",
    ),
    dict(
        type="waarofniet",
        vraag="Een snijpunt van de budgetlijn met een indifferentiecurve is het optimum.",
        antwoord=False,
        uitleg="Bij een snijpunt kan de consument nog beter: er ligt altijd nog een hogere curve die de lijn raakt. Pas bij een raakpunt kan het niet meer beter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het budget van een consument stijgt. Wat gebeurt er met zijn optimum?",
        opties=[
            "Het verschuift naar een hogere indifferentiecurve",
            "Het verschuift naar een lagere indifferentiecurve",
            "Het blijft op dezelfde indifferentiecurve liggen",
            "Er is geen optimum meer",
        ],
        antwoord=0,
        uitleg="Met meer budget ligt de budgetlijn verder naar buiten, en daar kan ze een hogere curve raken. Zijn nut stijgt dus.",
    ),
    dict(
        type="meerkeuze",
        vraag="De prijs van goed x daalt. Welke gevolgen zijn mogelijk? Duid alles aan wat juist is.",
        opties=[
            "De consument koopt meer van goed x",
            "Zijn koopkracht stijgt, want zijn budget reikt verder",
            "Zijn optimum verschuift naar een andere combinatie",
            "Zijn budget in euro stijgt mee",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een lagere prijs maakt x aantrekkelijker en maakt de consument rijker in wat hij kan kopen. Zijn budget in euro verandert daardoor niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin krijgt 10 % opslag, maar alle prijzen stijgen ook met 10 %. Wat gebeurt er met zijn budgetlijn?",
        opties=[
            "Ze blijft liggen waar ze lag",
            "Ze schuift naar buiten",
            "Ze schuift naar binnen",
            "Ze wordt merkbaar steiler dan voordien",
        ],
        antwoord=0,
        uitleg="Budget en prijzen stijgen even hard, dus de haalbare hoeveelheden blijven dezelfde. De koopkracht is onveranderd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een consument kan in het optimum zijn nut nog verhogen zonder zijn budget te overschrijden.",
        antwoord=False,
        uitleg="Dan was het geen optimum. Het optimum is juist het hoogste nut dat binnen het budget haalbaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom raakt de budgetlijn de indifferentiecurve in het optimum in plaats van ze te snijden?",
        opties=[
            "Omdat bij een snijpunt een hogere curve bereikbaar blijft",
            "Omdat een rechte en een curve elkaar nooit kunnen snijden",
            "Omdat de consument anders zijn budget overschrijdt",
            "Omdat twee curven van dezelfde consument elkaar nooit snijden",
        ],
        antwoord=0,
        uitleg="Zolang de lijn een curve doorsnijdt, ligt er een stukje budgetlijn boven die curve, en daar ligt meer nut binnen bereik. Pas als ze alleen nog raakt, is het beste bereikt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verschuiving van de budgetlijn wanneer alleen het budget verandert? Schrijf één woord.",
        antwoord=["evenwijdig", "parallel", "evenwijdige"],
        uitleg="De helling blijft gelijk, dus de lijn verschuift evenwijdig met zichzelf, naar buiten of naar binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een consument besteedt 200 euro, x kost 20 euro en y kost 10 euro. In zijn optimum koopt hij 6 stuks x. Hoeveel y koopt hij?",
        opties=[
            "8",
            "6",
            "10",
            "4",
        ],
        antwoord=0,
        uitleg="6 maal 20 is 120 euro, dus er blijft 80 euro over. 80 gedeeld door 10 is 8 stuks y. Samen is dat precies 200 euro, dus het punt ligt op de budgetlijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je in een tekening dat een combinatie haalbaar maar niet optimaal is?",
        opties=[
            "Ze ligt onder de budgetlijn",
            "Ze ligt boven de budgetlijn, buiten zijn bereik",
            "Ze ligt precies op het raakpunt",
            "Ze ligt op de as van een van beide goederen",
        ],
        antwoord=0,
        uitleg="Onder de lijn betekent: betaalbaar, maar er blijft geld over waarmee hij op een hogere curve kan geraken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan de overheid doen waardoor de budgetlijn van een gezin naar buiten schuift? Duid alles aan wat juist is.",
        opties=[
            "Een toelage uitkeren",
            "De belasting op het inkomen verlagen",
            "De btw op producten verlagen",
            "Een maximumprijs instellen boven de marktprijs",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een toelage en een lagere inkomstenbelasting vergroten het budget; een lagere btw verlaagt de prijzen. Een maximumprijs bóven de marktprijs verandert niets, want die prijs wordt toch niet gevraagd.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee consumenten met hetzelfde budget en dezelfde prijzen kunnen toch een andere combinatie kiezen.",
        antwoord=True,
        uitleg="Hun budgetlijn is dezelfde, maar hun indifferentiecurven niet. Met andere voorkeuren ligt het raakpunt ergens anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is deze theorie nuttig, ook al rekent niemand zo in de winkel?",
        opties=[
            "Ze verklaart waarom een lagere prijs meer verkoop oplevert",
            "Ze berekent de prijs die een winkel moet vragen",
            "Ze bepaalt het budget dat een gezin per maand te besteden heeft",
            "Ze voorspelt welk merk een consument zal kiezen",
        ],
        antwoord=0,
        uitleg="Het model verklaart de vraagcurve: daalt de prijs, dan verschuift het optimum en koopt de consument er meer van. Dat is precies wat je in de werkelijkheid ziet.",
    ),
]
