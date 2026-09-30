# -*- coding: utf-8 -*-
"""De vragen voor "Transport en overbrengingen" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technische systemen —
transportsysteem": overbrengingen, rechtstreekse en onrechtstreekse aandrijving,
de invloed van een overbrenging op de beweging of de kracht, en de
functiedriehoek van een transportsysteem.

Deel 1 gaat over de zes overbrengingen van de fiche (hefbomen, tandwielen,
riemen, katrollen, kettingen, wrijvingswielen), over drijver en volger, en over
rechtstreeks en onrechtstreeks aandrijven.
Deel 2 gaat over wat een overbrenging doet met de beweging: versnellen of
vertragen, de zin omkeren met een gekruiste riem, en kracht inruilen voor
snelheid.

De rekenvragen blijven bij ronde getallen (10 op 30, 40 op 10), zodat het over
de verhouding gaat en niet over het hoofdrekenen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn overbrengingen?",
        opties=[
            "Tandwielen",
            "Riemen",
            "Katrollen",
            "Een schroevendraaier",
            "Een boormachine op het net",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een overbrenging geeft een beweging door van het ene deel naar het andere. Gereedschap doet dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de drijver in een overbrenging?",
        opties=[
            "Het wiel dat de beweging geeft",
            "Het wiel dat de beweging ontvangt",
            "Het wiel dat stil blijft staan",
            "De as tussen de twee wielen in",
        ],
        antwoord=0,
        uitleg="De drijver zit aan de kant van de motor of van de trappers. Hij zet de beweging in gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de volger in een overbrenging?",
        opties=[
            "Het wiel dat de beweging ontvangt",
            "Het wiel dat de beweging zelf geeft",
            "Het wiel met de meeste tanden erop",
            "Het wiel dat het dichtst bij de motor zit",
        ],
        antwoord=0,
        uitleg="De volger volgt: hij draait mee doordat de drijver hem aandrijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een onrechtstreekse aandrijving zit er een riem of een ketting tussen de twee wielen.",
        antwoord=True,
        uitleg="Rechtstreeks betekent dat de wielen elkaar zelf raken, bijvoorbeeld twee tandwielen die in elkaar grijpen. Onrechtstreeks gaat via iets ertussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee tandwielen die in elkaar grijpen, zijn een voorbeeld van ...",
        opties=[
            "Een rechtstreekse aandrijving",
            "Een onrechtstreekse aandrijving",
            "Een hefboom met een steunpunt",
            "Een katrol met een touw eroverheen",
        ],
        antwoord=0,
        uitleg="De tanden van het ene wiel duwen rechtstreeks tegen die van het andere. Er zit niets tussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De ketting van een fiets is een voorbeeld van ...",
        opties=[
            "Een onrechtstreekse aandrijving",
            "Een rechtstreekse aandrijving",
            "Een wrijvingswiel met rubber",
            "Een hefboom met een steunpunt",
        ],
        antwoord=0,
        uitleg="De twee tandwielen raken elkaar niet; de ketting brengt de beweging over. Dat is precies wat onrechtstreeks betekent.",
    ),
    dict(
        type="invultekst",
        vraag="Het wiel dat de beweging doorgeeft aan het andere wiel, heet de ___.",
        antwoord="drijver",
        uitleg="De drijver drijft aan, de volger volgt. Die twee woorden komen op het examen terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een katrol?",
        opties=[
            "Een wiel met een groef waar een touw over loopt",
            "Een wiel met tanden die in andere tanden grijpen",
            "Een staaf die rond een vast steunpunt draait",
            "Twee wielen die elkaar raken en zo meedraaien",
        ],
        antwoord=0,
        uitleg="Een katrol leidt een touw of kabel om. Met meerdere katrollen samen hef je een zware last met minder kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hefboom?",
        opties=[
            "Een staaf die om een steunpunt draait",
            "Een wiel met tanden aan de rand",
            "Een touw dat over een wiel loopt",
            "Een riem tussen twee ronde wielen",
        ],
        antwoord=0,
        uitleg="Een hefboom is de eenvoudigste overbrenging die er is. Een schaar, een kruiwagen en een wip werken er alle drie mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kruiwagen werkt met een hefboom.",
        antwoord=True,
        uitleg="Het wiel is het steunpunt, de last ligt in de bak en jij duwt aan de handvatten. Hoe verder je handen van het wiel zitten, hoe lichter het gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een katrol kloppen?",
        opties=[
            "Er loopt een touw of een kabel over",
            "Ze kan de richting van een kracht veranderen",
            "Met meerdere katrollen hef je met minder kracht",
            "Ze maakt de last die je hijst zelf lichter",
        ],
        antwoord=[0, 1, 2],
        uitleg="De last blijft even zwaar. Wat verandert, is hoeveel kracht jij moet leveren en over welke afstand je moet trekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke overbrengingen noemt de vakfiche?",
        opties=[
            "Hefbomen",
            "Tandwielen",
            "Kettingen",
            "Wrijvingswielen",
            "Schroevendraaiers",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="De fiche noemt hefbomen, tandwielen, riemen, katrollen, kettingen en wrijvingswielen. Een schroevendraaier is gereedschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Wrijvingswielen geven de beweging door doordat ze elkaar raken.",
        antwoord=True,
        uitleg="Ze hebben geen tanden. Het is de wrijving tussen de twee oppervlakken die de beweging overbrengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom slippen wrijvingswielen soms?",
        opties=[
            "Ze houden elkaar alleen met wrijving vast",
            "Ze hebben tanden die makkelijk afbreken",
            "Er zit een ketting tussen die te los hangt",
            "Ze zijn altijd van gladde kunststof gemaakt",
        ],
        antwoord=0,
        uitleg="Is de kracht te groot of zijn de wielen nat of vettig, dan glijden ze langs elkaar. Tandwielen en kettingen kunnen dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke overbrenging zit er tussen de trappers en het achterwiel van een fiets?",
        opties=[
            "Een ketting over twee tandwielen",
            "Een riem over twee gladde katrollen",
            "Twee wrijvingswielen tegen elkaar",
            "Een hefboom met een vast steunpunt",
        ],
        antwoord=0,
        uitleg="Vooraan het grote tandwiel bij de trappers, achteraan het kleinere. De ketting verbindt ze en kan niet slippen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een riemoverbrenging kan alleen tussen twee wielen die elkaar raken.",
        antwoord=False,
        uitleg="Juist niet. Bij een riem zitten de wielen een eind uit elkaar, en de riem overbrugt die afstand. Dat is een onrechtstreekse aandrijving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van een ketting boven een riem?",
        opties=[
            "Een ketting kan niet slippen",
            "Een ketting werkt altijd stiller",
            "Een ketting hoeft nooit gesmeerd",
            "Een ketting is altijd lichter",
        ],
        antwoord=0,
        uitleg="De schakels grijpen in de tanden, dus de overbrenging staat vast. Een riem kan wel doorslippen, maar loopt stiller en hoeft niet gesmeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk toestel zit er een tandwieloverbrenging?",
        opties=[
            "In een handmixer",
            "In een gewone ladder",
            "In een tuinslang",
            "In een emmer water",
        ],
        antwoord=0,
        uitleg="De motor van een mixer draait heel snel; tandwielen maken daar een trager en krachtiger draaien van voor de kloppers.",
    ),
    dict(
        type="waarofniet",
        vraag="De volger is het wiel dat de beweging geeft.",
        antwoord=False,
        uitleg="De volger krijgt de beweging. Het wiel dat ze geeft, is de drijver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een transportsysteem?",
        opties=[
            "Een systeem dat iets of iemand verplaatst",
            "Een systeem dat informatie in en uit voert",
            "Een systeem dat voedsel langer houdbaar maakt",
            "Een systeem dat het gewicht van een gebouw draagt",
        ],
        antwoord=0,
        uitleg="Een fiets, een lift, een lopende band en een kraan zijn alle vier transportsystemen. De vier andere in het rijtje zijn de andere systemen van de fiche.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als een klein tandwiel een groot tandwiel aandrijft?",
        opties=[
            "Het grote wiel draait trager",
            "Het grote wiel draait sneller",
            "Beide wielen draaien even snel",
            "Het grote wiel blijft gewoon stilstaan",
        ],
        antwoord=0,
        uitleg="Het grote wiel heeft meer tanden, dus het moet meer tanden verwerken voor het één keer rond is. Trager draaien betekent wel meer kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als een groot tandwiel een klein tandwiel aandrijft?",
        opties=[
            "Het kleine wiel draait sneller",
            "Het kleine wiel draait trager",
            "Beide wielen draaien even snel",
            "Het kleine wiel draait de andere kant op",
        ],
        antwoord=0,
        uitleg="Het kleine wiel is met minder tanden al rond, dus het draait vaker. Sneller draaien betekent minder kracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee tandwielen die in elkaar grijpen, draaien in dezelfde zin.",
        antwoord=False,
        uitleg="Ze draaien tegengesteld. Duwt het ene wiel zijn tand naar rechts, dan wordt het andere daar juist naar links geduwd.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee wielen met een gewone, niet gekruiste riem draaien in dezelfde zin.",
        antwoord=True,
        uitleg="De riem loopt langs beide wielen dezelfde kant op. Pas als je hem kruist, draait de volger de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als je de riem van een riemoverbrenging laat kruisen?",
        opties=[
            "De volger draait in de andere zin",
            "De volger draait een stuk sneller rond",
            "De volger draait een stuk trager rond",
            "De volger blijft helemaal stilstaan",
        ],
        antwoord=0,
        uitleg="Dat voorbeeld staat in de fiche: de riem laten kruisen zodat de zin van de drijver en de volger verschillend is. De snelheid verandert er niet door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloed kan een overbrenging hebben?",
        opties=[
            "Ze kan de beweging versnellen",
            "Ze kan de beweging vertragen",
            "Ze kan de richting van de beweging veranderen",
            "Ze kan het materiaal van de as veranderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt versnellen, vertragen en het veranderen van richting en zin. Van materiaal verandert er niets.",
    ),
    dict(
        type="invultekst",
        vraag="Een overbrenging die de beweging trager maakt, noem je een ___.",
        antwoord="vertraging",
        uitleg="Een vertraging levert meer kracht op. Een versnelling doet het omgekeerde: sneller, maar met minder kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet je op een fiets een licht verzet als je een helling opfietst?",
        opties=[
            "Je trapt lichter maar moet sneller trappen",
            "Je trapt zwaarder en gaat toch sneller",
            "Je trapt even zwaar als op een vlakke weg",
            "De ketting springt er dan niet zomaar af",
        ],
        antwoord=0,
        uitleg="Een licht verzet is een vertraging: je ruilt snelheid in voor kracht. Daarom raak je bergop wel boven, maar traag.",
    ),
    dict(
        type="waarofniet",
        vraag="Meer snelheid bij een overbrenging gaat meestal ten koste van kracht.",
        antwoord=True,
        uitleg="Je krijgt er nooit iets bij. Wat je wint aan snelheid, verlies je aan kracht, en omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tandwiel met 10 tanden drijft er een met 30 aan. Hoe vaak draait het grote wiel rond als het kleine drie keer rondgaat?",
        opties=["Eén keer", "Drie keer", "Negen keer", "Dertig keer"],
        antwoord=0,
        uitleg="Het grote wiel heeft drie keer zoveel tanden, dus het draait drie keer trager. Drie toeren van het kleine wiel geven één toer van het grote.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tandwiel met 40 tanden drijft er een met 10 aan. Hoe vaak draait het kleine wiel als het grote één keer rondgaat?",
        opties=["Vier keer", "Eén keer", "Tien keer", "Veertig keer"],
        antwoord=0,
        uitleg="Veertig tanden gaan voorbij, en het kleine wiel is na tien tanden al rond. Veertig gedeeld door tien is vier.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer tanden een tandwiel heeft, hoe sneller het draait bij dezelfde aandrijving.",
        antwoord=False,
        uitleg="Net omgekeerd: meer tanden betekent trager draaien, en dus meer kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een versnellingsbak kloppen?",
        opties=[
            "Je kiest ermee tussen kracht en snelheid",
            "Ze bevat tandwielen van verschillende grootte",
            "In een lage versnelling trek je vlotter op",
            "Ze maakt de motor van het voertuig stiller",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een versnellingsbak is een rij overbrengingen waaruit je kiest. Met stiller rijden heeft ze niets te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de kracht als je bij een hefboom een langere arm gebruikt?",
        opties=[
            "Je hebt minder kracht nodig",
            "Je hebt juist meer kracht nodig",
            "De kracht blijft precies dezelfde",
            "De kracht verdwijnt dan helemaal",
        ],
        antwoord=0,
        uitleg="Hoe verder van het steunpunt je duwt, hoe lichter het gaat. Je moet dan wel over een grotere afstand bewegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Met een hefboom kan je een last optillen die je met je blote handen niet aankunt.",
        antwoord=True,
        uitleg="Dat is precies waarvoor een hefboom dient. Een koevoet en een kruiwagen werken allebei zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de functiedriehoek van een transportsysteem?",
        opties=[
            "De functie",
            "Het materiaal",
            "De bewerking",
            "De vorm",
            "De snelheid in kilometer per uur",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Een functiedriehoek bevat altijd dezelfde vier, voor welk systeem je hem ook opstelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een overbrenging kan de zin van een beweging omkeren.",
        antwoord=True,
        uitleg="Twee tandwielen die in elkaar grijpen doen dat vanzelf, en met een gekruiste riem kan je het ook bij een riemoverbrenging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kruisen sommige machines de riem met opzet?",
        opties=[
            "Omdat de volger dan de andere kant op moet draaien",
            "Omdat de riem dan veel minder snel verslijt",
            "Omdat de riem dan strakker over de wielen staat",
            "Omdat de riem dan een stuk stiller loopt",
        ],
        antwoord=0,
        uitleg="De bouw van de overbrenging volgt uit wat je wilt bereiken. Wil je dat de volger omgekeerd draait, dan kruis je de riem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee even grote wielen zijn verbonden met een riem. Wat gebeurt er?",
        opties=[
            "Ze draaien allebei even snel",
            "De volger draait twee keer zo snel",
            "De volger draait half zo snel rond",
            "De volger blijft helemaal stilstaan",
        ],
        antwoord=0,
        uitleg="Even groot betekent dezelfde omtrek, dus dezelfde snelheid. Zo'n overbrenging verandert alleen de plaats van de beweging.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stel katrollen verandert alleen de richting van het touw.",
        antwoord=False,
        uitleg="Eén vaste katrol doet alleen dat. Maar met meerdere katrollen samen heb je ook minder kracht nodig, al moet je dan wel meer touw doortrekken.",
    ),
]
