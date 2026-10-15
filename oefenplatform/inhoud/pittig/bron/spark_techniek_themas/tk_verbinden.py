# -*- coding: utf-8 -*-
"""Pittige vragen bij "Verbinden, afwerken en veilig werken" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en deel 2, maar je kiest zelf een verbinding of een
afwerking voor een concreet werkstuk en spoort onveilige redeneringen op.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="Je maakt een houten kist met een deksel dat open en dicht moet, en je wilt de kist later nog uit elkaar kunnen halen. Welke combinatie kies je?",
        opties=[
            "Een scharnier voor het deksel, schroeven voor de wanden",
            "Een scharnier voor het deksel, houtlijm voor de wanden",
            "Houtlijm voor het deksel, schroeven voor de wanden",
            "Nagels voor het deksel, houtlijm voor de wanden",
        ],
        antwoord=0,
        uitleg="Het deksel moet draaien, dus is er een scharnier nodig. De wanden moeten later weer los kunnen, dus kies je schroeven: die draai je eruit. Lijm en nagels zijn voor een verbinding die voorgoed vast mag zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de hoeken van een fotokader komen twee schuin afgezaagde stukken tegen elkaar, en ze zitten vast met houten pinnetjes. Welke twee verbindingen herken je?",
        opties=[
            "Een verstekverbinding en een deuvelverbinding",
            "Een boutverbinding en een lasverbinding",
            "Een deuvelverbinding en een soldeerverbinding",
            "Een verstekverbinding en een lasverbinding",
        ],
        antwoord=0,
        uitleg="Schuin afgezaagd tegen elkaar is een verstekverbinding. Houten pinnetjes zijn deuvels. Lassen en solderen zijn voor metaal en draden, niet voor een houten kader.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke voorwerpen kan je de verbinding losmaken zonder iets kapot te maken? (meerdere antwoorden mogelijk)",
        opties=[
            "De rits van je jas",
            "Het klittenband van je schoen",
            "De magneetsluiting van een etui",
            "De bout en moer van een fietsbel",
            "Een gelast hekje van metaal",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Een rits, klittenband, een magneet en een bout met moer kan je openmaken zonder schade. Een lasverbinding niet: de metalen delen zijn samengesmolten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je lijmt een houten vogelhuisje dat buiten komt te hangen, en je hebt veel tijd nodig om alle stukjes goed te schikken. Waar let je op bij de keuze van de lijm? (meerdere antwoorden mogelijk)",
        opties=[
            "Dat de lijm tegen nat kan",
            "Dat de verwerkingstijd lang genoeg is",
            "Dat de lijm geschikt is om hout aan hout te lijmen",
            "Dat de lijm zo snel mogelijk vastpakt",
            "Dat de tube van de lijm zo licht mogelijk is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het huisje komt buiten, dus kan het nat worden. Je wilt tijd om te schikken, dus heb je een lange verwerkingstijd nodig; een lijm die meteen pakt, is daar net het omgekeerde van. En de lijm moet passen bij de materialen, hier hout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen zijn NIET veilig? (meerdere antwoorden mogelijk)",
        opties=[
            "Met een ring aan je vinger aan de zaagmachine werken",
            "Even het meetbereik overschrijden omdat het maar kort is",
            "De stekker uittrekken voor je het zaagblad vervangt",
            "Gemorste olie op de vloer meteen opkuisen",
            "Je lange haar samenbinden voor je aan de boor begint",
        ],
        antwoord=[0, 1],
        uitleg="Een ring kan blijven haken aan een zaagmachine, en het meetbereik mag je nooit overschrijden, ook niet even. De stekker uittrekken, gemorste olie meteen opkuisen en lang haar samenbinden zijn juist wat je hoort te doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wilt een houten tafel een donkerdere kleur geven, maar de nerf van het hout moet zichtbaar blijven. Welke afwerking kies je?",
        opties=[
            "Beitsen",
            "Verven met dekkende verf",
            "Alleen goed schuren",
            "Twee lagen dekkende verf",
        ],
        antwoord=0,
        uitleg="Beits kleurt het hout en trekt erin, zodat je de nerf nog ziet. Verf legt een dekkende laag over het hout en verbergt de nerf. Schuren maakt glad, maar geeft geen kleur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een houten bankje komt buiten in de tuin te staan. In welke volgorde werk je het af?",
        opties=[
            "Eerst schuren, dan vernissen",
            "Eerst vernissen, dan schuren",
            "Alleen schuren, vernis is overbodig",
            "Eerst beitsen, dan schuren tot de kleur weg is",
        ],
        antwoord=0,
        uitleg="Schuren maakt het hout glad, en daarna komt de afwerking. Buiten krijgt het bankje vocht en slijtage te verwerken, en daar beschermt vernis tegen. Na het vernissen schuren zou die beschermlaag weer wegnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klasgenoot zegt: 'Ik beits mijn plank, dan ligt er een dekkende laag over het hout en zie je de nerf niet meer.' Wat klopt er niet?",
        opties=[
            "Beitsen kleurt het hout en legt geen dekkende laag",
            "Beitsen is geen afwerkingstechniek maar een verbinding",
            "Beitsen maakt het hout glad, net zoals schuren dat doet",
            "Er klopt niets niet, beitsen en verven zijn hetzelfde",
        ],
        antwoord=0,
        uitleg="Beits trekt in het hout en kleurt het, zodat je de nerf nog ziet. Een dekkende laag die de nerf verbergt, is wat verf doet. Glad maken is het werk van schuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand vervangt het zaagblad van een figuurzaag. De schakelaar staat uit, maar de stekker zit nog in het stopcontact. Wat is het gevaar?",
        opties=[
            "De machine kan aanslaan terwijl je eraan zit",
            "De stroom loopt langs het zaagblad naar de vloer",
            "Het zaagblad wordt magnetisch en trekt aan je ring",
            "Er is geen gevaar zolang de schakelaar uit staat",
        ],
        antwoord=0,
        uitleg="Zolang de stekker erin zit, kan de machine aanslaan, bijvoorbeeld als iemand per ongeluk tegen de schakelaar stoot. Daarom trek je eerst de stekker uit voor je iets aan een machine doet. Een uitgezette schakelaar is niet genoeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op de deur van de werkplaats hangt een blauw rond pictogram met een masker. Wat betekent dat?",
        opties=[
            "Een mondmasker is hier verplicht, want er is stof of damp",
            "Een mondmasker is hier verboden, want je moet goed praten",
            "Een mondmasker mag hier, maar je kiest het zelf",
            "Hier hangt de doos met mondmaskers voor de klas",
        ],
        antwoord=0,
        uitleg="Een blauw rond pictogram betekent altijd dat iets verplicht is. Met een masker erop gaat het om een mondmasker, dat je draagt bij stof of damp. Toegelaten of verboden is iets anders dan verplicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een botte zaag gevaarlijker dan een goed onderhouden zaag?",
        opties=[
            "Een botte zaag glijdt makkelijker weg",
            "Een botte zaag maakt meer lawaai in de klas",
            "Een botte zaag is zwaarder om op te tillen",
            "Een botte zaag geeft een andere kleur zaagsel",
        ],
        antwoord=0,
        uitleg="Onderhouden gereedschap blijft veilig en nauwkeurig werken. Een botte zaag pakt niet goed en glijdt weg, en dan kan je je verwonden. Zwaarder of luider wordt hij er niet van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wilt een fietsbel op je stuur zetten, en hem later naar je nieuwe fiets verhuizen. Welke verbinding kies je?",
        opties=[
            "Een boutverbinding",
            "Een lasverbinding",
            "Een lijmverbinding",
            "Een soldeerverbinding",
        ],
        antwoord=0,
        uitleg="Een bout met een moer kan je losdraaien zonder iets kapot te maken. Lassen, lijmen en solderen geven een verbinding die je niet zonder schade losmaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een smid zet twee metalen buizen van een hek voorgoed aan elkaar door ze samen te smelten. Welke verbinding is dat?",
        opties=[
            "Een lasverbinding",
            "Een soldeerverbinding",
            "Een lijmverbinding",
            "Een deuvelverbinding",
        ],
        antwoord=0,
        uitleg="Bij lassen smelten de twee metalen delen zelf samen. Bij solderen verbind je draden met gesmolten tin, dus daar smelt het tin en niet de draad. Een deuvel is een houten pinnetje.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor een kast die je later nog wilt demonteren, kies je beter nagels dan schroeven.",
        antwoord=False,
        uitleg="Een nagel gebruik je als het voorgoed vast mag. Wil je de kast later uit elkaar halen, dan kies je schroeven, want die draai je er gewoon weer uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een soldeerverbinding en een lasverbinding hebben gemeen dat je ze niet zomaar weer losmaakt.",
        antwoord=True,
        uitleg="Bij allebei wordt er iets gesmolten: bij lassen het metaal zelf, bij solderen het tin. Zulke verbindingen krijg je niet los zoals een bout of een schroef.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meetinstrument laat je best aanstaan tot de volgende les, dan hoef je het niet opnieuw aan te zetten.",
        antwoord=False,
        uitleg="Een meetinstrument schakel je uit als je klaar bent, anders loopt de batterij leeg. De volgende les werkt het dan misschien niet meer.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook als je de stofafzuiging van de figuurzaag gebruikt, draag je nog oogbescherming.",
        antwoord=True,
        uitleg="De stofafzuiging is er tegen het zaagstof dat je zou inademen. De oogbescherming is er tegen de spaanders die wegspringen. Het zijn twee aparte maatregelen op de veiligheidsinstructiekaart, en de ene vervangt de andere niet.",
    ),
    dict(
        type="invultekst",
        vraag="Twee draadjes in een zaklamp zijn aan elkaar gezet met een gesmolten metaal dat daarna weer hard werd. Welk metaal is dat? Antwoord met één woord.",
        antwoord="tin",
        uitleg="Dat is een soldeerverbinding: twee draden verbonden met gesmolten tin. Bij lassen smelt het metaal van de stukken zelf.",
    ),
    dict(
        type="invultekst",
        vraag="In het magazijn van de werkplaats kan er iets zwaars op je voeten vallen. Welke persoonlijke beschermingsmiddelen draag je daar? Antwoord met één woord.",
        antwoord="veiligheidsschoenen",
        uitleg="Waar iets zwaars kan vallen, zijn veiligheidsschoenen verplicht. Het pictogram is een blauw rond teken met een schoen erop.",
    ),
    dict(
        type="invultekst",
        vraag="Je hebt twee stukken gelijmd en wil ze nog een beetje verschuiven. Hoe heet de tijd waarin dat nog kan? Antwoord met één woord.",
        antwoord="verwerkingstijd",
        uitleg="De verwerkingstijd zegt hoe lang je de stukken nog kunt verschuiven voor de lijm pakt. Daarom let je er bij het kiezen van een lijm op.",
    ),
]
