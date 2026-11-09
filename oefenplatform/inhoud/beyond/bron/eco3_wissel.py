# -*- coding: utf-8 -*-
"""De wisselmarkt en de betalingsbalans.

Fiche: wisselmarkt als markt met volkomen concurrentie; partijen op de
valutamarkt; prijsvorming grafisch; depreciatie en appreciatie;
wisselkoersrisico; factoren (inflatieverschillen, inkomenswijziging in
binnen- of buitenland, rentevoetwijzigingen, speculatie, voorkeur van
consumenten) en hun effect grafisch; vlottende en vaste wisselkoersen;
betalingsbalans, samenstelling en deelrekeningen; oorzaken en gevolgen van
onevenwicht; wisselwerking met de wisselkoers; taken van IMF, Wereldbank en
OESO.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de wisselmarkt een markt met volkomen concurrentie?",
        opties=[
            "veel kopers en verkopers van een homogeen product",
            "er is maar één aanbieder van elke munt",
            "de overheid legt alle koersen vast",
            "enkel banken mogen er kopen en verkopen",
        ],
        antwoord=0,
        uitleg="Een dollar is een dollar, en de koers is overal meteen bekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie vraagt euro's op de wisselmarkt?",
        opties=[
            "Amerikaanse bedrijven die Belgische producten kopen",
            "Belgische bedrijven die Amerikaanse producten kopen",
            "Belgische toeristen die naar New York reizen",
            "Europese beleggers die Amerikaanse aandelen kopen",
        ],
        antwoord=0,
        uitleg="Om in euro te betalen, moeten ze dollars omwisselen in euro's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke partijen zijn actief op de valutamarkt? Duid alle juiste antwoorden aan.",
        opties=["exporteurs en importeurs", "beleggers en speculanten", "enkel toeristen", "enkel de Europese Commissie"],
        antwoord=[0, 1],
        uitleg="Ook centrale banken en toeristen kopen en verkopen munten.",
    ),
    dict(
        type="meerkeuze",
        vraag="De koers EUR/USD gaat van 1,10 naar 1,20. Wat is er met de euro gebeurd?",
        opties=["de euro apprecieerde", "de euro deprecieerde", "de euro werd gedevalueerd", "er veranderde niets"],
        antwoord=0,
        uitleg="Eén euro is nu meer dollar waard.",
    ),
    dict(
        type="waarofniet",
        vraag="Een depreciatie van de euro maakt Europese producten goedkoper voor Amerikanen.",
        antwoord=True,
        uitleg="Met evenveel dollars krijgen ze meer euro's.",
    ),
    dict(
        type="meerkeuze",
        vraag="De euro deprecieert tegenover de dollar. Wat is het gevolg voor Belgische exporteurs naar de VS?",
        opties=[
            "hun producten worden goedkoper in dollar, dus ze verkopen meer",
            "hun producten worden duurder in dollar, dus ze verkopen minder",
            "er verandert niets aan hun verkoop",
            "ze mogen niet meer exporteren",
        ],
        antwoord=0,
        uitleg="Een zwakkere munt helpt de export.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het wisselkoersrisico?",
        opties=[
            "het risico dat een koerswijziging verlies oplevert",
            "het risico dat een bank failliet gaat",
            "het risico dat een product beschadigd aankomt",
            "het risico dat de rente stijgt",
        ],
        antwoord=0,
        uitleg="Een exporteur die over drie maanden dollars ontvangt, weet niet hoeveel euro dat dan waard is.",
    ),
    dict(
        type="meerkeuze",
        vraag="De inflatie in de eurozone is veel hoger dan in de VS. Wat gebeurt er met de euro?",
        opties=["hij deprecieert", "hij apprecieert", "hij blijft gelijk", "hij wordt vervangen"],
        antwoord=0,
        uitleg="Europese producten worden duurder: minder vraag naar euro, meer aanbod van euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="De ECB verhoogt de rente, terwijl de rente in de VS gelijk blijft. Wat verwacht je?",
        opties=[
            "de vraag naar euro stijgt en de euro apprecieert",
            "het aanbod van euro stijgt en de euro deprecieert",
            "de euro verandert niet",
            "de dollar apprecieert",
        ],
        antwoord=0,
        uitleg="Beleggen in euro wordt aantrekkelijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het inkomen in de VS stijgt sterk. Wat is het effect op de euro?",
        opties=[
            "Amerikanen kopen meer Europese producten, dus de euro apprecieert",
            "Amerikanen kopen minder Europese producten, dus de euro deprecieert",
            "geen effect",
            "de dollar wordt de munt van Europa",
        ],
        antwoord=0,
        uitleg="De vraagcurve naar euro schuift naar rechts.",
    ),
    dict(
        type="waarofniet",
        vraag="Als het inkomen in de eurozone stijgt, importeren Europeanen meer en neemt het aanbod van euro toe.",
        antwoord=True,
        uitleg="Ze wisselen euro's om voor buitenlandse munten. De euro deprecieert dan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Speculanten verwachten dat de euro zal stijgen. Wat doen ze en wat is het gevolg?",
        opties=[
            "ze kopen nu euro's, waardoor de euro al stijgt",
            "ze verkopen nu euro's, waardoor de euro daalt",
            "ze doen niets",
            "ze vragen de ECB om de koers vast te leggen",
        ],
        antwoord=0,
        uitleg="Verwachtingen kunnen zichzelf waarmaken.",
    ),
    dict(
        type="waarofniet",
        vraag="Als consumenten wereldwijd Europese producten verkiezen, deprecieert de euro.",
        antwoord=False,
        uitleg="De vraag naar euro stijgt, dus de euro apprecieert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vlottende wisselkoers?",
        opties=[
            "een koers die vrij bepaald wordt door vraag en aanbod",
            "een koers die de centrale bank vastlegt",
            "een koers die enkel op zon- en feestdagen verandert",
            "een koers die altijd 1 is",
        ],
        antwoord=0,
        uitleg="De euro en de dollar zweven vrij tegenover elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van een vaste wisselkoers?",
        opties=[
            "minder wisselkoersrisico voor bedrijven",
            "de centrale bank hoeft nooit in te grijpen",
            "de koers past zich vanzelf aan de economie aan",
            "inflatie wordt onmogelijk",
        ],
        antwoord=0,
        uitleg="Het nadeel: de centrale bank moet munten kopen of verkopen om de koers te verdedigen.",
    ),
    dict(
        type="invultekst",
        vraag="1 euro = 1,25 dollar. Hoeveel dollar betaalt een Amerikaan voor een product van 80 euro?",
        antwoord=["100", "100 dollar"],
        uitleg="80 · 1,25 = 100.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een appreciatie van de euro worden Amerikaanse producten goedkoper voor Europeanen.",
        antwoord=True,
        uitleg="Met één euro krijg je meer dollars.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de grafiek van de euromarkt als de vraag naar euro stijgt?",
        opties=[
            "de vraagcurve schuift naar rechts en de koers stijgt",
            "de aanbodcurve schuift naar rechts en de koers daalt",
            "de vraagcurve schuift naar links en de koers daalt",
            "beide curves blijven staan",
        ],
        antwoord=0,
        uitleg="Net als op elke markt met volkomen concurrentie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Belgische toerist die naar Japan reist, biedt yen aan en vraagt euro's.",
        antwoord=False,
        uitleg="Omgekeerd: hij wisselt euro's om in yen. Hij vraagt yen en biedt euro's aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij vlottende wisselkoersen bepaalt de regering elke dag de koers.",
        antwoord=False,
        uitleg="Vraag en aanbod op de wisselmarkt bepalen de koers.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de betalingsbalans?",
        opties=[
            "alle transacties van een land met het buitenland",
            "enkel de export en import van goederen",
            "de begroting van de overheid",
            "de balans van de Nationale Bank",
        ],
        antwoord=0,
        uitleg="Ze is breder dan de handelsbalans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke deelrekeningen bestaat de betalingsbalans?",
        opties=[
            "lopende, kapitaal- en financiële rekening",
            "de spaarrekening, de zichtrekening en de termijnrekening",
            "de handelsbalans, de begroting en de kringloop",
            "de geldmarkt, de kapitaalmarkt en de wisselmarkt",
        ],
        antwoord=0,
        uitleg="De lopende rekening bevat goederen, diensten, primaire en secundaire inkomens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgisch bedrijf verkoopt machines aan Duitsland. Op welke deelrekening komt dat?",
        opties=["de lopende rekening (goederen)", "de financiële rekening", "de kapitaalrekening", "de lopende rekening (diensten)"],
        antwoord=0,
        uitleg="Het is export van goederen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgische belegger koopt Amerikaanse aandelen. Op welke deelrekening komt dat?",
        opties=["de financiële rekening", "de lopende rekening (goederen)", "de lopende rekening (diensten)", "de handelsbalans"],
        antwoord=0,
        uitleg="Het is een belegging in het buitenland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Nederlandse toerist betaalt een hotel in Brugge. Op welke deelrekening komt dat?",
        opties=["de lopende rekening (diensten)", "de lopende rekening (goederen)", "de financiële rekening", "de kapitaalrekening"],
        antwoord=0,
        uitleg="Toerisme is export van diensten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgische werknemer stuurt een deel van zijn loon naar familie in Marokko. Waar komt dat?",
        opties=["de lopende rekening (secundaire inkomens)", "de lopende rekening (primaire inkomens)", "de kapitaalrekening", "de lopende rekening (goederen)"],
        antwoord=0,
        uitleg="Het is een inkomensoverdracht zonder tegenprestatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Dividenden die een Belg ontvangt van een buitenlands bedrijf horen bij de primaire inkomens.",
        antwoord=True,
        uitleg="Primaire inkomens zijn lonen, rente en dividenden uit het buitenland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke posten horen bij de lopende rekening? Duid alle juiste antwoorden aan.",
        opties=["goederen", "diensten", "aankoop van buitenlandse obligaties", "directe investeringen in een buitenlandse fabriek"],
        antwoord=[0, 1],
        uitleg="Obligaties en directe investeringen horen op de financiële rekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land heeft een groot tekort op de lopende rekening. Wat kan dat betekenen voor de munt bij vlottende koersen?",
        opties=[
            "de munt kan depreciëren",
            "de munt apprecieert zeker",
            "er is geen enkel verband met de munt",
            "de munt verdwijnt",
        ],
        antwoord=0,
        uitleg="Het land betaalt meer aan het buitenland dan het ontvangt, dus er wordt meer van de eigen munt aangeboden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een depreciatie van de munt kan helpen om een tekort op de lopende rekening te verkleinen.",
        antwoord=True,
        uitleg="De export wordt goedkoper, de import duurder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een taak van het IMF (Internationaal Monetair Fonds)?",
        opties=[
            "landen met betalingsbalansproblemen helpen",
            "ontwikkelingsprojecten zoals scholen en wegen financieren",
            "de handelsregels tussen landen vastleggen",
            "de rente in de eurozone bepalen",
        ],
        antwoord=0,
        uitleg="Het waakt over de stabiliteit van het internationaal monetair systeem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de hoofdtaak van de Wereldbank?",
        opties=[
            "armoede bestrijden met ontwikkelingsleningen",
            "de wisselkoersen van alle munten vastleggen",
            "de euro uitgeven",
            "kartels opsporen",
        ],
        antwoord=0,
        uitleg="Ze financiert projecten zoals infrastructuur, onderwijs en gezondheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de OESO?",
        opties=[
            "onderzoek en beleidsadvies voor haar lidstaten",
            "leningen geven aan landen in crisis",
            "bankbiljetten drukken voor de eurozone",
            "de olieprijs bepalen voor de hele wereld",
        ],
        antwoord=0,
        uitleg="Ze vergelijkt landen en geeft aanbevelingen, bijvoorbeeld met de PISA-studie.",
    ),
    dict(
        type="waarofniet",
        vraag="De Wereldbank bepaalt de wisselkoers van de dollar.",
        antwoord=False,
        uitleg="Bij vlottende koersen bepaalt de markt de koers. De Wereldbank financiert ontwikkeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="De euro apprecieert sterk. Wat is het gevolg voor de Belgische betalingsbalans?",
        opties=[
            "de export daalt en de import stijgt",
            "de export stijgt en de import daalt",
            "er verandert niets",
            "de betalingsbalans verdwijnt",
        ],
        antwoord=0,
        uitleg="Belgische producten worden duurder in het buitenland, buitenlandse goedkoper hier.",
    ),
    dict(
        type="invultekst",
        vraag="1 euro = 1,10 dollar. Een Belgische importeur moet een factuur van 5 500 dollar betalen. Hoeveel euro is dat?",
        antwoord=["5000", "5 000", "5.000"],
        uitleg="5 500 / 1,10 = 5 000.",
    ),
    dict(
        type="waarofniet",
        vraag="Een exporteur die later in dollar betaald wordt, verliest als de dollar in tussentijd stijgt tegenover de euro.",
        antwoord=False,
        uitleg="Hij wint: zijn dollars zijn dan meer euro waard. Hij verliest als de dollar daalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren doen de euro depreciëren? Duid alle juiste antwoorden aan.",
        opties=[
            "hogere inflatie in de eurozone dan in het buitenland",
            "een daling van de rente in de eurozone",
            "een stijgende voorkeur voor Europese producten",
            "een stijging van het inkomen in het buitenland",
        ],
        antwoord=[0, 1],
        uitleg="De andere twee verhogen de vraag naar euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Belgisch bedrijf bouwt een fabriek in Polen. Op welke deelrekening van de Belgische betalingsbalans komt dat?",
        opties=["de financiële rekening", "de lopende rekening (goederen)", "de lopende rekening (diensten)", "de lopende rekening (secundaire inkomens)"],
        antwoord=0,
        uitleg="Het is een directe investering in het buitenland.",
    ),
    dict(
        type="waarofniet",
        vraag="De handelsbalans is een onderdeel van de lopende rekening van de betalingsbalans.",
        antwoord=True,
        uitleg="De handel in goederen is het eerste deel van de lopende rekening.",
    ),
]
