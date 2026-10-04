# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Eenparig rechtlijnige beweging.

Hoort bij "beweging - krachten" van de vakfiche fysica 2de graad
doorstroomfinaliteit, het onderdeel dat samen met grootheden en eenheden 35 %
van het examen weegt.

Deel 1 gaat over de begrippen: positie, baan, afgelegde weg en verplaatsing, de
vier kenmerken van de verplaatsings- en snelheidsvector, en het verschil tussen
een ogenblikkelijke en een gemiddelde snelheid. Deel 2 gaat over het rekenen en
over de grafieken: de positiefunctie x = x₀ + v.(t − t₀), het aflezen van een
x(t)- en een v(t)-grafiek, de oppervlakte onder een v(t)-grafiek, en inhaal- en
kruisingsproblemen.

De twee formules van dit thema zijn vg = Δx/Δt en x = x₀ + v.(t − t₀). De eerste
staat niet in de bijlage van het examen en moet dus uit het hoofd gekend zijn.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de afgelegde weg en de verplaatsing?",
        opties=[
            "de verplaatsing kijkt enkel naar begin- en eindpunt",
            "de afgelegde weg kijkt enkel naar begin- en eindpunt",
            "de afgelegde weg is altijd kleiner",
            "er is geen verschil, enkel een ander symbool",
        ],
        antwoord=0,
        uitleg="De verplaatsing Δx is het verschil tussen de eindpositie en de beginpositie. De afgelegde weg Δs is de hele weg die je echt gelopen hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een loper legt één volledige ronde van 400 m af op een piste. Wat geldt?",
        opties=[
            "de afgelegde weg is 400 m en de verplaatsing is 0 m",
            "de afgelegde weg is 0 m en de verplaatsing is 400 m",
            "beide zijn 400 m",
            "beide zijn 0 m",
        ],
        antwoord=0,
        uitleg="Na één ronde staat de loper weer op zijn startplaats, dus de verplaatsing is nul. De afgelegde weg is wel de hele 400 m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een eenparig rechtlijnige beweging? Kruis alles aan wat juist is.",
        opties=[
            "de snelheid blijft gelijk",
            "de versnelling is nul",
            "de positie van het voorwerp blijft gelijk",
            "de snelheid neemt gelijkmatig toe",
        ],
        antwoord=[0, 1],
        uitleg="Bij een ERB blijft de snelheid gelijk in grootte, richting en zin, en dus is de versnelling nul. De positie verandert juist wel, anders zou het voorwerp stilstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de snelheidsvector bij een ERB zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de grootte blijft gelijk",
            "de zin blijft gelijk",
            "het aangrijpingspunt blijft gelijk",
            "de richting verandert gelijkmatig",
        ],
        antwoord=[0, 1],
        uitleg="Bij een ERB blijven grootte, richting en zin gelijk. Het aangrijpingspunt schuift juist mee met het voorwerp, want dat verplaatst zich.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt 150 km in 2,0 uur. Wat is de gemiddelde snelheid?",
        opties=["75 km/h", "300 km/h", "7,5 km/h", "50 km/h"],
        antwoord=0,
        uitleg="Met vg = Δx / Δt krijg je 150 km / 2,0 h = 75 km/h. Dat zegt niets over de snelheid op één bepaald ogenblik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af op de snelheidsmeter van een auto?",
        opties=[
            "de ogenblikkelijke snelheid",
            "de gemiddelde snelheid van de rit",
            "de afgelegde weg",
            "de versnelling",
        ],
        antwoord=0,
        uitleg="De snelheidsmeter geeft de snelheid op dat ene moment. De gemiddelde snelheid van de hele rit kan heel anders zijn, bijvoorbeeld door een file.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser rijdt in de zin tegengesteld aan de x-as. Wat geldt voor zijn snelheid?",
        opties=[
            "het teken van de snelheid is negatief",
            "de grootte van de snelheid is negatief",
            "de snelheid is nul",
            "de afgelegde weg is negatief",
        ],
        antwoord=0,
        uitleg="Het teken zegt in welke zin het voorwerp beweegt. De grootte van een snelheid en een afgelegde weg zijn nooit negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van snelheid?",
        opties=["m/s", "km/h", "m/s²", "m"],
        antwoord=0,
        uitleg="De meter per seconde. De kilometer per uur mag je gebruiken, maar is geen SI-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een puntmassa zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "je doet alsof de hele massa in één punt zit",
            "het is een model dat het rekenen eenvoudiger maakt",
            "een puntmassa heeft geen massa",
            "enkel heel kleine voorwerpen mag je als puntmassa bekijken",
        ],
        antwoord=[0, 1],
        uitleg="Een puntmassa is een model: je vergeet de vorm en de grootte van het voorwerp. Een trein kan je als puntmassa bekijken als je enkel naar zijn plaats op het traject kijkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wandelaar vertrekt op positie x₀ = 20 m en wandelt in de positieve zin tot x = 95 m. Hoe groot is de verplaatsing?",
        opties=["75 m", "115 m", "−75 m", "95 m"],
        antwoord=0,
        uitleg="De verplaatsing is Δx = x − x₀ = 95 − 20 = 75 m. Ze is positief, want de wandelaar gaat in de zin van de x-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de baan van een puntmassa?",
        opties=[
            "de lijn die het voorwerp beschrijft",
            "het beginpunt van de beweging",
            "de tijd die de beweging duurt",
            "de snelheid op elk tijdstip",
        ],
        antwoord=0,
        uitleg="De baan is de lijn waarlangs het voorwerp beweegt. Is die lijn een rechte, dan heet de beweging rechtlijnig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenparig rechtlijnige beweging is de gemiddelde snelheid gelijk aan de ogenblikkelijke snelheid.",
        antwoord=True,
        uitleg="De snelheid verandert niet, dus het gemiddelde ervan is diezelfde waarde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verplaatsing kan negatief zijn.",
        antwoord=True,
        uitleg="Beweegt een voorwerp tegen de zin van de x-as in, dan is Δx negatief. Het teken hoort bij de zin van de beweging.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgelegde weg van een voorwerp is altijd even groot als de grootte van zijn verplaatsing.",
        antwoord=False,
        uitleg="Enkel als het voorwerp rechtdoor blijft gaan in dezelfde zin. Keert het terug, dan is de afgelegde weg groter.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp in rust heeft een snelheid van nul.",
        antwoord=True,
        uitleg="In rust verandert de positie niet, dus Δx is nul en daarmee ook de snelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De eenheid km/h is groter dan de eenheid m/s, want er staat kilo in.",
        antwoord=False,
        uitleg="Omgekeerd: 1 m/s is 3,6 km/h, dus de meter per seconde is de grotere eenheid. De uren in de noemer maken het verschil.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor een verplaatsing?",
        antwoord=["Δx", "delta x", "dx"],
        uitleg="Δx, met de Griekse letter delta voor een verandering. De afgelegde weg krijgt Δs.",
    ),
    dict(
        type="invultekst",
        vraag="Een auto rijdt met 25 m/s. Hoeveel meter rijdt hij in 4,0 s? Schrijf het getal in meter.",
        antwoord=["100", "100 m"],
        uitleg="Bij een ERB is Δx = v . Δt = 25 . 4,0 = 100 m.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de snelheid op één bepaald tijdstip?",
        antwoord=["ogenblikkelijke snelheid", "de ogenblikkelijke snelheid", "ogenblikkelijk"],
        uitleg="De ogenblikkelijke snelheid. De gemiddelde snelheid kijkt naar een hele tijdsduur.",
    ),
    dict(
        type="invultekst",
        vraag="Een trein legt 60 km af in een half uur. Wat is zijn gemiddelde snelheid in km/h? Schrijf het getal.",
        antwoord=["120", "120 km/h"],
        uitleg="vg = 60 km / 0,5 h = 120 km/h.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat stelt de steilheid van een x(t)-grafiek voor?",
        opties=["de snelheid", "de versnelling", "de afgelegde weg", "de tijdsduur"],
        antwoord=0,
        uitleg="De steilheid is Δx / Δt, en dat is net de snelheid. Een steilere rechte betekent dus sneller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de oppervlakte onder een v(t)-grafiek voor?",
        opties=["de verplaatsing", "de versnelling", "de snelheid", "de tijdsduur"],
        antwoord=0,
        uitleg="De oppervlakte is snelheid maal tijd, en dat is de verplaatsing. Ligt het stuk onder de tijdas, dan is de verplaatsing negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een x(t)-grafiek loopt een tijd lang horizontaal. Wat doet het voorwerp dan?",
        opties=[
            "het staat stil",
            "het beweegt met constante snelheid",
            "het beweegt achteruit",
            "het versnelt",
        ],
        antwoord=0,
        uitleg="De positie verandert niet, dus de snelheid is nul. Dat is een rustpauze.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een v(t)-grafiek van een ERB is de lijn:",
        opties=[
            "horizontaal",
            "een schuine rechte door de oorsprong",
            "een parabool",
            "verticaal",
        ],
        antwoord=0,
        uitleg="Bij een ERB blijft de snelheid gelijk, dus de v(t)-grafiek is een horizontale rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag="De positiefunctie van een beweging is x = 10 + 3 . t, met x in meter en t in seconde. Wat is de snelheid?",
        opties=["3 m/s", "10 m/s", "13 m/s", "30 m/s"],
        antwoord=0,
        uitleg="In x = x₀ + v . t is 10 m de beginpositie en 3 m/s de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="De positiefunctie is x = 40 − 5 . t, met x in meter en t in seconde. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het voorwerp vertrekt op 40 m",
            "het voorwerp beweegt tegen de zin van de x-as",
            "het voorwerp staat stil",
            "het voorwerp vertrekt in de oorsprong",
        ],
        antwoord=[0, 1],
        uitleg="De beginpositie is 40 m en de snelheid is −5 m/s. Het minteken zegt dat het voorwerp naar kleinere x-waarden toe gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp heeft een positiefunctie x = 40 − 5 . t, met x in meter en t in seconde. Op welk tijdstip is het in de oorsprong?",
        opties=["na 8,0 s", "na 5,0 s", "na 40 s", "na 200 s"],
        antwoord=0,
        uitleg="Stel x = 0: dan is 5 . t = 40, dus t = 8,0 s.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een v(t)-grafiek staat een horizontale lijn op −4 m/s gedurende 3,0 s. Hoe groot is de verplaatsing?",
        opties=["−12 m", "12 m", "−1,3 m", "−7,0 m"],
        antwoord=0,
        uitleg="Δx = v . Δt = −4 . 3,0 = −12 m. Het voorwerp gaat 12 m tegen de zin van de x-as in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee lopers vertrekken samen. In een v(t)-grafiek ligt de lijn van loper A hoger dan die van loper B. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "A loopt sneller dan B",
            "A legt in dezelfde tijd een grotere weg af",
            "A versnelt meer dan B",
            "A en B blijven naast elkaar",
        ],
        antwoord=[0, 1],
        uitleg="Een hogere lijn in een v(t)-grafiek betekent een grotere snelheid, en dus een grotere oppervlakte eronder. Van versnellen is geen sprake: beide lijnen zijn horizontaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wandelaar vertrekt om 9 uur en wandelt met 5,0 km/h. Een fietser vertrekt om 10 uur op dezelfde plaats met 15 km/h. Na hoeveel tijd haalt de fietser de wandelaar in?",
        opties=["na 0,50 h", "na 1,0 h", "na 1,5 h", "na 3,0 h"],
        antwoord=0,
        uitleg="Bij het vertrek van de fietser heeft de wandelaar al 5,0 km voorsprong. De fietser loopt 10 km/h in, dus hij heeft 5,0 / 10 = 0,50 h nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee auto's rijden naar elkaar toe, 120 km van elkaar, de ene met 70 km/h en de andere met 50 km/h. Wanneer kruisen ze?",
        opties=["na 1,0 h", "na 2,0 h", "na 0,50 h", "na 1,7 h"],
        antwoord=0,
        uitleg="Samen naderen ze met 70 + 50 = 120 km/h. Over 120 km duurt dat 1,0 h.",
    ),
    dict(
        type="waarofniet",
        vraag="In een v(t)-grafiek lees je de verplaatsing af als de hoogte van de lijn.",
        antwoord=False,
        uitleg="De hoogte van de lijn is de snelheid. De verplaatsing is de oppervlakte onder de lijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte in een x(t)-grafiek die naar beneden loopt, hoort bij een negatieve snelheid.",
        antwoord=True,
        uitleg="De positie wordt kleiner, dus Δx is negatief en de snelheid ook. Het voorwerp gaat tegen de zin van de x-as in.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan uit een x(t)-grafiek de bijbehorende v(t)-grafiek opstellen.",
        antwoord=True,
        uitleg="Per stuk bereken je de steilheid, en die waarde zet je als horizontale lijn in de v(t)-grafiek.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee rechten in een x(t)-grafiek die elkaar snijden, horen bij voorwerpen die elkaar op dat tijdstip kruisen of inhalen.",
        antwoord=True,
        uitleg="Op het snijpunt hebben beide voorwerpen dezelfde positie op hetzelfde tijdstip, dus zijn ze op dezelfde plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit een v(t)-grafiek kan je de beginpositie van het voorwerp aflezen.",
        antwoord=False,
        uitleg="Een v(t)-grafiek geeft enkel de snelheid en, via de oppervlakte, de verplaatsing. De beginpositie moet in de opgave staan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de grafiek waarin de positie tegen de tijd staat? Schrijf de naam van de grafiek.",
        antwoord=["x(t)-grafiek", "x(t)", "positiegrafiek"],
        uitleg="De x(t)-grafiek. Daarnaast bestaan de v(t)-grafiek en de a(t)-grafiek.",
    ),
    dict(
        type="invultekst",
        vraag="Een fietser rijdt met 6,0 m/s gedurende 1,0 minuut. Hoeveel meter legt hij af? Schrijf het getal in meter.",
        antwoord=["360", "360 m"],
        uitleg="Reken de tijd eerst om: 1,0 min = 60 s. Dan is Δx = 6,0 . 60 = 360 m.",
    ),
    dict(
        type="invultekst",
        vraag="In de positiefunctie x = x₀ + v.(t − t₀): wat stelt x₀ voor? Schrijf het woord.",
        antwoord=["beginpositie", "de beginpositie", "startpositie"],
        uitleg="De beginpositie, dus waar het voorwerp zich bevindt op het tijdstip t₀.",
    ),
    dict(
        type="invultekst",
        vraag="Een auto rijdt met een constante snelheid en legt 480 m af in 16 s. Wat is zijn snelheid in m/s? Schrijf het getal.",
        antwoord=["30", "30 m/s"],
        uitleg="v = 480 / 16 = 30 m/s. Dat is ongeveer 108 km/h.",
    ),
]
