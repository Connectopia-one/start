# -*- coding: utf-8 -*-
"""Bronnen van kennis, rationalisme en empirisme.

Het tweede van twaalf thema's over filosofie, en het eerste stuk kennisleer.
De fiche vraagt hier waar kennis vandaan komt, en zet twee stromingen tegenover
elkaar die daar tegengesteld op antwoorden.

De lijstjes staan letterlijk in de fiche:

    bronnen van kennis: afleiding, geheugen, introspectie, verhalen, zintuigen
    het verschil tussen waarneming en kennis aan de hand van de grotallegorie
        van Plato
    rationalisme volgens René Descartes: deductieve aanpak, methodische twijfel
    empirisme volgens John Locke en David Hume: inductieve aanpak
    empirisme en rationalisme herkennen in een gegeven voorbeeld, en hun
        verschillen uitleggen
    vaardigheden: een filosofische vraag formuleren, en argumenten voor en
        tegen een standpunt volgens de AUB-methode (bijlage 1)

De AUB-methode staat in de fiche bij elk filosofisch onderdeel opnieuw. Ze
krijgt haar eigen thema bij de argumentatieleer; hier staan er twee vragen over,
zodat ze vroeg in het vak al eens voorbijkomt.

Deel 1 zijn de vijf bronnen van kennis en de grotallegorie.
Deel 2 zijn het rationalisme en het empirisme.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Welke vijf bronnen van kennis noemt de fiche?",
         opties=["afleiding, geheugen, introspectie, verhalen en zintuigen",
                 "waarneming, meting, experiment, berekening en controle",
                 "deductie, inductie, abductie, intuïtie en traditie",
                 "zien, horen, ruiken, proeven en voelen samen genomen"],
         antwoord=0,
         uitleg="Die vijf staan letterlijk in de fiche. Let op: de zintuigen zijn er maar één van."),
    dict(type="meerkeuze",
         vraag="Je weet dat je gisteren aan zee was. Welke bron van kennis is dat?",
         opties=["het geheugen", "de zintuigen", "de introspectie", "een verhaal van iemand"],
         antwoord=0,
         uitleg="Wat je zelf hebt meegemaakt en opgeslagen, komt uit je geheugen."),
    dict(type="meerkeuze",
         vraag="Je weet dat je je op dit moment zenuwachtig voelt. Welke bron van kennis is dat?",
         opties=["de introspectie", "de zintuigen", "het geheugen", "de afleiding"],
         antwoord=0,
         uitleg="Introspectie is naar binnen kijken: wat je over je eigen gedachten en gevoelens "
                "te weten komt."),
    dict(type="meerkeuze",
         vraag="De straat is nat, dus het heeft geregend. Welke bron van kennis gebruik je hier?",
         opties=["de afleiding", "de zintuigen alleen", "het geheugen", "een verhaal"],
         antwoord=0,
         uitleg="Je neemt de natte straat waar, maar dat het geregend heeft zie je niet: dat leid "
                "je af. Afleiding bouwt verder op iets wat je al weet."),
    dict(type="meerkeuze",
         vraag="Je weet dat je overgrootmoeder in de oorlog een onderduiker verborg. Welke bron "
               "van kennis is dat?",
         opties=["een verhaal", "het geheugen", "de introspectie", "de afleiding"],
         antwoord=0,
         uitleg="Je hebt het niet zelf meegemaakt: je weet het doordat iemand het je vertelde. Dat "
                "is de bron die de fiche verhalen noemt, en ze is zo sterk als haar verteller."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over de bronnen van kennis kloppen?",
         opties=["één overtuiging kan op verschillende bronnen tegelijk steunen",
                 "geen enkele bron geeft op zich een waarborg dat je het juist hebt",
                 "een verhaal is altijd minder betrouwbaar dan een zintuiglijke waarneming",
                 "introspectie geeft als enige bron altijd zekerheid"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Bronnen werken samen, en elk van de vijf kan je bedriegen: ook je "
                "geheugen, ook je ogen, ook je blik naar binnen."),
    dict(type="meerkeuze",
         vraag="Wat zien de gevangenen in de grotallegorie van Plato?",
         opties=["schaduwen op de wand van de grot",
                 "de voorwerpen zelf, vlak voor hun ogen",
                 "het daglicht buiten de grot, in de verte",
                 "elkaar, en verder helemaal niets"],
         antwoord=0,
         uitleg="Ze zitten vastgebonden met hun gezicht naar de wand en zien enkel de schaduwen "
                "van wat er achter hen voorbijgedragen wordt."),
    dict(type="meerkeuze",
         vraag="Waarvoor staan de schaduwen in de grotallegorie?",
         opties=["voor wat onze zintuigen ons tonen: een afbeeldsel, niet de zaak zelf",
                 "voor de waarheid die iedereen vanzelf al kent",
                 "voor de verhalen die mensen elkaar vertellen over vroeger",
                 "voor de gevoelens die ons denken in de weg zitten"],
         antwoord=0,
         uitleg="De schaduw lijkt op het ding maar is het ding niet. Zo staat de waarneming "
                "tegenover de werkelijkheid zelf."),
    dict(type="meerkeuze",
         vraag="Wat gebeurt er in de allegorie met de gevangene die naar buiten gaat?",
         opties=["hij wordt verblind door het licht en moet aan het kijken wennen",
                 "hij ziet meteen alles helder en begrijpt alles in één keer",
                 "hij merkt dat er buiten de grot niets te zien valt",
                 "hij blijft liever buiten en keert nooit naar de grot terug"],
         antwoord=0,
         uitleg="Het licht doet eerst pijn. Plato laat daarmee zien dat inzicht niet vanzelf komt "
                "en in het begin onaangenaam is."),
    dict(type="meerkeuze",
         vraag="Wat is volgens de grotallegorie het verschil tussen waarneming en kennis?",
         opties=["waarneming geeft hoe iets lijkt, kennis geeft hoe het werkelijk is",
                 "waarneming is wat je zelf ziet, kennis is wat anderen je vertellen",
                 "waarneming is zeker, kennis blijft altijd een vermoeden",
                 "waarneming is van nu, kennis gaat alleen over vroeger"],
         antwoord=0,
         uitleg="Waarnemen is de schaduw zien. Kennis is begrijpen wat de schaduw werpt, en "
                "daarvoor heb je je verstand nodig."),
    dict(type="meerkeuze",
         vraag="Een stok in het water lijkt geknikt en is het niet. Wat toont dat volgens Plato?",
         opties=["dat de zintuigen ons kunnen bedriegen en het verstand moet nakijken",
                 "dat de zintuigen altijd de werkelijkheid juist weergeven",
                 "dat water geen deel uitmaakt van de werkelijke wereld",
                 "dat kennis onmogelijk is en we dus niets kunnen weten"],
         antwoord=0,
         uitleg="Precies het punt van de grot: wat je ziet, is niet zomaar hoe het is. Plato "
                "besluit daaruit niet dat kennis onmogelijk is, wel dat je er je verstand bij "
                "nodig hebt."),
    dict(type="meerkeuze",
         vraag="Waarom gelooft de teruggekeerde gevangene in de allegorie niemand?",
         opties=["de anderen kennen alleen de schaduwen en houden die voor de werkelijkheid",
                 "de anderen hebben hem nooit gekend en vertrouwen hem daarom niet",
                 "hij kan niet meer praten na zijn verblijf in het daglicht",
                 "hij wil zelf niet vertellen wat hij buiten gezien heeft"],
         antwoord=0,
         uitleg="Wie nooit iets anders zag dan schaduwen, vindt een verhaal over de zon "
                "ongeloofwaardig. Dat is het ongemakkelijke slot van de allegorie."),
    dict(type="waarofniet",
         vraag="De zintuigen zijn volgens de fiche één van de vijf bronnen van kennis.",
         antwoord=True,
         uitleg="Waar. De vijf zijn: afleiding, geheugen, introspectie, verhalen en zintuigen."),
    dict(type="waarofniet",
         vraag="Introspectie betekent dat je kennis haalt uit wat anderen je vertellen.",
         antwoord=False,
         uitleg="Niet waar. Introspectie is naar binnen kijken, bij jezelf. Wat anderen je "
                "vertellen, is de bron die de fiche verhalen noemt."),
    dict(type="waarofniet",
         vraag="In de grotallegorie staan de schaduwen voor de werkelijkheid zoals ze echt is.",
         antwoord=False,
         uitleg="Niet waar. De schaduwen staan voor wat onze zintuigen ons tonen: een afbeeldsel "
                "van de werkelijkheid, niet de werkelijkheid zelf."),
    dict(type="waarofniet",
         vraag="Plato besluit uit de grotallegorie dat je je verstand nodig hebt om van waarneming "
               "naar kennis te komen.",
         antwoord=True,
         uitleg="Waar. De waarneming geeft de schijn; het verstand brengt je bij het inzicht."),
    dict(type="invultekst",
         vraag="Hoe heet de bron van kennis waarbij je naar je eigen gedachten en gevoelens kijkt?",
         antwoord=["introspectie", "de introspectie"],
         uitleg="Introspectie betekent letterlijk naar binnen kijken."),
    dict(type="invultekst",
         vraag="Hoe heet de bron van kennis waarbij je uit iets wat je al weet iets nieuws "
               "besluit?",
         antwoord=["afleiding", "de afleiding"],
         uitleg="De straat is nat, dus het heeft geregend: dat is afleiding."),
    dict(type="invultekst",
         vraag="Welke allegorie van Plato gaat over gevangenen die naar schaduwen kijken? De ...",
         antwoord=["grotallegorie"],
         uitleg="De grotallegorie laat het verschil zien tussen waarneming en kennis."),
    dict(type="invultekst",
         vraag="Wat geeft volgens Plato enkel de schijn van de dingen: de waarneming of de kennis?",
         antwoord=["de waarneming", "waarneming"],
         uitleg="De waarneming geeft hoe iets lijkt; kennis geeft hoe het werkelijk is."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Waar komt kennis volgens het rationalisme vandaan?",
         opties=["uit de rede, uit het denken zelf",
                 "uit de ervaring en de zintuigen van de mens",
                 "uit de verhalen die een samenleving doorgeeft",
                 "uit de metingen die een onderzoeker verzamelt"],
         antwoord=0,
         uitleg="Ratio betekent rede. Voor een rationalist is het denken de betrouwbaarste weg "
                "naar kennis."),
    dict(type="meerkeuze",
         vraag="Waar komt kennis volgens het empirisme vandaan?",
         opties=["uit de ervaring, uit wat je waarneemt",
                 "uit de rede, die geen ervaring nodig heeft",
                 "uit de wiskunde, die altijd zeker is",
                 "uit de overlevering van vroegere generaties"],
         antwoord=0,
         uitleg="Empirie betekent ervaring. Voor een empirist begint alle kennis bij de "
                "waarneming."),
    dict(type="meerkeuze",
         vraag="Welke filosoof koppelt de fiche aan het rationalisme?",
         opties=["René Descartes", "John Locke", "David Hume", "Francis Bacon"],
         antwoord=0,
         uitleg="De fiche zet Descartes bij het rationalisme, en Locke en Hume bij het empirisme."),
    dict(type="meerkeuze",
         vraag="Welke filosofen koppelt de fiche aan het empirisme?",
         opties=["John Locke", "David Hume", "René Descartes", "Plato"],
         antwoord=[0, 1],
         uitleg="Locke en Hume staan in de fiche bij het empirisme en bij de inductieve aanpak."),
    dict(type="meerkeuze",
         vraag="Wat is de methodische twijfel van Descartes?",
         opties=["alles wat ook maar enigszins te betwijfelen valt voorlopig verwerpen",
                 "nooit iets geloven van wat een ander je vertelt over de wereld",
                 "aan alles twijfelen en daar ook nooit meer uit geraken",
                 "pas twijfelen als iemand je een tegenargument heeft gegeven"],
         antwoord=0,
         uitleg="Het is een methode, geen levenshouding: hij twijfelt met opzet aan alles, om te "
                "zien wat er overblijft dat niet te betwijfelen valt."),
    dict(type="meerkeuze",
         vraag="Wat blijft er bij Descartes na de methodische twijfel overeind?",
         opties=["dat hij denkt, en dus bestaat",
                 "dat zijn lichaam bestaat, want dat voelt hij",
                 "dat de wereld buiten hem bestaat zoals hij ze ziet",
                 "dat zijn herinneringen allemaal juist zijn"],
         antwoord=0,
         uitleg="Ik kan aan alles twijfelen, maar niet aan het feit dat ik twijfel, en wie twijfelt "
                "denkt. Ik denk, dus ik ben."),
    dict(type="meerkeuze",
         vraag="Wat is een deductieve aanpak?",
         opties=["van een algemene regel naar een besluit over een afzonderlijk geval",
                 "van losse waarnemingen naar een algemene regel",
                 "van een vermoeden naar een experiment dat het bevestigt",
                 "van een verhaal naar de les die eruit te trekken valt"],
         antwoord=0,
         uitleg="Deductie gaat van algemeen naar bijzonder. Alle mensen zijn sterfelijk, Socrates "
                "is een mens, dus Socrates is sterfelijk."),
    dict(type="meerkeuze",
         vraag="Wat is een inductieve aanpak?",
         opties=["van losse waarnemingen naar een algemene regel",
                 "van een algemene regel naar een afzonderlijk geval",
                 "van een besluit terug naar de veronderstelling erachter",
                 "van een begrip naar de definitie ervan in een woordenboek"],
         antwoord=0,
         uitleg="Inductie gaat van bijzonder naar algemeen. Ik zag duizend witte zwanen, dus alle "
                "zwanen zijn wit."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over deductie en inductie kloppen?",
         opties=["een geldige deductie met ware premissen geeft een zeker besluit",
                 "een inductie blijft altijd een besluit dat door nieuwe waarnemingen kan sneuvelen",
                 "inductie geeft meer zekerheid dan deductie, omdat ze op feiten steunt",
                 "deductie levert als enige nieuwe kennis over de wereld op"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Deductie is zeker maar leert niets nieuws over de wereld; "
                "inductie leert wel iets nieuws maar nooit met zekerheid."),
    dict(type="meerkeuze",
         vraag="Een onderzoeker bekijkt duizend gevallen en besluit daaruit een regel. Welke "
               "stroming en welke aanpak herken je?",
         opties=["het empirisme, met een inductieve aanpak",
                 "het rationalisme, met een deductieve aanpak",
                 "het empirisme, met een deductieve aanpak",
                 "het rationalisme, met een inductieve aanpak"],
         antwoord=0,
         uitleg="Hij vertrekt van ervaring (empirisme) en gaat van de gevallen naar de regel "
                "(inductie)."),
    dict(type="meerkeuze",
         vraag="Iemand zet zich aan tafel, verwerpt alles waaraan te twijfelen valt en bouwt van "
               "daaruit stap voor stap verder. Welke stroming herken je?",
         opties=["het rationalisme", "het empirisme", "de mythologie", "de natuurfilosofie"],
         antwoord=0,
         uitleg="Hij gebruikt geen ervaring maar enkel zijn denken, en werkt van een zeker "
                "beginpunt naar besluiten toe. Dat is het rationalisme van Descartes."),
    dict(type="meerkeuze",
         vraag="Wat is de B van de AUB-methode?",
         opties=["bijvoorbeeld: een voorbeeld dat je argument duidelijk maakt",
                 "bewijs: het onderzoek waarop je argument steunt",
                 "besluit: de zin waarmee je je betoog afsluit",
                 "bezwaar: het tegenargument dat je eerst weerlegt"],
         antwoord=0,
         uitleg="AUB staat voor Argument, Uitleg en Bijvoorbeeld. Eerst noem je je argument, dan "
                "leg je het uit, dan maak je het met een voorbeeld duidelijk."),
    dict(type="waarofniet",
         vraag="Descartes hoort volgens de fiche bij het rationalisme en de deductieve aanpak.",
         antwoord=True,
         uitleg="Waar. De fiche zet de methodische twijfel en de deductieve aanpak bij hem."),
    dict(type="waarofniet",
         vraag="De methodische twijfel van Descartes is bedoeld om nooit meer iets zeker te weten.",
         antwoord=False,
         uitleg="Niet waar. Het omgekeerde: hij twijfelt met opzet aan alles om te vinden wat niet "
                "te betwijfelen valt, en daarop bouwt hij verder."),
    dict(type="waarofniet",
         vraag="Inductie gaat van losse waarnemingen naar een algemene regel.",
         antwoord=True,
         uitleg="Waar. Deductie gaat de andere kant op: van een algemene regel naar een "
                "afzonderlijk geval."),
    dict(type="waarofniet",
         vraag="Volgens het empirisme kan je kennis opbouwen zonder ooit iets waar te nemen.",
         antwoord=False,
         uitleg="Niet waar. Voor een empirist begint alle kennis bij de ervaring. Dat kennis "
                "zonder ervaring kan, is juist de stelling van het rationalisme."),
    dict(type="invultekst",
         vraag="Welke stroming laat alle kennis bij de ervaring beginnen?",
         antwoord=["het empirisme", "empirisme"],
         uitleg="Empirie betekent ervaring. Locke en Hume horen erbij."),
    dict(type="invultekst",
         vraag="Welke stroming laat kennis uit de rede zelf komen?",
         antwoord=["het rationalisme", "rationalisme"],
         uitleg="Ratio betekent rede. Descartes hoort erbij."),
    dict(type="invultekst",
         vraag="Hoe heet de redenering van een algemene regel naar een afzonderlijk geval?",
         antwoord=["deductie", "een deductie"],
         uitleg="Deductie gaat van algemeen naar bijzonder; inductie de andere kant op."),
    dict(type="invultekst",
         vraag="Waar staan de drie letters van de AUB-methode voor? Argument, uitleg en ...",
         antwoord=["bijvoorbeeld"],
         uitleg="Eerst het argument, dan de uitleg, dan een voorbeeld."),
]
