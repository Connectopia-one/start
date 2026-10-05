# -*- coding: utf-8 -*-
"""Tekstsoorten, tekstverbanden, verwijswoorden en de leesstrategieën.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit. De fiche zet zes
soorten lees- en luisterteksten op een rij die je moet kunnen begrijpen:
informatieve, persuasieve, opiniërende, prescriptieve, narratieve en literaire
teksten, elk met voorbeelden. Daarnaast staat er een lijst strategieën die je
bij lezen en luisteren mag gebruiken.

Waarom dat een eigen thema is: op het examen weet je nooit vooraf welke soort
tekst je krijgt. Als je ziet dat een tekst je wil overtuigen, lees je anders dan
wanneer hij je iets uitlegt. En de structuuraanduiders — verwijswoorden zoals
ils en y, signaalwoorden zoals d'abord, puis en par contre — zijn precies de
woorden waarmee een tekst zijn gedachtegang vasthoudt.

Deel 1 gaat over de zes tekstsoorten en over het communicatiemodel: van wie is
de tekst, waarom is hij gemaakt, voor wie is hij bedoeld? Deel 2 gaat over de
woorden die de tekst aan elkaar houden en over wat je doet met een woord dat je
niet kent.
"""

SOUPE = (
    "Faites chauffer un litre de bouillon. Pendant ce temps, coupez les carottes en rondelles. "
    "Mettez-les dans le bouillon et laissez cuire quinze minutes."
)
PLAGE = (
    "Chaque été, trois tonnes de déchets restent sur nos plages. Ramasse ce que tu apportes. "
    "Une plage propre, c'est l'affaire de tout le monde."
)
FILM = (
    "Je suis sorti de la salle sans rien comprendre. Les images sont belles, d'accord, mais "
    "l'histoire ne va nulle part. À mon avis, deux heures c'est beaucoup trop long."
)
TRAIN = (
    "À partir du 15 décembre, le train de 7 h 12 vers Bruxelles partira cinq minutes plus tôt. "
    "Les voyageurs qui prennent le bus 24 peuvent toujours faire la correspondance."
)
GRAND = (
    "Ce matin-là, ma grand-mère a mis son chapeau rouge sans rien dire. Nous avons marché "
    "jusqu'au bout du village. Elle s'est arrêtée devant une maison bleue et elle a souri."
)
CHANSON = (
    "Je t'écris d'une ville où il pleut tous les jours, où les trains ne s'arrêtent plus. "
    "Si tu passes un dimanche, apporte-moi le soleil."
)

