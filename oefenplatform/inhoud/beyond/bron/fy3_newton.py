# -*- coding: utf-8 -*-
"""De wetten van Newton — 🌍 Beyond, fysica.

Deel 1 gaat over de eerste en de tweede wet: traagheid, wat een resulterende
kracht met de bewegingstoestand doet, en het rekenen met F is m maal a, ook
bij een lichaam op een helling of met wrijving. Deel 2 gaat over de derde
wet, actie en reactie, en over het herkennen van de drie wetten in gewone
situaties: de gordel in de auto, de raket, het terugslaan van een geweer en
het duwen tegen een muur.

De lastigste gewoonte om af te leren staat in de eerste wet: beweging heeft
géén kracht nodig om door te gaan, alleen verándering van beweging heeft er
een nodig.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de eerste wet van Newton?",
        opties=[
            "zonder resulterende kracht verandert de bewegingstoestand niet",
            "zonder resulterende kracht komt elk lichaam tot stilstand",
            "elke kracht veroorzaakt een even grote tegenkracht",
            "de versnelling is de kracht gedeeld door de massa",
        ],
        antwoord=0,
        uitleg="Ze heet ook de traagheidswet. Een lichaam blijft dus stilstaan óf eenparig "
        "rechtlijnig doorbewegen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de eerste wet van Newton met één woord?",
        antwoord=["traagheidswet", "traagheid", "de traagheidswet"],
        uitleg="Traagheid is de neiging van een lichaam om zijn bewegingstoestand te "
        "houden. Hoe groter de massa, hoe groter die traagheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vlieg je naar voren als de bus plots remt?",
        opties=[
            "je lichaam wil met dezelfde snelheid door blijven gaan",
            "de bus duwt je met een kracht naar voren toe",
            "de remmen trekken je naar de voorkant van de bus",
            "de zwaartekracht werkt tijdens het remmen vooruit",
        ],
        antwoord=0,
        uitleg="Er werkt geen kracht naar voren op jou: er werkt er juist geen naar achter. "
        "Dat is de traagheidswet, en daarom draag je een gordel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de tweede wet van Newton?",
        opties=[
            "de resulterende kracht is de massa maal de versnelling",
            "de resulterende kracht is de massa gedeeld door de versnelling",
            "de resulterende kracht is de massa maal de snelheid",
            "de resulterende kracht is de snelheid maal de tijd",
        ],
        antwoord=0,
        uitleg="Daaruit volgt dat dezelfde kracht een zwaar lichaam minder versnelt. De "
        "versnelling wijst altijd in de zin van de resulterende kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een lichaam van 4 kg werkt een resulterende kracht van 12 N. Hoe groot is de versnelling?",
        opties=[
            "3 m/s²",
            "48 m/s²",
            "0,33 m/s²",
            "16 m/s²",
        ],
        antwoord=0,
        uitleg="Deel de kracht door de massa: 12 gedeeld door 4 is 3 meter per seconde "
        "kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wagen van 1000 kg en een vrachtwagen van 10 000 kg krijgen dezelfde kracht. Wat gebeurt er?",
        opties=[
            "de wagen versnelt tien keer zo hard als de vrachtwagen",
            "de vrachtwagen versnelt tien keer zo hard als de wagen",
            "beide versnellen even hard, want de kracht is gelijk",
            "de vrachtwagen versnelt niet, want hij is te zwaar",
        ],
        antwoord=0,
        uitleg="De versnelling is de kracht gedeeld door de massa. Tien keer meer massa "
        "betekent dus tien keer minder versnelling.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lichaam dat met constante snelheid rechtdoor beweegt, voelt geen resulterende kracht.",
        antwoord=True,
        uitleg="De afzonderlijke krachten mogen er wel zijn, maar ze heffen elkaar op. Pas "
        "een resulterende kracht verandert de snelheid of de richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de resulterende kracht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is de vectoriële som van alle krachten",
            "ze wijst in dezelfde zin als de versnelling",
            "ze is altijd de grootste van alle krachten",
            "ze is nul zodra het lichaam in beweging komt",
        ],
        antwoord=[0, 1],
        uitleg="Ze kan net zo goed kleiner zijn dan elk van de krachten, bijvoorbeeld als "
        "twee krachten elkaar bijna opheffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke zin wijst de versnelling van een afremmende auto?",
        opties=[
            "tegen de bewegingszin in",
            "in de bewegingszin mee",
            "loodrecht op de beweging omhoog",
            "er is geen versnelling bij afremmen",
        ],
        antwoord=0,
        uitleg="Afremmen is ook een versnelling, maar dan met een tegengestelde zin. De "
        "resulterende kracht wijst dus ook naar achter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist van 5 kg wordt met 20 N geduwd en voelt 5 N wrijving. Hoe groot is de versnelling?",
        opties=[
            "3 m/s²",
            "4 m/s²",
            "5 m/s²",
            "1 m/s²",
        ],
        antwoord=0,
        uitleg="De resulterende kracht is 20 min 5 is 15 newton, en 15 gedeeld door 5 is 3 "
        "meter per seconde kwadraat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere massa heeft bij dezelfde kracht een grotere versnelling.",
        antwoord=False,
        uitleg="Net omgekeerd: massa staat in de noemer. Een zwaarder lichaam is trager te "
        "versnellen én trager te stoppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal rolt een helling af. Welke kracht zorgt voor de versnelling?",
        opties=[
            "de component van de zwaartekracht langs het vlak",
            "de normaalkracht van het hellend vlak omhoog",
            "de wrijvingskracht tussen bal en oppervlak",
            "de kracht waarmee je de bal hebt losgelaten",
        ],
        antwoord=0,
        uitleg="De normaalkracht heft de andere component op. Hoe steiler de helling, hoe "
        "groter de component langs het vlak en dus de versnelling.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je een versnelling uit?",
        antwoord=["m/s²", "m/s2", "meter per seconde²"],
        uitleg="Het is een snelheidsverandering per seconde, dus meter per seconde per "
        "seconde. Op aarde is de valversnelling ongeveer 9,81 van die eenheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de resulterende kracht op een lift die met constante snelheid naar boven gaat?",
        opties=[
            "nul, want de snelheid verandert niet",
            "even groot als de zwaartekracht, naar boven",
            "even groot als de zwaartekracht, naar beneden",
            "twee keer de zwaartekracht, naar boven",
        ],
        antwoord=0,
        uitleg="Constante snelheid betekent geen versnelling, en dus ook geen resulterende "
        "kracht. De spankracht van de kabel is dan precies gelijk aan de zwaartekracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lichaam heeft een voortdurende kracht nodig om met constante snelheid door te blijven bewegen.",
        antwoord=False,
        uitleg="Dat lijkt zo doordat er op aarde altijd wrijving is. In de ruimte blijft een "
        "sonde zonder motor gewoon doorvliegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke situaties zijn voorbeelden van traagheid? Kruis alles aan wat juist is.",
        opties=[
            "je glijdt vooruit als de trein plots afremt",
            "een tafellaken wegtrekken zonder de borden mee",
            "een bal die een helling af naar beneden rolt",
            "een veer die terugveert nadat je ze uitrekt",
        ],
        antwoord=[0, 1],
        uitleg="In beide gevallen houdt een lichaam zijn bewegingstoestand. De bal en de "
        "veer worden juist door een kracht in beweging gebracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht moet je op een lichaam van 2 kg uitoefenen om het vanuit rust in 5 s tot 10 m/s te brengen?",
        opties=[
            "4 N",
            "20 N",
            "1 N",
            "100 N",
        ],
        antwoord=0,
        uitleg="De versnelling is 10 gedeeld door 5 is 2 meter per seconde kwadraat, en 2 "
        "maal 2 is 4 newton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom valt een steen in een luchtledige buis even snel als een veertje?",
        opties=[
            "er is geen luchtweerstand, dus werkt enkel de zwaartekracht",
            "het veertje weegt in een luchtledige buis evenveel als de steen",
            "de zwaartekracht is in een luchtledige buis voor alles gelijk",
            "de buis duwt beide voorwerpen met dezelfde kracht omlaag",
        ],
        antwoord=0,
        uitleg="De zwaartekracht is wel groter op de steen, maar diens massa is evenredig "
        "groter. Kracht gedeeld door massa geeft voor beide dezelfde versnelling.",
    ),
    dict(
        type="waarofniet",
        vraag="De versnelling wijst altijd in dezelfde zin als de resulterende kracht.",
        antwoord=True,
        uitleg="Dat staat in de tweede wet: a is F gedeeld door m, en massa is altijd "
        "positief. Daarom kan je uit de versnelling meteen de zin van de kracht aflezen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid zegt hoe moeilijk een lichaam van bewegingstoestand verandert?",
        antwoord=["massa", "de massa", "traagheid"],
        uitleg="Ze staat in de noemer van de tweede wet. Hoe groter de massa, hoe kleiner "
        "de versnelling bij dezelfde kracht.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de derde wet van Newton?",
        opties=[
            "elke kracht gaat samen met een even grote tegengestelde kracht",
            "elke kracht veroorzaakt een versnelling van hetzelfde lichaam",
            "elke kracht wordt na een tijd vanzelf weer kleiner",
            "elke kracht is de som van alle kleinere krachten",
        ],
        antwoord=0,
        uitleg="Ze heet ook de actie-reactiewet. Let op: de twee krachten werken op "
        "verschillende lichamen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heffen actie en reactie elkaar niet op?",
        opties=[
            "ze werken op twee verschillende lichamen",
            "ze zijn niet precies even groot van elkaar",
            "ze werken niet op hetzelfde ogenblik in",
            "de ene is altijd een beetje later dan de andere",
        ],
        antwoord=0,
        uitleg="Opheffen kan alleen als twee krachten op hetzelfde lichaam werken. Daarom "
        "beweegt een raket wel degelijk vooruit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de derde wet van Newton met één woord?",
        antwoord=["actie-reactiewet", "actie-reactie", "actiereactiewet"],
        uitleg="Kracht en tegenkracht zijn even groot en tegengesteld. Ze grijpen aan op "
        "twee verschillende lichamen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duwt met 200 N tegen een muur. Hoe hard duwt de muur terug?",
        opties=[
            "met 200 N",
            "met 0 N, want de muur beweegt niet",
            "met 400 N, het dubbele van jouw kracht",
            "met 100 N, de helft van jouw kracht",
        ],
        antwoord=0,
        uitleg="Actie en reactie zijn altijd even groot. Dat de muur niet beweegt, komt door "
        "zijn enorme massa en zijn verankering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe komt een raket in de ruimte vooruit?",
        opties=[
            "ze duwt gassen naar achter en die duwen haar naar voren",
            "de uitlaatgassen duwen tegen de lucht achter de raket",
            "ze trekt zichzelf vooruit aan het zwaartekrachtveld",
            "ze stoot zich af tegen de dampkring van de aarde",
        ],
        antwoord=0,
        uitleg="Dat is precies de derde wet. Daarom werkt een raketmotor ook in het luchtledige, "
        "waar er niets is om tegen te duwen.",
    ),
    dict(
        type="waarofniet",
        vraag="Actie en reactie werken op hetzelfde lichaam in.",
        antwoord=False,
        uitleg="Ze werken juist op twee verschillende lichamen. Zouden ze op hetzelfde "
        "lichaam werken, dan zou er nooit iets bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht is de reactie op de zwaartekracht die de aarde op jou uitoefent?",
        opties=[
            "de kracht waarmee jij aan de aarde trekt",
            "de normaalkracht van de vloer op jou",
            "de wrijvingskracht van je schoenen",
            "de spankracht van je spieren",
        ],
        antwoord=0,
        uitleg="Actie en reactie zijn altijd van dezelfde soort en tussen dezelfde twee "
        "lichamen. De normaalkracht hoort bij een ander paar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom slaat een geweer terug bij het afvuren?",
        opties=[
            "de kogel duwt even hard terug als het geweer hem vooruit duwt",
            "het kruit duwt het geweer en de kogel allebei naar voren",
            "de lucht voor de loop duwt het geweer naar achter",
            "de schutter trekt het geweer zelf naar achter toe",
        ],
        antwoord=0,
        uitleg="De twee krachten zijn even groot, maar het geweer is veel zwaarder dan de "
        "kogel. Daarom is de snelheid van de terugslag veel kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van die situaties horen bij de derde wet? Kruis alles aan wat juist is.",
        opties=[
            "een zwemmer die water naar achter duwt",
            "een ballon die leegloopt en wegvliegt",
            "een auto die trager versnelt als hij volgeladen is",
            "een passagier die vooruit schiet bij het remmen",
        ],
        antwoord=[0, 1],
        uitleg="De derde situatie hoort bij de tweede wet en de vierde bij de eerste. Zo "
        "kan je de drie wetten in het dagelijks leven herkennen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als jij op de grond springt, duw jij de aarde ook een beetje weg.",
        antwoord=True,
        uitleg="De kracht op de aarde is precies even groot als die op jou. Door haar enorme "
        "massa is haar versnelling alleen onmeetbaar klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke wet van Newton herken je in een gordel die je bij een botsing tegenhoudt?",
        opties=[
            "de eerste, want je lichaam wil doorbewegen",
            "de tweede, want de kracht deelt door je massa",
            "de derde, want de gordel duwt even hard terug",
            "geen van de drie, want dit is enkel wrijving",
        ],
        antwoord=0,
        uitleg="De auto stopt, maar jij hebt niets dat je tegenhoudt, dus blijf je "
        "doorbewegen. De gordel levert de kracht die dat doorbewegen stopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom buigen voetgangers hun knieën bij het landen van een sprong?",
        opties=[
            "zo duurt het afremmen langer en is de kracht kleiner",
            "zo wordt hun massa tijdens de landing even kleiner",
            "zo valt de zwaartekracht tijdens de landing weg",
            "zo wordt de versnelling van de val juist groter",
        ],
        antwoord=0,
        uitleg="Dezelfde snelheidsverandering in meer tijd betekent een kleinere versnelling. "
        "Volgens de tweede wet is de kracht op de gewrichten dan ook kleiner.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel wetten van Newton zijn er?",
        antwoord=["drie", "3", "er zijn drie"],
        uitleg="De eerste gaat over traagheid, de tweede over kracht en versnelling en de "
        "derde over actie en reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een paard trekt aan een kar met dezelfde kracht als waarmee de kar aan het paard trekt. Waarom komt het geheel toch vooruit?",
        opties=[
            "het paard duwt ook met zijn hoeven tegen de grond",
            "de kracht van het paard is toch een beetje groter",
            "de kar duwt pas terug als hij al in beweging is",
            "de wrijving van de wielen duwt de kar vooruit",
        ],
        antwoord=0,
        uitleg="Voor de beweging van het geheel tellen de krachten van búiten. De grond duwt "
        "het paard vooruit, en dat is de kracht die alles in beweging brengt.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een botsing tussen een vrachtwagen en een auto zijn de twee krachten even groot.",
        antwoord=True,
        uitleg="Dat volgt uit de derde wet. De auto loopt wel veel meer schade op, want "
        "zijn kleinere massa geeft bij dezelfde kracht een veel grotere versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke wet van Newton verklaart waarom een volle winkelkar trager op gang komt?",
        opties=[
            "de tweede, want een grotere massa geeft minder versnelling",
            "de eerste, want de kar wil blijven stilstaan",
            "de derde, want de kar duwt even hard terug",
            "geen van de drie, want dit is enkel wrijving",
        ],
        antwoord=0,
        uitleg="Bij dezelfde duwkracht is de versnelling kleiner. De eerste wet verklaart "
        "alleen waarom hij blijft staan als je niets doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten vormen samen een actie-reactiepaar? Kruis alles aan wat juist is.",
        opties=[
            "de aarde trekt aan de maan en de maan aan de aarde",
            "jij duwt tegen de muur en de muur duwt tegen jou",
            "de zwaartekracht op een boek en de normaalkracht eronder",
            "de motorkracht van een auto en zijn luchtweerstand",
        ],
        antwoord=[0, 1],
        uitleg="De twee laatste paren werken op hetzelfde lichaam, en dat kan niet bij actie "
        "en reactie. Ze heffen elkaar wel op als het lichaam in evenwicht is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lift versnelt naar boven. Wat voel je?",
        opties=[
            "je voelt je zwaarder dan anders",
            "je voelt je lichter dan anders",
            "je voelt precies evenveel als anders",
            "je voelt helemaal geen gewicht meer",
        ],
        antwoord=0,
        uitleg="De vloer moet je niet alleen dragen maar ook versnellen, dus duwt hij harder. "
        "Bij het vertrek naar beneden voel je je juist lichter.",
    ),
    dict(
        type="waarofniet",
        vraag="Een astronaut in een baan rond de aarde voelt geen zwaartekracht meer.",
        antwoord=False,
        uitleg="De zwaartekracht is daar nog bijna even sterk; ze houdt het station juist in "
        "zijn baan. Hij voelt niets doordat hij samen met het station voortdurend valt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke wet van Newton herken je als een tafellaken onder de borden vandaan getrokken wordt?",
        antwoord=["de eerste", "eerste", "traagheidswet"],
        uitleg="De borden houden hun bewegingstoestand, dus blijven ze staan. Dat is de "
        "traagheidswet.",
    ),
]
