# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Rechtlijnige bewegingen.

Fysica, de koppen "Eenparig rechtlijnige beweging (ERB)" en "Eenparig
veranderlijke rechtlijnige beweging (EVRB)" van de vakfiche
natuurwetenschappen 2de graad doorstroom. Deel 1 gaat over de ERB, het
verschil tussen afgelegde weg en verplaatsing, de vier kenmerken van een
vector en de x(t)- en v(t)-grafiek; deel 2 over de EVRB, de versnelling en
het lezen van de drie grafieken.

De vragen beschrijven de grafieken in woorden, zodat ze zonder tekening te
volgen zijn.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een eenparig rechtlijnige beweging?",
        opties=[
            "de snelheid blijft onveranderd en de baan is een rechte lijn",
            "de snelheid neemt gelijkmatig toe langs een rechte lijn",
            "de snelheid blijft onveranderd maar de baan is een cirkel",
            "de snelheid wisselt voortdurend langs een rechte lijn",
        ],
        antwoord=0,
        uitleg="Eenparig betekent dat de snelheid gelijk blijft, rechtlijnig dat de baan recht is. In elke seconde wordt dan dezelfde afstand afgelegd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de afgelegde weg en de verplaatsing zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de afgelegde weg is de hele baan die je volgt",
            "de verplaatsing gaat enkel van begin naar eind",
            "wie naar zijn startpunt terugkeert, heeft een verplaatsing van nul",
            "de verplaatsing is altijd groter dan de afgelegde weg",
        ],
        antwoord=[0, 1, 2],
        uitleg="Loop je tien meter heen en tien meter terug, dan is de afgelegde weg twintig meter en de verplaatsing nul. De verplaatsing is dus nooit groter dan de afgelegde weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Verplaatsing en snelheid zijn vectoriële grootheden.",
        antwoord=True,
        uitleg="Ze hebben niet alleen een grootte maar ook een richting en een zin. Daarom stel je ze voor met een pijl.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft een vectoriële grootheid? Kruis alles aan wat juist is.",
        opties=["grootte", "richting", "zin", "temperatuur"],
        antwoord=[0, 1, 2],
        uitleg="De vier kenmerken zijn grootte, richting, zin en aangrijpingspunt. De temperatuur heeft met een vector niets te maken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waarop een vector aangrijpt?",
        antwoord="aangrijpingspunt",
        uitleg="Dat is het vierde kenmerk van een vector, naast grootte, richting en zin. Het zegt waar de pijl begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt 150 kilometer in 2 uur. Wat is zijn gemiddelde snelheid?",
        opties=["75 kilometer per uur", "150 kilometer per uur", "300 kilometer per uur", "50 kilometer per uur"],
        antwoord=0,
        uitleg="De gemiddelde snelheid is de verplaatsing gedeeld door het tijdsverloop, dus 150 gedeeld door 2.",
    ),
    dict(
        type="waarofniet",
        vraag="In een x(t)-grafiek van een eenparig rechtlijnige beweging is de grafiek een rechte lijn.",
        antwoord=True,
        uitleg="De positie verandert in elke seconde evenveel. De steilheid van die rechte is precies de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af aan de steilheid van een x(t)-grafiek?",
        opties=[
            "de snelheid van de puntmassa",
            "de versnelling van de puntmassa",
            "de afgelegde weg van de puntmassa",
            "de massa van de puntmassa",
        ],
        antwoord=0,
        uitleg="De steilheid is de verandering van de positie per tijdseenheid, en dat is de definitie van snelheid. Een steilere lijn betekent dus sneller gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een x(t)-grafiek loopt een tijdje vlak. Wat doet de puntmassa dan?",
        opties=[
            "ze staat stil, want haar positie verandert niet",
            "ze beweegt met een constante snelheid vooruit",
            "ze beweegt terug naar haar beginpositie toe",
            "ze versnelt gelijkmatig vanuit de stilstand",
        ],
        antwoord=0,
        uitleg="Een vlak stuk betekent dezelfde positie op elk tijdstip. Dat is een rustpauze.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grootheid bereken je als je de verplaatsing deelt door het tijdsverloop?",
        antwoord="snelheid",
        uitleg="Dat is de gemiddelde snelheid. Je rekent ze met het differentiequotiënt van de positie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een negatieve snelheid in een v(t)-grafiek?",
        opties=[
            "de puntmassa beweegt tegengesteld aan de zin van de x-as",
            "de puntmassa vertraagt en komt langzaam tot stilstand",
            "de puntmassa heeft een negatieve massa gekregen",
            "de puntmassa staat volledig stil op haar plaats",
        ],
        antwoord=0,
        uitleg="Het teken van de snelheid zegt alleen in welke zin de beweging gaat. Hoe snel het gaat, lees je af aan de grootte.",
    ),
    dict(
        type="waarofniet",
        vraag="In een v(t)-grafiek stelt de oppervlakte onder de kromme de verplaatsing voor.",
        antwoord=True,
        uitleg="Snelheid maal tijd geeft afstand, en dat is precies de oppervlakte van die rechthoek. Onder de tijdas gerekend wordt die verplaatsing negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de grafieken van een eenparig rechtlijnige beweging zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de x(t)-grafiek is een rechte lijn",
            "de v(t)-grafiek is een vlakke rechte lijn",
            "de a(t)-grafiek ligt op de tijdas",
            "de x(t)-grafiek is een kromme die steeds steiler wordt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De snelheid blijft gelijk, dus loopt de positie rechtlijnig op, blijft de snelheidslijn op dezelfde hoogte en is er geen versnelling. Een steeds steilere kromme hoort bij een versnelde beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een puntmassa start op positie 20 meter en rijdt met 5 meter per seconde in de zin van de x-as. Waar zit ze na 4 seconden?",
        opties=["op 40 meter", "op 20 meter", "op 5 meter", "op 80 meter"],
        antwoord=0,
        uitleg="Je telt bij de beginpositie de verplaatsing op: 20 plus 5 maal 4. Dat is de positiefunctie van een eenparig rechtlijnige beweging.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenparig rechtlijnige beweging zijn de afgelegde weg en de verplaatsing altijd verschillend.",
        antwoord=False,
        uitleg="Zolang de puntmassa niet van zin verandert, zijn ze gelijk. Pas als ze terugkeert, lopen de twee uiteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee wandelaars vertrekken op hetzelfde ogenblik vanuit dezelfde plaats, de ene met 4 en de andere met 6 kilometer per uur. Hoe ziet dat in een x(t)-grafiek?",
        opties=[
            "twee rechten vanuit hetzelfde punt, waarvan de ene steiler loopt",
            "twee rechten die elkaar na een uur ergens weer kruisen",
            "twee vlakke lijnen op een verschillende hoogte boven de tijdas",
            "twee krommen die beide steeds steiler naar boven lopen",
        ],
        antwoord=0,
        uitleg="Dezelfde beginplaats geeft hetzelfde startpunt, en de snelste krijgt de steilste rechte. Ze lopen daarna alleen maar verder uiteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een puntmassa?",
        opties=[
            "een voorwerp waarvan je de afmetingen bij deze beweging verwaarloost",
            "een voorwerp met een massa van precies één kilogram",
            "een voorwerp dat helemaal geen massa meer heeft",
            "een voorwerp dat alleen in een rechte lijn vooruit of achteruit beweegt",
        ],
        antwoord=0,
        uitleg="Je doet alsof de hele massa in één punt zit. Voor een auto op de snelweg is dat een prima benadering.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de tijd tussen twee tijdstippen?",
        antwoord="tijdsverloop",
        uitleg="Het tijdstip is een moment op de klok, het tijdsverloop is het verschil tussen twee van die momenten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een snelheid van 36 kilometer per uur is hetzelfde als 36 meter per seconde.",
        antwoord=False,
        uitleg="Je deelt kilometer per uur door 3,6 om meter per seconde te krijgen. 36 kilometer per uur is dus 10 meter per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser rijdt 10 kilometer naar het oosten en daarna 10 kilometer terug naar het westen. Wat is zijn verplaatsing?",
        opties=["nul kilometer", "20 kilometer", "10 kilometer", "5 kilometer"],
        antwoord=0,
        uitleg="Hij eindigt waar hij begon, dus is de verplaatsing nul. De afgelegde weg is wel 20 kilometer.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een eenparig veranderlijke rechtlijnige beweging?",
        opties=[
            "de versnelling blijft onveranderd en de baan is een rechte lijn",
            "de snelheid blijft onveranderd en de baan is een rechte lijn",
            "de versnelling wisselt voortdurend langs een rechte lijn",
            "de versnelling blijft onveranderd maar de baan is een cirkel",
        ],
        antwoord=0,
        uitleg="De snelheid verandert in elke seconde evenveel. Daardoor is de versnelling constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de versnelling van een voorwerp?",
        opties=[
            "de verandering van de snelheid per tijdseenheid",
            "de verandering van de positie per tijdseenheid",
            "de snelheid vermenigvuldigd met het tijdsverloop",
            "de afgelegde weg gedeeld door het tijdsverloop",
        ],
        antwoord=0,
        uitleg="De eenheid is meter per seconde per seconde. Een versnelling van 2 betekent dat de snelheid elke seconde met 2 meter per seconde toeneemt.",
    ),
    dict(
        type="waarofniet",
        vraag="In een v(t)-grafiek van een eenparig veranderlijke beweging is de grafiek een schuine rechte.",
        antwoord=True,
        uitleg="De snelheid verandert gelijkmatig, dus loopt de lijn recht omhoog of recht omlaag. De steilheid is de versnelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af aan de steilheid van een v(t)-grafiek?",
        opties=[
            "de versnelling",
            "de verplaatsing",
            "de positie",
            "de massa",
        ],
        antwoord=0,
        uitleg="De steilheid is de verandering van snelheid per tijdseenheid, en dat is de versnelling. De oppervlakte eronder geeft de verplaatsing.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruiken we voor de versnelling?",
        antwoord="a",
        uitleg="De eenheid ervan is meter per seconde kwadraat, want het is meter per seconde en dat per seconde opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt vooruit en zijn versnelling is negatief. Wat doet hij?",
        opties=[
            "hij vertraagt",
            "hij rijdt achteruit",
            "hij rijdt met constante snelheid",
            "hij staat helemaal stil",
        ],
        antwoord=0,
        uitleg="Snelheid en versnelling hebben dan een tegengesteld teken. Daardoor wordt de snelheid elke seconde kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een eenparig versnelde beweging zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de v(t)-grafiek is een schuine rechte die stijgt",
            "de a(t)-grafiek is een vlakke rechte boven de tijdas",
            "de x(t)-grafiek is een kromme die steeds steiler wordt",
            "de x(t)-grafiek is een rechte lijn met een vaste steilheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="De versnelling blijft gelijk, de snelheid stijgt rechtlijnig en de positie verandert daardoor steeds sneller. Een rechte x(t)-grafiek hoort bij een constante snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp start uit stilstand en versnelt met 3 meter per seconde kwadraat. Welke snelheid heeft het na 4 seconden?",
        opties=["12 meter per seconde", "3 meter per seconde", "7 meter per seconde", "0,75 meter per seconde"],
        antwoord=0,
        uitleg="Je vermenigvuldigt de versnelling met de tijd: 3 maal 4. Vanuit stilstand hoef je er niets bij te tellen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een a(t)-grafiek van een eenparig veranderlijke beweging is een vlakke rechte.",
        antwoord=True,
        uitleg="De versnelling verandert immers niet. Boven de tijdas is ze positief, eronder negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe onderscheid je in een v(t)-grafiek een versnelde van een vertraagde beweging?",
        opties=[
            "bij versnellen gaat de grootte van de snelheid omhoog, bij vertragen omlaag",
            "bij versnellen loopt de lijn boven de tijdas, bij vertragen onder de tijdas",
            "bij versnellen is de lijn recht, bij vertragen is ze gekromd",
            "bij versnellen is de lijn vlak, bij vertragen is ze schuin",
        ],
        antwoord=0,
        uitleg="Je kijkt naar de grootte van de snelheid, niet naar het teken. Een snelheid van min 2 naar min 8 is ook versnellen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een beweging waarbij de snelheid gelijkmatig kleiner wordt?",
        antwoord="eenparig vertraagd",
        uitleg="De versnelling is dan tegengesteld aan de snelheid, en blijft in grootte gelijk. Het remmen van een trein benadert dit goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee auto's hebben elk een v(t)-grafiek die vanuit nul stijgt, de ene steiler dan de andere. Wat weet je?",
        opties=[
            "de auto met de steilste lijn heeft de grootste versnelling",
            "de auto met de steilste lijn heeft de kleinste versnelling",
            "beide auto's hebben dezelfde versnelling maar een andere snelheid",
            "de auto met de steilste lijn heeft de grootste massa van de twee",
        ],
        antwoord=0,
        uitleg="De steilheid van een v(t)-grafiek is de versnelling. Steiler betekent dus elke seconde meer snelheid erbij.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eenparig veranderlijke beweging is de x(t)-grafiek een rechte lijn.",
        antwoord=False,
        uitleg="De snelheid verandert, dus verandert ook de steilheid. De x(t)-grafiek is daarom een kromme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een v(t)-grafiek daalt van 20 meter per seconde naar nul in 5 seconden. Wat is de versnelling?",
        opties=[
            "min 4 meter per seconde kwadraat",
            "plus 4 meter per seconde kwadraat",
            "min 100 meter per seconde kwadraat",
            "min 0,25 meter per seconde kwadraat",
        ],
        antwoord=0,
        uitleg="Je deelt de verandering van snelheid door de tijd: min 20 gedeeld door 5. Het minteken zegt dat het vertragen is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt met 20 meter per seconde en vertraagt gelijkmatig tot stilstand in 5 seconden. Hoeveel meter legt hij nog af?",
        opties=["50 meter", "100 meter", "25 meter", "20 meter"],
        antwoord=0,
        uitleg="De oppervlakte onder de v(t)-grafiek is een driehoek: de helft van 20 maal 5. Dat is de remweg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een versnelling kan nooit negatief zijn.",
        antwoord=False,
        uitleg="Een negatieve versnelling betekent gewoon dat ze tegengesteld aan de x-as werkt. Vaak komt dat op vertragen neer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden stel je bij een beweging met een vector voor? Kruis alles aan wat juist is.",
        opties=["de verplaatsing", "de snelheid", "de versnelling", "het tijdsverloop"],
        antwoord=[0, 1, 2],
        uitleg="Die drie hebben een grootte én een richting en zin. Het tijdsverloop is gewoon een getal met een eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee treinen rijden naar elkaar toe op hetzelfde spoor. Hoe vind je grafisch wanneer ze elkaar kruisen?",
        opties=[
            "je zoekt het snijpunt van hun twee x(t)-grafieken",
            "je zoekt het snijpunt van hun twee v(t)-grafieken",
            "je telt de oppervlakten onder hun v(t)-grafieken op",
            "je vergelijkt de steilheid van hun twee a(t)-grafieken",
        ],
        antwoord=0,
        uitleg="Kruisen betekent op hetzelfde tijdstip op dezelfde positie zijn. Dat is precies wat een snijpunt van twee x(t)-grafieken zegt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de snelheid op één bepaald tijdstip?",
        antwoord="ogenblikkelijke snelheid",
        uitleg="Die lees je af aan de steilheid van de x(t)-grafiek op dat ene punt. De gemiddelde snelheid kijkt naar een heel tijdsinterval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een a(t)-grafiek ligt een tijdje precies op de tijdas. Wat doet het voorwerp dan?",
        opties=[
            "het behoudt zijn snelheid, die kan ook nul zijn",
            "het staat zeker helemaal stil op zijn plaats",
            "het vertraagt gelijkmatig tot aan de stilstand",
            "het versnelt gelijkmatig vanuit de stilstand",
        ],
        antwoord=0,
        uitleg="Geen versnelling betekent geen verandering van snelheid. Rijdt het voorwerp, dan rijdt het gewoon verder met dezelfde snelheid.",
    ),
]
