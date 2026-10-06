# -*- coding: utf-8 -*-
"""De vragen voor "Economische groei, welvaart en welzijn" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"economische groei", tweede stuk: de oorzaken van groei en de gevolgen ervan
voor welvaart en welzijn. Het rekenwerk met het bbp staat in [[ec_bbp]].

Deel 1 gaat over de vier oorzaken die de fiche opsomt: productiviteit en
technologische ontwikkeling, kapitaalvorming, bevolkingsgroei en onderwijs.
Deel 2 gaat over welvaart en welzijn: wat het verschil is, en welke positieve
en negatieve effecten groei op allebei heeft.

Afspraak in dit thema: welvaart gaat altijd over de mate waarin behoeften met
schaarse middelen voldaan worden, welzijn over hoe goed mensen zich voelen.
Die twee worden nooit door elkaar gebruikt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt een econoom met economische groei?",
        opties=[
            "Een toename van de productie van goederen en diensten in een land",
            "Een stijging van de prijzen van goederen en diensten in een land",
            "Een toename van het aantal bedrijven dat in een land gevestigd is",
            "Een stijging van het spaargeld dat de gezinnen op de bank hebben",
        ],
        antwoord=0,
        uitleg="Economische groei is meer productie, gemeten met het reële bbp. Prijsstijging is inflatie, en dat is iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn oorzaken van economische groei? Duid alles aan wat juist is.",
        opties=[
            "Productiviteit en technologische ontwikkeling",
            "Kapitaalvorming",
            "Bevolkingsgroei en onderwijs",
            "Een stijging van de prijzen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vier oorzaken: productiviteit en technologie, kapitaalvorming, bevolkingsgroei en onderwijs. Een prijsstijging maakt de economie niet groter, alleen duurder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is arbeidsproductiviteit?",
        opties=[
            "De productie per werknemer of per gewerkt uur",
            "Het aantal werknemers dat in een bedrijf werkt",
            "Het loon dat een werknemer per uur verdient",
            "Het aantal uren dat een werknemer per week werkt",
        ],
        antwoord=0,
        uitleg="Productiviteit meet hoeveel er per eenheid arbeid geproduceerd wordt. Stijgt ze, dan maak je met evenveel mensen meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakkerij bakt met 4 werknemers 800 broden per dag, en na een nieuwe oven 1 000 broden met dezelfde 4 werknemers. Wat gebeurde er?",
        opties=[
            "De arbeidsproductiviteit steeg van 200 naar 250 broden",
            "De arbeidsproductiviteit bleef gelijk, want er kwam niemand bij",
            "De arbeidsproductiviteit daalde, want de oven deed het werk",
            "De arbeidsproductiviteit steeg van 800 naar 1 000 broden",
        ],
        antwoord=0,
        uitleg="800 gedeeld door 4 is 200 per werknemer, 1 000 gedeeld door 4 is 250. Dezelfde mensen maken meer, dankzij betere kapitaalgoederen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de productie per werknemer? Schrijf één woord.",
        antwoord=["arbeidsproductiviteit", "productiviteit"],
        uitleg="De arbeidsproductiviteit is de productie gedeeld door het aantal werknemers of gewerkte uren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kapitaalvorming?",
        opties=[
            "Het aanleggen van kapitaalgoederen waarmee je later kan produceren",
            "Het sparen van geld op een rekening bij een bank",
            "Het uitgeven van aandelen door een vennootschap",
            "Het betalen van intrest op een lening bij een bank",
        ],
        antwoord=0,
        uitleg="Kapitaalvorming is investeren in machines, gebouwen en infrastructuur. Met meer en betere kapitaalgoederen kan je in de toekomst meer produceren.",
    ),
    dict(
        type="waarofniet",
        vraag="Investeren in machines kost vandaag geld en levert pas later meer productie op.",
        antwoord=True,
        uitleg="Dat is net de afweging bij kapitaalvorming: je geeft nu uit en je plukt er later de vruchten van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is onderwijs een oorzaak van economische groei?",
        opties=[
            "Omdat beter opgeleide mensen productiever zijn en sneller nieuwe technieken leren",
            "Omdat scholen zelf goederen produceren die in het bbp meetellen",
            "Omdat jongeren die studeren niet meteen op de arbeidsmarkt komen",
            "Omdat de overheid veel geld uitgeeft aan de scholen van een land",
        ],
        antwoord=0,
        uitleg="Onderwijs verhoogt het menselijk kapitaal: kennis en vaardigheden. Dat maakt werknemers productiever en nieuwe technologie bruikbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kennis en de vaardigheden van de mensen in een land? Schrijf twee woorden.",
        antwoord=["menselijk kapitaal", "human capital"],
        uitleg="Menselijk kapitaal is het geheel van kennis, opleiding en ervaring. Het groeit door onderwijs en door werkervaring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan bevolkingsgroei tot economische groei leiden?",
        opties=[
            "Er zijn meer mensen die kunnen werken en meer mensen die kopen",
            "Er zijn meer mensen die een uitkering van de overheid krijgen",
            "Er zijn meer mensen die een opleiding moeten volgen",
            "Er is meer woonruimte nodig in de steden van dat land",
        ],
        antwoord=0,
        uitleg="Meer inwoners betekent een groter arbeidsaanbod en een grotere afzetmarkt. Daardoor kan het totale bbp stijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als het bbp door bevolkingsgroei stijgt, gaat elke inwoner er automatisch op vooruit.",
        antwoord=False,
        uitleg="Het bbp per capita kan dalen terwijl het totale bbp stijgt, namelijk als de bevolking sneller groeit dan de productie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land investeert zwaar in internetverbindingen en opleidingen. Welke twee oorzaken van groei zet het daarmee in?",
        opties=[
            "Kapitaalvorming en onderwijs",
            "Bevolkingsgroei en kapitaalvorming",
            "Onderwijs en bevolkingsgroei",
            "Prijsstijging en kapitaalvorming",
        ],
        antwoord=0,
        uitleg="Infrastructuur aanleggen is kapitaalvorming; opleidingen verhogen het menselijk kapitaal. Allebei verhogen ze de productiecapaciteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet technologische ontwikkeling met de productie? Duid alles aan wat juist is.",
        opties=[
            "Ze laat toe om met dezelfde middelen meer te maken",
            "Ze kan nieuwe producten mogelijk maken die er eerst niet waren",
            "Ze kan bepaalde taken overbodig maken",
            "Ze zorgt er altijd voor dat iedereen meer gaat verdienen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Technologie verhoogt de productiviteit, brengt nieuwe producten en laat taken verdwijnen. Of iedereen er ook op vooruitgaat, hangt af van hoe de opbrengst verdeeld wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan groei niet eindeloos uit bevolkingsgroei alleen komen?",
        opties=[
            "Omdat de productie per inwoner dan niet stijgt en de natuurlijke grenzen in zicht komen",
            "Omdat er na een tijd geen scholen meer zijn voor al die kinderen",
            "Omdat de overheid de bevolkingsgroei wettelijk kan tegenhouden",
            "Omdat de prijzen dan vanzelf beginnen te dalen in dat land",
        ],
        antwoord=0,
        uitleg="Met meer mensen maak je meer, maar niet meer per persoon. Echte vooruitgang in levensstandaard komt van hogere productiviteit, en ook grondstoffen en ruimte zijn beperkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stijging van de arbeidsproductiviteit betekent dat er meer mensen aan het werk zijn.",
        antwoord=False,
        uitleg="Productiviteit is productie per werknemer. Ze kan stijgen terwijl er net mínder mensen werken, bijvoorbeeld door betere machines.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het investeren in machines en gebouwen om later meer te kunnen produceren? Schrijf één woord.",
        antwoord=["kapitaalvorming", "investeren", "investering"],
        uitleg="Kapitaalvorming is het opbouwen van de kapitaalgoederenvoorraad van een land.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een land stijgt het reële bbp vijf jaar na elkaar met 2 %. Wat betekent dat?",
        opties=[
            "Er wordt elk jaar 2 % meer geproduceerd dan het jaar ervoor",
            "De prijzen stijgen elk jaar met 2 %",
            "Het aantal inwoners stijgt elk jaar met 2 %",
            "De lonen stijgen elk jaar met 2 %",
        ],
        antwoord=0,
        uitleg="Reëel wil zeggen: gezuiverd van prijsstijgingen. Dus het gaat echt om meer productie, elk jaar opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf koopt robots en ontslaat daarna geen enkele werknemer. Wat is het meest waarschijnlijke gevolg?",
        opties=[
            "De productie per werknemer stijgt",
            "De productie per werknemer daalt",
            "De loonkost per werknemer stijgt mee",
            "De omzet van het bedrijf blijft gelijk",
        ],
        antwoord=0,
        uitleg="Evenveel mensen met betere kapitaalgoederen maken meer: dat is precies wat hogere arbeidsproductiviteit betekent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land dat veel spaart, kan daarmee ook meer investeren.",
        antwoord=True,
        uitleg="Spaargeld komt via de banken terug in de economie als krediet. Zo maakt sparen kapitaalvorming mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee landen groeien allebei met 3 %. Land A heeft een bbp per capita van 40 000 euro, land B van 4 000 euro. Wat kan je zeggen?",
        opties=[
            "Dezelfde groei levert in land A in euro's veel meer op per inwoner",
            "Land B haalt land A binnen enkele jaren in",
            "De groei van land B is in werkelijkheid groter dan 3 %",
            "De twee landen zijn even rijk geworden dat jaar",
        ],
        antwoord=0,
        uitleg="3 % van 40 000 is 1 200 euro, 3 % van 4 000 is 120 euro. Een gelijk groeipercentage betekent dus niet dat de kloof kleiner wordt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is welvaart?",
        opties=[
            "De mate waarin behoeften voldaan worden met schaarse middelen",
            "De mate waarin mensen zich gelukkig en gezond voelen",
            "Het totale bedrag dat de inwoners van een land op de bank hebben",
            "Het aantal goederen dat in een land per jaar gemaakt wordt",
        ],
        antwoord=0,
        uitleg="Welvaart gaat over het voldoen van behoeften met middelen die schaars zijn. Hoe mensen zich voelen, is welzijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is welzijn?",
        opties=[
            "Hoe goed mensen zich voelen, ook door zaken die je niet kan kopen",
            "De hoeveelheid goederen en diensten die een gezin per jaar koopt",
            "Het inkomen dat een gezin na belastingen overhoudt",
            "De waarde van alles wat een gezin in huis heeft staan",
        ],
        antwoord=0,
        uitleg="Welzijn is ruimer dan welvaart: gezondheid, veiligheid, vrije tijd, een schone omgeving en sociale contacten horen erbij, en die staan niet allemaal in het bbp.",
    ),
    dict(
        type="waarofniet",
        vraag="Welvaart en welzijn betekenen in de economie precies hetzelfde.",
        antwoord=False,
        uitleg="Welvaart gaat over behoeften en schaarse middelen, welzijn over hoe goed het met mensen gaat. Je kan welvarend zijn en je toch niet goed voelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke positieve effecten kan economische groei hebben? Duid alles aan wat juist is.",
        opties=[
            "Meer werkgelegenheid",
            "Meer middelen voor onderwijs en gezondheidszorg",
            "Een hogere levensstandaard",
            "Minder druk op grondstoffen en milieu",
        ],
        antwoord=[0, 1, 2],
        uitleg="Groei brengt werk, belastinginkomsten en koopkracht mee. De druk op grondstoffen en milieu neemt bij groei meestal net toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk negatief effect van economische groei wordt het vaakst genoemd?",
        opties=[
            "De belasting van het milieu en de uitputting van grondstoffen",
            "De daling van het aantal werkenden in een land",
            "De daling van de belastinginkomsten van de overheid",
            "De stijging van het aantal scholen in een land",
        ],
        antwoord=0,
        uitleg="Meer produceren betekent meestal meer grondstoffen, meer energie en meer afval. Dat weegt op het welzijn, ook al stijgt de welvaart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het bbp van een land stijgt sterk, maar de lucht in de steden wordt slechter. Wat kan je besluiten?",
        opties=[
            "De welvaart stijgt, maar een deel van het welzijn gaat achteruit",
            "De welvaart en het welzijn stijgen allebei even snel",
            "De welvaart daalt, want vervuiling kost geld",
            "Het bbp kan niet stijgen als de lucht slechter wordt",
        ],
        antwoord=0,
        uitleg="Het bbp meet productie, niet luchtkwaliteit. Zo kan welvaart stijgen terwijl welzijn op een punt achteruitgaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel dat middelen beperkt zijn tegenover de behoeften? Schrijf één woord.",
        antwoord=["schaarste"],
        uitleg="Schaarste is het uitgangspunt van de economie: er is nooit genoeg van alles om elke behoefte te voldoen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bbp per capita zegt niets over hoe gelijk of ongelijk de welvaart verdeeld is.",
        antwoord=True,
        uitleg="Het is een gemiddelde. Twee landen met hetzelfde bbp per capita kunnen een heel verschillende verdeling hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruiken economen naast het bbp ook andere maatstaven?",
        opties=[
            "Omdat het bbp het welzijn, de verdeling en het milieu niet meet",
            "Omdat het bbp te moeilijk te berekenen is voor kleine landen",
            "Omdat het bbp alleen voor rijke landen beschikbaar is",
            "Omdat het bbp elk jaar met een andere methode gemaakt wordt",
        ],
        antwoord=0,
        uitleg="Het bbp is een goede maat voor productie, maar een gebrekkige maat voor hoe goed het met mensen gaat. Daarom kijkt men ook naar gezondheid, onderwijs en milieu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zaken verhogen het welzijn maar komen niet in het bbp? Duid alles aan wat juist is.",
        opties=[
            "Vrijwilligerswerk in een jeugdbeweging",
            "Zorgen voor een familielid zonder vergoeding",
            "Een propere lucht en veel groen in de buurt",
            "De bouw van een nieuw ziekenhuis",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat niet via een markt verloopt, blijft buiten het bbp. De bouw van een ziekenhuis wordt wél betaald en telt dus mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land werkt minder uren en houdt meer vrije tijd over, waardoor het bbp licht daalt. Hoe beoordeel je dat?",
        opties=[
            "De welvaart daalt licht, terwijl het welzijn kan stijgen",
            "De welvaart en het welzijn dalen allebei",
            "De welvaart stijgt, want vrije tijd is ook productie",
            "Er verandert niets, want vrije tijd telt niet mee",
        ],
        antwoord=0,
        uitleg="Minder productie betekent minder welvaart in de enge zin. Maar vrije tijd is voor veel mensen juist een stuk welzijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Economische groei leidt er altijd toe dat iedereen in een land erop vooruitgaat.",
        antwoord=False,
        uitleg="Groei zegt niets over de verdeling. Het is mogelijk dat de ene groep er fors op vooruitgaat en een andere groep niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verdeling van de productie onder de productiefactoren, in loon, intrest, pacht en winst? Schrijf twee woorden.",
        antwoord=["primaire inkomensverdeling", "functionele inkomensverdeling"],
        uitleg="De primaire of functionele inkomensverdeling deelt de toegevoegde waarde uit aan wie meegewerkt heeft. Daarna herverdeelt de overheid met belastingen en uitkeringen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe herverdeelt de overheid welvaart? Duid alles aan wat juist is.",
        opties=[
            "Met belastingen die stijgen naarmate het inkomen hoger is",
            "Met uitkeringen en toelagen aan wie weinig inkomen heeft",
            "Met diensten die voor iedereen toegankelijk zijn, zoals onderwijs",
            "Met het vastleggen van de prijs van elk product in de winkel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Belastingen, uitkeringen en collectieve diensten zijn de drie manieren van herverdeling. Prijzen in de winkel legt de overheid niet vast, op enkele uitzonderingen na.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is duurzame groei?",
        opties=[
            "Groei die rekening houdt met wat latere generaties nog nodig hebben",
            "Groei die elk jaar even groot is als het jaar ervoor",
            "Groei die alleen uit de dienstensector komt",
            "Groei die niet tot hogere prijzen leidt",
        ],
        antwoord=0,
        uitleg="Duurzame groei put grondstoffen en milieu niet uit, zodat de generaties na ons er ook nog iets aan hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoog bbp per capita is geen waarborg dat een land ook hoog scoort op gezondheid en onderwijs.",
        antwoord=True,
        uitleg="Er is meestal wel een verband, maar het is geen regel. Hoe het geld besteed en verdeeld wordt, maakt veel uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is schaarste het uitgangspunt van heel de economie?",
        opties=[
            "Omdat er van de meeste middelen te weinig is om alle behoeften te voldoen, zodat er gekozen moet worden",
            "Omdat er in de wereld heel weinig grondstoffen overblijven",
            "Omdat sommige producten maar in enkele winkels te koop zijn",
            "Omdat niet iedereen genoeg geld heeft om te kopen wat hij nodig heeft",
        ],
        antwoord=0,
        uitleg="Schaarste betekent: de middelen zijn beperkt tegenover de behoeften. Daarom moet elke actor kiezen, en net die keuzes bestudeert de economie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin kiest voor een duurdere wasmachine die minder energie verbruikt. Wat toont dat?",
        opties=[
            "Dat welvaart en welzijn in één keuze samen kunnen komen",
            "Dat welvaart altijd belangrijker is dan welzijn",
            "Dat het bbp daalt als mensen minder energie verbruiken",
            "Dat duurdere toestellen altijd beter zijn voor het milieu",
        ],
        antwoord=0,
        uitleg="Het gezin geeft vandaag meer uit en wint er later koopkracht én een kleinere milieudruk mee. Zo lopen welvaart en welzijn in dezelfde richting.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je groei die ook rekening houdt met de generaties na ons? Schrijf één woord.",
        antwoord=["duurzame", "duurzaam", "duurzaamheid"],
        uitleg="Duurzame groei houdt rekening met de draagkracht van de planeet en met de noden van latere generaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een regering wil de groei aanzwengelen. Welke maatregel past het best bij de oorzaken van groei?",
        opties=[
            "Investeren in opleiding en in infrastructuur",
            "De prijzen in de winkels laten stijgen",
            "Minder statistieken publiceren over de economie",
            "De invoer uit het buitenland volledig verbieden",
        ],
        antwoord=0,
        uitleg="Opleiding verhoogt het menselijk kapitaal en infrastructuur is kapitaalvorming. Dat zijn twee van de vier oorzaken van groei.",
    ),
]
