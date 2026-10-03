# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Warmte en faseovergangen.

Fysica, de koppen "Temperatuur en warmte", "Merkbare warmte" en "Latente
warmte" van de vakfiche natuurwetenschappen 2de graad doorstroom. Deel 1
gaat over warmtetransport, het thermisch evenwicht en de merkbare warmte met
de specifieke warmtecapaciteit; deel 2 over de faseovergangen en de latente
warmte.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als je twee voorwerpen met een verschillende temperatuur tegen elkaar legt?",
        opties=[
            "er gaat warmte van het warme naar het koude voorwerp",
            "er gaat warmte van het koude naar het warme voorwerp",
            "beide voorwerpen houden precies hun eigen temperatuur",
            "het koude voorwerp geeft koude af aan het warme voorwerp",
        ],
        antwoord=0,
        uitleg="Warmte stroomt altijd van warm naar koud. Koude is geen stof die zich verplaatst, het is enkel een gebrek aan warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is thermisch evenwicht?",
        opties=[
            "de toestand waarin beide voorwerpen dezelfde temperatuur hebben",
            "de toestand waarin beide voorwerpen dezelfde massa hebben gekregen",
            "de toestand waarin de warmte zich in één voorwerp verzameld heeft",
            "de toestand waarin beide voorwerpen hun warmte volledig kwijt zijn",
        ],
        antwoord=0,
        uitleg="Zodra de temperaturen gelijk zijn, stopt de netto overdracht. Dat is het eindpunt van elke warmtestroom.",
    ),
    dict(
        type="waarofniet",
        vraag="Temperatuur hangt samen met de kinetische energie van de deeltjes in een stof.",
        antwoord=True,
        uitleg="Hoe sneller de deeltjes bewegen, hoe hoger de temperatuur. Bij het absolute nulpunt zou die beweging stilvallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van warmtetransport zijn er? Kruis alles aan wat juist is.",
        opties=["geleiding", "convectie", "straling", "verdamping"],
        antwoord=[0, 1, 2],
        uitleg="Verdampen is een faseovergang, geen transportvorm. Bij geleiding en convectie is er stof nodig, bij straling niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het warmtetransport dat ook door het luchtledige gaat?",
        antwoord="straling",
        uitleg="De warmte van de zon bereikt ons zo, door de ruimte. Geleiding en convectie hebben wel een stof nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe gaat warmte door een metalen staaf?",
        opties=[
            "door geleiding, de deeltjes geven hun beweging aan hun buren door",
            "door convectie, de deeltjes van het metaal gaan samen stromen",
            "door straling, het metaal zendt de warmte als golven door zich heen",
            "door verdamping, de deeltjes aan het uiteinde laten los van het metaal",
        ],
        antwoord=0,
        uitleg="De deeltjes blijven op hun plaats en stoten hun buren aan. In een metaal helpen de vrije elektronen daar nog bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij convectie verplaatst de stof zelf zich en neemt ze de warmte mee.",
        antwoord=True,
        uitleg="Warme lucht of warm water stijgt en koud zakt. Zo komt de warmte van een radiator in de hele kamer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de merkbare warmte van een stof?",
        opties=[
            "de specifieke warmtecapaciteit maal de massa maal het temperatuurverschil",
            "de specifieke warmtecapaciteit maal de massa, gedeeld door de temperatuur",
            "de massa maal het temperatuurverschil, gedeeld door de warmtecapaciteit",
            "de specifieke warmtecapaciteit maal het kwadraat van het temperatuurverschil",
        ],
        antwoord=0,
        uitleg="Hoe meer massa en hoe meer graden verschil, hoe meer warmte je nodig hebt. De specifieke warmtecapaciteit hangt af van de stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een grote specifieke warmtecapaciteit?",
        opties=[
            "je hebt veel warmte nodig om één kilogram één graad op te warmen",
            "je hebt weinig warmte nodig om één kilogram één graad op te warmen",
            "de stof heeft een hoger smeltpunt dan de meeste andere stoffen",
            "de stof geleidt de warmte veel sneller dan de meeste andere stoffen",
        ],
        antwoord=0,
        uitleg="Water heeft een heel grote warmtecapaciteit. Daarom warmt de zee veel langer op dan het zand op het strand.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk toestel meet je in het labo hoeveel warmte een stof opneemt of afgeeft?",
        antwoord="calorimeter",
        uitleg="Een joulevat is daar een ander woord voor. Het is zo goed geïsoleerd dat de warmte er niet uit ontsnapt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft de zee in september nog warm terwijl de lucht al afkoelt?",
        opties=[
            "water heeft een veel grotere warmtecapaciteit dan lucht",
            "water geleidt de warmte veel sneller dan lucht dat doet",
            "water neemt in de zomer veel meer straling op dan lucht",
            "water heeft een veel hoger kookpunt dan de lucht erboven",
        ],
        antwoord=0,
        uitleg="Water moet veel energie kwijt voor het één graad afkoelt. Daarom loopt de zee een paar weken achter op de lucht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een halve liter water vraagt even veel warmte als een hele liter om er tien graden bij te krijgen.",
        antwoord=False,
        uitleg="De benodigde warmte is recht evenredig met de massa. Dubbel de massa betekent dus dubbel de warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom voelt een tegelvloer kouder aan dan een tapijt bij dezelfde temperatuur?",
        opties=[
            "de tegel geleidt de warmte van je voet veel sneller weg",
            "de tegel heeft werkelijk een lagere temperatuur dan het tapijt",
            "de tegel geeft koude af aan je voet en het tapijt niet",
            "het tapijt geeft warmte af die het eerder heeft opgeslagen",
        ],
        antwoord=0,
        uitleg="Je voelt niet de temperatuur maar hoe snel je warmte verliest. Een tegel is een goede geleider, een tapijt een isolator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verwarmt 2 kilogram water van 20 naar 30 graden. De specifieke warmtecapaciteit is 4180 joule per kilogram per graad. Hoeveel warmte is dat?",
        opties=["83 600 joule", "8 360 joule", "41 800 joule", "167 200 joule"],
        antwoord=0,
        uitleg="Je rekent 4180 maal 2 maal 10. Dat is bijna 84 kilojoule voor tien graden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een kleine specifieke warmtecapaciteit koelt heel langzaam af.",
        antwoord=False,
        uitleg="Een kleine warmtecapaciteit betekent dat de temperatuur snel verandert. Zo'n stof warmt snel op en koelt ook snel weer af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt warme lucht in een kamer naar het plafond?",
        opties=[
            "de deeltjes gaan verder uit elkaar, dus wordt de lucht lichter per liter",
            "de deeltjes worden zelf zwaarder en duwen de koude lucht naar boven",
            "de warmte zelf stijgt altijd op, los van de lucht waarin ze zit",
            "het plafond trekt de warme lucht met zijn eigen temperatuur aan",
        ],
        antwoord=0,
        uitleg="Opwarmen doet een gas uitzetten, en daardoor zakt zijn massadichtheid. De koudere, dichtere lucht zakt eronder en zo ontstaat een stroming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over warmte en temperatuur zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "temperatuur meet je in graden Celsius of in kelvin",
            "warmte is energie en meet je in joule",
            "warmte gaat altijd van warm naar koud",
            "warmte en temperatuur zijn twee woorden voor hetzelfde",
        ],
        antwoord=[0, 1, 2],
        uitleg="Temperatuur zegt hoe warm iets is, warmte is de energie die overgaat. Een bad van 30 graden bevat veel meer warmte dan een kop thee van 60 graden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de warmte die je merkt aan een verandering van temperatuur?",
        antwoord="merkbare warmte",
        uitleg="Bij latente warmte verandert de temperatuur juist niet, maar de fase van de stof wel.",
    ),
    dict(
        type="waarofniet",
        vraag="De warmtebalans is een toepassing van de wet van behoud van energie.",
        antwoord=True,
        uitleg="Wat het ene voorwerp afgeeft, neemt het andere op. Daarom kan je de eindtemperatuur van een mengsel berekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je giet een liter water van 80 graden bij een liter water van 20 graden. Wat wordt de eindtemperatuur ongeveer?",
        opties=["50 graden", "80 graden", "100 graden", "30 graden"],
        antwoord=0,
        uitleg="Gelijke massa's van dezelfde stof geven het gemiddelde. Wat het warme water afgeeft, neemt het koude op.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de temperatuur van ijs van nul graden terwijl het smelt?",
        opties=[
            "ze blijft op nul graden tot al het ijs gesmolten is",
            "ze stijgt gelijkmatig terwijl het ijs aan het smelten is",
            "ze daalt eerst en stijgt daarna weer naar nul graden",
            "ze stijgt onmiddellijk naar de temperatuur van de kamer",
        ],
        antwoord=0,
        uitleg="Alle toegevoerde warmte gaat naar het losbreken van de deeltjes. Daarom blijft de temperatuur tijdens een faseovergang gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke faseovergangen geeft een stof warmte af? Kruis alles aan wat juist is.",
        opties=["stollen", "condenseren", "desublimeren", "smelten"],
        antwoord=[0, 1, 2],
        uitleg="Die drie gaan naar een toestand met sterkere cohesiekrachten, dus komt er energie vrij. Smelten vraagt juist warmte.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een faseovergang blijft de temperatuur van de stof gelijk.",
        antwoord=True,
        uitleg="De warmte gaat naar het verbreken of maken van de bindingen tussen de deeltjes. Daarom heet ze latente, dus verborgen, warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke faseovergangen zijn het? Kruis alles aan wat juist is.",
        opties=["sublimeren", "condenseren", "desublimeren", "geleiden"],
        antwoord=[0, 1, 2],
        uitleg="Sublimeren is van vast rechtstreeks naar gas, desublimeren het omgekeerde. Geleiden is een vorm van warmtetransport.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de overgang van vast rechtstreeks naar gas?",
        antwoord="sublimeren",
        uitleg="Droogijs doet dat bij kamertemperatuur. Rijm op een koude ochtend ontstaat door het omgekeerde, desublimeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de latente warmte bij een faseovergang?",
        opties=[
            "de specifieke faseovergangswarmte maal de massa",
            "de specifieke faseovergangswarmte maal het temperatuurverschil",
            "de massa maal het temperatuurverschil van de hele overgang",
            "de specifieke warmtecapaciteit maal de massa maal de tijd",
        ],
        antwoord=0,
        uitleg="Er staat geen temperatuurverschil in, want dat is tijdens een faseovergang nul. Alleen de massa en de stof bepalen de warmte.",
    ),
    dict(
        type="waarofniet",
        vraag="Je hebt meer warmte nodig om water bij honderd graden te laten verdampen dan om het van nul naar honderd graden op te warmen.",
        antwoord=True,
        uitleg="De verdampingswarmte van water is bijzonder groot. Daarom koelt zweten zo goed en duurt het zo lang voor een pot leeggekookt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom koel je af als je zweet?",
        opties=[
            "het verdampen van het zweet haalt warmte uit je huid",
            "het zweet zelf is koeler dan je huid en koelt die zo af",
            "het zweet sluit je huid af zodat er geen warmte meer bij komt",
            "het zweet geleidt de warmte van binnen naar buiten door je huid",
        ],
        antwoord=0,
        uitleg="Verdampen vraagt energie, en die komt uit je huid. In vochtige lucht verdampt het zweet moeilijker, en daarom voelt het dan zo zwaar aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn cohesiekrachten?",
        opties=[
            "de krachten waarmee de deeltjes van een stof elkaar vasthouden",
            "de krachten waarmee een stof aan een ander oppervlak blijft kleven",
            "de krachten waarmee de kern de elektronen van een atoom vasthoudt",
            "de krachten waarmee twee voorwerpen bij een botsing op elkaar duwen",
        ],
        antwoord=0,
        uitleg="Bij een faseovergang breek je die krachten of maak je ze juist. Hoe sterker ze zijn, hoe hoger het smelt- en kookpunt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de warmte die bij een faseovergang opgenomen wordt zonder dat de temperatuur stijgt?",
        antwoord="latente warmte",
        uitleg="Latent betekent verborgen. Je meet er niets van op de thermometer, maar de energie zit wel in de stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een smeltcurve van een zuivere stof heeft een vlak stuk. Wat gebeurt er in dat stuk?",
        opties=[
            "de stof smelt, en alle warmte gaat naar de faseovergang",
            "de stof warmt gewoon op, maar heel langzaam deze keer",
            "de stof koelt af omdat ze warmte aan de omgeving verliest",
            "er gebeurt niets, want er wordt geen warmte meer toegevoerd",
        ],
        antwoord=0,
        uitleg="Dat vlakke stuk zit precies op het smeltpunt. Pas als alles vloeibaar is, stijgt de temperatuur weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof neemt bij het stollen warmte op uit haar omgeving.",
        antwoord=False,
        uitleg="Stollen is het omgekeerde van smelten, dus komt die energie juist vrij. Daarom zetten fruitboeren bij nachtvorst water tussen de bomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft de temperatuur van kokend water op honderd graden staan, ook als je harder stookt?",
        opties=[
            "alle extra warmte gaat naar het verdampen van het water",
            "het water kan boven honderd graden geen warmte meer opnemen",
            "de thermometer kan boven honderd graden niets meer meten",
            "de damp koelt het water precies even snel weer terug af",
        ],
        antwoord=0,
        uitleg="Harder stoken maakt alleen dat het sneller leegkookt. De temperatuur blijft op het kookpunt tot al het water weg is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel warmte heb je nodig om 0,5 kilogram ijs te smelten, met 334 000 joule per kilogram?",
        opties=["167 000 joule", "334 000 joule", "668 000 joule", "83 500 joule"],
        antwoord=0,
        uitleg="Je vermenigvuldigt de specifieke smeltwarmte met de massa: 334 000 maal 0,5. Het temperatuurverschil speelt hier geen rol.",
    ),
    dict(
        type="waarofniet",
        vraag="Het smeltpunt en het stolpunt van een zuivere stof liggen bij een verschillende temperatuur.",
        antwoord=False,
        uitleg="Het is dezelfde temperatuur, enkel de richting van de overgang verschilt. Water smelt en stolt allebei bij nul graden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan je je lelijk verbranden aan stoom van honderd graden, erger dan aan water van honderd graden?",
        opties=[
            "de stoom geeft bij het condenseren op je huid ook nog latente warmte af",
            "de stoom is in werkelijkheid veel heter dan honderd graden",
            "de stoom geleidt de warmte veel sneller dan vloeibaar water",
            "de stoom blijft veel langer op je huid liggen dan vloeibaar water zou doen",
        ],
        antwoord=0,
        uitleg="Bij het condenseren komt de hele verdampingswarmte vrij, en die is enorm. Dat komt bovenop de warmte van het water zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de deeltjes als een vaste stof smelt?",
        opties=[
            "ze komen los uit hun vaste plaats maar blijven bij elkaar",
            "ze gaan veel sneller bewegen zonder van plaats te veranderen",
            "ze laten elkaar volledig los en vullen de hele ruimte op",
            "ze vallen uiteen in atomen die daarna apart verder bewegen",
        ],
        antwoord=0,
        uitleg="In een vloeistof kunnen de deeltjes langs elkaar schuiven. Pas bij verdampen laten ze elkaar echt los.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de overgang van gas naar vloeistof?",
        antwoord="condenseren",
        uitleg="Dat zie je gebeuren op een koud raam of op het deksel van een kookpot. Daarbij komt warmte vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="Om de eindtemperatuur van een mengsel te berekenen, stel je een warmtebalans op.",
        antwoord=True,
        uitleg="De warmte die het warme deel afgeeft, is de warmte die het koude deel opneemt. Zit er een faseovergang bij, dan reken je die er apart in mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt een ijsblokje in een glas water en het water koelt af. Waarom?",
        opties=[
            "het ijs neemt warmte uit het water op om te kunnen smelten",
            "het ijs geeft koude af aan het water om het heen",
            "het ijs duwt het warme water naar de bovenkant van het glas",
            "het ijs laat de warmte van het water door zich heen stralen",
        ],
        antwoord=0,
        uitleg="Koude bestaat niet als iets dat overgaat. Het smelten haalt latente warmte uit het water, en daardoor zakt de temperatuur.",
    ),
]
