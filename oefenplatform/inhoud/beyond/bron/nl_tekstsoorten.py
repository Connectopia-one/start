# -*- coding: utf-8 -*-
"""Tekstsoorten en teksttypes — 🌍 Beyond, Nederlands.

Naast de vakfiche geschreven: de zeven soorten lees- en luisterteksten staan
er met hun eigen voorbeelden bij, en de opmerking dat veel teksten meer dan
één doel tegelijk dienen. Deel 1 gaat over de soorten zelf, deel 2 legt ze op
echte teksten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van een informatieve tekst?",
        opties=[
            "je iets laten weten over een onderwerp",
            "je overhalen om iets te kopen of te doen",
            "je stap voor stap laten zien hoe iets werkt",
            "je raken met een mooie of ontroerende vorm",
        ],
        antwoord=0,
        uitleg="Informeren is het doel. Een krantenartikel, een interview of een reportage wil je in de eerste plaats iets bijbrengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke tekst is in de eerste plaats persuasief?",
        opties=[
            "een folder van een politieke partij",
            "een bijsluiter bij een geneesmiddel",
            "een stukje uit een leerboek over fotosynthese",
            "een reisverslag van drie weken in Noorwegen",
        ],
        antwoord=0,
        uitleg="Persuasief betekent overtuigend of beïnvloedend. Een bijsluiter legt uit, een leerboek informeert en een reisverslag vertelt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een tekst die je instructies geeft over hoe je iets doet? Vul aan: een ... tekst.",
        antwoord=["prescriptieve", "prescriptief"],
        uitleg="Een recept, een handleiding of een schoolreglement schrijft voor wat je moet doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderscheidt een argumentatieve tekst van een opiniërende tekst?",
        opties=[
            "argumenten dragen er een standpunt",
            "er staat altijd een verhaal in verwerkt",
            "er komt geen enkele mening van de schrijver in voor",
            "hij verschijnt uitsluitend in gedrukte kranten en tijdschriften",
        ],
        antwoord=0,
        uitleg="In een opiniërende tekst geeft iemand zijn mening; in een argumentatieve tekst onderbouwt iemand een standpunt met argumenten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een recensie kan tegelijk informatief en opiniërend zijn.",
        antwoord=True,
        uitleg="Veel teksten combineren doelen. Een recensie vertelt eerst waar het boek over gaat en zegt daarna wat de schrijver ervan vond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke soort hoort een true crime podcast?",
        opties=[
            "narratief",
            "prescriptief",
            "argumentatief",
            "persuasief",
        ],
        antwoord=0,
        uitleg="Er wordt een verhaal verteld, met een begin, een verloop en een afloop. Dat is narratief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt een literaire tekst?",
        opties=[
            "de esthetische waarde, die vaak inspeelt op emoties",
            "het ontbreken van elke verhaallijn of personages",
            "de verplichting om in dichtvorm geschreven te zijn",
            "de aanwezigheid van een lijst met geraadpleegde bronnen",
        ],
        antwoord=0,
        uitleg="Een kortverhaal, een gedicht, een strip, een lied of stand-upcomedy kan literair zijn. Het gaat om de vorm en wat die teweegbrengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden horen bij de opiniërende teksten?",
        opties=[
            "een hotelbeoordeling op een online platform",
            "een productreview",
            "een protestlied",
            "een veiligheidsvoorschrift in een bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een veiligheidsvoorschrift geeft je instructies en is dus prescriptief. De drie andere geven elk iemands mening weer.",
    ),
    dict(
        type="waarofniet",
        vraag="De lees- en luisterteksten op het examen zijn uitsluitend in het Standaardnederlands.",
        antwoord=False,
        uitleg="Er zitten ook andere taalvariëteiten in, zoals tussentaal, dialect of jongerentaal. Die herkennen hoort bij de leerstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een instructiefilmpje op YouTube over hoe je een fietsband plakt. Welke soort is dat?",
        opties=[
            "prescriptief",
            "narratief",
            "opiniërend",
            "literair",
        ],
        antwoord=0,
        uitleg="Het schrijft je stap voor stap voor wat je moet doen. Dat de maker er ook wat bij vertelt, verandert het hoofddoel niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je teksten waarin een verhaal verteld wordt? Vul aan: ... teksten.",
        antwoord=["narratieve", "narratief"],
        uitleg="Een reisverslag, een videoblog of een verhalend gedicht zijn narratief.",
    ),
    dict(
        type="waarofniet",
        vraag="Een pleidooi, een betoog en een debat zijn alle drie argumentatief.",
        antwoord=True,
        uitleg="In alle drie onderbouwt iemand een standpunt met argumenten. Dat is wat argumentatieve teksten doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om bij het lezen de tekstsoort te bepalen?",
        opties=[
            "je weet dan wat de schrijver van je wil",
            "je kan de tekst dan sneller uitlezen zonder iets te missen",
            "je hoeft dan de titel en de tussentitels niet meer te lezen",
            "je kan dan met zekerheid zeggen wie de tekst geschreven heeft",
        ],
        antwoord=0,
        uitleg="Wie weet dat een tekst wil overtuigen, leest hem anders dan wie denkt dat hij enkel informeert. Het doel van de zender stuurt je leeshouding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een publireportage ziet eruit als een artikel maar is betaald door een merk. Welke soort is dat vooral?",
        opties=[
            "persuasief",
            "informatief",
            "prescriptief",
            "narratief",
        ],
        antwoord=0,
        uitleg="De vorm is informatief, maar het doel is je overtuigen. Daarom staat de publireportage bij de persuasieve teksten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stukje uit een leerboek is een voorbeeld van een narratieve tekst.",
        antwoord=False,
        uitleg="Een leerboek wil je iets bijbrengen over een onderwerp, dus dat is informatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over tekstsoorten kloppen?",
        opties=[
            "één tekst kan meer dan één doel tegelijk hebben",
            "de voorbeelden kunnen zowel geschreven als gesproken zijn",
            "de soort hangt af van het doel van de zender",
            "elke tekst hoort altijd bij precies één van de zeven soorten"
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste klopt net niet: een recensie, een documentaire of een column zit vaak op twee soorten tegelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je teksten die je proberen te overtuigen of te beïnvloeden? Vul aan: ... teksten.",
        antwoord=["persuasieve", "persuasief"],
        uitleg="Reclame, propaganda en nepnieuws horen daar allemaal bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stand-upcomedian vertelt vijf minuten over zijn jeugd, met veel woordspelingen. Bij welke soorten past dat?",
        opties=[
            "literair",
            "narratief",
            "prescriptief",
            "geen van de zeven soorten",
        ],
        antwoord=[0, 1],
        uitleg="Er wordt een verhaal verteld en er wordt bewust met taal gespeeld, dus narratief én literair.",
    ),
    dict(
        type="waarofniet",
        vraag="Propaganda en nepnieuws staan bij dezelfde tekstsoort als een reclamefilmpje.",
        antwoord=True,
        uitleg="Alle drie willen ze je beïnvloeden, dus alle drie zijn ze persuasief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de tekstsoort van een tekst over de betrouwbaarheid ervan?",
        opties=[
            "op zich niets, maar ze zet je wel op je hoede",
            "een informatieve tekst is altijd volledig betrouwbaar",
            "een persuasieve tekst bevat nooit juiste informatie",
            "enkel literaire teksten mag je zonder nakijken geloven",
        ],
        antwoord=0,
        uitleg="Een reclametekst kan kloppen en een krantenartikel kan fout zitten. De soort zegt wat de zender wil, niet of het waar is.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een folder van de gemeente legt uit hoe je je afval sorteert, met een schema per fractie. Welke soort is dat?",
        opties=[
            "prescriptief",
            "argumentatief",
            "opiniërend",
            "literair",
        ],
        antwoord=0,
        uitleg="Het zegt je wat je moet doen en in welke volgorde. Dat is voorschrijvend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een opiniestuk in de krant betoogt dat de schooluren later moeten beginnen, met cijfers uit slaaponderzoek. Welke soorten zitten erin?",
        opties=[
            "argumentatief",
            "opiniërend",
            "informatief",
            "prescriptief",
        ],
        antwoord=[0, 1, 2],
        uitleg="De schrijver geeft zijn mening, onderbouwt die met argumenten en brengt onderweg ook feiten aan. Hij schrijft je geen handeling voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een tekst feiten bevat, is hij daarom een informatieve tekst.",
        antwoord=False,
        uitleg="Ook reclame en propaganda zetten feiten in. Het doel van de zender bepaalt de soort, niet de aanwezigheid van feiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bekijkt een reportage over de haven van Antwerpen voor een spreekbeurt. Wat is je eerste vraag bij zo'n luistertekst?",
        opties=[
            "wie maakte de reportage en waarom",
            "hoeveel minuten de reportage precies duurt",
            "of er ondertitels beschikbaar zijn",
            "welke muziek er onder de beelden staat",
        ],
        antwoord=0,
        uitleg="Zender en doel komen eerst. Een reportage van de havenbedrijven zelf vertelt een ander verhaal dan een reportage van een milieugroep.",
    ),
    dict(
        type="invultekst",
        vraag="Een recept in een kookboek: welke tekstsoort is dat? Antwoord met één woord.",
        antwoord=["prescriptief", "prescriptieve"],
        uitleg="Het schrijft je stap voor stap voor hoe je iets klaarmaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gedicht over de dood van een grootvader raakt je. Bij welke soort hoort het?",
        opties=[
            "literair",
            "informatief",
            "prescriptief",
            "argumentatief",
        ],
        antwoord=0,
        uitleg="Literaire teksten hebben een esthetische waarde en spelen vaak in op emoties.",
    ),
    dict(
        type="waarofniet",
        vraag="Een strip kan een literaire tekst zijn.",
        antwoord=True,
        uitleg="Een strip staat uitdrukkelijk bij de voorbeelden van literaire teksten, net als een lied of stand-upcomedy.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag helpt je het best om een persuasieve tekst te herkennen?",
        opties=[
            "wat wil de zender dat ik doe of denk",
            "hoeveel alinea's telt deze tekst",
            "staan er moeilijke woorden in",
            "is de tekst recent gepubliceerd",
        ],
        antwoord=0,
        uitleg="Persuasief is een doel, geen vorm. Wie zich afvraagt wat de zender wil bereiken, heeft het snel door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een handleiding bij je telefoon en een schoolreglement hebben iets gemeen. Wat?",
        opties=[
            "ze zeggen allebei wat je moet doen",
            "ze vertellen allebei een verhaal",
            "ze geven allebei iemands mening",
            "ze bevatten allebei veel beeldspraak",
        ],
        antwoord=0,
        uitleg="Allebei prescriptief: ze schrijven handelingen of regels voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een interview is doorgaans een informatieve tekst.",
        antwoord=True,
        uitleg="Een interview brengt informatie over een onderwerp of over een persoon. Dat de ondervraagde ook meningen geeft, verandert het hoofddoel niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teksten kan je op het examen zowel lezen als beluisteren?",
        opties=[
            "een interview",
            "een gedicht",
            "een reclameboodschap",
            "geen enkele, een luistertekst is altijd anders",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dezelfde soort kan in beide vormen voorkomen. Een reportage beluister je, een krantenartikel lees je, en een interview kan allebei.",
    ),
    dict(
        type="invultekst",
        vraag="Een reactie op een discussieforum waarin iemand zegt wat hij ervan vindt: welke soort? Antwoord met één woord.",
        antwoord=["opiniërend", "opiniërende"],
        uitleg="Iemand geeft zijn mening, zonder die noodzakelijk met argumenten te onderbouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom raadt men aan om voor het examen veel verschillende tekstsoorten te lezen en te beluisteren?",
        opties=[
            "je leert de vorm en de bedoeling sneller herkennen",
            "je kent dan alle teksten die op het examen staan al",
            "je hoeft dan geen woordenboek meer te gebruiken",
            "je mag dan je eigen samenvatting meenemen",
        ],
        antwoord=0,
        uitleg="Ervaring met veel soorten maakt dat je vlugger ziet wat een tekst van je wil en hoe hij in elkaar zit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reisverslag en een handleiding horen bij dezelfde tekstsoort.",
        antwoord=False,
        uitleg="Een reisverslag vertelt wat er gebeurde en is narratief; een handleiding schrijft voor wat je moet doen en is prescriptief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een politieke partij publiceert op haar eigen site een artikel over hoe andere partijen de polarisatie aanwakkeren. Hoe lees je dat?",
        opties=[
            "als propaganda, want de zender heeft er belang bij",
            "als neutrale informatie, want het staat in artikelvorm",
            "als een literaire tekst, want het is overtuigend geschreven",
            "als een prescriptieve tekst, want het zegt wat we moeten vinden",
        ],
        antwoord=0,
        uitleg="De zender spreekt over zijn tegenstanders op zijn eigen kanaal. Dat is geen journalistiek maar partijcommunicatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een essay van een filosoof over vriendschap. Welke soorten kan je daarin aanwijzen?",
        opties=[
            "argumentatief",
            "literair",
            "opiniërend",
            "prescriptief",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een essay denkt hardop, onderbouwt, geeft een persoonlijke kijk en is vaak ook mooi geschreven. Het schrijft je geen handelingen voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een luistertekst gebruik je dezelfde vragen over zender, doel en publiek als bij een leestekst.",
        antwoord=True,
        uitleg="Het communicatiemodel werkt voor elke boodschap, gesproken of geschreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fabrikant van sportdrank laat een dokter in een filmpje uitleggen waarom je moet bijtanken. Wat valt op aan de zender?",
        opties=[
            "de dokter spreekt, maar de fabrikant is de echte zender",
            "een dokter in beeld maakt de boodschap wetenschappelijk",
            "de zender doet er niet toe zolang de informatie klopt",
            "er is geen zender, want het is een filmpje en geen tekst",
        ],
        antwoord=0,
        uitleg="Wie betaalt en wie spreekt zijn twee verschillende dingen. De autoriteit van de dokter wordt hier ingezet om te overtuigen.",
    ),
    dict(
        type="invultekst",
        vraag="Teksten die je informatie geven over een onderwerp, zoals een krantenartikel: welke soort? Antwoord met één woord.",
        antwoord=["informatief", "informatieve"],
        uitleg="Informeren is het hoofddoel van een krantenartikel, een reportage of een lemma in een naslagwerk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een column die grappig begint, een standpunt inneemt en eindigt met een oproep. Wat doe je met de soort?",
        opties=[
            "je noemt de doelen die je erin terugvindt",
            "je kiest het eerste doel dat je tegenkomt",
            "je besluit dat het geen van de zeven soorten is",
            "je laat de soort weg, want er is er maar één toegelaten",
        ],
        antwoord=0,
        uitleg="Zo'n tekst is literair, opiniërend en persuasief tegelijk. Dat benoemen is juister dan er één soort uit kiezen.",
    ),
]
