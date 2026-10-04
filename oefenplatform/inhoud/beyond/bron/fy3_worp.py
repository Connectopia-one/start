# -*- coding: utf-8 -*-
"""De horizontale worp — 🌍 Beyond, fysica.

Deel 1 gaat over het onafhankelijkheidsbeginsel: de horizontale beweging is
een ERB en de verticale een vrije val, en die twee weten niets van elkaar.
Daar hoort de vorm van de baan bij, en de klassieke proef waarbij een kogel
die je laat vallen en een kogel die je wegschiet samen de grond raken. Deel 2
is het rekenwerk: valtijd, dracht, hoogteverlies en de snelheid onderweg, en
wat er verandert als je de hoogte of de beginsnelheid wijzigt.

Alle oefeningen rekenen zonder luchtweerstand, zoals de formules van de fiche.
De vragen zeggen dat er ook bij, want in het echt maakt de lucht wel degelijk
een verschil.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt het onafhankelijkheidsbeginsel bij een horizontale worp?",
        opties=[
            "de horizontale en de verticale beweging beïnvloeden elkaar niet",
            "de horizontale beweging wordt door de val afgeremd",
            "de verticale beweging gaat sneller als je harder werpt",
            "de twee bewegingen beginnen pas na elkaar te lopen",
        ],
        antwoord=0,
        uitleg="Je mag ze dus apart uitrekenen en pas achteraf samenvoegen. De tijd is het "
        "enige dat ze gemeen hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voor beweging is het horizontale deel van een horizontale worp?",
        opties=[
            "een eenparig rechtlijnige beweging",
            "een eenparig versnelde beweging",
            "een eenparig vertraagde beweging",
            "een cirkelvormige beweging",
        ],
        antwoord=0,
        uitleg="Zonder luchtweerstand werkt er horizontaal geen kracht, dus blijft die "
        "snelheid constant. Verticaal is het wel een vrije val.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voor beweging is het verticale deel van een horizontale worp?",
        opties=[
            "een vrije val met beginsnelheid nul",
            "een vrije val met een flinke beginsnelheid",
            "een eenparig rechtlijnige beweging omlaag",
            "een beweging met een stijgende versnelling",
        ],
        antwoord=0,
        uitleg="Je werpt horizontaal, dus is de verticale beginsnelheid nul. De zwaartekracht "
        "doet de rest.",
    ),
    dict(
        type="invultekst",
        vraag="Welke vorm heeft de baan van een horizontale worp?",
        antwoord=["parabool", "een parabool", "parabolisch"],
        uitleg="Horizontaal groeit de afstand met t en verticaal met t kwadraat, en samen "
        "geeft dat een parabool. Met luchtweerstand wordt de baan wat steiler aan het "
        "einde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kogels vertrekken tegelijk van dezelfde hoogte: de ene valt gewoon, de andere wordt horizontaal weggeschoten. Welke raakt eerst de grond?",
        opties=[
            "ze raken de grond op hetzelfde ogenblik",
            "de kogel die gewoon valt, want die gaat recht naar beneden",
            "de weggeschoten kogel, want die heeft meer snelheid",
            "dat hangt af van hoe zwaar elke kogel is",
        ],
        antwoord=0,
        uitleg="De verticale beweging is bij allebei dezelfde vrije val. De horizontale "
        "snelheid verandert daar niets aan.",
    ),
    dict(
        type="waarofniet",
        vraag="De valtijd bij een horizontale worp hangt af van de beginsnelheid.",
        antwoord=False,
        uitleg="Ze hangt alleen af van de hoogte en van g. Een grotere beginsnelheid maakt "
        "de worp wel verder, niet langer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de valtijd bij een horizontale worp af? Kruis alles aan wat juist is.",
        opties=[
            "van de hoogte waarvan je werpt",
            "van de valversnelling g",
            "van de horizontale beginsnelheid",
            "van de massa van het voorwerp",
        ],
        antwoord=[0, 1],
        uitleg="De valtijd volgt uit h is een half maal g maal t kwadraat. Noch de "
        "beginsnelheid noch de massa staat daarin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de horizontale snelheid tijdens de vlucht, zonder luchtweerstand?",
        opties=[
            "ze blijft precies even groot",
            "ze wordt steeds kleiner",
            "ze wordt steeds groter",
            "ze wordt nul in het hoogste punt",
        ],
        antwoord=0,
        uitleg="Horizontaal werkt er geen kracht, dus geen versnelling. De verticale snelheid "
        "groeit ondertussen wel gestaag aan.",
    ),
    dict(
        type="waarofniet",
        vraag="De verticale snelheid bij een horizontale worp groeit elke seconde met ongeveer 9,81 m/s aan.",
        antwoord=True,
        uitleg="Dat is precies de valversnelling. De horizontale snelheid blijft ondertussen "
        "onveranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de snelheid van het voorwerp op een bepaald ogenblik tijdens de vlucht?",
        opties=[
            "je stelt de horizontale en de verticale snelheid samen met Pythagoras",
            "je telt de horizontale en de verticale snelheid gewoon op",
            "je neemt de grootste van de twee snelheden",
            "je vermenigvuldigt de twee snelheden met elkaar",
        ],
        antwoord=0,
        uitleg="De twee staan loodrecht op elkaar, dus is de totale snelheid de wortel uit "
        "de som van hun kwadraten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe staat de snelheidsvector van het voorwerp halverwege de vlucht?",
        opties=[
            "schuin naar beneden, raaklijnig aan de baan",
            "recht naar beneden, want de val overheerst",
            "recht vooruit, want de worp was horizontaal",
            "schuin naar boven, tot aan het hoogste punt",
        ],
        antwoord=0,
        uitleg="De snelheid is altijd raaklijnig aan de baan. Hoe verder in de vlucht, hoe "
        "steiler die vector komt te staan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de horizontale afstand die een voorwerp bij een worp aflegt?",
        antwoord=["dracht", "de dracht", "worpafstand"],
        uitleg="Ze is de horizontale snelheid maal de valtijd. Werp je van twee keer zo "
        "hoog, dan wordt ze maar wortel twee keer zo groot.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder luchtweerstand komt een zwaarder voorwerp bij dezelfde worp even ver als een lichter voorwerp.",
        antwoord=True,
        uitleg="De massa staat in geen enkele formule van de worp. In het echt valt een "
        "pingpongbal wel korter dan een golfbal, en dat komt door de lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom valt een pingpongbal in het echt korter dan de formules voorspellen?",
        opties=[
            "de luchtweerstand remt hem horizontaal af",
            "zijn kleine massa maakt de zwaartekracht groter",
            "hij draait rond zijn as en verliest daardoor hoogte",
            "de formules gelden enkel voor zware voorwerpen",
        ],
        antwoord=0,
        uitleg="De formules van de fiche rekenen zonder luchtweerstand. Bij een licht "
        "voorwerp met veel oppervlak is dat verschil het grootst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht werkt er tijdens de vlucht op het voorwerp, zonder luchtweerstand?",
        opties=[
            "enkel de zwaartekracht, recht naar beneden",
            "de zwaartekracht en een voortstuwende kracht vooruit",
            "enkel een kracht in de richting van de beweging",
            "er werkt geen enkele kracht meer op het voorwerp",
        ],
        antwoord=0,
        uitleg="De hand die werpt, heeft het voorwerp al losgelaten. Er is dus geen kracht "
        "meer die het vooruit duwt; het blijft gewoon doorbewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheid is bij de horizontale en de verticale beweging dezelfde?",
        opties=[
            "de tijd",
            "de snelheid",
            "de versnelling",
            "de afgelegde weg",
        ],
        antwoord=0,
        uitleg="Daarom kan je de valtijd uit de verticale beweging halen en hem in de "
        "horizontale gebruiken. De tijd is de brug tussen de twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een horizontale worp zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de baan is een parabool",
            "de horizontale snelheid blijft constant",
            "de verticale snelheid blijft constant",
            "de versnelling wijst in de bewegingsrichting",
        ],
        antwoord=[0, 1],
        uitleg="De versnelling wijst altijd recht naar beneden, ook als het voorwerp schuin "
        "vooruit beweegt. De verticale snelheid groeit juist aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorwerp raakt bij een horizontale worp loodrecht de grond.",
        antwoord=False,
        uitleg="Het heeft nog altijd zijn horizontale snelheid, dus komt het schuin aan. "
        "Alleen bij een beginsnelheid van nul valt het recht naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vliegtuig laat een pakket vallen. Waar komt het pakket terecht ten opzichte van het vliegtuig?",
        opties=[
            "recht onder het vliegtuig, als dat zijn koers aanhoudt",
            "ver achter het vliegtuig, want het verliest zijn snelheid",
            "ver voor het vliegtuig, want het valt sneller vooruit",
            "op de plaats waar het vliegtuig losliet, recht omlaag",
        ],
        antwoord=0,
        uitleg="Het pakket houdt de horizontale snelheid van het vliegtuig. Vanuit de piloot "
        "gezien valt het dus gewoon recht naar beneden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het beginsel dat de horizontale en de verticale beweging los van elkaar verlopen?",
        antwoord=["onafhankelijkheidsbeginsel", "onafhankelijkheid", "het onafhankelijkheidsbeginsel"],
        uitleg="Daardoor mag je elke richting apart behandelen. De tijd is het enige dat ze "
        "delen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een bal wordt horizontaal weggeschoten van 20 m hoog. Hoe lang duurt de val? Neem g gelijk aan 10 m/s².",
        opties=[
            "2 s",
            "4 s",
            "1 s",
            "20 s",
        ],
        antwoord=0,
        uitleg="Uit h is een half maal g maal t kwadraat volgt t kwadraat is 4, dus t is 2 "
        "seconden. De beginsnelheid doet er niet toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Die bal vertrok met 15 m/s. Hoe ver komt hij?",
        opties=[
            "30 m",
            "15 m",
            "60 m",
            "7,5 m",
        ],
        antwoord=0,
        uitleg="De dracht is de horizontale snelheid maal de valtijd: 15 maal 2 is 30 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe snel valt die bal verticaal op het ogenblik dat hij de grond raakt? Neem g gelijk aan 10 m/s².",
        opties=[
            "20 m/s",
            "15 m/s",
            "10 m/s",
            "25 m/s",
        ],
        antwoord=0,
        uitleg="De verticale snelheid is g maal t: 10 maal 2 is 20 meter per seconde. Samen "
        "met de 15 horizontaal geeft dat een totale snelheid van 25 meter per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de dracht als je de beginsnelheid verdubbelt, bij dezelfde hoogte?",
        opties=[
            "ze wordt twee keer zo groot",
            "ze wordt vier keer zo groot",
            "ze blijft precies even groot",
            "ze wordt wortel twee keer zo groot",
        ],
        antwoord=0,
        uitleg="De valtijd verandert niet, en de dracht is snelheid maal tijd. Dus is ze "
        "recht evenredig met de beginsnelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de dracht als je de hoogte verviervoudigt, bij dezelfde beginsnelheid?",
        opties=[
            "ze wordt twee keer zo groot",
            "ze wordt vier keer zo groot",
            "ze wordt zestien keer zo groot",
            "ze blijft precies even groot",
        ],
        antwoord=0,
        uitleg="De valtijd gaat met de wortel van de hoogte, dus vier keer hoger is twee "
        "keer zo lang vallen. De dracht volgt die valtijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De dracht is recht evenredig met de hoogte waarvan je werpt.",
        antwoord=False,
        uitleg="Ze is evenredig met de wortel van de hoogte, want zo gedraagt de valtijd "
        "zich. Met de beginsnelheid is ze wel recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kogel verlaat een tafel van 1,25 m hoog met 4 m/s. Hoe ver van de tafel komt hij neer? Neem g gelijk aan 10 m/s².",
        opties=[
            "2 m",
            "4 m",
            "1 m",
            "5 m",
        ],
        antwoord=0,
        uitleg="De valtijd is 0,5 seconden, want 1,25 is een half maal 10 maal t kwadraat. "
        "De dracht is dan 4 maal 0,5 is 2 meter.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verticale beginsnelheid heeft een voorwerp bij een horizontale worp?",
        antwoord=["nul", "0", "nul m/s"],
        uitleg="Je werpt immers precies horizontaal. Daardoor is de verticale beweging een "
        "gewone vrije val.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel hoogte verliest een bal die horizontaal met 10 m/s wordt weggeschoten na 20 m horizontaal? Neem g gelijk aan 10 m/s².",
        opties=[
            "20 m",
            "10 m",
            "40 m",
            "5 m",
        ],
        antwoord=0,
        uitleg="Na 20 meter horizontaal is er 2 seconden verlopen. Het hoogteverlies is dan "
        "een half maal 10 maal 4 is 20 meter.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee ballen die van dezelfde hoogte horizontaal vertrekken met verschillende snelheid, raken de grond tegelijk.",
        antwoord=True,
        uitleg="De valtijd hangt enkel van de hoogte af. De snellere bal komt alleen veel "
        "verder terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voetbal wordt van een klif van 45 m horizontaal weggetrapt en komt 60 m verder neer. Hoe hard werd hij getrapt? Neem g gelijk aan 10 m/s².",
        opties=[
            "20 m/s",
            "60 m/s",
            "15 m/s",
            "30 m/s",
        ],
        antwoord=0,
        uitleg="De valtijd is 3 seconden, want 45 is een half maal 10 maal 9. Dan is de "
        "beginsnelheid 60 gedeeld door 3 is 20 meter per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden heb je nodig om de dracht te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de hoogte waarvan je werpt",
            "de horizontale beginsnelheid",
            "de massa van het voorwerp",
            "de hoek waaronder je werpt",
        ],
        antwoord=[0, 1],
        uitleg="Samen met g volstaan die twee. Bij een horizontale worp is de hoek per "
        "definitie nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de totale snelheid van een voorwerp dat op het ogenblik van neerkomen 12 m/s horizontaal en 16 m/s verticaal beweegt?",
        opties=[
            "20 m/s",
            "28 m/s",
            "4 m/s",
            "192 m/s",
        ],
        antwoord=0,
        uitleg="Pythagoras: de wortel uit 144 plus 256 is 20 meter per seconde. Gewoon "
        "optellen mag niet, want de twee staan loodrecht op elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="De snelheid van een voorwerp bij een horizontale worp wordt tijdens de vlucht steeds groter.",
        antwoord=True,
        uitleg="De horizontale snelheid blijft gelijk, maar de verticale groeit aan. Samen "
        "wordt de totale snelheid dus groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mik je bij het werpen over een grote afstand hoger dan het doel?",
        opties=[
            "het voorwerp verliest onderweg hoogte door de val",
            "de lucht duwt het voorwerp onderweg naar beneden",
            "het voorwerp wordt onderweg vanzelf zwaarder",
            "de horizontale snelheid neemt onderweg toe",
        ],
        antwoord=0,
        uitleg="Het hoogteverlies gaat met het kwadraat van de horizontale afstand. Hoe "
        "verder het doel, hoe meer je dus hoger moet richten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal rolt van een tafel van 0,8 m hoog. Hoe lang duurt het voor hij de grond raakt? Neem g gelijk aan 10 m/s².",
        opties=[
            "0,4 s",
            "0,8 s",
            "0,16 s",
            "1,6 s",
        ],
        antwoord=0,
        uitleg="0,8 is een half maal 10 maal t kwadraat, dus t kwadraat is 0,16 en t is 0,4 "
        "seconden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hoogteverlies bij een horizontale worp is recht evenredig met de horizontale afstand zelf.",
        antwoord=False,
        uitleg="Het gaat met het kwádraat van die afstand: twee keer zo ver betekent vier "
        "keer zo veel hoogteverlies. Dat is wat de baan tot een parabool maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee identieke ballen rollen van dezelfde tafel, de ene twee keer zo snel als de andere. Wat verschilt er?",
        opties=[
            "enkel de dracht, en die is dubbel zo groot",
            "enkel de valtijd, en die is dubbel zo lang",
            "zowel de dracht als de valtijd verdubbelt",
            "er verandert helemaal niets aan de val",
        ],
        antwoord=0,
        uitleg="De valtijd hangt alleen van de hoogte af. De snellere bal legt in diezelfde "
        "tijd het dubbele af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangen de valtijd en de dracht van een horizontale worp af? Kruis alles aan wat juist is.",
        opties=[
            "de valtijd hangt enkel van de hoogte af",
            "de dracht hangt van de beginsnelheid af",
            "de dracht hangt ook van de hoogte af",
            "de valtijd hangt van de beginsnelheid af",
        ],
        antwoord=[0, 1, 2],
        uitleg="De hoogte bepaalt hoe lang het voorwerp onderweg is, en in die tijd schuift "
        "het met zijn beginsnelheid op. Daarom reken je altijd eerst de valtijd uit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid moet je eerst uitrekenen om een horizontale worp op te lossen?",
        antwoord=["de valtijd", "valtijd", "de tijd"],
        uitleg="Ze volgt uit de hoogte en uit g. Daarna reken je met die tijd de dracht en "
        "de snelheden uit.",
    ),
]
