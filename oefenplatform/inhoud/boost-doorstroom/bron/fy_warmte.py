# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Warmte, faseovergangen en de warmtebalans.

Hoort bij "warmteleer" van de vakfiche fysica 2de graad doorstroomfinaliteit,
een onderdeel van 10 % en daarmee één thema.

Deel 1 gaat over temperatuur en warmte: het verschil tussen de twee, de
inwendige energie, het thermisch evenwicht, de drie vormen van warmtetransport
(geleiding, convectie en straling), en de merkbare warmte met Q = c.m.ΔT en
Q = C.ΔT. Deel 2 gaat over de faseovergangen en de latente warmte Q = l.m: de
zes faseovergangen, het plateau in een smelt- of kookcurve, en de warmtebalans
waarin merkbare en latente warmte samen voorkomen.

De specifieke warmtecapaciteit van water, 4186 J/(kg.K), staat bij de
constanten van het examen. Alle andere waarden van c en l staan altijd bij de
opgave.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen temperatuur en warmte?",
        opties=[
            "temperatuur hoort bij de deeltjes, warmte is overgedragen energie",
            "temperatuur is zelf een energie en warmte is een soort kracht",
            "warmte hoort bij de massa en temperatuur bij het volume",
            "er is geen verschil, enkel een andere eenheid ervoor",
        ],
        antwoord=0,
        uitleg="De temperatuur zegt hoe snel de deeltjes gemiddeld bewegen. Warmte is de energie die van het warme naar het koude voorwerp stroomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor de warmtestroom tussen twee voorwerpen? Kruis alles aan wat juist is.",
        opties=[
            "ze gaat van het warme naar het koude voorwerp",
            "ze gaat van het koude naar het warme voorwerp",
            "ze stopt zodra beide dezelfde temperatuur hebben",
            "ze gaat van het zware naar het lichte voorwerp",
        ],
        antwoord=[0, 2],
        uitleg="Warmte stroomt altijd van hoge naar lage temperatuur, en stopt bij het thermisch evenwicht. De massa van de voorwerpen beslist daar niets over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van warmtetransport bestaan er?",
        opties=[
            "geleiding, convectie en straling",
            "geleiding, verdamping en straling",
            "convectie, straling en wrijving",
            "geleiding, convectie en smelten",
        ],
        antwoord=0,
        uitleg="Bij geleiding geven de deeltjes hun beweging aan elkaar door, bij convectie beweegt de warme stof zelf, en straling heeft geen stof nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan warmte van de zon ons bereiken door de lege ruimte?",
        opties=[
            "straling heeft geen stof nodig",
            "convectie werkt ook in het luchtledige",
            "geleiding werkt over elke afstand",
            "de ruimte geleidt warmte heel goed",
        ],
        antwoord=0,
        uitleg="Geleiding en convectie hebben deeltjes nodig, straling niet. Daarom warmt de zon de aarde op door een ruimte zonder lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de merkbare warmte van een stof?",
        opties=["Q = c . m . ΔT", "Q = l . m", "Q = c . m", "Q = m . ΔT"],
        antwoord=0,
        uitleg="De specifieke warmtecapaciteit maal de massa maal het temperatuursverschil. Q = l . m hoort bij een faseovergang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel warmte heb je nodig om 2,0 kg water 10 K op te warmen?",
        opties=["84 kJ", "8,4 kJ", "840 kJ", "21 kJ"],
        antwoord=0,
        uitleg="Q = 4186 . 2,0 . 10 = 83 720 J, dus ongeveer 84 kJ.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een grote specifieke warmtecapaciteit van een stof?",
        opties=[
            "één kilogram één kelvin opwarmen vraagt veel warmte",
            "de stof warmt bij dezelfde warmte heel snel op",
            "de stof heeft een hoog kookpunt en een hoog smeltpunt",
            "de stof geleidt de warmte heel goed door",
        ],
        antwoord=0,
        uitleg="Water heeft een grote c van 4186 J/(kg.K) en warmt dus traag op. Daarom blijft de zee lang koel in de lente en lang warm in de herfst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de warmtecapaciteit C en de specifieke warmtecapaciteit c?",
        opties=[
            "C hoort bij een voorwerp, c bij één kilogram stof",
            "C hoort bij één kilogram stof en c bij een voorwerp",
            "C wordt in joule gegeven en c in kelvin",
            "er is geen verschil behalve de letter zelf",
        ],
        antwoord=0,
        uitleg="C is de warmtecapaciteit van dat ene voorwerp, in J/K. De specifieke warmtecapaciteit c geldt per kilogram, in J/(kg.K).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de inwendige energie van een voorwerp zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze bestaat uit een kinetisch en een potentieel deel",
            "ze stijgt als de absolute temperatuur stijgt",
            "ze is gelijk aan nul bij een temperatuur van 0 °C",
            "ze hangt enkel van het volume van het voorwerp af",
        ],
        antwoord=[0, 1],
        uitleg="De deeltjes bewegen en trekken aan elkaar, dus zijn er twee delen. Een hogere absolute temperatuur betekent meer inwendige kinetische energie. Bij 0 °C is er nog altijd beweging, pas bij 0 K zou die stoppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over convectie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de warme stof beweegt zelf naar een andere plaats",
            "ze komt voor in vloeistoffen en gassen",
            "ze komt vooral voor in vaste stoffen",
            "ze heeft geen stof nodig",
        ],
        antwoord=[0, 1],
        uitleg="Warme lucht of warm water is lichter en stijgt, koude stof zakt. In een vaste stof kan de stof niet stromen, daar werkt geleiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp van 0,50 kg met c = 900 J/(kg.K) krijgt 9,0 kJ warmte. Hoeveel stijgt zijn temperatuur?",
        opties=["20 K", "2,0 K", "200 K", "4,5 K"],
        antwoord=0,
        uitleg="Uit ΔT = Q / (c . m) volgt 9000 / (900 . 0,50) = 20 K.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee voorwerpen in thermisch evenwicht hebben dezelfde temperatuur.",
        antwoord=True,
        uitleg="Daarom stroomt er geen warmte meer tussen die twee. Dat is het eindpunt van elke warmte-overdracht.",
    ),
    dict(
        type="waarofniet",
        vraag="De warmtebalans is een toepassing van de wet van behoud van energie.",
        antwoord=True,
        uitleg="De warmte die het warme voorwerp afgeeft, neemt het koude op. Niets verdwijnt, als je het vat goed isoleert.",
    ),
    dict(
        type="waarofniet",
        vraag="Een groot voorwerp heeft altijd een hogere temperatuur dan een klein voorwerp.",
        antwoord=False,
        uitleg="Temperatuur en hoeveelheid zijn twee verschillende dingen. Een kopje thee kan heter zijn dan een vol zwembad.",
    ),
    dict(
        type="waarofniet",
        vraag="Metaal en hout van dezelfde temperatuur voelen even koud aan.",
        antwoord=False,
        uitleg="Metaal geleidt de warmte van je hand snel weg, dus voelt het kouder. Hout geleidt slecht, dus blijft je hand daar warm.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een kleine specifieke warmtecapaciteit warmt traag op.",
        antwoord=False,
        uitleg="Een kleine c betekent dat er weinig warmte nodig is per kelvin, dus warmt de stof juist snel op. Een pan van metaal is sneller heet dan het water erin.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor warmte?",
        antwoord=["Q"],
        uitleg="Q, met als eenheid de joule. Dezelfde letter staat ook voor elektrische lading, dus let op de context.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de specifieke warmtecapaciteit van water? Schrijf het getal in J/(kg.K).",
        antwoord=["4186", "4186 J/kg.K", "4180"],
        uitleg="4186 J/(kg.K). Die waarde staat bij de constanten van het examen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het meettoestel waarin je een warmtebalans opmeet?",
        antwoord=["calorimeter", "een calorimeter", "joulevat"],
        uitleg="Een calorimeter of joulevat. Het is goed geïsoleerd zodat er geen warmte naar de kamer verdwijnt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel warmte heb je nodig om 1,0 kg water 1,0 K op te warmen? Schrijf het getal in joule.",
        antwoord=["4186", "4186 J", "4180"],
        uitleg="Q = 4186 . 1,0 . 1,0 = 4186 J. Dat is net de betekenis van de specifieke warmtecapaciteit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de overgang van vast naar vloeibaar?",
        opties=["smelten", "stollen", "verdampen", "sublimeren"],
        antwoord=0,
        uitleg="Smelten gaat van vast naar vloeibaar. Stollen is de omgekeerde weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de overgang van vast rechtstreeks naar gas?",
        opties=["sublimeren", "desublimeren", "verdampen", "condenseren"],
        antwoord=0,
        uitleg="Sublimeren slaat de vloeibare fase over. Droogijs doet dat, en rijp op een auto verdwijnt zo ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de latente warmte bij een faseovergang?",
        opties=["Q = l . m", "Q = c . m . ΔT", "Q = C . ΔT", "Q = l . ΔT"],
        antwoord=0,
        uitleg="De specifieke faseovergangswarmte maal de massa. Er staat geen ΔT in, want de temperatuur verandert tijdens de overgang niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de temperatuur van ijs van 0 °C terwijl het smelt?",
        opties=[
            "ze blijft 0 °C",
            "ze stijgt gelijkmatig",
            "ze daalt eerst",
            "ze stijgt tot 100 °C",
        ],
        antwoord=0,
        uitleg="Alle toegevoerde warmte gaat naar het losmaken van de deeltjes, niet naar hun beweging. In een grafiek geeft dat een plateau.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een horizontaal stuk in een opwarmingscurve van een stof?",
        opties=[
            "er gebeurt een faseovergang",
            "de stof krijgt geen warmte meer",
            "de stof koelt af",
            "de massa van de stof daalt",
        ],
        antwoord=0,
        uitleg="De warmte blijft toestromen, maar gaat volledig naar de faseovergang. Daarom blijft de temperatuur even gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel warmte heb je nodig om 0,20 kg ijs van 0 °C te smelten, met ls = 334 kJ/kg?",
        opties=["67 kJ", "6,7 kJ", "670 kJ", "1670 kJ"],
        antwoord=0,
        uitleg="Q = l . m = 334 000 . 0,20 = 66 800 J, dus ongeveer 67 kJ.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom voelt verdampende alcohol op je hand koud aan?",
        opties=[
            "de alcohol neemt warmte van je hand om te verdampen",
            "de alcohol in het flesje is kouder dan je hand",
            "de alcohol geeft bij het verdampen warmte af aan je hand",
            "de alcohol geleidt de warmte van je hand slecht",
        ],
        antwoord=0,
        uitleg="Een faseovergang van vloeibaar naar gas vraagt latente warmte, en die haalt de alcohol uit je hand. Zweten werkt op dezelfde manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de deeltjes tijdens het smelten zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de cohesiekrachten tussen de deeltjes worden losser",
            "de inwendige potentiële energie stijgt",
            "de deeltjes gaan sneller bewegen",
            "de temperatuur stijgt gelijkmatig",
        ],
        antwoord=[0, 1],
        uitleg="De energie gaat naar het losmaken van de deeltjes uit hun vast verband, dus naar de inwendige potentiële energie. Hun gemiddelde snelheid, en dus de temperatuur, blijft gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke faseovergangen geven warmte af aan de omgeving? Kruis alles aan wat juist is.",
        opties=["stollen", "condenseren", "smelten", "verdampen"],
        antwoord=[0, 1],
        uitleg="Stollen en condenseren gaan naar een meer gebonden toestand, dus komt er energie vrij. Smelten en verdampen hebben juist warmte nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je giet 0,10 kg water van 80 °C bij 0,10 kg water van 20 °C in een geïsoleerd vat. Welke eindtemperatuur krijg je?",
        opties=["50 °C", "60 °C", "40 °C", "100 °C"],
        antwoord=0,
        uitleg="Dezelfde massa van dezelfde stof, dus de eindtemperatuur ligt precies in het midden: (80 + 20) / 2 = 50 °C. De warmte die het warme water afgeeft, neemt het koude op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de temperatuur waarbij een stof van vloeibaar naar gas overgaat bij normale luchtdruk?",
        opties=["het kookpunt", "het smeltpunt", "het sublimatiepunt", "het absolute nulpunt"],
        antwoord=0,
        uitleg="Het kookpunt. Voor water is dat 100 °C bij een druk van 1013 hPa.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens een faseovergang blijft de temperatuur van de stof gelijk.",
        antwoord=True,
        uitleg="Alle warmte gaat naar het veranderen van de fase, niet naar de beweging van de deeltjes. Daarom zie je een plateau in de curve.",
    ),
    dict(
        type="waarofniet",
        vraag="De specifieke smeltwarmte van een stof is een heel ander getal dan haar specifieke stolwarmte.",
        antwoord=False,
        uitleg="Het is dezelfde waarde: wat je bij het smelten moet toevoegen, komt bij het stollen weer vrij. Enkel de zin van de warmtestroom is omgekeerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Water kan enkel verdampen bij 100 °C.",
        antwoord=False,
        uitleg="Verdampen gebeurt aan het oppervlak bij elke temperatuur, zoals natte was die droogt. Bij 100 °C begint water te koken, dus ook van binnenuit te verdampen.",
    ),
    dict(
        type="waarofniet",
        vraag="Om 1 kg water te laten verdampen heb je minder warmte nodig dan om het van 0 °C tot 100 °C op te warmen.",
        antwoord=False,
        uitleg="Opwarmen van 0 naar 100 °C kost ongeveer 419 kJ, verdampen ongeveer 2260 kJ. Verdampen kost dus veel méér.",
    ),
    dict(
        type="waarofniet",
        vraag="Rijp die verdwijnt zonder eerst te smelten, is een voorbeeld van sublimeren.",
        antwoord=True,
        uitleg="Het ijs gaat rechtstreeks over in waterdamp. Dat heet sublimeren; de omgekeerde weg heet desublimeren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de overgang van gas naar vloeibaar?",
        antwoord=["condenseren", "condensatie", "condenseert"],
        uitleg="Condenseren. Daarbij komt latente warmte vrij, zoals op een koude ruit in de winter.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor de specifieke smeltwarmte?",
        antwoord=["ls", "l_s", "l s"],
        uitleg="ls, met als eenheid J/kg. De specifieke verdampingswarmte krijgt lv.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel warmte heb je nodig om 0,50 kg van een stof te smelten, met ls = 200 kJ/kg? Schrijf het getal in kJ.",
        antwoord=["100", "100 kJ"],
        uitleg="Q = l . m = 200 . 0,50 = 100 kJ.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de warmte die bij een faseovergang hoort, zonder dat de temperatuur verandert? Schrijf het woord bij warmte.",
        antwoord=["latente", "latent", "latente warmte"],
        uitleg="De latente warmte. Verandert de temperatuur wel, dan heet het merkbare warmte.",
    ),
]
