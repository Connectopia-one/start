# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Chemische reacties en energie.

Hoort bij "chemische reacties" van de vakfiche chemie 2de graad
doorstroomfinaliteit. Eén thema, want dit onderdeel weegt 5 % van het examen.

Deel 1 gaat over de wet van behoud van massa en het kloppend maken van een
reactievergelijking. Deel 2 gaat over exo- en endo-energetische reacties, het
energiediagram en de energievormen die de fiche opsomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van behoud van massa?",
        opties=[
            "de totale massa blijft tijdens een reactie gelijk",
            "de massa neemt toe als er een gas ontstaat",
            "de massa neemt af als er warmte vrijkomt",
            "de massa hangt af van de temperatuur",
        ],
        antwoord=0,
        uitleg="Bij een reactie verdwijnt geen enkel atoom: ze worden alleen anders geschikt. De som van de massa's van de reagentia is dus gelijk aan die van de reactieproducten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de stoffen die links van de pijl in een reactievergelijking staan?",
        opties=[
            "de reagentia",
            "de reactieproducten",
            "de katalysatoren",
            "de indicatoren",
        ],
        antwoord=0,
        uitleg="De reagentia zijn de beginstoffen. Rechts van de pijl staan de reactieproducten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coëfficiënten maken de vergelijking ... H₂ + ... O₂ → ... H₂O kloppend?",
        opties=[
            "2, 1 en 2",
            "1, 1 en 1",
            "1, 2 en 1",
            "2, 2 en 1",
        ],
        antwoord=0,
        uitleg="Met 2 H₂ en 1 O₂ heb je links vier waterstof- en twee zuurstofatomen. Rechts geeft 2 H₂O precies hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het kloppend maken van een vergelijking zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "je past enkel de coëfficiënten aan",
            "het aantal atomen van elk element is links en rechts gelijk",
            "je mag een index in een formule aanpassen",
            "je mag een stof bijschrijven die er niet in staat",
        ],
        antwoord=[0, 1],
        uitleg="Een index aanpassen maakt er een andere stof van, en een stof bijschrijven verzint een reactie. Enkel de coëfficiënten mag je kiezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coëfficiënten maken de vergelijking ... Fe + ... O₂ → ... Fe₂O₃ kloppend?",
        opties=[
            "4, 3 en 2",
            "2, 1 en 1",
            "2, 3 en 2",
            "3, 2 en 1",
        ],
        antwoord=0,
        uitleg="Rechts staan met 2 Fe₂O₃ vier ijzeratomen en zes zuurstofatomen. Links geven 4 Fe en 3 O₂ precies dat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coëfficiënten maken de vergelijking ... CH₄ + ... O₂ → ... CO₂ + ... H₂O kloppend?",
        opties=[
            "1, 2, 1 en 2",
            "1, 1, 1 en 1",
            "2, 2, 2 en 1",
            "1, 3, 1 en 2",
        ],
        antwoord=0,
        uitleg="Één CH₄ geeft één CO₂ en twee H₂O. Rechts staan dan vier zuurstofatomen, dus links twee O₂.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tien gram ijzer reageert volledig met vier gram zwavel. Hoeveel ijzersulfide ontstaat er?",
        opties=[
            "veertien gram",
            "tien gram",
            "zes gram",
            "achttien gram",
        ],
        antwoord=0,
        uitleg="Niets gaat verloren, dus de massa van het product is de som van de twee beginmassa's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kaars brandt op en de kandelaar weegt achteraf lichter. Waarom is dat geen uitzondering op de wet van behoud van massa?",
        opties=[
            "de gassen zijn weggegaan in de lucht",
            "de massa gaat over in warmte",
            "de wet geldt niet voor verbrandingen",
            "de weegschaal is te onnauwkeurig",
        ],
        antwoord=0,
        uitleg="Bij de verbranding ontstaan koolstofdioxide en waterdamp, die wegwaaien. Weeg je in een gesloten vat, dan blijft de massa gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een chemische reactie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er ontstaan nieuwe stoffen",
            "het aantal atomen van elk element blijft gelijk",
            "er verdwijnen atomen",
            "er ontstaan nieuwe elementen",
        ],
        antwoord=[0, 1],
        uitleg="De atomen worden anders gegroepeerd, dus krijg je andere stoffen. Hun aantal en hun soort veranderen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan kan je merken dat er een chemische reactie is gebeurd en niet alleen een vermenging? Kruis alles aan wat juist is.",
        opties=[
            "er ontstaat een neerslag",
            "er komt een gas vrij",
            "het mengsel wordt troebel door zand",
            "de vloeistof wordt dunner",
        ],
        antwoord=[0, 1],
        uitleg="Een neerslag of een gas betekent dat er een nieuwe stof is. Zand dat troebel maakt, blijft gewoon zand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijft men in een reactievergelijking een pijl en geen gelijkheidsteken?",
        opties=[
            "de pijl geeft de richting van de omzetting aan",
            "een gelijkheidsteken bestaat niet in de chemie",
            "de massa is links en rechts niet gelijk",
            "de pijl staat voor de temperatuur",
        ],
        antwoord=0,
        uitleg="De pijl zegt dat de reagentia omgezet worden in de reactieproducten. Het aantal atomen is wel links en rechts gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een chemische reactie worden atomen anders geschikt, maar niet gemaakt of vernietigd.",
        antwoord=True,
        uitleg="Dat is precies de kern van de wet van behoud van massa.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een index in een formule veranderen om een vergelijking kloppend te maken.",
        antwoord=False,
        uitleg="Een index verandert de stof zelf. H₂O₂ is waterstofperoxide en niet meer water.",
    ),
    dict(
        type="waarofniet",
        vraag="In een gesloten vat blijft de massa tijdens een verbranding gelijk.",
        antwoord=True,
        uitleg="De gassen kunnen er niet uit, dus weeg je alles nog. Daarom doet men zo'n proef in een gesloten vat.",
    ),
    dict(
        type="waarofniet",
        vraag="Als er bij een reactie een gas ontstaat, verdwijnt er massa.",
        antwoord=False,
        uitleg="Het gas heeft ook massa. Het ontsnapt alleen uit een open vat, dus lijkt de massa gedaald.",
    ),
    dict(
        type="waarofniet",
        vraag="Een coëfficiënt 1 moet je in een reactievergelijking altijd uitdrukkelijk opschrijven.",
        antwoord=False,
        uitleg="Net als in de wiskunde laat men de één weg. Staat er niets voor een formule, dan is de coëfficiënt toch 1.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stoffen die rechts van de pijl in een reactievergelijking staan?",
        antwoord=["reactieproducten", "de reactieproducten"],
        uitleg="Dat zijn de nieuwe stoffen die na de reactie overblijven.",
    ),
    dict(
        type="invultekst",
        vraag="Welke coëfficiënt hoort voor O₂ in ... H₂ + ... O₂ → 2 H₂O?",
        antwoord=["1", "een", "één"],
        uitleg="Rechts staan twee zuurstofatomen, dus links precies één molecule O₂.",
    ),
    dict(
        type="invultekst",
        vraag="Vijftien gram koper reageert met vier gram zuurstofgas. Hoeveel gram koperoxide ontstaat er?",
        antwoord=["19", "19 g", "negentien"],
        uitleg="Niets gaat verloren: 15 plus 4 is 19 gram.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het getal vooraan een formule, dat zegt hoeveel deeltjes er zijn?",
        antwoord=["coëfficiënt", "de coëfficiënt", "coefficient"],
        uitleg="De coëfficiënt geldt voor het hele deeltje dat erachter staat.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een exo-energetische reactie?",
        opties=[
            "er komt energie vrij",
            "er wordt energie opgenomen",
            "de energie blijft precies gelijk",
            "de massa neemt toe",
        ],
        antwoord=0,
        uitleg="Exo betekent naar buiten. De reactieproducten hebben minder inwendige energie dan de reagentia, en het verschil gaat naar de omgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reacties zijn exo-energetisch? Kruis alles aan wat juist is.",
        opties=[
            "het verbranden van aardgas",
            "een handwarmer die warm wordt",
            "een koudepakje dat koud wordt",
            "het ontleden van water met elektriciteit",
        ],
        antwoord=[0, 1],
        uitleg="Bij een verbranding en bij een handwarmer komt energie vrij. Een koudepakje en het ontleden van water nemen energie op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ligt in het energiediagram van een exo-energetische reactie de energie van de reactieproducten?",
        opties=[
            "lager dan die van de reagentia",
            "hoger dan die van de reagentia",
            "precies even hoog",
            "dat hangt van de temperatuur af",
        ],
        antwoord=0,
        uitleg="Het verschil tussen de twee niveaus is net de energie die naar de omgeving gaat. Daarom liggen de producten lager.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat op de verticale as van een energiediagram?",
        opties=[
            "de inwendige energie",
            "de tijd",
            "de massa",
            "de temperatuur van het lokaal",
        ],
        antwoord=0,
        uitleg="Verticaal staat de inwendige energie van de stoffen, horizontaal het verloop van de reactie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men het verschil in energie tussen de reagentia en de reactieproducten?",
        opties=[
            "de reactie-energie",
            "de massadichtheid",
            "de activeringsenergie",
            "de stofhoeveelheid",
        ],
        antwoord=0,
        uitleg="De reactie-energie is de hoeveelheid die opgenomen of afgestaan wordt. Je leest ze af als het hoogteverschil in het diagram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling meet dat de temperatuur van een oplossing stijgt van 20 naar 34 graden tijdens een reactie. Wat besluit ze?",
        opties=[
            "de reactie is exo-energetisch",
            "de reactie is endo-energetisch",
            "er is geen reactie gebeurd",
            "de massa is toegenomen",
        ],
        antwoord=0,
        uitleg="De oplossing wordt warmer, dus komt er energie vrij uit de reactie. Dat is per definitie exo-energetisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energievorm zit opgeslagen in de bindingen van een stof?",
        opties=[
            "chemische energie",
            "thermische energie",
            "lichtenergie",
            "elektrische energie",
        ],
        antwoord=0,
        uitleg="Chemische energie zit in de bindingen. Bij een reactie wordt ze omgezet in bijvoorbeeld warmte of licht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energievormen komen vrij bij het branden van een kaars? Kruis alles aan wat juist is.",
        opties=[
            "thermische energie",
            "lichtenergie",
            "elektrische energie",
            "kernenergie",
        ],
        antwoord=[0, 1],
        uitleg="Een kaars geeft warmte en licht. Elektriciteit komt er niet aan te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Water ontleden met een batterij in waterstofgas en zuurstofgas: welke omzetting is dat?",
        opties=[
            "elektrische energie wordt chemische energie",
            "chemische energie wordt elektrische energie",
            "lichtenergie wordt thermische energie",
            "thermische energie wordt lichtenergie",
        ],
        antwoord=0,
        uitleg="De batterij levert de energie die nodig is om de bindingen in water te verbreken. Die energie zit daarna in de nieuwe stoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een batterij die een lampje doet branden?",
        opties=[
            "chemische energie wordt elektrische energie",
            "elektrische energie wordt chemische energie",
            "thermische energie wordt chemische energie",
            "lichtenergie wordt chemische energie",
        ],
        antwoord=0,
        uitleg="In een batterij gebeurt een reactie die elektronen levert. De chemische energie van de stoffen wordt zo elektrische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom voelt een koudepakje koud aan?",
        opties=[
            "de reactie neemt warmte op uit de omgeving",
            "er zit ijs in het pakje",
            "de reactie geeft warmte af aan de omgeving",
            "de massa van het pakje daalt",
        ],
        antwoord=0,
        uitleg="Het is een endo-energetische reactie: de stoffen hebben energie nodig en halen die uit hun omgeving, dus uit je hand.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een endo-energetische reactie liggen de reactieproducten hoger in het energiediagram.",
        antwoord=True,
        uitleg="Ze hebben energie opgenomen, dus zit er meer energie in dan in de reagentia.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke verbranding is endo-energetisch.",
        antwoord=False,
        uitleg="Een verbranding geeft juist warmte en vaak licht af, dus is ze exo-energetisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Fotosynthese is een endo-energetische reactie.",
        antwoord=True,
        uitleg="De plant heeft lichtenergie nodig om uit koolstofdioxide en water glucose te maken. Die energie zit daarna in de glucose.",
    ),
    dict(
        type="waarofniet",
        vraag="Aan een energiediagram kan je niet zien of een reactie energie opneemt of afstaat.",
        antwoord=False,
        uitleg="Je ziet het net in één oogopslag: liggen de producten lager, dan komt energie vrij, en liggen ze hoger, dan is er energie opgenomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reactie waarbij de beker koud aanvoelt, is exo-energetisch.",
        antwoord=False,
        uitleg="Koud betekent dat de reactie warmte uit de beker en uit je hand haalt. Dat is endo-energetisch.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een reactie die energie opneemt uit haar omgeving?",
        antwoord=["endo-energetisch", "endo-energetische", "endo energetisch"],
        uitleg="Endo betekent naar binnen: de reactie heeft energie nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Welke energievorm geeft een gloeiende houtskool vooral af, naast licht?",
        antwoord=["warmte", "thermische energie", "warmte-energie"],
        uitleg="Thermische energie, dus warmte, is bij een verbranding de belangrijkste vorm die vrijkomt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de hoeveelheid energie die bij een reactie opgenomen of afgestaan wordt?",
        antwoord=["reactie-energie", "de reactie-energie", "reactie energie"],
        uitleg="Je leest ze in het energiediagram af als het verschil tussen de twee energieniveaus.",
    ),
    dict(
        type="invultekst",
        vraag="Welke energievorm zet een plant bij de fotosynthese om in chemische energie?",
        antwoord=["lichtenergie", "licht", "zonlicht"],
        uitleg="De plant vangt met haar bladgroen het licht op en gebruikt die energie om glucose te vormen.",
    ),
]
