# -*- coding: utf-8 -*-
"""Veilig werken, meetinstrumenten en meetonzekerheid — 🌍 Beyond, fysica.

Deel 1 gaat over veilig en duurzaam werken in het labo en over de keuze van
een meetinstrument: het meetbereik en de nauwkeurigheid respecteren, een
toestel uitschakelen als je niet meet, nooit met natte handen aan
elektriciteit, een handleiding juist lezen, en weten wanneer je een
dynamometer, een chronometer, een multimeter, een sensor of een decibelmeter
nodig hebt en hoe je die correct afleest. Deel 2 gaat over het verwerken van
wat je gemeten hebt: de SI-eenheden met hun voorvoegsels van mega tot nano,
het juiste aantal beduidende cijfers, de wetenschappelijke notatie, het
schatten van een uitkomst, het omvormen en combineren van formules, en het
herkennen van een recht evenredig, omgekeerd evenredig, lineair of kwadratisch
verband.

De rode draad is dat een meting nooit exact is, en dat je dat in je antwoord
laat zien in plaats van het weg te rekenen met een lange reeks cijfers achter
de komma. Veilig en duurzaam werken wordt op het examen uitgelegd en niet
uitgevoerd, dus vragen de vragen naar het waarom van een handeling.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het meetbereik van een meetinstrument?",
        opties=[
            "de kleinste en de grootste waarde die het kan meten",
            "het kleinste verschil dat het nog kan aanwijzen",
            "de afstand waarover je het instrument kan gebruiken",
            "de tijd die het instrument nodig heeft om af te lezen",
        ],
        antwoord=0,
        uitleg="Meet je erbuiten, dan kan het toestel stukgaan of een onzin aanwijzen. Het "
        "kleinste verschil dat het aanwijst, is zijn nauwkeurigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je een meetinstrument niet buiten zijn meetbereik gebruiken?",
        opties=[
            "de meting is dan onbetrouwbaar en het toestel kan beschadigen",
            "de meting duurt dan veel langer dan ze normaal zou duren",
            "het toestel verbruikt dan veel meer stroom",
            "het toestel moet dan achteraf opnieuw geijkt worden",
        ],
        antwoord=0,
        uitleg="Bij een multimeter kan de zekering erin doorbranden. Kies dus eerst het "
        "juiste bereik en meet pas daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen zijn veilig en duurzaam in een fysicalabo? Kruis alles aan wat juist is.",
        opties=[
            "het meetbereik en de nauwkeurigheid van een toestel respecteren",
            "een meetinstrument uitschakelen als je er niet mee meet",
            "de handleiding van een toestel vooraf doorlezen",
            "een toestel met natte handen bedienen om sneller te gaan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Natte handen en elektriciteit zijn levensgevaarlijk, want water geleidt. De "
        "eerste drie sparen bovendien het toestel en de batterij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meetinstrument uitschakelen als je niet meet, hoort bij duurzaam werken.",
        antwoord=True,
        uitleg="Je spaart zo de batterij en de levensduur van het toestel. Bij een "
        "multimeter zet je hem ook terug op een veilige stand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je een kracht?",
        opties=[
            "met een dynamometer",
            "met een multimeter",
            "met een chronometer",
            "met een decibelmeter",
        ],
        antwoord=0,
        uitleg="Een dynamometer is een veer met een schaal in newton. Een multimeter meet "
        "spanning, stroom en weerstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je met een multimeter meten? Kruis alles aan wat juist is.",
        opties=[
            "de spanning over een lamp",
            "de stroom door een draad",
            "de weerstand van een component",
            "de kracht waarmee je aan een touw trekt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voor een kracht heb je een dynamometer nodig. Let op dat je voor stroom en "
        "spanning een andere stand én een andere plaats in de kring kiest.",
    ),
    dict(
        type="invultekst",
        vraag="Waarmee meet je het geluidsniveau in een ruimte?",
        antwoord=["een decibelmeter", "decibelmeter", "geluidsmeter"],
        uitleg="Hij geeft het niveau in decibel. Op een fuif kan je zo nagaan of de "
        "geluidsnorm gehaald wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet kiezen tussen twee chronometers, een van 0,1 s en een van 0,01 s nauwkeurig. Welke neem je voor een val van ongeveer een halve seconde?",
        opties=[
            "die van 0,01 s, want anders is de fout te groot",
            "die van 0,1 s, want die leest makkelijker af",
            "het maakt geen enkel verschil voor het resultaat",
            "geen van de twee, want een val meet je met een sensor",
        ],
        antwoord=0,
        uitleg="Met 0,1 seconde zit je bij een halve seconde al op een vijfde ernaast. Kies "
        "een toestel waarvan de nauwkeurigheid klein is tegenover wat je meet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nauwkeuriger meetinstrument is altijd de beste keuze, wat je ook meet.",
        antwoord=False,
        uitleg="Het is vaak duurder, trager of beperkter in bereik. Je kiest het toestel bij "
        "de meting die je wil doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lees je een analoge meter met een naald correct af?",
        opties=[
            "recht van boven, zodat de naald niet verschoven lijkt",
            "zo schuin mogelijk, want dan zie je de schaalverdeling beter",
            "van onderaf, zodat de naald groter lijkt",
            "met één oog dicht en van de zijkant",
        ],
        antwoord=0,
        uitleg="Kijk je schuin, dan lees je door de parallaxfout een andere waarde. Sommige "
        "toestellen hebben daar zelfs een spiegeltje voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een meting nooit helemaal exact?",
        opties=[
            "elk instrument heeft een beperkte nauwkeurigheid",
            "elke grootheid verandert tijdens het meten van waarde",
            "elke formule is maar een benadering van de werkelijkheid",
            "elke meter is verkeerd geijkt bij het verlaten van de fabriek",
        ],
        antwoord=0,
        uitleg="Daarom geef je je antwoord met een gepast aantal beduidende cijfers. Meer "
        "cijfers opschrijven maakt de meting niet beter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorzorgen horen bij het werken met een radioactieve bron? Kruis alles aan wat juist is.",
        opties=[
            "zo ver mogelijk van de bron blijven",
            "de bron zo kort mogelijk uit zijn houder halen",
            "een afscherming tussen jou en de bron zetten",
            "de bron even opwarmen zodat ze minder straalt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opwarmen doet niets, want verval trekt zich van temperatuur niets aan. "
        "Afstand, tijd en afscherming zijn de drie die werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet je een spanningsbron op de laagste stand voor je hem aansluit?",
        opties=[
            "zo kan je de spanning rustig opdrijven zonder iets te laten doorbranden",
            "zo verbruikt de bron tijdens het aansluiten van de kring minder stroom",
            "zo blijft de weerstand van de kring onveranderd",
            "zo hoef je achteraf niets meer te meten",
        ],
        antwoord=0,
        uitleg="Een lampje of een meter kan bij een te hoge spanning meteen weg zijn. Je "
        "bouwt de kring dus altijd op met de bron uit of op nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag elektrische toestellen niet met natte handen bedienen.",
        antwoord=True,
        uitleg="Water geleidt, dus daalt de weerstand van je huid sterk. Bij dezelfde "
        "spanning loopt er dan een veel grotere stroom door je lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor lees je de handleiding van een toestel voor je het gebruikt?",
        opties=[
            "om het meetbereik, de aansluiting en de voorzorgen te kennen",
            "om te weten hoeveel het toestel gekost heeft",
            "om de garantietermijn van het toestel bij de verkoper na te gaan",
            "om de uitkomst van je meting al vooraf te kennen",
        ],
        antwoord=0,
        uitleg="Zo voorkom je een verkeerde aansluiting of een beschadigd toestel. Een "
        "werktekening lees je om dezelfde reden eerst helemaal door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instrumenten passen bij welke meting? Kruis alles aan wat juist is.",
        opties=[
            "een dynamometer voor een kracht",
            "een chronometer voor een tijdsduur",
            "een decibelmeter voor een geluidsniveau",
            "een multimeter voor een temperatuur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voor een temperatuur neem je een thermometer of een temperatuursensor. Een "
        "multimeter blijft bij spanning, stroom en weerstand.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het kleinste verschil dat een meetinstrument nog kan aanwijzen?",
        antwoord=["de nauwkeurigheid", "nauwkeurigheid", "de resolutie"],
        uitleg="Bij een lat met millimeters is dat één millimeter. Je antwoord mag nooit "
        "nauwkeuriger lijken dan je instrument is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je bij een snelle beweging liever een sensor dan een handchronometer?",
        opties=[
            "je eigen reactietijd geeft bij de hand een fout van wel een tiende seconde",
            "een sensor kan over een veel grotere afstand meten",
            "een handchronometer heeft een veel kleiner meetbereik",
            "een sensor hoeft na de meting niet meer uitgeschakeld te worden",
        ],
        antwoord=0,
        uitleg="Bij een val van een halve seconde is dat al een vijfde ernaast. Een "
        "lichtpoortje start en stopt zonder reactietijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met de batterijen van een stuk meetmateriaal dat je weggooit?",
        opties=[
            "ze horen bij het klein gevaarlijk afval en gaan apart",
            "ze mogen bij het gewone restafval",
            "ze mogen bij het papier en karton",
            "ze mogen bij het oud metaal in de gewone container",
        ],
        antwoord=0,
        uitleg="Ze bevatten zware metalen die in de bodem terechtkomen. Duurzaam werken "
        "houdt ook op bij het afval niet op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een toestel dat een onwaarschijnlijke waarde aanwijst, mag je zonder meer overnemen.",
        antwoord=False,
        uitleg="Controleer eerst het bereik, de aansluiting en de stand van het toestel. Een "
        "schatting vooraf helpt je zo'n fout meteen te zien.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van kracht?",
        opties=[
            "de newton",
            "de joule",
            "het pascal",
            "de watt",
        ],
        antwoord=0,
        uitleg="De joule hoort bij energie, het pascal bij druk en de watt bij vermogen. Elk "
        "van die drie is uit de newton opgebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eenheden zijn SI-eenheden? Kruis alles aan wat juist is.",
        opties=[
            "de meter voor een lengte",
            "de kilogram voor een massa",
            "de seconde voor een tijd",
            "de kilometer per uur voor een snelheid",
        ],
        antwoord=[0, 1, 2],
        uitleg="De SI-eenheid van snelheid is de meter per seconde. Kilometer per uur is "
        "handig maar niet de eenheid waarmee je rekent.",
    ),
    dict(
        type="invultekst",
        vraag="Met hoeveel moet je vermenigvuldigen om van kilometer per uur naar meter per seconde te gaan?",
        antwoord=["1/3,6", "0,278", "delen door 3,6"],
        uitleg="Je deelt dus door 3,6, want een uur heeft 3600 seconden en een kilometer "
        "1000 meter. 72 kilometer per uur is zo 20 meter per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 2,5 mA in ampère?",
        opties=[
            "0,0025 A",
            "0,025 A",
            "2500 A",
            "250 A",
        ],
        antwoord=0,
        uitleg="Milli betekent een duizendste. Je schuift de komma dus drie plaatsen naar "
        "links.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorvoegsel hoort bij een miljoenste?",
        opties=[
            "micro",
            "milli",
            "nano",
            "mega",
        ],
        antwoord=0,
        uitleg="Milli is een duizendste en nano een miljardste. Mega is juist een miljoen "
        "keer zoveel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 4,7 kΩ in ohm?",
        opties=[
            "4700 Ω",
            "470 Ω",
            "0,0047 Ω",
            "47 000 Ω",
        ],
        antwoord=0,
        uitleg="Kilo betekent duizend. Een weerstand van 4,7 kilo-ohm is dus 4700 ohm.",
    ),
    dict(
        type="waarofniet",
        vraag="Nano staat voor een miljardste van de eenheid.",
        antwoord=True,
        uitleg="Dat is tien tot de macht min negen. Micro is een miljoenste en milli een "
        "duizendste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel beduidende cijfers heeft de meting 0,0250 m?",
        opties=[
            "drie",
            "twee",
            "vier",
            "vijf",
        ],
        antwoord=0,
        uitleg="De nullen vooraan tellen niet mee, de nul achteraan wel. Die laatste nul "
        "zegt namelijk dat er tot op die plaats gemeten is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet 2,5 m en 1,25 m en telt die op. Met hoeveel cijfers na de komma schrijf je het antwoord?",
        opties=[
            "met één cijfer na de komma, dus 3,8 m",
            "met twee cijfers na de komma, dus 3,75 m",
            "met drie cijfers na de komma, dus 3,750 m",
            "zonder komma, dus 4 m",
        ],
        antwoord=0,
        uitleg="Bij een som bepaalt de slechtste meting hoeveel cijfers na de komma je mag "
        "houden. Je antwoord kan niet nauwkeuriger zijn dan je meting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je niet alle cijfers van je rekenmachine op?",
        opties=[
            "je antwoord zou dan nauwkeuriger lijken dan je meting is",
            "een rekenmachine rekent met te veel afrondingsfouten",
            "lange getallen zijn moeilijker te controleren",
            "het is enkel een afspraak zonder verdere reden",
        ],
        antwoord=0,
        uitleg="De beduidende cijfers laten zien hoe goed je gemeten hebt. Tien cijfers "
        "achter de komma bij een meting met een lat is dus onzin.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe schrijf je 0,00045 in wetenschappelijke notatie?",
        antwoord=["4,5 · 10⁻⁴", "4,5e-4", "4,5 maal 10^-4"],
        uitleg="Je zet één cijfer voor de komma en de rest in de macht van tien. Zo zie je "
        "ook meteen hoeveel beduidende cijfers er zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="In de wetenschappelijke notatie staan er altijd twee cijfers voor de komma.",
        antwoord=False,
        uitleg="Er staat net één cijfer anders dan nul voor de komma: 32 000 wordt 3,2 maal "
        "tien tot de vierde. Daardoor zijn heel grote en heel kleine getallen vergelijkbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor maak je vooraf een schatting van je uitkomst?",
        opties=[
            "om een onzinnig antwoord meteen te herkennen",
            "om de meting zelf niet meer te hoeven doen",
            "om het aantal beduidende cijfers te bepalen",
            "om de eenheid van het antwoord te vinden",
        ],
        antwoord=0,
        uitleg="Een mens die 300 meter per seconde loopt, klopt niet. Een factor duizend "
        "ernaast door een verkeerd voorvoegsel zie je zo direct.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het verwerken van meetgegevens? Kruis alles aan wat juist is.",
        opties=[
            "de gegevens in een tabel zetten",
            "een grafiek tekenen om het verband te zien",
            "het antwoord met de juiste eenheid noteren",
            "de metingen die niet passen zonder meer weglaten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een meting weglaten mag alleen met een reden die je opschrijft. Anders pas "
        "je je gegevens aan je verwachting aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet in een grafiek een rechte door de oorsprong. Welk verband is dat?",
        opties=[
            "een recht evenredig verband",
            "een omgekeerd evenredig verband",
            "een kwadratisch verband",
            "een lineair verband dat niet recht evenredig is",
        ],
        antwoord=0,
        uitleg="Verdubbel je het ene, dan verdubbelt het andere. Een rechte die de as "
        "ergens anders snijdt, is wel lineair maar niet recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grafiek hoort bij een omgekeerd evenredig verband?",
        opties=[
            "een kromme die daalt en de assen nadert",
            "een rechte met een negatieve richtingscoëfficiënt",
            "een parabool door de oorsprong",
            "een horizontale rechte",
        ],
        antwoord=0,
        uitleg="Het product van de twee grootheden blijft dan constant. Een p(V)-grafiek bij "
        "constante temperatuur is daarvan het voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verbanden kan je tussen twee grootheden tegenkomen? Kruis alles aan wat juist is.",
        opties=[
            "recht evenredig",
            "omgekeerd evenredig",
            "kwadratisch",
            "beduidend",
        ],
        antwoord=[0, 1, 2],
        uitleg="Beduidend hoort bij de cijfers van een meting, niet bij een verband. Lineair "
        "is er ook nog een.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je weet dat F gelijk is aan m maal a. Hoe druk je a uit in functie van de rest?",
        opties=[
            "a is F gedeeld door m",
            "a is m gedeeld door F",
            "a is F maal m",
            "a is F min m",
        ],
        antwoord=0,
        uitleg="Je deelt beide kanten door de massa. Zo vorm je elke formule om naar de "
        "grootheid die je zoekt.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag twee formules combineren door een grootheid die in beide staat te vervangen.",
        antwoord=True,
        uitleg="Zo kom je van twee verbanden tot één nieuw. Let er wel op dat je overal "
        "dezelfde eenheden gebruikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een antwoord zonder eenheid is in de fysica even goed als een antwoord met eenheid.",
        antwoord=False,
        uitleg="Zonder eenheid weet niemand of je 5 meter of 5 kilometer bedoelt. De eenheid "
        "hoort dus bij het antwoord.",
    ),
]
