# -*- coding: utf-8 -*-
"""Pittige vragen bij "De elektrische stroomkring" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en 2, maar met gemengde schakelingen in woorden
beschreven, de keuze tussen serie en parallel voor een nieuwe situatie, en
storingen waarbij je van het gevolg naar de oorzaak terug moet redeneren.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="Een batterij, een gesloten schakelaar en lampje A staan in serie. Na lampje A splitst de kring in twee takken: in de ene tak zit lampje B, in de andere lampje C. Daarna komen de takken weer samen en gaat de draad terug naar de batterij. Lampje B gaat stuk. Welke lampjes branden nog?",
        opties=[
            "Lampje A en lampje C",
            "Geen enkel lampje meer",
            "Alleen lampje A",
            "Alleen lampje C",
        ],
        antwoord=0,
        uitleg="Lampje B zit in een eigen tak. Valt die tak weg, dan kan de stroom nog altijd door A en daarna door de tak met C. Was het lampje A geweest, dan was alles uitgegaan, want alle stroom moet door A.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een batterij voedt twee takken die in parallel staan. In de ene tak zitten schakelaar S en lampje L1, in de andere tak alleen lampje L2. Je opent schakelaar S. Wat zie je?",
        opties=[
            "L1 gaat uit en L2 blijft branden",
            "L1 en L2 gaan allebei uit",
            "L2 gaat uit en L1 blijft branden",
            "L1 en L2 blijven allebei branden",
        ],
        antwoord=0,
        uitleg="De schakelaar zit alleen in de tak van L1, dus alleen die tak wordt onderbroken. De tak van L2 blijft gesloten. Een schakelaar werkt alleen op de tak waarin hij staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zaagmachine mag alleen draaien als het beschermkapje dicht is én de startknop ingedrukt is. Aan het kapje zit een schakelaar die sluit als het kapje dicht is. Hoe schakel je de kapschakelaar en de startknop?",
        opties=[
            "In serie met elkaar",
            "In parallel met elkaar",
            "Elk in een eigen kring met een eigen batterij",
            "De kapschakelaar in parallel met de motor zelf",
        ],
        antwoord=0,
        uitleg="Net als bij de heggenschaar moeten beide schakelaars dicht zijn voor de kring gesloten is, en dat krijg je in serie. In parallel zou de machine al draaien als één van de twee gesloten is, dus ook met het kapje open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zoemer moet afgaan als iemand op de knop aan de voordeur of op de knop aan de achterdeur drukt. Eén knop indrukken moet volstaan. Hoe schakel je de twee knoppen?",
        opties=[
            "In parallel met elkaar",
            "In serie met elkaar",
            "Allebei in serie met een open schakelaar",
            "Elk aan een andere kant van de batterij",
        ],
        antwoord=0,
        uitleg="In parallel heeft elke knop een eigen tak, en één gesloten tak is genoeg om de kring rond te maken. In serie zou de zoemer pas afgaan als iemand aan beide deuren tegelijk drukt, zoals bij de heggenschaar.",
    ),
    dict(
        type="waarofniet",
        vraag="In een serieschakeling met drie lampjes kan je met een schakelaar één lampje uitzetten terwijl de andere twee blijven branden.",
        antwoord=False,
        uitleg="In serie is er maar één weg voor de stroom. Open je ergens een schakelaar, dan is de hele kring onderbroken en gaan alle drie de lampjes uit. Wil je één lampje apart uitzetten, dan moet het in een eigen tak staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een LED zit in een gesloten kring met een nieuwe batterij en goede draden, maar ze blijft donker. Wat is de meest waarschijnlijke oorzaak?",
        opties=[
            "De LED zit omgekeerd in de kring",
            "Een batterij levert gelijkspanning, en een LED werkt enkel op wisselspanning",
            "De schakelaar in de kring staat gesloten in plaats van open",
            "De draden zijn van koper, en koper geleidt de stroom te slecht",
        ],
        antwoord=0,
        uitleg="Een LED laat de stroom maar in één richting door. Zit ze omgekeerd, dan blijft ze donker, ook in een gesloten kring. Een gesloten schakelaar is net goed, en koper is een goede geleider.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil met een multimeter nagaan of een batterij nog genoeg spanning heeft. Hoe gebruik je de multimeter, en in welke eenheid lees je af?",
        opties=[
            "Als voltmeter, en je leest af in volt",
            "Als ampèremeter, en je leest af in volt",
            "Als voltmeter, en je leest af in ampère",
            "Als ampèremeter, en je leest af in ohm",
        ],
        antwoord=0,
        uitleg="Spanning meet je met de multimeter als voltmeter, en spanning druk je uit in volt. Als ampèremeter meet je de stroomsterkte, in ampère. De ohm is de eenheid van weerstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinaties van grootheid, symbool en eenheid kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Stroomsterkte, symbool I, in ampère",
            "Spanning, symbool U, in volt",
            "Weerstand, symbool R, in ohm",
            "Vermogen, symbool P, in volt",
            "Spanning, symbool U, in ampère",
        ],
        antwoord=[0, 1, 2],
        uitleg="Stroomsterkte I in ampère, spanning U in volt, weerstand R in ohm en vermogen P in watt. Vermogen in volt klopt dus niet, en spanning in ampère haalt spanning en stroomsterkte door elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand raakt een beschadigd snoer aan, en er lekt stroom weg door zijn lichaam. Welke veiligheidsvoorziening is net gemaakt om dan meteen uit te schakelen?",
        opties=[
            "De verliesstroomschakelaar",
            "De automatische zekering",
            "De dubbele isolatie",
            "Het kroonsteentje",
        ],
        antwoord=0,
        uitleg="De verliesstroomschakelaar schakelt uit zodra er stroom weglekt, bijvoorbeeld door een mens. De automatische zekering reageert op te veel stroom in de kring, en dat is iets anders. Dubbele isolatie is een bouwwijze en een kroonsteentje verbindt alleen draden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Er loopt al een tijd meer stroom door een snoer dan het aankan, en plots valt de stroom uit. Welk gevaar was er, en welke voorziening greep in?",
        opties=[
            "Overbelasting, en de automatische zekering onderbrak de kring",
            "Kortsluiting, en de aardingsdraad leidde de stroom naar de grond",
            "Elektrocutie, en de dubbele isolatie schakelde het snoer uit",
            "Overbelasting, en de aardingsdraad onderbrak meteen de kring",
        ],
        antwoord=0,
        uitleg="Meer stroom door een draad dan hij aankan, is overbelasting. De automatische zekering onderbreekt de kring bij te veel stroom. De aardingsdraad onderbreekt niets: hij leidt stroom naar de grond weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een batterij en een generator zijn allebei spanningsbronnen, maar alleen de batterij levert gelijkspanning.",
        antwoord=True,
        uitleg="Allebei leveren ze de spanning voor een kring. Een batterij is een gelijkspanningsbron, een generator levert wisselspanning.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een heggenschaar met twee schakelaars in serie stopt de motor zodra je één van de twee schakelaars loslaat.",
        antwoord=True,
        uitleg="In serie moeten beide schakelaars gesloten zijn voor de kring rond is. Laat je er één los, dan is de kring open en stopt de motor. Zo kan je hand nooit bij het mes als de schaar draait.",
    ),
    dict(
        type="waarofniet",
        vraag="Een striptang en een zijsnijtang doen hetzelfde: met allebei knip je een draad door.",
        antwoord=False,
        uitleg="Met een zijsnijtang knip je een draad door. Met een striptang haal je alleen het kunststof laagje van de draad, zonder het koper te beschadigen.",
    ),
    dict(
        type="invultekst",
        vraag="Je haalt eerst met een striptang het kunststof laagje van twee draden. Daarna wil je die twee draden met tin aan elkaar vastmaken. Welk gereedschap gebruik je voor die tweede stap? Antwoord met één woord.",
        antwoord="soldeerbout",
        uitleg="Een soldeerbout verbindt twee draden met tin. Een kroonsteentje verbindt ook twee draden, maar met schroefjes en zonder tin.",
    ),
    dict(
        type="invultekst",
        vraag="Een toestel heeft een extra draad die bij een defect de stroom veilig naar de grond wegleidt, zodat de stroom niet door jou loopt. Hoe heet die veiligheidsvoorziening? Antwoord met één woord.",
        antwoord="aarding",
        uitleg="Dat is de aarding: de aardingsdraad leidt de stroom veilig naar de grond weg. De verliesstroomschakelaar en de automatische zekering schakelen uit, maar leiden zelf geen stroom weg.",
    ),
    dict(
        type="invultekst",
        vraag="Mila heeft twee slingers van elk 20 lampjes. In de ene slinger staan de lampjes in serie, in de andere in parallel. In elke slinger gaan er 2 lampjes stuk. Hoeveel lampjes branden er dan nog in totaal? Antwoord met een getal.",
        antwoord="18",
        reken="0 + (20 - 2)",
        uitleg="In de serieslinger is de kring onderbroken, dus daar brandt niets meer. In de parallelslinger blijven de andere 18 lampjes branden. Wie bij beide slingers 18 rekent, komt op 36, maar vergeet dat serie maar één weg heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt telkens één voorwerp in de opening van een kring met een batterij en een lampje. Bij welke voorwerpen gaat het lampje branden? (meerdere antwoorden mogelijk)",
        opties=[
            "Een stalen paperclip",
            "Een stuk koperdraad zonder isolatie",
            "Een glazen knikker",
            "Een houten ijsstokje",
            "Een kunststof liniaal",
        ],
        antwoord=[0, 1],
        uitleg="Staal en koper zijn metalen en dus goede geleiders: de kring wordt gesloten en het lampje brandt. Glas, hout en kunststof zijn niet-metalen en laten de stroom niet door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze dingen teken je in een elektrisch schema met een eigen symbool? (meerdere antwoorden mogelijk)",
        opties=[
            "Een spanningsbron",
            "Een schakelaar",
            "Een LED",
            "Een zoemer",
            "Een striptang",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Een spanningsbron, een schakelaar, een LED en een zoemer zijn componenten die in de kring zelf zitten, en elk heeft een eigen symbool. Een striptang is gereedschap waarmee je een draad bewerkt: die zit niet in de kring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lampje in een kring met een nieuwe batterij en een gesloten schakelaar brandt toch niet. Het lampje zelf is in orde. Welke verklaring past?",
        opties=[
            "Er zit ergens een draad los, zodat de kring toch open is",
            "De kring is gesloten, en in een gesloten kring brandt geen lampje",
            "De schakelaar moet open staan om de stroom door te laten",
            "Een batterij levert gelijkspanning en een lampje heeft wisselspanning nodig",
        ],
        antwoord=0,
        uitleg="Een lampje brandt alleen in een gesloten kring. Is de schakelaar dicht en brandt het toch niet, dan is de kring ergens anders onderbroken, bijvoorbeeld door een losse draad. Een open schakelaar onderbreekt de kring net.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zou het gevaarlijk zijn om de twee schakelaars van een heggenschaar in parallel te zetten in plaats van in serie?",
        opties=[
            "Dan draait de motor al als je maar één knop indrukt",
            "Dan werkt de schaar helemaal niet meer, wat je ook doet",
            "Dan heb je drie handen nodig om de schaar te starten",
            "Dan loopt er nooit nog stroom door de motor van de schaar",
        ],
        antwoord=0,
        uitleg="In parallel heeft elke schakelaar een eigen tak, en één gesloten tak volstaat. Je kan de schaar dan met één hand starten, terwijl je andere hand bij het mes kan. Daarom staan ze juist in serie.",
    ),
]
