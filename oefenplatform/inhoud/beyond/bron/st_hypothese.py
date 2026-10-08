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
        uitleg="H0 is het uitgangspunt: er is niets veranderd, er is geen verschil. Je verwerpt ze alleen bij sterk tegenbewijs.",
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
        uitleg="H1 is wat je hoopt of vreest aan te tonen. H0 en H1 sluiten elkaar uit.",
    ),
    dict(
        type="waarofniet",
        vraag="De nulhypothese en de alternatieve hypothese gaan over de populatie en niet over de steekproef.",
        antwoord=True,
        uitleg="Je hypothesen bevatten mu of p, nooit x met een streepje of p met een dakje. De steekproef is je bewijsmateriaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fabrikant beweert dat zijn pakken gemiddeld vijfhonderd gram wegen. Een controleur vermoedt dat ze te licht zijn. Wat is H0?",
        opties=[
            "mu is gelijk aan vijfhonderd",
            "mu is kleiner dan vijfhonderd",
            "x met een streepje is gelijk aan vijfhonderd",
            "mu is groter dan vijfhonderd",
        ],
        antwoord=0,
        uitleg="H0 is altijd de gelijkheid, de bestaande bewering. Het vermoeden van de controleur komt in H1 terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde controleur vermoedt dat de pakken te licht zijn. Wat is H1?",
        opties=[
            "mu is kleiner dan vijfhonderd",
            "mu is groter dan vijfhonderd",
            "mu is gelijk aan vijfhonderd",
            "mu verschilt van vijfhonderd",
        ],
        antwoord=0,
        uitleg="Te licht betekent kleiner dan. Dat geeft een linkszijdige toets.",
    ),
    dict(
        type="invultekst",
        vraag="Welk teken staat er altijd in de nulhypothese? Geef het teken.",
        antwoord=["=", "is gelijk aan", "gelijkheid"],
        uitleg="H0 is altijd een gelijkheid. De ongelijkheid zit in H1.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kiest de richting van H1 nadat je de steekproefresultaten gezien hebt.",
        antwoord=False,
        uitleg="Nooit. De richting volgt uit de onderzoeksvraag en staat vast vóór je de data bekijkt. Anders toets je niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school beweert dat zestig procent van haar leerlingen slaagt. Een krant vermoedt dat het minder is. Wat is H0?",
        opties=[
            "p is gelijk aan nul komma zestig",
            "p is kleiner dan nul komma zestig",
            "p met een dakje is gelijk aan nul komma zestig",
            "p is groter dan nul komma zestig",
        ],
        antwoord=0,
        uitleg="Bij een proportie staat er p in de hypothese, en H0 is weer de gelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet men de bewering die men wil aantonen in H1 en niet in H0?",
        opties=[
            "omdat je enkel H0 kan verwerpen, en zo lever je bewijs voor H1",
            "omdat H0 altijd waar moet zijn in een toets",
            "omdat H1 de kleinste kans van de twee heeft",
            "omdat een rekenapp alleen met H1 kan rekenen",
        ],
        antwoord=0,
        uitleg="Een toets kan H0 verwerpen of niet verwerpen. Ze kan niets bewijzen, dus leg je je bewering aan de kant van H1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker schrijft H0: x met een streepje is gelijk aan twintig. Wat is daar fout aan?",
        opties=[
            "een hypothese gaat over de populatie, dus over mu en niet over het steekproefgemiddelde",
            "het getal twintig is te klein voor een hypothese",
            "H0 mag geen gelijkheid bevatten, enkel H1 mag dat",
            "er is niets fout, dat is een geldige nulhypothese",
        ],
        antwoord=0,
        uitleg="Het steekproefgemiddelde is een getal dat je meet. Over een gemeten getal stel je geen hypothese op.",
    ),
    dict(
        type="waarofniet",
        vraag="H0 en H1 mogen elkaar overlappen.",
        antwoord=False,
        uitleg="Ze moeten elkaar uitsluiten, anders kan je op grond van je data niet tussen de twee kiezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nieuwe lesmethode moet het gemiddelde boven de huidige zeventig tillen. Wat is H1?",
        opties=[
            "mu is groter dan zeventig",
            "mu is kleiner dan zeventig",
            "mu is gelijk aan zeventig",
            "mu verschilt van zeventig",
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
        vraag="Wat is er mis met de hypothese H0: mu is groter dan honderd?",
        opties=[
            "H0 moet een gelijkheid zijn, een ongelijkheid hoort in H1",
            "honderd is een te rond getal voor een hypothese",
            "er ontbreekt een steekproefgrootte in de hypothese",
            "er is niets mis, dat mag ook als nulhypothese",
        ],
        antwoord=0,
        uitleg="Zonder gelijkheid in H0 kan je geen steekproevenverdeling opstellen, want je hebt een concreet getal nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een hypothesetoets over een proportie staat er p in de hypothesen en bij een toets over een gemiddelde mu.",
        antwoord=True,
        uitleg="Dat bepaalt ook welke voorwaarden uit het formularium je moet controleren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een arts wil nagaan of een nieuw medicijn een ander effect heeft dan het oude, zonder te zeggen beter of slechter. Wat is H1?",
        opties=[
            "mu verschilt van de huidige waarde",
            "mu is groter dan de huidige waarde",
            "mu is kleiner dan de huidige waarde",
            "mu is gelijk aan de huidige waarde",
        ],
        antwoord=0,
        uitleg="Een ander effect kan in twee richtingen, dus een tweezijdige toets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij een hypothesetoets?",
        opties=[
            "je formuleert H0 en H1 in woorden en in symbolen",
            "je berekent de p-waarde met een rekenapp",
            "je kiest de steekproefgrootte die het mooiste resultaat geeft",
            "je bekijkt de data en zoekt het meest opvallende verschil",
        ],
        antwoord=0,
        uitleg="Pas daarna controleer je de voorwaarden, reken je de p-waarde uit en besluit je.",
    ),
    dict(
        type="invultekst",
        vraag="Over welk getal van de populatie gaat een hypothese bij een proportie? Eén letter.",
        antwoord=["p"],
        uitleg="De populatieproportie p, niet de steekproefproportie p met een dakje.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag twee verschillende alternatieve hypothesen tegelijk toetsen met één toets.",
        antwoord=False,
        uitleg="Eén toets, één H1. Wil je twee dingen weten, dan doe je twee toetsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente beweert dat de gemiddelde wachttijd tien minuten is. Bewoners klagen dat het langer duurt. Welk paar hypothesen hoort daarbij?",
        opties=[
            "H0: mu is gelijk aan tien en H1: mu is groter dan tien",
            "H0: mu is groter dan tien en H1: mu is gelijk aan tien",
            "H0: mu is gelijk aan tien en H1: mu is kleiner dan tien",
            "H0: mu is kleiner dan tien en H1: mu is groter dan tien",
        ],
        antwoord=0,
        uitleg="De bewering van de gemeente is de gelijkheid in H0, de klacht van de bewoners de richting in H1.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een hypothesetoets tweezijdig?",
        opties=[
            "als H1 zegt dat de waarde verschilt, zonder een richting te noemen",
            "als H1 zegt dat de waarde groter is dan het getal in H0",
            "als je twee steekproeven met elkaar vergelijkt",
            "als er twee voorwaarden uit het formularium gecontroleerd moeten worden",
        ],
        antwoord=0,
        uitleg="Verschilt van betekent zowel groter als kleiner, dus je kijkt naar beide staarten van de verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een toets met H1: p is groter dan nul komma drie is welk soort toets?",
        opties=["rechtszijdig", "linkszijdig", "tweezijdig", "dat hangt van de data af"],
        antwoord=0,
        uitleg="Groter dan wijst naar rechts op de getallenas, dus je kijkt enkel naar de rechterstaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een toets met H1: mu is kleiner dan vijftig is welk soort toets?",
        opties=["linkszijdig", "rechtszijdig", "tweezijdig", "eenzijdig naar rechts"],
        antwoord=0,
        uitleg="Kleiner dan wijst naar links, dus je kijkt enkel naar de linkerstaart.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een tweezijdige toets verdeel je het significantieniveau over de twee staarten.",
        antwoord=True,
        uitleg="Bij alfa gelijk aan nul komma nul vijf zit er dus nul komma nul twee vijf in elke staart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat controleer je nadat je H0 en H1 opgesteld hebt?",
        opties=[
            "of de voorwaarden om de steekproevenverdeling te benaderen voldaan zijn",
            "of de p-waarde kleiner is dan nul komma nul vijf",
            "of je besluit overeenkomt met wat je verwacht had",
            "of de steekproef groter is dan de populatie",
        ],
        antwoord=0,
        uitleg="De fiche vraagt dat als een apart leerdoel. Zijn de voorwaarden niet voldaan, dan mag je niet verder rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een toets over een gemiddelde met n gelijk aan vijfenveertig: is de voorwaarde voldaan?",
        opties=[
            "ja, want vijfenveertig is minstens dertig",
            "nee, want n moet minstens vijftig zijn",
            "nee, want je moet ook n maal p controleren",
            "dat kan je niet weten zonder de standaardafwijking",
        ],
        antwoord=0,
        uitleg="Bij een gemiddelde geeft het formularium enkel n minstens dertig. De twee extra voorwaarden gelden voor een proportie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een toets over een proportie moet je ook n maal p en n maal (1 min p) controleren.",
        antwoord=True,
        uitleg="Allebei minstens tien, naast n minstens dertig. Zo staat het in het formularium.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke parameters heeft de steekproevenverdeling van het steekproefgemiddelde onder H0?",
        opties=[
            "het gemiddelde uit H0 en sigma gedeeld door de wortel uit n",
            "het gemiddelde uit de steekproef en sigma",
            "het gemiddelde uit H1 en sigma gedeeld door n",
            "nul en één, want je standaardiseert altijd eerst",
        ],
        antwoord=0,
        uitleg="Je rekent alsof H0 waar is. Dat is de hele logica van een toets: hoe vreemd is mijn data in die wereld?",
    ),
    dict(
        type="invultekst",
        vraag="Een toets met H1: mu verschilt van honderd heeft hoeveel staarten? Geef het getal in cijfers.",
        antwoord=["2", "twee"],
        uitleg="Verschilt van is tweezijdig, dus twee staarten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een tweezijdige toets moeilijker om een verschil mee aan te tonen dan een eenzijdige?",
        opties=[
            "omdat je het significantieniveau over twee staarten moet verdelen",
            "omdat je twee keer zoveel data nodig hebt",
            "omdat de p-waarde dan altijd groter is dan één",
            "omdat je dan twee nulhypothesen moet opstellen",
        ],
        antwoord=0,
        uitleg="Elke staart krijgt maar de helft van alfa, dus de grens ligt verder weg en je hebt een groter verschil nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeker mag van tweezijdig naar eenzijdig overstappen als zijn tweezijdige toets niet significant uitkomt.",
        antwoord=False,
        uitleg="Dat is dataschoffelen. De richting hoort vast te staan vóór je de data bekijkt, anders is je besluit waardeloos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een slaagcijfer van zestig procent wordt getoetst met n gelijk aan honderd. Is de proportievoorwaarde voldaan?",
        opties=[
            "ja, honderd is minstens dertig, n maal p is zestig en n maal (1−p) is veertig",
            "nee, want n maal p is te groot",
            "nee, want zestig procent ligt te ver van de helft",
            "ja, maar enkel omdat p groter is dan de helft",
        ],
        antwoord=0,
        uitleg="Alle drie de getallen halen hun drempel van dertig en tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker toetst een proportie met n gelijk aan vijftig en p gelijk aan nul komma nul acht. Wat besluit hij?",
        opties=[
            "de voorwaarden zijn niet voldaan, want n maal p is vier",
            "de voorwaarden zijn voldaan, want vijftig is groter dan dertig",
            "hij mag verder rekenen maar met een groter significantieniveau",
            "hij moet een tweezijdige toets gebruiken in plaats van een eenzijdige",
        ],
        antwoord=0,
        uitleg="Vier is kleiner dan tien. Hij heeft een veel grotere steekproef nodig, of een andere aanpak.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een toets waarbij H1 enkel naar één kant kijkt? Eén woord.",
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
        vraag="Waarom reken je bij een hypothesetoets met het getal uit H0 en niet met het getal uit je steekproef?",
        opties=[
            "omdat je wil weten hoe waarschijnlijk je data zijn in de wereld waar H0 geldt",
            "omdat het getal in H0 altijd nauwkeuriger is dan dat van de steekproef",
            "omdat de rekenapp enkel het getal uit H0 aanvaardt",
            "omdat het steekproefgetal pas op het einde nodig is voor de besluitvorming",
        ],
        antwoord=0,
        uitleg="Zijn je data in die wereld heel onwaarschijnlijk, dan twijfel je aan die wereld. Dat is de kern van het toetsen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenzijdige toets naar rechts kijk je naar de kans op een resultaat dat minstens zo groot is als het gevondene.",
        antwoord=True,
        uitleg="Precies dat is de p-waarde bij een rechtszijdige toets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft: wij toetsen of de nieuwe maatregel werkt. Welke H0 hoort daarbij?",
        opties=[
            "de maatregel heeft geen effect",
            "de maatregel heeft een positief effect",
            "de maatregel heeft een negatief effect",
            "de maatregel werkt bij de helft van de mensen",
        ],
        antwoord=0,
        uitleg="H0 is altijd het saaie geval: geen verschil, geen effect. Pas als de data dat onwaarschijnlijk maken, besluit je anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling schrijft H0: mu is gelijk aan vijftig en H1: mu is groter dan zestig. Wat is er mis?",
        opties=[
            "H0 en H1 moeten samen alle mogelijkheden dekken en hetzelfde getal gebruiken",
            "H1 mag geen groter dan bevatten bij een gemiddelde",
            "het getal in H1 moet kleiner zijn dan dat in H0",
            "er is niets mis, de twee hypothesen sluiten elkaar uit",
        ],
        antwoord=0,
        uitleg="Nu valt alles tussen vijftig en zestig buiten beide hypothesen. Gebruik in H0 en H1 hetzelfde getal.",
    ),
]
