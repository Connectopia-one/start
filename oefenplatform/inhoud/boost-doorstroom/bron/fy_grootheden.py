# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Grootheden, eenheden en nauwkeurig meten.

Hoort bij "grootheden en eenheden" van de vakfiche fysica 2de graad
doorstroomfinaliteit. Dat onderdeel staat op de fiche samen met beweging en
krachten op 35 %; dit is daarvan het eerste van vijf thema's.

Deel 1 gaat over de grootheden zelf: welke eenheid bij welke grootheid hoort,
de voorvoegsels van mega tot nano, het omrekenen naar SI-eenheden en de
wetenschappelijke notatie. Deel 2 gaat over nauwkeurig meten en over verbanden
tussen grootheden: beduidende cijfers, schatten, een recht of omgekeerd
evenredig verband herkennen, en de vier kenmerken van een vector.

De voorvoegsels en de tabel met grootheden en eenheden staan in bijlage 1 van de
fiche, en die bijlage mag een kind níet gebruiken op het examen. Alles in dit
thema moet dus uit het hoofd gekend zijn.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van kracht?",
        opties=["newton", "kilogram", "joule", "pascal"],
        antwoord=0,
        uitleg="De newton (N) is de eenheid van kracht. De kilogram hoort bij massa, de joule bij energie en de pascal bij druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheden zijn SI-eenheden? Kruis alles aan wat juist is.",
        opties=["meter", "kilogram", "liter", "kilometer per uur"],
        antwoord=[0, 1],
        uitleg="De meter en de kilogram zijn SI-eenheden. De liter en de kilometer per uur zijn veelgebruikte eenheden, maar niet de SI-eenheid van volume (m³) of van snelheid (m/s).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke waarde hoort bij het voorvoegsel micro?",
        opties=["10⁻⁶", "10⁻³", "10⁻⁹", "10⁶"],
        antwoord=0,
        uitleg="Micro staat voor een miljoenste, dus 10⁻⁶. Milli is 10⁻³, nano is 10⁻⁹ en mega is 10⁶.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel meter is 2,5 km?",
        opties=["2500 m", "250 m", "25 000 m", "0,0025 m"],
        antwoord=0,
        uitleg="Kilo betekent duizend, dus 2,5 km = 2,5 . 10³ m = 2500 m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een snelheid van 72 km/h omgerekend naar de SI-eenheid is:",
        opties=["20 m/s", "72 m/s", "7,2 m/s", "259 m/s"],
        antwoord=0,
        uitleg="Deel door 3,6 om van km/h naar m/s te gaan: 72 / 3,6 = 20 m/s. In één uur zitten 3600 s en in één kilometer 1000 m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je 0,00045 m in de wetenschappelijke notatie?",
        opties=["4,5 . 10⁻⁴ m", "45 . 10⁻⁵ m", "4,5 . 10⁴ m", "0,45 . 10⁻³ m"],
        antwoord=0,
        uitleg="In de wetenschappelijke notatie staat er één cijfer voor de komma, van 1 tot 9. De komma schuift vier plaatsen naar rechts, dus de exponent is −4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheid hoort bij de eenheid pascal?",
        opties=["druk", "kracht", "arbeid", "vermogen"],
        antwoord=0,
        uitleg="Eén pascal is één newton per vierkante meter, dus de pascal is de eenheid van druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden worden met hun eigen symbool genoteerd? Kruis alles aan wat juist is.",
        opties=[
            "massa met m",
            "tijdsduur met Δt",
            "kracht met k",
            "druk met d",
        ],
        antwoord=[0, 1],
        uitleg="De massa krijgt m en een tijdsduur krijgt Δt. Kracht krijgt F, en k is het symbool van de veerconstante. Druk krijgt p.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kubieke meter is 500 liter?",
        opties=["0,5 m³", "5 m³", "50 m³", "0,05 m³"],
        antwoord=0,
        uitleg="Eén kubieke meter is 1000 liter. Dus 500 L = 500 / 1000 = 0,5 m³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke combinaties van grootheid en SI-eenheid horen bij elkaar? Kruis alles aan wat juist is.",
        opties=[
            "weerstand en ohm",
            "warmte en joule",
            "massadichtheid en kilogram",
            "versnelling en meter per seconde",
        ],
        antwoord=[0, 1],
        uitleg="De ohm hoort bij weerstand en de joule bij warmte. De massadichtheid heeft kg/m³ als eenheid, en een versnelling m/s².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een massa van 2,4 ton is in de SI-eenheid:",
        opties=["2400 kg", "240 kg", "24 000 kg", "2,4 kg"],
        antwoord=0,
        uitleg="Eén ton is 1000 kg, dus 2,4 ton = 2400 kg. De ton is geen SI-eenheid, de kilogram wel.",
    ),
    dict(
        type="waarofniet",
        vraag="De kilogram is de SI-eenheid van massa, ook al staat er al een voorvoegsel in.",
        antwoord=True,
        uitleg="De kilogram is een uitzondering: ze is de SI-eenheid van massa, hoewel het woord met kilo begint.",
    ),
    dict(
        type="waarofniet",
        vraag="Een graad Celsius en een kelvin zijn even grote stappen op de temperatuurschaal.",
        antwoord=True,
        uitleg="Een verschil van 1 °C is even groot als een verschil van 1 K. Enkel het nulpunt ligt anders: 0 K is −273,15 °C.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorvoegsel deca staat voor honderd.",
        antwoord=False,
        uitleg="Deca is tien, dus 10¹. Hecto is honderd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meting met een meetinstrument geeft altijd de exacte waarde van een grootheid.",
        antwoord=False,
        uitleg="Elk meetinstrument heeft een beperkte nauwkeurigheid, dus een meting benadert de waarde altijd. Daarom geef je een meetresultaat met het juiste aantal beduidende cijfers.",
    ),
    dict(
        type="waarofniet",
        vraag="De eenheid van vermogen is de watt, en één watt is één joule per seconde.",
        antwoord=True,
        uitleg="Vermogen is energie per tijd, dus 1 W = 1 J/s.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de SI-eenheid van tijd? Schrijf de naam van de eenheid.",
        antwoord=["seconde", "de seconde", "seconden"],
        uitleg="De seconde, met symbool s. De minuut en het uur worden ook gebruikt, maar zijn geen SI-eenheid.",
    ),
    dict(
        type="invultekst",
        vraag="Welk voorvoegsel hoort bij de waarde 10³? Schrijf de naam.",
        antwoord=["kilo", "kilo-"],
        uitleg="Kilo staat voor duizend, dus 10³. Het symbool is k, zoals in km en kg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel seconden zitten er in een kwartier? Schrijf het getal.",
        antwoord=["900", "900 s"],
        uitleg="Een kwartier is 15 minuten en elke minuut heeft 60 s: 15 . 60 = 900 s.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel beduidende cijfers heeft het meetresultaat 0,0250 m? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="De nullen vooraan tellen niet mee, maar de 2, de 5 en de laatste 0 wel. Die laatste nul staat er niet voor niets: ze zegt dat er tot op de tiende millimeter gemeten is.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier kenmerken heeft een vectoriële grootheid?",
        opties=[
            "grootte, richting, zin en aangrijpingspunt",
            "grootte, eenheid, symbool en teken",
            "lengte, breedte, hoogte en massa",
            "begin, midden, einde en grootte",
        ],
        antwoord=0,
        uitleg="Een vector heeft een grootte, een richting, een zin en een aangrijpingspunt. Die vier samen beschrijven bijvoorbeeld een kracht volledig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden zijn vectoriële grootheden? Kruis alles aan wat juist is.",
        opties=["verplaatsing", "kracht", "massa", "temperatuur"],
        antwoord=[0, 1],
        uitleg="Een verplaatsing en een kracht hebben een richting en een zin, dus zijn het vectoren. Massa en temperatuur zijn getallen met een eenheid, zonder richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt bij een recht evenredig verband tussen twee grootheden? Kruis alles aan wat juist is.",
        opties=[
            "de grafiek is een rechte door de oorsprong",
            "de verhouding van de twee grootheden blijft gelijk",
            "het product van de twee grootheden blijft gelijk",
            "de grafiek van het verband is een parabool",
        ],
        antwoord=[0, 1],
        uitleg="Recht evenredig betekent dat de verhouding gelijk blijft, en dat geeft een rechte door de oorsprong. Blijft het product gelijk, dan is het verband omgekeerd evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een omgekeerd evenredig verband tussen p en V geldt:",
        opties=[
            "p . V blijft gelijk",
            "p / V blijft gelijk",
            "p + V blijft gelijk",
            "p − V blijft gelijk",
        ],
        antwoord=0,
        uitleg="Omgekeerd evenredig betekent dat het product gelijk blijft: wordt V twee keer zo groot, dan wordt p twee keer zo klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet de massa van een appel. Welk meetinstrument kies je?",
        opties=["een balans", "een dynamometer", "een maatcilinder", "een manometer"],
        antwoord=0,
        uitleg="Een balans meet massa. Een dynamometer meet een kracht, een maatcilinder een volume en een manometer een druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit de formule p = F / A wil je A vrijmaken. Wat krijg je?",
        opties=["A = F / p", "A = p / F", "A = p . F", "A = F − p"],
        antwoord=0,
        uitleg="Vermenigvuldig beide leden met A en deel daarna door p: A = F / p.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het afronden van een rekenresultaat zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "je antwoord heeft niet meer beduidende cijfers dan het minst nauwkeurige gegeven",
            "je zet de eenheid bij je antwoord",
            "je rondt elk tussenresultaat af voor je verder rekent",
            "je mag de eenheid weglaten als de opgave ze al noemt",
        ],
        antwoord=[0, 1],
        uitleg="Je antwoord kan niet nauwkeuriger zijn dan je gegevens, en zonder eenheid betekent een getal in de fysica niets. Afronden doe je pas op het einde, anders sleep je een afrondingsfout mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling meet een tafel met een meetlint en noteert 1,2534 m. Wat is daar vreemd aan?",
        opties=[
            "een meetlint kan niet tot op een tiende millimeter meten",
            "het resultaat staat niet in de wetenschappelijke notatie",
            "een lengte moet altijd in centimeter staan",
            "de eenheid m is geen SI-eenheid",
        ],
        antwoord=0,
        uitleg="Het aantal beduidende cijfers moet passen bij de nauwkeurigheid van het instrument. Een gewoon meetlint leest tot op de millimeter af, dus 1,253 m is het meest dat je mag noteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet 0,8 L water afmeten. Welke maatcilinder is het geschiktst?",
        opties=[
            "een cilinder van 1 L met streepjes per 10 mL",
            "een cilinder van 5 L met streepjes per 100 mL",
            "een cilinder van 100 mL met streepjes per 1 mL",
            "een cilinder van 50 mL met streepjes per 0,5 mL",
        ],
        antwoord=0,
        uitleg="Je hebt een cilinder nodig waar 0,8 L in past en die toch fijn genoeg afleest. De cilinders van 100 mL en 50 mL zijn te klein, en bij de cilinder van 5 L zijn de streepjes te grof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke schatting is realistisch?",
        opties=[
            "een fles water van 1,5 L heeft een massa van ongeveer 1,5 kg",
            "een fles water van 1,5 L heeft een massa van ongeveer 15 kg",
            "een volwassen mens heeft een massa van ongeveer 700 kg",
            "een auto rijdt in de stad ongeveer 300 km/h",
        ],
        antwoord=0,
        uitleg="Water heeft een massadichtheid van 1000 kg/m³, dus één liter weegt ongeveer één kilogram. Schatten helpt om een rekenfout op te sporen: 700 kg voor een mens kan niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een grafiek van de veerkracht in functie van de lengteverandering van een veer krijg je een rechte door de oorsprong. Wat betekent de steilheid van die rechte?",
        opties=[
            "de veerconstante",
            "de massa van het gewicht",
            "de zwaarteveldsterkte",
            "de lengte van de veer in rust",
        ],
        antwoord=0,
        uitleg="Bij Fv = k . Δl is k de verhouding van de kracht tot de lengteverandering, en dat is net de steilheid van de rechte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grootheid met een vectorpijl erbij geschreven betekent dat je de richting en de zin ervan moet meegeven.",
        antwoord=True,
        uitleg="Het pijltje boven het symbool zegt dat het een vector is. Zonder pijltje bedoel je enkel de grootte.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee metingen zijn alleen met elkaar te vergelijken als ze in dezelfde eenheid staan.",
        antwoord=True,
        uitleg="Daarom reken je eerst om naar dezelfde eenheid. Anders vergelijk je bijvoorbeeld een snelheid in km/h met een snelheid in m/s.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lineair verband tussen twee grootheden betekent altijd dat ze recht evenredig zijn.",
        antwoord=False,
        uitleg="Een lineair verband geeft een rechte, maar die hoeft niet door de oorsprong te gaan. Enkel een rechte door de oorsprong is recht evenredig.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een meetinstrument blijven aanstaan als je niet meet, want dat verandert de meting niet.",
        antwoord=False,
        uitleg="Een instrument dat aan blijft staan, verbruikt zijn batterij en kan warm worden, en een multimeter op de verkeerde stand kan stuk gaan. Je schakelt het uit als je niet meet.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een kwadratisch verband tussen v en Ek wordt Ek vier keer zo groot als v verdubbelt.",
        antwoord=True,
        uitleg="In Ek = m . v² / 2 staat de snelheid in het kwadraat. Twee keer zo snel geeft dus vier keer zoveel kinetische energie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de eigenschap van een meetinstrument die zegt hoe fijn het kan aflezen?",
        antwoord=["nauwkeurigheid", "de nauwkeurigheid", "precisie"],
        uitleg="De nauwkeurigheid. Daarnaast heeft een instrument ook een meetbereik: de grootste waarde die het kan meten.",
    ),
    dict(
        type="invultekst",
        vraag="Welk meetinstrument gebruik je om een kracht te meten?",
        antwoord=["dynamometer", "een dynamometer", "krachtmeter"],
        uitleg="Een dynamometer. Die werkt met een veer: hoe groter de kracht, hoe verder de veer uitrekt.",
    ),
    dict(
        type="invultekst",
        vraag="Je rekent 45 mm om naar meter. Schrijf het resultaat in meter.",
        antwoord=["0,045", "0,045 m", "0.045"],
        uitleg="Milli is een duizendste, dus 45 mm = 45 / 1000 m = 0,045 m.",
    ),
    dict(
        type="invultekst",
        vraag="Welk woord gebruikt men voor het grootste getal dat een meetinstrument kan meten?",
        antwoord=["meetbereik", "het meetbereik", "bereik"],
        uitleg="Het meetbereik. Meet je iets groter dan het meetbereik, dan loopt het instrument over of gaat het stuk.",
    ),
]
