# -*- coding: utf-8 -*-
"""Betrouwbaarheidsinterval, betrouwbaarheidsniveau en foutenmarge.

De fiche is hier uitzonderlijk duidelijk over wat ze niet vraagt: "De nadruk
ligt op de betekenis, het is niet nodig om zelf berekeningen te maken." Er
staan dus geen opgaven in dit thema waarin een kind zelf een interval moet
uitrekenen. Wat ze wél vraagt, drie keer, is interpreteren en een fout
aanduiden en verbeteren:

  "Je krijgt een betrouwbaarheidsinterval ... en beoordeelt stellingen"
  "Je interpreteert een betrouwbaarheidsinterval"
  "Je duidt de fout aan bij het verkeerd interpreteren ... en verbetert deze"

Daarom zijn de vragen hier bijna allemaal stellingen die je moet beoordelen,
en staat de lijst met vaak voorkomende interpretatiefouten die de fiche zelf
noemt volledig in deel 2.

Het verband dat de fiche expliciet vraagt: de breedte van het interval hangt
af van de steekproefgrootte, de standaardafwijking én het
betrouwbaarheidsniveau. Grotere steekproef geeft smaller, meer spreiding
geeft breder, hoger betrouwbaarheidsniveau geeft breder.

Deel 1 is de betekenis van de drie begrippen en wat de breedte bepaalt.
Deel 2 zijn de interpretatiefouten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een betrouwbaarheidsinterval?",
        opties=[
            "een interval dat met een bepaald niveau de populatiewaarde bevat",
            "het interval waarin alle waarden van de steekproef liggen",
            "het interval tussen het kleinste en het grootste gemeten getal",
            "het interval waarin precies de helft van de populatie valt",
        ],
        antwoord=0,
        uitleg="Het is een schatting met een marge: niet één getal maar een reeks getallen die bij de data passen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de foutenmarge van een betrouwbaarheidsinterval?",
        opties=[
            "de helft van de breedte van het interval",
            "de hele breedte van het interval",
            "de kans dat het interval de populatiewaarde mist",
            "het verschil tussen de steekproef en de populatie",
        ],
        antwoord=0,
        uitleg="Bij 52 procent plus of min 3 procent is de foutenmarge 3 procent en is het interval 6 procent breed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een betrouwbaarheidsniveau van vijfennegentig procent?",
        opties=[
            "van alle zulke intervallen bevat vijfennegentig procent de populatiewaarde",
            "vijfennegentig procent van de populatie ligt in dit interval",
            "vijfennegentig procent van de steekproef ligt in dit interval",
            "de schatting is vijfennegentig procent nauwkeurig",
        ],
        antwoord=0,
        uitleg="Het niveau gaat over de methode, niet over dit ene interval. Vijf op de honderd intervallen missen de waarde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een groter betrouwbaarheidsniveau geeft een breder interval.",
        antwoord=True,
        uitleg="Wil je zekerder zijn dat je de waarde vangt, dan moet je net wijder gooien. Negenennegentig procent is breder dan vijfennegentig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het interval als de steekproef groter wordt?",
        opties=[
            "het wordt smaller",
            "het wordt breder",
            "het blijft even breed",
            "het schuift naar rechts",
        ],
        antwoord=0,
        uitleg="Meer gegevens betekent minder onzekerheid. Maar de winst gaat met de wortel uit n, dus vier keer meer werk halveert de marge.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het interval als de standaardafwijking in de populatie groter is?",
        opties=[
            "het wordt breder",
            "het wordt smaller",
            "het blijft even breed",
            "het schuift naar links",
        ],
        antwoord=0,
        uitleg="Meer spreiding betekent dat één steekproef minder zegt, dus de marge groeit.",
    ),
    dict(
        type="invultekst",
        vraag="Een onderzoek geeft 52 procent plus of min 3 procent. Wat is de ondergrens van het interval in procent? Geef het getal in cijfers.",
        antwoord=["49"],
        uitleg="52 min 3 is 49. De bovengrens is 55.",
    ),
    dict(
        type="waarofniet",
        vraag="Een smaller interval betekent altijd een betere steekproef.",
        antwoord=False,
        uitleg="Niet altijd. Smaller kan ook komen van een lager betrouwbaarheidsniveau, en een vertekende steekproef geeft een smal interval rond het verkeerde getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie dingen bepalen volgens de fiche de breedte van een betrouwbaarheidsinterval?",
        opties=[
            "de steekproefgrootte, de standaardafwijking en het betrouwbaarheidsniveau",
            "de populatiegrootte, het gemiddelde en de mediaan",
            "het significantieniveau, de p-waarde en de nulhypothese",
            "het aantal variabelen, de eenheid en het aantal decimalen",
        ],
        antwoord=0,
        uitleg="Die drie staan letterlijk in de fiche opgesomd. Het gemiddelde zelf bepaalt enkel waar het interval ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partij haalt in een enquête 48 procent met een foutenmarge van 4 procent. Mag men zeggen dat ze geen meerderheid haalt?",
        opties=[
            "nee, want het interval loopt van 44 tot 52 procent en vijftig zit erin",
            "ja, want 48 is kleiner dan 50",
            "ja, want de foutenmarge is kleiner dan het verschil",
            "nee, want een enquête zegt nooit iets over een verkiezing",
        ],
        antwoord=0,
        uitleg="Zodra vijftig procent in het interval ligt, kan je niet besluiten of de partij er onder of boven zit.",
    ),
    dict(
        type="waarofniet",
        vraag="Het betrouwbaarheidsinterval wordt breder als je het betrouwbaarheidsniveau van vijfennegentig naar negentig procent verlaagt.",
        antwoord=False,
        uitleg="Omgekeerd: minder zekerheid vragen geeft een smaller interval. Je koopt nauwkeurigheid met zekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je uit een interval van 44 tot 52 procent de schatting en de marge?",
        opties=[
            "het midden is 48 procent en de marge is 4 procent",
            "het midden is 44 procent en de marge is 8 procent",
            "het midden is 52 procent en de marge is 4 procent",
            "het midden is 48 procent en de marge is 8 procent",
        ],
        antwoord=0,
        uitleg="Het midden van 44 en 52 is 48, en de halve breedte is 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee onderzoeken schatten hetzelfde percentage. Het ene geeft een marge van 2 procent, het andere 6 procent. Wat weet je?",
        opties=[
            "het eerste onderzoek had waarschijnlijk een grotere steekproef",
            "het eerste onderzoek had een lager betrouwbaarheidsniveau nodig",
            "het tweede onderzoek is nauwkeuriger",
            "de twee onderzoeken zijn niet te vergelijken",
        ],
        antwoord=0,
        uitleg="Bij hetzelfde niveau is een smallere marge het teken van meer gegevens.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe breed is een interval met een foutenmarge van 2,5 procent? Geef het getal in procent, in cijfers.",
        antwoord=["5", "5 procent"],
        uitleg="De breedte is twee keer de foutenmarge, dus 5 procent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een betrouwbaarheidsinterval kan zowel voor een populatiegemiddelde als voor een populatieproportie opgesteld worden.",
        antwoord=True,
        uitleg="De fiche noemt beide gevallen apart: een interval voor het populatiegemiddelde en een voor de populatieproportie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft men bij een enquête liever een interval dan één getal?",
        opties=[
            "omdat één getal doet alsof er geen onzekerheid is",
            "omdat een interval altijd dichter bij de waarheid ligt",
            "omdat de wet een foutenmarge oplegt bij elke enquête",
            "omdat men het exacte getal niet mag publiceren",
        ],
        antwoord=0,
        uitleg="Een steekproef geeft nooit het exacte populatiegetal. Het interval maakt die onzekerheid zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker wil zijn marge halveren. Hoe groot moet zijn steekproef worden?",
        opties=[
            "vier keer zo groot",
            "twee keer zo groot",
            "acht keer zo groot",
            "de helft kleiner",
        ],
        antwoord=0,
        uitleg="De marge gaat met de wortel uit n, dus vier keer meer gegevens voor de helft minder marge.",
    ),
    dict(
        type="waarofniet",
        vraag="Het midden van een betrouwbaarheidsinterval is het steekproefresultaat.",
        antwoord=True,
        uitleg="Het interval ligt symmetrisch rond je schatting uit de steekproef, met de foutenmarge aan beide kanten.",
    ),
    dict(
        type="invultekst",
        vraag="Welk betrouwbaarheidsniveau wordt het vaakst gebruikt? Geef het getal in procent, in cijfers.",
        antwoord=["95", "95 procent"],
        uitleg="Vijfennegentig procent. Soms wordt negenennegentig procent gebruikt als men zekerder wil zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft: de marge is 3 procent, dus het interval is 3 procent breed. Wat is er mis?",
        opties=[
            "de marge gaat naar twee kanten, dus het interval is 6 procent breed",
            "de marge moet altijd in absolute getallen en niet in procent",
            "een interval heeft geen breedte, enkel een midden",
            "er is niets mis, marge en breedte zijn hetzelfde",
        ],
        antwoord=0,
        uitleg="Plus of min 3 procent betekent 3 omlaag en 3 omhoog. De breedte is dubbel de marge.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een onderzoek geeft een interval van 46 tot 54 procent op niveau vijfennegentig procent. Welke stelling is juist?",
        opties=[
            "alle percentages tussen 46 en 54 passen bij deze data",
            "vijfennegentig procent van de bevolking zit tussen 46 en 54 procent",
            "het echte percentage is zeker 50 procent",
            "vijfennegentig procent van de steekproef gaf hetzelfde antwoord",
        ],
        antwoord=0,
        uitleg="Het interval zegt welke populatiewaarden geloofwaardig zijn op grond van deze steekproef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: vijfennegentig procent van de Belgen ligt in dit betrouwbaarheidsinterval. Wat is de fout?",
        opties=[
            "het interval gaat over de populatiewaarde, niet over de individuen",
            "het moet negenennegentig procent zijn en niet vijfennegentig",
            "het interval gaat over de steekproef en niet over de populatie",
            "er is geen fout, dat is de juiste lezing",
        ],
        antwoord=0,
        uitleg="Dit is de meest gemaakte fout. Het interval schat één getal van de populatie, bijvoorbeeld het gemiddelde, en niet de spreiding van de mensen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een betrouwbaarheidsinterval van vijfennegentig procent bevat met zekerheid de populatiewaarde.",
        antwoord=False,
        uitleg="Nee. Eén op de twintig van zulke intervallen mist ze, en je weet nooit of jouw interval daartoe hoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: er is vijfennegentig procent kans dat het echte gemiddelde tussen deze twee getallen ligt. Waarom is dat ongelukkig geformuleerd?",
        opties=[
            "het populatiegemiddelde staat vast, het is de methode die in vijfennegentig procent lukt",
            "vijfennegentig procent moet negentig procent zijn bij een gemiddelde",
            "het populatiegemiddelde ligt nooit in zo'n interval, enkel de gemeten steekproefwaarden",
            "men mag niet over kans spreken bij een interval over een gemiddelde",
        ],
        antwoord=0,
        uitleg="Het echte gemiddelde beweegt niet. Het zijn de intervallen die van steekproef tot steekproef verschuiven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een interval voor het gemiddelde loopt van 18 tot 22 jaar. Iemand besluit dat vrijwel iedereen tussen 18 en 22 is. Wat is de fout?",
        opties=[
            "het interval schat het gemiddelde, niet de leeftijd van de mensen zelf",
            "het interval is te smal om een besluit te nemen",
            "het interval moet in maanden uitgedrukt worden",
            "er is geen fout, de leeftijden van de mensen liggen tussen die twee grenzen",
        ],
        antwoord=0,
        uitleg="De leeftijden zelf kunnen van 12 tot 80 lopen terwijl het gemiddelde netjes rond 20 ligt.",
    ),
    dict(
        type="invultekst",
        vraag="Een interval loopt van 30 tot 40. Wat is de foutenmarge? Geef het getal in cijfers.",
        antwoord=["5"],
        uitleg="De breedte is 10, dus de marge is de helft: 5. Het midden is 35.",
    ),
    dict(
        type="waarofniet",
        vraag="Neem je een nieuwe steekproef, dan krijg je meestal een ander betrouwbaarheidsinterval.",
        antwoord=True,
        uitleg="Dat is steekproefvariabiliteit. Het interval zelf verschuift, de populatiewaarde blijft waar ze is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee intervallen overlappen niet. Wat mag je besluiten?",
        opties=[
            "er is een aanwijzing dat de twee populatiewaarden verschillen",
            "de twee populatiewaarden zijn zeker gelijk",
            "een van de twee onderzoeken moet dan fout uitgevoerd zijn",
            "de intervallen zijn te smal gekozen",
        ],
        antwoord=0,
        uitleg="Geen overlap is een sterke aanwijzing voor een verschil. Omgekeerd bewijst overlap geen gelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: dit interval is smal, dus mijn steekproef was representatief. Wat is de fout?",
        opties=[
            "breedte zegt iets over de omvang van de steekproef, niet over de kwaliteit ervan",
            "een smal interval wijst juist op een kleine steekproef",
            "representatief heeft niets met statistiek te maken",
            "er is geen fout, een smal interval bewijst dat de steekproef representatief is",
        ],
        antwoord=0,
        uitleg="Een vertekende steekproef van tienduizend mensen geeft een smal interval rond het verkeerde getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoek geeft een interval van 2 tot 9 procent. Iemand zegt: dus ongeveer 2 procent. Wat is de fout?",
        opties=[
            "hij kiest één grens en negeert de hele onzekerheid",
            "hij mag enkel de bovengrens gebruiken",
            "hij moet het interval eerst in absolute getallen omzetten",
            "er is geen fout, de ondergrens is de veilige schatting",
        ],
        antwoord=0,
        uitleg="De beste schatting is het midden, hier 5,5 procent, en de marge erbij vermelden. Een grens uitkiezen is misleidend.",
    ),
    dict(
        type="waarofniet",
        vraag="Een betrouwbaarheidsinterval kan je gebruiken om een hypothese te beoordelen.",
        antwoord=True,
        uitleg="Ligt het getal van H0 buiten het interval van vijfennegentig procent, dan zou een tweezijdige toets op vijf procent H0 verwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partij haalt 53 procent met een interval van 50 tot 56 procent. Welke uitspraak past?",
        opties=[
            "een meerderheid is mogelijk maar niet aangetoond, want 50 is de ondergrens",
            "de partij haalt zeker een meerderheid",
            "de partij haalt zeker geen meerderheid",
            "het interval is fout opgesteld, want 53 ligt niet precies in het midden",
        ],
        antwoord=0,
        uitleg="Precies op de grens kan je niets besluiten. Een voorzichtige lezing is hier het eerlijkst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel van de honderd intervallen van vijfennegentig procent missen gemiddeld de populatiewaarde? Geef het getal in cijfers.",
        antwoord=["5"],
        uitleg="Vijf van de honderd, want vijfennegentig procent raakt ze.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoger betrouwbaarheidsniveau maakt je schatting nauwkeuriger.",
        antwoord=False,
        uitleg="Omgekeerd: zekerder maar vager. Negenennegentig procent zekerheid koop je met een breder en dus minder scherp interval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: mijn interval loopt van 40 tot 60, dus mijn onderzoek is mislukt. Wat zeg je?",
        opties=[
            "het interval is breed, dus de steekproef was klein, maar het resultaat is niet fout",
            "hij heeft gelijk, zo'n breed interval mag niet gepubliceerd worden",
            "hij moet het betrouwbaarheidsniveau verhogen om het smaller te maken",
            "hij moet het midden als exact resultaat opgeven",
        ],
        antwoord=0,
        uitleg="Een breed interval is een eerlijk verslag van weinig gegevens. Meer deelnemers maken het smaller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een foutenmarge en een meetfout?",
        opties=[
            "een foutenmarge komt van het steekproeven, een meetfout van het instrument",
            "er is geen verschil, het zijn twee woorden voor hetzelfde",
            "een meetfout is altijd groter dan een foutenmarge",
            "een foutenmarge geldt alleen bij een gemiddelde",
        ],
        antwoord=0,
        uitleg="De foutenmarge zit er zelfs bij een perfect meetinstrument, gewoon omdat je niet iedereen bevraagd hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Als het getal nul buiten het betrouwbaarheidsinterval van een verschil ligt, is er een aanwijzing voor een echt verschil.",
        antwoord=True,
        uitleg="Nul betekent geen verschil. Ligt nul buiten het interval, dan passen de data slecht bij geen verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vermeldt een goede krant altijd de steekproefgrootte bij een enquête?",
        opties=[
            "omdat de lezer dan kan inschatten hoe breed de foutenmarge is",
            "omdat de wet dat verplicht bij elke publicatie",
            "omdat het populatiegemiddelde er rechtstreeks uit volgt",
            "omdat de steekproefgrootte het resultaat bepaalt",
        ],
        antwoord=0,
        uitleg="Driehonderd of drieduizend deelnemers maakt een enorm verschil voor hoe serieus je het cijfer mag nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker rapporteert alleen het midden van zijn interval. Wat gaat daarmee verloren?",
        opties=[
            "de lezer kan niet zien hoe onzeker de schatting is",
            "de lezer kent het betrouwbaarheidsniveau niet meer",
            "het midden is nooit de beste schatting",
            "er gaat niets verloren, het midden volstaat",
        ],
        antwoord=0,
        uitleg="52 procent met een marge van 1 en 52 procent met een marge van 9 zijn twee heel verschillende boodschappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rapport zegt: het interval bevat de steekproefwaarde, dus het klopt. Wat is er mis?",
        opties=[
            "het interval ligt per constructie rond de steekproefwaarde, dat bewijst niets",
            "het interval mag de steekproefwaarde niet bevatten",
            "men moet eerst de p-waarde berekenen voor men dat mag zeggen",
            "er is niets mis, dat is een geldige controle",
        ],
        antwoord=0,
        uitleg="De steekproefwaarde is het midden. Wat je wil weten, is of de populatiewaarde erin ligt, en dat weet je nooit zeker.",
    ),
]
