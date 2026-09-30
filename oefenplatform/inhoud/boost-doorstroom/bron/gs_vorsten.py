# -*- coding: utf-8 -*-
"""De vragen voor "Vorsten, opstand en de Verlichting".

Uit de vakfiche: tussen absolute en parlementaire monarchie. Het vorstelijk
absolutisme in Frankrijk, de constitutionele parlementaire monarchie in Engeland
met de Glorious Revolution, en de Nederlanden onder Karel V en Filips II met de
Opstand, de Beeldenstorm, het Plakkaat van Verlatinghe en de Vrede van Münster.
Daarnaast de Verlichting: het ontstaan, de filosofen, de politieke en
wetenschappelijke ideeën, en hoe die ideeën in de Belgische grondwet
terugkomen.

Deel 1 gaat over de vorsten en de Opstand. Deel 2 over de Verlichting.

De fiche vraagt uitdrukkelijk dat een leerling het beeld van Alva in een Spaanse
bron kan vergelijken met het beeld in een bron uit de Habsburgse Nederlanden, en
dat hij de verlichte ideeën in de Belgische grondwet kan benoemen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn kenmerken van het vorstelijk absolutisme?",
        opties=[
            "alle macht ligt bij de koning, die aan niemand verantwoording schuldig is",
            "de koning stelt zijn ministers zelf aan en zet ze zelf af",
            "de standenvergadering wordt niet meer bijeengeroepen",
            "de koning wordt bij elke troonopvolging door het volk verkozen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verkozen worden hoort bij een republiek. De drie andere kenmerken passen precies op Lodewijk XIV.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop steunde de koning zijn absolute macht?",
        opties=[
            "op het droit divin: zijn macht komt rechtstreeks van God",
            "op een volksstemming waarin het hele land zich uitsprak",
            "op een grondwet die zijn bevoegdheden zwart op wit vastlegde",
            "op een contract dat hij met de adel van zijn rijk gesloten had",
        ],
        antwoord=0,
        uitleg="Wie zich tegen de koning verzet, verzet zich dan tegen God zelf. Godsdienst staat hier in dienst van de vorst.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Franse koning noemde men de Zonnekoning?",
        antwoord="Lodewijk XIV",
        uitleg="Hij regeerde tweeënzeventig jaar en bouwde Versailles. De zon in het midden, en alles eromheen dat draait: dat was het beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruikte Lodewijk XIV het hof van Versailles níét?",
        opties=[
            "om de standenvergadering te laten vergaderen",
            "om de adel aan het hof te binden",
            "om zijn macht in ceremonie te tonen",
            "om het bestuur onder zijn oog te houden",
        ],
        antwoord=0,
        uitleg="De Staten-Generaal riep hij juist niet meer samen. De drie andere maken van een paleis een machtsinstrument.",
    ),
    dict(
        type="waarofniet",
        vraag="Het vorstelijk absolutisme werd op lange termijn ondermijnd door oorlogen en geldgebrek.",
        antwoord=True,
        uitleg="Oorlogen en hofhouding kostten enorm veel; de belasting drukte op wie ze het minst kon dragen. Dat ongenoegen loopt tot in 1789 door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een constitutionele parlementaire monarchie?",
        opties=[
            "een koningschap dat aan een grondwet gebonden is, met een parlement dat mee beslist",
            "een koningschap waarin de vorst door geen enkele wet of raad beperkt wordt",
            "een staat zonder koning, waarin een verkozen president het staatshoofd is",
            "een staat die door de Kerk bestuurd wordt, met een geestelijke aan het hoofd",
        ],
        antwoord=0,
        uitleg="De koning blijft, maar hij regeert binnen regels die hij niet zelf kan veranderen. Engeland loopt daarin voorop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de oorzaken van de Glorious Revolution?",
        opties=[
            "de koning wilde zonder het parlement regeren",
            "de koning was katholiek in een overwegend protestants land",
            "het parlement vreesde voor zijn eigen bestaan",
            "Engeland verloor een oorlog tegen Frankrijk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een verloren oorlog was er niet. De drie andere redenen brachten het parlement ertoe Willem III uit de Nederlanden te halen.",
    ),
    dict(
        type="waarofniet",
        vraag="De Glorious Revolution van 1688 verliep zonder grote veldslag in Engeland.",
        antwoord=True,
        uitleg="Jacobus II vluchtte. Vandaar de naam: een omwenteling die als roemrijk gold omdat er nauwelijks bloed vloeide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat legde de Bill of Rights van 1689 vast?",
        opties=[
            "de koning mag geen wetten opheffen of belastingen heffen zonder het parlement",
            "de koning is voortaan de enige wetgever van het land en het parlement adviseert",
            "het parlement wordt afgeschaft en zijn bevoegdheden gaan naar de koning over",
            "de koning wordt voortaan door het volk verkozen voor een bepaalde termijn",
        ],
        antwoord=0,
        uitleg="Daarmee is de macht van de vorst voor het eerst in een tekst begrensd. Engeland en Frankrijk gaan vanaf dan echt uit elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deden Karel V en Filips II in de Nederlanden juist níét?",
        opties=[
            "de steden meer privileges geven",
            "het bestuur centraliseren",
            "nieuwe bisdommen instellen",
            "hard optreden tegen het protestantisme",
        ],
        antwoord=0,
        uitleg="Aan de privileges knabbelden ze net. Dat is een van de oorzaken van de Opstand.",
    ),
    dict(
        type="waarofniet",
        vraag="Centralisatie betekent dat elk gewest zijn eigen bestuur zelf mag blijven regelen.",
        antwoord=False,
        uitleg="Het is net het omgekeerde: alles wordt vanuit één punt geregeld. Voor een stad met een eigen keure voelt dat als diefstal van haar rechten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren oorzaken van de Opstand in de Nederlanden?",
        opties=[
            "de centralisatie tastte de oude privileges aan",
            "de vervolging van protestanten",
            "zware belastingen, zoals de tiende penning",
            "de sluiting van alle havens door Engeland",
        ],
        antwoord=[0, 1, 2],
        uitleg="Engeland sloot geen havens. De drie andere oorzaken brachten adel, steden en gelovigen samen in hetzelfde verzet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de vernieling van beelden in kerken in 1566?",
        antwoord="de Beeldenstorm",
        uitleg="Hij begon in Steenvoorde en trok in enkele weken over de Nederlanden. Voor Filips II was het het bewijs dat hard optreden nodig was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat de hertog van Alva zo verschillend beschreven in een Spaanse en in een Nederlandse bron?",
        opties=[
            "elke auteur schrijft vanuit zijn eigen kant van het conflict",
            "de ene bron is achteraf door een kopiist vervalst en de andere niet",
            "de ene bron is pas eeuwen later geschreven en de andere meteen",
            "de ene auteur heeft hem nooit gekend en schrijft van horen zeggen",
        ],
        antwoord=0,
        uitleg="Voor de ene is hij de man die de orde en het geloof redt, voor de andere de bloedhertog van de Raad van Beroerten. Dat is standplaatsgebondenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee bronnen die elkaar tegenspreken, betekenen dat er zeker één liegt.",
        antwoord=False,
        uitleg="Ze kunnen allebei eerlijk zijn en toch iets anders zien of belangrijk vinden. Juist dat verschil is voor een historicus bruikbaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de akte uit 1581 waarin de gewesten Filips II afzwoeren? (Plakkaat van ...)",
        antwoord="Verlatinghe",
        uitleg="Het redeneert dat een vorst die zijn onderdanen als een tiran behandelt, zijn recht verspeelt. Dat idee komt bij de Verlichting terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lang duurde de oorlog tussen de Nederlanden en Spanje?",
        opties=["tachtig jaar", "dertig jaar", "honderd jaar", "zeven jaar"],
        antwoord=0,
        uitleg="Van 1568 tot 1648, met een bestand van twaalf jaar ertussen. Vandaar de naam Tachtigjarige Oorlog.",
    ),
    dict(
        type="waarofniet",
        vraag="De Vrede van Münster in 1648 erkende de onafhankelijkheid van de Noordelijke Nederlanden.",
        antwoord=True,
        uitleg="De Republiek wordt een erkende staat. De Zuidelijke Nederlanden blijven Spaans, en later Oostenrijks.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg had de scheiding voor de Zuidelijke Nederlanden níét?",
        opties=[
            "het gebied werd een republiek",
            "de Schelde ging dicht",
            "veel kooplui trokken naar het noorden",
            "het gebied bleef katholiek en Spaans",
        ],
        antwoord=0,
        uitleg="Een republiek werd juist het noorden. De drie andere verklaren de bloei van Amsterdam en de terugval van Antwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grote verschil tussen de Franse en de Engelse weg in de 17de eeuw?",
        opties=[
            "in Frankrijk wint de vorst het van het parlement, in Engeland het parlement van de vorst",
            "in de twee landen verdwijnt de koning en komt er een verkozen staatshoofd in de plaats",
            "in de twee landen komt er een geschreven grondwet die de macht van de vorst begrenst",
            "in Frankrijk komt er een republiek en in Engeland blijft alles bij het oude",
        ],
        antwoord=0,
        uitleg="Frankrijk eindigt bij Versailles, Engeland bij de Bill of Rights. Dezelfde eeuw, twee tegengestelde antwoorden op dezelfde vraag.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de Verlichting?",
        opties=[
            "een stroming die het verstand als leidraad neemt voor kennis en samenleving",
            "een godsdienstige opwekkingsbeweging die de Kerk van binnenuit wilde zuiveren",
            "een schilderstijl met veel licht, ontstaan in de werkplaatsen van Amsterdam",
            "een politieke partij uit de 18de eeuw die in het Franse parlement zetelde",
        ],
        antwoord=0,
        uitleg="Het licht in de naam is dat van de rede tegenover de duisternis van vooroordeel en willekeur.",
    ),
    dict(
        type="waarofniet",
        vraag="De Verlichting ontstond vooral in de 18de eeuw, met Frankrijk en Engeland als zwaartepunten.",
        antwoord=True,
        uitleg="Salons, koffiehuizen en de Encyclopédie verspreidden de ideeën. Drukwerk was daarbij even belangrijk als bij de Reformatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke filosoof verdedigde de scheiding der machten?",
        opties=[
            "Charles de Montesquieu",
            "Jean-Jacques Rousseau",
            "Immanuel Kant",
            "John Locke",
        ],
        antwoord=0,
        uitleg="In 'De l'esprit des lois' splitst hij wetgevende, uitvoerende en rechterlijke macht, zodat de ene de andere kan tegenhouden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk idee hoort bij Jean-Jacques Rousseau?",
        opties=[
            "de volkssoevereiniteit: de macht gaat uit van het volk",
            "de scheiding der machten, met drie machten die elkaar in toom houden",
            "durf zelf te denken, en tree uit je eigen onmondigheid",
            "godsdienstige verdraagzaamheid als het hoofdthema van zijn hele werk",
        ],
        antwoord=0,
        uitleg="In 'Du contrat social' sluiten burgers onderling een verdrag. Het gezag is van hen, niet van een vorst bij Gods gratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ideeën horen bij John Locke?",
        opties=[
            "de mens heeft natuurlijke rechten op leven, vrijheid en bezit",
            "een bestuur dat die rechten schendt, mag afgezet worden",
            "kennis komt uit de ervaring",
            "de koning ontleent zijn macht rechtstreeks aan God",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het droit divin verwerpt hij juist. De drie andere ideeën vind je bijna letterlijk terug in de Amerikaanse Onafhankelijkheidsverklaring.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Franse filosoof streed vooral voor godsdienstige verdraagzaamheid en vrije meningsuiting?",
        antwoord="Voltaire",
        uitleg="Hij bestreed onverdraagzaamheid met spot en met pamfletten, en moest daarvoor meer dan eens het land uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke zin vatte Immanuel Kant de Verlichting samen?",
        opties=[
            "durf zelf te denken",
            "ik denk, dus ik ben",
            "de mens is de maat van alle dingen",
            "kennis is macht",
        ],
        antwoord=0,
        uitleg="Sapere aude. Verlichting is voor hem het uittreden uit een onmondigheid waar je zelf schuld aan hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Verlichte denkers wilden de koning altijd afschaffen.",
        antwoord=False,
        uitleg="Velen hoopten juist op een verlicht vorst die van bovenaf hervormde, zoals Jozef II. Pas de revoluties maken er een breuk van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent rechtsgelijkheid?",
        opties=[
            "dezelfde wet geldt voor iedereen, ongeacht stand of geboorte",
            "iedereen verdient evenveel geld, welk werk hij ook doet",
            "iedereen in het land moet dezelfde mening toegedaan zijn",
            "iedereen mag rechter worden, ook zonder een opleiding",
        ],
        antwoord=0,
        uitleg="Dat botst frontaal met de standensamenleving, waar adel en geestelijkheid hun eigen rechtbanken en vrijstellingen hadden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent rechtszekerheid?",
        opties=[
            "je kan vooraf weten wat verboden is en welke straf erop staat",
            "je wint altijd je proces, zolang je de wet gelezen hebt",
            "je hoeft als gewone burger nooit voor een rechter te verschijnen",
            "de rechter beslist volledig naar eigen goeddunken, per geval",
        ],
        antwoord=0,
        uitleg="Willekeur is precies het tegendeel: een brief van de koning die iemand zonder proces in de Bastille deed belanden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de tekst waarin de grondregels en de macht van een staat vastgelegd zijn?",
        antwoord="een grondwet",
        uitleg="Ze staat boven de gewone wetten. Zonder zo'n tekst kan een vorst zijn eigen bevoegdheid altijd weer oprekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het weerstandsrecht?",
        opties=[
            "het recht om je te verzetten tegen een bestuur dat je rechten schendt",
            "het recht om de belasting te weigeren die de vorst je oplegt",
            "het recht om het werk neer te leggen en te gaan staken",
            "het recht om te verhuizen naar een ander gewest of land",
        ],
        antwoord=0,
        uitleg="Locke schreef het uit, maar het Plakkaat van Verlatinghe redeneerde in 1581 al zo. Ideeën hebben vaak een langere voorgeschiedenis dan hun naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen empirisme en rationalisme?",
        opties=[
            "empirisme vertrekt van de waarneming, rationalisme van het redeneren",
            "empirisme vertrekt van het geloof, rationalisme van de traditie",
            "empirisme is ouder dan het rationalisme met duizend jaar",
            "er is geen verschil",
        ],
        antwoord=0,
        uitleg="In de praktijk lopen ze door elkaar: je meet, en je redeneert op wat je meet. Beide verwerpen wel het argument van het gezag alleen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vooruitgangsoptimisme is het geloof dat kennis en rede de samenleving beter kunnen maken.",
        antwoord=True,
        uitleg="Dat geloof draagt de hele 18de eeuw. De 20ste eeuw zal er scherpe vragen bij stellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verlichte ideeën herken je in de Belgische grondwet?",
        opties=[
            "de scheiding der machten",
            "de gelijkheid van alle Belgen voor de wet",
            "de vrijheid van godsdienst en van meningsuiting",
            "de erfelijke voorrechten van de adel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Adellijke voorrechten zijn juist afgeschaft. De grondwet van 1831 gold in haar tijd als een van de meest verlichte van Europa.",
    ),
    dict(
        type="waarofniet",
        vraag="De macht in België gaat volgens de grondwet uit van de natie.",
        antwoord=True,
        uitleg="Dat is de volkssoevereiniteit van Rousseau, in artikel 33. De koning heeft enkel de bevoegdheden die de grondwet hem geeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk bestuursniveau bestaat in België níét?",
        opties=[
            "de provincieraad van Europa",
            "de gemeente",
            "de gemeenschappen en gewesten",
            "het federale niveau",
        ],
        antwoord=0,
        uitleg="Europa beslist wel mee, maar niet met zo'n raad. De andere niveaus samen beslissen alles, van een voetpad tot een handelsverdrag.",
    ),
    dict(
        type="waarofniet",
        vraag="De scheiding der machten betekent dat de regering ook de rechtbanken leidt.",
        antwoord=False,
        uitleg="Net niet. Wetgevende, uitvoerende en rechterlijke macht staan los van elkaar, juist zodat de ene de andere kan controleren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je binnen een democratische rechtsstaat zelf verantwoordelijkheid opnemen?",
        opties=[
            "gaan stemmen en je informeren over wat er beslist wordt",
            "een petitie ondertekenen of naar een inspraakmoment gaan",
            "je aansluiten bij een vereniging of een jeugdraad",
            "alle beslissingen aan de vorst en zijn ministers overlaten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een rechtsstaat leeft van wie meedoet. De drie andere wegen staan voor iedereen open, ook voor wie nog niet mag stemmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noem je de Verlichting een keerpunt in het politieke domein?",
        opties=[
            "de bron van het gezag verschuift van God naar het volk",
            "er komt in Europa voor het eerst een koning aan het hoofd van een staat",
            "er komt in Europa voor het eerst een leger onder één bevelhebber",
            "de steden verdwijnen en iedereen keert terug naar het platteland",
        ],
        antwoord=0,
        uitleg="Wie zegt dat de macht van het volk komt, zegt ook dat ze teruggenomen kan worden. Daar begint de weg naar de revoluties.",
    ),
]
