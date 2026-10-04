# -*- coding: utf-8 -*-
"""Elektrodynamica: stroom, weerstand en schakelingen — 🌍 Beyond, fysica.

Deel 1 gaat over de grootheden zelf: stroomsterkte, spanning en weerstand, de
wet van Ohm, het elektrisch schema met zijn symbolen, en hoe je een
ampèremeter en een voltmeter aansluit. Deel 2 gaat over het rekenwerk in
schakelingen: serie, parallel en de gemengde schakeling van drie weerstanden
die de fiche uitdrukkelijk noemt.

De vragen geven telkens hele getallen, zodat het kind de redenering kan tonen
zonder rekentoestel. Bij een gemengde schakeling zegt de vraag erbij welke
twee weerstanden samen staan, want een schema tekenen kan hier niet.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de elektrische stroomsterkte?",
        opties=[
            "de lading die per seconde door een doorsnede gaat",
            "de energie die per seconde door een draad gaat",
            "het aantal elektronen dat in de draad aanwezig is",
            "de snelheid waarmee één elektron zich voortbeweegt",
        ],
        antwoord=0,
        uitleg="Het symbool is I en de eenheid de ampère. Eén ampère is één coulomb per "
        "seconde.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de stroomsterkte uit?",
        antwoord=["ampère", "A", "ampere"],
        uitleg="Het symbool van de eenheid is A, dat van de grootheid I. Eén ampère is één "
        "coulomb per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Ohm?",
        opties=[
            "de weerstand is de spanning gedeeld door de stroomsterkte",
            "de weerstand is de spanning maal de stroomsterkte",
            "de weerstand is de stroomsterkte gedeeld door de spanning",
            "de weerstand is de spanning gedeeld door het vermogen",
        ],
        antwoord=0,
        uitleg="R is gelijk aan U gedeeld door I. Zet je er meer spanning op, dan loopt er "
        "bij dezelfde weerstand evenredig meer stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Over een weerstand staat 12 V en er loopt 3 A door. Hoe groot is die weerstand?",
        opties=[
            "4 Ω",
            "36 Ω",
            "0,25 Ω",
            "15 Ω",
        ],
        antwoord=0,
        uitleg="Deel de spanning door de stroomsterkte: 12 gedeeld door 3 is 4 ohm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Door een weerstand van 25 Ω loopt een stroom van 0,4 A. Welke spanning staat erover?",
        opties=[
            "10 V",
            "62,5 V",
            "0,016 V",
            "25,4 V",
        ],
        antwoord=0,
        uitleg="De spanning is de weerstand maal de stroomsterkte: 25 maal 0,4 is 10 volt.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de elektrische weerstand uit?",
        antwoord=["ohm", "Ω", "de ohm"],
        uitleg="Het symbool is de Griekse hoofdletter omega. Eén ohm is één volt per "
        "ampère.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ampèremeter zet je in serie met het onderdeel waarvan je de stroom meet.",
        antwoord=True,
        uitleg="De stroom moet er dan ook echt door. Een voltmeter zet je er juist "
        "parallel over, want die meet het verschil tussen twee punten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een goede ampèremeter een heel kleine eigen weerstand?",
        opties=[
            "anders verandert hij de stroom die hij wil meten",
            "anders geeft hij een te kleine spanning weer",
            "anders wordt hij bij een grote stroom te koud",
            "anders meet hij de spanning in plaats van de stroom",
        ],
        antwoord=0,
        uitleg="Hij staat in serie, dus telt zijn weerstand bij die van de kring. Een "
        "voltmeter heeft om dezelfde reden juist een heel grote weerstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen hebben een eigen symbool in een elektrisch schema? Kruis alles aan wat juist is.",
        opties=[
            "de schakelaar",
            "de voltmeter",
            "de kleur van de draad",
            "de lengte van de kring",
        ],
        antwoord=[0, 1],
        uitleg="Ook de spanningsbron, de weerstand, de lamp en de ampèremeter hebben hun "
        "eigen symbool. Een schema toont de verbindingen, niet de afmetingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen gelijkstroom en wisselstroom?",
        opties=[
            "gelijkstroom loopt altijd in dezelfde zin",
            "gelijkstroom loopt altijd met dezelfde snelheid",
            "gelijkstroom loopt enkel door een metalen draad",
            "gelijkstroom heeft geen spanningsbron nodig",
        ],
        antwoord=0,
        uitleg="Een batterij levert gelijkstroom, het stopcontact wisselstroom. Bij "
        "wisselstroom keert de zin voortdurend om.",
    ),
    dict(
        type="waarofniet",
        vraag="De afgesproken zin van de stroom is die van de positieve lading, dus van plus naar min.",
        antwoord=True,
        uitleg="De elektronen bewegen in werkelijkheid net de andere kant op. Die afspraak "
        "dateert van voor men wist welk deeltje er beweegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de weerstand van een draad af? Kruis alles aan wat juist is.",
        opties=[
            "van de lengte van de draad",
            "van de dikte van de draad",
            "van de spanning die je erop zet",
            "van de stroom die je erdoor stuurt",
        ],
        antwoord=[0, 1],
        uitleg="Ook de stof en de temperatuur spelen mee. Spanning en stroom bepalen de "
        "weerstand niet, ze volgen er juist uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het toestel dat de spanning tussen twee punten meet?",
        antwoord=["voltmeter", "een voltmeter", "de voltmeter"],
        uitleg="Je zet hem parallel over het onderdeel. De ampèremeter zet je juist in "
        "serie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een draad warm als er stroom door loopt?",
        opties=[
            "de elektronen botsen tegen de atomen van het rooster",
            "de elektronen wrijven langs de buitenkant van de draad",
            "de spanningsbron stuurt warmte mee de draad in",
            "de lucht rond de draad wordt door de lading geduwd",
        ],
        antwoord=0,
        uitleg="Bij elke botsing geven de elektronen wat energie af aan het rooster, en dat "
        "trilt heviger. Dat is precies wat weerstand betekent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schakelaar in open stand laat de stroom gewoon verder lopen.",
        antwoord=False,
        uitleg="Een open schakelaar onderbreekt de kring, en dan loopt er nergens stroom. "
        "De stroom heeft een gesloten weg nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de stroom als je bij gelijke spanning de weerstand verdubbelt?",
        opties=[
            "de stroom wordt half zo groot",
            "de stroom wordt twee keer zo groot",
            "de stroom blijft precies even groot",
            "de stroom wordt vier keer zo klein",
        ],
        antwoord=0,
        uitleg="I is gelijk aan U gedeeld door R, dus stroom en weerstand zijn omgekeerd "
        "evenredig bij vaste spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lamp van 6 Ω staat op een bron van 9 V. Hoeveel stroom loopt er?",
        opties=[
            "1,5 A",
            "54 A",
            "0,67 A",
            "15 A",
        ],
        antwoord=0,
        uitleg="Deel de spanning door de weerstand: 9 gedeeld door 6 is 1,5 ampère.",
    ),
    dict(
        type="waarofniet",
        vraag="In een stroomkring worden de elektronen door de draad opgebruikt.",
        antwoord=False,
        uitleg="Er verdwijnt geen enkel elektron: er loopt er evenveel terug naar de bron "
        "als eruit vertrekt. Wat opgebruikt wordt, is energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de wet van Ohm zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de spanning is de weerstand maal de stroomsterkte",
            "bij gelijke spanning geeft een grotere weerstand een kleinere stroom",
            "ze geldt voor een weerstand waarvan de waarde niet verandert",
            "de weerstand van een draad hangt af van de spanning die je aanlegt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De weerstand is een eigenschap van de draad zelf, niet van de bron. Met een "
        "regelbare weerstand stel je de stroom in een kring in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een tekening van een stroomkring met symbolen in plaats van voorwerpen?",
        antwoord=["elektrisch schema", "schema", "een schema"],
        uitleg="Het toont welke onderdelen met elkaar verbonden zijn. De werkelijke plaats "
        "of lengte van de draden doet er niet toe.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor de stroomsterkte in een serieschakeling?",
        opties=[
            "ze is in elk onderdeel even groot",
            "ze verdeelt zich over de onderdelen",
            "ze is in het laatste onderdeel het kleinst",
            "ze is in het eerste onderdeel het grootst",
        ],
        antwoord=0,
        uitleg="Er is maar één weg, dus moet alles er overal door. De spanning verdeelt "
        "zich wel over de onderdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt er in een parallelschakeling voor de spanning en de stroom? Kruis alles aan wat juist is.",
        opties=[
            "over elke tak staat dezelfde spanning",
            "de stromen van de takken tellen samen tot de hoofdstroom",
            "door de kleinste weerstand loopt de grootste stroom",
            "door elke tak loopt dezelfde stroom",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dezelfde stroom door alles hoort bij een serieschakeling. Elke tak heeft hier "
        "zijn eigen weg naar de bron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee weerstanden van 4 Ω en 6 Ω staan in serie. Wat is de vervangingsweerstand?",
        opties=[
            "10 Ω",
            "2,4 Ω",
            "24 Ω",
            "5 Ω",
        ],
        antwoord=0,
        uitleg="In serie tel je de weerstanden gewoon op: 4 plus 6 is 10 ohm. De "
        "vervangingsweerstand is dus altijd groter dan de grootste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee weerstanden van 4 Ω en 6 Ω staan parallel. Wat is de vervangingsweerstand?",
        opties=[
            "2,4 Ω",
            "10 Ω",
            "5 Ω",
            "24 Ω",
        ],
        antwoord=0,
        uitleg="Het product gedeeld door de som: 24 gedeeld door 10 is 2,4 ohm. Parallel "
        "ligt het resultaat altijd onder de kleinste van de twee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de ene weerstand die je in de plaats van een hele schakeling mag denken?",
        antwoord=["vervangingsweerstand", "substitutieweerstand", "vervangweerstand"],
        uitleg="Ze geeft bij dezelfde spanning dezelfde totale stroom. Daarmee reken je een "
        "schakeling stap voor stap uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee gelijke weerstanden parallel geven samen de helft van één ervan.",
        antwoord=True,
        uitleg="Twee van 10 ohm geven samen 5 ohm. Er zijn immers twee even brede wegen "
        "voor de stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie weerstanden van 2 Ω, 3 Ω en 5 Ω staan in serie op een bron van 20 V. Hoeveel stroom loopt er?",
        opties=[
            "2 A",
            "10 A",
            "4 A",
            "0,5 A",
        ],
        antwoord=0,
        uitleg="Samen is dat 10 ohm, en 20 gedeeld door 10 is 2 ampère. Door elke weerstand "
        "loopt diezelfde 2 ampère.",
    ),
    dict(
        type="meerkeuze",
        vraag="In diezelfde serieschakeling van 2 Ω, 3 Ω en 5 Ω met 2 A: welke spanning staat er over de weerstand van 3 Ω?",
        opties=[
            "6 V",
            "20 V",
            "3 V",
            "1,5 V",
        ],
        antwoord=0,
        uitleg="U is R maal I: 3 maal 2 is 6 volt. De drie deelspanningen van 4, 6 en 10 "
        "volt zijn samen weer 20 volt.",
    ),
    dict(
        type="waarofniet",
        vraag="In een serieschakeling is de som van de deelspanningen groter dan de bronspanning.",
        antwoord=False,
        uitleg="Ze is er juist precies gelijk aan. De energie die een lading bij de bron "
        "krijgt, geeft ze onderweg stuk voor stuk af, en meer dan dat kan ze niet "
        "afgeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee weerstanden van 6 Ω en 12 Ω staan parallel op 24 V. Hoeveel stroom levert de bron?",
        opties=[
            "6 A",
            "4 A",
            "2 A",
            "1,33 A",
        ],
        antwoord=0,
        uitleg="Door de eerste loopt 4 ampère en door de tweede 2 ampère, samen 6 ampère. "
        "Dat klopt ook met de vervangingsweerstand van 4 ohm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een parallelschakeling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de totale stroom is de som van de deelstromen",
            "de vervangingsweerstand is kleiner dan de kleinste weerstand",
            "de totale spanning is de som van de deelspanningen",
            "de vervangingsweerstand is de som van de weerstanden",
        ],
        antwoord=[0, 1],
        uitleg="De twee laatste gelden juist voor een serieschakeling. Elke tak die je "
        "bijzet, maakt de totale weerstand kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijven de andere lampen branden als er in een parallelschakeling één lamp stukgaat?",
        opties=[
            "elke lamp heeft haar eigen weg naar de bron",
            "de andere lampen nemen de stroom van die lamp over",
            "een parallelschakeling heeft geen gesloten kring nodig",
            "de bron verhoogt dan vanzelf haar spanning een beetje",
        ],
        antwoord=0,
        uitleg="Er zijn evenveel gesloten kringen als takken. In een serieschakeling is er "
        "maar één weg, en daar valt alles uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe staan de lampen geschakeld als één kapotte lamp de hele reeks dooft?",
        antwoord=["in serie", "serie", "serieschakeling"],
        uitleg="De kring is dan onderbroken, dus loopt er nergens nog stroom. Parallel "
        "blijft de rest wel branden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een weerstand van 10 Ω staat in serie met twee parallelle weerstanden van elk 20 Ω. Wat is de totale weerstand?",
        opties=[
            "20 Ω",
            "50 Ω",
            "30 Ω",
            "10 Ω",
        ],
        antwoord=0,
        uitleg="De twee parallelle geven samen 10 ohm, en die staan in serie met de eerste: "
        "10 plus 10 is 20 ohm. Werk bij een gemengde schakeling altijd van binnen naar "
        "buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Die schakeling staat op 40 V. Hoeveel stroom levert de bron?",
        opties=[
            "2 A",
            "4 A",
            "1 A",
            "0,5 A",
        ],
        antwoord=0,
        uitleg="De totale weerstand is 20 ohm, en 40 gedeeld door 20 is 2 ampère. Die hele "
        "stroom gaat door de weerstand van 10 ohm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde schakeling: welke spanning staat er over het parallelle stuk?",
        opties=[
            "20 V",
            "40 V",
            "10 V",
            "4 V",
        ],
        antwoord=0,
        uitleg="Over de weerstand van 10 ohm staat 10 maal 2 is 20 volt, dus blijft er van "
        "de 40 volt nog 20 volt over voor het parallelle stuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een gemengde schakeling reken je eerst het parallelle stuk uit en pas daarna de serie.",
        antwoord=True,
        uitleg="Je vervangt het parallelle stuk door één weerstand en houdt zo een gewone "
        "serieschakeling over. Van binnen naar buiten werken houdt het overzichtelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een serieschakeling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "door elke weerstand loopt dezelfde stroom",
            "de spanningen over de weerstanden tellen samen tot de bronspanning",
            "de vervangingsweerstand is de som van de weerstanden",
            "valt één weerstand weg, dan blijft de rest werken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Valt er één weg, dan is de kring open en staat alles stil. Dat blijven "
        "werken hoort bij een parallelschakeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer weerstanden je parallel bijzet, hoe groter de totale weerstand wordt.",
        antwoord=False,
        uitleg="Net omgekeerd: elke extra tak is een extra weg voor de stroom, dus daalt de "
        "totale weerstand. In serie stijgt ze wel.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid is in een serieschakeling overal even groot?",
        antwoord=["de stroomsterkte", "stroomsterkte", "de stroom"],
        uitleg="Er is maar één weg, dus gaat overal dezelfde lading per seconde langs. In "
        "een parallelschakeling is juist de spanning overal gelijk.",
    ),
]
