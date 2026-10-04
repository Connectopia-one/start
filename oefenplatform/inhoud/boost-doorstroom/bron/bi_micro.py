# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Biodiversiteit en micro-organismen.

Hoort bij de kop "biodiversiteit en micro-organismen" van de vakfiche
biologie 2de graad doorstroomfinaliteit, die 10 % van het examen weegt.

Deel 1 gaat over biodiversiteit: soorten, indeling, het belang van variatie
en de bedreigingen. Deel 2 gaat over de micro-organismen zelf: bacteriën,
virussen, schimmels, eencellige organismen, hun nut en hun gevaar, en de
afweer van ons lichaam.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent biodiversiteit?",
        opties=[
            "de verscheidenheid aan leven, van genen over soorten tot ecosystemen",
            "het aantal diersoorten dat binnen de grenzen van een land leeft",
            "de hoeveelheid planten die in een land jaarlijks geoogst wordt",
            "het aantal soorten dat in de dierentuinen van een land te zien is",
        ],
        antwoord=0,
        uitleg="Biodiversiteit telt niet enkel soorten. Ook de variatie binnen een soort en de verscheidenheid aan ecosystemen horen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke drie niveaus kan je biodiversiteit bekijken? Kruis alles aan wat juist is.",
        opties=[
            "de variatie binnen een soort",
            "het aantal verschillende soorten",
            "de verscheidenheid aan ecosystemen",
            "het aantal dierentuinen in een land",
        ],
        antwoord=[0, 1, 2],
        uitleg="Genen, soorten en ecosystemen: dat zijn de drie niveaus. Dierentuinen bewaren wel soorten, maar zijn zelf geen niveau van biodiversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer horen twee organismen tot dezelfde soort?",
        opties=[
            "als ze zich onderling kunnen voortplanten en vruchtbare nakomelingen krijgen",
            "als ze er van buiten precies hetzelfde uitzien",
            "als ze in hetzelfde gebied naast elkaar leven",
            "als ze van hetzelfde voedsel leven",
        ],
        antwoord=0,
        uitleg="Het criterium is de voortplanting. Een paard en een ezel krijgen wel een muil, maar die is onvruchtbaar, dus zijn het twee soorten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het indelen van organismen in groepen volgens hun verwantschap?",
        antwoord=["classificatie", "de classificatie", "systematiek"],
        uitleg="Bij de classificatie gaan organismen van soort over geslacht en familie tot rijk. Hoe hoger de groep, hoe verder de verwantschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een determinatietabel geeft je de naam van een soort zonder dat je naar haar kenmerken moet kijken.",
        antwoord=False,
        uitleg="Zo'n tabel stelt juist telkens een keuze tussen twee kenmerken. Je moet dus goed kijken en de juiste tak volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is variatie binnen een soort belangrijk?",
        opties=[
            "bij een ziekte of een verandering overleven er altijd nog individuen",
            "een soort met variatie heeft meer nakomelingen per worp",
            "variatie laat twee soorten in elkaar overgaan",
            "variatie maakt alle individuen even sterk",
        ],
        antwoord=0,
        uitleg="Zijn alle individuen gelijk, dan treft één ziekte ze allemaal. Door variatie is er altijd een deel dat er beter tegen kan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een akker met één gewas heeft een lagere biodiversiteit dan een hooiland met tientallen plantensoorten.",
        antwoord=True,
        uitleg="Op de akker staat één soort, op het hooiland tientallen, met de insecten die daarbij horen. Daarom is zo'n hooiland veel rijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke menselijke oorzaken bedreigen de biodiversiteit? Kruis alles aan wat juist is.",
        opties=[
            "het verdwijnen en versnipperen van leefgebieden",
            "vervuiling van bodem, water en lucht",
            "het binnenbrengen van soorten die er niet thuishoren",
            "het aanleggen van natuurgebieden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Leefgebied, vervuiling en invasieve soorten zijn de grote bedreigingen. Natuurgebieden werken net de andere richting uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een soort die van elders komt en hier het inheemse leven verdringt?",
        antwoord=["invasieve soort", "een invasieve soort", "exoot"],
        uitleg="Een invasieve exoot heeft hier geen natuurlijke vijanden en kan zich daardoor ongeremd uitbreiden, ten koste van wat er al was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het versnipperen van een leefgebied schadelijk, ook als de totale oppervlakte gelijk blijft?",
        opties=[
            "kleine groepen raken van elkaar gescheiden, waardoor de variatie in hun erfelijk materiaal afneemt",
            "kleine stukken natuur krijgen per vierkante meter minder zonlicht te verwerken",
            "versnipperde stukken hebben per soort minder vruchtbare bodem beschikbaar",
            "soorten in kleine stukken krijgen meer nakomelingen dan de bodem kan dragen",
        ],
        antwoord=0,
        uitleg="Een wegversperring of een snelweg snijdt groepen van elkaar af. Die kleine groepen verliezen variatie en zijn daardoor kwetsbaarder.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ecoduct of natuurbrug is bedoeld om versnipperde gebieden weer met elkaar te verbinden.",
        antwoord=True,
        uitleg="Zo kunnen dieren toch van het ene gebied naar het andere, en blijft er uitwisseling tussen de groepen bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ecosysteemdienst?",
        opties=[
            "een nut dat de natuur de mens levert, zoals bestuiving of waterzuivering",
            "een dienst van de overheid die de natuurgebieden van een land beheert",
            "een bedrijf dat inheemse planten verkoopt voor een tuin of een berm",
            "een vereniging van vrijwilligers die elk jaar de vogels van een streek telt",
        ],
        antwoord=0,
        uitleg="Bijen die fruitbomen bestuiven, een bos dat water vasthoudt, bodemleven dat afval opruimt: dat zijn ecosysteemdiensten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijken onderscheidt de klassieke indeling van het leven? Kruis alles aan wat juist is.",
        opties=[
            "de bacteriën",
            "de schimmels",
            "de planten en de dieren",
            "de mineralen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bacteriën, schimmels, planten, dieren en eencellige organismen zijn levende rijken. Mineralen leven niet en horen er dus niet bij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de rij van kenmerken die men aflegt om een onbekende plant een naam te geven?",
        antwoord=["determineren", "determinatie", "het determineren"],
        uitleg="Determineren is de soort opzoeken aan de hand van haar kenmerken. Een determinatietabel of een sleutel leidt je daar stap voor stap naartoe.",
    ),
    dict(
        type="waarofniet",
        vraag="Een wetenschappelijke naam bestaat uit één woord en verschilt van land tot land.",
        antwoord=False,
        uitleg="Ze bestaat uit twee delen, een geslachtsnaam en een soortnaam, en is overal ter wereld dezelfde. Net daarom is ze eenduidig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruiken biologen wetenschappelijke namen in plaats van volkse namen?",
        opties=[
            "een volkse naam verschilt per streek en per taal, een wetenschappelijke naam niet",
            "een wetenschappelijke naam is altijd korter dan de volkse naam van die soort",
            "volkse namen bestaan enkel voor dieren en niet voor planten of schimmels",
            "een wetenschappelijke naam zegt hoeveel exemplaren er van die soort zijn",
        ],
        antwoord=0,
        uitleg="Eenzelfde plant heet in twee dorpen soms anders, en één naam dekt soms twee soorten. De wetenschappelijke naam is eenduidig.",
    ),
    dict(
        type="waarofniet",
        vraag="Het uitsterven van soorten gebeurt vandaag veel sneller dan uit de natuurlijke achtergrond te verwachten is.",
        antwoord=True,
        uitleg="Soorten sterven altijd uit, maar het tempo ligt nu veel hoger. De oorzaak daarvan is grotendeels menselijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vijver wordt gedempt om een parking te bouwen. Welk gevolg voor de biodiversiteit verwacht je?",
        opties=[
            "de soorten die van water afhangen verdwijnen uit het gebied",
            "de soorten verhuizen allemaal naar de volgende vijver",
            "de biodiversiteit stijgt, want er komt meer open ruimte",
            "er verandert niets zolang er elders nog vijvers zijn",
        ],
        antwoord=0,
        uitleg="Kikkers, libellen en waterplanten hebben die vijver nodig. Een parking is voor hen geen leefgebied, en niet elke soort kan verhuizen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan iemand in zijn eigen tuin de biodiversiteit verhogen? Kruis alles aan wat juist is.",
        opties=[
            "inheemse planten zetten die bloeien voor insecten",
            "een hoekje laten verwilderen",
            "geen chemische bestrijdingsmiddelen gebruiken",
            "alle bodem met tegels bedekken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voedsel, schuilplaats en geen gif: dat zijn de drie dingen die helpen. Tegels halen juist alle leven uit de bodem.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gebied met weinig soorten herstelt sneller na een verstoring dan een gebied met veel soorten.",
        antwoord=False,
        uitleg="Het is omgekeerd: met veel soorten kan een andere soort de rol overnemen van wie wegvalt. Dat maakt zo'n gebied veerkrachtiger.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een micro-organisme?",
        opties=[
            "een levend wezen dat te klein is om met het blote oog te zien",
            "een deeltje dat nog kleiner is dan een molecule water",
            "een cel die zich niet meer kan delen en dus niet groeit",
            "een organisme dat enkel in water en nooit op het land leeft",
        ],
        antwoord=0,
        uitleg="Micro-organismen zijn alleen onder een microscoop te zien. Bacteriën, veel schimmels en eencellige organismen horen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft een bacterie? Kruis alles aan wat juist is.",
        opties=[
            "ze bestaat uit één cel",
            "ze heeft geen echte celkern",
            "ze kan zich zelf delen en zo vermeerderen",
            "ze heeft een gastheercel nodig om zich te vermeerderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een bacterie is een volwaardige cel zonder kern en kan zich zelfstandig delen. Een gastheer nodig hebben is net het kenmerk van een virus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een virus geen gewoon levend wezen?",
        opties=[
            "het heeft geen eigen stofwisseling en kan zich enkel in een gastheercel vermeerderen",
            "het is veel groter dan een bacterie en past daarom in geen enkele gastheercel",
            "het bestaat uit meerdere cellen die elk geen echte celkern hebben",
            "het kan buiten een levend lichaam geen ogenblik blijven bestaan",
        ],
        antwoord=0,
        uitleg="Een virus is weinig meer dan erfelijk materiaal in een jasje. Zonder cel om te kapen doet het niets.",
    ),
    dict(
        type="invultekst",
        vraag="Wat heeft een virus nodig om zich te vermeerderen?",
        antwoord=["gastheercel", "een gastheercel", "een cel"],
        uitleg="Het virus brengt zijn erfelijk materiaal in een cel en laat die cel nieuwe virussen bouwen. Zonder gastheercel lukt dat niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Antibiotica werken tegen bacteriën en niet tegen virussen.",
        antwoord=True,
        uitleg="Antibiotica grijpen in op iets dat enkel een bacterie heeft, zoals haar celwand. Bij een griep of een verkoudheid helpen ze dus niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is antibioticaresistentie?",
        opties=[
            "bacteriën die tegen een antibioticum kunnen, winnen het pleit",
            "een mens die na een kuur allergisch wordt voor een antibioticum",
            "een virus dat tegen een antibioticum kan en er dus niet van sterft",
            "een antibioticum dat na zijn vervaldatum niet meer werkzaam is",
        ],
        antwoord=0,
        uitleg="Bij elke kuur blijven de bacteriën over die er het best tegen kunnen. Door onnodig gebruik wordt die groep groter, en dan werkt het middel niet meer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een antibioticakuur afmaken, ook als je je al beter voelt, helpt resistentie te voorkomen.",
        antwoord=True,
        uitleg="Stop je te vroeg, dan blijven net de taaiste bacteriën over. Die kunnen zich dan vermeerderen en zijn moeilijker te bestrijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruikt de mens micro-organismen? Kruis alles aan wat juist is.",
        opties=[
            "het maken van yoghurt en kaas",
            "het rijzen van brood en het brouwen van bier",
            "het zuiveren van afvalwater",
            "het bewaren van vlees in de diepvries",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bacteriën en gisten zetten stoffen om, en dat gebruiken we in de keuken en in de waterzuivering. Diepvriezen remt juist alle leven af.",
    ),
    dict(
        type="invultekst",
        vraag="Welk micro-organisme laat brooddeeg rijzen?",
        antwoord=["gist", "gisten", "de gist"],
        uitleg="Gist is een eencellige schimmel. Zij zet suiker om en maakt daarbij koolstofdioxide, en dat gas blaast het deeg op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de rol van bacteriën en schimmels in een ecosysteem?",
        opties=[
            "ze breken dood materiaal af en maken de mineralen weer vrij",
            "ze maken met behulp van licht hun eigen voedsel aan",
            "ze jagen op de kleine dieren die in de bodem leven",
            "ze slaan koolstofdioxide uit de lucht op in hun celwand",
        ],
        antwoord=0,
        uitleg="Zonder reducenten bleven de mineralen in dood blad en kadavers opgesloten. Zij maken de kringloop rond.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder bacteriën en schimmels zouden de mineralen in dood materiaal opgesloten blijven.",
        antwoord=True,
        uitleg="Zij breken de organische stof af tot stoffen die planten weer kunnen opnemen. Daarom heten ze reducenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke barrières houden micro-organismen uit het lichaam? Kruis alles aan wat juist is.",
        opties=[
            "de onbeschadigde huid",
            "het zuur in de maag",
            "het slijm in de luchtwegen",
            "het skelet van de romp",
        ],
        antwoord=[0, 1, 2],
        uitleg="Huid, maagzuur en slijmvliezen vormen de eerste verdedigingslinie. Het skelet heeft daar geen rol in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen witte bloedcellen bij een infectie?",
        opties=[
            "ze eten indringers op of maken antistoffen tegen ze",
            "ze vervoeren zuurstof naar de plaats van de infectie",
            "ze stoppen de bloeding bij een wonde",
            "ze maken de koorts zelf lager",
        ],
        antwoord=0,
        uitleg="Sommige witte bloedcellen slokken bacteriën op, andere maken antistoffen die precies op één indringer passen. Zuurstof vervoeren doen de rode bloedcellen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stof die het lichaam maakt en die precies op één indringer past?",
        antwoord=["antistof", "antistoffen", "antilichaam"],
        uitleg="Een antistof hecht zich aan de indringer en maakt hem onschadelijk of kenbaar voor de opruimers. Elke antistof past op één soort indringer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een vaccin?",
        opties=[
            "het laat het lichaam antistoffen en afweercellen aanmaken zonder dat je ziek wordt",
            "het doodt alle bacteriën die zich op dat ogenblik in het lichaam bevinden",
            "het geeft kant-en-klare antistoffen mee die iemand anders al gemaakt heeft",
            "het verhoogt de lichaamstemperatuur zodat de ziektekiemen eraan sterven",
        ],
        antwoord=0,
        uitleg="Een vaccin toont het afweersysteem een onschadelijk stuk van de ziekteverwekker. Komt de echte later, dan is de afweer al klaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Na een ziekte sta je tegen diezelfde ziekteverwekker weer even onbeschermd als voordien.",
        antwoord=False,
        uitleg="Het afweersysteem houdt cellen over die de indringer herkennen. Bij een tweede ontmoeting staat de reactie dus veel sneller klaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is handen wassen zo doeltreffend tegen besmetting?",
        opties=[
            "zeep en water halen de micro-organismen van de huid, voor ze in het lichaam raken",
            "zeep doodt de virussen die al in het bloed van de handen en de armen zitten",
            "warm water laat de huid zelf antistoffen tegen indringers maken",
            "handen wassen verhoogt de weerstand van het hele lichaam tegen ziekte",
        ],
        antwoord=0,
        uitleg="De meeste besmettingen gaan via de handen naar mond, neus of ogen. Wassen onderbreekt die weg en is dus de eenvoudigste maatregel.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle bacteriën in en op ons lichaam zijn schadelijk.",
        antwoord=False,
        uitleg="De meeste zijn onschuldig of zelfs nuttig. De darmbacteriën helpen bij de spijsvertering en houden schadelijke soorten weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een bacterie zich zo snel vermeerderen?",
        opties=[
            "ze deelt zich in twee, en in gunstige omstandigheden kan dat elk half uur",
            "ze krijgt bij elke deling honderden nakomelingen tegelijk, niet twee",
            "ze vermeerdert zich zonder enig voedsel of vocht op te nemen",
            "ze deelt zich enkel bij een temperatuur onder het vriespunt",
        ],
        antwoord=0,
        uitleg="Verdubbelen klinkt bescheiden, maar het gaat razendsnel: uit één bacterie worden er in tien uur al miljoenen. Daarom bederft voedsel in de warmte zo vlug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat een restje soep een nacht op het aanrecht staan. Waarom is dat af te raden?",
        opties=[
            "bij kamertemperatuur delen bacteriën zich snel tot er onveilige aantallen zijn",
            "soep verliest bij kamertemperatuur al haar voedingsstoffen en vitaminen",
            "bacteriën kunnen enkel in koude soep groeien en nergens anders in",
            "de soep neemt bacteriën uit de lucht op die er niet meer uit weggaan",
        ],
        antwoord=0,
        uitleg="Soep is vochtig en voedzaam, en kamertemperatuur is ideaal om te delen. In de koelkast gaat dat delen veel trager.",
    ),
]
