# -*- coding: utf-8 -*-
"""De vragen voor "De elektrische stroomkring" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technische systemen —
energiesysteem", het stuk over de elektrische stroomkring. Dat stuk is het
uitgebreidste van de hele fiche, vandaar een eigen thema.

Deel 1 gaat over de componenten en hun symbool, de open en de gesloten kring,
en de serie-, parallel- en gemengde schakeling, met de twee voorbeelden van de
fiche: de kerstboomlampjes in parallel en de twee schakelaars van een
heggenschaar in serie.
Deel 2 gaat over de grootheden en eenheden van elektriciteit, de multimeter als
ampèremeter en als voltmeter, de gevaren (kortsluiting, overbelasting,
brandgevaar, elektrocutie), de veiligheidsvoorzieningen en het gereedschap.

De symbolen zelf staan getekend in de leerbundel, niet in de vragen: bij een
oefening staat geen afbeelding, dus elke vraag is in woorden te beantwoorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn elektrische componenten uit de fiche?",
        opties=[
            "Een schakelaar",
            "Een weerstand",
            "Een zoemer",
            "Een schroevendraaier",
            "Een hamer met een houten steel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Componenten zijn de onderdelen die in de kring zelf zitten: de spanningsbron, de draad, de schakelaar, het lampje, de weerstand, de LED, de multimeter en de zoemer. Een schroevendraaier en een hamer zijn gereedschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een schakelaar in een stroomkring?",
        opties=[
            "Hij opent of sluit de kring",
            "Hij maakt de stroom sterker dan daarvoor",
            "Hij zet elektrische stroom om in licht",
            "Hij meet hoeveel stroom er door de kring loopt",
        ],
        antwoord=0,
        uitleg="Een schakelaar onderbreekt de kring of maakt ze weer rond. Meer doet hij niet: hij verandert niets aan de stroom zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="In een open stroomkring loopt er stroom.",
        antwoord=False,
        uitleg="Bij een open kring zit er een onderbreking. De stroom kan dan niet rond, dus er loopt niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer brandt een lampje in een stroomkring?",
        opties=[
            "Als de kring gesloten is",
            "Als de kring ergens open staat",
            "Als de schakelaar los in de doos ligt",
            "Als er een draad uit de kring ontbreekt",
        ],
        antwoord=0,
        uitleg="De stroom moet helemaal rond kunnen, van de ene pool van de bron naar de andere. Zit er ergens een gat, dan brandt er niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een serieschakeling?",
        opties=[
            "De verbruikers liggen achter elkaar in één kring",
            "De verbruikers liggen elk in een eigen tak van de kring",
            "De verbruikers hangen helemaal los van elkaar",
            "De verbruikers zitten in twee kringen naast elkaar",
        ],
        antwoord=0,
        uitleg="In serie loopt er maar één weg. Alle stroom die door het ene onderdeel gaat, gaat daarna door het volgende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de andere lampjes als je één lampje losdraait in een serieschakeling?",
        opties=[
            "Ze gaan allemaal uit",
            "Ze blijven rustig verder branden",
            "Ze branden dan feller dan daarvoor",
            "Er verandert helemaal niets aan de kring",
        ],
        antwoord=0,
        uitleg="Losdraaien maakt de kring open, en in serie is er maar één weg. Dus valt alles uit.",
    ),
    dict(
        type="waarofniet",
        vraag="In een parallelschakeling blijven de andere lampjes branden als er één stuk gaat.",
        antwoord=True,
        uitleg="Elk lampje heeft in parallel zijn eigen tak. Valt er één weg, dan blijven de andere takken gewoon gesloten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan de lampjes van een kerstboom in parallel?",
        opties=[
            "Zodat de andere blijven branden als er één stuk gaat",
            "Zodat ze samen veel minder stroom verbruiken",
            "Zodat je maar één draad nodig hebt in de boom",
            "Zodat ze feller branden dan in een serieschakeling",
        ],
        antwoord=0,
        uitleg="Dat voorbeeld staat letterlijk in de fiche. In serie zou één kapot lampje de hele slinger doven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan de twee schakelaars van een heggenschaar in serie?",
        opties=[
            "Omdat de schaar dan alleen werkt met twee handen",
            "Omdat de motor dan veel sneller kan draaien",
            "Omdat er dan minder stroom nodig is per uur",
            "Omdat de schaar dan een pak langer meegaat",
        ],
        antwoord=0,
        uitleg="In serie moeten beide schakelaars ingedrukt zijn voor de kring gesloten is. Zo kan je geen hand in de messen hebben terwijl de schaar draait.",
    ),
    dict(
        type="invultekst",
        vraag="Een schakeling die een serieschakeling en een parallelschakeling combineert, heet een ___ schakeling.",
        antwoord="gemengde",
        uitleg="In een gemengde schakeling zit een stuk in serie en een stuk in parallel. De meeste toestellen in huis werken zo.",
    ),
    dict(
        type="waarofniet",
        vraag="Een LED laat de stroom in twee richtingen door.",
        antwoord=False,
        uitleg="Een LED werkt maar in één richting. Sluit je hem omgekeerd aan, dan blijft hij donker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen kan je volgens de fiche in serie of in parallel schakelen?",
        opties=[
            "Verbruikers",
            "Schakelaars",
            "Spanningsbronnen",
            "De deur van de kamer",
            "De werktafel in het lokaal",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt uitdrukkelijk verbruikers, schakelaars en spanningsbronnen. Van batterijen achter elkaar krijg je bijvoorbeeld meer spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een batterij?",
        opties=[
            "Een gelijkspanningsbron",
            "Een wisselspanningsbron",
            "Een verbruiker in de kring",
            "Een veiligheidsvoorziening",
        ],
        antwoord=0,
        uitleg="Een batterij of accu levert gelijkspanning: de stroom loopt altijd in dezelfde richting. Een generator levert wisselspanning.",
    ),
    dict(
        type="waarofniet",
        vraag="Een generator levert wisselspanning.",
        antwoord=True,
        uitleg="De stroom uit het stopcontact komt van generatoren en is wisselspanning: de richting draait voortdurend om.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een elektrische geleider of draad?",
        opties=[
            "Hij verbindt de onderdelen met elkaar",
            "Hij houdt de stroom in de kring tegen",
            "Hij meet de spanning van de spanningsbron",
            "Hij zet elektrische stroom om in geluid",
        ],
        antwoord=0,
        uitleg="De draad is de weg waarlangs de stroom loopt. Hij is van koper, want koper geleidt goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk onderdeel zet elektrische stroom om in geluid?",
        opties=["De zoemer", "De LED", "De weerstand", "De schakelaar"],
        antwoord=0,
        uitleg="Een zoemer maakt geluid. Een LED maakt licht, een weerstand remt de stroom af en een schakelaar opent of sluit de kring.",
    ),
    dict(
        type="waarofniet",
        vraag="Een weerstand laat de stroom moeilijker doorlopen.",
        antwoord=True,
        uitleg="Dat is precies waar hij voor dient: de stroom afremmen, zodat er niet te veel door een onderdeel gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat teken je in een elektrisch schema in plaats van een afbeelding van het onderdeel?",
        opties=[
            "Een symbool",
            "Een pijl met de naam erbij",
            "Een cijfer van 1 tot 7 in een kader",
            "Een eigen kleur voor elk onderdeel",
        ],
        antwoord=0,
        uitleg="Elk onderdeel heeft een vast symbool. Zo leest iedereen hetzelfde schema, in welke taal het ook getekend is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heb je nodig om een lampje te laten branden?",
        opties=[
            "Een spanningsbron",
            "Geleidende draden",
            "Het lampje zelf",
            "Een thermometer met een schaal",
            "Een weegschaal met een wijzer",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een bron, draden en een verbruiker, samen tot een gesloten kring. Een thermometer en een weegschaal zijn meetinstrumenten en horen niet in de kring.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schakelaar die open staat, sluit de stroomkring.",
        antwoord=False,
        uitleg="Het is net omgekeerd: open betekent onderbroken. Pas als je de schakelaar sluit, is de kring rond.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van elektrische spanning?",
        opties=["De volt", "De ampère", "De ohm", "De watt"],
        antwoord=0,
        uitleg="Spanning draagt het symbool U en wordt gemeten in volt (V). Stroomsterkte is ampère, weerstand is ohm en vermogen is watt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van stroomsterkte?",
        opties=["De ampère", "De volt", "De joule", "De newton"],
        antwoord=0,
        uitleg="Stroomsterkte draagt het symbool I en wordt gemeten in ampère (A). Joule is de eenheid van energie en newton die van kracht.",
    ),
    dict(
        type="invultekst",
        vraag="Het elektrisch vermogen van een toestel wordt uitgedrukt in ___.",
        antwoord=["watt", "W"],
        uitleg="Vermogen draagt het symbool P en wordt gemeten in watt. Op een lamp of een boormachine staat dat getal erop.",
    ),
    dict(
        type="waarofniet",
        vraag="De elektrische weerstand wordt uitgedrukt in ampère.",
        antwoord=False,
        uitleg="Weerstand wordt uitgedrukt in ohm. Ampère is de eenheid van stroomsterkte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een multimeter in de stand ampèremeter?",
        opties=[
            "Om de stroomsterkte te meten",
            "Om de spanning van de bron te meten",
            "Om de temperatuur van de draad te meten",
            "Om de lengte van een draad te meten",
        ],
        antwoord=0,
        uitleg="Als ampèremeter meet hij hoeveel stroom er loopt. Zet je hem als voltmeter, dan meet hij de spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe test je met een lampje of een materiaal stroom geleidt?",
        opties=[
            "Je zet het materiaal in de kring en kijkt of het lampje brandt",
            "Je houdt het brandende lampje een tijdje tegen het materiaal aan",
            "Je legt het materiaal boven op de batterij en wacht een minuut",
            "Je wrijft met het materiaal over het glas van het lampje heen",
        ],
        antwoord=0,
        uitleg="Je maakt de kring open en legt het materiaal in het gat. Brandt het lampje, dan geleidt het materiaal de stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevaren kunnen er in een elektrische installatie optreden?",
        opties=[
            "Kortsluiting",
            "Overbelasting",
            "Elektrocutie",
            "Verroesting van de muur",
            "Uitdroging van de lucht",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt kortsluiting, overbelasting, brandgevaar en elektrocutie. Roest en droge lucht hebben er niets mee te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Kortsluiting kan brand veroorzaken.",
        antwoord=True,
        uitleg="Bij kortsluiting neemt de stroom een veel te korte weg. De draden worden dan bliksemsnel heet, en dat kan brand geven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is overbelasting?",
        opties=[
            "Er loopt meer stroom door een draad dan hij aankan",
            "Er loopt veel te weinig stroom door de hele kring",
            "De spanning van de batterij is te laag geworden",
            "De schakelaar blijft te lang in de open stand staan",
        ],
        antwoord=0,
        uitleg="Hang je te veel toestellen aan één kring, dan moet de draad meer stroom doorlaten dan waar hij voor gemaakt is. Hij wordt dan warm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een automatische zekering?",
        opties=[
            "Ze onderbreekt de kring bij te veel stroom",
            "Ze maakt de stroom sterker wanneer dat nodig is",
            "Ze meet hoeveel stroom je in een maand verbruikt",
            "Ze zet wisselspanning om in gelijkspanning voor het toestel",
        ],
        antwoord=0,
        uitleg="Een zekering springt eruit zodra er te veel stroom loopt. Zo kan de draad niet oververhitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veiligheidsvoorzieningen voor elektriciteit noemt de fiche?",
        opties=[
            "De aarding",
            "De automatische zekering",
            "De verliesstroomschakelaar",
            "De rookmelder in de gang",
            "Het brandblusapparaat aan de deur",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt de aarding, de automatische zekering, de elektrische isolatie, de dubbele isolatie en de verliesstroomschakelaar. Een rookmelder en een blusapparaat zijn nuttig, maar geen onderdeel van de installatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Dubbele isolatie is een soort gereedschap.",
        antwoord=False,
        uitleg="Dubbele isolatie is een veiligheidsvoorziening: er zit een tweede laag isolatie rond de onderdelen die onder spanning staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de aardingsdraad?",
        opties=[
            "Hij leidt stroom veilig naar de grond weg",
            "Hij maakt de kring een stuk sneller gesloten",
            "Hij vervangt de schakelaar in een grote kring",
            "Hij meet de weerstand van het aangesloten toestel",
        ],
        antwoord=0,
        uitleg="Komt er door een defect spanning op de metalen buitenkant van een toestel, dan loopt die stroom via de aarding weg in plaats van door jou.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram met de bliksemschicht waarschuwt voor gevaar voor elektrische spanning.",
        antwoord=True,
        uitleg="Dat is het pictogram dat je op kasten, deuren en toestellen vindt waar spanning achter zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gereedschap gebruik je om het kunststof laagje van een draad te halen?",
        opties=["Een striptang", "Een kniptang", "Een hamer", "Een verfborstel"],
        antwoord=0,
        uitleg="Een striptang snijdt net diep genoeg om de isolatie los te trekken zonder het koper te beschadigen. Een kniptang knipt de draad door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een soldeerbout?",
        opties=[
            "Om twee draden met tin te verbinden",
            "Om een draad netjes in twee te knippen",
            "Om een schroef in een plank vast te draaien",
            "Om de spanning van een batterij te meten",
        ],
        antwoord=0,
        uitleg="De soldeerbout smelt het tin, en dat tin houdt de twee draden vast als het weer hard wordt. Dat heet een soldeerverbinding.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kroonsteentje dient om een draad door te knippen.",
        antwoord=False,
        uitleg="Een kroonsteentje verbindt twee draden met schroefjes. Knippen doe je met een kniptang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent elektrocutie?",
        opties=[
            "Je krijgt een stroomstoot door je lichaam",
            "Een draad smelt door de warmte in de kring",
            "De zekering springt vanzelf uit haar houder",
            "Een toestel gebruikt te veel stroom per uur",
        ],
        antwoord=0,
        uitleg="Bij elektrocutie loopt er stroom door je lichaam. Daarom mag je een elektrisch toestel nooit met natte handen bedienen.",
    ),
    dict(
        type="invultekst",
        vraag="Een multimeter die je gebruikt om de spanning te meten, noem je een ___.",
        antwoord="voltmeter",
        uitleg="Dezelfde multimeter heet een ampèremeter als je er stroomsterkte mee meet, en een voltmeter als je er spanning mee meet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke materialen kan je gebruiken als geleider in een stroomkring?",
        opties=["Koper", "Aluminium", "Staal", "Hout", "Glas"],
        antwoord=[0, 1, 2],
        uitleg="Metalen geleiden stroom. Hout en glas zijn niet-metalen: die laten bijna niets door en worden juist als isolatie gebruikt.",
    ),
]
