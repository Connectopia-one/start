# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Archimedeskracht, moment en evenwicht.

Hoort bij "beweging - krachten" van de vakfiche fysica 2de graad
doorstroomfinaliteit, het vijfde en laatste thema voor dat onderdeel van 35 %.

Deel 1 gaat over de archimedeskracht: FA = ρ.g.Vond, de invloed van de
massadichtheid van de vloeistof en van het ondergedompelde volume, en het
verschil tussen zinken, zweven, stijgen en drijven via de krachtenbalans.
Deel 2 gaat over het moment van een kracht, M = F.d.sin α, en over het statisch
evenwicht: de krachtenbalans voor het translatie-evenwicht en de
krachtmomentenbalans voor het rotatie-evenwicht.

De massadichtheid van water, 1000 kg/m³, staat bij de constanten van het
examen. Andere massadichtheden staan altijd bij de opgave.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de archimedeskracht op een voorwerp in een vloeistof?",
        opties=[
            "FA = ρ . g . Vond",
            "FA = m . g",
            "FA = ρ . g . h",
            "FA = ρ . Vond",
        ],
        antwoord=0,
        uitleg="De massadichtheid van de vloeistof maal de zwaarteveldsterkte maal het ondergedompelde volume. ρ.g.h is de formule voor de hydrostatische druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de archimedeskracht op een voorwerp af? Kruis alles aan wat juist is.",
        opties=[
            "de massadichtheid van de vloeistof",
            "het ondergedompelde volume",
            "de massa van het voorwerp",
            "de vorm van het voorwerp",
        ],
        antwoord=[0, 1],
        uitleg="Enkel de vloeistof, de zwaarteveldsterkte en het volume dat onder water zit, tellen mee. Twee voorwerpen van hetzelfde volume ondervinden dezelfde archimedeskracht, ook als de ene veel zwaarder is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe is de archimedeskracht gericht?",
        opties=["verticaal naar boven", "verticaal naar beneden", "horizontaal", "langs het oppervlak"],
        antwoord=0,
        uitleg="De archimedeskracht duwt het voorwerp omhoog. Daarom lijkt een steen onder water lichter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp zweeft in een vloeistof. Wat geldt?",
        opties=[
            "de archimedeskracht is even groot als de zwaartekracht",
            "de archimedeskracht is groter dan de zwaartekracht",
            "de archimedeskracht is kleiner dan de zwaartekracht",
            "de archimedeskracht is nul",
        ],
        antwoord=0,
        uitleg="Bij zweven blijft het voorwerp op dezelfde diepte hangen, dus is de resulterende kracht nul. De massadichtheid van het voorwerp is dan gelijk aan die van de vloeistof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp met een massadichtheid van 1200 kg/m³ wordt in water gelegd. Wat gebeurt er?",
        opties=["het zinkt", "het drijft", "het zweeft", "het stijgt naar boven"],
        antwoord=0,
        uitleg="De massadichtheid is groter dan die van water, 1000 kg/m³, dus de zwaartekracht haalt het van de archimedeskracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de archimedeskracht op een blok dat volledig onder water zit, met een volume van 0,0020 m³?",
        opties=["19,6 N", "2,0 N", "196 N", "1962 N"],
        antwoord=0,
        uitleg="FA = 1000 . 9,81 . 0,0020 = 19,62 N, dus 19,6 N.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een blok drijft met driekwart van zijn volume onder water. Welk volume gebruik je in de formule van de archimedeskracht?",
        opties=[
            "driekwart van het volume van het blok",
            "het hele volume van het blok",
            "een kwart van het volume van het blok",
            "het volume van het hele bad",
        ],
        antwoord=0,
        uitleg="Enkel het ondergedompelde volume duwt water weg, dus enkel dat deel levert archimedeskracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom drijft een zwaar stalen schip, terwijl een stalen bout zinkt?",
        opties=[
            "het schip is hol, dus is zijn gemiddelde massadichtheid kleiner",
            "staal drijft altijd, zolang het stuk maar groot genoeg is",
            "op een schip op zee werkt de zwaartekracht niet meer",
            "de archimedeskracht hangt af van de massa van het schip",
        ],
        antwoord=0,
        uitleg="Een schip duwt veel water weg omdat het binnenin vol lucht zit. Zijn gemiddelde massadichtheid komt daardoor onder 1000 kg/m³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt hetzelfde voorwerp eerst in water en daarna in zout water, dat een grotere massadichtheid heeft. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "bij hetzelfde ondergedompelde volume is de archimedeskracht groter",
            "er zit een kleiner deel van het voorwerp onder water",
            "de zwaartekracht op het voorwerp wordt eveneens groter",
            "het voorwerp wordt in zout water zelf ook zwaarder",
        ],
        antwoord=[0, 1],
        uitleg="Een grotere ρ geeft bij hetzelfde volume meer archimedeskracht, dus het voorwerp hoeft minder diep te zakken om zijn gewicht te dragen. De zwaartekracht hangt enkel van de massa af en verandert niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een duikboot wil zinken. Wat doet ze?",
        opties=[
            "water in haar tanks laten om zwaarder te worden",
            "haar tanks juist met lucht vullen en leegblazen",
            "haar volume groter maken zonder zwaarder te worden",
            "sneller vooruit varen met haar schroeven",
        ],
        antwoord=0,
        uitleg="Water in de tanks vergroot de massa en dus de zwaartekracht, terwijl het volume gelijk blijft. Dan haalt de zwaartekracht het van de archimedeskracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een steen van 50 N hangt aan een dynamometer en wordt in water gedompeld. De dynamometer wijst 32 N aan. Hoe groot is de archimedeskracht?",
        opties=["18 N", "82 N", "32 N", "50 N"],
        antwoord=0,
        uitleg="De dynamometer meet wat er na de archimedeskracht overblijft: 50 − 32 = 18 N.",
    ),
    dict(
        type="waarofniet",
        vraag="De archimedeskracht is even groot als de zwaartekracht op de weggeduwde vloeistof.",
        antwoord=True,
        uitleg="Dat is de wet van Archimedes. Daarom staat de massadichtheid van de vloeistof in de formule en niet die van het voorwerp.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp dat drijft, ondervindt een archimedeskracht die even groot is als zijn eigen zwaartekracht.",
        antwoord=True,
        uitleg="Bij drijven ligt het voorwerp stil, dus is de resulterende kracht nul. Het zakt net zo diep tot de twee krachten elkaar opheffen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe dieper een voorwerp dat volledig onder water zit, hoe groter de archimedeskracht erop.",
        antwoord=False,
        uitleg="In de formule staat de diepte niet. Zolang het hele voorwerp onder water zit, blijft de archimedeskracht dezelfde, ook tien meter lager.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp dat stijgt in een vloeistof, heeft een grotere massadichtheid dan die vloeistof.",
        antwoord=False,
        uitleg="Net omgekeerd: stijgen betekent dat de archimedeskracht het haalt, dus dat het voorwerp een kleinere massadichtheid heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de maan zou de archimedeskracht in hetzelfde bad water kleiner zijn.",
        antwoord=True,
        uitleg="In FA = ρ.g.Vond staat g, en die is op de maan ongeveer zes keer kleiner. De zwaartekracht op het voorwerp wordt wel even veel kleiner, dus het drijft nog altijd even diep.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de wet die zegt hoe groot de opwaartse kracht in een vloeistof is? Schrijf de naam van de geleerde.",
        antwoord=["Archimedes", "archimedes", "wet van Archimedes"],
        uitleg="De wet van Archimedes. De opwaartse kracht heet daarom de archimedeskracht.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor massadichtheid?",
        antwoord=["ρ", "rho", "p"],
        uitleg="De Griekse letter ρ (rho), met als eenheid kg/m³.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de massadichtheid van water? Schrijf het getal in kg/m³.",
        antwoord=["1000", "1000 kg/m³"],
        uitleg="1000 kg/m³, of ook 1 kg per liter. Die waarde staat bij de constanten van het examen.",
    ),
    dict(
        type="invultekst",
        vraag="Een blok van 0,0050 m³ zit volledig onder water. Hoe groot is de archimedeskracht in newton? Schrijf het getal, afgerond op een eenheid.",
        antwoord=["49", "49 N", "49,05"],
        uitleg="FA = 1000 . 9,81 . 0,0050 = 49,05 N, dus ongeveer 49 N.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft het moment van een kracht?",
        opties=["M = F . d . sin α", "M = F . d", "M = F / d", "M = F . d . cos α"],
        antwoord=0,
        uitleg="De kracht maal de krachtarm maal de sinus van de hoek. Staat de kracht loodrecht op de arm, dan is sin α gelijk aan 1 en blijft M = F . d over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van het moment van een kracht?",
        opties=["Nm", "N", "N/m", "J"],
        antwoord=0,
        uitleg="De newtonmeter, want je vermenigvuldigt een kracht met een afstand. Het is geen joule, ook al heeft die dezelfde grootte-orde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de krachtarm van een kracht?",
        opties=[
            "de afstand van het draaipunt tot het aangrijpingspunt",
            "de lengte van de krachtvector op de tekening",
            "de grootte van de kracht in newton",
            "de hoek tussen de kracht en de arm",
        ],
        antwoord=0,
        uitleg="De krachtarm d is de afstand van het draaipunt tot waar de kracht aangrijpt. Samen met de hoek bepaalt die hoeveel draaieffect de kracht heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kracht van 40 N werkt loodrecht op een arm van 0,50 m. Hoe groot is het moment?",
        opties=["20 Nm", "80 Nm", "40 Nm", "0,013 Nm"],
        antwoord=0,
        uitleg="M = 40 . 0,50 . sin 90° = 20 Nm, want sin 90° is 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een moer losdraaien makkelijker met een lange sleutel dan met een korte?",
        opties=[
            "de krachtarm is groter, dus wordt het moment groter",
            "de kracht die je uitoefent wordt zelf groter",
            "de hoek met de arm wordt groter",
            "het draaipunt verschuift naar de moer toe",
        ],
        antwoord=0,
        uitleg="M = F . d . sin α: verdubbel je d, dan verdubbelt het moment bij dezelfde kracht. Daarom verlengt een monteur soms een sleutel met een buis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarden gelden samen bij statisch evenwicht? Kruis alles aan wat juist is.",
        opties=[
            "de som van alle krachten is nul",
            "de som van alle krachtmomenten is nul",
            "er werkt geen enkele kracht",
            "de krachtarmen zijn allemaal even lang",
        ],
        antwoord=[0, 1],
        uitleg="De eerste voorwaarde is het translatie-evenwicht, de tweede het rotatie-evenwicht. Er mogen wel krachten werken, zolang ze elkaar opheffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een wip zit links een kind van 30 kg op 1,2 m van het draaipunt. Rechts zit een kind van 36 kg. Op welke afstand moet dat zitten voor evenwicht?",
        opties=["1,0 m", "1,4 m", "0,83 m", "1,2 m"],
        antwoord=0,
        uitleg="De momenten moeten gelijk zijn: 30 . 1,2 = 36 . d, dus d = 36 / 36 = 1,0 m. Het zwaardere kind zit dichter bij het draaipunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kracht grijpt aan onder een hoek van 30° met de arm, met F = 60 N en d = 0,40 m. Hoe groot is het moment?",
        opties=["12 Nm", "24 Nm", "21 Nm", "48 Nm"],
        antwoord=0,
        uitleg="M = 60 . 0,40 . sin 30° = 60 . 0,40 . 0,50 = 12 Nm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke hoek tussen de kracht en de krachtarm is het moment het grootst?",
        opties=["90°", "0°", "45°", "180°"],
        antwoord=0,
        uitleg="Bij 90° is sin α gelijk aan 1, dus is het moment maximaal. Bij 0° of 180° werkt de kracht langs de arm en is het moment nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een balk ligt op twee steunpunten. Welke krachten neem je mee in de krachtenbalans? Kruis alles aan wat juist is.",
        opties=[
            "de zwaartekracht op de balk",
            "de twee steunkrachten van de steunpunten",
            "de momenten van de krachten",
            "de massa van de balk in kilogram",
        ],
        antwoord=[0, 1],
        uitleg="Een krachtenbalans telt enkel krachten in newton. De momenten horen in de krachtmomentenbalans, en een massa is geen kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat een bus met passagiers op het bovendek minder stabiel?",
        opties=[
            "het zwaartepunt ligt hoger",
            "de massa is kleiner",
            "de zwaartekracht verandert van richting",
            "de krachtarm van de zwaartekracht is nul",
        ],
        antwoord=0,
        uitleg="Hoe hoger het zwaartepunt, hoe minder de bus moet kantelen voor het zwaartepunt buiten het steunvlak komt. Dan kan het moment van de zwaartekracht hem doen omvallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp in rotatie-evenwicht draait niet, ook al werken er krachten op.",
        antwoord=True,
        uitleg="De momenten die links om willen draaien, heffen de momenten op die rechts om willen draaien. Hun som is nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht die door het draaipunt gaat, levert geen moment.",
        antwoord=True,
        uitleg="De krachtarm is dan nul, of de kracht ligt langs de arm, en in beide gevallen is M nul. Duwen op het hengsel van een deur doet ze niet draaien.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de som van alle krachten op een voorwerp nul is, dan kan het zeker niet draaien.",
        antwoord=False,
        uitleg="Twee gelijke en tegengestelde krachten op verschillende plaatsen heffen elkaar op als kracht, maar kunnen het voorwerp wel doen draaien. Daarom bestaat er naast de krachtenbalans ook een krachtmomentenbalans.",
    ),
    dict(
        type="waarofniet",
        vraag="Het moment van een kracht wordt in joule uitgedrukt.",
        antwoord=False,
        uitleg="Het moment krijgt de newtonmeter, Nm. De joule is de eenheid van arbeid en energie, ook al is ze eveneens een newton maal een meter.",
    ),
    dict(
        type="waarofniet",
        vraag="Een draaipunt heet ook een steunpunt als het voorwerp erop rust.",
        antwoord=True,
        uitleg="Bij een wip of een hefboom is dat hetzelfde punt: het voorwerp rust erop en draait er omheen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor het moment van een kracht?",
        antwoord=["M"],
        uitleg="M, met als eenheid de newtonmeter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het evenwicht waarbij een voorwerp niet verschuift? Schrijf het woord voor dat soort evenwicht.",
        antwoord=["translatie-evenwicht", "translatie", "translatieevenwicht"],
        uitleg="Het translatie-evenwicht: de som van de krachten is nul. Het rotatie-evenwicht gaat over niet draaien.",
    ),
    dict(
        type="invultekst",
        vraag="Een kracht van 25 N werkt loodrecht op een arm van 0,80 m. Hoe groot is het moment in Nm? Schrijf het getal.",
        antwoord=["20", "20 Nm"],
        uitleg="M = 25 . 0,80 . 1 = 20 Nm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de afstand van het draaipunt tot het aangrijpingspunt van een kracht?",
        antwoord=["krachtarm", "de krachtarm", "arm"],
        uitleg="De krachtarm, met symbool d. Een langere arm geeft bij dezelfde kracht een groter moment.",
    ),
]
