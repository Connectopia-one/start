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
        opties=["ρ = m / V", "ρ = m × V", "ρ = V / m"],
        antwoord=0,
        uitleg="Je deelt de massa door het volume. Het symbool ρ (rho) is de Griekse letter voor massadichtheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp heeft een massa van 300 g en een volume van 100 cm³. Wat is de massadichtheid?",
        opties=["3 g/cm³", "30 g/cm³", "0,3 g/cm³"],
        antwoord=0,
        uitleg="ρ = m / V = 300 g / 100 cm³ = 3 g/cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het volume van een kubus met een ribbe van 2 cm?",
        opties=["8 cm³", "6 cm³", "4 cm³"],
        antwoord=0,
        uitleg="V van een kubus = z³ = 2 × 2 × 2 = 8 cm³.",
    ),
    dict(
        type="invultekst",
        vraag="Een balk van 5 cm op 4 cm op 2 cm heeft een volume van ___ cm³.",
        antwoord="40",
        uitleg="V van een balk = l × b × h = 5 × 4 × 2 = 40 cm³.",
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
        vraag="Het water in een maatcilinder staat op 50 mL. Je laat er een moer in zakken en het staat op 65 mL. Wat is het volume van de moer?",
        opties=["15 cm³", "65 cm³", "50 cm³"],
        antwoord=0,
        uitleg="65 mL − 50 mL = 15 mL, en 1 mL is precies 1 cm³. Het volume van de moer is dus 15 cm³.",
    ),
    dict(
        type="invultekst",
        vraag="1 liter is evenveel als ___ cm³.",
        antwoord="1000",
        uitleg="1 L = 1 dm³ = 1000 cm³. En 1 mL = 1 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kubieke meter is 2 liter?",
        opties=["0,002 m³", "0,2 m³", "2000 m³"],
        antwoord=0,
        uitleg="1 m³ = 1000 L, dus 1 L = 0,001 m³. Twee liter is dan 0,002 m³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel liter gaat er in 0,5 m³?",
        opties=["500 L", "50 L", "5000 L"],
        antwoord=0,
        uitleg="1 m³ = 1000 L, dus 0,5 m³ = 0,5 × 1000 = 500 L.",
    ),
    dict(
        type="meerkeuze",
        vraag="Water heeft een massadichtheid van 1 g/cm³. Hoeveel is dat in kg/m³?",
        opties=["1000 kg/m³", "100 kg/m³", "1 kg/m³"],
        antwoord=0,
        uitleg="Van g/cm³ naar kg/m³ vermenigvuldig je met 1000. Eén liter water weegt dan ook precies 1 kg.",
    ),
    dict(
        type="invultekst",
        vraag="Aluminium heeft een massadichtheid van 2700 kg/m³. In g/cm³ is dat ___.",
        antwoord="2,7",
        uitleg="Van kg/m³ naar g/cm³ deel je door 1000: 2700 : 1000 = 2,7 g/cm³.",
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
        opties=["kg/m³", "g/cm³", "kg"],
        antwoord=0,
        uitleg="De SI-eenheid is kilogram per kubieke meter. g/cm³ mag ook, maar dat is geen SI-eenheid.",
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
        vraag="Welke van deze zinken in water (1 g/cm³)?",
        opties=[
            "IJzer, 7,8 g/cm³",
            "Aluminium, 2,7 g/cm³",
            "Kurk, 0,24 g/cm³",
            "Olie, 0,9 g/cm³",
        ],
        antwoord=[0, 1],
        uitleg="Alles met een massadichtheid groter dan 1 g/cm³ zinkt in water. Kurk en olie zijn lichter per cm³ en blijven drijven.",
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
        vraag="Een blok heeft een massa van 72 g en is een kubus met een ribbe van 2 cm. Wat is de massadichtheid?",
        opties=["9 g/cm³", "36 g/cm³", "144 g/cm³"],
        antwoord=0,
        uitleg="Eerst het volume: z³ = 2³ = 8 cm³. Dan ρ = 72 g / 8 cm³ = 9 g/cm³. Dat komt aardig in de buurt van koper.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel weegt 3 cm³ goud, als goud 19 g/cm³ weegt per kubieke centimeter?",
        opties=["57 g", "22 g", "6,3 g"],
        antwoord=0,
        uitleg="Uit ρ = m / V volgt m = ρ × V = 19 × 3 = 57 g.",
    ),
    dict(
        type="invultekst",
        vraag="IJzer heeft een massadichtheid van 7,8 g/cm³. Een stuk van 780 g heeft een volume van ___ cm³.",
        antwoord="100",
        uitleg="Uit ρ = m / V volgt V = m / ρ = 780 : 7,8 = 100 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het volume van een cilinder met een straal van 2 cm en een hoogte van 10 cm? Reken met π ≈ 3,14.",
        opties=["125,6 cm³", "62,8 cm³", "40 cm³"],
        antwoord=0,
        uitleg="V = π × r² × h = 3,14 × 2² × 10 = 3,14 × 4 × 10 = 125,6 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het volume van een bol met een straal van 3 cm? Reken met π ≈ 3,14.",
        opties=["113,04 cm³", "37,68 cm³", "28,26 cm³"],
        antwoord=0,
        uitleg="V = 4/3 × π × r³ = 4/3 × 3,14 × 27 = 113,04 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je dompelt een blokje onder: het water stijgt van 40 mL naar 55 mL. Het blokje weegt 40,5 g. Wat is de massadichtheid?",
        opties=["2,7 g/cm³", "1,35 g/cm³", "0,37 g/cm³"],
        antwoord=0,
        uitleg="Het volume is 55 − 40 = 15 cm³. Dan ρ = 40,5 : 15 = 2,7 g/cm³, dus dit is waarschijnlijk aluminium.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fles bevat 2 L olie met een massadichtheid van 0,9 g/cm³. Hoeveel weegt die olie?",
        opties=["1,8 kg", "0,45 kg", "18 kg"],
        antwoord=0,
        uitleg="2 L = 2000 cm³. m = ρ × V = 0,9 × 2000 = 1800 g, dus 1,8 kg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet van drie stukken van dezelfde stof: 10 cm³ weegt 27 g, 20 cm³ weegt 54 g, 30 cm³ weegt 81 g. Wat besluit je?",
        opties=["De massa is recht evenredig met het volume, en ρ = 2,7 g/cm³", "De massa is omgekeerd evenredig met het volume, en ρ = 2,7", "Er is geen verband"],
        antwoord=0,
        uitleg="Telkens als het volume verdubbelt, verdubbelt de massa: recht evenredig. De verhouding m/V is overal 2,7, en dat is de massadichtheid.",
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
        uitleg="Bij een recht evenredig verband krijg je een rechte door (0, 0). Hoe steiler die rechte, hoe groter de massadichtheid.",
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
        uitleg="Niet juist. De massadichtheid is een stofconstante. Blijft ρ gelijk en wordt V twee keer zo groot, dan wordt m = ρ × V ook twee keer zo groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een vaste massa: wat gebeurt er met de massadichtheid als het volume groter wordt?",
        opties=["Ze wordt kleiner: dezelfde massa in meer volume", "Ze wordt groter, want het volume staat in de teller", "Ze blijft gelijk, want het is een stofeigenschap"],
        antwoord=0,
        uitleg="ρ = m / V. Blijft m gelijk en wordt V groter, dan wordt de uitkomst kleiner. Zo drijft een schip van staal: door zijn grote volume is de gemiddelde massadichtheid klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom drijft een ijsblokje op water?",
        opties=["IJs is minder dicht dan water", "IJs is kouder dan het water eromheen", "IJs heeft bijna geen massa meer"],
        antwoord=0,
        uitleg="Bij het bevriezen zet water uit: hetzelfde aantal deeltjes neemt meer plaats in. IJs weegt ongeveer 0,92 g/cm³, minder dan de 1 g/cm³ van water.",
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
        vraag="Een voorwerp met een massadichtheid van 1200 kg/m³ dat je in water legt, zal ___.",
        antwoord="zinken",
        uitleg="Water is 1000 kg/m³. Het voorwerp is dichter, dus het zinkt naar de bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom drijft een vetlaag bovenop de soep?",
        opties=["Vet is minder dicht dan water", "Vet is warmer dan de soep eromheen", "Vet lost niet op in water"],
        antwoord=0,
        uitleg="Vet en olie zijn ongeveer 0,9 g/cm³, minder dan water. Ze mengen niet met water en blijven daarom als laag bovenop liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een blokje heeft een massa van 60 g en een volume van 75 cm³. Drijft of zinkt het in water?",
        opties=[
            "Het drijft, want ρ = 0,8 g/cm³",
            "Het zinkt, want ρ = 1,25 g/cm³",
            "Het zweeft, want ρ = 1 g/cm³",
        ],
        antwoord=0,
        uitleg="ρ = 60 : 75 = 0,8 g/cm³. Dat is kleiner dan de 1 g/cm³ van water, dus het blokje drijft.",
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
