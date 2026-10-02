# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Dosis en concentratie van stoffen.

Chemie, de kop "Dosis en concentratie van stoffen" uit de vakfiche
natuurwetenschappen 3DU. Deel 1 gaat over de concentratie-uitdrukkingen zelf:
massaprocent, volumeprocent, massaconcentratie en alcoholpercentage, met de
bijhorende rekenwerkjes. Deel 2 gaat over de dosis: het verschil met de
concentratie, de aanvaardbare dagelijkse inname en de LD50.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de dosis en de concentratie van een stof?",
        opties=[
            "de dosis is hoeveel je binnenkrijgt, de concentratie hoe sterk het is",
            "de dosis is hoe sterk het is, de concentratie hoeveel je binnenkrijgt",
            "de dosis geldt voor vaste stoffen, de concentratie voor vloeistoffen",
            "de dosis staat op het etiket, de concentratie moet je altijd meten",
        ],
        antwoord=0,
        uitleg="De concentratie is een eigenschap van het product: hoeveel stof er in het mengsel zit. De dosis is wat er in jouw lichaam terechtkomt, en die hangt ook af van hoeveel je ervan neemt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de concentratie-uitdrukking die zegt hoeveel gram stof er in 100 gram mengsel zit?",
        antwoord=["massaprocent", "het massaprocent", "massapercentage"],
        uitleg="Massaprocent vergelijkt massa met massa. Vijf massaprocent betekent vijf gram stof in elke honderd gram mengsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een fles wijn staat 12 % vol. Wat betekent dat?",
        opties=[
            "12 mL alcohol in elke 100 mL wijn",
            "12 g alcohol in elke 100 g wijn",
            "12 mL alcohol in de hele fles",
            "12 g alcohol per glas van 100 mL",
        ],
        antwoord=0,
        uitleg="Vol staat voor volumeprocent, en dat vergelijkt volume met volume. In elke honderd milliliter wijn zit dus twaalf milliliter alcohol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een flesje bier bevat 250 mL en 5 % vol alcohol. Hoeveel alcohol zit erin?",
        opties=[
            "12,5 mL",
            "5 mL",
            "25 mL",
            "50 mL",
        ],
        antwoord=0,
        uitleg="Je rekent 5 procent van 250 milliliter, dus 250 maal 0,05. Dat geeft 12,5 milliliter alcohol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fles wijn van 750 mL bevat 12 % vol alcohol. Hoeveel alcohol zit er in de hele fles?",
        opties=[
            "90 mL",
            "12 mL",
            "75 mL",
            "120 mL",
        ],
        antwoord=0,
        uitleg="Je rekent 750 maal 0,12. Dat geeft negentig milliliter, dus zeven keer zoveel als in het flesje bier van hiervoor.",
    ),
    dict(
        type="waarofniet",
        vraag="Volumeprocent wordt vooral gebruikt als je twee vloeistoffen mengt.",
        antwoord=True,
        uitleg="Bij vloeistoffen is het volume het makkelijkst te meten. Daarom staat op drank een volumeprocent en niet een massaprocent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost 15 g zout op in water en krijgt 300 g pekel. Wat is het massaprocent zout?",
        opties=[
            "5 %",
            "15 %",
            "20 %",
            "45 %",
        ],
        antwoord=0,
        uitleg="Je deelt 15 door 300 en maakt er procent van: 0,05 maal 100 is vijf procent. Let op dat je deelt door de massa van de hele oplossing, niet door die van het water alleen.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je een massaconcentratie meestal uit?",
        antwoord=["g/L", "gram per liter", "g per L", "g/l"],
        uitleg="Massaconcentratie vergelijkt een massa met een volume, dus gram per liter. Bij heel kleine hoeveelheden gebruik je milligram per liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lost 20 g suiker op in water tot 500 mL drank. Wat is de massaconcentratie?",
        opties=[
            "40 g/L",
            "20 g/L",
            "10 g/L",
            "100 g/L",
        ],
        antwoord=0,
        uitleg="Vijfhonderd milliliter is een halve liter, dus in een volle liter zou er dubbel zoveel zitten. Twintig gedeeld door 0,5 is veertig gram per liter.",
    ),
    dict(
        type="waarofniet",
        vraag="De concentratie van een product zegt op zich nog niet hoeveel je ervan binnenkrijgt.",
        antwoord=True,
        uitleg="Daarvoor moet je ook weten hoeveel je ervan neemt. Een klein glas van een sterke drank kan evenveel alcohol bevatten als een groot glas van een zwakke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze uitdrukkingen zijn concentratie-uitdrukkingen? Er zijn er drie.",
        opties=[
            "massaprocent",
            "volumeprocent",
            "massaconcentratie",
            "lichaamsgewicht",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie vergelijken de hoeveelheid stof met de hoeveelheid mengsel. Het lichaamsgewicht hoort bij de dosis, niet bij de concentratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Geconcentreerde ontstopper is bijtend, verdunde ontstopper enkel irriterend. Wat leer je daaruit?",
        opties=[
            "het gevaar van een stof hangt af van de concentratie",
            "het gevaar van een stof hangt enkel af van de soort stof",
            "verdunnen maakt elke stof volledig onschadelijk",
            "een bijtende stof is na verdunnen niet meer dezelfde stof",
        ],
        antwoord=0,
        uitleg="Het is dezelfde stof, maar hoe sterker ze is, hoe meer schade ze doet. Daarom staat er bij een sterker product ook een zwaarder pictogram op.",
    ),
    dict(
        type="waarofniet",
        vraag="Dezelfde stof kan een ander gevarenpictogram krijgen als de concentratie verandert.",
        antwoord=True,
        uitleg="Een sterk product is bijtend, een verdund product irriterend. Daarom verschilt het pictogram op een professionele fles van dat op een huishoudelijke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een drankje bevat 2 g vitamine C per 250 mL. Wat is de massaconcentratie?",
        opties=[
            "8 g/L",
            "2 g/L",
            "4 g/L",
            "0,5 g/L",
        ],
        antwoord=0,
        uitleg="Tweehonderdvijftig milliliter is een kwart liter, dus in een volle liter zit vier keer zoveel. Twee maal vier is acht gram per liter.",
    ),
    dict(
        type="waarofniet",
        vraag="Vijf massaprocent betekent vijf gram stof per liter mengsel.",
        antwoord=False,
        uitleg="Massaprocent rekent per honderd gram, niet per liter. Vijf gram per liter is een massaconcentratie, en dat is een andere uitdrukking.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het getal op een fles drank dat zegt welk deel van het volume alcohol is?",
        antwoord=["alcoholpercentage", "het alcoholpercentage", "volumeprocent"],
        uitleg="Het alcoholpercentage is een volumeprocent. Het staat op elke fles, meestal met de afkorting vol erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee glazen bevatten dezelfde drank. Het ene is 100 mL, het andere 200 mL. Wat is juist?",
        opties=[
            "in het grote glas zit twee keer zoveel alcohol",
            "in beide glazen zit evenveel alcohol",
            "in het kleine glas is de concentratie dubbel zo hoog",
            "in het grote glas is de concentratie dubbel zo hoog",
        ],
        antwoord=0,
        uitleg="De concentratie is in beide glazen dezelfde, want het is dezelfde drank. Het volume verdubbelt, dus de hoeveelheid alcohol ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat moet je kennen om te berekenen hoeveel alcohol er in een glas zit? Er zijn er twee.",
        opties=[
            "het volume van het glas",
            "het alcoholpercentage van de drank",
            "de temperatuur van de drank",
            "de prijs van de fles",
        ],
        antwoord=[0, 1],
        uitleg="Je vermenigvuldigt het volume met het percentage. Temperatuur en prijs veranderen niets aan de hoeveelheid alcohol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fles van 1 L bevat een oplossing van 30 g/L zout. Hoeveel zout zit er in 200 mL?",
        opties=[
            "6 g",
            "30 g",
            "15 g",
            "3 g",
        ],
        antwoord=0,
        uitleg="Tweehonderd milliliter is een vijfde van een liter, dus je deelt dertig door vijf. Dat geeft zes gram zout.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe hoger de concentratie van een oplossing, hoe minder stof er in elke liter zit.",
        antwoord=False,
        uitleg="Het is net omgekeerd: een hogere concentratie betekent meer stof in dezelfde hoeveelheid mengsel. Verdunnen verlaagt de concentratie.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag="Hoe noem je de hoeveelheid van een stof die je elke dag zonder gevaar binnen mag krijgen?",
        antwoord=["ADI", "aanvaardbare dagelijkse inname", "ADH"],
        uitleg="ADI staat voor acceptable daily intake, de aanvaardbare dagelijkse inname. Ze wordt uitgedrukt per kilogram lichaamsgewicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de ADI uitgedrukt per kilogram lichaamsgewicht?",
        opties=[
            "een zwaarder lichaam verdraagt meer van een stof",
            "een zwaarder lichaam verdraagt juist minder van een stof",
            "het lichaamsgewicht bepaalt de concentratie van de stof",
            "zo hoeft er geen aparte waarde per stof berekend te worden",
        ],
        antwoord=0,
        uitleg="Een stof verdeelt zich over je hele lichaam, dus in een groter lichaam wordt dezelfde hoeveelheid meer verdund. Daarom mag een volwassene meer dan een kind.",
    ),
    dict(
        type="meerkeuze",
        vraag="De ADI van een zoetstof is 7 mg per kg lichaamsgewicht per dag. Hoeveel mag een kind van 30 kg?",
        opties=[
            "210 mg per dag",
            "7 mg per dag",
            "30 mg per dag",
            "37 mg per dag",
        ],
        antwoord=0,
        uitleg="Je rekent 7 maal 30, want elke kilogram mag zeven milligram. Dat geeft 210 milligram per dag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de LD50 van een stof?",
        opties=[
            "de dosis waarbij de helft van de proefdieren sterft",
            "de dosis waarbij de helft van de stof afgebroken is",
            "de helft van de aanvaardbare dagelijkse inname",
            "de dosis waarbij de helft van de stof opgelost is",
        ],
        antwoord=0,
        uitleg="LD staat voor lethale dosis, en 50 voor de helft. Het is een maat om de giftigheid van stoffen met elkaar te vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="De LD50 van een stof is 2000 mg per kg. Welke dosis is dat voor een mens van 60 kg?",
        opties=[
            "120 g",
            "2 g",
            "12 g",
            "33 g",
        ],
        antwoord=0,
        uitleg="Je rekent 2000 maal 60, dat is 120 000 milligram. Milligram omzetten naar gram doe je door duizend keer te delen, dus 120 gram.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een lage LD50 is giftiger dan een stof met een hoge LD50.",
        antwoord=True,
        uitleg="Bij een lage LD50 is er maar een kleine hoeveelheid nodig voor hetzelfde effect. Hoe lager het getal, hoe giftiger de stof dus is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Stof A heeft een LD50 van 50 mg per kg, stof B van 5000 mg per kg. Wat volgt daaruit?",
        opties=[
            "stof A is honderd keer giftiger dan stof B",
            "stof B is honderd keer giftiger dan stof A",
            "beide stoffen zijn even giftig per kilogram",
            "stof B werkt honderd keer sneller dan stof A",
        ],
        antwoord=0,
        uitleg="Van stof A is honderd keer minder nodig voor hetzelfde effect. De LD50 zegt niets over hoe snel een stof werkt.",
    ),
    dict(
        type="waarofniet",
        vraag="De ADI geldt per dag en per kilogram lichaamsgewicht.",
        antwoord=True,
        uitleg="Daarom moet je altijd met je eigen gewicht rekenen. Dezelfde ADI geeft voor een kind van 20 kilogram een veel kleinere hoeveelheid dan voor een volwassene.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt het af of een stof jou schade doet? Er zijn er twee.",
        opties=[
            "hoeveel je ervan binnenkrijgt",
            "hoeveel je zelf weegt",
            "hoe duur de stof was",
            "in welke kleur de verpakking is",
        ],
        antwoord=[0, 1],
        uitleg="De dosis en je lichaamsgewicht bepalen samen hoeveel er per kilogram in je lichaam komt. Prijs en verpakking veranderen daar niets aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een drank bevat 40 g suiker per liter. Hoeveel suiker krijg je binnen met een glas van 200 mL?",
        opties=[
            "8 g",
            "40 g",
            "20 g",
            "4 g",
        ],
        antwoord=0,
        uitleg="Je neemt een vijfde van een liter, dus een vijfde van veertig gram. Dat is acht gram: de concentratie maal het volume geeft de dosis.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan de dosis die je binnenkrijgt gewoon van het etiket aflezen, zonder te rekenen.",
        antwoord=False,
        uitleg="Op het etiket staat de concentratie, meestal per honderd gram of per liter. Hoeveel je werkelijk binnenkrijgt, moet je er zelf bij rekenen met de hoeveelheid die je neemt.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de afkorting LD in LD50 voor?",
        antwoord=["lethale dosis", "letale dosis", "dodelijke dosis"],
        uitleg="De lethale dosis is de dodelijke dosis. Het getal 50 zegt dat de helft van de proefdieren bij die dosis stierf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een hoge LD50 kan je zonder zorgen in elke hoeveelheid gebruiken.",
        antwoord=False,
        uitleg="Een hoge LD50 betekent alleen dat er veel van nodig is voor een dodelijke dosis. Ook keukenzout en water worden schadelijk als je er genoeg van binnenkrijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zegt men dat elke stof giftig kan zijn?",
        opties=[
            "boven een bepaalde dosis doet elke stof schade",
            "elke stof bevat een kleine hoeveelheid gif",
            "elke stof heeft hetzelfde gevarenpictogram",
            "elke stof wordt in het lichaam omgezet tot gif",
        ],
        antwoord=0,
        uitleg="Het is de dosis die het gif maakt. Zelfs water verstoort je lichaam als je er in korte tijd te veel van drinkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat op een geneesmiddel voor kinderen een andere dosering dan voor volwassenen?",
        opties=[
            "kinderen wegen minder, dus ze verdragen minder",
            "kinderen breken geneesmiddelen veel sneller af",
            "kinderen hebben een andere concentratie nodig",
            "kinderen slikken het middel minder goed door",
        ],
        antwoord=0,
        uitleg="De veilige dosis wordt per kilogram lichaamsgewicht bepaald. Een kind van twintig kilogram mag dus veel minder dan een volwassene van tachtig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vitamine is nodig, maar in te grote hoeveelheid schadelijk. Wat leert dat je?",
        opties=[
            "ook een nuttige stof heeft een veilige bovengrens",
            "een nuttige stof heeft nooit een bovengrens",
            "een vitamine is eigenlijk geen voedingsstof",
            "je hebt van elke vitamine evenveel nodig",
        ],
        antwoord=0,
        uitleg="Vooral de vitaminen A, D, E en K worden in je vet opgeslagen en hopen zich dus op. Daarom staat er op een vitaminepotje een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee mensen die dezelfde hoeveelheid van een stof binnenkrijgen, krijgen altijd precies dezelfde dosis per kilogram.",
        antwoord=False,
        uitleg="Dat geldt alleen als ze even veel wegen. Bij een lichter lichaam is dezelfde hoeveelheid een grotere dosis per kilogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ADI geldt voor dagelijks gebruik, een LD50 voor één keer. Waarom is dat verschil belangrijk?",
        opties=[
            "een kleine hoeveelheid kan op lange termijn ophopen",
            "een kleine hoeveelheid verdwijnt altijd volledig",
            "een grote hoeveelheid is op lange termijn veiliger",
            "een stof werkt alleen de eerste keer dat je ze neemt",
        ],
        antwoord=0,
        uitleg="De LD50 gaat over een eenmalige, zware dosis; de ADI over elke dag opnieuw een beetje. Sommige stoffen blijven in je lichaam zitten, en dan telt het op.",
    ),
    dict(
        type="meerkeuze",
        vraag="De ADI van een kleurstof is 4 mg per kg per dag. Een volwassene weegt 70 kg. Hoeveel mag die per dag?",
        opties=[
            "280 mg",
            "4 mg",
            "70 mg",
            "74 mg",
        ],
        antwoord=0,
        uitleg="Je rekent 4 maal 70. Dat geeft 280 milligram per dag voor die persoon.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee stoffen met dezelfde concentratie kunnen een heel verschillend gevaar inhouden.",
        antwoord=True,
        uitleg="De concentratie zegt alleen hoeveel stof er in het mengsel zit, niet hoe giftig die stof is. Daarom kijk je ook naar de LD50 en de pictogrammen.",
    ),
]
