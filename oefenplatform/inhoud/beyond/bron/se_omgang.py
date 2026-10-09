# -*- coding: utf-8 -*-
"""Respectvol samenleven: communicatie, grenzen en samenwerken.

Het tweede thema uit het blok "ik leef samen met anderen". Waar het eerste
thema de begrippen van diversiteit vastlegt, gaat dit over gedrag: hoe je met
anderen omgaat en waar de grenzen liggen.

De fiche deelt dit op in vier stukken: sociale interactie en communicatie,
grenzen, context en relaties, en samenwerken en verantwoordelijkheid.

Het strengste rijtje van de hele fiche staat hier: de zes kenmerken van
geldige toestemming, met de uitleg die de fiche zelf meegeeft.

    vrijwillig        zonder druk, manipulatie, intimidatie of dwang
    duidelijk         expliciet geuit of ondubbelzinnig kenbaar gemaakt
    geïnformeerd      de persoon begrijpt waarvoor toestemming wordt gegeven
    specifiek         toestemming voor het ene is geen toestemming voor het andere
    actueel           ze geldt voor het huidige moment en de huidige situatie
    bekwaam gegeven   de persoon kan een vrije en bewuste keuze maken

Die zes zijn geen theorie om op te sommen: de fiche vraagt dat je aan de hand
van die kenmerken beoordeelt of er in een gegeven situatie toestemming was.
Daarom staan ze hier vooral in situatievragen, met verzonnen namen zoals de
fiche voorschrijft.

Deel 1 is communicatie en gedrag, met pesten, uitsluiting en racisme.
Deel 2 is grenzen en toestemming, formele en informele context, en samenwerken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer verloopt een sociale interactie respectvol?",
        opties=[
            "als beide personen rekening houden met elkaars grenzen",
            "als beide personen uiteindelijk hetzelfde vinden",
            "als niemand zijn mening hardop zegt",
            "als de sterkste partij beslist hoe het gesprek loopt",
        ],
        antwoord=0,
        uitleg="Respect betekent niet dat je het eens wordt, maar dat je elkaars grenzen erkent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt communicatie constructief?",
        opties=[
            "ze brengt het gesprek en de relatie vooruit",
            "ze geeft altijd gelijk aan wie het eerst sprak",
            "ze vermijdt elke vorm van kritiek",
            "ze eindigt altijd met een duidelijke winnaar",
        ],
        antwoord=0,
        uitleg="Constructief komt van bouwen: na het gesprek staat er iets, ook als je het oneens blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt communicatie destructief?",
        opties=[
            "ze breekt de ander of de relatie af",
            "ze duurt langer dan afgesproken",
            "ze gaat over een gevoelig onderwerp",
            "ze gebeurt schriftelijk in plaats van mondeling",
        ],
        antwoord=0,
        uitleg="Destructief komt van afbreken. Een gevoelig onderwerp aansnijden is dat niet per se.",
    ),
    dict(
        type="meerkeuze",
        vraag="Milan zegt in een discussie: ik begrijp dat je dit anders ziet, maar ik maak me zorgen over het tijdstip. Wat voor communicatie is dat?",
        opties=[
            "constructief, want hij benoemt zijn zorg zonder de ander af te breken",
            "destructief, want hij spreekt de ander tegen",
            "destructief, want hij gebruikt het woord maar",
            "neutraal, want hij geeft geen eigen mening",
        ],
        antwoord=0,
        uitleg="Tegenspreken mag. Het gaat erom hoe je het doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Yara wordt in een groepschat elke dag belachelijk gemaakt om haar stem. Wat is dit?",
        opties=["pestgedrag", "een meningsverschil", "groepsdenken", "een verschil in referentiekader"],
        antwoord=0,
        uitleg="Herhaald, gericht en kwetsend gedrag tegen dezelfde persoon: dat is pesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderscheidt pesten van een eenmalige ruzie?",
        opties=[
            "pesten is herhaald en gericht tegen dezelfde persoon",
            "pesten gebeurt enkel online",
            "pesten gebeurt enkel door een hele groep",
            "pesten laat geen sporen na bij het slachtoffer",
        ],
        antwoord=0,
        uitleg="De herhaling en het machtsverschil maken het pesten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een sportclub laat één speler nooit meedoen aan de groepsgesprekken en activiteiten. Wat is dat?",
        opties=["uitsluiting", "een meningsverschil", "een verschil in belangen", "netiquette"],
        antwoord=0,
        uitleg="Iemand systematisch buiten de groep houden is uitsluiting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen discriminatie en racisme?",
        opties=[
            "racisme is discriminatie op basis van afkomst of huidskleur",
            "discriminatie is strafbaar en racisme niet",
            "racisme gebeurt per ongeluk en discriminatie met opzet",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Discriminatie is het bredere woord; racisme is één vorm ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is volgens de fiche de impact van pesten op het slachtoffer?",
        opties=[
            "ze raakt het welzijn en kan lang nawerken",
            "ze blijft beperkt tot het moment zelf",
            "ze is enkel ernstig als er geweld bij komt",
            "ze verdwijnt zodra het pesten stopt",
        ],
        antwoord=0,
        uitleg="De fiche vraagt juist dat je die impact op de betrokkenen kan verklaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet dat een klasgenoot online wordt uitgelachen. Welke reactie is volgens de fiche het meest helpend?",
        opties=[
            "het slachtoffer steunen en de situatie melden",
            "niets doen, zodat het sneller overwaait",
            "zelf terugschrijven in dezelfde toon",
            "het slachtoffer vragen om minder op te vallen",
        ],
        antwoord=0,
        uitleg="De fiche vraagt te beoordelen welke handelingsopties het meest helpend zijn, en wegkijken is dat niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meningsverschil is volgens de fiche hetzelfde als destructieve communicatie.",
        antwoord=False,
        uitleg="Je kan het grondig oneens zijn en toch respectvol en constructief praten.",
    ),
    dict(
        type="waarofniet",
        vraag="Je gedrag en je keuzes hebben gevolgen voor het welzijn van anderen.",
        antwoord=True,
        uitleg="De fiche vraagt dat je die gevolgen voor jezelf én voor anderen kan beoordelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie bij pesten toekijkt zonder iets te doen, heeft volgens de fiche geen rol in de situatie.",
        antwoord=False,
        uitleg="De fiche vraagt naar handelingsopties, juist omdat omstaanders wel een rol hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="Racisme is een vorm van discriminatie.",
        antwoord=True,
        uitleg="Discriminatie is het bredere begrip, racisme een van de vormen ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke situaties moet je volgens de fiche kunnen analyseren?",
        opties=[
            "pestgedrag",
            "uitsluiting",
            "discriminatie en racisme",
            "schoolvertraging",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie staan letterlijk in de fiche. Over schoolvertraging zegt dit blok niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij een respectvolle en constructieve interactie?",
        opties=[
            "rekening houden met de grenzen van de ander",
            "je eigen standpunt rustig kunnen uitleggen",
            "kunnen luisteren zonder meteen te oordelen",
            "altijd toegeven om ruzie te vermijden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Altijd toegeven is geen respect voor jezelf, en lost het meningsverschil niet op.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je communicatie die het gesprek en de relatie vooruithelpt?",
        antwoord=["constructief", "constructieve"],
        uitleg="Het tegendeel is destructieve communicatie, die afbreekt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je herhaald en gericht kwetsend gedrag tegen dezelfde persoon?",
        antwoord=["pesten", "pestgedrag"],
        uitleg="De fiche gebruikt het woord pestgedrag in het rijtje met uitsluiting, discriminatie en racisme.",
    ),
    dict(
        type="invultekst",
        vraag="Welke vorm van discriminatie gaat over afkomst of huidskleur?",
        antwoord=["racisme", "het racisme"],
        uitleg="Racisme staat in de fiche naast pestgedrag, uitsluiting en discriminatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee leerlingen maken in de les ruzie over een opdracht en praten het daarna uit. Wat is dit?",
        opties=[
            "een meningsverschil dat constructief eindigt",
            "pestgedrag met twee daders",
            "uitsluiting van een van de twee",
            "een geval van racisme",
        ],
        antwoord=0,
        uitleg="Geen herhaling, geen machtsverschil, en het gesprek brengt het vooruit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel kenmerken van geldige toestemming noemt de fiche?",
        opties=["zes", "drie", "vier", "acht"],
        antwoord=0,
        uitleg="Vrijwillig, duidelijk, geïnformeerd, specifiek, actueel en bekwaam gegeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het kenmerk vrijwillig bij toestemming?",
        opties=[
            "zonder druk, manipulatie, intimidatie of dwang",
            "zonder dat iemand anders het te weten komt",
            "zonder dat er iets op papier staat",
            "zonder dat er iets voor betaald wordt",
        ],
        antwoord=0,
        uitleg="Die vier woorden staan letterlijk in de fiche bij vrijwillig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het kenmerk specifiek bij toestemming?",
        opties=[
            "toestemming voor het ene is geen toestemming voor het andere",
            "toestemming moet met heel precieze woorden gegeven worden",
            "toestemming geldt enkel voor één bepaalde persoon",
            "toestemming moet schriftelijk gegeven worden",
        ],
        antwoord=0,
        uitleg="Ja zeggen tegen de ene handeling of situatie betekent niet automatisch ja tegen een andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het kenmerk actueel bij toestemming?",
        opties=[
            "ze geldt voor het huidige moment en de huidige situatie",
            "ze geldt zolang de relatie duurt",
            "ze geldt vanaf het moment dat ze gegeven is",
            "ze geldt enkel als ze dezelfde dag herhaald wordt",
        ],
        antwoord=0,
        uitleg="Toestemming van vorige week is geen toestemming voor vandaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het kenmerk geïnformeerd bij toestemming?",
        opties=[
            "de persoon begrijpt waarvoor ze toestemming geeft",
            "de persoon heeft het aan iemand anders doorgegeven",
            "de persoon heeft erover nagedacht gedurende een dag",
            "de persoon heeft de wet daarover gelezen",
        ],
        antwoord=0,
        uitleg="Zonder te weten waarover het gaat, is een ja geen geldige ja.",
    ),
    dict(
        type="meerkeuze",
        vraag="Lotte zegt ja nadat haar vrienden een halfuur hebben aangedrongen. Welk kenmerk van toestemming ontbreekt?",
        opties=["vrijwillig", "geïnformeerd", "actueel", "specifiek"],
        antwoord=0,
        uitleg="Er was druk, dus de toestemming was niet vrijwillig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand stemde vorige maand in met een foto, maar nu niet meer. Welk kenmerk is hier van belang?",
        opties=["actueel", "bekwaam gegeven", "duidelijk", "vrijwillig"],
        antwoord=0,
        uitleg="Toestemming geldt voor het huidige moment, dus ze kan ingetrokken worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand is zo ziek dat hij niet goed kan overzien wat gevraagd wordt. Welk kenmerk ontbreekt?",
        opties=["bekwaam gegeven", "specifiek", "duidelijk", "actueel"],
        antwoord=0,
        uitleg="Bekwaam gegeven betekent dat de persoon een vrije en bewuste keuze kan maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt niets en blijft stil. Is dat toestemming?",
        opties=[
            "nee, toestemming moet duidelijk geuit of ondubbelzinnig zijn",
            "ja, wie niets zegt, stemt in",
            "ja, zolang de ander het zo begrijpt",
            "dat hangt af van hoelang de stilte duurt",
        ],
        antwoord=0,
        uitleg="Het kenmerk duidelijk vraagt dat de toestemming expliciet of ondubbelzinnig kenbaar wordt gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is groepsdruk?",
        opties=[
            "de invloed van een groep die je tot iets brengt wat je alleen niet zou doen",
            "het aantal mensen dat in een ruimte aanwezig is",
            "de regels die een vereniging aan haar leden oplegt",
            "de verantwoordelijkheid die een groep samen draagt",
        ],
        antwoord=0,
        uitleg="De fiche vraagt situaties rond grenzen, groepsdruk en invloed van anderen te analyseren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een formele context?",
        opties=[
            "een situatie met vaste regels en verwachtingen, zoals een sollicitatie",
            "een situatie waarin je alleen bent",
            "een situatie waarin iedereen elkaar goed kent",
            "een situatie waarin je schriftelijk communiceert",
        ],
        antwoord=0,
        uitleg="Formeel gaat over de regels van de situatie, niet over het middel dat je gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je stuurt een mail naar een mogelijke werkgever. Welke stijl past?",
        opties=[
            "een formele stijl met een correcte aanspreking",
            "dezelfde stijl als in een chat met vrienden",
            "een stijl met zo veel mogelijk emoji",
            "een stijl waarin je meteen je eisen stelt",
        ],
        antwoord=0,
        uitleg="De fiche vraagt te beoordelen welke omgangsvormen in professionele situaties het meest gepast zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Toestemming kan ook achteraf nog ingetrokken worden.",
        antwoord=True,
        uitleg="Het kenmerk actueel betekent dat ze geldt voor nu, en dus niet voor altijd.",
    ),
    dict(
        type="waarofniet",
        vraag="Stilzwijgen geldt volgens de fiche als geldige toestemming.",
        antwoord=False,
        uitleg="Het kenmerk duidelijk vraagt juist iets dat expliciet of ondubbelzinnig geuit wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="In een informele context gelden er helemaal geen omgangsvormen.",
        antwoord=False,
        uitleg="Ze zijn losser, maar er blijven verwachtingen, en respect geldt altijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche vraagt te beoordelen welke aanpak de samenwerking in een situatie het meest bevordert.",
        antwoord=True,
        uitleg="Dat staat zo bij het stuk over samenwerken en verantwoordelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken van geldige toestemming staan in de fiche?",
        opties=["vrijwillig", "geïnformeerd", "bekwaam gegeven", "schriftelijk"],
        antwoord=[0, 1, 2],
        uitleg="Schriftelijk staat er niet. Duidelijk, specifiek en actueel wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat draagt bij aan een effectieve samenwerking?",
        opties=[
            "duidelijke afspraken over wie wat doet",
            "elkaar op de hoogte houden van de voortgang",
            "elkaars sterke kanten gebruiken",
            "beslissingen zo lang mogelijk uitstellen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uitstellen helpt een samenwerking niet vooruit.",
    ),
    dict(
        type="invultekst",
        vraag="Welk kenmerk van toestemming betekent dat ze geldt voor het huidige moment?",
        antwoord=["actueel"],
        uitleg="Daarom kan toestemming van gisteren niet voor vandaag gelden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de invloed van een groep die je tot iets brengt wat je alleen niet zou doen?",
        antwoord=["groepsdruk", "de groepsdruk"],
        uitleg="De fiche noemt groepsdruk samen met grenzen en de invloed van anderen.",
    ),
]
