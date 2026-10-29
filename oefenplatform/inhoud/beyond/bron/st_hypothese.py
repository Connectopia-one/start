# -*- coding: utf-8 -*-
"""Hypothesen opstellen: de nulhypothese, de alternatieve hypothese en de keuze
tussen eenzijdig en tweezijdig.

De fiche splitst de hypothesetoets in twee leerdoelen die elk hun eigen
moeilijkheid hebben: eerst de hypothesen opstellen en de voorwaarden
controleren, dan de p-waarde berekenen en besluiten. Dat eerste staat hier,
het tweede in het volgende thema.

De bijlage noteert de nulhypothese als H met index nul en de alternatieve
hypothese als H met index één. Wij schrijven in de vragen H0 en H1, want een
kind kan dat intikken.

Twee fouten die kinderen hier bijna altijd maken, en daarom staan ze als
vraag in dit thema:
  1. Een hypothese formuleren over de steekproef in plaats van over de
     populatie. H0 gaat over mu of over p, nooit over x met een streepje of
     over p met een dakje.
  2. De richting van H1 uit de steekproef halen in plaats van uit de vraag.
     Wat je wil aantonen, bepaalt of de toets links, rechts of tweezijdig is,
     en dat beslis je vóór je naar je data kijkt.

Deel 1 is H0 en H1 opstellen.
Deel 2 is eenzijdig of tweezijdig, en de voorwaarden controleren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de nulhypothese bij een hypothesetoets?",
        opties=[
            "de aanname die geldt zolang de data niet het tegendeel aantonen",
            "de bewering die je zeker wil aantonen met je onderzoek",
            "het gemiddelde dat je in je steekproef gevonden hebt",
            "de kans dat je besluit fout is bij dit onderzoek",
        ],
        antwoord=0,
        uitleg=r"\(H_{0}\) is het uitgangspunt: er is niets veranderd, er is geen verschil. Je verwerpt ze alleen bij sterk tegenbewijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de alternatieve hypothese?",
        opties=[
            "de bewering die je wil aantonen met je onderzoek",
            "de aanname waar iedereen tot nu toe van uitging",
            "het resultaat dat je in je steekproef gemeten hebt",
            "de kans dat je nulhypothese toch waar is",
        ],
        antwoord=0,
        uitleg=r"\(H_{1}\) is wat je hoopt of vreest aan te tonen. \(H_{0}\) en \(H_{1}\) sluiten elkaar uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De nulhypothese en de alternatieve hypothese gaan over de populatie en niet over de steekproef.",
        antwoord=True,
        uitleg=r"Je hypothesen bevatten \(\mu\) of \(p\), nooit \(\bar{x}\) of \(\hat{p}\). De steekproef is je bewijsmateriaal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een fabrikant beweert dat zijn pakken gemiddeld vijfhonderd gram wegen. Een controleur vermoedt dat ze te licht zijn. Wat is \(H_{0}\)?",
        opties=[
            r"\(\mu = 500\)",
            r"\(\mu < 500\)",
            r"\(\bar{x} = 500\)",
            r"\(\mu > 500\)",
        ],
        antwoord=0,
        uitleg=r"\(H_{0}\) is altijd de gelijkheid, de bestaande bewering. Het vermoeden van de controleur komt in \(H_{1}\) terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde controleur vermoedt dat de pakken te licht zijn. Wat is \(H_{1}\)?",
        opties=[
            r"\(\mu < 500\)",
            r"\(\mu > 500\)",
            r"\(\mu = 500\)",
            r"\(\mu \neq 500\)",
        ],
        antwoord=0,
        uitleg="Te licht betekent kleiner dan. Dat geeft een linkszijdige toets.",
    ),
    dict(
        type="invultekst",
        vraag="Welk teken staat er altijd in de nulhypothese? Geef het teken.",
        antwoord=["=", "is gelijk aan", "gelijkheid"],
        uitleg=r"\(H_{0}\) is altijd een gelijkheid. De ongelijkheid zit in \(H_{1}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Je kiest de richting van \(H_{1}\) nadat je de steekproefresultaten gezien hebt.",
        antwoord=False,
        uitleg="Nooit. De richting volgt uit de onderzoeksvraag en staat vast vóór je de data bekijkt. Anders toets je niets.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een school beweert dat \(60\) procent van haar leerlingen slaagt. Een krant vermoedt dat het minder is. Wat is \(H_{0}\)?",
        opties=[
            r"\(p = 0\) komma zestig",
            r"\(p < 0\) komma zestig",
            r"\(\hat{p} = 0\) komma zestig",
            r"\(p > 0\) komma zestig",
        ],
        antwoord=0,
        uitleg=r"Bij een proportie staat er \(p\) in de hypothese, en \(H_{0}\) is weer de gelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom zet men de bewering die men wil aantonen in \(H_{1}\) en niet in \(H_{0}\)?",
        opties=[
            r"omdat je enkel \(H_{0}\) kan verwerpen, en zo lever je bewijs voor \(H_{1}\)",
            r"omdat \(H_{0}\) altijd waar moet zijn in een toets",
            r"omdat \(H_{1}\) de kleinste kans van de twee heeft",
            r"omdat een rekenapp alleen met \(H_{1}\) kan rekenen",
        ],
        antwoord=0,
        uitleg=r"Een toets kan \(H_{0}\) verwerpen of niet verwerpen. Ze kan niets bewijzen, dus leg je je bewering aan de kant van \(H_{1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een onderzoeker schrijft \(H_{0}\): \(\bar{x} = 20\). Wat is daar fout aan?",
        opties=[
            r"een hypothese gaat over de populatie, dus over \(\mu\) en niet over het steekproefgemiddelde",
            "het getal twintig is te klein voor een hypothese",
            r"\(H_{0}\) mag geen gelijkheid bevatten, enkel \(H_{1}\) mag dat",
            "er is niets fout, dat is een geldige nulhypothese",
        ],
        antwoord=0,
        uitleg="Het steekproefgemiddelde is een getal dat je meet. Over een gemeten getal stel je geen hypothese op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(H_{0}\) en \(H_{1}\) mogen elkaar overlappen.",
        antwoord=False,
        uitleg="Ze moeten elkaar uitsluiten, anders kan je op grond van je data niet tussen de twee kiezen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een nieuwe lesmethode moet het gemiddelde boven de huidige zeventig tillen. Wat is \(H_{1}\)?",
        opties=[
            r"\(\mu > 70\)",
            r"\(\mu < 70\)",
            r"\(\mu = 70\)",
            r"\(\mu \neq 70\)",
        ],
        antwoord=0,
        uitleg="Je wil een verbetering aantonen, dus een rechtszijdige toets.",
    ),
    dict(
        type="invultekst",
        vraag="Welke letter met welk indexcijfer gebruikt de bijlage voor de nulhypothese? Geef ze zoals je ze intikt.",
        antwoord=["H0", "h0"],
        uitleg="H met index nul voor de nulhypothese, H met index één voor de alternatieve hypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is er mis met de hypothese \(H_{0}\): \(\mu > 100\)?",
        opties=[
            r"\(H_{0}\) moet een gelijkheid zijn, een ongelijkheid hoort in \(H_{1}\)",
            "honderd is een te rond getal voor een hypothese",
            "er ontbreekt een steekproefgrootte in de hypothese",
            "er is niets mis, dat mag ook als nulhypothese",
        ],
        antwoord=0,
        uitleg=r"Zonder gelijkheid in \(H_{0}\) kan je geen steekproevenverdeling opstellen, want je hebt een concreet getal nodig.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een hypothesetoets over een proportie staat er \(p\) in de hypothesen en bij een toets over een gemiddelde \(\mu\).",
        antwoord=True,
        uitleg="Dat bepaalt ook welke voorwaarden uit het formularium je moet controleren.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een arts wil nagaan of een nieuw medicijn een ander effect heeft dan het oude, zonder te zeggen beter of slechter. Wat is \(H_{1}\)?",
        opties=[
            r"\(\mu\) verschilt van de huidige waarde",
            r"\(\mu\) is groter dan de huidige waarde",
            r"\(\mu\) is kleiner dan de huidige waarde",
            r"\(\mu\) is gelijk aan de huidige waarde",
        ],
        antwoord=0,
        uitleg="Een ander effect kan in twee richtingen, dus een tweezijdige toets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een hypothesetoets?",
        opties=[
            r"je formuleert \(H_{0}\) en \(H_{1}\) in woorden en in symbolen",
            r"je berekent de \(p\)-waarde met een rekenapp",
            "je kiest de steekproefgrootte die het mooiste resultaat geeft",
            "je bekijkt de data en zoekt het meest opvallende verschil",
        ],
        antwoord=0,
        uitleg=r"Pas daarna controleer je de voorwaarden, reken je de \(p\)-waarde uit en besluit je.",
    ),
    dict(
        type="invultekst",
        vraag="Over welk getal van de populatie gaat een hypothese bij een proportie? Eén letter.",
        antwoord=["p"],
        uitleg=r"De populatieproportie \(p\), niet de steekproefproportie \(\hat{p}\).",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag twee verschillende alternatieve hypothesen tegelijk toetsen met één toets.",
        antwoord=False,
        uitleg=r"Eén toets, één \(H_{1}\). Wil je twee dingen weten, dan doe je twee toetsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente beweert dat de gemiddelde wachttijd tien minuten is. Bewoners klagen dat het langer duurt. Welk paar hypothesen hoort daarbij?",
        opties=[
            r"\(H_{0}\): \(\mu = 10\) en \(H_{1}\): \(\mu > 10\)",
            r"\(H_{0}\): \(\mu > 10\) en \(H_{1}\): \(\mu = 10\)",
            r"\(H_{0}\): \(\mu = 10\) en \(H_{1}\): \(\mu < 10\)",
            r"\(H_{0}\): \(\mu < 10\) en \(H_{1}\): \(\mu > 10\)",
        ],
        antwoord=0,
        uitleg=r"De bewering van de gemeente is de gelijkheid in \(H_{0}\), de klacht van de bewoners de richting in \(H_{1}\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een hypothesetoets tweezijdig?",
        opties=[
            r"als \(H_{1}\) zegt dat de waarde verschilt, zonder een richting te noemen",
            r"als \(H_{1}\) zegt dat de waarde groter is dan het getal in \(H_{0}\)",
            "als je twee steekproeven met elkaar vergelijkt",
            "als er twee voorwaarden uit het formularium gecontroleerd moeten worden",
        ],
        antwoord=0,
        uitleg="Verschilt van betekent zowel groter als kleiner, dus je kijkt naar beide staarten van de verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een toets met \(H_{1}\): \(p\) is groter dan \(0{,}3\) is welk soort toets?",
        opties=["rechtszijdig", "linkszijdig", "tweezijdig", "dat hangt van de data af"],
        antwoord=0,
        uitleg="Groter dan wijst naar rechts op de getallenas, dus je kijkt enkel naar de rechterstaart.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een toets met \(H_{1}\): \(\mu < 50\) is welk soort toets?",
        opties=["linkszijdig", "rechtszijdig", "tweezijdig", "eenzijdig naar rechts"],
        antwoord=0,
        uitleg="Kleiner dan wijst naar links, dus je kijkt enkel naar de linkerstaart.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een tweezijdige toets verdeel je het significantieniveau over de twee staarten.",
        antwoord=True,
        uitleg=r"Bij \(\alpha\) gelijk aan \(0{,}05\) zit er dus \(0{,}025\) in elke staart.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat controleer je nadat je \(H_{0}\) en \(H_{1}\) opgesteld hebt?",
        opties=[
            "of de voorwaarden om de steekproevenverdeling te benaderen voldaan zijn",
            r"of de \(p\)-waarde kleiner is dan \(0{,}05\)",
            "of je besluit overeenkomt met wat je verwacht had",
            "of de steekproef groter is dan de populatie",
        ],
        antwoord=0,
        uitleg="Dat is een stap op zich. Zijn de voorwaarden niet voldaan, dan mag je niet verder rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij een toets over een gemiddelde met \(n\) gelijk aan vijfenveertig: is de voorwaarde voldaan?",
        opties=[
            "ja, want vijfenveertig is minstens dertig",
            r"nee, want \(n\) moet minstens vijftig zijn",
            r"nee, want je moet ook \(n \cdot p\) controleren",
            "dat kan je niet weten zonder de standaardafwijking",
        ],
        antwoord=0,
        uitleg=r"Bij een gemiddelde geeft het formularium enkel \(n\) minstens dertig. De twee extra voorwaarden gelden voor een proportie.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een toets over een proportie moet je ook \(n \cdot p\) en \(n\) maal (\(1\) min \(p\)) controleren.",
        antwoord=True,
        uitleg=r"Allebei minstens tien, naast \(n\) minstens dertig. Zo staat het in het formularium.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke parameters heeft de steekproevenverdeling van het steekproefgemiddelde onder \(H_{0}\)?",
        opties=[
            r"het gemiddelde uit \(H_{0}\) en \(\sigma : \sqrt{n}\)",
            r"het gemiddelde uit de steekproef en \(\sigma\)",
            r"het gemiddelde uit \(H_{1}\) en \(\sigma : n\)",
            "nul en één, want je standaardiseert altijd eerst",
        ],
        antwoord=0,
        uitleg=r"Je rekent alsof \(H_{0}\) waar is. Dat is de hele logica van een toets: hoe vreemd is mijn data in die wereld?",
    ),
    dict(
        type="invultekst",
        vraag=r"Een toets met \(H_{1}\): \(\mu \neq 100\) heeft hoeveel staarten? Geef het getal in cijfers.",
        antwoord=["2", "twee"],
        uitleg="Verschilt van is tweezijdig, dus twee staarten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een tweezijdige toets moeilijker om een verschil mee aan te tonen dan een eenzijdige?",
        opties=[
            "omdat je het significantieniveau over twee staarten moet verdelen",
            "omdat je twee keer zoveel data nodig hebt",
            r"omdat de \(p\)-waarde dan altijd groter is dan één",
            "omdat je dan twee nulhypothesen moet opstellen",
        ],
        antwoord=0,
        uitleg=r"Elke staart krijgt maar de helft van \(\alpha\), dus de grens ligt verder weg en je hebt een groter verschil nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeker mag van tweezijdig naar eenzijdig overstappen als zijn tweezijdige toets niet significant uitkomt.",
        antwoord=False,
        uitleg="Dat is dataschoffelen. De richting hoort vast te staan vóór je de data bekijkt, anders is je besluit waardeloos.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een slaagcijfer van \(60\) procent wordt getoetst met \(n = 100\). Is de proportievoorwaarde voldaan?",
        opties=[
            r"ja, honderd is minstens dertig, \(n \cdot p\) is zestig en \(n \cdot (1-p)\) is veertig",
            r"nee, want \(n \cdot p\) is te groot",
            r"nee, want \(60\) procent ligt te ver van de helft",
            r"ja, maar enkel omdat \(p\) groter is dan de helft",
        ],
        antwoord=0,
        uitleg="Alle drie de getallen halen hun drempel van dertig en tien.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een onderzoeker toetst een proportie met \(n = 50\) en \(p\) gelijk aan \(0{,}08\). Wat besluit hij?",
        opties=[
            r"de voorwaarden zijn niet voldaan, want \(n \cdot p\) is vier",
            "de voorwaarden zijn voldaan, want vijftig is groter dan dertig",
            "hij mag verder rekenen maar met een groter significantieniveau",
            "hij moet een tweezijdige toets gebruiken in plaats van een eenzijdige",
        ],
        antwoord=0,
        uitleg="Vier is kleiner dan tien. Hij heeft een veel grotere steekproef nodig, of een andere aanpak.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe noemt men een toets waarbij \(H_{1}\) enkel naar één kant kijkt? Eén woord.",
        antwoord=["eenzijdig", "eenzijdige", "enkelzijdig"],
        uitleg="Eenzijdig, met als twee vormen linkszijdig en rechtszijdig.",
    ),
    dict(
        type="waarofniet",
        vraag="De keuze tussen eenzijdig en tweezijdig volgt uit de grootte van de steekproef.",
        antwoord=False,
        uitleg="Ze volgt uit de onderzoeksvraag. Vraagt men of iets beter is, dan is het eenzijdig; vraagt men of er een verschil is, dan tweezijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf wil weten of een nieuwe verpakking de verkoop verandert, in welke richting dan ook. Welke toets kiest het?",
        opties=[
            "een tweezijdige toets",
            "een linkszijdige toets",
            "een rechtszijdige toets",
            "twee eenzijdige toetsen na elkaar",
        ],
        antwoord=0,
        uitleg="Verandert, zonder richting, is per definitie tweezijdig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom reken je bij een hypothesetoets met het getal uit \(H_{0}\) en niet met het getal uit je steekproef?",
        opties=[
            r"omdat je wil weten hoe waarschijnlijk je data zijn in de wereld waar \(H_{0}\) geldt",
            r"omdat het getal in \(H_{0}\) altijd nauwkeuriger is dan dat van de steekproef",
            r"omdat de rekenapp enkel het getal uit \(H_{0}\) aanvaardt",
            "omdat het steekproefgetal pas op het einde nodig is voor de besluitvorming",
        ],
        antwoord=0,
        uitleg="Zijn je data in die wereld heel onwaarschijnlijk, dan twijfel je aan die wereld. Dat is de kern van het toetsen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenzijdige toets naar rechts kijk je naar de kans op een resultaat dat minstens zo groot is als het gevondene.",
        antwoord=True,
        uitleg=r"Precies dat is de \(p\)-waarde bij een rechtszijdige toets.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een krant schrijft: wij toetsen of de nieuwe maatregel werkt. Welke \(H_{0}\) hoort daarbij?",
        opties=[
            "de maatregel heeft geen effect",
            "de maatregel heeft een positief effect",
            "de maatregel heeft een negatief effect",
            "de maatregel werkt bij de helft van de mensen",
        ],
        antwoord=0,
        uitleg=r"\(H_{0}\) is altijd het saaie geval: geen verschil, geen effect. Pas als de data dat onwaarschijnlijk maken, besluit je anders.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een leerling schrijft \(H_{0}\): \(\mu = 50\) en \(H_{1}\): \(\mu > 60\). Wat is er mis?",
        opties=[
            r"\(H_{0}\) en \(H_{1}\) moeten samen alle mogelijkheden dekken en hetzelfde getal gebruiken",
            r"\(H_{1}\) mag geen groter dan bevatten bij een gemiddelde",
            r"het getal in \(H_{1}\) moet kleiner zijn dan dat in \(H_{0}\)",
            "er is niets mis, de twee hypothesen sluiten elkaar uit",
        ],
        antwoord=0,
        uitleg=r"Nu valt alles tussen vijftig en zestig buiten beide hypothesen. Gebruik in \(H_{0}\) en \(H_{1}\) hetzelfde getal.",
    ),
]
