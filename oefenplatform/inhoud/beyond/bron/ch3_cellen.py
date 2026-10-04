# -*- coding: utf-8 -*-
"""Galvanische cellen en elektrolyse — 🌍 Beyond, chemie.

Deel 1 gaat over de galvanische cel: de bouw met twee halfcellen, de zoutbrug en
de elektronenbrug, de anode en de kathode met hun pool, de beweging van de
elektronen en de ionen, de bronspanning bij normomstandigheden en de
symbolische voorstelling. Deel 2 gaat over de elektrolyse: de bouw met een
spanningsbron, de gedwongen reactie, en de overeenkomsten en verschillen met de
galvanische cel.

De waarden van de normpotentialen staan in de vraag, want die tabel krijgt het
kind op het examen. Een schema van een cel staat er niet; de bouw wordt in
woorden beschreven.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er aan de anode van een galvanische cel?",
        opties=[
            "de oxidatie, waarbij elektronen vrijkomen",
            "de reductie, waarbij elektronen opgenomen worden",
            "de vorming van de zoutbrug tussen de halfcellen",
            "de meting van de spanning van de hele cel",
        ],
        antwoord=0,
        uitleg="Aan de anode gebeurt altijd de oxidatie, in een galvanische cel én bij "
        "een elektrolyse. Aan de kathode gebeurt de reductie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke pool is de anode in een galvanische cel?",
        opties=[
            "de negatieve pool",
            "de positieve pool",
            "dat hangt af van de gebruikte metalen",
            "dat hangt af van de richting van de zoutbrug",
        ],
        antwoord=0,
        uitleg="Daar komen de elektronen vrij, dus is er een overschot aan negatieve "
        "lading. Bij een elektrolyse is de anode net de positieve pool.",
    ),
    dict(
        type="invultekst",
        vraag="Waar gebeurt de reductie in een galvanische cel?",
        antwoord=["aan de kathode", "kathode", "de kathode"],
        uitleg="Daar nemen de ionen de elektronen op die door de draad zijn gekomen. De "
        "oxidatie gebeurt aan de anode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de zoutbrug in een galvanische cel?",
        opties=[
            "om de ladingen in de twee halfcellen in evenwicht te houden",
            "om de elektronen van de ene halfcel naar de andere te brengen",
            "om de twee oplossingen volledig te laten mengen",
            "om de spanning van de cel te kunnen meten",
        ],
        antwoord=0,
        uitleg="Zonder zoutbrug wordt de ene halfcel te positief en de andere te "
        "negatief, en valt de reactie stil. Ionen bewegen erdoor, elektronen niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De elektronen lopen in een galvanische cel door de zoutbrug van de ene halfcel naar de andere.",
        antwoord=False,
        uitleg="Ze lopen door de draad, de elektronenbrug. Door de zoutbrug bewegen "
        "alleen ionen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kant lopen de elektronen op in een galvanische cel?",
        opties=[
            "van de anode naar de kathode, door de draad",
            "van de kathode naar de anode, door de draad",
            "van de anode naar de kathode, door de zoutbrug",
            "van de kathode naar de anode, door de zoutbrug",
        ],
        antwoord=0,
        uitleg="Ze komen vrij bij de oxidatie en worden aan de kathode opgenomen. De "
        "stroomrichting die men in de natuurkunde afspreekt, is net omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de bronspanning van een galvanische cel bij normomstandigheden?",
        opties=[
            "de normpotentiaal van de kathode min die van de anode",
            "de normpotentiaal van de anode min die van de kathode",
            "de som van de twee normpotentialen",
            "het product van de twee normpotentialen",
        ],
        antwoord=0,
        uitleg="Zo komt er altijd een positief getal uit bij een spontane cel. Het "
        "koppel met de hoogste waarde wordt de kathode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cel met Cu²⁺/Cu op +0,34 V en Zn²⁺/Zn op −0,76 V. Wat is de bronspanning?",
        opties=[
            "1,10 V",
            "0,42 V",
            "0,34 V",
            "0,76 V",
        ],
        antwoord=0,
        uitleg="0,34 min min 0,76 is 1,10 volt. Koper is de kathode, zink de anode.",
    ),
    dict(
        type="invultekst",
        vraag="Welk metaal is de anode in een cel van zink en koper?",
        antwoord=["zink", "het zink", "Zn"],
        uitleg="Zink heeft de laagste normpotentiaal en is dus de sterkste reductor. Het "
        "lost op terwijl er koper neerslaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de elektroden van een galvanische cel zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "aan de anode gebeurt de oxidatie",
            "de anode wordt tijdens het gebruik dunner",
            "aan de anode gebeurt de reductie",
            "de kathode wordt tijdens het gebruik dunner",
        ],
        antwoord=[0, 1],
        uitleg="Het metaal van de anode lost op als ion. Aan de kathode slaat er metaal "
        "neer, dus wordt die juist zwaarder.",
    ),
    dict(
        type="waarofniet",
        vraag="Een galvanische cel zet chemische energie om in elektrische energie.",
        antwoord=True,
        uitleg="De reactie gaat spontaan door en levert daarbij spanning. Bij een "
        "elektrolyse gaat het net de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de symbolische voorstelling Zn/Zn²⁺//Cu²⁺/Cu?",
        opties=[
            "links de anode met haar oplossing, rechts de kathode met de hare",
            "links de kathode met haar oplossing, rechts de anode met de hare",
            "de twee metalen staan in dezelfde oplossing van twee zouten",
            "de twee halfcellen zijn met een draad in plaats van een zoutbrug verbonden",
        ],
        antwoord=0,
        uitleg="De dubbele streep is de zoutbrug. Links staat altijd de oxidatie, rechts "
        "de reductie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet elke halfcel haar eigen oplossing hebben?",
        opties=[
            "anders reageren de twee koppels rechtstreeks, zonder stroom door de draad",
            "anders kan de spanning van de cel niet gemeten worden",
            "anders lost de zoutbrug op in het mengsel van de twee",
            "anders slaat er aan beide elektroden metaal neer",
        ],
        antwoord=0,
        uitleg="Leg je het zink gewoon in de koperoplossing, dan gebeurt de reactie "
        "meteen aan het oppervlak en haal je er geen stroom uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de bronspanning zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is groter als de twee normpotentialen verder uit elkaar liggen",
            "ze wordt uitgedrukt in volt",
            "ze is groter als de twee elektroden dichter bij elkaar staan",
            "ze wordt uitgedrukt in ampère",
        ],
        antwoord=[0, 1],
        uitleg="De afstand tussen de elektroden speelt geen rol voor de spanning. Het "
        "verschil tussen de twee koppels is wat telt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke brug brengt de elektronen van de ene elektrode naar de andere?",
        antwoord=["elektronenbrug", "de draad", "de elektronenbrug"],
        uitleg="Dat is gewoon de geleidende draad met eventueel een toestel ertussen. De "
        "zoutbrug laat enkel ionen door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de massa van de kathode in een galvanische cel met metalen elektroden?",
        opties=[
            "ze wordt groter, want er slaat metaal op neer",
            "ze wordt kleiner, want het metaal lost op",
            "ze blijft gelijk, want de kathode doet niet mee",
            "ze wordt eerst groter en daarna weer kleiner",
        ],
        antwoord=0,
        uitleg="De metaalionen uit de oplossing nemen er elektronen op en worden metaal. "
        "Aan de anode gebeurt het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kant bewegen de negatieve ionen in de zoutbrug?",
        opties=[
            "naar de halfcel van de anode",
            "naar de halfcel van de kathode",
            "ze blijven in de zoutbrug staan",
            "ze bewegen naar beide kanten evenveel",
        ],
        antwoord=0,
        uitleg="Daar komen positieve metaalionen bij, dus moet er negatieve lading naartoe "
        "om alles in evenwicht te houden.",
    ),
    dict(
        type="waarofniet",
        vraag="In een galvanische cel gebeurt de oxidatie aan de positieve pool.",
        antwoord=False,
        uitleg="De oxidatie gebeurt aan de anode, en dat is in een galvanische cel de "
        "negatieve pool. Bij een elektrolyse is die anode wel positief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een batterij is een toepassing van een galvanische cel.",
        antwoord=True,
        uitleg="De spontane redoxreactie binnenin levert spanning. Is de reactie "
        "uitgewerkt, dan is de batterij leeg.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de bronspanning van een cel uit?",
        antwoord=["volt", "V", "in volt"],
        uitleg="De normpotentialen uit de tabel staan ook in volt, elk gemeten tegenover "
        "dezelfde waterstofelektrode.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat heeft een elektrolyse nodig dat een galvanische cel niet nodig heeft?",
        opties=[
            "een spanningsbron die de reactie afdwingt",
            "een zoutbrug tussen twee halfcellen",
            "twee elektroden van verschillend metaal",
            "een oplossing waarin ionen kunnen bewegen",
        ],
        antwoord=0,
        uitleg="Bij een elektrolyse verloopt de reactie niet spontaan. De stroom van "
        "buitenaf duwt ze de andere kant op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke pool is de kathode bij een elektrolyse?",
        opties=[
            "de negatieve pool",
            "de positieve pool",
            "dat hangt af van de gebruikte oplossing",
            "dat hangt af van de sterkte van de spanningsbron",
        ],
        antwoord=0,
        uitleg="De spanningsbron duwt daar elektronen naartoe, dus gebeurt daar de "
        "reductie. In een galvanische cel is de kathode net positief.",
    ),
    dict(
        type="invultekst",
        vraag="Waar gebeurt de oxidatie bij een elektrolyse?",
        antwoord=["aan de anode", "anode", "de anode"],
        uitleg="Dat is bij elke cel zo: oxidatie aan de anode, reductie aan de kathode. "
        "Alleen het teken van de polen verschilt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een gedwongen reactie?",
        opties=[
            "een reactie die enkel doorgaat met energie van buitenaf",
            "een reactie die spontaan doorgaat en energie levert",
            "een reactie die stopt zodra het evenwicht bereikt is",
            "een reactie die enkel met een katalysator doorgaat",
        ],
        antwoord=0,
        uitleg="Bij een elektrolyse dwingt de spanningsbron de reactie de kant op die ze "
        "zelf niet zou nemen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een elektrolyse en in een galvanische cel gebeurt de oxidatie telkens aan de anode.",
        antwoord=True,
        uitleg="Dat is de afspraak die altijd geldt. Wat verschilt, is of die anode de "
        "positieve of de negatieve pool is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een elektrolyse zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "elektrische energie wordt omgezet in chemische energie",
            "de reactie zou zonder spanningsbron niet doorgaan",
            "chemische energie wordt omgezet in elektrische energie",
            "de reactie levert spanning op de twee elektroden",
        ],
        antwoord=[0, 1],
        uitleg="Het is net de omgekeerde omzetting van een galvanische cel. Daarom kan je "
        "met een elektrolyse een batterij weer opladen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan je gesmolten keukenzout elektrolyseren en vast keukenzout niet?",
        opties=[
            "in de smelt kunnen de ionen bewegen, in het vaste rooster niet",
            "de smelt geleidt met elektronen en het rooster met ionen",
            "het vaste rooster heeft te veel elektronen om te geleiden",
            "de smelt heeft een hogere temperatuur en reageert sneller",
        ],
        antwoord=0,
        uitleg="Voor een elektrolyse moet de lading door de vloeistof kunnen. Daarom werkt "
        "het ook met een oplossing.",
    ),
    dict(
        type="invultekst",
        vraag="Welk toestel levert de energie voor een elektrolyse?",
        antwoord=["spanningsbron", "een spanningsbron", "de spanningsbron"],
        uitleg="Zonder die bron gaat de reactie de andere kant op, of gebeurt er niets. "
        "Een galvanische cel heeft er geen nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er aan de kathode bij de elektrolyse van een oplossing van een koperzout?",
        opties=[
            "koper slaat als metaal op de elektrode neer",
            "koperionen gaan in oplossing vanuit de elektrode",
            "zuurstofgas komt vrij aan de elektrode",
            "het koperzout valt uiteen in zijn twee ionen",
        ],
        antwoord=0,
        uitleg="Aan de kathode gebeurt de reductie, en Cu²⁺ plus twee elektronen geeft "
        "koper. Daarop berust het verkoperen van een voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken gelden voor zowel een galvanische cel als een elektrolyse? Kruis alles aan wat juist is.",
        opties=[
            "er is een oxidatie en een reductie",
            "er moeten ionen kunnen bewegen in de vloeistof",
            "er is altijd een spanningsbron nodig",
            "de anode is altijd de negatieve pool",
        ],
        antwoord=[0, 1],
        uitleg="Beide zijn redoxreacties met een gescheiden oxidatie en reductie. Het "
        "verschil zit in spontaan of gedwongen, en in het teken van de polen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een elektrolyse is de anode de positieve pool.",
        antwoord=True,
        uitleg="De spanningsbron trekt daar elektronen weg, dus gebeurt er een oxidatie. "
        "In een galvanische cel is de anode de negatieve pool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men elektrolyse om aluminium te maken?",
        opties=[
            "het aluminiumion is een te zwakke oxidator om spontaan te reageren",
            "aluminium komt in de natuur voor als zuiver metaal",
            "de reactie levert zelf genoeg spanning om door te gaan",
            "aluminium lost enkel op in een zure oplossing",
        ],
        antwoord=0,
        uitleg="Aluminium staat heel laag in de tabel: zijn ion houdt de elektronen niet "
        "graag vast. Daarom kost het veel elektriciteit om het te winnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de anode bij het verzilveren van een voorwerp?",
        opties=[
            "de zilveren anode lost langzaam op in de oplossing",
            "de zilveren anode wordt dikker tijdens het proces",
            "de anode blijft onveranderd en doet niet mee",
            "de anode geeft zuurstofgas af aan de oplossing",
        ],
        antwoord=0,
        uitleg="Zo blijft de concentratie zilverionen gelijk. Het zilver verhuist dus van "
        "de anode naar het voorwerp aan de kathode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verschillen zijn er tussen een galvanische cel en een elektrolyse? Kruis alles aan wat juist is.",
        opties=[
            "de reactie is spontaan of gedwongen",
            "het teken van de polen is omgekeerd",
            "de oxidatie gebeurt aan de kathode in plaats van de anode",
            "er is in het ene geval geen reductie nodig",
        ],
        antwoord=[0, 1],
        uitleg="De plaats van oxidatie en reductie blijft gelijk: anode en kathode. Alleen "
        "spontaan of gedwongen, en het teken van de polen, verschillen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het aanbrengen van een metaallaagje met behulp van elektrolyse?",
        antwoord=["galvaniseren", "galvanisatie", "elektrolytisch verzilveren"],
        uitleg="Verzilveren en verkoperen zijn voorbeelden. Het voorwerp hangt dan aan de "
        "kathode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij de elektrolyse van water ontstaat er waterstofgas en zuurstofgas. Waar ontstaat het waterstofgas?",
        opties=[
            "aan de kathode, want daar gebeurt de reductie",
            "aan de anode, want daar gebeurt de oxidatie",
            "in de zoutbrug tussen de twee elektroden",
            "aan beide elektroden in gelijke hoeveelheid",
        ],
        antwoord=0,
        uitleg="Waterstof gaat van +I naar nul, en dat is een reductie. Het volume "
        "waterstofgas is daarbij dubbel dat van het zuurstofgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laadt een oplaadbare batterij op. Wat gebeurt er dan?",
        opties=[
            "de reactie wordt door een elektrolyse teruggeduwd",
            "de reactie gaat spontaan verder in dezelfde richting",
            "de elektroden worden beide volledig vernieuwd",
            "de zoutbrug wordt opnieuw met zout gevuld",
        ],
        antwoord=0,
        uitleg="Het opladen is dus een gedwongen reactie. Daarom kost opladen energie en "
        "levert ontladen ze.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een elektrolyse bewegen de positieve ionen naar de anode.",
        antwoord=False,
        uitleg="Ze gaan naar de kathode, de negatieve pool, en nemen daar elektronen op. "
        "De negatieve ionen gaan naar de anode.",
    ),
    dict(
        type="waarofniet",
        vraag="Een elektrolyse levert elektrische energie op.",
        antwoord=False,
        uitleg="Ze verbruikt die juist. Een galvanische cel is de omzetting die energie "
        "oplevert.",
    ),
    dict(
        type="invultekst",
        vraag="Welke elektrode wordt bij het verkoperen aan de negatieve pool gehangen?",
        antwoord=["het voorwerp", "voorwerp", "de kathode"],
        uitleg="Daar gebeurt de reductie, en dus slaat het koper juist op dat voorwerp "
        "neer.",
    ),
]
