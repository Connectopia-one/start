# -*- coding: utf-8 -*-
"""De vragen voor "Grondstoffen, energie en industrie" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "economische processen" (20 % van
het examen, samen met [[ak_landbouw]]). Dit thema neemt het eerste stuk:
ontginning, energiewinning en industrie.

Deel 1 gaat over grondstoffen en energie: welke grondstoffen waar ontgonnen
worden en waarom, op welke manier dat gebeurt (in een groeve of in een mijn,
traditioneel of modern, of via recyclage), en welke energiebronnen waar
voorkomen, hernieuwbaar zowel als niet-hernieuwbaar.
Deel 2 gaat over de industrie: welke soorten industrie waar voorkomen, waar
producten gemaakt worden en voor welke afzetmarkt, het verschil tussen
traditionele en moderne industrie, en de geopolitieke, fysische en
sociaaleconomische factoren die het industriële proces sturen.

Bij landen en grondstoffen blijven de voorbeelden bij wat al jaren stabiel is
en in elke atlas staat. Waar een rangschikking kan verschuiven, wordt er
"een van de grootste" geschreven in plaats van "de grootste", zodat de vraag
over vijf jaar nog klopt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een groeve en een mijn?",
        opties=[
            "Een groeve ligt in open lucht, een mijn ondergronds",
            "Een groeve is groter dan een mijn in oppervlakte",
            "In een groeve wint men enkel steen, in een mijn enkel erts",
            "Een groeve is modern, een mijn is altijd traditioneel",
        ],
        antwoord=0,
        uitleg="In een groeve of dagbouw graaft men van bovenaf. Zit de laag te diep, dan moet men schachten en gangen maken, en dan spreekt men van een mijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kiest een bedrijf voor dagbouw als dat kan?",
        opties=[
            "Het is goedkoper en veiliger dan ondergronds werken",
            "Het levert altijd zuiverder erts op dan een mijn",
            "Het is beter voor het landschap dan een mijn",
            "Het mag alleen zo in landen met een hoge HDI",
        ],
        antwoord=0,
        uitleg="Geen schachten, geen instortingsgevaar, grote machines die veel tegelijk verzetten: dat drukt de kosten. Voor het landschap is dagbouw juist ingrijpender, want er verdwijnt een hele laag grond.",
    ),
    dict(
        type="waarofniet",
        vraag="Waar een grondstof ontgonnen wordt, hangt in de eerste plaats af van waar die in de bodem zit.",
        antwoord=True,
        uitleg="Zonder voorraad geen ontginning. Maar of die voorraad ook echt gewonnen wordt, hangt daarnaast af van de prijs, de politieke stabiliteit en de bereikbaarheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk land wordt veruit het meeste kobalt ontgonnen?",
        opties=[
            "De Democratische Republiek Congo",
            "Noorwegen",
            "Japan",
            "Nieuw-Zeeland",
        ],
        antwoord=0,
        uitleg="Het grootste deel van het kobalt in de wereld komt uit Congo. Dat metaal zit in de batterijen van gsm's en elektrische auto's, wat de ontginningsomstandigheden daar een politieke kwestie maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn niet-hernieuwbare energiebronnen? (meerdere antwoorden mogelijk)",
        opties=[
            "Aardolie",
            "Steenkool",
            "Uranium voor kernenergie",
            "Wind op de Noordzee",
            "Zonlicht op een dak",
        ],
        antwoord=[0, 1, 2],
        uitleg="Olie, steenkool en uranium zitten in eindige voorraden in de bodem. Wind en zon komen elke dag terug, en die noemen we daarom hernieuwbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Kernenergie is een hernieuwbare energiebron omdat een centrale nauwelijks CO₂ uitstoot.",
        antwoord=False,
        uitleg="Weinig CO₂ betekent niet hernieuwbaar. Uranium moet ontgonnen worden en raakt op, en er blijft radioactief afval over. Hernieuwbaar gaat over de bron, niet over de uitstoot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan windmolenparken in België vooral op de Noordzee en in open landschap?",
        opties=[
            "Daar waait het harder en constanter",
            "Daar is de bodem stevig genoeg om te bouwen",
            "Daar is de bevolkingsdichtheid het hoogst",
            "Daar is de luchtdruk het hele jaar gelijk",
        ],
        antwoord=0,
        uitleg="Een windmolen heeft wind nodig zonder gebouwen of bossen die hem afremmen. Boven zee is dat het best, en daar staan bovendien geen buren die er last van hebben.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord energiebronnen zoals wind, zon en waterkracht, die niet opraken?",
        antwoord=["hernieuwbare", "hernieuwbaar", "hernieuwbare energie"],
        uitleg="Hernieuwbare bronnen worden voortdurend aangevuld door de natuur. Fossiele brandstoffen en uranium zijn eindig en dus niet-hernieuwbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen zonneparken vooral in gebieden met veel zonuren?",
        opties=[
            "De opbrengst per paneel is er een stuk hoger",
            "Panelen gaan er langer mee dan elders",
            "De grond is er altijd goedkoper dan elders",
            "Er is er minder onderhoud aan nodig",
        ],
        antwoord=0,
        uitleg="Dezelfde investering levert er meer stroom op. Daarom liggen de grote parken in Spanje, Noord-Afrika of het zuidwesten van de Verenigde Staten.",
    ),
    dict(
        type="waarofniet",
        vraag="Recyclage kan een bron van grondstoffen zijn, naast ontginning uit de bodem.",
        antwoord=True,
        uitleg="Uit oud schroot, gebruikte batterijen en elektronica komen metalen terug. Dat heet soms stedelijke mijnbouw, en het spaart zowel energie als bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke redenen maken recyclage van metalen aantrekkelijk? (meerdere antwoorden mogelijk)",
        opties=[
            "Er is veel minder energie voor nodig dan voor nieuw erts",
            "Er hoeft geen nieuwe mijn of groeve voor open",
            "Het maakt een land minder afhankelijk van invoer",
            "Het gerecycleerde metaal is altijd zuiverder dan nieuw",
            "Er komen geen transportkosten meer bij kijken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Energie, landschap en onafhankelijkheid zijn de echte winsten. Gerecycleerd metaal is meestal net minder zuiver, en vervoerd moet het nog altijd worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen traditionele en moderne ontginning?",
        opties=[
            "Traditioneel gebeurt met handkracht, modern met machines",
            "Traditioneel levert altijd meer op dan modern",
            "Traditioneel gebeurt boven de grond, modern eronder",
            "Traditioneel is altijd duurzamer dan modern",
        ],
        antwoord=0,
        uitleg="Bij traditionele ontginning graven mensen met eenvoudig gereedschap, soms in gevaarlijke omstandigheden. Moderne ontginning draait op zware machines en levert veel meer per werkende op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land met grote grondstofvoorraden is daarom nog geen welvarend land.",
        antwoord=True,
        uitleg="Als de winst naar buitenlandse bedrijven of een kleine elite gaat, merkt de bevolking er weinig van. Men spreekt dan zelfs van de grondstoffenvloek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land met grote olievoorraden raakt in oorlog. Wat verwacht je met de productie?",
        opties=[
            "Ze valt terug, want investeerders en werknemers vertrekken",
            "Ze stijgt, want oorlog vraagt meer brandstof",
            "Ze blijft gelijk, want de olie zit gewoon in de grond",
            "Ze stijgt, want de prijzen gaan bij oorlog omhoog",
        ],
        antwoord=0,
        uitleg="Ontginning heeft rust, personeel en werkende havens en pijpleidingen nodig. Politieke stabiliteit is daarom een echte geopolitieke factor, geen bijzaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fysische factoren beïnvloeden waar energie geproduceerd wordt? (meerdere antwoorden mogelijk)",
        opties=[
            "Het klimaat en de klimaatverandering",
            "Het reliëf van het gebied",
            "De grondstoffen in de bodem",
            "De staatsvorm van het land",
            "Het loon van de werknemers",
        ],
        antwoord=[0, 1, 2],
        uitleg="Klimaat, reliëf en grondstoffen zijn fysische factoren. Staatsvorm is geopolitiek en verloning sociaaleconomisch; de fiche zet die drie groepen bewust naast elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je energiecentrales die stroom maken uit stromend water in een stuwdam?",
        antwoord=["waterkrachtcentrales", "waterkrachtcentrale", "waterkracht"],
        uitleg="Waterkracht heeft hoogteverschil en een constante watertoevoer nodig. Daarom liggen die centrales in bergachtige streken met veel neerslag of smeltwater.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaatverandering kan bepalen hoeveel een waterkrachtcentrale opbrengt.",
        antwoord=True,
        uitleg="Krimpen de gletsjers en valt er in de zomer minder neerslag, dan staat er minder water in het stuwmeer. Verschillende Alpenlanden merken dat al in hun jaarcijfers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lagen de oude steenkoolmijnen van de Kempen precies daar?",
        opties=[
            "Daar zat de steenkoollaag in de ondergrond",
            "Daar was de bevolkingsdichtheid het hoogst",
            "Daar liep de grens met Nederland vlakbij",
            "Daar was het klimaat het meest geschikt",
        ],
        antwoord=0,
        uitleg="Ontginning volgt de voorraad. De mijnen van onder andere Genk, Beringen en Houthalen kwamen er nadat men de steenkoollaag in de Kempense ondergrond gevonden had.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grondstof wordt altijd ontgonnen zodra men weet dat ze ergens zit.",
        antwoord=False,
        uitleg="Pas als de opbrengst hoger is dan de kosten van winnen en vervoeren, begint men eraan. Stijgt de wereldprijs, dan wordt een voorraad die jaren bleef liggen plots wel interessant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden zeldzame metalen voor batterijen steeds meer gezocht?",
        opties=[
            "De vraag naar elektrische toestellen en auto's stijgt",
            "De voorraden in de bodem groeien elk jaar aan",
            "Ze zijn goedkoper geworden om te ontginnen",
            "Ze zijn overal ter wereld even gemakkelijk te vinden",
        ],
        antwoord=0,
        uitleg="Vraag en aanbod sturen de ontginning. Doordat de wereld op elektriciteit overschakelt, stijgt de vraag naar lithium, kobalt en nikkel, en dus ook de druk op de gebieden waar ze zitten.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom lag de zware industrie vroeger vlak bij de steenkoolmijnen?",
        opties=[
            "Steenkool was zwaar en duur om te vervoeren",
            "De grond was daar goedkoper dan elders",
            "De arbeiders wilden dicht bij de mijn wonen",
            "De overheid verplichtte bedrijven daartoe",
        ],
        antwoord=0,
        uitleg="Voor één ton staal had men veel kolen nodig. Die naast de fabriek hebben scheelde enorm, en zo groeiden staal en glas langs de Samber en de Maas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt moderne industrie tegenover traditionele industrie?",
        opties=[
            "Ze kiest haar plaats vrijer, want grondstoffen wegen minder",
            "Ze gebruikt altijd meer arbeiders per product dan vroeger",
            "Ze ligt altijd verder van een haven of luchthaven",
            "Ze verbruikt altijd meer steenkool dan vroeger",
        ],
        antwoord=0,
        uitleg="Chips, medicijnen en software hangen niet aan een kolenlaag vast. Ze zoeken kennis, goede verbindingen en personeel, en kunnen dus bijna overal terecht.",
    ),
    dict(
        type="waarofniet",
        vraag="De afzetmarkt van een product is de plaats waar het verkocht wordt.",
        antwoord=True,
        uitleg="Waar iets gemaakt wordt en waar het verkocht wordt, kan ver uit elkaar liggen. Juist dat verschil maakt de wereldhandel en de rol van havens zo groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen de grote chemische bedrijven van ons land in en rond de haven van Antwerpen?",
        opties=[
            "Grondstoffen komen er per schip binnen en producten weer buiten",
            "De bodem is er het meest vruchtbaar van het land",
            "Het klimaat is er milder dan in de rest van het land",
            "De bevolkingsdichtheid is er het laagst van het land",
        ],
        antwoord=0,
        uitleg="Aardolie en chemische grondstoffen reizen over zee. Een fabriek aan de kade bespaart een dure rit over land, en dat weegt in de chemie zwaar door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke geopolitieke factoren beïnvloeden waar industrie zich vestigt? (meerdere antwoorden mogelijk)",
        opties=[
            "De staatsvorm van het land",
            "De politieke stabiliteit van het land",
            "De samenwerkingsverbanden met andere landen",
            "Het reliëf van de streek",
            "De klimaatzone van de streek",
        ],
        antwoord=[0, 1, 2],
        uitleg="Staatsvorm, stabiliteit en verdragen bepalen of een bedrijf er durft te investeren en of het vlot kan uitvoeren. Reliëf en klimaat zijn fysische factoren.",
    ),
    dict(
        type="waarofniet",
        vraag="Lagere lonen zijn de enige reden waarom bedrijven productie naar het buitenland verplaatsen.",
        antwoord=False,
        uitleg="Lonen wegen mee, maar ook belastingen, milieuregels, de nabijheid van de afzetmarkt en de beschikbaarheid van geschoold personeel. Vaak is het een combinatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt bedoeld met de-industrialisatie?",
        opties=[
            "Industrie verdwijnt uit een streek die er sterk op draaide",
            "Industrie breidt zich uit naar het platteland toe",
            "Industrie schakelt over op hernieuwbare energie",
            "Industrie wordt door de overheid overgenomen",
        ],
        antwoord=0,
        uitleg="Fabrieken sluiten of verhuizen, en de streek verliest werk en inkomen. Wallonië en Noord-Frankrijk maakten dat na de sluiting van de mijnen en de staalbedrijven mee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het omvormen van een oud industrieterrein tot iets nieuws, zoals de mijnsite van Genk die een bedrijven- en onderzoekspark werd?",
        antwoord=["reconversie", "de reconversie"],
        uitleg="Reconversie geeft een gebied een nieuwe functie: wetenschapspark, woonwijk, museum of natuurgebied. Het gebouw blijft vaak staan, het gebruik verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen heeft de sluiting van een grote fabriek voor een streek? (meerdere antwoorden mogelijk)",
        opties=[
            "Werkloosheid stijgt in de omliggende gemeenten",
            "Jongeren trekken weg op zoek naar werk",
            "Er komt een groot terrein leeg te staan",
            "De bevolkingsdichtheid stijgt er meteen",
            "Het klimaat van de streek verandert erdoor",
        ],
        antwoord=[0, 1, 2],
        uitleg="Werk, bevolking en ruimte veranderen alle drie. De dichtheid daalt juist als jongeren wegtrekken, en op het klimaat van de streek heeft een fabriek geen meetbare invloed.",
    ),
    dict(
        type="waarofniet",
        vraag="De nabijheid van de klanten weegt voor elk bedrijf even zwaar, welk product het ook maakt.",
        antwoord=False,
        uitleg="Bij zware of bederfelijke producten weegt ze zwaar: een betoncentrale of een bakkerij levert dicht bij huis. Bij lichte, dure producten zoals medicijnen of chips weegt ze bijna niet, want vervoeren kost daar weinig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke sociaaleconomische factoren noemt de vakfiche bij het industriële proces? (meerdere antwoorden mogelijk)",
        opties=[
            "De Human Development Index",
            "De verloning van de werknemers",
            "Vraag en aanbod en de afzetmarkt",
            "De klimaatzone van het gebied",
            "De reliëfeenheid van het gebied",
        ],
        antwoord=[0, 1, 2],
        uitleg="HDI, verloning, vraag en aanbod en de afzetmarkt zijn de sociaaleconomische factoren. Klimaatzone en reliëfeenheid staan bij de fysische.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fabrikant van kleding laat naaien in een land met lage lonen en verkoopt in Europa. Wat zegt dat over productie en afzetmarkt?",
        opties=[
            "Ze liggen op verschillende continenten",
            "Ze vallen altijd in hetzelfde land samen",
            "De afzetmarkt bepaalt waar genaaid wordt",
            "De productie bepaalt waar verkocht wordt",
        ],
        antwoord=0,
        uitleg="Het product legt duizenden kilometers af voor het in de winkel hangt. Dat uit elkaar halen van productie en verkoop is typisch voor een gemondialiseerde economie.",
    ),
    dict(
        type="waarofniet",
        vraag="Moderne industrie heeft geen goede transportverbindingen meer nodig.",
        antwoord=False,
        uitleg="Ze is minder aan grondstoffen gebonden, maar niet aan transport. Luchthavens, autosnelwegen en snelle datakabels zijn voor moderne bedrijven juist doorslaggevend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je op een kaart een gebied met zware industrie?",
        opties=[
            "Grote bedrijventerreinen bij een haven, spoor of kanaal",
            "Kleine winkels verspreid over de dorpskernen",
            "Grote aaneengesloten bossen zonder bebouwing",
            "Veel kleine akkers met hagen ertussen",
        ],
        antwoord=0,
        uitleg="Zware industrie vraagt ruimte en vervoer over water of spoor. Op een kaart zie je dus grote blokken langs een kanaal, een dok of een spoorbundel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verplaatsen van werk of productie naar een bedrijf in een ander land?",
        antwoord=["outsourcing", "uitbesteding", "delokalisatie"],
        uitleg="Outsourcing of uitbesteding brengt werk naar waar het goedkoper of beter kan. Het is een van de motoren van de mondialisering.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land dat lid is van een groot handelsblok, voert makkelijker uit naar de andere leden.",
        antwoord=True,
        uitleg="Binnen de Europese Unie vallen invoerrechten en veel controles weg. Dat is precies waarom samenwerkingsverbanden bij de geopolitieke factoren staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een streek verliest haar mijnen, maar krijgt later een wetenschapspark en een campus. Wat is hier gebeurd?",
        opties=[
            "De-industrialisatie gevolgd door reconversie",
            "Industrialisatie gevolgd door schaalvergroting",
            "Verstedelijking gevolgd door ontvolking",
            "Segregatie gevolgd door multiculturaliteit",
        ],
        antwoord=0,
        uitleg="Eerst verdween de oude industrie, daarna kreeg het terrein een nieuwe functie. Thor Park in Genk, op de oude mijnsite van Waterschei, is daar een voorbeeld van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ruimtelijke gevolgen heeft grondstofontginning? (meerdere antwoorden mogelijk)",
        opties=[
            "Het landschap verandert blijvend van vorm",
            "Er komen wegen en spoorlijnen naartoe",
            "Er ontstaan nederzettingen voor de werkers",
            "De klimaatzone van het gebied verschuift",
            "De geografische coördinaten verschuiven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een mijn of groeve trekt infrastructuur en mensen aan en laat een put of een terril na. Coördinaten en klimaatzones veranderen daar natuurlijk niet van.",
    ),
    dict(
        type="waarofniet",
        vraag="Industrie zoekt tegenwoordig vooral plaatsen met goedkope grond en een goede aansluiting op het wegennet.",
        antwoord=True,
        uitleg="Daarom liggen nieuwe bedrijventerreinen bij snelwegafritten buiten de stad. Het gevolg is dat werk uit de kernen wegtrekt en de open ruimte verder versnippert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een haven zo belangrijk voor de industrie van een land?",
        opties=[
            "Ze verbindt de fabrieken met afzetmarkten overzee",
            "Ze levert de fabrieken rechtstreeks elektriciteit",
            "Ze zorgt voor goedkopere lonen in de streek",
            "Ze verlaagt de belastingen voor bedrijven daar",
        ],
        antwoord=0,
        uitleg="Het grootste deel van de wereldhandel gaat over zee. Een haven is de poort waardoor grondstoffen binnenkomen en afgewerkte producten vertrekken.",
    ),
]