DEEL1 = [
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {SOUPE} » Wat voor soort tekst is dit?",
         opties=["een prescriptieve tekst",
                 "een opiniërende tekst",
                 "een narratieve tekst",
                 "een persuasieve tekst"],
         antwoord=0,
         uitleg="Faites, coupez, mettez: de tekst zegt je wat je moet doen. Dat is een prescriptieve tekst, zoals een recept of een handleiding."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {PLAGE} » Wat voor soort tekst is dit, en waaraan zie je dat?",
         opties=["persuasief, want de tekst wil je gedrag veranderen",
                 "informatief, want de tekst geeft alleen cijfers",
                 "narratief, want de tekst vertelt een gebeurtenis",
                 "literair, want de tekst speelt met woorden"],
         antwoord=0,
         uitleg="Ramasse ce que tu apportes is een oproep aan jou: raap op wat je meebrengt. Een tekst die je wil overtuigen of beïnvloeden, is persuasief."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {FILM} » Wat voor soort tekst is dit?",
         opties=["een opiniërende tekst",
                 "een informatieve tekst",
                 "een prescriptieve tekst",
                 "een narratieve tekst"],
         antwoord=0,
         uitleg="À mon avis betekent naar mijn mening. Iemand geeft zijn mening over een film: dat is een opiniërende tekst, zoals een recensie."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {TRAIN} » Wat voor soort tekst is dit?",
         opties=["een informatieve tekst",
                 "een persuasieve tekst",
                 "een opiniërende tekst",
                 "een literaire tekst"],
         antwoord=0,
         uitleg="De tekst geeft je gegevens over een uurwijziging, zonder je iets te vragen of een mening te geven. Dat is informatief."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {GRAND} » Wat voor soort tekst is dit?",
         opties=["een narratieve tekst",
                 "een prescriptieve tekst",
                 "een informatieve tekst",
                 "een persuasieve tekst"],
         antwoord=0,
         uitleg="De tekst geeft gebeurtenissen weer op een verhalende manier: eerst dit, dan dat. Dat is een narratieve tekst, zoals een reisverslag of een getuigenis."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {CHANSON} » Welke twee dingen maken hiervan een literaire tekst?",
         opties=["De tekst speelt in op een gevoel.",
                 "De woorden zeggen meer dan wat er letterlijk staat.",
                 "De tekst somt feiten en cijfers op.",
                 "De tekst geeft je een opdracht."],
         antwoord=[0, 1],
         uitleg="Apporte-moi le soleil vraagt niet om echte zon. Een literaire tekst heeft een esthetische waarde en speelt vaak in op emoties."),
    dict(type="waarofniet",
         vraag="Een hotelbeoordeling op een reiswebsite is volgens die indeling een opiniërende tekst.",
         antwoord=True,
         uitleg="Iemand geeft er zijn mening over het hotel. Een recensie en een reactie op sociale media horen bij dezelfde soort."),
    dict(type="waarofniet",
         vraag="De veiligheidsvoorschriften in een bedrijf zijn een narratieve tekst.",
         antwoord=False,
         uitleg="Ze leggen uit wat en hoe je iets moet doen, en dat is prescriptief. Narratief is een verhaal, zoals een videoblog of een getuigenis."),
    dict(type="meerkeuze",
         vraag="Een reclamefilmpje, een campagne tegen te snel rijden en een flyer van een fitnesszaal horen bij dezelfde soort. Welke?",
         opties=["persuasieve teksten",
                 "prescriptieve teksten",
                 "informatieve teksten",
                 "narratieve teksten"],
         antwoord=0,
         uitleg="Alle drie willen ze je overtuigen of beïnvloeden."),
    dict(type="invultekst",
         vraag="Een tekst die je uitlegt wat of hoe je iets moet doen, zoals een recept of een schoolreglement: hoe heet die soort? Schrijf het woord.",
         antwoord=["prescriptief", "prescriptieve"],
         uitleg="Prescriptief komt van prescrire, voorschrijven."),
    dict(type="invultekst",
         vraag="Een gedicht, een lied, een strip of een kortverhaal: hoe heet die soort tekst? Schrijf het woord.",
         antwoord=["literair", "literaire"],
         uitleg="Een literaire tekst heeft een esthetische waarde en speelt vaak in op emoties."),
    # --- Het communicatiemodel -------------------------------------------
    dict(type="meerkeuze",
         vraag="Je gebruikt bij het lezen het communicatiemodel. Welke drie vragen stel je jezelf dan?",
         opties=["Van wie is de tekst?",
                 "Waarom heeft de schrijver de tekst gemaakt?",
                 "Voor wie is de tekst bedoeld?",
                 "Hoeveel woorden telt de tekst?"],
         antwoord=[0, 1, 2],
         uitleg="Zender, bedoeling en ontvanger. Het aantal woorden zegt niets over de boodschap."),
    dict(type="meerkeuze",
         vraag="Je krijgt een Franse tekst die begint met « Chère Madame Dupont, ». Wat weet je dan al, nog voor je verder leest?",
         opties=["Het is een brief of mail aan één bepaalde persoon.",
                 "Het is een artikel uit een krant.",
                 "Het is een gedicht.",
                 "Het is een reclameboodschap."],
         antwoord=0,
         uitleg="Een aanspreking met een naam hoort bij een brief of een mail. De vorm van een tekst verklapt vaak al de soort."),
    dict(type="waarofniet",
         vraag="De titel, de tussentitels en een foto bij een tekst zijn visuele hulpmiddelen die je mag gebruiken voor je begint te lezen.",
         antwoord=True,
         uitleg="Ze geven je een eerste idee van het onderwerp. Vetgedrukte woorden en een grafiek horen daar ook bij."),
    dict(type="meerkeuze",
         vraag="Wat betekent het dat je hoofdzaken van bijzaken moet onderscheiden?",
         opties=["Je ziet welke zinnen de boodschap dragen en welke alleen een voorbeeld geven.",
                 "Je leest alleen de eerste en de laatste zin van een tekst.",
                 "Je onthoudt alle cijfers die in de tekst staan.",
                 "Je zoekt elk woord op dat je niet kent."],
         antwoord=0,
         uitleg="De hoofdpunten ondersteunen de hoofdgedachte. Een voorbeeld of een detail is een bijzaak."),
    dict(type="waarofniet",
         vraag="Voor je een tekst begint te lezen, is het nuttig om jezelf te vragen wat je al weet over het onderwerp.",
         antwoord=True,
         uitleg="Je voorkennis helpt je raden waarover de tekst zal gaan, en daardoor begrijp je sneller wat er staat."),
    dict(type="meerkeuze",
         vraag="Op het examen mag je een online woordenboek gebruiken. Hoe ga je daar best mee om?",
         opties=["Je zoekt alleen de woorden op die je echt nodig hebt om de tekst te begrijpen.",
                 "Je zoekt elk woord op dat je niet kent, van de eerste tot de laatste regel.",
                 "Je gebruikt het woordenboek beter helemaal niet.",
                 "Je zoekt eerst alle woorden op en leest daarna de tekst."],
         antwoord=0,
         uitleg="Je hebt niet de tijd om elk woord op te zoeken. Bepaal eerst of de betekenis van dat woord echt belangrijk is."),
    dict(type="waarofniet",
         vraag="Een mail naar een klant en een recept horen bij dezelfde tekstsoort.",
         antwoord=False,
         uitleg="De mail geeft informatie, het recept schrijft voor wat je moet doen. Een stukje uit een leerboek, een interview en een krantenartikel horen wél bij de mail: alle vier zijn ze informatief."),
    dict(type="meerkeuze",
         vraag="Je leest een Franse tekst over een onderwerp dat je niet kent, en halfweg snap je niets meer. Wat doe je het eerst?",
         opties=["Je leest verder tot het einde en kijkt dan welke stukken je wel begrepen hebt.",
                 "Je begint helemaal opnieuw en leest woord per woord.",
                 "Je zoekt het hele stuk woord voor woord op in het woordenboek.",
                 "Je slaat de tekst over en gaat naar de volgende vraag."],
         antwoord=0,
         uitleg="Een tekst legt zichzelf vaak verder uit. Eerst het geheel, dan de stukken: zo weet je ook welke woorden echt in de weg staan."),
    dict(type="waarofniet",
         vraag="Een tekst kan maar één soort zijn: informatief of persuasief, nooit een beetje van beide.",
         antwoord=False,
         uitleg="Een flyer van een sportclub geeft informatie én wil je overhalen. Je kijkt naar wat de tekst vooral wil."),
]

