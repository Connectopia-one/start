# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Versnelde beweging, vrije val en verticale worp.

Hoort bij "beweging - krachten" van de vakfiche fysica 2de graad
doorstroomfinaliteit, het derde van vijf thema's voor dat onderdeel van 35 %.

Deel 1 gaat over de eenparig veranderlijke rechtlijnige beweging: versnellen en
vertragen, het teken van de versnelling, en het onderscheid tussen een ERB, een
eenparig versnelde en een eenparig vertraagde beweging in een x(t)-, v(t)- of
a(t)-grafiek. Deel 2 gaat over de vrije val en de verticale worp naar boven, en
over het vergelijken van twee bewegingen in dezelfde grafiek.

De fiche geeft geen formules voor de EVRB: er staat geen v = v₀ + a.t en geen
baanvergelijking met t². De vragen blijven dus bij de grafieken en bij de
gemiddelde versnelling als Δv/Δt. De valversnelling in België is 9,81 m/s² en
staat bij de constanten die een kind op het examen krijgt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een eenparig veranderlijke rechtlijnige beweging?",
        opties=[
            "een beweging waarbij de versnelling gelijk blijft",
            "een beweging waarbij de snelheid gelijk blijft",
            "een beweging waarbij de positie gelijk blijft",
            "een beweging langs een gebogen baan",
        ],
        antwoord=0,
        uitleg="Bij een EVRB blijft de versnelling gelijk, dus verandert de snelheid elke seconde met evenveel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van versnelling?",
        opties=["m/s²", "m/s", "m", "N"],
        antwoord=0,
        uitleg="De meter per seconde kwadraat: hoeveel meter per seconde de snelheid elke seconde verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt in de positieve zin en vertraagt. Wat geldt?",
        opties=[
            "de versnelling is negatief",
            "de versnelling is positief",
            "de versnelling is nul",
            "de snelheid is negatief",
        ],
        antwoord=0,
        uitleg="De snelheid is positief maar wordt kleiner, dus Δv is negatief. Snelheid en versnelling hebben dan een tegengestelde zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een v(t)-grafiek is de lijn een schuine rechte die stijgt. Wat doet het voorwerp?",
        opties=[
            "het versnelt gelijkmatig",
            "het vertraagt gelijkmatig",
            "het beweegt met constante snelheid",
            "het staat stil",
        ],
        antwoord=0,
        uitleg="De snelheid neemt elke seconde met evenveel toe. De steilheid van die rechte is de versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de steilheid van een v(t)-grafiek voor?",
        opties=["de versnelling", "de verplaatsing", "de snelheid", "de positie"],
        antwoord=0,
        uitleg="De steilheid is Δv / Δt, en dat is de gemiddelde versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een a(t)-grafiek is een horizontale lijn boven de tijdas. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de versnelling blijft gelijk",
            "de snelheid neemt toe",
            "de snelheid blijft gelijk",
            "het voorwerp staat stil",
        ],
        antwoord=[0, 1],
        uitleg="De versnelling is constant en positief, dus de snelheid groeit gelijkmatig. Een voorwerp in rust zou een versnelling van nul hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wagen gaat van 0 naar 20 m/s in 5,0 s. Wat is de gemiddelde versnelling?",
        opties=["4,0 m/s²", "100 m/s²", "0,25 m/s²", "20 m/s²"],
        antwoord=0,
        uitleg="ag = Δv / Δt = 20 / 5,0 = 4,0 m/s².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een trein remt van 30 m/s naar 10 m/s in 8,0 s. Wat is de gemiddelde versnelling?",
        opties=["−2,5 m/s²", "2,5 m/s²", "−5,0 m/s²", "−20 m/s²"],
        antwoord=0,
        uitleg="Δv = 10 − 30 = −20 m/s en Δt = 8,0 s, dus ag = −20 / 8,0 = −2,5 m/s². Het minteken hoort bij het vertragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een x(t)-grafiek van een eenparig versnelde beweging is de lijn:",
        opties=[
            "een kromme die steeds steiler wordt",
            "een rechte",
            "horizontaal",
            "een kromme die steeds vlakker wordt",
        ],
        antwoord=0,
        uitleg="De snelheid neemt toe, dus de steilheid van de x(t)-grafiek groeit. Bij vertragen wordt de kromme juist vlakker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de versnellingsvector bij een vertragende beweging zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "hij heeft dezelfde richting als de snelheid",
            "hij heeft de tegengestelde zin van de snelheid",
            "hij heeft dezelfde zin als de snelheid",
            "hij is nul",
        ],
        antwoord=[0, 1],
        uitleg="Bij vertragen liggen snelheid en versnelling op dezelfde rechte, dus dezelfde richting, maar met tegengestelde zin. Daarom wordt de snelheid kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee voorwerpen staan in dezelfde v(t)-grafiek. De rechte van A is steiler dan die van B. Wat geldt?",
        opties=[
            "A heeft een grotere versnelling",
            "A heeft een grotere beginsnelheid",
            "A legt zeker een kleinere weg af",
            "A vertraagt en B versnelt",
        ],
        antwoord=0,
        uitleg="De steilheid van een v(t)-grafiek is de versnelling, dus de steilere rechte hoort bij de grotere versnelling. Over de beginsnelheid zegt de steilheid niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenparig veranderlijke beweging verandert de snelheid elke seconde met evenveel.",
        antwoord=True,
        uitleg="Dat is net wat eenparig veranderlijk betekent: de versnelling blijft gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve versnelling betekent altijd dat het voorwerp vertraagt.",
        antwoord=False,
        uitleg="Alleen als de snelheid positief is. Beweegt een voorwerp al in de negatieve zin, dan maakt een negatieve versnelling het juist sneller.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp met een snelheid van nul kan op dat ogenblik toch een versnelling hebben.",
        antwoord=True,
        uitleg="Een bal die je recht omhoog gooit staat op het hoogste punt een ogenblik stil, maar de valversnelling werkt daar wel. Een ogenblik later valt hij.",
    ),
    dict(
        type="waarofniet",
        vraag="In een a(t)-grafiek van een EVRB is de lijn een schuine rechte.",
        antwoord=False,
        uitleg="De versnelling blijft gelijk, dus de a(t)-grafiek is een horizontale lijn. Een schuine rechte zou betekenen dat de versnelling zelf verandert.",
    ),
    dict(
        type="waarofniet",
        vraag="Een horizontaal stuk in een v(t)-grafiek betekent dat het voorwerp stilstaat.",
        antwoord=False,
        uitleg="Een horizontaal stuk betekent een constante snelheid, dus een ERB. Stilstaan is enkel zo als die lijn op nul ligt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een beweging waarbij de snelheid gelijkmatig kleiner wordt? Schrijf het woord dat bij versneld hoort.",
        antwoord=["vertraagd", "vertraagde", "vertragend"],
        uitleg="Een eenparig vertraagde rechtlijnige beweging. De versnelling blijft gelijk, maar heeft de tegengestelde zin van de snelheid.",
    ),
    dict(
        type="invultekst",
        vraag="Een bromfiets gaat van 4,0 m/s naar 14 m/s in 5,0 s. Hoe groot is de gemiddelde versnelling in m/s²? Schrijf het getal.",
        antwoord=["2", "2,0", "2 m/s²"],
        uitleg="Δv = 14 − 4,0 = 10 m/s, dus ag = 10 / 5,0 = 2,0 m/s².",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor de gemiddelde versnelling?",
        antwoord=["ag", "a_g", "a g"],
        uitleg="ag, met een kleine g eronder voor gemiddeld. De ogenblikkelijke versnelling krijgt gewoon a.",
    ),
    dict(
        type="invultekst",
        vraag="In welke grafiek stelt de oppervlakte onder de lijn de verplaatsing voor? Schrijf de naam van de grafiek.",
        antwoord=["v(t)-grafiek", "v(t)", "snelheidsgrafiek"],
        uitleg="In de v(t)-grafiek. Snelheid maal tijd geeft een verplaatsing, dus de oppervlakte onder de lijn.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een vrije val? Kruis alles aan wat juist is.",
        opties=[
            "een val waarbij enkel de zwaartekracht werkt",
            "een val waarbij je de luchtweerstand buiten beschouwing laat",
            "elke beweging die naar beneden gaat",
            "een val met een snelheid die gelijk blijft",
        ],
        antwoord=[0, 1],
        uitleg="Enkel de zwaartekracht werkt, dus laat je de luchtweerstand weg. Het is een model: in het echt is er altijd wat lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de valversnelling in België?",
        opties=["9,81 m/s²", "1,62 m/s²", "98,1 m/s²", "0,981 m/s²"],
        antwoord=0,
        uitleg="g = 9,81 m/s², of ook 9,81 N/kg. Op de maan is dat veel kleiner, ongeveer 1,62 m/s².",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit een bal recht omhoog. Wat gebeurt er met zijn snelheid op de weg naar boven?",
        opties=[
            "ze wordt gelijkmatig kleiner",
            "ze wordt gelijkmatig groter",
            "ze blijft gelijk",
            "ze wordt eerst groter en dan kleiner",
        ],
        antwoord=0,
        uitleg="De valversnelling werkt naar beneden en de bal gaat naar boven, dus de snelheid neemt elke seconde met 9,81 m/s af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het hoogste punt van een verticale worp naar boven zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de snelheid is daar nul",
            "de versnelling is daar 9,81 m/s² naar beneden",
            "de versnelling is daar nul",
            "de zwaartekracht werkt daar niet",
        ],
        antwoord=[0, 1],
        uitleg="Op het hoogste punt keert de beweging om, dus is de snelheid één ogenblik nul. De zwaartekracht blijft wel werken, dus ook de valversnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een v(t)-grafiek van een vrije val vanuit rust, met de zin naar beneden positief, is de lijn:",
        opties=[
            "een stijgende rechte door de oorsprong",
            "een horizontale lijn boven de tijdas",
            "een rechte die gelijkmatig daalt",
            "een kromme die steeds vlakker wordt",
        ],
        antwoord=0,
        uitleg="De snelheid begint op nul en groeit elke seconde met 9,81 m/s. Dat geeft een rechte door de oorsprong.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een a(t)-grafiek van een vrije val is:",
        opties=[
            "een horizontale lijn op 9,81 m/s²",
            "een rechte die gelijkmatig stijgt",
            "een rechte die gelijkmatig daalt",
            "een horizontale lijn op nul",
        ],
        antwoord=0,
        uitleg="De valversnelling verandert niet tijdens de val, dus de a(t)-grafiek is een horizontale lijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een vrije val en een verticale worp naar boven?",
        opties=[
            "de beginsnelheid is bij een worp naar boven gericht",
            "bij een worp naar boven werkt de zwaartekracht niet mee",
            "bij een vrije val is de valversnelling veel groter",
            "bij een vrije val verandert de snelheid helemaal niet",
        ],
        antwoord=0,
        uitleg="Beide bewegingen hebben dezelfde versnelling naar beneden. Enkel de beginsnelheid verschilt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een steen valt vanuit rust. Welke snelheid heeft hij na 2,0 s, zonder luchtweerstand?",
        opties=["19,6 m/s", "9,81 m/s", "39,2 m/s", "4,9 m/s"],
        antwoord=0,
        uitleg="Elke seconde komt er 9,81 m/s bij, dus na 2,0 s is dat 2,0 . 9,81 = 19,6 m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit een bal met 15 m/s recht omhoog. Na hoeveel tijd is hij op zijn hoogste punt, zonder luchtweerstand?",
        opties=["na 1,5 s", "na 15 s", "na 0,65 s", "na 3,1 s"],
        antwoord=0,
        uitleg="Elke seconde verdwijnt er 9,81 m/s van de snelheid, dus 15 / 9,81 is ongeveer 1,5 s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een parachutist valt eerst sneller en sneller, maar bereikt daarna een constante snelheid. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de luchtweerstand is dan even groot als de zwaartekracht",
            "de resulterende kracht is dan nul",
            "de zwaartekracht is dan verdwenen",
            "de versnelling is dan 9,81 m/s²",
        ],
        antwoord=[0, 1],
        uitleg="Zodra de luchtweerstand even groot is als de zwaartekracht, heffen de twee krachten elkaar op. De resulterende kracht is dan nul en de snelheid verandert niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="In dezelfde v(t)-grafiek staan twee vallende voorwerpen zonder luchtweerstand, een van 1 kg en een van 5 kg. Wat zie je?",
        opties=[
            "twee lijnen die precies samenvallen",
            "een steilere lijn voor het zwaardere voorwerp",
            "een steilere lijn voor het lichtere voorwerp",
            "een horizontale lijn voor het zwaardere voorwerp",
        ],
        antwoord=0,
        uitleg="Zonder luchtweerstand valt alles met dezelfde versnelling van 9,81 m/s², hoe zwaar het ook is. De twee lijnen liggen dus op elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de maan valt een voorwerp langzamer dan op de aarde.",
        antwoord=True,
        uitleg="De zwaarteveldsterkte van de maan is ongeveer zes keer kleiner, dus de valversnelling is dat ook.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vrije val neemt de afgelegde weg elke seconde met evenveel toe.",
        antwoord=False,
        uitleg="De snelheid groeit, dus elke seconde valt het voorwerp verder dan de seconde ervoor. Enkel de snelheid groeit gelijkmatig, niet de afgelegde weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bal die je recht omhoog gooit, komt met dezelfde grootte van snelheid terug in je hand als waarmee hij vertrok, als je de luchtweerstand buiten beschouwing laat.",
        antwoord=True,
        uitleg="De weg naar boven en de weg naar beneden zijn even lang en hebben dezelfde versnelling, dus de snelheid is even groot. Enkel de zin is omgekeerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een verticale worp naar boven verandert de zin van de versnelling op het hoogste punt.",
        antwoord=False,
        uitleg="De versnelling blijft heel de beweging naar beneden gericht. Enkel de zin van de snelheid keert om.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwaar voorwerp valt altijd sneller naar beneden dan een licht voorwerp.",
        antwoord=False,
        uitleg="Zonder lucht vallen ze samen, want de valversnelling is voor alles dezelfde. In de echte lucht hangt het van de luchtweerstand af: een pluim valt trager dan een steen, maar een lichte kogel en een zware kogel vallen even snel.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor de valversnelling?",
        antwoord=["g"],
        uitleg="g, met de waarde 9,81 m/s² in België. Dezelfde letter staat ook voor de zwaarteveldsterkte in N/kg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een val waarbij je de luchtweerstand buiten beschouwing laat? Schrijf de twee woorden.",
        antwoord=["vrije val", "een vrije val", "vrijeval"],
        uitleg="Een vrije val. In het echt is er altijd wat luchtweerstand, dus is het een model.",
    ),
    dict(
        type="invultekst",
        vraag="Een steen valt vanuit rust en heeft na 3,0 s een snelheid van bijna 30 m/s. Hoeveel m/s komt er elke seconde bij? Schrijf het getal.",
        antwoord=["9,81", "9.81", "10"],
        uitleg="9,81 m/s per seconde, want dat is de valversnelling. Na 3,0 s is de snelheid 3,0 . 9,81 = 29,4 m/s.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kracht zorgt voor de versnelling bij een vrije val?",
        antwoord=["zwaartekracht", "de zwaartekracht", "gewicht"],
        uitleg="De zwaartekracht. Die is naar beneden gericht en zorgt voor een versnelling van 9,81 m/s².",
    ),
]
