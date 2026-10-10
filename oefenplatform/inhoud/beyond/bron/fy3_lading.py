# -*- coding: utf-8 -*-
r"""Elektrische lading, geleiders en influentie — 🌍 Beyond, fysica.

Deel 1 gaat over lading zelf: de grootheid \(Q\) en haar eenheid, de
elementaire lading, het verschil tussen een geleider en een isolator op
atomaire schaal, en laden door wrijving met de tribo-elektrische reeks erbij.
Deel 2 gaat over de twee andere manieren om te laden: door contact, waarbij de
lading zich over de voorwerpen verdeelt, en door influentie, met en zonder
aarding, plus de toepassingen in technische systemen.

Het verhaal van dit thema is telkens hetzelfde: lading ontstaat niet, ze
verhuist. Alleen elektronen bewegen, en elke vraag naar het teken van een
voorwerp is dus een vraag naar welke kant die elektronen op gegaan zijn.

In echte wetenschappelijke notatie, tussen \( en \); zie
oefenplatform/lib/wiskunde.ts. Enya Vermeyen, leerkracht wiskunde en fysica,
schreef op 10 oktober 2026 dat het symbool \(Q\) voor de grootheid elektrische
lading nergens in dit hoofdstuk stond, en dat er daardoor nuances ontbreken
waar een leerkracht fysica wel op let. Ze had gelijk: de hele tekst sprak over
"lading" en noemde enkel de eenheid. \(Q\), \(e\) en het verband \(Q=n\cdot e\)
staan er nu in, met rekenvragen erbij.

De elementaire lading \(e=1{,}602\cdot 10^{-19}\ \text{C}\) staat in het
formularium dat het kind op het examen krijgt, dus de vragen geven ze mee waar
ze nodig is.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk deeltje verhuist er als een voorwerp elektrisch geladen wordt?",
        opties=[
            "het elektron, want dat zit het losst van de kern",
            "het proton, want dat draagt de positieve lading",
            "het neutron, want dat is ongeladen en beweegt vlot",
            "de hele atoomkern, met de protonen erin",
        ],
        antwoord=0,
        uitleg="Protonen zitten vast in de kern en kunnen niet verhuizen. Een voorwerp "
        "wordt dus negatief door elektronen bij te krijgen, en positief door er te "
        "verliezen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruik je voor de grootheid elektrische lading? Schrijf de letter.",
        antwoord=["Q", "q"],
        uitleg=r"De grootheid is \(Q\), de eenheid is de coulomb met symbool \(\text{C}\). "
        r"Let op het verschil: \(Q\) is wat je meet, \(\text{C}\) is waarin je het uitdrukt.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je elektrische lading uit?",
        antwoord=["coulomb", "C", "de coulomb"],
        uitleg=r"Het symbool is \(\text{C}\). Je schrijft dus bijvoorbeeld "
        r"\(Q=-8\ \text{nC}\), en dat lees je als een lading van min acht nanocoulomb.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe groot is de elementaire lading \(e\)?",
        opties=[
            r"\(1{,}602\cdot 10^{-19}\ \text{C}\)",
            r"\(1{,}602\cdot 10^{-19}\ \text{kg}\)",
            r"\(9{,}109\cdot 10^{-31}\ \text{C}\)",
            r"\(6{,}022\cdot 10^{23}\ \text{C}\)",
        ],
        antwoord=0,
        uitleg=r"Dat is de lading van één proton, en op het teken na ook die van één "
        r"elektron. \(9{,}109\cdot 10^{-31}\ \text{kg}\) is de massa van een elektron en "
        r"\(6{,}022\cdot 10^{23}\) is het getal van Avogadro.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een voorwerp heeft \(5{,}0\cdot 10^{12}\) elektronen te veel. Hoe groot is \(Q\)? "
        r"Neem \(e=1{,}602\cdot 10^{-19}\ \text{C}\).",
        opties=[
            r"\(-8{,}0\cdot 10^{-7}\ \text{C}\)",
            r"\(+8{,}0\cdot 10^{-7}\ \text{C}\)",
            r"\(-5{,}0\cdot 10^{12}\ \text{C}\)",
            r"\(-3{,}1\cdot 10^{31}\ \text{C}\)",
        ],
        antwoord=0,
        uitleg=r"\(Q=n\cdot e=5{,}0\cdot 10^{12}\cdot 1{,}602\cdot 10^{-19}\ \text{C}"
        r"\approx 8{,}0\cdot 10^{-7}\ \text{C}\), en te véél elektronen betekent een "
        r"negatief teken. De laatste optie is wat je krijgt als je deelt in plaats van "
        r"vermenigvuldigt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bolletje draagt \(Q=8\ \text{nC}\). Hoeveel coulomb is dat?",
        opties=[
            r"\(8\cdot 10^{-9}\ \text{C}\)",
            r"\(8\cdot 10^{-6}\ \text{C}\)",
            r"\(8\cdot 10^{-12}\ \text{C}\)",
            r"\(8\cdot 10^{9}\ \text{C}\)",
        ],
        antwoord=0,
        uitleg=r"Nano betekent \(10^{-9}\). Micro is \(10^{-6}\) en pico is \(10^{-12}\); "
        r"in de elektrostatica kom je die drie alle drie tegen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De lading van een voorwerp is altijd een geheel veelvoud van \(e\).",
        antwoord=True,
        uitleg=r"Lading komt in pakjes: \(Q=n\cdot e\) met \(n\) een geheel getal. Je kan "
        r"er geen half elektron bij of af doen. Dat heet de kwantisatie van de lading.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een geleider en een isolator op atomaire schaal?",
        opties=[
            "een geleider heeft vrije elektronen, een isolator niet",
            "een geleider heeft meer protonen in zijn kernen dan een isolator",
            "een geleider heeft een groter aantal neutronen per atoom",
            "een geleider heeft atomen die dichter op elkaar gepakt zitten",
        ],
        antwoord=0,
        uitleg="In een metaal zijn de buitenste elektronen niet aan één atoom gebonden en "
        "kunnen ze door het hele rooster bewegen. In een isolator zit elk elektron vast "
        "bij zijn eigen atoom.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de elektronen in een metaal die niet aan één atoom vastzitten?",
        antwoord=["vrije elektronen", "vrije", "geleidingselektronen"],
        uitleg="Zij maken een metaal tot een geleider. Een isolator heeft ze niet, en "
        "daarom blijft lading daar zitten waar je ze zet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met lading die je op een geleider aanbrengt?",
        opties=[
            "ze verspreidt zich meteen over het hele oppervlak",
            "ze blijft zitten op de plaats waar je ze aanbracht",
            "ze zakt naar het zwaartepunt van het voorwerp toe",
            "ze verdwijnt binnen enkele seconden volledig weg",
        ],
        antwoord=0,
        uitleg="De gelijke ladingen stoten elkaar af en de vrije elektronen kunnen bewegen, "
        "dus gaan ze zo ver mogelijk uit elkaar. Op een isolator blijft de lading wel "
        "plaatselijk staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn goede geleiders? Kruis alles aan wat juist is.",
        opties=[
            "koper",
            "aluminium",
            "glas",
            "rubber",
        ],
        antwoord=[0, 1],
        uitleg="Metalen hebben vrije elektronen en geleiden dus. Glas en rubber zijn "
        "isolatoren, en daarom zit het handvat van gereedschap in kunststof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een isolator zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de elektronen blijven bij hun eigen atoom zitten",
            "de aangebrachte lading blijft plaatselijk staan",
            "de elektronen bewegen er vrij door het materiaal",
            "de aangebrachte lading verdwijnt er meteen weer",
        ],
        antwoord=[0, 1],
        uitleg="Zonder vrije elektronen kan de lading niet weglopen of zich verspreiden. "
        "Daarom kan je op een kunststof staaf één kant laden en de andere niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wrijft een pvc-staaf met een wollen doek. Wat gebeurt er?",
        opties=[
            "de staaf wordt negatief en de doek wordt positief",
            "de staaf wordt positief en de doek wordt negatief",
            "beide worden negatief door de wrijvingswarmte",
            "beide blijven neutraal, want wrijven laadt niet op",
        ],
        antwoord=0,
        uitleg="Pvc trekt elektronen harder aan dan wol, dus komen er elektronen op de "
        "staaf terecht. De doek blijft met evenveel positieve lading achter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de tribo-elektrische reeks?",
        opties=[
            "om te zien welke stof bij wrijving elektronen opneemt",
            "om te zien hoeveel stroom er door een stof kan lopen",
            "om de weerstand van een stof bij warmte af te lezen",
            "om de spanning tussen twee geladen platen te bepalen",
        ],
        antwoord=0,
        uitleg="De stoffen staan gerangschikt van elektronenafstaand naar elektronenopnemend. "
        "De stof die lager in de reeks staat, wordt bij wrijving negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een geladen voorwerp zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "negatief betekent dat er elektronen bij gekomen zijn",
            "positief betekent dat er elektronen weggegaan zijn",
            "positief betekent dat er protonen bij gekomen zijn",
            "negatief betekent dat er protonen weggegaan zijn",
        ],
        antwoord=[0, 1],
        uitleg="Alleen elektronen bewegen. Een tekort aan elektronen laat de positieve "
        "lading van de kernen overheersen, en dat noemen we positief geladen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Wrijf je twee voorwerpen tegen elkaar, dan geldt achteraf \(Q_{1}=-Q_{2}\).",
        antwoord=True,
        uitleg=r"Wat het ene verliest, wint het andere, dus \(Q_{1}+Q_{2}=0\), net als voor "
        r"het wrijven. Dat is het behoud van lading.",
    ),
    dict(
        type="waarofniet",
        vraag="Een isolator kan je niet elektrisch laden.",
        antwoord=False,
        uitleg="Je kan een isolator juist heel goed laden, bijvoorbeeld door wrijving. De "
        "lading blijft er alleen plaatselijk zitten in plaats van zich te verspreiden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een neutraal voorwerp bevat helemaal geen lading.",
        antwoord=False,
        uitleg=r"Het bevat er enorm veel, maar evenveel positieve als negatieve, dus "
        r"\(Q=0\) in totaal. Neutraal is geen derde soort lading maar een evenwicht tussen "
        r"de twee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het toestel met twee blaadjes dat aantoont dat een voorwerp geladen is?",
        antwoord=["elektroscoop", "een elektroscoop", "de elektroscoop"],
        uitleg="De twee blaadjes krijgen dezelfde lading en stoten elkaar daarom af. Hoe "
        "groter de lading, hoe verder ze uit elkaar staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wijken de blaadjes van een elektroscoop uit elkaar?",
        opties=[
            "ze dragen dezelfde lading en stoten elkaar daarom af",
            "ze dragen een andere lading en trekken elkaar dus aan",
            "de lucht ertussen wordt door de lading opgewarmd",
            "het metaal zet uit zodra er lading op gebracht wordt",
        ],
        antwoord=0,
        uitleg="De lading verdeelt zich over het hele metaal, dus ook over de twee "
        "blaadjes. Gelijke ladingen stoten elkaar af, en de blaadjes wijken uit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je raakt een neutrale metalen bol aan met een negatief geladen staaf. Wat gebeurt er?",
        opties=[
            "er lopen elektronen naar de bol en die wordt negatief",
            "er lopen elektronen naar de staaf en de bol wordt positief",
            "er lopen protonen naar de bol en die wordt positief",
            "er gebeurt niets, want de bol was ervoor neutraal",
        ],
        antwoord=0,
        uitleg="De elektronen op de staaf stoten elkaar af en verspreiden zich over het "
        "metaal dat erbij komt. Na het contact dragen staaf en bol dezelfde soort lading.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee gelijke metalen bollen met \(Q_{1}=+12\ \text{nC}\) en "
        r"\(Q_{2}=-4\ \text{nC}\) raken elkaar even aan. Welke lading draagt elke bol daarna?",
        opties=[
            r"\(+4\ \text{nC}\)",
            r"\(+8\ \text{nC}\)",
            r"\(+16\ \text{nC}\)",
            r"\(0\ \text{nC}\)",
        ],
        antwoord=0,
        uitleg=r"Lading blijft behouden, dus de som blijft "
        r"\(Q_{1}+Q_{2}=+12-4=+8\ \text{nC}\). Over twee even grote bollen verdeelt die "
        r"zich eerlijk: elk \(+4\ \text{nC}\). Zijn de bollen niet even groot, dan krijgt "
        r"de grootste een groter deel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel waarbij een geladen voorwerp de lading in een ander voorwerp verschuift zonder het aan te raken?",
        antwoord=["influentie", "elektrostatische influentie", "inductie"],
        uitleg="Men spreekt ook van elektrostatische inductie. Bij een isolator heet de "
        "kleinere versie ervan polarisatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een geleider die je in de buurt van een negatief geladen staaf brengt?",
        opties=[
            "de vrije elektronen worden naar de verste kant geduwd",
            "de vrije elektronen worden naar de dichtste kant getrokken",
            "de protonen schuiven naar de kant van de staaf toe",
            "er verandert niets zolang je de staaf niet aanraakt",
        ],
        antwoord=0,
        uitleg="Gelijke ladingen stoten elkaar af, dus vluchten de elektronen weg van de "
        "staaf. De dichtste kant blijft positief achter, en juist daardoor trekt de staaf "
        "de geleider aan.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een voorwerp dat enkel door influentie beïnvloed werd, heeft achteraf \(Q\neq 0\).",
        antwoord=False,
        uitleg=r"De lading is enkel verschoven: de ene kant is positief, de andere negatief, "
        r"en samen is dat nog altijd \(Q=0\). Haal je de staaf weg, dan verdeelt alles zich "
        r"weer gelijkmatig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen influentie bij een geleider en bij een isolator?",
        opties=[
            "bij een geleider verhuizen de elektronen door het hele voorwerp",
            "bij een isolator verhuizen de elektronen door het hele voorwerp",
            "bij een geleider gebeurt er niets, bij een isolator wel iets",
            "bij een isolator keren de atoomkernen zich volledig om",
        ],
        antwoord=0,
        uitleg="In een isolator kunnen de elektronen hun atoom niet verlaten; de ladingen "
        "verschuiven er alleen een klein beetje binnen elk molecule. Zo ontstaan er "
        "dipolen, en dat heet polarisatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een molecule waarvan de ene kant lichtpositief en de andere lichtnegatief is?",
        antwoord=["dipool", "een dipool", "dipolen"],
        uitleg="Bij polarisatie van een isolator worden de moleculen zulke dipolen. Ze "
        "draaien zich met hun aangetrokken kant naar de geladen staaf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je houdt een negatieve staaf bij een metalen bol, aardt de bol even en haalt dan de staaf weg. Hoe is de bol geladen?",
        opties=[
            "positief, want er liepen elektronen naar de aarde weg",
            "negatief, want er liepen elektronen van de staaf op",
            "neutraal, want de aarding maakt alles weer neutraal",
            "negatief, want de aarde stuurt elektronen naar de bol",
        ],
        antwoord=0,
        uitleg="De staaf duwde de elektronen naar de verste kant, en via de aarding konden "
        "die wegvluchten. Wat overblijft is een tekort aan elektronen, dus een positieve "
        "bol: laden door influentie geeft het tegengestelde teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke manieren kan je een voorwerp elektrisch laden? Kruis alles aan wat juist is.",
        opties=[
            "door het met een andere stof te wrijven",
            "door het met een geladen voorwerp aan te raken",
            "door influentie met een aarding erbij",
            "door het voorwerp op te warmen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opwarmen verplaatst geen elektronen van of naar het voorwerp. Op een vochtige "
        "dag lekt de lading trouwens snel via het water in de lucht weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Laden door contact geeft het voorwerp dezelfde soort lading als het geladen voorwerp.",
        antwoord=True,
        uitleg="De lading verdeelt zich over beide, dus is het teken gelijk. Bij laden door "
        "influentie met aarding krijg je net het tegengestelde teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom trekt een geladen staaf ook een neutraal stukje papier aan?",
        opties=[
            "de lading in het papier verschuift en de dichtste kant trekt",
            "het papier geeft zijn elektronen volledig aan de staaf af",
            "de lucht tussen staaf en papier duwt het stukje omhoog",
            "papier draagt altijd een kleine lading van zichzelf mee",
        ],
        antwoord=0,
        uitleg=r"Door polarisatie komt de tegengestelde lading het dichtst bij de staaf te "
        r"liggen. Omdat de kracht met \(\tfrac{1}{r^{2}}\) afneemt, weegt die dichte kant "
        r"zwaarder door dan de afstoting van de verdere kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over influentie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de ladingen in een geleider verschuiven naar één kant",
            "het voorwerp blijft in totaal even geladen als ervoor",
            "in een isolator draaien de moleculen zich een beetje",
            "het voorwerp wordt er netto negatief door geladen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Er komt geen lading bij of af, ze schuift enkel op. Aard je het voorwerp "
        "wel even, dan houdt het achteraf een echte lading over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen berusten op elektrostatica? Kruis alles aan wat juist is.",
        opties=[
            "een fotokopieertoestel",
            "poedercoating van metaal",
            "een gloeilamp in de keuken",
            "een gewone veer in een pen",
        ],
        antwoord=[0, 1],
        uitleg="Ook stoffilters, luchtzuivering en reinigingsdoekjes die stof aantrekken "
        "werken zo: geladen deeltjes worden naar een tegengesteld geladen oppervlak "
        "getrokken.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschuiven van de ladingen binnen de moleculen van een isolator?",
        antwoord=["polarisatie", "polariseren", "de polarisatie"],
        uitleg="De moleculen worden dipolen en richten zich naar het geladen voorwerp. In "
        "een geleider verhuizen de vrije elektronen in plaats daarvan door het hele stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt poedercoating met geladen poeder beter dan gewoon spuiten?",
        opties=[
            "het geladen poeder wordt naar het hele werkstuk getrokken",
            "het geladen poeder weegt minder en blijft dus beter hangen",
            "het geladen poeder droogt sneller op door de lading erin",
            "het geladen poeder kleurt dieper dan ongeladen poeder",
        ],
        antwoord=0,
        uitleg="Het werkstuk is tegengesteld geladen, dus buigen de poederdeeltjes mee rond "
        "de randen. Daardoor raakt ook de achterkant bedekt en gaat er veel minder poeder "
        "verloren.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een kopieertoestel wordt de toner met een laagje lijm op het papier gebracht.",
        antwoord=False,
        uitleg="Er komt geen lijm aan te pas: op de trommel staat een ladingspatroon van "
        "het beeld, en het geladen tonerpoeder blijft precies daar kleven. Warmte smelt "
        "het daarna vast in het papier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laadt een elektroscoop door contact met een negatieve staaf. Wat zie je daarna?",
        opties=[
            "de blaadjes blijven uit elkaar staan",
            "de blaadjes vallen meteen weer samen",
            "de blaadjes wijken uit en vallen dan samen",
            "de blaadjes blijven precies zoals ze waren",
        ],
        antwoord=0,
        uitleg="Door het contact houdt de elektroscoop zelf lading over, en die blijft op "
        "het metaal staan. Bij influentie zonder contact vallen de blaadjes wel weer "
        "samen zodra je de staaf weghaalt.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een geleider door influentie laden zonder hem ooit aan te raken met het geladen voorwerp.",
        antwoord=True,
        uitleg="Je hebt wel een aarding nodig terwijl het geladen voorwerp in de buurt is. "
        "De geleider houdt dan het tegengestelde teken over.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bol draagt \(Q=-4{,}8\cdot 10^{-9}\ \text{C}\). Hoeveel elektronen zitten "
        r"er te veel op? Neem \(e=1{,}602\cdot 10^{-19}\ \text{C}\).",
        opties=[
            r"\(3{,}0\cdot 10^{10}\)",
            r"\(7{,}7\cdot 10^{-28}\)",
            r"\(3{,}0\cdot 10^{-10}\)",
            r"\(4{,}8\cdot 10^{9}\)",
        ],
        antwoord=0,
        uitleg=r"Uit \(Q=n\cdot e\) volgt \(n=\dfrac{|Q|}{e}="
        r"\dfrac{4{,}8\cdot 10^{-9}}{1{,}602\cdot 10^{-19}}\approx 3{,}0\cdot 10^{10}\). "
        r"De tweede optie krijg je als je vermenigvuldigt in plaats van deelt. Een aantal "
        r"deeltjes kan nooit kleiner dan één zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Welk teken draagt een voorwerp dat elektronen verloren heeft?",
        antwoord=["positief", "plus", "een positief teken"],
        uitleg="De positieve lading van de kernen is dan niet meer in evenwicht. Een "
        "voorwerp met te veel elektronen is negatief.",
    ),
]
