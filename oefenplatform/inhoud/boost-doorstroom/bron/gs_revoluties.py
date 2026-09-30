# -*- coding: utf-8 -*-
"""De vragen voor "Amerika, Frankrijk en de industriële omwenteling".

Uit de vakfiche: de Amerikaanse Revolutie (oorzaken, aanleiding, gevolgen, de
Onafhankelijkheidsverklaring en de politieke kenmerken van de Amerikaanse
staat), de Franse Revolutie (oorzaken, aanleiding, gevolgen, de samenleving voor
en na, de Verklaring van de Rechten van de Mens en de Burger, de fasen, en de
sporen van het Franse bestuur in de Zuidelijke Nederlanden), en de weg naar een
industriële samenleving met haar technische en organisatorische vernieuwingen en
de aanbod- en vraagfactoren in Groot-Brittannië.

Deel 1 gaat over de twee politieke revoluties. Deel 2 over de industriële.

De fiche vraagt uitdrukkelijk dat een leerling de gemeenschappelijke politieke
oorzaken van beide revoluties kan toelichten, dat hij de culturele sporen van de
napoleontische tijd bij ons herkent, en dat hij kan aantonen dat de industriële
revolutie voor het arbeidsproces zowel evolutie als revolutie betekent.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat waren de oorzaken van de Amerikaanse Revolutie?",
        opties=[
            "belastingen zonder vertegenwoordiging in het Londense parlement",
            "Londen bepaalde met wie de kolonies mochten handelen",
            "verlichte ideeën over vrijheid en natuurlijke rechten",
            "een jarenlange hongersnood in de dertien kolonies zelf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Van een hongersnood was geen sprake. De drie andere oorzaken samen verklaren waarom dertien kolonies zich verenigden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de leuze 'no taxation without representation'?",
        opties=[
            "wie geen vertegenwoordigers in het parlement heeft, mag er ook niet belast worden",
            "belastingen moeten in een vrije samenleving volledig worden afgeschaft",
            "enkel de koning zelf mag belastingen heffen, en nooit een parlement",
            "elke burger bepaalt zelf hoeveel belasting hij dat jaar zal betalen",
        ],
        antwoord=0,
        uitleg="De kolonisten betwistten niet de belasting zelf, maar wie ze mocht opleggen. Dat is een politieke vraag, geen financiële.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar werd de Amerikaanse Onafhankelijkheidsverklaring ondertekend?",
        antwoord="1776",
        uitleg="Op 4 juli, in Philadelphia. Die dag is vandaag nog de nationale feestdag van de Verenigde Staten.",
    ),
    dict(
        type="waarofniet",
        vraag="De Onafhankelijkheidsverklaring steunt op de gedachte dat alle mensen met gelijke rechten geboren worden.",
        antwoord=True,
        uitleg="Leven, vrijheid en het streven naar geluk. Dat de slavernij tegelijk bleef bestaan, maakt de spanning in die tekst meteen zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk kenmerk past níét bij de Amerikaanse staat?",
        opties=[
            "een erfelijke koning als staatshoofd",
            "een republiek met een verkozen president",
            "een federale staat",
            "een strikte scheiding der machten",
        ],
        antwoord=0,
        uitleg="Een koning is er juist niet; dat was precies het punt. De drie andere kenmerken zijn verlichte ideeën in de praktijk gebracht.",
    ),
    dict(
        type="waarofniet",
        vraag="De Amerikaanse grondwet gaf vanaf het begin aan iedereen stemrecht.",
        antwoord=False,
        uitleg="Vrouwen, tot slaaf gemaakte mensen en inheemse volkeren bleven uitgesloten, en in veel staten moest je bezit hebben. Gelijkheid op papier is nog geen gelijkheid in feite.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke oorzaak van de Franse Revolutie wordt hier verzonnen?",
        opties=[
            "Frankrijk was door een buurland bezet",
            "de staatskas was leeg na dure oorlogen",
            "de derde stand betaalde en had niets te zeggen",
            "misoogsten deden de broodprijs stijgen",
        ],
        antwoord=0,
        uitleg="Bezet was Frankrijk niet. De drie andere kwamen in 1788 en 1789 wel samen, en dan volstaat een kleine aanleiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de aanleiding tot de Franse Revolutie?",
        opties=[
            "de koning riep de Staten-Generaal samen om geld, en die liep uit de hand",
            "de koning werd vermoord en liet geen troonopvolger na in het land",
            "een zware aardbeving verwoestte Parijs en maakte duizenden mensen dakloos",
            "Engeland verklaarde Frankrijk de oorlog en viel het land binnen",
        ],
        antwoord=0,
        uitleg="De derde stand eiste stemming per hoofd in plaats van per stand, verklaarde zich tot Nationale Vergadering, en daar begon het.",
    ),
    dict(
        type="invultekst",
        vraag="Welke gevangenis in Parijs werd op 14 juli 1789 bestormd?",
        antwoord="de Bastille",
        uitleg="Er zaten nauwelijks gevangenen. Het gebouw stond vooral voor de willekeur van de koning, en dat maakte het tot een symbool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de Verklaring van de Rechten van de Mens en de Burger van 1789?",
        opties=[
            "mensen worden vrij en gelijk in rechten geboren",
            "de soevereiniteit berust bij de natie",
            "vrijheid van mening en van godsdienst",
            "het behoud van de voorrechten van de adel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De voorrechten werden in de nacht van 4 augustus juist afgeschaft. De drie andere punten zijn verlichte ideeën, woord voor woord.",
    ),
    dict(
        type="waarofniet",
        vraag="De Verklaring van 1789 gaf ook aan vrouwen dezelfde politieke rechten.",
        antwoord=False,
        uitleg="Olympe de Gouges schreef daarom in 1791 een eigen verklaring voor de rechten van de vrouw. Ze werd twee jaar later onthoofd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fase hoort níét in de rij van de Franse Revolutie thuis?",
        opties=[
            "een terugkeer naar het absolutisme van voor 1789",
            "een grondwettelijke monarchie met een verkozen vergadering",
            "een republiek, met de jaren van de Terreur daarin",
            "het Directoire en de opkomst van Napoleon Bonaparte",
        ],
        antwoord=0,
        uitleg="Het absolutisme van voor 1789 kwam nooit meer terug, ook niet onder de latere koningen. De drie andere volgen elkaar op tussen 1789 en 1799.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens de Terreur werden duizenden mensen zonder behoorlijk proces terechtgesteld.",
        antwoord=True,
        uitleg="Een revolutie die vrijheid en rechtszekerheid op haar vaandel schreef, schond ze in die maanden zelf. Robespierre eindigde uiteindelijk onder dezelfde guillotine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grootste verschil tussen de samenleving voor en na de Franse Revolutie?",
        opties=[
            "de standen met hun voorrechten maken plaats voor burgers die gelijk zijn voor de wet",
            "er komt naast de bestaande koning nog een tweede koning bij in het land",
            "de landbouw verdwijnt volledig en iedereen gaat in de nijverheid werken",
            "de adel groeit uit tot de grootste bevolkingsgroep van het hele land",
        ],
        antwoord=0,
        uitleg="Ongelijkheid verdwijnt daarmee niet: rijkdom vervangt geboorte als scheidslijn. Maar de ongelijkheid staat niet langer in de wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de Amerikaanse en de Franse Revolutie politiek gemeen?",
        opties=[
            "allebei beroepen ze zich op verlichte ideeën",
            "allebei verwerpen ze een gezag waarin de bevolking niet vertegenwoordigd is",
            "allebei leggen ze rechten vast in een geschreven tekst",
            "allebei stellen ze op het einde een erfelijke keizer aan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een keizer komt er enkel in Frankrijk, en pas achteraf. De drie andere punten maken van de twee revoluties familie van elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="De Amerikaanse Revolutie had geen invloed op wat er in Frankrijk gebeurde.",
        antwoord=False,
        uitleg="Franse officieren, onder wie Lafayette, vochten mee in Amerika en kwamen terug met de ideeën én met het bewijs dat het kon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk spoor liet het Franse bestuur in de Zuidelijke Nederlanden níét na?",
        opties=[
            "het Nederlands als bestuurstaal",
            "de burgerlijke stand",
            "een wetboek aan de basis van ons burgerlijk recht",
            "het metriek stelsel, met meter en kilogram",
        ],
        antwoord=0,
        uitleg="Het Frans werd juist de bestuurstaal, en dat werkt tot ver in de 19de eeuw na. De drie andere sporen gebruik je vandaag nog elke dag.",
    ),
    dict(
        type="waarofniet",
        vraag="De napoleontische tijd liet bij ons ook op cultureel vlak sporen na die vandaag nog niet uitgewist zijn.",
        antwoord=True,
        uitleg="Kerkelijke goederen werden verkocht, kloosters opgeheven, begraafplaatsen buiten de dorpskern gelegd. Ook je familienaam staat sinds die tijd vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men 1789 een breuk in de geschiedenis?",
        opties=[
            "de bron van het gezag en de grondslag van de samenleving veranderen allebei",
            "er wordt in Europa voor de allereerste keer oorlog gevoerd tussen twee landen",
            "er wordt in Europa voor de allereerste keer belasting geheven op bezit",
            "de steden verdwijnen en de bevolking trekt opnieuw naar het platteland",
        ],
        antwoord=0,
        uitleg="Toch blijft er veel doorlopen: dezelfde dorpen, dezelfde landbouw, dezelfde armoede. Een breuk in het politieke domein is niet meteen een breuk in alle.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar breng je de Verklaring van de Rechten van de Mens onder qua maatschappelijk domein?",
        opties=[
            "het politieke domein",
            "het economische domein",
            "het maritieme domein",
            "het militaire domein",
        ],
        antwoord=0,
        uitleg="Ze gaat over wie het gezag heeft en waar het ophoudt. De gevolgen zijn wel meteen ook sociaal en cultureel.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar begon de industriële revolutie?",
        opties=[
            "in Groot-Brittannië",
            "in het koninkrijk Frankrijk",
            "in de Duitse gebieden",
            "in de Verenigde Staten",
        ],
        antwoord=0,
        uitleg="Vanaf ongeveer 1750. België volgt als eerste op het vasteland, met Wallonië en Gent voorop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vernieuwing hoort níét bij de industriële revolutie van de 18de eeuw?",
        opties=[
            "de verbrandingsmotor in elke fabriek",
            "de stoommachine",
            "machines om te spinnen en te weven",
            "cokes in plaats van houtskool bij het ijzer",
        ],
        antwoord=0,
        uitleg="De verbrandingsmotor komt pas veel later. De drie andere maken de doorbraak in textiel, ijzer en energie.",
    ),
    dict(
        type="invultekst",
        vraag="Welke machine zette warmte om in beweging en dreef de fabrieken aan?",
        antwoord="de stoommachine",
        uitleg="Newcomen bouwde er een om water uit mijnen te pompen; Watt maakte ze veel zuiniger en bruikbaar voor alles.",
    ),
    dict(
        type="waarofniet",
        vraag="Steenkool was de brandstof waarop de industriële revolutie draaide.",
        antwoord=True,
        uitleg="Ze stookte de stoomketels en maakte, als cokes, beter ijzer. Waar kolen lagen, groeiden de fabrieken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn organisatorische vernieuwingen in de industriële revolutie?",
        opties=[
            "het werk wordt opgesplitst in kleine, vaste handelingen",
            "arbeiders werken samen in een fabriek in plaats van thuis",
            "er wordt op vaste uren gewerkt, op het ritme van de machine",
            "elke arbeider maakt een product van begin tot eind",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat laatste is juist wat verdwijnt. De drie andere maken van werken iets heel anders dan het was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom betekende de industriële revolutie voor het arbeidsproces zowel evolutie als revolutie?",
        opties=[
            "de technieken groeiden geleidelijk, maar de manier van werken veranderde ingrijpend",
            "alles veranderde op één dag, zowel de techniek als de manier van werken",
            "er veranderde eigenlijk niets, men deed hetzelfde werk als altijd",
            "enkel de lonen veranderden, het werk zelf bleef precies hetzelfde",
        ],
        antwoord=0,
        uitleg="De ambachtsman die zijn eigen tempo bepaalde, wordt een arbeider die het tempo van de machine volgt. De machines zelf kwamen er wel stap voor stap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een aanbodfactor is iets dat de productie mogelijk maakt, zoals grondstoffen, kapitaal of arbeidskrachten.",
        antwoord=True,
        uitleg="De vraagkant gaat over wie het koopt. Je hebt beide nodig: machines zonder afzet blijven stilstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aanbodfactoren had Groot-Brittannië?",
        opties=[
            "steenkool en ijzererts in eigen bodem",
            "kapitaal uit handel en koloniën",
            "arbeidskrachten die door landbouwvernieuwing vrijkwamen",
            "een verbod op het oprichten van ondernemingen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een verbod was er juist niet; ondernemen was er makkelijker dan elders. De drie andere factoren lagen er toevallig alle drie samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraagfactor hielp de Britse industrie?",
        opties=[
            "een groeiende bevolking thuis en een groot koloniaal afzetgebied",
            "een dalende bevolking, waardoor er minder monden te voeden waren",
            "een verbod op uitvoer, waardoor alles in eigen land verkocht werd",
            "het ontbreken van havens, waardoor men op het binnenland aangewezen was",
        ],
        antwoord=0,
        uitleg="Wie massaal produceert, moet massaal verkopen. Kanalen, wegen en later spoorwegen brachten de waren tot bij de koper.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de omheinde velden die in Engeland de gemene gronden vervingen?",
        antwoord="enclosures",
        uitleg="Ze maakten de landbouw productiever, maar duwden kleine boeren van het land. Velen belandden zo in de fabrieken.",
    ),
    dict(
        type="waarofniet",
        vraag="Het vervoer bleef tijdens de industriële revolutie onveranderd.",
        antwoord=False,
        uitleg="Eerst kanalen en verharde wegen, daarna de spoorweg en het stoomschip. Zonder dat vervoer geraakt de productie nergens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg had de industrialisatie juist níét?",
        opties=[
            "de sociale ongelijkheid verdween",
            "de steden groeiden snel en werden overbevolkt",
            "er ontstond een nieuwe groep fabrieksarbeiders",
            "kinderarbeid was gewoon",
        ],
        antwoord=0,
        uitleg="De ongelijkheid verdween niet, ze kreeg een nieuwe vorm. De drie andere gevolgen tekenen de 19de eeuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een manufactuur en een fabriek?",
        opties=[
            "in een fabriek doen machines het zware werk, in een manufactuur handen",
            "een fabriek is veel kleiner dan een manufactuur en telt minder arbeiders",
            "een manufactuur werkt enkel met kinderen, een fabriek enkel met volwassenen",
            "er is geen enkel verschil, het zijn twee namen voor precies hetzelfde",
        ],
        antwoord=0,
        uitleg="Samen werken op één plaats deed men al in de manufactuur. Nieuw is de aandrijving: eerst water, daarna stoom.",
    ),
    dict(
        type="waarofniet",
        vraag="België kwam pas als een van de laatste landen van West-Europa aan de industrialisatie toe.",
        antwoord=False,
        uitleg="Het was juist een van de eerste op het vasteland: rond Luik, Charleroi en Gent. Cockerill bouwde in Seraing een bedrijf dat zijn eigen machines maakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de industriële revolutie ook een verandering in het sociale domein?",
        opties=[
            "er ontstaan twee nieuwe groepen: fabriekseigenaars en loonarbeiders",
            "de bevolking van Europa krimpt in die eeuw voor het eerst sinds de pest",
            "de steden verdwijnen en de mensen trekken opnieuw naar het platteland",
            "het onderwijs verdwijnt, want alle kinderen werken voortaan in de fabriek",
        ],
        antwoord=0,
        uitleg="Wie de machines bezit en wie ze bedient: die scheidslijn zal de hele 19de en 20ste eeuw de politiek beheersen.",
    ),
    dict(
        type="waarofniet",
        vraag="De industriële revolutie is één gebeurtenis met een vaste begin- en einddatum.",
        antwoord=False,
        uitleg="Het is een proces van meer dan een eeuw, dat per land en per streek op een ander moment begint. Historici kiezen de grenzen zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bron gebruik je om de aanbod- en vraagfactoren in Groot-Brittannië te onderzoeken?",
        opties=[
            "cijfers over steenkoolproductie en bevolkingsgroei",
            "kaarten met kolenvelden, kanalen en spoorlijnen",
            "verslagen van onderzoekscommissies over de arbeidsomstandigheden",
            "een roman uit de 21ste eeuw die in die tijd gesitueerd is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een hedendaagse roman is geen bron over die tijd zelf, hooguit over hoe wij ernaar kijken. De drie andere zijn wel bronnen uit de periode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de landbouwvernieuwing en de fabrieken?",
        opties=[
            "minder handen op het land betekent meer handen voor de fabriek",
            "de landbouw verdween volledig en alle grond kwam braak te liggen",
            "de fabrieken maakten enkel landbouwmachines en verder niets anders",
            "er is geen verband, de twee ontwikkelingen staan volledig los van elkaar",
        ],
        antwoord=0,
        uitleg="Meer opbrengst met minder mensen maakt arbeidskrachten vrij. Diezelfde opbrengst moet ook de groeiende stad voeden.",
    ),
    dict(
        type="waarofniet",
        vraag="De drie revoluties van deze periode raken elk een ander maatschappelijk domein.",
        antwoord=True,
        uitleg="De Amerikaanse en de Franse veranderen het politieke, de industriële het economische en het sociale. Ze werken wel op elkaar in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom spreekt men van een revolutie, ook al duurde de industrialisatie meer dan een eeuw?",
        opties=[
            "omdat de gevolgen zo diep ingrijpen dat de samenleving er een andere van wordt",
            "omdat er in die jaren in heel Europa zwaar gevochten werd om de fabrieken",
            "omdat er in die jaren in Groot-Brittannië een koning werd afgezet",
            "omdat het allemaal bijzonder snel ging, op enkele jaren tijd",
        ],
        antwoord=0,
        uitleg="Het woord slaat hier op de omvang van de verandering, niet op de snelheid. Vergelijk het met de commerciële revolutie.",
    ),
]
