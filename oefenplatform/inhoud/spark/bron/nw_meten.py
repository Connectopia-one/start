# -*- coding: utf-8 -*-
"""De vragen voor "Veilig werken, meten en eenheden" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel Onderzoek: veilig en duurzaam werken met stoffen,
organismen en technische systemen; de juiste meetinstrumenten en hulpmiddelen
kiezen en nauwkeurig aflezen; en grootheden, eenheden en symbolen correct
gebruiken, met de voorvoegsels van milli tot kilo en de omzettingen tussen de
SI-eenheden en de andere eenheden.

De tabel met grootheden, eenheden en meetinstrumenten staat in bijlage 1 van de
vakfiche. Die bijlage mag je níet gebruiken op het examen, dus ze moet je kennen.

Deel 1 gaat over veilig werken en over welk instrument bij welke grootheid
hoort. Deel 2 gaat over nauwkeurigheid, symbolen, voorvoegsels en omzetten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je morst een product op de werktafel. Wat doe je?",
        opties=[
            "Je kuist het onmiddellijk op",
            "Je laat het staan tot het les gedaan is",
            "Je veegt het op de grond",
        ],
        antwoord=0,
        uitleg="Gemorste producten ruim je meteen op. Zo kan niemand uitglijden of ermee in contact komen, en blijft je meting zuiver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij veilig en duurzaam werken?",
        opties=[
            "Meetinstrumenten uitschakelen als je niet meet",
            "Zuinig omspringen met chemische stoffen",
            "Biologisch afval correct sorteren",
            "Elektrische toestellen met natte handen bedienen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie sparen energie, materiaal en milieu. Natte handen en elektriciteit gaan nooit samen: dat is net gevaarlijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Glasscherven veeg je het best met je blote handen bij elkaar.",
        antwoord=False,
        uitleg="Glas ruim je op met een borstel en een blik, nooit met je handen. Glaswerk behandel je voorzichtig en maak je na gebruik schoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je de handleiding van een toestel voor je het gebruikt?",
        opties=[
            "Om te weten hoe je het veilig en juist bedient",
            "Omdat dat verplicht is bij elk examen",
            "Om te weten wat het kost",
        ],
        antwoord=0,
        uitleg="Onderhoudsvoorschriften, handleidingen en werktekeningen juist interpreteren hoort bij veilig werken. Zo gaat het toestel ook langer mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je de massa van een stof?",
        opties=["Met een weegschaal", "Met een maatcilinder", "Met een hygrometer"],
        antwoord=0,
        uitleg="Massa meet je met een weegschaal, in gram of kilogram. Een maatcilinder meet volume en een hygrometer de luchtvochtigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je het volume van een vloeistof?",
        opties=["Met een maatcilinder", "Met een meetlat", "Met een dynamometer"],
        antwoord=0,
        uitleg="Je giet de vloeistof in een maatcilinder en leest het volume af in milliliter, en 1 mL is 1 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instrumenten meten een lengte of een afstand?",
        opties=["Een meetlat", "Een rolmeter", "Een schuifmaat", "Een chronometer"],
        antwoord=[0, 1, 2],
        uitleg="Meetlat, rolmeter, vouwmeter, schuifmaat en micrometer meten lengte. Een chronometer meet tijdsduur.",
    ),
    dict(
        type="invultekst",
        vraag="Een tijdsduur meet je met een ___.",
        antwoord=["chronometer", "stopwatch", "klok"],
        uitleg="Een chronometer of een klok meet tijd, in seconden. Het symbool van tijdsduur is Δt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je de geluidssterkte?",
        opties=["Met een geluidsmeter", "Met een lichtmeter", "Met een anemometer"],
        antwoord=0,
        uitleg="De geluidssterkte krijgt het symbool L en meet je in decibel (dB) met een geluidsmeter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je de verlichtingssterkte?",
        opties=["Met een lichtmeter", "Met een hygrometer", "Met een thermometer"],
        antwoord=0,
        uitleg="Verlichtingssterkte heeft het symbool E en de eenheid lux (lx). Je meet ze met een lichtmeter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee bepaal je de bodemhardheid in een biotoop?",
        opties=[
            "Met een valpen met plastic buis",
            "Met een weegschaal",
            "Met een lichtmeter",
        ],
        antwoord=0,
        uitleg="Je laat een pen door een buis op de bodem vallen en kijkt hoe diep hij gaat. Hoe minder diep, hoe harder de bodem.",
    ),
    dict(
        type="invultekst",
        vraag="De SI-eenheid van lengte is de ___.",
        antwoord="meter",
        uitleg="De meter (m) is de SI-eenheid van lengte, afstand en verplaatsing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van massa?",
        opties=["De kilogram", "De gram", "De ton"],
        antwoord=0,
        uitleg="De kilogram (kg) is de SI-eenheid. De ton is een niet-SI-eenheid: 1 t = 1000 kg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheden horen bij volume?",
        opties=["m³", "liter", "kg", "newton"],
        antwoord=[0, 1],
        uitleg="De SI-eenheid van volume is de kubieke meter; de liter is de gebruikelijke niet-SI-eenheid. Kilogram hoort bij massa en newton bij kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel meter is 2 km?",
        opties=["2000 m", "200 m", "20 000 m"],
        antwoord=0,
        uitleg="Kilo betekent duizend, dus 1 km = 1000 m en 2 km = 2000 m.",
    ),
    dict(
        type="invultekst",
        vraag="500 g is ___ kg.",
        antwoord="0,5",
        uitleg="1 kg = 1000 g, dus 500 g is een halve kilogram: 0,5 kg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel liter is 250 mL?",
        opties=["0,25 L", "2,5 L", "25 L"],
        antwoord=0,
        uitleg="Milli betekent duizendste, dus 1 mL = 0,001 L en 250 mL = 0,25 L.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorvoegsel milli betekent duizendste.",
        antwoord=True,
        uitleg="Milli is 0,001, centi is 0,01, deci is 0,1 en kilo is 1000. Die vier moet je vlot kunnen gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool hoort bij de grootheid snelheid?",
        opties=["v", "V", "F"],
        antwoord=0,
        uitleg="De kleine letter v staat voor snelheid, de hoofdletter V voor volume en F voor kracht. Hoofdletters en kleine letters betekenen dus iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hulpmiddel gebruik je om een cel te bekijken?",
        opties=["Een lichtmicroscoop", "Een loep", "Een verrekijker"],
        antwoord=0,
        uitleg="Kies je hulpmiddel naar de vergroting die je nodig hebt: een loep voor een insect, een binoculair voor wat detail, een lichtmicroscoop voor cellen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je moet 25 mL water afmeten. Welk instrument kies je?",
        opties=[
            "Een maatcilinder van 50 mL met streepjes van 1 mL",
            "Een emmer van 10 L",
            "Een maatcilinder van 1 L met streepjes van 50 mL",
        ],
        antwoord=0,
        uitleg="Kies uit gelijksoortige instrumenten dat met de gepaste nauwkeurigheid: het kleinste instrument waar je hoeveelheid nog in past, geeft de fijnste verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lees je een maatcilinder correct af?",
        opties=["Met je oog op de onderkant van de holle bolling", "Van bovenaf, schuin naar beneden kijkend", "Terwijl je de cilinder schuin houdt"],
        antwoord=0,
        uitleg="De vloeistof staat hol in het glas. Lees af aan de onderkant van die holling, met de cilinder recht en je oog op dezelfde hoogte, anders kijk je ernaast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geef je bij een meting altijd de eenheid mee?",
        opties=["Zonder eenheid betekent het getal niets", "Omdat de eenheid het getal groter maakt", "Omdat het netter staat"],
        antwoord=0,
        uitleg="5 kan 5 gram of 5 kilogram zijn. Pas met de eenheid erbij is een meting ondubbelzinnig, en pas dan kan iemand anders ze gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over grootheden en eenheden kloppen?",
        opties=[
            "Kracht heeft het symbool F en de eenheid newton",
            "Massadichtheid heeft het symbool ρ en de SI-eenheid kg/m³",
            "Temperatuur heeft de SI-eenheid kelvin",
            "Volume heeft de SI-eenheid liter",
        ],
        antwoord=[0, 1, 2],
        uitleg="De SI-eenheid van volume is de kubieke meter; de liter is de niet-SI-eenheid. De drie andere staan zo in de tabel van de vakfiche.",
    ),
    dict(
        type="invultekst",
        vraag="Het symbool van de grootheid massadichtheid is de Griekse letter ___.",
        antwoord=["rho", "ρ"],
        uitleg="Massadichtheid schrijf je als ρ, uitgesproken als rho. De eenheid is kg/m³ of g/cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 3 mm in meter?",
        opties=["0,003 m", "0,3 m", "300 m"],
        antwoord=0,
        uitleg="Milli is duizendste: 3 mm = 3 × 0,001 m = 0,003 m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel gram is 1,5 kg?",
        opties=["1500 g", "150 g", "15 000 g"],
        antwoord=0,
        uitleg="1 kg = 1000 g, dus 1,5 kg = 1500 g.",
    ),
    dict(
        type="invultekst",
        vraag="75 cm is ___ m.",
        antwoord="0,75",
        uitleg="Centi is honderdste: 75 cm = 75 : 100 = 0,75 m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke schatting van de massa van een appel is realistisch?",
        opties=["Ongeveer 150 g", "Ongeveer 15 g", "Ongeveer 1,5 kg"],
        antwoord=0,
        uitleg="Een schatting maken hoort bij wetenschappelijk werken: kom je op een antwoord van 15 g of 1,5 kg uit, dan weet je meteen dat je je ergens vergist hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling meet de lengte van zijn tafel en schrijft op: 1,2. Wat ontbreekt er?",
        opties=["De eenheid", "De grootheid mag niet vermeld worden", "Het meetinstrument"],
        antwoord=0,
        uitleg="1,2 wat? Meter waarschijnlijk, maar dat moet er staan. Een meetresultaat is een getal én een eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instrumenten zou je gebruiken bij een veldwerk over een vijver?",
        opties=[
            "Een thermometer voor de watertemperatuur",
            "Een lichtmeter voor de verlichtingssterkte",
            "Een determineertabel voor de waterdiertjes",
            "Een dynamometer voor de waterdiepte",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie passen bij wat je wil weten. Een dynamometer meet kracht en zegt niets over diepte; daarvoor gebruik je een meetlat of een peilstok.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schuifmaat meet nauwkeuriger dan een gewone meetlat.",
        antwoord=True,
        uitleg="Met een schuifmaat lees je tienden van een millimeter af, met een meetlat alleen hele millimeters. Kies altijd het instrument dat nauwkeurig genoeg is voor je onderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schakel je een meettoestel uit als je even niet meet?",
        opties=[
            "Om energie te sparen en de batterij te sparen",
            "Omdat het anders verkeerd meet",
            "Omdat het dan sneller werkt",
        ],
        antwoord=0,
        uitleg="Duurzaam werken is ook zuinig werken met energie en materiaal. Het toestel gaat er bovendien langer mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je werkt met levend materiaal uit een vijver. Wat doe je achteraf?",
        opties=[
            "Je zet de diertjes terug en maakt je materiaal proper",
            "Je giet alles in de gootsteen",
            "Je laat het staan tot volgende week",
        ],
        antwoord=0,
        uitleg="Hygiënisch omgaan met biologisch materiaal en het correct sorteren hoort bij veilig en duurzaam werken. Levend materiaal zet je terug waar je het haalde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheid meet je in decibel?",
        opties=["De geluidssterkte", "De verlichtingssterkte", "De luchtvochtigheid"],
        antwoord=0,
        uitleg="Decibel (dB) hoort bij geluidssterkte. Verlichtingssterkte meet je in lux en de relatieve luchtvochtigheid in procent.",
    ),
    dict(
        type="invultekst",
        vraag="De relatieve luchtvochtigheid druk je uit in ___.",
        antwoord=["procent", "%", "percent"],
        uitleg="De relatieve luchtvochtigheid krijgt het symbool φ en wordt in procent (%) gegeven. Je meet ze met een hygrometer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je weegt een leeg bekerglas (120 g) en daarna hetzelfde glas met water (370 g). Hoeveel water zit erin?",
        opties=["250 g", "490 g", "370 g"],
        antwoord=0,
        uitleg="370 − 120 = 250 g. Je weegt eerst het lege glas, want de weegschaal weegt alles wat erop staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het gebruik van een bunsenbrander kloppen?",
        opties=[
            "Je bindt lang haar samen",
            "Je laat de brander nooit onbewaakt branden",
            "Je zet er brandbare stoffen naast om ze op te warmen",
            "Je draait de gastoevoer dicht als je klaar bent",
        ],
        antwoord=[0, 1, 3],
        uitleg="Haar samen, nooit onbewaakt en achteraf dichtdraaien. Brandbare stoffen horen net zo ver mogelijk van een open vlam.",
    ),
    dict(
        type="waarofniet",
        vraag="De graad Celsius is de SI-eenheid van temperatuur.",
        antwoord=False,
        uitleg="Niet juist. De SI-eenheid is de kelvin (K). In de dagelijkse praktijk gebruiken we graden Celsius (°C), maar dat is een niet-SI-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet dezelfde lengte drie keer en krijgt 12,4 cm, 12,5 cm en 12,4 cm. Wat doe je met die resultaten?",
        opties=[
            "Je neemt het gemiddelde, want herhalen maakt een meting betrouwbaarder",
            "Je neemt de grootste waarde",
            "Je neemt de eerste meting",
        ],
        antwoord=0,
        uitleg="Meerdere keren meten en het gemiddelde nemen vangt kleine afleesfouten op. Dat hoort bij nauwkeurig wetenschappelijk werken.",
    ),
]
