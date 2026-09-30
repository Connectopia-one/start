# -*- coding: utf-8 -*-
"""De vragen voor "Meten, eenheden en modelvoorstellingen" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom: de onderdelen "Meetinstrumenten en
hulpmiddelen" en "Grootheden en eenheden", samen met het stuk
"Modelvoorstellingen" van het constructiesysteem.

Deel 1 gaat over de meetinstrumenten en hulpmiddelen, over de grootheden met
hun symbool en hun SI-eenheid uit bijlage 1, over de voorvoegsels van milli tot
kilo en over de formules van bijlage 2.
Deel 2 gaat over de modelvoorstellingen: de functiedriehoek, de werktekening
met haar aanzichten, de ontvouwing, het isometrisch perspectief, de
conceptschets, de realisatietekening, het detailontwerp, de schaal en de
maataanduiding.

De symbolen worden gevraagd zoals ze in bijlage 1 staan, dus de letter zelf.
Bijlage 1 mag op het examen niet gebruikt worden, bijlage 2 met de formules
wel: vandaar dat de formules hier herkend moeten worden en niet uit het hoofd
opgezegd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk meetinstrument gebruik je om een hoeveelheid vloeistof te meten?",
        opties=[
            "Een maatbeker",
            "Een weegschaal",
            "Een schuifmaat",
            "Een thermometer",
        ],
        antwoord=0,
        uitleg="Een maatbeker of een maatcilinder heeft streepjes met het volume erbij. Een maatcilinder is smaller en dus nauwkeuriger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk meetinstrument gebruik je om de dikte van een plaatje nauwkeurig te meten?",
        opties=[
            "Een schuifmaat",
            "Een meetlat",
            "Een maatcilinder",
            "Een thermometer",
        ],
        antwoord=0,
        uitleg="Een schuifmaat klemt om het voorwerp en leest tot op een tiende millimeter af. Met een meetlat kom je niet zo nauwkeurig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn meetinstrumenten?",
        opties=[
            "Een weegschaal",
            "Een thermometer",
            "Een multimeter",
            "Een stappenplan",
            "Een IPO-model",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een meetinstrument geeft een waarde met een eenheid. Een stappenplan en een IPO-model zijn hulpmiddelen: die helpen je denken, niet meten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stappenplan is een meetinstrument.",
        antwoord=False,
        uitleg="Een stappenplan is een hulpmiddel. De fiche zet meetinstrumenten en hulpmiddelen naast elkaar, maar het zijn twee verschillende dingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het symbool van de grootheid massa?",
        opties=["m", "M", "kg", "g"],
        antwoord=0,
        uitleg="De grootheid massa krijgt de kleine letter m, de eenheid is de kilogram met symbool kg. Grootheid en eenheid zijn dus niet hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van massa?",
        opties=["De kilogram", "De gram", "De ton", "De newton"],
        antwoord=0,
        uitleg="De kilogram is de SI-eenheid. De ton is een niet-SI-eenheid die je ook mag gebruiken, en de newton is de eenheid van kracht.",
    ),
    dict(
        type="invultekst",
        vraag="De SI-eenheid van lengte is de ___.",
        antwoord="meter",
        uitleg="Lengte, breedte, hoogte, straal, zijde en omtrek worden allemaal in meter uitgedrukt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool hoort bij de grootheid oppervlakte?",
        opties=["A", "O", "P", "V"],
        antwoord=0,
        uitleg="Oppervlakte krijgt de letter A, omtrek de letter P en volume de letter V. Dat staat zo in bijlage 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool hoort bij de grootheid omtrek?",
        opties=["P", "O", "A", "U"],
        antwoord=0,
        uitleg="Omtrek is P. Let op: P is ook het symbool van vermogen, maar dan in een elektrisch verband. U is de spanning.",
    ),
    dict(
        type="waarofniet",
        vraag="Het symbool V hoort bij het volume.",
        antwoord=True,
        uitleg="Volume of inhoud krijgt de letter V, en de SI-eenheid is de kubieke meter. De liter is de niet-SI-eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel meter is een kilometer?",
        opties=["1000 meter", "100 meter", "10 meter", "10 000 meter"],
        antwoord=0,
        uitleg="Kilo betekent duizend. Daarom is een kilogram ook duizend gram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel millimeter is een centimeter?",
        opties=["10 millimeter", "100 millimeter", "1000 millimeter", "5 millimeter"],
        antwoord=0,
        uitleg="Milli is een duizendste en centi een honderdste. Een centimeter is dus tien keer een millimeter.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorvoegsel hecto betekent duizend.",
        antwoord=False,
        uitleg="Hecto betekent honderd. Duizend is kilo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorvoegsels maken een eenheid kleiner?",
        opties=["deci", "centi", "milli", "kilo", "hecto"],
        antwoord=[0, 1, 2],
        uitleg="Deci is een tiende, centi een honderdste en milli een duizendste. Kilo, hecto en deca maken een eenheid juist groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel liter is een kubieke decimeter?",
        opties=["1 liter", "10 liter", "100 liter", "1000 liter"],
        antwoord=0,
        uitleg="Een kubieke decimeter is precies een liter. Een kubieke meter is dus duizend liter.",
    ),
    dict(
        type="invultekst",
        vraag="De eenheid van kracht is de ___.",
        antwoord="newton",
        uitleg="Kracht draagt het symbool F en wordt uitgedrukt in newton, met symbool N.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke formule bereken je de oppervlakte van een rechthoek?",
        opties=["b maal h", "2 maal (b plus h)", "b plus h", "b maal h maal l"],
        antwoord=0,
        uitleg="Basis maal hoogte. De tweede formule is de omtrek van een rechthoek, de laatste het volume van een balk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke formule bereken je de omtrek van een vierkant?",
        opties=["4 maal z", "z maal z", "z maal z maal z", "2 maal z"],
        antwoord=0,
        uitleg="Vier gelijke zijden, dus vier keer de zijde. z maal z is de oppervlakte en z maal z maal z het volume van een kubus.",
    ),
    dict(
        type="waarofniet",
        vraag="Het volume van een balk bereken je met lengte maal breedte maal hoogte.",
        antwoord=True,
        uitleg="Die formule staat zo in bijlage 2, de bijlage die je op het examen wél mag gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formules staan in bijlage 2 van de vakfiche, die je op het examen mag gebruiken?",
        opties=[
            "De omtrek van een cirkel",
            "De oppervlakte van een vierkant",
            "Het volume van een bol",
            "De formule voor de massadichtheid",
            "De formule voor het elektrisch vermogen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bijlage 2 bevat alleen formules voor omtrek, oppervlakte en volume. De massadichtheid en het vermogen moet je dus zelf kennen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een functiedriehoek?",
        opties=[
            "Een schema met functie, materiaal, bewerking en vorm",
            "Een driehoek die een constructie stevig moet houden",
            "Een tekening van een voorwerp in drie verschillende aanzichten",
            "Een tabel met alle maten van een werkstuk op een rij",
        ],
        antwoord=0,
        uitleg="De functiedriehoek laat zien hoe die vier met elkaar samenhangen. Verander je het materiaal, dan verandert vaak ook de bewerking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dingen staan er in een functiedriehoek?",
        opties=[
            "De functie",
            "Het materiaal",
            "De bewerking",
            "De vorm",
            "De prijs van het werkstuk",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Die vier, en hun onderlinge verband. Wat het kost, hoort er niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werktekening en een technische tekening zijn twee heel verschillende dingen.",
        antwoord=False,
        uitleg="Het zijn twee namen voor hetzelfde. De fiche zet ze in één adem: werktekening of technische tekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het vooraanzicht van een voorwerp?",
        opties=[
            "Wat je ziet als je er recht van voren naar kijkt",
            "Wat je ziet als je er recht van bovenaf naar kijkt",
            "Wat je ziet als je er helemaal van opzij naar kijkt",
            "Wat je ziet als je er van onderuit naar kijkt",
        ],
        antwoord=0,
        uitleg="Het vooraanzicht is het beeld waar je recht tegenaan kijkt. Meestal is dat de kant die het meeste zegt over het voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aanzichten noemt de vakfiche?",
        opties=[
            "Het vooraanzicht",
            "Het bovenaanzicht",
            "Het zijaanzicht",
            "Het onderaanzicht",
            "Het binnenaanzicht",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Die vier staan in de fiche. Een binnenaanzicht bestaat niet; om binnenin te kijken maak je een doorsnede.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bovenaanzicht is wat je ziet als je recht van boven op het voorwerp kijkt.",
        antwoord=True,
        uitleg="Op een werktekening staat het bovenaanzicht meestal recht onder of recht boven het vooraanzicht, zodat de maten met elkaar kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ontvouwing?",
        opties=[
            "Het platte patroon dat je dichtvouwt tot het voorwerp",
            "Een tekening met de drie aanzichten naast elkaar",
            "De eerste ruwe schets van een nieuw idee",
            "Een tekening op de ware grootte van het voorwerp",
        ],
        antwoord=0,
        uitleg="Denk aan een kartonnen doos die je openvouwt: wat je dan plat op tafel ziet liggen, is de ontvouwing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een isometrisch perspectief?",
        opties=[
            "Een tekening waarin je het voorwerp ruimtelijk ziet",
            "Een tekening van één enkele vlakke kant ervan",
            "Een tabel met alle maten van het voorwerp erin",
            "Een snelle schets zonder een enkele maat erbij",
        ],
        antwoord=0,
        uitleg="Je ziet drie kanten tegelijk, met alle schuine lijnen onder dezelfde hoek. Zo zie je in één beeld hoe het voorwerp eruitziet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een conceptschets?",
        opties=[
            "Een eerste ruwe tekening van een idee",
            "De definitieve tekening waarmee je maakt",
            "Een tekening van één onderdeel alleen",
            "Een foto van het afgewerkte werkstuk",
        ],
        antwoord=0,
        uitleg="Een conceptschets of voorontwerp is snel getekend en nog niet af. Ze dient om ideeën te vergelijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een conceptschets is het definitieve ontwerp.",
        antwoord=False,
        uitleg="Een conceptschets is een eerste idee. Het definitieve ontwerp heet de realisatietekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een detailontwerp?",
        opties=[
            "Een tekening van één onderdeel, groter getekend",
            "Een tekening van het volledige werkstuk",
            "Een lijst met alle materialen die je nodig hebt",
            "Een foto van het werkstuk als het klaar is",
        ],
        antwoord=0,
        uitleg="Soms is een stuk te klein of te ingewikkeld om op de gewone tekening duidelijk te zijn. Dan teken je dat stuk apart en groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de schaal 1:2 op een tekening?",
        opties=[
            "De tekening is half zo groot als het voorwerp",
            "De tekening is twee keer zo groot als het voorwerp",
            "De tekening is precies even groot als het voorwerp",
            "Er staan twee voorwerpen naast elkaar op de tekening",
        ],
        antwoord=0,
        uitleg="Het eerste getal is de tekening, het tweede het echte voorwerp. Bij 1:2 is één centimeter op papier dus twee centimeter in het echt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de schaal 2:1 op een tekening?",
        opties=[
            "De tekening is twee keer zo groot als het voorwerp",
            "De tekening is half zo groot als het voorwerp",
            "De tekening is precies even groot als het voorwerp",
            "De tekening is tien keer zo groot als het voorwerp",
        ],
        antwoord=0,
        uitleg="Zo teken je kleine dingen, bijvoorbeeld een schroefje, groot genoeg om nog iets te zien.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij schaal 1:1 is de tekening even groot als het voorwerp.",
        antwoord=True,
        uitleg="Op ware grootte dus. Je kunt het werkstuk dan gewoon op de tekening leggen om te controleren.",
    ),
    dict(
        type="invultekst",
        vraag="De verhouding tussen de tekening en het echte voorwerp heet de ___.",
        antwoord="schaal",
        uitleg="De schaal staat altijd op de tekening vermeld, want zonder die verhouding zeggen de afmetingen op papier niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vind je terug op een werktekening?",
        opties=[
            "De maten van elk deel",
            "De aanzichten van het voorwerp",
            "De schaal waarop getekend is",
            "De prijs van het gebruikte materiaal",
            "De naam van de winkel waar je koopt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een werktekening bevat alles wat je nodig hebt om het werkstuk te maken. Wat het kost en waar je het koopt, hoort daar niet bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een werktekening staan de maten meestal in millimeter.",
        antwoord=True,
        uitleg="Millimeter is nauwkeurig genoeg en levert ronde getallen op. Daarom staat er bij de maat vaak zelfs geen eenheid: iedereen weet dat het mm is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekening toont een voorwerp van voren, van boven en van opzij. Wat is dat?",
        opties=[
            "Een werktekening met drie aanzichten",
            "Een isometrisch perspectief",
            "Een ontvouwing van het voorwerp",
            "Een functiedriehoek van het voorwerp",
        ],
        antwoord=0,
        uitleg="Drie vlakke beelden van dezelfde kant bekeken, met de maten erbij. Samen leggen ze de vorm helemaal vast.",
    ),
    dict(
        type="waarofniet",
        vraag="Een functiedriehoek is een tekening van een voorwerp in drie aanzichten.",
        antwoord=False,
        uitleg="Een functiedriehoek is geen tekening van de vorm maar een schema: functie, materiaal, bewerking en vorm en hoe ze samenhangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maakt een technicus eerst een schets voor hij begint te maken?",
        opties=[
            "Om te zien of het idee klopt voor er materiaal verloren gaat",
            "Om de tekening daarna te kunnen inkaderen en op te hangen",
            "Om te weten hoeveel de machine in de winkel kost",
            "Om alvast een kleur voor het werkstuk te kiezen",
        ],
        antwoord=0,
        uitleg="Op papier iets veranderen kost niets. In hout of metaal kost diezelfde fout je een plank en een uur werk.",
    ),
]
