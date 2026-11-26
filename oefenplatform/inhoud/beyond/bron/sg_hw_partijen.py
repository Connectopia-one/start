# -*- coding: utf-8 -*-
"""Humane wetenschappen: ideologieën, breuklijnen, partijen en verkiezingen.

Het derde van zes thema's over politieke wetenschappen, enkel voor humane
wetenschappen (fiche 3DDO, onderdeel "Belgische politiek", tweede helft).

De fiche vraagt:

    de begrippen ideologie en breuklijn
    de historische breuklijnen die tegenstellingen in taal, economie,
        ideologie en identiteit weerspiegelen
    de kernideeën van de Vlaamse politieke partijen, tot welke ideologie ze
        behoren, en waar ze op het links-rechtsassenstelsel staan
    het verkiezingsproces analyseren: identificatie (bestuursniveau), actoren
        (partijen, kiezers, media, belangenorganisaties), informatie
        (peilingen, campagne-uitingen, debatten), mechanismen (kieswetgeving,
        stemprocedure, campagnefinanciering), verkiezingsresultaat (winnaars
        en verliezers, regeringsvorming, coalitie en oppositie, veranderende
        machtsverhoudingen), politieke verschuivingen

Neutraliteit: de partijen worden beschreven met de ideologie waartoe ze
gewoonlijk gerekend worden en met hun kernideeën in algemene woorden, zonder
oordeel. De plaats op de links-rechtsas is een gangbare, ruwe indeling; een
partij kan per thema anders staan. Dat staat ook in de uitleg.

Deel 1 zijn ideologie, breuklijnen en de partijen.
Deel 2 zijn het verkiezingsproces en de uitslag.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een ideologie?",
        opties=[
            "een samenhangend geheel van ideeën over hoe de samenleving eruit moet zien",
            "een wet die het parlement goedkeurt over de werking van alle partijen",
            "een peiling die voorspelt hoeveel stemmen een partij zal halen",
            "de plaats waar een partij haar hoofdkwartier en haar kantoren heeft",
        ],
        antwoord=0,
        uitleg="Liberalisme, socialisme en ecologisme zijn voorbeelden. Een ideologie geeft een visie op mens en samenleving en richting aan politieke keuzes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een breuklijn in de politiek?",
        opties=[
            "een blijvende tegenstelling in de samenleving waarrond partijen zich vormen",
            "het moment waarop een regering ontslag neemt en er verkiezingen komen",
            "de grens tussen twee kieskringen op de kaart van een Belgische provincie",
            "een ruzie tussen twee politici van dezelfde partij over een voorstel",
        ],
        antwoord=0,
        uitleg="Een breuklijn deelt de samenleving in twee kampen met tegengestelde belangen of waarden. In België ontstonden veel partijen langs zulke breuklijnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke breuklijn hoort bij de tegenstelling tussen arbeid en kapitaal?",
        opties=[
            "de sociaal-economische breuklijn",
            "de levensbeschouwelijke breuklijn",
            "de communautaire breuklijn",
            "de breuklijn tussen stad en platteland",
        ],
        antwoord=0,
        uitleg="Werknemers en werkgevers hebben andere economische belangen. Uit die tegenstelling groeiden onder meer de socialistische partijen en de vakbonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke breuklijn hoort bij de tegenstelling tussen kerk en staat?",
        opties=[
            "de levensbeschouwelijke breuklijn",
            "de sociaal-economische breuklijn",
            "de communautaire breuklijn",
            "de ecologische breuklijn",
        ],
        antwoord=0,
        uitleg="Katholieken en vrijzinnigen streden lang over de rol van de kerk, bijvoorbeeld in het onderwijs. Dat is de levensbeschouwelijke of ideologische breuklijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke breuklijn hoort bij de tegenstelling tussen Nederlandstaligen en Franstaligen?",
        opties=[
            "de communautaire breuklijn",
            "de sociaal-economische breuklijn",
            "de levensbeschouwelijke breuklijn",
            "de generatiebreuklijn",
        ],
        antwoord=0,
        uitleg="De communautaire breuklijn gaat over taal en identiteit. Ze leidde tot de staatshervormingen en tot partijen die zich per taalgroep organiseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ideologie legt de nadruk op de vrijheid van het individu en een beperkte rol voor de overheid in de economie?",
        opties=["het liberalisme", "het socialisme", "het ecologisme", "de christendemocratie"],
        antwoord=0,
        uitleg="Liberalen vinden dat mensen zo vrij mogelijk moeten kunnen kiezen en ondernemen, met een overheid die niet te veel ingrijpt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ideologie legt de nadruk op gelijkheid en solidariteit, met een sterke rol voor de overheid?",
        opties=["het socialisme", "het liberalisme", "het nationalisme", "het conservatisme"],
        antwoord=0,
        uitleg="Socialisten willen ongelijkheid verkleinen, onder meer via sociale zekerheid, openbare diensten en de rechten van werknemers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ideologie plaatst de zorg voor milieu, klimaat en toekomstige generaties centraal?",
        opties=["het ecologisme", "het liberalisme", "het nationalisme", "de christendemocratie"],
        antwoord=0,
        uitleg="Ecologisten willen dat de samenleving binnen de grenzen van de natuur blijft en dat ook latere generaties goed kunnen leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ideologie vertrekt van het eigen volk of de eigen natie als belangrijkste gemeenschap?",
        opties=["het nationalisme", "het ecologisme", "het socialisme", "het liberalisme"],
        antwoord=0,
        uitleg="Nationalisten vinden dat een volk met een eigen taal en cultuur zoveel mogelijk zelf moet beslissen. In Vlaanderen spreekt men van Vlaams-nationalisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke ideologie wordt cd&v gewoonlijk gerekend?",
        opties=["de christendemocratie", "het liberalisme", "het ecologisme", "het Vlaams-nationalisme"],
        antwoord=0,
        uitleg="cd&v groeide uit de katholieke partij en vertrekt van christelijke waarden, met aandacht voor het gezin, het middenveld en verbondenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee Vlaamse partijen worden gewoonlijk tot het Vlaams-nationalisme gerekend?",
        opties=[
            "N-VA en Vlaams Belang",
            "Vooruit en Groen",
            "cd&v en Open Vld",
            "PVDA en Vooruit",
        ],
        antwoord=0,
        uitleg="Beide partijen willen meer zelfbestuur voor Vlaanderen. N-VA wordt meestal centrumrechts genoemd, Vlaams Belang radicaal-rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke partij wordt op de links-rechtsas gewoonlijk het verst links geplaatst?",
        opties=["PVDA", "Vooruit", "cd&v", "Open Vld"],
        antwoord=0,
        uitleg="PVDA is een radicaal-linkse partij met marxistische wortels. Vooruit en Groen staan ook links, cd&v in het centrum en Open Vld, N-VA en Vlaams Belang rechts. Die indeling is ruw: per thema kan een partij anders staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar gaat de links-rechtsas vooral over, als je het over economie hebt?",
        opties=[
            "over hoeveel de overheid moet ingrijpen om welvaart te herverdelen",
            "over de vraag of een partij uit Vlaanderen of uit Wallonië komt",
            "over het aantal zetels dat een partij in het parlement heeft",
            "over de leeftijd van de leden en de kiezers van een partij",
        ],
        antwoord=0,
        uitleg="Links wil meer herverdeling en een sterke overheid, rechts meer vrije markt en minder belastingen. Bij thema's zoals migratie of ethiek spreekt men ook van progressief en conservatief.",
    ),
    dict(
        type="invultekst",
        vraag="Een blijvende tegenstelling in de samenleving waarrond partijen ontstaan, noem je een ...",
        antwoord=["breuklijn"],
        uitleg="De drie klassieke breuklijnen in België zijn levensbeschouwelijk, sociaal-economisch en communautair.",
    ),
    dict(
        type="waarofniet",
        vraag="Veel Belgische partijen zijn ontstaan rond een historische breuklijn in de samenleving.",
        antwoord=True,
        uitleg="De katholieke en liberale partijen ontstonden rond kerk en staat, de socialistische rond arbeid en kapitaal, en de Vlaams-nationale rond de taalkwestie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een partij staat bij elk thema altijd op precies dezelfde plaats van de links-rechtsas.",
        antwoord=False,
        uitleg="Een partij kan economisch eerder rechts zijn en bij ethische thema's progressief, of omgekeerd. De as is dus een vereenvoudiging.",
    ),
    dict(
        type="waarofniet",
        vraag="Groen wordt gewoonlijk tot het ecologisme gerekend.",
        antwoord=True,
        uitleg="Groen zet klimaat, milieu en duurzaamheid voorop, samen met sociale rechtvaardigheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Open Vld wordt gewoonlijk tot het socialisme gerekend.",
        antwoord=False,
        uitleg="Open Vld is een liberale partij. Vooruit is de Vlaamse partij uit de socialistische traditie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke ideologische traditie komt Vooruit?",
        opties=["de sociaaldemocratie", "het liberalisme", "de christendemocratie", "het Vlaams-nationalisme"],
        antwoord=0,
        uitleg="Vooruit heette vroeger sp.a en daarvoor BSP. De partij zet in op sociale zekerheid, werk en gelijke kansen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partij zegt: \"Iedereen moet zo vrij mogelijk zijn eigen leven kunnen leiden. Lagere belastingen geven ondernemers ademruimte.\" Bij welke ideologie past die uitspraak het best?",
        opties=["het liberalisme", "het socialisme", "het ecologisme", "het communisme"],
        antwoord=0,
        uitleg="Individuele vrijheid en een overheid die niet te veel neemt of regelt, zijn kernideeën van het liberalisme.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn actoren in een verkiezingsproces?",
        opties=[
            "de politieke partijen",
            "de kiezers",
            "de media",
            "de belangenorganisaties",
            "het Hof van Cassatie",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="Partijen, kiezers, media en belangenorganisaties spelen allemaal een rol bij verkiezingen. Het Hof van Cassatie heeft daar geen rol in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een peiling?",
        opties=[
            "een onderzoek bij een groep kiezers om te schatten hoe er gestemd zal worden",
            "de officiële telling van alle stemmen na de sluiting van de stembureaus",
            "een debat op televisie tussen de voorzitters van de grote partijen",
            "de wet die bepaalt hoeveel geld een partij aan campagne mag uitgeven",
        ],
        antwoord=0,
        uitleg="Een peiling is een momentopname bij een steekproef. Ze kan kiezers beïnvloeden, maar is nooit de echte uitslag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn mechanismen die het verloop van verkiezingen regelen?",
        opties=[
            "de kieswetgeving",
            "de stemprocedure",
            "de regels over campagnefinanciering",
            "de peilingen in de krant",
            "de affiches van de partijen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kieswetgeving, stemprocedure en campagnefinanciering zijn regels. Peilingen en affiches zijn informatie die tijdens de campagne verspreid wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn er regels over campagnefinanciering?",
        opties=[
            "zodat partijen met veel geld de verkiezingen niet kunnen kopen",
            "zodat kiezers weten op welk uur het stembureau opengaat",
            "zodat elke partij evenveel zetels krijgt in het parlement",
            "zodat de media geen verslag mogen uitbrengen van de campagne",
        ],
        antwoord=0,
        uitleg="Er zijn grenzen aan wat een partij mag uitgeven en ontvangen. Zo blijven de kansen eerlijker en is duidelijker wie een partij steunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de identificatie van een verkiezing?",
        opties=[
            "nagaan voor welk bestuursniveau er gestemd wordt",
            "nagaan welke partij de meeste affiches ophing",
            "nagaan welke peiling het dichtst bij de uitslag zat",
            "nagaan hoeveel debatten er op televisie waren",
        ],
        antwoord=0,
        uitleg="Eerst bepaal je welke verkiezing het is: gemeenteraad, provincieraad, Vlaams Parlement, Kamer of Europees Parlement.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de weken voor de verkiezingen organiseert een televisiezender elke avond een debat tussen de lijsttrekkers. Onder welk criterium valt dat?",
        opties=["informatie", "mechanismen", "identificatie", "verkiezingsresultaat"],
        antwoord=0,
        uitleg="Peilingen, campagne-uitingen en debatten zijn de informatie waarmee kiezers zich een mening vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werkgeversorganisatie stuurt al haar leden een lijst met de standpunten van alle partijen over belastingen. Welke actor is hier aan het werk?",
        opties=["een belangenorganisatie", "een politieke partij", "de kieswetgever", "een controleorgaan"],
        antwoord=0,
        uitleg="Werkgeversorganisaties, vakbonden en milieuverenigingen zijn belangenorganisaties. Ze proberen de keuze van kiezers en partijen te beïnvloeden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er meestal na federale verkiezingen in België, voor er een nieuwe regering is?",
        opties=[
            "de partijen onderhandelen over een coalitie en een regeerakkoord",
            "de grootste partij vormt meteen alleen de nieuwe regering",
            "de koning kiest zelf de ministers zonder de partijen te horen",
            "er komt een tweede stemronde tussen de twee grootste partijen",
        ],
        antwoord=0,
        uitleg="Omdat geen partij alleen een meerderheid heeft, zoeken partijen samen een akkoord. Die regeringsvorming duurt in België soms erg lang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Partij A gaat van 12 naar 20 zetels, partij B van 18 naar 11. Wat zie je hier?",
        opties=[
            "een politieke verschuiving, met een winnaar en een verliezer",
            "een coalitie tussen partij A en partij B na de verkiezingen",
            "een verandering in de kieswetgeving tussen twee verkiezingen",
            "een bewijs dat de peilingen vooraf helemaal fout waren",
        ],
        antwoord=0,
        uitleg="Partij A wint acht zetels en partij B verliest er zeven. De machtsverhoudingen veranderen, en dat kan gevolgen hebben voor de regeringsvorming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Na de verkiezingen van 9 juni 2024 werd N-VA de grootste partij in de Kamer, met 24 van de 150 zetels. Wat volgt daaruit?",
        opties=[
            "N-VA had andere partijen nodig om samen een meerderheid te halen",
            "N-VA kon alleen een regering vormen, want ze was de grootste partij",
            "N-VA moest volgens de grondwet in de oppositie gaan zitten",
            "N-VA kreeg automatisch de helft van de ministers in de regering",
        ],
        antwoord=0,
        uitleg="Voor een meerderheid in de Kamer heb je minstens 76 van de 150 zetels. Met 24 zetels moest N-VA dus samenwerken met andere partijen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel zetels heb je minstens nodig voor een meerderheid in de Kamer van 150 zetels?",
        opties=["76", "75", "100", "51"],
        antwoord=0,
        uitleg="De helft van 150 is 75. Een meerderheid is meer dan de helft, dus minstens 76 zetels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maken structurele breuklijnen een regeringsvorming in België vaak moeilijk?",
        opties=[
            "partijen moeten akkoorden vinden over tegenstellingen in economie, geloof en taal",
            "de grondwet verbiedt dat partijen van verschillende ideologieën samenwerken",
            "de breuklijnen zorgen ervoor dat er in België geen verkiezingen kunnen plaatsvinden",
            "partijen mogen pas onderhandelen als alle peilingen hetzelfde tonen",
        ],
        antwoord=0,
        uitleg="Een coalitie moet partijen verzoenen die op verschillende breuklijnen tegenover elkaar staan. Bovendien zitten er volgens de grondwet in de federale regering, de eerste minister niet meegerekend, evenveel Nederlandstalige als Franstalige ministers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een linkse en een rechtse partij zitten samen in de regering. De linkse partij wil een vermogensbelasting, de rechtse wil minder belastingen. Wat is het meest waarschijnlijke gevolg?",
        opties=[
            "lang onderhandelen en een compromis, of de beslissing uitstellen",
            "de grootste partij beslist alleen en de andere partij volgt",
            "de rechter beslist welke van de twee partijen gelijk heeft",
            "de regering vraagt de Europese Commissie om te beslissen",
        ],
        antwoord=0,
        uitleg="Verschillen tussen links en rechts kunnen tot beleidsconflicten en vertraging leiden. In een coalitie zoekt men dan een compromis.",
    ),
    dict(
        type="invultekst",
        vraag="Een onderzoek bij een groep kiezers om te schatten hoe er gestemd zal worden, heet een ...",
        antwoord=["peiling", "opiniepeiling"],
        uitleg="Een peiling is een momentopname, met een foutenmarge. De echte uitslag kan anders zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="De grootste partij na de verkiezingen komt in België altijd in de regering.",
        antwoord=False,
        uitleg="De partijen die samen een meerderheid vinden, vormen de regering. Het kan dat de grootste partij in de oppositie belandt.",
    ),
    dict(
        type="waarofniet",
        vraag="Media spelen een rol in het verkiezingsproces, onder meer door debatten en berichtgeving over de campagne.",
        antwoord=True,
        uitleg="Media zijn een van de actoren. Ze geven informatie, organiseren debatten en bepalen mee welke thema's aandacht krijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een peiling is hetzelfde als de officiële verkiezingsuitslag.",
        antwoord=False,
        uitleg="Een peiling is een schatting vooraf bij een steekproef. De uitslag is de telling van alle echte stemmen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een partij veel zetels wint, kunnen de politieke machtsverhoudingen in het parlement veranderen.",
        antwoord=True,
        uitleg="Meer zetels betekent meer gewicht bij stemmingen en bij de regeringsvorming. Dat noem je een politieke verschuiving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk om bij een verkiezingsuitslag naar de zetels te kijken en niet enkel naar de stemmen?",
        opties=[
            "de zetels bepalen hoeveel gewicht een partij heeft bij stemmingen",
            "de stemmen worden na de verkiezingen niet meer bekendgemaakt aan het publiek",
            "de zetels tonen hoeveel leden een partij heeft betaald voor hun lidkaart",
            "de stemmen tellen enkel mee voor de verkiezingen van de gemeenteraad",
        ],
        antwoord=0,
        uitleg="Stemmen worden omgezet in zetels. Het zijn de verkozenen op die zetels die in het parlement stemmen en een meerderheid vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een regeerakkoord?",
        opties=[
            "de afspraken die de coalitiepartijen maken over wat de regering zal doen",
            "de lijst met alle kandidaten die een partij voorstelt bij de verkiezingen",
            "het vonnis van een rechter over een conflict tussen twee partijen",
            "de uitslag van de verkiezingen zoals de overheid die bekendmaakt",
        ],
        antwoord=0,
        uitleg="In het regeerakkoord staan de plannen en compromissen van de partijen die samen regeren. Het is de leidraad voor de nieuwe regering.",
    ),
]
