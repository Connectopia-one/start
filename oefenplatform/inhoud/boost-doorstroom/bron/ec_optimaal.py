# -*- coding: utf-8 -*-
"""De vragen voor "De optimale productiegrootte en winstmaximalisatie"
(🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"het keuzegedrag van de producent in een markt met volkomen concurrentie",
laatste stuk: het grafisch en rekenkundig bepalen en interpreteren van de
optimale productiegrootte, en het berekenen van de totale winst daarbij. De
kostencurven staan in [[ec_kosten]].

Deel 1 gaat over de regel MK is gelijk aan MO: waarom dat het optimum is, hoe
je het grafisch en rekenkundig vindt, en wat het betekent.
Deel 2 gaat over de winst: het break-evenpunt, winst en verlies in beeld, en
wanneer een bedrijf op korte termijn toch blijft doorproduceren.

Afspraak in dit thema: bij volkomen concurrentie is MO altijd gelijk aan de
prijs, en dat wordt in elke vraag waar het telt met zoveel woorden gezegd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Bij welke hoeveelheid is de winst van een bedrijf het grootst?",
        opties=[
            "Waar MK gelijk is aan MO",
            "Waar de gemiddelde kost het laagst ligt",
            "Waar de totale opbrengst het hoogst is",
            "Waar de totale kosten het laagst zijn",
        ],
        antwoord=0,
        uitleg="Zolang een stuk meer opbrengt dan het kost, komt er winst bij. Zodra het meer kost dan het opbrengt, gaat er winst af. Precies daartussen ligt het optimum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is MK gelijk aan MO het winstmaximum?",
        opties=[
            "Omdat elk stuk daarna winst wegneemt",
            "Omdat de gemiddelde kost daar het allerlaagst is",
            "Omdat de prijs daar het hoogst is",
            "Omdat de constante kosten daar gedekt zijn",
        ],
        antwoord=0,
        uitleg="Links van dat punt is MO groter dan MK, dus produceer je er beter nog bij. Rechts ervan kost elk stuk meer dan het opbrengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf verkoopt aan 12 euro per stuk op een markt met volkomen concurrentie. Bij welke MK ligt zijn optimum?",
        opties=[
            "Bij 12 euro",
            "Bij 6 euro",
            "Bij 24 euro",
            "Dat kan je zonder de totale kosten niet weten",
        ],
        antwoord=0,
        uitleg="Bij volkomen concurrentie is MO gelijk aan de prijs. Het optimum ligt dus waar MK gelijk is aan 12 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="MO is groter dan MK. Welke uitspraken kloppen dan? Duid alles aan wat juist is.",
        opties=[
            "Dat extra stuk brengt meer op dan het kost",
            "Het bedrijf verhoogt zijn winst door meer te produceren",
            "Het zit nog niet in zijn optimum",
            "Het produceert al meer dan zijn optimum",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zolang MO boven MK ligt, groeit de winst met elk extra stuk en ligt het optimum dus verderop. Te veel produceren herken je net aan het omgekeerde: MK boven MO.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bedrijf dat produceert waar MK groter is dan MO, kan zijn winst verhogen door minder te produceren.",
        antwoord=True,
        uitleg="Die laatste stuks kosten meer dan ze opbrengen. Ze weglaten verhoogt dus de winst.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee grootheden zijn aan elkaar gelijk in het optimum? Schrijf drie woorden.",
        antwoord=["MK en MO", "MO en MK"],
        uitleg="In de optimale productiegrootte is de marginale kost gelijk aan de marginale opbrengst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om het optimum grafisch te vinden? Duid alles aan wat juist is.",
        opties=[
            "De curve van de marginale kost",
            "De lijn van de marginale opbrengst",
            "De hoeveelheid op de horizontale as",
            "De indifferentiecurven van de consument",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je zoekt het snijpunt van MK en MO en leest daaronder de hoeveelheid af. De indifferentiecurven horen bij de consument, niet bij de producent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel: bij 5 stuks is MK 8 euro, bij 6 stuks 10 euro, bij 7 stuks 13 euro. De prijs is 10 euro. Wat is de optimale hoeveelheid?",
        opties=[
            "6 stuks",
            "5 stuks",
            "7 stuks",
            "10 stuks",
        ],
        antwoord=0,
        uitleg="Bij 6 stuks is MK precies gelijk aan de prijs van 10 euro. Het zevende stuk kost 13 euro en brengt maar 10 euro op.",
    ),
    dict(
        type="waarofniet",
        vraag="In het optimum is de totale opbrengst altijd het hoogst.",
        antwoord=False,
        uitleg="De totale opbrengst stijgt nog bij elk stuk extra. Wat je maximaliseert is het verschil tussen opbrengst en kosten, niet de opbrengst zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kijkt een producent naar marginale en niet naar gemiddelde grootheden om te beslissen?",
        opties=[
            "Omdat de beslissing over dat ene stuk extra gaat",
            "Omdat de gemiddelde kost nooit met zekerheid berekend kan worden",
            "Omdat het gemiddelde altijd te hoog uitvalt",
            "Omdat de gemiddelde opbrengst niets met de prijs te maken heeft",
        ],
        antwoord=0,
        uitleg="De vraag is telkens: loont het om er nog één bij te maken? Daarvoor tellen alleen de extra kost en de extra opbrengst van dat stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de optimale productiegrootte kloppen? Duid alles aan wat juist is.",
        opties=[
            "Ze ligt waar MK de lijn van MO snijdt in het stijgende deel van MK",
            "Ze geeft de hoogste totale winst",
            "Bij volkomen concurrentie ligt ze waar MK gelijk is aan de prijs",
            "Ze ligt altijd in het laagste punt van de gemiddelde kost",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het laagste punt van GK is het break-evenpunt bij die prijs, niet het winstmaximum. Alleen toevallig vallen die twee samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom telt alleen het snijpunt in het stijgende deel van de MK-curve?",
        opties=[
            "Omdat in het dalende deel uitbreiden nog loont",
            "Omdat MK in dat deel van de curve negatief is",
            "Omdat de prijs daar nog niet vastligt",
            "Omdat de constante kosten daar nog niet gedekt zijn",
        ],
        antwoord=0,
        uitleg="De MK-curve daalt eerst en stijgt daarna, dus ze snijdt MO twee keer. In het dalende deel loont uitbreiden nog; pas het tweede snijpunt is het optimum.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de hoeveelheid waarbij de winst het grootst is? Schrijf drie woorden.",
        antwoord=["optimale productiegrootte", "de optimale productiegrootte"],
        uitleg="De optimale productiegrootte is de hoeveelheid waarbij MK gelijk is aan MO.",
    ),
    dict(
        type="meerkeuze",
        vraag="De prijs op de markt stijgt van 10 naar 14 euro. Wat doet een bedrijf met stijgende MK?",
        opties=[
            "Het breidt uit tot MK weer de prijs raakt",
            "Het verkleint zijn productie, want de kosten stijgen mee",
            "Het laat zijn productie precies gelijk aan wat ze was",
            "Het verlaagt zijn eigen prijs tot 10 euro",
        ],
        antwoord=0,
        uitleg="De MO-lijn schuift omhoog, dus het snijpunt met MK verschuift naar rechts. Zo ontstaat de stijgende aanbodcurve van het bedrijf.",
    ),
    dict(
        type="waarofniet",
        vraag="De stijgende tak van de MK-curve is de aanbodcurve van het bedrijf.",
        antwoord=True,
        uitleg="Bij elke prijs produceert het bedrijf waar MK gelijk is aan die prijs. Het stijgende stuk van MK zegt dus bij elke prijs hoeveel het aanbiedt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf heeft bij zijn optimum 900 stuks, een prijs van 7 euro en totale kosten van 5 400 euro. Hoe groot is de winst?",
        opties=[
            "900 euro",
            "1 500 euro",
            "6 300 euro",
            "Een verlies van 900 euro",
        ],
        antwoord=0,
        uitleg="TO is 900 maal 7 is 6 300 euro. 6 300 min 5 400 geeft 900 euro winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen het optimum van de consument en dat van de producent?",
        opties=[
            "De consument maximaliseert zijn nut, de producent zijn winst",
            "De consument kijkt naar kosten, de producent naar nut",
            "De consument rekent marginaal, de producent gemiddeld",
            "De consument kiest op korte termijn, de producent op lange termijn",
        ],
        antwoord=0,
        uitleg="Allebei zoeken ze het beste punt binnen hun mogelijkheden, en allebei redeneren ze marginaal. Alleen wat ze maximaliseren verschilt.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle bedrijven in dezelfde sector hebben dezelfde optimale productiegrootte.",
        antwoord=False,
        uitleg="Ze krijgen allemaal dezelfde prijs, maar hun kostenstructuur en dus hun MK-curve verschillen. Daarom ligt hun snijpunt bij een andere hoeveelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een bedrijf dat per vergissing één stuk te veel produceert?",
        opties=[
            "Het maakt iets minder winst",
            "Het maakt noodzakelijk verlies",
            "Het maakt precies evenveel winst",
            "Het verliest zijn hele omzet van dat jaar",
        ],
        antwoord=0,
        uitleg="Dat ene stuk kost net iets meer dan het opbrengt. Het verschil is klein, maar de winst ligt lager dan in het optimum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel geeft TO en TK per hoeveelheid. Hoe vind je daarmee het optimum?",
        opties=[
            "Je zoekt het grootste verschil tussen TO en TK",
            "Je zoekt de hoeveelheid waar TO het grootst is",
            "Je zoekt waar TK het kleinst is",
            "Je zoekt waar TO en TK gelijk zijn",
        ],
        antwoord=0,
        uitleg="De winst is TO min TK, dus het grootste verschil is de hoogste winst. Waar TO en TK gelijk zijn, is net het break-evenpunt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het break-evenpunt?",
        opties=[
            "De hoeveelheid waarbij TO precies TK dekt",
            "De hoeveelheid waarbij de winst van het bedrijf het grootst is",
            "De hoeveelheid waarbij de marginale kost het laagst is",
            "De hoeveelheid waarbij een bedrijf stopt met produceren",
        ],
        antwoord=0,
        uitleg="Op het break-evenpunt is de winst nul: alles is gedekt, meer niet. Het winstmaximum ligt daar meestal verderop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf heeft 4 000 euro constante kosten, verkoopt aan 20 euro en heeft 12 euro variabele kost per stuk. Hoeveel stuks moet het verkopen om break-even te draaien?",
        opties=[
            "500",
            "200",
            "333",
            "800",
        ],
        antwoord=0,
        uitleg="Elk stuk levert 20 min 12 is 8 euro op om de constante kosten te dekken. 4 000 gedeeld door 8 is 500 stuks.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen de prijs en de variabele kost per stuk? Schrijf één woord.",
        antwoord=["dekkingsbijdrage", "marge", "brutomarge"],
        uitleg="De dekkingsbijdrage per stuk is wat er overblijft om de constante kosten te dekken. Zijn die gedekt, dan wordt alles daarna winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf verkoopt boven zijn break-evenpunt. Wat weet je? Duid alles aan wat juist is.",
        opties=[
            "De constante kosten zijn gedekt",
            "Elk extra stuk levert zijn dekkingsbijdrage als winst op",
            "De totale opbrengst ligt boven de totale kosten",
            "De marginale kost is daar altijd nul",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voorbij break-even is alles gedekt en wordt elke bijkomende marge winst. De marginale kost blijft gewoon positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer maakt een bedrijf in zijn optimum toch verlies?",
        opties=[
            "Wanneer de prijs onder zijn gemiddelde kost ligt",
            "Wanneer de prijs boven zijn marginale kost ligt",
            "Wanneer de marginale kost stijgt",
            "Wanneer de constante kosten hoog zijn",
        ],
        antwoord=0,
        uitleg="MK is gelijk aan MO zegt alleen dat dit de beste hoeveelheid is. Ligt de prijs onder GK, dan is dat de hoeveelheid met het kleinste verlies.",
    ),
    dict(
        type="waarofniet",
        vraag="MK gelijk aan MO betekent dat het bedrijf winst maakt.",
        antwoord=False,
        uitleg="Het betekent alleen dat dit de beste hoeveelheid is. Of er winst is, hangt af van de verhouding tussen de prijs en de gemiddelde kost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft een bedrijf met verlies op korte termijn soms toch produceren?",
        opties=[
            "Omdat het zo nog een deel van de huur dekt",
            "Omdat het anders meer belasting zou moeten betalen",
            "Omdat de prijs dan vanzelf stijgt",
            "Omdat het anders zijn klanten moet terugbetalen",
        ],
        antwoord=0,
        uitleg="Stoppen betekent dat de huur doorloopt zonder enige opbrengst. Zolang de prijs de variabele kost per stuk dekt, blijft er iets over voor de constante kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer sluit een bedrijf op korte termijn beter de deuren?",
        opties=[
            "Wanneer de prijs onder de GVK zakt",
            "Wanneer de prijs onder de gemiddelde kost per stuk zakt",
            "Wanneer de marginale kost stijgt",
            "Wanneer er verlies gemaakt wordt",
        ],
        antwoord=0,
        uitleg="Onder GVK brengt elk stuk minder op dan het aan grondstoffen en energie kost. Doorwerken vergroot dan het verlies.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waar de prijs gelijk is aan de laagste gemiddelde variabele kost? Schrijf drie woorden.",
        antwoord=["het sluitingspunt", "sluitingspunt", "het stoppunt"],
        uitleg="Onder het sluitingspunt dekt de opbrengst zelfs de variabele kosten niet meer. Dan is stoppen minder duur dan doorgaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf verkoopt aan 9 euro, zijn GVK is 7 euro en zijn GK 11 euro. Wat doet het op korte termijn?",
        opties=[
            "Doorproduceren, want de GVK is gedekt",
            "Stoppen, want het maakt op elk stuk verlies",
            "De prijs verhogen tot 11 euro",
            "De productie verdubbelen",
        ],
        antwoord=0,
        uitleg="Er is verlies, want 9 ligt onder 11. Maar 9 ligt boven 7, dus elk stuk levert nog 2 euro voor de constante kosten. Stoppen zou duurder uitvallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Op lange termijn stopt een bedrijf beter als de prijs onder zijn gemiddelde kost blijft liggen.",
        antwoord=True,
        uitleg="Op lange termijn kan het al zijn kosten vermijden door te stoppen, ook de huur. Blijft de prijs onder de gemiddelde kost, dan heeft doorgaan geen zin meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lees je de winst af in een grafiek met prijs, GK en de hoeveelheid?",
        opties=[
            "Als de rechthoek tussen prijs en GK",
            "Als het hele stuk onder de curve van MK",
            "Als het stuk onder de prijslijn",
            "Als het verschil tussen MK en GVK",
        ],
        antwoord=0,
        uitleg="De winst per stuk is prijs min GK, en dat maal de hoeveelheid geeft de totale winst: een rechthoek met die hoogte en die breedte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over winst en verlies in beeld kloppen? Duid alles aan wat juist is.",
        opties=[
            "Ligt de prijs boven GK, dan is er winst",
            "Ligt de prijs onder GK, dan is er verlies",
            "Ligt de prijs precies op GK, dan is de winst nul",
            "Ligt de prijs boven MK, dan is er altijd winst",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vergelijking met GK beslist over winst of verlies. MK zegt alleen iets over de beste hoeveelheid, niet over het resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf maakt 2 000 stuks, de prijs is 15 euro en GK is 13 euro. Hoe groot is de totale winst?",
        opties=[
            "4 000 euro",
            "2 000 euro",
            "30 000 euro",
            "26 000 euro",
        ],
        antwoord=0,
        uitleg="Per stuk 15 min 13 is 2 euro winst, maal 2 000 stuks is 4 000 euro.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bedrijf dat zijn omzet verdubbelt, verdubbelt daarmee ook zijn winst.",
        antwoord=False,
        uitleg="De kosten stijgen mee, en vanaf een bepaald punt zelfs sneller dan de opbrengsten. Meer omzet is dus niet automatisch meer winst.",
    ),
    dict(
        type="waarofniet",
        vraag="Valt er winst te halen in een markt met volkomen concurrentie, dan treden er nieuwe bedrijven toe en zakt de prijs.",
        antwoord=True,
        uitleg="Toetreden is bij volkomen concurrentie vrij. Winst trekt nieuwkomers aan, het aanbod stijgt en de marktprijs zakt, tot er alleen nog een normale vergoeding overblijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beslissingen neemt een bedrijf op basis van deze theorie? Duid alles aan wat juist is.",
        opties=[
            "Hoeveel het produceert bij een gegeven prijs",
            "Of het bij een lage prijs blijft doorproduceren",
            "Vanaf welke verkoop het break-even draait",
            "Welke prijs het aan zijn klanten vraagt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij volkomen concurrentie ligt de prijs vast op de markt. Het bedrijf kiest alleen zijn hoeveelheid en beslist of het blijft produceren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de hoeveelheid waarbij de winst nul is? Schrijf twee woorden.",
        antwoord=["break-evenpunt", "break even punt", "kritisch punt"],
        uitleg="In het break-evenpunt dekt de totale opbrengst precies de totale kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een restaurant draait 's winters met verlies maar blijft open. Wanneer is dat verstandig?",
        opties=[
            "Zolang de opbrengst meer dan de variabele kosten dekt",
            "Zolang de opbrengst meer dan de constante kosten dekt",
            "Zolang er klanten binnenkomen",
            "Zolang de prijzen niet dalen",
        ],
        antwoord=0,
        uitleg="De huur loopt toch door. Zolang elke klant meer opbrengt dan hij aan eten en energie kost, draagt hij bij aan de vaste lasten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet het winstmaximalisatie en niet opbrengstmaximalisatie?",
        opties=[
            "Omdat het om het verschil gaat, niet om de opbrengst",
            "Omdat de opbrengsten altijd vastliggen",
            "Omdat de kosten niet te berekenen zijn",
            "Omdat de opbrengst van een bedrijf gelijk is aan zijn winst",
        ],
        antwoord=0,
        uitleg="Wie alleen opbrengst najaagt, produceert te veel: de laatste stuks kosten dan meer dan ze opleveren. Het gaat om wat er netto overblijft.",
    ),
]
