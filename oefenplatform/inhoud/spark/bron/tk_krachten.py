# -*- coding: utf-8 -*-
"""De vragen voor "Krachten en stevigheid in een constructie" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technische systemen —
constructiesysteem", de stukken "Krachten op een constructie" en "Stabiliteit,
sterkte en stijfheid".

Deel 1 gaat over de vier krachten van de fiche (druk, trek, torsie en buiging),
waar je ze tegenkomt, en hoe je daarmee rekening houdt bij het kiezen van een
materiaal.
Deel 2 gaat over stabiliteit, sterkte en stijfheid, over driehoeken tegenover
rechthoeken, over zuilen en bogen, en over gewapend beton.

Stabiliteit, sterkte en stijfheid worden voortdurend door elkaar gehaald; ze
krijgen hier elk hun eigen vraag met dezelfde woorden als de fiche. Stabiliteit
gaat over omvallen, sterkte over breken, stijfheid over vervormen.

De constructies zelf staan getekend in de leerbundel. In de vragen staat geen
afbeelding, dus elke situatie wordt in woorden beschreven.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke kracht werkt er op de ophangkabels van een brug?",
        opties=[
            "Een trekkracht",
            "Een drukkracht",
            "Een torsiekracht",
            "Een buigkracht",
        ],
        antwoord=0,
        uitleg="De kabels worden naar beneden getrokken door het gewicht van de brug. Dat voorbeeld staat letterlijk in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht werkt er op de pilaren van een brug?",
        opties=[
            "Een drukkracht",
            "Een trekkracht",
            "Een torsiekracht",
            "Een buigkracht",
        ],
        antwoord=0,
        uitleg="Een pilaar draagt het gewicht dat erboven ligt en wordt dus samengeduwd. Dat is een drukkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een torsiekracht?",
        opties=[
            "Een kracht die iets verdraait",
            "Een kracht die iets uit elkaar rekt",
            "Een kracht die iets samendrukt",
            "Een kracht die iets doet doorbuigen",
        ],
        antwoord=0,
        uitleg="Torsie is wringen of verdraaien. Denk aan een natte handdoek die je uitwringt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een buigkracht?",
        opties=[
            "Een kracht die iets doet doorbuigen",
            "Een kracht die iets verdraait om zijn as",
            "Een kracht die iets uit elkaar trekt",
            "Een kracht die iets recht samenperst",
        ],
        antwoord=0,
        uitleg="Bij buiging wordt de bovenkant samengeduwd en de onderkant uitgerekt. Een plank die doorzakt onder gewicht is het voorbeeld bij uitstek.",
    ),
    dict(
        type="waarofniet",
        vraag="Boeken op een tafel oefenen een drukkracht uit op het tafelblad.",
        antwoord=True,
        uitleg="Ze duwen recht naar beneden. Ook dat voorbeeld staat in de fiche, naast de pilaren van een brug.",
    ),
    dict(
        type="waarofniet",
        vraag="Een touw waaraan je trekt, staat onder drukkracht.",
        antwoord=False,
        uitleg="Dat is een trekkracht. Een touw kan trouwens helemaal geen drukkracht opnemen: duw je ertegen, dan plooit het gewoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten op een constructie noemt de fiche?",
        opties=[
            "Drukkracht",
            "Trekkracht",
            "Torsiekracht",
            "Buigkracht",
            "Lichtkracht",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Druk, trek, torsie en buiging. Een lichtkracht bestaat niet.",
    ),
    dict(
        type="invultekst",
        vraag="De kracht die op een voorwerp werkt als je het uit elkaar trekt, heet een ___.",
        antwoord="trekkracht",
        uitleg="Kabels, touwen en kettingen zijn gemaakt om trekkracht op te nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je draait met een schroevendraaier een schroef vast. Welke kracht is hier de voornaamste?",
        opties=[
            "Een torsiekracht",
            "Een trekkracht",
            "Een buigkracht",
            "Een drukkracht",
        ],
        antwoord=0,
        uitleg="Je verdraait de steel rond zijn as, en dat is torsie. Je duwt ook wat, maar het draaien is wat de schroef doet bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plank ligt op twee steunen en je zet er iets zwaars op in het midden. Welke kracht werkt er op die plank?",
        opties=[
            "Een buigkracht",
            "Een torsiekracht",
            "Een trekkracht over de hele lengte",
            "Alleen een drukkracht naar boven toe",
        ],
        antwoord=0,
        uitleg="De plank zakt door in het midden, dus buigt ze. Daarom leggen bouwers er een derde steun onder als het te ver doorzakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Beton kan veel drukkracht verdragen maar weinig trekkracht.",
        antwoord=True,
        uitleg="Daarom zit er staal in gewapend beton: het staal neemt de trekkracht op die het beton niet aankan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk materiaal kies je voor een kabel die veel trekkracht moet verdragen?",
        opties=["Staal", "Glas", "Beton", "Karton"],
        antwoord=0,
        uitleg="Staal heeft een hoge treksterkte. Glas en beton zijn broos en breken bij trek, karton scheurt gewoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke materialen zijn geschikt voor een zuil die veel gewicht moet dragen?",
        opties=["Beton", "Staal", "Steen", "Rubber", "Papier"],
        antwoord=[0, 1, 2],
        uitleg="Een zuil moet vooral drukkracht aankunnen. Beton, staal en steen kunnen dat. Rubber vervormt en papier plooit dubbel.",
    ),
    dict(
        type="waarofniet",
        vraag="Glas is een goede keuze voor een onderdeel dat veel trekkracht moet opvangen.",
        antwoord=False,
        uitleg="Glas is broos: het breekt bij trek zonder eerst te vervormen. Voor trek kies je een taai materiaal zoals staal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar moet je op letten bij het kiezen van een materiaal voor een constructie?",
        opties=[
            "De trekkracht die het moet opvangen",
            "De drukkracht die het moet opvangen",
            "Hoe zwaar het materiaal zelf is",
            "Welke kleur het materiaal heeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="De krachten en het eigen gewicht bepalen of een constructie het houdt. De kleur is een kwestie van afwerking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een fietsframe gemaakt van buizen en niet van massieve staven?",
        opties=[
            "Buizen zijn licht en toch sterk genoeg",
            "Buizen zijn altijd goedkoper dan staven",
            "Buizen kunnen helemaal niet gaan roesten",
            "Buizen zijn veel makkelijker te schilderen",
        ],
        antwoord=0,
        uitleg="Bij buiging telt vooral het materiaal aan de buitenkant. Het midden weghalen scheelt veel gewicht en bijna geen sterkte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kraanarm die een last optilt, krijgt te maken met een buigkracht.",
        antwoord=True,
        uitleg="De last hangt aan het uiteinde en trekt de arm naar beneden, dus de arm buigt. Daarom is een kraanarm opgebouwd uit driehoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schommel hangt aan twee kettingen. Welke kracht werkt er op die kettingen?",
        opties=[
            "Een trekkracht",
            "Een drukkracht",
            "Een torsiekracht",
            "Helemaal geen kracht",
        ],
        antwoord=0,
        uitleg="Het gewicht van wie schommelt, trekt aan de kettingen. Een ketting kan alleen trek opnemen, geen druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Torsie betekent samendrukken.",
        antwoord=False,
        uitleg="Torsie is verdraaien. Samendrukken is een drukkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een materiaal dat meer trekkracht krijgt dan het aankan?",
        opties=[
            "Het scheurt of het breekt",
            "Het wordt dikker en zwaarder",
            "Het wordt magnetisch van binnen",
            "Het geleidt de stroom veel beter",
        ],
        antwoord=0,
        uitleg="Een taai materiaal rekt eerst nog uit, een broos materiaal breekt meteen. De grens waar dat gebeurt, is de treksterkte.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vorm houdt in een constructie het best zijn vorm?",
        opties=["De driehoek", "De rechthoek", "Het vierkant", "De ruit"],
        antwoord=0,
        uitleg="Een driehoek kan niet scheeftrekken zolang de zijden even lang blijven. Bij een rechthoek of een ruit kan dat wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zetten bouwers schuine balken in een rechthoekig frame?",
        opties=[
            "Zo ontstaan er driehoeken en vervormt het frame niet",
            "Zo wordt het frame een stuk lichter om te dragen",
            "Zo is er veel minder verf nodig voor het frame",
            "Zo past het frame nog door de deur van het lokaal",
        ],
        antwoord=0,
        uitleg="Die schuine balk heet een schoor. Hij snijdt de rechthoek in twee driehoeken, en daardoor kan het geheel niet meer scheeftrekken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechthoek van vier losse balken kan makkelijk scheeftrekken.",
        antwoord=True,
        uitleg="Duw je tegen een hoek, dan wordt de rechthoek een schuine vorm. Precies daarom zet je er een schuine balk in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is gewapend beton?",
        opties=[
            "Beton met staven staal erin",
            "Beton dat twee keer gegoten is",
            "Beton met een laag verf erover",
            "Beton dat in de zon gedroogd is",
        ],
        antwoord=0,
        uitleg="In de bekisting leggen bouwers eerst stalen staven, en daarrond gieten ze het beton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zit er staal in gewapend beton?",
        opties=[
            "Staal vangt de trekkracht op die beton niet aankan",
            "Staal maakt het beton een heel stuk lichter",
            "Staal zorgt dat het beton veel sneller droogt",
            "Staal geeft het beton zijn grijze kleur mee",
        ],
        antwoord=0,
        uitleg="Beton is sterk bij druk en zwak bij trek, staal net omgekeerd. Samen kunnen ze allebei.",
    ),
    dict(
        type="waarofniet",
        vraag="Gewapend beton kan meer trekkracht verdragen dan gewoon beton.",
        antwoord=True,
        uitleg="Het staal in het beton neemt die trek op. Zonder wapening zou een betonnen vloer bij de minste doorbuiging scheuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de stabiliteit van een constructie?",
        opties=[
            "Ze blijft staan en valt niet om",
            "Ze breekt niet als je er hard op duwt",
            "Ze buigt niet door onder een gewicht",
            "Ze weegt zo weinig mogelijk",
        ],
        antwoord=0,
        uitleg="Stabiliteit gaat over omvallen. Een constructie kan heel sterk zijn en toch omkieperen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de sterkte van een constructie?",
        opties=[
            "Ze kan veel kracht verdragen zonder te breken",
            "Ze valt niet om als je ertegen duwt",
            "Ze blijft recht zonder ergens door te buigen",
            "Ze is gemaakt van de duurste materialen",
        ],
        antwoord=0,
        uitleg="Sterkte gaat over breken. Hoeveel kan de constructie hebben voor er iets bezwijkt?",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de stijfheid van een constructie?",
        opties=[
            "Ze vervormt bijna niet onder belasting",
            "Ze kan veel gewicht dragen voor ze breekt",
            "Ze staat stevig en kiept niet om",
            "Ze gaat makkelijk uit elkaar te halen",
        ],
        antwoord=0,
        uitleg="Stijfheid gaat over vervormen. Een plank kan sterk zijn en toch flink doorbuigen: dan is ze sterk maar niet stijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Een constructie kan sterk zijn en toch omvallen.",
        antwoord=True,
        uitleg="Sterkte en stabiliteit zijn twee verschillende dingen. Een hoge smalle toren kan onbreekbaar zijn en toch omkieperen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt een constructie stabieler?",
        opties=[
            "Een brede voet",
            "Een laag zwaartepunt",
            "Schuine balken tussen de hoeken",
            "Een hoog en heel smal bovenstuk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Breed onderaan en zwaar onderaan houdt iets recht. Een hoog en smal bovenstuk doet net het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="De vorm die in een constructie niet vervormt en daarom in bruggen en daken zit, is de ___.",
        antwoord="driehoek",
        uitleg="Met drie vaste zijden ligt de vorm helemaal vast. Daarom is elk dakgebint en elke kraanarm uit driehoeken opgebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een boog in een constructie kloppen?",
        opties=[
            "Ze leidt het gewicht naar de zijkanten weg",
            "Ze zit in oude bruggen en in poorten",
            "Ze kan een grote opening overspannen",
            "Ze houdt de regen volledig tegen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een boog verandert het gewicht van bovenaf in drukkracht die schuin naar de steunpunten loopt. Steen kan die druk aan, en zo kan een boog ver overspannen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuil vangt vooral een trekkracht op.",
        antwoord=False,
        uitleg="Een zuil staat recht en draagt wat erboven ligt, dus wordt ze samengeduwd. Dat is een drukkracht. Trekkracht zit in kabels en kettingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een golfplaat steviger dan een vlakke plaat van dezelfde dikte?",
        opties=[
            "De plooien maken de plaat stijver",
            "Het materiaal is dikker op de plooien",
            "De plaat weegt een heel stuk minder",
            "De plooien houden het regenwater tegen",
        ],
        antwoord=0,
        uitleg="Door de plooien staat er overal materiaal boven en onder het midden, en juist dat maakt een plaat stijf tegen buigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoog zwaartepunt maakt een constructie stabieler.",
        antwoord=False,
        uitleg="Net omgekeerd. Hoe lager het zwaartepunt, hoe minder makkelijk iets omvalt. Daarom staat de motor van een bus onderaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boekenrek wiebelt heen en weer. Wat helpt het best?",
        opties=[
            "Een schuine lat achteraan tussen twee hoeken",
            "Het rek een flink stuk hoger maken",
            "Meer boeken op de bovenste plank zetten",
            "Het rek in een andere kleur schilderen",
        ],
        antwoord=0,
        uitleg="Die lat maakt van de rechthoek twee driehoeken, en dan kan het rek niet meer scheeftrekken. Hoger maken of bovenaan verzwaren maakt het juist erger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een driehoek in een constructie kloppen?",
        opties=[
            "Hij vervormt niet als de verbindingen vastzitten",
            "Hij komt voor in de gebinten van een dak",
            "Hij komt voor in de armen van een kraan",
            "Hij is altijd zwaarder dan een rechthoek",
        ],
        antwoord=[0, 1, 2],
        uitleg="Over het gewicht zegt de vorm niets: dat hangt af van het materiaal en de afmetingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Stijfheid en sterkte betekenen precies hetzelfde.",
        antwoord=False,
        uitleg="Stijfheid gaat over vervormen, sterkte over breken. Een duikplank is sterk maar met opzet niet stijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hebben hoge gebouwen een brede en zware voet?",
        opties=[
            "Zo ligt het zwaartepunt laag en staan ze stabiel",
            "Zo is er veel minder beton nodig in de muren",
            "Zo kan de lift een pak sneller naar boven",
            "Zo vangt het gebouw meer zonlicht op het dak",
        ],
        antwoord=0,
        uitleg="Een brede voet en gewicht onderaan houden een hoog gebouw recht, ook als de wind ertegen duwt.",
    ),
]
