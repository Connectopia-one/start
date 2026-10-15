# -*- coding: utf-8 -*-
"""Pittige vragen bij "Transport en overbrengingen" (✨ Spark, techniek).

Tandwielen in twee stappen en omgekeerd gerekend, de draaizin door een rij van
overbrengingen gevolgd, en de juiste overbrenging kiezen voor een concrete situatie.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag=r"Een tandwiel met \(12\) tanden drijft een tandwiel met \(36\) tanden aan. Het kleine wiel draait \(6\) keer rond. Hoe vaak draait het grote wiel rond?",
        opties=[r"\(2\) keer", r"\(18\) keer", r"\(3\) keer", r"\(6\) keer"],
        antwoord=0,
        reken="6 * 12 / 36",
        uitleg=r"Zes toeren van het kleine wiel laten \(6\) maal \(12\), dus \(72\) tanden passeren. Het grote wiel is na \(36\) tanden rond, dus het draait \(2\) keer. Wie \(18\) kiest, heeft vermenigvuldigd in plaats van gedeeld: het grote wiel draait juist trager.",
    ),
    dict(
        type="invultekst",
        vraag=r"Op een fiets heeft het tandwiel bij de trappers \(48\) tanden en het tandwiel aan het achterwiel \(16\) tanden. Het achterwiel zit vast aan dat kleine tandwiel. Hoe vaak draait het achterwiel rond als je de trappers één keer rond draait? Antwoord met een getal.",
        antwoord="3",
        reken="48 / 16",
        uitleg=r"Eén keer rondtrappen trekt \(48\) schakels van de ketting langs het kleine tandwiel. Dat is na \(16\) tanden rond, dus het draait \(48\) gedeeld door \(16\), of \(3\) keer. Groot drijft klein: het kleine wiel draait sneller.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De drijver van een tandwieloverbrenging heeft \(50\) tanden. Telkens als de drijver één keer rondgaat, draait de volger \(5\) keer. Hoeveel tanden heeft de volger?",
        opties=[r"\(10\) tanden", r"\(250\) tanden", r"\(55\) tanden", r"\(45\) tanden"],
        antwoord=0,
        reken="50 / 5",
        uitleg=r"Eén toer van de drijver laat \(50\) tanden passeren, en daarmee gaat de volger \(5\) keer rond. Per toer zijn dat dus \(50\) gedeeld door \(5\), of \(10\) tanden. De volger draait sneller, dus hij moet kleiner zijn dan de drijver, en \(250\) kan niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie tandwielen staan op een rij: A grijpt in B, en B grijpt in C. A draait in wijzerzin. In welke zin draait C?",
        opties=[
            "In wijzerzin, net als A",
            "Tegen de wijzerzin in, net als B",
            "C kan niet draaien, B blokkeert alles",
            "Nu eens in wijzerzin, dan weer niet",
        ],
        antwoord=0,
        uitleg="Twee tandwielen die in elkaar grijpen, draaien tegengesteld. A in wijzerzin geeft B tegen de wijzerzin, en B keert het nog eens om, dus C draait weer in wijzerzin.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een tandwiel met \(10\) tanden dat een tandwiel met \(40\) tanden aandrijft, laat de volger trager maar krachtiger draaien.",
        antwoord=True,
        uitleg=r"Klein drijft groot, dus de volger draait trager: vier keer trager zelfs, want hij heeft vier keer zoveel tanden. Wat je aan snelheid inlevert, win je aan kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een motorwiel draait in wijzerzin en drijft met een gekruiste riem wiel B aan. Wiel B is een tandwiel dat rechtstreeks in tandwiel C grijpt. In welke zin draait C?",
        opties=[
            "In wijzerzin, net als de motor",
            "Tegen de wijzerzin in, net als B",
            "C staat stil, want de riem slipt",
            "In wijzerzin, maar tegengesteld aan de motor",
        ],
        antwoord=0,
        uitleg="De gekruiste riem keert de zin om: B draait tegen de wijzerzin in. B en C grijpen in elkaar en draaien dus weer tegengesteld: C draait in wijzerzin, dezelfde zin als de motor.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bouwvakker hijst een emmer cement van \(20\) kg naar boven. Eerst gebruikt hij één katrol, daarna een stel van meerdere katrollen. Wat klopt er over het stel katrollen?",
        opties=[
            "Hij heeft minder kracht nodig dan met één katrol",
            "Het verandert alleen de richting van het touw",
            "Hij heeft meer kracht nodig, want er is meer touw",
            "Hij heeft precies even veel kracht nodig als eerst",
        ],
        antwoord=0,
        uitleg="Eén katrol verandert de richting van de kracht. Met meerdere katrollen samen hef je bovendien met minder kracht. Een stel katrollen doet dus meer dan alleen de richting van het touw veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wilt een zware steen optillen met een lange houten stok die over een blok hout ligt. Het blok is het steunpunt, de steen ligt aan het korte eind. Waar duw je best?",
        opties=[
            "Zo ver mogelijk van het blok, aan het andere eind",
            "Zo dicht mogelijk bij het blok, vlak naast het steunpunt",
            "Recht boven het blok, op het steunpunt zelf",
            "Vlak naast de steen, zo dicht mogelijk bij de last",
        ],
        antwoord=0,
        uitleg="De stok is een hefboom die om het steunpunt draait. Hoe verder van het steunpunt je duwt, hoe langer de arm en hoe minder kracht je nodig hebt. Op het steunpunt zelf duwen doet de stok helemaal niet draaien.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe korter de arm waaraan je duwt bij een hefboom, hoe minder kracht je nodig hebt om dezelfde last op te tillen.",
        antwoord=False,
        uitleg="Net omgekeerd. Een langere arm vraagt minder kracht; met een kortere arm moet je harder duwen om dezelfde last op te tillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke van deze overbrengingen kan de volger doorslippen als de kracht te groot wordt? (meerdere antwoorden mogelijk)",
        opties=[
            "Een riem over twee wielen",
            "Twee wrijvingswielen die elkaar raken",
            "Een ketting over twee tandwielen",
            "Twee tandwielen die in elkaar grijpen",
        ],
        antwoord=[0, 1],
        uitleg="Wrijvingswielen en een riem houden alleen met wrijving vast, dus die kunnen slippen. Bij een ketting haken de schakels in de tanden, en tandwielen grijpen rechtstreeks in elkaar: daar kan niets doorglijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze aandrijvingen zijn onrechtstreeks? (meerdere antwoorden mogelijk)",
        opties=[
            "De ketting van een fiets",
            "Een riem tussen een motor en een trommel",
            "Een gekruiste riem tussen twee wielen",
            "Een ketting tussen twee tandwielen van een brommer",
            "Twee tandwielen in een handmixer die in elkaar grijpen",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Bij elke riem en elke ketting raken de twee wielen elkaar niet: dat is onrechtstreeks, ook als de riem gekruist is. Alleen de tandwielen die rechtstreeks in elkaar grijpen, vormen een rechtstreekse aandrijving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser schakelt en merkt dat hij plots zwaarder moet trappen, maar bij elke trap verder komt. Wat heeft hij gedaan?",
        opties=[
            "Hij wint snelheid, en dat kost hem meer kracht",
            "Hij wint kracht, en dat kost hem wat snelheid",
            "Hij wint kracht én snelheid tegelijk",
            "Hij heeft naar een licht verzet geschakeld",
        ],
        antwoord=0,
        uitleg="Verder komen per trap betekent dat het achterwiel sneller draait. Meer snelheid gaat ten koste van kracht, dus het trappen voelt zwaarder. Een licht verzet doet net het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Met een slimme keuze van tandwielen kan de volger tegelijk sneller draaien én meer kracht leveren dan de drijver.",
        antwoord=False,
        uitleg="Dat kan geen enkele overbrenging. Draait de volger sneller, dan levert hij minder kracht; draait hij trager, dan levert hij meer kracht. Je ruilt het ene in voor het andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="De motor van een handmixer draait heel snel, maar de kloppers moeten trager en krachtiger draaien. Hoe zijn de tandwielen geplaatst?",
        opties=[
            "Een klein tandwiel op de motor drijft een groot bij de kloppers aan",
            "Een groot tandwiel op de motor drijft een klein bij de kloppers aan",
            "Twee even grote tandwielen, zodat er niets aan de snelheid verandert",
            "Een gekruiste riem tussen de motor en de kloppers, zonder tandwielen",
        ],
        antwoord=0,
        uitleg="Een klein tandwiel dat een groot aandrijft, maakt de beweging trager, en trager betekent meer kracht. Groot op klein zou de kloppers nog sneller laten draaien. Een gekruiste riem keert alleen de zin om.",
    ),
    dict(
        type="invultekst",
        vraag="Een groot tandwiel drijft een klein tandwiel aan. Is die overbrenging een versnelling of een vertraging? Antwoord met één woord.",
        antwoord="versnelling",
        uitleg="Groot drijft klein: het kleine wiel is met minder tanden al rond en draait dus sneller. Dat is een versnelling, en die levert minder kracht. Klein op groot zou een vertraging zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee even grote wielen met een gekruiste riem draaien even snel, maar in tegengestelde zin.",
        antwoord=True,
        uitleg="Even grote wielen draaien even snel, met of zonder kruising. Het kruisen van de riem verandert alleen de zin: de volger draait de andere kant op.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een tandwiel met \(20\) tanden drijft een tandwiel met \(60\) tanden aan. Het grote wiel moet \(4\) keer rondgaan. Hoe vaak moet het kleine wiel daarvoor rondgaan? Antwoord met een getal.",
        antwoord="12",
        reken="4 * 60 / 20",
        uitleg=r"Vier toeren van het grote wiel zijn \(4\) maal \(60\), dus \(240\) tanden. Het kleine wiel is na \(20\) tanden rond, dus het moet \(240\) gedeeld door \(20\), of \(12\) keer draaien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet dat de volger trager draait dan de drijver, en dat de twee in tegengestelde zin draaien. Welke overbrenging is het?",
        opties=[
            "Een klein tandwiel dat in een groot tandwiel grijpt",
            "Een groot tandwiel dat in een klein tandwiel grijpt",
            "Een gewone riem van een klein naar een groot wiel",
            "Twee even grote tandwielen die in elkaar grijpen",
        ],
        antwoord=0,
        uitleg="Tegengesteld draaien doen tandwielen die in elkaar grijpen; een gewone riem houdt dezelfde zin. Trager draaien betekent dat de volger het grootste wiel is. Dus een klein tandwiel dat een groot aandrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Tandwiel A heeft \(15\) tanden en drijft tandwiel B met \(45\) tanden rechtstreeks aan. Welke uitspraken kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "B draait drie keer trager dan A",
            "B draait in de andere zin dan A",
            "B kan meer kracht leveren dan A",
            "B draait drie keer sneller dan A",
            "A en B draaien in dezelfde zin",
        ],
        antwoord=[0, 1, 2],
        uitleg=r"B heeft drie keer zoveel tanden, dus het draait drie keer trager, en trager betekent meer kracht. Omdat de twee rechtstreeks in elkaar grijpen, draaien ze tegengesteld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee wielen staan een halve meter uit elkaar. De overbrenging tussen beide mag nooit slippen, ook niet bij een grote kracht. Welke kies je?",
        opties=[
            "Een ketting over twee tandwielen",
            "Een riem over twee gladde wielen",
            "Twee tandwielen die in elkaar grijpen",
            "Twee wrijvingswielen die elkaar raken",
        ],
        antwoord=0,
        uitleg="Een halve meter overbrug je alleen onrechtstreeks, met een riem of een ketting, want rechtstreekse wielen moeten elkaar raken. Van die twee kan alleen de ketting niet slippen.",
    ),
]
