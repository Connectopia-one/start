# -*- coding: utf-8 -*-
"""De atoomkern, radioactief verval en halveringstijd — 🌍 Beyond, fysica.

Deel 1 gaat over de bouw van de kern: het massagetal, het atoomnummer en het
neutronental, de schrijfwijze van een nuclide, de isotopen, en waarom een kern
stabiel is of niet, met de sterke kernkracht tegenover de coulombkracht en met
de stabiliteitsband op de nuclidenkaart. Deel 2 gaat over het verval zelf: de
alfa-, bèta- en gammastraling, de transmutatieregels van Soddy, de
halveringstijd, de activiteit met de desintegratieconstante, en het rekenen
met de radioactieve vervalwet.

De rode draad is dat een kern vervalt omdat hij naar een stabielere
verhouding van protonen en neutronen zoekt, en dat de halveringstijd daarbij
vastligt: je kan hem niet versnellen of vertragen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het massagetal van een nuclide?",
        opties=[
            "het aantal protonen en neutronen samen",
            "het aantal protonen alleen",
            "het aantal neutronen alleen",
            "het aantal protonen en elektronen samen",
        ],
        antwoord=0,
        uitleg="Die twee heten samen de nucleonen, en het symbool is A. Het aantal protonen "
        "apart is het atoomnummer Z.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de deeltjes van een atoomkern samen?",
        antwoord=["nucleonen", "de nucleonen", "kerndeeltjes"],
        uitleg="Dat zijn de protonen en de neutronen. Hun aantal samen is het massagetal A.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nuclide heeft massagetal 23 en atoomnummer 11. Hoeveel neutronen heeft hij?",
        opties=[
            "12",
            "11",
            "23",
            "34",
        ],
        antwoord=0,
        uitleg="Het neutronental is A min Z, dus 23 min 11. Dit is natrium-23.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het atoomnummer van een nuclide?",
        opties=[
            "hoeveel protonen de kern bevat",
            "hoeveel neutronen de kern bevat",
            "hoeveel nucleonen de kern bevat",
            "hoeveel keer de kern al vervallen is",
        ],
        antwoord=0,
        uitleg="Het bepaalt welk element het is, en het heet ook het ladingsgetal. Het "
        "symbool ervan is Z.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn isotopen van een element?",
        opties=[
            "kernen met hetzelfde aantal protonen en een ander aantal neutronen",
            "kernen met hetzelfde aantal neutronen en een ander aantal protonen",
            "kernen met hetzelfde massagetal en een ander atoomnummer",
            "kernen die bij verval altijd hetzelfde deeltje uitzenden",
        ],
        antwoord=0,
        uitleg="Ze zijn dus hetzelfde element met een ander massagetal. Koolstof-12 en "
        "koolstof-14 zijn er een voorbeeld van.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee isotopen van hetzelfde element hebben hetzelfde atoomnummer.",
        antwoord=True,
        uitleg="Het aantal protonen maakt het element, dus dat blijft gelijk. Hun aantal "
        "neutronen en dus hun massagetal verschilt wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je een nuclide van element X met massagetal 14?",
        opties=[
            "als X-14, met het massagetal achter de naam",
            "als X-7, met het halve massagetal achter de naam",
            "als 14-X, met het massagetal voor de naam",
            "als X met het aantal neutronen erachter",
        ],
        antwoord=0,
        uitleg="Je kan het massagetal ook linksboven bij het symbool zetten, met het "
        "atoomnummer linksonder. Koolstof-14 is daarvan het bekendste geval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht houdt de nucleonen in een kern samen?",
        opties=[
            "de sterke kernkracht",
            "de elektrische afstotingskracht",
            "de gravitatiekracht tussen de nucleonen",
            "de magnetische kracht tussen de protonen",
        ],
        antwoord=0,
        uitleg="Ze werkt alleen over een heel korte afstand, maar is daar veel sterker dan "
        "de afstoting. De protonen stoten elkaar namelijk elektrisch af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten spelen in een atoomkern tegen elkaar in? Kruis alles aan wat juist is.",
        opties=[
            "de sterke kernkracht, die alle nucleonen aantrekt",
            "de coulombkracht, die de protonen afstoot",
            "de gravitatiekracht, die de kern uiteentrekt",
            "de wrijvingskracht tussen de nucleonen",
        ],
        antwoord=[0, 1],
        uitleg="De gravitatie is op die schaal volkomen verwaarloosbaar, en wrijving bestaat "
        "er niet. Het is de strijd tussen die eerste twee die over stabiliteit beslist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn zware kernen met Z groter dan 20 pas stabiel met meer neutronen dan protonen?",
        opties=[
            "de extra neutronen geven kernkracht zonder extra afstoting",
            "de extra neutronen stoten de protonen van elkaar weg",
            "de extra neutronen maken de kern elektrisch neutraal",
            "de extra neutronen maken de kern kleiner en dus steviger",
        ],
        antwoord=0,
        uitleg="Elke proton erbij geeft ook afstoting, een neutron niet. Daarom buigt de "
        "stabiliteitsband bij de zware kernen weg van de diagonaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij lichte kernen met Z kleiner dan 20 zijn het aantal protonen en neutronen ongeveer gelijk.",
        antwoord=True,
        uitleg="Koolstof-12 heeft zes van elk. Bij de zware kernen komen er verhoudingsgewijs "
        "meer neutronen bij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de strook stabiele kernen op een nuclidenkaart?",
        antwoord=["de stabiliteitsband", "stabiliteitsband", "stabiliteitszone"],
        uitleg="Kernen erbuiten vervallen tot ze erin terechtkomen. Daaruit lees je ook af "
        "welk soort verval een kern zal doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je uit de plaats van een kern op de nuclidenkaart?",
        opties=[
            "of hij stabiel is en welk verval hij anders zal doen",
            "hoe lang zijn halveringstijd precies in seconden is",
            "hoeveel energie er bij zijn verval vrijkomt",
            "welke chemische verbindingen hij kan vormen",
        ],
        antwoord=0,
        uitleg="Ligt hij onder de band, dan heeft hij te veel neutronen. Dan vervalt hij via "
        "bèta-min-straling naar een stabielere kern.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een radionuclide?",
        opties=[
            "een kern die onstabiel is en spontaan vervalt",
            "een kern die precies even veel protonen als neutronen heeft",
            "een kern die geen enkele straling kan uitzenden",
            "een kern die alleen onder een hoge druk vervalt",
        ],
        antwoord=0,
        uitleg="Zijn verval komt van zichzelf, niet van iets wat je eraan doet. Daarom kan "
        "je een halveringstijd ook niet versnellen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan het verval van een radionuclide versnellen door hem te verwarmen.",
        antwoord=False,
        uitleg="Verval is een kernproces en trekt zich van druk of temperatuur niets aan. "
        "Dat is net waarom radioactief afval zo lang een probleem blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens liggen vast zodra je het massagetal en het atoomnummer kent? Kruis alles aan wat juist is.",
        opties=[
            "het aantal protonen in de kern",
            "het aantal neutronen in de kern",
            "om welk element het gaat",
            "de halveringstijd van de kern",
        ],
        antwoord=[0, 1, 2],
        uitleg="De halveringstijd moet je opzoeken, die volgt niet uit die twee getallen. De "
        "rest reken je er wel uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel protonen en neutronen heeft uranium-238, met atoomnummer 92?",
        opties=[
            "92 protonen en 146 neutronen",
            "92 protonen en 238 neutronen",
            "146 protonen en 92 neutronen",
            "119 protonen en 119 neutronen",
        ],
        antwoord=0,
        uitleg="Het neutronental is 238 min 92. Zo'n zware kern heeft die neutronenovermaat "
        "nodig om niet meteen uiteen te vallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschillen koolstof-12 en koolstof-14?",
        opties=[
            "in hun aantal neutronen",
            "in hun aantal protonen",
            "in hun atoomnummer",
            "in welk element ze zijn",
        ],
        antwoord=0,
        uitleg="Koolstof-12 heeft zes neutronen en koolstof-14 acht. Daardoor is de tweede "
        "onstabiel, en net dat maakt de koolstofdatering mogelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nuclide met een ander aantal neutronen is een ander element.",
        antwoord=False,
        uitleg="Het element hangt alleen van het aantal protonen af. Een ander aantal "
        "neutronen geeft een isotoop van hetzelfde element.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een nuclide zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het massagetal is de som van protonen en neutronen",
            "het atoomnummer is gelijk aan het aantal protonen",
            "het neutronental is de som van A en Z",
            "het ladingsgetal is gelijk aan het aantal neutronen",
        ],
        antwoord=[0, 1],
        uitleg="Het neutronental is A min Z, dus een verschil en geen som. En het "
        "ladingsgetal is een ander woord voor het atoomnummer.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zendt een kern uit bij alfaverval?",
        opties=[
            "een kern van helium, met twee protonen en twee neutronen",
            "een elektron, uit een neutron van de kern",
            "een foton met heel veel energie",
            "een los neutron uit de kern",
        ],
        antwoord=0,
        uitleg="Het massagetal daalt dus met vier en het atoomnummer met twee. Dat zijn de "
        "regels van Soddy voor alfaverval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij bèta-min-verval?",
        opties=[
            "een neutron wordt een proton en er vertrekt een elektron",
            "een proton wordt een neutron en er vertrekt een elektron",
            "een neutron verlaat de kern zonder iets te veranderen",
            "twee protonen en twee neutronen verlaten samen de kern",
        ],
        antwoord=0,
        uitleg="Het atoomnummer stijgt daardoor met één en het massagetal blijft gelijk. Er "
        "vertrekt ook een neutrino mee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het deeltje dat bij bèta-plus-verval wegvliegt?",
        antwoord=["een positron", "positron", "antielektron"],
        uitleg="Het is het antideeltje van het elektron, met een positieve lading. Daarbij "
        "wordt een proton een neutron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is gammastraling?",
        opties=[
            "een foton met heel veel energie uit de kern",
            "een kern van helium uit de kern",
            "een elektron uit de kern",
            "een neutron uit de kern",
        ],
        antwoord=0,
        uitleg="Het massagetal en het atoomnummer blijven daarbij dezelfde. De kern raakt "
        "alleen zijn overtollige energie kwijt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kern met massagetal 226 en atoomnummer 88 doet alfaverval. Wat krijg je?",
        opties=[
            "massagetal 222 en atoomnummer 86",
            "massagetal 222 en atoomnummer 88",
            "massagetal 226 en atoomnummer 86",
            "massagetal 224 en atoomnummer 87",
        ],
        antwoord=0,
        uitleg="Bij alfaverval gaat er vier van A af en twee van Z. Zo wordt radium-226 "
        "radon-222.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de regels van Soddy zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "bij alfaverval daalt het massagetal met vier",
            "bij bèta-min-verval stijgt het atoomnummer met één",
            "bij gammaverval blijven A en Z dezelfde",
            "bij alfaverval blijft het atoomnummer gelijk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij alfaverval daalt het atoomnummer juist met twee. In elke "
        "reactievergelijking moeten A en Z links en rechts kloppen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de tijd waarin de helft van de kernen vervalt?",
        antwoord=["de halveringstijd", "halveringstijd", "halfwaardetijd"],
        uitleg="Ze krijgt het symbool T met een half eronder. Na twee zulke tijden is er nog "
        "een kwart over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stof heeft een halveringstijd van 8 dagen. Welk deel is er na 24 dagen nog over?",
        opties=[
            "een achtste",
            "een derde",
            "een kwart",
            "een zestiende",
        ],
        antwoord=0,
        uitleg="24 dagen zijn drie halveringstijden, dus de helft van de helft van de helft. "
        "Dat geeft een achtste.",
    ),
    dict(
        type="waarofniet",
        vraag="Na twee halveringstijden is een radioactieve stof volledig vervallen.",
        antwoord=False,
        uitleg="Er is dan nog een kwart over, want elke keer verdwijnt maar de helft. "
        "Volledig verdwijnen gebeurt in dit model nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de activiteit van een radionuclide?",
        opties=[
            "het aantal kernen dat per seconde vervalt",
            "het aantal kernen dat nog niet vervallen is",
            "de energie die bij elk verval vrijkomt",
            "de tijd waarin de helft van de kernen vervalt",
        ],
        antwoord=0,
        uitleg="Ze staat in becquerel, dus in verval per seconde. Je berekent ze als de "
        "desintegratieconstante maal het aantal kernen.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de activiteit van een bron uit?",
        antwoord=["becquerel", "Bq", "de becquerel"],
        uitleg="Eén becquerel is één verval per seconde. De dosis die een mens opneemt, "
        "staat wel in gray of sievert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de desintegratieconstante uit de halveringstijd?",
        opties=[
            "0,693 gedeeld door de halveringstijd",
            "de halveringstijd gedeeld door 0,693",
            "0,693 maal de halveringstijd",
            "0,693 min de halveringstijd",
        ],
        antwoord=0,
        uitleg="Dat getal 0,693 is de natuurlijke logaritme van twee. Een korte "
        "halveringstijd geeft dus een grote constante.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de halveringstijd zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "na één halveringstijd is de helft van de kernen vervallen",
            "ze ligt voor elk radionuclide vast",
            "een kortere halveringstijd geeft bij dezelfde hoeveelheid een hogere activiteit",
            "je kan ze verkorten door de stof te verwarmen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verval trekt zich van druk of temperatuur niets aan. Daarom blijft "
        "langlevend afval ook duizenden jaren een probleem.",
    ),
    dict(
        type="waarofniet",
        vraag="De activiteit van een bron daalt in de tijd op dezelfde manier als het aantal kernen.",
        antwoord=True,
        uitleg="Ze is er recht evenredig mee, want A is lambda maal N. Beide grafieken "
        "halveren dus na elke halveringstijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de activiteit van een bron zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze staat in becquerel",
            "ze is de desintegratieconstante maal het aantal kernen",
            "ze halveert na elke halveringstijd",
            "ze is gelijk aan het aantal kernen in de bron",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ze is recht evenredig met dat aantal, maar niet gelijk eraan. Daarom daalt "
        "haar grafiek op dezelfde manier, steeds langzamer naar de tijdas toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bron heeft nu een activiteit van 800 Bq en een halveringstijd van 5 jaar. Welke activiteit heeft ze na 10 jaar?",
        opties=[
            "200 Bq",
            "400 Bq",
            "80 Bq",
            "100 Bq",
        ],
        antwoord=0,
        uitleg="Tien jaar zijn twee halveringstijden, dus een kwart van 800. De activiteit "
        "volgt dezelfde wet als het aantal kernen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om het aantal kernen in een massa stof te berekenen? Kruis alles aan wat juist is.",
        opties=[
            "de massa van de stof",
            "de molaire massa van de stof",
            "het getal van Avogadro",
            "de halveringstijd van de stof",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je deelt de massa door de molaire massa en vermenigvuldigt met het getal van "
        "Avogadro. De halveringstijd heb je pas nodig voor de activiteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kern onder de stabiliteitsband heeft te veel neutronen en vervalt via bèta-min-straling.",
        antwoord=True,
        uitleg="Een neutron wordt daarbij een proton, dus schuift de kern naar de band toe. "
        "Boven de band gebeurt net het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt de koolstof-14-methode om ouderdom te bepalen?",
        opties=[
            "het gehalte koolstof-14 daalt na de dood met een vaste halveringstijd",
            "het gehalte koolstof-14 stijgt na de dood met een vaste halveringstijd",
            "koolstof-14 ontstaat in een dood organisme steeds sneller",
            "koolstof-14 verdwijnt bij de dood in één keer volledig",
        ],
        antwoord=0,
        uitleg="Zolang een organisme leeft, vult het zijn koolstof-14 aan. Daarna vervalt het "
        "met een halveringstijd van ongeveer 5730 jaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij gammaverval verandert de kern in een ander element.",
        antwoord=False,
        uitleg="Het atoomnummer blijft gelijk, dus blijft het hetzelfde element. Enkel de "
        "energie van de kern daalt.",
    ),
]