TRI = (
    "D'abord, enlevez le couvercle. Ensuite, rincez le bocal à l'eau froide. Enfin, mettez-le "
    "dans le sac bleu. Attention : les bouchons vont dans le sac bleu aussi, mais pas les "
    "couvercles en métal."
)
VOISINS = (
    "Nos voisins ont un grand jardin. Ils y cultivent des tomates et des haricots. L'été "
    "dernier, ils nous en ont donné un plein panier. Nous les avons remerciés avec une tarte."
)
MARCHE = (
    "Le marché est moins cher que le supermarché, par contre il n'ouvre que le mercredi. Comme "
    "je travaille ce jour-là, j'y vais rarement. Donc j'achète mes légumes au magasin du coin, "
    "même si c'est dommage."
)
ATELIER = (
    "L'atelier est complet pour le mois de mars. Cependant, nous ouvrons un deuxième groupe en "
    "avril. Si vous êtes intéressé, répondez avant le 1er mars, car les places partent vite."
)

DEEL2 = [
    # --- Signaalwoorden ---------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {TRI} » Welke woorden geven de orde van de stappen aan?",
         opties=["d'abord",
                 "ensuite",
                 "enfin",
                 "attention"],
         antwoord=[0, 1, 2],
         uitleg="D'abord is eerst, ensuite is daarna, enfin is tot slot. Attention is een waarschuwing, geen stap in de rij."),
    dict(type="invultekst",
         vraag="Hetzelfde tekstje over het sorteren. Welk Frans woord betekent 'daarna'? Schrijf het woord.",
         antwoord=["ensuite"],
         uitleg="Ensuite, rincez le bocal: daarna, spoel de pot."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {MARCHE} » Wat doet het woord par contre in die eerste zin?",
         opties=["het zet twee dingen tegenover elkaar",
                 "het geeft een reden",
                 "het geeft een gevolg",
                 "het voegt een voorbeeld toe"],
         antwoord=0,
         uitleg="Par contre betekent daarentegen: goedkoper, maar wel alleen op woensdag open."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje over de markt. Welk woord geeft daar een gevolg aan?",
         opties=["donc", "comme", "même si", "moins"],
         antwoord=0,
         uitleg="Donc betekent dus. Comme geeft hier een reden (omdat), même si betekent zelfs als."),
    dict(type="waarofniet",
         vraag="In dat tekstje over de markt geeft comme je travaille ce jour-là een reden.",
         antwoord=True,
         uitleg="Comme betekent hier omdat: omdat ik die dag werk, ga ik er zelden naartoe."),
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {ATELIER} » Wat betekent cependant hier?",
         opties=["nochtans, toch",
                 "daarom",
                 "bijvoorbeeld",
                 "eerst"],
         antwoord=0,
         uitleg="De les van maart is vol; cependant, nochtans, komt er een tweede groep in april. Cependant zet het tweede stuk tegenover het eerste."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje over de workshop. Welk woord geeft de reden waarom je snel moet antwoorden?",
         opties=["car", "si", "avant", "deuxième"],
         antwoord=0,
         uitleg="Car les places partent vite: want de plaatsen gaan snel weg. Car betekent want."),
    dict(type="invultekst",
         vraag="Welk Frans signaalwoord betekent 'omdat' en legt een reden uit, bijvoorbeeld in « Je reste à la maison ... il pleut »? Schrijf de twee woorden.",
         antwoord=["parce que"],
         uitleg="Parce qu'il pleut: omdat het regent. Voor een klinker wordt het parce qu'."),
    # --- Verwijswoorden ---------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {VOISINS} » Naar wie verwijst ils in de tweede zin?",
         opties=["naar de buren",
                 "naar de tomaten",
                 "naar de schrijver en zijn gezin",
                 "naar de tuinen in de straat"],
         antwoord=0,
         uitleg="Nos voisins ont un grand jardin. Ils y cultivent: zij, de buren, kweken daar. Ils verwijst naar het onderwerp van de zin ervoor."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje over de buren. Waarnaar verwijst y in Ils y cultivent des tomates?",
         opties=["naar de tuin",
                 "naar de tomaten",
                 "naar de buren",
                 "naar de zomer"],
         antwoord=0,
         uitleg="Y vervangt een plaats: dans le jardin. Ze kweken er, in de tuin, tomaten."),
    dict(type="meerkeuze",
         vraag="Nog dat tekstje over de buren. Naar wie verwijst les in Nous les avons remerciés?",
         opties=["naar de buren",
                 "naar de bonen",
                 "naar de tomaten en de bonen",
                 "naar de mensen van de straat"],
         antwoord=0,
         uitleg="Je bedankt mensen, geen bonen. Het voltooid deelwoord remerciés staat trouwens in het meervoud, net omdat les naar de buren verwijst."),
    dict(type="waarofniet",
         vraag="In datzelfde tekstje vervangt en in ils nous en ont donné de buren.",
         antwoord=False,
         uitleg="En vervangt een onbepaalde hoeveelheid, hier de tomaten en de bonen: ze hebben ons daarvan een volle mand gegeven. Naar de buren verwijst ils."),
    dict(type="meerkeuze",
         vraag="Waarom zijn verwijswoorden zoals il, elle, y en en belangrijk als je leest?",
         opties=["Ze houden de zinnen aan elkaar, en als je niet weet waarnaar ze verwijzen, verlies je de draad.",
                 "Ze staan altijd vooraan in een tekst.",
                 "Ze zeggen je welke soort tekst je leest.",
                 "Ze vervangen altijd een persoon."],
         antwoord=0,
         uitleg="Ze verwijzen naar personen, voorwerpen, begrippen of plaatsen uit een vorige zin. Een schrijver gebruikt ze om niet te moeten herhalen."),
    # --- Betekenis afleiden ------------------------------------------------
    dict(type="meerkeuze",
         vraag="Je leest « Il a oublié son parapluie, donc il est rentré tout mouillé. » Je kent mouillé niet. Wat betekent het waarschijnlijk?",
         opties=["nat", "moe", "boos", "laat"],
         antwoord=0,
         uitleg="Hij vergat zijn paraplu, dus kwam hij zo thuis. De rest van de zin geeft de betekenis weg: dat is betekenis afleiden uit de context."),
    dict(type="meerkeuze",
         vraag="Je leest het Franse woord dangereux en je kent het niet. Hoe raad je de betekenis?",
         opties=["Je ziet er het Nederlandse of Engelse woord in dat erop lijkt.",
                 "Je kijkt naar het aantal letters.",
                 "Je kijkt of het woord vetgedrukt staat.",
                 "Je leest het woord luidop."],
         antwoord=0,
         uitleg="Dangereux lijkt op dangerous en op het Nederlandse danger: gevaarlijk. Je kennis van andere talen helpt je woorden raden."),
    dict(type="meerkeuze",
         vraag="Je leest « Le chemin est impraticable en hiver. » Hoe helpt de bouw van het woord impraticable je?",
         opties=["Het voorvoegsel im- betekent niet, dus het is niet begaanbaar.",
                 "Het achtervoegsel -able betekent dat het verboden is.",
                 "Het woord staat in het meervoud.",
                 "Het woord is een werkwoord in de verleden tijd."],
         antwoord=0,
         uitleg="Praticable is begaanbaar, im- maakt het negatief. Zo kan je de betekenis van een onbekend woord afleiden uit de manier waarop het gevormd is."),
    dict(type="waarofniet",
         vraag="Als je in een tekst een woord niet kent, moet je altijd eerst beslissen of dat woord wel nodig is om de tekst te begrijpen.",
         antwoord=True,
         uitleg="Soms kan je er gewoon over: de tekst blijft duidelijk. Zoek alleen op wat je echt nodig hebt."),
    dict(type="meerkeuze",
         vraag="Welke van deze woorden zijn signaalwoorden die je helpen de gedachtegang van een Franse tekst te volgen?",
         opties=["d'abord",
                 "par contre",
                 "enfin",
                 "beaucoup"],
         antwoord=[0, 1, 2],
         uitleg="Eerst, daarentegen, tot slot: die drie zeggen hoe de stukken van de tekst zich tot elkaar verhouden. Beaucoup betekent gewoon veel."),
    dict(type="meerkeuze",
         vraag="Je krijgt een Franse tekst met als titel « Trois bonnes raisons de prendre le vélo ». Wat verwacht je?",
         opties=["een tekst die je wil overhalen om te gaan fietsen",
                 "een tekst die uitlegt hoe je een fiets herstelt",
                 "een verhaal over een fietstocht van de schrijver",
                 "een lijst met de prijzen van fietsen"],
         antwoord=0,
         uitleg="Trois bonnes raisons de betekent drie goede redenen om. Een titel die redenen belooft, hoort bij een tekst die je wil overtuigen."),
    dict(type="waarofniet",
         vraag="Signaalwoorden staan altijd aan het begin van een alinea.",
         antwoord=False,
         uitleg="Ze kunnen midden in een zin staan, zoals donc of car. Hun plaats zegt niets, hun betekenis wel."),
]
