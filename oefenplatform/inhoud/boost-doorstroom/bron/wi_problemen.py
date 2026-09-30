# -*- coding: utf-8 -*-
"""De vragen voor "Een opgave aanpakken: van context naar wiskunde".

Uit de bouwsteen Probleemoplossend denken van de vakfiche: mathematiseren en
demathematiseren, de vier stappen (begrijp het probleem, maak een plan, voer
het plan uit, reflecteer), de heuristieken die de fiche opsomt, en het verschil
tussen een vraagstuk, een probleem en een meetkundig probleem.

Deel 1 is de aanpak zelf: de begrippen en de stappen. Deel 2 laat je kiezen
welke heuristiek bij welke opgave past, en oefent schatten en controleren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent mathematiseren?",
        opties=[
            "een situatie uit de wereld omzetten in wiskundetaal en symbolen",
            "een berekening laten nakijken door een rekenapp op je telefoon",
            "een wiskundige uitkomst terugvertalen naar de situatie waarover het ging",
            "een oefening zo lang herhalen tot je ze vanbuiten kent",
        ],
        antwoord=0,
        uitleg="Mathematiseren is de heenweg: van de situatie naar de formule. De terugweg heet demathematiseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je berekent dat een ladder 4,7 meter lang moet zijn, en je antwoordt dat een ladder van 5 meter volstaat. Wat doe je in die laatste stap?",
        opties=[
            "demathematiseren: je vertaalt de uitkomst terug naar de situatie",
            "mathematiseren: je zet de situatie om in een berekening",
            "afronden: je vervangt het antwoord door een gemakkelijker getal",
            "schatten: je gokt een waarde die ongeveer klopt",
        ],
        antwoord=0,
        uitleg="Een ladder van 4,7 meter bestaat niet in de winkel. Je uitkomst betekent pas iets als je ze terugvertaalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is volgens de vakfiche het verschil tussen een vraagstuk en een probleem?",
        opties=[
            "een vraagstuk los je op met de leerstof van één hoofdstuk, bij een probleem combineer je hoofdstukken",
            "een vraagstuk staat altijd in gewone woorden, terwijl een probleem altijd in symbolen staat",
            "een vraagstuk heeft één antwoord, een probleem heeft er meerdere",
            "een vraagstuk komt op het examen, een probleem enkel in de les",
        ],
        antwoord=0,
        uitleg="De fiche zegt het zo: een probleem laat zich niet aan één hoofdstuk koppelen, je combineert leerinhouden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier stappen noemt de fiche om een opgave procedureel op te lossen?",
        opties=[
            "begrijp het probleem, maak een plan, voer het plan uit, reflecteer",
            "lees de opgave, reken, noteer en controleer met je rekenmachine",
            "schat, reken, rond af, schrijf op",
            "teken, meet, bereken, vergelijk",
        ],
        antwoord=0,
        uitleg="Die volgorde komt van Pólya. De laatste stap, reflecteren, wordt het vaakst overgeslagen en levert het meeste op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een meetkundig probleem volgens de vakfiche?",
        opties=[
            "de verzamelnaam voor vraagstukken en problemen waarvoor je meetkundige vaardigheden nodig hebt",
            "elke opgave waarin een tekening staat, ook als je daar niet voor hoeft te meten of te construeren",
            "een opgave die je enkel met passer en geodriehoek mag oplossen",
            "een opgave over ruimtefiguren, nooit over vlakke figuren",
        ],
        antwoord=0,
        uitleg="Het gaat om de vaardigheden die je nodig hebt, niet om de vorm van de opgave.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met een opgave 'zonder context'?",
        opties=[
            "een opgave die abstract en zuiver wiskundig is",
            "een opgave waarbij de gegevens ontbreken",
            "een opgave zonder tekening erbij",
            "een opgave waarvan het antwoord niet vastligt",
        ],
        antwoord=0,
        uitleg="Met context vertrekt van een situatie uit de wereld, zonder context is zuivere wiskunde. Allebei komen ze op het examen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze aanpakken is géén heuristiek uit de lijst van de fiche?",
        opties=[
            "het antwoord opzoeken in de oplossingen achteraan",
            "gegevens schematisch voorstellen en netjes ordenen",
            "terugrekenen, van achter naar voor werken",
            "opsplitsen in deelproblemen",
        ],
        antwoord=0,
        uitleg="Een heuristiek is een manier om zélf verder te geraken. Het antwoord opzoeken brengt je geen stap vooruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt hoeveel verschillende broodjes je kan samenstellen en je schrijft eerst alle mogelijkheden onder elkaar. Welke heuristiek gebruik je?",
        opties=[
            "alle mogelijkheden opschrijven",
            "variabelen invoeren",
            "gebruik maken van symmetrie",
            "van achter naar voor werken",
        ],
        antwoord=0,
        uitleg="Bij kleine aantallen is uitschrijven sneller dan een formule zoeken, en je ziet meteen of je iets vergeet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opgave vraagt de leeftijd van twee zussen, en je noemt de leeftijd van de jongste x. Welke heuristiek is dat?",
        opties=[
            "variabelen invoeren",
            "een tekening maken",
            "schatten en testen",
            "simuleren van de situatie",
        ],
        antwoord=0,
        uitleg="Zodra je een letter geeft aan wat je niet weet, kan je de rest van de gegevens ermee opschrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort reflecteren bij het oplossen en niet erna?",
        opties=[
            "omdat je zo merkt of je uitkomst kan kloppen en of je aanpak elders bruikbaar is",
            "omdat je anders punten verliest voor de netheid van je uitwerking en je notatie",
            "omdat de fiche het in die volgorde opsomt",
            "omdat je pas na het reflecteren mag afronden",
        ],
        antwoord=0,
        uitleg="Een uitkomst van 340 kilometer per uur voor een fietser wijst op een rekenfout. Reflecteren vangt dat op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vaardigheid noemt de fiche bij ICT-vaardigheid?",
        opties=[
            "rekenapps gebruiken en constructies maken in GeoGebra",
            "een verslag typen in een tekstverwerker",
            "je oplossing opzoeken op een website",
            "een grafiek fotograferen met je telefoon en bijhouden",
        ],
        antwoord=0,
        uitleg="ICT is hulp bij het rekenen en het tekenen, geen vervanging van de redenering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opgave geeft een tekening met een ladder tegen een muur. Wat doe je eerst?",
        opties=[
            "nagaan wat gegeven is en wat gevraagd wordt",
            "meteen Pythagoras toepassen",
            "de tekening zorgvuldig natekenen op schaal",
            "je rekenmachine op graden zetten",
        ],
        antwoord=0,
        uitleg="Begrijp het probleem komt voor maak een plan. Wie te snel rekent, rekent vaak het verkeerde uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze vaardigheden rekent de fiche onder meet- en tekenvaardigheid?",
        opties=[
            "hoeken meten met een geodriehoek en tekenen met passer en geodriehoek",
            "handig hoofdrekenen met grote getallen",
            "een grafiek aflezen en beschrijven",
            "een vraagstuk in je eigen woorden navertellen aan iemand die het niet kent",
        ],
        antwoord=0,
        uitleg="De fiche noemt vier vaardigheden: taal, rekenen, meten en tekenen, en ICT.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een opgave met context mag je zelf kiezen welke oplossingsstrategie je gebruikt.",
        antwoord=True,
        uitleg="De fiche zegt uitdrukkelijk dat je zelf de strategie kiest aan de hand van je kennis en vaardigheden.",
    ),
    dict(
        type="waarofniet",
        vraag="Demathematiseren betekent dat je de opgave vereenvoudigt tot je ze aankan.",
        antwoord=False,
        uitleg="Demathematiseren is je wiskundige uitkomst terugvertalen naar de situatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schets maken telt als een volwaardige oplossingsstrategie.",
        antwoord=True,
        uitleg="De fiche noemt een schets, tekening of tabel als eerste heuristiek in de lijst.",
    ),
    dict(
        type="waarofniet",
        vraag="Op het examen komen enkel opgaven met context voor.",
        antwoord=False,
        uitleg="Je bereidt je voor op allebei: met context en zuiver wiskundig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het omzetten van een situatie uit de wereld naar wiskundetaal?",
        antwoord=["mathematiseren", "het mathematiseren"],
        uitleg="De heenweg is mathematiseren, de terugweg demathematiseren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de tweede van de vier stappen, na 'begrijp het probleem'?",
        antwoord=["maak een plan", "een plan maken", "plan maken"],
        uitleg="Pas daarna voer je het plan uit, en helemaal op het einde reflecteer je.",
    ),
    dict(
        type="invultekst",
        vraag="Een opgave die je niet aan één hoofdstuk kan koppelen, noemt de fiche een ...",
        antwoord=["probleem", "een probleem"],
        uitleg="Bij een probleem combineer je leerinhouden uit verschillende hoofdstukken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je moet weten hoeveel liter verf je nodig hebt voor een muur van 4,2 m op 2,6 m. Welke eerste stap past het best?",
        opties=[
            "de oppervlakte berekenen en pas daarna naar het verbruik per liter kijken",
            "meteen delen door het aantal liters in de bus",
            "de omtrek van de muur berekenen",
            "de afmetingen eerst afronden naar hele meters en daarmee verder rekenen",
        ],
        antwoord=0,
        uitleg="Verf wordt per vierkante meter gerekend. Wie eerst de oppervlakte neemt, heeft daarna maar één deling nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een som geeft als uitkomst dat een vijver 0,004 kubieke meter water bevat. Wat doe je bij het reflecteren?",
        opties=[
            "nagaan of je de eenheden niet door elkaar haalde, want dat zijn maar vier liter",
            "het antwoord afronden naar nul",
            "de uitkomst overnemen, want de berekening is af",
            "de vraag opnieuw lezen en daarna precies hetzelfde antwoord noteren als eerst",
        ],
        antwoord=0,
        uitleg="Vier liter is geen vijver. Een onmogelijke uitkomst wijst bijna altijd op een eenheid die misging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke heuristiek gebruik je als je een vierkant patroon halveert omdat de linkerhelft hetzelfde is als de rechter?",
        opties=[
            "gebruik maken van symmetrie",
            "alle mogelijkheden opschrijven",
            "van achter naar voor werken",
            "voorbeelden geven",
        ],
        antwoord=0,
        uitleg="Symmetrie halveert je werk en halveert dus ook de kans op een rekenfout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opgave zegt: na een korting van 20 procent betaal je 48 euro. Hoe pak je dat het handigst aan?",
        opties=[
            "terugrekenen: 48 euro is 80 procent van de oude prijs",
            "20 procent van 48 euro bijtellen",
            "48 euro delen door 20",
            "48 euro vermenigvuldigen met 1,20 en dat afronden",
        ],
        antwoord=0,
        uitleg="De oude prijs is 48 gedeeld door 0,8, dus 60 euro. Wie 20 procent bijtelt, komt op 57,60 en zit fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is schatten nuttig vóór je precies rekent?",
        opties=[
            "omdat je dan meteen ziet of je uitkomst in de juiste grootteorde ligt",
            "omdat een schatting altijd sneller gaat dan een volledige berekening",
            "omdat je dan geen rekenmachine meer nodig hebt",
            "omdat een schatting op het examen als antwoord telt",
        ],
        antwoord=0,
        uitleg="Wie 19 keer 21 schat op ongeveer 400, ziet meteen dat 3999 niet kan kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdeelt de vraag 'hoeveel kost een weekje kamperen' in reis, kampeerplaats en eten. Welke heuristiek is dat?",
        opties=[
            "opsplitsen in deelproblemen",
            "variabelen invoeren",
            "patronen ontdekken",
            "simuleren",
        ],
        antwoord=0,
        uitleg="Drie kleine vragen die je kan beantwoorden, zijn beter dan één grote die je niet aankan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opgave vraagt de hoogte van een toren uit de kijkhoek en de afstand. Welk plan past?",
        opties=[
            "een rechthoekige driehoek tekenen en met de tangens werken",
            "de omtrek van de toren schatten",
            "de stelling van Pythagoras toepassen op de twee gegeven hoeken",
            "de gegevens optellen en delen door twee",
        ],
        antwoord=0,
        uitleg="Overstaande en aanliggende rechthoekszijde samen: dat is precies de tangens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent taalvaardigheid in de lijst van de fiche?",
        opties=[
            "wiskundige uitdrukkingen, tekeningen, grafieken en diagrammen begrijpen",
            "een opgave vlot kunnen voorlezen",
            "een verslag schrijven over je oplossing",
            "vaktaal vermijden zodat iedereen je snapt",
        ],
        antwoord=0,
        uitleg="Veel fouten zijn leesfouten: de opgave vroeg iets anders dan wat er uitgerekend werd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je probeert een getal, ziet dat het te groot uitvalt en probeert een kleiner. Hoe noemt de fiche dat?",
        opties=[
            "schatten, slim gissen, testen en controleren",
            "het vraagstuk simuleren",
            "gegevens ordenen",
            "logisch redeneren",
        ],
        antwoord=0,
        uitleg="Slim gissen is geen gokken: elke poging vertelt je in welke richting de volgende moet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opgave geeft een rij 2, 6, 12, 20, 30. Welke aanpak ligt voor de hand?",
        opties=[
            "patronen en regelmaat ontdekken door de verschillen te bekijken",
            "alle mogelijkheden opschrijven",
            "een vergelijking van de tweede graad oplossen",
            "de getallen ordenen van groot naar klein",
        ],
        antwoord=0,
        uitleg="De verschillen zijn 4, 6, 8, 10. Het volgende verschil is dus 12 en het volgende getal 42.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitkomst is een teken dat er iets misging bij een oppervlakte in vierkante meter?",
        opties=[
            "een negatief getal",
            "een getal met twee cijfers na de komma",
            "een getal groter dan honderd",
            "een geheel getal",
        ],
        antwoord=0,
        uitleg="Een oppervlakte kan niet negatief zijn. Zo'n uitkomst stuurt je terug naar je berekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche dat je je tussenstappen verantwoordt?",
        opties=[
            "omdat een lezer dan kan volgen welke eigenschap je toepast en waar het misloopt",
            "omdat een langere oplossing meer punten oplevert",
            "omdat je anders je rekenmachine niet mag gebruiken",
            "omdat het examen alleen open vragen bevat",
        ],
        antwoord=0,
        uitleg="Een antwoord zonder redenering is niet na te kijken, en jijzelf vindt er je eigen fout niet in terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser legt 24 kilometer af in anderhalf uur. Je berekent 36 kilometer per uur. Wat doe je?",
        opties=[
            "opnieuw rekenen, want delen door 1,5 geeft 16",
            "het antwoord aanvaarden, want 36 is een normale snelheid",
            "de eenheid veranderen naar meter per seconde",
            "de afstand verdubbelen",
        ],
        antwoord=0,
        uitleg="24 gedeeld door 1,5 is 16. Wie vermenigvuldigt in plaats van deelt, krijgt een uitkomst die te groot is.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag bij een probleem gegevens uit meerdere hoofdstukken van de fiche combineren.",
        antwoord=True,
        uitleg="Dat is net wat een probleem onderscheidt van een vraagstuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een goede schatting maakt, hoeft de exacte berekening niet meer uit te voeren.",
        antwoord=False,
        uitleg="Een schatting is een controle vooraf of achteraf, geen antwoord.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tegenvoorbeeld volstaat om aan te tonen dat een wiskundige uitspraak vals is.",
        antwoord=True,
        uitleg="Eén geval waarin het niet opgaat, breekt de uitspraak. Voorbeelden bewijzen daarentegen nooit dat ze waar is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een paar voorbeelden die kloppen, bewijzen dat een eigenschap altijd geldt.",
        antwoord=False,
        uitleg="Voorbeelden illustreren, ze bewijzen niet. Daarvoor heb je een redenering nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is 24 kilometer in anderhalf uur, in kilometer per uur?",
        antwoord=["16", "16 km/u", "16 kilometer"],
        uitleg="24 gedeeld door 1,5 is 16.",
    ),
    dict(
        type="invultekst",
        vraag="Welk getal volgt in de rij 2, 6, 12, 20, 30?",
        antwoord=["42"],
        uitleg="De verschillen lopen op met telkens 2: 4, 6, 8, 10, 12. Dus 30 plus 12.",
    ),
    dict(
        type="invultekst",
        vraag="Na 20 procent korting betaal je 48 euro. Wat was de prijs in euro?",
        antwoord=["60", "60 euro"],
        uitleg="48 is 80 procent, dus de volle prijs is 48 gedeeld door 0,8.",
    ),
]
