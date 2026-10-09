# -*- coding: utf-8 -*-
"""Persoonlijkheid: wat ze is en hoe een brein reageert.

Het eerste van drie thema's over persoonlijkheidspsychologie, het derde
onderdeel van gedragswetenschappen. Eerst de begrippen, dan de benadering die
de persoonlijkheid in het brein zelf zoekt.

De lijstjes staan letterlijk in de fiche:

    elementen van persoonlijkheid: karakter, motivatie, temperament, trekken
        of disposities, zelfbeeld
    biologische benadering
        reinforcement sensitivity theory: Jeffrey Gray - Behavioral
            Inhibition System, Behavioral Activation System
        biologische theorie van persoonlijkheid: Hans Eysenck - introversie
            en extraversie, arousal

De fiche vraagt ook uitdrukkelijk naar de invloed van culturele factoren op de
vorming van persoonlijkheid, met cross-cultureel onderzoek erbij. Dat zit in
deel 1.

Hans Eysenck komt in deze fiche twee keer voor: hier met zijn biologische
theorie en de arousal, en in het thema over de trekken met zijn PEN-model.

Deel 1 is wat persoonlijkheid is en welke elementen ze heeft.
Deel 2 is de biologische benadering.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is persoonlijkheid?",
        opties=[
            "het geheel van wat iemand kenmerkt en vrij stabiel blijft",
            "de stemming waarin iemand op een bepaalde dag is",
            "de rol die iemand in een groep opneemt",
            "de mening die anderen over iemand hebben",
        ],
        antwoord=0,
        uitleg="Persoonlijkheid is wat vrij stabiel blijft doorheen situaties en jaren. Een stemming wisselt, een persoonlijkheid niet zomaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vijf elementen van persoonlijkheid noemt de fiche?",
        opties=[
            "karakter",
            "temperament",
            "zelfbeeld",
            "attributie",
            "conformisme",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vijf zijn karakter, motivatie, temperament, trekken of disposities en zelfbeeld. Attributie en conformisme horen bij de sociale psychologie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is temperament?",
        opties=[
            "de aangeboren aard waarmee iemand reageert",
            "het geheel van wat iemand zelf aanleert",
            "het beeld dat iemand van zichzelf heeft",
            "de reden waarom iemand iets doet",
        ],
        antwoord=0,
        uitleg="Temperament is de aangeboren kant: hoe snel, hoe heftig en hoe lang iemand reageert. Je ziet het al bij een baby.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het zelfbeeld?",
        opties=[
            "het beeld dat iemand van zichzelf heeft",
            "het beeld dat anderen van iemand hebben",
            "de aangeboren aard van iemand",
            "de drijfveer achter het gedrag",
        ],
        antwoord=0,
        uitleg="Het zelfbeeld is hoe iemand zichzelf ziet. Dat hoeft niet te kloppen met hoe anderen hem zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn trekken of disposities?",
        opties=[
            "vaste eigenschappen die in veel situaties terugkomen",
            "stemmingen die van dag tot dag wisselen",
            "regels die een groep aan haar leden oplegt",
            "doelen die iemand voor zichzelf stelt",
        ],
        antwoord=0,
        uitleg="Een trek is een vaste eigenschap, zoals zorgvuldig of spontaan. Je ziet ze in verschillende situaties terugkomen.",
    ),
    dict(
        type="invultekst",
        vraag="Het element van persoonlijkheid dat over de aangeboren aard van reageren gaat, is het ...",
        antwoord=["temperament"],
        uitleg="Het temperament. De vijf elementen zijn karakter, motivatie, temperament, trekken of disposities en zelfbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Motivatie staat in de fiche als een element van persoonlijkheid.",
        antwoord=True,
        uitleg="Waar. De vijf elementen zijn karakter, motivatie, temperament, trekken of disposities en zelfbeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="Temperament en karakter betekenen volgens de fiche precies hetzelfde.",
        antwoord=False,
        uitleg="Niet waar. Ze staan als twee aparte elementen. Temperament is aangeboren, karakter krijgt ook vorm door opvoeding en ervaring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een baby huilt van de eerste week fel en lang bij elke verandering. Welk element van persoonlijkheid zie je hier?",
        opties=[
            "het temperament",
            "het zelfbeeld",
            "de motivatie",
            "het karakter",
        ],
        antwoord=0,
        uitleg="Bij een baby van een week is er nog geen opvoeding geweest. Wat je ziet is zijn temperament.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jade zegt over zichzelf dat ze slecht is in talen, terwijl haar rapport dat niet toont. Welk element van persoonlijkheid is hier aan het werk?",
        opties=[
            "het zelfbeeld",
            "het temperament",
            "de trekken",
            "de motivatie",
        ],
        antwoord=0,
        uitleg="Haar beeld van zichzelf klopt niet met de feiten. Dat is precies wat een zelfbeeld kan doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met de invloed van culturele factoren op persoonlijkheid?",
        opties=[
            "welke eigenschappen gewaardeerd worden, verschilt per cultuur",
            "persoonlijkheid is in elke cultuur precies hetzelfde",
            "cultuur bepaalt het temperament van een baby",
            "cultuur speelt alleen bij volwassenen een rol",
        ],
        antwoord=0,
        uitleg="In de ene samenleving wordt opvallen gewaardeerd, in de andere bescheidenheid. Dat stuurt mee welke kanten iemand ontwikkelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient cross-cultureel onderzoek in de persoonlijkheidspsychologie?",
        opties=[
            "nagaan of een theorie ook buiten één cultuur opgaat",
            "nagaan hoeveel mensen in een land een trek hebben",
            "nagaan of een theorie bij dieren ook opgaat",
            "nagaan hoe oud een theorie precies is",
        ],
        antwoord=0,
        uitleg="Een theorie die alleen in één land is getest, kan iets van die cultuur meten in plaats van iets van de mens.",
    ),
    dict(
        type="invultekst",
        vraag="Het beeld dat iemand van zichzelf heeft, heet het ...",
        antwoord=["zelfbeeld"],
        uitleg="Het zelfbeeld. Het is een van de vijf elementen van persoonlijkheid in de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Een persoonlijkheid ligt volgens de fiche al bij de geboorte helemaal vast.",
        antwoord=False,
        uitleg="Niet waar. De fiche spreekt over de vorming en de ontwikkeling van persoonlijkheid, en noemt ook culturele factoren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een trek verschilt van een stemming doordat ze in veel verschillende situaties terugkomt.",
        antwoord=True,
        uitleg="Waar. Een stemming is van vandaag, een trek zie je ook morgen en in een ander gezelschap terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt de fiche de twee woorden die ze voor hetzelfde element gebruikt: trekken en ...?",
        opties=[
            "disposities",
            "attributies",
            "cognities",
            "motivaties",
        ],
        antwoord=0,
        uitleg="Trekken of disposities. Het woord dispositie kwam ook terug bij de dispositionele attributie van Heider.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kinderen groeien in hetzelfde gezin op en krijgen een heel verschillende persoonlijkheid. Wat volgt daaruit?",
        opties=[
            "persoonlijkheid komt niet van de omgeving alleen",
            "persoonlijkheid komt volledig van de omgeving",
            "de omgeving speelt geen enkele rol",
            "persoonlijkheid ligt volledig vast bij de geboorte",
        ],
        antwoord=0,
        uitleg="Zelfde gezin en toch verschillend: dan spelen aanleg en eigen keuzes ook mee. Dat is de tweede basisvraag uit het eerste thema.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk element van persoonlijkheid gaat over de drijfveer achter gedrag?",
        opties=[
            "de motivatie",
            "het temperament",
            "het zelfbeeld",
            "de trekken",
        ],
        antwoord=0,
        uitleg="De motivatie is wat iemand in beweging zet. Ze staat als een van de vijf elementen in de fiche.",
    ),
    dict(
        type="invultekst",
        vraag="De vijf elementen van persoonlijkheid zijn karakter, motivatie, temperament, zelfbeeld en ... of disposities.",
        antwoord=["trekken"],
        uitleg="Trekken of disposities. Zij vormen de kern van de trektheoretische benadering, later in dit vak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om persoonlijkheid in vijf elementen op te delen?",
        opties=[
            "omdat elke theorie vooral op een ander element inzet",
            "omdat elk element bij een andere leeftijd hoort",
            "omdat je zo kan voorspellen wat iemand gaat doen",
            "omdat elk element in elke cultuur gelijk is",
        ],
        antwoord=0,
        uitleg="De biologische benadering kijkt naar het temperament, de humanistische naar het zelfbeeld, de trektheorie naar de trekken. De elementen helpen om de theorieën te plaatsen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar zoekt de biologische benadering van persoonlijkheid de verklaring?",
        opties=[
            "in de werking van het brein en het lichaam",
            "in de opvoeding die iemand kreeg",
            "in de groep waar iemand bij hoort",
            "in het beeld dat iemand van zichzelf heeft",
        ],
        antwoord=0,
        uitleg="De biologische benadering legt het verschil tussen mensen in hoe hun brein en hun lichaam reageren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de reinforcement sensitivity theory?",
        opties=[
            "Jeffrey Gray",
            "Hans Eysenck",
            "Albert Bandura",
            "Julian Rotter",
        ],
        antwoord=0,
        uitleg="Gray. Zijn twee systemen zijn het Behavioral Inhibition System en het Behavioral Activation System.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor is het Behavioral Inhibition System van Gray gevoelig?",
        opties=[
            "voor dreiging en straf",
            "voor beloning en winst",
            "voor gezelschap en drukte",
            "voor nieuwe ervaringen",
        ],
        antwoord=0,
        uitleg="Het BIS remt gedrag af bij gevaar. Wie een sterk BIS heeft, is voorzichtiger en sneller ongerust.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor is het Behavioral Activation System van Gray gevoelig?",
        opties=[
            "voor beloning en winst",
            "voor dreiging en straf",
            "voor stilte en rust",
            "voor regels en afspraken",
        ],
        antwoord=0,
        uitleg="Het BAS zet gedrag juist in gang bij iets dat iets oplevert. Wie een sterk BAS heeft, gaat er sneller op af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bram ziet een kans om snel geld te verdienen en gaat er meteen op in, zonder de risico's te bekijken. Welk systeem van Gray is hier sterk?",
        opties=[
            "het Behavioral Activation System",
            "het Behavioral Inhibition System",
            "de arousal van Eysenck",
            "de locus of control van Rotter",
        ],
        antwoord=0,
        uitleg="Op een beloning af gaan zonder te remmen past bij een sterk BAS.",
    ),
    dict(
        type="meerkeuze",
        vraag="Lien denkt bij elk voorstel eerst aan wat er kan mislopen en houdt zich daarom in. Welk systeem van Gray is hier sterk?",
        opties=[
            "het Behavioral Inhibition System",
            "het Behavioral Activation System",
            "het realiteitsprincipe van Freud",
            "de zelfeffectiviteit van Bandura",
        ],
        antwoord=0,
        uitleg="Remmen bij mogelijke dreiging is het werk van het BIS.",
    ),
    dict(
        type="invultekst",
        vraag="Het systeem van Gray dat gedrag afremt bij dreiging, is het Behavioral ... System.",
        antwoord=["Inhibition"],
        uitleg="Het Behavioral Inhibition System, afgekort BIS. Het andere is het Behavioral Activation System, afgekort BAS.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Gray heeft iedereen zowel een BIS als een BAS, maar is het ene bij de ene mens sterker dan het andere.",
        antwoord=True,
        uitleg="Waar. Het verschil tussen mensen zit in de verhouding tussen de twee systemen, niet in het ontbreken van een systeem.",
    ),
    dict(
        type="waarofniet",
        vraag="Het BAS van Gray reageert vooral op straf.",
        antwoord=False,
        uitleg="Niet waar, dat is het BIS. Het BAS reageert op beloning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de biologische theorie van persoonlijkheid met de arousal?",
        opties=[
            "Hans Eysenck",
            "Jeffrey Gray",
            "Gordon Allport",
            "Carl Rogers",
        ],
        antwoord=0,
        uitleg="Eysenck. Hij verklaart introversie en extraversie door een verschil in arousal, het activatieniveau van het brein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is arousal bij Eysenck?",
        opties=[
            "het activatieniveau van het brein",
            "de snelheid waarmee iemand leert",
            "de sterkte van iemands zelfbeeld",
            "de hoeveelheid vrienden die iemand heeft",
        ],
        antwoord=0,
        uitleg="Arousal is hoe sterk het brein al in gang staat. Wie van nature een hoge arousal heeft, heeft minder prikkels van buiten nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt Eysenck over iemand die introvert is?",
        opties=[
            "zijn brein staat al hoog in arousal en zoekt minder prikkels",
            "zijn brein staat laag in arousal en zoekt meer prikkels",
            "zijn brein reageert niet op prikkels van buiten",
            "zijn brein wisselt elke dag van arousal",
        ],
        antwoord=0,
        uitleg="Bij een hoge arousal is drukte snel te veel. Daarom zoekt een introvert eerder rust op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt Eysenck over iemand die extravert is?",
        opties=[
            "zijn brein staat laag in arousal en zoekt meer prikkels",
            "zijn brein staat al hoog in arousal en zoekt rust",
            "zijn brein reageert niet op gezelschap",
            "zijn brein heeft geen vast arousalniveau",
        ],
        antwoord=0,
        uitleg="Bij een lage arousal is er van buiten meer nodig om op een aangenaam niveau te komen. Daarom zoekt een extravert gezelschap en drukte op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee vrienden komen van een drukke fuif. De ene is opgeladen, de andere volledig leeg. Welke verklaring geeft Eysenck?",
        opties=[
            "zij hebben een verschillend arousalniveau",
            "zij hebben een verschillende locus of control",
            "zij hebben een verschillend zelfbeeld",
            "zij hebben een verschillende motivatie",
        ],
        antwoord=0,
        uitleg="De extravert had de prikkels nodig, de introvert had er al te veel. Dat is het verschil in arousal.",
    ),
    dict(
        type="invultekst",
        vraag="Het begrip van Eysenck voor het activatieniveau van het brein is ...",
        antwoord=["arousal"],
        uitleg="Arousal. Met dat begrip verklaart hij het verschil tussen introversie en extraversie.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Eysenck is introvert zijn hetzelfde als verlegen zijn.",
        antwoord=False,
        uitleg="Niet waar. Introversie gaat over hoeveel prikkels iemand nodig heeft, niet over durven. Een introvert kan heel goed spreken voor een groep.",
    ),
    dict(
        type="waarofniet",
        vraag="Zowel Gray als Eysenck zoekt de verklaring voor persoonlijkheid in de werking van het brein.",
        antwoord=True,
        uitleg="Waar. Daarom staan ze samen onder de biologische benadering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee begrippen horen bij Jeffrey Gray en welke bij Hans Eysenck?",
        opties=[
            "BIS en BAS horen bij Gray",
            "arousal hoort bij Eysenck",
            "wederzijds determinisme hoort bij Gray",
            "locus of control hoort bij Eysenck",
        ],
        antwoord=[0, 1],
        uitleg="BIS en BAS zijn van Gray, de arousal is van Eysenck. Wederzijds determinisme is van Bandura en de locus of control van Rotter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk element van persoonlijkheid sluit het nauwst aan bij de biologische benadering?",
        opties=[
            "het temperament",
            "het zelfbeeld",
            "de motivatie",
            "het karakter",
        ],
        antwoord=0,
        uitleg="Het temperament is de aangeboren aard van reageren, en dat is precies wat Gray en Eysenck in het brein zoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bezwaar tegen een volledig biologische verklaring van persoonlijkheid?",
        opties=[
            "ze geeft te weinig plaats aan ervaring en cultuur",
            "ze geeft te veel plaats aan ervaring en cultuur",
            "ze kan het temperament niet verklaren",
            "ze werkt niet met meetbare begrippen",
        ],
        antwoord=0,
        uitleg="Wie alles in het brein legt, krijgt het moeilijk met de invloed van opvoeding en cultuur, en die staat ook in de fiche.",
    ),
]
