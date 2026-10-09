# -*- coding: utf-8 -*-
"""Maatschappelijke vraagstukken en de redeneeractiviteiten.

Het eerste van twee thema's over de onderzoekscyclus, het laatste blok van de
fiche. Dit thema gaat over de inhoud van de vraagstukken en over het schema
waarmee je erover redeneert; het volgende over het onderzoek zelf.

De lijstjes staan letterlijk in de fiche:

    maatschappelijke vraagstukken: arbeid, diversiteit, individualisering,
        kansenongelijkheid, klimaat, media, migratie, mobiliteit, onderwijs,
        privacy, rationalisering, samenlevingsvormen
    invalshoeken bij het beschrijven: economisch, sociaal, cultureel,
        politiek, juridisch
    schema redeneeractiviteiten (staat in de bijlage van de fiche)
        1. een maatschappelijk probleem beschrijven
        2. een maatschappelijk probleem verklaren
        3. creatieve ideeën genereren
        4. oplossingen evalueren
        bij elke stap: redeneren met bewijs
    criteria om de uitvoerbaarheid van een oplossing te beoordelen: tijd,
        middelen, ethische principes, duurzaamheidsprincipes

De bijlage met het schema krijgt het kind volgens de fiche niet op het examen:
ze is er om mee voor te bereiden. De redeneeractiviteiten zelf worden wel
gevraagd, dus ze zitten hier in de vragen.

Deel 1 zijn de vraagstukken en de invalshoeken.
Deel 2 zijn de vier redeneeractiviteiten en het redeneren met bewijs.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een maatschappelijk vraagstuk?",
        opties=[
            "een probleem dat een hele samenleving aangaat",
            "een probleem van één persoon of één gezin",
            "een vraag die met een opzoeking opgelost is",
            "een vraag waarop maar één antwoord bestaat",
        ],
        antwoord=0,
        uitleg="Een maatschappelijk vraagstuk raakt veel mensen, heeft meerdere oorzaken en er zijn verschillende standpunten over mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderwerpen noemt de fiche als maatschappelijk vraagstuk?",
        opties=[
            "kansenongelijkheid",
            "migratie",
            "privacy",
            "persoonlijkheid",
            "conditionering",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt twaalf vraagstukken. Persoonlijkheid en conditionering zijn begrippen uit de gedragswetenschappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent individualisering als maatschappelijk vraagstuk?",
        opties=[
            "mensen maken hun eigen weg, losser van vaste groepen",
            "mensen gaan steeds meer in groepen samenwonen",
            "mensen trekken zich volledig uit de samenleving terug",
            "mensen worden steeds meer door de overheid gestuurd",
        ],
        antwoord=0,
        uitleg="Individualisering betekent dat tradities, kerk en buurt minder vastleggen hoe iemand leeft. Dat geeft vrijheid en ook onzekerheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent rationalisering als maatschappelijk vraagstuk?",
        opties=[
            "steeds meer wordt geregeld volgens regels en doelmatigheid",
            "steeds meer wordt geregeld volgens gewoonte en traditie",
            "steeds meer mensen gaan rationeel denken over geloof",
            "steeds minder beslissingen worden met cijfers onderbouwd",
        ],
        antwoord=0,
        uitleg="Rationalisering is dat berekening, procedures en techniek steeds meer het werk organiseren. Het maakt dingen efficiënt en ook onpersoonlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invalshoeken noemt de fiche om een maatschappelijk probleem te beschrijven?",
        opties=[
            "de economische invalshoek",
            "de politieke invalshoek",
            "de juridische invalshoek",
            "de biologische invalshoek",
            "de wiskundige invalshoek",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vijf invalshoeken zijn economisch, sociaal, cultureel, politiek en juridisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand bekijkt het woningprobleem door te kijken naar de huurprijzen en de bouwkosten. Welke invalshoek is dit?",
        opties=[
            "de economische invalshoek",
            "de sociale invalshoek",
            "de juridische invalshoek",
            "de culturele invalshoek",
        ],
        antwoord=0,
        uitleg="Prijzen, kosten en markt horen bij de economische invalshoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand bekijkt het woningprobleem door te kijken naar de rechten van huurders in de wet. Welke invalshoek is dit?",
        opties=[
            "de juridische invalshoek",
            "de politieke invalshoek",
            "de economische invalshoek",
            "de sociale invalshoek",
        ],
        antwoord=0,
        uitleg="Wetten, rechten en rechtspraak horen bij de juridische invalshoek. De politieke invalshoek kijkt naar wie beslist en met welk programma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand bekijkt het woningprobleem door te kijken naar wie met wie samenwoont en wie alleen achterblijft. Welke invalshoek is dit?",
        opties=[
            "de sociale invalshoek",
            "de economische invalshoek",
            "de culturele invalshoek",
            "de juridische invalshoek",
        ],
        antwoord=0,
        uitleg="Relaties, groepen en wie erbij hoort of buiten valt, horen bij de sociale invalshoek.",
    ),
    dict(
        type="invultekst",
        vraag="Een vraagstuk bekijken vanuit de wet en de rechtspraak is de ... invalshoek.",
        antwoord=["juridische", "juridisch"],
        uitleg="De juridische invalshoek. De vijf zijn economisch, sociaal, cultureel, politiek en juridisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een maatschappelijk vraagstuk kan je het best vanuit meerdere invalshoeken beschrijven.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk verschillende invalshoeken te gebruiken en standpunten aan die invalshoeken te koppelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een maatschappelijk vraagstuk is een probleem voor alle mensen in gelijke mate.",
        antwoord=False,
        uitleg="Niet waar. De fiche vraagt juist te beschrijven voor wie het een probleem is. Wat voor de ene een probleem is, is voor de andere een voordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent diversiteit als maatschappelijk vraagstuk?",
        opties=[
            "samenleven met verschillen in taal, geloof, afkomst en meer",
            "samenleven met mensen uit precies dezelfde groep",
            "het aantal mensen dat naar een land migreert",
            "het aantal talen dat op school wordt gegeven",
        ],
        antwoord=0,
        uitleg="Diversiteit gaat over de verschillen die in een samenleving aanwezig zijn, en over hoe je er samen vorm aan geeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent samenlevingsvormen als maatschappelijk vraagstuk?",
        opties=[
            "de manieren waarop mensen samen een huishouden vormen",
            "de manieren waarop landen met elkaar samenwerken",
            "de manieren waarop een school wordt bestuurd",
            "de manieren waarop media mensen verbinden",
        ],
        antwoord=0,
        uitleg="Huwelijk, samenwonen, alleenstaand, nieuw samengesteld gezin, co-ouderschap: de vormen zijn de laatste decennia sterk veranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat media zelf ook in de lijst van maatschappelijke vraagstukken?",
        opties=[
            "omdat de invloed van media zelf een vraagstuk geworden is",
            "omdat media over alle andere vraagstukken berichten",
            "omdat media geen enkele invloed meer hebben",
            "omdat media enkel over politiek berichten",
        ],
        antwoord=0,
        uitleg="Beeldvorming, desinformatie, schermtijd en de macht van platformen zijn vandaag zelf onderwerp van debat en van beleid.",
    ),
    dict(
        type="invultekst",
        vraag="Het vraagstuk over hoe losser mensen van vaste groepen en tradities hun eigen weg maken, heet ...",
        antwoord=["individualisering"],
        uitleg="Individualisering. Rationalisering is iets anders: dat gaat over regels, berekening en doelmatigheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De lijst van maatschappelijke vraagstukken in de fiche eindigt met drie puntjes, en is dus niet volledig.",
        antwoord=True,
        uitleg="Waar. De fiche zet er zelf puntjes achter. Er kan dus ook een vraagstuk komen dat niet met naam in de lijst staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaat staat niet in de lijst van maatschappelijke vraagstukken van de fiche.",
        antwoord=False,
        uitleg="Niet waar, klimaat staat er wel in, naast onder meer arbeid, migratie, mobiliteit en onderwijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand bekijkt het klimaatvraagstuk door te kijken naar wat mensen gewoon zijn te eten en hoe ze reizen. Welke invalshoek is dit?",
        opties=[
            "de culturele invalshoek",
            "de economische invalshoek",
            "de juridische invalshoek",
            "de politieke invalshoek",
        ],
        antwoord=0,
        uitleg="Gewoonten, waarden en wat normaal gevonden wordt, horen bij de culturele invalshoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche om standpunten aan invalshoeken te koppelen?",
        opties=[
            "omdat je dan ziet waarom mensen van mening verschillen",
            "omdat je dan weet welk standpunt het juiste is",
            "omdat elk standpunt maar één invalshoek kent",
            "omdat je dan geen bronnen meer nodig hebt",
        ],
        antwoord=0,
        uitleg="Wie vanuit de economie kijkt, komt bij een andere conclusie dan wie vanuit het recht kijkt. Dat maakt het meningsverschil begrijpelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is kansenongelijkheid een vraagstuk dat in dit vak zo vaak terugkomt?",
        opties=[
            "omdat het met stratificatie, mobiliteit en onderwijs samenhangt",
            "omdat het alleen met het onderwijs te maken heeft",
            "omdat het met de gedragswetenschappen samenhangt",
            "omdat het in de fiche het enige vraagstuk is",
        ],
        antwoord=0,
        uitleg="Het thema loopt door het hele blok sociale wetenschappen: de lagen, de beweging ertussen, het matheüseffect en de rol van de school.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel redeneeractiviteiten staan in het schema van de fiche?",
        opties=[
            "vier",
            "drie",
            "vijf",
            "zes",
        ],
        antwoord=0,
        uitleg="Vier: beschrijven, verklaren, creatieve ideeën genereren en oplossingen evalueren. Bij elke stap hoort redeneren met bewijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij het beschrijven van een maatschappelijk probleem?",
        opties=[
            "voor wie, waarom, waar en hoe het ontstaan is",
            "welke oplossing er het best bij past",
            "welke oorzaken je kan aanwijzen",
            "welke ideeën je zelf kan verzinnen",
        ],
        antwoord=0,
        uitleg="Beschrijven is de context in kaart brengen: voor wie het een probleem is, waarom, waar het speelt en wat de ontstaansgeschiedenis is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij het verklaren van een maatschappelijk probleem?",
        opties=[
            "meerdere oorzaken aanbrengen en ze indelen per invalshoek",
            "één duidelijke oorzaak aanwijzen en de rest weglaten",
            "de context en de geschiedenis in kaart brengen",
            "de uitvoerbaarheid van een oplossing beoordelen",
        ],
        antwoord=0,
        uitleg="Verklaren vraagt meerdere oorzaken, en die oorzaken kan je ordenen volgens de vijf invalshoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de derde redeneeractiviteit?",
        opties=[
            "creatieve ideeën genereren",
            "oplossingen evalueren",
            "het probleem beschrijven",
            "het probleem verklaren",
        ],
        antwoord=0,
        uitleg="Pas na beschrijven en verklaren komt het verzinnen van ideeën, met technieken om ideeën te maken en om er daarna uit te kiezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij het evalueren van oplossingen?",
        opties=[
            "ook de ongewenste gevolgen van een aanpak benoemen",
            "enkel de voordelen van een aanpak opsommen",
            "de oorzaken van het probleem opsommen",
            "de ontstaansgeschiedenis beschrijven",
        ],
        antwoord=0,
        uitleg="Elke oplossing heeft neveneffecten. De fiche vraagt die uitdrukkelijk te benoemen en af te leiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke criteria beoordeel je volgens de fiche of een oplossing uitvoerbaar is?",
        opties=[
            "de tijd en de middelen",
            "de ethische principes",
            "de duurzaamheidsprincipes",
            "het aantal betrokkenen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vier criteria zijn tijd, middelen, ethische principes en duurzaamheidsprincipes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent redeneren met bewijs?",
        opties=[
            "je uitspraken met bronnen en data onderbouwen",
            "je uitspraken met je eigen ervaring onderbouwen",
            "je uitspraken zonder bronnen doen",
            "je uitspraken aan één bron ophangen",
        ],
        antwoord=0,
        uitleg="De fiche vraagt meerdere bronnen in te zetten en te vergelijken, met de criteria van betrouwbare en valide data erbij.",
    ),
    dict(
        type="invultekst",
        vraag="Een oplossing beoordelen op tijd, middelen, ethiek en duurzaamheid is de ... van oplossingen.",
        antwoord=["evaluatie", "evalueren"],
        uitleg="Het evalueren van oplossingen, de vierde redeneeractiviteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens het schema komt het verzinnen van oplossingen pas na het beschrijven en het verklaren.",
        antwoord=True,
        uitleg="Waar. Wie meteen naar oplossingen springt, lost vaak het verkeerde probleem op.",
    ),
    dict(
        type="waarofniet",
        vraag="Het schema met de redeneeractiviteiten krijgt het kind volgens de fiche op het examen zelf ter beschikking.",
        antwoord=False,
        uitleg="Niet waar. De fiche zegt uitdrukkelijk dat de bijlage met dat schema niet op het examen gegeven wordt. De zes criteria van een onderzoeksvraag wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling schrijft over de files: het probleem speelt vooral rond de grote steden en is sinds de jaren tachtig gegroeid. Welke redeneeractiviteit is dit?",
        opties=[
            "het probleem beschrijven",
            "het probleem verklaren",
            "ideeën genereren",
            "oplossingen evalueren",
        ],
        antwoord=0,
        uitleg="Waar het speelt en hoe het gegroeid is, horen bij de beschrijving van de context en de ontstaansgeschiedenis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling schrijft over de files: er zijn drie oorzaken, en twee ervan zijn economisch en een is juridisch. Welke redeneeractiviteit is dit?",
        opties=[
            "het probleem verklaren",
            "het probleem beschrijven",
            "ideeën genereren",
            "oplossingen evalueren",
        ],
        antwoord=0,
        uitleg="Oorzaken aanbrengen en ze per invalshoek indelen, is precies wat verklaren inhoudt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling schrijft over de files: rekeningrijden zou werken, maar het raakt mensen zonder alternatief het hardst. Welke redeneeractiviteit is dit?",
        opties=[
            "oplossingen evalueren",
            "ideeën genereren",
            "het probleem verklaren",
            "het probleem beschrijven",
        ],
        antwoord=0,
        uitleg="Een oplossing afwegen met haar ongewenste gevolgen, en met een ethisch principe erbij, is evalueren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een ideegeneratietechniek en een ideeselectietechniek?",
        opties=[
            "de eerste maakt ideeën, de tweede kiest eruit",
            "de eerste kiest ideeën, de tweede maakt ze",
            "de eerste geldt voor groepen, de tweede voor personen",
            "de eerste gebruikt bronnen, de tweede niet",
        ],
        antwoord=0,
        uitleg="Eerst zo veel mogelijk ideeën op tafel, zonder te beoordelen. Daarna pas kiezen met criteria. Dat zijn twee verschillende stappen.",
    ),
    dict(
        type="invultekst",
        vraag="De eerste redeneeractiviteit van het schema is het ... van een maatschappelijk probleem.",
        antwoord=["beschrijven", "beschrijving"],
        uitleg="Het beschrijven. Daarna volgen verklaren, ideeën genereren en oplossingen evalueren.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het evalueren van een oplossing vraagt de fiche ook naar verschillende perspectieven van betrokkenen.",
        antwoord=True,
        uitleg="Waar. Oplossingen herkennen en daarbij verschillende perspectieven onderscheiden, staat er met zoveel woorden.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén goede bron volstaat volgens de fiche om een uitspraak over een vraagstuk te onderbouwen.",
        antwoord=False,
        uitleg="Niet waar. De fiche vraagt meerdere bronnen in te zetten en met elkaar te vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling wil een idee beoordelen op duurzaamheid. Welke vraag past daarbij?",
        opties=[
            "houdt deze oplossing ook over tien jaar nog stand?",
            "hoeveel kost deze oplossing vandaag?",
            "hoeveel mensen vinden deze oplossing goed?",
            "hoe snel kan deze oplossing ingevoerd worden?",
        ],
        antwoord=0,
        uitleg="Duurzaamheid vraagt naar de lange termijn en naar wat een oplossing achterlaat. Kosten en snelheid horen bij middelen en tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorgestelde maatregel zou werken maar raakt één groep onevenredig hard. Welk criterium weegt hier?",
        opties=[
            "de ethische principes",
            "de tijd",
            "de middelen",
            "de duurzaamheidsprincipes",
        ],
        antwoord=0,
        uitleg="De vraag of een maatregel rechtvaardig is tegenover alle betrokkenen, hoort bij de ethische principes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat redeneren met bewijs bij élke stap van het schema en niet alleen bij de laatste?",
        opties=[
            "omdat ook een beschrijving en een oorzaak onderbouwd moeten zijn",
            "omdat alleen oplossingen bronnen nodig hebben",
            "omdat bronnen alleen bij het evalueren tellen",
            "omdat een beschrijving nooit fout kan zijn",
        ],
        antwoord=0,
        uitleg="Een verkeerde beschrijving of een verzonnen oorzaak leidt tot een verkeerde oplossing. Daarom hoort bewijs bij elke stap.",
    ),
]
