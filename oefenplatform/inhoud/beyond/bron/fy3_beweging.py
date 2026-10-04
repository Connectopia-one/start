# -*- coding: utf-8 -*-
"""Rechtlijnige beweging: ERB en EVRB — 🌍 Beyond, fysica.

Deel 1 gaat over de eenparig rechtlijnige beweging en over het lezen van de
drie bewegingsgrafieken: wat de steilheid van een x(t)-grafiek betekent, wat
de oppervlakte onder een v(t)-grafiek voorstelt, en het verschil tussen
afgelegde weg en verplaatsing, en tussen gemiddelde en ogenblikkelijke
snelheid. Deel 2 gaat over de eenparig veranderlijke beweging: versnellen en
vertragen, de formules met en zonder beginsnelheid, de vrije val, de
verticale worp en inhaalproblemen.

De fiche vraagt om grafieken op te stellen; dat kan hier niet, dus vragen de
vragen naar het verloop van zo'n grafiek in woorden en naar wat je eruit
afleest.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een eenparig rechtlijnige beweging?",
        opties=[
            "een beweging op een rechte lijn met constante snelheid",
            "een beweging op een rechte lijn met constante versnelling",
            "een beweging op een cirkel met constante snelheid",
            "een beweging waarbij de snelheid gelijkmatig toeneemt",
        ],
        antwoord=0,
        uitleg="De versnelling is dan nul, dus is ook de resulterende kracht nul. Dat is de "
        "eerste wet van Newton.",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor staat de afkorting ERB?",
        antwoord=["eenparig rechtlijnige beweging", "eenparig rechtlijnig", "ERB"],
        uitleg="De snelheid blijft daarbij constant in grootte én in zin. Verandert de "
        "snelheid gelijkmatig, dan spreek je van een EVRB.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de x(t)-grafiek van een ERB eruit?",
        opties=[
            "een rechte met een constante helling",
            "een rechte die evenwijdig met de tijdas loopt",
            "een parabool die steeds steiler wordt",
            "een kromme die naar een vaste waarde toe buigt",
        ],
        antwoord=0,
        uitleg="De helling van die rechte is precies de snelheid. Bij een EVRB krijg je wel "
        "een parabool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af uit de helling van een x(t)-grafiek?",
        opties=[
            "de snelheid op dat ogenblik",
            "de versnelling op dat ogenblik",
            "de afgelegde weg tot dan toe",
            "de kracht die op het lichaam werkt",
        ],
        antwoord=0,
        uitleg="Positie per tijd is snelheid. De helling van een v(t)-grafiek geeft op "
        "dezelfde manier de versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de oppervlakte onder een v(t)-grafiek voor?",
        opties=[
            "de verplaatsing van het lichaam",
            "de versnelling van het lichaam",
            "de kracht op het lichaam",
            "de tijd die het lichaam onderweg was",
        ],
        antwoord=0,
        uitleg="Snelheid maal tijd is afstand, en dat is precies wat die oppervlakte "
        "voorstelt. Ligt een stuk onder de as, dan telt het negatief mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Afgelegde weg en verplaatsing zijn altijd even groot.",
        antwoord=False,
        uitleg="Wie heen en weer loopt, legt een weg af maar heeft een verplaatsing van nul. "
        "Alleen bij een beweging in één zin vallen de twee samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser rijdt 3 km naar het noorden en daarna 3 km terug. Hoe groot zijn de afgelegde weg en de verplaatsing?",
        opties=[
            "weg 6 km en verplaatsing 0 km",
            "weg 0 km en verplaatsing 6 km",
            "weg 6 km en verplaatsing 6 km",
            "weg 3 km en verplaatsing 3 km",
        ],
        antwoord=0,
        uitleg="De verplaatsing is het verschil tussen begin- en eindpunt, en dat is nul. De "
        "weg telt elke meter mee, ook de terugweg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de gemiddelde en de ogenblikkelijke snelheid?",
        opties=[
            "de gemiddelde snelheid kijkt naar een heel traject, de ogenblikkelijke naar één moment",
            "de gemiddelde snelheid is altijd kleiner dan de ogenblikkelijke snelheid",
            "de gemiddelde snelheid geldt enkel voor een ERB en de andere voor een EVRB",
            "de gemiddelde snelheid staat in meter per seconde en de andere in kilometer per uur",
        ],
        antwoord=0,
        uitleg="De ogenblikkelijke snelheid lees je af op de snelheidsmeter. Bij een ERB "
        "zijn de twee gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel meter per seconde is 72 km/h?",
        antwoord=["20", "20 m/s", "twintig"],
        uitleg="Deel door 3,6 om van kilometer per uur naar meter per seconde te gaan. "
        "Omgekeerd vermenigvuldig je met 3,6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt 150 km in 2 uur. Wat is zijn gemiddelde snelheid?",
        opties=[
            "75 km/h",
            "300 km/h",
            "50 km/h",
            "25 km/h",
        ],
        antwoord=0,
        uitleg="Deel de afstand door de tijd: 150 gedeeld door 2 is 75 kilometer per uur. "
        "Hoe hard hij onderweg reed, weet je daarmee niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een a(t)-grafiek van een ERB valt samen met de tijdas.",
        antwoord=True,
        uitleg="De versnelling is er nul, dus loopt de lijn op de hoogte nul. Bij een EVRB "
        "loopt ze horizontaal op een andere hoogte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een x(t)-grafiek zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de helling van de grafiek is de snelheid",
            "een horizontaal stuk betekent dat het lichaam stilstaat",
            "een dalend stuk betekent dat het terugkeert naar het vertrekpunt",
            "de oppervlakte onder de grafiek is de verplaatsing",
        ],
        antwoord=[0, 1, 2],
        uitleg="De oppervlakte onder een v(t)-grafiek is de verplaatsing, niet die onder een "
        "x(t)-grafiek. Daar lees je de plaats rechtstreeks op de verticale as af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een snelheid zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze heeft een grootte, een richting en een zin",
            "ze wordt voorgesteld door een vector",
            "ze is altijd positief, hoe het lichaam ook beweegt",
            "ze wordt in meter per seconde kwadraat uitgedrukt",
        ],
        antwoord=[0, 1],
        uitleg="Beweegt een lichaam tegen de zin van de x-as, dan is de snelheid langs die "
        "as negatief. Meter per seconde kwadraat is de eenheid van versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een x(t)-grafiek loopt eerst stijgend en daarna dalend. Wat doet het lichaam?",
        opties=[
            "het keert onderweg om en komt terug",
            "het versnelt eerst en vertraagt dan",
            "het staat eerst stil en vertrekt daarna",
            "het beweegt de hele tijd dezelfde kant op",
        ],
        antwoord=0,
        uitleg="De helling wisselt van teken, dus ook de snelheid. Op het hoogste punt van "
        "de grafiek is de snelheid even nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Een snelheid langs de x-as kan nooit negatief zijn.",
        antwoord=False,
        uitleg="Ze kan dat wel: het teken zegt de zin van de beweging langs die as. Alleen "
        "de grootte van de snelheid blijft altijd positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om een gemiddelde snelheid te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de afgelegde weg",
            "de tijdsduur van de beweging",
            "de massa van het lichaam",
            "de versnelling van het lichaam",
        ],
        antwoord=[0, 1],
        uitleg="Je deelt de afgelegde weg door de tijdsduur. De massa en de versnelling doen "
        "daar niets toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee fietsers vertrekken samen, de ene met 4 m/s en de andere met 6 m/s. Hoe ver liggen ze na 30 s uit elkaar?",
        opties=[
            "60 m",
            "300 m",
            "120 m",
            "30 m",
        ],
        antwoord=0,
        uitleg="Het verschil in snelheid is 2 meter per seconde: 2 maal 30 is 60 meter. Je "
        "kan ook beide afstanden apart uitrekenen en aftrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een trein rijdt met 20 m/s. Hoe ver komt hij in 2 minuten?",
        opties=[
            "2400 m",
            "40 m",
            "1200 m",
            "240 m",
        ],
        antwoord=0,
        uitleg="Zet de tijd eerst om: 2 minuten is 120 seconden, en 20 maal 120 is 2400 "
        "meter.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid lees je af uit de oppervlakte onder een v(t)-grafiek?",
        antwoord=["de verplaatsing", "verplaatsing", "de afgelegde weg"],
        uitleg="Snelheid maal tijd is afstand. De helling van diezelfde grafiek geeft de "
        "versnelling.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een ERB zijn de gemiddelde en de ogenblikkelijke snelheid even groot.",
        antwoord=True,
        uitleg="De snelheid verandert niet, dus kan het gemiddelde niet anders uitvallen. "
        "Bij een EVRB lopen de twee wel uiteen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een eenparig veranderlijke rechtlijnige beweging zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de versnelling blijft dezelfde",
            "de v(t)-grafiek is een rechte",
            "de x(t)-grafiek is een parabool",
            "de snelheid blijft dezelfde",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een constante snelheid hoort juist bij een eenparige beweging. Hier verandert "
        "de snelheid elke seconde met dezelfde hoeveelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de v(t)-grafiek van een EVRB eruit?",
        opties=[
            "een schuine rechte",
            "een horizontale rechte",
            "een parabool die opent naar boven",
            "een kromme die afvlakt naar een grens",
        ],
        antwoord=0,
        uitleg="De helling van die rechte is de versnelling. De x(t)-grafiek is dan een "
        "parabool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto gaat in 8 s van 0 naar 24 m/s. Hoe groot is zijn versnelling?",
        opties=[
            "3 m/s²",
            "192 m/s²",
            "0,33 m/s²",
            "32 m/s²",
        ],
        antwoord=0,
        uitleg="De snelheidsverandering gedeeld door de tijd: 24 gedeeld door 8 is 3 meter "
        "per seconde kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser remt van 10 m/s naar stilstand in 5 s. Hoe groot is zijn versnelling?",
        opties=[
            "−2 m/s²",
            "2 m/s²",
            "−50 m/s²",
            "−0,5 m/s²",
        ],
        antwoord=0,
        uitleg="Het teken min betekent dat de versnelling tegen de bewegingszin in wijst. "
        "Dat noemt men ook een vertraging.",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve versnelling betekent altijd dat het lichaam vertraagt.",
        antwoord=False,
        uitleg="Het betekent dat de versnelling tegen de zin van de as in wijst. Beweegt het "
        "lichaam ook die kant op, dan versnelt het juist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wagen vertrekt uit rust met 2 m/s². Hoe ver komt hij in 6 s?",
        opties=[
            "36 m",
            "12 m",
            "72 m",
            "6 m",
        ],
        antwoord=0,
        uitleg="De afstand is een half maal a maal t kwadraat: 0,5 maal 2 maal 36 is 36 "
        "meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde wagen: hoe snel rijdt hij na die 6 s?",
        opties=[
            "12 m/s",
            "36 m/s",
            "6 m/s",
            "3 m/s",
        ],
        antwoord=0,
        uitleg="De snelheid is a maal t: 2 maal 6 is 12 meter per seconde. De gemiddelde "
        "snelheid over die rit was maar 6 meter per seconde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de valversnelling op aarde ongeveer?",
        antwoord=["9,81 m/s²", "9,81", "ongeveer 10"],
        uitleg="Men rekent vaak met 9,81 of afgerond met 10. Op de maan is ze zes keer "
        "kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe snel valt een steen na 3 s vrije val, met g gelijk aan 10 m/s²?",
        opties=[
            "30 m/s",
            "45 m/s",
            "10 m/s",
            "3,3 m/s",
        ],
        antwoord=0,
        uitleg="De snelheid is g maal t: 10 maal 3 is 30 meter per seconde. De afgelegde "
        "hoogte is daarbij 45 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe diep is een put als een steen er 2 s over doet om de bodem te raken? Neem g gelijk aan 10 m/s².",
        opties=[
            "20 m",
            "40 m",
            "10 m",
            "5 m",
        ],
        antwoord=0,
        uitleg="De hoogte is een half maal g maal t kwadraat: 0,5 maal 10 maal 4 is 20 "
        "meter. Het geluid van de plons doet er ook nog even over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vrije val hangt de valtijd af van de massa van het voorwerp.",
        antwoord=False,
        uitleg="Zonder luchtweerstand valt alles even snel. De zwaartekracht is wel groter "
        "op een zware massa, maar die massa is evenredig moeilijker te versnellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit een bal recht omhoog. Wat gebeurt er in het hoogste punt?",
        opties=[
            "de snelheid is nul en de versnelling niet",
            "de snelheid en de versnelling zijn allebei nul",
            "de versnelling is nul en de snelheid niet",
            "de versnelling keert daar van zin om",
        ],
        antwoord=0,
        uitleg="De zwaartekracht blijft ook in het hoogste punt werken, dus blijft de "
        "versnelling 9,81 omlaag. Daarom valt de bal meteen weer terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit een bal met 20 m/s recht omhoog. Hoe lang duurt het tot hij het hoogste punt bereikt? Neem g gelijk aan 10 m/s².",
        opties=[
            "2 s",
            "4 s",
            "1 s",
            "20 s",
        ],
        antwoord=0,
        uitleg="De snelheid moet van 20 naar nul met 10 per seconde eraf. De hele vlucht "
        "duurt dus 4 seconden, want het terugvallen duurt even lang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bewegingen zijn een EVRB? Kruis alles aan wat juist is.",
        opties=[
            "een vrije val zonder luchtweerstand",
            "een auto die gelijkmatig optrekt",
            "een fietser die met constante snelheid rijdt",
            "een kind op een draaimolen aan één stuk door",
        ],
        antwoord=[0, 1],
        uitleg="Bij een draaimolen verandert de richting voortdurend, dus is de beweging "
        "niet rechtlijnig. Een constante snelheid hoort bij een ERB.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt met 15 m/s en remt met 3 m/s². Hoeveel meter heeft hij nodig om te stoppen?",
        opties=[
            "37,5 m",
            "75 m",
            "5 m",
            "22,5 m",
        ],
        antwoord=0,
        uitleg="Gebruik v kwadraat gedeeld door 2 maal a: 225 gedeeld door 6 is 37,5 meter. "
        "Bij de dubbele snelheid is die remweg vier keer zo lang.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij dubbele snelheid is de remweg vier keer zo lang.",
        antwoord=True,
        uitleg="De remweg gaat met het kwadraat van de snelheid. Daarom is een kleine "
        "snelheidsverhoging in de bebouwde kom zo gevaarlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wagen rijdt met 20 m/s voorbij een stilstaande motor, die meteen vertrekt met 4 m/s². Wanneer haalt de motor hem in?",
        opties=[
            "na 10 s",
            "na 5 s",
            "na 20 s",
            "na 2 s",
        ],
        antwoord=0,
        uitleg="Stel de twee afstanden gelijk: 20 maal t is 0,5 maal 4 maal t kwadraat. Dat "
        "geeft t is 10 seconden, en dan hebben beide 200 meter afgelegd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een vrije val zonder luchtweerstand zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de versnelling blijft de hele val even groot",
            "de snelheid groeit recht evenredig met de tijd",
            "de afgelegde hoogte groeit met het kwadraat van de tijd",
            "een zwaarder voorwerp valt sneller naar beneden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zonder luchtweerstand vallen een steen en een pluim even snel. De massa staat "
        "niet in de formules van een vrije val.",
    ),
    dict(
        type="waarofniet",
        vraag="De oppervlakte onder een a(t)-grafiek geeft de snelheidsverandering.",
        antwoord=True,
        uitleg="Versnelling maal tijd is snelheid, net zoals snelheid maal tijd afstand is. "
        "De drie grafieken hangen zo met elkaar samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een beweging waarbij enkel de zwaartekracht werkt en de beginsnelheid nul is?",
        antwoord=["vrije val", "een vrije val", "val"],
        uitleg="Ze is een EVRB met een versnelling van 9,81 meter per seconde kwadraat. "
        "Gooi je het voorwerp eerst omhoog, dan spreek je van een verticale worp.",
    ),
]
