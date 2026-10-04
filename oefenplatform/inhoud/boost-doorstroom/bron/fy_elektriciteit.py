# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Elektrische stroom, spanning en weerstand.

Hoort bij "elektriciteit" van de vakfiche fysica 2de graad doorstroomfinaliteit,
een onderdeel van 10 % en daarmee één thema.

Deel 1 gaat over de wet van Ohm en de grootheden: lading, stroomsterkte,
spanning en weerstand, het verschil tussen een geleider en een isolator, de
conventionele en de werkelijke stroomzin, het meten met een ampèremeter en een
voltmeter, en het elektrisch vermogen met het joule-effect. Deel 2 gaat over de
schakelingen: de stroom- en spanningsverdeling in een serie- en een
parallelschakeling, de substitutieweerstand met twee of drie weerstanden, een
gemengde schakeling, en de veiligheidsaspecten van een installatie.

De formules van dit thema zijn R = U/I en de regels voor serie en parallel. De
wet van Ohm staat in de bijlage van het examen, de regels voor serie en parallel
ook.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de wet van Ohm?",
        opties=["R = U / I", "R = I / U", "R = U . I", "R = U + I"],
        antwoord=0,
        uitleg="De weerstand is de spanning gedeeld door de stroomsterkte. Je kan ze ook schrijven als U = R . I.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van weerstand?",
        opties=["de ohm", "de volt", "de ampère", "de watt"],
        antwoord=0,
        uitleg="De ohm, met symbool Ω. De volt hoort bij spanning en de ampère bij stroomsterkte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Door een lamp staat 230 V en er loopt 0,50 A. Hoe groot is haar weerstand?",
        opties=["460 Ω", "115 Ω", "0,0022 Ω", "230 Ω"],
        antwoord=0,
        uitleg="R = U / I = 230 / 0,50 = 460 Ω.",
    ),
    dict(
        type="meerkeuze",
        vraag="Over een weerstand van 25 Ω staat 5,0 V. Hoe groot is de stroomsterkte?",
        opties=["0,20 A", "5,0 A", "125 A", "20 A"],
        antwoord=0,
        uitleg="I = U / R = 5,0 / 25 = 0,20 A.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een geleider en een isolator?",
        opties=[
            "een geleider heeft een kleine weerstand, een isolator een grote",
            "een geleider heeft een grote weerstand, een isolator een kleine",
            "een geleider heeft geen spanning nodig",
            "een isolator heeft een hogere spanning nodig",
        ],
        antwoord=0,
        uitleg="Bij dezelfde spanning loopt er door een geleider veel stroom en door een isolator bijna geen. Daarom zit er rubber om een koperdraad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de conventionele stroomzin?",
        opties=[
            "van de plus- naar de minpool, buiten de bron",
            "van de min- naar de pluspool, buiten de bron",
            "altijd dezelfde zin als de elektronen",
            "de zin waarin de spanning daalt in de bron",
        ],
        antwoord=0,
        uitleg="Die afspraak is ouder dan de kennis over elektronen. De elektronen bewegen in werkelijkheid net de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe sluit je een ampèremeter aan?",
        opties=[
            "in serie met het onderdeel",
            "parallel met het onderdeel",
            "altijd rechtstreeks over de bron",
            "tussen de aarding en de fase",
        ],
        antwoord=0,
        uitleg="Een ampèremeter moet de stroom door het onderdeel meten, dus de stroom moet erdoor lopen. Een voltmeter zet je wel parallel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formules geven het elektrisch vermogen van een toestel? Kruis alles aan wat juist is.",
        opties=["P = U . I", "P = |ΔE| / Δt", "P = U / I", "P = R . I"],
        antwoord=[0, 1],
        uitleg="Spanning maal stroomsterkte geeft het vermogen, en vermogen is ook altijd energie per tijd. U/I is de weerstand en R.I is de spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het joule-effect?",
        opties=[
            "een stroom warmt een weerstand op",
            "een weerstand maakt licht zonder warmte",
            "een spanning ontstaat door warmte",
            "een stroom maakt een magnetisch veld",
        ],
        antwoord=0,
        uitleg="De elektronen botsen op de deeltjes van de draad en geven hun energie als warmte door. In een waterkoker is dat gewenst, in een kabel niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over kortsluiting zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de weerstand in de kring is heel klein geworden",
            "de stroomsterkte wordt heel groot",
            "de spanning van de bron wordt heel groot",
            "de stroom valt helemaal weg",
        ],
        antwoord=[0, 1],
        uitleg="Uit I = U / R volgt dat een heel kleine R een heel grote stroom geeft. Door het joule-effect worden de draden dan snel heet, met brandgevaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee toestellen doen hetzelfde werk, maar het ene heeft een kleiner vermogen. Wat geldt?",
        opties=[
            "het zuinigste toestel is dat met het kleinste vermogen",
            "het toestel met het grootste vermogen is het zuinigst",
            "het vermogen zegt niets over het verbruik",
            "beide gebruiken evenveel energie per seconde",
        ],
        antwoord=0,
        uitleg="Het vermogen is de energie per seconde. Doen twee toestellen hetzelfde werk, dan gebruikt dat met het kleinste vermogen minder energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vaste weerstand zijn de spanning en de stroomsterkte recht evenredig.",
        antwoord=True,
        uitleg="Uit U = R . I volgt dat een dubbele spanning een dubbele stroom geeft, zolang R gelijk blijft. In een grafiek geeft dat een rechte door de oorsprong.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vaste spanning zijn de stroomsterkte en de weerstand recht evenredig.",
        antwoord=False,
        uitleg="Ze zijn omgekeerd evenredig: I = U / R. Een dubbele weerstand geeft bij dezelfde spanning de helft van de stroom.",
    ),
    dict(
        type="waarofniet",
        vraag="De elektronen in een draad bewegen in de conventionele stroomzin.",
        antwoord=False,
        uitleg="Ze bewegen juist tegen die zin in, van de min- naar de pluspool. De conventionele zin is een oude afspraak die men behouden heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een geleidbaarheid die groot is, hoort bij een weerstand die klein is.",
        antwoord=True,
        uitleg="Geleidbaarheid en weerstand zijn omgekeerd aan elkaar. Koper geleidt goed, dus heeft het een kleine weerstand.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een elektrisch toestel met natte handen bedienen, zolang de spanning onder 230 V blijft.",
        antwoord=False,
        uitleg="Nat water verlaagt de weerstand van je huid sterk, dus loopt er bij dezelfde spanning veel meer stroom door je lichaam. Dat is net wat elektrocutie gevaarlijk maakt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor stroomsterkte?",
        antwoord=["I"],
        uitleg="Een hoofdletter I, met als eenheid de ampère.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de eenheid van spanning? Schrijf de naam van de eenheid.",
        antwoord=["volt", "de volt", "V"],
        uitleg="De volt, met symbool V. Een stopcontact in België staat op 230 V.",
    ),
    dict(
        type="invultekst",
        vraag="Een toestel staat op 230 V en trekt 2,0 A. Hoeveel watt vermogen heeft het? Schrijf het getal.",
        antwoord=["460", "460 W"],
        uitleg="P = U . I = 230 . 2,0 = 460 W.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het meettoestel dat spanning, stroomsterkte en weerstand kan meten?",
        antwoord=["multimeter", "een multimeter", "universeelmeter"],
        uitleg="Een multimeter. Je kiest met een draaiknop wat je wil meten, bijvoorbeeld DCV voor gelijkspanning.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat geldt in een serieschakeling? Kruis alles aan wat juist is.",
        opties=[
            "de stroomsterkte is in elk onderdeel dezelfde",
            "de stroomsterkte verdeelt zich over de onderdelen",
            "de spanning verdeelt zich over de onderdelen",
            "de spanning is nul over het laatste onderdeel",
        ],
        antwoord=[0, 2],
        uitleg="Er is maar één weg voor de stroom, dus loopt overal dezelfde stroom. De spanning verdeelt zich wel, en samen is dat weer de bronspanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor de spanning in een parallelschakeling?",
        opties=[
            "ze is over elke tak dezelfde",
            "ze verdeelt zich over de takken",
            "ze is het grootst over de grootste weerstand",
            "ze is nul in de tweede tak",
        ],
        antwoord=0,
        uitleg="Elke tak hangt tussen dezelfde twee punten, dus staat er dezelfde spanning over. De stroom verdeelt zich wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee weerstanden van 30 Ω en 60 Ω staan in serie. Hoe groot is de substitutieweerstand?",
        opties=["90 Ω", "20 Ω", "45 Ω", "30 Ω"],
        antwoord=0,
        uitleg="In serie tel je de weerstanden op: 30 + 60 = 90 Ω.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee weerstanden van 30 Ω en 60 Ω staan parallel. Hoe groot is de substitutieweerstand?",
        opties=["20 Ω", "90 Ω", "45 Ω", "1,5 Ω"],
        antwoord=0,
        uitleg="Rs = (1/30 + 1/60)⁻¹ = (3/60)⁻¹ = 20 Ω. Parallel geeft altijd minder dan de kleinste van de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie weerstanden van elk 60 Ω staan parallel. Hoe groot is de substitutieweerstand?",
        opties=["20 Ω", "180 Ω", "60 Ω", "30 Ω"],
        antwoord=0,
        uitleg="Bij gelijke weerstanden parallel deel je door hun aantal: 60 / 3 = 20 Ω.",
    ),
    dict(
        type="meerkeuze",
        vraag="Over een serieschakeling van 20 Ω en 40 Ω staat 12 V. Hoe groot is de stroomsterkte?",
        opties=["0,20 A", "0,60 A", "0,30 A", "2,0 A"],
        antwoord=0,
        uitleg="Rs = 20 + 40 = 60 Ω, dus I = 12 / 60 = 0,20 A. Die stroom loopt door beide weerstanden.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de vorige serieschakeling van 20 Ω en 40 Ω met 0,20 A: hoe groot is de spanning over de weerstand van 40 Ω?",
        opties=["8,0 V", "4,0 V", "12 V", "200 V"],
        antwoord=0,
        uitleg="U = R . I = 40 . 0,20 = 8,0 V. Over de 20 Ω staat 4,0 V, en samen is dat weer 12 V.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kerstboomsnoer in serie gaat helemaal uit als één lampje stuk is. Waarom?",
        opties=[
            "de kring is onderbroken, dus loopt er nergens stroom",
            "de spanning valt weg over de hele kring",
            "de weerstand van de andere lampjes wordt nul",
            "de stroom zoekt een andere weg",
        ],
        antwoord=0,
        uitleg="In serie is er maar één weg. Valt die weg, dan staat de stroom overal stil. Parallel geschakelde lampjes blijven wel branden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een parallelschakeling van twee lampen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "elke lamp krijgt de volle spanning van de bron",
            "de substitutieweerstand is kleiner dan die van één lamp",
            "de stroom door elke lamp is de helft van wat één lamp alleen trekt",
            "beide lampen gaan uit als er één stuk is",
        ],
        antwoord=[0, 1],
        uitleg="Elke tak staat over de hele bron en elke extra tak geeft de stroom een weg bij, dus daalt de totale weerstand. Elke lamp trekt even veel stroom als alleen, en de andere blijft branden als er één uitvalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een gemengde schakeling staat R1 = 10 Ω in serie met twee parallelle weerstanden van elk 20 Ω. Hoe groot is de substitutieweerstand?",
        opties=["20 Ω", "50 Ω", "30 Ω", "10 Ω"],
        antwoord=0,
        uitleg="Eerst de parallelle twee: 20 / 2 = 10 Ω. Die zet je in serie met R1: 10 + 10 = 20 Ω.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veiligheidsaspecten horen bij een elektrische installatie? Kruis alles aan wat juist is.",
        opties=[
            "een automatische zekering",
            "een verliesstroomschakelaar",
            "een grotere spanning op de kring zetten",
            "de aarddraad doorknippen",
        ],
        antwoord=[0, 1],
        uitleg="Een zekering legt de kring af bij een te grote stroom, een verliesstroomschakelaar bij een stroom die via een mens of een vochtige wand wegloopt. De twee andere maken een installatie juist gevaarlijk.",
    ),
    dict(
        type="waarofniet",
        vraag="In een serieschakeling is de som van de spanningen over de onderdelen gelijk aan de spanning van de bron.",
        antwoord=True,
        uitleg="De spanning verdeelt zich, en samen is dat weer de bronspanning. Over de grootste weerstand staat de grootste spanning.",
    ),
    dict(
        type="waarofniet",
        vraag="De substitutieweerstand van een parallelschakeling is altijd groter dan de kleinste van de weerstanden.",
        antwoord=False,
        uitleg="Ze is altijd kléiner dan de kleinste, want elke extra tak geeft de stroom een weg bij. Enkel bij serie wordt de totale weerstand groter.",
    ),
    dict(
        type="waarofniet",
        vraag="De stopcontacten in een huis staan parallel geschakeld.",
        antwoord=True,
        uitleg="Zo staat op elk stopcontact 230 V, los van wat er elders aanhangt. In serie zou elk toestel maar een deel van de spanning krijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verliesstroomschakelaar beschermt vooral tegen een te grote stroom door de toestellen.",
        antwoord=False,
        uitleg="Dat doet de automatische zekering. Een verliesstroomschakelaar merkt dat er stroom wegloopt die niet terugkomt, bijvoorbeeld door een mens, en legt de kring af.",
    ),
    dict(
        type="waarofniet",
        vraag="Een aarddraad leidt een stroom die op de metalen kast van een toestel komt, veilig naar de aarde.",
        antwoord=True,
        uitleg="Zo gaat de stroom niet door de persoon die de kast aanraakt. Samen met een zekering of een verliesstroomschakelaar legt dat de kring af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de ene weerstand die je in de plaats van een hele schakeling mag zetten?",
        antwoord=["substitutieweerstand", "de substitutieweerstand", "vervangweerstand"],
        uitleg="De substitutieweerstand, met symbool Rs. Ze laat dezelfde totale stroom lopen bij dezelfde spanning.",
    ),
    dict(
        type="invultekst",
        vraag="Twee weerstanden van 50 Ω staan in serie. Hoe groot is de substitutieweerstand in ohm? Schrijf het getal.",
        antwoord=["100", "100 Ω", "100 ohm"],
        uitleg="In serie tel je op: 50 + 50 = 100 Ω.",
    ),
    dict(
        type="invultekst",
        vraag="Twee weerstanden van 50 Ω staan parallel. Hoe groot is de substitutieweerstand in ohm? Schrijf het getal.",
        antwoord=["25", "25 Ω", "25 ohm"],
        uitleg="Bij twee gelijke weerstanden parallel is Rs de helft: 50 / 2 = 25 Ω.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe sluit je een voltmeter aan ten opzichte van het onderdeel? Schrijf het woord.",
        antwoord=["parallel", "in parallel", "nevenschakeling"],
        uitleg="Parallel, dus over het onderdeel heen. Een ampèremeter zet je in serie.",
    ),
]
