# -*- coding: utf-8 -*-
"""Toepassingen van redox: batterijen, galvaniseren en corrosie — chemie.

🌍 Beyond. Deel 1 gaat over de batterij en de brandstofcel: hoe een cel spanning
levert, waarom een batterij leeg raakt, wat een oplaadbare batterij anders maakt,
en waarom een brandstofcel blijft werken zolang je ze voedt. Deel 2 gaat over
corrosie: waarom ijzer roest, wat het sneller doet gaan, en de manieren om het
tegen te gaan, van een laagje zink tot kathodische bescherming met een
verteringselektrode.

De vragen vragen telkens naar het waarom van een keuze, want dat is wat je met
de tabel van de normpotentialen kan verklaren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom levert een batterij spanning?",
        opties=[
            "er verloopt binnenin een spontane redoxreactie",
            "er zit een spanningsbron in de batterij ingebouwd",
            "de twee polen hebben een verschillende temperatuur",
            "de elektrolyt in de batterij is zuur en geleidt goed",
        ],
        antwoord=0,
        uitleg="Het verschil in normpotentiaal tussen de twee koppels is de bronspanning. "
        "De elektronen lopen door de kring die je ermee sluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom raakt een batterij leeg?",
        opties=[
            "de stoffen die de reactie voeden, zijn opgebruikt",
            "de elektronen in de batterij zijn uitgeput",
            "de spanning verdwijnt door het opwarmen van de polen",
            "de polen wisselen na een tijd van teken",
        ],
        antwoord=0,
        uitleg="De reactie loopt tot minstens één reagens op is. Daarna is er geen "
        "elektronenstroom meer en valt de spanning weg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een batterij die je opnieuw kan opladen?",
        antwoord=["oplaadbaar", "een accu", "accu"],
        uitleg="Bij het opladen duwt een spanningsbron de reactie terug, en dat is een "
        "elektrolyse. Een gewone batterij kan dat niet veilig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij het opladen van een accu?",
        opties=[
            "de reactie wordt door een elektrolyse teruggeduwd",
            "de twee elektroden worden van plaats gewisseld",
            "er wordt nieuwe elektrolyt in de cel gepompt",
            "de elektronen worden in de polen opgeslagen",
        ],
        antwoord=0,
        uitleg="De stoffen van het begin worden opnieuw gevormd. Daarom kost opladen "
        "energie en levert ontladen energie.",
    ),
    dict(
        type="waarofniet",
        vraag="In een brandstofcel wordt de brandstof voortdurend aangevoerd.",
        antwoord=True,
        uitleg="Daarom raakt ze niet leeg zoals een batterij. Stopt de aanvoer van "
        "waterstofgas en zuurstofgas, dan stopt de cel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het reactieproduct van een waterstofbrandstofcel?",
        opties=[
            "water",
            "koolstofdioxide",
            "waterstofperoxide",
            "stikstofoxide",
        ],
        antwoord=0,
        uitleg="Waterstofgas wordt geoxideerd en zuurstofgas gereduceerd. Er komt dus "
        "enkel water uit de cel, en geen broeikasgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een brandstofcel zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zet chemische energie direct om in elektrische energie",
            "ze blijft werken zolang er brandstof aangevoerd wordt",
            "ze slaat de brandstof binnenin op zoals een batterij",
            "ze heeft een spanningsbron nodig om te werken",
        ],
        antwoord=[0, 1],
        uitleg="Een brandstofcel is een galvanische cel met een open toevoer. Daardoor "
        "hoeft ze niet opgeladen te worden, alleen bijgevuld.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pool van een batterij is de anode?",
        antwoord=["de negatieve", "negatieve pool", "min"],
        uitleg="Daar gebeurt de oxidatie en komen de elektronen vrij. Bij het opladen "
        "wordt die plaats net de kathode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er op een batterij een spanning in volt?",
        opties=[
            "het is het verschil in normpotentiaal tussen de twee koppels",
            "het is de hoeveelheid lading die de batterij kan leveren",
            "het is de tijd die de batterij meegaat bij gebruik",
            "het is de temperatuur waarbij de batterij werkt",
        ],
        antwoord=0,
        uitleg="Hoeveel lading er in zit, staat er apart bij in milliampère-uur. Dat is "
        "iets anders dan de spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag je een batterij niet kortsluiten?",
        opties=[
            "de reactie loopt dan heel snel en de batterij wordt gevaarlijk warm",
            "de polen wisselen dan van teken en de batterij laadt op",
            "de elektrolyt verdampt dan en de batterij droogt uit",
            "de spanning stijgt dan tot boven de waarde op het etiket",
        ],
        antwoord=0,
        uitleg="Zonder weerstand in de kring is er niets dat de stroom beperkt. Bij een "
        "lithiumbatterij kan dat zelfs brand geven.",
    ),
    dict(
        type="waarofniet",
        vraag="Een batterij levert gelijkspanning.",
        antwoord=True,
        uitleg="De oxidatie gebeurt altijd aan dezelfde pool, dus loopt de stroom altijd "
        "in dezelfde richting. Het stopcontact levert wisselspanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom horen oude batterijen bij het klein gevaarlijk afval?",
        opties=[
            "ze bevatten zware metalen die in het milieu terechtkomen",
            "ze bevatten nog genoeg spanning om brand te maken",
            "ze zijn te zwaar voor de gewone vuilniszak",
            "ze bevatten glas dat de zakken kan openscheuren",
        ],
        antwoord=0,
        uitleg="Zink, lithium, nikkel en soms cadmium horen niet in de grond. Bij de "
        "inzameling worden die metalen teruggewonnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over galvaniseren zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het voorwerp hangt aan de kathode",
            "er wordt een laagje metaal op het voorwerp neergeslagen",
            "het voorwerp hangt aan de anode",
            "er wordt een laagje metaal van het voorwerp afgehaald",
        ],
        antwoord=[0, 1],
        uitleg="Aan de kathode gebeurt de reductie, dus worden de metaalionen daar "
        "metaal. De anode levert die ionen aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het aanbrengen van een dun laagje zilver met elektrolyse?",
        antwoord=["verzilveren", "zilveren", "elektrolytisch verzilveren"],
        uitleg="Het voorwerp hangt aan de kathode in een oplossing van een zilverzout. De "
        "anode is van zilver en lost langzaam op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verguldt of verzilvert men juwelen in plaats van ze volledig uit dat metaal te maken?",
        opties=[
            "een dun laagje volstaat voor het uitzicht en kost veel minder",
            "zuiver goud of zilver geleidt de stroom niet goed genoeg",
            "een massief juweel zou te snel corroderen in de lucht",
            "goud en zilver zijn te zacht om een laagje te vormen",
        ],
        antwoord=0,
        uitleg="Het laagje bepaalt het uitzicht en de weerstand tegen aantasting. De kern "
        "mag van een goedkoper metaal zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat levert de anode bij het verkoperen van een voorwerp?",
        opties=[
            "koperionen, doordat ze zelf oplost",
            "elektronen, doordat ze koper opneemt",
            "zuurstofgas, doordat het water oxideert",
            "niets, want ze doet niet mee aan de reactie",
        ],
        antwoord=0,
        uitleg="Zo blijft de concentratie koperionen in het bad gelijk. Het koper "
        "verhuist dus van de anode naar het voorwerp.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij galvaniseren ligt de dikte van het laagje vast en kan je ze niet kiezen.",
        antwoord=False,
        uitleg="Je kiest ze wel: hoe langer en hoe sterker de stroom, hoe meer metaal er "
        "neerslaat. Dat volgt rechtstreeks uit het aantal elektronen dat erdoor gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een oplaadbare batterij op lange termijn goedkoper dan een gewone?",
        opties=[
            "je kan de reactie honderden keren terugduwen met een lader",
            "ze levert een veel hogere spanning per cel",
            "ze bevat geen zware metalen die ingezameld moeten worden",
            "ze raakt nooit leeg als je ze goed bewaart",
        ],
        antwoord=0,
        uitleg="Elke oplaadcyclus gaat wel een beetje slechter, want de elektroden "
        "veranderen langzaam van structuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gewone alkalinebatterij kan je veilig opladen met een lader.",
        antwoord=False,
        uitleg="Haar reactie is niet goed omkeerbaar. Er ontstaat gas, en dan kan de cel "
        "openbarsten of lekken.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stoffen voedt men aan een waterstofbrandstofcel?",
        antwoord=["waterstof en zuurstof", "waterstofgas en zuurstofgas", "H2 en O2"],
        uitleg="Het waterstofgas wordt geoxideerd aan de anode, het zuurstofgas "
        "gereduceerd aan de kathode. Er komt alleen water uit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is corrosie?",
        opties=[
            "het aantasten van een metaal door een redoxreactie met zijn omgeving",
            "het smelten van een metaal bij een te hoge temperatuur",
            "het oplossen van een metaal in een zuur zonder reactie",
            "het afslijten van een metaal door wrijving en stoten",
        ],
        antwoord=0,
        uitleg="Het metaal wordt geoxideerd, meestal door zuurstof uit de lucht. Roest op "
        "ijzer is daarvan het bekendste voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee stoffen heeft ijzer nodig om te roesten?",
        opties=[
            "zuurstof en water",
            "zuurstof en stikstof",
            "water en koolstofdioxide",
            "stikstof en waterdamp",
        ],
        antwoord=0,
        uitleg="In droge lucht of onder water zonder zuurstof roest ijzer bijna niet. "
        "Daarom roest een auto vooral in een vochtige garage.",
    ),
    dict(
        type="invultekst",
        vraag="Welke rol speelt ijzer bij het roesten: oxidator of reductor?",
        antwoord=["reductor", "de reductor", "reducens"],
        uitleg="Het staat elektronen af en wordt zelf geoxideerd. Zuurstof is hier de "
        "oxidator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom roest een auto sneller aan de kust of in de winter?",
        opties=[
            "zout maakt het water geleidend en versnelt de redoxreactie",
            "zout reageert zelf met het ijzer tot ijzerchloride",
            "zout haalt het zuurstofgas uit de lucht naar het metaal",
            "zout verhoogt de temperatuur van het natte oppervlak",
        ],
        antwoord=0,
        uitleg="De ionen laten de lading door het laagje water stromen. Daardoor kan de "
        "oxidatie op de ene plaats en de reductie op de andere gebeuren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een laag verf beschermt ijzer doordat ze het van lucht en water afsluit.",
        antwoord=True,
        uitleg="Komt er een kras in, dan begint het roesten daar wel. Daarom roest een "
        "beschadigde carrosserie net op die kras.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beschermt een laagje zink ijzer ook nog als er een kras in zit?",
        opties=[
            "zink is de sterkere reductor en wordt in plaats van het ijzer aangetast",
            "zink vult de kras op doordat het zacht genoeg is",
            "zink laat geen water meer door naar het ijzer",
            "zink maakt het ijzer onder de kras elektrisch neutraal",
        ],
        antwoord=0,
        uitleg="Het zink geeft zijn elektronen af en het ijzer blijft gespaard. Dat heet "
        "verzinken of galvaniseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een verteringselektrode zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is van een metaal dat een sterkere reductor is",
            "ze wordt opgebruikt en moet af en toe vervangen worden",
            "ze is van een metaal dat een sterkere oxidator is",
            "ze blijft onveranderd en gaat levenslang mee",
        ],
        antwoord=[0, 1],
        uitleg="Magnesium of zink aan een scheepsromp of in een boiler wordt opgegeten in "
        "plaats van het staal. Daarom hoort ze op het onderhoudsschema.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de bescherming waarbij je het metaal aan de negatieve pool legt?",
        antwoord=["kathodische bescherming", "kathodisch", "kathodische"],
        uitleg="Als kathode kan het metaal geen elektronen meer afstaan, en dus niet "
        "oxideren. Een verteringselektrode doet hetzelfde zonder spanningsbron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom roest een conservenblik juist op een kras in het tinlaagje?",
        opties=[
            "tin is een zwakkere reductor, dus wordt het ijzer aangetast",
            "tin houdt het water in de kras vast tegen het ijzer",
            "tin reageert met het ijzer op de plaats van de kras",
            "tin laat het zuurstofgas sneller door de kras heen",
        ],
        antwoord=0,
        uitleg="Bij zink is het net omgekeerd: dat wordt zelf opgegeten. Bij tin blijft "
        "het ijzer de reductor, en daar gaat het roesten snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke manieren beschermen ijzer tegen corrosie? Kruis alles aan wat juist is.",
        opties=[
            "een laagje zink erop brengen",
            "een verteringselektrode van magnesium aansluiten",
            "het metaal in zout water leggen",
            "het metaal aan de positieve pool van een bron leggen",
        ],
        antwoord=[0, 1],
        uitleg="Aan de positieve pool zou het ijzer juist de anode worden en dus sneller "
        "oxideren. Zout water versnelt het roesten.",
    ),
    dict(
        type="waarofniet",
        vraag="Roest is een laag die het metaal eronder beschermt, zoals bij aluminium.",
        antwoord=False,
        uitleg="Roest is poreus en laat water en lucht door, dus gaat het roesten verder. "
        "Bij aluminium vormt het oxide wel een dichte beschermlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom corrodeert aluminium in de praktijk zo weinig?",
        opties=[
            "er vormt zich een dicht laagje oxide dat de rest afschermt",
            "aluminium reageert niet met zuurstof uit de lucht",
            "aluminium is een zwakkere reductor dan ijzer",
            "aluminium geleidt de stroom te goed om te oxideren",
        ],
        antwoord=0,
        uitleg="Aluminium is juist een sterke reductor. Het eerste laagje oxide is zo "
        "dicht dat er niets meer bij het metaal onder komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangt men magnesiumblokken aan een stalen scheepsromp?",
        opties=[
            "het magnesium wordt opgegeten in plaats van het staal",
            "het magnesium maakt het water rond de romp minder zout",
            "het magnesium houdt het zuurstofgas van de romp weg",
            "het magnesium maakt de romp lichter in het water",
        ],
        antwoord=0,
        uitleg="Magnesium staat lager in de tabel en staat zijn elektronen eerst af. Het "
        "blok wordt daarbij opgebruikt en moet vervangen worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over roesten zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het ijzer wordt geoxideerd tot ionen",
            "het zuurstofgas wordt daarbij gereduceerd",
            "het ijzer wordt gereduceerd tot ionen",
            "het water wordt daarbij geoxideerd",
        ],
        antwoord=[0, 1],
        uitleg="Water is nodig als midden waarin de ionen kunnen bewegen, maar het "
        "verandert zelf niet van oxidatiegetal.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het aanbrengen van een laagje zink op staal?",
        antwoord=["verzinken", "galvaniseren", "verzinking"],
        uitleg="Dat gebeurt door onderdompelen in gesmolten zink of met elektrolyse. "
        "Dakgoten en schroeven zijn vaak zo behandeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een boiler langer mee met een anode van magnesium erin?",
        opties=[
            "de anode wordt aangetast in plaats van de stalen wand",
            "de anode warmt het water sneller op dan het staal",
            "de anode houdt het kalk uit het water tegen",
            "de anode maakt het water in de boiler basisch",
        ],
        antwoord=0,
        uitleg="Dat is kathodische bescherming met een verteringselektrode. Bij een "
        "onderhoud wordt ze nagekeken en vervangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beschermt vet of olie op een gereedschap tegen roest?",
        opties=[
            "het laagje houdt water en zuurstof van het metaal weg",
            "het laagje is zelf een sterkere reductor dan het ijzer",
            "het laagje geleidt de elektronen weg van het metaal",
            "het laagje reageert met het ijzer tot een oxidelaag",
        ],
        antwoord=0,
        uitleg="Het werkt net als verf: een barrière. Het beschermt dus niet meer zodra "
        "het laagje weg is.",
    ),
    dict(
        type="waarofniet",
        vraag="Kathodische bescherming kan ook zonder spanningsbron, met een onedeler metaal.",
        antwoord=True,
        uitleg="Dat is net wat een verteringselektrode doet. Het verschil in "
        "normpotentiaal levert zelf de nodige spanning.",
    ),
    dict(
        type="waarofniet",
        vraag="Een metaal dat laag in de tabel van de normpotentialen staat, corrodeert moeilijker.",
        antwoord=False,
        uitleg="Het is net omgekeerd: laag betekent een sterke reductor, dus makkelijk te "
        "oxideren. Goud en platina staan hoog en corroderen bijna niet.",
    ),
    dict(
        type="invultekst",
        vraag="Welk metaal wordt het meest gebruikt als verteringselektrode?",
        antwoord=["magnesium", "zink", "Mg"],
        uitleg="Zowel magnesium als zink zijn sterkere reductoren dan ijzer. Welk van de "
        "twee men kiest, hangt af van het water of de grond errond.",
    ),
]
