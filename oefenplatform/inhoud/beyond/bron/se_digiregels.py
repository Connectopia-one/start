# -*- coding: utf-8 -*-
"""Veilig en correct online: recht, phishing en netiquette.

Het vierde en laatste thema uit "ik ben digitaal vaardig" (17,5 procent), en
het enige van dat blok dat niet over Office gaat.

De fiche zegt hier iets anders dan bij Word, Excel en PowerPoint. Daar moet je
weten wat een knop doet; hier moet je handelen:

    "Je krijgt op het examen een situatie die zich afspeelt in de digitale
    wereld. Je handelt volgens de juridische, ethische en sociaal
    verantwoorde regels. Je krijgt bronmateriaal waar je informatie uit haalt
    en je verwerkt deze op een kritische manier."

Daarom staan er in dit thema veel vragen met een situatie erin: iemand vindt
een foto, iemand krijgt een mail, iemand ziet een bericht. De vraag is dan
niet wat een begrip betekent maar wat je doet.

Wat de fiche opsomt als mogelijke situaties:
    auteursrecht
    creative commons
    cyberpesten en -intimidatie
    digitale wachtwoorden
    nepnieuws
    phishing
    portretrecht
    privacyrecht
    ...

Daarnaast staat er één aparte regel: "Je past de principes van netiquette toe
in je online communicatie."

De puntjes achter het rijtje betekenen dat er meer kan komen. We blijven hier
toch bij wat de fiche noemt, want een verzonnen regel is erger dan een regel
die ontbreekt.

Twee verschillen waar het vaak op vastloopt:

  1. **Auteursrecht tegenover portretrecht.** Het auteursrecht is van wie de
     foto maakte, het portretrecht van wie erop staat. Voor een foto van een
     persoon heb je dus met twee rechten te maken.

  2. **Creative commons is geen "mag alles".** De maker geeft vooraf
     toelating, maar onder voorwaarden: naam vermelden, niet commercieel, of
     niets veranderen.

Deel 1 is auteursrecht, creative commons, portretrecht en privacyrecht.
Deel 2 is wachtwoorden, phishing, nepnieuws, cyberpesten en netiquette.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer krijgt iemand het auteursrecht op een tekst of een foto?",
        opties=[
            "automatisch, zodra hij het werk zelf gemaakt heeft",
            "pas nadat hij het werk heeft laten registreren bij een dienst",
            "pas nadat hij het werk ergens gepubliceerd heeft",
            "enkel als hij er het tekentje voor auteursrecht bij zet",
        ],
        antwoord=0,
        uitleg="Je moet niets aanvragen. Het ontstaat bij het maken van iets eigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt online een mooie foto zonder enige vermelding erbij. Wat mag je ervan uitgaan?",
        opties=[
            "dat ze beschermd is en je toelating nodig hebt om ze te gebruiken",
            "dat ze vrij is, want er staat nergens dat ze beschermd is",
            "dat ze vrij is zodra je ze via een zoekmachine gevonden hebt",
            "dat ze vrij is als je ze enkel voor school wil gebruiken",
        ],
        antwoord=0,
        uitleg="Geen vermelding betekent niet vrij. De bescherming is er ook zonder dat iemand het erbij schrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoelang blijft het auteursrecht in ons land gelden?",
        opties=[
            "tot zeventig jaar na het overlijden van de maker",
            "tot zeventig jaar na het maken van het werk zelf",
            "tot vijftig jaar na de eerste publicatie van het werk",
            "zolang de maker het werk zelf nog ergens verkoopt",
        ],
        antwoord=0,
        uitleg="Daarna is het werk vrij. Daarom kan je oude boeken en schilderijen wel vrij gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is creative commons?",
        opties=[
            "een licentie waarmee de maker vooraf toelating geeft, onder voorwaarden",
            "een wet die alle werken op het internet vrij van rechten maakt",
            "een website waar je beschermde beelden zonder toelating vindt",
            "een dienst die het auteursrecht van makers laat registreren",
        ],
        antwoord=0,
        uitleg="De maker zegt zelf vooraf wat mag. Je moet hem dus niet meer apart iets vragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een foto staat onder creative commons met naamsvermelding. Wat moet je doen?",
        opties=[
            "de naam van de maker bij de foto zetten waar je ze gebruikt",
            "de maker eerst een bericht sturen met de vraag of het mag",
            "de foto betalen voor je ze op je eigen pagina zet",
            "de foto enkel offline gebruiken en nooit online zetten",
        ],
        antwoord=0,
        uitleg="Naamsvermelding is de lichtste voorwaarde, en meteen de voorwaarde die het vaakst vergeten wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarden kan een maker aan een creative commons licentie hangen? Er zijn meerdere juiste antwoorden.",
        opties=[
            "zijn naam moet vermeld worden bij elk gebruik",
            "het werk mag niet commercieel gebruikt worden",
            "het werk mag niet aangepast of bewerkt worden",
            "het werk mag enkel in België gebruikt worden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Naamsvermelding, niet commercieel en niets veranderen zijn de gewone voorwaarden. Een grens per land hoort er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het portretrecht?",
        opties=[
            "het recht van wie op een beeld staat om over dat beeld te beslissen",
            "het recht van wie een beeld maakte om over dat beeld te beslissen",
            "het recht om in een openbare ruimte foto's te mogen nemen",
            "het recht om een foto van jezelf gratis te laten afdrukken",
        ],
        antwoord=0,
        uitleg="Het auteursrecht is van de fotograaf, het portretrecht van wie erop te zien is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je neemt op een feest een foto van een vriendin en wil die op je verhaal zetten. Wat heb je nodig?",
        opties=[
            "haar toelating, want zij is herkenbaar op de foto te zien",
            "niets, want jij hebt de foto zelf met je eigen gsm gemaakt",
            "niets, want het was een feest en dus een openbare plaats",
            "de toelating van de organisator van dat feest in de zaal",
        ],
        antwoord=0,
        uitleg="Jij hebt het auteursrecht, maar zij heeft het portretrecht. Vragen is dus niet alleen vriendelijk, het hoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zet zonder te vragen een foto van jou op zijn pagina. Wat kan je doen?",
        opties=[
            "hem vragen de foto weg te halen, want je hebt portretrecht",
            "niets, want hij heeft de foto gemaakt en mag erover beslissen",
            "niets, want wat online staat is niet meer weg te halen",
            "enkel iets doen als je op de foto iets verkeerds doet",
        ],
        antwoord=0,
        uitleg="En lukt dat niet, dan kan je het bij het platform zelf melden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschermt het privacyrecht?",
        opties=[
            "je persoonsgegevens en wat er met die gegevens mag gebeuren",
            "de teksten en de beelden die je zelf gemaakt hebt",
            "je rekening tegen diefstal door iemand van buiten",
            "de berichten die je op een openbare pagina plaatst",
        ],
        antwoord=0,
        uitleg="Gegevens over jou zijn van jou. Wie ze bijhoudt, moet zeggen waarvoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een website vraagt bij een inschrijving voor een nieuwsbrief ook je rijksregisternummer. Wat klopt daar niet aan?",
        opties=[
            "er worden meer gegevens gevraagd dan voor dat doel nodig zijn",
            "een nieuwsbrief mag volgens de wet nooit gegevens vragen",
            "een website mag enkel een mailadres bijhouden, niets anders",
            "gegevens mogen enkel op papier en nooit digitaal gevraagd worden",
        ],
        antwoord=0,
        uitleg="Voor een nieuwsbrief is een mailadres genoeg. Niet meer vragen dan je nodig hebt is een vaste regel.",
    ),
    dict(
        type="waarofniet",
        vraag="Het auteursrecht is van wie het werk maakte, het portretrecht van wie erop staat.",
        antwoord=True,
        uitleg="Bij een foto van een persoon spelen dus twee rechten tegelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werk onder creative commons mag je altijd zonder voorwaarden gebruiken.",
        antwoord=False,
        uitleg="De maker geeft vooraf toelating, maar meestal met voorwaarden zoals naamsvermelding.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een stukje uit een boek citeren als je de bron vermeldt.",
        antwoord=True,
        uitleg="Kort citeren met bronvermelding mag, bijvoorbeeld in een werkje of een bespreking. Een heel hoofdstuk overnemen is geen citaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Gegevens die een bedrijf over jou bijhoudt, mag je nooit inkijken.",
        antwoord=False,
        uitleg="Je mag ze juist opvragen, laten verbeteren en in veel gevallen laten verwijderen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het recht van wie een werk gemaakt heeft om erover te beslissen?",
        antwoord=["auteursrecht", "het auteursrecht"],
        uitleg="Het auteursrecht. Het ontstaat automatisch bij het maken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het recht van wie herkenbaar op een foto staat?",
        antwoord=["portretrecht", "het portretrecht"],
        uitleg="Het portretrecht, los van het auteursrecht van de fotograaf.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel jaar na het overlijden van de maker loopt het auteursrecht nog door?",
        antwoord=["70", "zeventig", "70 jaar"],
        uitleg="Zeventig jaar. Daarna is het werk vrij te gebruiken.",
    ),
    dict(
        type="invultekst",
        vraag="Welke voorwaarde van een creative commons licentie vraagt dat je de maker noemt?",
        antwoord=["naamsvermelding", "de naamsvermelding"],
        uitleg="Naamsvermelding. In de licenties staat ze als BY.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het recht dat je persoonsgegevens beschermt?",
        antwoord=["privacyrecht", "het privacyrecht", "privacy"],
        uitleg="Het privacyrecht. Het bepaalt wie welke gegevens mag bijhouden en waarvoor.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat maakt een wachtwoord sterk?",
        opties=[
            "het is lang, niet te raden en je gebruikt het maar op één plaats",
            "het is kort en moeilijk, zodat je het nergens moet opschrijven",
            "het is de naam van je huisdier met een cijfer erachter",
            "het is hetzelfde op al je sites, zodat je het nooit vergeet",
        ],
        antwoord=0,
        uitleg="Lengte helpt meer dan rare tekens, en hergebruik is de grootste fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is hetzelfde wachtwoord op verschillende sites gebruiken een slecht idee?",
        opties=[
            "raakt het op één site buiten, dan liggen al je andere rekeningen open",
            "sommige sites laten een wachtwoord niet twee keer gebruiken",
            "je wachtwoord wordt daardoor na een tijd automatisch zwakker",
            "je moet het dan op elke site tegelijk komen veranderen",
        ],
        antwoord=0,
        uitleg="Wie het ene wachtwoord heeft, probeert het gewoon elders. Daarom overal een ander.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is tweestapsverificatie?",
        opties=[
            "naast je wachtwoord nog een code of een vinger als tweede slot",
            "twee verschillende wachtwoorden na elkaar op dezelfde site",
            "je wachtwoord twee keer intikken om tikfouten te vermijden",
            "een wachtwoord dat na twee dagen van zelf vervalt",
        ],
        antwoord=0,
        uitleg="Ook met je wachtwoord komt iemand er dan niet in zonder dat tweede stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is phishing?",
        opties=[
            "een nagemaakt bericht dat je gegevens of je geld wil loskrijgen",
            "een beschadigd bestand dat je computer trager laat werken",
            "een reclamebericht dat je te vaak in je mailbox krijgt",
            "een bericht dat per ongeluk bij de verkeerde persoon komt",
        ],
        antwoord=0,
        uitleg="Het bericht doet zich voor als je bank, de post of een bekende dienst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een mail van je bank met de vraag om via een link je gegevens te bevestigen. Wat doe je?",
        opties=[
            "niet klikken en zelf naar de site of de app van je bank gaan",
            "op de link klikken en kijken of de pagina er echt uitziet",
            "je gegevens invullen, want de mail draagt het logo van je bank",
            "de mail doorsturen naar je vrienden om hen te waarschuwen",
        ],
        antwoord=0,
        uitleg="Een bank vraagt je nooit om via een link je codes te bevestigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dingen verraden vaak een phishingbericht? Er zijn meerdere juiste antwoorden.",
        opties=[
            "een afzender waarvan het adres net niet juist is",
            "haast: je moet nu iets doen of je rekening gaat dicht",
            "een link die naar een adres gaat dat je niet herkent",
            "een bericht dat in het Nederlands geschreven is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Haast en een adres dat net niet klopt zijn de twee sterkste tekens. De taal zegt niets, want een nepbericht kan vlekkeloos Nederlands zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is nepnieuws?",
        opties=[
            "onjuiste berichten die met opzet als echt nieuws verspreid worden",
            "nieuws dat je zelf niet gelooft omdat het je niet bevalt",
            "nieuws dat enkel op sociale media en nooit op tv komt",
            "nieuws met een fout dat later door de redactie hersteld wordt",
        ],
        antwoord=0,
        uitleg="Een vergissing in een krant is geen nepnieuws. De opzet maakt het verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een schokkend bericht op sociale media zonder bron erbij. Wat doe je eerst?",
        opties=[
            "nakijken of ernstige media hetzelfde bericht ook brengen",
            "het meteen doorsturen zodat je vrienden het ook weten",
            "kijken hoeveel mensen het bericht al gedeeld hebben",
            "in de reacties vragen of iemand weet of het waar is",
        ],
        antwoord=0,
        uitleg="Deel nooit iets dat je niet nagekeken hebt. Hoeveel keer iets gedeeld is, zegt niets over de waarheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een foto bij een bericht lijkt verdacht. Hoe kan je ze nakijken?",
        opties=[
            "de foto omgekeerd opzoeken en zien waar ze eerder opdook",
            "de foto groter maken tot je ziet dat ze bewerkt is",
            "kijken of de kleuren van de foto natuurlijk overkomen",
            "aan de persoon die het bericht plaatste vragen waar ze vandaan komt",
        ],
        antwoord=0,
        uitleg="Oude foto's duiken vaak bij een nieuwe gebeurtenis op. Omgekeerd zoeken laat dat meteen zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand uit je klas wordt in een groepsgesprek dag na dag belachelijk gemaakt. Wat is de beste reactie?",
        opties=[
            "bewijs bewaren, het melden en de persoon zelf niet alleen laten",
            "er niet op reageren en het gesprek gewoon stil verlaten",
            "in het gesprek terug pesten zodat ze het zelf ook voelen",
            "wachten tot het stopt, want zoiets gaat meestal van zelf over",
        ],
        antwoord=0,
        uitleg="Een schermafbeelding is je bewijs. Niet meedoen is nodig maar niet genoeg: wie gepest wordt, heeft iemand nodig die iets zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand stuurt een foto van een klasgenoot door die duidelijk niet bedoeld was om gedeeld te worden. Hoe zit dat?",
        opties=[
            "dat mag niet, ook al heeft hij de foto zelf gekregen",
            "dat mag, want hij heeft de foto van die persoon zelf gekregen",
            "dat mag zolang hij er geen naam bij vermeldt",
            "dat mag binnen een gesloten groep van vrienden",
        ],
        antwoord=0,
        uitleg="Een foto krijgen is geen toelating om ze verder te sturen. Daar gaan portretrecht en privacy over.",
    ),
    dict(
        type="waarofniet",
        vraag="Een wachtwoord deel je nooit, ook niet met iemand die zegt dat hij van de helpdesk is.",
        antwoord=True,
        uitleg="Een echte helpdesk heeft je wachtwoord niet nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bericht in vlot Nederlands met het juiste logo kan geen phishing zijn.",
        antwoord=False,
        uitleg="Nepberichten zien er vaak perfect uit. Kijk naar de afzender en de link, niet naar de opmaak.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij cyberpesten is een schermafbeelding nemen een goede eerste stap.",
        antwoord=True,
        uitleg="Berichten worden vaak gewist. Met een schermafbeelding heb je nog iets in handen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bericht volledig in hoofdletters tikken hoort bij goede netiquette.",
        antwoord=False,
        uitleg="Hoofdletters lezen online als roepen. Netiquette vraagt net het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet een nagemaakt bericht dat je gegevens of je geld wil loskrijgen?",
        antwoord=["phishing", "phising"],
        uitleg="Phishing, naar het Engelse woord voor vissen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de extra code naast je wachtwoord als tweede slot op je rekening?",
        antwoord=["tweestapsverificatie", "tweefactorauthenticatie"],
        uitleg="Tweestapsverificatie, soms tweefactorauthenticatie genoemd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heten de omgangsregels voor hoe je je online gedraagt?",
        antwoord=["netiquette", "de netiquette"],
        uitleg="Netiquette, uit net en etiquette.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je onjuiste berichten die met opzet als echt nieuws verspreid worden?",
        antwoord=["nepnieuws", "fake news"],
        uitleg="Nepnieuws. De opzet maakt het verschil met een gewone fout.",
    ),
    dict(
        type="invultekst",
        vraag="Wat neem je van een pestbericht zodat je het bewijs nog hebt als het gewist wordt?",
        antwoord=["schermafbeelding", "een schermafbeelding", "screenshot"],
        uitleg="Een schermafbeelding of screenshot.",
    ),
]
