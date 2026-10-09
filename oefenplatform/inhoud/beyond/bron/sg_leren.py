# -*- coding: utf-8 -*-
"""Ontwikkeling: de behavioristische en de cognitieve benadering.

Benadering drie en vier van de zes. Deze twee gaan over leren: de
behavioristische over wat je van buitenaf kan zien en meten, de cognitieve
over wat er in het hoofd gebeurt.

De namen en de schema's staan letterlijk in de fiche:

    behavioristische benadering
        klassieke conditionering: Ivan Pavlov, John B. Watson
            S-R-schema, ongeconditioneerde stimulus en reflex, neutrale
            stimulus, geconditioneerde stimulus en reflex, het experiment van
            Pavlov, het Little Albert-experiment
        operante conditionering: B.F. Skinner
            S-R-C-schema, Skinner-box, bekrachtiging (positief en negatief),
            straf (positief en negatief)
    cognitieve benadering
        sociaal-cognitieve leertheorie: Albert Bandura - modelleren,
            imitatieleren, Bobo doll experiment (voorloper van de cognitieve
            benadering)
        theorie van cognitieve ontwikkeling: Jean Piaget - sensomotorisch,
            pre-operationeel, concreet-operationeel, formeel-operationeel
        informatieverwerkingstheorie - sensorisch geheugen,
            kortetermijngeheugen, langetermijngeheugen (expliciet: episodisch
            en semantisch; impliciet: procedureel)

Let op bij de vier soorten gevolg van Skinner. Positief en negatief zeggen
niets over leuk of niet leuk, maar over toevoegen of wegnemen. Dat verschil is
hier meerdere keren gevraagd, want het is de klassieke valkuil.

Deel 1 is de behavioristische benadering.
Deel 2 is de cognitieve benadering.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar kijkt de behavioristische benadering van ontwikkeling naar?",
        opties=[
            "naar gedrag dat je van buitenaf kan zien en meten",
            "naar gedachten en gevoelens binnen in iemand",
            "naar de genen en de rijping van het lichaam",
            "naar de cultuur waarin iemand opgroeit",
        ],
        antwoord=0,
        uitleg="Behaviour betekent gedrag. Het behaviorisme wil alleen uitspraken doen over wat je kan waarnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee vormen van conditionering horen volgens de fiche bij de behavioristische benadering?",
        opties=[
            "de klassieke conditionering",
            "de operante conditionering",
            "de sociaal-cognitieve conditionering",
            "de systemische conditionering",
        ],
        antwoord=[0, 1],
        uitleg="De klassieke conditionering van Pavlov en Watson, en de operante conditionering van Skinner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee namen zet de fiche bij de klassieke conditionering?",
        opties=[
            "Ivan Pavlov",
            "John B. Watson",
            "B.F. Skinner",
            "Albert Bandura",
        ],
        antwoord=[0, 1],
        uitleg="Pavlov met zijn honden en Watson met het Little Albert-experiment. Skinner hoort bij de operante conditionering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de letters in het S-R-schema?",
        opties=[
            "stimulus en respons",
            "straf en respons",
            "stimulus en reflex",
            "signaal en reactie",
        ],
        antwoord=0,
        uitleg="Een stimulus is een prikkel, een respons is de reactie erop. Bij Skinner komt er een derde letter bij: C van consequentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het experiment van Pavlov begint een hond te kwijlen bij het zien van vlees. Wat is het vlees?",
        opties=[
            "een ongeconditioneerde stimulus",
            "een neutrale stimulus",
            "een geconditioneerde stimulus",
            "een geconditioneerde reflex",
        ],
        antwoord=0,
        uitleg="Het vlees werkt vanzelf, zonder dat de hond iets geleerd heeft. Dat is een ongeconditioneerde stimulus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor het experiment begint, laat een belletje de hond van Pavlov volledig koud. Wat is dat belletje op dat moment?",
        opties=[
            "een neutrale stimulus",
            "een ongeconditioneerde stimulus",
            "een geconditioneerde stimulus",
            "een ongeconditioneerde reflex",
        ],
        antwoord=0,
        uitleg="Een neutrale stimulus doet nog niets. Pas na het koppelen aan het vlees wordt ze een geconditioneerde stimulus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Na vele keren koppelen kwijlt de hond al bij het belletje alleen. Hoe heet die reactie?",
        opties=[
            "een geconditioneerde reflex",
            "een ongeconditioneerde reflex",
            "een neutrale respons",
            "een negatieve bekrachtiging",
        ],
        antwoord=0,
        uitleg="Het kwijlen bij het belletje is geleerd, dus geconditioneerd. Het kwijlen bij het vlees was ongeconditioneerd.",
    ),
    dict(
        type="invultekst",
        vraag="Een prikkel die op zichzelf nog niets doet bij een proefdier, heet een ... stimulus.",
        antwoord=["neutrale", "neutrale stimulus"],
        uitleg="Een neutrale stimulus. Door ze telkens samen met de ongeconditioneerde stimulus aan te bieden, wordt ze geconditioneerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Little Albert-experiment hoort bij de klassieke conditionering.",
        antwoord=True,
        uitleg="Waar. Watson maakte een jongetje bang voor iets waar het eerst niet bang voor was, door het te koppelen aan een hard geluid.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Little Albert-experiment zou vandaag zonder bezwaar opnieuw mogen worden uitgevoerd.",
        antwoord=False,
        uitleg="Niet waar. Een kind opzettelijk bang maken komt nooit door een ethische commissie. De fiche noemt het experiment wel, als geschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de derde letter in het S-R-C-schema van Skinner?",
        opties=[
            "consequentie, het gevolg van het gedrag",
            "controle, het toezicht op het gedrag",
            "conditie, de staat van het proefdier",
            "continuïteit, het verloop van het gedrag",
        ],
        antwoord=0,
        uitleg="Bij Skinner wordt gedrag gestuurd door wat erna komt. Dat gevolg heet de consequentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekenen positief en negatief bij de bekrachtiging en de straf van Skinner?",
        opties=[
            "toevoegen of wegnemen",
            "leuk of niet leuk",
            "vaak of zelden",
            "sterk of zwak",
        ],
        antwoord=0,
        uitleg="Positief is iets toevoegen, negatief is iets wegnemen. Dat is de valkuil: negatief betekent niet onaangenaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Sofie krijgt een sticker als ze haar boekentas opruimt, en ruimt sindsdien elke dag op. Wat is dit?",
        opties=[
            "positieve bekrachtiging",
            "negatieve bekrachtiging",
            "positieve straf",
            "negatieve straf",
        ],
        antwoord=0,
        uitleg="Er komt iets aangenaams bij, en het gedrag neemt toe. Dus bekrachtiging, en positief omdat er iets bij komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Ruben moet de vaat niet doen in de week dat hij al zijn taken maakt, en maakt sindsdien al zijn taken. Wat is dit?",
        opties=[
            "negatieve bekrachtiging",
            "positieve bekrachtiging",
            "negatieve straf",
            "positieve straf",
        ],
        antwoord=0,
        uitleg="Er wordt iets onaangenaams weggenomen, en het gedrag neemt toe. Dus bekrachtiging, en negatief omdat er iets weg gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Nina mag een week niet gamen nadat ze gelogen heeft, en liegt sindsdien minder. Wat is dit?",
        opties=[
            "negatieve straf",
            "positieve straf",
            "negatieve bekrachtiging",
            "positieve bekrachtiging",
        ],
        antwoord=0,
        uitleg="Er wordt iets aangenaams weggenomen en het gedrag neemt af. Dus straf, en negatief omdat er iets weg gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hond krijgt een standje als hij op de zetel springt, en springt er sindsdien minder op. Wat is dit?",
        opties=[
            "positieve straf",
            "negatieve straf",
            "positieve bekrachtiging",
            "negatieve bekrachtiging",
        ],
        antwoord=0,
        uitleg="Er komt iets onaangenaams bij en het gedrag neemt af. Dus straf, en positief omdat er iets bij komt.",
    ),
    dict(
        type="invultekst",
        vraag="Het kooitje waarin Skinner zijn proefdieren liet leren door op een knop te duwen, heet de ...",
        antwoord=["Skinner-box", "Skinnerbox", "skinner box"],
        uitleg="De Skinner-box. Het dier ontdekt er zelf dat duwen op de knop voedsel oplevert.",
    ),
    dict(
        type="waarofniet",
        vraag="Het verschil tussen bekrachtiging en straf zit in de vraag of het gedrag erna toeneemt of afneemt.",
        antwoord=True,
        uitleg="Waar. Bekrachtiging doet gedrag toenemen, straf doet het afnemen. Positief en negatief zeggen alleen of er iets bij komt of weg gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij klassieke conditionering leert iemand door het gevolg van zijn eigen gedrag, bij operante conditionering door twee prikkels te koppelen.",
        antwoord=False,
        uitleg="Niet waar, dat staat omgekeerd. Klassiek is het koppelen van prikkels, operant is leren van het gevolg van je gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk antwoord geeft het behaviorisme op de tweede basisvraag?",
        opties=[
            "het legt de nadruk op nurture",
            "het legt de nadruk op nature",
            "het legt de nadruk op zelfbepaling",
            "het geeft er geen antwoord op",
        ],
        antwoord=0,
        uitleg="Voor het behaviorisme is bijna alles geleerd, en dus komt het van buitenaf. Dat is de kant van nurture.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar kijkt de cognitieve benadering naar?",
        opties=[
            "naar wat er in het hoofd met informatie gebeurt",
            "naar wat je aan gedrag van buitenaf kan meten",
            "naar de genen en de erfelijkheid",
            "naar de systemen rond een kind",
        ],
        antwoord=0,
        uitleg="Cognitie is denken, onthouden en verwerken. De cognitieve benadering kijkt dus naar het hoofd, niet alleen naar het gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de sociaal-cognitieve leertheorie?",
        opties=[
            "Albert Bandura",
            "Jean Piaget",
            "B.F. Skinner",
            "Lev Vygotsky",
        ],
        antwoord=0,
        uitleg="Bandura. De fiche noemt zijn theorie een voorloper van de cognitieve benadering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Bandura met modelleren?",
        opties=[
            "leren door te kijken naar wat iemand anders doet",
            "leren door zelf te proberen en beloond te worden",
            "leren door een stimulus aan een prikkel te koppelen",
            "leren door informatie in het geheugen te sorteren",
        ],
        antwoord=0,
        uitleg="Bij modelleren kijkt iemand naar een model en neemt het gedrag over. Dat heet ook imitatieleren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet het bekende experiment van Bandura met een opblaaspop?",
        opties=[
            "het Bobo doll experiment",
            "het Little Albert-experiment",
            "het experiment van Pavlov",
            "het experiment met de Skinner-box",
        ],
        antwoord=0,
        uitleg="Het Bobo doll experiment. Kinderen die een volwassene zagen slaan, sloegen daarna zelf ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt de fiche de theorie van Bandura een voorloper van de cognitieve benadering en geen zuiver behaviorisme?",
        opties=[
            "omdat leren bij hem ook zonder bekrachtiging gebeurt",
            "omdat hij niet met proefpersonen werkte",
            "omdat hij alleen naar gedrag van dieren keek",
            "omdat hij geen enkele rol gaf aan de omgeving",
        ],
        antwoord=0,
        uitleg="Bij Bandura leert een kind door te kijken, ook als het zelf niets beloond krijgt. Er gebeurt dus iets in het hoofd.",
    ),
    dict(
        type="invultekst",
        vraag="Het woord van Bandura voor gedrag overnemen van iemand naar wie je kijkt, is ...",
        antwoord=["imitatieleren", "modelleren", "imitatie"],
        uitleg="Imitatieleren, ook modelleren genoemd. De fiche zet beide woorden bij Bandura.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel stadia onderscheidt Piaget in de cognitieve ontwikkeling?",
        opties=[
            "vier",
            "vijf",
            "drie",
            "acht",
        ],
        antwoord=0,
        uitleg="Vier: het sensomotorische, het pre-operationele, het concreet-operationele en het formeel-operationele stadium.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk stadium van Piaget komt als eerste?",
        opties=[
            "het sensomotorische stadium",
            "het pre-operationele stadium",
            "het concreet-operationele stadium",
            "het formeel-operationele stadium",
        ],
        antwoord=0,
        uitleg="Het sensomotorische stadium hoort bij de baby- en peutertijd: leren via de zintuigen en de beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind van negen kan heel goed rekenen met echte blokjes, maar loopt vast bij een som met letters in plaats van getallen. In welk stadium van Piaget zit het?",
        opties=[
            "het concreet-operationele stadium",
            "het formeel-operationele stadium",
            "het pre-operationele stadium",
            "het sensomotorische stadium",
        ],
        antwoord=0,
        uitleg="Concreet-operationeel betekent dat denken lukt zolang het over echte, tastbare dingen gaat. Abstract denken komt pas later.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zestienjarige kan nadenken over een wet die nog niet bestaat en de gevolgen ervan afwegen. In welk stadium van Piaget zit hij?",
        opties=[
            "het formeel-operationele stadium",
            "het concreet-operationele stadium",
            "het pre-operationele stadium",
            "het sensomotorische stadium",
        ],
        antwoord=0,
        uitleg="Formeel-operationeel is abstract kunnen denken, over dingen die er niet zijn en over mogelijkheden.",
    ),
    dict(
        type="invultekst",
        vraag="Het stadium van Piaget waarin een baby de wereld vooral leert kennen via zijn zintuigen en zijn beweging, is het ... stadium.",
        antwoord=["sensomotorische", "sensomotorisch"],
        uitleg="Het sensomotorische stadium. Senso staat voor de zintuigen, motorisch voor de beweging.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Piaget doorlopen kinderen de vier stadia in een vaste orde, zonder er een over te slaan.",
        antwoord=True,
        uitleg="Waar. Daarom is de theorie van Piaget een antwoord van discontinuïteit op de eerste basisvraag.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pre-operationele stadium komt bij Piaget na het concreet-operationele.",
        antwoord=False,
        uitleg="Niet waar, het komt ervoor. De orde is sensomotorisch, pre-operationeel, concreet-operationeel, formeel-operationeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten geheugen noemt de informatieverwerkingstheorie?",
        opties=[
            "het sensorisch geheugen",
            "het kortetermijngeheugen",
            "het langetermijngeheugen",
            "het operante geheugen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Informatie komt binnen in het sensorisch geheugen, gaat naar het kortetermijngeheugen en kan dan in het langetermijngeheugen blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het langetermijngeheugen valt uiteen in een expliciet en een impliciet deel. Wat zit in het impliciete deel?",
        opties=[
            "het procedureel geheugen",
            "het episodisch geheugen",
            "het semantisch geheugen",
            "het sensorisch geheugen",
        ],
        antwoord=0,
        uitleg="Het procedureel geheugen is impliciet: fietsen en veters knopen zitten erin, zonder dat je het in woorden kan uitleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je weet nog precies waar je was toen je een belangrijk bericht kreeg. Welk geheugen is dit?",
        opties=[
            "het episodisch geheugen",
            "het semantisch geheugen",
            "het procedureel geheugen",
            "het sensorisch geheugen",
        ],
        antwoord=0,
        uitleg="Het episodisch geheugen bewaart gebeurtenissen die jij zelf hebt meegemaakt. Het hoort bij het expliciete geheugen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je weet dat Brussel de hoofdstad van België is, zonder te weten wanneer je dat geleerd hebt. Welk geheugen is dit?",
        opties=[
            "het semantisch geheugen",
            "het episodisch geheugen",
            "het procedureel geheugen",
            "het kortetermijngeheugen",
        ],
        antwoord=0,
        uitleg="Het semantisch geheugen bewaart feiten en betekenissen, los van de gebeurtenis waarin je ze leerde.",
    ),
    dict(
        type="invultekst",
        vraag="Het geheugen voor vaardigheden die je doet zonder erbij na te denken, zoals fietsen, is het ... geheugen.",
        antwoord=["procedureel", "procedurele"],
        uitleg="Het procedureel geheugen, het impliciete deel van het langetermijngeheugen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het episodisch en het semantisch geheugen horen beide bij het expliciete langetermijngeheugen.",
        antwoord=True,
        uitleg="Waar. Expliciet betekent dat je het in woorden kan zeggen. Episodisch gaat over je eigen ervaringen, semantisch over feiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bandura en Skinner geven op de tweede basisvraag een volledig verschillend antwoord.",
        antwoord=False,
        uitleg="Niet waar. Beiden leggen sterk de nadruk op nurture. Het verschil zit elders: bij Bandura gebeurt er ook iets in het hoofd.",
    ),
]
