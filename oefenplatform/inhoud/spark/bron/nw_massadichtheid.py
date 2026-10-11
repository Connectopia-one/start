# -*- coding: utf-8 -*-
"""De vragen voor "Massadichtheid" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel chemie en fysica, "Massadichtheid": de formule ρ = m/V
toepassen, het volume van een regelmatig voorwerp berekenen (kubus, balk, bol,
cilinder) of door onderdompeling bepalen, de massa wegen, de juiste
meetinstrumenten kiezen en aflezen, inhoudsmaten omzetten tussen liter en
kubieke meter en tussen kg/m³ en g/cm³, het verband tussen massa en volume uit
meetresultaten en grafieken afleiden, en uitleggen wanneer een voorwerp zinkt,
zweeft, stijgt of drijft.

Deel 1 oefent de formule, de eenheden en de meetinstrumenten. Deel 2 vraagt
omgekeerd rekenen, grafieken lezen, drijven en zinken, en het verschil tussen
een recht en een omgekeerd evenredig verband.

De getallen zijn zo gekozen dat je ze uit het hoofd kan narekenen. Elke
berekening in dit bestand wordt ook echt nagerekend door
`controleer_natuurwetenschappen.py`.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom weegt een blok ijzer zwaarder dan een even groot blok hout?",
        opties=[
            "IJzer heeft een grotere massadichtheid",
            "IJzer heeft een groter volume",
            "Hout heeft geen massa",
        ],
        antwoord=0,
        uitleg="Massadichtheid zegt hoeveel massa er in één bepaalde hoeveelheid ruimte zit. Bij ijzer zitten de deeltjes zwaarder en dichter op elkaar dan bij hout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij de massadichtheid?",
        opties=[r"\(\rho = m / V\)", r"\(\rho = m \times V\)", r"\(\rho = V / m\)"],
        antwoord=0,
        uitleg=r"Je deelt de massa door het volume. Het symbool \(\rho\) (rho) is de Griekse letter voor massadichtheid.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een voorwerp heeft een massa van \(300\) g en een volume van \(100\,\text{cm}^{3}\). Wat is de massadichtheid?",
        opties=[r"\(3\) g/\(\text{cm}^{3}\)", r"\(30\) g/\(\text{cm}^{3}\)", r"\(0{,}3\) g/\(\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"\(\rho = m / V = 300\) g / \(100\,\text{cm}^{3} = 3\) g/\(\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het volume van een kubus met een ribbe van \(2\) cm?",
        opties=[r"\(8\,\text{cm}^{3}\)", r"\(6\,\text{cm}^{3}\)", r"\(4\,\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"V van een kubus = \(z^{3} = 2 \cdot 2 \cdot 2 = 8\,\text{cm}^{3}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een balk van \(5\) cm op \(4\) cm op \(2\) cm heeft een volume van ___ \(\text{cm}^{3}\).",
        antwoord="40",
        uitleg=r"V van een balk = l × b × h = \(5 \cdot 4 \cdot 2 = 40\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welk meetinstrument bepaal je de massa van een voorwerp?",
        opties=["Met een weegschaal", "Met een maatcilinder", "Met een dynamometer"],
        antwoord=0,
        uitleg="De weegschaal meet massa in gram of kilogram. Een maatcilinder meet volume en een dynamometer meet kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke meetinstrumenten heb je nodig om de massadichtheid van een steen te bepalen?",
        opties=[
            "Een weegschaal",
            "Een maatcilinder met water",
            "Een thermometer",
            "Een chronometer",
        ],
        antwoord=[0, 1],
        uitleg="Je weegt de steen en je meet zijn volume door onderdompeling in een maatcilinder. Temperatuur en tijd heb je daar niet voor nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bepaal je het volume van een onregelmatig voorwerp, zoals een steen?",
        opties=[
            "Door het onder te dompelen en te kijken hoeveel het water stijgt",
            "Door het te wegen",
            "Door de lengte te meten met een meetlat",
        ],
        antwoord=0,
        uitleg="Het voorwerp duwt evenveel water opzij als zijn eigen volume. Het verschil tussen het waterpeil vóór en na het onderdompelen is dus het volume.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het water in een maatcilinder staat op \(50\) mL. Je laat er een moer in zakken en het staat op \(65\) mL. Wat is het volume van de moer?",
        opties=[r"\(15\,\text{cm}^{3}\)", r"\(65\,\text{cm}^{3}\)", r"\(50\,\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"\(65\) mL \(- 50\) mL = \(15\) mL, en \(1\) mL is precies \(1\,\text{cm}^{3}\). Het volume van de moer is dus \(15\,\text{cm}^{3}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"\(1\) liter is evenveel als ___ \(\text{cm}^{3}\).",
        antwoord="1000",
        uitleg=r"\(1\) L = \(1\,\text{dm}^{3} = 1000\,\text{cm}^{3}\). En \(1\) mL = \(1\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel kubieke meter is \(2\) liter?",
        opties=[r"\(0{,}002\,\text{m}^{3}\)", r"\(0{,}2\,\text{m}^{3}\)", r"\(2000\,\text{m}^{3}\)"],
        antwoord=0,
        uitleg=r"\(1\,\text{m}^{3} = 1000\) L, dus \(1\) L = \(0{,}001\,\text{m}^{3}\). Twee liter is dan \(0{,}002\,\text{m}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel liter gaat er in \(0{,}5\,\text{m}^{3}\)?",
        opties=[r"\(500\) L", r"\(50\) L", r"\(5000\) L"],
        antwoord=0,
        uitleg=r"\(1\,\text{m}^{3} = 1000\) L, dus \(0{,}5\,\text{m}^{3} = 0{,}5 \cdot 1000 = 500\) L.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Water heeft een massadichtheid van \(1\) g/\(\text{cm}^{3}\). Hoeveel is dat in kg/\(\text{m}^{3}\)?",
        opties=[r"\(1000\) kg/\(\text{m}^{3}\)", r"\(100\) kg/\(\text{m}^{3}\)", r"\(1\) kg/\(\text{m}^{3}\)"],
        antwoord=0,
        uitleg=r"Van g/\(\text{cm}^{3}\) naar kg/\(\text{m}^{3}\) vermenigvuldig je met \(1000\). Eén liter water weegt dan ook precies \(1\) kg.",
    ),
    dict(
        type="invultekst",
        vraag=r"Aluminium heeft een massadichtheid van \(2700\) kg/\(\text{m}^{3}\). In g/\(\text{cm}^{3}\) is dat ___.",
        antwoord="2,7",
        uitleg=r"Van kg/\(\text{m}^{3}\) naar g/\(\text{cm}^{3}\) deel je door \(1000\): \(2700 : 1000 = 2{,}7\) g/\(\text{cm}^{3}\).",
    ),
    dict(
        type="waarofniet",
        vraag="Massadichtheid is een stofeigenschap: ze hangt niet af van hoe groot je stuk is.",
        antwoord=True,
        uitleg="Een spijker en een balk van hetzelfde ijzer hebben dezelfde massadichtheid. Massa en volume veranderen samen, hun verhouding blijft gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van massadichtheid?",
        opties=[r"kg/\(\text{m}^{3}\)", r"g/\(\text{cm}^{3}\)", "kg"],
        antwoord=0,
        uitleg=r"De SI-eenheid is kilogram per kubieke meter. g/\(\text{cm}^{3}\) mag ook, maar dat is geen SI-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stuk kurk drijft op water. Wat weet je dan?",
        opties=[
            "De massadichtheid van kurk is kleiner dan die van water",
            "De massadichtheid van kurk is groter dan die van water",
            "Kurk heeft geen massa",
        ],
        antwoord=0,
        uitleg="Wat minder dicht is dan de vloeistof, drijft. Wat dichter is, zinkt. Is de massadichtheid precies gelijk, dan zweeft het voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke van deze zinken in water (\(1\) g/\(\text{cm}^{3}\))?",
        opties=[
            r"IJzer, \(7{,}8\) g/\(\text{cm}^{3}\)",
            r"Aluminium, \(2{,}7\) g/\(\text{cm}^{3}\)",
            r"Kurk, \(0{,}24\) g/\(\text{cm}^{3}\)",
            r"Olie, \(0{,}9\) g/\(\text{cm}^{3}\)",
        ],
        antwoord=[0, 1],
        uitleg=r"Alles met een massadichtheid groter dan \(1\) g/\(\text{cm}^{3}\) zinkt in water. Kurk en olie zijn lichter per \(\text{cm}^{3}\) en blijven drijven.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp zweeft in een vloeistof als het even dicht is als die vloeistof.",
        antwoord=True,
        uitleg="Bij gelijke massadichtheid blijft het voorwerp hangen waar je het loslaat: het stijgt niet en het zinkt niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welk instrument kan je rechtstreeks de massadichtheid van een vloeistof meten?",
        opties=["Met een dichtheidsmeter", "Met een thermometer", "Met een weegschaal"],
        antwoord=0,
        uitleg="Een dichtheidsmeter of densiteitsmeter drijft in de vloeistof en je leest de massadichtheid af op de schaal.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Een blok heeft een massa van \(72\) g en is een kubus met een ribbe van \(2\) cm. Wat is de massadichtheid?",
        opties=[r"\(9\) g/\(\text{cm}^{3}\)", r"\(36\) g/\(\text{cm}^{3}\)", r"\(144\) g/\(\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"Eerst het volume: \(z^{3} = 2^{3} = 8\,\text{cm}^{3}\). Dan \(\rho = 72\) g / \(8\,\text{cm}^{3} = 9\) g/\(\text{cm}^{3}\). Dat komt aardig in de buurt van koper.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel weegt \(3\,\text{cm}^{3}\) goud, als goud \(19\) g/\(\text{cm}^{3}\) weegt per kubieke centimeter?",
        opties=[r"\(57\) g", r"\(22\) g", r"\(6{,}3\) g"],
        antwoord=0,
        uitleg=r"Uit \(\rho = m / V\) volgt \(m = \rho \cdot V = 19 \cdot 3 = 57\) g.",
    ),
    dict(
        type="invultekst",
        vraag=r"IJzer heeft een massadichtheid van \(7{,}8\) g/\(\text{cm}^{3}\). Een stuk van \(780\) g heeft een volume van ___ \(\text{cm}^{3}\).",
        antwoord="100",
        uitleg=r"Uit \(\rho = m / V\) volgt \(V = m / \rho = 780 : 7{,}8 = 100\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het volume van een cilinder met een straal van \(2\) cm en een hoogte van \(10\) cm? Reken met \(\pi \approx 3{,}14\).",
        opties=[r"\(125{,}6\,\text{cm}^{3}\)", r"\(62{,}8\,\text{cm}^{3}\)", r"\(40\,\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"\(V = \pi \cdot r^{2} \times h = 3{,}14 \cdot 2^{2} \cdot 10 = 3{,}14 \cdot 4 \cdot 10 = 125{,}6\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het volume van een bol met een straal van \(3\) cm? Reken met \(\pi \approx 3{,}14\).",
        opties=[r"\(113{,}04\,\text{cm}^{3}\)", r"\(37{,}68\,\text{cm}^{3}\)", r"\(28{,}26\,\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"\(V = \tfrac{4}{3} \cdot \pi \cdot r^{3} = \tfrac{4}{3} \cdot 3{,}14 \cdot 27 = 113{,}04\,\text{cm}^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je dompelt een blokje onder: het water stijgt van \(40\) mL naar \(55\) mL. Het blokje weegt \(40{,}5\) g. Wat is de massadichtheid?",
        opties=[r"\(2{,}7\) g/\(\text{cm}^{3}\)", r"\(1{,}35\) g/\(\text{cm}^{3}\)", r"\(0{,}37\) g/\(\text{cm}^{3}\)"],
        antwoord=0,
        uitleg=r"Het volume is \(55 - 40 = 15\,\text{cm}^{3}\). Dan \(\rho = 40{,}5 : 15 = 2{,}7\) g/\(\text{cm}^{3}\), dus dit is waarschijnlijk aluminium.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een fles bevat \(2\) L olie met een massadichtheid van \(0{,}9\) g/\(\text{cm}^{3}\). Hoeveel weegt die olie?",
        opties=[r"\(1{,}8\) kg", r"\(0{,}45\) kg", r"\(18\) kg"],
        antwoord=0,
        uitleg=r"\(2\) L = \(2000\,\text{cm}^{3}\). \(m = \rho \cdot V = 0{,}9 \cdot 2000 = 1800\) g, dus \(1{,}8\) kg.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je meet van drie stukken van dezelfde stof: \(10\,\text{cm}^{3}\) weegt \(27\) g, \(20\,\text{cm}^{3}\) weegt \(54\) g, \(30\,\text{cm}^{3}\) weegt \(81\) g. Wat besluit je?",
        opties=[r"De massa is recht evenredig met het volume, en \(\rho = 2{,}7\) g/\(\text{cm}^{3}\)", r"De massa is omgekeerd evenredig met het volume, en \(\rho = 2{,}7\)", "Er is geen verband"],
        antwoord=0,
        uitleg=r"Telkens als het volume verdubbelt, verdubbelt de massa: recht evenredig. De verhouding m/V is overal \(2{,}7\), en dat is de massadichtheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zet massa (y) uit tegenover volume (x) voor één stof. Hoe ziet de grafiek eruit?",
        opties=[
            "Een rechte door de oorsprong",
            "Een dalende kromme",
            "Een horizontale rechte",
        ],
        antwoord=0,
        uitleg=r"Bij een recht evenredig verband krijg je een rechte door (\(0\), \(0\)). Hoe steiler die rechte, hoe groter de massadichtheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="In één grafiek staan twee rechten: stof A loopt steiler dan stof B. Wat weet je?",
        opties=[
            "Stof A heeft de grootste massadichtheid",
            "Stof B heeft de grootste massadichtheid",
            "Ze zijn even dicht",
        ],
        antwoord=0,
        uitleg="Bij hetzelfde volume heeft de steilste rechte de grootste massa, dus de grootste massadichtheid. Zo herken je op een grafiek welke stof welke is.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je bij dezelfde stof het volume verdubbelt, blijft de massa gelijk.",
        antwoord=False,
        uitleg=r"Niet juist. De massadichtheid is een stofconstante. Blijft \(\rho\) gelijk en wordt V twee keer zo groot, dan wordt \(m = \rho \times V\) ook twee keer zo groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een vaste massa: wat gebeurt er met de massadichtheid als het volume groter wordt?",
        opties=["Ze wordt kleiner: dezelfde massa in meer volume", "Ze wordt groter, want het volume staat in de teller", "Ze blijft gelijk, want het is een stofeigenschap"],
        antwoord=0,
        uitleg=r"\(\rho = m / V\). Blijft m gelijk en wordt V groter, dan wordt de uitkomst kleiner. Zo drijft een schip van staal: door zijn grote volume is de gemiddelde massadichtheid klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom drijft een ijsblokje op water?",
        opties=["IJs is minder dicht dan water", "IJs is kouder dan het water eromheen", "IJs heeft bijna geen massa meer"],
        antwoord=0,
        uitleg=r"Bij het bevriezen zet water uit: hetzelfde aantal deeltjes neemt meer plaats in. IJs weegt ongeveer \(0{,}92\) g/\(\text{cm}^{3}\), minder dan de \(1\) g/\(\text{cm}^{3}\) van water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over drijven en zinken kloppen?",
        opties=[
            "Een voorwerp drijft als zijn massadichtheid kleiner is dan die van de vloeistof",
            "Een voorwerp zinkt als zijn massadichtheid groter is dan die van de vloeistof",
            "Een luchtballon stijgt omdat de warme lucht erin minder dicht is dan de koude buitenlucht",
            "Een zwaar voorwerp zinkt altijd",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het gaat altijd om de vergelijking van de twee massadichtheden, niet om het gewicht op zich: een zware boomstam drijft en een klein muntstuk zinkt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een voorwerp met een massadichtheid van \(1200\) kg/\(\text{m}^{3}\) dat je in water legt, zal ___.",
        antwoord="zinken",
        uitleg=r"Water is \(1000\) kg/\(\text{m}^{3}\). Het voorwerp is dichter, dus het zinkt naar de bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom drijft een vetlaag bovenop de soep?",
        opties=["Vet is minder dicht dan water", "Vet is warmer dan de soep eromheen", "Vet lost niet op in water"],
        antwoord=0,
        uitleg=r"Vet en olie zijn ongeveer \(0{,}9\) g/\(\text{cm}^{3}\), minder dan water. Ze mengen niet met water en blijven daarom als laag bovenop liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een blokje heeft een massa van \(60\) g en een volume van \(75\,\text{cm}^{3}\). Drijft of zinkt het in water?",
        opties=[
            r"Het drijft, want \(\rho = 0{,}8\) g/\(\text{cm}^{3}\)",
            r"Het zinkt, want \(\rho = 1{,}25\) g/\(\text{cm}^{3}\)",
            r"Het zweeft, want \(\rho = 1\) g/\(\text{cm}^{3}\)",
        ],
        antwoord=0,
        uitleg=r"\(\rho = 60 : 75 = 0{,}8\) g/\(\text{cm}^{3}\). Dat is kleiner dan de \(1\) g/\(\text{cm}^{3}\) van water, dus het blokje drijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee voorwerpen met dezelfde massa hebben altijd dezelfde massadichtheid.",
        antwoord=False,
        uitleg="Een kilo veren en een kilo lood wegen even zwaar, maar de veren nemen veel meer plaats in. Je moet altijd massa én volume kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt twee even grote blokjes van dezelfde stof en je legt ze samen op de weegschaal. Wat verandert er?",
        opties=["Massa en volume verdubbelen, de massadichtheid niet", "De massadichtheid wordt twee keer zo groot", "De massadichtheid wordt de helft"],
        antwoord=0,
        uitleg="Massa en volume worden allebei twee keer zo groot, dus hun verhouding verandert niet. Massadichtheid hangt alleen van de stof af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke stappen bepaal je de massadichtheid van een onregelmatige steen?",
        opties=[
            "Weeg de steen",
            "Meet het volume door onderdompeling",
            "Deel de massa door het volume",
            "Meet de temperatuur van de steen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Massa wegen, volume bepalen en dan delen. De temperatuur heb je hier niet nodig.",
    ),
]
