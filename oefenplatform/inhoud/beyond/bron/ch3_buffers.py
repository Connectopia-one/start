# -*- coding: utf-8 -*-
"""Buffers en zuurbasetitraties — 🌍 Beyond, chemie.

Deel 1 gaat over de buffer: waaraan je een buffermengsel herkent, hoe het werkt
als je zuur of base toevoegt, het verschil tussen een zure en een basische
buffer, en wanneer een buffer optimaal is en binnen welk bereik hij werkt.
Deel 2 gaat over de titratie: het equivalentiepunt op een titratiecurve, het
verloop van de pH, de keuze van een indicator, het correct uitvoeren en aflezen,
en wat een fout bij de uitvoering met het resultaat doet.

Een titratiecurve staat in een vraag op het scherm niet. Daarom beschrijven de
vragen de curve in woorden: waar de sprong ligt, hoe steil ze is en bij welke pH
ze eindigt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat een buffermengsel?",
        opties=[
            "een zwak zuur samen met zijn geconjugeerde base",
            "een sterk zuur samen met zijn geconjugeerde base",
            "een sterk zuur samen met een sterke base",
            "een zwak zuur samen met een sterke base",
        ],
        antwoord=0,
        uitleg="Beide deeltjes moeten in vergelijkbare hoeveelheden aanwezig zijn. Een "
        "mengsel van azijnzuur met natriumacetaat is daarvan het schoolvoorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een buffer als je er een beetje sterk zuur bij giet?",
        opties=[
            "de geconjugeerde base neemt de hydroxoniumionen weg",
            "het zwakke zuur neemt de hydroxoniumionen weg",
            "de pH daalt even sterk als in zuiver water",
            "het mengsel stopt met werken en valt uiteen",
        ],
        antwoord=0,
        uitleg="De base van het paar vangt het proton op en wordt zelf het zwakke zuur. "
        "Daardoor blijft de pH bijna gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een mengsel dat de pH bijna gelijk houdt als je zuur of base toevoegt?",
        antwoord=["buffer", "een buffer", "buffermengsel"],
        uitleg="Een buffer vangt beide kanten op: het zuur van het paar neemt base weg, "
        "de base van het paar neemt zuur weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke mengsels zijn buffers? Kruis alles aan wat juist is.",
        opties=[
            "azijnzuur met natriumacetaat",
            "ammoniak met ammoniumchloride",
            "zoutzuur met natriumchloride",
            "zoutzuur met natriumhydroxide",
        ],
        antwoord=[0, 1],
        uitleg="Het eerste is een zure buffer, het tweede een basische. Een sterk zuur "
        "met zijn zout buffert niet, want het chloride-ion neemt geen protonen op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een buffer houdt de pH precies gelijk, hoeveel zuur je er ook bij giet.",
        antwoord=False,
        uitleg="Hij vangt het op zolang er genoeg van beide deeltjes is. Giet je te veel "
        "bij, dan is de buffer uitgeput en schiet de pH weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer werkt een buffer het best?",
        opties=[
            "als het zuur en zijn geconjugeerde base in dezelfde concentratie aanwezig zijn",
            "als er veel meer zuur dan geconjugeerde base aanwezig is",
            "als het zuur zo sterk mogelijk is bij dezelfde concentratie",
            "als de oplossing zo verdund mogelijk gemaakt is",
        ],
        antwoord=0,
        uitleg="Dan kan hij naar beide kanten evenveel opvangen, en dan is de pH gelijk "
        "aan de pKz van het zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een buffer is gemaakt met een zuur met pKz 5. Binnen welk pH-gebied werkt hij goed?",
        opties=[
            "ongeveer tussen pH 4 en pH 6",
            "ongeveer tussen pH 1 en pH 9",
            "ongeveer tussen pH 6 en pH 8",
            "enkel precies bij pH 5",
        ],
        antwoord=0,
        uitleg="Het bereik is ongeveer de pKz plus of min één eenheid. Daarbuiten is een "
        "van de twee deeltjes bijna op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een basische buffer zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "hij bestaat uit een zwakke base met haar geconjugeerde zuur",
            "zijn pH ligt boven zeven",
            "hij bestaat uit een sterke base met haar zout",
            "zijn pH ligt onder zeven",
        ],
        antwoord=[0, 1],
        uitleg="Ammoniak met ammoniumchloride is zo'n buffer. Een sterke base met haar "
        "zout werkt niet, want het geconjugeerde zuur is dan te zwak.",
    ),
    dict(
        type="invultekst",
        vraag="Welke pH heeft een buffer waarin zuur en base in gelijke concentratie zitten?",
        antwoord=["pKz", "de pKz", "gelijk aan pKz"],
        uitleg="Dan vallen de twee concentraties in de uitdrukking tegen elkaar weg. Zo "
        "kies je een zuur met de pKz die je nodig hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft de pH van bloed zo constant?",
        opties=[
            "koolzuur en het waterstofcarbonaation vormen er een buffer",
            "het bloed bevat heel veel zuiver water om te verdunnen",
            "de nieren halen alle zuren direct uit het bloed weg",
            "het bloed bevat een sterke base die alles neutraliseert",
        ],
        antwoord=0,
        uitleg="Dat paar houdt de pH rond 7,4. Een afwijking van een paar tienden is al "
        "levensgevaarlijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Verdunnen verandert de pH van een buffer bijna niet.",
        antwoord=True,
        uitleg="De verhouding tussen zuur en base blijft gelijk, en die bepaalt de pH. De "
        "capaciteit van de buffer wordt wel kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een buffer als je een beetje sterke base toevoegt?",
        opties=[
            "het zwakke zuur van het paar neemt de hydroxide-ionen weg",
            "de geconjugeerde base van het paar neemt de hydroxide-ionen weg",
            "de hydroxide-ionen blijven vrij in de oplossing zitten",
            "de pH stijgt even sterk als in zuiver water",
        ],
        antwoord=0,
        uitleg="Het zuur staat zijn proton af aan OH⁻, en daarbij ontstaat water. Zo "
        "verdwijnt de base bijna helemaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen kan je mengen om een buffer rond pH 9 te maken?",
        opties=[
            "ammoniak met ammoniumchloride",
            "azijnzuur met natriumacetaat",
            "zoutzuur met natriumchloride",
            "zwavelzuur met natriumsulfaat",
        ],
        antwoord=0,
        uitleg="Het ammoniumion heeft een pKz van ongeveer 9,2, dus ligt het bereik van "
        "die buffer rond pH 9. Azijnzuur zou je rond pH 5 brengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de capaciteit van een buffer zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze is groter als de concentraties hoger zijn",
            "ze is op als een van de twee deeltjes verbruikt is",
            "ze is groter als de buffer meer verdund is",
            "ze is onbeperkt zolang het paar aanwezig is",
        ],
        antwoord=[0, 1],
        uitleg="Een buffer van 1 mol/L vangt veel meer op dan een van 0,01 mol/L, ook al "
        "hebben ze dezelfde pH.",
    ),
    dict(
        type="invultekst",
        vraag="Welk geconjugeerd paar buffert het bloed?",
        antwoord=["koolzuur en waterstofcarbonaat", "H2CO3 en HCO3-", "koolzuurbuffer"],
        uitleg="Door sneller te ademen verlies je koolstofdioxide, en dat verschuift dat "
        "evenwicht. Zo regelt het lichaam de pH mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mengt een zwak zuur met een sterke base, maar niet genoeg base om alles weg te werken. Wat krijg je?",
        opties=[
            "een buffer van het zwakke zuur met zijn geconjugeerde base",
            "een neutrale oplossing van een zout in water",
            "een sterk zure oplossing zonder bufferwerking",
            "een sterk basische oplossing met een overmaat base",
        ],
        antwoord=0,
        uitleg="De base zet een deel van het zuur om in zijn geconjugeerde base. Zo zitten "
        "beide deeltjes in dezelfde beker, en dat is precies een buffer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom buffert een mengsel van zoutzuur en natriumchloride niet?",
        opties=[
            "het chloride-ion is een te zwakke base om protonen op te nemen",
            "het chloride-ion is een te sterke base en neemt alles op",
            "zoutzuur is te verdund om een buffer te kunnen vormen",
            "natriumchloride lost niet goed genoeg op in water",
        ],
        antwoord=0,
        uitleg="Een buffer heeft een paar nodig dat beide kanten op kan. Bij een sterk "
        "zuur is de geconjugeerde base daarvoor te zwak.",
    ),
    dict(
        type="waarofniet",
        vraag="Een buffer werkt enkel tegen toegevoegd zuur, niet tegen toegevoegde base.",
        antwoord=False,
        uitleg="Hij werkt naar twee kanten: de base van het paar vangt zuur op, het zuur "
        "van het paar vangt base op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een buffer met pKz 7 is geschikt om een oplossing rond pH 7 te houden.",
        antwoord=True,
        uitleg="Het bereik van een buffer ligt rond de pKz van zijn zuur. Daarom kies je "
        "het zuur op basis van de pH die je nodig hebt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel pH-eenheden rond de pKz werkt een buffer ongeveer?",
        antwoord=["een", "één", "1"],
        uitleg="Buiten dat bereik van plus of min één is de verhouding tussen zuur en "
        "base te scheef geworden.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het equivalentiepunt van een zuurbasetitratie?",
        opties=[
            "het punt waarop er precies genoeg base is voor al het zuur",
            "het punt waarop de indicator van kleur begint te veranderen",
            "het punt waarop de pH van de oplossing precies zeven is",
            "het punt waarop de buret helemaal leeg gelopen is",
        ],
        antwoord=0,
        uitleg="Daar is het aantal mol base gelijk aan het aantal mol zuur, met de "
        "waardigheid meegerekend. De pH is daar niet altijd zeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je het equivalentiepunt op een titratiecurve?",
        opties=[
            "aan de steile sprong in de pH, midden in het verloop",
            "aan het vlakke begin van de kromme bij lage pH",
            "aan het vlakke einde van de kromme bij hoge pH",
            "aan het snijpunt van de kromme met de verticale as",
        ],
        antwoord=0,
        uitleg="Rond dat punt verandert de pH heel snel bij een paar druppels titrans. "
        "Het midden van die sprong is het equivalentiepunt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de oplossing die je uit de buret laat lopen?",
        antwoord=["titrans", "het titrans", "titreervloeistof"],
        uitleg="Haar concentratie moet nauwkeurig gekend zijn. De onbekende oplossing "
        "staat in de erlenmeyer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke pH ligt het equivalentiepunt van een sterk zuur met een sterke base?",
        opties=[
            "bij pH 7, want er blijft een neutraal zout over",
            "boven pH 7, want er blijft een basisch zout over",
            "onder pH 7, want er blijft een zuur zout over",
            "dat is niet te voorspellen zonder de constanten",
        ],
        antwoord=0,
        uitleg="Beide ionen van het zout reageren niet meer met water. Bij een zwak zuur "
        "met een sterke base ligt het punt boven zeven.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de titratie van een zwak zuur met een sterke base ligt het equivalentiepunt boven pH 7.",
        antwoord=True,
        uitleg="Er blijft de geconjugeerde base van een zwak zuur over, en die maakt de "
        "oplossing basisch. Daarom past fenolftaleïen daar goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kies je een geschikte indicator voor een titratie?",
        opties=[
            "haar omslaggebied moet binnen de pH-sprong van de curve vallen",
            "haar omslaggebied moet precies bij pH 7 liggen",
            "ze moet dezelfde kleur hebben als de te titreren oplossing",
            "ze moet een sterker zuur zijn dan het zuur dat je titreert",
        ],
        antwoord=0,
        uitleg="Dan valt de kleuromslag samen met het equivalentiepunt. Een indicator die "
        "ernaast ligt, geeft een verkeerd volume.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het aflezen van een buret zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "je leest af bij de onderkant van de meniscus",
            "je houdt je oog op dezelfde hoogte als de vloeistof",
            "je leest af bij de bovenkant van de meniscus",
            "je leest af terwijl je de buret schuin houdt",
        ],
        antwoord=[0, 1],
        uitleg="Scheef aflezen geeft een parallaxfout. De schaal van een buret loopt van "
        "boven naar onder, dus reken altijd het verschil uit.",
    ),
    dict(
        type="invultekst",
        vraag="Met welke vloeistof spoel je de buret voor je begint?",
        antwoord=["met titrans", "titrans", "de titreervloeistof"],
        uitleg="Water zou het titrans verdunnen en dus een te groot volume geven. De "
        "erlenmeyer mag wel nat zijn van water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag de erlenmeyer nat zijn van water, en de buret niet?",
        opties=[
            "water verandert het aantal mol in de erlenmeyer niet",
            "water verdampt in de erlenmeyer tijdens de titratie",
            "de erlenmeyer heeft geen nauwkeurige schaal nodig",
            "water reageert alleen met het titrans uit de buret",
        ],
        antwoord=0,
        uitleg="In de erlenmeyer gaat het om mol, niet om concentratie. In de buret zou "
        "water het titrans verdunnen en dus de concentratie veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom doe je eerst een proeftitratie?",
        opties=[
            "om ongeveer te weten waar de sprong ligt, zodat je daarna traag kan druppelen",
            "om de buret op te warmen voor de echte metingen",
            "om de indicator te laten reageren met het glaswerk",
            "om het titrans te laten mengen met de lucht in de buret",
        ],
        antwoord=0,
        uitleg="Bij de echte titratie kan je dan vlak voor het equivalentiepunt druppel "
        "per druppel werken. Zo mis je de omslag niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het equivalentiepunt en het punt van de kleuromslag zijn altijd precies hetzelfde.",
        antwoord=False,
        uitleg="Ze vallen bijna samen als je de juiste indicator kiest. Het punt van de "
        "omslag heet het eindpunt, en dat ligt er meestal een druppel naast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je titreert 20 mL zuur met 0,1 mol/L base en verbruikt 20 mL. Wat is de concentratie van het zuur, als het eenwaardig is?",
        opties=[
            "0,1 mol/L",
            "0,2 mol/L",
            "0,05 mol/L",
            "0,02 mol/L",
        ],
        antwoord=0,
        uitleg="Gelijke volumes en gelijke waardigheid betekent gelijke concentratie: "
        "0,1 maal 0,020 is 0,002 mol base, dus ook 0,002 mol zuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je titreert 20 mL van een tweewaardig zuur met 0,1 mol/L base en verbruikt 40 mL. Wat is de concentratie van het zuur?",
        opties=[
            "0,1 mol/L",
            "0,2 mol/L",
            "0,05 mol/L",
            "0,4 mol/L",
        ],
        antwoord=0,
        uitleg="0,004 mol base neutraliseert 0,002 mol tweewaardig zuur. Dat is 0,002 "
        "gedeeld door 0,020 liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fouten geven een te groot volume titrans? Kruis alles aan wat juist is.",
        opties=[
            "de buret is met water gespoeld en niet met titrans",
            "je druppelt door na de kleuromslag",
            "je pipetteert te weinig van de onbekende oplossing",
            "je leest de buret af bij de bovenkant van de meniscus",
        ],
        antwoord=[0, 1],
        uitleg="Verdund titrans en doordruppelen geven beide een te hoog volume, en dus "
        "een te hoge berekende concentratie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk glaswerk gebruik je om precies 20 mL van de onbekende oplossing af te meten?",
        antwoord=["pipet", "een pipet", "maatpipet"],
        uitleg="Een pipet is veel nauwkeuriger dan een maatbeker. Je vult ze met een "
        "pipetvuller, nooit met de mond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de pH-sprong als je een verdunder zuur titreert?",
        opties=[
            "de sprong wordt kleiner en minder steil",
            "de sprong wordt groter en steiler dan ervoor",
            "de sprong verdwijnt helemaal uit de curve",
            "de sprong verschuift naar een veel hogere pH",
        ],
        antwoord=0,
        uitleg="Begin en einde liggen dichter bij pH 7, dus is er minder verschil te "
        "overbruggen. Daardoor is de omslag moeilijker te zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je het equivalentiepunt bepalen zonder indicator?",
        opties=[
            "met een pH-meter of met een geleidbaarheidsmeting",
            "door het volume van de erlenmeyer af te lezen",
            "door de temperatuur van de oplossing te meten",
            "door het gewicht van de buret te wegen voor en na",
        ],
        antwoord=0,
        uitleg="Met een pH-meter meet je de hele curve punt per punt. De geleidbaarheid "
        "verandert ook, want de ionen in de oplossing wisselen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de titratie van een zwak zuur loopt er een stuk van de curve vlak, want daar werkt een buffer.",
        antwoord=True,
        uitleg="Halverwege zitten het zuur en zijn geconjugeerde base samen in de beker. "
        "Daar is de pH gelijk aan de pKz van dat zuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag de buret vullen tot boven de nulstreep en dan het verschil berekenen.",
        antwoord=False,
        uitleg="Boven de nulstreep is er geen schaal, dus kan je het beginvolume niet "
        "aflezen. Je laat eerst tot op of onder nul lopen.",
    ),
    dict(
        type="invultekst",
        vraag="In welk glaswerk staat de oplossing die je titreert?",
        antwoord=["erlenmeyer", "een erlenmeyer", "de erlenmeyer"],
        uitleg="Haar schuine wanden laten je zwenken zonder te spatten. Het titrans komt "
        "uit de buret erboven.",
    ),
]
