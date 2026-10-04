# -*- coding: utf-8 -*-
"""De gravitatiekracht en de cirkelbeweging — 🌍 Beyond, fysica.

Deel 1 gaat over de eenparig cirkelvormige beweging: periode, frequentie,
hoeksnelheid en baansnelheid, en waarom een lichaam dat met constante
snelheid rondgaat tóch een versnelling heeft. Deel 2 gaat over de
gravitatiekracht: de universele gravitatiewet, het gravitatieveld dat net als
het elektrisch veld radiaal is, het verband tussen zwaartekracht en
gravitatiekracht, en satellieten die precies door de gravitatie in hun baan
worden gehouden.

De twee onderdelen komen bij de satelliet samen: de gravitatiekracht is daar
de middelpuntzoekende kracht, en uit die gelijkheid volgt de baansnelheid en
de hoogte.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer voert een lichaam een eenparig cirkelvormige beweging uit?",
        opties=[
            "als het een cirkel beschrijft met een constante baansnelheid",
            "als het een cirkel beschrijft met een stijgende baansnelheid",
            "als het rechtdoor gaat met een constante versnelling",
            "als het heen en weer beweegt rond een evenwichtsstand",
        ],
        antwoord=0,
        uitleg="De grootte van de snelheid blijft gelijk, maar haar richting verandert "
        "voortdurend. Daarom is er wel degelijk een versnelling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de tijd die een lichaam nodig heeft voor één volledige omwenteling?",
        antwoord=["periode", "de periode", "omlooptijd"],
        uitleg="Het symbool is T en de eenheid de seconde. De frequentie is precies haar "
        "omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wiel draait 120 keer per minuut rond. Wat is zijn frequentie?",
        opties=[
            "2 Hz",
            "120 Hz",
            "60 Hz",
            "0,5 Hz",
        ],
        antwoord=0,
        uitleg="Deel door 60 om van omwentelingen per minuut naar per seconde te gaan. De "
        "periode is dan een halve seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de hoeksnelheid?",
        opties=[
            "de afgelegde hoek per seconde",
            "de afgelegde weg per seconde",
            "het aantal omwentelingen per seconde",
            "de hoek tussen snelheid en versnelling",
        ],
        antwoord=0,
        uitleg="Ze staat in radialen per seconde en is twee pi gedeeld door de periode. De "
        "baansnelheid is de hoeksnelheid maal de straal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een draaimolen draait met een hoeksnelheid van 0,5 rad/s. Hoe snel beweegt een kind op 4 m van het midden?",
        opties=[
            "2 m/s",
            "8 m/s",
            "0,125 m/s",
            "0,5 m/s",
        ],
        antwoord=0,
        uitleg="De baansnelheid is omega maal r: 0,5 maal 4 is 2 meter per seconde. Verder "
        "van het midden beweeg je dus sneller.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee kinderen op dezelfde draaimolen hebben dezelfde hoeksnelheid, ook al zitten ze niet even ver van het midden.",
        antwoord=True,
        uitleg="Ze doen er even lang over om rond te gaan, dus is hun hoek per seconde "
        "gelijk. Hun baansnelheid verschilt wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een lichaam in een ECB toch een versnelling?",
        opties=[
            "de richting van de snelheid verandert voortdurend",
            "de grootte van de snelheid verandert voortdurend",
            "de massa van het lichaam verandert tijdens de beweging",
            "de tijd die het per ronde nodig heeft, wordt steeds korter",
        ],
        antwoord=0,
        uitleg="Versnelling betekent een verandering van de snelheidsvector, en die heeft "
        "ook een richting. Daarom is er een middelpuntzoekende versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kant op wijst de middelpuntzoekende versnelling?",
        opties=[
            "naar het middelpunt van de cirkel",
            "weg van het middelpunt van de cirkel",
            "in de zin van de beweging langs de cirkel",
            "tegen de zin van de beweging in",
        ],
        antwoord=0,
        uitleg="Daarom heet ze centripetaal, wat middelpuntzoekend betekent. De snelheid "
        "staat er loodrecht op, raaklijnig aan de cirkel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de versnelling die naar het middelpunt van de cirkel wijst?",
        antwoord=["centripetale versnelling", "centripetaal", "middelpuntzoekende"],
        uitleg="Ze is v kwadraat gedeeld door r. De kracht die haar veroorzaakt, heet de "
        "middelpuntzoekende kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt met 10 m/s door een bocht met een straal van 20 m. Hoe groot is de centripetale versnelling?",
        opties=[
            "5 m/s²",
            "0,5 m/s²",
            "2 m/s²",
            "200 m/s²",
        ],
        antwoord=0,
        uitleg="De versnelling is v kwadraat gedeeld door r: 100 gedeeld door 20 is 5 meter "
        "per seconde kwadraat.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenparig cirkelvormige beweging staan de snelheid en de versnelling loodrecht op elkaar.",
        antwoord=True,
        uitleg="De snelheid raakt aan de cirkel, de versnelling wijst naar het midden. "
        "Daarom verandert wel de richting van de snelheid, maar niet haar grootte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de middelpuntzoekende versnelling zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze wijst naar het midden van de cirkel",
            "ze is het kwadraat van de snelheid gedeeld door de straal",
            "ze wordt vier keer zo groot als je twee keer zo snel rijdt",
            "ze is nul zolang de snelheid dezelfde blijft",
        ],
        antwoord=[0, 1, 2],
        uitleg="De richting van de snelheid verandert voortdurend, en dat is al een "
        "versnelling. Daarom is ze nooit nul bij een cirkelbeweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht houdt een auto in een bocht?",
        opties=[
            "de wrijvingskracht tussen de banden en het wegdek",
            "de motorkracht die de auto vooruit duwt",
            "de normaalkracht van het wegdek omhoog",
            "een middelpuntvliedende kracht naar buiten toe",
        ],
        antwoord=0,
        uitleg="Zonder die wrijving zou de auto rechtdoor schuiven. De middelpuntzoekende "
        "kracht is dus geen nieuwe kracht, maar de rol die een bestaande kracht speelt.",
    ),
    dict(
        type="waarofniet",
        vraag="De middelpuntzoekende kracht is een extra kracht naast de gewone krachten.",
        antwoord=False,
        uitleg="Ze is de naam voor de rol die een bestaande kracht speelt: wrijving, "
        "spankracht of gravitatie. Daarom teken je haar niet apart bij de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een ECB zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de grootte van de baansnelheid blijft constant",
            "de richting van de baansnelheid verandert voortdurend",
            "de versnelling is nul, want de snelheid blijft gelijk",
            "de resulterende kracht wijst in de bewegingszin",
        ],
        antwoord=[0, 1],
        uitleg="De resulterende kracht wijst naar het middelpunt, loodrecht op de beweging. "
        "Daardoor verricht ze zelfs geen arbeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een steen aan een touw wordt rondgeslingerd. Wat gebeurt er als het touw breekt?",
        opties=[
            "de steen vliegt raaklijnig verder, niet naar buiten",
            "de steen vliegt recht van het middelpunt weg",
            "de steen valt meteen loodrecht naar beneden",
            "de steen blijft nog even in zijn cirkel verder gaan",
        ],
        antwoord=0,
        uitleg="Er is geen kracht meer naar het midden, dus geldt de traagheidswet: de steen "
        "gaat door in de richting die hij op dat ogenblik had.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind op 3 m van het midden van een draaimolen doet 6 s over één ronde. Wat is zijn baansnelheid?",
        opties=[
            "ongeveer 3,1 m/s",
            "ongeveer 0,5 m/s",
            "ongeveer 18 m/s",
            "ongeveer 2 m/s",
        ],
        antwoord=0,
        uitleg="De omtrek is twee pi maal 3 is ongeveer 18,8 meter, en dat gedeeld door 6 "
        "seconden geeft ongeveer 3,1 meter per seconde.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je een frequentie uit?",
        antwoord=["hertz", "Hz", "de hertz"],
        uitleg="Eén hertz is één keer per seconde. De periode is het omgekeerde van de "
        "frequentie.",
    ),
    dict(
        type="waarofniet",
        vraag="De middelpuntzoekende kracht verricht arbeid op een lichaam in een ECB.",
        antwoord=False,
        uitleg="Ze staat loodrecht op de beweging, dus is de arbeid nul. Daarom blijft de "
        "kinetische energie constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten kunnen de rol van middelpuntzoekende kracht spelen? Kruis alles aan wat juist is.",
        opties=[
            "de wrijving van de wielen van een auto in een bocht",
            "de spanning in een touw waaraan je een steen rondslingert",
            "de gravitatiekracht op een satelliet rond de aarde",
            "de luchtweerstand op een auto die rechtdoor rijdt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Middelpuntzoekend is geen nieuwe soort kracht maar een rol. De luchtweerstand "
        "werkt tegen de beweging in en niet naar een middelpunt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de universele gravitatiewet?",
        opties=[
            "elke twee massa's trekken elkaar aan, met r² in de noemer",
            "elke twee massa's stoten elkaar af, met r² in de noemer",
            "enkel grote hemellichamen trekken elkaar aan",
            "de aantrekking hangt enkel van de grootste massa af",
        ],
        antwoord=0,
        uitleg="De kracht is G maal het product van de massa's gedeeld door het kwadraat "
        "van hun afstand. Ze werkt tussen álle massa's, ook tussen twee mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin lijkt de gravitatiewet op de wet van Coulomb? Kruis alles aan wat juist is.",
        opties=[
            "beide hebben het kwadraat van de afstand in de noemer",
            "beide hebben het product van twee grootheden in de teller",
            "beide kunnen zowel aantrekken als afstoten",
            "beide hangen af van de lading van het voorwerp",
        ],
        antwoord=[0, 1],
        uitleg="Het grote verschil is dat de gravitatie altijd aantrekt. Er bestaat geen "
        "negatieve massa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de constante G uit de gravitatiewet?",
        antwoord=["gravitatieconstante", "de gravitatieconstante", "constante van Newton"],
        uitleg="Ze is ongeveer 6,67·10⁻¹¹ en staat in de bijlage van het examen. Door die "
        "kleine waarde merk je gravitatie pas bij enorme massa's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de universele gravitatiewet zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de kracht is recht evenredig met het product van de twee massa's",
            "de kracht is omgekeerd evenredig met het kwadraat van de afstand",
            "de kracht werkt tussen alle massa's, hoe klein ook",
            "de kracht werkt enkel tussen hemellichamen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Tussen twee mensen in een kamer werkt ze ook, maar ze is daar veel te klein "
        "om te voelen. De constante G is namelijk bijzonder klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het gravitatieveld rond een planeet eruit?",
        opties=[
            "radiaal, met de lijnen naar de planeet toe",
            "radiaal, met de lijnen van de planeet weg",
            "homogeen, met evenwijdige lijnen rond de planeet",
            "als gesloten kringen rond de planeet heen",
        ],
        antwoord=0,
        uitleg="Gravitatie trekt altijd aan, dus wijzen de lijnen naar binnen. Vlak bij het "
        "oppervlak lijkt het veld over een klein gebied wel homogeen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vlak boven het aardoppervlak mag je het zwaarteveld als homogeen beschouwen.",
        antwoord=True,
        uitleg="Over een paar honderd meter verandert de sterkte nauwelijks, en de lijnen "
        "lopen er zowat evenwijdig. Over de hele aarde gezien is het veld wel radiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de zwaartekracht en de gravitatiekracht?",
        opties=[
            "de zwaartekracht is de gravitatiekracht van de aarde op een lichaam",
            "de zwaartekracht werkt enkel op aarde en gravitatie enkel in de ruimte",
            "de zwaartekracht is het dubbele van de gravitatiekracht",
            "de twee hebben niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg="Stel m maal g gelijk aan G maal M maal m gedeeld door r², en je ziet dat g "
        "volgt uit de massa en de straal van de planeet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is g op de maan ongeveer zes keer kleiner dan op aarde?",
        opties=[
            "de maan heeft veel minder massa, ondanks haar kleinere straal",
            "de maan draait trager rond haar eigen as",
            "de maan heeft geen dampkring om massa tegen te houden",
            "de maan ligt verder van de zon dan de aarde",
        ],
        antwoord=0,
        uitleg="In de formule voor g staan de massa van het hemellichaam en zijn straal. De "
        "maan is wel kleiner, maar haar massa is nog veel kleiner in verhouding.",
    ),
    dict(
        type="waarofniet",
        vraag="Je massa verandert als je naar de maan gaat.",
        antwoord=False,
        uitleg="Massa is de hoeveelheid stof en blijft overal gelijk. Je gewicht, dat een "
        "kracht is, wordt er wel ongeveer zes keer kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de gravitatiekracht als je de afstand tussen twee massa's verdrievoudigt?",
        opties=[
            "ze wordt negen keer zo klein",
            "ze wordt drie keer zo klein",
            "ze wordt negen keer zo groot",
            "ze blijft precies even groot",
        ],
        antwoord=0,
        uitleg="In de noemer staat r kwadraat, dus drie in het kwadraat is negen. Dat heet "
        "de kwadratenwet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht houdt een satelliet in zijn baan rond de aarde?",
        opties=[
            "de gravitatiekracht van de aarde",
            "de stuwkracht van zijn motoren",
            "een middelpuntvliedende kracht naar buiten",
            "de druk van de zonnewind",
        ],
        antwoord=0,
        uitleg="Die kracht speelt daar de rol van middelpuntzoekende kracht. Een satelliet "
        "heeft dus geen motor nodig om in zijn baan te blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de baansnelheid van een satelliet?",
        opties=[
            "je stelt de gravitatiekracht gelijk aan de middelpuntzoekende kracht",
            "je deelt de omtrek van de aarde door de duur van een dag",
            "je vermenigvuldigt de massa van de satelliet met g",
            "je deelt de massa van de aarde door die van de satelliet",
        ],
        antwoord=0,
        uitleg="De massa van de satelliet valt dan links en rechts weg. Daarom hangt de "
        "baansnelheid enkel af van de massa van de aarde en van de straal van de baan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zware en een lichte satelliet in dezelfde baan hebben dezelfde snelheid.",
        antwoord=True,
        uitleg="De massa van de satelliet valt weg als je de gravitatiekracht gelijkstelt "
        "aan de middelpuntzoekende kracht. Alleen de massa van de aarde en de straal van "
        "de baan tellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een satelliet die verder van de aarde draait?",
        opties=[
            "hij beweegt trager en doet er langer over per omloop",
            "hij beweegt sneller en doet er korter over per omloop",
            "hij beweegt even snel als een satelliet dichterbij",
            "hij valt sneller terug naar de aarde toe",
        ],
        antwoord=0,
        uitleg="De gravitatie is daar zwakker, dus volstaat een kleinere snelheid. Een "
        "geostationaire satelliet doet er precies een etmaal over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een satelliet die altijd boven hetzelfde punt van de aarde blijft hangen?",
        antwoord=["geostationair", "geostationaire", "geostationaire satelliet"],
        uitleg="Hij draait in precies één etmaal rond, boven de evenaar. Daarom hoef je een "
        "schotelantenne nooit bij te stellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zweven astronauten in een ruimtestation?",
        opties=[
            "ze vallen samen met het station voortdurend rond de aarde",
            "er is daar geen zwaartekracht meer van de aarde",
            "ze zijn daar te ver van de aarde om nog iets te voelen",
            "de snelheid van het station heft de zwaartekracht op",
        ],
        antwoord=0,
        uitleg="Op die hoogte is g nog ongeveer negentig procent van die aan het oppervlak. "
        "Ze voelen niets doordat niets hen tegenhoudt tijdens dat vallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden bepalen de valversnelling aan het oppervlak van een planeet? Kruis alles aan wat juist is.",
        opties=[
            "de massa van de planeet",
            "de straal van de planeet",
            "de massa van het vallende voorwerp",
            "de omlooptijd van de planeet rond de zon",
        ],
        antwoord=[0, 1],
        uitleg="De massa van het voorwerp valt weg: g is G maal M gedeeld door r². Daarom "
        "valt alles even snel.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gravitatieveld van de aarde houdt ergens op.",
        antwoord=False,
        uitleg="Het wordt met de afstand wel steeds zwakker, maar het wordt nooit precies "
        "nul. Daarom voelt een sonde ver voorbij de maan de aarde nog altijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een satelliet in een cirkelbaan zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de gravitatiekracht speelt de rol van middelpuntzoekende kracht",
            "verder van de aarde hoort bij een kleinere baansnelheid",
            "de massa van de satelliet valt uit de formule van de baansnelheid weg",
            "de satelliet zweeft omdat er daar geen gravitatie meer werkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De gravitatie is er juist nodig om de satelliet in zijn baan te houden. Hij "
        "zweeft omdat hij samen met het station in een vrije val zit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kracht speelt bij een satelliet de rol van middelpuntzoekende kracht?",
        antwoord=["de gravitatiekracht", "gravitatiekracht", "de zwaartekracht"],
        uitleg="Ze trekt de satelliet voortdurend naar de aarde toe en houdt hem zo in zijn "
        "cirkel. Zonder haar zou hij raaklijnig rechtdoor vliegen.",
    ),
]
