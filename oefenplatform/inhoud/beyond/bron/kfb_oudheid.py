# -*- coding: utf-8 -*-
"""Kunst van de prehistorie, Egypte en de klassieke oudheid.

Derde thema kunstbeschouwing (fiche 3DDO, kunsthistorisch referentiekader).
De fiche vraagt bij elke stroming de basiskenmerken (context en vormelijke
kenmerken), de belangrijkste vertegenwoordigers, en die kenmerken toepassen
op een ongezien werk. Hier:

    kunst van de prehistorie: schilderkunst, beeldhouwkunst
    kunst van Egypte en het nabije Oosten
    kunst van de klassieke oudheid: Griekse kunst, Romeinse kunst

Bij de vertegenwoordigers blijft het bij de bekendste namen en werken uit
elk handboek: Lascaux en Altamira, de Venus van Willendorf, de piramiden van
Gizeh, de Ishtarpoort, het Parthenon met Phidias, de Discuswerper van Myron,
de Doryphoros van Polykleitos, het Pantheon en het Colosseum.

Deel 1 zijn de prehistorie en Egypte met het nabije Oosten.
Deel 2 is de klassieke oudheid.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat stellen de grotschilderingen van Lascaux en Altamira vooral voor?",
        opties=[
            "dieren zoals bizons, paarden en herten",
            "goden en godinnen met een menselijk lichaam",
            "portretten van koningen en hun familie",
            "landschappen met rivieren en bergen",
        ],
        antwoord=0,
        uitleg="De prehistorische grotschilderingen tonen vooral jachtdieren. Mensen staan er zelden en dan heel eenvoudig op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee schilderden prehistorische mensen in de grotten?",
        opties=[
            "natuurlijke pigmenten zoals oker, houtskool en aarde",
            "olieverf op houten panelen",
            "fresco op natte kalk, zoals in de renaissance",
            "acrylverf uit tubes",
        ],
        antwoord=0,
        uitleg="Ze gebruikten aarde, oker en houtskool, soms gemengd met vet, en bliezen verf ook door een holle buis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kenmerk van de Venus van Willendorf?",
        opties=[
            "een klein vrouwenbeeldje met sterk benadrukte borsten, buik en heupen",
            "een levensgroot marmeren beeld van een godin in een tempel",
            "een geschilderd portret van een koningin op een grotwand",
            "een beeld met een perfect berekende, slanke lichaamsverhouding",
        ],
        antwoord=0,
        uitleg="Het beeldje is maar ongeveer 11 centimeter hoog. Men denkt dat de vormen met vruchtbaarheid te maken hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maakten prehistorische mensen wellicht grotschilderingen van dieren?",
        opties=[
            "men denkt aan magie of rituelen rond de jacht",
            "om ze te verkopen op een markt",
            "om de grotten gezellig te maken voor bezoekers",
            "om de kerk te versieren",
        ],
        antwoord=0,
        uitleg="Zeker weten we het niet, want er zijn geen geschreven bronnen. Een veel gehoorde uitleg is jachtmagie of een ritueel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke regel volgden Egyptische kunstenaars bij het tekenen van een mens?",
        opties=[
            "hoofd en benen van opzij, oog en schouders van voren",
            "alles vanuit één standpunt, met een verdwijnpunt",
            "de figuur in een sterke draaiing, met diagonale beweging",
            "het lichaam in een losse houding met het gewicht op één been",
        ],
        antwoord=0,
        uitleg="Zo toonden ze elk lichaamsdeel van zijn meest herkenbare kant. Men noemt dat de aspectieve weergave.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de farao op Egyptische reliëfs vaak veel groter afgebeeld dan de andere mensen?",
        opties=[
            "de grootte toont hoe belangrijk iemand is",
            "de farao was echt veel groter dan zijn onderdanen",
            "hij stond dichter bij de kunstenaar",
            "om het perspectief juist weer te geven",
        ],
        antwoord=0,
        uitleg="De belangrijkste figuur is de grootste. Dat noem je een hiërarchische weergave.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de belangrijkste functie van de piramiden van Gizeh?",
        opties=[
            "grafmonument voor een farao, voor zijn leven na de dood",
            "woning van de farao en zijn familie",
            "tempel waar het volk elke week samenkwam",
            "uitkijktoren om vijanden te zien naderen",
        ],
        antwoord=0,
        uitleg="De Egyptenaren geloofden in een leven na de dood. Grote delen van hun kunst staan daarmee in verband.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken passen bij Egyptische beeldhouwkunst?",
        opties=[
            "strak en frontaal, gericht op eeuwigheid",
            "symmetrisch en stijf, met de armen vaak tegen het lichaam",
            "vol beweging, met wapperende kleren en draaiende lichamen",
            "realistische portretten met rimpels en littekens",
        ],
        antwoord=[0, 1],
        uitleg="Egyptische beelden zijn rustig, frontaal en symmetrisch. Ze moesten eeuwig blijven, niet bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk bouwwerk hoort bij de kunst van het nabije Oosten, in Mesopotamië?",
        opties=["de ziggoerat", "het Parthenon", "het Colosseum", "de kathedraal"],
        antwoord=0,
        uitleg="Een ziggoerat is een trapvormige tempeltoren. De Ishtarpoort van Babylon, met blauwe geglazuurde tegels en dieren, is een ander bekend voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor de Ishtarpoort van Babylon?",
        opties=[
            "blauwe geglazuurde bakstenen met dieren in reliëf",
            "witte marmeren zuilen met acanthusbladeren",
            "spitse bogen met grote glasramen",
            "een koepel van beton met een opening bovenaan",
        ],
        antwoord=0,
        uitleg="De poort is versierd met leeuwen, stieren en draken op blauwe tegels.",
    ),
    dict(
        type="invultekst",
        vraag="Egyptenaren schreven met beeldtekens die men ... noemt.",
        antwoord=["hiërogliefen", "hierogliefen"],
        uitleg="Hiërogliefen staan vaak samen met afbeeldingen op muren en grafkamers.",
    ),
    dict(
        type="invultekst",
        vraag="Een trapvormige tempeltoren uit Mesopotamië heet een ...",
        antwoord=["ziggoerat", "zigurat", "ziggurat"],
        uitleg="Op de top stond een heiligdom voor de god van de stad.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit de prehistorie bestaan geschreven bronnen die precies uitleggen waarom de grotschilderingen gemaakt werden.",
        antwoord=False,
        uitleg="Prehistorie is net de tijd vóór het schrift. Over de bedoeling kunnen we enkel vermoedens hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="Egyptische kunst bleef duizenden jaren opvallend gelijk van stijl.",
        antwoord=True,
        uitleg="Vaste regels en het streven naar eeuwigheid zorgden voor weinig verandering.",
    ),
    dict(
        type="waarofniet",
        vraag="Egyptische kunstenaars tekenden figuren met een diep perspectief en een verdwijnpunt.",
        antwoord=False,
        uitleg="Ze werkten vlak en aspectief. Het perspectief met verdwijnpunt komt pas in de renaissance.",
    ),
    dict(
        type="waarofniet",
        vraag="Veel Egyptische kunst had te maken met het geloof in een leven na de dood.",
        antwoord=True,
        uitleg="Grafkamers, sarcofagen en beelden moesten de dode helpen in het hiernamaals.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien beeld: een stijve, rechtopstaande man, frontaal, één voet iets naar voren, de armen tegen het lichaam, met een hoofddoek met strepen. Uit welke kunst komt het wellicht?",
        opties=["Egyptische kunst", "Romeinse kunst", "barok", "prehistorische kunst"],
        antwoord=0,
        uitleg="Frontaliteit, symmetrie en de typische hoofddoek wijzen op Egypte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de context van de prehistorische kunst?",
        opties=[
            "rondtrekkende jagers en verzamelaars, zonder schrift",
            "een rijk keizerrijk met wegen en steden",
            "een samenleving waarin de kerk alle kunst bestelde",
            "een tijd van fabrieken en stoommachines",
        ],
        antwoord=0,
        uitleg="De prehistorische mensen leefden van jagen en verzamelen. Het schrift bestond nog niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn er van de Egyptische kunst zoveel werken bewaard gebleven?",
        opties=[
            "ze waren gemaakt voor de eeuwigheid, in steen, en lagen goed beschermd in droge graven",
            "ze werden pas honderd jaar geleden gemaakt",
            "ze hingen altijd in musea",
            "ze waren van plastic gemaakt",
        ],
        antwoord=0,
        uitleg="Het droge klimaat en de stevige graven hielpen om veel te bewaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben prehistorische en Egyptische kunst gemeen?",
        opties=[
            "ze hangen sterk samen met geloof, rituelen of het leven na de dood",
            "ze gebruiken allebei perspectief met een verdwijnpunt",
            "ze zijn allebei vooral gemaakt om te verkopen",
            "ze tonen allebei vooral realistische portretten van gewone mensen",
        ],
        antwoord=0,
        uitleg="In beide gevallen speelt kunst een rol in geloof en rituelen, eerder dan als decoratie of handel.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat streefden Griekse beeldhouwers in de klassieke periode na?",
        opties=[
            "een ideale, harmonieuze schoonheid met perfecte verhoudingen",
            "een zo lelijk mogelijke weergave om de kijker te schokken",
            "een vlakke, frontale weergave zoals in Egypte",
            "abstracte vormen zonder herkenbare mensen",
        ],
        antwoord=0,
        uitleg="De Grieken zochten het ideale lichaam, in evenwicht en met de juiste verhoudingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is contrapposto?",
        opties=[
            "een houding waarbij het gewicht op één been rust, zodat het lichaam natuurlijk en los staat",
            "een beeld dat aan twee kanten van de straat staat",
            "een schilderij met sterke tegenstellingen tussen licht en donker",
            "een zuil met een gekrulde bovenkant",
        ],
        antwoord=0,
        uitleg="Door het gewicht op één been kantelen heupen en schouders. Het beeld lijkt levendiger dan een stijve Egyptische figuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie bouworden kent de Griekse architectuur?",
        opties=["Dorisch", "Ionisch", "Korinthisch", "Gotisch"],
        antwoord=[0, 1, 2],
        uitleg="Dorisch is sober, Ionisch heeft voluten (krullen), Korinthisch heeft acanthusbladeren. Gotisch is middeleeuws.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een zuil met een kapiteel vol acanthusbladeren. Welke orde is dat?",
        opties=["Korinthisch", "Dorisch", "Ionisch", "Romaans"],
        antwoord=0,
        uitleg="De Korinthische orde is de rijkst versierde, met bladeren op het kapiteel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beeldhouwer hoort bij het Parthenon in Athene?",
        opties=["Phidias", "Myron", "Michelangelo", "Bernini"],
        antwoord=0,
        uitleg="Phidias leidde het beeldhouwwerk van het Parthenon. Michelangelo en Bernini zijn veel later.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk beroemd beeld maakte Myron?",
        opties=["de Discuswerper", "de Venus van Willendorf", "David", "de Doryphoros"],
        antwoord=0,
        uitleg="De Discuswerper toont een atleet in volle beweging. De Doryphoros of speerdrager is van Polykleitos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is typisch voor een Romeins portretbeeld?",
        opties=[
            "het toont iemand realistisch, met rimpels en eigen trekken",
            "het toont altijd een ideaal, jong lichaam zonder eigen trekken",
            "het is vlak en frontaal zoals in Egypte",
            "het bestaat uit geometrische vormen zonder gezicht",
        ],
        antwoord=0,
        uitleg="Romeinen vonden het belangrijk om een persoon herkenbaar te tonen, vaak oud en waardig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke technieken maakten de grote Romeinse bouwwerken mogelijk?",
        opties=["de rondboog", "de koepel", "beton", "de spitsboog"],
        antwoord=[0, 1, 2],
        uitleg="Met bogen, koepels en beton bouwden de Romeinen aquaducten, het Pantheon en het Colosseum. De spitsboog is gotisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk Romeins gebouw heeft een enorme betonnen koepel met een ronde opening bovenaan?",
        opties=["het Pantheon", "het Parthenon", "het Colosseum", "de ziggoerat"],
        antwoord=0,
        uitleg="De opening bovenaan heet het oculus. Het Parthenon is Grieks.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn veel Griekse beelden vandaag vooral bekend via Romeinse kopieën?",
        opties=[
            "de Romeinen bewonderden de Griekse kunst en lieten ze in marmer kopiëren, terwijl veel bronzen originelen verloren gingen",
            "de Grieken verboden om hun eigen beelden te bewaren",
            "de Grieken maakten hun beelden enkel uit hout",
            "Romeinse kopieën zijn altijd beter dan het origineel",
        ],
        antwoord=0,
        uitleg="Veel Griekse originelen waren in brons en werden later omgesmolten.",
    ),
    dict(
        type="invultekst",
        vraag="Een staande houding waarbij het gewicht op één been rust, heet ...",
        antwoord=["contrapposto"],
        uitleg="Het woord is Italiaans en betekent tegenstelling: heupen en schouders kantelen tegengesteld.",
    ),
    dict(
        type="invultekst",
        vraag="De soberste Griekse bouworde, zonder voet onder de zuil, is de ... orde.",
        antwoord=["Dorische", "dorische", "Dorisch"],
        uitleg="Het Parthenon is in de Dorische orde gebouwd.",
    ),
    dict(
        type="waarofniet",
        vraag="Griekse beelden waren oorspronkelijk vaak beschilderd, ook al zien we ze nu wit.",
        antwoord=True,
        uitleg="Onderzoek vond resten van verf. De verf is in de loop der eeuwen verdwenen.",
    ),
    dict(
        type="waarofniet",
        vraag="De Romeinen namen niets over van de Griekse kunst.",
        antwoord=False,
        uitleg="De Romeinen namen veel over, zoals de bouworden en het beeldhouwen, maar voegden er eigen dingen aan toe.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Colosseum in Rome is een amfitheater voor spelen en gevechten.",
        antwoord=True,
        uitleg="Het Colosseum diende voor gladiatorengevechten en andere spektakels voor het volk.",
    ),
    dict(
        type="waarofniet",
        vraag="De klassieke Griekse beelden tonen vooral stijve figuren met de armen tegen het lichaam, zoals in Egypte.",
        antwoord=False,
        uitleg="De klassieke Griekse beelden staan losser, met contrapposto en beweging. Vroege Griekse beelden leken nog meer op Egyptische.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien marmeren beeld van een naakte, jonge atleet in een losse houding, met een perfect lichaam en een rustig gezicht. Uit welke kunst komt het wellicht?",
        opties=["Griekse kunst", "Egyptische kunst", "prehistorische kunst", "gotische kunst"],
        antwoord=0,
        uitleg="Het ideale lichaam, contrapposto en rust zijn typisch voor de klassieke Griekse beeldhouwkunst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een ongezien borstbeeld van een oudere man met diepe rimpels, een kale kop en een vastberaden blik. Uit welke kunst komt het wellicht?",
        opties=["Romeinse kunst", "Griekse kunst", "Egyptische kunst", "prehistorische kunst"],
        antwoord=0,
        uitleg="Het realistische portret met ouderdomstekens is typisch Romeins.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke context hoort bij de Griekse kunst?",
        opties=[
            "stadstaten zoals Athene, waar de mens, de rede en de democratie centraal stonden",
            "een rijk waarin één farao als god werd vereerd",
            "jagers en verzamelaars die in grotten schuilden",
            "een tijd waarin de kerk de grootste opdrachtgever was",
        ],
        antwoord=0,
        uitleg="In Athene stonden de mens en zijn verstand centraal. Dat zie je terug in het ideale menselijke lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bouwden de Romeinen zoveel wegen, aquaducten en grote openbare gebouwen?",
        opties=[
            "om een groot rijk te besturen en de macht van Rome te tonen",
            "omdat de goden hen verboden om tempels te bouwen",
            "om de bouwkunst van de Egyptenaren na te doen",
            "omdat ze geen beeldhouwers hadden",
        ],
        antwoord=0,
        uitleg="Romeinse kunst en bouwkunst dienden vaak het rijk: nuttig en indrukwekkend tegelijk.",
    ),
]
